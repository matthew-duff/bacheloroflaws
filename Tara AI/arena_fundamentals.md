# Context

This document contains the source code for the relevant Markdown files in this set of exercises. The exercises are part of the ARENA (Alignment Research Engineer Accelerator) course, which is designed to provide a hands-on introduction to AI alignment research topics (e.g. LLM interpretability, reinforcement learning, evaluations) as well as fundamentals of machine learning.

The file structure is as follows:

```
chapter0_fundamentals/
└── instructions/
    └── pages/
        ├── 00_[0.0]_Prerequisites.md
        ├── 01_[0.1]_Ray_Tracing.md
        ├── 02_[0.2]_CNNs_&_ResNets.md
        ├── 03_[0.3]_Optimization.md
        ├── 04_[0.4]_Backprop.md
        └── 05_[0.5]_VAEs_&_GANs.md
```

---

## chapter0_fundamentals/instructions/pages/00_[0.0]_Prerequisites.md

```markdown
# [0.0] - Prerequisites


> **Colab: [exercises](https://colab.research.google.com/github/callummcdougall/arena-pragmatic-interp/blob/main/chapter0_fundamentals/exercises/part0_prereqs/0.0_Prerequisites_exercises.ipynb?t=20260303) | [solutions](https://colab.research.google.com/github/callummcdougall/arena-pragmatic-interp/blob/main/chapter0_fundamentals/exercises/part0_prereqs/0.0_Prerequisites_solutions.ipynb?t=20260303)**

Please send any problems / bugs on the `#errata` channel in the [Slack group](https://join.slack.com/t/arena-uk/shared_invite/zt-3afdmdhye-Mdb3Sv~ss_V_mEaXEbkABA), and ask any questions on the dedicated channels for this chapter of material.

If you want to change to dark mode, you can do this by clicking the three horizontal lines in the top-right, then navigating to Settings → Theme.

Links to all other chapters: [(0) Fundamentals](https://arena-chapter0-fundamentals.streamlit.app/), [(1) Transformer Interpretability](https://arena-chapter1-transformer-interp.streamlit.app/), [(2) RL](https://arena-chapter2-rl.streamlit.app/).

<img src="https://raw.githubusercontent.com/info-arena/ARENA_img/main/misc/headers/header-00.png" width="350">


# Introduction


This page contains important prerequisites for the rest of the material in this chapter. The first page **Core Concepts / Knowledge** is a long list of important concepts and libraries that you should be familiar with before starting the rest of the material. The second page **Einops, Einsum & Tensor Manipulation** provides some coding exercises to help you get familiar with the `einops` and `einsum` libraries, as well as some exercises on indexing and other aspects of tensor manipulation. We anticipate adding more exercises here in the future, in the style of the second page.

See the homepage for more instructions on how to set up your environment, and install all the dependencies you need to run the exercises.


## Content & Learning Objectives

### 1️⃣ Core Concepts / Knowledge

This section doesn't have exercises; it goes through a list of important concepts with associated reading material and questions to check your understanding. We cover all the core material that you'll need for the rest of the course such as neural networks, linear algebra, probability, and calculus.

> ##### Learning Objectives
>
> - Understand the structure and function of neural networks
> - Learn essential linear algebra concepts like matrix operations and transformations
> - Understand core principles of probability and statistics, including expected value and variance
> - Learn how calculus concepts (particularly differentiation) are applied in optimization tasks
> - Cover some foundational information theory concepts, such as entropy and KL divergence
> - Enhance Python programming skills, focusing on NumPy and PyTorch basics

### 2️⃣ Einops, Einsum & Tensor Manipulation

These sections will introduce you to a third party library which you'll find very useful for the rest of this course, and will also require you to engage with various tensor operations (something else that will come up repeatedly during this course). 

> ##### Learning Objectives
>
> - Understand the basics of Einstein summation convention
> - Learn how to use `einops` to perform basic tensor rearrangement, and `einsum` to to perform standard linear algebra operations on tensors




=== NEW CHAPTER ===


# 1️⃣ Core Concepts / Knowledge



> ##### Learning Objectives
>
> - Understand the structure and function of neural networks
> - Learn essential linear algebra concepts like matrix operations and transformations
> - Understand core principles of probability and statistics, including expected value and variance
> - Learn how calculus concepts (particularly differentiation) are applied in optimization tasks
> - Cover some foundational information theory concepts, such as entropy and KL divergence
> - Enhance Python programming skills, focusing on NumPy and PyTorch basics

This page contains a list of all prerequisites we think will be helpful to learn before studying the ARENA program material. You can return to this page while you study. None of it is compulsory and some resources are likely to be much more helpful than others. We denote very high and high-priority resources with a double and single asterisk respectively, so if you have limited time then prioritise these. It is strongly recommended to at least read over everything with a double asterisk. Also, you should try and prioritise areas you think you might be weaker in than others (for instance, if you have a strong SWE background but less maths experience then you might want to spend more time on the maths sections). You can also return to this document throughout the programme, if there are any areas you want to brush up on.

The content is partially inspired by a similar doc handed out by Redwood to participants before the start of MLAB, as well as by pre-prerequisite material provided by Jacob Hilton on his [GitHub page](https://github.com/jacobhilton/deep_learning_curriculum).

> Throughout this document, there are some questions thrown in (denoted with boxes like these). It's not essential to answer all of these questions, but you should be able to answer most (or at least know how you might go about answering them).

If you are reading this, and know of any good material for these topics which we've missed out, please let us know and we might be able to add it in!


## Maths

### Neural Networks**

We won't assume any deep knowledge of neural networks or machine learning before the programme starts, but it's useful to have an idea of the basis so that the first week doesn't have quite as steep a learning curve. The best introductory resources here are 3B1B's videos on neural networks:

* [But what is a neural network? | Chapter 1, Deep learning](https://www.youtube.com/watch?v=aircAruvnKk)
* [Gradient descent, how neural networks learn | Chapter 2, Deep learning](https://www.youtube.com/watch?v=IHZwWFHWa-w)
* [What is backpropagation really doing? | Chapter 3, Deep learning](https://www.youtube.com/watch?v=Ilg3gGewQ5U)

You should prioritise the first two videos in this sequence.

<blockquote>

**What makes neural networks more powerful than basic statistical methods like linear regression?**

<details>
<summary>Answer</summary>

Some possible answers / points to consider:

* Neural networks exploit **nonlinearity**, which allows them to express a much wider set of possible functions, whereas linear regression is relatively limited.
* Neural networks are learned using gradient descent, meaning their power isn't upper-bounded by the algorithms which programmers or mathematicians can feasibly design by hand.

</details>

</blockquote>
&nbsp;
<blockquote>

**What are the advantages of ReLU activations over sigmoids?**

<details>
<summary>Answer</summary>

Some possible answers / points to consider:

* ReLU more effectively avoids the **vanishing gradient problem**, which is common in sigmoids.
* ReLU is more **computationally efficient** to evaluate than sigmoid.

However, an important point about ReLU and much of ML in general - the better empirical results often come before the theoretical justifications! A lot of ML is built on the philosophy of "experiment until you find something that works, *then* figure out why it works."

</details>

</blockquote>


### Linear Algebra**

Linear algebra lies at the core of a lot of machine learning.

<img src = "https://lh3.googleusercontent.com/lc5-ykchkkSylhM77XrLuCzfthg8bEtdUTV5EUcArilVKPlh9NZQDWkVnp55s35HftZAWdmyVmh3h5g83HtkOscn1g7x4wS5JO8s4mujPV8N2RbBqoCKiY0K_lVRJgVj7zuSyqPV4SIkbsjaWUQkqJY" width="360">

Here is a list of topics you should be comfortable with:

*   Linear transformations - what they are, and why they are important
    *   See [this](https://www.youtube.com/watch?v=kYB8IZa5AuE) video from 3B1B
*   How [matrix multiplication works](http://mlwiki.org/index.php/Matrix-Matrix_Multiplication)
*   Basic matrix properties: rank, trace, determinant, transpose
*   Bases, and basis transformations

Some other non-essential topics that we also weakly recommend:

*   [Singular value decomposition](https://www.lesswrong.com/posts/iupCxk3ddiJBAJkts/six-and-a-half-intuitions-for-svd)
*   Eigenvalues and eigenvectors
*   Different types of matrix, and their significance (e.g. symmetric, orthogonal, identity, rotation matrices)

[This video series](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab) by 3B1B provides a good overview of these core topics (although you can probably skip it if you already have a reasonably strong mathematical background).

If you have a lot more time, [Linear Algebra Done Right](https://link.springer.com/book/10.1007/978-3-319-11080-6) is the canonical textbook for covering this topic (although it will probably cover much more than you need to know). Alternatively, Neel Nanda has two [YouTube](https://www.youtube.com/watch?v=GkPhwnvRe-8) [videos](https://www.youtube.com/watch?v=0EB23unfLSU) covering linear algebra extensively.

<blockquote>

**What is the problem in trying to create a neural network using only linear transformations?**

<details>
<summary>Answer</summary>

The composition of linear transformations is also linear, so if you only use linear transformations then you can only create linear functions. This is a problem because many functions we want to learn are not linear.

Composing linear and nonlinear transformations however, we can learn basically anything!

</details>

</blockquote>
&nbsp;
<blockquote>

**Matrices $A$ and $B$ have shapes $(n, m)$ and $(m, l)$. What is the maximum possible rank of the matrix $AB$?**

<details>
<summary>Answer</summary>

The rank of $AB$ is upper-bounded by the minimum of the ranks of $A$ and $B$, and the rank of a matrix is upper-bounded by the minimum of its row number and column number (since matrix rank equals the dimensionality of its column span, and also equals the dimensionality of its row span). So $\text{rank}(AB) \leq \min(\text{rank}(A), \text{rank}(B)) \leq \min(n, m, l)$.

Note - in **transformer language models**, we often have cases where $m \ll n, l$, so we have a large, low-rank matrix $AB$. We use tools like singular value decomposition to understand these matrices (e.g. see [this post](https://www.lesswrong.com/posts/mkbGjzxD8d8XqKHzA/the-singular-value-decompositions-of-transformer-weight)), since SVD is a common tool for large low-rank matrices.

</details>

</blockquote>


### Probability & Statistics**

It's essential to understand the rules of probability, expected value and standard deviation, and helpful to understand independence and the normal distribution.

[This link](https://medium.com/jun94-devpblog/prob-stats-3-expected-value-variance-and-standard-deviation-bce9303d8da8) covers some of the essentials.


<blockquote>

**What is the expected value and variance of the sum of two independent normally distributed random variables $X_1 \sim N(\mu_1, \sigma_1^2)$ and $X_2 \sim N(\mu_2, \sigma_2^2)$? Are either of these different if they're correlated? (We don't necessarily expect you to be able to derive this kind of result.)**

<details>
<summary>Answer</summary>

For indepdenent variables, the expected value and variances are both additive, in other words $\mu_1 + \mu_2$ and $\sigma_1^2 + \sigma_2^2$ respectively.

If the variables are correlated, the mean is the same, but the variance will be different: larger if they're correlated, smaller if they're anticorrelated. For some intuition: if they're perfectly correlated then you're basically just doubling a single value so you'll quadruple the variance, whereas if they're perfectly anticorrelated then the sum is always zero, so variance is zero.

</details>

</blockquote>


### Calculus**

It's essential to understand differentiation and partial differentiation, and helpful to understand the basics of vector calculus including the chain rule and Taylor series.

Again, 3Blue1Brown has a good [video series](https://www.3blue1brown.com/topics/calculus) on this.

<blockquote>

**What is the derivative of quadratic loss $L(x, y) = \frac{1}{2}(x-y)^2$ wrt the input $x$ (assuming all variables are scalars, not vectors)? How about for cross entropy loss $L(x, y) = -(y\log{x} + (1-y)\log{(1-x)})$, assuming that $x \in (0, 1)$ and $y$ is a binary classification label with value either zero or one? What will be the qualitative behaviour of performing gradient descent on $x$ with these loss functions?**

<details>
<summary>Answer</summary>

**MSE loss**

The derivative of $L$ wrt $x$ is $x-y$. Qualitatively, this means $x$ will be increased if $x < y$, and decreased if $x > y$, with the size of the increase / decrease proportional to the difference between them.

Qualitatively, this loss function will push $x_n$ downwards if $x_n > y_n$ (with the size of the gradient proportional to the difference between them).

**BCE loss**

The derivative of $L$ wrt $x$ is $-\frac{y}{x} + \frac{1-y}{1-x}$, which equals $-\frac{1}{x}$ when $y=1$ and $\frac{1}{1-x}$ when $y=0$. Qualitatively, this means that $x$ will be increased if $y=1$, and decreased if $y=0$, with the size of the increase / decrease getting unboundedly large when $x$ is close to $1-y$ (i.e. far from the correct value).

Note - in this case, $x$ is the probability output by our model, which is probably the result of applying a sigmoid or softmax function to the model's **logit output**. So the gradient of $L$ wrt $x$ being unbounded doesn't mean the gradient on the model's weights will be unbounded.

</details>

</blockquote>


### Information theory

It's helpful to understand information, entropy and KL divergence. These play key roles in interpreting loss functions.

[Elements of Information Theory](http://staff.ustc.edu.cn/~cgong821/Wiley.Interscience.Elements.of.Information.Theory.Jul.2006.eBook-DDU.pdf) by Thomas M. Cover is the textbook recommended by Jacob Hilton. It will probably cover more than you need to know, and this need not be prioritised over other items on the list.

For an overview of Kullback Leibler divergence (an important concept in information theory and machine learning), see [Six (and a half) intuitions for KL divergence](https://www.lesswrong.com/posts/no5jDTut5Byjqb4j5/six-and-a-half-intuitions-for-kl-divergence). Note that this probably won't make sense if you don't already have a solid grasp of what entropy is.

<blockquote>

**Suppose $P$ is the probability distribution of which word comes next in natural language, and $Q$ is a language model's estimated probability distribution. What will the cross entropy $H(P, Q)$ be if the model is guessing words uniformly? What will the cross entropy be if the model can predict words with the exact right frequency?**

<details>
<summary>Answer</summary>

If the model is guessing uniformly, then:

$$
H(P, Q) = -\sum_x P(x) \log Q(x) = -\sum_x P(x) \log \frac{1}{|V|} = \log |V|
$$

where $V$ is the vocabulary set, and $|V|$ is the number of words in the vocabulary.

If the model is guessing with the exact right frequency, then:

$$
H(P, Q) = -\sum_x P(x) \log Q(x) = -\sum_x P(x) \log P(x) = H(P)
$$

in other words, cross entropy just reduces to the entropy of natural language.
</details>

</blockquote>


## Programming

### Python**

It's important to be strong in Python, because this is the language we'll be using during the programme. As a rough indication, we expect you to be comfortable with at least 80-90% of the material [**here**](https://book.pythontips.com/en/latest/), up to section **"21. for/else"**. For a more thorough treatment of Python's core functionality, see [**here**](https://docs.python.org/3/tutorial/).


### Libraries

The following libraries would be useful to know to at least a basic level, before the course starts.

#### [NumPy](https://numpy.org/)**

Being familiar with NumPy is a staple for working with high-performance Python. Additionally, the syntax for working with NumPy arrays is very similar to how you work with PyTorch tensors (often there are only minor differences, e.g. Torch tends to use the keyword dim where NumPy uses axis). Working through [these 100 basic NumPy exercises](https://github.com/rougier/numpy-100/blob/master/100_Numpy_exercises.ipynb) would be a good idea, or if you're comfortable with NumPy already then you could try doing them in PyTorch (see below).

#### [PyTorch](https://pytorch.org/)**

We will be starting chapter 0 of the programme with some structured exercises designed to get everyone familiar with working in PyTorch. However, the more comfortable you are with PyTorch going in, the easier you'll probably find this. PyTorch has several useful tutorials, and to get comfortable working with tensors you might want to implement the 100 basic NumPy exercises linked to above, using PyTorch instead. Another option would be this [Learn the Basics](https://pytorch.org/tutorials/beginner/basics/intro.html) tutorial. You can skip this if you can clearly explain:

> * **At a high level, what is a `torch.Tensor`?**
> * **What is a `nn.Parameter`, and `nn.Module`?**
> * **When you call `.backward()`, where are your gradients stored?**
> * **What is a loss function? In general, what does it take for arguments, and what does it return?**
> * **What does an optimization algorithm do?**
> * **What is a hyperparameter, and how does it differ from a regular parameter?**
> * **What are some examples of hyperparameters?**

#### [Einops](https://einops.rocks/1-einops-basics) and [Einsum](https://einops.rocks/api/einsum/)*

These are great libraries to get comfortable with, when manipulating tensors. If you're comfortable using them, then you can say goodbye to awkward NumPy/PyTorch methods like transpose, permute and squeeze! We'll have a few einops and einsum exercises on the second day of the fundamentals chapter, but the more comfortable you are with these libraries the faster you'll be.

For einops, you can read through the examples up to "Fancy examples in random order". It's worth trying to play around with these in your own Jupyter notebook, to get more comfortable with them.

For einsum, [this page](https://rockt.github.io/2018/04/30/einsum) provides a basic intro to einstein summation convention, and shows some example tensor implementations. Note that we'll be using the einsum function from the einops library, which allows you to refer to dimensions by name rather than by a single letter.

#### [Typing](https://docs.python.org/3/library/typing.html)*

Type-checking Python functions that you write is a great way to catch bugs, and keep your code clear and readable. Python isn't a strongly-typed language so you won't get errors from using incorrect type specifications unless you use a library like MyPy. However, if you're using VSCode then you can pair this library with a really useful automatic type checker (see next section).

#### [Plotly](https://plotly.com/python)

Plotly is an interactive graphing library which is great for presenting results and investigating data. If you're already very familiar with a different Python plotting library (e.g. matplotlib) then I wouldn't recommend re-learning Plotly, but if you aren't already very familiar with matplotlib or you're open to learning Plotly, I'd strongly recommend giving it a try!

#### [Streamlit](https://share.streamlit.io)

Streamlit is a cool library for building and sharing data-based applications. It integrates very nicely with Plotly (see above), can be hosted on your personal GitHub, and is very intuitive & easy to learn relative to other libraries with similar features (e.g. Dash). This is not compulsory, but if you like the look of Streamlit then you might want to think about using it as a way to submit (or even make public) your end-of-week or capstone projects. See [this page](https://copy-suppression.streamlit.app/) I (Callum) made for presenting the results from the Copy Suppression paper I worked on during SERI MATS, as an example of what Streamlit can do.


## Software Engineering

### Basic coding skills**

If you've been accepted into this programme, then you probably already have this box ticked! However, polishing this area can't hurt. LeetCode is a good place to keep basic coding skills sharp, in particular practising the planning and implementation of functions in the medium-hard sections of LeetCode might be helpful. Practising problems on [Project Euler](https://projecteuler.net/) is another idea.


### VSCode**

Although many of you might already be familiar with Jupyter Notebooks, we recommend working through structured exercises using VSCode. This is a powerful text editor which provides more features than Jupyter Notebooks. Some features it has are:

* **Shortcuts**  
    These are much more powerful than anything offered in Jupyter Notebooks. Below is a table of some particularly useful ones (see [this link](https://www.geeksforgeeks.org/visual-studio-code-shortcuts-for-windows-and-mac/) for more detail on how each of them works).
    |       Commands       |                   Windows/Linux                   |                         MAC                         |
    |:--------------------:|:-------------------------------------------------:|:---------------------------------------------------:|
    |      Delete Line     |                  Ctrl + Shift + K                 |                   Cmd + Shift + K                   |
    | Copy Line Up or Down | Shift + Alt + Up arrow or Shift +Alt + Down arrow | Opt + Shift + Up arrow or  Opt + Shift + Down arrow |
    |      Global Find     |                  Ctrl + Shift + F                 |                   Cmd + Shift + F                   |
    |       Copilot*       |             Ctrl + i / Ctrl + Shift + i           |              Cmd + i / Cmd + Shift + i              |
    | Toggle Block Comment |                  Ctrl + Shift + /                 |                   Cmd + Shift + /                   |
    |    Command Palette   |                  Ctrl + Shift + P                 |                   Cmd + Shift + P                   |
    |  Toggle Line Comment |                      Ctrl + /                     |                       Cmd + /                       |
    |  Trigger Suggestion  |                    Ctrl + Space                   |                     Cmd + Space                     |
    |    Toggle Sidebar    |                      Ctrl + B                     |                       Cmd + B                       |
    |  Multi Select Cursor |                      Ctrl + D                     |                       Cmd + D                       |
    |      Quick Open      |                      Ctrl + P                     |                       Cmd + P                       |
<br>

* **Type checking**      
    We discussed the typing module in a section above. This is particularly powerful when used alongside VSCode's type checker extension. You can activate typing by going to the `settings.json` file in VSCode, and adding this line:  
    
    ```json
    {
        "python.analysis.typeCheckingMode": "basic"
    }
    ```

    You can open the `settings.json` file by first opening VSCode's Command Palette (see the shortcuts above), then finding the option Preferences: Open User Settings (JSON). We won't be using type checking like this in the course, because it can be a bit too strict sometimes, but it's a useful thing to know about.

* **Notebook functionality**  
Although VSCode does provide an extension which acts just like a Jupyter Notebook, it actually has a much more useful feature. Python files can also be made to act like notebooks, by adding the line #%% which act as cell dividers. In this way, you can separate chunks of code and run them individually (and see their output in a new window). See [this page](https://code.visualstudio.com/docs/python/jupyter-support-py) for a further explanation.  
  
* **Debugger**  
The VSCode debugger is a great tool, and can be much more powerful and efficient than the standard practice of adding lines to print information about your output! You can set breakpoints in your code, and closely examine the local variables which are stored at that point in the program. More information can be found on [this page](https://lightrun.com/debugging/debug-python-in-vscode/).  
  
* **Testing**  
VSCode provides ways to easily keep track of and run tests which are written using the pytest or unittest libraries. We'll have a look at the former during the course.  
  
* **Remote machines**  
VSCode offers easy ways to execute code on remote machines over SSH.  
  
* **Copilot**  
GitHub Copilot uses the OpenAI Codex to suggest code and entire functions in real-time, right from your editor. We will be encouraging (although not requiring) use of copilot during the program. It can't do everything, but it's very helpful in abstracting away the annoying low-level details and allowing you to focus on the higher-level concepts and structures.  
  
* **Local imports**  
If you're getting squiggly yellow lines under local imports (or local imports aren't working), add this to the workspace JSON file (you can access it by searching "workspace JSON" into the command palette):

    ```json
    {
        "python.analysis.extraPaths": [
            "extrapath"
        ],
        "python.analysis.include": [
            "extrapath"
        ]
    }
    ```
    where `extrapath` is the path you want to add (e.g. `./chapter0_fundamentals/exercises`, if you're running imports like `import part1_raytracing.solutions as solutions`).


### Jupyter Notebook / Colab**

Despite the overall awesomeness of VSCode, Jupyter Notebooks still have some advantages over VSCode, primarily in exploration and visualisation. Several of the advantages listed in the previous section also apply to .ipynb files created and edited in VSCode; the main reason we're not encouraging this for the ARENA in-person program is because we want participants to be able to write code that they can import from previous days (and because using .py files can help encourage better coding practices, rather than just creating a huge number of cells and dropping them under different headings, losing track of what code is where!).

Colab has a similar structure to Jupyter Notebooks, but it provides several additional features, most importantly GPU access. For anyone following this material virtually, we unfortunately won't be able to provide compute, so (assuming you don't have any way of accessing better compute yourselves e.g. via Lambda Labs) Colab might be the best option for you.


### Git*

Git is a piece of version control software, designed for tracking and managing changes in a set of files. It can be very powerful, but also a bit of a headache to use. 

If you're following this course from the [repo](https://github.com/callummcdougall/ARENA_3.0), you'll need to be comfortable using Git to push and pull files. We also love to see participants contributing to open-source libraries during the program or capstone projects (e.g. TransformerLens or nnsight) as well as using GitHub for collaboration during their capstone projects. These will also require comfort working with Git.

![](https://lh3.googleusercontent.com/jpF1jPI7VGb9ssE-Lzn58nB_d4CQlZItqxhFFU_ZLTL3bv_x_82WVmgyIHQRDyemS7Ne5zpj4-rGVRkpACfR_u7Cw8DTGrMr8H_Sm7w74k03gfcJ2nkAwyk2CElLhMonZ6nhQiirM43DP40BIw1Id0k)

If you already have a strong SWE background then you might not need to spend as much time on this section. Otherwise, we recommend the [Learn Git Branching](https://learngitbranching.js.org/) tutorial series, for an intuitive and interactive set of exercises on Git. A few other resources which have been recommended (which will probably have a lot of overlap):

* [An Intro to Git and GitHub for Beginners](https://product.hubspot.com/blog/git-and-github-tutorial-for-beginners)
* [Git Immersion](https://gitimmersion.com/index.html)
* [Git cheat sheet](https://www.atlassian.com/git/tutorials/atlassian-git-cheatsheet)

Ideally, you should feel comfortable with the following:

* Cloning a repository
* Creating and switching between branches
* Staging and committing changes
* Pushing branches


### Conda*

Virtual environments are a common way to manage dependencies when working across multiple different projects and are standard practice in all professional development contexts. During ARENA, we expect that participants will be working inside likely one, but possibly more environments. 

If you haven't used them already, please ensure that you have conda installed and know how to activate it. See: [Getting started with conda](https://conda.io/projects/conda/en/latest/user-guide/getting-started.html).


### Unix

This won't matter a huge amount for this course (at least for the minimal versions of it), but it's an important part of your development as an engineer. [UC Berkeley's UNIX Tutorial](https://people.ischool.berkeley.edu/~kevin/unix-tutorial/toc.html) provides a comprehensive introduction (up to & including section 4 should suffice for most things you might be doing during this course). [Surrey University's UNIX Tutorial](https://users.cs.duke.edu/~alvy/courses/unixtut/) is also a good resource - up to tutorial 2 should be sufficient.

Also, you can use the instructions on [this page](https://cs50.readthedocs.io/terminal/) to set up a UNIX terminal to experiment with the methods covered in the above tutorials.


## Optional Reading

We will teach the course assuming you haven't read any of these, but they are all useful and relevant things to know and will allow you to understand the material more deeply and/or tackle a more advanced Week 4 project.

#### [**100 NumPy Exercises**](https://github.com/rougier/numpy-100)

After you've done the pre-course exercises, if you want more practice with this sort of thing, try these. Some of these are a lot more interesting than others - pick out some that sound fun and challenging and try solving them in PyTorch.

#### [**What is torch.nn really?**](https://pytorch.org/tutorials/beginner/nn_tutorial.html) **by Jeremy Howard**

You'll be implementing a lot of functionality of torch.nn and torch.optim yourself during the course. This is a good introduction to what functionality is in these packages. If you don't learn this now, you can pick it up during the course, though perhaps less deeply.

#### [**NLP Demystified**](https://www.nlpdemystified.org/) **by Nitin Punjabi**

An introduction to natural language processing assuming zero ML background.

*   If you've never done NLP before, it's worth skimming to get a general idea of the field. 
*   If you've never built a basic feedforward neural network (MLP) from scratch, the section "Neural Networks I” has a good exercise on this.

#### [**Visualising Representations: Deep Learning and Human Beings**](https://colah.github.io/posts/2015-01-Visualizing-Representations/) **by Chris Olah**

Builds intuition with nice pictures about what deep networks are doing inside.

#### [**Spinning Up in Deep RL**](https://spinningup.openai.com/en/latest/) **by OpenAI**

Introduction to using deep learning for reinforcement learning. ARENA will assume zero RL experience, but having some understanding already means you'll have an easier time and can tackle more advanced versions of things in the course.

#### [**Introduction to Reinforcement Learning**](https://www.youtube.com/watch?v=2pWv7GOvuf0) **with David Silver**

This video course is fairly old (2015) and the state of the art has come a long way, but this is still useful to cover the basics. I would recommend Spinning Up in Deep RL over this unless you learn better from video lectures than reading.

#### [**The Matrix Cookbook**](https://www.math.uwaterloo.ca/~hwolkowi/matrixcookbook.pdf) **by Petersen and Pedersen**

A densely packed reference of facts and identities about matrices. Definitely not intended to teach topics, but a good place to look up something you need. It's worth memorising identities 1-6, 11-16, and 18-23 from Page 6.

#### [**Zoom In: An Introduction to Circuits**](https://distill.pub/2020/circuits/zoom-in/) **by Chris Olah et al**

A very fun article on interpretability in neural networks trained for computer vision.

#### [**Why Momentum Really Works**](https://distill.pub/2017/momentum/) **by Gabriel Goh**

Variations of gradient descent that use momentum are extremely common. We'll teach the basics of momentum in the course, but if you want a richer and deeper understanding then this is a good article to read and reread.

#### [**The Matrix Calculus You Need for Deep Learning**](https://explained.ai/matrix-calculus/) **by Terence Parr and Jeremy Howard**

Takes you from knowing introductory calculus to calculus on matrices. This will be helpful for the backpropagation material, on day 3 of the course.

#### [**A Mathematical Framework for Transformer Circuits**](https://transformer-circuits.pub/2021/framework/index.html) **by Anthropic**

Analyses transformers starting with the simplest toy models and working up. A heavy read but very good for building intuition about what transformers can do. This will form the cornerstone of the mechanistic interpretability chapter.

#### [**In-context Learning and Induction Heads**](https://transformer-circuits.pub/2022/in-context-learning-and-induction-heads/index.html) **by Anthropic**

Describes and analyses "induction heads", an important circuit learned by transformers.

#### [**Neural Networks and Deep Learning**](http://neuralnetworksanddeeplearning.com/) **by Michael Nielsen**




=== NEW CHAPTER ===


# 2️⃣ Einops, Einsum & Tensor Manipulation



> ##### Learning Objectives
>
> - Understand the basics of Einstein summation convention
> - Learn how to use `einops` to perform basic tensor rearrangement, and `einsum` to to perform standard linear algebra operations on tensors

Note - this section contains a large number of exercises. You should feel free to skim through them if you feel comfortable with the basic ideas.


## Reading

* Read about the benefits of the `einops` library [here](https://www.blopig.com/blog/2022/05/einops-powerful-library-for-tensor-operations-in-deep-learning/).
* If you haven't already, then review the [Einops basics tutorial](https://einops.rocks/1-einops-basics/) (up to the "fancy examples" section).
* Read [einsum is all you need](https://rockt.github.io/2018/04/30/einsum) (or [watch it](https://www.youtube.com/watch?v=pkVwUVEHmfI)) for a brief overview of the `einsum` function and how it works. (You don't need to read past section 2.10.)


## Setup


```python
import math
import os
import sys
from pathlib import Path

import einops
import numpy as np
import torch as t
from torch import Tensor

# Make sure exercises are in the path
chapter = "chapter0_fundamentals"
section = "part0_prereqs"
root_dir = next(p for p in Path.cwd().parents if (p / chapter).exists())
exercises_dir = root_dir / chapter / "exercises"
section_dir = exercises_dir / section
if str(exercises_dir) not in sys.path:
    sys.path.append(str(exercises_dir))

import part0_prereqs.tests as tests
from part0_prereqs.utils import display_array_as_img, display_soln_array_as_img

MAIN = __name__ == "__main__"
```


## Einops


```python
arr = np.load(section_dir / "numbers.npy")
```


`arr` is a 4D numpy array. The first axes corresponds to the number, and the next three axes are channels (i.e. RGB), height and width respectively. You have the function `utils.display_array_as_img` which takes in a numpy array and displays it as an image. There are two possible ways this function can be run:

* If the input is three-dimensional, the dimensions are interpreted as `(channel, height, width)` - in other words, as an RGB image.
* If the input is two-dimensional, the dimensions are interpreted as `(height, width)` - i.e. a monochrome image.

For example:


```python
print(arr[0].shape)
display_array_as_img(arr[0])  # plotting the first image in the batch
```


<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">(3, 150, 150)</pre>
<div style="text-align: left"><embed src="https://info-arena.github.io/ARENA_img/misc/media-00/demo1.html" width="167" height="167"></div>


```python
print(arr[0, 0].shape)
display_array_as_img(arr[0, 0])  # plotting the first channel of the first image, as monochrome
```


<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">(150, 150)</pre>
<div style="text-align: left"><embed src="https://info-arena.github.io/ARENA_img/misc/media-00/demo2.html" width="167" height="167"></div>


```python
arr_stacked = einops.rearrange(arr, "b c h w -> c h (b w)")
print(arr_stacked.shape)
display_array_as_img(arr_stacked)  # plotting all images, stacked in a row
```


<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">(3, 150, 900)</pre>
<div style="text-align: left"><embed src="https://info-arena.github.io/ARENA_img/misc/media-00/demo3.html" width="917" height="167"></div>


A series of images follow below, which have been created using einops functions performed on arr. You should work through these and try to produce each of the images yourself. This page also includes solutions, but you should only look at them after you've tried for at least five minutes.

**Note - if you find you're comfortable with the first ~half of these, you can skip to later sections if you'd prefer, since these aren't particularly conceptually important.**


### Exercises - einops operations (match images)

> ```yaml
> Difficulty: 🔴🔴🔴⚪⚪
> Importance: 🔵🔵⚪⚪⚪
> 
> You should spend up to ~45 minutes on these exercises collectively.
> If you think you get the general idea, then you can skip to the next section.
> You shouldn't spend longer than ~10 mins per exercise.
> ```


#### (1) Column-stacking


<div style="text-align: left"><embed src = "https://info-arena.github.io/ARENA_img/misc/media-00/ex1.html" width="167" height = "917"></div>


```python
# Your code here - define arr1

display_array_as_img(arr1)
```


<details><summary>Solution</summary>

```python
arr1 = einops.rearrange(arr, "b c h w -> c (b h) w")
```
</details>


#### (2) Column-stacking and copying

In this example we take just the first digit, and copy it along rows using `einops.repeat`.


<div style="text-align: left"><embed src = "https://info-arena.github.io/ARENA_img/misc/media-00/ex2.html" width="167" height = "317"></div>


```python
# Your code here - define arr2

display_array_as_img(arr2)
```


<details><summary>Solution</summary>

```python
arr2 = einops.repeat(arr[0], "c h w -> c (2 h) w")
```
</details>


#### (3) Row-stacking and double-copying

This example is pretty similar to the previous one, except that the part of the original image we need to slice and pass into `einops.repeat` also has a batch dimension of 2 (since it includes the first 2 digits).


<div style="text-align: left"><embed src = "https://info-arena.github.io/ARENA_img/misc/media-00/ex3.html" width="317" height = "317"></div>


```python
# Your code here - define arr3

display_array_as_img(arr3)
```


<details><summary>Solution</summary>

```python
arr3 = einops.repeat(arr[0:2], "b c h w -> c (b h) (2 w)")
```
</details>


#### (4) Stretching

The image below was stretched vertically by a factor of 2.


<div style="text-align: left"><embed src = "https://info-arena.github.io/ARENA_img/misc/media-00/ex4.html" width="167" height = "317"></div>


```python
# Your code here - define arr4

display_array_as_img(arr4)
```


<details><summary>Solution</summary>

```python
arr4 = einops.repeat(arr[0], "c h w -> c (h 2) w")
```
</details>


#### (5) Split channels

The image below was created by splitting out the 3 channels of the image (i.e. red, green, blue) and turning these into 3 stacked horizontal images. The output is 2D (the display function interprets this as a monochrome image).


<div style="text-align: left"><embed src = "https://info-arena.github.io/ARENA_img/misc/media-00/ex5.html" width="467" height = "167"></div>


```python
# Your code here - define arr5

display_array_as_img(arr5)
```


<details><summary>Solution</summary>

```python
arr5 = einops.rearrange(arr[0], "c h w -> h (c w)")
```
</details>


#### (6) Stack into rows & cols

This requires a rearrange operation with dimensions for row and column stacking.


<div style="text-align: left"><embed src = "https://info-arena.github.io/ARENA_img/misc/media-00/ex6.html" width="467" height = "317"></div>


```python
# Your code here - define arr6

display_array_as_img(arr6)
```


<details><summary>Solution</summary>

```python
arr6 = einops.rearrange(arr, "(b1 b2) c h w -> c (b1 h) (b2 w)", b1=2)
```
</details>


#### (7) Transpose

Here, we've just flipped the model's horizontal and vertical dimensions. Transposing is a fairly common tensor operation.


<div style="text-align: left"><embed src = "https://info-arena.github.io/ARENA_img/misc/media-00/ex7.html" width="167" height = "167"></div>


```python
# Your code here - define arr7

display_array_as_img(arr7)
```


<details><summary>Solution</summary>

```python
arr7 = einops.rearrange(arr[1], "c h w -> c w h")
```
</details>


#### (8) Shrinking

Hint - for this one, you should use **max pooling** - i.e. each pixel value in the output is the maximum of the corresponding 2x2 square in the original image.


<div style="text-align: left"><embed src = "https://info-arena.github.io/ARENA_img/misc/media-00/ex8.html" width="242" height = "167"></div>


```python
# Your code here - define arr8

display_array_as_img(arr8)
```


<details><summary>Solution</summary>

```python
arr8 = einops.reduce(arr, "(b1 b2) c (h h2) (w w2) -> c (b1 h) (b2 w)", "max", h2=2, w2=2, b1=2)
```
</details>


### Broadcasting

Before we go through the next exercises, we'll need to address one important topic in tensor operations - **broadcasting**.

Both NumPy and PyTorch have the same rules for broadcasting. When two tensors are involved in an elementwise operation, NumPy/PyTorch tries to broadcast them (i.e. copying them along dimensions) so that they both have the same shape. The rules of broadcasting are as follows:

1. You can prepend dummy dimensions (of size 1) to the start of a tensor until both have the same number of dimensions
2. After this point, if some dimension has size 1 in one of the tensors, it can be repeated until it matches the size of the corresponding dimension in the other tensor

To give a simple example - suppose we have a 2D batch of data, of shape `data.shape = (N, k)` (i.e. we have `N` separate datapoints, each being a vector of length `k`). Suppose we want to add a vector `vec` of length `k` to each datapoint. This is a valid operation, because when we try and add these two objects together:

1. `vec` gets prepended with a dummy dimension so it has shape `(1, k)` and both are 2D
2. `vec` gets repeated along the first dimension so it has shape `(N, k)`, matching the shape of `data`

Then, our output has shape `(N, k)`, and elements `output[i, j] = data[i, j] + vec[j]`.

Broadcasting can be a very easy place to make mistakes, because it's easy to lose track of the exact shape of your tensors involved. As a warm-up exercise, below are some examples of broadcasting. Can you figure out which are valid, and which will raise errors?


```python
x = t.ones((3, 1, 5))
y = t.ones((1, 4, 5))

z = x + y
```

<details>
<summary>Answer</summary>

This is valid, because the 0th dimension of `y` and the 1st dimension of `x` can both be copied so that `x` and `y` have the same shape: `(3, 4, 5)`. The resulting array `z` will also have shape `(3, 4, 5)`.

This example illustrates an important point - it's not always the case that one of the tensors is strictly smaller and the other is strictly bigger. Sometimes, both tensors will get expanded. 

</details>

```python
x = t.ones((8, 2, 6))
y = t.ones((8, 2))

z = x + y
```

<details>
<summary>Answer</summary>

This is not valid. We first need to expand `y` by appending a dimension to the front, and the last two dimensions of `x` are `(2, 6)`, which won't broadcast with `y`'s `(8, 2)`.
</details>

```python
x = t.ones((8, 2, 6))
y = t.ones((2, 6))

z = x + y
```

<details>
<summary>Answer</summary>

This is valid. Once PyTorch expands `y` by appending a single dimension to the front, it can then be broadcast with `x`.
</details>

```python
x = t.ones((10, 20, 30))
y = t.ones((20, 1))

z = x + y
```

<details>
<summary>Answer</summary>

This is valid. Once PyTorch expands `y` by appending a single dimension to the front, it can then be broadcast with `x` (this will involve copying along the first and last dimensions).
</details>

```python
x = t.ones((4, 1))
y = t.ones((4,))

z = x + y
```

<details>
<summary>Answer</summary>

This is valid. Numpy will expand the second one to `(1, 4)` then broadcast them both to `(4, 4)`.

Although this won't raise an error, it's very possible that this isn't what the person adding these two arrays intended. A common source of mistakes is when you add 2 tensors thinking they're the same shape, but one actually has a dummy dimension you forgot about. Sadly this is something you'll just have to be vigilant for (e.g. adding assert statements where necessary, or making sure you aren't combining too many different tensor operations in a single line), because PyTorch doesn't have built-in ways of statically checking your tensor shapes.

</details>


Einops is a useful tool for reshaping tensors to enable broadcasting. If you just need to add or remove a dummy dimension, you don't need to use einops: `tensor.unsqueeze(dim)` will give you a new tensor with a dummy dimension of size 1 inserted at position `dim` in the new tensor, and `tensor.squeeze(dim)` will give you a tensor with the dimension at position `dim` removed (if it had size 1, otherwise nothing happens).

```python
x = t.ones((3, 1, 5))

print(x.unsqueeze(3).shape)  # (3, 1, 5, 1) because we add a new dummy dimension at idx 3 (the end) in the new tensor

print(x.squeeze(1).shape) # (3, 5) because we remove the dimension at idx 1 (it has size 1)

print(x.squeeze(0).shape) # (3, 1, 5) because we don't remove the leading dimension (it has size 3)
```


### Exercises - einops operations & broadcasting

> ```yaml
> Difficulty: 🔴🔴⚪⚪⚪
> Importance: 🔵🔵🔵⚪⚪
> 
> You should spend up to ~45 minutes on these exercises collectively.
> These are more representative of the kinds of einops operations you'll use in practice.
> ```

Next, we have a series of functions which you should implement using `einops`. In the dropdown below these exercises, you can find solutions to all of them.

First, let's define some functions to help us test our solutions:


```python
def assert_all_equal(actual: Tensor, expected: Tensor) -> None:
    assert actual.shape == expected.shape, f"Shape mismatch, got: {actual.shape}"
    assert (actual == expected).all(), f"Value mismatch, got: {actual}"
    print("Tests passed!")


def assert_all_close(actual: Tensor, expected: Tensor, atol=1e-3) -> None:
    assert actual.shape == expected.shape, f"Shape mismatch, got: {actual.shape}"
    t.testing.assert_close(actual, expected, atol=atol, rtol=0.0)
    print("Tests passed!")
```


#### (A1) rearrange

We'll start with a simple rearrange operation - you're asked to return a particular tensor using only `t.arange` and `einops.rearrange`. The `t.arange` function is similar to the numpy equivalent: `torch.arange(start, end)` will return a 1D tensor containing all the values from `start` to `end - 1` inclusive.


```python
def rearrange_1() -> Tensor:
    """Return the following tensor using only t.arange and einops.rearrange:

    [[3, 4],
     [5, 6],
     [7, 8]]
    """
    raise NotImplementedError()


expected = t.tensor([[3, 4], [5, 6], [7, 8]])
assert_all_equal(rearrange_1(), expected)
```


<details><summary>Solution</summary>

```python
def rearrange_1() -> Tensor:
    """Return the following tensor using only t.arange and einops.rearrange:

    [[3, 4],
     [5, 6],
     [7, 8]]
    """
    return einops.rearrange(t.arange(3, 9), "(h w) -> h w", h=3, w=2)
```
</details>


#### (A2) rearrange

This exercise has the same pattern as the previous one.


```python
def rearrange_2() -> Tensor:
    """Return the following tensor using only t.arange and einops.rearrange:

    [[1, 2, 3],
     [4, 5, 6]]
    """
    raise NotImplementedError()


assert_all_equal(rearrange_2(), t.tensor([[1, 2, 3], [4, 5, 6]]))
```


<details><summary>Solution</summary>

```python
def rearrange_2() -> Tensor:
    """Return the following tensor using only t.arange and einops.rearrange:

    [[1, 2, 3],
     [4, 5, 6]]
    """
    return einops.rearrange(t.arange(1, 7), "(h w) -> h w", h=2, w=3)
```
</details>


#### (B1) temperature average

Here you're given a 1D tensor containing temperatures for each day. You should return a 1D tensor containing the average temperature for each week.

This could be done in 2 separate operations (a reshape from 1D to 2D followed by taking the mean over one of the axes), however we encourage you to try and find a solution with `einops.reduce` in just a single line.


```python
def temperatures_average(temps: Tensor) -> Tensor:
    """Return the average temperature for each week.

    temps: a 1D temperature containing temperatures for each day.
    Length will be a multiple of 7 and the first 7 days are for the first week, second 7 days for the second week, etc.

    You can do this with a single call to reduce.
    """
    assert len(temps) % 7 == 0
    raise NotImplementedError()


temps = t.tensor([71, 72, 70, 75, 71, 72, 70, 75, 80, 85, 80, 78, 72, 83]).float()
expected = [71.571, 79.0]
assert_all_close(temperatures_average(temps), t.tensor(expected))
```


<details><summary>Solution</summary>

```python
def temperatures_average(temps: Tensor) -> Tensor:
    """Return the average temperature for each week.

    temps: a 1D temperature containing temperatures for each day.
    Length will be a multiple of 7 and the first 7 days are for the first week, second 7 days for the second week, etc.

    You can do this with a single call to reduce.
    """
    assert len(temps) % 7 == 0
    return einops.reduce(temps, "(h 7) -> h", "mean")
```
</details>


#### (B2) temperature difference

Here, we're asking you to subtract the average temperature from each week from the daily temperatures. You'll have to be careful of **broadcasting** here, since your temperatures tensor has shape `(14,)` while your average temperature computed above has shape `(2,)` - these are not broadcastable.


```python
def temperatures_differences(temps: Tensor) -> Tensor:
    """For each day, subtract the average for the week the day belongs to.

    temps: as above
    """
    assert len(temps) % 7 == 0
    raise NotImplementedError()


expected = [-0.571, 0.429, -1.571, 3.429, -0.571, 0.429, -1.571, -4.0, 1.0, 6.0, 1.0, -1.0, -7.0, 4.0]
actual = temperatures_differences(temps)
assert_all_close(actual, t.tensor(expected))
```


<details>
<summary>Hint - how to make the tensors broadcastable</summary>

Your averages tensor from earlier was (hopefully) computed using `einops.reduce(temps, "(h 7) -> h", "mean")`, giving it shape `(2,)`. You have 2 options:

- Repeat this averages tensor back to shape `(14,)` so you can subtract it from temps
- Rehsape `temps` tensor to have shape `(7, 2)` which would make it broadcastable with `(2,)`, then flatten it back to `(14,)` after subtracting the average


</details>


<details><summary>Solution</summary>

```python
def temperatures_differences(temps: Tensor) -> Tensor:
    """For each day, subtract the average for the week the day belongs to.

    temps: as above
    """
    assert len(temps) % 7 == 0
    avg = einops.reduce(temps, "(w 7) -> w", "mean")
    return temps - einops.repeat(avg, "w -> (w 7)")
```
</details>


#### (B3) temperature normalized

Lastly, you need to subtract the average and divide by the standard deviation. Note that you can pass `t.std` into the `einops.reduce` function to return the std dev of the values you're reducing over.


```python
def temperatures_normalized(temps: Tensor) -> Tensor:
    """For each day, subtract the weekly average and divide by the weekly standard deviation.

    temps: as above

    Pass t.std to reduce.
    """
    raise NotImplementedError()


expected = [-0.333, 0.249, -0.915, 1.995, -0.333, 0.249, -0.915, -0.894, 0.224, 1.342, 0.224, -0.224, -1.565, 0.894]
actual = temperatures_normalized(temps)
assert_all_close(actual, t.tensor(expected))
```


<details><summary>Solution</summary>

```python
def temperatures_normalized(temps: Tensor) -> Tensor:
    """For each day, subtract the weekly average and divide by the weekly standard deviation.

    temps: as above

    Pass t.std to reduce.
    """
    avg = einops.reduce(temps, "(w 7) -> w", "mean")
    std = einops.reduce(temps, "(h 7) -> h", t.std)
    return (temps - einops.repeat(avg, "w -> (w 7)")) / einops.repeat(std, "w -> (w 7)")
```
</details>


#### (C1) normalize a matrix

Here, we're asking you to normalize the rows of a matrix so that each row has L2 norm (sum of squared values) equal to 1. Note - L2 norm and standard deviation are not the same thing; L2 norm leaves out the averaging over size of vector step. We recommend you try and use the torch function `t.norm` directly rather than einops for this task.

Two useful things we should highlight here:

- Most PyTorch functions like `t.norm(tensor, ...)` which operate on a single tensor are also tensor methods, i.e. they can be used as `tensor.norm(...)` with the same arguments.
- Most PyTorch dimensionality-reducing functions have the `keepdim` argument, which is false by default but will cause your output tensor to keep dummy dimensions if set to true. For example, if `tensor` has shape `(3, 4)` then `tensor.sum(dim=1)` has shape `(3,)` but `tensor.sum(dim=1, keepdim=True)` has shape `(3, 1)`.


```python
def normalize_rows(matrix: Tensor) -> Tensor:
    """Normalize each row of the given 2D matrix.

    matrix: a 2D tensor of shape (m, n).

    Returns: a tensor of the same shape where each row is divided by its l2 norm.
    """
    raise NotImplementedError()


matrix = t.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]]).float()
expected = t.tensor([[0.267, 0.535, 0.802], [0.456, 0.570, 0.684], [0.503, 0.574, 0.646]])
assert_all_close(normalize_rows(matrix), expected)
```


<details><summary>Solution</summary>

```python
def normalize_rows(matrix: Tensor) -> Tensor:
    """Normalize each row of the given 2D matrix.

    matrix: a 2D tensor of shape (m, n).

    Returns: a tensor of the same shape where each row is divided by its l2 norm.
    """
    row_norms = matrix.norm(dim=1, keepdim=True)  # keepdim=True
    return matrix / row_norms
```
</details>


#### (C2) pairwise cosine similarity

Now, you should compute a matrix of shape `(m, m)` where `out[i, j]` is the cosine similarity between the `i`-th and `j`-th rows of `matrix`. 

The cosine similarity between two vectors is given by summing the elementwise products of the normalized vectors. We haven't covered `einsum` yet, but you should be able to get this working using normal elementwise multiplication and summing (or even do this in one step - can you see how?).


```python
def cos_sim_matrix(matrix: Tensor) -> Tensor:
    """Return the cosine similarity matrix for each pair of rows of the given matrix.

    matrix: shape (m, n)
    """
    raise NotImplementedError()


matrix = t.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]]).float()
expected = t.tensor([[1.0, 0.975, 0.959], [0.975, 1.0, 0.998], [0.959, 0.998, 1.0]])
assert_all_close(cos_sim_matrix(matrix), expected)
```


<details>
<summary>Solution</summary>

```python
def cos_sim_matrix(matrix: Tensor) -> Tensor:
    """Return the cosine similarity matrix for each pair of rows of the given matrix.

    matrix: shape (m, n)
    """
    matrix_normalized = normalize_rows(matrix)
    return matrix_normalized @ matrix_normalized.T
```

The reason this solution works is that `matrix_normalized @ matrix_normalized.T` multiplies along the columns of `matrix_normalized` and the rows of `matrix_normalized.T` then sums the output - in other words, it computes the dot products!

For a more verbose solution using explicit broadcasting, you could also do this:

```python
left_matrix = matrix_normalized.unsqueeze(-1)  # shape (m, n, 1)
right_matrix = matrix_normalized.T.unsqueeze(0)  # shape (1, n, m)
products = left_matrix * right_matrix  # shape (m, n, m)
return products.sum(dim=1)  # shape (m, m)
```

</details>


#### (D) sample distribution

Here we're having you do something a bit more practical and less artificial. You're given a probability distribution (i.e. a tensor of probabilities that sum to 1) and asked to sample from it.

Hint - you can use the torch functions `t.rand` and `t.cumsum` to do this without any explicit loops.


```python
def sample_distribution(probs: Tensor, n: int) -> Tensor:
    """Return n random samples from probs, where probs is a normalized probability distribution.

    probs: shape (k,) where probs[i] is the probability of event i occurring.
    n: number of random samples

    Return: shape (n,) where out[i] is an integer indicating which event was sampled.

    Use t.rand and t.cumsum to do this without any explicit loops.
    """
    raise NotImplementedError()


n = 5_000_000
probs = t.tensor([0.05, 0.1, 0.1, 0.2, 0.15, 0.4])
freqs = t.bincount(sample_distribution(probs, n)) / n
assert_all_close(freqs, probs)
```


<details>
<summary>Help - I'm not sure how to use <code>t.rand</code> and <code>t.cumsum</code> in this way.</summary>

Suppose our probabilities were `probs = [0.2, 0.3, 0.5]`. Then the cumsum is `probs_cumsum = [0.2, 0.5, 1.0]`. If we generate a random value `v` between 0 and 1, then sum the boolean tensor `v > probs_cumsum`, it will be 0 exactly `0.2` of the time, 1 exactly `0.3` of the time, and 2 exactly `0.5` of the time - exactly what we want.

</details>


<details><summary>Solution</summary>

```python
def sample_distribution(probs: Tensor, n: int) -> Tensor:
    """Return n random samples from probs, where probs is a normalized probability distribution.

    probs: shape (k,) where probs[i] is the probability of event i occurring.
    n: number of random samples

    Return: shape (n,) where out[i] is an integer indicating which event was sampled.

    Use t.rand and t.cumsum to do this without any explicit loops.
    """
    assert abs(probs.sum() - 1.0) < 0.001
    assert (probs >= 0).all()
    return (t.rand(n, 1) > t.cumsum(probs, dim=0)).sum(dim=-1)
```
</details>


#### (E) classifier accuracy

Here, we're asking you to compute the accuracy of a classifier. `scores` is a tensor of shape `(batch, n_classes)` where `scores[b, i]` is the score the classifier gave to class `i` for input `b`, and `true_classes` is a tensor of shape `(batch,)` where `true_classes[b]` is the true class for input `b`. We want you to return the fraction of times the maximum score is equal to the true class.

You can use the torch function `t.argmax`, it works as follows: `tensor.argmax(dim)` will return a tensor of the index containing the maximum value along the dimension `dim` (i.e. the shape of this output will be the same as the shape of `tensor` except for the dimension `dim`).


```python
def classifier_accuracy(scores: Tensor, true_classes: Tensor) -> Tensor:
    """Return the fraction of inputs for which the maximum score corresponds to the true class for that input.

    scores: shape (batch, n_classes). A higher score[b, i] means that the classifier thinks class i is more likely.
    true_classes: shape (batch, ). true_classes[b] is an integer from [0...n_classes).

    Use t.argmax.
    """
    raise NotImplementedError()


scores = t.tensor([[0.75, 0.5, 0.25], [0.1, 0.5, 0.4], [0.1, 0.7, 0.2]])
true_classes = t.tensor([0, 1, 0])
expected = 2.0 / 3.0
assert classifier_accuracy(scores, true_classes) == expected
print("Tests passed!")
```


<details><summary>Solution</summary>

```python
def classifier_accuracy(scores: Tensor, true_classes: Tensor) -> Tensor:
    """Return the fraction of inputs for which the maximum score corresponds to the true class for that input.

    scores: shape (batch, n_classes). A higher score[b, i] means that the classifier thinks class i is more likely.
    true_classes: shape (batch, ). true_classes[b] is an integer from [0...n_classes).

    Use t.argmax.
    """
    assert true_classes.max() < scores.shape[1]
    return (scores.argmax(dim=1) == true_classes).float().mean()
```
</details>


#### (F1) total price indexing

The next few exercises involve indexing, often using the `torch.gather` function. You can read about it in the docs [here](https://pytorch.org/docs/stable/generated/torch.gather.html).

If you find gather confusing, an alternative is the `eindex` library, which was designed to provide indexing features motivated by how `einops` works. You can read more about that [here](https://www.perfectlynormal.co.uk/blog-eindex), and as a suggested bonus you can try implementing / rewriting the next few functions using `eindex`.


```python
def total_price_indexing(prices: Tensor, items: Tensor) -> float:
    """Given prices for each kind of item and a tensor of items purchased, return the total price.

    prices: shape (k, ). prices[i] is the price of the ith item.
    items: shape (n, ). A 1D tensor where each value is an item index from [0..k).

    Use integer array indexing. The below document describes this for NumPy but it's the same in PyTorch:

    https://numpy.org/doc/stable/user/basics.indexing.html#integer-array-indexing
    """
    raise NotImplementedError()


prices = t.tensor([0.5, 1, 1.5, 2, 2.5])
items = t.tensor([0, 0, 1, 1, 4, 3, 2])
assert total_price_indexing(prices, items) == 9.0
print("Tests passed!")
```


<details><summary>Solution</summary>

```python
def total_price_indexing(prices: Tensor, items: Tensor) -> float:
    """Given prices for each kind of item and a tensor of items purchased, return the total price.

    prices: shape (k, ). prices[i] is the price of the ith item.
    items: shape (n, ). A 1D tensor where each value is an item index from [0..k).

    Use integer array indexing. The below document describes this for NumPy but it's the same in PyTorch:

    https://numpy.org/doc/stable/user/basics.indexing.html#integer-array-indexing
    """
    assert items.max() < prices.shape[0]
    return prices[items].sum().item()
```
</details>


#### (F2) gather 2D


```python
def gather_2d(matrix: Tensor, indexes: Tensor) -> Tensor:
    """Perform a gather operation along the second dimension.

    matrix: shape (m, n)
    indexes: shape (m, k)

    Return: shape (m, k). out[i][j] = matrix[i][indexes[i][j]]

    For this problem, the test already passes and it's your job to write at least three asserts relating the arguments and the output. This is a tricky function and worth spending some time to wrap your head around its behavior.

    See: https://pytorch.org/docs/stable/generated/torch.gather.html?highlight=gather#torch.gather
    """
    # YOUR CODE HERE - add assert statement(s) here for `indices` and `matrix`

    out = matrix.gather(1, indexes)
    # YOUR CODE HERE - add assert statement(s) here for `out`

    return out


matrix = t.arange(15).view(3, 5)
indexes = t.tensor([[4], [3], [2]])
expected = t.tensor([[4], [8], [12]])
assert_all_equal(gather_2d(matrix, indexes), expected)

indexes2 = t.tensor([[2, 4], [1, 3], [0, 2]])
expected2 = t.tensor([[2, 4], [6, 8], [10, 12]])
assert_all_equal(gather_2d(matrix, indexes2), expected2)
```


<details><summary>Solution</summary>

```python
def gather_2d(matrix: Tensor, indexes: Tensor) -> Tensor:
    """Perform a gather operation along the second dimension.

    matrix: shape (m, n)
    indexes: shape (m, k)

    Return: shape (m, k). out[i][j] = matrix[i][indexes[i][j]]

    For this problem, the test already passes and it's your job to write at least three asserts relating the arguments and the output. This is a tricky function and worth spending some time to wrap your head around its behavior.

    See: https://pytorch.org/docs/stable/generated/torch.gather.html?highlight=gather#torch.gather
    """
    assert matrix.ndim == indexes.ndim
    assert indexes.shape[0] <= matrix.shape[0]

    out = matrix.gather(1, indexes)
    assert out.shape == indexes.shape

    return out
```
</details>


#### (F3) total price gather


```python
def total_price_gather(prices: Tensor, items: Tensor) -> float:
    """Compute the same as total_price_indexing, but use torch.gather."""
    assert items.max() < prices.shape[0]
    raise NotImplementedError()


prices = t.tensor([0.5, 1, 1.5, 2, 2.5])
items = t.tensor([0, 0, 1, 1, 4, 3, 2])
assert total_price_gather(prices, items) == 9.0
print("Tests passed!")
```


<details><summary>Solution</summary>

```python
def total_price_gather(prices: Tensor, items: Tensor) -> float:
    """Compute the same as total_price_indexing, but use torch.gather."""
    assert items.max() < prices.shape[0]
    return prices.gather(0, items).sum().item()
```
</details>


#### (G) indexing


```python
def integer_array_indexing(matrix: Tensor, coords: Tensor) -> Tensor:
    """Return the values at each coordinate using integer array indexing.

    For details on integer array indexing, see:
    https://numpy.org/doc/stable/user/basics.indexing.html#integer-array-indexing

    matrix: shape (d_0, d_1, ..., d_n)
    coords: shape (batch, n)

    Return: (batch, )
    """
    raise NotImplementedError()


mat_2d = t.arange(15).view(3, 5)
coords_2d = t.tensor([[0, 1], [0, 4], [1, 4]])
actual = integer_array_indexing(mat_2d, coords_2d)
assert_all_equal(actual, t.tensor([1, 4, 9]))

mat_3d = t.arange(2 * 3 * 4).view((2, 3, 4))
coords_3d = t.tensor([[0, 0, 0], [0, 1, 1], [0, 2, 2], [1, 0, 3], [1, 2, 0]])
actual = integer_array_indexing(mat_3d, coords_3d)
assert_all_equal(actual, t.tensor([0, 5, 10, 15, 20]))
```


<details><summary>Solution</summary>

```python
def integer_array_indexing(matrix: Tensor, coords: Tensor) -> Tensor:
    """Return the values at each coordinate using integer array indexing.

    For details on integer array indexing, see:
    https://numpy.org/doc/stable/user/basics.indexing.html#integer-array-indexing

    matrix: shape (d_0, d_1, ..., d_n)
    coords: shape (batch, n)

    Return: (batch, )
    """
    return matrix[tuple(coords.T)]
```
</details>


#### (H1) batched logsumexp


```python
def batched_logsumexp(matrix: Tensor) -> Tensor:
    """For each row of the matrix, compute log(sum(exp(row))) in a numerically stable way.

    matrix: shape (batch, n)

    Return: (batch, ). For each i, out[i] = log(sum(exp(matrix[i]))).

    Do this without using PyTorch's logsumexp function.

    A couple useful blogs about this function:
    - https://leimao.github.io/blog/LogSumExp/
    - https://gregorygundersen.com/blog/2020/02/09/log-sum-exp/
    """
    raise NotImplementedError()


matrix = t.tensor([[-1000, -1000, -1000, -1000], [1000, 1000, 1000, 1000]])
expected = t.tensor([-1000 + math.log(4), 1000 + math.log(4)])
actual = batched_logsumexp(matrix)
assert_all_close(actual, expected)

matrix2 = t.randn((10, 20))
expected2 = t.logsumexp(matrix2, dim=-1)
actual2 = batched_logsumexp(matrix2)
assert_all_close(actual2, expected2)
```


<details><summary>Solution</summary>

```python
def batched_logsumexp(matrix: Tensor) -> Tensor:
    """For each row of the matrix, compute log(sum(exp(row))) in a numerically stable way.

    matrix: shape (batch, n)

    Return: (batch, ). For each i, out[i] = log(sum(exp(matrix[i]))).

    Do this without using PyTorch's logsumexp function.

    A couple useful blogs about this function:
    - https://leimao.github.io/blog/LogSumExp/
    - https://gregorygundersen.com/blog/2020/02/09/log-sum-exp/
    """
    C = matrix.max(dim=-1).values
    exps = t.exp(matrix - einops.rearrange(C, "n -> n 1"))
    return C + t.log(t.sum(exps, dim=-1))
```
</details>


#### (H2) batched softmax


```python
def batched_softmax(matrix: Tensor) -> Tensor:
    """For each row of the matrix, compute softmax(row).

    Do this without using PyTorch's softmax function.
    Instead, use the definition of softmax: https://en.wikipedia.org/wiki/Softmax_function

    matrix: shape (batch, n)

    Return: (batch, n). For each i, out[i] should sum to 1.
    """
    raise NotImplementedError()


matrix = t.arange(1, 6).view((1, 5)).float().log()
expected = t.arange(1, 6).view((1, 5)) / 15.0
actual = batched_softmax(matrix)
assert_all_close(actual, expected)
for i in [0.12, 3.4, -5, 6.7]:
    assert_all_close(actual, batched_softmax(matrix + i))  # check it's translation-invariant

matrix2 = t.rand((10, 20))
actual2 = batched_softmax(matrix2)
assert actual2.min() >= 0.0
assert actual2.max() <= 1.0
assert_all_equal(actual2.argsort(), matrix2.argsort())
assert_all_close(actual2.sum(dim=-1), t.ones(matrix2.shape[:-1]))
```


<details><summary>Solution</summary>

```python
def batched_softmax(matrix: Tensor) -> Tensor:
    """For each row of the matrix, compute softmax(row).

    Do this without using PyTorch's softmax function.
    Instead, use the definition of softmax: https://en.wikipedia.org/wiki/Softmax_function

    matrix: shape (batch, n)

    Return: (batch, n). For each i, out[i] should sum to 1.
    """
    exp = matrix.exp()
    return exp / exp.sum(dim=-1, keepdim=True)
```
</details>


#### (H3) batched logsoftmax


```python
def batched_logsoftmax(matrix: Tensor) -> Tensor:
    """Compute log(softmax(row)) for each row of the matrix.

    matrix: shape (batch, n)

    Return: (batch, n).

    Do this without using PyTorch's logsoftmax function.
    For each row, subtract the maximum first to avoid overflow if the row contains large values.
    """
    raise NotImplementedError()


matrix = t.arange(1, 7).view((2, 3)).float()
start = 1000
matrix2 = t.arange(start + 1, start + 7).view((2, 3)).float()
actual = batched_logsoftmax(matrix2)
expected = t.tensor([[-2.4076, -1.4076, -0.4076], [-2.4076, -1.4076, -0.4076]])
assert_all_close(actual, expected)
```


<details><summary>Solution</summary>

```python
def batched_logsoftmax(matrix: Tensor) -> Tensor:
    """Compute log(softmax(row)) for each row of the matrix.

    matrix: shape (batch, n)

    Return: (batch, n).

    Do this without using PyTorch's logsoftmax function.
    For each row, subtract the maximum first to avoid overflow if the row contains large values.
    """
    C = matrix.max(dim=1, keepdim=True).values
    return matrix - C - (matrix - C).exp().sum(dim=1, keepdim=True).log()
```
</details>


#### (H4) batched cross entropy loss


```python
def batched_cross_entropy_loss(logits: Tensor, true_labels: Tensor) -> Tensor:
    """Compute the cross entropy loss for each example in the batch.

    logits: shape (batch, classes). logits[i][j] is the unnormalized prediction for example i and class j.
    true_labels: shape (batch, ). true_labels[i] is an integer index representing the true class for example i.

    Return: shape (batch, ). out[i] is the loss for example i.

    Hint: convert the logits to log-probabilities using your batched_logsoftmax from above.
    Then the loss for an example is just the negative of the log-probability that the model assigned to the true class. Use torch.gather to perform the indexing.
    """
    assert logits.shape[0] == true_labels.shape[0]
    assert true_labels.max() < logits.shape[1]
    raise NotImplementedError()


logits = t.tensor([[float("-inf"), float("-inf"), 0], [1 / 3, 1 / 3, 1 / 3], [float("-inf"), 0, 0]])
true_labels = t.tensor([2, 0, 0])
expected = t.tensor([0.0, math.log(3), float("inf")])
actual = batched_cross_entropy_loss(logits, true_labels)
assert_all_close(actual, expected)
```


<details><summary>Solution</summary>

```python
def batched_cross_entropy_loss(logits: Tensor, true_labels: Tensor) -> Tensor:
    """Compute the cross entropy loss for each example in the batch.

    logits: shape (batch, classes). logits[i][j] is the unnormalized prediction for example i and class j.
    true_labels: shape (batch, ). true_labels[i] is an integer index representing the true class for example i.

    Return: shape (batch, ). out[i] is the loss for example i.

    Hint: convert the logits to log-probabilities using your batched_logsoftmax from above.
    Then the loss for an example is just the negative of the log-probability that the model assigned to the true class. Use torch.gather to perform the indexing.
    """
    assert logits.shape[0] == true_labels.shape[0]
    assert true_labels.max() < logits.shape[1]
    logprobs = batched_logsoftmax(logits)
    indices = einops.rearrange(true_labels, "n -> n 1")
    pred_at_index = logprobs.gather(1, indices)
    return -einops.rearrange(pred_at_index, "n 1 -> n")
```
</details>


#### (I1) collect rows


```python
def collect_rows(matrix: Tensor, row_indexes: Tensor) -> Tensor:
    """Return a 2D matrix whose rows are taken from the input matrix in order according to row_indexes.

    matrix: shape (m, n)
    row_indexes: shape (k,). Each value is an integer in [0..m).

    Return: shape (k, n). out[i] is matrix[row_indexes[i]].
    """
    raise NotImplementedError()


matrix = t.arange(15).view((5, 3))
row_indexes = t.tensor([0, 2, 1, 0])
actual = collect_rows(matrix, row_indexes)
expected = t.tensor([[0, 1, 2], [6, 7, 8], [3, 4, 5], [0, 1, 2]])
assert_all_equal(actual, expected)
```


<details><summary>Solution</summary>

```python
def collect_rows(matrix: Tensor, row_indexes: Tensor) -> Tensor:
    """Return a 2D matrix whose rows are taken from the input matrix in order according to row_indexes.

    matrix: shape (m, n)
    row_indexes: shape (k,). Each value is an integer in [0..m).

    Return: shape (k, n). out[i] is matrix[row_indexes[i]].
    """
    assert row_indexes.max() < matrix.shape[0]
    return matrix[row_indexes]
```
</details>


#### (I2) collect columns


```python
def collect_columns(matrix: Tensor, column_indexes: Tensor) -> Tensor:
    """Return a 2D matrix whose columns are taken from the input matrix in order according to column_indexes.

    matrix: shape (m, n)
    column_indexes: shape (k,). Each value is an integer in [0..n).

    Return: shape (m, k). out[:, i] is matrix[:, column_indexes[i]].
    """
    assert column_indexes.max() < matrix.shape[1]
    raise NotImplementedError()


matrix = t.arange(15).view((5, 3))
column_indexes = t.tensor([0, 2, 1, 0])
actual = collect_columns(matrix, column_indexes)
expected = t.tensor([[0, 2, 1, 0], [3, 5, 4, 3], [6, 8, 7, 6], [9, 11, 10, 9], [12, 14, 13, 12]])
assert_all_equal(actual, expected)
```


<details><summary>Solution</summary>

```python
def collect_columns(matrix: Tensor, column_indexes: Tensor) -> Tensor:
    """Return a 2D matrix whose columns are taken from the input matrix in order according to column_indexes.

    matrix: shape (m, n)
    column_indexes: shape (k,). Each value is an integer in [0..n).

    Return: shape (m, k). out[:, i] is matrix[:, column_indexes[i]].
    """
    assert column_indexes.max() < matrix.shape[1]
    return matrix[:, column_indexes]
```
</details>


## Einsum

Einsum is a very useful function for performing linear operations, which you'll probably be using a lot during this programme.

> Note - we'll be using the `einops.einsum` version of the function, which works differently to the more conventional `torch.einsum`:
> 
> * `einops.einsum` has the arrays as the first arguments, and uses spaces to separate dimensions in the string.
> * `torch.einsum` has the string as its first argument, and doesn't use spaces to separate dimensions (each dim is represented by a single character).
> 
> For instance, `torch.einsum("ij,i->j", A, b)` is equivalent to `einops.einsum(A, b, "i j, i -> j")`. (Note, einops doesn't care whether there are spaces either side of `,` and `->`, so you don't need to match this syntax exactly.)

Although there are many different kinds of operations you can perform, they are all derived from three key rules:

1. Repeating letters in different inputs means those values will be multiplied, and those products will be in the output. 
    * For example, `M = einops.einsum(A, B, "i j, i j -> i j")` just corresponds to the elementwise product `M = A * B` (because $M_{ij} = A_{ij} B_{ij}$).
2. Omitting a letter means that the axis will be summed over.
    * For example, if `x` is a 2D array with shape `(I, J)`, then `einops.einsum(x, "i j -> i")` will be a 1D array of length `I` containing the row sums of `x` (we're summing along the `j`-index, i.e. across rows).
3. We can return the unsummed axes in any order.
    * For example, `einops.einsum(x, "i j k -> k j i")` does the same thing as `einops.rearrange(x, "i j k -> k j i")`.

*Note - the einops creators supposedly have plans to support shape rearrangement, e.g. with operations like `einops.einsum(x, y, "i j, j k l -> i (k l)")` (i.e. combining the features of rearrange and einsum), so we can all look forward to that day!*


### Exercises - einsum

> ```yaml
> Difficulty: 🔴🔴⚪⚪⚪
> Importance: 🔵🔵🔵🔵⚪
> 
> You should spend up to 15-20 minutes on these exercises collectively.
> If you think you get the general idea, then you can skip to the next section.
> ```

In the following exercises, you'll write simple functions using `einsum` which replicate the functionality of standard NumPy functions: trace, matrix multiplication, inner and outer products. We've also included some test functions which you should run.

Note - this version of einsum will require that you include `->`, even if you're summing to a scalar (i.e. the right hand side of your string expression is empty).


```python
def einsum_trace(mat: np.ndarray):
    """
    Returns the same as `np.trace`.
    """
    raise NotImplementedError()


def einsum_mv(mat: np.ndarray, vec: np.ndarray):
    """
    Returns the same as `np.matmul`, when `mat` is a 2D array and `vec` is 1D.
    """
    raise NotImplementedError()


def einsum_mm(mat1: np.ndarray, mat2: np.ndarray):
    """
    Returns the same as `np.matmul`, when `mat1` and `mat2` are both 2D arrays.
    """
    raise NotImplementedError()


def einsum_inner(vec1: np.ndarray, vec2: np.ndarray):
    """
    Returns the same as `np.inner`.
    """
    raise NotImplementedError()


def einsum_outer(vec1: np.ndarray, vec2: np.ndarray):
    """
    Returns the same as `np.outer`.
    """
    raise NotImplementedError()


tests.test_einsum_trace(einsum_trace)
tests.test_einsum_mv(einsum_mv)
tests.test_einsum_mm(einsum_mm)
tests.test_einsum_inner(einsum_inner)
tests.test_einsum_outer(einsum_outer)
```


```

---

## chapter0_fundamentals/instructions/pages/01_[0.1]_Ray_Tracing.md

```markdown
# [0.1] - Ray Tracing


> **Colab: [exercises](https://colab.research.google.com/github/callummcdougall/arena-pragmatic-interp/blob/main/chapter0_fundamentals/exercises/part1_ray_tracing/0.1_Ray_Tracing_exercises.ipynb?t=20260303) | [solutions](https://colab.research.google.com/github/callummcdougall/arena-pragmatic-interp/blob/main/chapter0_fundamentals/exercises/part1_ray_tracing/0.1_Ray_Tracing_solutions.ipynb?t=20260303)**

Please send any problems / bugs on the `#errata` channel in the [Slack group](https://join.slack.com/t/arena-uk/shared_invite/zt-3afdmdhye-Mdb3Sv~ss_V_mEaXEbkABA), and ask any questions on the dedicated channels for this chapter of material.

If you want to change to dark mode, you can do this by clicking the three horizontal lines in the top-right, then navigating to Settings → Theme.

Links to all other chapters: [(0) Fundamentals](https://arena-chapter0-fundamentals.streamlit.app/), [(1) Transformer Interpretability](https://arena-chapter1-transformer-interp.streamlit.app/), [(2) RL](https://arena-chapter2-rl.streamlit.app/).

<img src="https://raw.githubusercontent.com/info-arena/ARENA_img/main/misc/headers/header-01.png" width="350">


# Introduction


Today we'll be practicing batched matrix operations in PyTorch by writing a basic graphics renderer. We'll start with an extremely simplified case and work up to rendering your very own 3D Pikachu!

We'll also be touching on some general topics which will be important going forwards in this course, such as:

* Using GPT systems to assist your learning and coding
* Typechecking, and good coding practices
* Debugging, with VSCode's built-in run & debug features


## Content & Learning Objectives

### 1️⃣ Rays & Segments

This section introduces the key ideas and concepts in today's exercises, and guides you through some basic functions involving creating & using 2D rays.

> ##### Learning Objectives
>
> - Learn how to create PyTorch tensors in a variety of ways
> - Understand how to parametrize lines and rays in 2D
> - Learn about type annotations and linear operations in PyTorch

### 2️⃣ Batched Operations

In the next section, you'll extend your work from the first section to perform batched operations, i.e. operations over several different dimensions at once.

> ##### Learning Objectives
>
> - Learn about some important concepts related to batched operations, e.g. broadcasting and logical reductions
> - Understand and use the `einops` library
> - Apply this knowledge to create & work with a batch of rays

### 3️⃣ Triangles

In the final section we move into the 2D and 3D realms, and build up to rendering a full 3D mesh as a 2D image.

> ##### Learning Objectives
>
> - Understand how to parametrize triangles in 2D and 3D, and solve for their intersection with rays
> - Put everything together, to render your mesh as a 2D image

### 4️⃣ Video & Lighting

In the last set of exercises, you can implement some more mathematically complex forms of raytracing to get things like dynamic lighting & videos. There's also some optional material at the very end which covers the `pytest` library, and has you write your own tests.

> ##### Learning Objectives
> 
> - Learn how surface normal vectors can be used to compute lighting effects
> - Render your figures in video form (as an animated camera pan)
> - (optional) Learn about the `pytest` library, and write your own tests for the functions you wrote


## Setup code


```python
import os
import sys
from functools import partial
from pathlib import Path
from typing import Callable

import einops
import plotly.express as px
import plotly.graph_objects as go
import torch as t
from IPython.display import display
from ipywidgets import interact
from jaxtyping import Bool, Float
from torch import Tensor
from tqdm import tqdm

# Make sure exercises are in the path
chapter = "chapter0_fundamentals"
section = "part1_ray_tracing"
root_dir = next(p for p in Path.cwd().parents if (p / chapter).exists())
exercises_dir = root_dir / chapter / "exercises"
section_dir = exercises_dir / section
if str(exercises_dir) not in sys.path:
    sys.path.append(str(exercises_dir))

import part1_ray_tracing.tests as tests
from part1_ray_tracing.utils import (
    render_lines_with_plotly,
    setup_widget_fig_ray,
    setup_widget_fig_triangle,
)
from plotly_utils import imshow

MAIN = __name__ == "__main__"
```


<details>
<summary>Help - I get a NumPy-related error</summary>

This is an annoying colab-related issue which I haven't been able to find a satisfying fix for. If you restart runtime (but don't delete runtime), and run just the imports cell above again (but not the `%pip install` cell), the problem should go away.
</details>


<details>
<summary>Note on <code>pathlib</code></summary>

We'll be using the `pathlib` library to define file paths. This is a more modern way of working with file paths than the `os` library, and is more cross-platform. You can read more about it [here](https://realpython.com/python-pathlib/).

A major advantage of using `pathlib` rather than just relative path names is that it is more robust to which file / directory you happen to be running your code in. There's nothing more frustrating than failing to import or load a file, even though you can see it right there in your directory! Most of our code to load files will look something like this:

```python
with open(section_dir / "pikachu.pt", "rb") as f:
    triangles = t.load(f)
```

since `section_dir` is the name of the `part1_ray_tracing` directory, and forward slashes are used to define files or directories within that directory.
</details>




=== NEW CHAPTER ===


# 1️⃣ Rays & Segments



> ##### Learning Objectives
>
> - Learn how to create PyTorch tensors in a variety of ways
> - Understand how to parametrize lines and rays in 2D
> - Learn about type annotations and linear operations in PyTorch

## 1D Image Rendering

In our initial setup, the **camera** will be a single point at the origin, and the **screen** will be the plane at x=1.

**Objects** in the world consist of triangles, where triangles are represented as 3 points in 3D space (so 9 floating point values per triangle). You can build any shape out of sufficiently many triangles and your Pikachu will be made from 412 triangles.

The camera will emit one or more **rays**, where a ray is represented by an **origin** point and a **direction** point. Conceptually, the ray is emitted from the origin and continues in the given direction until it intersects an object.

We have no concept of lighting or color yet, so for now we'll say that a pixel on our screen should show a bright color if a ray from the origin through it intersects an object, otherwise our screen should be dark.


<img src="https://raw.githubusercontent.com/info-arena/ARENA_img/main/misc/ray_tracing.png" width="400">


To start, we'll let the z dimension in our `(x, y, z)` space be zero and work in the remaining two dimensions.


### Exercise - implement `make_rays_1d`

> ```yaml
> Difficulty: 🔴🔴⚪⚪⚪
> Importance: 🔵🔵🔵⚪⚪
> 
> You should spend up to 10-15 minutes on this exercise.
> ```


Implement the following `make_rays_1d` function so it generates some rays coming out of the origin, which we'll take to be `(0, 0, 0)`.

Calling `render_lines_with_plotly` on your rays will display them in a 3D plot.


```python
def make_rays_1d(num_pixels: int, y_limit: float) -> Tensor:
    """
    num_pixels: The number of pixels in the y dimension. Since there is one ray per pixel, this is
        also the number of rays.
    y_limit: At x=1, the rays should extend from -y_limit to +y_limit, inclusive of both endpoints.

    Returns: shape (num_pixels, num_points=2, num_dim=3) where the num_points dimension contains
        (origin, direction) and the num_dim dimension contains xyz.

    Example of make_rays_1d(9, 1.0): [
        [[0, 0, 0], [1, -1.0, 0]],
        [[0, 0, 0], [1, -0.75, 0]],
        [[0, 0, 0], [1, -0.5, 0]],
        ...
        [[0, 0, 0], [1, 0.75, 0]],
        [[0, 0, 0], [1, 1, 0]],
    ]
    """
    raise NotImplementedError()


rays1d = make_rays_1d(9, 10.0)
fig = render_lines_with_plotly(rays1d)
```


<details><summary>Click to see the expected output</summary>

<div style="text-align: left"><embed src="https://info-arena.github.io/ARENA_img/misc/media-01/0101.html" width="620" height="620"></div>

</details>


<details><summary>Solution</summary>

```python
def make_rays_1d(num_pixels: int, y_limit: float) -> Tensor:
    """
    num_pixels: The number of pixels in the y dimension. Since there is one ray per pixel, this is
        also the number of rays.
    y_limit: At x=1, the rays should extend from -y_limit to +y_limit, inclusive of both endpoints.

    Returns: shape (num_pixels, num_points=2, num_dim=3) where the num_points dimension contains
        (origin, direction) and the num_dim dimension contains xyz.

    Example of make_rays_1d(9, 1.0): [
        [[0, 0, 0], [1, -1.0, 0]],
        [[0, 0, 0], [1, -0.75, 0]],
        [[0, 0, 0], [1, -0.5, 0]],
        ...
        [[0, 0, 0], [1, 0.75, 0]],
        [[0, 0, 0], [1, 1, 0]],
    ]
    """
    rays = t.zeros((num_pixels, 2, 3), dtype=t.float32)
    t.linspace(-y_limit, y_limit, num_pixels, out=rays[:, 1, 1])
    rays[:, 1, 0] = 1
    return rays
```
</details>


### Tip - the `out` keyword argument

Many PyTorch functions take an optional keyword argument `out`. If provided, instead of allocating a new tensor and returning that, the output is written directly to the `out` tensor.

If you used `torch.arange` or `torch.linspace` above, try using the `out` argument. Note that a basic indexing expression like `rays[:, 1, 1]` returns a view that shares storage with `rays`, so writing to the view will modify `rays`. You'll learn more about views later today.

## Ray-Object Intersection

Suppose we have a line segment defined by points $L_1$ and $L_2$. Then for a given ray, we can test if the ray intersects the line segment like so:

- Supposing both the ray and line segment were infinitely long, solve for their intersection point.
- If the point exists, check whether that point is inside the line segment and the ray.

Our camera ray is defined by the origin $O$ and direction $D$ and our object line is defined by points $L_1$ and $L_2$.

We can write the equations for all points on the camera ray as $R(u)=O +u D$ for $u \in [0, \infty)$ and on the object line as $O(v)=L_1+v(L_2 - L_1)$ for $v \in [0, 1]$.

The following interactive widget lets you play with this parameterization of the problem. Run the cells one after another:


```python
fig: go.FigureWidget = setup_widget_fig_ray()
display(fig)


@interact(v=(0.0, 6.0, 0.01), seed=(0, 10, 1))
def update(v=0.0, seed=0):
    t.manual_seed(seed)
    L_1, L_2 = t.rand(2, 2)
    P = lambda v: L_1 + v * (L_2 - L_1)
    x, y = zip(P(0), P(6))
    with fig.batch_update():
        fig.update_traces({"x": x, "y": y}, 0)
        fig.update_traces({"x": [L_1[0], L_2[0]], "y": [L_1[1], L_2[1]]}, 1)
        fig.update_traces({"x": [P(v)[0]], "y": [P(v)[1]]}, 2)
```


<div style="text-align: left"><embed src="https://info-arena.github.io/ARENA_img/misc/media-01/animation-1a.mp4" width="400" height="450" style="background-color: white;"></div>


Setting the line equations from above equal gives the solution:

$$
\begin{aligned}O + u D &= L_1 + v(L_2 - L_1) \\ u D - v(L_2 - L_1) &= L_1 - O  \\ \begin{pmatrix} D_x & (L_1 - L_2)_x \\ D_y & (L_1 - L_2)_y \\ \end{pmatrix} \begin{pmatrix} u \\ v \\ \end{pmatrix} &=  \begin{pmatrix} (L_1 - O)_x \\ (L_1 - O)_y \\ \end{pmatrix} \end{aligned}
$$

Once we've found values of $u$ and $v$ which satisfy this equation, if any (the lines could be parallel) we just need to check that $u \geq 0$ and $v \in [0, 1]$.


### Exercise - implement `intersect_ray_1d`

> ```yaml
> Difficulty: 🔴🔴🔴⚪⚪
> Importance: 🔵🔵🔵🔵⚪
> 
> You should spend up to 20-25 minutes on this exercise.
> It involves some of today's core concepts - tensor manipulation, linear operations, etc.
> ```

Using [`torch.linalg.solve`](https://pytorch.org/docs/stable/generated/torch.linalg.solve.html) and [`torch.stack`](https://pytorch.org/docs/stable/generated/torch.stack.html), implement the `intersect_ray_1d` function to solve the above matrix equation.

<details>
<summary>Aside - difference between stack and concatenate</summary>

`torch.stack` will combine tensors along a new dimension.

```python
>>> t.stack([t.ones(2, 2), t.zeros(2, 2)], dim=0)
tensor([[[1., 1.],
         [1., 1.]],

        [[0., 0.],
         [0., 0.]]])
```

`torch.concat` (alias `torch.cat`) will combine tensors along an existing dimension.

```python
>>> t.cat([t.ones(2, 2), t.zeros(2, 2)], dim=0)
tensor([[1., 1.],
        [1., 1.],
        [0., 0.],
        [0., 0.]])
```

Here, you should use `torch.stack` to construct e.g. the matrix on the left hand side, because you want to combine the vectors $D$ and $L_1 - L_2$ to make a matrix.
</details>

Is it possible for the solve method to fail? Give a sample input where this would happen.

<details>
<summary>Answer - Failing Solve</summary>

If the ray and segment are exactly parallel, then the solve will fail because there is no solution to the system of equations. For this function, handle this by catching the exception and returning False.
</details>


```python
def intersect_ray_1d(ray: Float[Tensor, "points dims"], segment: Float[Tensor, "points dims"]) -> bool:
    """
    ray: shape (n_points=2, n_dim=3)  # O, D points
    segment: shape (n_points=2, n_dim=3)  # L_1, L_2 points

    Return True if the ray intersects the segment.
    """
    raise NotImplementedError()


tests.test_intersect_ray_1d(intersect_ray_1d)
tests.test_intersect_ray_1d_special_case(intersect_ray_1d)
```


<details>
<summary>Help! My code is failing with a 'must be batches of square matrices' exception.</summary>

Our formula only uses the x and y coordinates - remember to discard the z coordinate for now.

It's good practice to write asserts on the shape of things so that your asserts will fail with a helpful error message. In this case, you could assert that the `mat` argument is of shape (2, 2) and the `vec` argument is of shape (2,). Also, see the aside below on typechecking.
</details>


<details><summary>Solution</summary>

```python
def intersect_ray_1d(ray: Float[Tensor, "points dims"], segment: Float[Tensor, "points dims"]) -> bool:
    """
    ray: shape (n_points=2, n_dim=3)  # O, D points
    segment: shape (n_points=2, n_dim=3)  # L_1, L_2 points

    Return True if the ray intersects the segment.
    """
    # Get the x and y coordinates (ignore z)
    ray = ray[:, :2]
    segment = segment[:, :2]

    # Ray is [[Ox, Oy], [Dx, Dy]]
    O, D = ray
    # Segment is [[L1x, L1y], [L2x, L2y]]
    L_1, L_2 = segment

    # Create matrix and vector, and solve equation
    mat = t.stack([D, L_1 - L_2], dim=-1)
    vec = L_1 - O

    # Solve equation (return False if no solution)
    try:
        sol = t.linalg.solve(mat, vec)
    except RuntimeError:
        return False

    # If there is a solution, check the soln is in the correct range for there to be an intersection
    u = sol[0].item()
    v = sol[1].item()
    return (u >= 0.0) and (v >= 0.0) and (v <= 1.0)
```
</details>


### Aside - type hints

Adding type hints to your code is a useful habit to get into. Some advantages of using them:

- **They help document your code**, making it more readable (for yourself and for others)
- **The improve IDE behaviour**, i.e. getting better code completion
- **They encourage better code structure**, since they force you to consider your inputs & outputs explicitly
- **They make debugging easier**, since you'll find it easier to spot where a variable might not match the type signature you've given for it

As well as simple objects, you can also typecheck iterables of objects, for example:

- `list[int]` for a list of integers,
- `dict[str, float]` for a dict mapping strings to floats,
- `tuple[Tensor, Tensor]` for a length-2 tuple containing tensors,
- `tuple[int, ...]` for a tuple containing one or more integers.

and you can also use other syntax to extend behaviour, e.g. `x: int | None` for a variable which can either be an integer or `None`.

Jaxtyping also gives us useful type hint features, e.g. we have `ray: Float[Tensor, "points dims"]` to indicate a tensor of floats with dimensions `points` and `dims`. Unlike the examples above this is unlikely to be captured by syntax highlighting when you make a mistake, instead it's best to view this as an alternative to annotating the tensor shape. You may or may not prefer to use this. 

When in doubt however, it's best to make assertions on the variable type or tensor shape explicitly, e.g. `assert isinstance(x, Tensor)` or `assert x.shape == ...`. We generally don't recommend static type checking like [mypy](https://mypy-lang.org/) in this course, because there aren't generally standard and robust ways to do it which will fit all IDEs & use-cases.




=== NEW CHAPTER ===


# 2️⃣ Batched Operations



> ##### Learning Objectives
>
> - Learn about some important concepts related to batched operations, e.g. broadcasting and logical reductions
> - Understand and use the `einops` library
> - Apply this knowledge to create & work with a batch of rays

In this section, we'll move onto batched operations. First, it's necessary to cover some important tips for working effectively with PyTorch tensors. If you've gone through the prerequisite material then several of these should already be familiar to you.


## Tensor Operations - 5 Tips


### Tip (1/5) - Elementwise Logical Operations on Tensors

For regular booleans, the keywords `and`, `or`, and `not` are used to do logical operations and the operators `&`, `|`, and `~` do `and`, `or` and `not` on each bit of the input numbers. Analogously, we use the operators `&`, `|` `~` on tensors to perform these operations on each element of the tensor, e.g. `x & y` returns the tensor with elements `x[i] and y[i]`.

A few important gotchas here:

- Don't try to use `and`, `or` or `not` on tensors, since Python will try to coerce the tensors to booleans, and you'll get an exception.
- Remember about **operator precedence**! For instance, `v >= 0 & v <= 1` will actually throw an error because it's actually evaluated as `(v >= (0 & v)) <= 1` (because `&` has high precedence) and `0 & v` is not a valid operation. When in doubt, use parentheses to force the correct parsing: `(v >= 0) & (v <= 1)`.


### Tip (2/5) - `einops`

Einops is a useful library which we'll dive deeper with tomorrow. For now, the only important function you'll need to know is `einops.repeat`. This takes as arguments a tensor and a string, and returns a new tensor which has been repeated along the specified dimensions. For example, the following code shows how we can repeat a 2D tensor along the last dimension:

```python
x = t.randn(4, 3)
x_repeated = einops.repeat(x, 'a b -> a b c', c=2) # copies x along a new dimension at the end

assert x_repeated.shape == (4, 3, 2)
t.testing.assert_close(x_repeated[:, :, 0], x)
t.testing.assert_close(x_repeated[:, :, 1], x)
```


### Tip (3/5) - Logical Reductions

In plain Python, if you have a list of lists and want to know if any element in a row is `True`, you could use a list comprehension like `[any(row) for row in rows]`. The efficient way to do this in PyTorch is with `torch.any()` or equivalently the `.any()` method of a tensor, which accept the dimension to reduce over. Similarly, `torch.all()` or `.all()` method. Both of these methods accept a `dim` argument, which is the dimension to reduce over.

<details>
<summary>Aside - tensor methods</summary>

Most functions like `torch.any(tensor, ...)` (which take a tensor as first argument) have an equivalent tensor method `tensor.any(...)`. We'll see many more examples of functions like this as we go through the course.
</details>


### Tip (4/5) - Broadcasting

Broadcasting is what happens when you perform an operation on two tensors, and one is a smaller size, but is copied along the dimensions of the larger one in order to apply to it. There are some complicated broadcasting rules which we'll get into later in the course (you can also review the broadcasting section in the prerequisite material which comes before this chapter), but for our purposes the only thing you need to know is this: if you perform an operation on 2 tensors `A, B` where `A.shape == B.shape[-A.ndim:]` (i.e. `A` matches the last dimensions of `B`), then `A` will be copied along its leading dimensions until it has the same shape as `B`. For example:

```python
B = t.ones(4, 3, 2)
A = t.ones(3, 2)
C = A + B
print(C.shape) # torch.Size([4, 3, 2]), the size of the broadcasted tensor
print(C.max(), C.min()) # tensor(2.) tensor(2.), because all elements are 2
```


### Tip (5/5) - Indexing

Indexing is a pretty deep topic in PyTorch, and it takes a while to get fully comfortable with it. However, we'll specifically cover some features which will be useful for the following exercises.

**Using ellipses.** You can use an ellipsis `...` in an indexing expression to avoid repeated `:` and to write indexing expressions that work on varying numbers of input dimensions. For example, `x[..., 0]` is equivalent to `x[:, :, 0]` if `x` is 3D, and equivalent to `x[:, :, :, 0]` if `x` is 4D.

**Boolean indexing.** Boolean indexing allows you to select elements of a tensor based on a corresponding boolean tensor. Only the elements where the boolean value is True are selected. The following example shows boolean indexing *and* broadcasting:

```python
D = t.ones(2)  # Tensor with shape (2,)
E = t.zeros(3, 2)  # Tensor with shape (3, 2)
E[[True, False, True], :].shape  # Shape: (2, 2)
E[[True, False, True], :] = D  # Assign values from D to selected rows
print(E)
# output:
# tensor([[1., 1.],
#         [0., 0.],
#         [1., 1.]])
```

Note that `E` gets modified when `E[[True, False, True], :]` gets modified - this is because the latter is a **view** of the former, not a new tensor (i.e. it points to the same place in memory) - we'll look a bit more at this topic later.

**Multi-dimensional indexing.** You can also apply boolean indexing to multiple dimensions simultaneously. This allows you to select elements across several dimensions based on a boolean condition. The following example shows multi-dimensional boolean indexing *and* broadcasting:

```python
D = t.ones(2)  # Tensor with shape (2,)
F = t.zeros(2, 2, 2)  # Tensor with shape (2, 2, 2)
F[[[True, True], [False, True]], :].shape  # Shape: (3, 2)
F[[[True, True], [False, True]], :] = D
print(F)
# output:
# tensor([[[1., 1.],
#          [1., 1.]],

#         [[0., 0.],
#          [1., 1.]]])
```

This works because our indexing creates a tensor of shape `(3, 2)`, formed by stacking the three tensors `F[0, 0]`, `F[0, 1]` and `F[1, 1]` (those where the corresponding index value is True) along a new leading dimension.


### Summary of tips

> * Use `...` to avoid repeated `:` in indexing expressions
> * Use `&`, `|`, and `~` for elementwise logical operations on tensors
> * Use parentheses to force the correct operator precedence
> * Use `torch.any()` or `.any()` to do logical reductions (you can do this over a single dimension, with the `dim` argument)
> * Tensors can broadcast along leading dimensions to operate together
>   * e.g. `t.ones(2) + t.ones(3, 2)` works because the former tensor gets broadcasted to shape `(3, 2)`
> * We can index with boolean tensors to select multiple elements
>   * e.g. if `A.shape = (3, n1, n2, ...)` then `A[[True, False, True]]` has shape `(2, n1, n2, ...)` and contains the first & third rows of `A`
> * We can index with multi-dimensional boolean tensors too
>   * e.g. if `A.shape = (2, 2, n1, n2, ...)` then `A[[[True, True], [False, True]], :]` has shape `(3, n1, n2, ...)` and contains the elements `A[0, 0]`, `A[0, 1]` and `A[1, 1]`, stacked along a new leading dimension


## Batched Ray-Segment Intersection

We'll now move on to implementing a batched version of our previous function which takes multiple rays, multiple line segments, and returns a boolean for each ray indicating whether ***any*** segment intersects with that ray.

Note - in the batched version, we don't want the solver to throw an exception just because some of the equations don't have a solution - these should just return False.


### Exercise - implement `intersect_rays_1d`

> ```yaml
> Difficulty: 🔴🔴🔴🔴⚪
> Importance: 🔵🔵🔵🔵⚪
> 
> You should spend up to 25-40 minutes on this exercise.
> This will probably be one of the hardest exercises you'll complete today.
> ```

One part you might find difficult is dealing with the zero determinant cases. Previously we dealt with those by using `try / except`, but here we can't do that because we want to perform all the operations at once. Instead, we can use the following clever trick to find all the pairs of intersecting rays and segments:

1. Figure out which matrices have zero determinant (e.g. with `determinants.abs() < 1e-8`)
2. Replace those matrices with the identity matrix `t.eye(2)`, since this will certainly not raise an error when solving
3. Find the matrices s.t. `u, v` are in the required range **and** our original matrix was non-singular

This way, we've identified all pairs of rays and segments where an intersection point exists **and** that intersection point is valid (i.e. it's actually on the positive side of the ray, and somewhere in the middle of the segment).

Once we have this 2D array of booleans representing whether each ray intersects with each segment, we can reduce using the torch function `t.any` to find the rays which intersect *any* segment.


```python
def intersect_rays_1d(
    rays: Float[Tensor, "nrays 2 3"], segments: Float[Tensor, "nsegments 2 3"]
) -> Bool[Tensor, " nrays"]:
    """
    For each ray, return True if it intersects any segment.
    """
    raise NotImplementedError()


tests.test_intersect_rays_1d(intersect_rays_1d)
tests.test_intersect_rays_1d_special_case(intersect_rays_1d)
```


<details>
<summary>Help - I don't know how to set all my matrices to the identity</summary>

You should have some variable `mat` which is a batch of matrices, i.e. it has shape `(n_rays, n_segments, 2, 2)`. You can then define `is_singular` as a boolean tensor of shape `(n_rays, n_segments)` which is true wherever the matrix is singular. Now, indexing `mat[is_singular]` returns a tensor of shape `(N, 2, 2)` where the `[i, :, :]`-th element is the `i`-th singular matrix. Thanks to broadcasting rules, you can set `mat[is_singular] = t.eye(2)`, and the identity matrix with shape `(2, 2)` will get broadcasted to the left hand shape `(N, 2, 2)`.

</details>


<details><summary>Solution</summary>

```python
def intersect_rays_1d(
    rays: Float[Tensor, "nrays 2 3"], segments: Float[Tensor, "nsegments 2 3"]
) -> Bool[Tensor, " nrays"]:
    """
    For each ray, return True if it intersects any segment.
    """
    NR = rays.size(0)
    NS = segments.size(0)

    # Get just the x and y coordinates
    rays = rays[..., :2]
    segments = segments[..., :2]

    # Repeat rays and segments so that we can compuate the intersection of every (ray, segment) pair
    rays = einops.repeat(rays, "nrays p d -> nrays nsegments p d", nsegments=NS)
    segments = einops.repeat(segments, "nsegments p d -> nrays nsegments p d", nrays=NR)

    # Each element of `rays` is [[Ox, Oy], [Dx, Dy]]
    O = rays[:, :, 0]
    D = rays[:, :, 1]
    assert O.shape == (NR, NS, 2)

    # Each element of `segments` is [[L1x, L1y], [L2x, L2y]]
    L_1 = segments[:, :, 0]
    L_2 = segments[:, :, 1]
    assert L_1.shape == (NR, NS, 2)

    # Define matrix on left hand side of equation
    mat = t.stack([D, L_1 - L_2], dim=-1)
    # Get boolean of where matrix is singular, and replace it with the identity in these positions
    dets = t.linalg.det(mat)
    is_singular = dets.abs() < 1e-8
    assert is_singular.shape == (NR, NS)
    mat[is_singular] = t.eye(2)

    # Define vector on the right hand side of equation
    vec = L_1 - O

    # Solve equation, get results
    sol = t.linalg.solve(mat, vec)
    u = sol[..., 0]
    v = sol[..., 1]

    # Return boolean of (matrix is nonsingular, and soln is in correct range implying intersection)
    return ((u >= 0) & (v >= 0) & (v <= 1) & ~is_singular).any(dim=-1)
```
</details>


## Using GPT to understand code

*Note, the world of LLMs moves fast, so this section is likely to get out of date at some point!*

Next week we'll start learning about transformers and how to build them, but it's not too early to start using them to accelerate your own learning!

We'll be discussing more advanced ways to use GPT 3 and 4 as coding partners / research assistants in the coming weeks, but for now we'll look at a simple example: **using GPT to understand code**. You're recommended to read the recent [LessWrong post](https://www.lesswrong.com/posts/ptY6X3BdW4kgqpZFo/using-gpt-4-to-understand-code) by Siddharth Hiregowdara in which he explains his process. This works best on GPT-4, but I've found GPT-3.5 works equally well for reasonably straightforward problems (see the section below).

Firstly, you should get an account to use GPT with if you haven't already. Next, try asking GPT-3.5 / 4 for an explanation of the function above. You can do this e.g. via the following prompt:

> Explain this Python function, line by line. You should break up your explanation by inserting sections of the code.
> 
> ```python
> def intersect_rays_1d(rays: Float[Tensor, "nrays 2 3"], segments: Float[Tensor, "nsegments 2 3"]) -> Bool[Tensor, " nrays"]:
>     NR = rays.size(0)
>     NS = segments.size(0)
>     rays = rays[..., :2]
>     ...
> ```

I've found removing comments is often more helpful, because then GPT will answer in its own words rather than just repeating the comments (and the comments can sometimes confuse it).

Once you've got a response, here are a few more things you might want to consider asking:

* Can you suggest ways to improve the code?
    * GPT-4 recommended using a longer docstring and more descriptive variable names, among other things.
* Can you explain why the line `mat[is_singular] = t.eye(2)` works?
    * GPT-4 gave me a correct and very detailed explanation involving broadcasting and tensor shapes.

Is using GPT in this way cheating? It can be, if your first instinct is to jump to GPT rather than trying to understand the code yourself. But it's important here to bring up the distinction of [playing in easy mode](https://www.lesswrong.com/posts/nJPtHHq6L7MAMBvRK/play-in-easy-mode) vs [playing in hard mode](https://www.lesswrong.com/posts/7hLWZf6kFkduecH2g/play-in-hard-mode). There are situations where it's valuable for you to think about a problem for a while before moving forward because that deliberation will directly lead to you becoming a better researcher or engineer (e.g. when you're thinking of a hypothesis for how a circuit works while doing mechanistic interpretability on a transformer, or you're pondering which datastructure best fits your use case while implementing some RL algorithm). But there are also situations (like this one) where you'll get more value from speedrunning towards an understanding of certain code or concepts, and apply your understanding in subsequent exercises. It's important to find a balance!

#### When to use GPT-3.5 and GPT-4

GPT-3.5 and 4 both have advantages and disadvantages in different situations. GPT-3.5 has a large advantage in speed over GPT-4, and works equally well on simple problems or functions. If it's anything that Copilot is capable of writing, then you're likely better off using it instead of GPT-4.

On the other hand, GPT-4 has an advantage at generating coherent code (although we don't expect you to be using it for code generation much at this stage in the program), and is generally better at responding to complex tasks with less prompt engineering.

#### Additional notes on using GPT (from Joseph Bloom)

* ChatGPT is overly friendly. If you give it bad code it won't tell you it's shit so you need to encourage it to give feedback and/or show you examples of great code. Especially for beginner coders using it, it's important to realise how *under* critical it is.
* GPT is great at writing tests (asking it to write a test for a function is often better than asking it if a function is correct), refactoring code (identifying repeated tasks and extracting them) and naming variables well. These are specific things worth doing a few times to see how useful they can be.
* GPT-4 does well with whole modules/scripts so don't hesitate to add those. When you start managing repos on GitHub, use tracked files so that when you copy-paste edited code back, all the changes are highlighted for you as if you'd made them. (VSCode highlights changes with small blue bars next to the line numbers in your python files.)

Here are some things you can play around with:

* Ask GPT it to write tests for the function. You can give more specific instructions (e.g. asking it to use / not to use the `unittests` library, or to print more informative error messages).
* Ask GPT how to refactor the function above. (When I did this, it suggested splitting the function up into subfunctions which performed the discrete tasks of "compute intersection points")


## 2D Rays

Now we're going to make use of the z dimension and have rays emitted from the origin in both y and z dimensions.


### Exercise - implement `make_rays_2d`

> ```yaml
> Difficulty: 🔴🔴🔴⚪⚪
> Importance: 🔵🔵⚪⚪⚪
> 
> You should spend up to 10-20 minutes on this exercise.
> ```

Implement `make_rays_2d` analogously to `make_rays_1d`. The result should look like a pyramid with the tip at the origin.


```python
def make_rays_2d(num_pixels_y: int, num_pixels_z: int, y_limit: float, z_limit: float) -> Float[Tensor, "nrays 2 3"]:
    """
    num_pixels_y: The number of pixels in the y dimension
    num_pixels_z: The number of pixels in the z dimension

    y_limit: At x=1, the rays should extend from -y_limit to +y_limit, inclusive of both.
    z_limit: At x=1, the rays should extend from -z_limit to +z_limit, inclusive of both.

    Returns: shape (num_rays=num_pixels_y * num_pixels_z, num_points=2, num_dims=3).
    """
    raise NotImplementedError()


rays_2d = make_rays_2d(10, 10, 0.3, 0.3)
render_lines_with_plotly(rays_2d)
```


<details><summary>Click to see the expected output</summary>

<div style="text-align: left"><embed src="https://info-arena.github.io/ARENA_img/misc/media-01/0102.html" width="620" height="620"></div>

</details>


<details>
<summary>Help - I'm not sure how to implement this function.</summary>

Don't write it as a function right away. The most efficient way is to write and test each line individually in the REPL to verify it does what you expect before proceeding.

You can either build up the output tensor using `torch.stack`, or you can initialize the output tensor to its final size and then assign to slices like `rays[:, 1, 1] = ...`. It's good practice to be able to do it both ways.

Each y coordinate needs a ray with each corresponding z coordinate - in other words this is an outer product. The most elegant way to do this is with two calls to `einops.repeat`. You can also accomplish this with `unsqueeze`, `expand`, and `reshape` combined.
</details>


<details><summary>Solution</summary>

```python
def make_rays_2d(num_pixels_y: int, num_pixels_z: int, y_limit: float, z_limit: float) -> Float[Tensor, "nrays 2 3"]:
    """
    num_pixels_y: The number of pixels in the y dimension
    num_pixels_z: The number of pixels in the z dimension

    y_limit: At x=1, the rays should extend from -y_limit to +y_limit, inclusive of both.
    z_limit: At x=1, the rays should extend from -z_limit to +z_limit, inclusive of both.

    Returns: shape (num_rays=num_pixels_y * num_pixels_z, num_points=2, num_dims=3).
    """
    n_pixels = num_pixels_y * num_pixels_z
    ygrid = t.linspace(-y_limit, y_limit, num_pixels_y)
    zgrid = t.linspace(-z_limit, z_limit, num_pixels_z)
    rays = t.zeros((n_pixels, 2, 3), dtype=t.float32)
    rays[:, 1, 0] = 1
    rays[:, 1, 1] = einops.repeat(ygrid, "y -> (y z)", z=num_pixels_z)
    rays[:, 1, 2] = einops.repeat(zgrid, "z -> (y z)", y=num_pixels_y)
    return rays
```
</details>




=== NEW CHAPTER ===


# 3️⃣ Triangles



> ##### Learning Objectives
>
> - Understand how to parametrize triangles in 2D and 3D, and solve for their intersection with rays
> - Put everything together, to render your mesh as a 2D image

## Triangle Coordinates

The area inside a triangle can be defined by three (non-collinear) points $A$, $B$ and $C$, and can be written algebraically as a **convex combination** of those three points:

$$
\begin{align*}
P(w, u, v) &= wA + uB + vC \quad\quad \\
    \\
s.t. \quad 0 &\leq w,u,v \\
1 &= w + u + v
\end{align*}
$$

Or equivalently:

$$
\begin{align*}
\quad\quad\quad\quad P(u, v) &= (1 - u - v)A + uB + vC \\
&= A + u(B - A) + v(C - A) \\
\\
s.t. \quad 0 &\leq u,v \\
u + v &\leq 1
\end{align*}
$$

These $u, v$ are called "barycentric coordinates".

If we remove the bounds on $u$ and $v$, we get an equation for the plane containing the triangle. Play with the widget to understand the behavior of $u, v$.


```python
one_triangle = t.tensor([[0, 0, 0], [4, 0.5, 0], [2, 3, 0]])
A, B, C = one_triangle
x, y, z = one_triangle.T

fig: go.FigureWidget = setup_widget_fig_triangle(x, y, z)
display(fig)


@interact(u=(-0.5, 1.5, 0.01), v=(-0.5, 1.5, 0.01))
def update(u=0.0, v=0.0):
    P = A + u * (B - A) + v * (C - A)
    fig.update_traces({"x": [P[0]], "y": [P[1]]}, 2)
```


<div style="text-align: left"><embed src="https://info-arena.github.io/ARENA_img/misc/media-01/animation-1b.mp4" width="420" height="450" style="background-color: white;"></div>


### Triangle-Ray Intersection

Given a ray with origin $O$ and direction $D$, our intersection algorithm will consist of two steps:

- Finding the intersection between the line and the plane containing the triangle, by solving the equation $P(u, v) = P(s)$;
- Checking if $u$ and $v$ are within the bounds of the triangle.

Expanding the equation $P(u, v) = P(s)$, we have:

$$
\begin{align*}
A + u(B - A) + v(C - A) &= O + sD \\
\Rightarrow
\begin{pmatrix}
    -D & (B - A) & (C - A) \\
\end{pmatrix}
\begin{pmatrix}
    s \\
    u \\
    v  
\end{pmatrix}
&= \begin{pmatrix} O - A \end{pmatrix} \\
\Rightarrow \begin{pmatrix}
    -D_x & (B - A)_x & (C - A)_x \\
    -D_y & (B - A)_y & (C - A)_y \\
    -D_z & (B - A)_z & (C - A)_z \\
\end{pmatrix}
\begin{pmatrix}
    s \\
    u \\
    v  
\end{pmatrix} &= \begin{pmatrix}
    (O - A)_x \\
    (O - A)_y \\
    (O - A)_z \\
\end{pmatrix}
\end{align*}
$$

$$
$$

We can therefore find the coordinates `s`, `u`, `v` of the intersection point by solving the linear system above.


### Exercise - implement `triangle_ray_intersects`

> ```yaml
> Difficulty: 🔴🔴🔴⚪⚪
> Importance: 🔵🔵🔵⚪⚪
> 
> You should spend up to 15-20 minutes on this exercise.
> ```

Using `torch.linalg.solve` and `torch.stack`, implement `triangle_ray_intersects(A, B, C, O, D)`.

A few tips:

* If you have a 0-dimensional tensor with shape `()` containing a single value, use the `item()` method to convert it to a plain Python value.
* If you have a tensor of shape `tensor.shape = (3, ...)`, then you can unpack it along the first dimension into three separate tensors the same way that you'd unpack a normal python list: `s, u, v = tensor`.
    * Note - if the dimension you want to unpack isn't at the start, a nice alternative is `s, u, v = tensor.unbind(dim)`, which does the same thing but along the dimension given by `dim` rather than the first dimension.
* If your function isn't working, try making a simple ray and triangle with nice round numbers where you can work out manually if it should intersect or not, then debug from there.


```python
Point = Float[Tensor, "points=3"]


def triangle_ray_intersects(A: Point, B: Point, C: Point, O: Point, D: Point) -> bool:
    """
    A: shape (3,), one vertex of the triangle
    B: shape (3,), second vertex of the triangle
    C: shape (3,), third vertex of the triangle
    O: shape (3,), origin point
    D: shape (3,), direction point

    Return True if the ray and the triangle intersect.
    """
    raise NotImplementedError()


tests.test_triangle_ray_intersects(triangle_ray_intersects)
```


<details><summary>Solution</summary>

```python
def triangle_ray_intersects(A: Point, B: Point, C: Point, O: Point, D: Point) -> bool:
    """
    A: shape (3,), one vertex of the triangle
    B: shape (3,), second vertex of the triangle
    C: shape (3,), third vertex of the triangle
    O: shape (3,), origin point
    D: shape (3,), direction point

    Return True if the ray and the triangle intersect.
    """
    s, u, v = t.linalg.solve(t.stack([-D, B - A, C - A], dim=1), O - A)
    return ((s >= 0) & (u >= 0) & (v >= 0) & (u + v <= 1)).item()
```
</details>


## Single-Triangle Rendering

Implement `raytrace_triangle` using only one call to `torch.linalg.solve`.

Reshape the output and visualize with `plt.imshow`. It's normal for the edges to look pixelated and jagged - using a small number of pixels is a good way to debug quickly.

If you think it's working, increase the number of pixels and verify that it looks less pixelated at higher resolution.


### Views and Copies

It's critical to know when you are making a copy of a `Tensor`, versus making a view of it that shares the data with the original tensor. It's preferable to use a view whenever possible to avoid copying memory unnecessarily. On the other hand, modifying a view modifies the original tensor which can be unintended and surprising. Consult [the documentation](https://pytorch.org/docs/stable/tensor_view.html) if you're unsure if a function returns a view. A short reference of common functions:

- `torch.expand`: always returns a view
- `torch.view`: always returns a view
- `torch.detach`: always returns a view
- `torch.repeat`: always copies
- `torch.clone`: always copies
- `torch.flip`: always copies (different than numpy.flip which returns a view)
- `torch.tensor`: always copies, but PyTorch recommends using `.clone().detach()` instead.
- `torch.Tensor.contiguous`: returns self if possible, otherwise a copy
- `torch.transpose`: returns a view if possible, otherwise (sparse tensor) a copy
- `torch.reshape`: returns a view if possible, otherwise a copy
- `torch.flatten`: returns a view if possible, otherwise a copy (different than numpy.flatten which returns a copy)
- `einops.repeat`: returns a view if possible, otherwise a copy
- `einops.rearrange`: returns a view if possible, otherwise a copy
- Basic indexing returns a view, while advanced indexing returns a copy.


### Storage Objects

Calling `storage()` on a `Tensor` returns a Python object wrapping the underlying C++ array. This array is 1D regardless of the dimensionality of the `Tensor`. This allows you to look inside the `Tensor` abstraction and see how the actual data is laid out in RAM.

Note that a new Python wrapper object is generated each time you call `storage()`, and both `x.storage() == x.storage()` and `x.storage() is x.storage()` evaluates to False.

If you want to check if two `Tensor`s share an underlying C++ array, you can compare their `storage().data_ptr()` fields. This can be useful for debugging.


### `Tensor._base`

If `x` is a view, you can access the original `Tensor` with `x._base`. This is an undocumented internal feature that's useful to know. Consider the following code:

```python
x = t.zeros(1024*1024*1024)
y = x[0]
del x
```

Here, `y` was created through basic indexing, so `y` is a view and `y._base` refers to `x`. This means `del x` won't actually deallocate the 4GB of memory, and that memory will remain in use which can be quite surprising. `y = x[0].clone()` would be an alternative here that does allow reclaiming the memory.


### Exercise - implement `raytrace_triangle`

> ```yaml
> Difficulty: 🔴🔴🔴🔴⚪
> Importance: 🔵🔵🔵🔵⚪
> 
> You should spend up to 15-20 minutes on this exercise.
> This is about as hard as `intersect_rays_1d`, although hopefully you should find it more familiar.
> ```

Below, you should implement `raytrace_triangle`, a funtion which checks whether each ray in `ray` intersects a single given triangle.


```python
def raytrace_triangle(
    rays: Float[Tensor, "nrays rayPoints=2 dims=3"],
    triangle: Float[Tensor, "trianglePoints=3 dims=3"],
) -> Bool[Tensor, " nrays"]:
    """
    For each ray, return True if the triangle intersects that ray.
    """
    raise NotImplementedError()


A = t.tensor([1, 0.0, -0.5])
B = t.tensor([1, -0.5, 0.0])
C = t.tensor([1, 0.5, 0.5])
num_pixels_y = num_pixels_z = 15
y_limit = z_limit = 0.5

# Plot triangle & rays
test_triangle = t.stack([A, B, C], dim=0)
rays2d = make_rays_2d(num_pixels_y, num_pixels_z, y_limit, z_limit)
triangle_lines = t.stack([A, B, C, A, B, C], dim=0).reshape(-1, 2, 3)
render_lines_with_plotly(rays2d, triangle_lines)

# Calculate and display intersections
intersects = raytrace_triangle(rays2d, test_triangle)
img = intersects.reshape(num_pixels_y, num_pixels_z).int()
imshow(img, origin="lower", width=600, title="Triangle (as intersected by rays)")
```


<details><summary>Click to see the expected output</summary>

<div style="text-align: left"><embed src="https://info-arena.github.io/ARENA_img/misc/media-01/0103.html" width="620" height="620"></div><br>
<div style="text-align: left"><embed src="https://info-arena.github.io/ARENA_img/misc/media-01/0104.html" width="620" height="620"></div>

</details>


<details><summary>Solution</summary>

```python
def raytrace_triangle(
    rays: Float[Tensor, "nrays rayPoints=2 dims=3"],
    triangle: Float[Tensor, "trianglePoints=3 dims=3"],
) -> Bool[Tensor, " nrays"]:
    """
    For each ray, return True if the triangle intersects that ray.
    """
    NR = rays.size(0)

    # Triangle is [[Ax, Ay, Az], [Bx, By, Bz], [Cx, Cy, Cz]]
    A, B, C = einops.repeat(triangle, "pts dims -> pts NR dims", NR=NR)
    assert A.shape == (NR, 3)

    # Each element of `rays` is [[Ox, Oy, Oz], [Dx, Dy, Dz]]
    O, D = rays.unbind(dim=1)
    assert O.shape == (NR, 3)

    # Define matrix on left hand side of equation
    mat: Float[Tensor, "NR 3 3"] = t.stack([-D, B - A, C - A], dim=-1)

    # Get boolean of where matrix is singular, and replace it with the identity in these positions
    # Note - this works because mat[is_singular] has shape (NR_where_singular, 3, 3), so we
    # can broadcast the identity matrix to that shape.
    dets: Float[Tensor, "NR"] = t.linalg.det(mat)
    is_singular = dets.abs() < 1e-8
    mat[is_singular] = t.eye(3)

    # Define vector on the right hand side of equation
    vec = O - A

    # Solve eqns
    sol: Float[Tensor, "NR 3"] = t.linalg.solve(mat, vec)
    s, u, v = sol.unbind(dim=-1)

    # Return boolean of (matrix is nonsingular) && (solution is in correct range implying intersection)
    return (s >= 0) & (u >= 0) & (v >= 0) & (u + v <= 1) & ~is_singular
```
</details>


## Debugging


Debugging code is an extremely important thing to learn. Just like using GPT to assist your coding, it's something that can significantly speedrun your development, and stop you getting hung up on all the frustrating things!

To give you practice debugging using VSCode's built-in debugger\*, we've provided an example function below. This is an implementation of `raytrace_triangle` which has a few mistakes in it. Your task is to use the debugger to find the mistake and fix it. (Note - you're encouraged to actually use the debugger, rather than comparing it to the solution above!)


<details>
<summary>Incorrect function</summary>

```python
def raytrace_triangle_with_bug(
    rays: Float[Tensor, "nrays rayPoints=2 dims=3"],
    triangle: Float[Tensor, "trianglePoints=3 dims=3"]
) -> Bool[Tensor, " nrays"]:
    '''
    For each ray, return True if the triangle intersects that ray.
    '''
    NR = rays.size[0]

    A, B, C = einops.repeat(triangle, "pts dims -> pts NR dims", NR=NR)

    O, D = rays.unbind(-1)

    mat = t.stack([- D, B - A, C - A])
    
    dets = t.linalg.det(mat)
    is_singular = dets.abs() < 1e-8
    mat[is_singular] = t.eye(3)

    vec = O - A

    sol = t.linalg.solve(mat, vec)
    s, u, v = sol.unbind(dim=-1)

    return ((u >= 0) & (v >= 0) & (u + v <= 1) & ~is_singular)


intersects = raytrace_triangle_with_bug(rays2d, test_triangle)
img = intersects.reshape(num_pixels_y, num_pixels_z).int()
imshow(img, origin="lower", width=600, title="Triangle (as intersected by rays)")
```
</details>


You can debug a cell by clicking on the **Debug cell** option at the bottom of your cell. Your cell should contain the code that is actually run to cause an error (rather than needing to contain the function which is the source of the error). Before you run your debugger, you can set breakpoints by clicking on the left-hand side of the line number (a red dot will appear). You can then step through your code, using the toolbar of buttons which will appear when you run the debugger (see [here](https://pawelgrzybek.com/continue-step-over-step-into-and-step-out-actions-in-visual-studio-code-debugger-explained/) for an explanation of what each of the buttons does). When you reach a breakpoint, you can use the following tools:

* Inspect local and global variables, in the **VARIABLES** window that appears on the left sidebar.
* Add variables expressions to watch, in the **WATCH** window that appears on the left sidebar.
    * You can just type in any expression here, e.g. the type of a variable or the length of a list, and this will update as you step through the function.
* Evaluate expressions on a one-time basis, by typing them into the **DEBUG CONSOLE** (which appears at the bottom of the screen)

Note, when you run the debugger, it will stop *before* the breakpoint line is evaluated. So if you've run a cell and got an error on a specific line, then *that* is the line you want to set a breakpoint on.

*This all works basically the same if you're in a notebook in VSCode, except for a few changes e.g. the debug button is on the dropdown at the top-left of the cell (if it doesn't appear for you then you'll need to go into user settings and add the line `"notebook.consolidatedRunButton": true`).*

There's much more detail we could go into about debugging, but this will suffice for most purposes. It's generally a much more efficient way of debugging than using print statements or asserts (although these can also be helpful in some situations).


<details>
<summary>Answer - what are the bugs, and how can they be fixed?</summary>

```python
NR = rays.size[0]
```

This should be `rays.size(0)` (or equivalently, `rays.shape[0]`). `size` is a method which takes an int and returns the size of that dimension; `shape` returns a `torch.Size` object which can be indexed into.

This would have been pretty easy to realise without using the debugger, because the error message is informative.

```python
O, D = rays.unbind(-1)
```

We're unbinding from the wrong dimension. `rays` has shape `(nrays, points=2, dims=3)`, and we actually want to unbind along the `points` dimension. So we should use `rays.unbind(1)`.

We could have found this by inspecting the `rays` object in the variables pane (you can click on the dropdown next to the variable name to look at its attributes, including `shape`), or you could just type `rays.shape` into the debug console. However, this error should also have been apparent given the type signature of the function (a good case for using typing!).

```python
mat = t.stack([- D, B - A, C - A])
```

This should have had the argument `dim=-1` on the end, because `torch.stack` by default stacks along the first dimension.

This error is a bit harder to diagnose, because the line causing an error is after the line containing the mistake. Again, we could have diagnosed this with the debugger by inspecting the shape of our `mat` tensor in the variables pane.

---

These were all relatively easy bugs to diagnose (not all bugs will present as actual errors in your code, some might just be an unexpected set of results). But hopefully this has given you a sense for how to use the debugger. It's a very powerful tool, and can save you a lot of time!
</details>


\**If you're using Colab, you'll have to use different strategies for debugging. See [this page](https://zohaib.me/debugging-in-google-collab-notebook/) for one suggested approach.*


## Mesh Loading

Use the given code to load the triangles for your Pikachu. By convention, files written with `torch.save` end in the `.pt` extension, but these are actually just zip files.


```python
triangles = t.load(section_dir / "pikachu.pt", weights_only=True)
```


## Mesh Rendering

For our purposes, a mesh is just a group of triangles, so to render it we'll intersect all rays and all triangles at once. We previously just returned a boolean for whether a given ray intersects the triangle, but now it's possible that more than one triangle intersects a given ray.

For each ray (pixel) we will return a float representing the minimum distance to a triangle if applicable, otherwise the special value `float('inf')` representing infinity. We won't return which triangle was intersected for now.

Note - by distance to a triangle, we specifically mean **distance along the x-dimension**, not Euclidean distance.


### Exercise - implement `raytrace_mesh`

> ```yaml
> Difficulty: 🔴🔴🔴⚪⚪
> Importance: 🔵🔵🔵🔵⚪
> 
> You should spend up to 20-25 minutes on this exercise.
> 
> This is the main function we've been building towards, and marks the end of the core exercises. If should involve a lot of repurposed code from the last excercise.
> ```

Implement `raytrace_mesh` and as before, reshape and visualize the output. Your Pikachu is centered on (0, 0, 0), so you'll want to slide the ray origin back to at least `x=-2` to see it properly.

Reminder - `t.linalg.solve` (and most batched operations) can accept multiple dimensions as being batch dims. Previously, you've just used `NR` (the number of rays) as the batch dimension, but you can also use `(NR, NT)` (the number of rays and triangles) as your batch dimensions, so you can solve for all rays and triangles at once.


```python
def raytrace_mesh(
    rays: Float[Tensor, "nrays rayPoints=2 dims=3"],
    triangles: Float[Tensor, "ntriangles trianglePoints=3 dims=3"],
) -> Float[Tensor, " nrays"]:
    """
    For each ray, return the distance to the closest intersecting triangle, or infinity.
    """
    raise NotImplementedError()


num_pixels_y = 120
num_pixels_z = 120
y_limit = z_limit = 1

rays = make_rays_2d(num_pixels_y, num_pixels_z, y_limit, z_limit)
rays[:, 0] = t.tensor([-2, 0.0, 0.0])
dists = raytrace_mesh(rays, triangles)
intersects = t.isfinite(dists).view(num_pixels_y, num_pixels_z)
dists_square = dists.view(num_pixels_y, num_pixels_z)
img = t.stack([intersects, dists_square], dim=0)

fig = px.imshow(img, facet_col=0, origin="lower", color_continuous_scale="magma", width=1000)
fig.update_layout(coloraxis_showscale=False)
for i, text in enumerate(["Intersects", "Distance"]):
    fig.layout.annotations[i]["text"] = text
fig.show()
```


<details><summary>Click to see the expected output</summary>

<iframe src="https://info-arena.github.io/ARENA_img/misc/media-01/0105.html" width="1020" height="620"></iframe>

</details>


<details><summary>Solution</summary>

```python
def raytrace_mesh(
    rays: Float[Tensor, "nrays rayPoints=2 dims=3"],
    triangles: Float[Tensor, "ntriangles trianglePoints=3 dims=3"],
) -> Float[Tensor, " nrays"]:
    """
    For each ray, return the distance to the closest intersecting triangle, or infinity.
    """
    NR = rays.size(0)
    NT = triangles.size(0)

    # Each triangle is [[Ax, Ay, Az], [Bx, By, Bz], [Cx, Cy, Cz]]
    triangles = einops.repeat(triangles, "NT pts dims -> pts NR NT dims", NR=NR)
    A, B, C = triangles
    assert A.shape == (NR, NT, 3)

    # Each ray is [[Ox, Oy, Oz], [Dx, Dy, Dz]]
    rays = einops.repeat(rays, "NR pts dims -> pts NR NT dims", NT=NT)
    O, D = rays
    assert O.shape == (NR, NT, 3)

    # Define matrix on left hand side of equation
    mat: Float[Tensor, "NR NT 3 3"] = t.stack([-D, B - A, C - A], dim=-1)
    # Get boolean of where matrix is singular, and replace it with the identity in these positions
    dets: Float[Tensor, "NR NT"] = t.linalg.det(mat)
    is_singular = dets.abs() < 1e-8
    mat[is_singular] = t.eye(3)

    # Define vector on the right hand side of equation
    vec: Float[Tensor, "NR NT 3"] = O - A

    # Solve eqns (note, s is the distance along ray)
    sol: Float[Tensor, "NR NT 3"] = t.linalg.solve(mat, vec)
    s, u, v = sol.unbind(-1)

    # Scale s by Dx to get the distance along ray
    s *= D[..., 0]

    # Get boolean of intersects, and use it to set distance = infinity when there is no intersection
    intersects = (u >= 0) & (v >= 0) & (u + v <= 1) & ~is_singular
    s[~intersects] = float("inf")  # t.inf

    # Get the minimum distance (over all triangles) for each ray
    return einops.reduce(s, "NR NT -> NR", "min")


num_pixels_y = 120
num_pixels_z = 120
y_limit = z_limit = 1

rays = make_rays_2d(num_pixels_y, num_pixels_z, y_limit, z_limit)
rays[:, 0] = t.tensor([-2, 0.0, 0.0])
dists = raytrace_mesh(rays, triangles)
intersects = t.isfinite(dists).view(num_pixels_y, num_pixels_z)
dists_square = dists.view(num_pixels_y, num_pixels_z)
img = t.stack([intersects, dists_square], dim=0)

fig = px.imshow(img, facet_col=0, origin="lower", color_continuous_scale="magma", width=1000)
fig.update_layout(coloraxis_showscale=False)
for i, text in enumerate(["Intersects", "Distance"]):
    fig.layout.annotations[i]["text"] = text
fig.show()
```
</details>


Congratulations, you've now got to the end of the exercises! Read on for some more bonus material.




=== NEW CHAPTER ===


# 4️⃣ Video & Lighting



> ##### Learning Objectives
>
> - Learn how surface normal vectors can be used to compute lighting effects
> - Render your figures in video form (as an animated camera pan)
> - (optional) Learn about the `pytest` library, and write your own tests for the functions you wrote

Here, we've included some more raytracing exercises, which extend the previous animation by providing video and lighting.


### Exercise - rotation matrix

> ```yaml
> Difficulty: 🔴🔴⚪⚪⚪
> Importance: 🔵🔵🔵⚪⚪
> 
> You should spend up to 10-15 minutes on this exercise.
> ```

Below is some code to iterate through a range of angles, rotating the pikachu model around the y-axis and raytracing the mesh at each angle. These frames are then concatenated together and animated into some dramatic footage! Your job is to fill in the `rotation_matrix` function, which should give you a matrix that rotates counterclockwise around the y-axis by a given angle `theta` (which is a scalar tensor). If you're stuck, see [this Wikipedia page](https://en.wikipedia.org/wiki/Rotation_matrix#Basic_3D_rotations) on basic 3D rotations.


```python
def rotation_matrix(theta: Float[Tensor, ""]) -> Float[Tensor, "rows cols"]:
    """
    Creates a rotation matrix representing a counterclockwise rotation of `theta` around the y-axis.
    """
    raise NotImplementedError()


tests.test_rotation_matrix(rotation_matrix)
```


<details><summary>Solution</summary>

```python
def rotation_matrix(theta: Float[Tensor, ""]) -> Float[Tensor, "rows cols"]:
    """
    Creates a rotation matrix representing a counterclockwise rotation of `theta` around the y-axis.
    """
    return t.tensor(
        [
            [t.cos(theta), 0.0, t.sin(theta)],
            [0.0, 1.0, 0.0],
            [-t.sin(theta), 0.0, t.cos(theta)],
        ]
    )
```
</details>


Once you've passed the tests, you can run the code below to create an animation! It might take a while to run, but should be no longer than 2 minutes.


```python
def raytrace_mesh_video(
    rays: Float[Tensor, "nrays points dim"],
    triangles: Float[Tensor, "ntriangles points dims"],
    rotation_matrix: Callable[[float], Float[Tensor, "rows cols"]],
    raytrace_function: Callable,
    num_frames: int,
) -> Bool[Tensor, "nframes nrays"]:
    """
    Creates a stack of raytracing results, rotating the triangles by `rotation_matrix` each frame.
    """
    result = []
    theta = t.tensor(2 * t.pi) / num_frames
    R = rotation_matrix(theta)
    for theta in tqdm(range(num_frames)):
        triangles = triangles @ R
        result.append(raytrace_function(rays, triangles))
        t.cuda.empty_cache()  # clears GPU memory (this line will be more important later on!)
    return t.stack(result, dim=0)


def display_video(distances: Float[Tensor, "frames y z"]):
    """
    Displays video of raytracing results, using Plotly. `distances` is a tensor where the [i, y, z]
    element is distance to the closest triangle for the i-th frame & the [y, z]-th ray in our 2D
    grid of rays.
    """
    px.imshow(
        distances,
        animation_frame=0,
        origin="lower",
        zmin=0.0,
        zmax=distances[distances.isfinite()].quantile(0.99).item(),
        color_continuous_scale="viridis_r",  # "Brwnyl"
    ).update_layout(coloraxis_showscale=False, width=550, height=600, title="Raytrace mesh video").show()


num_pixels_y = 250
num_pixels_z = 250
y_limit = z_limit = 0.8
num_frames = 50

rays = make_rays_2d(num_pixels_y, num_pixels_z, y_limit, z_limit)
rays[:, 0] = t.tensor([-3.0, 0.0, 0.0])
dists = raytrace_mesh_video(rays, triangles, rotation_matrix, raytrace_mesh, num_frames)
dists = einops.rearrange(dists, "frames (y z) -> frames y z", y=num_pixels_y)

display_video(dists)
```


<details><summary>Click to see the expected output</summary>

<div style="text-align: left"><embed src="https://info-arena.github.io/ARENA_img/misc/media-01/0106.html" width="570" height="620"></div>

</details>


### Exercise - use GPUs

> ```yaml
> Difficulty: 🔴⚪⚪⚪⚪
> Importance: 🔵🔵🔵⚪⚪
> 
> You should spend up to 10-15 minutes on this exercise.
> ```

We'll discuss GPUs a lot more in later sections and exercises. For now, One last thing to discuss before we move onto training our model: **GPUs**. Essentially, the GPU (graphics processing unit) is a specialized processor for rendering graphics and doing other kinds of parallel processing. Although we are actually using it for graphics in this section, it's much better known today for its role in deep learning, since it allows for efficient parallelized computations.

When you create a tensor, by default it's located on the CPU. You can use the `to` method to move your tensor between devices, e.g. `x = x.to("cuda")` to move to the GPU, and `x = x.to("cpu")` to move back to the CPU (or `x = x.cuda()` and `x = x.cpu()` as a shorthand). **CUDA** stands for Compute Unified Device Architecture, a parallel computing platform and programming model developed by NVIDIA which is supported by PyTorch. Note that this method returns a copy of the tensor rather than the tensor itself (unless the `to` command doesn't change its device). You can check whether CUDA is available by calling `t.cuda.is_available()` - if it's not, you can try installing a CUDA-supporting version of PyTorch from the [homepage](https://pytorch.org/).

Below, you should write the `raytrace_mesh_gpu` function to be identical to `raytrace_mesh`, except that the computation should be done on the GPU. This means `triangles` and `rays` should be moved to the GPU before the computation is done, and the returned object should be moved back to the CPU before finishing.


```python
def raytrace_mesh_gpu(
    rays: Float[Tensor, "nrays rayPoints=2 dims=3"],
    triangles: Float[Tensor, "ntriangles trianglePoints=3 dims=3"],
) -> Float[Tensor, " nrays"]:
    """
    For each ray, return the distance to the closest intersecting triangle, or infinity.

    All computations should be performed on the GPU.
    """
    raise NotImplementedError()


dists = raytrace_mesh_video(rays, triangles, rotation_matrix, raytrace_mesh_gpu, num_frames)
dists = einops.rearrange(dists, "frames (y z) -> frames y z", y=num_pixels_y)
display_video(dists)
```


<details><summary>Click to see the expected output</summary>

<div style="text-align: left"><embed src="https://info-arena.github.io/ARENA_img/misc/media-01/0107.html" width="570" height="620"></div>

</details>


<details><summary>Solution</summary>

```python
def raytrace_mesh_gpu(
    rays: Float[Tensor, "nrays rayPoints=2 dims=3"],
    triangles: Float[Tensor, "ntriangles trianglePoints=3 dims=3"],
) -> Float[Tensor, " nrays"]:
    """
    For each ray, return the distance to the closest intersecting triangle, or infinity.

    All computations should be performed on the GPU.
    """
    NR = rays.size(0)
    NT = triangles.size(0)
    device = "cuda"
    triangles = triangles.to(device)
    rays = rays.to(device)

    # Each triangle is [[Ax, Ay, Az], [Bx, By, Bz], [Cx, Cy, Cz]]
    triangles = einops.repeat(triangles, "NT pts dims -> pts NR NT dims", NR=NR)
    A, B, C = triangles
    assert A.shape == (NR, NT, 3)

    # Each ray is [[Ox, Oy, Oz], [Dx, Dy, Dz]]
    rays = einops.repeat(rays, "NR pts dims -> pts NR NT dims", NT=NT)
    O, D = rays
    assert O.shape == (NR, NT, 3)

    # Define matrix on left hand side of equation
    mat: Float[Tensor, "NR NT 3 3"] = t.stack([-D, B - A, C - A], dim=-1)
    # Get boolean of where matrix is singular, and replace it with the identity in these positions
    dets: Float[Tensor, "NR NT"] = t.linalg.det(mat)
    is_singular = dets.abs() < 1e-8
    mat[is_singular] = t.eye(3).to(device)

    # Define vector on the right hand side of equation
    vec: Float[Tensor, "NR NT 3"] = O - A

    # Solve eqns (note, s is the distance along ray)
    sol: Float[Tensor, "NR NT 3"] = t.linalg.solve(mat, vec)
    s, u, v = sol.unbind(-1)

    # Scale s by Dx to get the distance along ray
    s *= D[..., 0]

    # Get boolean of intersects, and use it to set distance = infinity when there is no intersection
    intersects = (s >= 0) & (u >= 0) & (v >= 0) & (u + v <= 1) & ~is_singular
    s[~intersects] = t.inf

    # Get the minimum distance (over all triangles) for each ray
    return einops.reduce(s, "NR NT -> NR", "min").cpu()


dists = raytrace_mesh_video(rays, triangles, rotation_matrix, raytrace_mesh_gpu, num_frames)
dists = einops.rearrange(dists, "frames (y z) -> frames y z", y=num_pixels_y)
display_video(dists)
```
</details>


### Exercise (bonus) - add lighting

> ```yaml
> Difficulty: 🔴🔴🔴🔴🔴
> Importance: 🔵🔵⚪⚪⚪
> 
> You've done all the essential content for today at this point.
> You can complete this exercise for fun if you have time, or just read & run the solution!
> ```

We can improve our images by adding lighting, i.e. coloring triangles based on the angle of some light source rather than just from distance from the origin. The most common way to do this is using the [Lambertian reflection model](https://en.wikipedia.org/wiki/Lambertian_reflectance), which says that the intensity of the light that reflects off a surface is proportional to the cosine of the angle between the light vector and the surface normal (or equivalently, proportional to their dot product, assuming both vectors are normalized).

<img src="https://raw.githubusercontent.com/info-arena/ARENA_img/main/misc/raytracing-lighting-2.png" width="750">

You should implement the `raytrace_mesh_lambert` function below, which puts this into practice. In other words, your function should return the following for each ray:

- Zero if there is no intersection, i.e. distance to every triangle is infinite
- `intensity + ambient_intensity` if there is an interesection, where `ambient_intensity` is a value we give you (minimum brightness for a triangle, to distinguish it from the black background) and `intensity` is the intensity of light hitting the triangle, i.e. the dot product of the triangle's normal vector and the light vector, set to zero if this dot product is negative.

To emphasize - unlike in your previous functions where you used the distance of each ray to the nearest triangle to determine the color of a given ray/pixel, here every triangle has a unique intensity value and the color of a given ray/pixel is determined only by what its nearest triangle is. The only reason we still need to compute distances is to compute what (if any) the first triangle is that the ray intersects with.


```python
def raytrace_mesh_lambert(
    rays: Float[Tensor, "nrays points=2 dims=3"],
    triangles: Float[Tensor, "ntriangles points=3 dims=3"],
    light: Float[Tensor, "dims=3"],
    ambient_intensity: float,
    device: str = "cuda",
) -> Float[Tensor, " nrays"]:
    """
    For each ray, return the intensity of light hitting the triangle it intersects with (or zero if
    no intersection).

    Args:
        rays:   A tensor of rays, with shape `[nrays, 2, 3]`.
        triangles:  A tensor of triangles, with shape `[ntriangles, 3, 3]`.
        light:  A tensor representing the light vector, with shape `[3]`. We compute the intensity
                as the dot product of the triangle normals & the light vector, then set it to be
                zero if the sign is negative.
        ambient_intensity:  A float representing the ambient intensity. This is the minimum
                            brightness for a triangle, to differentiate it from the black background
                            (rays that don't hit any triangle).
        device: The device to perform the computation on.

    Returns:
        A tensor of intensities for each of the rays, flattened over the [y, z] dimensions. The
        values are zero when there is no intersection, and `ambient_intensity + intensity` when
        there is an interesection (where `intensity` is the dot product of the triangle's normal
        vector and the light vector, truncated at zero).
    """
    raise NotImplementedError()


def display_video_with_lighting(intensity: Float[Tensor, "frames y z"]):
    """
    Displays video of raytracing results, using Plotly. `distances` is a tensor where the [i, y, z]
    element is the lighting intensity based on the angle of light & the surface of the triangle
    which this ray hits first.
    """
    px.imshow(
        intensity,
        animation_frame=0,
        origin="lower",
        color_continuous_scale="magma",
    ).update_layout(coloraxis_showscale=False, width=550, height=600, title="Raytrace mesh video (lighting)").show()


ambient_intensity = 0.5
light = t.tensor([0.0, -1.0, 1.0])
raytrace_function = partial(
    raytrace_mesh_lambert,
    ambient_intensity=ambient_intensity,
    light=light,
)

intensity = raytrace_mesh_video(rays, triangles, rotation_matrix, raytrace_function, num_frames)
intensity = einops.rearrange(intensity, "frames (y z) -> frames y z", y=num_pixels_y)
display_video_with_lighting(intensity)
```


<details><summary>Click to see the expected output</summary>

<div style="text-align: left"><embed src="https://info-arena.github.io/ARENA_img/misc/media-01/0108.html" width="570" height="620"></div>

</details>


<details>
<summary>Help - I'm not sure how to compute the normal vectors.</summary>

You can use the `torch.cross` function, using two edges of the triangle as arguments. For example, you can compute the un-normalized vectors as:

```python
normals = t.cross(triangles[:, 2] - triangles[:, 0], triangles[:, 1] - triangles[:, 0], dim=1)
```

which will have the same shape as each of `triangles[:, i]`.

</details>

<details>
<summary>Help - I'm not sure how to set the intensity to zero if the light is coming from the wrong side of the triangle.</summary>

The `pikachu.stl` file stores triangles in a consistent orientation based on the right hand rule. Assuming you chose a consistent method for computing normal vectors like the one in the dropdown above, your computed intensity values per triangle will either all be the correct sign or all be the opposite sign to the true signed values. This means you can either use `t.where(intensity > 0, intensity, 0.0)` or `t.where(intensity < 0, -intensity, 0.0)` as your final zeroed intensity values and both should look fine (although one will look like the light source is coming from the opposite direction to the other). It doesn't matter which orientation you choose.

</details>


<details><summary>Solution</summary>

```python
def raytrace_mesh_lambert(
    rays: Float[Tensor, "nrays points=2 dims=3"],
    triangles: Float[Tensor, "ntriangles points=3 dims=3"],
    light: Float[Tensor, "dims=3"],
    ambient_intensity: float,
    device: str = "cuda",
) -> Float[Tensor, " nrays"]:
    """
    For each ray, return the intensity of light hitting the triangle it intersects with (or zero if
    no intersection).

    Args:
        rays:   A tensor of rays, with shape `[nrays, 2, 3]`.
        triangles:  A tensor of triangles, with shape `[ntriangles, 3, 3]`.
        light:  A tensor representing the light vector, with shape `[3]`. We compute the intensity
                as the dot product of the triangle normals & the light vector, then set it to be
                zero if the sign is negative.
        ambient_intensity:  A float representing the ambient intensity. This is the minimum
                            brightness for a triangle, to differentiate it from the black background
                            (rays that don't hit any triangle).
        device: The device to perform the computation on.

    Returns:
        A tensor of intensities for each of the rays, flattened over the [y, z] dimensions. The
        values are zero when there is no intersection, and `ambient_intensity + intensity` when
        there is an interesection (where `intensity` is the dot product of the triangle's normal
        vector and the light vector, truncated at zero).
    """
    NR = rays.size(0)
    NT = triangles.size(0)
    triangles = triangles.to(device)
    rays = rays.to(device)

    # Each triangle is [[Ax, Ay, Az], [Bx, By, Bz], [Cx, Cy, Cz]]
    triangles_repeated = einops.repeat(triangles, "NT pts dims -> pts NR NT dims", NR=NR)
    A, B, C = triangles_repeated
    assert A.shape == (NR, NT, 3)

    # Each ray is [[Ox, Oy, Oz], [Dx, Dy, Dz]]
    rays_repeated = einops.repeat(rays, "NR pts dims -> pts NR NT dims", NT=NT)
    O, D = rays_repeated
    assert O.shape == (NR, NT, 3)

    # Define matrix on left hand side of equation
    mat: Float[Tensor, "NR NT 3 3"] = t.stack([-D, B - A, C - A], dim=-1)
    # Get boolean of where matrix is singular, and replace it with the identity in these positions
    dets: Float[Tensor, "NR NT"] = t.linalg.det(mat)
    is_singular = dets.abs() < 1e-8
    mat[is_singular] = t.eye(3).to(device)

    # Define vector on the right hand side of equation
    vec: Float[Tensor, "NR NT 3"] = O - A

    # Solve eqns (note, s is the distance along ray)
    sol: Float[Tensor, "NR NT 3"] = t.linalg.solve(mat, vec)
    s, u, v = sol.unbind(-1)  # each shape [NR, NT]

    # Scale s by Dx to get the distance along ray
    s *= D[..., 0]

    # Get boolean of intersects, and use it to set distance = infinity when there is no intersection
    intersects = (s >= 0) & (u >= 0) & (v >= 0) & (u + v <= 1) & ~is_singular
    s[~intersects] = float("inf")

    # Get the minimum distance (over all triangles) for each ray
    closest_distances, closest_triangles_for_each_ray = s.min(dim=-1)  # both shape [NR]

    # Get the intensity by taking dot product of triangle normals & light vector
    normals = t.cross(triangles[:, 2] - triangles[:, 0], triangles[:, 1] - triangles[:, 0], dim=1)  # shape [NT dims]
    normals /= normals.norm(dim=1, keepdim=True)
    intensity_per_triangle = einops.einsum(normals, light.to(device), "nt dims, dims -> nt")
    intensity_per_triangle_signed = t.where(intensity_per_triangle > 0, intensity_per_triangle, 0.0)

    # Get intensity for each ray, and add ambient intensity where there's an intersection
    intensity = intensity_per_triangle_signed[closest_triangles_for_each_ray] + ambient_intensity

    # Set to zero if the ray doesn't intersect with any triangle
    intensity = t.where(closest_distances.isfinite(), intensity, 0.0)

    return intensity.cpu()


def display_video_with_lighting(intensity: Float[Tensor, "frames y z"]):
    """
    Displays video of raytracing results, using Plotly. `distances` is a tensor where the [i, y, z]
    element is the lighting intensity based on the angle of light & the surface of the triangle
    which this ray hits first.
    """
    px.imshow(
        intensity,
        animation_frame=0,
        origin="lower",
        color_continuous_scale="magma",
    ).update_layout(coloraxis_showscale=False, width=550, height=600, title="Raytrace mesh video (lighting)").show()


ambient_intensity = 0.5
light = t.tensor([0.0, -1.0, 1.0])
raytrace_function = partial(
    raytrace_mesh_lambert,
    ambient_intensity=ambient_intensity,
    light=light,
)

intensity = raytrace_mesh_video(rays, triangles, rotation_matrix, raytrace_function, num_frames)
intensity = einops.rearrange(intensity, "frames (y z) -> frames y z", y=num_pixels_y)
display_video_with_lighting(intensity)
```
</details>


As a final bonus exercise before we conclude, you can try rendering with a **wireframe**, i.e. only including the edges of the triangles rather than the full triangle. All you have to do here is change your `triangle_ray_intersects` function, so that it only detects intersection at a certain subset of the parameter values `u` and `v` (can you see how to do this?).


## Bonus - testing with `pytest`


> *Note - this section was also just written with VSCode in mind, so it might be less suitable for Colab, and you might consider skipping it.*


To wrap up today, we're going to have a further discussion of **testing**. So far, our test functions have been pretty simple - we imported a test from the `part1_ray_tracing/tests.py` file, and ran it to compare our answers to the answers in `part1_ray_tracing/solutions.py`. This works perfectly fine, but there are other Python libraries which can make testing easier and more powerful. In particular, two such libraries are `unittest` and `pytest`. Both these libraries provide extensive features for modularizing and running test functions, and have nice integrations with VSCode. `unittest` is very powerful, but also has a steep learning curve and isn't worth the trouble of learning during a 6 week course. However, `pytest` is very useful and easy to learn, so we'll spend some time here discussing it.

The pytest framework makes it easy to write small, readable tests, and can scale to support complex functional testing for applications and libraries. Today we'll just discuss a few features which will be particularly useful for the kinds of tests we'll be writing, but you're welcome to explore more tests later on.

*Important note - if you're working on Colab or a notebook for these exercises, your tests won't work, because in this setup we'll be importing answers from our test file, rather than importing tests from our answers file. For this reason, we won't be using pytest for the structured exercises in this course (in case anybody is following these exercises in a notebook), but you're strongly recommended to use pytest when you're working from `.py` files instead - which is strongly recommended during much of the bonus content.*

First, look at `part1_ray_tracing/tests.py`. The tests in this file all follow a similar pattern: evaluate your function on some input, check it equals the solution. This is a clear sign that we can use modularization to simplify our code! Compare this file to `part1_ray_tracing/test_with_pytest.py`, which contains the same tests but refactored using pytest. The latter is clearly separated into three sections: one for library imports, one for defining the inputs we'll use for our test functions, and one where we define our test functions.

### Parametrization

We use `pytest.mark.parametrize` to parametrize our tests. This means we can run the same test a bunch of different times on different inputs. In the non-pytest version, we did this by defining different functions (e.g. `test_intersect_ray_1d` and `test_intersect_ray_1d_special_case`), but this isn't necessary here.

The syntax of a function decorated by `pytest.mark.parametrize` is:

```python
@pytest.mark.parametrize("arg1, arg2, arg3", [
    (val1, val2, val3),
    (val4, val5, val6),
    ...
])
def test_function(arg1, arg2, arg3):
    ...
```

This will result in running `test_function` multiple times, the first time with `arg1=val1, arg2=val2, arg3=val3`, and the second time with `arg1=val4, arg2=val5, arg3=val6`, etc. This is a much better way to write tests, because it makes it easy for us to add new test cases without having to write new functions.

### How to run these tests?

There are three ways to run the above tests:

1. **From the terminal**

You can run them from the command line using the pytest command. Open your terminal in VSCode at the bottom of the screen, make sure you're in the directory `chapter0_fundamentals`, then enter the command `pytest`. This will search the current directory (or subdirectories) for any python files with the prefix `test_`, and within that file run all functions with the prefix `test_` (i.e. all the tests for these exercises).

You can also add more complicated commands, like:

* `pytest test_intersect_ray_1d` to specify the file to run tests from
* `pytest test_intersect_ray_1d::test_intersect_ray_1d` to specify the file and test function

2. **From your Python file**

To do this, you need to call `pytest.main` (make sure this is wrapped in an `if MAIN` block). The first argument of this function is a list of args to `pytest`. This has analogous syntax to the command line option, for instance here are a few ways you can do this:

```python
if MAIN:
    pytest.main([])
    pytest.main(["test_part1_ray_tracing.py"])
    pytest.main(["test_part1_ray_tracing.py::test_intersect_ray_1d"])
```

3. **From VSCode's testing display**

This is by far the most useful way to run test functions. VSCode provides a helpful interface to run all test functions in your directory, and see which of them have passed. First, press the test icon on the left hand sidebar (it will look like a triangular flask). If this is your first time, then you'll need to click on the **Configure Python Tests** button, then select `pytest` as your framework (you may have to install pytest when prompted). This should automatically perform test discovery for you, showing you all the test files & functions in your current directory in the left hand window (it detects this the same way pytest does, using the `test_` prefix). You can hover over tests or files to see options like "run test(s)" or debug test(s)". When you run them, you'll see a tick or cross appear next to the test, indicating whether it passed or failed.

This is a very useful interface when you're working on a large project, because as you make updates you can easily re-run all tests, then identify & fix problems.

<details>
<summary>Help - I get <code>Error discovering pytest tests</code></summary>

Try opening your terminal (at the bottom of the screen) and running `pytest --collect-only`. This should print output that helps you diagnose the problem.

One possible issue is changing directories within your python files (e.g. with `os.chdir`), because this can often confuse PyTest's search for tests.
</details>


<details>
<summary>Aside - <code># type: ignore</code></summary>

Note that the test file has the annotation `# type: ignore` at the end of an import line, at the top of the file. This is because VSCode's typechecker will complain when you try and import a file that doesn't exist yet! This line removes the type error, and allows you to write functions without all those annoying squiggly red lines! However, don't overuse this annotation, because it can often be a signal that you've made a mistake in your code, or else have followed a bad coding practice.

</details>

<details>
<summary>Aside - named tuples</summary>

Another way you can clean this code up is to use **named tuples**. These are an especially nice and Pythonic structure which maintains the features of a tuple, but also allows you to define instances & access elements by name. For instance, instead of:

```python
ray_segment_batch = (
    solutions.rays1d,
    solutions.segments
)
```

you could have:

```python
from collections import namedtuple
TestCase = namedtuple("TestCase", "rays segments")

ray_segment_batch = TestCase(
    rays = solutions.rays1d,
    segments = solutions.segments
)
```

and this `ray_segment_batch` object would still be treated like a tensor when it's used in a parameterized test.

</details>


```

---

## chapter0_fundamentals/instructions/pages/02_[0.2]_CNNs_&_ResNets.md

```markdown
# [0.2] - CNNs & ResNets


> **Colab: [exercises](https://colab.research.google.com/github/callummcdougall/arena-pragmatic-interp/blob/main/chapter0_fundamentals/exercises/part2_cnns/0.2_CNNs_&_ResNets_exercises.ipynb?t=20260303) | [solutions](https://colab.research.google.com/github/callummcdougall/arena-pragmatic-interp/blob/main/chapter0_fundamentals/exercises/part2_cnns/0.2_CNNs_&_ResNets_solutions.ipynb?t=20260303)**

Please send any problems / bugs on the `#errata` channel in the [Slack group](https://join.slack.com/t/arena-uk/shared_invite/zt-3afdmdhye-Mdb3Sv~ss_V_mEaXEbkABA), and ask any questions on the dedicated channels for this chapter of material.

If you want to change to dark mode, you can do this by clicking the three horizontal lines in the top-right, then navigating to Settings → Theme.

Links to all other chapters: [(0) Fundamentals](https://arena-chapter0-fundamentals.streamlit.app/), [(1) Transformer Interpretability](https://arena-chapter1-transformer-interp.streamlit.app/), [(2) RL](https://arena-chapter2-rl.streamlit.app/).

<img src="https://raw.githubusercontent.com/info-arena/ARENA_img/main/misc/headers/header-02.png" width="350">


# Introduction


This section is designed to get you familiar with basic neural networks: how they are structured, the basic operations like linear layers and convolutions which go into making them, and why they work as well as they do. You'll start by making very simple neural networks, and by the end of today you'll build up to assembling ResNet34, a comparatively much more complicated architecture.

For a lecture on the material today, which provides some high-level understanding before you dive into the material, watch the video below:

<iframe width="540" height="304" src="https://www.youtube.com/embed/qZWrL4bBYgw" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


## Content & Learning Objectives

### 1️⃣ Making your own modules

In the first set of exercises, we'll cover the general structure of modules in PyTorch. You'll also implement your own basic modules, including for ReLU and Linear layers. You'll finish by assembling a very simple neural network.

> ##### Learning Objectives
>
> - Learn how to create your own modules in PyTorch, by inheriting from `nn.Module`
> - Assemble the pieces together to create a simple fully-connected network, to classify MNIST digits

### 2️⃣ Training Neural Networks

Here, you'll learn how to write a training loop in PyTorch. We'll keep it simple for today (and later on we'll experiment with more modular and extensible designs).

> ##### Learning Objectives
>
> - Understand how to work with transforms, datasets and dataloaders
> - Understand the basic structure of a training loop
> - Learn how to write your own validation loop

### 3️⃣ Convolutions

In this section, you'll read about convolutions, and implement them as an `nn.Module` (not from scratch; we leave that to the bonus exercises). You'll also learn about maxpooling, and implement that as well.

> ##### Learning Objectives
>
> * Learn how convolutions work, and why they are useful for vision models
> * Implement your own convolutions, and maxpooling layers

### 4️⃣ ResNets

Here, you'll combine all the pieces you've learned so far to assemble ResNet34, a much more complex architecture used for image classification.

> ##### Learning Objectives
>
> * Learn about skip connections, and how they help overcome the degradation problem
> * Learn about batch normalization, and why it is used in training
> * Assemble your own ResNet, and load in weights from PyTorch's ResNet implementation

### ☆ Bonus - Feature Extraction

In this section, you'll learn how to repurpose your ResNet to perform a different task than it was designed for, using feature extraction.

> ##### Learning Objectives
>
> * Understand the difference between feature extraction and finetuning
> * Perform feature extraction on a pre-trained ResNet

### ☆ Bonus - Convolutions From Scratch

This section takes you through the low-level details of how to actually implement convolutions. It's not necessary to understand this section to complete the exercises, but it's a good way to get a deeper understanding of how convolutions work.

> ##### Learning Objectives
>
> * Understand how array strides work, and why they're important for efficient linear operations
> * Learn how to use `as_strided` to perform simple linear operations like trace and matrix multiplication
> * Implement your own convolutions and maxpooling functions using stride-based methods


## Setup code


```python
import json
import sys
from collections import namedtuple
from dataclasses import dataclass
from pathlib import Path

import einops
import numpy as np
import torch as t
import torch.nn as nn
import torch.nn.functional as F
import torchinfo
from IPython.display import display
from jaxtyping import Float, Int
from PIL import Image
from rich import print as rprint
from rich.table import Table
from torch import Tensor
from torch.utils.data import DataLoader, Subset
from torchvision import datasets, models, transforms
from tqdm.notebook import tqdm

# Make sure exercises are in the path
chapter = "chapter0_fundamentals"
section = "part2_cnns"
root_dir = next(p for p in Path.cwd().parents if (p / chapter).exists())
exercises_dir = root_dir / chapter / "exercises"
section_dir = exercises_dir / section
if str(exercises_dir) not in sys.path:
    sys.path.append(str(exercises_dir))

MAIN = __name__ == "__main__"

import part2_cnns.tests as tests
import part2_cnns.utils as utils
from plotly_utils import line
```


<details>
<summary>Help - I get a NumPy-related error</summary>

This is an annoying colab-related issue which I haven't been able to find a satisfying fix for. If you restart runtime (but don't delete runtime), and run just the imports cell above again (but not the `%pip install` cell), the problem should go away.
</details>




=== NEW CHAPTER ===


# 1️⃣ Making your own modules



> ##### Learning Objectives
>
> - Learn how to create your own modules in PyTorch, by inheriting from `nn.Module`
> - Assemble the pieces together to create a simple fully-connected network, to classify MNIST digits

Note - from this point on we'll start referring to the PyTorch documentation pages quite a lot. We will also include a lot of content within this material if we want to highlight it for you, however it's also an important skill to be able to use documentation pages to find answers to specific questions & assist you in debugging.


## Subclassing `nn.Module`

One of the most basic parts of PyTorch that you will see over and over is the `nn.Module` class. All types of neural net components inherit from it, from the simplest `nn.Relu` to the most complex `nn.Transformer`. Often, a complex `nn.Module` will have sub-`Module`s which implement smaller pieces of its functionality.

Other common `Module`s  you'll see include

- `nn.Linear`, for fully-connected layers with or without a bias
- `nn.Conv2d`, for a two-dimensional convolution (we'll see more of these in a future section)
- `nn.Softmax`, which implements the [softmax](https://pytorch.org/docs/stable/generated/torch.nn.Softmax.html) function

The list goes on, including activation functions, normalizations, pooling, attention, and more. You can see all the `Module`s that PyTorch provides [here](https://pytorch.org/docs/stable/nn.html). You can also create your own `Module`s, as we will do often!

The `Module` class provides a lot of functionality, but we'll only cover a little bit of it here.

In this section, we'll add another layer of abstraction to all the linear operations we've done in previous sections, by packaging them inside `nn.Module` objects.


### `__init__` and `forward`

A subclass of `nn.Module` usually looks something like this:

```python
import torch.nn as nn

class MyModule(nn.Module):
    def __init__(self, arg1, arg2, ...):
        super().__init__()
        # Initialization code

    def forward(self, x: Tensor) -> Tensor:
        # Forward pass code
```

The initialization sets up attributes that will be used for the life of the `Module`, like its parameters, hyperparameters, or other sub-`Module`s it might need to use. These are usually added to the instance with something like `self.attribute = attr`, where `attr` might be provided as an argument. Some modules are simple enough that they don't need any persistent attributes, and in this case you can skip the `__init__`.

The `forward` method is called on each forward pass of the `Module`, possibly using the attributes that were set up in the `__init__`. It should take in the input, do whatever it's supposed to do, and return the result. Subclassing `nn.Module` automatically makes instances of your class callable, so you can do `model(x)` on an input `x` to invoke the `forward` method.


### The `nn.Parameter` class

A `nn.Parameter` is a special type of `Tensor`. Basically, this is the class that torch has provided for storing the weights and biases of a `Module`. It has some special properties for doing this:

- If a `Parameter` is set as an attribute of a `Module`, it will be auto-detected by torch and returned when you call `module.parameters()` (along with all the other `Parameters` associated with the `Module`, or any of the `Module`'s sub-modules!).
- This makes it easy to pass all the parameters of a model into an optimizer and update them all at once.

When you create a `Module` that has weights or biases, be sure to wrap them in `nn.Parameter` so that torch can detect and update them appropriately:

```python
class MyModule(nn.Module):
    def __init__(self, weights: Tensor, biases: Tensor):
        super().__init__()
        self.weights = nn.Parameter(weights) # wrapping a tensor in nn.Parameter
        self.biases = nn.Parameter(biases)
```


### Printing information with `extra_repr`

Another useful method is called `extra_repr`. This allows you to format the string representation of your `Module` in a way that's more informative than the default. For example, the following:

```python
class MyModule(nn.Module):
    def __init__(self, arg1, arg2, ...):
        super().__init__()
        # Initialization code

    def extra_repr(self) -> str:
        return f"arg1={self.arg1}, arg2={self.arg2}, ..."
```

will result in the output `"MyModule(arg1=arg1, arg2=arg2, ...)"` when you print an instance of this module. You might want to take this opportunity to print out useful invariant information about the module. The Python built-in function `getattr` might be helpful here (it can be used e.g. as `getattr(self, "arg1")`, which returns the same as `self.arg1` would). For simple modules, it's fine not to implement `extra_repr`.


## ReLU

The first module you should implement is `ReLU`. This will relatively simple, since it doesn't involve any argument (so we only need to implement `forward`). Make sure you look at the PyTorch documentation page for [ReLU](https://pytorch.org/docs/stable/generated/torch.nn.ReLU.html) so that you're comfortable with how they work.

ReLU is defined as the element-wise maximum between the input and a tensor of zeros. It's one of the simplest types of **nonlinear activation functions**. These are essential because linear operations compose to make more linear operations, which is very limiting. On the other hand, the **universal approximation theorem** tells us that we can approximate any continuous function using a sufficiently large neural network, if we use nonlinear activation functions. It's worth emphasizing that the theory of the UAT and what networks look like in practice are very different - in particular, many versions of the UAT are based on a shallow but extremely wide neural network, on the other hand most of the power of modern neural networks comes from their ability to compose between layers: feeding the output of one layer into the input of another, and create increasingly expressive functions. We'll explore this idea more when we study circuits in next week's interpretability material.


### Exercise - implement `ReLU`

> ```yaml
> Difficulty: 🔴🔴⚪⚪⚪
> Importance: 🔵🔵🔵⚪⚪
> 
> You should spend up to ~10 minutes on this exercise.
> ```

You should fill in the `forward` method of the `ReLU` class below.


```python
class ReLU(nn.Module):
    def forward(self, x: Tensor) -> Tensor:
        raise NotImplementedError()


tests.test_relu(ReLU)
```


<details><summary>Solution</summary>

```python
class ReLU(nn.Module):
    def forward(self, x: Tensor) -> Tensor:
        return t.maximum(x, t.tensor(0.0))
```
</details>


## Linear

Now implement your own `Linear` module. This applies a simple linear transformation, with a weight matrix and optional bias vector. The PyTorch documentation page is [here](https://pytorch.org/docs/stable/generated/torch.nn.Linear.html). Note that this is the first `Module` you'll implement that has learnable weights and biases.

<details>
<summary>Question - what type do you think these variables should be?</summary>

They have to be `torch.Tensor` objects wrapped in `nn.Parameter` in order for `nn.Module` to recognize them. If you forget to do this, `module.parameters()` won't include your `Parameter`, which prevents an optimizer from being able to modify it during training.
        
Also, in tomorrow's exercises we'll be building a ResNet and loading in weights from a pretrained model, and this is hard to do if you haven't registered all your parameters!
</details>

For any layer, initialization is very important for the stability of training: with a bad initialization, your model will take much longer to converge or may completely fail to learn anything. The default PyTorch behavior isn't necessarily optimal and you can often improve performance by using something more custom, but we'll follow it for today because it's simple and works decently well.

Each float in the weight and bias tensors are drawn independently from the uniform distribution on the interval:

$$
\bigg[-\frac{1}{\sqrt{N_{in}}}, \frac{1}{\sqrt{N_{in}}}\bigg]
$$

where $N_{in}$ is the number of inputs contributing to each output value. The rough intuition for this is that it keeps the variance of the activations at each layer constant, since each one is calculated by taking the sum over $N_{in}$ inputs multiplied by the weights (and standard deviation of the sum of independent random variables scales as the square root of number of variables).

This initialization technique is called **uniform Kaiming initialization**. A few last notes on initialization methods:

- Kaiming often has a different constant in the numerator depending on what the target variance is, also there are uniform & normal variants of it (we'll only be using the uniform variant)
- **Xavier initialization** is the other well-known technique, and differs in that it uses $N_{in} + N_{out}$ in the denominator (this makes sense when also considering variance scaling of backward passes as well as forward passes - see the next dropdown for technical details)

<details>
<summary>Technical details (derivation of distribution)</summary>

The key intuition behind Kaiming initialisation (and others like it) is that we want the variance of our activations to be the same through all layers of the model when we initialize. Suppose $x$ and $y$ are activations from two adjacent layers, and $w$ are the weights connecting them (so we have $y_i = \sum_j w_{ij} x_j + b_i$, where $b$ is the bias). With $N_{x}$ as the number of neurons in layer $x$, we have:

$$
\begin{aligned}
\operatorname{Var}\left(y_i\right)=\sigma_x^2 & =\operatorname{Var}\left(\sum_j w_{i j} x_j\right) \\
& =\sum_j \operatorname{Var}\left(w_{i j} x_j\right) \quad \text { Inputs and weights are independent of each other } \\
& =\sum_j \operatorname{Var}\left(w_{i j}\right) \cdot \operatorname{Var}\left(x_j\right) \quad \text { Variance of product of independent RVs with zero mean is product of variances } \\
& = N_x \cdot \sigma_x^2 \cdot \operatorname{Var}\left(w_{i j}\right) \quad \text { Variance equal for all } N_x \text { neurons, call this value } \sigma_x^2
\end{aligned}
$$

For this to be the same as $\sigma_x^2$, we need $\operatorname{Var}(w_{ij}) = \frac{1}{N_x}$, so the standard deviation is $\frac{1}{\sqrt{N_x}}$.

This is not exactly the case for the Kaiming uniform distribution (which has variance $\frac{12}{(2 \sqrt{N_x})^2} = \frac{3}{N_x}$), and as far as I'm aware there's no principled reason why PyTorch does this. But the most important thing is that the variance scales as $O(1 / N_x)$, rather than what the exact scaling constant is.

There are other initializations with some theoretical justification. For instance, **Xavier initialization** has a uniform distribution in the interval:

$$
\bigg[-\frac{\sqrt{6}}{\sqrt{N_{in} + N_{out} + 1}}, \frac{\sqrt{6}}{\sqrt{N_{in} + N_{out} + 1}}\bigg]
$$

which is motivated by the idea of both keeping the variance of activations constant and keeping the ***gradients*** constant when we backpropagate.

However, you don't need to worry about any of this here, just implement Kaiming He uniform with a bound of $\frac{1}{\sqrt{N_{in}}}$!
</details>


### Exercise - implement `Linear`

> ```yaml
> Difficulty: 🔴🔴⚪⚪⚪
> Importance: 🔵🔵🔵🔵⚪
> 
> You should spend up to ~10 minutes on this exercise.
> ```

Remember, you should define the weights (and bias, if `bias=True`) in the `__init__` block. Also, make sure not to mix up `bias` (which is the boolean parameter to `__init__`) and `self.bias` (which should either be the actual bias tensor, or `None` if `bias` is false).

You should also fill in `forward` (which will multiply the input by the weight matrix and add the bias, if present).

Lastly, you should fill in `extra_repr` to give a string representation of the `Linear` module. There are no tests for this method, you should just make sure it's suitably informative (this will help when printing out your model later on).


```python
class Linear(nn.Module):
    def __init__(self, in_features: int, out_features: int, bias=True):
        """
        A simple linear (technically, affine) transformation.

        The fields should be named `weight` and `bias` for compatibility with PyTorch.
        If `bias` is False, set `self.bias` to None.
        """
        super().__init__()
        raise NotImplementedError()

    def forward(self, x: Tensor) -> Tensor:
        """
        x: shape (*, in_features)
        Return: shape (*, out_features)
        """
        raise NotImplementedError()

    def extra_repr(self) -> str:
        raise NotImplementedError()


tests.test_linear_parameters(Linear, bias=False)
tests.test_linear_parameters(Linear, bias=True)
tests.test_linear_forward(Linear, bias=False)
tests.test_linear_forward(Linear, bias=True)
```


<details>
<summary>Help - when I print my Linear module, it also prints a large tensor.</summary>

This is because you've (correctly) defined `self.bias` as either `torch.Tensor` or `None`, rather than set it to the boolean value of `bias` used in initialisation.
        
To fix this, you will need to change `extra_repr` so that it prints the boolean value of `bias` rather than the value of `self.bias`.
</details>


<details><summary>Solution</summary>

```python
class Linear(nn.Module):
    def __init__(self, in_features: int, out_features: int, bias=True):
        """
        A simple linear (technically, affine) transformation.

        The fields should be named `weight` and `bias` for compatibility with PyTorch.
        If `bias` is False, set `self.bias` to None.
        """
        super().__init__()
        self.in_features = in_features
        self.out_features = out_features
        self.bias = bias

        sf = 1 / np.sqrt(in_features)

        weight = sf * (2 * t.rand(out_features, in_features) - 1)
        self.weight = nn.Parameter(weight)

        if bias:
            bias = sf * (2 * t.rand(out_features) - 1)
            self.bias = nn.Parameter(bias)
        else:
            self.bias = None

    def forward(self, x: Tensor) -> Tensor:
        """
        x: shape (*, in_features)
        Return: shape (*, out_features)
        """
        x = einops.einsum(x, self.weight, "... in_feats, out_feats in_feats -> ... out_feats")
        if self.bias is not None:
            x += self.bias
        return x

    def extra_repr(self) -> str:
        # note, we need to use `self.bias is not None`, because `self.bias` is either a tensor or
        # None, not bool
        return f"in_features={self.in_features}, out_features={self.out_features}, bias={self.bias is not None}"
```
</details>


## Flatten

Lastly, we've given you the `Flatten` module rather than including it as an exercise (because it's simple but quite finnicky to implement). This is a standardised way to rearrange our tensors so that they can be fed into a linear layer. It's a bit like `einops.rearrange`, but more specialised and less flexible (it flattens over some contiguous range of dimensions, rather than allowing for general reshape operations). By default we use `Flatten(start_dim=1, end_dim=-1)` which means flattening over the dimensions from `input.shape[1:]`, in other words over all except the batch dimension.

Make sure you understand what this module is doing before moving on.

<!-- <details>
<summary>Help - I can't figure out what shape the output should be in Flatten.</summary>

If `input.shape = (n0, n1, ..., nk)`, and the `Flatten` module has `start_dim=i, end_dim=j`, then the new shape should be `(n0, n1, ..., ni*...*nj, ..., nk)`. This is because we're **flattening** over the dimensions `(ni, ..., nj)`.

</details>

<details>
<summary>Help - I can't see why my Flatten module is failing the tests.</summary>

The most common reason is failing to correctly handle indices. Make sure that:
* You're indexing up to **and including** `end_dim`.
* You're correctly managing the times when `end_dim` is negative (e.g. if `input` is an nD tensor, and `end_dim=-1`, this should be interpreted as `end_dim=n-1`).
</details> -->


```python
class Flatten(nn.Module):
    def __init__(self, start_dim: int = 1, end_dim: int = -1) -> None:
        super().__init__()
        self.start_dim = start_dim
        self.end_dim = end_dim

    def forward(self, input: Tensor) -> Tensor:
        """
        Flatten out dimensions from start_dim to end_dim, inclusive of both.
        """
        shape = input.shape

        # Get start & end dims, handling negative indexing for end dim
        start_dim = self.start_dim
        end_dim = self.end_dim if self.end_dim >= 0 else len(shape) + self.end_dim

        # Get the shapes to the left / right of flattened dims, as well as size of flattened middle
        shape_left = shape[:start_dim]
        shape_right = shape[end_dim + 1 :]
        shape_middle = t.prod(t.tensor(shape[start_dim : end_dim + 1])).item()

        return t.reshape(input, shape_left + (shape_middle,) + shape_right)

    def extra_repr(self) -> str:
        return ", ".join([f"{key}={getattr(self, key)}" for key in ["start_dim", "end_dim"]])
```


## Simple Multi-Layer Perceptron

Now, we can put together these two modules to create a neural network. We'll create one of the simplest networks which can be used to separate data that is non-linearly separable: a single linear layer, followed by a nonlinear function (ReLU), followed by another linear layer. This type of architecture (alternating linear layers and nonlinear functions) is often called a **multi-layer perceptron** (MLP).

The output of this network will have 10 dimensions, corresponding to the 10 classes of MNIST digits. We can then use the **softmax function** $x_i \to \frac{e^{x_i}}{\sum_i e^{x_i}}$ to turn these values into probabilities. However, it's common practice for the output of a neural network to be the values before we take softmax, rather than after. We call these pre-softmax values the **logits**.

<details>
<summary>Question - can you see what makes logits non-unique (i.e. why any given set of probabilities might correspond to several different possible sets of logits)?</summary>

Logits are **translation invariant**. If you add some constant $c$ to all logits $x_i$, then the new probabilities are:

$$
p_i' = \frac{e^{x_i + c}}{\sum_j e^{x_j + c}} = \frac{e^{x_i}}{\sum_j e^{x_j}} = p_i
$$

in other words, the probabilities don't change.

We can define **logprobs** as the log of the probabilities, i.e. $y_i = \log p_i$. Unlike logits, these are uniquely defined.

</details>


### Exercise - implement the simple MLP

> ```yaml
> Difficulty: 🔴🔴🔴⚪⚪
> Importance: 🔵🔵🔵🔵⚪
> 
> You should spend up to ~20 minutes on this exercise.
> ```

The diagram below shows what your MLP should look like:

<img src="https://raw.githubusercontent.com/info-arena/ARENA_img/main/misc/mlp-mermaid.svg" width="170">

Please ask a TA (or message the Slack group) if any part of this diagram is unclear.


```python
class SimpleMLP(nn.Module):
    def __init__(self):
        super().__init__()
        raise NotImplementedError()

    def forward(self, x: Tensor) -> Tensor:
        raise NotImplementedError()


tests.test_mlp_module(SimpleMLP)
tests.test_mlp_forward(SimpleMLP)
```


<details><summary>Solution</summary>

```python
class SimpleMLP(nn.Module):
    def __init__(self):
        super().__init__()
        self.flatten = Flatten()
        self.linear1 = Linear(in_features=28 * 28, out_features=100)
        self.relu = ReLU()
        self.linear2 = Linear(in_features=100, out_features=10)

    def forward(self, x: Tensor) -> Tensor:
        return self.linear2(self.relu(self.linear1(self.flatten(x))))
```
</details>


In the next section, we'll learn how to train and evaluate our model on real data.




=== NEW CHAPTER ===


# 2️⃣ Training Neural Networks



> ##### Learning Objectives
>
> - Understand how to work with transforms, datasets and dataloaders
> - Understand the basic structure of a training loop
> - Learn how to write your own validation loop

## Transforms, Datasets & DataLoaders

Before we use this model to make any predictions, we first need to think about our input data. Below is a block of code to fetch and process MNIST data. We will go through it line by line.


```python
MNIST_TRANSFORM = transforms.Compose(
    [
        transforms.ToTensor(),
        transforms.Normalize(0.1307, 0.3081),
    ]
)


def get_mnist(trainset_size: int = 10_000, testset_size: int = 1_000) -> tuple[Subset, Subset]:
    """Returns a subset of MNIST training data."""

    # Get original datasets, which are downloaded to "./data" for future use
    mnist_trainset = datasets.MNIST(exercises_dir / "data", train=True, download=True, transform=MNIST_TRANSFORM)
    mnist_testset = datasets.MNIST(exercises_dir / "data", train=False, download=True, transform=MNIST_TRANSFORM)

    # # Return a subset of the original datasets
    mnist_trainset = Subset(mnist_trainset, indices=range(trainset_size))
    mnist_testset = Subset(mnist_testset, indices=range(testset_size))

    return mnist_trainset, mnist_testset


mnist_trainset, mnist_testset = get_mnist()
mnist_trainloader = DataLoader(mnist_trainset, batch_size=64, shuffle=True)
mnist_testloader = DataLoader(mnist_testset, batch_size=64, shuffle=False)

# Get the first batch of test data, by starting to iterate over `mnist_testloader`
for img_batch, label_batch in mnist_testloader:
    print(f"{img_batch.shape=}\n{label_batch.shape=}\n")
    break

# Get the first datapoint in the test set, by starting to iterate over `mnist_testset`
for img, label in mnist_testset:
    print(f"{img.shape=}\n{label=}\n")
    break

t.testing.assert_close(img, img_batch[0])
assert label == label_batch[0].item()
```


The `torchvision` package consists of popular datasets, model architectures, and common image transformations for computer vision, and `torchvision.transforms` provides access to a suite of functions for preprocessing data. We define a transform for the MNIST data (which is applied to each image in the dataset) by composing `ToTensor` (which converts a `PIL.Image` object into a PyTorch tensor) and `Normalize` (which takes arguments for the mean and standard deviation, and performs the linear transformation `x -> (x - mean) / std`). For the latter, we use `0.1307` and `0.3081` which are the empirical mean & std of the raw data (so after this transformation, the data will have mean 0 and variance 1).

Next, we define our datasets using `torchvision.datasets`. The first argument tells us where to save our data to (so that when we run this in the future we won't have to re-save it), and `transform=MNIST_TRANSFORM` tells us that we should apply our previously defined `transform` to each element in our dataset. We also use `Subset` which allows us to return a slice of the dataset rather than the whole thing (because our model won't need much data to train!).

Finally, since our dataset only allows for iteration over individual datapoints, we wrap it in `DataLoader` which enables iteration over **batches**. It also provides useful arguments like `shuffle`, which determine whether we randomize the order after each epoch. The code above demonstrates iteration over the dataset & dataloader respectively, showing how the first element in the dataloader's first batch equals the first element in the dataset (note that this wouldn't be true for the training set, because we've shuffled it).

<details>
<summary>Aside - why batch sizes are often powers of 2</summary>

It's common to see batch sizes which are powers of two. The motivation is for efficient GPU utilisation, since processor architectures are normally organised around powers of 2, and computational efficiency is often increased by having the items in each batch split across processors. Or at least, that's the idea. The truth is a bit more complicated, and some studies dispute whether it actually saves time, so at this point it's more of a standard convention than a hard rule which will always lead to more efficient training.

</details>


Before proceeding, try and answer the following questions:


<details>
<summary>Question - can you explain why we include a data normalization function in <code>torchvision.transforms</code> ?</summary>

One consequence of unnormalized data is that you might find yourself stuck in a very flat region of the domain, and gradient descent may take much longer to converge.

Normalization isn't strictly necessary for this reason, because any rescaling of an input vector can be effectively undone by the network learning different weights and biases. But in practice, it does usually help speed up convergence.

Normalization also helps avoid numerical issues.
</details>

<details>
<summary>Question - what is the benefit of using <code>shuffle=True</code> when defining our dataloaders? What might the problem be if we didn't do this?</summary>

Shuffling is done during the training to make sure we aren't exposing our model to the same cycle (order) of data in every epoch. It is basically done to ensure the model isn't adapting its learning to any kind of spurious pattern.
</details>


### Aside - `tqdm`

You might have seen some blue progress bars running when you first downloaded your MNIST data. These were generated using a library called `tqdm`, which is also a really useful tool when training models or running any process that takes a long period of time.

The `tqdm` function wraps around an iterable, and displays a progress bar as you iterate through it. The code below shows a minimal example:

```python
from tqdm.notebook import tqdm
import time

for i in tqdm(range(100)):
    time.sleep(0.1)
```

There are some more advanced features of `tqdm` too, for example:

- If you define the progress bar `pbar = tqdm(...)` before your iteration, then you have the option of adding extra information to it using `pbar.set_description` or `pbar.set_postfix`
- You can specify the total number of iterations with `tqdm(iterable, total=...)`; this is actually very important when the iterable is something like `enumerate(...)` which doesn't have a length attribute, since tqdm will usually try and infer the total from calling `len` on the iterable you pass it.

Here's some code that demonstrates these extra features:

```python
word = "hello!"
pbar = tqdm(enumerate(word), total=len(word))
t0 = time.time()

for i, letter in pbar:
    time.sleep(1.0)
    pbar.set_postfix(i=i, letter=letter, time=f"{time.time()-t0:.3f}")
```


### Aside - `device`

One last thing to discuss before we move onto training our model: **GPUs**. We'll discuss this in more detail in later exercises. For now, [this page](https://wandb.ai/wandb/common-ml-errors/reports/How-To-Use-GPU-with-PyTorch---VmlldzozMzAxMDk) should provide a basic overview of how to use your GPU. A few things to be aware of here:

* The `to` method is really useful here - it can move objects between different devices (i.e. CPU and GPU) *as well as* changing a tensor's datatype.
    * Note that `to` is never inplace for tensors (i.e. you have to call `x = x.to(device)`), but when working with models, calling `model = model.to(device)` or `model.to(device)` are both perfectly valid.
* Errors from having one tensor on cpu and another on cuda are very common. Some useful practices to avoid this:
    * Throw in assert statements, to make sure tensors are on the same device
    * Remember that when you initialise an array (e.g. with `t.zeros` or `t.arange`), it will be on CPU by default.
    * Tensor methods like [`new_zeros`](https://pytorch.org/docs/stable/generated/torch.Tensor.new_zeros.html) or [`new_full`](https://pytorch.org/docs/stable/generated/torch.Tensor.new_full.html) are useful, because they'll create tensors which match the device and dtype of the base tensor.

It's common practice to put a line like this at the top of your file, defining a global variable which you can use in subsequent modules and functions (excluding the print statement):


```python
device = t.device("mps" if t.backends.mps.is_available() else "cuda" if t.cuda.is_available() else "cpu")

# If this is CPU, we recommend figuring out how to get cuda access (or MPS if you're on a Mac).
print(device)
```


## Training loop

Below is a very simple training loop, which you can run to train your model.

In later exercises, we'll try to **modularize** our training loops. This will involve things like creating a `Trainer` class which wraps around our model, and giving it methods like `training_step` and `validation_step` which correspond to different parts of the training loop. This will make it easier to add features like logging and validation, and will also make our code more readable and easier to refactor. However, for now we've kept things simple.


```python
model = SimpleMLP().to(device)

batch_size = 128
epochs = 3

mnist_trainset, _ = get_mnist()
mnist_trainloader = DataLoader(mnist_trainset, batch_size=batch_size, shuffle=True)

optimizer = t.optim.Adam(model.parameters(), lr=1e-3)
loss_list = []

for epoch in range(epochs):
    pbar = tqdm(mnist_trainloader)

    for imgs, labels in pbar:
        # Move data to device, perform forward pass
        imgs, labels = imgs.to(device), labels.to(device)
        logits = model(imgs)

        # Calculate loss, perform backward pass
        loss = F.cross_entropy(logits, labels)
        loss.backward()
        optimizer.step()
        optimizer.zero_grad()

        # Update logs & progress bar
        loss_list.append(loss.item())
        pbar.set_postfix(epoch=f"{epoch + 1}/{epochs}", loss=f"{loss:.3f}")

line(
    loss_list,
    x_max=epochs * len(mnist_trainset),
    labels={"x": "Examples seen", "y": "Cross entropy loss"},
    title="SimpleMLP training on MNIST",
    width=700,
)
```


<details><summary>Click to see the expected output</summary>

<div style="text-align: left"><embed src="https://info-arena.github.io/ARENA_img/misc/media-02/0201.html" width="720" height="480"></div>

</details>


Let's break down the important parts of this code.

The batch size is the number of samples in each batch (i.e. the number of samples we feed into the model at once). While training our model, we differentiate with respect to the average loss over all samples in the batch (so a smaller batch usually means the loss is more noisy). However, if you're working with large models, then often having a batch size too large will result in a memory error. This will be relevant for models later on in the course, but for now we're working with very small models so this isn't an issue.

Next, we get our training set, via the helper function `get_mnist`. This helper function used `torchvision.datasets.MNIST` to load in data, and then (optionally) the `torch.utils.data.Subset` function to return a subset of this data. Don't worry about the details of this function, it's not the kind of thing you'll need to know by heart.

We then define our optimizer, using `torch.optim.Adam`. The `torch.optim` module gives a wide variety of modules, such as Adam, SGD, and RMSProp. Adam is generally the most popular and seen as the most effective in the majority of cases. We'll discuss optimizers in more detail tomorrow, but for now it's enough to understand that the optimizer calculates the amount to update parameters by (as a function of those parameters' gradients, and sometimes other inputs), and performs this update step. The first argument passed to our optimizer is the parameters of our model (because these are the values that will be updated via gradient descent), and you can also pass keyword arguments to the optimizer which change its behaviour (e.g. the learning rate).

Lastly, we have the actual training loop. We iterate through our training data, and for each batch we:

1. Evaluate our model on the batch of data, to get the logits for our class predictions,
2. Calculate the loss between our logits and the true class labels,
3. Backpropagate the loss through our model (this step accumulates gradients in our model parameters),
4. Step our optimizer, which is what actually updates the model parameters,
5. Zero the gradients of our optimizer, ready for the next step.


### Cross entropy loss

The formula for cross entropy loss over a batch of size $N$ is:

$$
\begin{aligned}
l &= \frac{1}{N} \sum_{n=1}^{N} l_n \\
l_n &=-\log p_{n, y_{n}}
\end{aligned}
$$

where $p_{n, c}$ is the probability the model assigns to class $c$ for sample $n$, and $y_{n}$ is the true label for this sample.

<details>
<summary>See this dropdown, if you're still confused about this formula, and how this relates to the information-theoretic general formula for cross entropy.</summary>

The cross entropy of a distribution $p$ relate to a distribution $q$ is:

$$
\begin{aligned}
H(q, p) &= -\sum_{n} q(n) \log p(n)
\end{aligned}
$$

In our case, $q$ is the true distribution (i.e. the one-hot encoded labels, which equals one for $n = y_n$, zero otherwise), and $p$ is our model's output. With these subsitutions, this formula becomes equivalent to the formula for $l$ given above.
</details>

<details>
<summary>See this dropdown, if you're confused about how this is the same as the <a href="https://pytorch.org/docs/stable/generated/torch.nn.CrossEntropyLoss.html#torch.nn.CrossEntropyLoss">PyTorch definition</a>.</summary>

The PyTorch definition of cross entropy loss is:

$$
\ell(x, y)=\frac{1}{N}\sum_{n=1}^{N} l_n, \quad l_n=-\sum_{c=1}^C w_c \log \frac{\exp \left(x_{n, c}\right)}{\sum_{i=1}^C \exp \left(x_{n, i}\right)} y_{n, c}
$$

$w_c$ are the weights (which all equal one by default), $p_{n, c} = \frac{\exp \left(x_{n, c}\right)}{\sum_{i=1}^C \exp \left(x_{n, i}\right)}$ are the probabilities, and $y_{n, c}$ are the true labels (which are one-hot encoded, i.e. their value is one at the correct label $c$ and zero everywhere else). With this, the formula for $l_n$ reduces to the one we see above (i.e. the mean of the negative log probabilities).

</details>

The function `torch.functional.cross_entropy` expects the **unnormalized logits** as its first input, rather than probabilities. We get probabilities from logits by applying the softmax function:

$$
\begin{aligned}
p_{n, c} &= \frac{\exp(x_{n, c})}{\sum_{c'=1}^{C} \exp(x_{n, c'})}
\end{aligned}
$$

where $x_{n, c}$ is the model's output for class $c$ and sample $n$, and $C$ is the number of classes (in the case of MNIST, $C = 10$).

Some terminology notes:

* When we say **logits**, we mean the output of the model before applying softmax. We can uniquely define a distribution with a set of logits, just like we can define a distribution with a set of probabilities (and sometimes it's easier to think of a distribution in terms of logits, as we'll see later in the course).

* When we say **unnormalized**, we mean the denominator term $\sum_{c'} \exp(x_{n, c'})$ isn't necessarily equal to 1. We can add a constant value onto all the logits which makes this term 1 without changing any of the actual probabilities, then we have the relation $p_{n, c} = \exp(-l_{n, c})$. Here, we call $-l_{n, c}$ the **log probabilities** (or log probs), since $-l_{n, c} = \log p_{n, c}$.

If you're interested in the intuition behind cross entropy as a loss function, see [this post on KL divergence](https://www.lesswrong.com/posts/no5jDTut5Byjqb4j5/six-and-a-half-intuitions-for-kl-divergence) (note that KL divergence and cross entropy differ by an amount which is independent of our model's predictions, so minimizing cross entropy is equivalent to minimizing KL divergence). Also see these two videos:

* [Intuitively Understanding the Cross Entropy Loss](https://www.youtube.com/watch?v=Pwgpl9mKars&amp;ab_channel=AdianLiusie)
* [Intuitively Understanding the KL Divergence](https://www.youtube.com/watch?v=SxGYPqCgJWM&amp;ab_channel=AdianLiusie)


### Aside - `dataclasses`

Sometimes, when we have a lot of different input parameters to our model, it can be helpful to use dataclasses to keep track of them all. Dataclasses are a special kind of class which come with built-in methods for initialising and printing (i.e. no need to define an `__init__` or `__repr__`). Another advantage of using them is autocompletion: when you type in `args.` in VSCode, you'll get a dropdown of all your different dataclass attributes, which can be useful when you've forgotten what you called a variable!

Here's an example of how we might rewrite our training code above using dataclasses. We've wrapped all the training code inside a single argument called `train`, which takes a `SimpleMLPTrainingArgs` object as its only argument.


```python
@dataclass
class SimpleMLPTrainingArgs:
    """
    Defining this class implicitly creates an __init__ method, which sets arguments as below, e.g.
    self.batch_size=64. Any of these fields can also be overridden when you create an instance, e.g.
    SimpleMLPTrainingArgs(batch_size=128).
    """

    batch_size: int = 64
    epochs: int = 3
    learning_rate: float = 1e-3


def train(args: SimpleMLPTrainingArgs) -> tuple[list[float], SimpleMLP]:
    """
    Trains & returns the model, using training parameters from the `args` object. Returns the model,
    and loss list.
    """
    model = SimpleMLP().to(device)

    mnist_trainset, _ = get_mnist()
    mnist_trainloader = DataLoader(mnist_trainset, batch_size=args.batch_size, shuffle=True)

    optimizer = t.optim.Adam(model.parameters(), lr=args.learning_rate)
    loss_list = []

    for epoch in range(args.epochs):
        pbar = tqdm(mnist_trainloader)

        for imgs, labels in pbar:
            # Move data to device, perform forward pass
            imgs, labels = imgs.to(device), labels.to(device)
            logits = model(imgs)

            # Calculate loss, perform backward pass
            loss = F.cross_entropy(logits, labels)
            loss.backward()
            optimizer.step()
            optimizer.zero_grad()

            # Update logs & progress bar
            loss_list.append(loss.item())
            pbar.set_postfix(epoch=f"{epoch + 1}/{args.epochs}", loss=f"{loss:.3f}")

    return loss_list, model


args = SimpleMLPTrainingArgs()
loss_list, model = train(args)

line(
    loss_list,
    x_max=args.epochs * len(mnist_trainset),
    labels={"x": "Examples seen", "y": "Cross entropy loss"},
    title="SimpleMLP training on MNIST",
    width=700,
)
```


<details><summary>Click to see the expected output</summary>

<div style="text-align: left"><embed src="https://info-arena.github.io/ARENA_img/misc/media-02/0202.html" width="720" height="480"></div>

</details>


### Exercise - add a validation loop

> ```yaml
> Difficulty: 🔴🔴🔴⚪⚪
> Importance: 🔵🔵🔵🔵🔵
> 
> You should spend up to ~20 minutes on this exercise.
> It is very important that you understand training loops and how they work, because we'll be doing a lot of model training in this way.
> ```

Edit the `train` function above to include a validation loop. Train your model, making sure you measure the accuracy at the end of each epoch.

Here are a few tips to help you:

* You'll need a dataloader for the testset, just like we did for the trainset. It doesn't matter whether you shuffle the testset or not, because we're not updating our model parameters during validation (we usually set `shuffle=False` for testsets).
    * You can set the same batch size as for your training set (we'll discuss more optimal choices for this later in the course).
* During the validation step, you should be measuring **accuracy**, which is defined as **the fraction of correctly classified images**.
    * Note that (unlike loss) accuracy should only be logged after you've gone through the whole validation set. This is because your model doesn't update between computing different accuracies, so it doesn't make sense to log all of them separately.
    * Computing accuracy is meant to be a very short operation, so you shouldn't need a progress bar.
    * You can wrap your forward pass in `with t.inference_mode():` to make sure that your model is in inference mode during validation (i.e. gradients don't propagate).


```python
def train(args: SimpleMLPTrainingArgs) -> tuple[list[float], list[float], SimpleMLP]:
    """
    Trains the model, using training parameters from the `args` object.

    Returns:
        The model, and lists of loss & accuracy.
    """
    # YOUR CODE HERE - add a validation loop to the train function from above

    return loss_list, accuracy_list, model


args = SimpleMLPTrainingArgs()
loss_list, accuracy_list, model = train(args)

line(
    y=[loss_list, [0.1] + accuracy_list],  # we start by assuming a uniform accuracy of 10%
    use_secondary_yaxis=True,
    x_max=args.epochs * len(mnist_trainset),
    labels={"x": "Num examples seen", "y1": "Cross entropy loss", "y2": "Test Accuracy"},
    title="SimpleMLP training on MNIST",
    width=800,
)
```


<details><summary>Click to see the expected output</summary>

<div style="text-align: left"><embed src="https://info-arena.github.io/ARENA_img/misc/media-02/0203.html" width="820" height="480"></div>

</details>


<details>
<summary>Help - I'm not sure how to measure correct classifications.</summary>

You can take argmax of the output of your model, using `torch.argmax` (with the keyword argument `dim` to specify the dimension you want to take max over).

</details>

<details>
<summary>Help - I get <code>RuntimeError: expected scalar type Float but found Byte</code>.</summary>

This is commonly because one of your operations is between tensors with the wrong datatypes (e.g. `int` and `float`). You can try adding assert or logging statements in your code, or alternatively if you're in VSCode then you can try navigating to the error line and checking your dtypes using VSCode's built-in debugger.
</details>


<details><summary>Solution</summary>

```python
def train(args: SimpleMLPTrainingArgs) -> tuple[list[float], list[float], SimpleMLP]:
    """
    Trains the model, using training parameters from the `args` object.

    Returns:
        The model, and lists of loss & accuracy.
    """
    model = SimpleMLP().to(device)

    mnist_trainset, mnist_testset = get_mnist()
    mnist_trainloader = DataLoader(mnist_trainset, batch_size=args.batch_size, shuffle=True)
    mnist_testloader = DataLoader(mnist_testset, batch_size=args.batch_size, shuffle=False)

    optimizer = t.optim.Adam(model.parameters(), lr=args.learning_rate)

    loss_list = []
    accuracy_list = []
    accuracy = 0.0

    for epoch in range(args.epochs):
        # Training loop
        pbar = tqdm(mnist_trainloader)
        for imgs, labels in pbar:
            # Move data to device, perform forward pass
            imgs, labels = imgs.to(device), labels.to(device)
            logits = model(imgs)

            # Calculate loss, perform backward pass
            loss = F.cross_entropy(logits, labels)
            loss.backward()
            optimizer.step()
            optimizer.zero_grad()

            # Update logs & progress bar
            loss_list.append(loss.item())
            pbar.set_postfix(epoch=f"{epoch + 1}/{args.epochs}", loss=f"{loss:.3f}")

        # Validation loop
        num_correct_classifications = 0
        for imgs, labels in mnist_testloader:
            # Move data to device, perform forward pass in inference mode
            imgs, labels = imgs.to(device), labels.to(device)
            with t.inference_mode():
                logits = model(imgs)

            # Compute num correct by comparing argmaxed logits to true labels
            predictions = t.argmax(logits, dim=1)
            num_correct_classifications += (predictions == labels).sum().item()

        # Compute & log total accuracy
        accuracy = num_correct_classifications / len(mnist_testset)
        accuracy_list.append(accuracy)

    return loss_list, accuracy_list, model
```
</details>


You should find that after the first epoch, the model is already doing much better than random chance (i.e. >80%), and it improves slightly in subsequent epochs.




=== NEW CHAPTER ===


# 3️⃣ Convolutions



> ##### Learning Objectives
>
> * Learn how convolutions work, and why they are useful for vision models
> * Implement your own convolutions, and maxpooling layers

_Note, this section is light on exercises, because it actually ends up being surprisingly hard to implement convolutional and linear operations from scratch (unlike the case for linear layers). It requires engaging with **strides**, an under-the-hood attribute of PyTorch tensors which we usually don't think about in regular work. For this reason, this section focuses more on understanding how convolutions work & giving you implementations of it, rather than asking you to implement it from scratch. There are implementation from scratch exercises in the bonus section at the end of today's material, if you get that far!_


## Reading

We strongly recommend you at least watch the video in the first bullet point. The second article is recommended, but not essential. The third is more for interest (and will be more relevant next week, when we study interpretability).

* [But what is a convolution?](https://www.youtube.com/watch?v=KuXjwB4LzSA) by 3Blue1Brown
* [A Comprehensive Guide to Convolutional Neural Networks (Medium)](https://medium.com/towards-data-science/a-comprehensive-guide-to-convolutional-neural-networks-the-eli5-way-3bd2b1164a53)
* [Zoom In: An Introduction to Circuits](https://distill.pub/2020/circuits/zoom-in/)


## What are convolutions?

A convolution is an operation which takes a kernel and slides it across the input, applying the kernel to each patch of the input. We can view it as a logical extension of the linear layer, except rather than having every output value being determined as a linear combination of every input value, we have a **prior of locality** - assuming that the input has some spatial structure, and each output value should only be determined by a small patch of the input. The kernel contains our learned weights, and we slide that kernel across our input, with each output value being computed by a sumproduct of the kernel values and the corresponding patch in the input. Note that we use all input channels when computing each output value, which means the sumproduct is over `kernel_length * in_channels` elements (or `kernel_width * kernel_height * in_channels` when, as is most often the case, we're using 2D kernels).


### Mathematical definition

Convolutions have 4 important parameters:

- **Size** - the size of the kernel, i.e. the size of each patch of the input that the kernel is applied to when computing each output value.
- **Stride** - the distance the kernel moves each time it is applied.
- **Padding** - the number of pixels we pad around the input on each side.
- **Output channels** - the number of separate kernels of shape `(in_channels, kernel_width, kernel_height)` we apply to the input. Each separate kernel has different learned weights, and will produce a separate output channel.

Below is an illustration with `size=(3,3), stride=1, padding=1`, three input channels and a single output channel. Note that although the illustration below only shows padding on the left and top of the image, in reality we pad all sides of the image.

<img src="https://miro.medium.com/v2/resize:fit:1400/1*ciDgQEjViWLnCbmX-EeSrA.gif" width="800">

For width or height, we can compute the output dim size as a function of the input dim and convolution parameters:

$$
L_{\text {out }}=\left\lfloor\dfrac{L_{\text {in }}+2 \times \text { padding }- \text { kernel\_size }}{\text { stride }}+1\right\rfloor
$$

Notably, with our parameters `size=(3,3), stride=1, padding=1` this simplifies to $L_{\text{out}} = \left\lfloor\frac{L_{\text{in}} + 2 - 3}{1} + 1\right\rfloor = L_{\text{in}}$. We refer to this as a **shape-preserving convolution**, because the input & output dimensions for width/height are the same. This is quite useful because often when building neural networks we have to be careful to match the shapes of different tensors (otherwise skip connections will fail - we can't add together `x + conv(x)` if they're different shapes!).

> A quick note on terminology - you might see docs and docstrings use `num_features`, sometimes use `channels` (sometimes abbreviated as $N_{in}$ or $C$ in PyTorch docs). When we're talking about convolutions specifically, these usually mean the same thing.


### What do convolutions learn?

The terminology `num_features` hints at this, but often convolutions can be thought of as learning certain features from our data. For instance, there's evidence to suggest that early convolutional layers pick up on very simple low-level features such as edges, corners and curves, whereas later convolutional layers are able to combine these lower-level features hierarchically to form more complex representations.

For more on this, we recommend the Distill post [Zoom In: An Introduction to Circuits](https://distill.pub/2020/circuits/zoom-in/), which discusses various lines of evidence for interpreting the features learned by convolutional layers (and how they connect up to form circuits). Interestingly, this post philosophically underpins quite a lot of the current interpretability field - even though the focus has primarily shifted from vision models to language models, many of the underlying ideas remain the same.

<img src="https://distill.pub/2020/circuits/zoom-in/images/curves.png" width="700">


### Some questions about convolutions

Here are some questions about convolutions to make sure you've understood the material. You should try and answer these questions without referring back to the article or video above.

<details>
<summary>Why would convolutional layers be less likely to overfit data than standard linear (fully connected) layers?</summary>

Convolutional layers require significantly fewer weights to be learned. This is because the same kernel is applied all across the image, rather than every pair of `(input, output)` nodes requiring a different weight to be learned.
</details>

<details>
<summary>Suppose you fixed some random permutation of the pixels in an image, and applied this to all images in your dataset, before training a convolutional neural network for classifying images. Do you expect this to be less effective, or equally effective?</summary>

It will be less effective, because CNNs work thanks to **spatial locality** - groups of pixels close together are more meaningful. For instance, CNNs will often learn convolutions at an early layer which recognise gradients or simple shapes. If you permute the pixels (even if you permute in the same way for every image), you destroy locality.
</details>

<details>
<summary>If you have a 28x28 image, and you apply a 3x3 convolution with stride 2, padding 1, and 5 output channels, what shape will the output be?</summary>

Applying the formula above, we get:

$
L_{\text {out }}=\left\lfloor\frac{L_{\text {in }}+2 \times \text { padding }- \text { kernel\_size }}{\text { stride }}+1\right\rfloor = \left\lfloor\frac{28 + 2 \times 1 - 3}{2} + 1\right\rfloor = 14
$

So our image has width & height 14. The shape will go from `(3, 28, 28)` to `(5, 14, 14)` (since the output dimensions are `out_channels, width, height`).

As a general rule, a 3x3 convolution with padding 1, stride `stride` and input images with shape `(width, height)` will map to an output shape of `(width // stride, height // stride)`. This will be useful when we study GANs tomorrow, and we'll assemble a series of 3x3 convolutions with padding 1 and stride 2, which should each halve our input image size.

</details>


### Exercise - implement `Conv2d`

> ```yaml
> Difficulty: 🔴🔴⚪⚪⚪
> Importance: 🔵🔵🔵⚪⚪
> 
> You should spend up to 10-20 minutes on this exercise.
> This only requires you to create the conv weights - making your own fwd pass method is a bonus exercise later.
> ```

Rather than implementing the `conv2d` function from scratch, we'll allow you to use `t.nn.functional.conv2d`. In the exercise below, you should use this function to implement the `nn.Conv2d` layer. All you need to do is fill in the `__init__` method. Some guidance:

- You should look at the PyTorch page for `nn.Conv2d` [here](https://pytorch.org/docs/stable/generated/torch.nn.Conv2d.html) (and review the discussion above) to understand what the shape of the weights should be.
- We assume `bias=False`, so the only `nn.Parameter` object we need to define is `weight`.
- You should use **uniform Kaiming initialization** like you have before, i.e. the bounds of the uniform distribution should be $\pm 1/\sqrt{N_{in}}$ where $N_{in}$ is the product of input channels and kernel height & width, as described at the bottom of the `nn.Conv2d` docs (the bullet points under the **Variables** header).

<details>
<summary>Question - why do you think we use the product of input channels and kernel height & width for our Kaiming initialization bounds?</summary>

This is because each value in the output is computed by taking the product over `in_channels * kernel_height * kernel_width` elements, analogously to how each value in the linear layer is computed by taking the product over just `in_features` elements.

</details>


```python
class Conv2d(nn.Module):
    def __init__(
        self,
        in_channels: int,
        out_channels: int,
        kernel_size: int,
        stride: int = 1,
        padding: int = 0,
    ):
        """
        Same as torch.nn.Conv2d with bias=False.

        Name your weight field `self.weight` for compatibility with the PyTorch version.

        We assume kernel is square, with height = width = `kernel_size`.
        """
        super().__init__()
        self.in_channels = in_channels
        self.out_channels = out_channels
        self.kernel_size = kernel_size
        self.stride = stride
        self.padding = padding

        # YOUR CODE HERE - define & initialize `self.weight`
        raise NotImplementedError()

    def forward(self, x: Tensor) -> Tensor:
        """Apply the functional conv2d, which you can import."""
        return t.nn.functional.conv2d(x, self.weight, stride=self.stride, padding=self.padding)

    def extra_repr(self) -> str:
        keys = ["in_channels", "out_channels", "kernel_size", "stride", "padding"]
        return ", ".join([f"{key}={getattr(self, key)}" for key in keys])


tests.test_conv2d_module(Conv2d)
m = Conv2d(in_channels=24, out_channels=12, kernel_size=3, stride=2, padding=1)
print(f"Manually verify that this is an informative repr: {m}")
```


<details><summary>Solution</summary>

```python
class Conv2d(nn.Module):
    def __init__(
        self,
        in_channels: int,
        out_channels: int,
        kernel_size: int,
        stride: int = 1,
        padding: int = 0,
    ):
        """
        Same as torch.nn.Conv2d with bias=False.

        Name your weight field `self.weight` for compatibility with the PyTorch version.

        We assume kernel is square, with height = width = `kernel_size`.
        """
        super().__init__()
        self.in_channels = in_channels
        self.out_channels = out_channels
        self.kernel_size = kernel_size
        self.stride = stride
        self.padding = padding

        kernel_height = kernel_width = kernel_size
        sf = 1 / np.sqrt(in_channels * kernel_width * kernel_height)
        self.weight = nn.Parameter(sf * (2 * t.rand(out_channels, in_channels, kernel_height, kernel_width) - 1))

    def forward(self, x: Tensor) -> Tensor:
        """Apply the functional conv2d, which you can import."""
        return t.nn.functional.conv2d(x, self.weight, stride=self.stride, padding=self.padding)

    def extra_repr(self) -> str:
        keys = ["in_channels", "out_channels", "kernel_size", "stride", "padding"]
        return ", ".join([f"{key}={getattr(self, key)}" for key in keys])
```
</details>


### `MaxPool2d`

We often add a maxpool layer after a convolutional layer. This layer is responsible for reducing the spatial size of the convolved feature. It works by taking the maximum value in each kernel-sized window, and outputting that value. For instance, if we have a 2x2 kernel, then we take the maximum of each 2x2 window in the input.

Maxpool is useful for downsampling the image (reducing the total amount of data we're having to work with), as well as extracting dominant features in the image. For example, if we're training a model for classification, the model might find it useful to create a "wheel detector" to identify whether a wheel is present in the image - even if most chunks of the image don't contain a wheel, we care more about whether a wheel exists _somewhere_ in the image, and so we might only be interested in the largest values.

<img src="https://miro.medium.com/v2/resize:fit:640/format:webp/1*uoWYsCV5vBU8SHFPAPao-w.gif" width="360">

We've given you `MaxPool2d` below. This is a wrapper for the `max_pool2d` function (although in the bonus exercises later you can implement your own version of this).


```python
class MaxPool2d(nn.Module):
    def __init__(self, kernel_size: int, stride: int | None = None, padding: int = 1):
        super().__init__()
        self.kernel_size = kernel_size
        self.stride = stride
        self.padding = padding

    def forward(self, x: Tensor) -> Tensor:
        """Call the functional version of maxpool2d."""
        return F.max_pool2d(x, kernel_size=self.kernel_size, stride=self.stride, padding=self.padding)

    def extra_repr(self) -> str:
        """Add additional information to the string representation of this class."""
        return ", ".join([f"{key}={getattr(self, key)}" for key in ["kernel_size", "stride", "padding"]])
```




=== NEW CHAPTER ===


# 4️⃣ ResNets



> ##### Learning Objectives
>
> * Learn about skip connections, and how they help overcome the degradation problem
> * Learn about batch normalization, and why it is used in training
> * Assemble your own ResNet, and load in weights from PyTorch's ResNet implementation

## Reading

* [Batch Normalization in Convolutional Neural Networks](https://www.baeldung.com/cs/batch-normalization-cnn)
* [Deep Residual Learning for Image Recognition](https://arxiv.org/pdf/1512.03385.pdf)

You should move on once you can answer the following questions:


<details>
<summary>"Batch Normalization allows us to be less careful about initialization." Explain this statement.</summary>

Weight initialisation methods like Xavier (which we encountered yesterday) are based on the idea of making sure the activations have approximately the same distribution across layers at initialisation. But batch normalization ensures that this is the case as signals pass through the network.
</details>

<details>
<summary>Give at least 2 reasons why batch normalization improves the performance of neural networks.</summary>

Reasons you can give here include:

* Input normalization avoids extreme activation values, which helps stabilize gradient-based optimization methods.
* Internal covariate shift is reduced, i.e. the mean and standard deviation is kept constant across the layers.
* Regularisation effect: noise internal to each minibatch is reduced.

Note, some of these points overlap because they gesture to the same underlying ideas.

</details>

<details>
<summary>If you have an input tensor of size (batch, channels, width, height), and you apply a batchnorm layer, how many learned parameters will there be?</summary>

A mean and standard deviation is calculated for each channel (i.e. each calculation is done across the batch, width, and height dimensions). So the number of learned params will be `2 * channels`.
</details>

<details>
<summary>In the paper, the diagram shows additive skip connections (i.e. F(x) + x). One can also form concatenated skip connections, by "gluing together" F(x) and x into a single tensor. Give one advantage and one disadvantage of these, relative to additive connections.</summary>

One advantage of concatenation: the subsequent layers can re-use middle representations; maintaining more information which can lead to better performance. Also, this still works if the tensors aren't exactly the same shape. One disadvantage: less compact, so there may be more weights to learn in subsequent layers.

Crucially, both the addition and concatenation methods have the property of preserving information, to at least some degree of fidelity. For instance, you can [use calculus to show](https://theaisummer.com/skip-connections/#:~:text=residual%20skip%20connections.-,ResNet%3A%20skip%20connections%C2%A0via%C2%A0addition,-The%20core%20idea) that both methods will fix the vanishing gradients problem.
</details>


In this section, we'll do a more advanced version of the exercise in part 1. Rather than building a relatively simple network in which computation can be easily represented by a sequence of simple layers, we're going to build a more complex architecture which requires us to define nested blocks.

We'll start by defining a few more `nn.Module` objects, which we hadn't needed before.


## Sequential

Firstly, now that we're working with large and complex architectures, we should create a version of `nn.Sequential`. As the name suggests, when an `nn.Sequential` is fed an input, it sequentially applies each of its submodules to the input, with the output from one module feeding into the next one.

The implementation is given to you below. A few notes:

* In initalization, we add to the `_modules` dictionary.
    * This is a special type of dict called an **ordered dictionary**, which preserves the order of elements that get added (although Python sort-of does this now by default).
    * When we call `self.parameters()`, this recursively goes through all modules in `self._modules`, and returns the params in those modules. This means we can nest sequentials within sequentials!
* The special `__getitem__` and `__setitem__` methods determine behaviour when we get and set modules within the sequential.
* The `repr` of the base class `nn.Module` already recursively prints out the submodules, so we don't need to write anything in `extra_repr`.
    * To see how this works in practice, try defining a `Sequential` which takes a sequence of modules that you've defined above, and see what it looks like when you print it.

Don't worry about deeply understanding this code. The main takeaway is that `nn.Sequential` is a useful list-like object to store modules, and apply them all sequentially.

<details>
<summary>Aside - initializing Sequential with an OrderedDict</summary>

The actual `nn.Sequential` module can be initialized with an ordered dictionary, rather than a list of modules. For instance, rather than doing this:

```python
seq = nn.Sequential(
    nn.Linear(10, 20),
    nn.ReLU(),
    nn.Linear(20, 30)
)
```

we can do this:

```python
from collections import OrderedDict

seq = nn.Sequential(OrderedDict([
    ("linear1", nn.Linear(10, 20)),
    ("relu", nn.ReLU()),
    ("linear2", nn.Linear(20, 30))
]))
```

This is handy if we want to give each module an descriptive name.

The `Sequential` implementation below doesn't allow the input to be an OrderedDict. As a bonus exercise, can you rewrite the `__init__`, `__getitem__` and `__setitem__` methods to allow the input to be an OrderedDict? If you do this, you'll actually be able to match your eventual `ResNet` model names exactly to the PyTorch implementation.

</details>


```python
class Sequential(nn.Module):
    _modules: dict[str, nn.Module]

    def __init__(self, *modules: nn.Module):
        super().__init__()
        for index, mod in enumerate(modules):
            self._modules[str(index)] = mod

    def __getitem__(self, index: int) -> nn.Module:
        index %= len(self._modules)  # deal with negative indices
        return self._modules[str(index)]

    def __setitem__(self, index: int, module: nn.Module) -> None:
        index %= len(self._modules)  # deal with negative indices
        self._modules[str(index)] = module

    def forward(self, x: Tensor) -> Tensor:
        """Chain each module together, with the output from one feeding into the next one."""
        for mod in self._modules.values():
            x = mod(x)
        return x
```


## BatchNorm2d

Now, we'll implement our `BatchNorm2d`, the layer described in the reading material you hopefully read above. You'll be implementing it according to the [PyTorch docs](https://pytorch.org/docs/stable/generated/torch.nn.BatchNorm2d.html) (with `affine=True` and `track_running_stats=True`).

The primary function of batchnorm is to normalize the activations of each layer within the neural network during training. It normalizes each batch of input data to have a mean of 0 and std dev of 1. This normalization helps mitigate the **internal covariate shift** problem, which refers to the change in the distribution of layer inputs as the network trains. This becomes a particularly big problem as we build deeper networks, because there's more opportunity for the activation distribution to change over time.


### Buffers

A question that might have occurred to you as you read about batchnorm - how does averaging over input data work in inference mode, if you only have a single input rather than a batch? The answer is that during training mode we compute a running average of our data's mean and variance, and we use this running average in inference mode.

How do we store these moving averages? We want them to be saved and loaded with the model (because we need these values in order to run our model), but we don't want to update them using gradient descent (so we don't want to use `nn.Parameter`). So instead, we use the Pytorch **buffers** feature. These are essentially tensors which are included in `model.state_dict()` (and so they're saved & loaded with the rest of the model) but not included in `model.parameters()`.

You can create a buffer by calling [`self.register_buffer`](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module.register_buffer) from inside a `nn.Module`. We've initialized the necessary buffers for you in the `__init__` method below - you'll need a running mean and variance, as well as a counter for the number of batches seen (technically this isn't strictly necessary because the running mean & variance are updated using an exponential moving average so the update rule is independent of the number of previous updates, but we're doing this so our state dict matches the PyTorch implementation).


### Train and Eval Modes

Okay so we have buffers, but how can we make them behave differently in different modes - i.e. updating the running mean & variance in training mode, and using the stored values in eval mode? The answer is that we use the `training` method of the `nn.Module` class, which is a boolean attribute that gets flipped when we call `self.eval()` or `self.train()`. In the case of batch norm, your code should look like this:

```python
if self.training:
    # Use this data's mean & variance to normalize, then use it to update the buffers
else:
    # Use the buffer mean & variance to normalize
```

The other commonly used module which has different behaviour in training and eval modes is `Dropout` - in eval mode this module uses all its inputs, but in training it randomly selects some fraction `1 - p` of the input values to zero out and scales the remaining values by `1 / (1 - p)`. 

Note that other normalization modules we'll address later in this course like `LayerNorm` don't have different behaviour in training and eval modes, because these don't normalize over the batch dimension.


### Exercise - implement `BatchNorm2d`

> ```yaml
> Difficulty: 🔴🔴🔴⚪⚪
> Importance: 🔵🔵🔵⚪⚪
> 
> You should spend up to 15-30 minutes on this exercise.
> ```

Implement `BatchNorm2d` according to the [PyTorch docs](https://pytorch.org/docs/stable/generated/torch.nn.BatchNorm2d.html). We're implementing it with `affine=True` and `track_running_stats=True`. All the parameters are defined for you in the `__init__` method, your job will be to fill in the `forward` and `extra_repr` methods.

A few final tips:

- Remember to use `weight` and `bias` in the fwd pass, after normalizing. You should multiply by `weight` and add `bias`.
- All your tensors (`weight`, `bias`, `running_mean` and `running_var`) are vectors of length `num_features`, this should help you figure out what dimensions you're operating on.
- Remember that the shape of `x` is `(batch, num_features, height, width)` which doesn't broadcast with `(num_features,)`. The easiest way to fix this is to reshape the latter to something like `(1, num_features, 1, 1)`, or optionally just `(num_features, 1, 1)`.


```python
class BatchNorm2d(nn.Module):
    # The type hints below aren't functional, they're just for documentation
    running_mean: Float[Tensor, " num_features"]
    running_var: Float[Tensor, " num_features"]
    num_batches_tracked: Int[Tensor, ""]  # This is how we denote a scalar tensor

    def __init__(self, num_features: int, eps=1e-05, momentum=0.1):
        """
        Like nn.BatchNorm2d with track_running_stats=True and affine=True.

        Name the learnable affine parameters `weight` and `bias` in that order.
        """
        super().__init__()
        self.num_features = num_features
        self.eps = eps
        self.momentum = momentum

        self.weight = nn.Parameter(t.ones(num_features))
        self.bias = nn.Parameter(t.zeros(num_features))

        self.register_buffer("running_mean", t.zeros(num_features))
        self.register_buffer("running_var", t.ones(num_features))
        self.register_buffer("num_batches_tracked", t.tensor(0))

    def forward(self, x: Tensor) -> Tensor:
        """
        Normalize each channel.

        Compute the variance using `torch.var(x, unbiased=False)`
        Hint: you may also find it helpful to use the argument `keepdim`.

        x: shape (batch, channels, height, width)
        Return: shape (batch, channels, height, width)
        """
        raise NotImplementedError()

    def extra_repr(self) -> str:
        raise NotImplementedError()


tests.test_batchnorm2d_module(BatchNorm2d)
tests.test_batchnorm2d_forward(BatchNorm2d)
tests.test_batchnorm2d_running_mean(BatchNorm2d)
```


<details>
<summary>Help - I'm stuck on this implementation, and need a template.</summary>

The easiest way is to structure it like this (we've omitted the reshaping to make sure the mean & variance broadcasts correctly):

```python
if self.training:
    mean = ... # mean of new data
    var = ... # variance of new data
    self.running_mean = ... # update running mean using exponential moving average
    self.running_var = ... # update running variance using exponential moving average
    self.num_batches_tracked += 1
else:
    mean = self.running_mean
    var = self.running_var

x_normed = ... # normalize x using `mean` and `var` (make sure `mean` and `var` are broadcastable with `x`)
x_affine = ... # apply affine transformation from `self.weight` and `self.bias` (again, be careful of broadcasting)
return x_affine
```


</details>

<details><summary> Help - I'm not sure how to implement the <code>running_mean</code> and <code>running_var</code> formula</summary>

To track the running mean, we use an exponentially weighted moving average. The formula for this is as follows, at step $T$ the moving average is given by $$\sum_{t=1}^{T} \mu (1-\mu)^{T-t} \cdot \text{mean}_{t}.$$ We implement the exponential moving average for the running variance using the same formula.

</details>

<details>
<summary>Solution</summary>

```python
def forward(self, x: Tensor) -> Tensor:
    """
    Normalize each channel.

    Compute the variance using `torch.var(x, unbiased=False)`
    Hint: you may also find it helpful to use the argument `keepdim`.

    x: shape (batch, channels, height, width)
    Return: shape (batch, channels, height, width)
    """
    # Calculating mean and var over all dims except for the channel dim
    if self.training:
        # Take mean over all dimensions except the feature dimension
        mean = x.mean(dim=(0, 2, 3))
        var = x.var(dim=(0, 2, 3), unbiased=False)
        # Updating running mean and variance, in line with PyTorch documentation
        self.running_mean = (1 - self.momentum) * self.running_mean + self.momentum * mean
        self.running_var = (1 - self.momentum) * self.running_var + self.momentum * var
        self.num_batches_tracked += 1
    else:
        mean = self.running_mean
        var = self.running_var

    # Rearranging these so they can be broadcasted
    reshape = lambda x: einops.rearrange(x, "channels -> 1 channels 1 1")

    # Normalize, then apply affine transformation from self.weight & self.bias
    x_normed = (x - reshape(mean)) / (reshape(var) + self.eps).sqrt()
    x_affine = x_normed * reshape(self.weight) + reshape(self.bias)
    return x_affine
```

</details>


## AveragePool

Let's end our collection of `nn.Module`s with an easy one 🙂

The ResNet has a Linear layer with 1000 outputs at the end in order to produce classification logits for each of the 1000 classes. Any Linear needs to have a constant number of input features, but the ResNet is supposed to be compatible with arbitrary height and width, so we can't just do a pooling operation with a fixed kernel size and stride.

Luckily, the simplest possible solution works decently: take the mean over the spatial dimensions. Intuitively, each position has an equal "vote" for what objects it can "see".


### Exercise - implement `AveragePool`

> ```yaml
> Difficulty: 🔴⚪⚪⚪⚪
> Importance: 🔵🔵⚪⚪⚪
> 
> You should spend up to 5-10 minutes on this exercise.
> ```

This should be a pretty straightforward implementation; it doesn't have any weights or parameters of any kind, so you only need to implement the `forward` method.


```python
class AveragePool(nn.Module):
    def forward(self, x: Tensor) -> Tensor:
        """
        x: shape (batch, channels, height, width)
        Return: shape (batch, channels)
        """
        raise NotImplementedError()


tests.test_averagepool(AveragePool)
```


<details><summary>Solution</summary>

```python
class AveragePool(nn.Module):
    def forward(self, x: Tensor) -> Tensor:
        """
        x: shape (batch, channels, height, width)
        Return: shape (batch, channels)
        """
        return t.mean(x, dim=(2, 3))
```
</details>


## Building ResNet

Now we have all the building blocks we need to start assembling your own ResNet! The following diagram describes the architecture of ResNet34 - the other versions are broadly similar.

Note - unless otherwise noted, you should assume convolutions have `kernel_size=3, stride=1, padding=1` (this is a **shape preserving convolution** i.e. the width & height of the input and output will be the same). None of the convolutions have biases.

You don't have to understand every detail in this diagram before proceeding; specific points will be clarified as we go through each exercise.

<details>
<summary>Question: why do we not care about including biases in the convolutional layers?</summary>

Every convolution layer in this network is followed by a batch normalization layer. The first operation in the batch normalization layer is to subtract the mean of each output channel. But a convolutional bias just adds some scalar `b` to each output channel, increasing the mean by `b`. This means that for any `b` added, the batch normalization will subtract `b` to exactly negate the bias term.
</details>

<details>
<summary>Help - I'm confused about how the nested subgraphs work.</summary>

The right-most block in the diagram, `ResidualBlock`, is nested inside `BlockGroup` multiple times. When you see `ResidualBlock` in `BlockGroup`, you should visualise a copy of `ResidualBlock` sitting in that position.
    
Similarly, `BlockGroup` is nested multiple times (four to be precise) in the full `ResNet34` architecture.
</details>

<img src="https://raw.githubusercontent.com/info-arena/ARENA_img/main/misc/resnet-fixed.svg" width="900">


### Exercise - implement `ResidualBlock`

> ```yaml
> Difficulty: 🔴🔴🔴🔴⚪
> Importance: 🔵🔵🔵🔵⚪
> 
> You should spend up to 20-30 minutes on this exercise.
> ```

Implement `ResidualBlock` by referring to the diagram (i.e. the right-most of the three hierarchical diagrams above).

The **left branch** starts with a strided convolution which changes the number of features from `in_feats` to `out_feats`. It has all conv parameters default i.e. `kernel_size=3, stride=1, padding=1` except for the stride which is instead given by `first_stride`. The second convolution has all default parameters, and maps from `out_feats` to `out_feats` (meaning it's fully shape preserving).

As for the **right branch** - this is meant to essentially be a skip connection, the problem is we can't just use a skip connection because the shapes might not match up (and so we couldn't add them together at the end). The left branch is fully shape preserving if and only if `first_stride == 1` and `in_feats == out_feats`. If this is true then we do set the right branch to be the identity (that's what the "OPTIONAL" annotation refers to), but if this isn't true then we set the right branch to be a 1x1 convolution with stride `first_stride`, zero padding, and mapping from `in_feats` to `out_feats`, followed by a batchnorm layer. This is in a sense the simplest operation we can get which matches the left branch shape, since the convolution is basically just a downsampling operation (keeping pixels based on a `::first_stride` slice across the height and width dimensions).


```python
class ResidualBlock(nn.Module):
    def __init__(self, in_feats: int, out_feats: int, first_stride=1):
        """
        A single residual block with optional downsampling.

        For compatibility with the pretrained model, declare the left side branch first using a
        `Sequential`.

        If first_stride is > 1, this means the optional (conv + bn) should be present on the right
        branch. Declare it second using another `Sequential`.
        """
        super().__init__()
        is_shape_preserving = (first_stride == 1) and (in_feats == out_feats)  # determines if right branch is identity

        raise NotImplementedError()

    def forward(self, x: Tensor) -> Tensor:
        """
        Compute the forward pass. If no downsampling block is present, the addition should just add
        the left branch's output to the input.

        x: shape (batch, in_feats, height, width)

        Return: shape (batch, out_feats, height / stride, width / stride)
        """
        raise NotImplementedError()


tests.test_residual_block(ResidualBlock)
```


<details><summary>Solution</summary>

```python
class ResidualBlock(nn.Module):
    def __init__(self, in_feats: int, out_feats: int, first_stride=1):
        """
        A single residual block with optional downsampling.

        For compatibility with the pretrained model, declare the left side branch first using a
        `Sequential`.

        If first_stride is > 1, this means the optional (conv + bn) should be present on the right
        branch. Declare it second using another `Sequential`.
        """
        super().__init__()
        is_shape_preserving = (first_stride == 1) and (in_feats == out_feats)  # determines if right branch is identity

        self.left = Sequential(
            Conv2d(in_feats, out_feats, kernel_size=3, stride=first_stride, padding=1),
            BatchNorm2d(out_feats),
            ReLU(),
            Conv2d(out_feats, out_feats, kernel_size=3, stride=1, padding=1),
            BatchNorm2d(out_feats),
        )
        self.right = (
            nn.Identity()
            if is_shape_preserving
            else Sequential(
                Conv2d(in_feats, out_feats, kernel_size=1, stride=first_stride),
                BatchNorm2d(out_feats),
            )
        )
        self.relu = ReLU()

    def forward(self, x: Tensor) -> Tensor:
        """
        Compute the forward pass. If no downsampling block is present, the addition should just add
        the left branch's output to the input.

        x: shape (batch, in_feats, height, width)

        Return: shape (batch, out_feats, height / stride, width / stride)
        """
        x_left = self.left(x)
        x_right = self.right(x)
        return self.relu(x_left + x_right)
```
</details>


### Exercise - implement `BlockGroup`

> ```yaml
> Difficulty: 🔴🔴🔴⚪⚪
> Importance: 🔵🔵🔵🔵⚪
> 
> You should spend up to 10-15 minutes on this exercise.
> ```

Implement `BlockGroup` according to the diagram. There should be `n_blocks` total blocks in the group. Only the first block has the possibility of having a right branch (because we might have either `first_stride > 1` or `in_feats != out_feats`), but every subsequent block will have the identity instead of a right branch.

<details>
<summary>Help - I don't understand why all blocks after the first one won't have a right branch.</summary>

- The `first_stride` argument only gets applied to the first block, definitionally (i.e. the purpose of the `BlockGroup` is to downsample the input by `first_stride` just once, not on every single block).
- After we pass through the first block we can guarantee that the number of channels will be `out_feats`, so every subsequent block will have `out_feats` input channels and `out_feats` output channels.

Combining these two facts, we see that every subsequent block will have a shape-preserving left branch, so it can have the identity as its right branch.

</details>


```python
class BlockGroup(nn.Module):
    def __init__(self, n_blocks: int, in_feats: int, out_feats: int, first_stride=1):
        """
        An n_blocks-long sequence of ResidualBlock where only the first block uses the provided
        stride.
        """
        super().__init__()
        # YOUR CODE HERE - define all components of block group
        raise NotImplementedError()

    def forward(self, x: Tensor) -> Tensor:
        """
        Compute the forward pass.

        x: shape (batch, in_feats, height, width)

        Return: shape (batch, out_feats, height / first_stride, width / first_stride)
        """
        raise NotImplementedError()


tests.test_block_group(BlockGroup)
```


<details><summary>Solution</summary>

```python
class BlockGroup(nn.Module):
    def __init__(self, n_blocks: int, in_feats: int, out_feats: int, first_stride=1):
        """
        An n_blocks-long sequence of ResidualBlock where only the first block uses the provided
        stride.
        """
        super().__init__()
        self.blocks = Sequential(
            ResidualBlock(in_feats, out_feats, first_stride),
            *[ResidualBlock(out_feats, out_feats) for _ in range(n_blocks - 1)],
        )

    def forward(self, x: Tensor) -> Tensor:
        """
        Compute the forward pass.

        x: shape (batch, in_feats, height, width)

        Return: shape (batch, out_feats, height / first_stride, width / first_stride)
        """
        return self.blocks(x)
```
</details>


### Exercise - implement `ResNet34`

> ```yaml
> Difficulty: 🔴🔴🔴🔴⚪
> Importance: 🔵🔵🔵🔵⚪
> 
> You should spend up to 30-45 minutes on this exercise. This can sometimes involve a lot of fiddly debugging.
> ```

Last step! Assemble `ResNet34` using the diagram.

To test your implementation, you can use the helper function `print_param_count` which prints out a stylized dataframe comparing your model's parameter count to the PyTorch implementation. Alternatively, you can use the following code to import your own `resnet34`, and inspect its architecture:

```python
resnet = models.resnet34()
print(torchinfo.summary(resnet, input_size=(1, 3, 64, 64)))
print(torchinfo.summary(my_resnet, input_size=(1, 3, 64, 64)))
```

Both will give you the shape & size of each of your model's parameters & buffers, and code is provided for both of these methods below.

Note - in order to copy weights from the reference model to your implementation (which we'll do after this exercise), you'll need to have all the parameters defined in the same order as they are in the reference model - in other words, the rows from the two halves of the dataframe created via `print_param_count` should perfectly match up with each other. This can be a bit fiddly to get right, especially if the names of your parameters are different to the names in the PyTorch implementation. We recommend you look at the `__init__` methods of the solution if you're stuck (since it's the order that things are defined in for the various ResNet modules which determines the order of the rows in the dataframe).

This 1-to-1 weight comparison won't always be possible during model replications, for example when we replicate GPT2-Small next week we'll be defining the attention weight matrices differently (in a way that's more condusive to interpretability research). In these cases, you'll need to resort to different debugging methods, like running the models on the same input and checking they give the same output. You can also break this down into smaller steps by running individual models, and by checking the shape before checking values. However in this case we don't need to resort to that, because our implementation is equivalent to the reference model's implementation.

As a more general point, tweaking your model until all the layers match up might be a difficult and frustrating exercise at times, however it's a pretty good example of the kind of low-level model implementation and debugging that is important for your growth as ML engineers! So don't be disheartened if you find it hard to get exactly right (although we certainly recommend looking at the solutions and moving on if you're stuck on this particular exercise for more than ~45 minutes).


```python
class ResNet34(nn.Module):
    def __init__(
        self,
        n_blocks_per_group=[3, 4, 6, 3],
        out_features_per_group=[64, 128, 256, 512],
        first_strides_per_group=[1, 2, 2, 2],
        n_classes=1000,
    ):
        super().__init__()
        out_feats0 = 64
        self.n_blocks_per_group = n_blocks_per_group
        self.out_features_per_group = out_features_per_group
        self.first_strides_per_group = first_strides_per_group
        self.n_classes = n_classes

        # YOUR CODE HERE - define all components of resnet34
        raise NotImplementedError()

    def forward(self, x: Tensor) -> Tensor:
        """
        x: shape (batch, channels, height, width)
        Return: shape (batch, n_classes)
        """
        raise NotImplementedError()


my_resnet = ResNet34()

# (1) Test via helper function `print_param_count`
target_resnet = models.resnet34()  # without supplying a `weights` argument, we just initialize with random weights
utils.print_param_count(my_resnet, target_resnet)

# (2) Test via `torchinfo.summary`
print("My model:", torchinfo.summary(my_resnet, input_size=(1, 3, 64, 64)), sep="\n")
print(
    "\nReference model:",
    torchinfo.summary(target_resnet, input_size=(1, 3, 64, 64), depth=2),
    sep="\n",
)
```


<details>
<summary>Help - I'm not sure how to construct each of the BlockGroups.</summary>

Each BlockGroup takes arguments `n_blocks`, `in_feats`, `out_feats` and `first_stride`. In the initialisation of `ResNet34` below, we're given a list of `n_blocks`, `out_feats` and `first_stride` for each of the BlockGroups. To find `in_feats` for each block, it suffices to note two things:
    
1. The first `in_feats` should be 64, because the input is coming from the convolutional layer with 64 output channels.
2. The `out_feats` of each layer should be equal to the `in_feats` of the subsequent layer (because the BlockGroups are stacked one after the other; with no operations in between to change the shape).

You can use these two facts to construct a list `in_features_per_group`, and then create your BlockGroups by zipping through all four lists.
</details>

<details>
<summary>Help - I'm not sure how to construct the 7x7 conv at the very start.</summary>

The stride, padding & output channels are givin in the diagram; the only thing not provided is `in_channels`. Recall that the input to this layer is an RGB image - can you deduce from this how many input channels your layer should have?

</details>

<details>
<summary>Help - I'm getting the right total parameter count, but my rows don't match up, and I'm not sure how to debug this.</summary>

We'll use an example case to illustrate how to debug this. In the following case, our rows match up until the 21st row where we have our first discrepancy:

<img src="https://raw.githubusercontent.com/info-arena/ARENA_img/main/misc/row-diff.png" width="1000">

We can see that the first discrepancy occurs at the first parameter from `residual_layers.1`, meaning something in the second `BlockGroup` in our sequential of blockgroups. We can see that the first blockgroup only had left branches but no right branches (this is because for the very first blockgroup we had `in_feats == out_feats == 64` and also `first_strides_per_group[0] == 1`, meaning this first blockgroup was shape-preserving and it didn't need a right branch). So it's the presence of a right branch that's causing the mismatch.

Looking closer at the dataframe, we see that the left-hand parameter (from our model) has shape `(128, 64, 1, 1)` and has `right` in its name, so we deduce it's the 1x1 convolutional weight from the right branch. But the parameter from the PyTorch model has shape `(128, 64, 3, 3)`, i.e. it's a convolutional weight with a 3x3 kernel, so must be from the left branch (it also matches the naming convention for the left-branch convolutional weight from the first blockgroup - row index 3 in the dataframe). So we've now figured out what the problem is: **your implementation defines the right branch before the left branch in the the `ResidualBlock.__init__` method, and to match param orders with the PyTorch model you should swap them around.**

</details>


<details><summary>Solution</summary>

```python
class ResNet34(nn.Module):
    def __init__(
        self,
        n_blocks_per_group=[3, 4, 6, 3],
        out_features_per_group=[64, 128, 256, 512],
        first_strides_per_group=[1, 2, 2, 2],
        n_classes=1000,
    ):
        super().__init__()
        out_feats0 = 64
        self.n_blocks_per_group = n_blocks_per_group
        self.out_features_per_group = out_features_per_group
        self.first_strides_per_group = first_strides_per_group
        self.n_classes = n_classes

        self.in_layers = Sequential(
            Conv2d(3, out_feats0, kernel_size=7, stride=2, padding=3),
            BatchNorm2d(out_feats0),
            ReLU(),
            MaxPool2d(kernel_size=3, stride=2, padding=1),
        )

        residual_layers = []
        for i in range(len(n_blocks_per_group)):
            residual_layers.append(
                BlockGroup(
                    n_blocks=n_blocks_per_group[i],
                    in_feats=[64, *self.out_features_per_group][i],
                    out_feats=self.out_features_per_group[i],
                    first_stride=self.first_strides_per_group[i],
                )
            )
        self.residual_layers = Sequential(*residual_layers)

        self.out_layers = Sequential(
            AveragePool(),
            Linear(out_features_per_group[-1], n_classes),
        )

    def forward(self, x: Tensor) -> Tensor:
        """
        x: shape (batch, channels, height, width)
        Return: shape (batch, n_classes)
        """
        post_first_conv_block = self.in_layers(x)
        post_block_groups = self.residual_layers(post_first_conv_block)
        logits = self.out_layers(post_block_groups)
        return logits
```
</details>


### Copying over weights

Now that you've built your `ResNet34`, we'll copy weights over from PyTorch's pretrained resnet to yours. This is another good way to verify that you've designed the architecture correctly (although if you've passed all tests above and your parameter count order matches up, it's very likely that this code will also work).


```python
def copy_weights(my_resnet: ResNet34, pretrained_resnet: models.resnet.ResNet) -> ResNet34:
    """Copy over the weights of `pretrained_resnet` to your resnet."""

    # Get the state dictionaries for each model, check they have the same number of parameters &
    # buffers
    mydict = my_resnet.state_dict()
    pretraineddict = pretrained_resnet.state_dict()
    assert len(mydict) == len(pretraineddict), "Mismatching state dictionaries."

    # Define a dictionary mapping the names of your parameters / buffers to their values in the
    # pretrained model
    state_dict_to_load = {
        mykey: pretrainedvalue
        for (mykey, myvalue), (pretrainedkey, pretrainedvalue) in zip(mydict.items(), pretraineddict.items())
    }

    # Load in this dictionary to your model
    my_resnet.load_state_dict(state_dict_to_load)

    return my_resnet


pretrained_resnet = models.resnet34(weights=models.ResNet34_Weights.IMAGENET1K_V1).to(device)
my_resnet = copy_weights(my_resnet, pretrained_resnet).to(device)
print("Weights copied successfully!")
```


<details><summary>Click to see the expected output</summary>

<Bdiv style="text-align: left"><embed src="https://info-arena.github.io/ARENA_img/misc/media-02/0202-table.html" width="940" height="420"></div>

</details>


This function uses the `state_dict()` method, which returns an  `OrderedDict` (documentation [here](https://realpython.com/python-ordereddict/)) object containing all the parameter/buffer names and their values. State dicts can be extracted from models, saved to your filesystem (this is a common way to store the results of training a model), and can also be loaded back into a model using the `load_state_dict` method. (Note that you can also load weights using a regular Python `dict`, but since Python 3.7, the builtin `dict` is guaranteed to maintain items in the order they're inserted.)


## Running Your Model

We've provided you with some images for your model to classify:


```python
IMAGE_FILENAMES = [
    "chimpanzee.jpg",
    "golden_retriever.jpg",
    "platypus.jpg",
    "frogs.jpg",
    "fireworks.jpg",
    "astronaut.jpg",
    "iguana.jpg",
    "volcano.jpg",
    "goofy.jpg",
    "dragonfly.jpg",
]

IMAGE_FOLDER = section_dir / "resnet_inputs"

images = [Image.open(IMAGE_FOLDER / filename) for filename in IMAGE_FILENAMES]
```


Our `images` are of type `PIL.Image.Image`, so we can just call them in a cell to display them, or alternatively use a function like IPython's `display`:


```python
display(images[0])
```


<img src="https://raw.githubusercontent.com/callummcdougall/ARENA_3.0/refs/heads/main/chapter0_fundamentals/exercises/part2_cnns/resnet_inputs/chimpanzee.jpg" width="750">


We now need to define a `transform` object like we did for MNIST. We will use the same transforms to convert the PIL image to a tensor, and to normalize it. But we also want to resize the images to `height=224, width=224`, because not all of them start out with this size and we need them to be consistent before passing them through our model.

In the normalization step, we'll use a mean of `[0.485, 0.456, 0.406]`, and a standard deviation of `[0.229, 0.224, 0.225]` (these are the mean and std dev of images from [ImageNet](https://www.image-net.org/)). Note that the means and std devs have three elements, because ImageNet contains RGB rather than monochrome images, and we're normalising over each of the three RGB channels separately.


```python
IMAGE_SIZE = 224
IMAGENET_MEAN = [0.485, 0.456, 0.406]
IMAGENET_STD = [0.229, 0.224, 0.225]

IMAGENET_TRANSFORM = transforms.Compose(
    [
        transforms.ToTensor(),
        transforms.Resize((IMAGE_SIZE, IMAGE_SIZE)),
        transforms.Normalize(mean=IMAGENET_MEAN, std=IMAGENET_STD),
    ]
)

prepared_images = t.stack([IMAGENET_TRANSFORM(img) for img in images], dim=0).to(device)
assert prepared_images.shape == (len(images), 3, IMAGE_SIZE, IMAGE_SIZE)
```


### Exercise - verify your model's predictions

> ```yaml
> Difficulty: 🔴🔴⚪⚪⚪
> Importance: 🔵🔵🔵⚪⚪
> 
> You should spend up to ~10 minutes on this exercise.
> ```

Lastly, you should run your model with these prepared images, and verify that your predictions are the same as the model's predictions.

You can do this by filling in the `predict` function below, then running the code. We've also provided you with a file `imagenet_labels.json` which you can use to get the actual classnames of imagenet data, and see what your model's predictions actually are. 

When you run the code, you should find that your top prediction probabilities are within about 0.01% of the reference model's probabilities most (not all) of the time. This kind of error is not uncommon when you have slightly different orders of linear operations or small implementation details which differ between models, and which can introduce floating point errors that compound as we move through the model. As a bonus exercise (which may or may not break your sanity), you're welcome to try and work through our implementation, comparing it to the PyTorch model's implementation and find where the discrepancy comes from!

*Tip - the torch method `torch.max` will return a tuple of (values, indices) if you supply a dimension argument `dim`.*


```python
@t.inference_mode()
def predict(
    model: nn.Module, images: Float[Tensor, "batch rgb h w"]
) -> tuple[Float[Tensor, " batch"], Int[Tensor, " batch"]]:
    """
    Returns the maximum probability and predicted class for each image, as a tensor of floats and
    ints respectively.
    """
    model.eval()
    raise NotImplementedError()


with open(section_dir / "imagenet_labels.json") as f:
    imagenet_labels = list(json.load(f).values())

# Check your predictions match those of the pretrained model
my_probs, my_predictions = predict(my_resnet, prepared_images)
pretrained_probs, pretrained_predictions = predict(pretrained_resnet, prepared_images)
assert (my_predictions == pretrained_predictions).all()
t.testing.assert_close(my_probs, pretrained_probs, atol=5e-4, rtol=0)  # tolerance of 0.05%
print("All predictions match!")

# Print out your predictions, next to the corresponding images
for i, img in enumerate(images):
    table = Table("Model", "Prediction", "Probability")
    table.add_row("My ResNet", imagenet_labels[my_predictions[i]], f"{my_probs[i]:.3%}")
    table.add_row(
        "Reference Model",
        imagenet_labels[pretrained_predictions[i]],
        f"{pretrained_probs[i]:.3%}",
    )
    rprint(table)
    display(img)
```


<details><summary>Click to see the expected output (for first image)</summary>

<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">┏━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━┓
┃<span style="font-weight: bold"> Model           </span>┃<span style="font-weight: bold"> Prediction                         </span>┃<span style="font-weight: bold"> Probability </span>┃
┡━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━┩
│ My ResNet       │ chimpanzee, chimp, Pan troglodytes │ 90.515%     │
│ Reference Model │ chimpanzee, chimp, Pan troglodytes │ 90.513%     │
└─────────────────┴────────────────────────────────────┴─────────────┘
</pre>

<img src="https://raw.githubusercontent.com/callummcdougall/ARENA_3.0/refs/heads/main/chapter0_fundamentals/exercises/part2_cnns/resnet_inputs/chimpanzee.jpg" width="750">

</details>


<details>
<summary>Help! My model is predicting roughly the same percentage for every category!</summary>

This can indicate that your model weights are randomly initialized, meaning the weight loading process didn't actually take. Or, you reinitialized your model by accident after loading the weights.
</details>


<details><summary>Solution</summary>

```python
@t.inference_mode()
def predict(
    model: nn.Module, images: Float[Tensor, "batch rgb h w"]
) -> tuple[Float[Tensor, " batch"], Int[Tensor, " batch"]]:
    """
    Returns the maximum probability and predicted class for each image, as a tensor of floats and
    ints respectively.
    """
    model.eval()
    logits = model(images)
    probabilities = logits.softmax(dim=-1)
    return probabilities.max(dim=-1)
```
</details>


If you've done everything correctly, your version should give the same classifications, and the percentages should match at least to a couple decimal places.

If it does, congratulations, you've now run an entire ResNet, using barely any code from `torch.nn`! The only things we used were `nn.Module` and `nn.Parameter`.

If it doesn't, you get to practice model debugging! Remember to use the `utils.print_param_count` function that was provided.


### Aside - hooks

One problem you might have encountered is that your model outputs `NaN`s rather than actual numbers. When debugging this, it's useful to try and identify which module the error first appears in. This is a great use-case for **hooks**, which are something we'll be digging a lot more into during our mechanistic interpretability exercises later on.

A hook is basically a function which you can attach to a particular `nn.Module`, which gets executed during your model's forward or backward passes. Here, we'll only consider forward hooks. A hook function's type signature is:

```python
def hook(module: nn.Module, inputs: list[Tensor], output: Tensor) -> None:
    pass
```

The `inputs` argument is a list of the inputs to the module (often just one tensor), and the `output` argument is the output of the module. This hook gets registered to a module by calling `module.register_forward_hook(hook)`. During forward passes, the hook function will run.

Here is some code which will check for `NaN`s in the output of each module, and raise a `ValueError` if it finds any. We've also given you an example tiny network which produces a `NaN` in the output of the second layer, to demonstrate it on.


```python
class NanModule(nn.Module):
    """
    Define a module that always returns NaNs (we will use hooks to identify this error).
    """

    def forward(self, x):
        return t.full_like(x, float("nan"))


def hook_check_for_nan_output(module: nn.Module, input: tuple[Tensor], output: Tensor) -> None:
    """
    Hook function which detects when the output of a layer is NaN.
    """
    if t.isnan(output).any():
        raise ValueError(f"NaN output from {module}")


def add_hook(module: nn.Module) -> None:
    """
    Register our hook function in a module.

    Use model.apply(add_hook) to recursively apply the hook to model and all submodules.
    """
    module.register_forward_hook(hook_check_for_nan_output)


def remove_hooks(module: nn.Module) -> None:
    """
    Remove all hooks from module.

    Use module.apply(remove_hooks) to do this recursively.
    """
    module._backward_hooks.clear()
    module._forward_hooks.clear()
    module._forward_pre_hooks.clear()


# Create our model with a NaN in the middle, and apply a hook fn to it which checks for NaNs
model = nn.Sequential(nn.Identity(), NanModule(), nn.Identity())
model = model.apply(add_hook)

# Run the model, and our hook function should raise an error that gets caught by the try-except
try:
    input = t.randn(3)
    output = model(input)
except ValueError as e:
    print(e)

# Remove hooks at the end
model = model.apply(remove_hooks)
```


When you run this code, you should find it raising an error at the `NanModule`.


> Important - when you're working with PyTorch hooks, make sure you **remember to remove them at the end of each use**! This is a classic source of bugs, and one of the things that make PyTorch hooks so janky. When we study TransformerLens in the next chapter, we'll use a version of hooks that is essentially the same under the hood, but comes with quite a few quality of life improvements!




=== NEW CHAPTER ===


# ☆ Bonus - Feature Extraction



> ##### Learning Objectives
>
> * Understand the difference between feature extraction and finetuning
> * Perform feature extraction on a pre-trained ResNet

Now that you've seen how to build a modular training loop, and you've seen how ResNet works and is built, we're going to put these two things together to finetune a ResNet model on a new dataset.

**Finetuning** can mean slightly different things in different contexts, but broadly speaking it means using the weights of an already trained network as the starting values for training a new network. Because training networks from scratch is very computationally expensive, this is a common practice in ML.

The specific type of finetuning we'll be doing here is called **feature extraction**. This is when we freeze most layers of a model except the last few, and perform gradient descent on those. We call this feature extraction because the earlier layers of the model have already learned to identify important features of the data (and these features are also relevant for the new task), so all that we have to do is train a few final layers in the model to extract these features.

*Terminology note - sometimes feature extraction and finetuning are defined differently, with finetuning referring to the training of all the weights in a pretrained model (usually with a small or decaying learning rate), and feature extraction referring to the freezing of some layers and training of others. To avoid confusion here, we'll use the term "feature extraction" rather than "finetuning".*

<img src="https://raw.githubusercontent.com/info-arena/ARENA_img/main/misc/feature_extraction.png" width="400">

How do we prepare a model for feature extraction? By **freezing layers** of our model.

We'll discuss freezing layers & the backpropagation algorithm in much more detail tomorrow, but for now it's fine to just understand what's going on at a basic level. When we call `loss.backward()` in our training loop (or when this is implicitly called by our PyTorch Lightning trainer), this propagates gradients from our `loss` scalar back to all parameters in our model. If a parameter has its `requires_grad` attribute set to `False`, it means gradients won't be computed for this tensor during backpropagation. Thanks to PyTorch helpfully keeping track of the parameters which require gradients (using a structure called the **computational graph**), if we set `requires_grad = False` for the first few layers of parameters in our model, PyTorch will actually save us time and compute by not calculating gradients for these parameters at all.

See the code below as an example of how gradient propagation stops at tensors with `requires_grad = False`.


```python
layer0, layer1 = nn.Linear(3, 4), nn.Linear(4, 5)

layer0.requires_grad_(False)  # generic code to set `param.requires_grad=False` recursively for a module / entire model

x = t.randn(3)
out = layer1(layer0(x)).sum()
out.backward()

assert layer0.weight.grad is None
assert layer1.weight.grad is not None
```


### Exercise - prepare ResNet for feature extraction

> ```yaml
> Difficulty: 🔴🔴🔴⚪⚪
> Importance: 🔵🔵🔵⚪⚪
> 
> You should spend up to 15-20 minutes on this exercise.
> ```

First, you should complete the function below to do the following:

* Instantiate a `ResNet34` model using your class, and copy in weights from a pretrained model (you can use code from earlier here)
* Disable gradients for all layers
* Replace the final linear layer with a new linear layer, which has the same number of `in_features`, but a different number of `out_features` (given by the `n_classes` argument).


```python
def get_resnet_for_feature_extraction(n_classes: int) -> ResNet34:
    """
    Creates a ResNet34 instance, replaces its final linear layer with a classifier for `n_classes`
    classes, and freezes all weights except the ones in this layer.

    Returns the ResNet model.
    """
    raise NotImplementedError()


tests.test_get_resnet_for_feature_extraction(get_resnet_for_feature_extraction)
```


<details><summary>Solution</summary>

```python
def get_resnet_for_feature_extraction(n_classes: int) -> ResNet34:
    """
    Creates a ResNet34 instance, replaces its final linear layer with a classifier for `n_classes`
    classes, and freezes all weights except the ones in this layer.

    Returns the ResNet model.
    """
    # Create a ResNet34 with the default number of classes
    my_resnet = ResNet34()

    # Load the pretrained weights
    pretrained_resnet = models.resnet34(weights=models.ResNet34_Weights.IMAGENET1K_V1)

    # Copy the weights over
    my_resnet = copy_weights(my_resnet, pretrained_resnet)

    # Freeze grads for all layers
    my_resnet.requires_grad_(False)

    # Redefine last layer, with new number of classes (this unfreezes the last layer)
    my_resnet.out_layers[-1] = Linear(my_resnet.out_features_per_group[-1], n_classes)

    return my_resnet
```
</details>


We'll now give you some boilerplate code to load in and transform your data (this is pretty similar to the MNIST code).


```python
def get_cifar() -> tuple[datasets.CIFAR10, datasets.CIFAR10]:
    """Returns CIFAR-10 train and test sets."""
    cifar_trainset = datasets.CIFAR10(exercises_dir / "data", train=True, download=True, transform=IMAGENET_TRANSFORM)
    cifar_testset = datasets.CIFAR10(exercises_dir / "data", train=False, download=True, transform=IMAGENET_TRANSFORM)
    return cifar_trainset, cifar_testset


@dataclass
class ResNetTrainingArgs:
    batch_size: int = 64
    epochs: int = 5
    learning_rate: float = 1e-3
    n_classes: int = 10
```


The dataclass we've defined containing training arguments is basically the same as the one we had for the convnet, the main difference is that we're now using the [CIFAR-10 dataset](https://www.cs.toronto.edu/~kriz/cifar.html). This is the dataset we'll be training our model on. It consists of 60000 32x32 colour images in 10 classes, with 6000 images per class. See the link for more information.


### Exercise - write training loop for feature extraction

> ```yaml
> Difficulty: 🔴🔴🔴⚪⚪
> Importance: 🔵🔵🔵⚪⚪
> 
> You should spend up to 15-25 minutes on this exercise.
> ```

We now come to the final task - write a training loop for your ResNet model. This shouldn't be too difficult because most of the code can be directly taken from the exercise in section 2️⃣, however there are a few changes you should take note of:

- Since all other parameters' gradients have been frozen, it doesn't really matter which parameters you pass to your optimizer. However, note that you have the option of passing just a subset of parameters using e.g. `AdamW(model.some_module.parameters(), ...)`.
- Now that we're working with batchnorm, you'll have to call `model.train()` and `model.eval()` before your training and validation loops (recall that the behaviour of batchnorm changes between training and eval modes).
- Make sure you're connected to GPU runtime rather than CPU, otherwise this training might take quite a while. 
- Also make sure you're logging progress within each epoch, since the epochs might each take a while (although we've given you the `get_cifar_subset` function which returns a subset of the CIFAR10 data, and we recommend using this function with default parameters so that each epoch is a bit faster).


```python
from torch.utils.data import Subset


def get_cifar_subset(trainset_size: int = 10_000, testset_size: int = 1_000) -> tuple[Subset, Subset]:
    """Returns a subset of CIFAR-10 train & test sets (slicing the first examples)."""
    cifar_trainset, cifar_testset = get_cifar()
    return Subset(cifar_trainset, range(trainset_size)), Subset(cifar_testset, range(testset_size))


def train(args: ResNetTrainingArgs) -> tuple[list[float], list[float], ResNet34]:
    """
    Performs feature extraction on ResNet, returning the model & lists of loss and accuracy.
    """
    # YOUR CODE HERE - write your train function for feature extraction
    raise NotImplementedError()


args = ResNetTrainingArgs()
loss_list, accuracy_list, model = train(args)

line(
    y=[
        loss_list,
        [1 / args.n_classes] + accuracy_list,
    ],  # we start by assuming a uniform accuracy of 10%
    use_secondary_yaxis=True,
    x_max=args.epochs * 10_000,
    labels={"x": "Num examples seen", "y1": "Cross entropy loss", "y2": "Test Accuracy"},
    title="ResNet Feature Extraction",
    width=800,
)
```


<details><summary>Click to see the expected output</summary>

<div style="text-align: left"><embed src="https://info-arena.github.io/ARENA_img/misc/media-02/0204.html" width="820" height="480"></div>

</details>


<details>
<summary>Spoilers - what kind of results should you get?</summary>

If you train the whole model rather than just the final layer, you should find accuracy increases very slowly, not getting very far above random chance. This reflects the fact that the model is trying to learn a new task (classifying images into 10 classes) from scratch, rather than just learning to extract features from images, and this takes a long time!

If you train just the final layer, your accuracy should reach around 70-80% by the first epoch. This is because the model is already very good at extracting features from images, and it just needs to learn how to turn these features into predictions for this new set of classes.

</details>


<details><summary>Solution</summary>

```python
from torch.utils.data import Subset


def get_cifar_subset(trainset_size: int = 10_000, testset_size: int = 1_000) -> tuple[Subset, Subset]:
    """Returns a subset of CIFAR-10 train & test sets (slicing the first examples)."""
    cifar_trainset, cifar_testset = get_cifar()
    return Subset(cifar_trainset, range(trainset_size)), Subset(cifar_testset, range(testset_size))


def train(args: ResNetTrainingArgs) -> tuple[list[float], list[float], ResNet34]:
    """
    Performs feature extraction on ResNet, returning the model & lists of loss and accuracy.
    """
    model = get_resnet_for_feature_extraction(args.n_classes).to(device)

    trainset, testset = get_cifar_subset()
    trainloader = DataLoader(trainset, batch_size=args.batch_size, shuffle=True)
    testloader = DataLoader(testset, batch_size=args.batch_size, shuffle=False)

    optimizer = t.optim.Adam(model.out_layers[-1].parameters(), lr=args.learning_rate)

    loss_list = []
    accuracy_list = []

    for epoch in range(args.epochs):
        # Training loop
        model.train()
        for imgs, labels in (pbar := tqdm(trainloader)):
            # Move data to device, perform forward pass
            imgs, labels = imgs.to(device), labels.to(device)
            logits = model(imgs)

            # Calculate loss, perform backward pass
            loss = F.cross_entropy(logits, labels)
            loss.backward()
            optimizer.step()
            optimizer.zero_grad()

            # Update logs & progress bar
            loss_list.append(loss.item())
            pbar.set_postfix(epoch=f"{epoch + 1}/{args.epochs}", loss=f"{loss:.3f}")

        # Validation loop
        model.eval()
        num_correct_classifications = 0
        for imgs, labels in testloader:
            # Move data to device, perform forward pass in inference mode
            imgs, labels = imgs.to(device), labels.to(device)
            with t.inference_mode():
                logits = model(imgs)

            # Compute num correct by comparing argmaxed logits to true labels
            predictions = t.argmax(logits, dim=1)
            num_correct_classifications += (predictions == labels).sum().item()

        # Compute & log total accuracy
        accuracy = num_correct_classifications / len(testset)
        accuracy_list.append(accuracy)

    return loss_list, accuracy_list, model
```
</details>




=== NEW CHAPTER ===


# ☆ Bonus - Convolutions From Scratch



> ##### Learning Objectives
>
> * Understand how array strides work, and why they're important for efficient linear operations
> * Learn how to use `as_strided` to perform simple linear operations like trace and matrix multiplication
> * Implement your own convolutions and maxpooling functions using stride-based methods

This section is designed to get you familiar with the implementational details of layers like `Linear` and `Conv2d`. You'll be using libraries like `einops`, and functions like `torch.as_strided` to get a very low-level picture of how these operations work, which will help build up your overall understanding.

Note that `torch.as_strided` isn't something which will come up explicitly in much of the rest of the course (unlike `einops`). The purpose of the stride exercises is more to give you an appreciation for what's going on under the hood, so that we can build layers of abstraction on top of that during the rest of this week (and by extension this course). I see this as analogous to how [many CS courses](https://cs50.harvard.edu/x/2023/) start by teaching you about languages like C and concepts like pointers and memory management before moving on to higher-level langauges like Python which abstract away these details. The hope is that when you get to the later sections of the course, you'll have the tools to understand them better.


## Reading

* [Python NumPy, 6.1 - `as_strided()`](https://www.youtube.com/watch?v=VlkzN00P0Bc) explains what array strides are.
* [`as_strided` and `sum` are all you need](https://jott.live/markdown/as_strided) gives an overview of how to use `as_strided` to perform array operations.
* [Advanced NumPy: Master stride tricks with 25 illustrated exercises](https://towardsdatascience.com/advanced-numpy-master-stride-tricks-with-25-illustrated-exercises-923a9393ab20) provides several clear and intuitive examples of `as_strided` being used to construct arrays.


## Basic stride exercises

Array strides, and the `as_strided` method, are important to understand well because lots of linear operations are actually implementing something like `as_strided` under the hood.

Run the following code, to define this tensor:


```python
test_input = t.tensor(
    [
        [0, 1, 2, 3, 4],
        [5, 6, 7, 8, 9],
        [10, 11, 12, 13, 14],
        [15, 16, 17, 18, 19],
    ],
    dtype=t.float,
)
```


This tensor is stored in a contiguous block in computer memory.

We can call the `stride` method to get the strides of this particular array. Running `test_input.stride()`, we get `(5, 1)`. This means that we need to skip over one element in the storage of this tensor to get to the next element in the row, and 5 elements to get the next element in the column (because you have to jump over all 5 elements in the row). Another way of phrasing this: the `n`th element in the stride is the number of elements we need to skip over to move one index position in the `n`th dimension.


### Exercise - fill in the correct size and stride

> ```yaml
> Difficulty: 🔴🔴🔴🔴⚪
> Importance: 🔵🔵⚪⚪⚪
> 
> You should spend up to ~30 minutes on these exercises collectively.
> Strides can be confusing and fiddly, so you should be willing to look at the solution if you're stuck! They are not the most important part of the material today.
> ```

In the exercises below, we will work with the `test_input` tensor above. You should fill in the `size` and `stride` arguments so that calling `test_input.as_strided` with these arguments produces the desired output. When you run the cell, the `for` loop at the end will iterate through the test cases and print out whether the test passed or failed.

We've already filled in the first two as an example, along with illustrations explaining what's going on:

<img src="https://raw.githubusercontent.com/info-arena/ARENA_img/main/misc/strides3c.png" width="700">

By the end of these examples, hopefully you'll have a clear idea of what's going on. If you're still confused by some of these, then the dropdown below the codeblock contains some annotations to explain the answers.


```python
TestCase = namedtuple("TestCase", ["output", "size", "stride"])

test_cases = [
    # Example 1
    TestCase(
        output=t.tensor([0, 1, 2, 3]),
        size=(4,),
        stride=(1,),
    ),
    # Example 2
    TestCase(
        output=t.tensor([[0, 2], [5, 7]]),
        size=(2, 2),
        stride=(5, 2),
    ),
    # Start of exercises (you should fill in size & stride for all 6 of these):
    TestCase(
        output=t.tensor([0, 1, 2, 3, 4]),
        size=None,
        stride=None,
    ),
    TestCase(
        output=t.tensor([0, 5, 10, 15]),
        size=None,
        stride=None,
    ),
    TestCase(
        output=t.tensor([[0, 1, 2], [5, 6, 7]]),
        size=None,
        stride=None,
    ),
    TestCase(
        output=t.tensor([[0, 1, 2], [10, 11, 12]]),
        size=None,
        stride=None,
    ),
    TestCase(
        output=t.tensor([[0, 0, 0], [11, 11, 11]]),
        size=None,
        stride=None,
    ),
    TestCase(
        output=t.tensor([0, 6, 12, 18]),
        size=None,
        stride=None,
    ),
]


for i, test_case in enumerate(test_cases):
    if (test_case.size is None) or (test_case.stride is None):
        print(f"Test {i} failed: attempt missing.")
    else:
        actual = test_input.as_strided(size=test_case.size, stride=test_case.stride)
        if (test_case.output != actual).any():
            print(f"Test {i} failed\n  Expected: {test_case.output}\n  Actual: {actual}")
        else:
            print(f"Test {i} passed!")
```


<details><summary>Solution</summary>

```python
test_cases = [
    # Example 1
    TestCase(
        output=t.tensor([0, 1, 2, 3]),
        size=(4,),
        stride=(1,),
    ),
    # Example 2
    TestCase(
        output=t.tensor([[0, 2], [5, 7]]),
        size=(2, 2),
        stride=(5, 2),
    ),
    # Start of exercises (you should fill in size & stride for all 6 of these):
    TestCase(
        output=t.tensor([0, 1, 2, 3, 4]),
        size=(5,),
        stride=(1,),
    ),
    # # Explanation: the tensor is held in a contiguous memory block. When you get to the end of one
    # # row, a single stride jumps to the start of the next row.
    #
    TestCase(
        output=t.tensor([0, 5, 10, 15]),
        size=(4,),
        stride=(5,),
    ),
    # # Explanation: this is same as previous case, only now you're moving in colspace (i.e.
    # # skipping 5 elements) each time you move one element across the output tensor. So stride is 5
    # # rather than 1.
    #
    TestCase(
        output=t.tensor([[0, 1, 2], [5, 6, 7]]),
        size=(2, 3),
        stride=(5, 1),
    ),
    # # Explanation: as you move one column to the right in the output tensor, you want to jump one
    # # element in `test_input` (since you're just going one column to the right). As you move one
    # # row down in the output tensor, you want to jump down one row in `test_input` (which is
    # # equivalent to a stride of 5, because we're jumping 5 elements).
    #
    TestCase(
        output=t.tensor([[0, 1, 2], [10, 11, 12]]),
        size=(2, 3),
        stride=(10, 1),
    ),
    # # Explanation: same as previous, except now we're jumping over 10 elements (2 rows of 5
    # # elements) each time we move down in the output tensor.
    #
    TestCase(
        output=t.tensor([[0, 0, 0], [11, 11, 11]]),
        size=(2, 3),
        stride=(11, 0),
    ),
    # # Explanation: we're copying horizontally, i.e. we don't move in the original tensor when we
    # # step right in the output tensor, so the stride is 0 (this is a very important case to
    # # understand for the later exercises, since it's effectively our way of doing an einops.repeat
    # # operation!). As we move one row down, we're jumping over 11 elements in the original tensor
    # # (going from 0 to 11).
    #
    TestCase(
        output=t.tensor([0, 6, 12, 18]),
        size=(4,),
        stride=(6,),
    ),
    # Explanation: we're effectively taking the diagonal elements of the original tensor here,
    # since we're creating a 1D tensor with stride equal to (row_stride + col_stride) of the
    # original tensor.
]
```
</details>


## Intermediate stride exercises

Now that you're comfortable with the basics, we'll dive a little deeper with `as_strided`. In the last few exercises of this section, you'll start to implement some more challenging stride functions: trace, matrix-vector and matrix-matrix multiplication, just like we did for `einsum` in the previous section.


### Exercise - trace

> ```yaml
> Difficulty: 🔴🔴⚪⚪⚪
> Importance: 🔵🔵⚪⚪⚪
> 
> You should spend up to 10-15 minutes on this exercise.
> Use the hint if you're stuck.
> ```

You might find the very last example in the previous section helpful for this exercise.


```python
def as_strided_trace(mat: Float[Tensor, "i j"]) -> Float[Tensor, ""]:
    """
    Returns the same as `torch.trace`, using only `as_strided` and `sum` methods.
    """
    raise NotImplementedError()


tests.test_trace(as_strided_trace)
```


<details>
<summary>Hint</summary>

The trace is the sum of all the elements you get from starting at `[0, 0]` and then continually stepping down and right one element. Use strides to create a 1D array which contains these elements.
</details>


<details><summary>Solution</summary>

```python
def as_strided_trace(mat: Float[Tensor, "i j"]) -> Float[Tensor, ""]:
    """
    Returns the same as `torch.trace`, using only `as_strided` and `sum` methods.
    """
    stride = mat.stride()

    assert len(stride) == 2, f"matrix should be 2D, not {len(stride)}"
    assert mat.size(0) == mat.size(1), "matrix should be square"

    diag = mat.as_strided((mat.size(0),), (stride[0] + stride[1],))

    return diag.sum()
```
</details>


### Exercise - matrix-vector multiplication

> ```yaml
> Difficulty: 🔴🔴🔴⚪⚪
> Importance: 🔵🔵🔵⚪⚪
> 
> You should spend up to 15-20 minutes on this exercise.
> The hints should be especially useful here if you're stuck. There are two hints available to you.
> ```

You should implement this using only `as_strided` and `sum` methods, and elementwise multiplication `*` - in other words, no matrix multiplication functions!

You might find the second last example in the previous section helpful for this exercise (i.e. the one that involved a stride of zero).


```python
def as_strided_mv(mat: Float[Tensor, "i j"], vec: Float[Tensor, " j"]) -> Float[Tensor, " i"]:
    """
    Returns the same as `torch.matmul`, using only `as_strided` and `sum` methods.
    """
    raise NotImplementedError()


tests.test_mv(as_strided_mv)
tests.test_mv2(as_strided_mv)
```


<details>
<summary>Hint 1</summary>

You want your output array to be as follows:

$$
\text{output}[i] = \sum_j \text{mat}[i, j] \times \text{vector}[j]
$$

so first try to create an array with:

$$
\text{arr}[i, j] = \text{mat}[i, j] \times \text{vector}[j]
$$

then you can calculate `output` by summing over the second dimension of `arr`.
</details>

<details>
<summary>Hint 2</summary>

First try to use strides to create `vec_expanded` such that:

$$
\text{vec\_expanded}[i, j] = \text{vec}[j]
$$

We can then compute:

$$
\begin{align}
\text{arr}[i, j] &= \text{mat}[i, j] \times \text{vec\_expanded}[i, j] \\
\text{output}[i] &= \sum_j \text{arr}[i, j]
\end{align}
$$

with the first equation being a simple elementwise multiplication, and the second equation being a sum over the second dimension.

</details>

<details>
<summary>Help - I'm passing the first test, but failing the second.</summary>

It's possible that the input matrices you recieve could themselves be the output of an `as_strided` operation, so that they're represented in memory in a non-contiguous way. Make sure that your `as_strided `operation is using the strides from the original input arrays, i.e. it's not just assuming the last element in the `stride()` tuple is 1.
</details>


<details><summary>Solution</summary>

```python
def as_strided_mv(mat: Float[Tensor, "i j"], vec: Float[Tensor, " j"]) -> Float[Tensor, " i"]:
    """
    Returns the same as `torch.matmul`, using only `as_strided` and `sum` methods.
    """
    sizeM = mat.shape
    sizeV = vec.shape
    strideV = vec.stride()

    assert len(sizeM) == 2, f"mat1 should be 2D, not {len(sizeM)}"
    assert sizeM[1] == sizeV[0], f"mat{list(sizeM)}, vec{list(sizeV)} not compatible for multiplication"

    vec_expanded = vec.as_strided(mat.shape, (0, strideV[0]))

    return (mat * vec_expanded).sum(dim=1)
```
</details>


### Exercise - matrix-matrix multiplication

> ```yaml
> Difficulty: 🔴🔴🔴🔴⚪
> Importance: 🔵🔵🔵⚪⚪
> 
> You should spend up to 15-25 minutes on this exercise.
> The hints should be especially useful here if you're stuck. There are two hints available to you.
> ```
                
Like the previous function, this should only involve `as_strided`, `sum`, and pointwise multiplication.


```python
def as_strided_mm(matA: Float[Tensor, "i j"], matB: Float[Tensor, "j k"]) -> Float[Tensor, "i k"]:
    """
    Returns the same as `torch.matmul`, using only `as_strided` and `sum` methods.
    """
    raise NotImplementedError()


tests.test_mm(as_strided_mm)
tests.test_mm2(as_strided_mm)
```


<details>
<summary>Hint 1</summary>

If you did the first one, this isn't too dissimilar. We have:

$$
\text{output}[i, k] = \sum_j \text{matA}[i, j] \times \text{matB}[j, k]
$$


so in this case, try to create an array with:

$$
\text{arr}[i, j, k] = \text{matA}[i, j] \times \text{matB}[j, k]
$$

then sum this array over `j` to get our output.

We need to create expanded versions of both `matA` and `matB` in order to take this product.
</details>

<details>
<summary>Hint 2</summary>

We want to compute

$$
\text{matA\_expanded}[i, j, k] = \text{matA}[i, j]
$$

so our stride for `matA` should be `(matA.stride(0), matA.stride(1), 0)` (because we're repeating over the last dimension but iterating over the first 2 dimensions just like for the 2D matrix `matA`).
        
A similar idea applies for `matB`.
</details>


<details><summary>Solution</summary>

```python
def as_strided_mm(matA: Float[Tensor, "i j"], matB: Float[Tensor, "j k"]) -> Float[Tensor, "i k"]:
    """
    Returns the same as `torch.matmul`, using only `as_strided` and `sum` methods.
    """
    assert len(matA.shape) == 2, f"mat1 should be 2D, not {len(matA.shape)}"
    assert len(matB.shape) == 2, f"mat2 should be 2D, not {len(matB.shape)}"
    assert matA.shape[1] == matB.shape[0], (
        f"mat1{list(matA.shape)}, mat2{list(matB.shape)} not compatible for multiplication"
    )

    # Get the matrix strides, and matrix dims
    sA0, sA1 = matA.stride()
    dA0, dA1 = matA.shape
    sB0, sB1 = matB.stride()
    _, dB1 = matB.shape

    # Get target size for matrices, as well as the strides necessary to create them
    expanded_size = (dA0, dA1, dB1)
    matA_expanded_stride = (sA0, sA1, 0)
    matB_expanded_stride = (0, sB0, sB1)

    # Create the strided matrices, and return their product summed over middle dimension
    matA_expanded = matA.as_strided(expanded_size, matA_expanded_stride)
    matB_expanded = matB.as_strided(expanded_size, matB_expanded_stride)
    return (matA_expanded * matB_expanded).sum(dim=1)
```
</details>


## conv1d minimal

Here, we will implement the PyTorch `conv1d` function, which can be found [here](https://pytorch.org/docs/stable/generated/torch.nn.Conv1d.html). We will start with a simple implementation where `stride=1` and `padding=0`, with the other arguments set to their default values.

Firstly, some explanation of `conv1d` in PyTorch. The `1` in `1d` here refers to the number of dimensions along which we slide the weights (also called the kernel) when we convolve. Importantly, it does not refer to the number of dimensions of the tensors that are being used in our calculations. Typically the input and kernel are both 3D:

* `input.shape = (batch, in_channels, width)`
* `kernel.shape = (out_channels, in_channels, kernel_width)`

A typical convolution operation is illustrated in the sketch below. Some notes on this sketch:

* The `kernel_width` dimension of the kernel slides along the `width` dimension of the input. The `output_width` of the output is determined by the number of kernels that can be fit inside it; the formula can be seen in the right part of the sketch.
* For each possible position of the kernel inside the model (i.e. each freezeframe position in the sketch), the operation happening is as follows:
    * We take the product of the kernel values with the corresponding input values, and then take the sum
    * This gives us a single value for each output channel
    * These values are then passed into the output tensor
* The sketch assumes a batch size of 1. To generalise to a larger batch number, we can just imagine this operation being repeated identically on every input.

<img src="https://raw.githubusercontent.com/info-arena/ARENA_img/main/misc/ch0-conv1d-general.png" width=950>


### A note on `out_channels`

The out_channels in a conv2d layer denotes the number of filters the layer uses. Each filter detects specific features in the input, producing an output with as many channels as filters.

This number isn't tied to the input image's channels but is a design choice in the neural network architecture. Commonly, powers of 2 are chosen for computational efficiency, and deeper layers might have more channels to capture complex features. Additionally, this parameter is sometimes chosen based on the heuristic of wanting to balance the parameter count / compute for each layer - which is why you often see `out_channels` growing as the size of each feature map gets smaller.


### Exercise - implement minimal 1D conv (part 1)

> ```yaml
> Difficulty: 🔴🔴🔴🔴⚪
> Importance: 🔵🔵⚪⚪⚪
> 
> You should spend up to 15-25 minutes on this exercise.
> Use the diagram in the dropdown below, if you're stuck.
> ```

Below, you should implement `conv1d_minimal`. This is a function which works just like `conv1d`, but takes the default stride and padding values (these will be added back in later). You are allowed to use `as_strided` and `einsum`.

Because this is a difficult exercise, we've given you a "simplified" function to implement first. This gets rid of the batch dimension, and input & output channel dimensions, so you only have to think about `x` and `weights` being one-dimensional tensors:


<img src="https://raw.githubusercontent.com/info-arena/ARENA_img/main/misc/ch0-conv1d-minimal.png" width=650>


```python
def conv1d_minimal_simple(
    x: Float[Tensor, " width"], weights: Float[Tensor, " kernel_width"]
) -> Float[Tensor, " output_width"]:
    """
    Like torch's conv1d using bias=False and all other keyword arguments left at default values.

    Simplifications: batch = input channels = output channels = 1.
    """
    raise NotImplementedError()


tests.test_conv1d_minimal_simple(conv1d_minimal_simple)
```


<details>
<summary>If you're stuck on <code>conv1d_minimal_simple</code>, click here to see a diagram which should help.</summary>

This diagram illustrates the striding operation you'll need to perform on `x`. Once you do this, it's just a matter of using the right `einsum` operation to get the output.

<img src="https://raw.githubusercontent.com/info-arena/ARENA_img/main/misc/ch0-conv1d-explained.png" width=800>
</details>


<details><summary>Solution</summary>

```python
def conv1d_minimal_simple(
    x: Float[Tensor, " width"], weights: Float[Tensor, " kernel_width"]
) -> Float[Tensor, " output_width"]:
    """
    Like torch's conv1d using bias=False and all other keyword arguments left at default values.

    Simplifications: batch = input channels = output channels = 1.
    """
    # Get output width, using formula
    w = x.shape[0]
    kw = weights.shape[0]
    ow = w - kw + 1

    # Get strides for x
    s_w = x.stride(0)

    # Get strided x (the new dimension has same stride as the original stride of x)
    x_new_shape = (ow, kw)
    x_new_stride = (s_w, s_w)
    # Common error: s_w is always 1 if the tensor `x` wasn't itself created via striding, so if you
    # put 1 here you won't spot your mistake until you try this with conv2d!
    x_strided = x.as_strided(size=x_new_shape, stride=x_new_stride)

    return einops.einsum(x_strided, weights, "ow kw, kw -> ow")
```
</details>


### Exercise - implement minimal 1D conv (part 2)

> ```yaml
> Difficulty: 🔴🔴🔴🔴⚪
> Importance: 🔵🔵⚪⚪⚪
> 
> You should spend up to 15-25 minutes on this exercise.
> ```

Once you've implemented this function, you should now adapt it to make a "full version", which includes batch, in_channel and out_channel dimensions. If you're stuck, the dropdowns provide hints for how each of these new dimensions should be handled.


```python
def conv1d_minimal(
    x: Float[Tensor, "batch in_channels width"],
    weights: Float[Tensor, "out_channels in_channels kernel_width"],
) -> Float[Tensor, "batch out_channels output_width"]:
    """
    Like torch's conv1d using bias=False and all other keyword arguments left at default values.
    """
    raise NotImplementedError()


tests.test_conv1d_minimal(conv1d_minimal)
```


<details>
<summary>Help - I'm stuck on going from <code>conv1d_minimal_simple</code> to <code>conv1d_minimal</code>.</summary>

The principle is the same as before. In your function, you should:

* Create a strided version of `x` by adding a dimension of length `output_width` and with the same stride as the `width` stride of `x` (the purpose of which is to be able to do all the convolutions at once).
* Perform an einsum between this strided version of `x` and `weights`, summing over the appropriate dimensions.

The way each of the new dimensions `batch`, `out_channels` and `in_channels` are handled is as follows:

* `batch` - this is an extra dimension for `x`, it is *not* summed over when creating `output`.
* `out_channels` - this is an extra dimension for `weights`, it is *not* summed over when creating `output`.
* `in_channels` - this is an extra dimension for `weights` *and* for `x`, it *is* summed over when creating `output`.
</details>


<details><summary>Solution</summary>

```python
def conv1d_minimal(
    x: Float[Tensor, "batch in_channels width"],
    weights: Float[Tensor, "out_channels in_channels kernel_width"],
) -> Float[Tensor, "batch out_channels output_width"]:
    """
    Like torch's conv1d using bias=False and all other keyword arguments left at default values.
    """
    b, ic, w = x.shape
    oc, ic2, kw = weights.shape
    assert ic == ic2, "in_channels for x and weights don't match up"
    # Get output width, using formula
    ow = w - kw + 1

    # Get strides for x
    s_b, s_ic, s_w = x.stride()

    # Get strided x (the new dimension has the same stride as the original width-stride of x)
    x_new_shape = (b, ic, ow, kw)
    x_new_stride = (s_b, s_ic, s_w, s_w)
    # Common error: xsWi is always 1, so if you put 1 here you won't spot your mistake until you try
    # this with conv2d!
    x_strided = x.as_strided(size=x_new_shape, stride=x_new_stride)

    return einops.einsum(x_strided, weights, "b ic ow kw, oc ic kw -> b oc ow")
```
</details>


## conv2d minimal

2D convolutions are conceptually similar to 1D. The only difference is in how you move the kernel across the tensor as you take your convolution. In this case, you will be moving the tensor across two dimensions:

<img src="https://raw.githubusercontent.com/info-arena/ARENA_img/main/misc/ch0-conv2d-general.png" width=1050>

For this reason, 1D convolutions tend to be used for signals (e.g. audio), 2D convolutions are used for images, and 3D convolutions are used for 3D scans (e.g. in medical applications).


### Exercise - implement 2D minimal convolutions

> ```yaml
> Difficulty: 🔴🔴🔴🔴⚪
> Importance: 🔵🔵⚪⚪⚪
> 
> You should spend up to 20-25 minutes on this exercise.
> Use the diagram in the dropdown below, if you're stuck.
> ```

You should implement `conv2d` in a similar way to `conv1d`. Again, this is expected to be difficult and there are several hints you can go through. We've also provided a diagram to help you, like for the 1D case:

<img src="https://raw.githubusercontent.com/info-arena/ARENA_img/main/misc/ch0-conv2d-minimal.png" width=900>


```python
def conv2d_minimal(
    x: Float[Tensor, "batch in_channels height width"],
    weights: Float[Tensor, "out_channels in_channels kernel_height kernel_width"],
) -> Float[Tensor, "batch out_channels height_padding width_padding"]:
    """
    Like torch's conv2d using bias=False and all other keyword arguments left at default values.
    """
    raise NotImplementedError()


tests.test_conv2d_minimal(conv2d_minimal)
```


<details>
<summary>Hint & diagram</summary>

You should be doing the same thing that you did for the 1D version. The only difference is that you're introducing 2 new dimensions to your strided version of x, rather than 1 (their sizes should be `output_height` and `output_width`, and their strides should be the same as the original `height` and `width` strides of `x` respectively).

<img src="https://raw.githubusercontent.com/info-arena/ARENA_img/main/misc/ch0-conv2d-minimal-help.png" width=700>
</details>


<details><summary>Solution</summary>

```python
def conv2d_minimal(
    x: Float[Tensor, "batch in_channels height width"],
    weights: Float[Tensor, "out_channels in_channels kernel_height kernel_width"],
) -> Float[Tensor, "batch out_channels height_padding width_padding"]:
    """
    Like torch's conv2d using bias=False and all other keyword arguments left at default values.
    """
    b, ic, h, w = x.shape
    oc, ic2, kh, kw = weights.shape
    assert ic == ic2, "in_channels for x and weights don't match up"
    ow = w - kw + 1
    oh = h - kh + 1

    s_b, s_ic, s_h, s_w = x.stride()

    # Get strided x (the new height/width dims have the same stride as the original
    # height/width-strides of x)
    x_new_shape = (b, ic, oh, ow, kh, kw)
    x_new_stride = (s_b, s_ic, s_h, s_w, s_h, s_w)

    x_strided = x.as_strided(size=x_new_shape, stride=x_new_stride)

    return einops.einsum(x_strided, weights, "b ic oh ow kh kw, oc ic kh kw -> b oc oh ow")
```
</details>


## Padding


For a full version of `conv`, and for `maxpool` (which will follow shortly), you'll need to implement `pad` helper functions. PyTorch has some very generic padding functions, but to keep things simple and build up gradually, we'll write 1D and 2D functions individually.


### Exercise - implement padding

> ```yaml
> Difficulty: 🔴🔴⚪⚪⚪
> Importance: 🔵🔵⚪⚪⚪
> 
> You should spend up to 15-20 minutes on this exercise, and the next.
> ```

The `pad1d` function applies padding to the width dimension of a 1D tensor, i.e. we pad with `left` entries to the start of the last dimension of `x` and with `right` entries to the end of the last dimension of `x`.

Tips:
* Use the `new_full` method of the input tensor. This is a clean way to ensure that the output tensor is on the same device as the input, and has the same dtype.
* You can use three dots to denote slicing over multiple dimensions. For instance, `x[..., 0]` will take the `0th` slice of `x` along its last dimension. This is equivalent to `x[:, 0]` for 2D, `x[:, :, 0]` for 3D, etc.


```python
def pad1d(
    x: Float[Tensor, "batch in_channels width"], left: int, right: int, pad_value: float
) -> Float[Tensor, "batch in_channels width_padding"]:
    """Return a new tensor with padding applied to the edges."""
    raise NotImplementedError()


tests.test_pad1d(pad1d)
tests.test_pad1d_multi_channel(pad1d)
```


<details>
<summary>Help - I get <code>RuntimeError: The expanded size of the tensor (0) must match ...</code></summary>

This might be because you've indexed with `left : -right`. Think about what will happen here when `right` is zero.
</details>


<details><summary>Solution</summary>

```python
def pad1d(
    x: Float[Tensor, "batch in_channels width"], left: int, right: int, pad_value: float
) -> Float[Tensor, "batch in_channels width_padding"]:
    """Return a new tensor with padding applied to the edges."""
    B, C, W = x.shape
    output = x.new_full(size=(B, C, left + W + right), fill_value=pad_value)
    output[..., left : left + W] = x  # note we can't use `left:-right`, because `right` might be zero
    return output
```
</details>


Once you've passed the tests, you can implement the 2D version. The `left` and `right` padding arguments apply to the width dimension, and the `top` and `bottom` padding arguments apply to the height dimension.


```python
def pad2d(
    x: Float[Tensor, "batch in_channels height width"],
    left: int,
    right: int,
    top: int,
    bottom: int,
    pad_value: float,
) -> Float[Tensor, "batch in_channels height_padding width_padding"]:
    """Return a new tensor with padding applied to the width & height dimensions."""
    raise NotImplementedError()


tests.test_pad2d(pad2d)
tests.test_pad2d_multi_channel(pad2d)
```


<details><summary>Solution</summary>

```python
def pad2d(
    x: Float[Tensor, "batch in_channels height width"],
    left: int,
    right: int,
    top: int,
    bottom: int,
    pad_value: float,
) -> Float[Tensor, "batch in_channels height_padding width_padding"]:
    """Return a new tensor with padding applied to the width & height dimensions."""
    B, C, H, W = x.shape
    output = x.new_full(size=(B, C, top + H + bottom, left + W + right), fill_value=pad_value)
    output[..., top : top + H, left : left + W] = x
    return output
```
</details>


## Full convolutions

Now, you'll extend `conv1d` to handle the `stride` and `padding` arguments.

`stride` is the number of input positions that the kernel slides at each step. `padding` is the number of zeros concatenated to each side of the input before the convolution.

Output shape should be `(batch, output_channels, output_length)`, where output_length can be calculated as follows:

$$
\text{output\_length} = \left\lfloor\frac{\text{input\_length} + 2 \times \text{padding} - \text{kernel\_size}}{\text{stride}} \right\rfloor + 1
$$

Verify for yourself that the forumla above simplifies to the formula we used earlier when padding is 0 and stride is 1.

Docs for pytorch's `conv1d` can be found [here](https://pytorch.org/docs/stable/generated/torch.nn.Conv1d.html).


### Exercise - implement 1D convolutions

> ```yaml
> Difficulty: 🔴🔴🔴🔴⚪
> Importance: 🔵🔵⚪⚪⚪
> 
> You should spend up to 20-25 minutes on this exercise.
> ```


```python
def conv1d(
    x: Float[Tensor, "batch in_channels width"],
    weights: Float[Tensor, "out_channels in_channels kernel_width"],
    stride: int = 1,
    padding: int = 0,
) -> Float[Tensor, "batch out_channels width"]:
    """
    Like torch's conv1d using bias=False.
    """
    raise NotImplementedError()


tests.test_conv1d(conv1d)
```


<details>
<summary>Hint - dealing with padding</summary>

As the first line of your function, replace `x` with the padded version of `x`. This way, you won't have to worry about accounting for padding in the rest of the function (e.g. in the formula for the output width).
</details>

<details>
<summary>Hint - dealing with strides</summary>

The following diagram shows how you should create the strided version of `x` differently, if you have a stride of 2 rather than the default stride of 1.

<img src="https://raw.githubusercontent.com/info-arena/ARENA_img/main/misc/ch0-conv1d-help.png" width="850">

Remember, you'll need a new formula for `output_width` (see formula in the  [documentation](https://pytorch.org/docs/stable/generated/torch.nn.Conv1d.html) for help with this, or see if you can derive it without help).
</details>


<details><summary>Solution</summary>

```python
def conv1d(
    x: Float[Tensor, "batch in_channels width"],
    weights: Float[Tensor, "out_channels in_channels kernel_width"],
    stride: int = 1,
    padding: int = 0,
) -> Float[Tensor, "batch out_channels width"]:
    """
    Like torch's conv1d using bias=False.
    """
    x_padded = pad1d(x, left=padding, right=padding, pad_value=0)

    b, ic, w = x_padded.shape
    oc, ic2, kw = weights.shape
    assert ic == ic2, "in_channels for x and weights don't match up"
    ow = 1 + (w - kw) // stride
    # Note, we assume padding is zero in the formula here, because we're working with input which
    # has already been padded

    s_b, s_ic, s_w = x_padded.stride()

    # Get strided x (the new height/width dims have the same stride as the original
    # height/width-strides of x, scaled by the stride (because we're "skipping over" x as we slide
    # the kernel over it)). See diagram in hints for more explanation.
    x_new_shape = (b, ic, ow, kw)
    x_new_stride = (s_b, s_ic, s_w * stride, s_w)
    x_strided = x_padded.as_strided(size=x_new_shape, stride=x_new_stride)

    return einops.einsum(x_strided, weights, "b ic ow kw, oc ic kw -> b oc ow")
```
</details>


### Exercise - implement 2D convolutions

> ```yaml
> Difficulty: 🔴🔴🔴🔴⚪
> Importance: 🔵🔵⚪⚪⚪
> 
> You should spend up to 20-25 minutes on this exercise.
> ```

A recurring pattern in these 2d functions is allowing the user to specify either an int or a pair of ints for an argument: examples are stride and padding. We've provided some type aliases and a helper function to simplify working with these.


```python
IntOrPair = int | tuple[int, int]
Pair = tuple[int, int]


def force_pair(v: IntOrPair) -> Pair:
    """Convert v to a pair of int, if it isn't already."""
    if isinstance(v, tuple):
        if len(v) != 2:
            raise ValueError(v)
        return (int(v[0]), int(v[1]))
    elif isinstance(v, int):
        return (v, v)
    raise ValueError(v)


# Examples of how this function can be used:
for v in [(1, 2), 2, (1, 2, 3)]:
    try:
        print(f"{v!r:9} -> {force_pair(v)!r}")
    except ValueError:
        print(f"{v!r:9} -> ValueError")
```


Finally, you can implement a full version of `conv2d`. If you've done the full version of `conv1d`, and you've done `conv2d_minimal`, then you should be able to pull code from here to help you.


```python
def conv2d(
    x: Float[Tensor, "batch in_channels height width"],
    weights: Float[Tensor, "out_channels in_channels kernel_height kernel_width"],
    stride: IntOrPair = 1,
    padding: IntOrPair = 0,
) -> Float[Tensor, "batch out_channels height width"]:
    """
    Like torch's conv2d using bias=False.
    """
    raise NotImplementedError()


tests.test_conv2d(conv2d)
```


<details><summary>Solution</summary>

```python
def conv2d(
    x: Float[Tensor, "batch in_channels height width"],
    weights: Float[Tensor, "out_channels in_channels kernel_height kernel_width"],
    stride: IntOrPair = 1,
    padding: IntOrPair = 0,
) -> Float[Tensor, "batch out_channels height width"]:
    """
    Like torch's conv2d using bias=False.
    """
    stride_h, stride_w = force_pair(stride)
    padding_h, padding_w = force_pair(padding)

    x_padded = pad2d(x, left=padding_w, right=padding_w, top=padding_h, bottom=padding_h, pad_value=0)

    b, ic, h, w = x_padded.shape
    oc, ic2, kh, kw = weights.shape
    assert ic == ic2, "in_channels for x and weights don't match up"
    ow = 1 + (w - kw) // stride_w
    oh = 1 + (h - kh) // stride_h

    s_b, s_ic, s_h, s_w = x_padded.stride()

    # Get strided x (new height/width dims have same stride as original height/width-strides of x,
    # scaled by stride)
    x_new_shape = (b, ic, oh, ow, kh, kw)
    x_new_stride = (s_b, s_ic, s_h * stride_h, s_w * stride_w, s_h, s_w)
    x_strided = x_padded.as_strided(size=x_new_shape, stride=x_new_stride)

    return einops.einsum(x_strided, weights, "b ic oh ow kh kw, oc ic kh kw -> b oc oh ow")
```
</details>


## Max pooling

We have just one function left now - **max pooling**. You can review the [Medium post](https://medium.com/towards-data-science/a-comprehensive-guide-to-convolutional-neural-networks-the-eli5-way-3bd2b1164a53) from earlier to understand max pooling better.

A "max pooling" layer is similar to a convolution in that you have a window sliding over some number of dimensions. The main difference is that there's no kernel: instead of multiplying by the kernel and adding, you just take the maximum.

The way multiple channels work is also different. A convolution has some number of input and output channels, and each output channel is a function of all the input channels. There can be any number of output channels. In a pooling layer, the maximum operation is applied independently for each input channel, meaning the number of output channels is necessarily equal to the number of input channels.


### Exercise - implement 2D max pooling

> ```yaml
> Difficulty: 🔴🔴⚪⚪⚪
> Importance: 🔵🔵🔵⚪⚪
> 
> You should spend up to 10-15 minutes on this exercise.
> ```

Implement `maxpool2d` using `torch.as_strided` and `torch.amax` (= max over axes) together. Your version should behave the same as the PyTorch version, but only the indicated arguments need to be supported.


```python
def maxpool2d(
    x: Float[Tensor, "batch in_channels height width"],
    kernel_size: IntOrPair,
    stride: IntOrPair | None = None,
    padding: IntOrPair = 0,
) -> Float[Tensor, "batch out_channels height width"]:
    """
    Like PyTorch's maxpool2d. If stride is None, should be equal to kernel size.
    """
    raise NotImplementedError()


tests.test_maxpool2d(maxpool2d)
```


<details>
<summary>Hint</summary>

Conceptually, this is similar to `conv2d`.
    
In `conv2d`, you had to use `as_strided` to turn the 4D tensor `x` into a 6D tensor `x_strided` (adding dimensions over which you would take the convolution), then multiply this tensor by the kernel and sum over these two new dimensions.

`maxpool2d` is the same, except that you're simply taking max over those dimensions rather than a dot product with the kernel. So you should find yourself able to reuse a lot of code from your `conv2d` function.
</details>

<details>
<summary>Help - I'm getting a small number of mismatched elements each time (e.g. between 0 and 5%).</summary>

This is likely because you used an incorrect `pad_value`. In the convolution function, we set `pad_value=0` so these values wouldn't have any effect in the linear transformation. What pad value would make our padded elements "invisible" when we take the maximum?
</details>


<details><summary>Solution</summary>

```python
def maxpool2d(
    x: Float[Tensor, "batch in_channels height width"],
    kernel_size: IntOrPair,
    stride: IntOrPair | None = None,
    padding: IntOrPair = 0,
) -> Float[Tensor, "batch out_channels height width"]:
    """
    Like PyTorch's maxpool2d. If stride is None, should be equal to kernel size.
    """
    # Set actual values for stride and padding, using force_pair function
    if stride is None:
        stride = kernel_size
    stride_h, stride_w = force_pair(stride)
    padding_h, padding_w = force_pair(padding)
    kh, kw = force_pair(kernel_size)

    # Get padded version of x
    x_padded = pad2d(x, left=padding_w, right=padding_w, top=padding_h, bottom=padding_h, pad_value=-t.inf)

    # Calculate output height and width for x
    b, ic, h, w = x_padded.shape
    ow = 1 + (w - kw) // stride_w
    oh = 1 + (h - kh) // stride_h

    # Get strided x
    s_b, s_c, s_h, s_w = x_padded.stride()

    x_new_shape = (b, ic, oh, ow, kh, kw)
    x_new_stride = (s_b, s_c, s_h * stride_h, s_w * stride_w, s_h, s_w)
    x_strided = x_padded.as_strided(size=x_new_shape, stride=x_new_stride)

    # Argmax over dimensions of the maxpool kernel
    # (note these are the same dims that we multiply over in 2D convolutions)
    return x_strided.amax(dim=(-1, -2))
```
</details>


Now, you're finished! You can go back to the ResNets exercises, and build your ResNet ***entirely using your own stride-based functions***.


```

---

## chapter0_fundamentals/instructions/pages/03_[0.3]_Optimization.md

```markdown
# [0.3] Optimization & Hyperparameters


> **Colab: [exercises](https://colab.research.google.com/github/callummcdougall/arena-pragmatic-interp/blob/main/chapter0_fundamentals/exercises/part3_optimization/0.3_Optimization_exercises.ipynb?t=20260303) | [solutions](https://colab.research.google.com/github/callummcdougall/arena-pragmatic-interp/blob/main/chapter0_fundamentals/exercises/part3_optimization/0.3_Optimization_solutions.ipynb?t=20260303)**

Please send any problems / bugs on the `#errata` channel in the [Slack group](https://join.slack.com/t/arena-uk/shared_invite/zt-3afdmdhye-Mdb3Sv~ss_V_mEaXEbkABA), and ask any questions on the dedicated channels for this chapter of material.

If you want to change to dark mode, you can do this by clicking the three horizontal lines in the top-right, then navigating to Settings → Theme.

Links to all other chapters: [(0) Fundamentals](https://arena-chapter0-fundamentals.streamlit.app/), [(1) Transformer Interpretability](https://arena-chapter1-transformer-interp.streamlit.app/), [(2) RL](https://arena-chapter2-rl.streamlit.app/).

<img src="https://raw.githubusercontent.com/info-arena/ARENA_img/main/misc/headers/header-03.png" width="350">


# Introduction


In today's exercises, we will explore various optimization algorithms and their roles in training deep learning models. We will delve into the inner workings of different optimization techniques such as Stochastic Gradient Descent (SGD), RMSprop, and Adam, and learn how to implement them using code. Additionally, we will discuss the concept of loss landscapes and their significance in visualizing the challenges faced during the optimization process. By the end of this set of exercises, you will have a solid understanding of optimization algorithms and their impact on model performance. We'll also take a look at Weights and Biases, a tool that can be used to track and visualize the training process, and test different values of hyperparameters to find the most effective ones.

> Note - the third set of exercises in this section are on distributed training, and have different requirements: specifically, you'll need to SSH into a virtual machine which has multiple GPUs, and run the exercises from a Python file (not notebook or Colab). However you can still treat the first 2 sections as normal and then make this switch for the third section.

For a lecture on the material today, which provides some high-level understanding before you dive into the material, watch the video below:

<iframe width="540" height="304" src="https://www.youtube.com/embed/BhUj4n5Nqp4" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


## Content & Learning Objectives

### 1️⃣ Optimizers

These exercises will take you through how different optimization algorithms work (specifically SGD, RMSprop and Adam). You'll write your own optimisers, and use plotting functions to visualise gradient descent on loss landscapes.

> ##### Learning Objectives
>
> * Understand how different optimization algorithms work
> * Translate pseudocode for these algorithms into code
> * Understand the idea of loss landscapes, and how they can visualize specific challenges in the optimization process

### 2️⃣ Weights and Biases

In this section, we'll look at methods for choosing hyperparameters effectively. You'll learn how to use **Weights and Biases**, a useful tool for hyperparameter search. By the end of today, you should be able to use Weights and Biases to train the ResNet you created in the last set of exercises.

> ##### Learning Objectives
>
> * Write modular, extensible code for training models
> * Learn what the most important hyperparameters are, and methods for efficiently searching over hyperparameter space
> * Learn how to use Weights & Biases for logging your runs
> * Adapt your code from yesterday to log training runs to Weights & Biases, and use this service to run **hyperparameter sweeps**

### 3️⃣ Distributed Training

In this section, we'll take you through the basics of distributed training, which is the process via which training is split over multiple separate GPUs to improve efficiency and capacity.

> ##### Learning Objectives
> 
> * Understand the different kinds of parallelization used in deep learning (data, pipeline, tensor)
> * Understand how primitive operations in `torch.distributed` work, and how they come together to enable distributed training
> * Launch and benchmark your own distributed training runs, to train your implementation of `ResNet34` from scratch

### 4️⃣ Bonus

This section gives you suggestions for further exploration of optimizers, and Weights & Biases.


## Setup code


```python
import os
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Iterable, Literal

import numpy as np
import torch as t
import torch.distributed as dist
import torch.multiprocessing as mp
import torch.nn.functional as F
import wandb
from IPython.core.display import HTML
from IPython.display import display
from jaxtyping import Float, Int
from torch import Tensor, optim
from torch.utils.data import DataLoader, DistributedSampler
from torchvision import datasets, transforms
from tqdm import tqdm

# Make sure exercises are in the path
chapter = "chapter0_fundamentals"
section = "part3_optimization"
root_dir = next(p for p in Path.cwd().parents if (p / chapter).exists())
exercises_dir = root_dir / chapter / "exercises"
section_dir = exercises_dir / section
if str(exercises_dir) not in sys.path:
    sys.path.append(str(exercises_dir))

MAIN = __name__ == "__main__"

import part3_optimization.tests as tests
from part2_cnns.solutions import Linear, ResNet34, get_resnet_for_feature_extraction
from part3_optimization.utils import plot_fn, plot_fn_with_points
from plotly_utils import bar, imshow, line

device = t.device("mps" if t.backends.mps.is_available() else "cuda" if t.cuda.is_available() else "cpu")
```


<details>
<summary>Help - I get a NumPy-related error</summary>

This is an annoying colab-related issue which I haven't been able to find a satisfying fix for. If you restart runtime (but don't delete runtime), and run just the imports cell above again (but not the `%pip install` cell), the problem should go away.
</details>




=== NEW CHAPTER ===


# 1️⃣ Optimizers



> ##### Learning Objectives
>
> * Understand how different optimization algorithms work
> * Translate pseudocode for these algorithms into code
> * Understand the idea of loss landscapes, and how they can visualize specific challenges in the optimization process

## Reading

Some of these are strongly recommended, while others are optional. If you like, you can jump back to some of these videos while you're going through the material, if you feel like you need to.

* Andrew Ng's video series on gradient descent variants: [Gradient Descent With Momentum](https://www.youtube.com/watch?v=k8fTYJPd3_I) (9 mins), [RMSProp](https://www.youtube.com/watch?v=_e-LFe_igno) (7 mins), [Adam](https://www.youtube.com/watch?v=JXQT_vxqwIs&list=PLkDaE6sCZn6Hn0vK8co82zjQtt3T2Nkqc&index=23) (7 mins)
    * These videos are strongly recommended, especially the RMSProp video
* [A Visual Explanation of Gradient Descent Methods](https://medium.com/towards-data-science/a-visual-explanation-of-gradient-descent-methods-momentum-adagrad-rmsprop-adam-f898b102325c)
    * This is also strongly recommended; if you only want to read/watch one thing, make it this
* [Why Momentum Really Works (distill.pub)](https://distill.pub/2017/momentum/)
    * This is optional, but a fascinating read if you have time and are interested in engaging with the mathematical details of optimization


## Gradient Descent

Tomorrow, we'll look in detail about how the backpropagation algorithm works. But for now, let's take it as read that calling `loss.backward()` on a scalar `loss` will result in the computation of the gradients $\frac{\partial loss}{\partial w}$ for every parameter `w` in the model, and store these values in `w.grad`. How do we use these gradients to update our parameters in a way which decreases loss?


A loss function can be any differentiable function such that we prefer a lower value. To apply gradient descent, we start by initializing the parameters to random values (the details of this are subtle), and then repeatedly compute the gradient of the loss with respect to the model parameters. It [can be proven](https://tutorial.math.lamar.edu/Classes/CalcIII/DirectionalDeriv.aspx) that for an infinitesimal step, moving in the direction of the gradient would increase the loss by the largest amount out of all possible directions.

We actually want to decrease the loss, so we subtract the gradient to go in the opposite direction. Taking infinitesimal steps is no good, so we pick some learning rate $\lambda$ (also called the step size) and scale our step by that amount to obtain the update rule for gradient descent:

$$\theta_t \leftarrow \theta_{t-1} - \lambda \nabla L(\theta_{t-1})$$

We know that an infinitesimal step will decrease the loss, but a finite step will only do so if the loss function is linear enough in the neighbourhood of the current parameters. If the loss function is too curved, we might actually increase our loss.

The biggest advantage of this algorithm is that for N bytes of parameters, you only need N additional bytes of memory to store the gradients, which are of the same shape as the parameters. GPU memory is very limited, so this is an extremely relevant consideration. The amount of computation needed is also minimal: one multiply and one add per parameter.

The biggest disadvantage is that we're completely ignoring the curvature of the loss function, not captured by the gradient consisting of partial derivatives. Intuitively, we can take a larger step if the loss function is flat in some direction or a smaller step if it is very curved. Generally, you could represent this by some matrix P that pre-multiplies the gradients to rescale them to account for the curvature. $P$ is called a preconditioner, and gradient descent is equivalent to approximating $P$ by an identity matrix, which is a very bad approximation.

Most competing optimizers can be interpreted as trying to do something more sensible for $P$, subject to the constraint that GPU memory is at a premium. In particular, constructing $P$ explicitly is infeasible, since it's an $N \times N$ matrix and N can be hundreds of billions. One idea is to use a diagonal $P$, which only requires N additional memory. An example of a more sophisticated scheme is [Shampoo](https://arxiv.org/pdf/1802.09568.pdf).


> The algorithm is called **Shampoo** because you put shampoo on your hair before using conditioner, and this method is a pre-conditioner.
>     
> If you take away just one thing from this entire curriculum, please don't let it be this.


## Stochastic Gradient Descent

The terms gradient descent and SGD are used loosely in deep learning. To be technical, there are three variations:

- Batch gradient descent - the loss function is the loss over the entire dataset. This requires too much computation unless the dataset is small, so it is rarely used in deep learning.
- Stochastic gradient descent - the loss function is the loss on a randomly selected example. Any particular loss may be completely in the wrong direction of the loss on the entire dataset, but in expectation it's in the right direction. This has some nice properties but doesn't parallelize well, so it is rarely used in deep learning.
- Mini-batch gradient descent - the loss function is the loss on a batch of examples of size `batch_size`. This is the standard in deep learning.

The class `torch.optim.SGD` can be used for any of these by varying the number of examples passed in. We will be using only mini-batch gradient descent in this course.


## Batch Size

In addition to choosing a learning rate or learning rate schedule, we need to choose the batch size or batch size schedule as well. Intuitively, using a larger batch means that the estimate of the gradient is closer to that of the true gradient over the entire dataset, but this requires more compute. Each element of the batch can be computed in parallel so with sufficient compute, one can increase the batch size without increasing wall-clock time. For small-scale experiments, a good heuristic is thus "fill up all of your GPU memory".

At a larger scale, we would expect diminishing returns of increasing the batch size, but empirically it's worse than that - a batch size that is too large generalizes more poorly in many scenarios. The intuition that a closer approximation to the true gradient is always better is therefore incorrect. See [this paper](https://arxiv.org/pdf/1706.02677.pdf) for one discussion of this.

For a batch size schedule, most commonly you'll see batch sizes increase over the course of training. The intuition is that a rough estimate of the proper direction is good enough early in training, but later in training it's important to preserve our progress and not "bounce around" too much.

You will commonly see batch sizes that are a multiple of 32. One motivation for this is that when using CUDA, threads are grouped into "warps" of 32 threads which execute the same instructions in parallel. So a batch size of 64 would allow two warps to be fully utilized, whereas a size of 65 would require waiting for a third warp to finish. As batch sizes become larger, this wastage becomes less important.

Powers of two are also common - the idea here is that work can be recursively divided up among different GPUs or within a GPU. For example, a matrix multiplication can be expressed by recursively dividing each matrix into four equal blocks and performing eight smaller matrix multiplications between the blocks.

In tomorrow's exercises, you'll have the option to expore batch sizes in more detail.


## Common Themes in Gradient-Based Optimizers


### Weight Decay

Weight decay means that on each iteration, in addition to a regular step, we also shrink each parameter very slightly towards 0 by multiplying a scaling factor close to 1, e.g. 0.9999. Empirically, this seems to help but there are no proofs that apply to deep neural networks.

In the case of linear regression, weight decay is mathematically equivalent to having a prior that each parameter is Gaussian distributed - in other words it's very unlikely that the true parameter values are very positive or very negative. This is an example of "**inductive bias**" - we make an assumption that helps us in the case where it's justified, and hurts us in the case where it's not justified.

For a `Linear` layer, it's common practice to apply weight decay only to the weight and not the bias. It's also common to not apply weight decay to the parameters of a batch normalization layer. Again, there is empirical evidence (such as [Jai et al 2018](https://arxiv.org/pdf/1807.11205.pdf)) and there are heuristic arguments to justify these choices, but no rigorous proofs. Note that PyTorch will implement weight decay on the weights *and* biases of linear layers by default - see the bonus exercises tomorrow for more on this.


### Momentum

Momentum means that the step includes a term proportional to a moving average of past gradients. [Distill.pub](https://distill.pub/2017/momentum/) has a great article on momentum, which you should definitely read if you have time. Don't worry if you don't understand all of it; skimming parts of it can be very informative. For instance, the first half discusses the **conditioning number** (a very important concept to understand in optimisation), and concludes by giving an intuitive argument for why we generally set the momentum parameter close to 1 for ill-conditioned problems (those with a very large conditioning number).


## Visualising optimization with pathological curvatures

A pathological curvature is a type of surface that is similar to ravines and is particularly tricky for plain SGD optimization. In words, pathological curvatures typically have a steep gradient in one direction with an optimum at the center, while in a second direction we have a slower gradient towards a (global) optimum. Let’s first create an example surface of this and visualize it. The code below creates 2 visualizations (3D and 2D) and also adds the minimum point to the plot (note this is the min in the visible region, not the global minimum).


```python
def pathological_curve_loss(x: Tensor, y: Tensor):
    # Example of a pathological curvature. There are many more possible, feel free to experiment here!
    x_loss = t.tanh(x) ** 2 + 0.01 * t.abs(x)
    y_loss = t.sigmoid(y)
    return x_loss + y_loss


plot_fn(pathological_curve_loss, min_points=[(0, "y_min")])
```


<details><summary>Click to see the expected output</summary>

<div style="text-align: left"><embed src="https://info-arena.github.io/ARENA_img/misc/media-03/0301.html" width="1020" height="470"></div>

</details>


In terms of optimization, you can image that `x` and `y` are weight parameters, and the curvature represents the loss surface over the space of `x` and `y`. Note that in typical networks, we have many, many more parameters than two, and such curvatures can occur in multi-dimensional spaces as well.

Ideally, our optimization algorithm would find the center of the ravine and focuses on optimizing the parameters towards the direction of `y`. However, if we encounter a point along the ridges, the gradient is much greater in `x` than `y`, and we might end up jumping from one side to the other. Due to the large gradients, we would have to reduce our learning rate slowing down learning significantly.

To test our algorithms, we can implement a simple function to train two parameters on such a surface.


### Exercise - implement `opt_fn_with_sgd`

> ```yaml
> Difficulty: 🔴🔴🔴⚪⚪
> Importance: 🔵🔵🔵🔵⚪
> 
> You should spend up to 15-20 minutes on this exercise.
> ```

Implement the `opt_fn_with_sgd` function using `torch.optim.SGD`. This function optimizes parameters `(x, y)` (which represent coordinates at which we evaluate a function) using gradient descent on that function value. In other words, this should look just like your optimization loops in previous days' material, except rather than passing in `model.parameters()` to your optimizer, you pass in `(xy,)` (because it needs to be an iterable of parameters, not just a single parameter).

Remember, your update steps `optimizer.step()` will automatically change the values of `xy` inplace - this means that you shouldn't store past values like `xy_list.append(xy)` because then past elements of that list will be modified when `xy` is updated. Instead, you should use something like `xy_list.append(xy.detach().clone())` to make sure you're returning a copy of the tensor, which won't continue to be modified.

We've also provided you with a function `plot_fn_with_points`, which plots a function as well as a list of points produced by functions like the one above. The code below starts from `(2.5, 2.5)` and adds the resulting trajectory of `(x, y)` coordinates to the contour plot. Does it find the minimum? Play with the learning rate and momentum a bit and see how close you can get within 100 iterations.


```python
def opt_fn_with_sgd(
    fn: Callable, xy: Float[Tensor, "2"], lr=0.001, momentum=0.98, n_iters: int = 100
) -> Float[Tensor, "n_iters 2"]:
    """
    Optimize the a given function starting from the specified point.

    xy: shape (2,). The (x, y) starting point.
    n_iters: number of steps.
    lr, momentum: parameters passed to the torch.optim.SGD optimizer.

    Return: (n_iters+1, 2). The (x, y) values, from initial values to values after step `n_iters`.
    """
    # Make sure tensor has requires_grad=True, otherwise it can't be optimized (more on this tomorrow!)
    assert xy.requires_grad

    raise NotImplementedError()


points = []

optimizer_list = [
    (optim.SGD, {"lr": 0.1, "momentum": 0.0}),
    (optim.SGD, {"lr": 0.02, "momentum": 0.99}),
]

for optimizer_class, params in optimizer_list:
    xy = t.tensor([2.5, 2.5], requires_grad=True)
    xys = opt_fn_with_sgd(pathological_curve_loss, xy=xy, lr=params["lr"], momentum=params["momentum"])
    points.append((xys, optimizer_class, params))
    print(f"{params=}, last point={xys[-1]}")

plot_fn_with_points(pathological_curve_loss, points=points, min_points=[(0, "y_min")])
```


<details><summary>Click to see the expected output</summary>

<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">params={'lr': 0.1, 'momentum': 0.0}, last point=tensor([0.2300, 1.4820])
params={'lr': 0.02, 'momentum': 0.99}, last point=tensor([ 0.7196, -6.4586])</pre>

<div style="text-align: left"><embed src="https://info-arena.github.io/ARENA_img/misc/media-03/0302.html" width="1020" height="470"></div>

</details>


<details>
<summary>Help - I'm not sure if my <code>opt_fn_with_sgd</code> is implemented properly.</summary>

With a learning rate of `0.02` and momentum of `0.99`, my SGD was able to reach `[ 0.8110, -6.3344]` after 100 iterations.
</details>

<details>
<summary>Help - I'm getting <code>Can't call numpy() on Tensor that requires grad</code>.</summary>

This is a protective mechanism built into PyTorch. The idea is that once you convert your Tensor to NumPy, PyTorch can no longer track gradients, but you might not understand this and expect backprop to work on NumPy arrays.

All you need to do to convince PyTorch you're a responsible adult is to call `detach()` on the tensor first, which returns a view that does not require grad and isn't part of the computation graph.
</details>


<details><summary>Solution</summary>

```python
def opt_fn_with_sgd(
    fn: Callable, xy: Float[Tensor, "2"], lr=0.001, momentum=0.98, n_iters: int = 100
) -> Float[Tensor, "n_iters 2"]:
    """
    Optimize the a given function starting from the specified point.

    xy: shape (2,). The (x, y) starting point.
    n_iters: number of steps.
    lr, momentum: parameters passed to the torch.optim.SGD optimizer.

    Return: (n_iters+1, 2). The (x, y) values, from initial values to values after step `n_iters`.
    """
    # Make sure tensor has requires_grad=True, otherwise it can't be optimized (more on this tomorrow!)
    assert xy.requires_grad

    optimizer = optim.SGD((xy,), lr=lr, momentum=momentum)

    xy_list = [xy.detach().clone()]  # so we don't unintentionally modify past values in `xy_list`

    for i in range(n_iters):
        fn(xy[0], xy[1]).backward()
        optimizer.step()
        optimizer.zero_grad()
        xy_list.append(xy.detach().clone())

    return t.stack(xy_list)
```
</details>


## Build Your Own Optimizers

Now let's build our own drop-in replacement for these three classes from `torch.optim`. For each of the exercises you'll have to translate pseudocode that we give you into actual code. If you want an extra challenge, you can try and work directly from the pseudocode in the PyTorch documentation page rather than what we give you.


> **A warning regarding in-place operations**
>
> Be careful with expressions like `x = x + y` and `x += y`. They are NOT equivalent in Python.
>
> - The first one allocates a new `Tensor` of the appropriate size and adds `x` and `y` to it, then rebinds `x` to point to the new variable. The original `x` is not modified.
> - The second one modifies the storage referred to by `x` to contain the sum of `x` and `y` - it is an "in-place" operation. `x.add_(y)` and `torch.add(x, y, out=x)` also work the same way.
> 
> Another example: if `x` and `y` are the same shape, then `x = y` won't change the value of `x` inplace, but `x.copy_(y)` will (i.e. changing its values to the values of `y`).
> 
> When you're updating parameters in your network you _should_ use inplace operations (because your `optimizer` was passed an iterable of parameters, and so defining a new parameter value via `theta = theta - step` will take it out of the optimizer's scope - it will continue to point to the old, unmodified version).
> 
> However, be careful of using inplace operations where you shouldn't be - you don't want to accidentally do something like modify the gradients manually!


### Exercise - implement SGD

> ```yaml
> Difficulty: 🔴🔴🔴🔴⚪
> Importance: 🔵🔵🔵⚪⚪
> 
> You should spend up to 25-35 minutes on this exercise.
> This is the first of several exercises like it. The first will probably take the longest.
> ```

First, you should implement stochastic gradient descent. It should be like the [PyTorch version](https://pytorch.org/docs/stable/generated/torch.optim.SGD.html#torch.optim.SGD), but assume `nesterov=False`, `maximize=False`, and `dampening=0`. The pseudocode simplifies to:

$
b_0 \leftarrow 0 \\
\text {for } t=1 \text { to } \ldots \text { do } \\
\quad\; g_t \leftarrow \nabla_\theta f_t\left(\theta_{t-1}\right) \\
\quad\; \text {if } \lambda \neq 0 \\
\quad\;\quad\; g_t \leftarrow g_t+\lambda \theta_{t-1} \\
\quad\; \text {if } \mu \neq 0 \\
\quad\;\quad\; b_t \leftarrow \mu b_{t-1} + g_t \\
\quad\;\quad\; g_t \leftarrow b_t \\
\quad\; \theta_t \leftarrow \theta_{t-1} - \gamma g_t
$

where $\theta_t$ are the parameters, $g_t$ are the gradients (after being modified by operations like weight decay & momentum if necessary), and $b_t$ are the values we track to implement momentum.

<details>
<summary>Derivation of the simplified pseudocode</summary>

We start by removing the "if nesterov" and "if maximize" sections, since we're not using either of those. We also substitute $\tau=0$ since we're not using dampening. This gives us:

$
\text {for } t=1 \text { to } \ldots \text { do } \\
\quad\; g_t \leftarrow \nabla_\theta f_t\left(\theta_{t-1}\right) \\
\quad\; \text {if } \lambda \neq 0 \\
\quad\;\quad\; g_t \leftarrow g_t+\lambda \theta_{t-1} \\
\quad\; \text {if } \mu \neq 0 \\
\quad\;\quad\; \text{if } t>1 \\
\quad\;\quad\;\quad\; b_t \leftarrow \mu b_{t-1} + g_t \\
\quad\;\quad\; else \\
\quad\;\quad\;\quad\; b_t \leftarrow g_t \\
\quad\;\quad\; g_t \leftarrow b_t \\
\quad\; \theta_t \leftarrow \theta_{t-1} - \gamma g_t
$

Finally, we observe that we can set $b_0 = 0$ and then remove the special case handling of the $t=1$ case, which gives us the pseudocode above.

</details>

You should complete the `step` method below, which implements the algorithm described by the pseudocode above. Note that we've added the `torch.inference_mode` decorator to the `step` method, which is equivalent to using the context manager `with torch.inference_mode():`. This is similar to `torch.no_grad`; the difference between them isn't worth getting into here but in general know that `torch.inference_mode` is mostly preferred. 

The configurations used during `tests.test_sgd` will start simple (e.g. all parameters set to zero except `lr`) and gradually move to more complicated ones. This will help you track exactly where in your model the error is coming from.


You should also read the `__init__` and `zero_grad` methods, making sure you understand how these work and what they are doing. Note that setting `grad=None` like the code below is treated as equivalent to setting `grad` equal to a tensor of zeros, i.e. the first time we're required to do an operation on the gradient it'll be replaced with this. Making it be `None` by default is the standard, so as to not use unnecessary memory.


```python
class SGD:
    def __init__(
        self,
        params: Iterable[t.nn.parameter.Parameter],
        lr: float,
        momentum: float = 0.0,
        weight_decay: float = 0.0,
    ):
        """Implements SGD with momentum.

        Like the PyTorch version, but assume nesterov=False, maximize=False, and dampening=0
            https://pytorch.org/docs/stable/generated/torch.optim.SGD.html#torch.optim.SGD
        """
        self.params = list(params)  # turn params into a list (it might be a generator, so iterating over it empties it)
        self.lr = lr
        self.mu = momentum
        self.lmda = weight_decay

        self.b = [t.zeros_like(p) for p in self.params]

    def zero_grad(self) -> None:
        """Zeros all gradients of the parameters in `self.params`."""
        for param in self.params:
            param.grad = None

    @t.inference_mode()
    def step(self) -> None:
        """Performs a single optimization step of the SGD algorithm."""
        raise NotImplementedError()

    def __repr__(self) -> str:
        return f"SGD(lr={self.lr}, momentum={self.mu}, weight_decay={self.lmda})"


tests.test_sgd(SGD)
```


<details><summary>Solution</summary>

```python
class SGD:
    def __init__(
        self,
        params: Iterable[t.nn.parameter.Parameter],
        lr: float,
        momentum: float = 0.0,
        weight_decay: float = 0.0,
    ):
        """Implements SGD with momentum.

        Like the PyTorch version, but assume nesterov=False, maximize=False, and dampening=0
            https://pytorch.org/docs/stable/generated/torch.optim.SGD.html#torch.optim.SGD
        """
        self.params = list(params)  # turn params into a list (it might be a generator, so iterating over it empties it)
        self.lr = lr
        self.mu = momentum
        self.lmda = weight_decay

        self.b = [t.zeros_like(p) for p in self.params]

    def zero_grad(self) -> None:
        """Zeros all gradients of the parameters in `self.params`."""
        for param in self.params:
            param.grad = None

    @t.inference_mode()
    def step(self) -> None:
        """Performs a single optimization step of the SGD algorithm."""
        for b, theta in zip(self.b, self.params):
            g = theta.grad
            if self.lmda != 0:
                g = g + self.lmda * theta  # this shouldn't be inplace since we don't want to modify theta.grad
            if self.mu != 0:
                b.copy_(self.mu * b + g)  # this does need to be inplace, since we're modifying the value in `self.b`
                g = b
            theta -= self.lr * g  # inplace operation, to modify params

    def __repr__(self) -> str:
        return f"SGD(lr={self.lr}, momentum={self.mu}, weight_decay={self.lmda})"


tests.test_sgd(SGD)
```
</details>


If you feel comfortable with this implementation, you can skim through the remaining ones, since there's diminishing marginal returns to be gained from doing the actual exercises. We still recommend you read the content on the optimizers before the actual exercises, because they contain useful theory to understand. If you want an extra challenge in the actual exercises, you can try and implement the optimization algorithms directly from the PyTorch documentation pseudocode rather than from the simplified pseudocode we give you.


### RMSProp (and adaptive methods)

From SGD, we'll move onto discussing **adaptive gradient descent methods**. These are methods which automatically adjust the learning rate of each parameter during training, based on the size of gradients at previous steps. In a sense this is similar to how momentum operates in SGD, but we don't tend to describe SGD plus momentum as an adaptive method. When discussing momentum, we usually think of the analogy of a ball rolling down a hill, and the ball's velocity accelerates until it reaches some terminal velocity. The momentum parameter $\mu$ controls the terminal velocity: as $\mu \to 1$ the terminal velocity gets very high, which also means it can take a long time to adjust its speed when it enters new territory. In contrast, adaptive methods are better thought of as deliberate, conscious updates to the learning rate of parameters based on past values. They allow us to speed up when we need to, but without sacrificing our ability to adapt quickly when we enter new regimes.

The first adaptive method we'll look at is **RMSprop**. This is actually the second main adaptive method that was proposed in the optimization literature, after AdaGrad (however the problem with AdaGrad is that it decays the learning rates too quickly - this is the problem that RMSprop solves). RMSprop is similar to SGD, with an added dynamic: **the size of parameter steps are scaled according to the variance of past gradients**, with higher variance leading to smaller steps. Intuitively, if you're in a very monotonic region of the loss landscape then you want to take larger steps (since you know where you're going and you just want to get there quickly), whereas if you're in a very noisy region and possibly oscillating around minima then you want to take smaller steps.

One final note - when we're using non-adaptive methods like SGD we tend to have an inverse relationship between the learning rate and the batch size. Broadly speaking, this is because a larger batch size means our gradients will have smaller variance, and so we can safely use a larger learning rate. This generally isn't necessary for adaptive methods since the learning rates will be adjusted automatically during training based on the variance of our gradients - we don't need to manually scale them ourselves. Most commonly during optimization, we'll start with the default hyperparameters for whatever adaptive optimizer we're using, and then adjust from there.


### Exercise - implement RMSprop

> ```yaml
> Difficulty: 🔴🔴🔴⚪⚪
> Importance: 🔵🔵⚪⚪⚪
> 
> You should spend up to 15-25 minutes on this exercise.
> ```

Below, you should implement RMSprop in the same way as you implemented SGD. The pseudocode is slightly more complicated, since we now have to track 2 variables: $b_t$ for applying the momentum effect, and $v_t$ for tracking the variance of past gradients (we've called these `b` and `v` below).

[Here](https://pytorch.org/docs/stable/generated/torch.optim.RMSprop.html) is a link to the PyTorch version, alternatively you can use our simplified pseudocode again:

<details>
<summary>Click here for the simplified pseudocode</summary>

$
b_0 \leftarrow 0 \\
\text {for } t=1 \text { to } \ldots \text { do } \\
\quad\; g_t \leftarrow \nabla_\theta f_t\left(\theta_{t-1}\right) \\
\quad\; \text {if } \lambda \neq 0 \\
\quad\;\quad\; g_t \leftarrow g_t+\lambda \theta_{t-1} \\
\quad\; v_t \leftarrow \alpha v_{t-1} + (1-\alpha) g_t^2 \\
\quad\; g_t \leftarrow g_t / (\sqrt{v_t} + \epsilon) \\
\quad\; \text {if } \mu \neq 0 \\
\quad\;\quad\; b_t \leftarrow \mu b_{t-1} + g_t \\
\quad\;\quad\; g_t \leftarrow b_t \\
\quad\; \theta_t \leftarrow \theta_{t-1} - \gamma g_t
$

Note that we've reordered the pseudocode slightly differently to the PyTorch docs, so that we divide $g_t$ by $\sqrt{v_t + \epsilon}$ before applying momentum. Both ways are equivalent though.

</details>


```python
class RMSprop:
    def __init__(
        self,
        params: Iterable[t.nn.parameter.Parameter],
        lr: float = 0.01,
        alpha: float = 0.99,
        eps: float = 1e-08,
        weight_decay: float = 0.0,
        momentum: float = 0.0,
    ):
        """Implements RMSprop.

        Like the PyTorch version, but assumes centered=False
            https://pytorch.org/docs/stable/generated/torch.optim.RMSprop.html
        """
        self.params = list(params)  # turn params into a list (because it might be a generator)
        self.lr = lr
        self.eps = eps
        self.mu = momentum
        self.lmda = weight_decay
        self.alpha = alpha

        self.b = [t.zeros_like(p) for p in self.params]
        self.v = [t.zeros_like(p) for p in self.params]

    def zero_grad(self) -> None:
        for p in self.params:
            p.grad = None

    @t.inference_mode()
    def step(self) -> None:
        raise NotImplementedError()

    def __repr__(self) -> str:
        return (
            f"RMSprop(lr={self.lr}, eps={self.eps}, momentum={self.mu}, weight_decay={self.lmda}, alpha={self.alpha})"
        )


tests.test_rmsprop(RMSprop)
```


<details><summary>Solution</summary>

```python
class RMSprop:
    def __init__(
        self,
        params: Iterable[t.nn.parameter.Parameter],
        lr: float = 0.01,
        alpha: float = 0.99,
        eps: float = 1e-08,
        weight_decay: float = 0.0,
        momentum: float = 0.0,
    ):
        """Implements RMSprop.

        Like the PyTorch version, but assumes centered=False
            https://pytorch.org/docs/stable/generated/torch.optim.RMSprop.html
        """
        self.params = list(params)  # turn params into a list (because it might be a generator)
        self.lr = lr
        self.eps = eps
        self.mu = momentum
        self.lmda = weight_decay
        self.alpha = alpha

        self.b = [t.zeros_like(p) for p in self.params]
        self.v = [t.zeros_like(p) for p in self.params]

    def zero_grad(self) -> None:
        for p in self.params:
            p.grad = None

    @t.inference_mode()
    def step(self) -> None:
        for theta, b, v in zip(self.params, self.b, self.v):
            g = theta.grad
            if self.lmda != 0:
                g = g + self.lmda * theta
            v.copy_(self.alpha * v + (1 - self.alpha) * g.pow(2))  # inplace operation, to modify value in self.v
            g = g / (v.sqrt() + self.eps)  # not inplace operation
            if self.mu > 0:
                b.copy_(self.mu * b + g)  # inplace operation, to modify value in self.b
                g = b
            theta -= self.lr * g  # inplace operation, to modify params

    def __repr__(self) -> str:
        return (
            f"RMSprop(lr={self.lr}, eps={self.eps}, momentum={self.mu}, weight_decay={self.lmda}, alpha={self.alpha})"
        )


tests.test_rmsprop(RMSprop)
```
</details>


### Adam, and "momentum"

We'll end by implementing Adam and AdamW, two of the most popular optimizers in deep learning. These combine the benefits of RMSprop and SGD with momentum: they have the same variance-based scaling as RMSprop, but they also have an update rule based on the first moment of gradients as well.

There's an important clarification to make here - the first order adjustment of Adam is sometimes called momentum as a shorthand, but there's an important sense in which it isn't. The key difference is that SGD's momentum causes acceleration until we hit terminal velocity, which could be very large for $\mu \approx 1$. In contrast, Adam's momentum is an exponentially weighted moving average - the parameter $\beta_1$ controls how quickly it adjusts (with a value closer to 1 meaning it adjust to newer values more slowly), but it doesn't change the terminal velocity in any sense. Mathematically, the difference between these two is minimal (all you'd need to do is take Adam's update rule $m_t \leftarrow \beta_1 m_{t-1} + (1-\beta_1) g_t$ and change it to $m_t \leftarrow \beta_1 m_{t-1} + g_t$ for it to have the same qualitative behaviour as SGD), but this extra factor makes a lot of difference!


### Exercise - implement Adam

> ```yaml
> Difficulty: 🔴🔴🔴🔴⚪
> Importance: 🔵🔵🔵⚪⚪
> 
> You should spend up to 15-20 minutes on this exercise.
> ```

This should just be an extension of your RMSprop implementation. You still have 2 variables to track, but now the variable $b_t$ for applying momentum has been replaced with $m_t$ for tracking the exponentially weighted moving average of first order moments.

[Here's](https://pytorch.org/docs/stable/generated/torch.optim.Adam.html) a link to the PyTorch version, alternatively you can use the simplified pseudocode below:

<details>
<summary>Click here for the simplified pseudocode</summary>

$
\text {for } t=1 \text { to } \ldots \text { do } \\
\quad\; g_t \leftarrow \nabla_\theta f_t\left(\theta_{t-1}\right) \\
\quad\; \text {if } \lambda \neq 0 \\
\quad\;\quad\; g_t \leftarrow g_t+\lambda \theta_{t-1} \\
\quad\; m_t \leftarrow \beta_1 m_{t-1} + (1-\beta_1) g_t \\
\quad\; v_t \leftarrow \beta_2 v_{t-1} + (1-\beta_2) g_t^2 \\
\quad\; \widehat{m_t} \leftarrow m_t / (1 - \beta_1^t) \\
\quad\; \widehat{v_t} \leftarrow v_t / (1 - \beta_2^t) \\
\quad\; \theta_t \leftarrow \theta_{t-1} - \gamma \widehat{m_t} / (\sqrt{\widehat{v_t}} + \epsilon)
$

</details>

Note - we center our first & second moment estimators by dividing by $1 - \beta^t$, which means for this optimizer we do have to track the variable $t$ (make sure to remember to increment it after each use of the `step` function). We do this because Adam's exponentially weighted moving average would otherwise take a while to converge to the true mean (since its estimates initially behave like the truncated sum of a geometric series). We leave it as an exercise for the reader to derive this (hint - try assuming the expected value $\mathbb{E}[g_t] = g_0$ is the same for all $t$, what does the expression $\mathbb{E}[m_t]$ simplify to?).


```python
class Adam:
    def __init__(
        self,
        params: Iterable[t.nn.parameter.Parameter],
        lr: float = 0.001,
        betas: tuple[float, float] = (0.9, 0.999),
        eps: float = 1e-08,
        weight_decay: float = 0.0,
    ):
        """Implements Adam.

        Like the PyTorch version, but assumes amsgrad=False and maximize=False
            https://pytorch.org/docs/stable/generated/torch.optim.Adam.html
        """
        self.params = list(params)
        self.lr = lr
        self.beta1, self.beta2 = betas
        self.eps = eps
        self.lmda = weight_decay
        self.t = 1

        self.m = [t.zeros_like(p) for p in self.params]
        self.v = [t.zeros_like(p) for p in self.params]

    def zero_grad(self) -> None:
        for p in self.params:
            p.grad = None

    @t.inference_mode()
    def step(self) -> None:
        raise NotImplementedError()

    def __repr__(self) -> str:
        return f"Adam(lr={self.lr}, beta1={self.beta1}, beta2={self.beta2}, eps={self.eps}, weight_decay={self.lmda})"


tests.test_adam(Adam)
```


<details><summary>Solution</summary>

```python
class Adam:
    def __init__(
        self,
        params: Iterable[t.nn.parameter.Parameter],
        lr: float = 0.001,
        betas: tuple[float, float] = (0.9, 0.999),
        eps: float = 1e-08,
        weight_decay: float = 0.0,
    ):
        """Implements Adam.

        Like the PyTorch version, but assumes amsgrad=False and maximize=False
            https://pytorch.org/docs/stable/generated/torch.optim.Adam.html
        """
        self.params = list(params)
        self.lr = lr
        self.beta1, self.beta2 = betas
        self.eps = eps
        self.lmda = weight_decay
        self.t = 1

        self.m = [t.zeros_like(p) for p in self.params]
        self.v = [t.zeros_like(p) for p in self.params]

    def zero_grad(self) -> None:
        for p in self.params:
            p.grad = None

    @t.inference_mode()
    def step(self) -> None:
        for theta, m, v in zip(self.params, self.m, self.v):
            g = theta.grad
            if self.lmda != 0:
                g = g + self.lmda * theta
            m.copy_(self.beta1 * m + (1 - self.beta1) * g)
            v.copy_(self.beta2 * v + (1 - self.beta2) * g.pow(2))
            m_hat = m / (1 - self.beta1**self.t)
            v_hat = v / (1 - self.beta2**self.t)
            theta -= self.lr * m_hat / (v_hat.sqrt() + self.eps)
        self.t += 1

    def __repr__(self) -> str:
        return f"Adam(lr={self.lr}, beta1={self.beta1}, beta2={self.beta2}, eps={self.eps}, weight_decay={self.lmda})"
```
</details>


### Exercise - implement AdamW

> ```yaml
> Difficulty: 🔴🔴⚪⚪⚪
> Importance: 🔵🔵⚪⚪⚪
> 
> You should spend up to 10-15 minutes on this exercise.
> ```

Finally, you'll adapt your Adam implementation to implement AdamW. This is a very small modification of the Adam update rule, where we apply weight decay in a different way (by modifying the weights $theta_t$ themselves, rather than modifying the gradients $g_t$ and then using those modified gradients in the first & second moment calculations). This means that, unlike with Adam, using weight decay is equivalent to having a Gaussian prior on the weights with mean zero (or alternatively, equivalent to L2 regularization). This is seen as the more "correct" way to implement weight decay, and so AdamW is now generally preferred over Adam.

You can read more about this variant of Adam [here](https://arxiv.org/abs/1711.05101). The PyTorch docs are [here](https://pytorch.org/docs/stable/generated/torch.optim.AdamW.html), and the pseudocode is again provided for you below (but for this exercise we do recommend trying to go without it - having to work with more complex pseudocode and parse out the bits that actually matter is a useful exercise!).

<details>
<summary>Click here for the simplified pseudocode</summary>

$
\text {for } t=1 \text { to } \ldots \text { do } \\
\quad\; g_t \leftarrow \nabla_\theta f_t\left(\theta_{t-1}\right) \\
\quad\; \theta_t \leftarrow \theta_{t-1} - \gamma \lambda \theta_{t-1} \\
\quad\; m_t \leftarrow \beta_1 m_{t-1} + (1-\beta_1) g_t \\
\quad\; v_t \leftarrow \beta_2 v_{t-1} + (1-\beta_2) g_t^2 \\
\quad\; \widehat{m_t} \leftarrow m_t / (1 - \beta_1^t) \\
\quad\; \widehat{v_t} \leftarrow v_t / (1 - \beta_2^t) \\
\quad\; \theta_t \leftarrow \theta_t - \gamma \widehat{m_t} / (\sqrt{\widehat{v_t}} + \epsilon)
$

</details>


```python
class AdamW:
    def __init__(
        self,
        params: Iterable[t.nn.parameter.Parameter],
        lr: float = 0.001,
        betas: tuple[float, float] = (0.9, 0.999),
        eps: float = 1e-08,
        weight_decay: float = 0.0,
    ):
        """Implements Adam.

        Like the PyTorch version, but assumes amsgrad=False and maximize=False
            https://pytorch.org/docs/stable/generated/torch.optim.AdamW.html
        """
        self.params = list(params)
        self.lr = lr
        self.beta1, self.beta2 = betas
        self.eps = eps
        self.lmda = weight_decay
        self.t = 1

        self.m = [t.zeros_like(p) for p in self.params]
        self.v = [t.zeros_like(p) for p in self.params]

    def zero_grad(self) -> None:
        for p in self.params:
            p.grad = None

    @t.inference_mode()
    def step(self) -> None:
        raise NotImplementedError()

    def __repr__(self) -> str:
        return f"AdamW(lr={self.lr}, beta1={self.beta1}, beta2={self.beta2}, eps={self.eps}, weight_decay={self.lmda})"


tests.test_adamw(AdamW)
```


<details><summary>Solution</summary>

```python
class AdamW:
    def __init__(
        self,
        params: Iterable[t.nn.parameter.Parameter],
        lr: float = 0.001,
        betas: tuple[float, float] = (0.9, 0.999),
        eps: float = 1e-08,
        weight_decay: float = 0.0,
    ):
        """Implements Adam.

        Like the PyTorch version, but assumes amsgrad=False and maximize=False
            https://pytorch.org/docs/stable/generated/torch.optim.AdamW.html
        """
        self.params = list(params)
        self.lr = lr
        self.beta1, self.beta2 = betas
        self.eps = eps
        self.lmda = weight_decay
        self.t = 1

        self.m = [t.zeros_like(p) for p in self.params]
        self.v = [t.zeros_like(p) for p in self.params]

    def zero_grad(self) -> None:
        for p in self.params:
            p.grad = None

    @t.inference_mode()
    def step(self) -> None:
        for theta, m, v in zip(self.params, self.m, self.v):
            g = theta.grad
            theta *= 1 - self.lr * self.lmda
            m.copy_(self.beta1 * m + (1 - self.beta1) * g)
            v.copy_(self.beta2 * v + (1 - self.beta2) * g.pow(2))
            m_hat = m / (1 - self.beta1**self.t)
            v_hat = v / (1 - self.beta2**self.t)
            theta -= self.lr * m_hat / (v_hat.sqrt() + self.eps)
        self.t += 1

    def __repr__(self) -> str:
        return f"AdamW(lr={self.lr}, beta1={self.beta1}, beta2={self.beta2}, eps={self.eps}, weight_decay={self.lmda})"
```
</details>


## Plotting multiple optimisers

Finally, we've provided some code which should allow you to plot more than one of your optimisers at once.


### Exercise - experiment with different optimizers & params

> ```yaml
> Difficulty: 🔴🔴⚪⚪⚪
> Importance: 🔵🔵🔵⚪⚪
> 
> You should spend up to 20-30 minutes on this exercise.
> ```

We've given you a function below which works just like `opt_fn_with_sgd` from earlier, but takes in a general optimizer and hyperparameters (as a dictionary of keyword arguments like `lr` and `momentum`).

You should use this function to play around with different optimizers and hyperparameters, comparing their performance. The code below gives one example of such a comparison, run it now and see what you get:


```python
def opt_fn(
    fn: Callable,
    xy: Tensor,
    optimizer_class,
    optimizer_hyperparams: dict,
    n_iters: int = 100,
) -> Tensor:
    """Optimize the a given function starting from the specified point.

    optimizer_class: one of the optimizers you've defined, either SGD, RMSprop, or Adam
    optimzer_kwargs: keyword arguments passed to your optimiser (e.g. lr and weight_decay)
    """
    assert xy.requires_grad

    optimizer = optimizer_class([xy], **optimizer_hyperparams)

    xy_list = [xy.detach().clone()]  # so that we don't unintentionally modify past values in `xy_list`

    for i in range(n_iters):
        fn(xy[0], xy[1]).backward()
        optimizer.step()
        optimizer.zero_grad()
        xy_list.append(xy.detach().clone())

    return t.stack(xy_list)


points = []

optimizer_list = [
    (SGD, {"lr": 0.03, "momentum": 0.99}),
    (RMSprop, {"lr": 0.02, "alpha": 0.99, "momentum": 0.8}),
    (Adam, {"lr": 0.2, "betas": (0.99, 0.99), "weight_decay": 0.005}),
    (AdamW, {"lr": 0.2, "betas": (0.99, 0.99), "weight_decay": 0.005}),
]

for optimizer_class, params in optimizer_list:
    xy = t.tensor([2.5, 2.5], requires_grad=True)
    xys = opt_fn(
        pathological_curve_loss,
        xy=xy,
        optimizer_class=optimizer_class,
        optimizer_hyperparams=params,
    )
    points.append((xys, optimizer_class, params))

plot_fn_with_points(pathological_curve_loss, min_points=[(0, "y_min")], points=points)
```


<details><summary>Click to see the expected output</summary>

<div style="text-align: left"><embed src="https://info-arena.github.io/ARENA_img/misc/media-03/0303.html" width="1020" height="470"></div>

</details>


Note that the focus shouldn't be on figuring out "which one is the best optimizer" - this loss landscape (and other examples we'll give you) were specifically designed to be pathological, and exhibit interesting kinds of behaviours from optimizers. The focus should instead be on understanding how the characteristics of optimizers we discussed in the previous sections are reflected visually in the plots produced on these loss landscapes. Some questions you might want to ask:

- We discussed that Adam (and AdamW) center their first and second moments, so that the early values are large - otherwise they start off small and take a long time to grow. Is this reflected in the plots, i.e. with Adam/AdamW taking larger early steps relative to SGD or RMSprop?
- The momentum used in SGD and RMSprop causes acceleration until "terminal velocity", which is usually a higher cap than Adam and AdamW. Is this reflected in the step size (and the instability) of those optimizers? Do Adam and AdamW seem to adapt slightly faster when they enter new terrain?
- Are there any landscapes where weight decay is advantageous, and can you see why it would be?

Some more functions you might want to try out (with their minima marked on the plots):


```python
def bivariate_gaussian(x, y, x_mean=0.0, y_mean=0.0, x_sig=1.0, y_sig=1.0):
    norm = 1 / (2 * np.pi * x_sig * y_sig)
    x_exp = 0.5 * ((x - x_mean) ** 2) / (x_sig**2)
    y_exp = 0.5 * ((y - y_mean) ** 2) / (y_sig**2)
    return norm * t.exp(-x_exp - y_exp)


means = [(1.0, -0.5), (-1.0, 0.5), (-0.5, -0.8)]


def neg_trimodal_func(x, y):
    """
    This function has 3 global minima, at `means`. Unstable methods can overshoot these minima, and
    non-adaptive methods can fail to converge to them in the first place given how shallow the
    gradients are everywhere except in the close vicinity of the minima.
    """
    z = -bivariate_gaussian(x, y, x_mean=means[0][0], y_mean=means[0][1], x_sig=0.2, y_sig=0.2)
    z -= bivariate_gaussian(x, y, x_mean=means[1][0], y_mean=means[1][1], x_sig=0.2, y_sig=0.2)
    z -= bivariate_gaussian(x, y, x_mean=means[2][0], y_mean=means[2][1], x_sig=0.2, y_sig=0.2)
    return z


plot_fn(neg_trimodal_func, x_range=(-2, 2), y_range=(-2, 2), min_points=means)
```


<div style="text-align: left"><embed src="https://info-arena.github.io/ARENA_img/misc/media-03/0304.html" width="1020" height="470"></div>


```python
def rosenbrocks_banana_func(x: Tensor, y: Tensor, a=1, b=100) -> Tensor:
    """
    This function has a global minimum at `(a, a)` so in this case `(1, 1)`. It's characterized by a
    long, narrow, parabolic valley (parameterized by `y = x**2`). Various gradient descent methods
    have trouble navigating this valley because they often oscillate unstably (gradients from the
    `b`-term dwarf the gradients from the `a`-term).

    See more on this function: https://en.wikipedia.org/wiki/Rosenbrock_function.
    """
    return (a - x) ** 2 + b * (y - x**2) ** 2 + 1


plot_fn(
    rosenbrocks_banana_func,
    x_range=(-2.5, 2.5),
    y_range=(-2, 4),
    z_range=(0, 100),
    min_points=[(1, 1)],
)
```


<div style="text-align: left"><embed src="https://info-arena.github.io/ARENA_img/misc/media-03/0305.html" width="1020" height="470"></div>


<details>
<summary>Some example visualizations & observations</summary>

Let's start with the negative trimodal function. You should find that weight decay massively helps performance here, but this is for pretty uninteresting reasons - it essentially adds a slope towards the origin, and when the ball rolls towards the origin it will probably also get caught in one of the three minima. So it doesn't tell us much about the actual optimizers.

More interestingly, we can compare the optimizers when they have weight decay switched off. You should find that Adam can outperform SGD and RMSprop here, because the way it uses "momentum" is better suited to this task. For one thing, the first and second moment centering means it can take larger early steps relative to SGD and RMSprop (which both take a while to accelerate). For another, momentum causes RMSprop step sizes to increase in an unstable way, which is why it will overshoot the minima and get stuck on the other side without careful hyperparameter tuning. SGD is even worse - because of its lack of variance-based scaling, it'll utterly fail to move anywhere unless it starts out very close to one of the three minima.

```python
optimizer_list = [
    (SGD, {"lr": 0.1, "momentum": 0.5}),
    (RMSprop, {"lr": 0.1, "alpha": 0.99, "momentum": 0.5}),
    (Adam, {"lr": 0.1, "betas": (0.9, 0.999)}),
]

points = []
for optimizer_class, params in optimizer_list:
    xy = t.tensor([1.0, 1.0], requires_grad=True)
    xys = opt_fn(neg_trimodal_func, xy=xy, optimizer_class=optimizer_class, optimizer_hyperparams=params)
    points.append((xys, optimizer_class, params))

plot_fn_with_points(neg_trimodal_func, points=points, x_range=(-2, 2), y_range=(-2, 2), min_point=means)
```

<div style="text-align: left"><embed src="https://info-arena.github.io/ARENA_img/misc/media-03/0304-points.html" width="1020" height="470"></div>

Next, Rosenbrock's banana. This function has a global minimum at `(1, 1)` inside a long, narrow, parabolic-shaped valley. Basic gradient descent often zigzags back and forth along the valley, making very slow progress. Momentum is absolutely essential to perform well in this task. This is a rare case where SGD plus momentum does converge faster than Adam because the higher terminal velocity enables larger step sizes plus the extreme slope of the loss landscape prevents the kind of instability that usually hinders SGD. However, some caveats: SGD requires a very small step size to prevent unstable oscillations (given how steep the valley is), whereas Adam is much more stable. Furthermore, if we extend the number of iterations, we see that Adam does also converge, and it does so with fewer oscillations than SGD (it stays within the parabolic valley).

```python
optimizer_list = [
    (SGD, {"lr": 0.001, "momentum": 0.99}),
    (Adam, {"lr": 0.1, "betas": (0.9, 0.999)}),
]

points = []
for optimizer_class, params in optimizer_list:
    xy = t.tensor([-1.5, 2.5], requires_grad=True)
    xys = opt_fn(
        rosenbrocks_banana_func, xy=xy, optimizer_class=optimizer_class, optimizer_hyperparams=params, n_iters=500
    )
    points.append((xys, optimizer_class, params))

plot_fn_with_points(
    rosenbrocks_banana_func, x_range=(-2.5, 2.5), y_range=(-2, 4), z_range=(0, 100), min_points=[(1, 1)], points=points
)
```

<div style="text-align: left"><embed src="https://info-arena.github.io/ARENA_img/misc/media-03/0305-points.html" width="1020" height="470"></div>


## Bonus - parameter groups


> *If you're interested in these exercises then you can go through them, if not then you can move on to the next section (weights and biases).*


Rather than passing a single iterable of parameters into an optimizer, you have the option to pass a list of parameter groups, each one with different hyperparameters. As an example of how this might work:

```python
optim.SGD([
    {'params': model.base.parameters()},
    {'params': model.classifier.parameters(), 'lr': 1e-3}
], lr=1e-2, momentum=0.9)
```

The first argument here is a list of dictionaries, with each dictionary defining a separate parameter group. Each should contain a `params` key, which contains an iterable of parameters belonging to this group. The dictionaries may also contain keyword arguments. If a parameter is not specified in a group, PyTorch uses the value passed as a keyword argument. So the example above is equivalent to:

```python
optim.SGD([
    {'params': model.base.parameters(), 'lr': 1e-2, 'momentum': 0.9},
    {'params': model.classifier.parameters(), 'lr': 1e-3, 'momentum': 0.9}
])
```

All parameters have default values, with the exception of `lr` which is why you need to specify it either as a keyword arg to the optimizer or separately in each group.

PyTorch optimisers will store all their params and hyperparams in the `param_groups` attribute - this is why when we want to modify an optimizer's learning rate (which we'll do later on in the course), even if we didn't specify any parameter groups we'll still need to use `optimizer.param_groups[0].lr = new_lr`.


### When to use parameter groups

Parameter groups can be useful in several different circumstances. A few examples:

* Finetuning a model by freezing earlier layers and only training later layers is an extreme form of parameter grouping. We can use the parameter group syntax to apply a modified form, where the earlier layers have a smaller learning rate. This allows these earlier layers to adapt to the specifics of the problem, while making sure they don't forget all the useful features they've already learned.
* Often it's good to treat weights and biases differently, e.g. effects like weight decay are often applied to weights but not biases. PyTorch doesn't differentiate between these two, so you'll have to do this manually using paramter groups.
    * This in particular, you might be doing later in the course, if you choose the "train BERT from scratch" exercises during the transformers chapter.
* On the subject of transformers, weight decay is often *not* applied to embeddings and layernorms in transformer models.

More generally, if you're trying to replicate a paper, it's important to be able to use all the same training details that the original authors did, so you can get the same results.


### Exercise - rewrite SGD to use parameter groups

> ```yaml
> Difficulty: 🔴🔴🔴🔴⚪
> Importance: 🔵⚪⚪⚪⚪
> 
> You should spend up to 30-40 minutes on this exercise.
> It's somewhat useful to understand the idea of parameter groups, less so to know how they're actually implemented.
> ```

You should rewrite the `SGD` optimizer from the earlier exercises, to use `param_groups`. This will involve filling in the 3 methods `__init__`, `zero_grad`, and `step`. Some guidance:

- In `__init__` you should create `self.param_groups`, which is a list of dictionaries with each one containing `"params"` as well as all the hyperparameters for that group. Remember the hierarchy for hparams: "specified for group" > "specified as a keyword argument" > "default value".
- In `zero_grad` and `step` the logic is the same as before, but now you need a double nested for loop: once over the param groups in `self.param_groups`, and once over the params in each group. For the latter, make sure you're using the group-specific hyperparameters (i.e. the ones you hopefully stored in `self.param_groups` in the init method).


```python
class SGD:
    def __init__(self, params, **kwargs):
        """Implements SGD with momentum.

        Accepts parameters in groups, or an iterable.

        Like the PyTorch version, but assume nesterov=False, maximize=False, and dampening=0
            https://pytorch.org/docs/stable/generated/torch.optim.SGD.html#torch.optim.SGD
        """
        # Deal with case where we didn't supply groups, so we just make it into a single dictionary
        if not isinstance(params, (list, tuple)):
            params = [{"params": params}]

        # Make sure each group["params"] is a list of params not a generator (so we don't iterate
        # over & destroy it!)
        for p in params:
            p["params"] = list(p["params"])

        self.param_groups = []

        # YOUR CODE HERE - fill in `self.param_groups`
        raise NotImplementedError()

    def zero_grad(self) -> None:
        raise NotImplementedError()

    @t.inference_mode()
    def step(self) -> None:
        raise NotImplementedError()


tests.test_sgd_param_groups(SGD)
```


<details><summary>Solution</summary>

```python
class SGD:
    def __init__(self, params, **kwargs):
        """Implements SGD with momentum.

        Accepts parameters in groups, or an iterable.

        Like the PyTorch version, but assume nesterov=False, maximize=False, and dampening=0
            https://pytorch.org/docs/stable/generated/torch.optim.SGD.html#torch.optim.SGD
        """
        # Deal with case where we didn't supply groups, so we just make it into a single dictionary
        if not isinstance(params, (list, tuple)):
            params = [{"params": params}]

        # Make sure each group["params"] is a list of params not a generator (so we don't iterate
        # over & destroy it!)
        for p in params:
            p["params"] = list(p["params"])

        self.param_groups = []

        for param_group in params:
            # Set hyperparameters hierarchically: specified for group > specified as a keyword
            # argument > default value. We do this via dict merge (right takes precedence over left).
            param_group = {"momentum": 0.0, "weight_decay": 0.0, **kwargs, **param_group}

            # Check that "lr" is supplied
            assert "lr" in param_group, "Error: one of the param groups didn't specify 'lr'"

            # Set "params" and "b" in our group
            param_group["b"] = [t.zeros_like(p) for p in param_group["params"]]

            self.param_groups.append(param_group)

    def zero_grad(self) -> None:
        for param_group in self.param_groups:
            for p in param_group["params"]:
                p.grad = None

    @t.inference_mode()
    def step(self) -> None:
        # loop through each param group

        for param_group in self.param_groups:
            # Get hparams for this group
            lmda = param_group["weight_decay"]
            mu = param_group["momentum"]
            lr = param_group["lr"]

            # Same code as for SGD implementation before, but using group-specific hparams
            for b, theta in zip(param_group["b"], param_group["params"]):
                g = theta.grad
                if lmda != 0:
                    g = g + lmda * theta  # not inplace, since we're not changing theta.grad
                if mu != 0:
                    b.copy_(mu * b + g)  # needs to be inplace, since we're changing `self.b` value
                    g = b
                theta -= lr * g  # inplace operation, to modify params


tests.test_sgd_param_groups(SGD)
```
</details>


## Bonus - Muon Optimizer


Hot off the press is a new optimizer called *Muon*. Muon is an optimizer specialized only for the parameters of a network that are *hidden* and *at least 2-dimensional*.
 * For image classification, we skip anything that directly interfaces with the input, or the output.
 * For language models, this means skipping the embedding and unembedding layers.
The dimensionality requirement also means skipping biases, $\gamma$ or $\beta$ in layernorms, etc.
All other parameters are optimized using Adam as per usual.

<figure>
  <img src="https://pbs.twimg.com/media/GZELa2YbUAAqbW6?format=jpg&name=large" width="500">
  <figcaption>Comparison of Muon to AdamW optimizer for NanoGPT training speedrun. Taken from <a href="https://x.com/kellerjordan0/status/1842300916864844014">https://x.com/kellerjordan0/status/1842300916864844014</a></figcaption>
</figure>

Muon has shown great promise for language models, shaving a massive 40%(!) off the training time for [nanoGPT speedrun](https://www.tylerromero.com/posts/nanogpt-speedrun-worklog/), a collaborative project to train a model as performant as GPT-2 as fast as possible, based on [Andrej Karpathy's nanoGPT implementation](https://github.com/karpathy/llm.c/discussions/481).

We might make this into an actual exercise later, but for now, here's a series of resources should you wish to implement it yourself:
* [Introduction to Muon](https://kellerjordan.github.io/posts/muon/)
* [NanoGPT Speedrun Project](https://github.com/KellerJordan/modded-nanogpt/) Current word record is sub-3 minutes(!!)*
  - On a 8xH100 cluster, about 16 PFLOPS of power. On a single consumer GPU (RTX 3090), (assuming no issues with out-of-memory), with ~140TFLOPS of power,  this would take ~5 hours, still incredibly impressive.
* [Twitter thread on Muon](https://x.com/kellerjordan0/status/1842300916864844014)
* [Derivation of Muon](https://jeremybernste.in/writing/deriving-muon)
  * Not required reading, but if you're curious about the math
* [Reference Muon implementation in PyTorch](https://github.com/KellerJordan/Muon)




=== NEW CHAPTER ===


# 2️⃣ Weights and Biases



> ##### Learning Objectives
>
> * Write modular, extensible code for training models
> * Learn what the most important hyperparameters are, and methods for efficiently searching over hyperparameter space
> * Learn how to use Weights & Biases for logging your runs
> * Adapt your code from yesterday to log training runs to Weights & Biases, and use this service to run **hyperparameter sweeps**

Next, we'll look at methods for choosing hyperparameters effectively. You'll learn how to use **Weights and Biases**, a useful tool for hyperparameter search.

The exercises themselves will be based on your ResNet implementations from yesterday, although the principles should carry over to other models you'll build in this course (such as transformers next week).

Note, this page only contains a few exercises, and they're relatively short. You're encouraged to spend some time playing around with Weights and Biases, but you should also spend some more time finetuning your ResNet from yesterday (you might want to finetune ResNet during the morning, and look at today's material in the afternoon - you can discuss this with your partner). You should also spend some time reviewing the last three days of material, to make sure there are no large gaps in your understanding.


## Finetuning & feature extraction

> We'll start with a brief discussion of the related concepts **finetuning** and **feature extraction**. If you've already gone through yesterday's bonus material on feature extraction then you can skip this section.

**Finetuning** can mean slightly different things in different contexts, but broadly speaking it means using the weights of an already trained network as the starting values for training a new network. Because training networks from scratch is very computationally expensive, this is a common practice in ML.

The specific type of finetuning we'll be doing here is called **feature extraction**. This is when we freeze most layers of a model except the last few, and perform gradient descent on those. We call this feature extraction because the earlier layers of the model have already learned to identify important features of the data (and these features are also relevant for the new task), so all that we have to do is train a few final layers in the model to extract these features.

*Terminology note - sometimes feature extraction and finetuning are defined differently, with finetuning referring to the training of all the weights in a pretrained model (usually with a small or decaying learning rate), and feature extraction referring to the freezing of some layers and training of others. To avoid confusion here, we'll use the term "feature extraction" rather than "finetuning".*

<img src="https://raw.githubusercontent.com/info-arena/ARENA_img/main/misc/feature_extraction.png" width="400">

The way we implement feature extraction in PyTorch is by **freezing** all but the last few layers of our model, meaning gradients don't propagate back through them (and we don't perform gradient descent updates on them) - more on gradient freezing tomorrow! We've used the `get_resnet_for_feature_extraction` function to do this (the code for this is given to you below so you won't have to write it yourself). This function creates a version of the `ResNet34` model, loads in weights from the PyTorch ResNet34 implementation, freezes all layers, and replaces the final linear layer with an unfrozen randomly initialized linear layer with a certain number of output features (in our case 10 because we're doing feature extraction on CIFAR10 - see next section).


## CIFAR10

The benchmark we'll be doing feature extraction on is [CIFAR10](https://www.cs.toronto.edu/~kriz/cifar.html), which consists of 60000 32x32 colour images in 10 different classes (as opposed to the 1000 different classes that `ResNet34` was originally trained on). Don't peek at what other people online have done for CIFAR10 (it's a common benchmark), because the point is to develop your own process by which you can figure out how to improve your model. Just reading the results of someone else would prevent you from learning how to get the answers. To get an idea of what's possible: using one V100 and a modified ResNet, one entry in the DAWNBench competition was able to achieve 94% test accuracy in 24 epochs and 76 seconds. 94% is approximately [human level performance](http://karpathy.github.io/2011/04/27/manually-classifying-cifar10/).

Below is some boilerplate code for downloading and transforming `CIFAR10` data (this shouldn't take more than a minute to run the first time). Note, even though CIFAR10 data is 32x32, we'll resize it to 224x224 like we did for ImageNet yesterday, because ResNet expects 224x224 images as input.


```python
def get_cifar() -> tuple[datasets.CIFAR10, datasets.CIFAR10]:
    """Returns CIFAR-10 train and test sets."""
    cifar_trainset = datasets.CIFAR10(exercises_dir / "data", train=True, download=True, transform=IMAGENET_TRANSFORM)
    cifar_testset = datasets.CIFAR10(exercises_dir / "data", train=False, download=True, transform=IMAGENET_TRANSFORM)
    return cifar_trainset, cifar_testset


IMAGE_SIZE = 224
IMAGENET_MEAN = [0.485, 0.456, 0.406]
IMAGENET_STD = [0.229, 0.224, 0.225]

IMAGENET_TRANSFORM = transforms.Compose(
    [
        transforms.ToTensor(),
        transforms.Resize((IMAGE_SIZE, IMAGE_SIZE)),
        transforms.Normalize(mean=IMAGENET_MEAN, std=IMAGENET_STD),
    ]
)


cifar_trainset, cifar_testset = get_cifar()

imshow(
    cifar_trainset.data[:15],
    facet_col=0,
    facet_col_wrap=5,
    facet_labels=[cifar_trainset.classes[i] for i in cifar_trainset.targets[:15]],
    title="CIFAR-10 images",
    height=600,
    width=1000,
)
```


<div style="text-align: left"><embed src="https://info-arena.github.io/ARENA_img/misc/media-03/0306-A.html" width="1020" height="620"></div>


## Train function (modular)

First, let's build on the training function we used yesterday. Previously, we just used a single `train` function which took a dataclass as argument. But this resulted in a very long function with many nested loops and some repeated code. Instead, we'll write our code in the form of a `ResNetFinetuner` class with multiple methods, each one being responsible for a single part of the training process. This will make our code more modular, and easier to read and debug. 

We've given you the `ResNetFinetuner` class below, as well as a dataclass which contains all the hyperparameters we'll use (again this helps us keep everything organized). You should read this and make sure you understand the role of each method. A brief summary:

* `pre_training_setup` defines the model, optimizer, dataset, and objects for logging data. Note that it's not good practice to have this logic run in `__init__`, because it's something we only need to do just before actually training (this structural flexibility will prove useful later, when we introduce weights & biases).
* `training_step` does a single gradient update step on a single batch of data, and logs & returns the loss.
* `evaluate` method computes the total accuracy of the model over the validation set, and logs & returns this accuracy. Note use of the `torch.inference_mode()` decorator, which stops gradients propagating (this is equivalent to using it as a context manager).
* `train` combines this all: it performs the pre-training setup, then alternates between training & evaluation for some number of epochs. Note that `model.train()` and `model.eval()` are called before these stages respectively - for why we have to do this, see yesterday's discussion of BatchNorm.


```python
@dataclass
class ResNetFinetuningArgs:
    n_classes: int = 10
    batch_size: int = 128
    epochs: int = 3
    learning_rate: float = 1e-3
    weight_decay: float = 0.0


class ResNetFinetuner:
    def __init__(self, args: ResNetFinetuningArgs):
        self.args = args

    def pre_training_setup(self):
        self.model = get_resnet_for_feature_extraction(self.args.n_classes).to(device)
        self.optimizer = AdamW(
            self.model.out_layers[-1].parameters(),
            lr=self.args.learning_rate,
            weight_decay=self.args.weight_decay,
        )
        self.trainset, self.testset = get_cifar()
        self.train_loader = DataLoader(self.trainset, batch_size=self.args.batch_size, shuffle=True)
        self.test_loader = DataLoader(self.testset, batch_size=self.args.batch_size, shuffle=False)
        self.logged_variables = {"loss": [], "accuracy": []}
        self.examples_seen = 0

    def training_step(
        self,
        imgs: Float[Tensor, "batch channels height width"],
        labels: Int[Tensor, " batch"],
    ) -> Float[Tensor, ""]:
        """Perform a gradient update step on a single batch of data."""
        imgs, labels = imgs.to(device), labels.to(device)

        logits = self.model(imgs)
        loss = F.cross_entropy(logits, labels)
        loss.backward()
        self.optimizer.step()
        self.optimizer.zero_grad()

        self.examples_seen += imgs.shape[0]
        self.logged_variables["loss"].append(loss.item())
        return loss

    @t.inference_mode()
    def evaluate(self) -> float:
        """Evaluate the model on the test set and return the accuracy."""
        self.model.eval()
        total_correct, total_samples = 0, 0

        for imgs, labels in tqdm(self.test_loader, desc="Evaluating"):
            imgs, labels = imgs.to(device), labels.to(device)
            logits = self.model(imgs)
            total_correct += (logits.argmax(dim=1) == labels).sum().item()
            total_samples += len(imgs)

        accuracy = total_correct / total_samples
        self.logged_variables["accuracy"].append(accuracy)
        return accuracy

    def train(self) -> dict[str, list[float]]:
        self.pre_training_setup()

        accuracy = self.evaluate()

        for epoch in range(self.args.epochs):
            self.model.train()

            pbar = tqdm(self.train_loader, desc="Training")
            for imgs, labels in pbar:
                loss = self.training_step(imgs, labels)
                pbar.set_postfix(loss=f"{loss:.3f}", ex_seen=f"{self.examples_seen:06}")

            accuracy = self.evaluate()
            pbar.set_postfix(loss=f"{loss:.3f}", accuracy=f"{accuracy:.2f}", ex_seen=f"{self.examples_seen:06}")

        return self.logged_variables
```


With this class, we can perform feature extraction on our model as follows:


```python
args = ResNetFinetuningArgs()
trainer = ResNetFinetuner(args)
logged_variables = trainer.train()


line(
    y=[logged_variables["loss"][: 391 * 3 + 1], logged_variables["accuracy"][:4]],
    x_max=len(logged_variables["loss"][: 391 * 3 + 1] * args.batch_size),
    yaxis2_range=[0, 1],
    use_secondary_yaxis=True,
    labels={"x": "Examples seen", "y1": "Cross entropy loss", "y2": "Test Accuracy"},
    title="Feature extraction with ResNet34",
    width=800,
)
```


<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">Files already downloaded and verified
Files already downloaded and verified
Evaluating: 100%|██████████| 79/79 [00:23<00:00,  3.30it/s]
Training: 100%|██████████| 391/391 [02:06<00:00,  3.09it/s, ex_seen=050000, loss=0.744]
Evaluating: 100%|██████████| 79/79 [00:23<00:00,  3.39it/s]
Training: 100%|██████████| 391/391 [02:05<00:00,  3.10it/s, ex_seen=100000, loss=0.731]
Evaluating: 100%|██████████| 79/79 [00:22<00:00,  3.44it/s]
Training: 100%|██████████| 391/391 [02:05<00:00,  3.13it/s, ex_seen=150000, loss=0.584]
Evaluating: 100%|██████████| 79/79 [00:22<00:00,  3.44it/s]</pre><div style="text-align: left"><embed src="https://info-arena.github.io/ARENA_img/misc/media-03/0306.html" width="820" height="480"></div>


Let's see how well our ResNet performs on the first few inputs!


```python
def test_resnet_on_random_input(model: ResNet34, n_inputs: int = 3, seed: int | None = 42):
    if seed is not None:
        np.random.seed(seed)
    indices = np.random.choice(len(cifar_trainset), n_inputs).tolist()
    classes = [cifar_trainset.classes[cifar_trainset.targets[i]] for i in indices]
    imgs = cifar_trainset.data[indices]
    device = next(model.parameters()).device
    with t.inference_mode():
        x = t.stack(list(map(IMAGENET_TRANSFORM, imgs)))
        logits: Tensor = model(x.to(device))
    probs = logits.softmax(-1)
    if probs.ndim == 1:
        probs = probs.unsqueeze(0)
    for img, label, prob in zip(imgs, classes, probs):
        display(HTML(f"<h2>Classification probabilities (true class = {label})</h2>"))
        imshow(img, width=200, height=200, margin=0, xaxis_visible=False, yaxis_visible=False)
        bar(
            prob,
            x=cifar_trainset.classes,
            width=600,
            height=400,
            text_auto=".2f",
            labels={"x": "Class", "y": "Prob"},
        )


test_resnet_on_random_input(trainer.model)
```


<div style="text-align: left"><embed src="https://info-arena.github.io/ARENA_img/misc/media-03/0307-A.html" width="220" height="220"></div>
<div style="text-align: left"><embed src="https://info-arena.github.io/ARENA_img/misc/media-03/0307-B.html" width="620" height="420"></div>


## What is Weights and Biases?

Weights and Biases is a cloud service that allows you to log data from experiments. Your logged data is shown in graphs during training, and you can easily compare logs across different runs. It also allows you to run **sweeps**, where you can specifiy a distribution over hyperparameters and then start a sequence of test runs which use hyperparameters sampled from this distribution.

Before you run any of the code below, you should visit the [Weights and Biases homepage](https://wandb.ai/home), and create your own account.

We'll be able to keep the same structure of training loop when using weights and biases, we'll just have to add a few functions. The key functions to know are:


#### `wandb.init`

This initialises a training run. It should be called once, at the start of your training loop.

A few important arguments are:

* `project` - the name of the project where you're sending the new run. For example, this could be `'day3-resnet'` for us. You can have many different runs in each project.
* `name` - a display name for this run. By default, if this isn't supplied, wandb generates a random 2-word name for you (e.g. `gentle-sunflower-42`).
* `config` - a dictionary containing hyperparameters for this run. If you pass this dictionary, then you can compare different runs' hyperparameters & results in a single table. Alternatively, you can pass a dataclass.

#### `wandb.watch`

This function tells wandb to watch a model - this means that it will log the gradients and parameters of the model during training. We'll call this function once, after we've created our model. The 3 most important arguments are:

* `models` - a module or list of modules (e.g. in our case we might just want to log the weights of the final linear layer, because the others aren't being trained)
* `log` - determines what gets tracked, possible values are `'gradients'` (default), `'parameters'` or `'all'`
* `log_freq` - the number of batches between each logging step (default is 1000)

Why do we log parameters and gradients? Mainly this is [helpful for debugging](https://wandb.ai/wandb_fc/articles/reports/Debugging-Neural-Networks-with-PyTorch-and-W-B-Using-Gradients-and-Visualizations--Vmlldzo1NDQxNTA5), because it helps us identify problems like exploding or vanishing gradients, dead ReLUs, etc.

#### `wandb.log`

For logging metrics to the wandb dashboard. This is used as `wandb.log(data, step)`, where `step` is an integer (the x-axis on your metric plots) and `data` is a dictionary of metrics (i.e. the keys are metric names, and the values are metric values).

#### `wandb.finish`

This function should be called at the end of your training loop. It finishes the run, and saves the results to the cloud. 

If a run terminates early (either because of an error or because you manually terminated it), remember to still run `wandb.finish()` - it will speed things up when you start a new run (otherwise you have to wait for the previous run to be terminated & uploaded).


### Exercise - rewrite training loop with wandb

> ```yaml
> Difficulty: 🔴🔴⚪⚪⚪
> Importance: 🔵🔵🔵🔵⚪
> 
> You should spend up to 10-25 minutes on this exercise.
> ```

You should now take the training loop from above (i.e. the `ResNetTrainer` class) and rewrite it to use the four `wandb` functions above (in place of the `logged_variables` dictionary, which you can now remove). This will require:

- Initializing your run
    - Your new `pre_training_setup` method should call `wandb.watch` and `wandb.init` as well as all the stuff it previously did
    - For `wandb.init`, you can use the project & name arguments from your new dataclass (see below)
    - For `wandb.watch`, be careful of the `log_freq` value - you want to make sure you're logging more than once per epoch
- Logging variables to wandb during your run
    - i.e. replace updating of `self.logged_variables` with calls to `wandb.log`
    - We recommend tracking `self.examples_seen` and passing this as the `step` argument to your logging calls, this way it's easier to compare across different runs with e.g. different batch sizes (more on this later)
- Finishing the run
    - i.e. calling `wandb.finish` at the end of your training loop

This is all you need to do to get wandb working, so the vast majority of the code you write below will be copied and pasted from the previous `ResNetFinetuner` class. We've given you a template for this below, along with a new dataclass. Both the dataclass and the trainer class use inheritance to remove code duplication (e.g. because we don't need to rewrite our `__init__` method, it'll be the same as for `ResNetFinetuner`).

Note, we generally recommend keeping progress bars in wandb because they update slightly faster and can give you a better sense of whether something is going wrong in training.


```python
@dataclass
class WandbResNetFinetuningArgs(ResNetFinetuningArgs):
    """Contains new params for use in wandb.init, as well as all the ResNetFinetuningArgs params."""

    wandb_project: str | None = "day3-resnet"
    wandb_name: str | None = None


class WandbResNetFinetuner(ResNetFinetuner):
    args: WandbResNetFinetuningArgs  # adding this line helps with typechecker!
    examples_seen: int = 0  # tracking examples seen (used as step for wandb)

    def pre_training_setup(self):
        """Initializes the wandb run using `wandb.init` and `wandb.watch`."""
        super().pre_training_setup()
        raise NotImplementedError()

    def training_step(
        self,
        imgs: Float[Tensor, "batch channels height width"],
        labels: Int[Tensor, " batch"],
    ) -> Float[Tensor, ""]:
        """Equivalent to ResNetFinetuner.training_step, but logging the loss to wandb."""
        raise NotImplementedError()

    @t.inference_mode()
    def evaluate(self) -> float:
        """Equivalent to ResNetFinetuner.evaluate, but logging the accuracy to wandb."""
        raise NotImplementedError()

    def train(self) -> None:
        """Equivalent to ResNetFinetuner.train, but with wandb integration."""
        self.pre_training_setup()
        raise NotImplementedError()


args = WandbResNetFinetuningArgs()
trainer = WandbResNetFinetuner(args)
trainer.train()
```


<details><summary>Solution</summary>

```python
@dataclass
class WandbResNetFinetuningArgs(ResNetFinetuningArgs):
    """Contains new params for use in wandb.init, as well as all the ResNetFinetuningArgs params."""

    wandb_project: str | None = "day3-resnet"
    wandb_name: str | None = None


class WandbResNetFinetuner(ResNetFinetuner):
    args: WandbResNetFinetuningArgs  # adding this line helps with typechecker!
    examples_seen: int = 0  # tracking examples seen (used as step for wandb)

    def pre_training_setup(self):
        """Initializes the wandb run using `wandb.init` and `wandb.watch`."""
        super().pre_training_setup()
        wandb.init(project=self.args.wandb_project, name=self.args.wandb_name, config=self.args)
        wandb.watch(self.model.out_layers[-1], log="all", log_freq=50)
        self.examples_seen = 0

    def training_step(
        self,
        imgs: Float[Tensor, "batch channels height width"],
        labels: Int[Tensor, " batch"],
    ) -> Float[Tensor, ""]:
        """Equivalent to ResNetFinetuner.training_step, but logging the loss to wandb."""
        imgs, labels = imgs.to(device), labels.to(device)

        logits = self.model(imgs)
        loss = F.cross_entropy(logits, labels)
        loss.backward()
        self.optimizer.step()
        self.optimizer.zero_grad()

        self.examples_seen += imgs.shape[0]
        wandb.log({"loss": loss.item()}, step=self.examples_seen)
        return loss

    @t.inference_mode()
    def evaluate(self) -> float:
        """Equivalent to ResNetFinetuner.evaluate, but logging the accuracy to wandb."""
        self.model.eval()
        total_correct, total_samples = 0, 0

        for imgs, labels in tqdm(self.test_loader, desc="Evaluating"):
            imgs, labels = imgs.to(device), labels.to(device)
            logits = self.model(imgs)
            total_correct += (logits.argmax(dim=1) == labels).sum().item()
            total_samples += len(imgs)

        accuracy = total_correct / total_samples
        wandb.log({"accuracy": accuracy}, step=self.examples_seen)
        return accuracy

    def train(self) -> None:
        """Equivalent to ResNetFinetuner.train, but with wandb integration."""
        self.pre_training_setup()
        accuracy = self.evaluate()

        for epoch in range(self.args.epochs):
            self.model.train()

            pbar = tqdm(self.train_loader, desc="Training")
            for imgs, labels in pbar:
                loss = self.training_step(imgs, labels)
                pbar.set_postfix(loss=f"{loss:.3f}", ex_seen=f"{self.examples_seen=:06}")

            accuracy = self.evaluate()
            pbar.set_postfix(loss=f"{loss:.3f}", accuracy=f"{accuracy:.2f}", ex_seen=f"{self.examples_seen=:06}")

        wandb.finish()
```
</details>


When you run the code for the first time, you'll have to login to Weights and Biases, and paste an API key into VSCode. After this is done, your Weights and Biases training run will start. It'll give you a lot of output text, one line of which will look like:

```
View run at https://wandb.ai/<USERNAME>/<PROJECT-NAME>/runs/<RUN-NAME>
```

which you can click on to visit the run page.

A nice thing about using Weights and Biases is that you don't need to worry about generating your own plots, that will all be done for you when you visit the page.


<img src="https://raw.githubusercontent.com/info-arena/ARENA_img/main/misc/wandb-day3.png" width="900">


### Run & project pages

The page you visit will show you a plot of all the variables you've logged, among other things. You can do many things with these plots (e.g. click on the "edit" icon for your `train_loss` plot, and apply smoothing & change axis bounds to get a better picture of your loss curve).

<img src="https://raw.githubusercontent.com/info-arena/ARENA_img/main/misc/wandb-day3-smoothed.png" width="1000">

The charts are a useful feature of the run page that gets opened when you click on the run page link, but they're not the only feature. You can also navigate to the project page (click on the option to the right of **Projects** on the bar at the top of the Wandb page), and see superimposed plots of all the runs in this project. You can also click on the **Table** icon on the left hand sidebar to see a table of all the runs in this project, which contains useful information (e.g. runtime, the most recent values of any logged variables, etc). However, comparing runs like this becomes especially useful when we start doing hyperparameter search.

You can also look at the system tab to inspect things like GPU utilization - this is a good way of checking whether you're saturating your GPU or whether you can afford to increase your batch size more. This tab will be especially useful in the next section, when we move onto distributed training.


## Some training heuristics

One important skill which every aspiring ML researcher should develop is the ability to play around with hyperparameters and improve a model's training. At times this is more of an art than a science, because frequently rules and heuristics which work most of the time will break down in certain special cases. For example, a common heuristic for number of workers in a `DataLoader` is to set them to be 4 times the number of GPUs you have available (see later sections on distributed computing for more on this). However, setting these values too high can lead to issues where your CPU is bottlenecked by the workers and your epochs take a long time to start - it took me a long time to realize this was happening when I was initially writing these exercises!

Sweeping over hyperparameters (which we'll cover shortly) can help remove some of the difficulty here, because you can use sweep methods that guide you towards an optimal set of hyperparameter choices rather than having to manually pick your own. However, here are a few heuristics that you might find useful in a variety of situations:

- **Setting batch size**
    - Generally you should aim to **saturate your GPU** with data - this means choosing a batch size that's as large as possible without causing memory errors
        - You should generally aim for over 70% utilization of your GPU
    - Note, this means you should generally try for a larger batch size in your testloader than your trainloader (because evaluation is done without gradients, and so a smaller memory constraint)
        - A good starting point is 4x the size, but this will vary between models
- **Choosing a learning rate**
    - Inspecting loss curves can be a good way of evaluating our learning rate
        - If loss is decreasing very slowly & monotonically then this is a sign you should increase the learning rate, whereas very large loss spikes are a sign that you should decrease it
    - A common strategy is **warmup**, i.e. having a smaller learning rate for a short period of time at the start of training - we'll do this a lot in later material
    - [Jeremy Jordan](https://www.jeremyjordan.me/nn-learning-rate/) has a good blog post on learning rates
- **Balancing learning rate and batch size**
    - For standard optimizers like `SGD`, it's a good idea to scale the learning rate inversely to the batch size - this way the variance of each parameter step remains the same
    - However for **adaptive optimizers** such as `Adam` (where the size of parameter updates automatically adjusts based on the first and second moments of our gradients), this isn't as necessary
        - This is why we generally start with default parameters for Adam, and then adjust from there
- **Misc. advice**
    - If you're training a larger model, it's sometimes a good idea to start with a smaller version of that same model. Good hyperparameters tend to transfer if the architecture & data is the same; the main difference is the larger model may require more regularization to prevent overfitting.
    - Bad hyperparameters are usually clearly worse by the end of the first 1-2 epochs. You can manually abort runs that don't look promising (or do it automatically - see discussion of Hyperband in wandb sweeps at the end of this section)
    - Overfitting at the start is better than underfitting, because it means your model is capable of learning and has enough capacity


## Hyperparameter search

One way to search for good hyperparameters is to choose a set of values for each hyperparameter, and then search all combinations of those specific values. This is called **grid search**. The values don't need to be evenly spaced and you can incorporate any knowledge you have about plausible values from similar problems to choose the set of values. Searching the product of sets takes exponential time, so is really only feasible if there are a small number of hyperparameters. I would recommend forgetting about grid search if you have more than 3 hyperparameters, which in deep learning is "always".

A much better idea is for each hyperparameter, decide on a sampling distribution and then on each trial just sample a random value from that distribution. This is called **random search** and back in 2012, you could get a [publication](https://www.jmlr.org/papers/volume13/bergstra12a/bergstra12a.pdf) for this. The diagram below shows the main reason that random search outperforms grid search. Empirically, some hyperparameters matter more than others, and random search benefits from having tried more distinct values in the important dimensions, increasing the chances of finding a "peak" between the grid points.

<img src="https://raw.githubusercontent.com/callummcdougall/Fundamentals/main/images/grid_vs_random.png" width="540">


It's worth noting that both of these searches are vastly less efficient than gradient descent at finding optima - imagine if you could only train neural networks by randomly initializing them and checking the loss! Either of these search methods without a dose of human (or eventually AI) judgement is just a great way to turn electricity into a bunch of models that don't perform very well.


## Running hyperparameter sweeps with `wandb`

Now we've come to one of the most impressive features of `wandb` - being able to perform hyperparameter sweeps. We do this by defining a `sweep_config` dict which tells us how our hyperparameters will be randomly sampled, then we write a `train` function which takes no arguments and launches a training run with our modified hyperparameters. Lastly we use `wandb.sweep` and `wandb.agent` to run our sweep. We'll go through each step of this below.


### Sweep config syntax

The basic syntax for a sweep config looks like this:

```python
sweep_config = dict(
    method = method, # can be "grid", "random" or "bayes"
    metric = dict(
        name = metric_name, # name of the metric you're optimising (should be a numeric type logged in `wandb.log`)
        goal = goal, # either "maximize" or "minimize"
    )),
    parameters = dict(
        param_1 = dict(...),
        param_2 = dict(...),
        ...
    ),
)
```

The `method` argument determines how we perform search: `grid` is over all combinations, `random` independently samples each hyperparameter, and `bayes` uses Bayesian optimization to sample hyperparameters. The `metric` dict determines what logged variable we're optimizing, and in what direction. Lastly, `parameters` is a list of parameters we're varying, with each dictionary describing how we want that parameter to be sampled. Possible ways to specify distributions include:

```python
parameters = dict(
    param_1 = dict(values = [...]), # uniformly sample from list of values
    param_2 = dict(values = [...], probabilities = [...]), # sample from list with given probabilities
    param_3 = dict(min = ..., max = ...), # uniform distribution over [min, max), can either be ints or floats
    param_4 = dict(min = ..., max = ..., distribution = "log_uniform_values"), # use log-uniform distribution instead
)
```

Note on log uniform distribution - this essentially means we return `value` s.t. `log(value)` is uniformly distributed between `log(min)` and `log(max)`. It can be a useful way to sample hyperparameters which take values in a very large range.

You can read more about the syntax [here](https://docs.wandb.ai/guides/sweeps/define-sweep-configuration), but the examples we've given you above should be enough to complete the rest of these exercises.

<details>
<summary>Note on using YAML files for sweeps (optional)</summary>

Rather than using a dictionary, you can alternatively store the `sweep_config` data in a YAML file if you prefer. You will then be able to run a sweep via the following terminal commands:

```
wandb sweep sweep_config.yaml

wandb agent <SWEEP_ID>
```

where `SWEEP_ID` is the value returned from the first terminal command. You will also need to add another line to the YAML file, specifying the program to be run. For instance, your YAML file might start like this:

```yaml
program: train.py
method: random
metric:
    name: test_accuracy
    goal: maximize
```

For more, see [this link](https://docs.wandb.ai/guides/sweeps/define-sweep-configuration).

</details>


### Exercise - define a sweep config & update `args`

> ```yaml
> Difficulty: 🔴🔴⚪⚪⚪
> Importance: 🔵🔵🔵⚪⚪
> 
> You should spend up to 10-20 minutes on this exercise.
> Learning how to use wandb for sweeps is very useful, so make sure you understand all parts of this code.
> ```

Using the syntax discussed above, you should define a dictionary `sweep_config` which has the following rules for hyperparameter sweeps:

* Hyperparameters are chosen **randomly**, according to the distributions given in the dictionary
* Your goal is to **maximize** the **accuracy** metric
* The hyperparameters you vary are:
    * Learning rate - a log-uniform distribution between 1e-4 and 1e-1
    * Batch size - sampled uniformly from (32, 64, 128, 256)
    * Weight decay - with 50% probability set to 0, and with 50% probability log-uniform between 1e-4 and 1e-2

You should also fill in the `update_args` function, which returns a modified version of `args` based on the hyperparameters sampled by the sweep. In other words, it should take an `args` object and a dictionary of sampled parameters that might look something like `{"lr": 0.001, "batch_size": 64, ...}`, and return a new `args` object with these fields modified.


```python
# YOUR CODE HERE - fill `sweep_config` so it has the requested behaviour
sweep_config = dict(
    method = ...,
    metric = ...,
    parameters = ...,
)


def update_args(args: WandbResNetFinetuningArgs, sampled_parameters: dict) -> WandbResNetFinetuningArgs:
    """
    Returns a new args object with modified values. The dictionary `sampled_parameters` will have
    the same keys as your `sweep_config["parameters"]` dict, and values equal to the sampled values
    of those hyperparameters.
    """
    assert set(sampled_parameters.keys()) == set(sweep_config["parameters"].keys())

    # YOUR CODE HERE - update `args` based on `sampled_parameters`
    raise NotImplementedError()


tests.test_sweep_config(sweep_config)
tests.test_update_args(update_args, sweep_config)
```


<details>
<summary>Help - I'm not sure how to implement the weight decay distribution that was requested.</summary>

The easiest option is to include 2 parameters: one is a boolean and determines whether to use weight decay, one is log-uniform and gives you the value in the cases where it's non-zero. Both parameters are used to set the final value in `args`.

</details>

<details>
<summary>Solution</summary>

```python
sweep_config = dict(
    method="random",
    metric=dict(name="accuracy", goal="maximize"),
    parameters=dict(
        learning_rate=dict(min=1e-4, max=1e-1, distribution="log_uniform_values"),
        batch_size=dict(values=[32, 64, 128, 256]),
        weight_decay=dict(min=1e-4, max=1e-2, distribution="log_uniform_values"),
        weight_decay_bool=dict(values=[True, False]),
    ),
)

def update_args(args: WandbResNetFinetuningArgs, sampled_parameters: dict) -> WandbResNetFinetuningArgs:
    assert set(sampled_parameters.keys()) == set(sweep_config["parameters"].keys())

    args.learning_rate = sampled_parameters["learning_rate"]
    args.batch_size = sampled_parameters["batch_size"]
    args.weight_decay = sampled_parameters["weight_decay"] if sampled_parameters["weight_decay_bool"] else 0.0
    return args
```

Alternatively, for a solution with less repetition, you can use the `dataclasses.replace` function to update multiple fields of `args` at once:

```python
def update_args(args: WandbResNetFinetuningArgs, sampled_parameters: dict) -> WandbResNetFinetuningArgs:
    assert set(sampled_parameters.keys()) == set(sweep_config["parameters"].keys())

    sampled_parameters["weight_decay"] *= float(sampled_parameters.pop("weight_decay_bool"))
    return replace(args, **sampled_parameters)
```

If you use this solution, you need to be careful that the names of your fields in `sweep_config` match the names of the fields in `WandbResNetFinetuningArgs`.

</details>


Now we've done this, we'll define a `train` function that takes no arguments and launches a training run with our modified hyperparameters. This is done in the following way:

- The train function calls `wandb.init`
- Our sampled hyperparameters are now available in `wandb.config`, so we use this object to update `args`
- We then launch a training run based on these new hyperparameters

The line `sweep_id = wandb.sweep(...)` initializes a hyperparameter sweep (giving it an ID) and the line `wandb.agent(...)` starts an agent that runs the training script `train` 3 times, with different randomly sampled sets of hyperparameters each time.

Note that we pass `reinit=False` into our `wandb.init` call - this is so we ignore the second `wandb.init` call that takes place in our pretraining setup when we run `trainer.train()` (so we can avoid the hassle of having to rewrite this method to remove that line).


```python
def train():
    # Define args & initialize wandb
    args = WandbResNetFinetuningArgs()
    wandb.init(project=args.wandb_project, name=args.wandb_name, reinit=False)

    # After initializing wandb, we can update args using `wandb.config`
    args = update_args(args, dict(wandb.config))

    # Train the model with these new hyperparameters (the second `wandb.init` call will be ignored)
    trainer = WandbResNetFinetuner(args)
    trainer.train()


sweep_id = wandb.sweep(sweep=sweep_config, project="day3-resnet-sweep")
wandb.agent(sweep_id=sweep_id, function=train, count=3)
wandb.finish()
```


When you run this code, you should click on the link which looks like:

```
View sweep at https://wandb.ai/<USERNAME>/<PROJECT-NAME>/sweeps/<SWEEP-NAME>
```

This link will bring you to a page comparing each of your sweeps. You'll be able to see overlaid graphs of each of their training loss and test accuracy, as well as a bunch of other cool things like:

* Bar charts of the [importance](https://docs.wandb.ai/guides/app/features/panels/parameter-importance) (and correlation) of each hyperparameter wrt the target metric. Note that only looking at the correlation could be misleading - something can have a correlation of 1, but still have a very small effect on the metric.
* A [parallel coordinates plot](https://docs.wandb.ai/guides/app/features/panels/parallel-coordinates), which summarises the relationship between the hyperparameters in your config and the model metric you're optimising.

What can you infer from these results? Are there any hyperparameters which are especially correlated / anticorrelated with the target metric? Are there any results which suggest the model is being undertrained?

You might also want to play around with Bayesian hyperparameter search, if you get the time! Note that wandb sweeps also offer [early termination](https://docs.wandb.ai/guides/sweeps/define-sweep-configuration/#early_terminate) of runs that don't look promising, based on the [Hyperband](https://www.jmlr.org/papers/volume18/16-558/16-558.pdf) algorithm. 

To conclude - `wandb` is an incredibly useful tool when training models, and you should find yourself using it a fair amount throughout this program. You can always return to this page of exercises if you forget how any part of it works!




=== NEW CHAPTER ===


# 3️⃣ Distributed Training



> ##### Learning Objectives
>
> * Understand the different kinds of parallelization used in deep learning (data, pipeline, tensor)
> * Understand how primitive operations in `torch.distributed` work, and how they come together to enable distributed training
> * Launch and benchmark your own distributed training runs, to train your implementation of `ResNet34` from scratch

## Intro to distributed training

Distributed training is a model training paradigm that involves spreading training workload across multiple worker nodes, therefore significantly improving the speed of training and model accuracy. While distributed training can be used for any type of ML model training, it is most beneficial to use it for large models and compute demanding tasks as deep learning.

There are 2 main families of distributed training methods: **data parallelism** and **model parallelism**. In data parallelism, we split batches of data across different processes, run forward & backward passes on each separately, and accumulate the gradients to update the model parameters. In model parallelism, the model is segmented into different parts that can run concurrently in different nodes, and each one runs on the same data. Model parallelism further splits into horizontal and vertical parallelism depending on whether we're splitting the model up into sequential or parallel parts. Most often horizontal parallelism is called **tensor parallelism** (because it involves splitting up the weights in a single layer across multiple GPUs, into what we commonly call **sharded weights**), and vertical parallelism is called **pipeline parallelism**.

<img src="https://raw.githubusercontent.com/info-arena/ARENA_img/main/misc/parallelism.png" width="1100">

Data & model parallelism are both widely used, and can be more or less appropriate in different circumstances (e.g. some kind of model parallelism is necessary when your model is too large to fit on a single GPU). However it is possible to create hybrid forms of parallelism by combining these; this is especially common when training large models like current SOTA LLMs. In these exercises, we'll focus on just data parallelism, although we'll suggest a few bonus exercises that explore model parallelism.


### Summary of exercises

The exercises below will take you through **data parallelism**. You'll start by learning how to use the basic send and receive functions in PyTorch's distributed training module `torch.distributed` to transfer tensors between different processes (and different GPUs). Note that **you'll need multiple GPUs for these exercises** - we've included instructions in a dropdown below.

<details>
<summary>Getting multiple GPUs</summary>

The instructions for booting up a machine from vastai can already be found on the Streamlit homepage (i.e. navigate to "Home" on the sidebar, then to the section "Virtual Machines"). The only extra thing you'll need to do here is filter for an appropriate machine type.

We recommend filtering for "Disk Space To Allocate" (i.e. the primary slider on the top of the filter menu) of at least 40GB, not for the model (which is actually quite small) but for installing the ARENA dependencies. You should also filter for number of GPUs: we recommend 4x or 8x. You can do this using the options menu at the very top of the list of machines. Lastly, we recommend filtering for a decent PCIE Bandwidth (e.g. at least 20GB/s) - this is important for efficient gradient sychronization between GPUs. We're training a small model today: approx 22m parameters, which translates to ~88MB total size of weights, and so we'll transfer 88MB of data between GPUs per process (since we're transferring the model's gradients, which have the same size as the weights). We don't want this to be a bottleneck, which is why we should filter for this bandwidth.

Once you've filtered for this, we recommend picking an RTX 3090 or 4090 machine. These won't be as powerful as an A100, but the purpose today is more to illustrate the basic ideas behind distributed training than to push your model training to its limits. Note that if you were using an A100 then you should filter for a high NVLink Bandwidth rather than PCIE (since A100s use NVLink instead of PCIE).

</details>

Once you've done this, you'll use those 2 primitive point-to-point functions to build up some more advanced functions: `broadcast` (which gets a tensor from one process to all others), `gather` (which gathers all tensors from different devices to a single device) and `all_reduce` (which combines both `broadcast` and `gather` to make aggregate tensor values across all processes). These functions (`all_reduce` in particular) are key parts of how distributed computing works.

Lastly, you'll learn how to use these functions to build a distributed training loop, which will be adapted from the `ResNetTrainer` code from your previous exercises. We also explain how you can use `DistributedDataParallel` to abstract away these low-level operations, which you might find useful later on (although you will benefit from building these components up from scratch, and understanding how they work under the hood).


### Running these exercises

> These exercises can't all be run in a notebook or Colab, because distributed training typically requires spawning multiple processes and Jupyter notebooks run in a single interactive process - they're not designed for this kind of use-case.

You have 2 different options:

1. **Do everything in a Python file** (either `# %%`-separated cells or [execute on selection](https://stackoverflow.com/questions/38952053/how-can-i-run-text-selected-in-the-active-editor-in-vs-codes-integrated-termina)), but make sure to wrap any execution code in `if __name__ == "__main__":` blocks. This makes sure that when you launch multiple processes they don't recursively launch their own processes, and they'll only execute the code you want them to.
2. **Write your functions in a Python file, then import & run them in a notebook**. For example in the example code below, you could define the `send_receive` function in a Python file, then import this function & pass it into the `mp.spawn()` call.

In either case, make sure when you run `mp.spawn` you're passing in the most updated version of your function. This means saving the Python file after you make changes, and also using something like `importlib.reload()` if you're running the code in a notebook.


```python
IN_COLAB = "google.colab" in sys.modules
assert not IN_COLAB, "Should be doing these exercises in VS Code"
```


## Basic send & receiving

The code below is a simplified example that demonstrates distributed communication between multiple processes.

At the highest level, `mp.spawn()` launches multiple worker processes, each with a unique rank. For each worker, we create a new Python interpreter (called a "child process") which will execute the function passed to `mp.spawn` (which in this case is `send_receive`). The function has to have the type signature `fn(rank, *args)` where `args` is the tuple we pass into `mp.spawn()`. The total number of processes is determined by `world_size`. Note that this isn't the same as the number of GPUs - in fact, in the code below we've not moved any of our data to GPUs, we're just using the distributed API to sync data across multiple processes. We'll introduce GPUs in the code below this!

We require the environment variables `MASTER_ADDR` and `MASTER_PORT` to be set before launching & communicating between processes. The former specifies the IP address or hostname of the machine that will act as the central coordinator (the "master" node) for setting up and managing the distributed environment, while the latter specifies the port number that the master node will use for communication. In our case we're running all our processes from a single node, so all we need is for this to be an unused port on our machine.

Now, breaking down the `send_receive` function line by line:

- `dist.init_process_group` initializes each process with a common address and port, and a communication backend. It also gives each process a unique rank, so they know who is sending & receiving data.
- If the function is being run by rank 0, then we create a tensor of zeros and send it using `dist.send`.
- If the function is being run by rank 1, then we create a tensor of ones and wait to receive a tensor from rank 0 using `dist.recv`. This will overwrite the data in the original tensor that we created, i.e. so we're just left with a tensor of zeros.
- `dist.destroy_process_group()` is called at the end of the function to destroy the process group and release resources.

The functions `dist.send` and `dist.recv` are the basic primitives for point-to-point communication between processes (we'll look at the primitives for collective communication later on). Each `recv` for a given source process `src` will wait until it receives a `send` from that source to continue, and likewise each `send` to a given destination process `dst` will wait until it receives a `recv` from that process to continue. We call these **blocking operations** (later on we'll look at non-blocking operations).


```python
WORLD_SIZE = min(t.cuda.device_count(), 3)

os.environ["MASTER_ADDR"] = "localhost"
os.environ["MASTER_PORT"] = "12345"


def send_receive(rank, world_size):
    dist.init_process_group(backend="gloo", rank=rank, world_size=world_size)

    if rank == 0:
        # Send tensor to rank 1
        sending_tensor = t.zeros(1)
        print(f"{rank=}, sending {sending_tensor=}")
        dist.send(tensor=sending_tensor, dst=1)
    elif rank == 1:
        # Receive tensor from rank 0
        received_tensor = t.ones(1)
        print(f"{rank=}, creating {received_tensor=}")
        dist.recv(received_tensor, src=0)  # this line overwrites the tensor's data with our `sending_tensor`
        print(f"{rank=}, received {received_tensor=}")

    dist.destroy_process_group()


if MAIN:
    world_size = 2  # simulate 2 processes
    mp.spawn(
        send_receive,
        args=(world_size,),
        nprocs=world_size,
        join=True,
    )
```


<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">rank=0, sending sending_tensor=tensor([0.])
rank=1, creating received_tensor=tensor([1.])
rank=1, received received_tensor=tensor([0.])</pre>


Now, let's adapt this toy example to work with our multiple GPUs! You can check how many GPUs you have access to using `torch.cuda.device_count()`.


```python
assert t.cuda.is_available()
assert t.cuda.device_count() > 1, "This example requires at least 2 GPUs per machine"
```


Before writing our new code, let's first return to the `backend` argument for `dist.init_process_group`. There are 3 main backends for distributed training: MPI, GLOO and NCCL. The first two are more general-purpose and support both CPU & GPU tensor communication, while NCCL is a GPU-only protocol optimized specifically for NVIDIA GPUs. It provides better bandwidth and lower latency for GPU-GPU communication, and so we'll be using it for subsequent exercises.

When sending & receiving tensors between GPUs with a NCCL backend, there are 3 important things to remember:

1. Send & received tensors should be of the same datatype.
2. Tensors need to be moved to the GPU before sending or receiving.
3. No two processes should be using the same GPU.

Because of this third point, each process `rank` will be using the GPU with index `rank` - hence we'll sometimes refer to the process rank and its corresponding GPU index interchangeably. However it's worth emphasizing that this only applies to our specific data parallelism & NCCL backend example, and so this correspondence doesn't have to exist in general.

The code below is a slightly modified version of the prior code; all we're doing is changing the backend to NCCL & moving the tensors to the appropriate device before sending or receiving.

Note - if at any point during this section you get errors related to the socket, then you can kill the processes by running `kill -9 <pid>` where `<pid>` is the process ID. If the process ID isn't given in the error message, you can find it using `lsof -i :<port>` where `<port>` is the port number specified in `os.environ["MASTER_PORT"]` (note you might have to `sudo apt-get install lsof` before you can run this). If your code is still failing, try changing the port in `os.environ["MASTER_PORT"]` and running it again.

<!-- Note - an alternative to explicitly defining the device here is to run the line `torch.cuda.set_device(rank)`, then code like `tensor.cuda()` will automatically send the tensor to the correct device. Which one you use is a matter of preference, however for the solutions & demo code we'll stick with the explicit device definition. -->


```python
def send_receive_nccl(rank, world_size):
    dist.init_process_group(backend="nccl", rank=rank, world_size=world_size)

    device = t.device(f"cuda:{rank}")

    if rank == 0:
        # Create a tensor, send it to rank 1
        sending_tensor = t.tensor([rank], device=device)
        print(f"{rank=}, {device=}, sending {sending_tensor=}")
        dist.send(sending_tensor, dst=1)  # Send tensor to CPU before sending
    elif rank == 1:
        # Receive tensor from rank 0 (it needs to be on the CPU before receiving)
        received_tensor = t.tensor([rank], device=device)
        print(f"{rank=}, {device=}, creating {received_tensor=}")
        dist.recv(received_tensor, src=0)  # this line overwrites the tensor's data with our `sending_tensor`
        print(f"{rank=}, {device=}, received {received_tensor=}")

    dist.destroy_process_group()


if MAIN:
    world_size = 2  # simulate 2 processes
    mp.spawn(
        send_receive_nccl,
        args=(world_size,),
        nprocs=world_size,
        join=True,
    )
```


<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">rank=1, device=device(type='cuda', index=1), creating received_tensor=tensor([1], device='cuda:1')
rank=0, device=device(type='cuda', index=0), sending sending_tensor=tensor([0], device='cuda:0')
rank=1, device=device(type='cuda', index=1), received received_tensor=tensor([0], device='cuda:1')</pre>


## Collective communication primitives

We'll now move from basic point-to-point communication to **collective communication**. This refers to operations that synchronize data across multiple processes, rather than just between a single sender and receiver. There are 3 important kinds of collective communication functions:

- **Broadcast**: send a tensor from one process to all other processes
- **Gather**: collect tensors from all processes and concatenates them into a single tensor
- **Reduce**: like gather, but perform a reduction operation (e.g. sum, mean) rather than concatenation

The latter 2 functions have different variants depending on whether you want the final result to be in just a single destination process or in all of them: for example `dist.gather` will gather data to a single destination process, while `dist.all_gather` will make sure every process ends up with all the data.

The functions we're most interested in building are `broadcast` and `all_reduce` - the former for making sure all processes have the same initial model parameters, and the latter for aggregating gradients across all processes.


### Exercise - implement `broadcast`

> ```yaml
> Difficulty: 🔴🔴🔴⚪⚪
> Importance: 🔵🔵🔵⚪⚪
> 
> You should spend up to 10-20 minutes on this exercise.
> ```

Below, you should implement `broadcast`. If you have tensor $T_i$ on process $i$ for each index, then after running this function you should have $T_s$ on all processes, where $s$ is the source process. If you're confused, you can see exactly what is expected of you by reading the test code in `tests.py`. Again, remember that you should be running tests either from the command line or in the Python interactive terminal, not in a notebook cell.


```python
def broadcast(tensor: Tensor, rank: int, world_size: int, src: int = 0):
    """
    Broadcast averaged gradients from rank 0 to all other ranks.
    """
    raise NotImplementedError()


if MAIN:
    tests.test_broadcast(broadcast, WORLD_SIZE)
```


<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">Rank 1 broadcasted tensor: expected 0.0 (from rank 0), got tensor([0.], device='cuda:1')
Rank 0 broadcasted tensor: expected 0.0 (from rank 0), got tensor([0.], device='cuda:0')
Rank 2 broadcasted tensor: expected 0.0 (from rank 0), got tensor([0.], device='cuda:2')
All tests in `test_broadcast` passed!</pre>


<details><summary>Solution</summary>

```python
def broadcast(tensor: Tensor, rank: int, world_size: int, src: int = 0):
    """
    Broadcast averaged gradients from rank 0 to all other ranks.
    """
    if rank == src:
        for other_rank in range(world_size):
            if other_rank != src:
                dist.send(tensor, dst=other_rank)
    else:
        received_tensor = t.zeros_like(tensor)
        dist.recv(received_tensor, src=src)
        tensor.copy_(received_tensor)
```
</details>


### Exercise - implement `all_reduce`

> ```yaml
> Difficulty: 🔴🔴🔴⚪⚪
> Importance: 🔵🔵🔵⚪⚪
> 
> You should spend up to 10-20 minutes on this exercise.
> ```

You should now implement `reduce` and `all_reduce`. The former will aggregate the tensors at some destination process (either sum or mean), and the latter will do the same but then broadcast the result to all processes.

Note, more complicated allreduce algorithms exist than this naive one, and you'll be able to look at some of them in the bonus material.


```python
def reduce(tensor, rank, world_size, dst=0, op: Literal["sum", "mean"] = "sum"):
    """
    Reduces gradients to rank `dst`, so this process contains the sum or mean of all tensors across
    processes.
    """
    raise NotImplementedError()


def all_reduce(tensor, rank, world_size, op: Literal["sum", "mean"] = "sum"):
    """
    Allreduce the tensor across all ranks, using 0 as the initial gathering rank.
    """
    raise NotImplementedError()


if MAIN:
    tests.test_reduce(reduce, WORLD_SIZE)
    tests.test_all_reduce(all_reduce, WORLD_SIZE)
```


<details><summary>Solution</summary>

```python
def reduce(tensor, rank, world_size, dst=0, op: Literal["sum", "mean"] = "sum"):
    """
    Reduces gradients to rank `dst`, so this process contains the sum or mean of all tensors across
    processes.
    """
    if rank != dst:
        dist.send(tensor, dst=dst)
    else:
        for other_rank in range(world_size):
            if other_rank != dst:
                received_tensor = t.zeros_like(tensor)
                dist.recv(received_tensor, src=other_rank)
                tensor += received_tensor
    if op == "mean":
        tensor /= world_size


def all_reduce(tensor, rank, world_size, op: Literal["sum", "mean"] = "sum"):
    """
    Allreduce the tensor across all ranks, using 0 as the initial gathering rank.
    """
    reduce(tensor, rank, world_size, dst=0, op=op)
    broadcast(tensor, rank, world_size, src=0)
```
</details>


<!-- <pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">Running reduce on dst=0, with initial tensors: [0, 0], [1, 2], [10, 20]
Rank 1, op='sum', expected non-reduced tensor([1., 2.]), got tensor([1., 2.])
Rank 1, op='mean', expected non-reduced tensor([0.3333, 0.6667]), got tensor([0.3333, 0.6667])
Rank 0, op='sum', expected reduced tensor([11., 22.]), got tensor([11., 22.])
Rank 2, op='sum', expected non-reduced tensor([10., 20.]), got tensor([10., 20.])
Rank 0, op='mean', expected reduced tensor([3.6667, 7.3333]), got tensor([3.6667, 7.3333])
Rank 2, op='mean', expected non-reduced tensor([3.3333, 6.6667]), got tensor([3.3333, 6.6667])
All tests in `test_reduce` passed!

Running all_reduce, with initial tensors: [0, 0], [1, 2], [10, 20]
Rank 1, op='sum', expected non-reduced tensor([11., 22.]), got tensor([11., 22.])
Rank 2, op='sum', expected non-reduced tensor([11., 22.]), got tensor([11., 22.])
Rank 0, op='sum', expected non-reduced tensor([11., 22.]), got tensor([11., 22.])
Rank 1, op='mean', expected non-reduced tensor([3.6667, 7.3333]), got tensor([3.6667, 7.3333])
Rank 2, op='mean', expected non-reduced tensor([3.6667, 7.3333]), got tensor([3.6667, 7.3333])
Rank 0, op='mean', expected non-reduced tensor([3.6667, 7.3333]), got tensor([3.6667, 7.3333])
All tests in `test_all_reduce` passed!</pre> -->

Once you've passed these tests, you can run the code below to see how this works for a toy example of model training. In this case our model just has a single parameter and we're performing gradient descent using the squared error between its parameters and the input data as our loss function (in other words we're training the model's parameters to equal the mean of the input data). 

The data in the example below is the same as the rank index, i.e. `r = 0, 1`. For initial parameter `x = 2` this gives us errors of `(x-r).pow(2) = 4, 2` respectively, and gradients of `2x(x-r) = 8, 4`. Averaging these gives us a gradient of `6`, so after a single optimization step with learning rate `lr=0.1` we get our gradients changing to `2.0 - 0.6 = 1.4`.


```python
class SimpleModel(t.nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.param = t.nn.Parameter(t.tensor([2.0]))

    def forward(self, x: Tensor):
        return x - self.param


def run_simple_model(rank, world_size):
    dist.init_process_group(backend="nccl", rank=rank, world_size=world_size)

    device = t.device(f"cuda:{rank}")
    model = SimpleModel().to(device)  # Move the model to the device corresponding to this process
    optimizer = t.optim.SGD(model.parameters(), lr=0.1)

    input = t.tensor([rank], dtype=t.float32, device=device)
    output = model(input)
    loss = output.pow(2).sum()
    loss.backward()  # Each rank has separate gradients at this point

    print(f"Rank {rank}, before all_reduce, grads: {model.param.grad=}")
    all_reduce(model.param.grad, rank, world_size)  # Synchronize gradients
    print(f"Rank {rank}, after all_reduce, synced grads (summed over processes): {model.param.grad=}")

    optimizer.step()  # Step with the optimizer (this will update all models the same way)
    print(f"Rank {rank}, new param: {model.param.data}")

    dist.destroy_process_group()


if MAIN:
    world_size = 2
    mp.spawn(
        run_simple_model,
        args=(world_size,),
        nprocs=world_size,
        join=True,
    )
```


<details><summary>Click to see the expected output</summary>

<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">Rank 1, before all_reduce, grads: model.param.grad=tensor([2.], device='cuda:1')
Rank 0, before all_reduce, grads: model.param.grad=tensor([4.], device='cuda:0')
Rank 0, after all_reduce, synced grads (summed over processes): model.param.grad=tensor([6.], device='cuda:0')
Rank 1, after all_reduce, synced grads (summed over processes): model.param.grad=tensor([6.], device='cuda:1')
Rank 0, new param: tensor([1.4000], device='cuda:0')
Rank 1, new param: tensor([1.4000], device='cuda:1')</pre>

</details>


## Full training loop

We'll now use everything we've learned to put together a full training loop! Rather than finetuning it which we've been doing so far, you'll be training your resnet from scratch (although still using the same CIFAR10 dataset). We've given you a function `get_untrained_resnet` which uses the `ResNet34` class from yesterday's solutions, although you're encouraged to replace this function with your implementation if you've completed those exercises.

There are 4 key elements you'll need to change from the non-distributed version of training:

1. **Weight broadcasting at initialization**
    - For each process you'll need to initialize your model and move it onto the corresponding GPU, but you also want to make sure each process is working with the same model. You do this by **broadcasting weights in the `__init__` method**, e.g. using process 0 as the shared source process.
    - Note - you may find you'll have to brodcast `param.data` rather than `param` when you iterate through the model's parameters, because broadcasting only works for tensors not parameters. Parameters are a special class wrapping around and extending standard PyTorch tensors - we'll look at this in more detail tomorrow!
2. **Dataloader sampling at each epoch**
    - Distributed training works by splitting each batch of data across all the running processes, and so we need to implement this by splitting each batch randomly across our GPUs.
    - Some sample code for this is given below - we recommend you start with this (although you're welcome to play around with some of the parameters here like `num_workers` and `pin_memory`).
3. **Parameter syncing after each training step**
    - After each `loss.backward()` call but before stepping with the optimizer, you'll need to use `all_reduce` to sync gradients across each parameter in the model.
    - Just like in the example we gave above, calling `all_reduce` on `param.grad` should work, because `.grad` is a standard PyTorch tensor.
4. **Aggregating correct predictions after each evaluation step**\*
    - We can also split the evaluation step across GPUs - we use `all_reduce` at the end of the `evaluate` method to sum the total number of correct predictions across GPUs.
    - This is optional, and often it's not implemented because the evaluation step isn't a bottleneck compared to training, however we've included it in our solutions for completeness.

<details>
<summary>Dataloader sampling example code</summary>

```python
self.train_sampler = t.utils.data.DistributedSampler(
    self.trainset,
    num_replicas=args.world_size, # we'll divide each batch up into this many random sub-batches
    rank=self.rank, # this determines which sub-batch this process gets
)
self.train_loader = t.utils.data.DataLoader(
    self.trainset,
    self.args.batch_size, # this is the sub-batch size, i.e. the batch size that each GPU gets
    sampler=self.train_sampler, 
    num_workers=2,  # setting this low so as not to risk bottlenecking CPU resources
    pin_memory=True,  # this can improve data transfer speed between CPU and GPU
)

for epoch in range(self.args.epochs):
self.train_sampler.set_epoch(epoch)
for imgs, labels in self.train_loader:
    ...
```

</details>


### Exercise - complete `DistResNetTrainer`

> ```yaml
> Difficulty: 🔴🔴🔴🔴🔴
> Importance: 🔵🔵🔵⚪⚪
> 
> You should spend up to 30-60 minutes on this exercise.
> If you get stuck on specific bits, you're encouraged to look at the solutions for guidance.
> ```

We've given you the function `dist_train_resnet_from_scratch` which you'll be able to pass into `mp.spawn` just like the examples above, and we've given you a very light template for the `DistResNetTrainer` class which you should fill in. Your job is just to make the 4 adjustments described above. We recommend not using inheritance for this, because there are lots of minor modifications you'll need to make to the previous code and so you won't be reducing code duplication by very much. 

A few last tips before we get started:

- If your code is running slowly, we recommend you also `wandb.log` the duration of each stage of the training step from the rank 0 process (fwd pass, bwd pass, and `all_reduce` for parameter syncing), as well as logging the duration of the training & evaluation phases across the epoch. These kinds of logs are generally very helpful for debugging slow code.
- Since running this code won't directly return your model as output, it's good practice to save your model at the end of training using `torch.save`.
- We recommend you increment `examples_seen` by the total number of examples across processes, i.e. `len(input) * world_size`. This will help when you're comparing across different runs with different world sizes (it's convenient for them to have a consistent x-axis).


```python
def get_untrained_resnet(n_classes: int) -> ResNet34:
    """
    Gets untrained resnet using code from part2_cnns.solutions (you can replace this with your
    implementation).
    """
    resnet = ResNet34()
    resnet.out_layers[-1] = Linear(resnet.out_features_per_group[-1], n_classes)
    return resnet


@dataclass
class DistResNetTrainingArgs(WandbResNetFinetuningArgs):
    world_size: int = 1
    wandb_project: str | None = "day3-resnet-dist-training"


class DistResNetTrainer:
    args: DistResNetTrainingArgs

    def __init__(self, args: DistResNetTrainingArgs, rank: int):
        self.args = args
        self.rank = rank
        self.device = t.device(f"cuda:{rank}")

    def pre_training_setup(self):
        raise NotImplementedError()

    def training_step(self, imgs: Tensor, labels: Tensor) -> Tensor:
        raise NotImplementedError()

    @t.inference_mode()
    def evaluate(self) -> float:
        raise NotImplementedError()

    def train(self):
        raise NotImplementedError()


def dist_train_resnet_from_scratch(rank, world_size):
    dist.init_process_group(backend="nccl", rank=rank, world_size=world_size)
    args = DistResNetTrainingArgs(world_size=world_size)
    trainer = DistResNetTrainer(args, rank)
    trainer.train()
    dist.destroy_process_group()


if MAIN:
    world_size = t.cuda.device_count()
    mp.spawn(
        dist_train_resnet_from_scratch,
        args=(world_size,),
        nprocs=world_size,
        join=True,
    )
```


<details><summary>Solution</summary>

```python
def get_untrained_resnet(n_classes: int) -> ResNet34:
    """
    Gets untrained resnet using code from part2_cnns.solutions (you can replace this with your
    implementation).
    """
    resnet = ResNet34()
    resnet.out_layers[-1] = Linear(resnet.out_features_per_group[-1], n_classes)
    return resnet


@dataclass
class DistResNetTrainingArgs(WandbResNetFinetuningArgs):
    world_size: int = 1
    wandb_project: str | None = "day3-resnet-dist-training"


class DistResNetTrainer:
    args: DistResNetTrainingArgs

    def __init__(self, args: DistResNetTrainingArgs, rank: int):
        self.args = args
        self.rank = rank
        self.device = t.device(f"cuda:{rank}")

    def pre_training_setup(self):
        self.model = get_untrained_resnet(self.args.n_classes).to(self.device)
        if self.args.world_size > 1:
            for param in self.model.parameters():
                broadcast(param.data, self.rank, self.args.world_size, src=0)
                # dist.broadcast(param.data, src=0)

        self.optimizer = t.optim.AdamW(
            self.model.parameters(), lr=self.args.learning_rate, weight_decay=self.args.weight_decay
        )

        self.trainset, self.testset = get_cifar()
        self.train_sampler = self.test_sampler = None
        if self.args.world_size > 1:
            self.train_sampler = DistributedSampler(self.trainset, num_replicas=self.args.world_size, rank=self.rank)
            self.test_sampler = DistributedSampler(self.testset, num_replicas=self.args.world_size, rank=self.rank)
        dataloader_shared_kwargs = dict(batch_size=self.args.batch_size, num_workers=2, pin_memory=True)
        self.train_loader = DataLoader(self.trainset, sampler=self.train_sampler, **dataloader_shared_kwargs)
        self.test_loader = DataLoader(self.testset, sampler=self.test_sampler, **dataloader_shared_kwargs)
        self.examples_seen = 0

        if self.rank == 0:
            wandb.init(
                project=self.args.wandb_project,
                name=self.args.wandb_name,
                config=self.args,
            )

    def training_step(self, imgs: Tensor, labels: Tensor) -> Tensor:
        t0 = time.time()

        # Forward pass
        imgs, labels = imgs.to(self.device), labels.to(self.device)
        logits = self.model(imgs)
        t1 = time.time()

        # Backward pass
        loss = F.cross_entropy(logits, labels)
        loss.backward()
        t2 = time.time()

        # Gradient sychronization
        if self.args.world_size > 1:
            for param in self.model.parameters():
                all_reduce(param.grad, self.rank, self.args.world_size, op="mean")
                # dist.all_reduce(param.grad, op=dist.ReduceOp.SUM); param.grad /= self.args.world_size
        t3 = time.time()

        # Optimizer step, update examples seen & log data
        self.optimizer.step()
        self.optimizer.zero_grad()
        self.examples_seen += imgs.shape[0] * self.args.world_size
        if self.rank == 0:
            wandb.log(
                {
                    "loss": loss.item(),
                    "fwd_time": (t1 - t0),
                    "bwd_time": (t2 - t1),
                    "dist_time": (t3 - t2),
                },
                step=self.examples_seen,
            )
        return loss

    @t.inference_mode()
    def evaluate(self) -> float:
        self.model.eval()
        total_correct, total_samples = 0, 0

        for imgs, labels in tqdm(self.test_loader, desc="Evaluating", disable=self.rank != 0):
            imgs, labels = imgs.to(self.device), labels.to(self.device)
            logits = self.model(imgs)
            total_correct += (logits.argmax(dim=1) == labels).sum().item()
            total_samples += len(imgs)

        # Turn total_correct & total_samples into a tensor, so we can use all_reduce to sum them
        # across processes
        tensor = t.tensor([total_correct, total_samples], device=self.device)
        all_reduce(tensor, self.rank, self.args.world_size, op="sum")
        total_correct, total_samples = tensor.tolist()

        accuracy = total_correct / total_samples
        if self.rank == 0:
            wandb.log({"accuracy": accuracy}, step=self.examples_seen)
        return accuracy

    def train(self):
        self.pre_training_setup()

        accuracy = self.evaluate()  # our evaluate method is the same as parent class

        for epoch in range(self.args.epochs):
            t0 = time.time()

            if self.args.world_size > 1:
                self.train_sampler.set_epoch(epoch)
                self.test_sampler.set_epoch(epoch)

            self.model.train()

            pbar = tqdm(self.train_loader, desc="Training", disable=self.rank != 0)
            for imgs, labels in pbar:
                loss = self.training_step(imgs, labels)
                pbar.set_postfix(loss=f"{loss:.3f}", ex_seen=f"{self.examples_seen=:06}")

            accuracy = self.evaluate()

            if self.rank == 0:
                wandb.log({"epoch_duration": time.time() - t0}, step=self.examples_seen)
                pbar.set_postfix(
                    loss=f"{loss:.3f}",
                    accuracy=f"{accuracy:.3f}",
                    ex_seen=f"{self.examples_seen=:06}",
                )

        if self.rank == 0:
            wandb.finish()
            t.save(self.model.state_dict(), f"resnet_{self.rank}.pth")


def dist_train_resnet_from_scratch(rank, world_size):
    dist.init_process_group(backend="nccl", rank=rank, world_size=world_size)
    args = DistResNetTrainingArgs(world_size=world_size)
    trainer = DistResNetTrainer(args, rank)
    trainer.train()
    dist.destroy_process_group()
```
</details>


## Bonus - DDP

In practice, the most convenient way to use DDP is to wrap your model in `torch.nn.parallel.DistributedDataParallel`, which removes the need for explicitly calling `broadcast` at the start and `all_reduce` at the end of each training step. When you define a model in this way, it will automatically broadcast its weights to all processes, and the gradients will sync after each `loss.backward()` call. Here's the example `SimpleModel` code from above, rewritten to use these features:


```python
from torch.nn.parallel import DistributedDataParallel as DDP


def run(rank: int, world_size: int):
    dist.init_process_group(backend="nccl", rank=rank, world_size=world_size)

    device = t.device(f"cuda:{rank}")
    model = DDP(SimpleModel().to(device), device_ids=[rank])  # Wrap the model with DDP
    optimizer = t.optim.SGD(model.parameters(), lr=0.1)

    input = t.tensor([rank], dtype=t.float32, device=device)
    output = model(input)
    loss = output.pow(2).sum()
    loss.backward()  # DDP handles gradient synchronization

    optimizer.step()
    print(f"Rank {rank}, new param: {model.module.param.data}")

    dist.destroy_process_group()


if MAIN:
    world_size = 2
    mp.spawn(
        run,
        args=(world_size,),
        nprocs=world_size,
        join=True,
    )
```


Can you use these features to rewrite your ResNet training code? Can you compare it to the code you wrote and see how much faster the built-in DDP version is? Note, you won't be able to separate the time taken for backward passes and gradient synchronization since these happen in the same line, but you can assume that the time taken for the backward pass is approximately unchanged and so any speedup you see is due to the better gradient synchronization.


## Bonus - ring operations

Our all reduce operation would scale quite badly when we have a large number of models. It chooses a single process as the source process to receive then send out all data, and so this process risks becoming a bottleneck. One of the most popular alternatives is **ring all-reduce**. Broadly speaking, ring-based algorithms work by sending data in a cyclic pattern (i.e. worker `n` sends it to worker `n+1 % N` where `N` is the total number of workers). After each sending round, we perform a reduction operation to the data that was just sent. [This blog post](https://andrew.gibiansky.com/blog/machine-learning/baidu-allreduce/) illustrates the ring all-reduce algorithm for the sum operation.

Can you implement the ring all-reduce algorithm by filling in the function below & passing tests? Once you've implemented it, you can compare the speed of your ring all-reduce vs the all-reduce we implemented earlier - is it faster? Do you expect it to be faster in this particular case?


```python
def ring_all_reduce(tensor: Tensor, rank, world_size, op: Literal["sum", "mean"] = "sum") -> None:
    """
    Ring all_reduce implementation using non-blocking send/recv to avoid deadlock.
    """
    raise NotImplementedError()


if MAIN:
    tests.test_all_reduce(ring_all_reduce)
```


<details>
<summary>Solution</summary>

```python
def ring_all_reduce(tensor: Tensor, rank, world_size, op: Literal["sum", "mean"] = "sum") -> None:
    """
    Ring all_reduce implementation using non-blocking send/recv to avoid deadlock.
    """
    # Clone the tensor as the "send_chunk" for initial accumulation
    send_chunk = tensor.clone()

    # Step 1: Reduce-Scatter phase
    for _ in range(world_size - 1):
        # Compute the ranks involved in this round of sending/receiving
        send_to = (rank + 1) % world_size
        recv_from = (rank - 1 + world_size) % world_size

        # Prepare a buffer for the received chunk
        recv_chunk = t.zeros_like(send_chunk)

        # Non-blocking send and receive
        send_req = dist.isend(send_chunk, dst=send_to)
        recv_req = dist.irecv(recv_chunk, src=recv_from)
        send_req.wait()
        recv_req.wait()

        # Accumulate the received chunk into the tensor
        tensor += recv_chunk

        # Update send_chunk for the next iteration
        send_chunk = recv_chunk

    # Step 2: All-Gather phase
    send_chunk = tensor.clone()
    for _ in range(world_size - 1):
        # Compute the ranks involved in this round of sending/receiving
        send_to = (rank + 1) % world_size
        recv_from = (rank - 1 + world_size) % world_size

        # Prepare a buffer for the received chunk
        recv_chunk = t.zeros_like(send_chunk)

        # Non-blocking send and receive, and wait for completion
        send_req = dist.isend(send_chunk, dst=send_to)
        recv_req = dist.irecv(recv_chunk, src=recv_from)
        send_req.wait()
        recv_req.wait()

        # Update the tensor with received data
        tensor.copy_(recv_chunk)

        # Update send_chunk for the next iteration
        send_chunk = recv_chunk

    # Step 3: Average the final result
    if op == "mean":
        tensor /= world_size
```

We should expect this algorithm to be better when we scale up the number of GPUs, but it won't always be faster in small-world settings like ours, because the naive allreduce algorithm requires fewer individual communication steps and this could outweigh the benefits brought by the ring-based allreduce.

</details>




=== NEW CHAPTER ===


# ☆ Bonus


Congratulations for getting to the end of the main content! This section gives some suggestions for more features of Weights and Biases to explore, or some other experiments you can run.


## Scaling Laws


These bonus exercises are taken directly from Jacob Hilton's [online deep learning curriculum](https://github.com/jacobhilton/deep_learning_curriculum/blob/master/2-Scaling-Laws.md) (which is what the original version of the ARENA course was based on).

First, you can start by reading the [Chinchilla paper](https://arxiv.org/abs/2203.15556). This is a correction to the original scaling laws paper: parameter count scales linearly with token budget for compute-optimal models, not ~quadratically. The difference comes from using a separately-tuned learning rate schedule for each token budget, rather than using a single training run to measure performance for every token budget. This highlights the importance of hyperparameter tuning for measuring scaling law exponents.

You don't have to read the entire paper, just skim the graphs. Don't worry if they don't all make sense yet (it will be more illuminating when we study LLMs next week). Note that, although it specifically applies to language models, the key underlying ideas of tradeoffs between optimal dataset size and model size are generally applicable.

### Suggested exercise

Perform your own study of scaling laws for MNIST.

- Write a script to train a small CNN on MNIST, or find one you have written previously.
- Training for a single epoch only, vary the model size and dataset size. For the model size, multiply the width by powers of sqrt(2) (rounding if necessary - the idea is to vary the amount of compute used per forward pass by powers of 2). For the dataset size, multiply the fraction of the full dataset used by powers of 2 (i.e. 1, 1/2, 1/4, ...). To reduce noise, use a few random seeds and always use the full validation set.
- The learning rate will need to vary with model size. Either tune it carefully for each model size, or use the rule of thumb that for Adam, the learning rate should be proportional to the initialization scale, i.e. `1/sqrt(fan_in)` for the standard Kaiming He initialization (which is what PyTorch generally uses by default).
    - Note - `fan_in` refers to the variable $N_{in}$, which is `in_features` for a linear layer, and `in_channels * kernel_size * kernel_size` for a convolutional layer - in other words, the number of input parameters/activations we take a sumproduct over to get each output activation.
- Plot the amount of compute used (on a log scale) against validation loss. The compute-efficient frontier should follow an approximate power law (straight line on a log scale).
How does validation accuracy behave?
- Study how the compute-efficient model size varies with compute. This should also follow an approximate power law. Try to estimate its exponent.
- Repeat your entire experiment with 20% [dropout](https://pytorch.org/docs/stable/generated/torch.nn.Dropout.html) to see how this affects the scaling exponents.


## Other WandB features

Here are a few more Weights & Biases features you might also want to play around with:

* [Logging media and objects in experiments](https://docs.wandb.ai/guides/track/log?fbclid=IwAR3NxKsGpEjZwq3vSwYkohZllMpBwxHgOCc_k0ByuD9XGUsi_Scf5ELvGsQ) - you'll be doing this during the RL week, and it's useful when you're training generative image models like VAEs and diffusion models.
* [Code saving](https://docs.wandb.ai/guides/app/features/panels/code?fbclid=IwAR2BkaXbRf7cqEH8kc1VzqH_kOJWGxqjUb_JCBq_SCnXOx1oF-Rt-hHydb4) - this captures all python source code files in the current director and all subdirectories. It's great for reproducibility, and also for sharing your code with others.
* [Saving and loading PyTorch models](https://wandb.ai/wandb/common-ml-errors/reports/How-to-Save-and-Load-Models-in-PyTorch--VmlldzozMjg0MTE?fbclid=IwAR1Y9MzFTxIiVBJG06b4ppitwKWR4H5_ncKyT2F_rR5Z_IHawmpBTKskPcQ) - you can do this easily using `torch.save`, but it's also possible to do this directly through Weights and Biases as an **artifact**.


## The Optimizer's Curse

The [optimizer's curse](https://www.lesswrong.com/posts/5gQLrJr2yhPzMCcni/the-optimizer-s-curse-and-how-to-beat-it) applies to tuning hyperparameters. The main take-aways are:

- You can expect your best hyperparameter combination to actually underperform in the future. You chose it because it was the best on some metric, but that metric has an element of noise/luck, and the more combinations you test the larger this effect is.
- Look at the overall trends and correlations in context and try to make sense of the values you're seeing. Just because you ran a long search process doesn't mean your best output is really the best.

For more on this, see [Preventing "Overfitting" of Cross-Validation Data](https://ai.stanford.edu/~ang/papers/cv-final.pdf) by Andrew Ng.


```

---

## chapter0_fundamentals/instructions/pages/04_[0.4]_Backprop.md

```markdown
# [0.4] - Build Your Own Backpropagation Framework


> **Colab: [exercises](https://colab.research.google.com/github/callummcdougall/arena-pragmatic-interp/blob/main/chapter0_fundamentals/exercises/part4_backprop/0.4_Backprop_exercises.ipynb?t=20260303) | [solutions](https://colab.research.google.com/github/callummcdougall/arena-pragmatic-interp/blob/main/chapter0_fundamentals/exercises/part4_backprop/0.4_Backprop_solutions.ipynb?t=20260303)**

Please send any problems / bugs on the `#errata` channel in the [Slack group](https://join.slack.com/t/arena-uk/shared_invite/zt-3afdmdhye-Mdb3Sv~ss_V_mEaXEbkABA), and ask any questions on the dedicated channels for this chapter of material.

If you want to change to dark mode, you can do this by clicking the three horizontal lines in the top-right, then navigating to Settings → Theme.

Links to all other chapters: [(0) Fundamentals](https://arena-chapter0-fundamentals.streamlit.app/), [(1) Transformer Interpretability](https://arena-chapter1-transformer-interp.streamlit.app/), [(2) RL](https://arena-chapter2-rl.streamlit.app/).

<img src="https://raw.githubusercontent.com/info-arena/ARENA_img/main/misc/headers/header-04.png" width="350">


# Introduction


Today you're going to build your very own system that can run the backpropagation algorithm in essentially the same way as PyTorch does. By the end of the day, you'll be able to train a multi-layer perceptron neural network, using your own backprop system!

The main differences between the full PyTorch and our version are:

* We will focus on CPU only, as all the ideas are the same on GPU.
* We will use NumPy arrays internally instead of ATen, the C++ array type used by PyTorch. Backpropagation works independently of the array type.
* A real `torch.Tensor` has about 700 fields and methods. We will only implement a subset that are particularly instructional and/or necessary to train the MLP.

Note - for today, I'd lean a lot more towards being willing to read the solutions, and even move on from some of them if you don't fully understand them (especially in the first half of section 3). The low-level messy implementation details for today are much less important than the high-level conceptual takeaways.

For a lecture on the material today, which provides some high-level understanding before you dive into the material, watch the video below:

<iframe width="540" height="304" src="https://www.youtube.com/embed/-24lS-kk5I0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


## Content & Learning Objectives

### 1️⃣ Introduction to backprop

This takes you through what a **computational graph** is, and the basics of how gradients can be backpropagated through such a graph. You'll also implement the backwards versions of some basic functions: if we have tensors `output = func(input)`, then the backward function of `func` can calculate the grad of `input` as a function of the grad of `output`.

> ##### Learning Objectives
>
> * Understand what a computational graph is, and how it can be used to calculate gradients.
> * Start to implement backwards versions of some basic functions.

### 2️⃣ Autograd

This section goes into more detail on the backpropagation methodology. In order to find the `grad` of each tensor in a computational graph, we first have to perform a **topological sort** of the tensors in the graph, so that each time we try to calculate `tensor.grad`, we've already computed all the other gradients which are used in this calculation. We end this section by writing a `backprop` function, which works just like the `tensor.backward()` method you're already used to in PyTorch.

> ##### Learning Objectives
>
> * Perform a topological sort of a computational graph (and understand why this is important).
> * Implement a the `backprop` function, to calculate and store gradients for all tensors in a computational graph.

### 3️⃣ Training on MNIST from scratch

In this section, we build your own equivalents of `torch.nn` features like `nn.Parameter`, `nn.Module`, and `nn.Linear`. We can then use these to build our own neural network to classify MINST data.

This completes the chain which starts at basic numpy arrays, and ends with us being able to build essentially any neural network architecture we want!

> ##### Learning Objectives
>
> * Implement more forward and backward functions, including for indexing, summing, and matrix multiplication
> * Learn how to build higher-level abstractions like parameters and modules on top of individual functions and tensors
> * Complete the process of building up a neural network from scratch and training it via gradient descent.

### 4️⃣ Bonus

A few bonus exercises are suggested, for pushing your understanding of backpropagation further.


## Setup code


```python
import os
import re
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable, Iterable, Iterator

import numpy as np
from torch.utils.data import DataLoader
from tqdm import tqdm

Arr = np.ndarray
grad_tracking_enabled = True

# Make sure exercises are in the path
chapter = "chapter0_fundamentals"
section = "part4_backprop"
root_dir = next(p for p in Path.cwd().parents if (p / chapter).exists())
exercises_dir = root_dir / chapter / "exercises"
section_dir = exercises_dir / section
if str(exercises_dir) not in sys.path:
    sys.path.append(str(exercises_dir))

MAIN = __name__ == "__main__"

import part4_backprop.tests as tests
from part4_backprop.utils import get_mnist, visualize
from plotly_utils import line
```




=== NEW CHAPTER ===


# 1️⃣ Introduction to backprop



> ##### Learning Objectives
>
> * Understand what a computational graph is, and how it can be used to calculate gradients.
> * Start to implement backwards versions of some basic functions.

## Reading

* [Calculus on Computational Graphs: Backpropagation (Chris Olah)](https://colah.github.io/posts/2015-08-Backprop/)


## Computing Gradients with Backpropagation

This section will briefly review the backpropagation algorithm, but focus mainly on the concrete implementation in software.

To train a neural network, we want to know how the loss would change if we slightly adjust one of the learnable parameters.

One obvious and straightforward way to do this would be just to add a small value  to the parameter, and run the forward pass again. This is called finite differences, and the main issue is we need to run a forward pass for every single parameter that we want to adjust. This method is infeasible for large networks, but it's important to know as a way of sanity checking other methods.

A second obvious way is to write out the function for the entire network, and then symbolically take the gradient to obtain a symbolic expression for the gradient. This also works and is another thing to check against, but the expression gets quite complicated.

Suppose that you have some **computational graph**, and you want to determine the derivative of the some scalar loss L with respect to NumPy arrays a, b, and c:


<img src="https://raw.githubusercontent.com/callummcdougall/Fundamentals/main/images/abc_de_L.png" width="400">


This graph corresponds to the following Python:

```python
d = a * b
e = b + c
L = d + e
```

The goal of our system is that users can write ordinary looking Python code like this and have all the book-keeping needed to perform backpropagation happen behind the scenes. To do this, we're going to wrap each array and each function in special objects from our library that do the usual thing plus build up this graph structure that we need.


### Backward Functions

We've drawn our computation graph from left to right and the arrows pointing to the right, so that in the forward pass, boxes to the right depend on boxes to the left. In the backwards pass, the opposite is true: the gradient of boxes on the left depends on the gradient of boxes on the right.

If we want to compute the derivative of $L$ wrt all other variables (as was described in the reading), we should traverse the graph from right to left. Each time we encounter an instance of function application, we can use the chain rule from calculus to proceed one step further to the left. For example, if we have $d = a \times b$, then:

$$
\frac{dL}{da} = \frac{dL}{dd}\times \frac{dd}{da} = \frac{dL}{dd}\times b
$$

Suppose we are working from right to left, trying to calculate $\frac{dL}{da}$. If we already know the values of the variables $a$, $b$ and $d$, as well as the value of $\frac{dL}{dd}$, then we can use the following function to find $\frac{dL}{da}$:

$$
F\left(a, b, d, \frac{dL}{dd}\right) = \frac{dL}{dd}\times b
$$

and we can do something similar when trying to calculate $\frac{dL}{db}$.

In other words, we can take the **"forward function"** $(a, b) \to a \cdot b$, and for each of its parameters, we can define an associated **"backwards function"** which tells us how to compute the gradient wrt this argument using only known quantities as inputs.

Ignoring issues of unbroadcasting (which we'll cover later), we could write the backward with respect to the first argument as:

```python
def multiply_back(grad_out, out, a, b):
    '''
    Inputs:
        grad_out = dL/d(out)
        out = a * b

    Returns:
        dL/da
    '''
    return grad_out * b
```

where `grad_out` is the gradient of the loss of the function with respect to the output (i.e. $\frac{dL}{dd}$), `out` is the output of the function (i.e. $d$), and `a` and `b` are our inputs.


### Topological Ordering

When we're actually doing backprop, how do we guarantee that we'll always know the value of our backwards functions' inputs? For instance, in the example above we couldn't have computed $\frac{dL}{da}$ without first knowing $\frac{dL}{dd}$.

The answer is that we sort all our nodes using an algorithm called [topological sorting](https://en.wikipedia.org/wiki/Topological_sorting), and then do our computations in this order. After each computation, we store the gradients in our nodes for use in subsequent calculations.

When described in terms of the diagram above, topological sort can be thought of as an ordering of nodes from right to left. Crucially, this sorting has the following property: if there is a directed path in the computational graph going from node `x` to node `y`, then `x` must follow `y` in the sorting.

There are many ways of proving that a cycle-free directed graph contains a topological ordering. You can try and prove this for yourself, or click on the expander below to reveal the outline of a simple proof.


<details>
<summary>Click to reveal proof</summary>

We can prove by induction on the number of nodes $N$.
    
If $N=1$, the problem is trivial.

If $N>1$, then pick any node, and follow the arrows until you reach a node with no directed arrows going out of it. Such a node must exist, or else you would be following the arrows forever, and you'd eventually return to a node you previously visited, but this would be a cycle, which is a contradiction. Once you've found this "root node", you can put it first in your topological ordering, then remove it from the graph and apply the topological sort on the subgraph created by removing this node. By induction, your topological sorting algorithm on this smaller graph should return a valid ordering. If you append the root node to the start of this ordering, you have a topological ordering for the whole graph.
</details>


A quick note on some potentially confusing terminology. We will refer to the "end node" as the **root node**, and the "starting nodes" as **leaf nodes**. For instance, in the diagram at the top of the section, the left nodes `a`, `b` and `c` are the leaf nodes, and `L` is the root node. This might seem odd given it makes the leaf nodes come before the root nodes, but the reason is as follows: *when we're doing the backpropagation algorithm, we start at `L` and work our way back through the graph*. So, by our notation, we start at the root node and work our way out to the leaves.

Another important piece of terminology here is **parent node**. This means the same thing as it does in most other contexts - the parents of node `x` are all the nodes `y` with connections `y -> x` (so in the diagram, `L`'s parents are `d` and `e`).


<details>
<summary>Question - can you think of a reason it might be important for a node to store a list of all of its parent nodes?</summary>

During backprop, we're moving from right to left in the diagram. If a node doesn't store its parent, then there will be no way to get access to that parent node during backprop, so we can't propagate gradients to it.
</details>


The very first node in our topological sort will be $L$, the root node.


### Backpropagation

After all this setup, the backpropagation mechanism becomes pretty straightforward. We sort the nodes topologically, then we iterate over them and call each backward function exactly once in order to accumulate the gradients at each node.

It's important that the grads be accumulated instead of overwritten in a case like value $b$ which has two outgoing edges, since $\frac{dL}{db}$ will then be the sum of two terms. Since addition is commutative it doesn't matter whether we `backward()` the Mul or the Add that depend on $b$ first.

During backpropagation, for each forward function in our computational graph we need to find the partial derivative of the output with respect to each of its inputs. Each partial is then multiplied by the gradient of the loss with respect to the forward functions output (`grad_out`) to find the gradient of the loss with respect to each input. We'll handle these calculations using backward functions.


## Backward function of log

First, we'll write the backward function for `x -> out = log(x)`. This should be a function which, when fed the values `x, out, grad_out = dL/d(out)` returns the value of `dL/dx` just from this particular computational path.


<img src="https://raw.githubusercontent.com/callummcdougall/Fundamentals/main/images/x_log_out.png" width="400">


Note - it might seem strange at first why we need `x` and `out` to be inputs, `out` can be calculated directly from `x`. The answer is that sometimes it is computationally cheaper to express the derivative in terms of `out` than in terms of `x`.


<details>
<summary>Question - can you think of an example function where it would be computationally cheaper to use 'out' than to use 'x'?</summary>

The most obvious answer is the exponential function, `out = e ^ x`. Here, the gradient `d(out)/dx` is equal to `out`. We'll see this when we implement a backward version of `torch.exp` later today.
</details>


### Exercise - implement `log_back`

> ```yaml
> Difficulty: 🔴🔴⚪⚪⚪
> Importance: 🔵🔵🔵⚪⚪
> 
> You should spend up to 5-10 minutes on this exercise.
> ```


You should fill in this function below. Don't worry about division by zero or other edge cases - the goal here is just to see how the pieces of the system fit together.

*This should just be a short, one-line function.*


```python
def log_back(grad_out: Arr, out: Arr, x: Arr) -> Arr:
    """Backwards function for f(x) = log(x)

    grad_out: Gradient of some loss wrt out
    out: the output of np.log(x).
    x: the input of np.log.

    Return: gradient of the given loss wrt x
    """
    raise NotImplementedError()


tests.test_log_back(log_back)
```


<details>
<summary>Help - I'm not sure what the output of this backward function for log should be.</summary>

By the chain rule, we have:

$$
\frac{dL}{dx} = \frac{dL}{d(\text{out})} \cdot \frac{d(\text{out})}{dx} = \frac{dL}{d(\text{out})} \cdot \frac{d(\log{x})}{dx} = \frac{dL}{d(\text{out})} \cdot \frac{1}{x}
$$

---

(Note - technically, $\frac{d(\text{out})}{dx}$ is a tensor containing the derivatives of each element of $\text{out}$ with respect to each element of $x$, and we should matrix multiply when we use the chain rule. However, since $\text{out} = \log x$ is an elementwise function of $x$, our application of the chain rule here will also be an elementwise multiplication: $\frac{dL}{dx_{ij}} = \frac{dL}{d(\text{out}_{ij})} \cdot \frac{d(\text{out}_{ij})}{dx_{ij}}$. When we get to things like matrix multiplication later, we'll have to be a bit more careful!)
</details>

<details>
<summary>Help - I get <code>ImportError: numpy.core.multiarray failed to import</code></summary>

This is an annoying colab-related error which I haven't been able to find a satisfying fix for. The setup code at the top of this notebook should have installed a version of numpy which works, although you'll have to click "Restart Runtime" (from the Runtime menu) to make this work. Make sure you don't re-run the cell with `pip install`s.

If this still doesn't work, please flag it in the Slack channel errata.
</details>


<details><summary>Solution</summary>

```python
def log_back(grad_out: Arr, out: Arr, x: Arr) -> Arr:
    """Backwards function for f(x) = log(x)

    grad_out: Gradient of some loss wrt out
    out: the output of np.log(x).
    x: the input of np.log.

    Return: gradient of the given loss wrt x
    """
    return grad_out / x
```
</details>


## Backward functions of two tensors

Now we'll implement backward functions for multiple tensors. From this point onwards, we'll be working with vector-valued derivatives, i.e. terms like $\frac{\partial x}{\partial y}$ where $y$ (and possibly $x$) are tensors. To recap what this notation means - these terms are tensors where each value is the scalar derivative of one of the elements of $x$ wrt one of the elements of $y$. For example:

- If $x$ is a scalar and $y$ is a tensor with shape `(3, 4)`, then $\frac{\partial x}{\partial y}$ is a tensor with shape `(3, 4)` where the `[i, j]`-th element is $\frac{\partial x}{\partial y[i, j]}$, i.e. the derivative of $x$ wrt a particular element of $y$.
- If $x$ is a length-5 vector and $y$ is a tensor with shape `(3, 4)` then $\frac{\partial x}{\partial y}$ is a tensor with shape `(5, 3, 4)` where the `[i, j, k]`-th element is $\frac{\partial x[i]}{\partial y[j, k]}$.


### Broadcasting

Before we go through the next exercises, we'll need to address one important topic in tensor operations - **broadcasting**. We've discussed it in earlier exercises, but we're reviewing it here because it's very important for backprop. If you're comfortable with the topic, feel free to jump forwards to the section "Why do we need broadcasting for backprop?".

Both NumPy and PyTorch have the same rules for broadcasting. When two tensors are involved in an elementwise operation, NumPy/PyTorch tries to broadcast them (i.e. copying them along dimensions) so that they both have the same shape. The rules of broadcasting are as follows:

1. You can prepend dummy dimensions (of size 1) to the start of a tensor until both have the same number of dimensions
2. After this point, if some dimension has size 1 in one of the tensors, it can be repeated until it matches the size of the corresponding dimension in the other tensor

To give a simple example - suppose we have a 2D batch of data, of shape `data.shape = (N, k)` (i.e. we have `N` separate datapoints, each being a vector of length `k`). Suppose we want to add a vector `vec` of length `k` to each datapoint. This is a valid operation, because when we try and add these two objects together:

1. `vec` gets prepended with a dummy dimension so it has shape `(1, k)` and both are 2D
2. `vec` gets repeated along the first dimension so it has shape `(N, k)`, matching the shape of `data`

Then, our output has shape `(N, k)`, and elements `output[i, j] = data[i, j] + vec[j]`.

Broadcasting can be a very easy place to make mistakes, because it's easy to lose track of the exact shape of your tensors involved. As a warm-up exercise, below are some examples of broadcasting. Can you figure out which are valid, and which will raise errors?


```python
x = np.ones((3, 1, 5))
y = np.ones((1, 4, 5))

z = x + y
```

<details>
<summary>Answer</summary>

This is valid, because the 0th dimension of `y` and the 1st dimension of `x` can both be copied so that `x` and `y` have the same shape: `(3, 4, 5)`. The resulting array `z` will also have shape `(3, 4, 5)`.

This example illustrates an important point - it's not always the case that one of the tensors is strictly smaller and the other is strictly bigger. Sometimes, both tensors will get expanded. 

</details>

```python
x = np.ones((8, 2, 6))
y = np.ones((8, 2))

z = x + y
```

<details>
<summary>Answer</summary>

This is not valid. We first need to expand `y` by appending a dimension to the front, and the last two dimensions of `x` are `(2, 6)`, which won't broadcast with `y`'s `(8, 2)`.
</details>

```python
x = np.ones((8, 2, 6))
y = np.ones((2, 6))

z = x + y
```

<details>
<summary>Answer</summary>

This is valid. Once NumPy expands `y` by appending a single dimension to the front, it can then be broadcast with `x`.
</details>

```python
x = np.ones((10, 20, 30))
y = np.ones((20, 1))

z = x + y
```

<details>
<summary>Answer</summary>

This is valid. Once NumPy expands `y` by appending a single dimension to the front, it can then be broadcast with `x` (this will involve copying along the first and last dimensions).
</details>

```python
x = np.ones((4, 1))
y = np.ones((4,))

z = x + y
```

<details>
<summary>Answer</summary>

This is valid. Numpy will expand the second one to `(1, 4)` then broadcast them both to `(4, 4)`.

Although this won't raise an error, it's very possible that this isn't what the person adding these two arrays intended. A common source of mistakes is when you add 2 tensors thinking they're the same shape, but one actually has a dummy dimension you forgot about. Sadly this is something you'll just have to be vigilant for (e.g. adding assert statements where necessary, or making sure you aren't combining too many different tensor operations in a single line), because PyTorch doesn't have built-in ways of statically checking your tensor shapes.

</details>


### Why do we need broadcasting for backprop?


Often, operations like `out = f(x, y)` involve an implicit broadcasting step. For example, if `out = x + y` with `x.shape = (4,)` and `y.shape = (3, 4)`, then really our operation has 2 steps:

1. Broadcast `x` to a broadcasted version `x_b` which has the shape of `y`, i.e. copy it along the zeroth dimension to have shape `(3, 4)`,
2. Define `out = x_b + y`, which is an operation that doesn't involve broadcasting.

<img src="https://raw.githubusercontent.com/info-arena/ARENA_img/main/misc/broadcast-last-1.png" width="600">

How can we go from the gradient `dL/d(x_b)` (which might be easy to compute given it involves no broadcasting) to the gradient of `dL/dx`? The answer is that **we take `dL/d(x_b)` and sum it over the dimensions along which `x` was broadcasted to get `dL/dx`.**

For the mathematically inclined this can be proved fairly easily (we provide a sketch of the proof below). But let's focus on the intuition here. When we copy `x` along axes to create `x_b`, we're essentially creating multiple pathways for each element of `x` to affect the final loss: one path for each time the element of `x` was copied. So when we change some element of `x`, this causes a first-order change in the loss from all of these different pathways, and we have to sum these changes to get the total first-order change (i.e. the derivative). For example:

<img src="https://raw.githubusercontent.com/info-arena/ARENA_img/main/misc/broadcast-last-2.png" width="540">


> ##### Summary
>
> If we know $\frac{\partial L}{\partial (\mathbf{out})}$, and want to know $\frac{\partial L}{\partial \mathbf{x}}$ (where $x$ was broadcasted to produce $\text{out}$) then there are two steps:
>
> 1. Compute $\frac{\partial L}{\partial \mathbf{x_b}}$ in the standard way, i.e. using one of your backward functions (assuming no broadcasting happened).
> 2. ***Unbroadcast*** $\frac{\partial L}{\partial \mathbf{x_b}}$, by summing it over the dimensions along which $\mathbf{x}$ was broadcasted.


<details>
<summary>Mathematical derivation (sketch)</summary>

We start with:

$$
\frac{\partial L}{\partial \mathbf{x}} = \sum_{i_1, i_2, ...} \frac{\partial L}{\partial x_b[i_1, i_2, ...]} \cdot \frac{\partial x_b[i_1, i_2, ...]}{\partial \mathbf{x}}
$$

using the chain rule. Next, we can use the fact that $\frac{\partial x_b[i_1, i_2, ...]}{\partial x[j_1, j_2, ...]}$ equals 0 everywhere except the indices where $x$ was broadcasted to produce $x_b$, where it equals 1. Therefore, this sum over indices $i_1, i_2, ...$ is equivalent to just summing $\frac{\partial L}{\partial x_b[i_1, i_2, ...]}$ over the repeated elements of $x$.

</details>


We used the term "unbroadcast" because the way that our tensor's shape changes will be the reverse of how it changed during broadcasting. If `x` was broadcasted from `(4,) -> (3, 4)`, then unbroadcasting will have to take a tensor of shape `(3, 4)` and sum over it to return a tensor of shape `(4,)`. Similarly, if `x` was broadcasted from `(1, 4) -> (3, 4)`, then we need to sum over the zeroth dimension, but leave it as a 2D tensor with a leading dummy dimension of size 1.


### Exercise - implement `unbroadcast`

> ```yaml
> Difficulty: 🔴🔴🔴⚪⚪
> Importance: 🔵🔵🔵⚪⚪
> 
> You should spend up to 10-25 minutes on this exercise.
> This function can be quite fiddly - if you're stuck, read and understand the solution code instead.
> ```


The `unbroadcast` function below should take any value like $\frac{\partial L}{\partial x_b}$ and return $\frac{\partial L}{\partial x}$ (where the arguments `original` and `broadcasted` represent $x$ and $x_b$ respectively). In the same way that broadcasting `original` to the shape of `broadcasted` can be described as a 2-step process:

1. Extend dummy dimensions (size 1) of `original` to match the last dimensions of `broadcasted`,
2. Prepend dimensions to `original` until it has the same ndims as `broadcasted`,

the unbroadcasting process is the same process in reverse:

1. Sum over prepended dimensions of `broadcasted` until it has the same ndims as `original`,
2. Now they have the same ndims, sum over dimensions of `broadcasted` where `original` had size 1.

For example, if `original.shape = (3, 1)` and `broadcasted.shape = (1, 2, 3, 4)` then the broadcasting steps look like `(3, 1) -> (3, 4) -> (1, 2, 3, 4)` (copying along those dimensions at each step) and the unbroadcasting steps look like `(1, 2, 3, 4) -> (3, 4) -> (3, 1)` (summing over those dimensions at each step).


```python
def unbroadcast(broadcasted: Arr, original: Arr) -> Arr:
    """
    Sum 'broadcasted' until it has the shape of 'original'.

    broadcasted: An array that was formerly of the same shape of 'original' and was expanded by
        broadcasting rules.
    """
    # YOUR CODE HERE: sum over `broadcasted` until it has the shape of `original`

    assert broadcasted.shape == original.shape
    return broadcasted


tests.test_unbroadcast(unbroadcast)
```


<details><summary>Solution</summary>

```python
def unbroadcast(broadcasted: Arr, original: Arr) -> Arr:
    """
    Sum 'broadcasted' until it has the shape of 'original'.

    broadcasted: An array that was formerly of the same shape of 'original' and was expanded by
        broadcasting rules.
    """
    # Step 1: sum and remove prepended dims, so both arrays have same number of dims
    n_dims_to_sum = len(broadcasted.shape) - len(original.shape)
    broadcasted = broadcasted.sum(axis=tuple(range(n_dims_to_sum)))

    # Step 2: sum over dims which were originally 1 (but don't remove them)
    dims_to_sum = tuple([i for i, (o, b) in enumerate(zip(original.shape, broadcasted.shape)) if o == 1 and b > 1])
    broadcasted = broadcasted.sum(axis=dims_to_sum, keepdims=True)

    assert broadcasted.shape == original.shape
    return broadcasted
```
</details>


### Backward Function for Elementwise Multiply

Functions that are differentiable with respect to more than one input tensor are straightforward given that we already know how to handle broadcasting.

- We're going to have two backwards functions, one for each input argument.
- If the input arguments were broadcasted together to create a larger output, the incoming `grad_out` will be of the larger common broadcasted shape and we need to make use of `unbroadcast` from earlier to match the shape to the appropriate input argument.
- We'll want our backward function to work when one of the inputs is a float (as opposed to a tensor). We won't need to calculate the grad_in with respect to floats, so we only need to consider when y is a float for `multiply_back0` and when x is a float for `multiply_back1`.


### Exercise - implement both `multiply_back` functions

> ```yaml
> Difficulty: 🔴🔴🔴⚪⚪
> Importance: 🔵🔵⚪⚪⚪
> 
> You should spend up to 10-15 minutes on these exercises.
> ```

Below, you should implement both `multiply_back0` and `multiply_back1`.

You might be wondering why we need two different functions, rather than just having a single function to serve both purposes. This will become more important later on, once we deal with functions with more than one argument, which is not symmetric in its arguments. For instance, the derivative of $x / y$ wrt $x$ is not the same as the expression you get after differentiating this wrt $y$ then swapping the labels around.

The first part of each function has been provided for you (this makes sure that both inputs are arrays, since we want to support multiplication by floats or scalars).


```python
def multiply_back0(grad_out: Arr, out: Arr, x: Arr, y: Arr | float) -> Arr:
    """Backwards function for x * y wrt argument 0 aka x."""
    if not isinstance(y, Arr):
        y = np.array(y)

    raise NotImplementedError()


def multiply_back1(grad_out: Arr, out: Arr, x: Arr | float, y: Arr) -> Arr:
    """Backwards function for x * y wrt argument 1 aka y."""
    if not isinstance(x, Arr):
        x = np.array(x)

    raise NotImplementedError()


tests.test_multiply_back(multiply_back0, multiply_back1)
tests.test_multiply_back_float(multiply_back0, multiply_back1)
```


<details>
<summary>Hint</summary>

Using the chain rule for scalar functions, we can find that:

$$
\frac{\partial L}{\partial x} = \frac{\partial L}{\partial (xy)} \cdot \frac{\partial (xy)}{\partial x} = \frac{\partial L}{\partial (xy)} \cdot y
$$

An equivalent result\* holds for vector-valued inputs:

$$
\frac{\partial L}{\partial \mathbf{x}_b} = \frac{\partial L}{\partial (\mathbf{x}_b \cdot \mathbf{y}_b)} \cdot \mathbf{y}_b
$$

where $\cdot$ is the elementwise multiplication operator, and $\mathbf{x}_b, \mathbf{y}_b$ are the broadcasted versions of the input tensors. This allows us to compute $\frac{\partial L}{\partial \mathbf{x}_b}$ based on the inputs to our `multiply_back0` function. Can you use `unbroadcast` to finish the calculation?

\*You can derive this result for yourself using the chain rule. Note that application of the chain rule here would require you to sum over the elements of the intermediate tensor $\mathbf{x}_b \cdot \mathbf{y}_b$, but we're working with elementwise operations so $\partial (\mathbf{x}_b \cdot \mathbf{y}_b)[i_1, i_2, ...] / \partial \mathbf{x}_b$ will have all elements zero except for one and the sum falls out, leaving us with the result above.

</details>

<details>
<summary>Solution (and explanation)</summary>

Based on the discussion in hint 1, we can conclude that the value $\partial L / \partial \mathbf{x}_b$ is equal to `y_b * grad_out`. Note that this is just equivalent to `y * grad_out` because `y` will be broadcasted to the shape of `y_b` when we multiply it with `grad_out` (since we know `grad_out` has the same shape as the broadcasted `x * y` tensor).

Now, we need to go from this broadcasted derivative to the shape of `x`, and we do this by applying `unbroadcast`, summing `y * grad_out` over dimensions so that it's the same shape as `x` - in other words, we return `unbroadcast(y * grad_out, x)`.

The output of `multiply_back1` is the same as `multiply_back0`, except the roles of `x` and `y` are reversed.

```python
def multiply_back0(grad_out: Arr, out: Arr, x: Arr, y: Arr | float) -> Arr:
    """Backwards function for x * y wrt argument 0 aka x."""
    if not isinstance(y, Arr):
        y = np.array(y)

    return unbroadcast(y * grad_out, x)


def multiply_back1(grad_out: Arr, out: Arr, x: Arr | float, y: Arr) -> Arr:
    """Backwards function for x * y wrt argument 1 aka y."""
    if not isinstance(x, Arr):
        x = np.array(x)

    return unbroadcast(x * grad_out, y)
```

<!-- Derivation: first we compute the gradient of the broadcasted tensor, using the chain rule:

$$
\frac{\partial L}{\partial x_b[i_1, i_2, ...]} = \frac{\partial L}{\partial (x_b \cdot y_b)[i_1, i_2, ...]} \cdot \frac{\partial (x_b \cdot y_b)[i_1, i_2, ...]}{\partial x_b[i_1, i_2, ...]}
$$

where we've avoided the sum over indices of $x_b \cdot y_b$ because this is an elementwise operation, and so those gradients must be zero everywhere except where all $i_k = j_k$. We can further write this as:

$$
\frac{\partial L}{\partial x_b[i_1, i_2, ...]} = \text{grad\_out}[i_1, i_2, ...] \cdot y[i_1, i_2, ...]
$$

which gives us the result for broadcasted tensors! Note that although this tensor is `grad_out * y_b`, we can compute it as `grad_out * y` because we know that `y` is broadcastable to the shape of `grad_out` (since this is also the same as the shape of `out`).

Once we have this result `grad_out * y`, we just use `unbroadcast` to sum over the dimensions `x` was broadcasted along.  -->

</details>


Now we'll use our backward functions to do backpropagation manually, for the following computational graph:

<img src="https://raw.githubusercontent.com/callummcdougall/Fundamentals/main/images/abcdefg.png" width=550>


### Exercise - implement `forward_and_back`

> ```yaml
> Difficulty: 🔴🔴🔴⚪⚪
> Importance: 🔵🔵🔵🔵⚪
> 
> You should spend up to 15-20 minutes on these exercises.
> This function is very useful for getting a sense for what backprop looks like in practice.
> ```

Below, you should implement the `forward_and_back` function. This is an opportunity for you to practice using the backward functions you've written so far, and should hopefully give you a better sense of how the full backprop function will eventually work.

Note - you might be wondering what `grad_out` should be the first time you call a backward function. We've so far assumed that the final node `L` in the computational graph is a scalar, and all gradients (i.e. the `grad_out` input to our backward functions and the output of our backward functions) are gradients of `L`. In this case, it would make sense to set `grad_out = [1]` for the first backward function call, since we're computing $\frac{\partial L}{\partial L} = 1$. But what about cases like the one above, when our final node `g` might not be a scalar?

The answer is that we effectively add a final scalar node into our graph, defined as `L = (g * v).sum()` for some tensor `v` of the same shape as `g`. This is called the **directional derivative**. We then compute all tensor gradients using `L` as our final node. For example, this means that in our first gradient calculation (where `g` is the output and `f` is the input) we'll use `grad_out = dL/dg = v`. You don't really need to worry about this, because most of the time (including in the exercise below) we'll just be using the default behaviour where `v` is a tensor of 1s - this is equivalent to `L = g.sum()`.


```python
def forward_and_back(a: Arr, b: Arr, c: Arr) -> tuple[Arr, Arr, Arr]:
    """
    Calculates the output of the computational graph above (g), then backpropogates the gradients
    and returns dg/da, dg/db, and dg/dc.
    """
    d = a * b
    e = np.log(c)
    f = d * e
    g = np.log(f)
    final_grad_out = np.ones_like(g)

    # YOUR CODE HERE - use your backward functions to compute the gradients of g wrt a, b, and c

    return (dg_da, dg_db, dg_dc)


tests.test_forward_and_back(forward_and_back)
```


<details><summary>Solution</summary>

```python
def forward_and_back(a: Arr, b: Arr, c: Arr) -> tuple[Arr, Arr, Arr]:
    """
    Calculates the output of the computational graph above (g), then backpropogates the gradients
    and returns dg/da, dg/db, and dg/dc.
    """
    d = a * b
    e = np.log(c)
    f = d * e
    g = np.log(f)
    final_grad_out = np.ones_like(g)

    dg_df = log_back(grad_out=final_grad_out, out=g, x=f)
    dg_dd = multiply_back0(dg_df, f, d, e)
    dg_de = multiply_back1(dg_df, f, d, e)
    dg_da = multiply_back0(dg_dd, d, a, b)
    dg_db = multiply_back1(dg_dd, d, a, b)
    dg_dc = log_back(dg_de, e, c)

    return (dg_da, dg_db, dg_dc)
```
</details>


In the next section, you'll build up to full automation of this backpropagation process, in a way that's similar to PyTorch's `autograd`.




=== NEW CHAPTER ===


# 2️⃣ Autograd



> ##### Learning Objectives
>
> * Perform a topological sort of a computational graph (and understand why this is important).
> * Implement a the `backprop` function, to calculate and store gradients for all tensors in a computational graph.

Now, rather than figuring out which backward functions to call, in what order, and what their inputs should be, we'll write code that takes care of that for us. We'll implement this with a few major components:

- `Tensor`, which is a wrapper around numpy arrays which is equivalent to PyTorch's `Tensor` class
- `Recipe`, which tracks the extra information needed to run backpropagation (mainly how this tensor was created from other tensors)
- `wrap_forward_fn`, which takes a numpy function mapping arrays to arrays (e.g. `np.log`) and returns a new function that maps tensors to tensors (while also creating the recipe for the new tensor)


## Wrapping Arrays (Tensor)

We're going to wrap each array with a wrapper object from our library which we'll call `Tensor` because it's going to behave similarly to a `torch.Tensor`.

Each Tensor that is created by one of our forward functions will have a `Recipe`, which tracks the extra information need to run backpropagation.

`wrap_forward_fn` will take a forward function and return a new forward function that does the same thing while recording the info we need to do backprop in the `Recipe`.


## Recipe

Let's start by taking a look at `Recipe`.

`@dataclass` is a handy class decorator that sets up an `__init__` function for the class that takes the provided attributes as arguments and sets them as you'd expect.

The class `Recipe` is designed to track the forward functions in our computational graph, so that gradients can be calculated during backprop. Each tensor created by a forward function has its own `Recipe`. We're naming it this because it is a set of instructions that tell us which ingredients went into making our tensor: what the function was, and what tensors were used as input to the function to produce this one as output.


```python
@dataclass(frozen=True)
class Recipe:
    """Extra information necessary to run backpropagation. You don't need to modify this."""

    func: Callable
    "The 'inner' NumPy function that does the actual forward computation."
    "Note, we call it 'inner' to distinguish it from the wrapper we'll create for it later on."

    args: tuple
    "The input arguments passed to func."
    "For instance, if func=np.sum then args would be a length-1 tuple with the tensor to be summed."

    kwargs: dict[str, Any]
    "Keyword arguments passed to func."
    "For instance, if func was np.sum then kwargs might contain 'dim' and 'keepdims'."

    parents: dict[int, "Tensor"]
    "Map from positional argument index to the Tensor at that position."
    "For passing gradients back along the computational graph."
```


Note that `args` just stores the values of the underlying arrays, but `parents` stores the actual tensors. This is because they serve two different purposes: `args` is required for computing the value of gradients during backpropagation, and `parents` is required to infer the structure of the computational graph (i.e. which tensors were used to produce which other tensors).

Here are some examples, to build intuition for what the four fields of `Recipe` are, and why we need all four of them to fully describe a tensor in our graph and how it was created. Make sure you understand each of these examples before moving on, because it'll really help you progress quickly through the following exercises.

<img src="https://raw.githubusercontent.com/info-arena/ARENA_img/main/misc/recipe-v2.png" width="800">


## Registering backwards functions

The `Recipe` takes care of tracking the forward functions in our computational graph, but we still need a way to find the backward function corresponding to a given forward function when we do backprop (or possibly the set of backward functions, if the forward function takes more than one argument).


### Exercise - implement `BackwardFuncLookup`

> ```yaml
> Difficulty: 🔴🔴⚪⚪⚪
> Importance: 🔵🔵🔵⚪⚪
> 
> You should spend up to 10-15 minutes on these exercises.
> These exercises should be very short, once you understand what is being asked.
> ```

We will define a class `BackwardFuncLookup` in order to find the backward function for a given forward function. The implementation details are left up to you - all that matters is that you pass the test code in the cell below. Reading this test code should explain how the `BackwardFuncLookup` class needs to be used - for any given forward function e.g. `np.log`, we need to be able to add a set of backward functions for each of its positional arguments.


```python
class BackwardFuncLookup:
    def __init__(self) -> None:
        raise NotImplementedError()

    def add_back_func(self, forward_fn: Callable, arg_position: int, back_fn: Callable) -> None:
        raise NotImplementedError()

    def get_back_func(self, forward_fn: Callable, arg_position: int) -> Callable:
        raise NotImplementedError()


BACK_FUNCS = BackwardFuncLookup()

BACK_FUNCS.add_back_func(np.log, 0, log_back)
BACK_FUNCS.add_back_func(np.multiply, 0, multiply_back0)
BACK_FUNCS.add_back_func(np.multiply, 1, multiply_back1)

assert BACK_FUNCS.get_back_func(np.log, 0) == log_back
assert BACK_FUNCS.get_back_func(np.multiply, 0) == multiply_back0
assert BACK_FUNCS.get_back_func(np.multiply, 1) == multiply_back1

print("Tests passed - BackwardFuncLookup class is working as expected!")
```


<details>
<summary>Help - I'm stuck on this implementation</summary>

You can define a dict like `self.back_funcs` in the `__init__` method. When you add / retrieve a function, you can use the tuple `(forward_fn, arg_position)` as a key, and the backward function as the value.

</details>


<details><summary>Solution</summary>

```python
class BackwardFuncLookup:
    def __init__(self) -> None:
        self.back_funcs = {}  # each entry is a tuple of (forward_fn, arg_position) -> back_fn

    def add_back_func(self, forward_fn: Callable, arg_position: int, back_fn: Callable) -> None:
        self.back_funcs[(forward_fn, arg_position)] = back_fn

    def get_back_func(self, forward_fn: Callable, arg_position: int) -> Callable:
        return self.back_funcs[(forward_fn, arg_position)]
```
</details>


## Tensors

Our Tensor object has these fields:

- An `array` field of type `np.ndarray`. These are the actual tensor values.
- A `requires_grad` field of type `bool`. This determines whether we need to compute gradients for this tensor (note this doesn't necessarily mean we need to store them, see below).
- A `grad` field of the same size and type as the value. This is where gradients are stored.
- A `recipe` field, as we've already seen. A tensor has a recipe if and only if it was created by some operation on other tensors.


### `requires_grad` and `is_leaf`

The meaning of `requires_grad` is that when doing operations using this tensor, the recipe will be stored and it and any descendents will be included in the computational graph. Note that `requires_grad` does not necessarily mean that we will save the accumulated gradients to this tensor's `.grad` parameter when doing backprop - for example we require gradients to propagate through the hidden activations of a neural network to get back to grads for our model weights, but we don't need to actually store the gradients of the hidden activations.

We use `is_leaf` to differentiate between these cases (see the method `Tensor.is_leaf` defined below) - a leaf tensor is one that represents the end of a backprop path, either because it doesn't require gradients or it has no nodes further back in the computational graph which require gradients. So our backprop algorithm will always terminate at a leaf node, then store that leaf node's gradient as `.grad` only if `requires_grad` is true.

<img src="https://raw.githubusercontent.com/info-arena/ARENA_img/main/misc/is_leaf.png" width="900">

You can investigate this by running the following code:

```python
layer = torch.nn.Linear(3, 4)
input = torch.ones(3)
output = layer(input)

print(layer.weight.is_leaf)       # -> True
print(layer.weight.requires_grad) # -> True

print(output.is_leaf)             # -> False
print(output.requires_grad)       # -> True

print(input.is_leaf)              # -> True
print(input.requires_grad)        # -> False
```

When creating tensors, we can set `requires_grad` explicitly (e.g. it's false by default for most tensors, but is true by default if that tensor is wrapped in `torch.nn.Parameter` - we'll create our own version of this later). When creating a tensor from another tensor or tensors, `requires_grad` is true if and only if all of the following 3 conditions hold:

1. Global grad tracking is enabled. In this notebook we've represented this with the global variable `grad_tracking_enabled`, but in PyTorch this is done with `torch.set_grad_enabled(False)`. This is useful because when you're looking at a model in inference mode, gradient tracking can waste memory and it's useful to disable it (we'll do this a lot next week, when we study transformer interpretability).
2. At least one of the input tensors requires grad (since this is equivalent to "there are other tensors further upstream which we need to get gradients for").
3. The function is differentiable (if not, obviously we can't compute gradients).


Now, we're giving you the full `Tensor` class. Most of these methods are currently undefined, and you'll go on to define them in later exercises (so you won't need to write any code this class). For now, just pay attention to the docstring & `__init__` methods.


```python
Arr = np.ndarray


class Tensor:
    """
    A drop-in replacement for torch.Tensor supporting a subset of features.
    """

    array: Arr
    "The underlying array. Can be shared between multiple Tensors."
    requires_grad: bool
    "If True, calling functions or methods on this tensor will track relevant data for backprop."
    grad: "Tensor | None"
    "Backpropagation will accumulate gradients into this field."
    recipe: "Recipe | None"
    "Extra information necessary to run backpropagation."

    def __init__(self, array: Arr | list, requires_grad=False):
        self.array = array if isinstance(array, Arr) else np.array(array)
        if self.array.dtype == np.float64:
            self.array = self.array.astype(np.float32)
        self.requires_grad = requires_grad
        self.grad = None
        self.recipe = None
        "If not None, this tensor's array was created as recipe.func(*recipe.args, **recipe.kwargs)."

    def __neg__(self) -> "Tensor":
        return negative(self)

    def __add__(self, other) -> "Tensor":
        return add(self, other)

    def __radd__(self, other) -> "Tensor":
        return add(other, self)

    def __sub__(self, other) -> "Tensor":
        return subtract(self, other)

    def __rsub__(self, other) -> "Tensor":
        return subtract(other, self)

    def __mul__(self, other) -> "Tensor":
        return multiply(self, other)

    def __rmul__(self, other):
        return multiply(other, self)

    def __truediv__(self, other):
        return true_divide(self, other)

    def __rtruediv__(self, other):
        return true_divide(other, self)

    def __matmul__(self, other):
        return matmul(self, other)

    def __rmatmul__(self, other):
        return matmul(other, self)

    def __eq__(self, other):
        return eq(self, other)

    def __repr__(self) -> str:
        return f"Tensor({repr(self.array)}, requires_grad={self.requires_grad})"

    def __len__(self) -> int:
        if self.array.ndim == 0:
            raise TypeError
        return self.array.shape[0]

    def __hash__(self) -> int:
        return id(self)

    def __getitem__(self, index) -> "Tensor":
        return getitem(self, index)

    def add_(self, other: "Tensor", alpha: float = 1.0) -> "Tensor":
        add_(self, other, alpha=alpha)
        return self

    def sub_(self, other: "Tensor", alpha: float = 1.0) -> "Tensor":
        sub_(self, other, alpha=alpha)
        return self

    def __iadd__(self, other: "Tensor") -> "Tensor":
        self.add_(other)
        return self

    def __isub__(self, other: "Tensor") -> "Tensor":
        self.sub_(other)
        return self

    @property
    def T(self) -> "Tensor":
        return permute(self, axes=(-1, -2))

    def item(self):
        return self.array.item()

    def sum(self, dim=None, keepdim=False) -> "Tensor":
        return sum(self, dim=dim, keepdim=keepdim)

    def log(self) -> "Tensor":
        return log(self)

    def exp(self) -> "Tensor":
        return exp(self)

    def reshape(self, new_shape) -> "Tensor":
        return reshape(self, new_shape)

    def permute(self, dims) -> "Tensor":
        return permute(self, dims)

    def maximum(self, other) -> "Tensor":
        return maximum(self, other)

    def relu(self) -> "Tensor":
        return relu(self)

    def argmax(self, dim=None, keepdim=False) -> "Tensor":
        return argmax(self, dim=dim, keepdim=keepdim)

    def uniform_(self, low: float, high: float) -> "Tensor":
        self.array[:] = np.random.uniform(low, high, self.array.shape)
        return self

    def backward(self, end_grad: "Arr | Tensor | None" = None) -> None:
        if isinstance(end_grad, Arr):
            end_grad = Tensor(end_grad)
        return backprop(self, end_grad)

    def size(self, dim: int | None = None):
        if dim is None:
            return self.shape
        return self.shape[dim]

    @property
    def shape(self):
        return self.array.shape

    @property
    def ndim(self):
        return self.array.ndim

    @property
    def is_leaf(self):
        """Same as https://pytorch.org/docs/stable/generated/torch.Tensor.is_leaf.html"""
        if self.requires_grad and self.recipe and self.recipe.parents:
            return False
        return True

    def __bool__(self):
        if np.array(self.shape).prod() != 1:
            raise RuntimeError("bool value of Tensor with more than one value is ambiguous")
        return bool(self.item())


def empty(*shape: int) -> Tensor:
    """Like torch.empty."""
    return Tensor(np.empty(shape))


def zeros(*shape: int) -> Tensor:
    """Like torch.zeros."""
    return Tensor(np.zeros(shape))


def arange(start: int, end: int, step=1) -> Tensor:
    """Like torch.arange(start, end)."""
    return Tensor(np.arange(start, end, step=step))


def tensor(array: Arr, requires_grad=False) -> Tensor:
    """Like torch.tensor."""
    return Tensor(array, requires_grad=requires_grad)
```


## Forward Pass: Building the Computational Graph

Let's start with a simple case: our `log` function. `log_forward` is a wrapper, which should implement the functionality of `np.log` but work with tensors rather than arrays.


### Exercise - implement `log_forward`

> ```yaml
> Difficulty: 🔴🔴🔴⚪⚪
> Importance: 🔵🔵🔵⚪⚪
> 
> You should spend up to 15-20 minutes on this exercise.
> ```

Your `log` function should be a wrapper around `np.log`, which takes and returns a `Tensor` object rather than numpy arrays. You can refer to the first of the five diagrams at the start of the "Recipe" section if you're stuck.

Some more hints / tips:

- As a reminder, `requires_grad` is true if both global gradient tracking is enabled (i.e. `grad_tracking_enabled` is true) and at least one of the inputs has `requires_grad` true.
- You should also set the recipe for the new tensor, if `requires_grad` is true (if not then you can just set the recipe to None).

Later we'll write code to wrap numpy functions in a generic and reusable way, but for now we just want to get this working for `np.log`.


```python
def log_forward(x: Tensor) -> Tensor:
    """Performs np.log on a Tensor object."""
    raise NotImplementedError()


log = log_forward
tests.test_log(Tensor, log_forward)
tests.test_log_no_grad(Tensor, log_forward)
a = Tensor([1], requires_grad=True)
grad_tracking_enabled = False
b = log_forward(a)
grad_tracking_enabled = True
assert not b.requires_grad, "should not require grad if grad tracking globally disabled"
assert b.recipe is None, "should not create recipe if grad tracking globally disabled"
```


<details><summary>Solution</summary>

```python
def log_forward(x: Tensor) -> Tensor:
    """Performs np.log on a Tensor object."""
    # Get the function output (as a numpy array)
    array = np.log(x.array)

    # Find whether the tensor requires grad
    requires_grad = grad_tracking_enabled and x.requires_grad

    # Create the tensor
    out = Tensor(array, requires_grad)

    # Set the recipe (if we need it)
    if requires_grad:
        out.recipe = Recipe(func=np.log, args=(x.array,), kwargs={}, parents={0: x})

    return out
```
</details>


Now let's do the same for multiply, to see how to handle functions with multiple arguments.


### Exercise - implement `multiply_forward`

> ```yaml
> Difficulty: 🔴🔴🔴🔴⚪
> Importance: 🔵🔵🔵⚪⚪
> 
> You should spend up to 15-20 minutes on this exercise.
> ```

There are a few differences between this and log:

- The actual function to be called is different
- We need more than one argument in `args` and `parents`, when defining `Recipe`
- `requires_grad` should be true if `grad_tracking_enabled=True`, and ANY of the input tensors require grad
- One of the inputs may be an int, so you'll need to deal with this case before calculating `out`

If you're confused, you can scroll up to the diagram at the top of the page (which tells you how to construct the recipe for functions like multiply or add when they are both arrays, or when one is an array and the other is a scalar).


```python
def multiply_forward(a: Tensor | int, b: Tensor | int) -> Tensor:
    """Performs np.multiply on a Tensor object."""
    assert isinstance(a, Tensor) or isinstance(b, Tensor)

    # Get all function arguments as non-tensors (i.e. either ints or arrays)
    arg_a = a.array if isinstance(a, Tensor) else a
    arg_b = b.array if isinstance(b, Tensor) else b

    raise NotImplementedError()


multiply = multiply_forward
tests.test_multiply(Tensor, multiply_forward)
tests.test_multiply_no_grad(Tensor, multiply_forward)
tests.test_multiply_float(Tensor, multiply_forward)
a = Tensor([2], requires_grad=True)
b = Tensor([3], requires_grad=True)
grad_tracking_enabled = False
b = multiply_forward(a, b)
grad_tracking_enabled = True
assert not b.requires_grad, "should not require grad if grad tracking globally disabled"
assert b.recipe is None, "should not create recipe if grad tracking globally disabled"
```


<details>
<summary>Help - I get <code>AttributeError: 'int' object has no attribute 'array'</code>.</summary>

Remember that your multiply function should also accept integers. You need to separately deal with the cases where `a` and `b` are integers or Tensors.
</details>

<details>
<summary>Help - I get <code>AssertionError: assert len(c.recipe.parents) == 1 and c.recipe.parents[0] is a</code> in the "test_multiply_float" test.</summary>

This is probably because you've stored the inputs to `multiply` as integers when one of the is an integer. Remember, `parents` should just be a list of the **Tensors** that were inputs to `multiply`, so you shouldn't add ints.
</details>


<details><summary>Solution</summary>

```python
def multiply_forward(a: Tensor | int, b: Tensor | int) -> Tensor:
    """Performs np.multiply on a Tensor object."""
    assert isinstance(a, Tensor) or isinstance(b, Tensor)

    # Get all function arguments as non-tensors (i.e. either ints or arrays)
    arg_a = a.array if isinstance(a, Tensor) else a
    arg_b = b.array if isinstance(b, Tensor) else b

    # Calculate the output (which is a numpy array)
    out_arr = arg_a * arg_b
    assert isinstance(out_arr, np.ndarray)

    # Find whether the tensor requires grad (need to check if ANY of the inputs do)
    requires_grad = grad_tracking_enabled and any([isinstance(x, Tensor) and x.requires_grad for x in (a, b)])

    # Create the output tensor from the underlying data and the requires_grad flag
    out = Tensor(out_arr, requires_grad)

    # If requires_grad, then create a recipe
    if requires_grad:
        parents = {idx: arr for idx, arr in enumerate([a, b]) if isinstance(arr, Tensor)}
        out.recipe = Recipe(np.multiply, (arg_a, arg_b), {}, parents)

    return out
```
</details>


## Forward Pass - Generic Version

All our forward functions are going to look extremely similar to `log_forward` and `multiply_forward`.
Implement the higher order function `wrap_forward_fn` that takes a `Arr -> Arr` function and returns a `Tensor -> Tensor` function. In other words, `wrap_forward_fn(np.multiply)` should evaluate to a callable that does the same thing as your `multiply_forward` (and same for `np.log`).


### Exercise - implement `wrap_forward_fn`

> ```yaml
> Difficulty: 🔴🔴🔴🔴⚪
> Importance: 🔵🔵🔵🔵⚪
> 
> You should spend up to 20-25 minutes on this exercise.
> This exercise is probably the 2nd most conceptually important today, after the backprop implementation at the end of the section.
> ```

If you're stuck, you can start with the same structure as the wrapped multiply function above (i.e. just copy and paste the code from solutions and use this as a stand in for `tensor_func` below, then modify it).


```python
def wrap_forward_fn(numpy_func: Callable, is_differentiable=True) -> Callable:
    """
    Args:
        numpy_func:
            takes any number of positional arguments, some of which may be NumPy arrays, and any
            number of keyword arguments which we aren't allowing to be NumPy arrays at present. It
            returns a single NumPy array.

        is_differentiable:
            if True, numpy_func is differentiable with respect to some input argument, so we may
            need to track information in a Recipe. If False, we definitely don't need to track
            information.

    Returns:
        tensor_func
            It has the same signature as numpy_func, except it operates on Tensors instead of Arr.
    """

    def tensor_func(*args: Any, **kwargs: Any) -> Tensor:
        # Get all function arguments as non-tensors (i.e. either ints or arrays)
        arg_arrays = tuple([(a.array if isinstance(a, Tensor) else a) for a in args])

        # YOUR CODE HERE - create output array & make it a tensor with requires_grad (& recipe)

        return out

    return tensor_func


def _sum(x: Arr, dim=None, keepdim=False) -> Arr:
    # need to be careful with sum, because kwargs have different names in torch and numpy
    return np.sum(x, axis=dim, keepdims=keepdim)


log = wrap_forward_fn(np.log)
multiply = wrap_forward_fn(np.multiply)
eq = wrap_forward_fn(np.equal, is_differentiable=False)
sum = wrap_forward_fn(_sum)

tests.test_log(Tensor, log)
tests.test_log_no_grad(Tensor, log)
tests.test_multiply(Tensor, multiply)
tests.test_multiply_no_grad(Tensor, multiply)
tests.test_multiply_float(Tensor, multiply)
tests.test_eq(Tensor, eq)
tests.test_sum(Tensor)
```


<details>
<summary>Help - I'm getting <code>NameError: name 'getitem' is not defined</code>.</summary>

This is probably because you're calling `numpy_func` on the args themselves. Recall that `args` will be a list of `Tensor` objects, and that you should call `numpy_func` on the underlying arrays.
</details>

<details>
<summary>Help - I'm getting an AssertionError on <code>assert c.requires_grad == True</code> (or something similar).</summary>

This is probably because you're not defining `requires_grad` correctly. Remember that the output of a forward function should have `requires_grad = True` if and only if all of the following hold:

* Grad tracking is enabled
* The function is differentiable
* **Any** of the inputs are tensors with `requires_grad = True`
</details>

<details>
<summary>Help - my function passes all tests up to <code>test_sum</code>, but then fails here.</summary>

`test_sum`, unlike the previous tests, wraps a function that uses keyword arguments. So if you're failing here, it's probably because you didn't use `kwargs` correctly.

`kwargs` should be used in two ways: once when actually calling the `numpy_func`, and once when defining the `Recipe` object for the output tensor.
</details>


<details><summary>Solution</summary>

```python
def wrap_forward_fn(numpy_func: Callable, is_differentiable=True) -> Callable:
    """
    Args:
        numpy_func:
            takes any number of positional arguments, some of which may be NumPy arrays, and any
            number of keyword arguments which we aren't allowing to be NumPy arrays at present. It
            returns a single NumPy array.

        is_differentiable:
            if True, numpy_func is differentiable with respect to some input argument, so we may
            need to track information in a Recipe. If False, we definitely don't need to track
            information.

    Returns:
        tensor_func
            It has the same signature as numpy_func, except it operates on Tensors instead of Arr.
    """

    def tensor_func(*args: Any, **kwargs: Any) -> Tensor:
        # Get all function arguments as non-tensors (i.e. either ints or arrays)
        arg_arrays = tuple([(a.array if isinstance(a, Tensor) else a) for a in args])

        # Calculate the output (which is a numpy array)
        out_arr = numpy_func(*arg_arrays, **kwargs)

        # Find whether the tensor requires grad (need to check if ANY of the inputs do)
        requires_grad = (
            grad_tracking_enabled
            and is_differentiable
            and any([(isinstance(a, Tensor) and a.requires_grad) for a in args])
        )

        # Create the output tensor from the underlying data and the requires_grad flag
        out = Tensor(out_arr, requires_grad)

        # If requires_grad, then create a recipe
        if requires_grad:
            parents = {idx: a for idx, a in enumerate(args) if isinstance(a, Tensor)}
            out.recipe = Recipe(numpy_func, arg_arrays, kwargs, parents)

        return out

    return tensor_func
```
</details>


Note - none of these functions involve keyword args, so the tests won't detect if you're handling kwargs incorrectly (or even failing to use them at all). If your code fails in later exercises, you might want to come back here and check that you're using the kwargs correctly. Alternatively, once you pass the tests, you can compare your code to the solutions and see how they handle kwargs.


## Backpropagation

Now all the pieces are in place to implement backpropagation. We need to loop over our nodes from right to left (i.e. starting with the tensors computed last and moving backwards chronologically). At each node, we:

- Call the backward function to transform the grad wrt output to the grad wrt input.
- If the node is a leaf, write the grad to the grad field.
- Otherwise, accumulate the grad into temporary storage.


### Topological Sort

As part of backprop, we need to sort the nodes of our graph so we can traverse the graph in the appropriate order.


### Exercise - implement `topological_sort`

> ```yaml
> Difficulty: 🔴🔴🔴🔴⚪
> Importance: 🔵⚪⚪⚪⚪
> 
> You should spend up to 20-25 minutes on this exercise.
> Note, it's completely fine to skip this problem if you're not very interested in it.
> It's more of a fun LeetCode-style challenge, and writing a solution for it isn't crucial for understanding today's content.
> ```

Write a general function `topological_sort` that return a list of node's children in topological order (beginning with the furthest descendants, ending with the starting node) using [depth-first search](https://en.wikipedia.org/wiki/Topological_sorting).

We've given you a `Node` class, with a `children` attribute, and a `get_children` function. You shouldn't change any of these, and your `topological_sort` function should use `get_children` to access a node's children rather than calling `node.children` directly. In subsequent exercises, we'll replace the `Node` class with the `Tensor` class (and using a different `get_children` function), so this will ensure your code still works for this new case.

If you're stuck, try looking at the pseudocode from some of [these examples](https://en.wikipedia.org/wiki/Topological_sorting#Kahn's_algorithm).


```python
class Node:
    def __init__(self, *children):
        self.children = list(children)


def get_children(node: Node) -> list[Node]:
    return node.children


def topological_sort(node: Node, get_children: Callable) -> list[Node]:
    """
    Return a list of node's descendants in reverse topological order from future
    to past (i.e. `node` should be last).

    Should raise an error if the graph with `node` as root is not in fact acyclic.
    """
    raise NotImplementedError()


tests.test_topological_sort_linked_list(topological_sort)
tests.test_topological_sort_branching(topological_sort)
tests.test_topological_sort_rejoining(topological_sort)
tests.test_topological_sort_cyclic(topological_sort)
```


<details>
<summary>Help - my function is hanging without returning any values.</summary>

This is probably because it's going around in cycles when fed a cyclic graph. You should add a way of raising an error if your function detects that the graph isn't cyclic. One way to do this is to create a set `temp`, which stores the nodes you've visited on a particular excursion into the graph, then you can raise an error if you come across an already visited node.
</details>

<details>
<summary>Help - I'm completely stuck on how to implement this, and would like the template for some code.</summary>

Here is the template for a depth-first search implementation:

```python
def topological_sort(node: Node, get_children: Callable) -> list[Node]:
    
    result: list[Node] = [] # stores the list of nodes to be returned (in reverse topological order)
    perm: set[Node] = set() # same as `result`, but as a set (faster to check for membership)
    temp: set[Node] = set() # keeps track of previously visited nodes (to detect cyclicity)

    def visit(cur: Node):
        '''
        Recursive function which visits all the children of the current node, and appends them all
        to `result` in the order they were found.
        '''
        pass

    visit(node)
    return result
```
</details>


<details><summary>Solution</summary>

```python
def topological_sort(node: Node, get_children: Callable) -> list[Node]:
    """
    Return a list of node's descendants in reverse topological order from future
    to past (i.e. `node` should be last).

    Should raise an error if the graph with `node` as root is not in fact acyclic.
    """
    result: list[Node] = []  # stores the list of nodes to be returned (in reverse topological order)
    perm: set[Node] = set()  # same as `result`, but as a set (faster to check for membership)
    temp: set[Node] = set()  # keeps track of previously visited nodes (to detect cyclicity)

    def visit(cur: Node):
        """
        Recursive function which visits all the children of the current node,
        and appends them all to `result` in the order they were found.
        """
        if cur in perm:
            return
        if cur in temp:
            raise ValueError("Not a DAG!")
        temp.add(cur)

        for next in get_children(cur):
            visit(next)

        result.append(cur)
        perm.add(cur)
        temp.remove(cur)

    visit(node)
    return result
```
</details>


Now, we've given you the function `sorted_computational_graph`. This calls `topological_sort` and returns the result in reverse order (because we want to start with the root node). The "get children" function we're using here is "return all tensors in the recipe for this tensor".


<img src="https://github.com/callummcdougall/Fundamentals/blob/main/images/abcdefg.png?raw=true" width=500>


```python
def sorted_computational_graph(tensor: Tensor) -> list[Tensor]:
    """
    For a given tensor, return a list of Tensors that make up the nodes of the given Tensor's
    computational graph, in reverse topological order (i.e. `tensor` should be first).
    """

    def get_parents(tensor: Tensor) -> list[Tensor]:
        if tensor.recipe is None:
            return []
        return list(tensor.recipe.parents.values())

    return topological_sort(tensor, get_parents)[::-1]


a = Tensor([1], requires_grad=True)
b = Tensor([2], requires_grad=True)
c = Tensor([3], requires_grad=True)
d = a * b
e = c.log()
f = d * e
g = f.log()
name_lookup = {a: "a", b: "b", c: "c", d: "d", e: "e", f: "f", g: "g"}

print([name_lookup[t] for t in sorted_computational_graph(g)])
```


<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">['g', 'f', 'e', 'c', 'd', 'b', 'a']</pre>


Compare your output with the computational graph. You should never be printing `x` before `y` if there is an edge `x --> ... --> y` (this should result in approximately reverse alphabetical order).


### The `backward` method

Now we're really ready for backprop!

Recall that in the implementation of the class `Tensor`, we had:

```python
class Tensor:
    ...
    def backward(self, end_grad: "Arr | Tensor | None" = None) -> None:
        if isinstance(end_grad, Arr):
            end_grad = Tensor(end_grad)
        return backprop(self, end_grad)
```

In other words, for a tensor `out`, calling `out.backward()` is equivalent to `backprop(out)`.

Recall that in the last section, we said that calling `backward` on a scalar tensor is equivalent to backpropagating on the weighted sum of all the elements of the tensor, i.e. `L = (tensor * v).sum()`. By default `v` is a tensor of 1s of the same shape as the tensor you're calling `backward` from, meaning we're just backpropagating on `L.sum()`. Here, the `end_grad` argument you pass to `backward` gives you the option to override this default behaviour, in other words if it's supplied you should use it as the first input to your backward function instead of a tensor of 1s. The use case for this is pretty niche (used for things like **influence functions**), but it's still useful to understand!


### Exercise - implement `backprop`

> ```yaml
> Difficulty: 🔴🔴🔴🔴🔴
> Importance: 🔵🔵🔵🔵🔵
> 
> You should spend up to 30-45 minutes on this exercise.
> 
> This exercise is the most conceptually important today, and probably the hardest. We've provided several dropdowns to help you.
> ```

Now, we get to the actual backprop function! Some code is provided below, which you should complete.

If you want a challenge, you can try and implement it straight away, with out any help. However, because this is quite a challenging exercise, you can also use the dropdowns below. The first one gives you a sketch of the backpropagation algorithm, the second gives you a diagram which provides a bit more detail, and the third gives you the annotations for the function (so you just have to fill in the code). You are recommended to start by trying to implement it without help, but use the dropdowns (in order) if this is too difficult.

We've also provided a few dropdowns to address specific technical errors that can arise from implementing this function. If you're having trouble, you can use these to help you debug. You should take some time with this function, as it's definitely the most important exercise to understand today.


```python
def backprop(end_node: Tensor, end_grad: Tensor | None = None) -> None:
    """Accumulates gradients in the grad field of each leaf node.

    tensor.backward() is equivalent to backprop(tensor).

    end_node:
        The rightmost node in the computation graph. If it contains more than one element, end_grad
        must be provided.
    end_grad:
        A tensor of the same shape as end_node. Set to 1 if not specified and end_node has only one
        element.
    """
    # Get value of end_grad_arr
    end_grad_arr = np.ones_like(end_node.array) if end_grad is None else end_grad.array

    # Create dict to store gradients
    grads: dict[Tensor, Arr] = {end_node: end_grad_arr}

    # YOUR CODE HERE - iterate through the sorted computational graph, performing backprop algorithm
    raise NotImplementedError()


tests.test_backprop(Tensor)
tests.test_backprop_branching(Tensor)
tests.test_backprop_requires_grad_sum(Tensor)
tests.test_backprop_requires_grad_false(Tensor)
tests.test_backprop_float_arg(Tensor)
```


<details>
<summary>Help - I get AttributeError: 'NoneType' object has no attribute 'func'</summary>

This error is probably because you're trying to access `recipe.func` from the wrong node. Possibly, you're calling your backward functions using the parents nodes' `recipe.func`, rather than the node's `recipe.func`.
        
To explain further, suppose your computational graph is simply:

<img src="https://raw.githubusercontent.com/info-arena/ARENA_img/refs/heads/main/img/Screenshot%25202023-02-17%2520174308.png" width=320>

When you reach `b` in your backprop iteration, you should calculate the gradient wrt `a` (the only parent of `b`) and store it in your `grads` dictionary, as `grads[a]`. In order to do this, you need the backward function for `func1`, which is stored in the node `b` (recall that the recipe of a tensor can be thought of as a set of instructions for how that tensor was created).
</details>

<details>
<summary>Help - I get AttributeError: 'numpy.ndarray' object has no attribute 'array'</summary>

This might be because you've set `node.grad` to be an array, rather than a tensor. You should store gradients as tensors (think of PyTorch, where `tensor.grad` will have type `torch.Tensor`).
        
It's fine to store numpy arrays in the `grads` dictionary, but when it comes time to set a tensor's grad attribute, you should use a tensor.
</details>

<details>
<summary>Help - I get 'RuntimeError: bool value of Tensor with more than one value is ambiguous'.</summary>

This error is probably because your computational graph function checks whether a tensor is in a list. The way these classes are compared for equality is a bit funky, and using sets rather than lists should make this error go away (i.e. checking whether a tensor is in a set should be fine).
</details>

<details>
<summary>Help - I'm failing on the <code>test_backprop_requires_grad_sum</code> test and I don't know why.</summary>

This test is designed to spot cases where you're accidentally **overwriting the gradient with each backward fn call**, rather than summing them. Remember that if a node has multiple paths from itself to the end node, then that node's grad attribute should be the sum of the gradients from all those

</details>

<details>
<summary>Help - I'm stuck, and I need a template for the function.</summary>

You just need to fill in the code below the comments labelled (1) and (2).

```python
def backprop(end_node: Tensor, end_grad: Tensor | None = None) -> None:

    # Get value of end_grad_arr
    end_grad_arr = np.ones_like(end_node.array) if end_grad is None else end_grad.array

    # Create dict to store gradients
    grads: dict[Tensor, Arr] = {end_node: end_grad_arr}

    for node in sorted_computational_graph(end_node):
        outgrad = grads.pop(node)

        # (1) If this is a leaf node, then set/update the gradient if requires_grad
        ...

        # (2) If this isn't a leaf node, then iterate through this node's parents and update their values in the `grads`
        # dict, using the outgrad values returned from this node's backward function
        ...
```

</details>


<details><summary>Solution</summary>

```python
def backprop(end_node: Tensor, end_grad: Tensor | None = None) -> None:
    """Accumulates gradients in the grad field of each leaf node.

    tensor.backward() is equivalent to backprop(tensor).

    end_node:
        The rightmost node in the computation graph. If it contains more than one element, end_grad
        must be provided.
    end_grad:
        A tensor of the same shape as end_node. Set to 1 if not specified and end_node has only one
        element.
    """
    # Get value of end_grad_arr
    end_grad_arr = np.ones_like(end_node.array) if end_grad is None else end_grad.array

    # Create dict to store gradients
    grads: dict[Tensor, Arr] = {end_node: end_grad_arr}

    for node in sorted_computational_graph(end_node):
        # Get the outgrad from the grads dict
        outgrad = grads.pop(node)

        # (1) If it's a leaf node, then set/update gradient if requires_grad=True, and stop here.
        if node.is_leaf:
            if node.requires_grad:
                node.grad = Tensor(outgrad) if node.grad is None else node.grad + outgrad

        # (2) If not a leaf node then it must have a recipe, so we iterate through its parents and
        # update their grads.
        else:
            for argnum, parent in node.recipe.parents.items():
                # Get backward function, from the fwd function that created `node` from `parent`.
                back_fn = BACK_FUNCS.get_back_func(node.recipe.func, argnum)

                # Use it to compute the gradient we'll add onto parent from the path `parent -> node
                # -> ... -> end_node`.
                in_grad = back_fn(outgrad, node.array, *node.recipe.args, **node.recipe.kwargs)

                # Add this gradient to the grads dict (handling special case where parent is not in
                # grads yet).
                grads[parent] = in_grad if (parent not in grads) else grads[parent] + in_grad
```
</details>




=== NEW CHAPTER ===


# 3️⃣ Training on MNIST from scratch



> ##### Learning Objectives
>
> * Implement more forward and backward functions, including for indexing, summing, and matrix multiplication
> * Learn how to build higher-level abstractions like parameters and modules on top of individual functions and tensors
> * Complete the process of building up a neural network from scratch and training it via gradient descent.

Congrats on implementing backprop! Soon we'll be able to train a full model from scratch, but first we'll go through a bunch of backward functions which will be necessary for training (as well as ones that cover some interesting cases). These should be a lot like your `log_back` and `multiply_back0`, `multiplyback1` examples earlier.


## More backward functions!

> Note - some of these exercises can get a bit repetitive, and so **you're welcome to skip through many of these exercises if you don't find them interesting, and/or you're pressed for time.** The exercises in the section "Parameters & Modules" and beyond are much more conceptually valuable.
> 
> Additionally, most of these functions can be implemented simply in 1 or 2 lines, so if you find yourself writing a lot more than that then you might want to look at the solution instead.


### Exercise - `negative`

> ```yaml
> Difficulty: 🔴⚪⚪⚪⚪
> Importance: 🔵⚪⚪⚪⚪
> 
> You should spend up to ~5 minutes on this exercise (it's not a trick question, it is as simple as it looks!).
> ```

`torch.negative` just performs `-x` elementwise. Make your own version `negative` using `wrap_forward_fn`. Note, you don't need to worry about unbroadcasting here because `np.negative` won't change the input shape (technically it can since `np.negative(x, out)` is actually the negative version of `x` broadcasted to the shape of `out`, but we won't be using it in this way during our exercises).


```python
def negative_back(grad_out: Arr, out: Arr, x: Arr) -> Arr:
    """Backward function for f(x) = -x elementwise."""
    raise NotImplementedError()


negative = wrap_forward_fn(np.negative)
BACK_FUNCS.add_back_func(np.negative, 0, negative_back)

tests.test_negative_back(Tensor)
```


<details><summary>Solution</summary>

```python
def negative_back(grad_out: Arr, out: Arr, x: Arr) -> Arr:
    """Backward function for f(x) = -x elementwise."""
    return -grad_out
```
</details>


### Exercise - `exp`

> ```yaml
> Difficulty: 🔴⚪⚪⚪⚪
> Importance: 🔵🔵⚪⚪⚪
> 
> You should spend up to 5-10 minutes on this exercise.
> ```

Make your own version of `torch.exp`. The backward function should express the result in terms of the `out` parameter - this more efficient than expressing it in terms of `x`.


```python
def exp_back(grad_out: Arr, out: Arr, x: Arr) -> Arr:
    """Backward function for f(x) = exp(x) elementwise."""
    raise NotImplementedError()


exp = wrap_forward_fn(np.exp)
BACK_FUNCS.add_back_func(np.exp, 0, exp_back)

tests.test_exp_back(Tensor)
```


<details><summary>Solution</summary>

```python
def exp_back(grad_out: Arr, out: Arr, x: Arr) -> Arr:
    """Backward function for f(x) = exp(x) elementwise."""
    return out * grad_out
```
</details>


### Exercise - `reshape`

> ```yaml
> Difficulty: 🔴🔴⚪⚪⚪
> Importance: 🔵⚪⚪⚪⚪
> 
> You should spend up to 5-10 minutes on this exercise.
> ```

`reshape` is a bit different than the functions we've dealt with so far: it changes the shape of the tensor, not its values. In other words, the backward function needs to be able to map from the gradient $\partial L / \partial \mathbf{x_r}$ to $\partial L / \partial \mathbf{x}$, where $\mathbf{x_r}$ is the reshaped version of $\mathbf{x}$.

Depending how you wrote `wrap_forward_fn` and `backprop`, you might need to go back and adjust them to handle this - if you're failing tests but think your implementation is correct, we recommend you go back to these functions and check them.

This function should just be a single line.


```python
def reshape_back(grad_out: Arr, out: Arr, x: Arr, new_shape: tuple) -> Arr:
    """Backward function for torch.reshape."""
    raise NotImplementedError()


reshape = wrap_forward_fn(np.reshape)
BACK_FUNCS.add_back_func(np.reshape, 0, reshape_back)

tests.test_reshape_back(Tensor)
```


<details>
<summary>Solution (and explanation)</summary>

Explanation: the reshape operation that takes us from the tensor $\frac{\partial L}{\partial \mathbf{x_r}}$ to $\frac{\partial L}{\partial \mathbf{x}}$ is exactly the inverse of the forward reshape operation that produced $\mathbf{x_r}$ from $\mathbf{x}$. In other words, we want to to take `grad_out` and reshape it back to the shape of `x`.

```python
def reshape_back(grad_out: Arr, out: Arr, x: Arr, new_shape: tuple) -> Arr:
    """Backward function for torch.reshape."""
    return np.reshape(grad_out, x.shape)
```

</details>


### Exercise - `permute`

> ```yaml
> Difficulty: 🔴🔴🔴⚪⚪
> Importance: 🔵⚪⚪⚪⚪
> 
> You should spend up to 5-10 minutes on this exercise.
> ```

In NumPy, the equivalent of `torch.permute` is called `np.transpose`, so we will wrap that. Permute is somewhat similar to reshape, but the difference is that it does actually change the order of elements in the underlying array.

Hint - just like with `reshape`, the inverse of a transposition is another transposition. You might find the function `np.argsort` useful for getting the inverse transposition.

This function should also just be a single line.


```python
def permute_back(grad_out: Arr, out: Arr, x: Arr, axes: tuple) -> Arr:
    """
    Backward function for torch.permute. Works by inverting the transposition in the forward
    function.
    """
    raise NotImplementedError()


BACK_FUNCS.add_back_func(np.transpose, 0, permute_back)
permute = wrap_forward_fn(np.transpose)

tests.test_permute_back(Tensor)
```


<details>
<summary>Solution (and explanation)</summary>

The inverse of transposing with `axes` is transposing using `np.argsort(axes)`. To see this: the forward transpose will send axis `j` to axis `axes[j]`, and so we want the inverse transposition `axes_inv` to satisfy `axes_inv[axes[j]] = j`, in other words **the indices of `axes_inv` should sort `axes`** - this is exactly what `np.argsort` does.

```python
def permute_back(grad_out: Arr, out: Arr, x: Arr, axes: tuple) -> Arr:
    """
    Backward function for torch.permute. Works by inverting the transposition in the forward
    function.
    """
    return np.transpose(grad_out, np.argsort(axes))
```

</details>


### Exercise - `sum`

> ```yaml
> Difficulty: 🔴🔴🔴⚪⚪
> Importance: 🔵🔵⚪⚪⚪
> 
> You should spend up to 20-30 minutes on this exercise.
> ```

The output can also be smaller than the input, such as when calling `torch.sum`.

Recall that when we looked at broadcasting, the backwards operation was summing over the broadcasted dimensions. This is because a broadcast operation effectively copies our tensor, giving it more gradient paths that we need to sum over. Similarly, the backwards operation for summing is broadcasting. We can intuitively see this as follows: if we have some value `L = L(x_summed)` where `x_summed` is the result of summing `x` over some number of dimensions, then editing `x_summed[i, j, ...] += delta` has the same downstream effect as editing any one of the `x` values which were summed over to get `x_summed[i, j, ...]`. So to get the gradient of `L` wrt `x`, we need to copy (broadcast) the gradient of `L` wrt `x_summed` up to the full size of `x`.

Implementing `sum_back` should have 2 steps:

1. **Adding new dims if they were summed over with `keepdim=False`**. You can do this with `np.expand_dims`, for example if `arr` has shape `(2, 3)` then `np.expand_dims(arr, (0, 2))` has shape `(1, 2, 1, 3)`, i.e. it's a new tensor with dummy dimensions created at indices 0 and 2.
2. **Broadcasting along dims that were summed over**. Since after step (1) you've effectively reduced to the `keepdim=True` case, you can now use `np.broadcast_to` to get the correct shape.

Note, if you get weird errors that you can't explain, and these exceptions don't even go away when you use the solutions provided, this could mean that your implementation of `wrap_forward_fn` was wrong in a way which wasn't picked up by the tests. You should return to this function and try to fix it (or just use the solution).


```python
def sum_back(grad_out: Arr, out: Arr, x: Arr, dim=None, keepdim=False):
    """Backward function for torch.sum"""
    raise NotImplementedError()


def _sum(x: Arr, dim=None, keepdim=False) -> Arr:
    """Like torch.sum, calling np.sum internally."""
    return np.sum(x, axis=dim, keepdims=keepdim)


sum = wrap_forward_fn(_sum)
BACK_FUNCS.add_back_func(_sum, 0, sum_back)

tests.test_sum_keepdim_false(Tensor)
tests.test_sum_keepdim_true(Tensor)
tests.test_sum_dim_none(Tensor)
tests.test_sum_nonscalar_grad_out(Tensor)
```


<details>
<summary>Help - I'm not sure how to handle the case where <code>dim=None</code>.</summary>

You can actually handle this pretty easily - if `dim=None` then `grad_out` will be a scalar, so it's always fine to broadcast it along the dims that were summed over! This means you can skip step (1), i.e. this step only needs to handle the case where `keepdim=False` and `dim` is not `None`.

</details>

<details>
<summary>Help - I get the error "Encountered error when running `backward` in the test for nonscalar grad_out."</summary>

This error is likely due to the fact that you're expanding your tensor in a way that doesn't refer to the dimensions being summed over (i.e. the `dim` argument).

Remember that in the previous exercise we assumed that the tensors were broadcastable with each other, and our functions could just internally call `np.broadcast_to` as a result. But here, one tensor is the sum over another tensor's dimensions, and if `keepdim=False` then they might not broadcast. For instance, if `x.shape = (2, 5)`, `out = x.sum(dim=1)` has shape `(2,)` and `grad_out.shape = (2,)`, then the tensors `grad_out` and `x` are not broadcastable.

How can you carefully handle the case where `keepdim=False` and `dim` doesn't just refer to dimensions at the start of the tensor? (Hint - try and use `np.expand_dims`).

</details>


<details><summary>Solution</summary>

```python
def sum_back(grad_out: Arr, out: Arr, x: Arr, dim=None, keepdim=False):
    """Backward function for torch.sum"""
    # Step (1): if keepdim=False, then we need to add back in dims, so grad_out and x have the
    # same number of dims. We don't bother with the dim=None case, since then grad_out is a scalar
    # and this will be handled by our broadcasting in step (2).
    if (not keepdim) and (dim is not None):
        grad_out = np.expand_dims(grad_out, dim)

    # Step (2): repeat grad_out along the dims over which x was summed
    return np.broadcast_to(grad_out, x.shape)
```
</details>


### Elementwise add, subtract, divide

> ```yaml
> Difficulty: 🔴🔴🔴⚪⚪
> Importance: 🔵🔵⚪⚪⚪
> 
> You should spend up to 10-15 minutes on this exercise.
> ```

These are exactly analogous to the multiply case. Note that Python and NumPy have the notion of "floor division", which is a truncating integer division as in `7 // 3 = 2`. You can ignore floor division: - we only need the usual floating point division which is called "true division".

Use lambda functions to define and register the backward functions each in one line. We've given you the first one.


```python
add = wrap_forward_fn(np.add)
subtract = wrap_forward_fn(np.subtract)
true_divide = wrap_forward_fn(np.true_divide)

BACK_FUNCS.add_back_func(np.add, 0, lambda grad_out, out, x, y: unbroadcast(grad_out, x))
# YOUR CODE HERE - continue adding to BACK_FUNCS, for each of the 3 functions & both arg orders

tests.test_add_broadcasted(Tensor)
tests.test_subtract_broadcasted(Tensor)
tests.test_truedivide_broadcasted(Tensor)
```


<details><summary>Solution</summary>

```python
BACK_FUNCS.add_back_func(np.add, 0, lambda grad_out, out, x, y: unbroadcast(grad_out, x))
BACK_FUNCS.add_back_func(np.add, 1, lambda grad_out, out, x, y: unbroadcast(grad_out, y))
BACK_FUNCS.add_back_func(np.subtract, 0, lambda grad_out, out, x, y: unbroadcast(grad_out, x))
BACK_FUNCS.add_back_func(np.subtract, 1, lambda grad_out, out, x, y: unbroadcast(-grad_out, y))
BACK_FUNCS.add_back_func(np.true_divide, 0, lambda grad_out, out, x, y: unbroadcast(grad_out / y, x))
BACK_FUNCS.add_back_func(np.true_divide, 1, lambda grad_out, out, x, y: unbroadcast(grad_out * (-x / y**2), y))
```
</details>


### Indexing

If we have the gradient of `L` wrt `x[index]`, what is the gradient of `L` wrt `x`? The answer is it'll be an array of zeros, filled in with the values of `dL/dx[index]` at the appropriate index positions. For example, if `x = [1, 2, 3]` and `L = x[0]`, then we trivially have `dL/dx[0] = 1`, and we can compute `dL/dx = [1, 0, 0]` in this way.

In its full generality, exactly how you can index a `torch.Tensor` is really complicated and there are quite a few cases to handle separately. Our implementation only handles 2 cases:

- The index is an integer or tuple of integers.
- The index is a tuple of (array or Tensor) representing coordinates. Each array is 1D and of equal length. Some coordinates may be repeated. This is [Integer array indexing](https://numpy.org/doc/stable/user/basics.indexing.html#integer-array-indexing).

This latter case is very important, because it describes how we index correct logprobs / probabilities. For example if we're training a classifier and we have tensors `logprobs.shape = (batch_size, n_classes)` and `targets.shape = (n_classes,)` then we index the correct logprobs using `logprobs[arange(batch_size), targets]` (note that the `arange` function has been given to you earlier, when we defined the `Tensor` class - it's a simple wrapper around `np.arange`).


```python
Index = int | tuple[int, ...] | tuple[Arr] | tuple[Tensor]


def coerce_index(index: Index):
    """Helper function: converts array of tensors to array of numpy arrays."""
    if isinstance(index, tuple) and all(isinstance(i, Tensor) for i in index):
        return tuple([i.array for i in index])
    else:
        return index


def _getitem(x: Arr, index: Index) -> Arr:
    """Like x[index] when x is a torch.Tensor."""
    return x[coerce_index(index)]


def getitem_back(grad_out: Arr, out: Arr, x: Arr, index: Index):
    """
    Backwards function for _getitem.

    Hint: use np.add.at(a, indices, b)
    This function works just like a[indices] += b, except that it allows for repeated indices.
    """
    new_grad_out = np.full_like(x, 0)
    np.add.at(new_grad_out, coerce_index(index), grad_out)
    return new_grad_out


getitem = wrap_forward_fn(_getitem)
BACK_FUNCS.add_back_func(_getitem, 0, getitem_back)
```


### Non-Differentiable Functions

For functions like `torch.argmax` or `torch.eq`, there's no sensible way to define gradients with respect to the input tensor. For these, we will still use `wrap_forward_fn` because we still need to unbox the arguments and box the result, but by passing `is_differentiable=False` we can avoid doing any unnecessary computation.

We've given you this one as an example:


```python
def _argmax(x: Arr, dim=None, keepdim=False):
    """Like torch.argmax."""
    result = np.argmax(x, axis=dim)
    if keepdim:
        return np.expand_dims(result, axis=([] if dim is None else dim))
    return result


argmax = wrap_forward_fn(_argmax, is_differentiable=False)

a = Tensor([1.0, 0.0, 3.0, 4.0], requires_grad=True)
b = a.argmax()
assert not b.requires_grad
assert b.recipe is None
assert b.item() == 3
```


### In-Place Operations

Supporting in-place operations introduces substantial complexity and generally doesn't help performance that much. The problem is that if any of the inputs used in the backward function have been modified in-place since the forward pass, then the backward function will incorrectly calculate using the modified version. PyTorch will warn you when this causes a problem with the error "RuntimeError: a leaf Variable that requires grad is being used in an in-place operation.".

Note - you don't have to fill anything in here; just run the cell. If you're curious, you can implement inplace operations as a bonus exercise at the end, but for now we just warn against inplace operations unless we specify otherwise.


```python
def add_(x: Tensor, other: Tensor, alpha: float = 1.0) -> Tensor:
    """Like torch.add_. Compute x += other * alpha in-place and return tensor."""
    np.add(x.array, other.array * alpha, out=x.array)
    return x


def sub_(x: Tensor, other: Tensor, alpha: float = 1.0) -> Tensor:
    """Like torch.sub_. Compute x -= other * alpha in-place and return tensor."""
    np.subtract(x.array, other.array * alpha, out=x.array)
    return x


def safe_example():
    """This example should work properly."""
    a = Tensor([0.0, 1.0, 2.0, 3.0], requires_grad=True)
    b = Tensor([2.0, 3.0, 4.0, 5.0], requires_grad=True)
    a.add_(b)
    c = a * b
    c.sum().backward()
    assert a.grad is not None and np.allclose(a.grad.array, [2.0, 3.0, 4.0, 5.0])
    assert b.grad is not None and np.allclose(b.grad.array, [2.0, 4.0, 6.0, 8.0])


def unsafe_example():
    """
    This example is expected to compute the wrong gradients, because dc/db is calculated using the
    modified a.
    """
    a = Tensor([0.0, 1.0, 2.0, 3.0], requires_grad=True)
    b = Tensor([2.0, 3.0, 4.0, 5.0], requires_grad=True)
    c = a * b
    a.add_(b)
    c.sum().backward()
    if a.grad is not None and np.allclose(a.grad.array, [2.0, 3.0, 4.0, 5.0]):
        print("Grad wrt a is OK!")
    else:
        print("Grad wrt a is WRONG!")
    if b.grad is not None and np.allclose(b.grad.array, [0.0, 1.0, 2.0, 3.0]):
        print("Grad wrt b is OK!")
    else:
        print("Grad wrt b is WRONG!")


safe_example()
unsafe_example()
```


### Mixed Scalar-Tensor Operations

You may have been wondering why our `Tensor` class has to define both `__mul__` and `__rmul__` magic methods.

Without `__rmul__` defined, executing `2 * a` when `a` is a `Tensor` would try to call `2.__mul__(a)`, and the built-in class `int` would be confused about how to handle this.

Since we have defined `__rmul__` for you at the start, and you implemented multiply to work with floats as arguments, the following should "just work".


```python
a = Tensor([0, 1, 2, 3], requires_grad=True)
(a * 2).sum().backward()
b = Tensor([0, 1, 2, 3], requires_grad=True)
(2 * b).sum().backward()
assert a.grad is not None
assert b.grad is not None
assert np.allclose(a.grad.array, b.grad.array)
```


### Exercise - `max`

> ```yaml
> Difficulty: 🔴🔴🔴⚪⚪
> Importance: 🔵🔵⚪⚪⚪
> 
> You should spend up to 10-15 minutes on this exercise.
> ```

Since this is an elementwise function, we can think about the scalar case. For scalar $x$, $y$, the derivative for $\max(x, y)$ wrt $x$ is 1 when $x > y$ and 0 when $x < y$. What should happen when $x = y$?

Intuitively, since $\max(x, x)$ is equivalent to the identity function which has a derivative of 1 wrt $x$, it makes sense for the sum of our partial derivatives wrt $x$ and $y$ to also therefore total 1. The convention used by PyTorch is to split the derivative evenly between the two arguments. We will follow this behavior for compatibility, but it's just as legitimate to say it's 1 wrt $x$ and 0 wrt $y$, or some other arbitrary combination that sums to one.


<details>
<summary>Help - I'm not sure how to implement this function.</summary>

Try returning `grad_out * bool_sum`, where `bool_sum` is an array constructed from the sum of two boolean arrays.

You can alternatively use `np.where`.
</details>

<details>
<summary>Help - I'm passing the first test but not the second.</summary>

This probably means that you haven't implemented `unbroadcast`. You'll need to do this, to get `grad_out` into the right shape before you use it in `np.where`.
</details>


```python
def maximum_back0(grad_out: Arr, out: Arr, x: Arr, y: Arr):
    """Backwards function for max(x, y) wrt x."""
    raise NotImplementedError()


def maximum_back1(grad_out: Arr, out: Arr, x: Arr, y: Arr):
    """Backwards function for max(x, y) wrt y."""
    raise NotImplementedError()


maximum = wrap_forward_fn(np.maximum)
BACK_FUNCS.add_back_func(np.maximum, 0, maximum_back0)
BACK_FUNCS.add_back_func(np.maximum, 1, maximum_back1)

tests.test_maximum(Tensor)
tests.test_maximum_broadcasted(Tensor)
```


<details><summary>Solution</summary>

```python
def maximum_back0(grad_out: Arr, out: Arr, x: Arr, y: Arr):
    """Backwards function for max(x, y) wrt x."""
    bool_sum = (x > y) + 0.5 * (x == y)
    return unbroadcast(grad_out * bool_sum, x)


def maximum_back1(grad_out: Arr, out: Arr, x: Arr, y: Arr):
    """Backwards function for max(x, y) wrt y."""
    bool_sum = (x < y) + 0.5 * (x == y)
    return unbroadcast(grad_out * bool_sum, y)
```
</details>


### Exercise - functional `ReLU`

> ```yaml
> Difficulty: 🔴⚪⚪⚪⚪
> Importance: 🔵⚪⚪⚪⚪
> 
> You should spend ~5 minutes on this exercise.
> ```

A simple and correct ReLU function can be defined in terms of your maximum function. Note the PyTorch version also supports in-place operation, which we are punting to the bonus section for now.

Again, at $x = 0$ your derivative could reasonably be anything between 0 and 1 inclusive, but we've followed PyTorch in making it 0.5. This means you can just use the `maximum` function defined above!


```python
def relu(x: Tensor) -> Tensor:
    """Like torch.nn.function.relu(x, inplace=False)."""
    raise NotImplementedError()


tests.test_relu(Tensor)
```


<details><summary>Solution</summary>

```python
def relu(x: Tensor) -> Tensor:
    """Like torch.nn.function.relu(x, inplace=False)."""
    return maximum(x, 0.0)
```
</details>


### Exercise - 2D `matmul`

> ```yaml
> Difficulty: 🔴🔴🔴⚪⚪
> Importance: 🔵🔵🔵⚪⚪
> 
> You should spend up to 20-25 minutes on this exercise.
> ```

Implement your version of `torch.matmul`, restricting it to the simpler case where both inputs are 2D (this means we don't need to worry about unbroadcasting or anything).

Note - althought the solution to this exercise is very short (just one line), you may find the actual mathematical derivation a bit tricky. We've given hints to help you, which we recommend using if you're stuck.


```python
def _matmul2d(x: Arr, y: Arr) -> Arr:
    """Matrix multiply restricted to the case where both inputs are exactly 2D."""
    return x @ y


def matmul2d_back0(grad_out: Arr, out: Arr, x: Arr, y: Arr) -> Arr:
    raise NotImplementedError()


def matmul2d_back1(grad_out: Arr, out: Arr, x: Arr, y: Arr) -> Arr:
    raise NotImplementedError()


matmul = wrap_forward_fn(_matmul2d)
BACK_FUNCS.add_back_func(_matmul2d, 0, matmul2d_back0)
BACK_FUNCS.add_back_func(_matmul2d, 1, matmul2d_back1)

tests.test_matmul2d(Tensor)
```


<details>
<summary>Help - I need a hint about the math</summary>

Let $X$, $Y$ and $M$ denote the variables `x`, `y` and `out`, so we have the matrix relation $M = XY$. The object `grad_out` is a tensor with elements `grad_out[p, q]` $ = \frac{\partial L}{\partial M_{p q}}$.

The output of `matmul2d_back0` should be the gradient of $L$ wrt $X$, i.e. it should have elements $\frac{\partial L}{\partial X_{i j}}$. Can you write this in terms of the elements of `x`, `y`, `out` and `grad_out`?
</details>

<details>
<summary>Help - I need the math explained</summary>

We can write $\frac{\partial L}{\partial X_{i j}}$ as:

$$
\begin{aligned}
\frac{\partial L}{\partial X_{i j}} &=\sum_{pq} \frac{\partial L}{\partial M_{p q}} \frac{\partial M_{p q}}{\partial X_{i j}} \\
&=\sum_{pqr} \left[\text{ grad\_out }\right]_{p q} \frac{\partial (X_{p r} Y_{r q})}{\partial X_{i j}} \\
&=\sum_{q} \left[\text{ grad\_out }\right]_{iq} Y_{j q} \\
&= \left[\text{ grad\_out } \times Y^{\top}\right]_{ij}
\end{aligned}
$$

where the second line follows because $M_{pq} = \sum_r X_{pr} Y_{rq}$ (and we can rearrange the summands), and the third line follows because $\frac{\partial{X_{pr}}}{X_{ij}} = 1 \text{ if } (p, r) = (i, j), \text{ else } 0$.


In other words, the `x.grad` attribute should be is `grad_out @ y.T`.

You can calculate the gradient wrt `y` in a similar way - we leave this as an exercise for the reader.
</details>


<details><summary>Solution</summary>

```python
def _matmul2d(x: Arr, y: Arr) -> Arr:
    """Matrix multiply restricted to the case where both inputs are exactly 2D."""
    return x @ y


def matmul2d_back0(grad_out: Arr, out: Arr, x: Arr, y: Arr) -> Arr:
    return grad_out @ y.T


def matmul2d_back1(grad_out: Arr, out: Arr, x: Arr, y: Arr) -> Arr:
    return x.T @ grad_out
```
</details>


## Parameters & Modules

We've now written enough backwards passes that we can go up a layer and write our own `nn.Parameter` and `nn.Module`. These are important abstractions that help us building up neural networks.

Below is a simple implementation of `Parameter`. It is itself a `Tensor`, shares storage with the provided `Tensor` and requires_grad is `True` by default - that's it! Make sure you understand the code being run in this cell to test the functionality of this class.


```python
class Parameter(Tensor):
    def __init__(self, tensor: Tensor, requires_grad=True):
        """Share the array with the provided tensor."""
        return super().__init__(tensor.array, requires_grad=requires_grad)

    def __repr__(self):
        return f"Parameter containing:\n{super().__repr__()}"


x = Tensor([1.0, 2.0, 3.0])
p = Parameter(x)
assert p.requires_grad
assert p.array is x.array
assert repr(p) == "Parameter containing:\nTensor(array([1., 2., 3.], dtype=float32), requires_grad=True)"
x.add_(Tensor(np.array(2.0)))
assert np.allclose(p.array, np.array([3.0, 4.0, 5.0])), (
    "in-place modifications to the original tensor should affect the parameter"
)
```


Just like `torch.Tensor`, the `nn.Module` class has a lot of functionality which we mostly don't care about today. We will just implement enough to get our network training.

Below is a simple implementation. We'll explain it a bit below (if you're already experienced in Python then this might be obvious to you and you can skip it).

- **Single-underscore attributes** are a notational convention; they're not treated differently by Python but they're used to indicate that the attribute is private and shouldn't be accessed directly by anyone using the class.
    - `_modules` is a dict mapping module names to module objects. The `modules` method returns an iterator over these modules.
    - `_parameters` is similar, with added recursion to include submodule parameters.
- **Double-underscore attributes** are special methods that determine how your class instance behaves when you use certain syntax.
    - `__call__` determines what the module does when you call it like a function. In this case, `module(*args, **kwargs)` calls `module.forward(**args, **kwargs)` - this is why we only ever need to implement `forward` in the modules we've written so far.
    - `__setattr__` manages attribute setting (i.e. running `module.attr = value` actually calls `module.__setattr__("attr", value)`). The default behaviour is to add the attribute to `self.__dict__`, but we've added custom logic so modules & parameters are also added to `self._modules` and `self._parameters` respectively - this is basically how logic like `module.parameters()` can work.
        - Note that there's a related method `__getattr__` which specifies attribute getting behaviour when lookup in `self.__dict__` fails.


```python
class Module:
    _modules: dict[str, "Module"]
    _parameters: dict[str, Parameter]

    def __init__(self):
        self._modules: dict[str, "Module"] = {}
        self._parameters: dict[str, Parameter] = {}

    def modules(self) -> Iterator["Module"]:
        """Return the direct child modules of this module, not including self."""
        yield from self._modules.values()

    def parameters(self, recurse: bool = True) -> Iterator[Parameter]:
        """
        Return an iterator over Module parameters.

        recurse: if True, the iterator includes parameters of submodules, recursively.
        """
        yield from self._parameters.values()
        if recurse:
            for mod in self.modules():
                yield from mod.parameters(recurse=True)

    def __setattr__(self, key: str, val: Any) -> None:
        """
        If val is a Parameter or Module, store it in the appropriate _parameters or _modules dict.
        Otherwise, call __setattr__ from the superclass.
        """
        if isinstance(val, Parameter):
            self._parameters[key] = val
        elif isinstance(val, Module):
            self._modules[key] = val
        super().__setattr__(key, val)

    def __call__(self, *args, **kwargs):
        return self.forward(*args, **kwargs)

    def forward(self):
        raise NotImplementedError("Subclasses must implement forward!")

    def __repr__(self):
        _indent = lambda s_, nSpaces: re.sub("\n", "\n" + (" " * nSpaces), s_)
        lines = [f"({key}): {_indent(repr(module), 2)}" for key, module in self._modules.items()]
        return "".join(
            [
                self.__class__.__name__ + "(",
                "\n  " + "\n  ".join(lines) + "\n" if lines else "",
                ")",
            ]
        )


class TestInnerModule(Module):
    def __init__(self):
        super().__init__()
        self.param1 = Parameter(Tensor([1.0]))
        self.param2 = Parameter(Tensor([2.0]))


class TestModule(Module):
    def __init__(self):
        super().__init__()
        self.inner = TestInnerModule()
        self.param3 = Parameter(Tensor([3.0]))


mod = TestModule()
assert list(mod.modules()) == [mod.inner]
assert list(mod.parameters()) == [mod.param3, mod.inner.param1, mod.inner.param2]
print("Manually verify that the repr looks reasonable:")
print(mod)
print("All tests for `Module` passed!")
```


### Exercise - implement `Linear`

> ```yaml
> Difficulty: 🔴🔴🔴⚪⚪
> Importance: 🔵🔵🔵🔵⚪
> 
> You should spend up to 20-25 minutes on this exercise.
> ```

Now, let's go one level of abstraction higher and create a `Linear` module. This should inherit from `Module` and have `__init__` & `forward` methods just like your linear module inheriting from `nn.Module` in previous exercises. In fact, your code can probably be extremely similar to the time you implemented `Linear` in the earlier exercises, except you'll need to use methods we've defined already. You should be able to do everything you need in `forward` using just the matmul operator `@`, the transpose operator `.T` (which is equivalent to `.permute(-1, -2)` as you can see in the tensor class above) and standard tensor addition `+`.

To restate the task in case you don't remember it from the previous exercises, you should:

- Define `self.weight` and `self.bias` in `__init__`, with both tensors having a uniform distribution in the range `[-sf, sf]` where `sf = 1/sqrt(in_features)`,
- Write the appropriate affine operation in `forward`, i.e. multiplying by `self.weight` and adding `self.bias` if it exists.

Don't forget to wrap your weights as `Parameter(Tensor(...))`.


```python
class Linear(Module):
    weight: Parameter
    bias: Parameter | None

    def __init__(self, in_features: int, out_features: int, bias=True):
        """
        A simple linear (technically, affine) transformation.

        The fields should be named `weight` and `bias` for compatibility with PyTorch.
        If `bias` is False, set `self.bias` to None.
        """
        super().__init__()
        self.in_features = in_features
        self.out_features = out_features

        raise NotImplementedError()

    def forward(self, x: Tensor) -> Tensor:
        """
        x: shape (*, in_features)
        Return: shape (*, out_features)
        """
        raise NotImplementedError()

    def extra_repr(self) -> str:
        return f"in_features={self.in_features}, out_features={self.out_features}, bias={self.bias is not None}"


linear = Linear(3, 4)
assert isinstance(linear.weight, Tensor)
assert linear.weight.requires_grad

input = Tensor([[1.0, 2.0, 3.0]])
output = linear(input)
assert output.requires_grad

expected_output = input @ linear.weight.T + linear.bias
np.testing.assert_allclose(output.array, expected_output.array)

print("All tests for `Linear` passed!")
```


<details><summary>Solution</summary>

```python
class Linear(Module):
    weight: Parameter
    bias: Parameter | None

    def __init__(self, in_features: int, out_features: int, bias=True):
        """
        A simple linear (technically, affine) transformation.

        The fields should be named `weight` and `bias` for compatibility with PyTorch.
        If `bias` is False, set `self.bias` to None.
        """
        super().__init__()
        self.in_features = in_features
        self.out_features = out_features

        sf = in_features**-0.5
        self.weight = Parameter(Tensor(sf * (2 * np.random.rand(out_features, in_features) - 1)))
        self.bias = Parameter(Tensor(sf * (2 * np.random.rand(out_features) - 1))) if bias else None

    def forward(self, x: Tensor) -> Tensor:
        """
        x: shape (*, in_features)
        Return: shape (*, out_features)
        """
        out = x @ self.weight.T  # transpose has been defined as .permute(-1, -2), see the `Tensor` class
        if self.bias is not None:
            out = out + self.bias
        return out

    def extra_repr(self) -> str:
        return f"in_features={self.in_features}, out_features={self.out_features}, bias={self.bias is not None}"
```
</details>


Finally, for the sake of completeness, we'll define a `ReLU` module:


```python
class ReLU(Module):
    def forward(self, x: Tensor) -> Tensor:
        return relu(x)
```


Now we can define a MLP suitable for classifying MNIST, with zero PyTorch dependency!


```python
class MLP(Module):
    def __init__(self):
        super().__init__()
        self.linear1 = Linear(28 * 28, 64)
        self.linear2 = Linear(64, 64)
        self.relu1 = ReLU()
        self.relu2 = ReLU()
        self.output = Linear(64, 10)

    def forward(self, x: Tensor) -> Tensor:
        x = x.reshape((x.shape[0], 28 * 28))
        x = self.relu1(self.linear1(x))
        x = self.relu2(self.linear2(x))
        x = self.output(x)
        return x
```


### Exercise - implement `cross_entropy`

> ```yaml
> Difficulty: 🔴🔴🟠⚪⚪
> Importance: 🔵🔵🔵⚪⚪
> 
> You should spend up to 10-15 minutes on this exercise.
> ```

Make use of your integer array indexing to implement `cross_entropy`. See the documentation page [here](https://pytorch.org/docs/stable/generated/torch.nn.CrossEntropyLoss.html).

We discussed this briefly in the section on indexing earlier, but the kind of indexing you should be doing on your logprobs is `logprobs[range(batch_size), true_labels]`, since this is equivalent to returning the vector of length `batch_size` with elements `[logprobs[0, true_labels[0]], logprobs[1, true_labels[1]], ...]`. Rather than using `range`, you should be using the `arange` function we've provided for you (this is equivalent to torch's `torch.arange` function, and is defined just below the `Tensor` class).

Note - if you're using the `exp` function, it's usually good to make your implementation numerically stable (since taking the exponential of large numbers is prone to overflow). The common solution here is to subtract the maximum value of the tensor from all elements. However, you don't need to worry about that here (consider it a bonus exercise).


```python
def cross_entropy(logits: Tensor, true_labels: Tensor) -> Tensor:
    """Like torch.nn.functional.cross_entropy with reduction='none'.

    logits: shape (batch, classes)
    true_labels: shape (batch,). Each element is the index of the correct label in the logits.

    Return: shape (batch, ) containing the per-example loss.
    """
    raise NotImplementedError()


tests.test_cross_entropy(Tensor, cross_entropy)
```


<details>
<summary>Help - I'm not sure how to get logprobs from logits.</summary>

They're equal up to a constant: `logprobs = logits - log(sum(exp(logits)))` (where the sum is over the last dimension).

To see why this is true: let's define `C = logits - logprobs`. We know `sum(exp(logits - C)) = sum(exp(logprobs)) = 1` (this is by definition of `logprobs`). Factoring out the `exp(-C)` term, we get `exp(C) = sum(exp(logits))`, hence `C = log(sum(exp(logits)))` as required.

</details>

<details>
<summary>Solution</summary>

```python
def cross_entropy(logits: Tensor, true_labels: Tensor) -> Tensor:
    """Like torch.nn.functional.cross_entropy with reduction='none'.

    logits: shape (batch, classes)
    true_labels: shape (batch,). Each element is the index of the correct label in the logits.

    Return: shape (batch, ) containing the per-example loss.
    """
    batch_size = logits.shape[0]
    logprobs = logits - logits.exp().sum(-1, keepdim=True).log()
    return -logprobs[arange(0, batch_size), true_labels]
```

or alternatively we can solve a slightly different way, which is still equivalent:

```python
true = logits[arange(0, batch_size), true_labels]
return -log(exp(true) / exp(logits).sum(1))
```

</details>


## `NoGrad` context manager

The last thing our backpropagation system needs is the ability to turn it off completely like `torch.no_grad` (or `torch.inference_mode`). We've given you an implementation below, which works by modifying the global `grad_tracking_enabled` variable. 

A few notes on the actual python here (again for people who are more familiar with Python and understand it can skip this):

- The `global` keyword is required in order to modify the global `grad_tracking_enabled` variable. We can still reference its value without this keyword, but we wouldn't be able to change it.
- The special `__enter__` and `__exit__` methods are part of the protocol for context managers, which is a more pythonic way of doing this kind of thing. If we have a context manager block like `with NoGrad(): ...`, then we'll run `NoGrad().__enter__()` before any of the code in this block, and `NoGrad().__exit__()` after the block finishes.


```python
class NoGrad:
    """Context manager that disables grad inside the block. Like torch.no_grad."""

    was_enabled: bool

    def __enter__(self):
        """
        Method which is called whenever the context manager is entered, i.e. at the start of the
        `with NoGrad():` block. This disables gradient tracking (but stores the value it had before,
        so we can set it back to this on exit).
        """
        global grad_tracking_enabled
        self.was_enabled = grad_tracking_enabled
        grad_tracking_enabled = False

    def __exit__(self, type, value, traceback):
        """
        Method which is called whenever we exit the context manager. This sets the global
        `grad_tracking_enabled` variable back to the value it had before we entered the context
        manager.
        """
        global grad_tracking_enabled
        grad_tracking_enabled = self.was_enabled


assert grad_tracking_enabled
with NoGrad():
    assert not grad_tracking_enabled
assert grad_tracking_enabled
print("Verified that we've disabled gradients inside `NoGrad`, then set back to its previous value once we exit.")
```


### Exercise - implement `SGD`

> ```yaml
> Difficulty: 🔴🔴🔴⚪⚪
> Importance: 🔵🔵🔵⚪⚪
> 
> You should spend up to 10-20 minutes on this exercise.
> ```

In today's final exercise, you should implement the `SGD` class methods `zero_grad` and `step`. This should be pretty familiar if you've gone through yesterday's exercises on optimizers (although without all the bells and whistles from those exercises, because we're literally just implementing plain SGD with no momentum, weight decay or anything).

Important note - in yesterday's exercises it was important to use inplace operations, so we would actually modify the existing tensor data rather than creating new tensors, and this is also the case here. The inplace operation `+=` is supported, since under the hood this calls `__iadd__` which we've defined in our `Tensor` class (same for subtraction, the underlying method here is `__isub__`). Note that we did discuss earlier how inplace operations are very risky for backprop, this is generally true however here we're using it for parameter updates which aren't meant to be differentiated and which are performed just before zeroing all gradients - this makes it safe in this particular context.


```python
class SGD:
    def __init__(self, params: Iterable[Parameter], lr: float):
        """Vanilla SGD with no additional features."""
        self.params = list(params)
        self.lr = lr
        self.b = [None for _ in self.params]

    def zero_grad(self) -> None:
        """Iterates through params, and sets all grads to None."""
        raise NotImplementedError()

    def step(self) -> None:
        """Iterates through params, and updates each of them by subtracting `param.grad * lr`."""
        raise NotImplementedError()


tests.test_sgd(Parameter, Tensor, SGD)
```


<details><summary>Solution</summary>

```python
class SGD:
    def __init__(self, params: Iterable[Parameter], lr: float):
        """Vanilla SGD with no additional features."""
        self.params = list(params)
        self.lr = lr
        self.b = [None for _ in self.params]

    def zero_grad(self) -> None:
        """Iterates through params, and sets all grads to None."""
        for p in self.params:
            p.grad = None

    def step(self) -> None:
        """Iterates through params, and updates each of them by subtracting `param.grad * lr`."""
        with NoGrad():
            for p in self.params:
                p -= p.grad * self.lr
```
</details>


## Training Your Network

We've already looked at data loading and training loops earlier in the course, so we'll provide a minimal version of these today as well as the data loading code.


```python
train_loader, test_loader = get_mnist()
visualize(train_loader)
```


<div style="text-align: left"><embed src="https://info-arena.github.io/ARENA_img/misc/media-04/0401.html" width="1020" height="470"></div>


To finish the day, below is some code for a training/testing loop for MNIST images, which also logs & plots the results.

Note, it's normal to encounter some bugs and glitches at this point - just go back and fix them until everything runs! Because backprop is annoying and fiddly and depends heavily on exactly how the implementation works (with too many edge cases to test all of them), you may have to resort to replacing your code with the reference solution until you find the source of the error - this is a bit frustrating, but we'd be lying if we said ML isn't without its share of slow debugging sessions!


```python
def train(
    model: MLP,
    train_loader: DataLoader,
    optimizer: SGD,
    epoch: int,
    train_loss_list: list | None = None,
):
    print(f"Epoch: {epoch}")
    progress_bar = tqdm(train_loader)
    for data, target in progress_bar:
        data, target = Tensor(data.numpy()), Tensor(target.numpy())
        optimizer.zero_grad()
        output = model(data)
        loss = cross_entropy(output, target).sum() / len(output)
        loss.backward()
        progress_bar.set_description(f"Train set: Avg loss: {loss.item():.3f}")
        optimizer.step()
        if train_loss_list is not None:
            train_loss_list.append(loss.item())


def test(model: MLP, test_loader: DataLoader, test_accuracy_list: list | None = None):
    test_loss = 0
    test_accuracy = 0
    with NoGrad():
        for data, target in test_loader:
            data, target = Tensor(data.numpy()), Tensor(target.numpy())
            output: Tensor = model(data)
            test_loss += cross_entropy(output, target).sum().item()
            pred = output.argmax(dim=1, keepdim=True)
            test_accuracy += (pred == target.reshape(pred.shape)).sum().item()
    n_data = len(test_loader.dataset)
    test_loss /= n_data
    print(f"Test set:  Avg loss: {test_loss:.3f}, Accuracy: {test_accuracy}/{n_data} ({test_accuracy / n_data:.1%})")
    if test_accuracy_list is not None:
        test_accuracy_list.append(test_accuracy / n_data)


num_epochs = 5
model = MLP()
start = time.time()
train_loss_list = []
test_accuracy_list = []
optimizer = SGD(model.parameters(), 0.01)
for epoch in range(num_epochs):
    train(model, train_loader, optimizer, epoch, train_loss_list)
    test(model, test_loader, test_accuracy_list)

print(f"\nCompleted in {time.time() - start: .2f}s")

line(
    [train_loss_list, test_accuracy_list],
    x_max=num_epochs,
    yaxis2_range=[0, 1],
    use_secondary_yaxis=True,
    labels={"x": "Batches seen", "y1": "Cross entropy loss", "y2": "Test accuracy"},
    title="MLP training on MNIST from scratch!",
    width=800,
)
```


<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">Epoch: 0
Train set: Avg loss: 1.864: 100%|██████████| 118/118 [00:02<00:00, 55.00it/s]
Test set:  Avg loss: 1.848, Accuracy: 5763/10000 (57.6%)
Epoch: 1
Train set: Avg loss: 1.056: 100%|██████████| 118/118 [00:02<00:00, 56.57it/s]
Test set:  Avg loss: 0.998, Accuracy: 7843/10000 (78.4%)
Epoch: 2
Train set: Avg loss: 0.783: 100%|██████████| 118/118 [00:02<00:00, 54.62it/s]
Test set:  Avg loss: 0.652, Accuracy: 8315/10000 (83.2%)
Epoch: 3
Train set: Avg loss: 0.548: 100%|██████████| 118/118 [00:02<00:00, 54.98it/s]
Test set:  Avg loss: 0.518, Accuracy: 8600/10000 (86.0%)
Epoch: 4
Train set: Avg loss: 0.425: 100%|██████████| 118/118 [00:02<00:00, 56.93it/s]
Test set:  Avg loss: 0.447, Accuracy: 8768/10000 (87.7%)

Completed in  11.24s</pre>
<div style="text-align: left"><embed src="https://info-arena.github.io/ARENA_img/misc/media-04/0402.html" width="820" height="470"></div>


Note - this training loop (if done correctly) will look to the one we used in earlier sections is that we're using SGD rather than Adam. You can try adapting your Adam code from the previous day's exercises, and get the same results as you have in earlier sections.

If it works then congratulations - you've implemented a fully-functional autograd system!




=== NEW CHAPTER ===


# Bonus


Congratulations on finishing the day's main content! Here are a few more bonus things for you to explore.


### In-Place Operation Warnings

The most severe issue with our current system is that it can silently compute the wrong gradients when in-place operations are used. Have a look at how [PyTorch handles it](https://pytorch.org/docs/stable/notes/autograd.html#in-place-operations-with-autograd) and implement a similar system yourself so that it either computes the right gradients, or raises a warning.


### In-Place `ReLU`

Instead of implementing ReLU in terms of maximum, implement your own forward and backward functions that support `inplace=True`.


### Backward for `einsum`

Write the backward pass for your equivalent of `torch.einsum`.


### Reuse of Module during forward

Consider the following MLP, where the same `nn.ReLU` instance is used twice in the forward pass. Without running the code, explain whether this works correctly or not with reference to the specifics of your implementation.

```python
class MyModule(Module):
    def __init__(self):
        super().__init__()
        self.linear1 = Linear(28*28, 64)
        self.linear2 = Linear(64, 64)
        self.linear3 = Linear(64, 10)
        self.relu = ReLU()
    def forward(self, x):
        x = self.relu(self.linear1(x))
        x = self.relu(self.linear2(x))
        return self.linear3(x)
```

<details>
<summary>Answer (what you should find)</summary>

This implementation will work correctly.

The danger of reusing modules is that you'd be creating a cyclical computational graph (because the same parameters would appear twice), but the `ReLU` module doesn't have any parameters (or any internal state), so this isn't a problem. It's effectively just a wrapper for the `relu` function, and you could replace `self.relu` with applying the `relu` function directly without changing the model's behaviour.

This is slightly different if we're thinking about adding **hooks** to our model. Hooks are functions that are called during the forward or backward pass, and they can be used to inspect the state of the model during training. We generally want each hook to be associated with a single position in the model, rather than being called at two different points.
</details>


### Convolutional layers

Now that you've implemented a linear layer, it should be relatively straightforward to take your convolutions code from day 2 and use it to make a convolutional layer. How much better performance do you get on the MNIST task once you replace your first two linear layers with convolutions?


### ResNet Support

Make a list of the features that would need to be implemented to support ResNet inference, and training. It will probably take too long to do all of them, but pick some interesting features to start implementing.


### Central Difference Checking

Write a function that compares the gradients from your backprop to a central difference method. See [Wikipedia](https://en.wikipedia.org/wiki/Finite_difference) for more details.


### Non-Differentiable Function Support

Your `Tensor` does not currently support equivalents of `torch.all`, `torch.any`, `torch.floor`, `torch.less`, etc. which are non-differentiable functions of Tensors. Implement them so that they are usable in computational graphs, but gradients shouldn't flow through them (their contribution is zero).


### Differentiation wrt Keyword Arguments

In the real PyTorch, you can sometimes pass tensors as keyword arguments and differentiation will work, as in `t.add(other=t.tensor([3,4]), input=t.tensor([1,2]))`. In other similar looking cases like `t.dot`, it raises an error that the argument must be passed positionally. Decide on a desired behavior in your system and implement and test it.


### `torch.stack`

So far we've registered a separate backwards for each input argument that could be a Tensor. This is problematic if the function can take any number of tensors like `torch.stack` or `numpy.stack`. Think of and implement the backward function for stack. It may require modification to your other code.


```

---

## chapter0_fundamentals/instructions/pages/05_[0.5]_VAEs_&_GANs.md

```markdown
# [0.5] - VAEs & GANs


> **Colab: [exercises](https://colab.research.google.com/github/callummcdougall/arena-pragmatic-interp/blob/main/chapter0_fundamentals/exercises/part5_vaes_and_gans/0.5_VAEs_&_GANs_exercises.ipynb?t=20260303) | [solutions](https://colab.research.google.com/github/callummcdougall/arena-pragmatic-interp/blob/main/chapter0_fundamentals/exercises/part5_vaes_and_gans/0.5_VAEs_&_GANs_solutions.ipynb?t=20260303)**

Please send any problems / bugs on the `#errata` channel in the [Slack group](https://join.slack.com/t/arena-uk/shared_invite/zt-3afdmdhye-Mdb3Sv~ss_V_mEaXEbkABA), and ask any questions on the dedicated channels for this chapter of material.

If you want to change to dark mode, you can do this by clicking the three horizontal lines in the top-right, then navigating to Settings → Theme.

Links to all other chapters: [(0) Fundamentals](https://arena-chapter0-fundamentals.streamlit.app/), [(1) Transformer Interpretability](https://arena-chapter1-transformer-interp.streamlit.app/), [(2) RL](https://arena-chapter2-rl.streamlit.app/).

<img src="https://raw.githubusercontent.com/info-arena/ARENA_img/main/misc/headers/header-05.png" width="350">


# Introduction


Today, we're studying two important classes of generative image models: **Generative Adversarial Networks (GANs)** and **Variational Autoencoders (VAEs)**. Although these generally aren't SOTA any more (thanks in part to the rise of diffusion models), there are some deep conceptual insights which can be gleaned from studying these models (VAEs in particular) which help lay the groundwork for more advanced models.

These exercises will also hopefully bring much of this chapter full-circle:

* We'll cover transposed convolutions, which will serve as a refresher on some of the ideas behind convolutions **(day 2: CNNs & ResNets)**
* We'll be assembling NNet architectures from scratch, like in the ResNets exercises **(day 2: CNNs & ResNets)**
* We'll work with different loss functions, and think intuitively about what it means to optimize them **(day 3: Optimization & Hyperparameters)**
* We'll be working with `wandb`, and will learn how to log outputs produced by our models **(day 3: Optimization & Hyperparameters)**
* We'll have to think carefully about how gradient propagation works between different parts of our model **(day 4: Backpropagation)**

Note, many of today's exercises (especially those involving building models & writing forward pass functions) don't have as rigorous unit tests as previous days of content. Part of this is because the design spec for these models is less strict (we're not copying over weights from a pretrained model like last time, all that matters is that our model actually trains correctly, and so small changes to the solution architecture can sometimes be allowed). However, another part is that we're trying to move participants away from being too reliant on unit tests, and towards being able to independently reason through exercises or replications given just a description of the task or a paper implementation to follow. This is an invaluable skill to develop for any aspiring ML practitioner!

For a lecture on the material today, which provides some high-level understanding before you dive into the material, watch the video below:

<iframe width="540" height="304" src="https://www.youtube.com/embed/NWbtTogKcXg" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


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
                
<img src="https://raw.githubusercontent.com/info-arena/ARENA_img/main/misc/gan-last-output.png" width="1100">

> ##### Learning Objectives
>
> - Understand the loss function used in GANs, and why it can be expected to result in the generator producing realistic outputs.
> - Implement the DCGAN architecture from the paper, with relatively minimal guidance.
> - Learn how to identify and fix bugs in your GAN architecture, to improve convergence properties.


### 3️⃣ Bonus - Transposed Convolutions

In this section, you'll implement the transposed convolution operation manually. This is similar to a regular convolution, but designed for upsampling rather than downsampling (i.e. producing an image from a latent vector rather producing output from an image). These are very important in many generative algorithms. Once you implement this, you'll be able to build your own GANs and VAEs from scratch, without using any pre-built layers.

*Note - the bonus section from the CNNs day is a prerequisite for these bonus exercises. If you haven't completed that section, you'll need to do so before attempting these.*

> ##### Learning Objectives
>
> - Learn about & implement the transposed convolution operation.
> - Implement GANs and/or VAEs entirely from scratch.


## Setup code


```python
import os
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Literal

import einops
import torch as t
import torchinfo
import wandb
from datasets import load_dataset
from einops.layers.torch import Rearrange
from jaxtyping import Float
from torch import Tensor, nn
from torch.utils.data import DataLoader, Dataset, Subset
from torchvision import datasets, transforms
from tqdm import tqdm

# Make sure exercises are in the path
chapter = "chapter0_fundamentals"
section = "part5_vaes_and_gans"
root_dir = next(p for p in Path.cwd().parents if (p / chapter).exists())
exercises_dir = root_dir / chapter / "exercises"
section_dir = exercises_dir / section
if str(exercises_dir) not in sys.path:
    sys.path.append(str(exercises_dir))

MAIN = __name__ == "__main__"

import part5_vaes_and_gans.tests as tests
import part5_vaes_and_gans.utils as utils
from plotly_utils import imshow

device = t.device("mps" if t.backends.mps.is_available() else "cuda" if t.cuda.is_available() else "cpu")
```




=== NEW CHAPTER ===


# 1️⃣ Autoencoders & VAEs



> ##### Learning Objectives
>
> - Learn about the transposed convolution operation
> - Understand the basic architecture of autoencoders and VAEs
> - Learn about the reparameterization trick for VAEs
> - Implement your own autoencoder
> - Implement your own VAE, and use it to generate realistic MNIST images
> - (optional) Dive deeper into the mathematical underpinnings of VAEs, and learn about the ELBO loss function

## Reading

**Note** - before you start the reading, you might want to run the first block of code in the "Loading data" section, because it can take a few minutes to run.

* [Understanding VAEs (Medium)](https://medium.com/towards-data-science/understanding-variational-autoencoders-vaes-f70510919f73)
    * A clear and accessible explanation of autoencoders and VAEs.
    * You can stop at "Mathematical details of VAEs"; we'll (optionally) cover this in more detail later.
* [Six (and a half) intuitions for KL divergence](https://www.lesswrong.com/posts/no5jDTut5Byjqb4j5/six-and-a-half-intuitions-for-kl-divergence)
    * Optional reading.
    * KL divergence is an important concept in VAEs (and will continue to be a useful concept for the rest of this course).
* [From Autoencoder to Beta-VAE](https://lilianweng.github.io/posts/2018-08-12-vae/)
    * Optional reading.
    * This is a more in-depth look at VAEs, the maths behind them, and different architecture variants.
* [Transposed Convolutions explained with… MS Excel!](https://medium.com/apache-mxnet/transposed-convolutions-explained-with-ms-excel-52d13030c7e8) (optional)
    * Optional reading.
    * The first part (up to the highlighted comment) is most valuable, since understanding transposed convolutions at a high level is more important than understanding the exact low-level operations that go into them (that's what the bonus is for!).
    * [These visualisations](https://github.com/vdumoulin/conv_arithmetic/blob/master/README.md) may also help.


## Loading data

In these exercises, we'll be using either the Celeb-A dataset or the MNIST dataset. For convenience, we'll include a few functions here to load that data in.

You should already be familiar with MNIST. You can read about the Celeb-A dataset [here](https://mmlab.ie.cuhk.edu.hk/projects/CelebA.html) - essentially it's a large-scale face attributes dataset with more than 200k celebrity images, but we'll only be taking the images from this dataset rather the classifications. Run the code below to download the data from HuggingFace, and save it in your filesystem as images.

The code should take 4-15 minutes to run in total, but feel free to move on if it's taking longer (you'll mostly be using MNIST in this section, and only using Celeb-A when you move on to GANs).


```python
celeb_data_dir = section_dir / "data/celeba"
celeb_image_dir = celeb_data_dir / "img_align_celeba"

os.makedirs(celeb_image_dir, exist_ok=True)

if len(list(celeb_image_dir.glob("*.jpg"))) > 0:
    print("Dataset already loaded.")
else:
    dataset = load_dataset("nielsr/CelebA-faces")
    print("Dataset loaded.")

    for idx, item in tqdm(enumerate(dataset["train"]), total=len(dataset["train"]), desc="Saving imgs...", ascii=True):
        # The image is already a JpegImageFile, so we can directly save it
        item["image"].save(celeb_image_dir / f"{idx:06}.jpg")

    print("All images have been saved.")
```


<details>
<summary>Note on why we double-nest our saving paths, i.e. <code>celeba/img_align_celeba</code></summary>

In the code above, each image is saved in the format `'data/celeba/img_align_celeba/000001.jpg'`, etc. The reason for this double nesting (rather than e.g. `data/celeba/000001.jpg`) is that the child folders represent the image classes. If we were training a classifier, we'd have multiple folders within `data/celeba`, with each one being a different class. In this dataset, we only have one class (real celeb images), so we only need one child folder.

</details>

Now, here's some code to load in either the Celeb-A or MNIST data. It also applies transformations to the data, to get it into the right input format for us.

The function below allows you to load in either the Celeb-A or MNIST data.


```python
def get_dataset(dataset: Literal["MNIST", "CELEB"], train: bool = True) -> Dataset:
    assert dataset in ["MNIST", "CELEB"]

    if dataset == "CELEB":
        image_size = 64
        assert train, "CelebA dataset only has a training set"
        transform = transforms.Compose(
            [
                transforms.Resize(image_size),
                transforms.CenterCrop(image_size),
                transforms.ToTensor(),
                transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),
            ]
        )
        trainset = datasets.ImageFolder(root=exercises_dir / "part5_vaes_and_gans/data/celeba", transform=transform)

    elif dataset == "MNIST":
        img_size = 28
        transform = transforms.Compose(
            [
                transforms.Resize(img_size),
                transforms.ToTensor(),
                transforms.Normalize((0.1307,), (0.3081,)),
            ]
        )
        trainset = datasets.MNIST(
            root=exercises_dir / "part5_vaes_and_gans/data",
            transform=transform,
            download=True,
            train=train,
        )

    return trainset
```


We've also given you some code for visualising your data. You should run this code to make sure your data is correctly loaded in.


```python
def display_data(x: Tensor, nrows: int, title: str):
    """Displays a batch of data, using plotly."""
    ncols = x.shape[0] // nrows
    # Reshape into the right shape for plotting (make it 2D if image is monochrome)
    y = einops.rearrange(x, "(b1 b2) c h w -> (b1 h) (b2 w) c", b1=nrows).squeeze()
    # Normalize in the 0-1 range, then map to integer type
    y = (y - y.min()) / (y.max() - y.min())
    y = (y * 255).to(dtype=t.uint8)
    # Display data
    imshow(
        y,
        binary_string=(y.ndim == 2),
        height=50 * (nrows + 4),
        width=50 * (ncols + 5),
        title=f"{title}<br>single input shape = {x[0].shape}",
    )


trainset_mnist = get_dataset("MNIST")
trainset_celeb = get_dataset("CELEB")

# Display MNIST
x = next(iter(DataLoader(trainset_mnist, batch_size=25)))[0]
display_data(x, nrows=5, title="MNIST data")

# Display CelebA
x = next(iter(DataLoader(trainset_celeb, batch_size=25)))[0]
display_data(x, nrows=5, title="CelebA data")
```


<div style="text-align: left"><embed src="https://info-arena.github.io/ARENA_img/misc/media-05/0501-A.html" width="520" height="490"></div>
<div style="text-align: left"><embed src="https://info-arena.github.io/ARENA_img/misc/media-05/0501-B.html" width="520" height="490"></div>


### Holdout data

Lastly, we'll also get some **holdout data** that we can use during training. The tensor below has shape `(10, 1, 28, 28)`, and contains a single image from each of the 10 MNIST classes. We do this because we want to monitor our autoencoder's reconstructions for each different image type while it trains. We might find that some images are reconstructed better than others!


```python
testset = get_dataset("MNIST", train=False)
HOLDOUT_DATA = dict()
for data, target in DataLoader(testset, batch_size=1):
    if target.item() not in HOLDOUT_DATA:
        HOLDOUT_DATA[target.item()] = data.squeeze()
        if len(HOLDOUT_DATA) == 10:
            break
HOLDOUT_DATA = t.stack([HOLDOUT_DATA[i] for i in range(10)]).to(dtype=t.float, device=device).unsqueeze(1)

display_data(HOLDOUT_DATA, nrows=1, title="MNIST holdout data")
```


<div style="text-align: left"><embed src="https://info-arena.github.io/ARENA_img/misc/media-05/0502.html" width="770" height="270"></div>


You might be wondering why we do this, rather than just e.g. generating some random noise and seeing what the decoder's reconstruction is. The answer is that **our autoencoder's latent space might not be meaningful**. In other words, it's unclear exactly how to sample from it to get output which will look like an MNIST image. We'll return to this idea when we study VAEs later in these exercises.

*For the rest of this section (not including the bonus), we'll assume we're working with the MNIST dataset rather than Celeb-A.*


## Transposed Convolutions

**What are transposed convolutions, and why should we care about them?** One high-level intuition goes something like this: most of the generator's architecture is basically the discriminator architecture in reverse. We need something that performs the reverse of a convolution - not literally the inverse operation, but something reverse in spirit, which uses a kernel of weights to project up to some array of larger size.

**Importantly, a transposed convolution isn't literally the inverse of a convolution**. A lot of confusion can come from misunderstanding this!

You can describe the difference between convolutions and transposed convolutions as follows:

* In convolutions, you slide the kernel around inside the input. At each position of the kernel, you take a sumproduct between the kernel and that section of the input to calculate a single element in the output.
* In transposed convolutions, you slide the kernel around what will eventually be your output, and at each position you add some multiple of the kernel to your output.

Below is an illustration of both for comparison, in the 1D case (where $*$ stands for the 1D convolution operator, and $*^T$ stands for the transposed convolution operator). Note the difference in size between the output in both cases. With standard convolutions, our output is smaller than our input, because we're having to fit the kernel inside the input in order to produce the output. But in our transposed convolutions, the output is actually larger than the input, because we're fitting the kernel inside the output.

<img src="https://raw.githubusercontent.com/info-arena/ARENA_img/main/misc/convtranspose-1.png" width="700">

We won't actually have you implement the transposed convolution operation in these exercises; instead we've pushed it to the bonus section. For now, you can just use the `ConvTranspose2d` module which has already been imported for you from today's solutions file, in place of your own implementation. You can use it exactly the same way you use normal convolutional layers: for instance `ConvTranspose2d(32, 16, 4, stride=2, padding=1)` will define a convolution layer that maps a tensor from `(batch_size, in_channels=32, height, width)` up to shape `(batch_size, out_channels=16, height * 2, width * 2)`.

[These visualisations](https://github.com/vdumoulin/conv_arithmetic/blob/master/README.md) (linked in the reading material) may also help build intuition for the transposed convolution module.


## Autoencoders

We'll start by looking at **Autoencoders**, which are much conceptually simpler than VAEs. These are simply systems which learn a compressed representation of the input, and then reconstruct it. There are two parts to this:

* The **encoder** learns to compress the output into a latent space which is lower-dimensional than the original image.
* The **decoder** learns to uncompress the encoder's output back into a faithful representation of the original image.

<img src="https://raw.githubusercontent.com/info-arena/ARENA_img/main/misc/gan_images/ae-diagram-l.png" width="700">
                
Our loss function is simply some metric of the distance between the input and the reconstructed input, e.g. the $l_2$ loss.

You'll start by writing your own autoencoder. We've given some guidance on architecture below, although in general because we're working with a fairly simple dataset (MNIST) and a fairly robust architecture (at least compared to GANs in the next section!), you model is still likely to work well even if it deviates slightly from the specification we'll give below.


### Exercise - implement autoencoder

> ```yaml
> Difficulty: 🔴🔴🔴⚪⚪
> Importance: 🔵🔵🔵🔵⚪
> 
> You should spend up to 15-30 minutes on this exercise.
> ```

*Note - for the rest of this section (not including the bonus), we'll assume we're working with the MNIST dataset rather than Celeb-A.*

Your encoder should consist of two convolutional blocks (i.e. convolution plus ReLU), followed by two fully connected linear layers with a ReLU in between them. Both convolutions will have kernel size 4, stride 2, padding 1 (recall this halves the size of the image). We'll have 16 and 32 output channels respectively.

The decoder will be the exact mirror image of the encoder (with convolutions replaced by transposed convolutions).

The only free parameters in your implementation will be `latent_dim_size` and `hidden_dim_size`. The former determines the size of the latent space (otherwise called the bottleneck dimension) between the encoder and decoder, and the latter determines the size of the final linear layer we insert just before the end / just after the start of the encoder / decoder's architecture respectively.

<img src="https://raw.githubusercontent.com/info-arena/ARENA_img/main/misc/gan_images/ae-help-10.png" width="1100">

A few extra notes:

* You'll need to reshape between the convolutional blocks and linear layers. For this, you might find the `einops` library helpful - they have a function `einops.layers.torch.Rearrange` (imported for you as `Rearrange`) which works like the standard einops function, except that it takes a string and returns a module which performs the corresponding rearrangement. Just like any other module, it can be used inside things like `Sequential` (this way, the logic inside the `forward` method can be very simple!).

```python
>>> x = t.randn(100, 3, 4, 5)
>>> x.shape
torch.Size([100, 3, 4, 5])

>>> module = Rearrange("b c h w -> b (c h w)")
>>> module(x).shape
torch.Size([100, 60])
```

* Note that we don't include a ReLU in the very last layer of the decoder or generator, we only include them ***between successive convolutions or linear layers*** - can you see why it wouldn't make sense to put ReLUs at the end?
* The convolutions don't have biases, although we have included biases in the linear layers (this will be important if you want your parameter count to match the solution, but not really that important for good performance).

Now, implement your autoencoder below. We recommend you define `encoder` and `decoder` to help make your code run with the functions we've written for you later.

<!-- You can test your answer by comparing the architecture to the solution directly. As this course goes on, we won't always include test functions as the exercises get a bit more open-ended and solutions to them are likely to vary more; it's also good practice to find ways to test your answers when you don't have access to black-box tests that you can trust!

from part5_vaes_and_gans.solutions import Autoencoder as SolutionAutoencoder

if MAIN:
    soln_Autoencoder = SolutionAutoencoder(latent_dim_size=5, hidden_dim_size=128)
    my_Autoencoder = Autoencoder(latent_dim_size=5, hidden_dim_size=128)

    print_param_count(my_Autoencoder, soln_Autoencoder)
    # print_param_count(my_Autoencoder, soln_Autoencoder, filename=str(section_dir / "0503.html"))

<iframe src="https://info-arena.github.io/ARENA_img/misc/media-05/0503.html" width="920" height="470"></iframe> -->


```python
# Importing all modules you'll need, from previous solutions (you're encouraged to substitute your
# own implementations instead, if you want to!)
from part2_cnns.solutions import BatchNorm2d, Conv2d, Linear, ReLU, Sequential

from part5_vaes_and_gans.solutions import ConvTranspose2d


class Autoencoder(nn.Module):
    def __init__(self, latent_dim_size: int, hidden_dim_size: int):
        """Creates the encoder & decoder modules."""
        super().__init__()
        self.encoder = ...
        self.decoder = ...

    def forward(self, x: Tensor) -> Tensor:
        """Returns the reconstruction of the input, after mapping through encoder & decoder."""
        raise NotImplementedError()


tests.test_autoencoder(Autoencoder)
```


<details><summary>Solution</summary>

```python
class Autoencoder(nn.Module):
    def __init__(self, latent_dim_size: int, hidden_dim_size: int):
        """Creates the encoder & decoder modules."""
        super().__init__()
        self.latent_dim_size = latent_dim_size
        self.hidden_dim_size = hidden_dim_size
        self.encoder = Sequential(
            Conv2d(1, 16, 4, stride=2, padding=1),
            ReLU(),
            Conv2d(16, 32, 4, stride=2, padding=1),
            ReLU(),
            Rearrange("b c h w -> b (c h w)"),
            Linear(7 * 7 * 32, hidden_dim_size),
            ReLU(),
            Linear(hidden_dim_size, latent_dim_size),
        )
        self.decoder = nn.Sequential(
            Linear(latent_dim_size, hidden_dim_size),
            ReLU(),
            Linear(hidden_dim_size, 7 * 7 * 32),
            ReLU(),
            Rearrange("b (c h w) -> b c h w", c=32, h=7, w=7),
            ConvTranspose2d(32, 16, 4, stride=2, padding=1),
            ReLU(),
            ConvTranspose2d(16, 1, 4, stride=2, padding=1),
        )

    def forward(self, x: Tensor) -> Tensor:
        """Returns the reconstruction of the input, after mapping through encoder & decoder."""
        z = self.encoder(x)
        x_prime = self.decoder(z)
        return x_prime
```
</details>


## Training your Autoencoder

Once you've got the architecture right, you should write a training loop which works with [MSE loss](https://pytorch.org/docs/stable/generated/torch.nn.MSELoss.html) between the original and reconstructed data. The standard Adam optimiser with default parameters should suffice.


### Logging images to `wandb`

Weights and biases provides a nice feature allowing you to log images! This requires you to use the function `wandb.Image`. The first argument is `data_or_path`, which can be any of the following:

* A numpy array in shape `(height, width)` or `(height, width, 1)` -> interpreted as monochrome image
* A numpy array in shape `(height, width, 3)` -> interpreted as RGB image
* A PIL image (can be RGB or monochrome)

When it comes to logging, you can log a list of images rather than a single image. Example code, and the output it produces from my GAN (you'll create output like this in the next section!):

```python
# arr is a numpy array of shape (8, 28, 28, 3), i.e. it's an array of 8 RGB images
images = [wandb.Image(a) for a in arr]
wandb.log({"images": images}, step=self.step)
```

<img src="https://raw.githubusercontent.com/info-arena/ARENA_img/main/misc/gan_images/gan_output_2.png" width="750">


### Exercise - write autoencoder training loop

> ```yaml
> Difficulty: 🔴🔴🔴🔴⚪
> Importance: 🔵🔵🔵🔵⚪
> 
> You should spend up to 20-35 minutes on this exercise.
> ```

You should now implement your training loop below. We've filled in some methods for you (and have given you a dataclass to hold arguments), your job is to complete `training_step` and `train`. The former should perform a single training step by optimizing against the reconstruction loss between the image and target (you might find `nn.MSELoss` suitable for this). The latter should be structured like training code you might have seen before, in other words:

- Iterate over `self.args.epochs` epochs
- For each epoch, you should:
    - Iterate over the training data and perform a training step for each batch. We also recommend using & updating a progress bar, and logging to wandb if this is enabled in your training arguments.
    - Evaluate the model on the holdout data via `self.log_samples()`, every `args.log_every_n_steps` total steps.

Some last tips before we get started:

- Don't use wandb until you've ironed out the bugs in your code, and loss seems to be going down based on the in-notebook logging. This is why we've given you the `use_wandb` argument in your dataclass.
- Remember to increment `self.step` as you train (this is necessary if you're passing this argument to `wandb.log`). Note we're using `step` here rather than `examples_seen` like in earlier exercises, because it'll prove more useful for our purposes.
- Your wandb logging should take place in `training_step` not `train` (this is better practice in general because often there will be variables only defined in the scope of `training_step` that you might want to log - even though that's not the case here, it will be later).
- Iterating through `self.trainloader` will give you tuples of `(img, label)`, but you don't need to use the labels - all you need is the image.



```python
@dataclass
class AutoencoderArgs:
    # architecture
    latent_dim_size: int = 5
    hidden_dim_size: int = 128

    # data / training
    dataset: Literal["MNIST", "CELEB"] = "MNIST"
    batch_size: int = 512
    epochs: int = 10
    lr: float = 1e-3
    betas: tuple[float, float] = (0.5, 0.999)

    # logging
    use_wandb: bool = True
    wandb_project: str | None = "day5-autoencoder"
    wandb_name: str | None = None
    log_every_n_steps: int = 250


class AutoencoderTrainer:
    def __init__(self, args: AutoencoderArgs):
        self.args = args
        self.trainset = get_dataset(args.dataset)
        self.trainloader = DataLoader(self.trainset, batch_size=args.batch_size, shuffle=True)
        self.model = Autoencoder(
            latent_dim_size=args.latent_dim_size,
            hidden_dim_size=args.hidden_dim_size,
        ).to(device)
        self.optimizer = t.optim.Adam(self.model.parameters(), lr=args.lr, betas=args.betas)

    def training_step(self, img: Tensor) -> Tensor:
        """
        Performs a training step on the batch of images in `img`. Returns the loss. Logs to wandb
        if enabled.
        """
        raise NotImplementedError()

    @t.inference_mode()
    def log_samples(self) -> None:
        """
        Evaluates model on holdout data, either logging to weights & biases or displaying output.
        """
        assert self.step > 0, "First call should come after a training step. Remember to increment `self.step`."
        output = self.model(HOLDOUT_DATA)
        if self.args.use_wandb:
            output = (output - output.min()) / (output.max() - output.min())  # Normalize to [0, 1]
            output = (output * 255).to(dtype=t.uint8)  # Convert to uint8 for logging
            wandb.log({"images": [wandb.Image(arr) for arr in output.cpu().numpy()]}, step=self.step)
        else:
            display_data(t.concat([HOLDOUT_DATA, output]), nrows=2, title="AE reconstructions")

    def train(self) -> Autoencoder:
        """Performs a full training run."""
        self.step = 0
        if self.args.use_wandb:
            wandb.init(project=self.args.wandb_project, name=self.args.wandb_name)
            wandb.watch(self.model)

        # YOUR CODE HERE - iterate over epochs, and train your model

        if self.args.use_wandb:
            wandb.finish()

        return self.model


args = AutoencoderArgs(use_wandb=False)
trainer = AutoencoderTrainer(args)
autoencoder = trainer.train()
```


<details><summary>Solution</summary>

```python
class AutoencoderTrainer:
    def __init__(self, args: AutoencoderArgs):
        self.args = args
        self.trainset = get_dataset(args.dataset)
        self.trainloader = DataLoader(self.trainset, batch_size=args.batch_size, shuffle=True)
        self.model = Autoencoder(
            latent_dim_size=args.latent_dim_size,
            hidden_dim_size=args.hidden_dim_size,
        ).to(device)
        self.optimizer = t.optim.Adam(self.model.parameters(), lr=args.lr, betas=args.betas)

    def training_step(self, img: Tensor) -> Tensor:
        """
        Performs a training step on the batch of images in `img`. Returns the loss. Logs to wandb
        if enabled.
        """
        # Compute loss, backprop on it, and perform an optimizer step
        img_reconstructed = self.model(img)
        loss = nn.MSELoss()(img, img_reconstructed)
        loss.backward()
        self.optimizer.step()
        self.optimizer.zero_grad()

        # Increment step counter and log to wandb if enabled
        self.step += img.shape[0]
        if self.args.use_wandb:
            wandb.log(dict(loss=loss), step=self.step)

        return loss

    @t.inference_mode()
    def log_samples(self) -> None:
        """
        Evaluates model on holdout data, either logging to weights & biases or displaying output.
        """
        assert self.step > 0, "First call should come after a training step. Remember to increment `self.step`."
        output = self.model(HOLDOUT_DATA)
        if self.args.use_wandb:
            output = (output - output.min()) / (output.max() - output.min())  # Normalize to [0, 1]
            output = (output * 255).to(dtype=t.uint8)  # Convert to uint8 for logging
            wandb.log({"images": [wandb.Image(arr) for arr in output.cpu().numpy()]}, step=self.step)
        else:
            display_data(t.concat([HOLDOUT_DATA, output]), nrows=2, title="AE reconstructions")

    def train(self) -> Autoencoder:
        """Performs a full training run."""
        self.step = 0
        if self.args.use_wandb:
            wandb.init(project=self.args.wandb_project, name=self.args.wandb_name)
            wandb.watch(self.model)

        for epoch in range(self.args.epochs):
            # Iterate over training data, performing a training step for each batch
            progress_bar = tqdm(self.trainloader, total=int(len(self.trainloader)), ascii=True)
            for img, label in progress_bar:  # remember that label is not used
                img = img.to(device)
                loss = self.training_step(img)
                progress_bar.set_description(f"{epoch=:02d}, {loss=:.4f}, step={self.step:05d}")
                if self.step % self.args.log_every_n_steps == 0:
                    self.log_samples()


        if self.args.use_wandb:
            wandb.finish()

        return self.model
```
</details>


After the first epoch, you should be able to get output of the following quality:

<br>
<img src="https://raw.githubusercontent.com/info-arena/ARENA_img/main/misc/ae-epoch-1.png" width="750">

And by the 10th epoch, you should be getting something like this:

<br>
<img src="https://raw.githubusercontent.com/info-arena/ARENA_img/main/misc/ae-epoch-10.png" width="750">

Note how the reconstructions it's mixing up features for some of the numbers - for instance, the 5 seems to have been partly reconstructed as a 3. But overall, it seems pretty accurate!


## Latent space of an autoencoder

We'll now return to the issue we mentioned briefly earlier - how to generate output? We might want to generate output by just producing random noise and passing it through our decoder, but this raises a question - how should we interpret the latent space between our encoder and decoder?

We can try and plot the outputs produced by the decoder over a range. The code below does this (you might have to adjust it slightly depending on how you've implemented your autoencoder):


```python
def create_grid_of_latents(
    model, interpolation_range=(-1, 1), n_points=11, dims=(0, 1)
) -> Float[Tensor, "rows_x_cols latent_dims"]:
    """Create a tensor of zeros which varies along the 2 specified dimensions of the latent space."""
    grid_latent = t.zeros(n_points, n_points, model.latent_dim_size, device=device)
    x = t.linspace(*interpolation_range, n_points)
    grid_latent[..., dims[0]] = x.unsqueeze(-1)  # rows vary over dim=0
    grid_latent[..., dims[1]] = x  # cols vary over dim=1
    return grid_latent.flatten(0, 1)  # flatten over (rows, cols) into a single batch dimension


grid_latent = create_grid_of_latents(autoencoder, interpolation_range=(-3, 3))

# Map grid latent through the decoder
output = autoencoder.decoder(grid_latent)

# Visualize the output
utils.visualise_output(output, grid_latent, title="Autoencoder latent space visualization")
```


<details><summary>Click to see the expected output</summary>

<div style="text-align: left"><embed src="https://info-arena.github.io/ARENA_img/misc/media-05/0504.html" width="670" height="620"></div>

</details>


This code generates images from a vector in the latent space which is zero in all directions, except for the first two dimensions. (Note, we normalize with `(0.3081, 0.1307)` in the code above because this is the mean and standard deviation of the MNIST dataset - see discussion [here](https://discuss.pytorch.org/t/normalization-in-the-mnist-example/457).)

This is ... pretty underwhelming. Some of these shapes seem legible in some regions (e.g. in the demo example on Streamlit we have some patchy but still recognisable 9s, 3s, 0s and 4s in the corners of the latent space), but a lot of the space doesn't look like any recognisable number. For example, much of the middle region is just an unrecognisable blob. Using the default interpolation range of `(-1, 1)` makes things look even worse. And this is a problem, since our goal is to be able to randomly sample points inside this latent space and use them to generate output which resembles the MNIST dataset - this is our true goal, not accurate reconstruction.

Why does this happen? Well unfortunately, the model has no reason to treat the latent space in any meaningful way. It might be the case that almost all the images are embedded into a particular subspace of the latent space, and so the encoder only gets trained on inputs in this subspace. To further illustrate this, the code below feeds MNIST data into your encoder, and plots the resulting latent vectors (projected along the first two latent dimensions). Note that there are some very high-density spots, and other much lower-density spots. So it stands to reason that we shouldn't expect the decoder to be able to produce good output for all points in the latent space (especially when we're using a 5-dimensional latent space rather than just 2-dimensional as visualised below - we can imagine that 5D latent space would have significantly more "dead space").

To emphasise, we're not looking for a crisp separation of digits here. We're only plotting 2 of 5 dimensions, it would be a coincidence if they were cleanly separated. We're looking for efficient use of the space, because this is likely to lead to an effective generator when taken out of the context of the discriminator. We don't really see that here.


```python
# Get a small dataset with 5000 points
small_dataset = Subset(get_dataset("MNIST"), indices=range(0, 5000))
imgs = t.stack([img for img, label in small_dataset]).to(device)
labels = t.tensor([label for img, label in small_dataset]).to(device).int()

# Get the latent vectors for this data along first 2 dims, plus for the holdout data
latent_vectors = autoencoder.encoder(imgs)[:, :2]
holdout_latent_vectors = autoencoder.encoder(HOLDOUT_DATA)[:, :2]

# Plot the results
utils.visualise_input(latent_vectors, labels, holdout_latent_vectors, HOLDOUT_DATA)
```


<details><summary>Click to see the expected output</summary>

<div style="text-align: left"><embed src="https://info-arena.github.io/ARENA_img/misc/media-05/0505.html" width="720" height="720"></div>

</details>


## Variational Autoencoders

Variational autoencoders try and solve the problem posed by autoencoders: how to actually make the latent space meaningful, such that you can generate output by feeding a $N(0, 1)$ random vector into your model's decoder?

The key perspective shift is this: **rather than mapping the input into a fixed vector, we map it into a distribution**. The way we learn a distribution is very similar to the way we learn our fixed inputs for the autoencoder, i.e. we have a bunch of linear or convolutional layers, our input is the original image, and our output is the tuple of parameters $(\mu(\boldsymbol{x}), \Sigma(\boldsymbol{x}))$ (as a trivial example, our VAE learning a distribution $\mu(\boldsymbol{x})=z(\boldsymbol{x})$, $\Sigma(\boldsymbol{x})=0$ is equivalent to our autoencoder learning the function $z(\boldsymbol{x})$ as its encoder).

From this [TowardsDataScience](https://towardsdatascience.com/understanding-variational-autoencoders-vaes-f70510919f73) article:

> Due to overfitting, the latent space of an autoencoder can be extremely irregular (close points in latent space can give very *different* decoded data, some point of the latent space can give *meaningless* content once decoded) and, so, we can’t really define a *generative* process that simply consists to sample a point from the *latent space* and make it go through the decoder to get new data. *Variational autoencoders* (VAEs) are autoencoders that tackle the problem of the latent space irregularity by making the encoder return a *distribution over the latent space* instead of a single point and by adding in the loss function a *regularisation* term over that returned distribution in order to ensure a better *organisation* of the latent space.

Or, in fewer words:

> **A variational autoencoder can be defined as being an autoencoder whose training is regularised to avoid overfitting and ensure that the latent space has good properties that enable generative process.**

At first, this idea of mapping to a distribution sounds like a crazy hack - why on earth does it work? This diagram should help convey some of the intuitions:

<img src="https://raw.githubusercontent.com/info-arena/ARENA_img/main/misc/vae-scatter-one.png" width="800">

With our encoder, there was nothing incentivising us to make full and meaningful use of the latent space. It's hypothetically possible that our network was mapping all the inputs to some very small subspace and reconstructing them with perfect fidelity. This wouldn't have required numbers with different features to be far apart from each other in the latent space, because even if they are close together no information is lost. See the first image above.

But with our variational autoencoder, each MNIST image produces a **sample** from the latent space, with a certain mean and variance. This means that, when two numbers look very different, their latent vectors are forced apart - if the means were close together then the decoder wouldn't be able to reconstruct them.

Another nice property of using random latent vectors is that the entire latent space will be meaningful. For instance, with autoencoders there is no reason why we should expect the linear interpolation between two points in the latent space to have meaningful decodings. The decoder output *will* change continuously as we continuously vary the latent vector, but that's about all we can say about it. However, if we use a variational autoencoder, we don't have this problem. The output of a linear interpolation between the cluster of $2$s and cluster of $7$s will be ***"a symbol which pattern-matches to the family of MNIST digits, but has equal probability to be interpreted as a $2$ or a $7$"***, and this is indeed what we find.

<img src="https://raw.githubusercontent.com/info-arena/ARENA_img/main/misc/vae-scatter-two.png" width="700">


### Reparameterisation trick

One question that might have occurred to you - how can we perform backward passes through our network? We know how to differentiate with respect to the inputs to a function, but how can we differentiate wrt the parameters of a probability distribution from which we sample our vector? The solution is to convert our random sampling into a function, by introducing an extra parameter $\epsilon$. We sample $\epsilon$ from the standard normal distribution, and then express $\boldsymbol{z}$ as a deterministic function of $\mu$, $\sigma$ and $\epsilon$:

$$
z = \mu + \sigma \odot \epsilon
$$

where $\odot$ is a notation meaning pointwise product, i.e. $z_i = \mu_i + \sigma_i \epsilon_i$. Intuitively, we can think of this as follows: when there is randomness in the process that generates the output, there is also randomness in the derivative of the output wrt the input, so **we can get a value for the derivative by sampling from this random distribution**. If we average over enough samples, this will give us a valid gradient for training.

<img src="https://raw.githubusercontent.com/info-arena/ARENA_img/main/misc/gan_images/vae-reparam-l.png" width="800">

Note that if we have $\sigma_\theta(\boldsymbol{x})=0$ for all $\boldsymbol{x}$, the VAE reduces to an autoencoder (since the latent vector $z = \mu_\theta(\boldsymbol{x})$ is once again a deterministic function of $\boldsymbol{x}$). This is why it's important to add a KL-divergence term to the loss function, to make sure this doesn't happen. It's also why, if you print out the average value of $\sigma(\boldsymbol{x})$ while training, you'll probably see it stay below 1 (it's being pulled towards 1 by the KL-divergence loss, **and** pulled towards 0 by the reconstruction loss).

---

Before you move on to implementation details, there are a few questions below designed to test your understanding. They are based on material from this section, as well as the [KL divergence LessWrong post](https://www.lesswrong.com/posts/no5jDTut5Byjqb4j5/six-and-a-half-intuitions-for-kl-divergence). You might also find [this post](https://lilianweng.github.io/posts/2018-08-12-vae/#vae-variational-autoencoder) on VAEs from the readings helpful.

<details>
<summary>State in your own words why we need the reparameterization trick in order to train our network.</summary>

The following would work:

We can't backpropagate through random processes like $z_i \sim N(\mu_i(\boldsymbol{x}), \sigma_i(\boldsymbol{x})^2)$, but if we instead write $\boldsymbol{z}$ as a deterministic function of $\mu_i(\boldsymbol{x})$ and $\sigma_i(\boldsymbol{x})$ with the randomness coming from some some auxiliary random variable $\epsilon$, then we can differentiate our loss function wrt the inputs, and train our network.

<!-- Our encoder works by generating parameters and then using those parameters to sample latent vectors $\boldsymbol{z}$ (i.e. a **stochastic process**). Our decoder is deterministic; it just maps our latent vectors $\boldsymbol{z}$ to fixed outputs $x'$. The stochastic part is the problem; we can't backpropagate gradients through random functions. However, instead of just writing $\boldsymbol{z} \sim N(\mu_\theta(\boldsymbol{x}), \sigma_\theta(\boldsymbol{x})^2I)$, we can write $\boldsymbol{z}$ as a deterministic function of its inputs: $z = g(\theta, x, \epsilon)$, where $\theta$ are the parameters of the distribution, $\boldsymbol{x}$ is the input, and $\epsilon$ is a randomly sampled value. We can then backpropagate through the network. -->

</details>

<details>
<summary>Summarize in one sentence what concept we're capturing when we measure the KL divergence D(P||Q) between two distributions.</summary>

Any of the following would work - $D(P||Q)$ is...

* How much information is lost if the distribution $Q$ is used to represent $P$.
* The quality of $Q$ as a probabilistic model for $P$ (where lower means $Q$ is a better model).
* How close $P$ and $Q$ are, with $P$ as the actual ground truth.
* How much evidence you should expect to get for hypothesis $P$ over $Q$, when $P$ is the actual ground truth.
</details>


## Building a VAE

For your final exercise of this section, you'll build a VAE and run it to produce the same kind of output you did in the previous section. Luckily, this won't require much tweaking from your encoder architecture. The decoder can stay unchanged; there are just two big changes you'll need to make:

### Probabilistic encoder

Rather than your encode outputting a latent vector $\boldsymbol{z}$, it should output a mean $\mu$ and standard deviation $\sigma$; both vectors of dimension `latent_dim_size`. We then sample our latent vector $\boldsymbol{z}$ using $z_i = \mu_i + \sigma_i \cdot \epsilon_i$. Note that this is equivalent to $z = \mu + \Sigma \epsilon$ as shown in the diagram above, but where we assume $\Sigma$ is a diagonal matrix (i.e. the auxiliary random variables $\epsilon$ which we're sampling are independent). This is the most common approach taken in situations like these.

Note - we actually calculate `mu` and `logsigma` rather than `mu` and `sigma` - we get `sigma = logsigma.exp()` from this. This is a more numerically stable method.

How exactly should this work in your model's architecture? You can replace the final linear layer (which previously just gave you the latent vector) with two linear layers returning `mu` and `logsigma`, then you calculate `z` from these (and from a randomly sampled `epsilon`). If you want, you can combine the two linear layers into one linear layer with `out_channels=2*latent_dim_size`, then rearrange to split this up into `mu` and `logsigma` (this is what we do in the solution, and in the diagram below).

You should also return the parameters `mu` and `logsigma` in your VAE's forward function, as well as the final output - the reasons for this will become clear below.

<img src="https://raw.githubusercontent.com/info-arena/ARENA_img/main/misc/ae-before-after-fixed.png" width="750">


### Exercise - build your VAE

> ```yaml
> Difficulty: 🔴🔴🔴⚪⚪
> Importance: 🔵🔵🔵🔵⚪
> 
> You should spend up to 15-25 minutes on this exercise.
> ```

Build your VAE. It should be identical to the autoencoder you built above, except for the changes made at the end of the encoder (outputting mean and std rather than a single latent vector; this latent vector needs to get generated via the reparameterisation trick).

For consistency with code that will come later, we recommend having your `model.encoder` output be of shape `(2, batch_size, latent_dim_size)`, where `output[0]` are the mean vectors $\mu$ and `output[1]` are the log standard deviation vectors $\log \sigma$. The tests below will check this. 

We've also given you a `sample_latent_vector` method - this should return the output of your encoder, but in the form of sampled latent vectors $\mu$ and $\sigma$ rather than the deterministic output `model.encoder(x)` of shape `(2, batch_size, latent_dim_size)`. This will be a useful method for later (and you can use it in your implementation of `forward`).


```python
class VAE(nn.Module):
    encoder: nn.Module
    decoder: nn.Module

    def __init__(self, latent_dim_size: int, hidden_dim_size: int):
        super().__init__()
        self.encoder = ...
        self.decoder = ...

    def sample_latent_vector(self, x: Tensor) -> tuple[Tensor, Tensor, Tensor]:
        """
        Passes `x` through the encoder, returns tuple of (sampled latent vector, mean, log std dev).
        This function can be used in `forward`, but also used on its own to generate samples for
        evaluation.
        """
        raise NotImplementedError()

    def forward(self, x: Tensor) -> tuple[Tensor, Tensor, Tensor]:
        """
        Passes `x` through the encoder and decoder. Returns the reconstructed input, as well as mu
        and logsigma.
        """
        raise NotImplementedError()


tests.test_vae(VAE)
```


<details><summary>Solution</summary>

```python
class VAE(nn.Module):
    encoder: nn.Module
    decoder: nn.Module

    def __init__(self, latent_dim_size: int, hidden_dim_size: int):
        super().__init__()
        self.latent_dim_size = latent_dim_size
        self.hidden_dim_size = hidden_dim_size
        self.encoder = Sequential(
            Conv2d(1, 16, 4, stride=2, padding=1),
            ReLU(),
            Conv2d(16, 32, 4, stride=2, padding=1),
            ReLU(),
            Rearrange("b c h w -> b (c h w)"),
            Linear(7 * 7 * 32, hidden_dim_size),
            ReLU(),
            Linear(hidden_dim_size, latent_dim_size * 2),
            Rearrange("b (n latent_dim) -> n b latent_dim", n=2),  # makes it easier to separate mu and sigma
        )
        self.decoder = nn.Sequential(
            Linear(latent_dim_size, hidden_dim_size),
            ReLU(),
            Linear(hidden_dim_size, 7 * 7 * 32),
            ReLU(),
            Rearrange("b (c h w) -> b c h w", c=32, h=7, w=7),
            ConvTranspose2d(32, 16, 4, stride=2, padding=1),
            ReLU(),
            ConvTranspose2d(16, 1, 4, stride=2, padding=1),
        )

    def sample_latent_vector(self, x: Tensor) -> tuple[Tensor, Tensor, Tensor]:
        """
        Passes `x` through the encoder, returns tuple of (sampled latent vector, mean, log std dev).
        This function can be used in `forward`, but also used on its own to generate samples for
        evaluation.
        """
        mu, logsigma = self.encoder(x)
        sigma = t.exp(logsigma)
        z = mu + sigma * t.randn_like(sigma)
        return z, mu, logsigma

    def forward(self, x: Tensor) -> tuple[Tensor, Tensor, Tensor]:
        """
        Passes `x` through the encoder and decoder. Returns the reconstructed input, as well as mu
        and logsigma.
        """
        z, mu, logsigma = self.sample_latent_vector(x)
        x_prime = self.decoder(z)
        return x_prime, mu, logsigma
```
</details>


You can also do the previous thing (compare your architecture to the solution), but this might be less informative if your model doesn't implement the 2-variables approach in the same way as the solution does.


## New loss function


We're no longer calculating loss simply as the reconstruction error between the original input $\boldsymbol{x}$ and our decoder's output $\boldsymbol{x}'$. Instead, we have a new loss function. For a fixed input $\boldsymbol{x}$, our loss is:

$$
L_{\mathrm{VAE}}(\boldsymbol{x}, \boldsymbol{x}') = \|\boldsymbol{x} - \boldsymbol{x}'\|^2 + D_{\mathrm{KL}}(N(\mu, \sigma^2) || N(0, 1))
$$

The first term is just the regular reconstruction loss we used for our autoencoder. The second term is the KL divergence between the generator's output distribution and the standard normal distribution, and it's designed to penalize the generator for producing latent vectors which are far from the standard normal distribution.

There is a much deeper way to understand this loss function, which also connects to intuitions around diffusion models and other more complicated generative models. For more on this, see the section at the end. For now, we'll move on to the practicalities of implementing this loss function.

The KL divergence of these two distributions has a closed form expression, which is given by:

$$
D_{KL}(N(\mu, \sigma^2) || N(0, 1)) = \frac{\sigma^2 + \mu^2 - 1}{2} - \log{\sigma}
$$

This is why it was important to output `mu` and `logsigma` in our forward functions, so we could compute this expression! (It's easier to use `logsigma` than `sigma` when evaluating the expression above, for stability reasons).

We won't ask you to derive this formula, because it requires understanding of **differential entropy** which is a topic we don't need to get into here. However, it is worth doing some sanity checks, e.g. plot some graphs and convince yourself that this expression is larger as $\mu$ is further away from 0, or $\sigma$ is further away from 1.

(Note that we want our loss term to be a single number. When we calculate the KL divergence, we'll get a vector of `latent_dim`-many KL divergences between the $\mu$ and $\sigma$ of each of our normal distributions. To get our final KL loss penalty, we'll take the mean over this vector.)

<details>
<summary>Derivation of KL divergence result</summary>

If you'd like a derivation, you can find one [here](https://statproofbook.github.io/P/norm-kl), where a slightly more general form of the KL divergence between two normal distributions is derived. Our result is a special case of this, for $\mu_2 = 0$, $\sigma_2^2 = 1$.
In this derivation, they use $\langle \cdot \rangle_{p(x)}$ to denote the expectation of a function under the distribution $p$, i.e. $\langle f(x) \rangle_{p(x)} = \mathbb{E}_{p} [ f(x) ] = \int_{\mathcal{X}} p(x) f(x) \; dx$.
A more general result for multi-variate normal distributions with different means and covariances
can be found [here](https://mr-easy.github.io/2020-04-16-kl-divergence-between-2-gaussian-distributions/).
</details>

One can interpret this as the penalty term to make the latent space meaningful. If all the latent vectors $\boldsymbol{z}$ you generate have each component $z_i$ normally distributed with mean 0, variance 1 (and we know they're independent because our $\epsilon_i$ we used to generate them are independent), then there will be no gaps in your latent space where you produce weird-looking output (like we saw in our autoencoder plots from the previous section). You can try training your VAE without this term, and it might do okay at reproducing $\boldsymbol{x}$, but it will perform much worse when it comes time to use it for generation. Again, you can quantify this by encoding some input data and projecting it onto the first two dimensions. When you include this term you should expect to see a nice regular cloud surrounding the origin, but without this term you might see some irregular patterns or blind spots:

<img src="https://raw.githubusercontent.com/info-arena/ARENA_img/main/misc/gan_images/vae_latent_space.png" width="700">

Once you've computed both of these loss functions, you should add them together and perform gradient descent on them.


### Beta-VAEs

The Beta-VAE is a very simple extension of the VAE, with a different loss function: we multiply the KL Divergence term by a constant $\beta$. This helps us balance the two different loss terms. Here, we've given you the default value of $\beta = 0.1$ rather than using $\beta = 1$ (which is implicit when we use regular VAEs rather than beta-VAEs).

As a general comment on tuning hyperparameters like $\beta$, it's important to sweep over ranges of different values and know how to tell when one of them is dominating the model's behaviour. In this particular case, $\beta$ being too large means your model will too heavily prioritize having its latent vectors' distribution equal to the standard normal distribution, to the point where it might essentially lose all structure in the data and ignore accurate reconstruction. On the other hand, $\beta$ being too small means we just reduce to the autoencoder case where the model has no incentive to make meaningful use of the latent space. Weights and biases hyperparameter searches are a good tool for sweeping over ranges and testing the results, but they'll only work if you log the relevant data / output and know how to interpret it.


### Exercise - write your VAE training loop

> ```yaml
> Difficulty: 🔴🔴🔴⚪⚪
> Importance: 🔵🔵🔵⚪⚪
> 
> You should spend up to 15-30 minutes on this exercise.
> ```

You should write and run your training loop below. This will involve a lot of recycled code from the corresponding `Autoencoder` exercise - in fact, depending on how you implemented the `train` method before, you might literally be able to copy and paste that method here!


```python
@dataclass
class VAEArgs(AutoencoderArgs):
    wandb_project: str | None = "day5-vae-mnist"
    beta_kl: float = 0.1


class VAETrainer:
    def __init__(self, args: VAEArgs):
        self.args = args
        self.trainset = get_dataset(args.dataset)
        self.trainloader = DataLoader(self.trainset, batch_size=args.batch_size, shuffle=True, num_workers=8)
        self.model = VAE(
            latent_dim_size=args.latent_dim_size,
            hidden_dim_size=args.hidden_dim_size,
        ).to(device)
        self.optimizer = t.optim.Adam(self.model.parameters(), lr=args.lr, betas=args.betas)

    def training_step(self, img: Tensor):
        """
        Performs a training step on the batch of images in `img`. Returns the loss. Logs to wandb
        if enabled.
        """
        raise NotImplementedError()

    @t.inference_mode()
    def log_samples(self) -> None:
        """
        Evaluates model on holdout data, either logging to wandb or displaying output inline.
        """
        assert self.step > 0, "First call should come after a training step. Remember to increment `self.step`."
        output = self.model(HOLDOUT_DATA)[0]
        if self.args.use_wandb:
            output = (output - output.min()) / (output.max() - output.min())  # Normalize to [0, 1]
            output = (output * 255).to(dtype=t.uint8)  # Convert to uint8 for logging
            wandb.log({"images": [wandb.Image(arr) for arr in output.cpu().numpy()]}, step=self.step)
        else:
            display_data(t.concat([HOLDOUT_DATA, output]), nrows=2, title="VAE reconstructions")

    def train(self) -> VAE:
        """Performs a full training run."""
        self.step = 0
        if self.args.use_wandb:
            wandb.init(project=self.args.wandb_project, name=self.args.wandb_name)
            wandb.watch(self.model)

        # YOUR CODE HERE - iterate over epochs, and train your model

        if self.args.use_wandb:
            wandb.finish()

        return self.model


args = VAEArgs(latent_dim_size=5, hidden_dim_size=100, use_wandb=True)
trainer = VAETrainer(args)
vae = trainer.train()
```


<details><summary>Solution</summary>

```python
@dataclass
class VAEArgs(AutoencoderArgs):
    wandb_project: str | None = "day5-vae-mnist"
    beta_kl: float = 0.1


class VAETrainer:
    def __init__(self, args: VAEArgs):
        self.args = args
        self.trainset = get_dataset(args.dataset)
        self.trainloader = DataLoader(self.trainset, batch_size=args.batch_size, shuffle=True, num_workers=8)
        self.model = VAE(
            latent_dim_size=args.latent_dim_size,
            hidden_dim_size=args.hidden_dim_size,
        ).to(device)
        self.optimizer = t.optim.Adam(self.model.parameters(), lr=args.lr, betas=args.betas)

    def training_step(self, img: Tensor):
        """
        Performs a training step on the batch of images in `img`. Returns the loss. Logs to wandb
        if enabled.
        """
        # Get the different loss components, as well as the total loss
        img = img.to(device)
        img_reconstructed, mu, logsigma = self.model(img)
        reconstruction_loss = nn.MSELoss()(img, img_reconstructed)
        kl_div_loss = (0.5 * (mu**2 + t.exp(2 * logsigma) - 1) - logsigma).mean() * self.args.beta_kl
        loss = reconstruction_loss + kl_div_loss

        # Backprop on the loss, and step with optimizers
        loss.backward()
        self.optimizer.step()
        self.optimizer.zero_grad()

        # Log various values, and also increment `self.step`
        if self.args.use_wandb:
            wandb.log(
                dict(
                    reconstruction_loss=reconstruction_loss.item(),
                    kl_div_loss=kl_div_loss.item(),
                    mean=mu.mean(),
                    std=t.exp(logsigma).mean(),
                    total_loss=loss.item(),
                ),
                step=self.step,
            )
        return loss

    @t.inference_mode()
    def log_samples(self) -> None:
        """
        Evaluates model on holdout data, either logging to wandb or displaying output inline.
        """
        assert self.step > 0, "First call should come after a training step. Remember to increment `self.step`."
        output = self.model(HOLDOUT_DATA)[0]
        if self.args.use_wandb:
            output = (output - output.min()) / (output.max() - output.min())  # Normalize to [0, 1]
            output = (output * 255).to(dtype=t.uint8)  # Convert to uint8 for logging
            wandb.log({"images": [wandb.Image(arr) for arr in output.cpu().numpy()]}, step=self.step)
        else:
            display_data(t.concat([HOLDOUT_DATA, output]), nrows=2, title="VAE reconstructions")

    def train(self) -> VAE:
        """Performs a full training run."""
        self.step = 0
        if self.args.use_wandb:
            wandb.init(project=self.args.wandb_project, name=self.args.wandb_name)
            wandb.watch(self.model)

        for epoch in range(self.args.epochs):
            # Iterate over training data, performing a training step for each batch
            progress_bar = tqdm(self.trainloader, total=int(len(self.trainloader)), ascii=True)
            for img, label in progress_bar:  # remember that label is not used
                img = img.to(device)
                loss = self.training_step(img)
                self.step += 1
                progress_bar.set_description(f"{epoch=:02d}, {loss=:.4f}, batches={self.step:05d}")
                if self.step % self.args.log_every_n_steps == 0:
                    self.log_samples()


        if self.args.use_wandb:
            wandb.finish()

        return self.model


```
</details>


You might be disappointed when comparing your VAE's reconstruction to the autoencoder, since it's likely to be worse. However, remember that the focus of VAEs is in better generation, not reconstruction. To test it's generation, let's produce some plots of latent space like we did for the autoencoder.

First, we'll visualize the latent space:


```python
grid_latent = create_grid_of_latents(vae, interpolation_range=(-1, 1))
output = vae.decoder(grid_latent)
utils.visualise_output(output, grid_latent, title="VAE latent space visualization")
```


<details><summary>Click to see the expected output</summary>

<div style="text-align: left"><embed src="https://info-arena.github.io/ARENA_img/misc/media-05/0506.html" width="670" height="620"></div>

</details>


which should look a lot better! The vast majority of images in this region should be recognisable digits. In this case, starting from the top-left and going clockwise, we can see 0s, 6s, 5s, 1s, 9s and 8s. Even the less recognisable regions seem like they're just interpolations between digits which are recognisable (which is something we should expect to happen given our VAE's output is continuous).

Now for the scatter plot to visualize our input space:


```python
small_dataset = Subset(get_dataset("MNIST"), indices=range(0, 5000))
imgs = t.stack([img for img, label in small_dataset]).to(device)
labels = t.tensor([label for img, label in small_dataset]).to(device).int()

# We're getting the mean vector, which is the [0]-indexed output of the encoder
latent_vectors = vae.encoder(imgs)[0, :, :2]
holdout_latent_vectors = vae.encoder(HOLDOUT_DATA)[0, :, :2]

utils.visualise_input(latent_vectors, labels, holdout_latent_vectors, HOLDOUT_DATA)
```


<details><summary>Click to see the expected output</summary>

<div style="text-align: left"><embed src="https://info-arena.github.io/ARENA_img/misc/media-05/0507.html" width="720" height="720"></div>

</details>


The range of the distribution looks much more like a standard normal distribution (most points are in `[-2, 2]` whereas in the previous plot the range was closer to `[-10, 10]`). There are also no longer any large gaps in the latent space that you wouldn't find in the corresponding standard normal distribution.

To emphasize - don't be disheartened if your *reconstructions of the original MNIST images* don't look as faithful for your VAE than they did for your encoder. Remember the goal of these architectures isn't to reconstruct images faithfully, it's to generate images from samples in the latent dimension. This is the basis on which you should compare your models to each other.


## A deeper dive into the maths of VAEs

If you're happy with the loss function as described in the section above, then you can move on from here. If you'd like to take a deeper dive into the mathematical justifications of this loss function, you can read the following content. I'd consider it pretty essential in laying the groundwork for understanding diffusion models, and most kinds of generative image models (which we might dip into later in this course).

> *Note - this section is meant to paint more of an intuitive picture than deal with formal and rigorous mathematics, which is why we'll play fairly fast and loose with things like limit theorems and whether we can swap around integrals and expected values. This can be formalized further, but we'll leave that for other textbooks.*

Firstly, let's ignore the encoder, and suppose we're just starting from a latent vector $\boldsymbol{z} \sim p(z) = N(0, I)$. We can parameterize a **probabilistic decoder** as $p_\theta(\boldsymbol{x} \mid \boldsymbol{z})$, i.e. a way of mapping from latent vectors $z$ to a distribution over images $\boldsymbol{x}$. To use it as a decoder, we just sample a latent vector then sample from the resulting probability distribution our decoder gives us. Imagine this as a factory line: the latent vector $\boldsymbol{z}$ is some kind of compressed blueprint for our image, and our decoder is a way of reconstructing images from this information.

On this factory line, the probability of producing any given image $\boldsymbol{x}$ can be found from integrating over the possible latent vectors $\boldsymbol{z}$ which could have produced it:
$$
\begin{aligned}
p(\boldsymbol{x})&=\int_z p_\theta(\boldsymbol{x} \mid \boldsymbol{z}) p(\boldsymbol{z}) \; d \boldsymbol{z} \\
&= \mathbb{E}_{\boldsymbol{z} \sim p(\boldsymbol{z})}\big[p_\theta(\boldsymbol{x} \mid \boldsymbol{z})\big]
\end{aligned}
$$
What if we estimate this value over random samples $x_i \sim \hat{p}(\boldsymbol{x})$ from our dataset? We could perform gradient ascent on $\theta$ using this estimate to find a decoder $p_\theta(\boldsymbol{x} \mid \boldsymbol{z})$ that makes this estimate high, in other words a factory line that is *likely to produce images like the ones in our dataset*. Then we're done - right?

Unfortunately, it's not that easy. Evaluating this integral would be computationally intractible, because we would have to sample over all possible values for the latent vectors $\boldsymbol{z}$:
$$
\theta^*=\underset{\theta}{\operatorname{argmax}}\; \mathbb{E}_{x \sim \hat{p}(\boldsymbol{x}),\, \boldsymbol{z} \sim p(\boldsymbol{z})}\big[p_\theta(\boldsymbol{x} \mid \boldsymbol{z})\big]
$$
In our ideal factory line, for any given image $\boldsymbol{x}$ there's probably only a small cluster of latent vectors $\boldsymbol{z}$ that could have produced it, and it's that small cluster that we should be concentrating our probability mass over. Without this, it'll take an exponentially long time to get full sampling coverage of the latent space of $\boldsymbol{z}$.

This is where our encoder function $q_\phi(\boldsymbol{z} \mid \boldsymbol{x})$ comes in! It helps concentrate our guess for $\boldsymbol{z}$ for any given $\boldsymbol{x}$, essentially telling us **which latent vectors were likely to have produced the image $\boldsymbol{x}$**. We can now replace our original integral with the following:

<!-- <img src="https://raw.githubusercontent.com/info-arena/ARENA_img/main/misc/gan_images/vae-graphical.png" width="500"> -->

$$
\begin{aligned}
p(\boldsymbol{x}) &=\int q_\phi(\boldsymbol{z} \mid \boldsymbol{x}) \frac{p_\theta(\boldsymbol{x} \mid \boldsymbol{z}) p(\boldsymbol{z})}{q_\phi(\boldsymbol{z} \mid \boldsymbol{x})} \;d \boldsymbol{z}\\
\theta^*&=\underset{\theta}{\operatorname{argmax}}\; \mathbb{E}_{\boldsymbol{x} \sim \hat{p}(\boldsymbol{x}), \boldsymbol{z} \sim q_\phi(\boldsymbol{z}\mid \boldsymbol{x})}\left[\frac{p_\theta(\boldsymbol{x} \mid \boldsymbol{z})p(\boldsymbol{z})}{q_\phi(\boldsymbol{z} \mid \boldsymbol{x})}\right] \\
&=\underset{\theta}{\operatorname{argmax}}\; \mathbb{E}_{\boldsymbol{x} \sim \hat{p}(\boldsymbol{x})}\left[\mathbb{E}_{\boldsymbol{z} \sim q_\phi(\boldsymbol{z}\mid \boldsymbol{x})}\left[\frac{p_\theta(\boldsymbol{x} \mid \boldsymbol{z})p(\boldsymbol{z})}{q_\phi(\boldsymbol{z} \mid \boldsymbol{x})}\right]\right]
\end{aligned}
$$
Why is this easier? Well, now that we've rearranged it by introducing this $q_\phi$ term, our distribution of $\boldsymbol{z}$ is conditioned on $\boldsymbol{x}$. So for any given sample $x_i$, we don't need to sample a huge number of latent vectors $\boldsymbol{z}$ to estimate the inner expected value in the expression above - we can just sample from $q_\phi(\boldsymbol{z}\mid \boldsymbol{x_i})$, which already concentrates a lot of our probability mass for where $\boldsymbol{z}$ should be.

We now introduce an important quantity, called the **ELBO**, or **evidence lower-bound**. It is defined as the value inside the expectation in the expression above, but using log instead. 
$$
\operatorname{ELBO}(\boldsymbol{x})=\mathbb{E}_{\boldsymbol{z} \sim q_\phi(\boldsymbol{z} \mid \boldsymbol{x})}\left[\log \frac{p_\theta(\boldsymbol{x} \mid \boldsymbol{z})p(\boldsymbol{z})}{q_\phi(\boldsymbol{z} \mid \boldsymbol{x})}\right]
$$
Why do we call this the ELBO? Answer - because it's a lower bound for the quantity $\log p(\boldsymbol{x})$, which we call the **evidence**. The proof for this being a lower bound comes from **Jensen's inequality**, which states that $\mathbb{E}[f(X)] \geq f(\mathbb{E}[X])$ for any convex function $f$ (and $f(\boldsymbol{x})=-\log(\boldsymbol{x})$ is convex). 

<!-- In fact,  [we can prove](https://lilianweng.github.io/posts/2018-08-12-vae/#loss-function-elbo) that the difference between $\log p(\boldsymbol{x})$ and the ELBO is equal to the KL divergence between the distribution $q_\phi$ and the **posterior distribution** $p_\theta(\boldsymbol{z} \mid \boldsymbol{x})$ (the order of $\boldsymbol{z}$ and $\boldsymbol{x}$ have been swapped). KL divergence is always non-negative, hence the lower bound. -->

<!-- $$
\log{p(\boldsymbol{x})}=\mathbb{E}_{\mathbb{z} \sim q_{\boldsymbol{\phi}}(\boldsymbol{z} \mid \boldsymbol{x})}\left[\log \frac{p(\boldsymbol{z}) p_\theta(\boldsymbol{x} \mid \boldsymbol{z})}{q_{\boldsymbol{\phi}}(\boldsymbol{z} \mid \boldsymbol{x})}\right]+D_{\mathrm{KL}}\left(q_{\boldsymbol{\phi}}(\boldsymbol{z} \mid \boldsymbol{x}) \,\|\, p_\theta(\boldsymbol{z} \mid \boldsymbol{x})\right)
$$ -->

It turns out that by looking at log probs rather than probabilities, we can now rewrite the ELBO as something which looks a lot like our VAE loss function! $p_\theta(\boldsymbol{x} \mid \boldsymbol{z})$ is our decoder, $q_\phi(\boldsymbol{z} \mid \boldsymbol{x})$ is our encoder, and we train them jointly using gradient ascent on our estimate of the ELBO. For any given sample $x_i$, the value $\operatorname{ELBO}(x_i)$ is estimated by sampling a latent vector $z_i \sim q_\phi(\boldsymbol{z} \mid \boldsymbol{x_i})$, and then performing gradient ascent on the ELBO, which can be rewritten as:

$$
\begin{aligned}
\operatorname{ELBO}(\boldsymbol{x}) & =\mathbb{E}_{\mathbb{z} \sim q_{\boldsymbol{\phi}}(\boldsymbol{z} \mid \boldsymbol{x})}\left[\log p_{\boldsymbol{\theta}}(\boldsymbol{x} \mid \boldsymbol{z}) + \log \frac{p(\boldsymbol{z})}{q_{\boldsymbol{\phi}}(\boldsymbol{z} \mid \boldsymbol{x})}\right] \\
& =\underbrace{\mathbb{E}_{\boldsymbol{z} \sim q_\phi(\boldsymbol{z} \mid \boldsymbol{x})}\left[\log p_{\boldsymbol{\theta}}(\boldsymbol{x} \mid \boldsymbol{z})\right]}_{\text {reconstruction loss}}-\underbrace{D_{\mathrm{KL}}\left(q_{\boldsymbol{\phi}}(\boldsymbol{z} \mid \boldsymbol{x}) \,\|\, p(\boldsymbol{z})\right)}_{\text {regularisation term}}
\end{aligned}
$$
which if you tilt your head a bit, is just like our VAE loss function! To see this:

* **The first term** is playing the role of reconstruction loss, since it's equivalent to the log probability that our image $x$ is perfectly reconstructed via the series of maps $\boldsymbol{x} \xrightarrow{\text{encoder}} \boldsymbol{z} \xrightarrow{\text{decoder}} \boldsymbol{x}$. If we had perfect reconstruction then this value would be zero (which is its maximum value).
* **The second term** is the KL divergence between $q_\phi(\boldsymbol{z} \mid \boldsymbol{x})$ and $p_{\theta}(\boldsymbol{z})$. The former is your own encoder's distribution of latent vectors which you may recall is $N(\mu(\boldsymbol{x}), \sigma(\boldsymbol{x})^2)$, and the latter was assumed to be the uniform distribution $N(0, I)$. This just reduces to our KL penalty term from earlier.

The decoder used in our VAE isn't actually probabilistic $p_\theta(\cdot \mid \boldsymbol{z})$, it's deterministic (i.e. it's a map from latent vector $\boldsymbol{z}$ to reconstructed input $\boldsymbol{x}'$). But we can pretend that the decoder output is actually the mean of a probability distribution, and we're choosing this mean as the value of our reconstruction $\boldsymbol{x}'$. The reconstruction loss term in the formula above will be smallest when this mean is close to the original value $\boldsymbol{x}$ (because then $p_\theta(\cdot \mid \boldsymbol{z})$ will be a probability distribution centered around $\boldsymbol{x}$). And it turns out that we can just replace this reconstruction loss with something that fulfils basically the same purpose (the $L_2$ penalty) - although we sometimes need to adjust these two terms (see $\beta$-VAEs above).

And that's the math of VAEs in a nutshell!


## Bonus exercises

### PCA

In the code earlier, we visualised our autoencoder / VAE output along the first two dimensions of the latent space. If each dimension is perfectly IID then we should expect this to get similar results to varying along any two arbitrarily chosen orthogonal directions. However, in practice you might find it an improvement to choose directions in a more principled way. One way to do this is to use **principal component analysis** (PCA). Can you write code to extract the PCA components from your model's latent space, and plot the data along these components?

<details>
<summary>Template (code for extracting PCA from the Autoencoder)</summary>

```python
from sklearn.decomposition import PCA

@t.inference_mode()
def get_pca_components(
    model: Autoencoder,
    dataset: Dataset,
) -> tuple[Tensor, Tensor]:
    '''
    Gets the first 2 principal components in latent space, from the data.

    Returns:
        pca_vectors: shape (2, latent_dim_size)
            the first 2 principal component vectors in latent space
        principal_components: shape (batch_size, 2)
            components of data along the first 2 principal components
    '''
    # Unpack the (small) dataset into a single batch
    imgs = t.stack([batch[0] for batch in dataset]).to(device)
    labels = t.tensor([batch[1] for batch in dataset])

    # Get the latent vectors
    latent_vectors = model.encoder(imgs.to(device)).cpu().numpy()
    if latent_vectors.ndim == 3: latent_vectors = latent_vectors[0] # useful for VAEs; see later

    # Perform PCA, to get the principle component directions (& projections of data in these dirs)
    pca = PCA(n_components=2)
    principal_components = pca.fit_transform(latent_vectors)
    pca_vectors = pca.components_
    return (
        t.from_numpy(pca_vectors).float(),
        t.from_numpy(principal_components).float(),
    )
```

And then you can use this function in your `visualise_output` by replacing the code at the start with this:

```python
pca_vectors, principal_components = get_pca_components(model, dataset)

# Constructing latent dim data by making two of the dimensions vary independently in the
# interpolation range.
x = t.linspace(*interpolation_range, n_points)
grid_latent = t.stack([
    einops.repeat(x, "dim1 -> dim1 dim2", dim2=n_points),
    einops.repeat(x, "dim2 -> dim1 dim2", dim1=n_points),
], dim=-1)
# Map grid to the basis of the PCA components
grid_latent = grid_latent @ pca_vectors
```

Note that this will require adding `dataset` to the arguments of this function.


You can do something similar for the `visualise_input` function:

```python
@t.inference_mode()
def visualise_input(
    model: Autoencoder,
    dataset: Dataset,
) -> None:
    '''
    Visualises (in the form of a scatter plot) the input data in the latent space, along the first
    two latent dims.
    '''
    # First get the model images' latent vectors, along first 2 dims
    imgs = t.stack([batch for batch, label in dataset]).to(device)
    latent_vectors = model.encoder(imgs)
    if latent_vectors.ndim == 3: latent_vectors = latent_vectors[0] # useful for VAEs later
    latent_vectors = latent_vectors[:, :2].cpu().numpy()
    labels = [str(label) for img, label in dataset]

    # Make a dataframe for scatter (px.scatter is more convenient to use when supplied with a dataframe)
    df = pd.DataFrame({"dim1": latent_vectors[:, 0], "dim2": latent_vectors[:, 1], "label": labels})
    df = df.sort_values(by="label")
    fig = px.scatter(df, x="dim1", y="dim2", color="label")
    fig.update_layout(height=700, width=700, title="Scatter plot of latent space dims", legend_title="Digit")
    data_range = df["dim1"].max() - df["dim1"].min()

    # Add images to the scatter plot (optional)
    output_on_data_to_plot = model.encoder(HOLDOUT_DATA.to(device))
    if output_on_data_to_plot.ndim == 3:
        output_on_data_to_plot = output_on_data_to_plot[0] # useful for VAEs later
    output_on_data_to_plot = output_on_data_to_plot[:, :2].cpu()
    data_translated = (HOLDOUT_DATA.cpu().numpy() * 0.3081) + 0.1307
    data_translated = (255 * data_translated).astype(np.uint8).squeeze()
    for i in range(10):
        x, y = output_on_data_to_plot[i]
        fig.add_layout_image(
            source=Image.fromarray(data_translated[i]).convert("L"),
            xref="x", yref="y",
            x=x, y=y,
            xanchor="right", yanchor="top",
            sizex=data_range/15, sizey=data_range/15,
        )
    fig.show()
```
    
</details>

### Beta-VAEs

Read the section on [Beta-VAEs](https://lilianweng.github.io/posts/2018-08-12-vae/#beta-vae), if you haven't already. Can you choose a better value for $\beta$?

To decide on an appropriate $\beta$, you can look at the distribution of your latent vector. For instance, if your latent vector looks very different to the standard normal distribution when it's projected onto one of its components (e.g. maybe that component is very sharply spiked around some particular value), this is a sign that you need to use a larger parameter $\beta$. You can also just use hyperparameter searches to find an optimal $\beta$. See [the paper](https://openreview.net/pdf?id=Sy2fzU9gl) which introduced Beta-VAEs for more ideas.

### CelebA dataset

Try to build an autoencoder for the CelebA dataset. You shouldn't need to change the architecture much from your MNIST VAE. You should find the training much easier than with your GAN (as discussed yesterday, GANs are notoriously unstable when it comes to training). Can you get better results than you did for your GAN?

### Hierarchical VAEs

Hierarchical VAEs are ones which stack multiple layers of parameter-learning and latent-vector-sampling, rather than just doing this once. Read the section of [this paper](https://arxiv.org/pdf/2208.11970.pdf) for a more thorough description.

<img src="https://raw.githubusercontent.com/info-arena/ARENA_img/main/misc/vae-and-hvae-final.png" width="1100">

(Note - the KL divergence loss used in HVAEs can sometimes be more complicated than the one presented in this diagram, if you want to implement conditional dependencies between the different layers. However, this isn't necessary for the basic HVAE architecture.)

Try to implement your own hierarchical VAE.

Note - when you get to the material on **diffusion models** later in the course, you might want to return here, because understanding HVAEs can be a useful step to understanding diffusion models. In fact diffusion models can almost be thought of as a special type of HVAE.

### Denoising and sparse autoencoders

The reading material on VAEs talks about [denoising](https://lilianweng.github.io/posts/2018-08-12-vae/#denoising-autoencoder) and [sparse](https://lilianweng.github.io/posts/2018-08-12-vae/#sparse-autoencoder) autoencoders. Try changing the architecture of your autoencoder (not your VAE) to test out one of these two techniques. Do does your decoder output change? How about your encoder scatter plot?

***Note - sparse autoencoders will play an important role in some later sections of this course (when we study superposition in mechanistic interpretability).***

If you're mathematically confident and feeling like a challenge, you can also try to implement [contractive autoencoders](https://lilianweng.github.io/posts/2018-08-12-vae/#contractive-autoencoder)!




=== NEW CHAPTER ===


# 2️⃣ GANs



> ##### Learning Objectives
>
> - Understand the loss function used in GANs, and why it can be expected to result in the generator producing realistic outputs.
> - Implement the DCGAN architecture from the paper, with relatively minimal guidance.
> - Learn how to identify and fix bugs in your GAN architecture, to improve convergence properties.

## Reading

* Google Machine Learning Education, [Generative Adversarial Networks](https://developers.google.com/machine-learning/gan) (strongly recommended, ~15 mins)
    * This is a very accessible introduction to the core ideas behind GANs
    * You should read at least the sections in **Overview**, and the sections in **GAN Anatomy** up to and including **Loss Functions**
* [Unsupervised representation learning with deep convolutional generative adversarial networks](https://paperswithcode.com/method/dcgan) (optional, we'll be going through parts of this paper later on in the exercises)
    * This paper introduced the DCGAN, and describes an architecture very close to the one we'll be building today.
    * It's one of the most cited ML papers of all time!


## How GANs work

The basic idea behind GANs is as follows:

* You have two networks, the **generator** and the **discriminator**.
* The generator's job is to produce output realistic enough to fool the discriminator, and the discriminator's job is to try and tell the difference between real and fake output.

The idea is for both networks to be trained simultaneously, in a positive feedback loop: as the generator produces better output, the discriminator's job becomes harder, and it has to learn to spot more subtle features distinguishing real and fake images, meaning the generator has to work harder to produce images with those features.

### Discriminator

The discriminator works by taking an image (either real, or created by the generator), and outputting a single value between 0 and 1, which is the probability that the discriminator puts on the image being real. The discriminator sees the images, but not the labels (i.e. whether the images are real or fake), and it is trained to distinguish between real and fake images with maximum accuracy. The discriminator's loss function is the cross entropy between its probability estimates ($D(x)$ for real images, $D(G(z))$ for fake images) and the true labels ($1$ for real images, $0$ for fake images).

### Generator

The architecture of generators in a GAN setup is generally a mirror image of the discriminator, with convolutions swapped out for **transposed convolutions**. This is the case for the DCGAN paper we'll be reading (which is why they only give a diagram of the generator, not both). The generator works by taking in a vector $z$, whose elements are all normally distributed with mean 0 and variance 1. We call the space from which $z$ is sampled **latent dimension** or **latent space**, and we call $z$ a **latent vector**. The formal definition of a latent space is *an abstract multi-dimensional space that encodes a meaningful internal representation of externally observed events.* We'll dive a little deeper into what this means and the overall significance of latent spaces later on, but for now it's fine to understand this vector $z$ as a kind of random seed, which causes the generator to produce different outputs. After all, if the generator only ever produced the same image as output then the discriminator's job would be pretty easy (just subtract the image $g$ always produces from the input image, and see if the result is close to zero!). The generator's objective function is an increasing function of $D(G(z))$, in other words it tries to produce images $G(z)$ which have a high chance of fooling the discriminator (i.e. $D(G(z)) \approx 1$).

### Convergence

The ideal outcome when training a GAN is for the generator to produce perfect output indistinguishable from real images, and the discriminator just guesses randomly. However, the precise nature of the situations when GANs converge is an ongoing area of study (in general, adversarial networks have very unstable training patterns). For example, you can imagine a situation where the discriminator becomes almost perfect at spotting fake outputs, because of some feature that the discriminator spots and that the generator fails to capture in its outputs. It will be very difficult for the generator to get a training signal, because it has to figure out what feature is missing from its outputs, and how it can add that feature to fool the discriminator. And to make matters worse, maybe marginal steps in that direction will only increase the probability of fooling the discriminator from almost-zero to slightly-more-than-almost-zero, which isn't much of a training signal! Later on we will see techniques people have developed to overcome problems like this and others, but in general they can't be solved completely.

<details>
<summary>Optional exercise - what conditions must hold for the discriminator's best strategy to be random guessing with probability 0.5?</summary>

It is necessary for the generator to be producing perfect outputs, because otherwise the discriminator could do better than random guessing.

If the generator is producing perfect outputs, then the discriminator never has any ability to distinguish real from fake images, so it has no information. Its job is to minimise the cross entropy between its output distribution $(D(x), 1-D(x))$, and the distribution of real/fake images. Call this $(p, 1-p)$, i.e. $p$ stands for the proportion of images in training which are real. Note how we just used $p$ rather than $p(x)$, because there's no information in the image $x$ which indicates whether it is real or fake. Trying to minimize the cross entropy between $(p, 1-p)$ and $(D(x), 1-D(x))$ gives us the solution $D(x) = p$ for all $x$. In other words, our discriminator guesses real/fake randomly with probability equal to the true underlying frequency of real/fake images in the data. This is 0.5 if and only if the data contains an equal number of real and fake images.

To summarize, the necessary and sufficient conditions for $(\forall x) \; D(x) = 0.5$ being the optimal strategy are:

* The generator $G$ produces perfect output
* The underlying frequency of real/fake images in the data is 50/50

</details>

<br>

<img src="https://raw.githubusercontent.com/info-arena/ARENA_img/main/misc/gan_images/dcgan-9-solid.png" width="1000">


### Exercise - some more modules

> ```yaml
> Difficulty: 🔴🔴⚪⚪⚪
> Importance: 🔵🔵⚪⚪⚪
> 
> You should spend up to 10-20 minutes on this exercise.
> ```

You'll also need to implement a few more modules, which have docstrings provided below (they should be fairly quick, and will just serve as a refresher for the structure of modules). They are:

* [`Tanh`](https://pytorch.org/docs/stable/generated/torch.nn.Tanh.html) which is an activation function used by the DCGAN you'll be implementing.
* [`LeakyReLU`](https://pytorch.org/docs/stable/generated/torch.nn.LeakyReLU.html) which is an activation function used by the DCGAN you'll be implementing. This function is popular in tasks where we we may suffer from sparse gradients (GANs are a primary example of this).
* [`Sigmoid`](https://pytorch.org/docs/stable/generated/torch.nn.Sigmoid.html), for converting the single logit output from the discriminator into a probability.

They should all be relatively short. You can go back to day 2's exercises to remind yourself of the basic syntax.


```python
class Tanh(nn.Module):
    def forward(self, x: Tensor) -> Tensor:
        raise NotImplementedError()


class LeakyReLU(nn.Module):
    def __init__(self, negative_slope: float = 0.01):
        super().__init__()
        self.negative_slope = negative_slope

    def forward(self, x: Tensor) -> Tensor:
        raise NotImplementedError()

    def extra_repr(self) -> str:
        return f"negative_slope={self.negative_slope}"


class Sigmoid(nn.Module):
    def forward(self, x: Tensor) -> Tensor:
        raise NotImplementedError()


tests.test_Tanh(Tanh)
tests.test_LeakyReLU(LeakyReLU)
tests.test_Sigmoid(Sigmoid)
```


<details><summary>Solution</summary>

```python
class Tanh(nn.Module):
    def forward(self, x: Tensor) -> Tensor:
        return (t.exp(x) - t.exp(-x)) / (t.exp(x) + t.exp(-x))


class LeakyReLU(nn.Module):
    def __init__(self, negative_slope: float = 0.01):
        super().__init__()
        self.negative_slope = negative_slope

    def forward(self, x: Tensor) -> Tensor:
        return t.where(x > 0, x, self.negative_slope * x)

    def extra_repr(self) -> str:
        return f"negative_slope={self.negative_slope}"


class Sigmoid(nn.Module):
    def forward(self, x: Tensor) -> Tensor:
        return 1 / (1 + t.exp(-x))
```
</details>


## GANs

Now, you're ready to implement and train your own DCGAN! You'll be basing your implementation on the [DCGAN paper](https://arxiv.org/abs/1511.06434v2). Implementing architectures based on descriptions in papers is an incredibly valuable skill for any would-be research engineer, however in these exercises we've given enough guidance on this page that you shouldn't need to refer to the paper much if at all. However, we do encourage you to skim the paper, and think about how you might go about this replication task without guidance!


### Discriminator & Generator architectures

We refer back to the diagram at the start of this section for the basic discriminator and generator architectures. Rather than hardcoding a single set of values, we're going to make our architecture more flexible - giving us the ability to change the number of layers, or the sizes of each layer, by using different input arguments.


#### Discriminator

The discriminator starts with a series of blocks of the form `(Conv -> BatchNorm -> ActivationFunction)`. Following the paper's conventions:

* Each convolution should have kernel size 4, stride 2, padding 1. This will halve the width and height of the image at each step. The output channels of each convolution are given by the `hidden_channels` argument. For instance, if `img_channels=3` (because the image is RGB) and `hidden_channels=[128, 256, 512]`, then there will be three convolutions: the first mapping from 3 -> 128 channels, the second from 128 -> 256, and the third from 256 -> 512.
* All blocks have a batchnorm layer, **except for the very first one**.
* All blocks' activation functions are `LeakyRelu`.

Lastly, we flatten the output of the final convolutional block, and use a fully connected layer to map it to a single value (i.e. a vector of length `batch_size`) which we then pass through a sigmoid to get a probability that the image is real. Again, we recommend the `Rearrange` module from the `einops` library for this.

None of the convolutions or linear layers should have biases (this is also true for the generator).

The diagram below shows what we'd get with the following arguments:

```python
img_size = 64
img_channels = 3
hidden_channels = [128, 256, 512]
```

<img src="https://raw.githubusercontent.com/info-arena/ARENA_img/main/misc/gan_images/dcgan-d-help-9-solid.png" width="700">


#### Generator

The generator is essentially the mirror image of the discriminator. While the discriminator had convolutions which halved the image size on each layer, the generator has transposed convolutions which double the size on each layer (so apart from the very start of the generator / end of the discriminator, all the activations have the same shape, just in reverse).

We start with the latent vector of shape `(batch_size, latent_dim_size)`, and apply a fully connected layer & reshaping to get our first tensor which has shape `(batch_size, channels, height, width)`. The parameters `channels` and `height` (which is equal to `width`) can be calculated from the `img_size` and `hidden_channels` arguments (remember that image size doubles at each transposed convolution, and after applying all the transposed convolutions we'll eventually get back to `img_size`). Then, we apply batchnorm and relu.

After this, we apply a series of blocks of the form `(ConvTranspose -> BatchNorm -> ActivationFunction)`. Following the paper's conventions:

* Each transposed convolution has kernel size 4, stride 2, padding 1. Like for the discriminator, the input & output channels of the convolutions are determined by the `hidden_channels` argument (although this time they're in reverse order).
* All blocks have a batchnorm layer, except for the very last one.
* All blocks' activation functions are `ReLU`, except for the last one which is `Tanh`.

The diagram below shows what we'd get with the following arguments:

```python
img_size = 64
img_channels = 3
hidden_channels = [128, 256, 512]
latent_dim_size = 100
```

<img src="https://raw.githubusercontent.com/info-arena/ARENA_img/main/misc/gan_images/dcgan-g-help-10-light.png" width="800">


### Exercise - building your GAN

> ```yaml
> Difficulty: 🔴🔴🔴🔴🔴
> Importance: 🔵🔵🔵🔵⚪
> 
> You should spend up to 30-50 minutes on this exercise.
> ```

You should implement your code below. We've provided one possible design choice and the corresponding forward functions:

- The generator is made of an initial `project_and_reshape` block that performs the first linear map, and then `hidden_layers` which are a stack of blocks each consisting of a (transponsed convolution, optional batchnorm, activation fn).
- The discriminator is made of `hidden_layers` which are a stack of (convolution, optional batchnorm, activation fn) blocks, and a final `classifier` block which flattens and maps to a single output (which represents the probability pre-sigmoid).

We've also given you the `DCGAN` class - note that we've not included a `forward` method here, because you'll usually be calling your discriminator and generators' forward methods directly. You can think of the DCGAN class as essentially a wrapper for both.

If you're stuck, you can import the generator and discriminator from the solutions, and compare it with yours. We've given you this option in place of test functions.

```python
from part2_cnns.utils import print_param_count

print_param_count(Generator(), solutions.DCGAN().netG)
print_param_count(Discriminator(), solutions.DCGAN().netD)
```

Lastly, remember that `torchinfo` is a useful library for inspecting the architecture of your model. Since it works by running input through your model, it provides another useful way to check your model's architecture is correct (since errors like the wrong convolution size will often cause forward passes to fail).

```python
model = DCGAN().to(device)
x = t.randn(3, 100).to(device)
print(torchinfo.summary(model.netG, input_data=x), end="\n\n")
print(torchinfo.summary(model.netD, input_data=model.netG(x)))
```

You can also check that the output of your model is the correct shape. **Note - we're using a 3-layer model rather than the 4-layer model shown in the diagram and described the paper.**


```python
class Generator(nn.Module):
    def __init__(
        self,
        latent_dim_size: int = 100,
        img_size: int = 64,
        img_channels: int = 3,
        hidden_channels: list[int] = [128, 256, 512],
    ):
        """
        Implements the generator architecture from the DCGAN paper (the diagram at the top
        of page 4). We assume the size of the activations doubles at each layer (so image
        size has to be divisible by 2 ** len(hidden_channels)).

        Args:
            latent_dim_size:
                the size of the latent dimension, i.e. the input to the generator
            img_size:
                the size of the image, i.e. the output of the generator
            img_channels:
                the number of channels in the image (3 for RGB, 1 for grayscale)
            hidden_channels:
                the number of channels in the hidden layers of the generator (starting closest
                to the middle of the DCGAN and going outward, i.e. in chronological order for
                the generator)
        """
        n_layers = len(hidden_channels)
        assert img_size % (2**n_layers) == 0, "activation size must double at each layer"

        super().__init__()

        # self.project_and_reshape = ...
        # self.hidden_layers = ...

    def forward(self, x: Tensor) -> Tensor:
        x = self.project_and_reshape(x)
        x = self.hidden_layers(x)
        return x


class Discriminator(nn.Module):
    def __init__(
        self,
        img_size: int = 64,
        img_channels: int = 3,
        hidden_channels: list[int] = [128, 256, 512],
    ):
        """
        Implements the discriminator architecture from the DCGAN paper (the mirror image of
        the diagram at the top of page 4). We assume the size of the activations doubles at
        each layer (so image size has to be divisible by 2 ** len(hidden_channels)).

        Args:
            img_size:
                the size of the image, i.e. the input of the discriminator
            img_channels:
                the number of channels in the image (3 for RGB, 1 for grayscale)
            hidden_channels:
                the number of channels in the hidden layers of the discriminator (starting
                closest to the middle of the DCGAN and going outward, i.e. in reverse-
                chronological order for the discriminator)
        """
        n_layers = len(hidden_channels)
        assert img_size % (2**n_layers) == 0, "activation size must double at each layer"

        super().__init__()

        self.hidden_layers = ...
        self.classifier = ...

    def forward(self, x: Tensor) -> Tensor:
        x = self.hidden_layers(x)
        x = self.classifier(x)
        return x.squeeze()  # remove dummy `out_channels` dimension


class DCGAN(nn.Module):
    netD: Discriminator
    netG: Generator

    def __init__(
        self,
        latent_dim_size: int = 100,
        img_size: int = 64,
        img_channels: int = 3,
        hidden_channels: list[int] = [128, 256, 512],
    ):
        super().__init__()
        self.latent_dim_size = latent_dim_size
        self.img_size = img_size
        self.img_channels = img_channels
        self.hidden_channels = hidden_channels
        self.netD = Discriminator(img_size, img_channels, hidden_channels)
        self.netG = Generator(latent_dim_size, img_size, img_channels, hidden_channels)
```


<details><summary>Solution</summary>

```python
class Generator(nn.Module):
    def __init__(
        self,
        latent_dim_size: int = 100,
        img_size: int = 64,
        img_channels: int = 3,
        hidden_channels: list[int] = [128, 256, 512],
    ):
        """
        Implements the generator architecture from the DCGAN paper (the diagram at the top
        of page 4). We assume the size of the activations doubles at each layer (so image
        size has to be divisible by 2 ** len(hidden_channels)).

        Args:
            latent_dim_size:
                the size of the latent dimension, i.e. the input to the generator
            img_size:
                the size of the image, i.e. the output of the generator
            img_channels:
                the number of channels in the image (3 for RGB, 1 for grayscale)
            hidden_channels:
                the number of channels in the hidden layers of the generator (starting closest
                to the middle of the DCGAN and going outward, i.e. in chronological order for
                the generator)
        """
        n_layers = len(hidden_channels)
        assert img_size % (2**n_layers) == 0, "activation size must double at each layer"

        super().__init__()

        # Reverse hidden channels, so they're in chronological order
        hidden_channels = hidden_channels[::-1]

        self.latent_dim_size = latent_dim_size
        self.img_size = img_size
        self.img_channels = img_channels
        # Reverse them, so they're in chronological order for generator
        self.hidden_channels = hidden_channels

        # Define the first layer, i.e. latent dim -> (512, 4, 4) and reshape
        first_height = img_size // (2**n_layers)
        first_size = hidden_channels[0] * (first_height**2)
        self.project_and_reshape = Sequential(
            Linear(latent_dim_size, first_size, bias=False),
            Rearrange("b (ic h w) -> b ic h w", h=first_height, w=first_height),
            BatchNorm2d(hidden_channels[0]),
            ReLU(),
        )

        # Equivalent, but using conv rather than linear:
        # self.project_and_reshape = Sequential(
        #     Rearrange("b ic -> b ic 1 1"),
        #     solutions.ConvTranspose2d(latent_dim_size, hidden_channels[0], first_height, 1, 0),
        #     BatchNorm2d(hidden_channels[0]),
        #     ReLU(),
        # )

        # Get list of input & output channels for the convolutional blocks
        in_channels = hidden_channels
        out_channels = hidden_channels[1:] + [img_channels]

        # Define all the convolutional blocks (conv_transposed -> batchnorm -> activation)
        conv_layer_list = []
        for i, (c_in, c_out) in enumerate(zip(in_channels, out_channels)):
            conv_layer = [
                ConvTranspose2d(c_in, c_out, 4, 2, 1),
                ReLU() if i < n_layers - 1 else Tanh(),
            ]
            if i < n_layers - 1:
                conv_layer.insert(1, BatchNorm2d(c_out))
            conv_layer_list.append(Sequential(*conv_layer))

        self.hidden_layers = Sequential(*conv_layer_list)

    def forward(self, x: Tensor) -> Tensor:
        x = self.project_and_reshape(x)
        x = self.hidden_layers(x)
        return x


class Discriminator(nn.Module):
    def __init__(
        self,
        img_size: int = 64,
        img_channels: int = 3,
        hidden_channels: list[int] = [128, 256, 512],
    ):
        """
        Implements the discriminator architecture from the DCGAN paper (the mirror image of
        the diagram at the top of page 4). We assume the size of the activations doubles at
        each layer (so image size has to be divisible by 2 ** len(hidden_channels)).

        Args:
            img_size:
                the size of the image, i.e. the input of the discriminator
            img_channels:
                the number of channels in the image (3 for RGB, 1 for grayscale)
            hidden_channels:
                the number of channels in the hidden layers of the discriminator (starting
                closest to the middle of the DCGAN and going outward, i.e. in reverse-
                chronological order for the discriminator)
        """
        n_layers = len(hidden_channels)
        assert img_size % (2**n_layers) == 0, "activation size must double at each layer"

        super().__init__()

        self.img_size = img_size
        self.img_channels = img_channels
        self.hidden_channels = hidden_channels

        # Get list of input & output channels for the convolutional blocks
        in_channels = [img_channels] + hidden_channels[:-1]
        out_channels = hidden_channels

        # Define all the convolutional blocks (conv_transposed -> batchnorm -> activation)
        conv_layer_list = []
        for i, (c_in, c_out) in enumerate(zip(in_channels, out_channels)):
            conv_layer = [
                Conv2d(c_in, c_out, 4, 2, 1),
                LeakyReLU(0.2),
            ]
            if i > 0:
                conv_layer.insert(1, BatchNorm2d(c_out))
            conv_layer_list.append(Sequential(*conv_layer))

        self.hidden_layers = Sequential(*conv_layer_list)

        # Define the last layer, i.e. reshape and (512, 4, 4) -> real/fake classification
        final_height = img_size // (2**n_layers)
        final_size = hidden_channels[-1] * (final_height**2)
        self.classifier = Sequential(
            Rearrange("b c h w -> b (c h w)"),
            Linear(final_size, 1, bias=False),
            Sigmoid(),
        )
        # Equivalent, but using conv rather than linear:
        # self.classifier = Sequential(
        #     Conv2d(out_channels[-1], 1, final_height, 1, 0),
        #     Rearrange("b c h w -> b (c h w)"),
        #     Sigmoid(),
        # )

    def forward(self, x: Tensor) -> Tensor:
        x = self.hidden_layers(x)
        x = self.classifier(x)
        return x.squeeze()  # remove dummy `out_channels` dimension
```
</details>


### Exercise - Weight initialisation

> ```yaml
> Difficulty: 🔴🔴⚪⚪⚪
> Importance: 🔵🔵⚪⚪⚪
> 
> You should spend up to 10-15 minutes on this exercise.
> ```

The paper mentions at the end of page 3 that all weights were initialized from a $N(0, 0.02)$ distribution. This applies to the convolutional and convolutional transpose layers' weights (plus the weights in the linear classifier), but the BatchNorm layers' weights should be initialised from $N(1, 0.02)$ (since 1 is their default value). The BatchNorm biases should all be set to zero.

You can fill in the following function to initialise your weights, and call it within the `__init__` method of your DCGAN. (Hint: you can use the functions `nn.init.normal_` and `nn.init.constant_` here.)


```python
def initialize_weights(model: nn.Module) -> None:
    """
    Initializes weights according to the DCGAN paper (details at the end of page 3 of the DCGAN
    paper), by modifying the weights of the model in place.
    """
    raise NotImplementedError()


tests.test_initialize_weights(initialize_weights, ConvTranspose2d, Conv2d, Linear, BatchNorm2d)
```


<details><summary>Solution</summary>

```python
def initialize_weights(model: nn.Module) -> None:
    """
    Initializes weights according to the DCGAN paper (details at the end of page 3 of the DCGAN
    paper), by modifying the weights of the model in place.
    """
    for module in model.modules():
        if isinstance(module, (ConvTranspose2d, Conv2d, Linear)):
            nn.init.normal_(module.weight.data, 0.0, 0.02)
        elif isinstance(module, BatchNorm2d):
            nn.init.normal_(module.weight.data, 1.0, 0.02)
            nn.init.constant_(module.bias.data, 0.0)
```
</details>


Note - the tests for this aren't maximally strict, but don't worry if you don't get things exactly right, since your model will still probably train successfully. If you think you've got the architecture right but your model still isn't training, you might want to return here and check your initialisation.


```python
model = DCGAN().to(device)
x = t.randn(3, 100).to(device)
print(torchinfo.summary(model.netG, input_data=x), end="\n\n")
print(torchinfo.summary(model.netD, input_data=model.netG(x)))
```


<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">==========================================================================================
Layer (type:depth-idx)                   Output Shape              Param #
==========================================================================================
Generator                                [3, 3, 64, 64]            --
├─Sequential: 1-1                        [3, 512, 8, 8]            --
│    └─Linear: 2-1                       [3, 32768]                3,276,800
│    └─Rearrange: 2-2                    [3, 512, 8, 8]            --
│    └─BatchNorm2d: 2-3                  [3, 512, 8, 8]            1,024
│    └─ReLU: 2-4                         [3, 512, 8, 8]            --
├─Sequential: 1-2                        [3, 3, 64, 64]            --
│    └─Sequential: 2-5                   [3, 256, 16, 16]          --
│    │    └─ConvTranspose2d: 3-1         [3, 256, 16, 16]          2,097,152
│    │    └─BatchNorm2d: 3-2             [3, 256, 16, 16]          512
│    │    └─ReLU: 3-3                    [3, 256, 16, 16]          --
│    └─Sequential: 2-6                   [3, 128, 32, 32]          --
│    │    └─ConvTranspose2d: 3-4         [3, 128, 32, 32]          524,288
│    │    └─BatchNorm2d: 3-5             [3, 128, 32, 32]          256
│    │    └─ReLU: 3-6                    [3, 128, 32, 32]          --
│    └─Sequential: 2-7                   [3, 3, 64, 64]            --
│    │    └─ConvTranspose2d: 3-7         [3, 3, 64, 64]            6,144
│    │    └─Tanh: 3-8                    [3, 3, 64, 64]            --
==========================================================================================
Total params: 5,906,176
Trainable params: 5,906,176
Non-trainable params: 0
Total mult-adds (Units.GIGABYTES): 3.31
==========================================================================================
Input size (MB): 0.00
Forward/backward pass size (MB): 11.30
Params size (MB): 23.62
Estimated Total Size (MB): 34.93
==========================================================================================

==========================================================================================
Layer (type:depth-idx)                   Output Shape              Param #
==========================================================================================
Discriminator                            [3]                       --
├─Sequential: 1-1                        [3, 512, 8, 8]            --
│    └─Sequential: 2-1                   [3, 128, 32, 32]          --
│    │    └─Conv2d: 3-1                  [3, 128, 32, 32]          6,144
│    │    └─LeakyReLU: 3-2               [3, 128, 32, 32]          --
│    └─Sequential: 2-2                   [3, 256, 16, 16]          --
│    │    └─Conv2d: 3-3                  [3, 256, 16, 16]          524,288
│    │    └─BatchNorm2d: 3-4             [3, 256, 16, 16]          512
│    │    └─LeakyReLU: 3-5               [3, 256, 16, 16]          --
│    └─Sequential: 2-3                   [3, 512, 8, 8]            --
│    │    └─Conv2d: 3-6                  [3, 512, 8, 8]            2,097,152
│    │    └─BatchNorm2d: 3-7             [3, 512, 8, 8]            1,024
│    │    └─LeakyReLU: 3-8               [3, 512, 8, 8]            --
├─Sequential: 1-2                        [3, 1]                    --
│    └─Rearrange: 2-4                    [3, 32768]                --
│    └─Linear: 2-5                       [3, 1]                    32,768
│    └─Sigmoid: 2-6                      [3, 1]                    --
==========================================================================================
Total params: 2,661,888
Trainable params: 2,661,888
Non-trainable params: 0
Total mult-adds (Units.MEGABYTES): 824.28
==========================================================================================
Input size (MB): 0.15
Forward/backward pass size (MB): 7.86
Params size (MB): 10.65
Estimated Total Size (MB): 18.66
==========================================================================================
</pre>


## Training loop

Recall, the goal of training the discriminator is to maximize the probability of correctly classifying a given input as real or fake. The goal of the generator is to produce images to fool the discriminator. This is framed as a **minimax game**, where the discriminator and generator try to solve the following:
$$
\min_G \max_D V(D, G)=\mathbb{E}_x[\log (D(x))]+\mathbb{E}_z[\log (1-D(G(z)))]
$$
where $D$ is the discriminator function mapping an image to a probability estimate for whether it is real, and $G$ is the generator function which produces an image from latent vector $z$.

The literature on minimax games is extensive, so we won't go into it here. It's better to understand this formula on an intuitive level:

* Given a fixed $G$ (generator), the goal of the discriminator is to produce high values for $D$ when fed real images $x$, and low values when fed fake images $G(z)$.
* The generator $G$ is searching for a strategy where, even if the discriminator $D$ was optimal, it would still find it hard to distinguish between real and fake images with high confidence.

Since we can't know the true distribution of $x$, we instead estimate the expression above by calculating it over a batch of real images $x$ (and some random noise $z$). This gives us a loss function to train against (since $D$ wants to maximise this value, and $G$ wants to minimise this value). For each batch, we perform gradient descent on the discriminator and then on the generator.

</details>


### Training the discriminator

We take the following steps:

* Zero the gradients of $D$.
    * This is important because if the last thing we did was evaluate $D(G(z))$ (in order to update the parameters of $G$), then $D$ will have stored gradients from that backward pass.
* Generate random noise $z$, and compute $D(G(z))$. Take the average of $\log(1 - D(G(z)))$, and we have the first part of our loss function.
    * Note - you can use the same random noise (and even the same fake image) as in the generator step. But make sure you're using the detached version, because we don't want gradients to propagate back through the generator!
* Take the real images  $x$ in the current batch, and use that to compute $\log(D(x))$. This gives us the second part of our loss function.
* We now add the two terms together, and perform gradient ascent (since we're trying to maximise this expression).
    * You can perform gradient ascent by either flipping the sign of the thing you're doing a backward pass on, or passing the keyword argument `maximize=True` when defining your optimiser (all optimisers have this option).

Tip - when calculating $D(G(z))$, for the purpose of training the discriminator, it's best to first calculate $G(z)$ then call `detach` on this tensor before passing it to $D$. This is because you then don't need to worry about gradients accumulating for $G$.


### Training the generator

We take the following steps:

* Zero the gradients of $G$.
* Generate random noise $z$, and compute $D(G(z))$.
* We **don't** use $\log(1 - D(G(z)))$ to calculate our loss function, instead we use $\log(D(G(z)))$ (and gradient ascent).

**Question - can you explain why we use $\log(D(G(z))$? (The Google reading material mentions this but doesn't really explain it.)**

<details>
<summary>Answer</summary>

Early in learning, when the generator is really bad at producing realistic images, it will be easy for the discriminator to distinguish between them. So $\log(1 - D(G(z)))$ will be very close to $\log(1) = 0$. The gradient of $\log$ at this point is quite flat, so there won't be a strong gradient with which to train $G$. To put it another way, a marginal improvement in $G$ will have very little effect on the loss function. On the other hand, $\log(D(G(z)))$ tends to negative infinity as $D(G(z))$ gets very small. So the gradients here are very steep, and a small improvement in $G$ goes a long way.

It's worth emphasising that these two functions are both monotonic in opposite directions, so maximising one is equivalent to minimising the other. We haven't changed anything fundamental about how the GAN works; this is just a trick to help with gradient descent.
</details>


Note - PyTorch's [`BCELoss`](https://pytorch.org/docs/stable/generated/torch.nn.BCELoss.html) clamps its log function outputs to be greater than or equal to -100. This is because in principle our loss function could be negative infinity (if we take log of zero). You might find you need to employ a similar trick if you're manually computing the log of probabilities. Aside from the clamping, the following two code snippets are equivalent:

```python
# Calculating loss manually, without clamping:
loss = - t.log(D_G_z)

# Calculating loss with clamping behaviour:
labels_real = t.ones_like(D_G_z)
loss = nn.BCELoss()(D_G_z, labels_real)
```


### Optimizers

The generator and discriminator will have separate optimizers (this makes sense, since we'll have separate training steps for these two, and both are "trying" to optimize different things). The [paper](https://arxiv.org/abs/1511.06434v2) describes using an Adam optimizer with learning rate 0.0002, and momentum parameters $\beta_1 = 0.5, \beta_2 = 0.999$. This is set up for you already, in the `__init__` block below.


### Gradient Clipping

Gradient clipping is a useful technique for improving the stability of certain training loops, especially those like DCGANs which have potentially unstable loss functions. The idea is that you clip the gradients of your weights to some fixed threshold during backprop, and use these clipped gradients to update the weights. This can be done using [`nn.utils.clip_grad_norm`](https://pytorch.org/docs/stable/generated/torch.nn.utils.clip_grad_norm_.html), which is called between the `loss.backward()` and `optimizer.step()` methods (since it directly modifies the `.grad` attributes of your weights). You shouldn't find this absolutely necessary to train your models, however it might help to clip the gradients to a value like `1.0` for your generator & discriminator. We've given you this as an optional parameter to use in your `DCGANArgs` dataclass.


### Exercise - implement GAN training loop

> ```yaml
> Difficulty: 🔴🔴🔴🔴⚪
> Importance: 🔵🔵🔵🔵⚪
> 
> You should spend up to 30-45 minutes on this exercise.
> ```

You should now implement your training loop below. We've filled in the `__init__` method for you, as well as `log_samples` method which determines the core structure of the training loop. Your task is to:

* Fill in the two functions `training_step_discriminator` and `training_step_generator`, which perform a single gradient step on the discriminator and generator respectively.
    * Note that the discriminator training function takes two arguments: the real and fake image (in the notation above, $x$ and $z$), because it trains to distinguish real and fake. The generator training function only takes the fake image $z$, because it trains to fool the discriminator.
    * Also note, you should increment `self.step` only once per (discriminator & generator) step, not for both.
* Fill in the `train` method, which should perform the training loop over the number of epochs specified in `args.epochs`. This will be similar to previous training loops, but with a few key differences we'll highlight here:
    * You'll need to compute both losses from `training_step_generator` and `training_step_discriminator`. For the former you should pass in just the fake image (you're only training the generator to produce better fake images), for the latter you should pass in the real image and the **detached fake image** i.e. `img.detach()` (because you're training the discriminator to tell real from fake, and you don't want gradients propagating back to the generator).
        * The fake image should be created from random noise `t.randn(batch_size, latent_dim_size)` and passing it into your generator.
    * Once again the trainloader gives us an iterable of `(img, label)` but we don't need to use the labels (because all these images are real, and that's all we care about).

Again, we recommend not using `wandb` until you've got your non-wandb based code working without errors. Once the generator loss is going down (or at least not exploding!) then you can enable it. However, an important note - **generator loss going down is does not imply the model is working, and vice-versa!** For training systems as unstable as GANs, the best you can do is often just inspecting the output. Although it varies depending on details of the hardware and dataset & model you're training with, at least for these exercises if your generator's output doesn't resemble anything like a face after the first epoch, then something's probably going wrong in your code.


```python
@dataclass
class DCGANArgs:
    """
    Class for the arguments to the DCGAN (training and architecture).
    Note, we use field(defaultfactory(...)) when our default value is a mutable object.
    """

    # architecture
    latent_dim_size: int = 100
    hidden_channels: list[int] = field(default_factory=lambda: [128, 256, 512])

    # data & training
    dataset: Literal["MNIST", "CELEB"] = "CELEB"
    batch_size: int = 64
    epochs: int = 3
    lr: float = 0.0002
    betas: tuple[float, float] = (0.5, 0.999)
    clip_grad_norm: float | None = 1.0

    # logging
    use_wandb: bool = False
    wandb_project: str | None = "day5-gan"
    wandb_name: str | None = None
    log_every_n_steps: int = 250


class DCGANTrainer:
    def __init__(self, args: DCGANArgs):
        self.args = args
        self.trainset = get_dataset(self.args.dataset)
        self.trainloader = DataLoader(self.trainset, batch_size=args.batch_size, shuffle=True, num_workers=8)

        batch, img_channels, img_height, img_width = next(iter(self.trainloader))[0].shape
        assert img_height == img_width

        self.model = DCGAN(args.latent_dim_size, img_height, img_channels, args.hidden_channels).to(device).train()
        self.optG = t.optim.Adam(self.model.netG.parameters(), lr=args.lr, betas=args.betas)
        self.optD = t.optim.Adam(self.model.netD.parameters(), lr=args.lr, betas=args.betas)

    def training_step_discriminator(
        self,
        img_real: Float[Tensor, "batch channels height width"],
        img_fake: Float[Tensor, "batch channels height width"],
    ) -> Float[Tensor, ""]:
        """
        Generates a real and fake image, and performs a gradient step on the discriminator to
        maximize log(D(x)) + log(1-D(G(z))). Logs to wandb if enabled.
        """
        raise NotImplementedError()

    def training_step_generator(self, img_fake: Float[Tensor, "batch channels height width"]) -> Float[Tensor, ""]:
        """
        Performs a gradient step on the generator to maximize log(D(G(z))). Logs to wandb if enabled.
        """
        raise NotImplementedError()

    @t.inference_mode()
    def log_samples(self) -> None:
        """
        Performs evaluation by generating 8 instances of random noise and passing them through the
        generator, then optionally logging the results to Weights & Biases.
        """
        assert self.step > 0, "First call should come after a training step. Remember to increment `self.step`."
        self.model.netG.eval()

        # Generate random noise
        t.manual_seed(42)
        noise = t.randn(10, self.model.latent_dim_size).to(device)
        # Get generator output
        output = self.model.netG(noise)
        # Clip values to make the visualization clearer
        output = output.clamp(output.quantile(0.01), output.quantile(0.99))
        # Log to weights and biases
        if self.args.use_wandb:
            output = einops.rearrange(output, "b c h w -> b h w c").cpu().numpy()
            wandb.log({"images": [wandb.Image(arr) for arr in output]}, step=self.step)
        else:
            display_data(output, nrows=1, title="Generator-produced images")

        self.model.netG.train()

    def train(self) -> DCGAN:
        """Performs a full training run."""
        self.step = 0
        if self.args.use_wandb:
            wandb.init(project=self.args.wandb_project, name=self.args.wandb_name)

        for epoch in range(self.args.epochs):
            progress_bar = tqdm(self.trainloader, total=len(self.trainloader), ascii=True)

            for img_real, label in progress_bar:
                # YOUR CODE HERE - fill in the training step for generator & discriminator

        if self.args.use_wandb:
            wandb.finish()

        return self.model
```


<details>
<summary>Help - I'm getting OOMs/crashes when I try to use the trainloader</summary>

This is a known issue on MacOS machines. To fix this, try adding `multiprocessing_context="fork"` to your `DataLoader` instantiation.

</details>

<details>
<summary>Solution</summary>

```python
def training_step_discriminator(
    self,
    img_real: Float[Tensor, "batch channels height width"],
    img_fake: Float[Tensor, "batch channels height width"],
) -> Float[Tensor, ""]:
    """
    Generates a real and fake image, and performs a gradient step on the discriminator to maximize
    log(D(x)) + log(1-D(G(z))). Logs to wandb if enabled.
    """
    # Zero gradients
    self.optD.zero_grad()

    # Calculate D(x) and D(G(z)), for use in the objective function
    D_x = self.model.netD(img_real)
    D_G_z = self.model.netD(img_fake)

    # Calculate loss
    lossD = -(t.log(D_x).mean() + t.log(1 - D_G_z).mean())

    # Gradient descent step (with optional clipping)
    lossD.backward()
    if self.args.clip_grad_norm is not None:
        nn.utils.clip_grad_norm_(self.model.netD.parameters(), self.args.clip_grad_norm)
    self.optD.step()

    if self.args.use_wandb:
        wandb.log(dict(lossD=lossD), step=self.step)
    return lossD


def training_step_generator(self, img_fake: Float[Tensor, "batch channels height width"]) -> Float[Tensor, ""]:
    """
    Performs a gradient step on the generator to maximize log(D(G(z))). Logs to wandb if enabled.
    """
    # Zero gradients
    self.optG.zero_grad()

    # Calculate D(G(z)), for use in the objective function
    D_G_z = self.model.netD(img_fake)

    # Calculate loss
    lossG = -(t.log(D_G_z).mean())

    # Gradient descent step (with optional clipping)
    lossG.backward()
    if self.args.clip_grad_norm is not None:
        nn.utils.clip_grad_norm_(self.model.netG.parameters(), self.args.clip_grad_norm)
    self.optG.step()

    if self.args.use_wandb:
        wandb.log(dict(lossG=lossG), step=self.step)
    return lossG


def train(self) -> DCGAN:
    """Performs a full training run."""
    self.step = 0
    if self.args.use_wandb:
        wandb.init(project=self.args.wandb_project, name=self.args.wandb_name)

    for epoch in range(self.args.epochs):
        progress_bar = tqdm(self.trainloader, total=len(self.trainloader), ascii=True)

        for img_real, label in progress_bar:
            # Generate random noise & fake image
            noise = t.randn(self.args.batch_size, self.args.latent_dim_size).to(device)
            img_real = img_real.to(device)
            img_fake = self.model.netG(noise)

            # Training steps
            lossD = self.training_step_discriminator(img_real, img_fake.detach())
            lossG = self.training_step_generator(img_fake)

            # Update progress bar
            self.step += 1
            progress_bar.set_description(f"{epoch=}, {lossD=:.4f}, {lossG=:.4f}, batches={self.step}")

            # Log batch of data
            if self.step % self.args.log_every_n_steps == 0:
                self.log_samples()

    if self.args.use_wandb:
        wandb.finish()

    return self.model
```

</details>


Once you've written your code, here are some default arguments for MNIST and CelebA you can try out.

Note that the MNIST model is very small in comparison to CelebA - if you make it any larger, you fall into a very common GAN failure mode where the discriminator becomes perfect (loss goes to zero) and the generator is unable to get a gradient signal to produce better images - see next section for a discussion of this. Larger architectures are generally more likely to fall into this failure mode, and empirically it seems to happen more for MNIST than for CelebA which is why we generally recommend using the CelebA dataset & architecture for this exercise - although this failure mode can happen in both cases!


```python
# Arguments for CelebA
args = DCGANArgs(
    dataset="CELEB",
    hidden_channels=[128, 256, 512],
    batch_size=32,  # if you get OOM errors, reduce this!
    epochs=5,
    use_wandb=False,
)
trainer = DCGANTrainer(args)
dcgan = trainer.train()
```


<details>
<summary>Click to see an example of the output you should be producing by the end of this CelebA training run.</summary>

Here was my output after 250 batches (8000 images):

<img src="https://raw.githubusercontent.com/info-arena/ARENA_img/main/misc/celeb-gans-1.png" width="700">

After 2000 batches (64000 images):

<img src="https://raw.githubusercontent.com/info-arena/ARENA_img/main/misc/celeb-gans-2.png" width="700">

And after the end of training (5 epochs, approx 625k images):

<img src="https://raw.githubusercontent.com/info-arena/ARENA_img/main/misc/celeb-gans-3.png" width="700">

</details>


```python
# Arguments for MNIST
args = DCGANArgs(
    dataset="MNIST",
    hidden_channels=[12, 24],
    epochs=20,
    batch_size=128,
    use_wandb=False,
)
trainer = DCGANTrainer(args)
dcgan = trainer.train()
```


<details>
<summary>Click to see an example of the output you should be producing by the end of this MNIST training run.</summary>

Here was my output after 250 batches (32k images):

<img src="https://raw.githubusercontent.com/info-arena/ARENA_img/main/misc/mnist-gans-1.png" width="700">

After 2000 batches (256k images):

<img src="https://raw.githubusercontent.com/info-arena/ARENA_img/main/misc/mnist-gans-2.png" width="700">

About 90% of the way through training, it was achieving the best results:

<img src="https://raw.githubusercontent.com/info-arena/ARENA_img/main/misc/mnist-gans-3.png" width="700">

However after this point it broke, and produced NaNs from both the discriminator and the generator:

<img src="https://raw.githubusercontent.com/info-arena/ARENA_img/main/misc/mnist-gans-nan.png" width="900">

This is a common problem for training GANs - they're just a pretty cursed architecture! Read on for more on this.

</details>


### Fixing bugs

GANs are notoriously hard to get exactly right. I ran into quite a few bugs myself building this architecture, and I've tried to mention them somewhere on this page to help participants avoid them. If you run into a bug and are able to fix it, please send it to me and I can add it here, for the benefit of everyone else!

* Make sure you apply the layer normalization (mean 0, std dev 0.02) to your linear layers as well as your convolutional layers.
* More generally, in your function to initialise the weights of your network, make sure no layers are being missed out. The easiest way to do this is to inspect your model afterwards (i.e. loop through all the params, printing out their mean and std dev).

Also, you might find [this page](https://github.com/soumith/ganhacks) useful. It provides several tips and tricks for how to make your GAN work (many of which we've already mentioned on this page).


## Why so unstable during training?

If you try training your GAN on MNIST, you might find that it eventually blows up (with close to zero discriminator loss, and spiking generator loss - possibly even gradients large enough to overflow and lead to `nan` values). This might also happen if you train on CelebA but your architecture is too big, or even if you train with a reasonably-sized architecture but for too long!

This is a common problem with GANs, which are notoriously unstable to train. Essentially, the discriminator gets so good at its job that the generator can't latch onto a good gradient for improving its performance. Although the theoretical formulation of GANs as a minimax game is elegant, there are quite a few assumptions that have to go into it in order for there to be one theoretical optimum involving the generator producing perfect images - and in practice this is rarely achieved, even in the limit.

Different architectures like diffusion models and VAEs are generally more stable, although many of the most advanced image generation architectures do still take important conceptual ideas from the GAN framework.


## Bonus - Smooth interpolation

Suppose you take two vectors in the latent space. If you use your generator to create output at points along the linear interpolation between these vectors, your image will change continuously (because it is a continuous function of the latent vector), but it might look very different at the start and the end. Can you create any cool animations from this?

Instead of linearly interpolating between two vectors, you could try applying a [rotation matrix](https://en.wikipedia.org/wiki/Rotation_matrix) to a vector (this has the advantage of keeping the interpolated vector "in distribution", since the rotation between two standard normally distributed vectors is also standard normal, whereas the linear interpolation isn't). Are the results better?




=== NEW CHAPTER ===


# 3️⃣ Bonus - Transposed Convolutions



> ##### Learning Objectives
>
> - Learn about & implement the transposed convolution operation.
> - Implement GANs and/or VAEs entirely from scratch.

## Transposed convolutions

In this section, we'll build all the modules required to implement our DCGAN.

> Note - this section is similar in flavour to the bonus exercises from the "CNNs & ResNets" chapter, i.e. you'll be implementing transposed convolutions using low-level stride and tensor manipulation operations. That section should be considered a prerequisite for this one.

Now, **what are transposed convolutions, and why should we care about them?** One high-level intuition goes something like this: most of the generator's architecture is basically the discriminator architecture in reverse. We need something that performs the reverse of a convolution - not literally the inverse operation, but something reverse in spirit, which uses a kernel of weights to project up to some array of larger size.

**Importantly, a transposed convolution isn't literally the inverse of a convolution**. A lot of confusion can come from misunderstanding this!

You can describe the difference between convolutions and transposed convolutions as follows:

* In convolutions, you slide the kernel around inside the input. At each position of the kernel, you take a sumproduct between the kernel and that section of the input to calculate a single element in the output.
* In transposed convolutions, you slide the kernel around what will eventually be your output, and at each position you add some multiple of the kernel to your output.

Below is an illustration of both for comparison, in the 1D case (where $*$ stands for the 1D convolution operator, and $*^T$ stands for the transposed convolution operator). Note the difference in size between the output in both cases. With standard convolutions, our output is smaller than our input, because we're having to fit the kernel inside the input in order to produce the output. But in our transposed convolutions, the output is actually larger than the input, because we're fitting the kernel inside the output.

<img src="https://raw.githubusercontent.com/info-arena/ARENA_img/main/misc/convtranspose-1.png" width="700">


<details>
<summary>Question - what do you think the formula is relating <code>input_size</code>, <code>kernel_size</code> and <code>output_size</code> in the case of 1D convolutions (with no padding or stride)?</summary>

The formula is `output_size = input_size + kernel_size - 1`.
        
Note how this exactly mirrors the equation in the convolutional case; it's identical if we swap around `output_size` and `input_size`.
</details>

<br>

Now, consider the elements in the output of the transposed convolution: `z+4y+3x, 4x+3y-2x`, etc. Note that these look a bit like convolutions, since they're inner products of slices of the input with versions of the kernel. This observation leads nicely into why transposed convolutions are called transposed convolutions - because they can actually be written as convolutions, just with a slightly modified input and kernel.

<details>
<summary>Question - how can this operation be cast as a convolution? In other words, exactly what arrays <code>input</code> and <code>kernel</code> would produce the same output as the transposed convolution above, if we performed a standard convolution on them?</summary>

From looking at the diagram, note that the final output (the blue row at the bottom) looks a bit like sliding the _reversed_ kernel over the input. In other words, we get elements like `z+4y+3x` which are an inner product between the input slice `input[:3] = [1, 4, 3]` and the reversed kernel `[z, y, x]`. This suggests we should be using the reversed kernel in our convolution.

Can we just use a reversed kernel on our original input and call it a day? No, because the output size wouldn't be correct. Using a reversed kernel on our original input would give us just the two elements `[z+4y+3x, 4z+3y-2x]`, not the full 6-element output we actually get. The answer is that we need to pad out our input with zeros on the left and right, with the padding amount equal to `kernel_size - 1`. 

To conclude - with `input_modified = pad(input, kernel_size-1)` and `kernel_modified = kernel[::-1]`, we get:

<img src="https://raw.githubusercontent.com/info-arena/ARENA_img/main/misc/convtranspose-2A.png" width="850">

Note - it's also valid to say we use the original kernel and pad & flip the input, but for the exercises below we'll stick to the former interpretation.

</details>

> 

<!-- <details>
<summary>Hint</summary>

Let `input_mod` and `kernel_mod` be the modified versions of the input and kernel, to be used in the convolution.

You should be able to guess what `kernel_mod` is by looking at the diagram.

Also, from the formula for transposed convolutions, we must have:

```
output_size = input_mod_size + kernel_mod_size - 1
```

But we currently have:

```
output_size = input_size - kernel_size + 1
```

which should help you figure out what size `input_mod` needs to be, relative to `input`.
</details>

<details>
<summary>Hint 2</summary>

`kernel_mod` should be the same size as kernel (but altered in a particular way). `input_mod` should be formed by padding `input`, so that its size increases by `2 * (kernel_size - 1)`.
</details>

<details>
<summary>Answer</summary>

If you create `input_mod` by padding `input` with exactly `kernel_size - 1` zeros on either side, and reverse your kernel to create `kernel_mod`, then the convolution of these modified arrays equals your original transposed convolution output.

<img src="https://raw.githubusercontent.com/info-arena/ARENA_img/main/misc/convtranspose-2A.png" width="850">

</details> -->


### Exercise - minimal 1D transposed convolutions

> ```yaml
> Difficulty: 🔴🔴🔴🔴⚪
> Importance: 🔵🔵⚪⚪⚪
> 
> You should spend up to 15-25 minutes on this exercise.
> ```

Now, you should implement the function `conv_transpose1d_minimal`. You're allowed to call functions like `conv1d_minimal` and `pad1d` which you wrote previously (if you didn't do these exercises, then you can import the solution versions of them - although we do recommend doing the conv from scratch exercises before these ones).

One important note - in our convolutions we assumed the kernel had shape `(out_channels, in_channels, kernel_width)`. Here, the order is different: `in_channels` comes before `out_channels`.


```python
from part2_cnns.solutions import (
    IntOrPair,
    conv1d_minimal,
    conv2d_minimal,
    force_pair,
    pad1d,
    pad2d,
)


def conv_transpose1d_minimal(
    x: Float[Tensor, "batch in_channels width"],
    weights: Float[Tensor, "in_channels out_channels kernel_width"],
) -> Float[Tensor, "batch out_channels output_width"]:
    """Like torch's conv_transpose1d using bias=False and all other keyword arguments left at their default values."""
    raise NotImplementedError()


tests.test_conv_transpose1d_minimal(conv_transpose1d_minimal)
```


<details><summary>Solution</summary>

```python
from part2_cnns.solutions import (
    IntOrPair,
    conv1d_minimal,
    conv2d_minimal,
    force_pair,
    pad1d,
    pad2d,
)


def conv_transpose1d_minimal(
    x: Float[Tensor, "batch in_channels width"],
    weights: Float[Tensor, "in_channels out_channels kernel_width"],
) -> Float[Tensor, "batch out_channels output_width"]:
    """Like torch's conv_transpose1d using bias=False and all other keyword arguments left at their default values."""
    batch, in_channels, width = x.shape
    in_channels_2, out_channels, kernel_width = weights.shape
    assert in_channels == in_channels_2, "in_channels for x and weights don't match up"

    x_mod = pad1d(x, left=kernel_width - 1, right=kernel_width - 1, pad_value=0)
    weights_mod = einops.rearrange(weights.flip(-1), "i o w -> o i w")

    return conv1d_minimal(x_mod, weights_mod)
```
</details>


### Exercise - 1D transposed convolutions

> ```yaml
> Difficulty: 🔴🔴🔴🔴🔴
> Importance: 🔵🔵⚪⚪⚪
> 
> You should spend up to 25-40 minutes on this exercise.
> ```

Now we add in the extra parameters `padding` and `stride`, just like we did for our convolutions back in week 0.

The basic idea is that both parameters mean the inverse of what they did in for convolutions.

In convolutions, `padding` tells you how much to pad the input by. But in transposed convolutions, we pad the input by `kernel_size - 1 - padding` (recall that we're already padding by `kernel_size - 1` by default). So padding decreases our output size rather than increasing it.

In convolutions, `stride` tells you how much to step the kernel by, as it's being moved around inside the input. In transposed convolutions, stride does something different: you space out all your input elements by an amount equal to `stride` before performing your transposed convolution. This might sound strange, but **it's actually equivalent to performing strides as you're moving the kernel around inside the output.** This diagram should help show why:

<img src="https://raw.githubusercontent.com/info-arena/ARENA_img/main/misc/convtranspose-3.png" width="750">

For this reason, transposed convolutions are also referred to as **fractionally strided convolutions**, since a stride of 2 over the output is equivalent to a 1/2 stride over the input (i.e. every time the kernel takes two steps inside the spaced-out version of the input, it moves one stride with reference to the original input).

**Question - what is the formula relating output size, input size, kernel size, stride and padding? (note, you shouldn't need to refer to this explicitly in your functions)**

<details>
<summary>Answer</summary>

Without any padding, we had:

```
output_size = input_size + kernel_size - 1
```

Twice the `padding` parameter gets subtracted from the RHS (since we pad by the same amount on each side), so this gives us:

```
output_size = input_size + kernel_size - 1 - 2 * padding
```

Finally, consider `stride`. As mentioned above, we can consider stride here to have the same effect as "spacing out" elements in the input. Each non-zero element will be `stride - 1` positions apart (for instance, `stride = 2` turns `[1, 2, 3]` into `[1, 0, 2, 0, 3]`). You can check that the number of zeros added between elements equals `(input_size - 1) * (stride - 1)`. When you add this to the right hand side, and simplify, you are left with:

```
output_size = (input_size - 1) * stride + kernel_size - 2 * padding
```
</details>

Padding should be pretty easy for you to implement on top of what you've already done. For strides, you will need to construct a strided version of the input which is "spaced out" in the way described above, before performing the transposed convolution. It might help to write a `fractional_stride` function; we've provided the code for you to do this.


```python
def fractional_stride_1d(
    x: Float[Tensor, "batch in_channels width"], stride: int = 1
) -> Float[Tensor, "batch in_channels output_width"]:
    """
    Returns a version of x suitable for transposed convolutions, i.e. "spaced out" with zeros
    between its values. This spacing only happens along the last dimension.

    x: shape (batch, in_channels, width)

    Example:
        x = [[[1, 2, 3], [4, 5, 6]]]
        stride = 2
        output = [[[1, 0, 2, 0, 3], [4, 0, 5, 0, 6]]]
    """
    raise NotImplementedError()


tests.test_fractional_stride_1d(fractional_stride_1d)
```


<details>
<summary>Help - I'm not sure how to implement <code>fractional_stride</code>.</summary>

The easiest way is to initialise an array of zeros with the appropriate size, then slicing to set its elements from `x`.

Warning - if you do it this way, **make sure the output has the same device as `x`**.
</details>


<details><summary>Solution</summary>

```python
def fractional_stride_1d(
    x: Float[Tensor, "batch in_channels width"], stride: int = 1
) -> Float[Tensor, "batch in_channels output_width"]:
    """
    Returns a version of x suitable for transposed convolutions, i.e. "spaced out" with zeros
    between its values. This spacing only happens along the last dimension.

    x: shape (batch, in_channels, width)

    Example:
        x = [[[1, 2, 3], [4, 5, 6]]]
        stride = 2
        output = [[[1, 0, 2, 0, 3], [4, 0, 5, 0, 6]]]
    """
    batch, in_channels, width = x.shape
    width_new = width + (stride - 1) * (
        width - 1
    )  # the RHS of this sum is the number of zeros we need to add between elements
    x_new_shape = (batch, in_channels, width_new)

    # Create an empty array to store the spaced version of x in.
    x_new = t.zeros(size=x_new_shape, dtype=x.dtype, device=x.device)

    x_new[..., ::stride] = x

    return x_new
```
</details>


```python
def conv_transpose1d(
    x: Float[Tensor, "batch in_channels width"],
    weights: Float[Tensor, "in_channels out_channels kernel_width"],
    stride: int = 1,
    padding: int = 0,
) -> Float[Tensor, "batch out_channels output_width"]:
    """
    Like torch's conv_transpose1d using bias=False and all other keyword arguments left at their
    default values.
    """
    raise NotImplementedError()


tests.test_conv_transpose1d(conv_transpose1d)
```


<details>
<summary>Help - I'm not sure how to implement <code>conv_transpose1d</code>.</summary>

There are three things you need to do:

* Modify `x` by "spacing it out" with `fractional_stride_1d` and padding it the appropriate amount
* Modify `weights` (just like you did for `conv_transpose1d_minimal`)
* Use `conv1d_minimal` on your modified `x` and `weights` (just like you did for `conv_transpose1d_minimal`)
</details>


<details><summary>Solution</summary>

```python
def conv_transpose1d(
    x: Float[Tensor, "batch in_channels width"],
    weights: Float[Tensor, "in_channels out_channels kernel_width"],
    stride: int = 1,
    padding: int = 0,
) -> Float[Tensor, "batch out_channels output_width"]:
    """
    Like torch's conv_transpose1d using bias=False and all other keyword arguments left at their
    default values.
    """
    batch, ic, width = x.shape
    ic_2, oc, kernel_width = weights.shape
    assert ic == ic_2, f"in_channels for x and weights don't match up. Shapes are {x.shape}, {weights.shape}."

    # Apply spacing
    x_spaced_out = fractional_stride_1d(x, stride)

    # Apply modification (which is controlled by the padding parameter)
    padding_amount = kernel_width - 1 - padding
    assert padding_amount >= 0, "total amount padded should be positive"
    x_mod = pad1d(x_spaced_out, left=padding_amount, right=padding_amount, pad_value=0)

    # Modify weights, then return the convolution
    weights_mod = einops.rearrange(weights.flip(-1), "i o w -> o i w")

    return conv1d_minimal(x_mod, weights_mod)
```
</details>


Another fun fact about transposed convolutions - they are also called **backwards strided convolutions**, because they are equivalent to taking the gradient of Conv2d with respect to its output. As an optional bonus, can you formally prove this?


### Exercise - 2D transposed convolutions

> ```yaml
> Difficulty: 🔴🔴🔴🔴⚪
> Importance: 🔵⚪⚪⚪⚪
> 
> You should spend up to 10-20 minutes on this exercise.
> ```

Finally, we get to 2D transposed convolutions! Since there's no big conceptual difference between this and the 1D case, we'll jump straight to implementing the full version of these convolutions, with padding and strides. A few notes:

* You'll need to make `fractional_stride_2d`, which performs spacing along the last two dimensions rather than just the last dimension.
* Defining the modified version of your kernel will involve reversing on more than one dimension. You'll still need to perform the same rearrangement flipping the output and input channel dimensions though.
* You can use the `force_pair` function from earlier this week (it's been imported for you, as have the `Pair` and `IntOrPair` types).


```python
def fractional_stride_2d(
    x: Float[Tensor, "batch in_channels height width"], stride_h: int, stride_w: int
) -> Float[Tensor, "batch in_channels output_height output_width"]:
    """
    Same as fractional_stride_1d, except we apply it along the last 2 dims of x (height and width).
    """
    raise NotImplementedError()


def conv_transpose2d(x, weights, stride: IntOrPair = 1, padding: IntOrPair = 0) -> Tensor:
    """Like torch's conv_transpose2d using bias=False
    x: shape (batch, in_channels, height, width)
    weights: shape (out_channels, in_channels, kernel_height, kernel_width)
    Returns: shape (batch, out_channels, output_height, output_width)
    """
    raise NotImplementedError()


tests.test_fractional_stride_2d(fractional_stride_2d)
tests.test_conv_transpose2d(conv_transpose2d)
```


<details><summary>Solution</summary>

```python
def fractional_stride_2d(
    x: Float[Tensor, "batch in_channels height width"], stride_h: int, stride_w: int
) -> Float[Tensor, "batch in_channels output_height output_width"]:
    """
    Same as fractional_stride_1d, except we apply it along the last 2 dims of x (height and width).
    """
    batch, in_channels, height, width = x.shape
    width_new = width + (stride_w - 1) * (width - 1)
    height_new = height + (stride_h - 1) * (height - 1)
    x_new_shape = (batch, in_channels, height_new, width_new)

    # Create an empty array to store the spaced version of x in.
    x_new = t.zeros(size=x_new_shape, dtype=x.dtype, device=x.device)

    x_new[..., ::stride_h, ::stride_w] = x

    return x_new


def conv_transpose2d(x, weights, stride: IntOrPair = 1, padding: IntOrPair = 0) -> Tensor:
    """Like torch's conv_transpose2d using bias=False
    x: shape (batch, in_channels, height, width)
    weights: shape (out_channels, in_channels, kernel_height, kernel_width)
    Returns: shape (batch, out_channels, output_height, output_width)
    """
    stride_h, stride_w = force_pair(stride)
    padding_h, padding_w = force_pair(padding)

    batch, ic, height, width = x.shape
    ic_2, oc, kernel_height, kernel_width = weights.shape
    assert ic == ic_2, f"in_channels for x and weights don't match up. Shapes are {x.shape}, {weights.shape}."

    # Apply spacing
    x_spaced_out = fractional_stride_2d(x, stride_h, stride_w)

    # Apply modification (which is controlled by the padding parameter)
    pad_h_actual = kernel_height - 1 - padding_h
    pad_w_actual = kernel_width - 1 - padding_w
    assert min(pad_h_actual, pad_w_actual) >= 0, "total amount padded should be positive"
    x_mod = pad2d(
        x_spaced_out,
        left=pad_w_actual,
        right=pad_w_actual,
        top=pad_h_actual,
        bottom=pad_h_actual,
        pad_value=0,
    )

    # Modify weights
    weights_mod = einops.rearrange(weights.flip(-1, -2), "i o h w -> o i h w")

    # Return the convolution
    return conv2d_minimal(x_mod, weights_mod)
```
</details>


### Exercise - transposed conv module

> ```yaml
> Difficulty: 🔴🔴⚪⚪⚪
> Importance: 🔵🔵⚪⚪⚪
> 
> You should spend up to 10-15 minutes on this exercise.
> ```

Now that you've written a function to calculate the convolutional transpose, you should implement it as a module just like you've done for `Conv2d` previously. Your weights should be initialised with the uniform distribution `Unif[-sqrt(k), sqrt(k)]` where `k = 1 / (out_channels * kernel_width * kernel_height)` (this is PyTorch's standard behaviour for convolutional transpose layers).


```python
class ConvTranspose2d(nn.Module):
    def __init__(
        self,
        in_channels: int,
        out_channels: int,
        kernel_size: IntOrPair,
        stride: IntOrPair = 1,
        padding: IntOrPair = 0,
    ):
        """
        Same as torch.nn.ConvTranspose2d with bias=False.
        Name your weight field `self.weight` for compatibility with the tests.
        """
        super().__init__()

        self.in_channels = in_channels
        self.out_channels = out_channels
        self.kernel_size = force_pair(kernel_size)
        self.stride = stride
        self.padding = padding

        raise NotImplementedError()

    def forward(
        self, x: Float[Tensor, "batch in_channels height width"]
    ) -> Float[Tensor, "batch out_channels output_height output_width"]:
        raise NotImplementedError()

    def extra_repr(self) -> str:
        keys = ["in_channels", "out_channels", "kernel_size", "stride", "padding"]
        return ", ".join([f"{key}={getattr(self, key)}" for key in keys])


tests.test_ConvTranspose2d(ConvTranspose2d)
```


<details><summary>Solution</summary>

```python
class ConvTranspose2d(nn.Module):
    def __init__(
        self,
        in_channels: int,
        out_channels: int,
        kernel_size: IntOrPair,
        stride: IntOrPair = 1,
        padding: IntOrPair = 0,
    ):
        """
        Same as torch.nn.ConvTranspose2d with bias=False.
        Name your weight field `self.weight` for compatibility with the tests.
        """
        super().__init__()

        self.in_channels = in_channels
        self.out_channels = out_channels
        self.kernel_size = force_pair(kernel_size)
        self.stride = stride
        self.padding = padding

        sf = 1 / (self.out_channels * self.kernel_size[0] * self.kernel_size[1]) ** 0.5
        self.weight = nn.Parameter(sf * (2 * t.rand(in_channels, out_channels, *self.kernel_size) - 1))

    def forward(
        self, x: Float[Tensor, "batch in_channels height width"]
    ) -> Float[Tensor, "batch out_channels output_height output_width"]:
        return conv_transpose2d(x, self.weight, self.stride, self.padding)

    def extra_repr(self) -> str:
        keys = ["in_channels", "out_channels", "kernel_size", "stride", "padding"]
        return ", ".join([f"{key}={getattr(self, key)}" for key in keys])
```
</details>


Now, you're all done! You can go back and implement GANs or VAEs using the transposed convolution module you've just written.


```

