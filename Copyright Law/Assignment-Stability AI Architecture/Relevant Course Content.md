# [0.5] - VAEs & GANs

> **Colab: [exercises](https://colab.research.google.com/github/callummcdougall/arena-pragmatic-interp/blob/main/chapter0_fundamentals/exercises/part5_vaes_and_gans/0.5_VAEs_&_GANs_exercises.ipynb?t=20260301) | [solutions](https://colab.research.google.com/github/callummcdougall/arena-pragmatic-interp/blob/main/chapter0_fundamentals/exercises/part5_vaes_and_gans/0.5_VAEs_&_GANs_solutions.ipynb?t=20260301)**

Please send any problems / bugs on the `#errata` channel in the [Slack group](https://join.slack.com/t/arena-uk/shared_invite/zt-3afdmdhye-Mdb3Sv~ss_V_mEaXEbkABA), and ask any questions on the dedicated channels for this chapter of material.

If you want to change to dark mode, you can do this by clicking the three horizontal lines in the top-right, then navigating to Settings → Theme.

Links to all other chapters: [(0) Fundamentals](https://arena-chapter0-fundamentals.streamlit.app/), [(1) Transformer Interpretability](https://arena-chapter1-transformer-interp.streamlit.app/), [(2) RL](https://arena-chapter2-rl.streamlit.app/).

![](https://raw.githubusercontent.com/info-arena/ARENA_img/main/misc/headers/header-05.png)

# Introduction

Today, we're studying two important classes of generative image models: **Generative Adversarial Networks (GANs)** and **Variational Autoencoders (VAEs)**. Although these generally aren't SOTA any more (thanks in part to the rise of diffusion models), there are some deep conceptual insights which can be gleaned from studying these models (VAEs in particular) which help lay the groundwork for more advanced models.

These exercises will also hopefully bring much of this chapter full-circle:

- We'll cover transposed convolutions, which will serve as a refresher on some of the ideas behind convolutions **(day 2: CNNs & ResNets)**
- We'll be assembling NNet architectures from scratch, like in the ResNets exercises **(day 2: CNNs & ResNets)**
- We'll work with different loss functions, and think intuitively about what it means to optimize them **(day 3: Optimization & Hyperparameters)**
- We'll be working with `wandb`, and will learn how to log outputs produced by our models **(day 3: Optimization & Hyperparameters)**
- We'll have to think carefully about how gradient propagation works between different parts of our model **(day 4: Backpropagation)**

Note, many of today's exercises (especially those involving building models & writing forward pass functions) don't have as rigorous unit tests as previous days of content. Part of this is because the design spec for these models is less strict (we're not copying over weights from a pretrained model like last time, all that matters is that our model actually trains correctly, and so small changes to the solution architecture can sometimes be allowed). However, another part is that we're trying to move participants away from being too reliant on unit tests, and towards being able to independently reason through exercises or replications given just a description of the task or a paper implementation to follow. This is an invaluable skill to develop for any aspiring ML practitioner!

For a lecture on the material today, which provides some high-level understanding before you dive into the material, watch the video below:

## Content & Learning Objectives

### 1️⃣ Autoencoders & VAEs

Autoencoders are a relatively simple architecture, at least compared to GANs: you learn a compressed representation of your data (mainly using linear layers and convolutions), then reconstruct it back into an image (with linear layers and transposed convolutions).

Although autoencoders can learn some interesting low-dimensional representations, they are less good for generating images because their latent spaces aren't generally meaningful. This leads to VAEs, which solve this problem by having their encoders map to a distribution over latent vectors, rather than a single latent vector. This incentivises the latent space to be more meaningful, and we can more easily generate images from sample vectors in this space.

We start with some reading material on autoencoders and transposed convolutions (which are often used in parallel with convolutions, to take a latent space and map it back into a full-size image). Then, we actually implement and train VAEs to generate MNIST images, as well as a do a bit of exploring our our autoencoders' latent spaces.

> ##### Learning Objectives
> 
> - Learn about the transposed convolution operation
> - Understand the basic architecture of autoencoders and VAEs
> - Learn about the reparameterization trick for VAEs
> - Implement your own autoencoder
> - Implement your own VAE, and use it to generate realistic MNIST images
> - (optional) Dive deeper into the mathematical underpinnings of VAEs, and learn about the ELBO loss function

### 2️⃣ GANs

Relative to autoencoders, GANs have a few more moving pieces in their architecture. They're best thought of as two separate networks (the generator and the discriminator) which are learning different goals simultaneously. The goal of the generator is to create images which fool the discriminator, and the goal of the discriminator is to distinguish between real and fake images. The ideal equilibrium point of training is when the generator produces perfect images and the discriminator can't tell the difference between real and fake - however, that's much simpler said than done! GANs are notoriously difficult to train, and we'll have to engage with some of these difficulties during our exercises.

By the end of these exercises, you should have built and trained your own GANs, to generate celebrity pictures. By the time you're done, you'll hopefully have produced output like this (below), and you'll have everything you need to set up a competitor to Midjourney (plus or minus a few other foundational ML papers and an investment of a few hundred million dollars).

![](https://raw.githubusercontent.com/info-arena/ARENA_img/main/misc/gan-last-output.png)

> ##### Learning Objectives
> 
> - Understand the loss function used in GANs, and why it can be expected to result in the generator producing realistic outputs.
> - Implement the DCGAN architecture from the paper, with relatively minimal guidance.
> - Learn how to identify and fix bugs in your GAN architecture, to improve convergence properties.

### 3️⃣ Bonus - Transposed Convolutions

In this section, you'll implement the transposed convolution operation manually. This is similar to a regular convolution, but designed for upsampling rather than downsampling (i.e. producing an image from a latent vector rather producing output from an image). These are very important in many generative algorithms. Once you implement this, you'll be able to build your own GANs and VAEs from scratch, without using any pre-built layers.

_Note - the bonus section from the CNNs day is a prerequisite for these bonus exercises. If you haven't completed that section, you'll need to do so before attempting these._

> ##### Learning Objectives
> 
> - Learn about & implement the transposed convolution operation.
> - Implement GANs and/or VAEs entirely from scratch.

## Setup code

`import os import sys from dataclasses import dataclass, field from pathlib import Path from typing import Literal  import einops import torch as t import torchinfo import wandb from datasets import load_dataset from einops.layers.torch import Rearrange from jaxtyping import Float from torch import Tensor, nn from torch.utils.data import DataLoader, Dataset, Subset from torchvision import datasets, transforms from tqdm import tqdm  # Make sure exercises are in the path chapter = "chapter0_fundamentals" section = "part5_vaes_and_gans" root_dir = next(p for p in Path.cwd().parents if (p / chapter).exists()) exercises_dir = root_dir / chapter / "exercises" section_dir = exercises_dir / section if str(exercises_dir) not in sys.path:     sys.path.append(str(exercises_dir))  MAIN = __name__ == "__main__"  import part5_vaes_and_gans.tests as tests import part5_vaes_and_gans.utils as utils from plotly_utils import imshow  device = t.device("mps" if t.backends.mps.is_available() else "cuda" if t.cuda.is_available() else "cpu")`