DATE DOWNLOADED: Sun Apr 13 19:50:00 2025
SOURCE: Content Downloaded from HeinOnline

Citations:
Please note: citations are provided as a general guideline. Users should consult their preferred
citation format's style manual for proper citation formatting.

Bluebook 21st ed.
			                                                                
Jonathan H. Choi, Amy B. Monahan & Daniel Schwarcz, Lawyering in the Age of
Artificial Intelligence, 109 MINN. L. REV. 147 (2024).

ALWD 7th ed.                                                                         
Jonathan H. Choi, Amy B. Monahan & Daniel Schwarcz, Lawyering in the Age of
Artificial Intelligence, 109 Minn. L. Rev. 147 (2024).

APA 7th ed.                                                                          
Choi, J. H., Monahan, A. B., & Schwarcz, Daniel. (2024). Lawyering in the age of
artificial intelligence. Minnesota Law Review, 109(1), 147-218.

Chicago 17th ed.                                                                     
Jonathan H. Choi; Amy B. Monahan; Daniel Schwarcz, "Lawyering in the Age of
Artificial Intelligence," Minnesota Law Review 109, no. 1 (2024): 147-218

McGill Guide 10th ed.                                                                
Jonathan H. Choi et al, "Lawyering in the Age of Artificial Intelligence" (2024)
109:1 Minn L Rev 147.

AGLC 4th ed.                                                                         
Jonathan H. Choi et al, 'Lawyering in the Age of Artificial Intelligence' (2024)
109(1) Minnesota Law Review 147

MLA 9th ed.                                                                          
Choi, Jonathan H., et al. "Lawyering in the Age of Artificial Intelligence."
Minnesota Law Review, vol. 109, no. 1, 2024, pp. 147-218. HeinOnline.

OSCOLA 4th ed.                                                                       
Jonathan H. Choi, Amy B. Monahan & Daniel Schwarcz, 'Lawyering in the Age of
Artificial Intelligence' (2024) 109 Minn L Rev 147                   Please note:
citations are provided as a general guideline. Users should consult their preferred
citation format's style manual for proper citation formatting.

-- Your use of this HeinOnline PDF indicates your acceptance of HeinOnline's Terms and 
   Conditions of the license agreement available at

https://heinonline.org/HOL/License
-- The search text of this PDF is generated from  uncorrected OCR text.
-- To obtain permission to use this article beyond the scope of your  license, please use:

Copyright Information

Article

Lawyering in the Age of Artificial
Intelligence

Jonathan H. Choi,t Amy B. Monahan,tt
and Daniel Schwarczttt

We conducted the first randomized controlled trial to study
the effect of AI assistance on human legal analysis. We randomly
assigned law school students to complete realistic legal tasks ei-
ther with or without the assistance of GPT-4, tracking how long
the students took on each task and blind-grading the results.
We found that access to GPT-4 only slightly and inconsist-
ently improved the quality of participants' legal analysis but in-
duced large and consistent increases in speed. AI assistance im-
proved the quality of output unevenly where it was useful at all,
the lowest-skilled participants saw the largest improvements. On
the other hand, AI assistance saved participants roughly the
same amount of time regardless of their baseline speed. In follow-
up surveys, participants reported increased satisfaction from

t Professor of Law, University of Southern California Gould School of
Law.
tt Distinguished McKnight University Professor and Melvin C. Steen Pro-
fessor, University of Minnesota Law School.
ttt Fredrikson & Byron Professor of Law, University of Minnesota Law
School. For their feedback, we thank David Abrams, Ben Alarie, Paul Connell,
Kristin Hickman, David Hoffman, Michael Morse, Anthony Niblett, Jed Stiglitz,
Eric Talley, and the participants at the Mitchell Hamline Faculty Workshop,
the University of Pennsylvania Law and Economics Seminar, the Southern
Methodist University Conference on ChatGPT, the University of Toronto Law
School Faculty Workshop, the Harvard Law School Legal Profession Seminar,
and the Duke Law School Faculty Workshop. This research was supported by
the Kommerstad Faculty Imagination Fund at the University of Minnesota Law
School. Copyright © 2024 by Jonathan H. Choi, Amy B. Monahan, and Daniel
Schwarez.

147

148 
MINNESOTA LAW REVIEW 
[109:147

using Al to complete legal tasks and correctly guessed the tasks
for which GPT-4 was most helpful.
These results have important descriptive and normative im-
plications for the future of lawyering. Descriptively, they suggest
that AI assistance can significantly improve productivity and sat-
isfaction, and that it can be selectively employed by lawyers in
areas where Al is most useful. Because Al tools have an equaliz-
ing effect on performance, they may also promote equality in a
famously unequal profession. Normatively, our findings suggest
that law schools, lawyers, judges, and clients should thoughtfully
embrace Al tools and plan for a future in which they will become
widespread.

2024] 
LAWYERING IN THE AGE OF AI 
149

TABLE OF CONTENTS

Introduction.............................................................................. 
150
I. Background.......................................................................... 
155
II. M eth odology.................................................................... . 166
III. Results............................................................................... 
170
IV. Limitations, Assumptions, and Robustness Checks....... 187
V. Implications ........................................................................ 
191
A. 
Implications for the Future of Legal Services .......... 191
B. 
Normative Implications.............................................. 
199
1. Lawyers and Law Firms........................................ 199
2. Legal Clients........................................................... 
201
3. Judges ..................................................................... 203
4. Law Schools and Law Students ............................ 204
Conclusion................................................................................. 
208
Appendix................................................................................... 
209

MINNESOTA LAW REVIEW

INTRODUCTION

Rapid new improvements in the performance of artificial in-
telligence (AI) models have triggered excitement and trepidation
about the future of lawyering.1 Will Al replace human lawyers,
or will it make them happier and more efficient? Should lawyers
and judges embrace Al to perform legal tasks, or should they es-
chew it as unreliable and opaque? Should law schools incorpo-
rate Al into the curriculum, or is Al too speculative to be worth
learning about?
Studies to date offer limited insight into these questions. Ex-
isting scholarship focuses on AI's ability to conduct legal analysis
on its own, rather than its ability to assist humans. 2 Yet the

1. 
See John G. Roberts, Jr., 2023 Year-End Report on the Federal Judici-
ary, SUP. CT. OF THE U.S. 5 (2023), https://www.supremecourt.gov/publicinfo/
year-end/2023year-endreport.pdf [https://perma.cc/T6SC-FH9S] 
(urging "cau-
tion and humility" in the use of artificial intelligence); Roger Barton, How Will
Leveraging AI Change the Future of Legal Services?, REUTERS (Aug. 23, 2023),
https://www.reuters.com/legal/legalindustry/how-will-leveraging-ai-change
-future-legal-services-2023-08-23 [https://perma.cc/6DYK-3END] (arguing that
lawyers must adapt to, rather than compete with, AI advancements); Daniel
Farrar, To Future-Proof Their Firms, Attorneys Must Embrace AI, FORBES (July
13, 2023), https://www.forbes.com/sites/forbesbusinesscouncil/2023/07/13/to
-future-proof-their-firms-attorneys-must-embrace-ai/?sh=6282438b245b
[https://perma.cc/SHK5-FHLN] (recommending lawyers to leverage and not
fear AI); Steve Lohr, A.L Is Coming for Lawyers, Again, N.Y. TIMES (Apr. 10,
2023), https://www.nytimes.com/2023/04/10/technology/ai-is-coming-for
-lawyers-again.html [https://perma.cc/5D7C-HDGU] (emphasizing the simulta-
neous threat and opportunity of AI in the legal industry); John Villasenor, How
AI Will Revolutionize the Practice of Law, BROOKINGS INST. (Mar. 20, 2023),
https://www.brookings.edu/articles/how-ai-will-revolutionize-the-practice-of
-law [https://perma.cc/C3MU-6E6L] (evaluating the future role of AI in the legal
field).
2. 
See, e.g., Jonathan H. Choi, Kristin E. Hickman, Amy B. Monahan

&

Daniel Schwarcz, ChatGPT Goes to Law School, 71 J. LEGAL EDUC. 387, 388-91
(2022) (finding that exam answers drafted by ChatGPT, with limited prompt
engineering, achieved an average grade of a C+ in four real exams at the Uni-
versity of Minnesota Law School); Daniel Martin Katz, Michael James Bom-
marito, Shang Gao & Pablo Arredondo, GPT-4 Passes the Bar Exam, PHIL.
TRANS. R. SOC. A, Apr. 15, 2024, at 1, 3-5 (finding that under zero-shot perfor-
mance 
where a model completes a task without training examples 
GPT-4
passed the Uniform Bar Examination and outperformed the average human
test-taker by seven percent on the Multistate Bar Examination portion); Mat-
thew Dahl, Varun Magesh, Mirac Suzgun, & Daniel E. Ho, Large Legal Fictions:
Profiling Legal Hallucinations in Large Language Models, 16 J. LEGAL ANALY-
SIS 64, 66 (2024) (finding a "widespread occurrence of legal hallucinations" in
analysis conducted by large language models, but failing to account for the

150
[109:147

LAWYERING IN THE AGE OF AI1

latter application is significantly more plausible for the foresee-
able future given lawyers' ethical obligation to ensure that their
work product is accurate and consistent with their clients' inter-
ests, 3 as well as the irreducibly normative nature of law. 4 A sec-
ond limitation of prior research is that, for reasons of conven-
ience, it has generally focused on how Al impacts performance
on exams, like law school exams and the bar exam. 5 But exam
results may not translate to lawyering in the real world.6 Fi-
nally, many studies to date have suffered from methodological

straightforward methods to ameliorate hallucinations that we discuss in our
training materials).

3. 
See, e.g., The State Bar of Cal. Standing Comm. on Pro. Resp. and Con-
duct, Practical Guidance for the Use of Generative Artificial Intelligence in the
Practice of Law, THE STATE BAR OF CAL. 3 (Nov. 17, 2023), https://www.calbar
.ca.gov/Portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf
[https://perma.cc/JG6S-J62V] ("A lawyer must critically review, validate, and
correct both the input and the output of generative AI to ensure the content
accurately reflects and supports the interests and priorities of the client in the
matter at hand .... "); Jonathan Grabb, Lawyers and AI: How Lawyers' Use of
Artificial Intelligence Could Implicate the Rules of Professional Conduct, THE
FLA. BAR (Mar. 13, 2023), https://www.floridabar.org/the-florida-bar-news/
lawyers-and-ai-how-lawyers-use-of-artificial-intelligence-could-implicate-the
-rules-of-professional-conduct [https://perma.cc/79BH-JUGZ] ("While a chatbot
may be able to draft a document in mere seconds, any lawyer who uses AT as-
sistance is still responsible for generating work product that is legally and fac-
tually accurate, competent, and meritorious."); see also Nicole Yamane, Artifi-
cial Intelligence in the Legal Field and the Indispensable Human Element Legal
Ethics Demands, 33 GEO. J. LEGAL ETHICS 877, 882 (2020) (noting ethical con-
cerns due to the rising use of AI); W. Bradley Wendel, The Promise and Limita-
tions of Artificial Intelligence in the Practice of Law, 72 OKLA. L. REV. 21, 24-26
(2019) (differentiating between routine legal work that may be automated by AT
and high-risk work that still requires the human element).
4. 
See, e.g., Frank Pasquale, A Rule of Persons, Not Machines: The Limits
of Legal Automation, 87 GEO. WASH. L. REV. 1, 6 (2019) (advocating for under-
standing "technology as a tool to complement attorneys' skills, rather than sub-
stitute for them"); Rebecca Crootof, Margot E. Kaminski & W. Nicholson Price
II, Humans in the Loop, 76 VAND. L. REV. 429, 486 (2023) (describing efforts by
lawyers and lawprofessors to "keep[] human lawyers involved in legal processes
rather than relying fully on AI").
5. 
See infra Part I (denoting the limited nature of GPT-4 studies in the
legal field).

6. 
See, e.g., Marsha Griggs, Building a Better Bar Exam, 7 TEX. A&M L.
REV. 1, 2 (2019) (discussing challenges to how well performance on the bar exam
measures "readiness to enter the legal profession"); JOAN W. HOWARTH, SHAP-
ING THE BAR: THE FUTURE OF ATTORNEY LICENSING 99-109 (2023) (arguing for
significant reforms in the bar exam because it has historically failed to test the
skills that new lawyers need to represent clients while unfairly harming tradi-
tionally marginalized groups).

2024]
151

MINNESOTA LAW REVIEW

limitations, like non-blind grading of results 7 or imperfectly
matched treatment and control groups.8

To better understand how Al will affect the lawyers of the
future and what should be done now, we conducted the first ran-
domized controlled trial of the effect of large language model
(LLM) assistance on human legal analysis. 9 To do so, we ran-
domly assigned sixty students at the University of Minnesota
Law School to complete four separate legal tasks (resulting in
240 total task completions), either with or without the assistance
of the most advanced general-purpose generative Al tool then
available, GPT-4.10 We selected the four assigned tasks-draft-
ing a complaint, a contract, a section of an employee handbook,
and a client memo-because they typify the type of work per-
formed by junior attorneys.11 Prior to completing these tasks,
study participants received several hours of training on how to
use GPT-4 effectively, which we patterned on real attorney train-
ing materials. 12 After participants completed the four assigned

7. 
See Katz, Bommarito, Gao, & Arredondo, supra note 2, at 9 (acknowl-
edging that the answers produced by GPT-4 in the study were not blindly
graded, but attempting to address this issue by soliciting the views of peers who
were provided with blind samples of the answers produced by GPT-4). See gen-
erally Eric Martinez, Re-Evaluating GPT-4's Bar Exam Performance, A.I. & L.,
Mar. 30, 2023, at 1 (critiquing OpenAI's claims that GPT-4 performed at the
ninetieth percentile on the Uniform Bar Examination).

8. 
See Jonathan H. Choi & Daniel Schwarcz, AI Assistance in Legal Anal-
ysis: An Empirical Study, 73 J. LEGAL EDUC. (forthcoming 2024) (manuscript at
29-35) (on file with the Minnesota Law Review) [hereinafter AI Assistance in
Legal Analysis] (reporting that the impact on exam scores of providing students
with access to GPT-4 depended significantly on the student's starting skill level,
while acknowledging various methodological limitations in the study's approach
to measuring this effect).
9. 
The raw data is on file with the authors and may be requested.
10. 
See OpenAI, GPT-4 Technical Report, ARXIV 14 (Mar. 4, 2024), https://
arxiv.org/abs/2303.08774 [https://perma.cc/L4X2-KZC6] (reporting that GPT-
4's performance on various benchmarks exceeds the performance of prior gen-
erative AT models).
11. 
See Ann Sinsheimer & David J. Herring, Lawyers at Work: A Study of
the Reading, Writing, and Communication Practices of Legal Professionals, 21
LEGAL WRITING: J. LEGAL WRITING INST. 63, 99-100 (2016) (reporting the re-
sults of a three-year ethnographic study of junior associates at law firms, which
found that common documents that these lawyers drafted included formal sum-
maries of their research findings, contracts, and complaints, among many other
documents).
12. 
See infra Part II (describing the process for training study participants
to use GPT-4 effectively to complete basic legal writing tasks).

152
[109:147

LAWYERING IN THE AGE OF AI1

tasks, we blind-graded the results and tracked how long they
took on each task.13
We found that access to GPT-4 only slightly improved the
quality of participants' legal analysis, with improvements that
were small in magnitude and inconsistent across tasks (+0.17,
+0.24, +0.07, and -0.07 on a 4.0 grading scale). 14 However, we
found that Al assistance consistently induced large declines in
the amount of time taken to complete tasks (-24.1%, -32.1%,

-

21.1%, and -11. 8 %). 15 The benefits of Al assistance were not
evenly distributed; for the tasks on which Al was the most use-
ful, it was significantly more useful to lower-skilled participants
(judged by their scores on tasks for which they did not have Al
assistance). 16 On the other hand, Al assistance reduced the
amount of time that participants took to complete the tasks
roughly uniformly regardless of their baseline speed.17
We also surveyed participants on their perceptions of how
access to GPT-4 impacted their work on the assigned legal
tasks. 18 We found that, with respect to the tasks on which GPT-
4 was most useful, participants reported increased satisfaction
from using it. 19 Although they completed the survey without
knowing their results, participants also correctly understood
GPT-4's strengths and weaknesses, reporting that they expected
the improvements in speed to be greater than the improvements
in quality and correctly identifying the tasks at which GPT-4 in-
duced larger quality improvements.20 This suggests that alt-
hough the benefits from Al use may be inconsistent, participants
generally correctly perceived the tasks at which it was most use-
ful and could selectively use Al in situations where it provides
the greatest benefits. 2 1

13. 
See infra Part II.
14. 
See infra Table 1 (tabulating task performance with and without
GPT-4).
15. 
See infra Table 2 (tabulating duration of tasks with and without
GPT-4).
16. 
See infra Figures 9-12 (demonstrating higher GPA benefits for lower-
skilled participants).
17. 
See infra Table 2 (tabulating time reductions from the use of GPT-4 on
tasks).
18. 
See infra pp. 185-86 (presenting the survey questions).
19. 
See Figure 17 and accompanying text.
20. Id.
21. Id.

2024]
153

MINNESOTA LAW REVIEW

Taken together, these results point toward large potential
productivity gains from Al assistance in the legal profession, es-
pecially by reducing the time taken to conduct legal analysis.
They also suggest that Al could be a force to improve lawyer sat-
isfaction. 22 Moreover, the results almost certainly serve as a
lower-bound estimate on AI's capacity to improve the efficiency
of legal services for three reasons. First, whereas our partici-
pants used the general purpose Al GPT-4 to assist them with
assigned tasks, lawyers are increasingly gaining access to spe-
cialized generative Al tools that already offer better performance
than GPT-4 on legal tasks.23 Second, study participants only re-
ceived a few hours of training on GPT-4 before completing as-
signed tasks,24 whereas lawyers that use AI-based tools will con-
tinually refine their ability to skillfully use Al over the course of
months or years. Finally, and perhaps most obviously, rapid Al
innovation has continued since we conducted the experiment in
the summer of 2023 and will likely do so for the foreseeable fu-
ture.25

22. 
See id. (noting a boost to personal satisfaction when using GPT-4).
23. 
See infra notes 99-102 and accompanying text (discussing improved
tools). For instance, LexisNexis just recently launched an AI legal assistant that
is built into its general-purpose search engine. See Press Release, LexisNexis,
LexisNexis Launches Lexis+ AI, a Generative AT Solution with Hallucination-
Free Linked Legal Citations (Oct. 25, 2023), https://www.lexisnexis.com/
community/pressroom/b/news/posts/lexisnexis-launches-lexis-ai-a-generative-
ai-solution-with-hallucination-free-linked-legal-citations [https://perma.cc/
ZQ69-RRVB]. Similarly, Thomson Reuters, the owner of Westlaw, recently ac-
quired the firm Casetext in large part due to its generative AT capabilities.
Thomson Reuters to Acquire Legal AI Firm Casetext for $650 Million, REUTERS
(June 27, 2023), https://www.reuters.com/markets/deals/thomson-reuters
-acquire-legal-tech-provider-casetext-650-mln-2023-06-27 [https://perma.cc/
S43E-D3XY]. Westlaw is currently working to integrate at least some of these
capabilities into its Westlaw Precision product. See Press Release, Thomson
Reuters, Thomson Reuters Unveils Generative AI Strategy Designed to Trans-
form the Future of Professionals (Nov. 1, 2023), https://www.thomsonreuters
.com/en/press-releases/2023/november/thomson-reuters-unveils-generative-ai
-strategy-designed-to-transform-the-future-of-professionals.html [https://
perma.cc/VH4H-FD4S].
24. 
See infra Appendix A (describing the training undergone by partici-
pants).
25. 
See, e.g., What's the Future of Generative AI? An Early View in 15
Charts, MCKINSEY & CO. (Aug. 25, 2023), https://www.mckinsey.com/featured
-insights/mckinsey-explainers/whats-the-future-of-generative-ai-an-early-view
-in-15-charts [https://perma.cc/T7LE-SQAD] (illustrating the pace of innovation
in generative AT).

154
[109:147

LAWYERING IN THE AGE OF AI1

Especially when understood as a lower-bound estimate on
AI's potential impact on lawyering, our results have important
normative implications for actors across the legal services indus-
try. 26 Lawyers and judges should affirmatively explore how to
incorporate Al into their work, though AI's usefulness will vary
by practice area, task, and the stakes of the underlying mat-
ters.27 Purchasers of legal services also should pay close atten-
tion to our results, reconsidering what types of legal matters
should be sent to outside counsel rather than handled in-house,
and how matters that are handled externally are managed and
billed. 28 Law schools should reassess when and how law stu-
dents are trained to use Al, and when and how access to that tool
should be limited.29

We develop these results and implications in four parts. Part
I briefly reviews both the evolution of legal technology and the
state of the scholarly literature on how Al can impact lawyering
and other knowledge-based tasks. Part II details our methodol-
ogy, which employs a randomized controlled trial that allows us
to make a strong causal inference about AI's impact on legal
tasks. In Part III, we highlight and discuss our key results,
which demonstrate that generative Al can significantly improve
the speed at which legal tasks are completed without degrading
the quality of the resulting work product. The implications of
these results are then discussed in Part IV, which emphasizes
that virtually all actors in the legal ecosystem-including
judges, lawyers, clients, law schools, and law students-should
devote significant attention to ethically and intelligently incor-
porating generative Al into their daily workflows and into their
broader decision-making. Finally, a technical Appendix includes
additional details about our methodology and results.

I. BACKGROUND

The first legal databases were introduced fifty years ago, at
the beginning of what many consider the modern era of legal

26. 
See infra Part V.B.
27. 
See infra Parts V.B.1, V.B.3.
28. 
See infra Part V.B.2.
29. 
See infra Part V.B.4.

2024]
155

MINNESOTA LAW REVIEW

technology.30 Over the next decades, innovations such as email,
document management systems, billing software, e-discovery
systems, and online dispute resolution platforms were widely
adopted and helped shape practice patterns. 31 In addition, tech-
based "disrupters" such as Rocket Lawyer, Legal Zoom, and
Trust & Will entered the market, offering an online, often auto-
mated, solution for the drafting of common legal documents. 32

Historically, these major legal tech innovations have im-
proved lawyer efficiency rather than fundamentally altered the
core skills needed to be an effective lawyer. 33 For example, a law-
yer with access to an easily searchable legal database can com-
plete legal research in much less time than would be possible if
they needed to search through hard copy indices. 34 But the skill
involved in analyzing and applying cases and statutes remains
fundamentally the same. Similarly, e-discovery tools allow law-
yers to automate the search function in discovery, 35 but cannot

30. 
William G. Harrington, A Brief History of Computer-Assisted Legal Re-
search, 77 LAW LIBR. J. 543, 553 (1984) (recounting the development of Lex-
isNexis and Westlaw); Olufunmilayo B. Arewa, Open Access in a Closed Uni-
verse: Lexis, Westlaw, Law Schools, and the Legal InformationMarket, 10 LEWIS
& CLARK L. REV. 797, 816 (2006) (describing the creation of online legal data-
bases); James A. Sprowl, Computer-Assisted Legal Research: Westlaw and Lexis,
62. A.B.A. J. 320, 321-23 (1976) (describing the similarities and differences of
the Lexis and Westlaw databases).
31. 
See, e.g., Roberts, supra note 1, at 2-5 (describing the legal profession's
adoption of technologies ranging from personal computers to digitalization and
technology-assisted review of discovery-related documents).
32. 
See Susan Saab Fortney, Online Legal Document Providers and the
Public Interest: Using a Certification Approach to Balance Access to Justice and
Public Protection, 72 OKLA. L. REV. 91, 93 (2019) (highlighting the demand for
the "computerization of legal services" in America).
33. 
Compare Mark Fenwick, Wulf A. Kaal & Erik P.M. Vermeulen, Legal
Education in the Blockchain Revolution, 20 VAND. J. ENT. & TECH. L. 351, 357
(2017) (describing the introduction of "Legal Tech" tools that have increased the
efficiency of lawyers), with Symposium, Legal Reasoning and Artificial Intelli-
gence: How Computers "Think" Like Lawyers, 8 U. CHI. L. SCH. ROUNDTABLE 1,
21 (2001) (noting that AI systems available at the time were not capable of the
type of analogical reasoning that lawyers and judges engage in).
34. 
See Raymond H. Brescia, Walter McCarthy, Ashley McDonald, Kellan
Potts & Cassandra Rivais, Embracing Disruption: How Technological Change
in the Delivery of Legal Services Can Improve Access to Justice, 78 ALB. L. REV.
553, 567-68 (2014) (attributing an increase in legal research speed to websites
like "LexisNexis, Westlaw, and Bloomberg").
35. 
See John 0. McGinnis & Russell G. Pearce, The Great Disruption: How
Machine Intelligence Will Transform the Role of Lawyers in the Delivery of Legal

156
[109:147

LAWYERING IN THE AGE OF AI1

provide the knowledge necessary to identify what must be pro-
duced and what is protected by privilege.
Even before the recent wave of progress in generative Al
tools like ChatGPT, the rise of Al in legal tech was disrupting
this historical pattern. For example, Al tools like predictive cod-
ing in e-discovery systems have become increasingly prominent
in recent years.36 These tools allow a lawyer to code a sample of
discovery documents, which are then used by an algorithm to
identify other relevant documents. 37 To a certain degree, tools
such as these actually displace an attorney's work. 38

With each new innovation, lawyers have typically fretted
about the implications for the legal profession and lawyer jobs.39

Services, 82 FORDHAM L. REV. 3041, 3047-48 (2014) (recounting the use of "pre-
dictive coding" by lawyers to automate e-discovery in part).
36. Id.
37. 
See id. at 3047; see also Daniel Martin Katz, Quantitative Legal Predic-
tion or How I Learned to Stop Worrying and Start Preparing for the Data-
Driven Future of the Legal Services Industry, 62 EMORY L.J. 909, 936 (2013)
(arguing that the prediction of legal outcomes is of primary interest to potential
clients, which can be assisted with the aid of technology that leverages data
about similar legal questions).
38. 
See Maura R. Grossman & Gordon V. Cormack, Quantifying Success:
Using Data Science to Measure the Accuracy of Technology-Assisted Review in
Electronic Discovery (finding that "technology-assisted review" systems in e-dis-
covery provided "significantly superior precision" compared to manual review),
in DATA DRIVEN LAW: DATA ANALYTICS AND THE NEW LEGAL SERVICES 127,
150-51 (Ed Walters ed., 2019). But see Emily S. Taylor Poppe, The Future Is
Br-igh Complicated: Al, Apps & Access to Justice, 72 OKLA. L. REV. 185, 189
(2019) (arguing that displacement concerns are less significant when it comes
to tasks that were already "subject to outsourcing").
39. 
See, e.g., RICHARD SUSSKIND & DANIEL SUSSKIND, THE FUTURE OF THE
PROFESSIONS: HOW TECHNOLOGY WILL TRANSFORM THE WORK OF HUMAN EX-
PERTS 66-67 (2015) (expressing the belief of the authors and other legal com-
mentators that the legal world is "on the brink of unprecedented upheaval");
Katz, supra note 37, at 909 ("Welcome to law's information revolution-revolu-
tion already in progress." (footnote omitted)); Dana Remus & Frank Levy, Can
Robots Be Lawyers? Computers, Lawyers, and the Practice of Law, 30 GEO. J.
LEGAL ETHICS 501, 501 (2017) ("We assess frequently advanced arguments that
automation will soon replace much of the work currently performed by law-
yers."); Tanina Rostain, Robots Versus Lawyers: A User-Centered Approach, 30
GEO. J. LEGAL ETHICS 559, 560 (2017) (identifying a recent trend of predictions
that new legal technologies will push lawyers out of much of their current work
and leave only narrow elaborate areas of law to humans); Sean Semmler

&

Zeeve Rose, Artificial Intelligence: Application Today and Implications Tomor-
row, 16 DUKE L. & TECH. REV. 85, 86 (2017) ("As artificial intelligence looms
over the practice of law, it is important to dispel the notion that artificially-

2024]
157

MINNESOTA LAW REVIEW

If technology allowed the same work to be done in less time, 40 or
could replace lawyers altogether for certain tasks,4 1 it was feared
that there would be fewer jobs available for lawyers. In some
cases, lawyers have responded to these fears by employing self-
regulatory tools to limit the permissible use of technologies that
could undermine demand for legal services. 42 Of course, others
championed at least some of these advances as having the poten-
tial to lower legal fees and therefore increase access to legal ser-
vices. 43 Moreover, it is possible that task automation could also

intelligent machines will replace humans."); Harry Surden, Machine Learning
and Law, 89 WASH. L. REV. 87, 87 (2014) (arguing that it is "overly broad" to
conclude that AI will have little impact until it displays "higher-order cogni-
tion"); David C. Vladeck, Machines Without Principals: Liability Rules and Ar-
tificial Intelligence, 89 WASH. L. REV. 117, 117-20 (2014) (describing positive
and negative visions of intelligent machines); John Markoff, Armies of Expen-
sive Lawyers, Replaced by Cheaper Software, N.Y. TIMES (Mar. 4, 2011), https://
www.nytimes.com/2011/03/05/science/051egal.html [https://perma.cc/2UHS
-BWRY] (explaining new e-discovery software and its potential impact on the
legal market); JAMES E. MOLITERNO, THE AMERICAN LEGAL PROFESSION IN CRI-
SIS: RESISTANCE AND RESPONSES TO CHANGE 208 (2013) (detailing several
states' struggles regarding confidentiality at the inception of email).
40. 
See Fenwick, Kaal & Vermeulen, supra note 33 (describing technology
advances that led to efficiency gains in legal practice).
41. 
See, e.g., Christopher A. Suarez, Disruptive Legal Technology, COVID-
19, and Resilience in the Profession, 72 S.C. L. REV. 393, 404 (2020) (touting new
e-discovery technology that "can eliminate the need for lawyers to review each
and every document").
42. 
See Gillian K. Hadfield, Legal Barriers to Innovation: The Growing Eco-
nomic Cost of Professional Control Over Corporate Legal Markets, 60 STAN. L.
REV. 1689, 1724-25 (2008) (describing regulation of "unauthorized practice[s]
of law" by state bar associations).
43. 
See, e.g., SUSSKIND & SUSSKIND, supra note 39; McGinnis & Pearce,
supra note 35, at 3055; Brescia, McCarthy, McDonald, Potts & Rivais, supra
note 34, at 553 ("[T]he provision of legal services is becoming commodified: car-
ried out by lawyers and nonlawyers alike in a way that is far less expensive
than the traditional, 'bespoke' model of lawyering."). See generally Elinor R. Jor-
dan, Point, Click, Green Card: Can Technology Close the Gap in Immigrant Ac-
cess to Justice?, 31 GEO. IMMIGR. L.J. 287 (2017) (exploring the difficulties of
obtaining a green card and ways that new legal technology has or can assist in
the process); Kathleen Elliott Vinson & Samantha A. Moppett, Digital Pro Bono:
Leveraging Technology to Provide Access to Justice, 92 ST. JOHN'S L. REV. 551
(2018) (identifying the need for more pro bono work and how that need can be
facilitated by legal organizations and law schools employing new technologies);
J.J. Prescott, Improving Access to Justice in State Courts with Platform Tech-
nology, 70 VAND. L. REV. 1993, 1993-94, 2026-39 (2017) (presenting evidence
showing accessible state court websites reduce dispute resolution and fee pay-
ment times).

158
[109:147

LAWYERING IN THE AGE OF AI1

increase the demand for lawyers, either because the lower cost
of legal services increases the overall quantity of legal services
provided (induced demand) or because automation creates new
tasks for which human labor is an important complement (what
Daron Acemoglu and Pascual Restrepo have called a "reinstate-
ment effect"). 44

Similar dynamics exist in recent discussions of how increas-
ingly capable LLMs like GPT-4 will impact the legal profession.45
At the same time, LLMs like GPT-4 seem to represent a qualita-
tively different type of technological advance from those that
came before. As a result, many have speculated that these LLMs
will lead to true revolution in the practice of law, 46 radically
changing market demand for human lawyers. 47

Yet, despite these sizeable questions and concerns, rela-
tively little is known empirically about AI's capacity to displace

44. Daron Acemoglu & Pascual Restrepo, Automation and New Tasks: How
Technology Displaces and Reinstates Labor, 33 J. ECON. PERSPECTIVES 3, 3-4
(2019) (describing the countervailing actions of the "displacement effect,"
whereby labor is replaced by automation, and the reinstatement effect); see also
Daron Acemoglu, David Autor, Johnathon Hazell, & Pascual Restrepo, Artifi-
cial Intelligence and Jobs: Evidence from Online Vacancies, 40 J. LABOR ECON.
293, 293 (2022) (analyzing the effect of AT on jobs but finding it too small for
definitive conclusions); Daron Acemoglu, The Simple Macroeconomics of AI 23-
42 (Nat'l Bureau of Econ. Rsch., Working Paper No. 32487, 2024) (analyzing the
macroeconomic effects of recent AT developments).
45. 
See, e.g., Erin Mulvaney & Lauren Weber, End of the Billable Hour?
Law Firms Get on Board with Artificial Intelligence, WALL ST. J. (May 11, 2023),
https://www.wsj.com/articles/end-of-the-billable-hour-law-firms-get-on-board
-with-artificial-intelligence-17ebd3f8 
[https://perma.cc/X6VG-UFK4] 
(discuss-
ing how A tools can "handle the drudgery" of repetitive work and "simplify com-
plex work").
46. Even before the advent of large language model AT, some "legal futur-
ists" were envisioning such transformation. See, e.g., Benjamin Alarie, The Path
of the Law: Towards Legal Singularity, 66 U. TORONTO L.J. 443, 445 (2016) (de-
scribing the "legal singularity" that will occur when "the accumulation of a mas-
sive amount of data and dramatically improved methods of inference make legal
uncertainty obsolete"); Benjamin Alarie, Anthony Niblett & Albert H. Yoon,
How Artificial Intelligence Will Affect the Practice of Law, 68 U. TORONTO L.J.
106, 114 (2018) (speculating that AT will substantially transform the work of
lawyers in the future).
47. 
The impact of generative AT on the labor market is certainly not limited
to the legal profession. See, e.g., Tyna Eloundou, Sam Manning, Pamela Mish-
kin & Daniel Rock, GPTs Are GPTs: An Early Look at the Labor Market Impact
Potential of Large Language Models (Aug. 22, 2023) (unpublished manuscript)
(on file with the Minnesota Law Review) (evaluating the potential labor market
effects of LLMs like GPT-4 on a variety of industries).

2024]
159

MINNESOTA LAW REVIEW

lawyers or even capably assist lawyers at lawyering tasks. To
date, the best information we have is found in studies of GPT-4's
performance on law school examinations, 48 bar examinations, 49

and in answering discrete legal questions. 50 Other non-empirical
research considers the ethical implications of using such tech-
nology in the practice of law, 51 how artificial intelligence may
change the skills needed to be a successful lawyer, 52 and how law
firms may begin to compete on the basis of technological exper-
tise. 53

Studies examining GPT's proficiency on legal exams have
found that its performance varies widely depending on the type
of exam and prompting methodology used. One study found that
GPT-4 alone performed in the ninetieth percentile on the

48. 
Choi, Hickman, Monahan & Schwarcz, supra note 2 (testing the perfor-
mance of GPT-3.5 alone on law school exams); see also Andrew Blair-Stanek,
Anne-Marie Carstens, Daniel Goldberg, Mark A. Graber, David Gray, & Max-
well L. Stearns, GPT-4's Law School Grades: Con Law C, Crim C-, Law & Econ
C, Partnership Tax B, Property B-, Tax B, 2 (May 24, 2023) (unpublished man-
uscript) (on file with the Minnesota Law Review) [hereinafter GPT-4's Law
School Grades] (reporting mixed results with law school exams).
49. 
See Katz, Bommarito, Gao & Arredondo, supra note 2, at 1, 7 (examin-
ing GPT-4's performance on different bar exam sections).
50. 
See John J. Nay et al., Large Language Models as Tax Attorneys: A Case
Study in Legal Capabilities Emergence, PHIL. TRANSACTIONS ROYAL SOC'Y A,
Apr. 15, 2024, at 1, 5-9 (studying large language models' ability to apply tax
law); Andrew Blair-Stanek, Nils Holzenberger & Benjamin van Durme, OpenAI
Cribbed Our Tax Example, but Can GPT-4 Really Do Tax?, 180 TAx NOTES FED.
1101, 1105 (2023) [hereinafter OpenAI Cribbed Our Tax Example] (examining
data from GPT-4 tax study).
51. 
See, e.g., Katherine Medianik, Note, Artificially Intelligent Lawyers:
Updating the Model Rules of Professional Conduct in Accordance with the New
Technological Era, 39 CARDOzO L. REV. 1497, 1501 (2018) (examining the Model
Rules of Professional Conduct in the context of AI). See generally Brian L. Frye,
Should Using an Al Text Generator to Produce Academic Writing Be Plagia-
rism?, 33 FORDHAM INTELL. PROP., MEDIA & ENT. L.J. 946 (2023) (asking
ChatGPT itself about plagiarism and the ethical considerations of its use).
52. 
See, e.g., Alyson Carrel, Legal Intelligence Through Artificial Intelli-
gence Requires Emotional Intelligence: A New Competency Model for the 21st
Century Legal Professional, 35 GA. ST. U. L. REV. 1153, 1154 (2019) (describing
the skills a lawyer will need in the context of AI); Suarez, supra note 41, at 396
(explaining that lawyers will need "increased resilience" in an "uncertain tech-
nological future").
53. 
See Bruce A. Green & Carole Silver, Technocapital@BigLaw.com, 18
NW. J. TECH. & INTELL. PROP. 265, 282-308 (2021) (studying technology and
law firm competition).

160
[109:147

LAWYERING IN THE AGE OF AI1

Uniform Bar Examination 54 (although scholars have subse-
quently raised methodological doubts about this claim). 55 In an-
other study evaluating AI-generated answers to law school exam
questions, researchers found that although exams drafted by
GPT-3.5 often included solid explanations of basic legal rules
and strong organization and composition, they also often "strug-
gled to identify relevant issues" and tended to "only superficially
appl[y] rules to facts as compared [to] real law students." 56

54. 
Katz, Bommarito, Gao & Arredondo, supra note 2, at 12 n.3. This result
extended both to the multiple-choice portion of the exam as well as to the open-
ended essay components of the exam. Id. at 1. Although the authors did not use
any prompt-engineering strategies to generate multiple-choice answers, they
slightly modified essay questions by presenting each sub-question in an inde-
pendent prompt and by "lightly correct[ing] the language" in the prompt so that
it formed a complete sentence. Id. at 9.
55. 
See, e.g., Martinez, supra note 7, at 16-17 (discussing potential meth-
odological issues with the initial finding that GPT-4 surpassed the bar exam
score of ninety percent of human test takers). In addition, the authors in the
Katz et al. study did not grade GPT-4's performance blind and did not have
experience grading bar exams, raising concerns about subjective bias in evalu-
ation. Id.
56. 
Choi, Hickman, Monahan & Schwarcz, supra note 2, at 393; see also
GPT-4's Law School Grades, supra note 48, at 7-8 (finding that GPT-4 "per-
formed well below average," despite being "decent[] at multiple choice" and
sometimes spotting issues missed by students). There are concerns about how
to format exams to address potential cheating. See generally Margaret Ryznar,
Exams in the Time of ChatGPT, 80 WASH. & LEE L. REV. ONLINE 305 (2023).
In other disciplines, GPT has been found to be a proficient and sometimes
superior test taker as compared to humans. See Harsha Nori, Nicholas King,
Scott Mayer McKinney, Dean Carignan & Eric Horvitz, Capabilities of GPT-4
on Medical Challenge Problems 1 (Apr. 12, 2023) (unpublished manuscript) (on
file with the Minnesota Law Review) (finding that GPT-4, without any special-
ized prompting, passes a range of medical exams and outperforms both
ChatGPT and LLM models specifically fine-tuned on medical knowledge); John
C. Lin, David N. Younessi, Sai S. Kurapati, Oliver Y. Tang & Ingrid U. Scott,
Comparison of GPT-3.5, GPT-4, and Human User Performance on a Practice
Ophthalmology Written Examination, 37 EYE 3694, 3695 (2023) ("GPT-4but not
GPT-3.5 achieved the passing threshold for a practice ophthalmology written
examination."); Rohaid Ali et al., Performance of ChatGPT and GPT-4 on Neu-
rosurgery Written Board Examinations, 93 NEUROSURGERY 1353, 1357-59
(2023) (finding that both GPT-4 and GPT-3.5 pass neurosurgery practice board
exams at rates comparable to neurosurgery residents); Hanmeng Liu, Ruoxi
Ning, Zhiyang Teng, Jian Liu, Qiji Shou & Yue Zhang, Evaluating the Logical
Reasoning Ability of ChatGPT and GPT-4, at 5-6 (May 5, 2023) (unpublished
manuscript) (on file with the Minnesota Law Review) (describing the perfor-
mance of ChatGPT and GPT-4 on multi-choice reading comprehension and nat-
ural language inference datasets); Vinay Pursnani, Yusuf Sermet, Musa Kurt

2024]
161

MINNESOTA LAW REVIEW

Perhaps most interestingly, a later study examining GPT-4 as-
sistance on law school exams, where some study participants
used GPT-4 to help generate exam answers, but then reviewed
those answers and edited them as they felt appropriate, found
that such assistance boosted the scores of lower-performing stu-
dents but had no effect or a slightly negative effect on the perfor-
mance of top students. 57

Outside of the exam context, little evidence exists on how
access to LLM tools like GPT-4 might impact lawyers' or law stu-
dents' abilities to complete legal tasks. Tax scholars have tested
GPT-4's ability to answer questions about federal tax law, gen-
erally finding low accuracy with basic prompting to 70 %- 9 0

%

accuracy with significant human assistance (particularly
prompting with hand-selected correct sources). 58 Many scholars
have anecdotally tested GPT's capabilities, including a series of
YouTube videos that illustrate GPT-4's capabilities in various
legal contexts. 59 These anecdotal reports find, for example, that
with good prompting, GPT-4 is able to accurately apply copyright
law, although its performance falters on more difficult legal
analysis.60
In areas other than law, we see the same general focus on
exam performance rather than studies of realistic tasks.6 1 And
as with law, the exam results are mixed. Whereas exams

& Ibrahim Demir, Performance of ChatGPT on the US Fundamentals of Engi-
neering Exam: Comprehensive Assessment of Proficiency and Potential Impli-
cations for Professional Environmental Engineering Practice 1 (Apr. 20, 2023)
(unpublished manuscript) (on file with the Minnesota Law Review) (detailing
the "significant improvement" of ChatGPT and GPT-4 in the context of the Fun-
damentals of Engineering Environmental Exam).

57. AI Assistance in Legal Analysis, supra note 8, at 12-13, 17.
58. 
Nay et al., supra note 50, at 8 (showing results with few shot and chain-
of-thought prompting, in addition to gold truth retrieval); cf. OpenAI Cribbed
Our Tax Example, supra note 50, at 1105 (describing GPT-4 using a simplified
version of the Internal Revenue Code as a reference text and getting tax liabil-
ities exactly correct roughly one-third of the time).
59. 
See generally Harry Surden, YOUTUBE (last visited Jan. 8, 2024),
https://www.youtube.com/@harrysurden3116 (testing GPT-4's performance on
various legal problems).
60. Harry Surden, GPT-4 and Law: ChatGPT Analyzes Copyright Law,
YOUTUBE (Mar. 22, 2023), https://www.youtube.com/watch?v=nqZcrhR8yPU.
61. 
See, e.g., Wayne Geerling, G. Dirk Mateer, Jadrian Wooten & Nikhil
Damodaran, ChatGPT Has Aced the Test of Understanding in College Econom-
ics: Now What?, 68 AM. ECONOMIST 233, 237-39 (2023) (studying ChatGPT's
performance on an economics exam).

162
[109:147

LAWYERING IN THE AGE OF AI1

generated by ChatGPT were highly rated in economics, 62 they
achieved more middling results in computer programming ("out-
standing to satisfactory")6 3 and medical education,64 and "unsat-
isfactory" results in fields like mathematics and psychology. 65

Common problems with ChatGPT-drafted exams included inac-
curate, unreliable, and outdated information. 66 These studies
vary significantly in the methods they use to test LLM perfor-
mance. Some test the performance of Al acting alone, where a
question or prompt is entered into an LLM and its answer is
evaluated without modification.67 Other studies examine the
value of Al assistance, where a human subject uses an LLM on
various tasks or subtasks and then reviews, edits, or otherwise
refines those results to produce a final work product. 68

62. Id. at 233 (finding that GPT ranked in the 91st percentile for Microeco-
nomics and the 99th percentile for Macroeconomics when compared to college
students taking the Test of Understanding in College Economics).
63. 
Chung Kwan Lo, What Is the Impact of ChatGPT on Education? A
Rapid Review of the Literature, 13 EDUC. SCIS., Apr. 2023, at 1, 5 (reviewing
literature on ChatGPT's performance across subject areas, including computer
programming).
64. Tiffany H. Kung et al., Performance of ChatGPT on USMLE: Potential
for AI-Assisted Medical Education Using Large Language Models, PLOS DIGI-
TAL HEALTH, Feb. 2023, at 1 (reporting that ChatGPT performed "at or near the
passing threshold" on the United States Medical Licensing Exam); see also Pe-
ter Lee, Sebastien Bubeck & Joseph Petro, Benefits, Limits, and Risks of GPT-
4 as an Al Chatbot for Medicine, 388 NEW ENG. J. MED. 1233, 1238 (2023) (ex-
amining GPT-4's performance on various medical applications and finding that,
although GPT-4 excels in some areas, it has important limitations).
65. 
Lo, supra note 63, at 6 (reviewing literature on ChatGPT's performance
across subject areas and finding that its performance on mathematics and psy-
chology problems is subpar); see also Lakshmi Varanasi, ChatGPT Can Ace the
Bar, but It Only Has a Decent Chance of Passing the CFA Exams. Here's a List
of Difficult Exams the ChatGPT and GPT-4 Have Passed, BUS. INSIDER (Nov.
5, 2023), https://www.businessinsider.com/list-here-are-the-exams-chatgpt-has
-passed-so-far-2023-1 [https://perma.cc/SW5W-PDU2] (compiling study results
and noting that GPT-4 "still struggles with high school math exams").
66. 
See generally Lo, supra note 63 (discussing the challenges of ChatGPT
in education).
67. 
See, e.g., Nori, King, McKinney, Carignan & Horvitz, supra note 56, at
1 (testing GPT acting alone).
68. 
See, e.g., Fabrizio Dell'Acqua et al., Navigating the Jagged Technologi-
cal Frontier: Field Experimental Evidence of the Effects of Al on Knowledge
Worker Productivity and Quality 2 (Harvard Bus. Sch., Working Paper 24-013,
2023) (on file with the Minnesota Law Review) [hereinafter Navigating the Jag-
ged Technological Frontier] (studying the productivity of consultants working
with GPT-4).

2024]
163

MINNESOTA LAW REVIEW

Outside of the exam setting, a small number of studies have
evaluated how Al can improve human performance at non-legal
professional writing tasks.69 One study found that giving college-
educated professionals access to GPT-3.5 substantially improved
their performance at a variety of writing tasks, with the greatest
gains going to the least-skilled workers. 70 On the other hand,
other empirical work has suggested that human use of Al to as-
sist with certain tasks can undermine humans' incentives to
take care. 71

One of the most extensive studies of AI-assistance in
knowledge-intensive work examined the effect of AI-assistance
on a range of work tasks common within the field of high-level

69. There are some recent papers that evaluate how access to generative AI
can improve professionals' ability to perform non-writing tasks, like computer
coding. See, e.g., Sida Peng, Erini Kalliamvakou, Peter Cihon & Mert Demirer,
The Impact of AT on Developer Productivity: Evidence from GitHub Copilot 2
(Feb. 13, 2023) (unpublished manuscript) (on file with the Minnesota Law Re-
view) (examining "the productivity effects of AI on software development").
None of these studies evaluate how more-sophisticated prompting techniques
can impact results.
70. 
Shakked Noy & Whitney Zhang, Experimental Evidence on the Produc-
tivity Effects of Generative Artificial Intelligence, 381 SC1. 187, 190 (2023). To
reach this conclusion, the experimenters recruited over 400 participants in five
professional categories: grant writers, consultants, data analysts, human re-
source professionals, and managers. Id. at 187. Participants were then tasked
with completing two short writing assignments comparable to those they would
complete in their professional settings, such as drafting press releases, short
reports, or emails. Id. After completing the first writing assignment, half of the
participants were given access to ChatGPT for the second writing assignment.
Id. The study found that participants who were provided with access to
ChatGPT completed their writing tasks faster and produced higher quality
work than participants who were not provided access to this tool. Id. at 188.
Moreover, the participants who performed relatively poorly on the initial task
(which took place prior to being instructed how to use ChatGPT) disproportion-
ately benefited from access to AI, receiving both higher quality scores and tak-
ing decreased amounts of time to complete their writing task. Id. at 188-89. By
contrast, access to ChatGPT did not improve the quality of work for participants
who scored well in the initial writing task, though it did increase the speed at
which they could produce that work. Id.
71. 
See Fabrizio Dell'Acqua, Falling Asleep at the Wheel: Human/AI Col-
laboration in a Field Experiment on HR Recruiters 1 (Dec. 2, 2021) (unpublished
manuscript) (on file with the Minnesota Law Review) [hereinafter Falling
Asleep at the Wheel] ("As AT quality increases, humans have fewer incentives
to exert effort and remain attentive, allowing the AT to substitute, rather than
augment their performance.").

164
[109:147

LAWYERING IN THE AGE OF AI1

management consulting. 72 The results show that Al is remarka-
bly capable of increasing both quality and productivity on certain
types of tasks but not others, even where the tasks are consid-
ered of similar difficulty. 73 Specifically, consultants completing a
series of tasks that involved conceptualizing and developing new
product ideas significantly improved both the quality and speed
of their work with the assistance of AI.74 Where consultants were
working on problem-solving tasks that required the synthesis of
quantitative data and qualitative information from interviews,
Al provided much less of a boost. 75 Further, the greatest gains
on both tasks were seen in the group that not only used Al assis-
tance, but were also trained in effective prompt engineering. 76

The study also found, consistent with studies conducted by Choi
& Schwarcz and Noy & Zhang, that the most significant benefi-
ciaries of Al assistance were lower-skilled participants. 77 How-
ever, in contrast to Choi & Schwarcz, the study found perfor-
mance improvements even among those in the top half of skill
rankings. 78 While quality and productivity improved in all
groups utilizing Al, the study found that on tasks involving cre-
ativity, those using the assistance of Al showed less variability
in ideas than among those working without AI.79 Researchers
also found that participants who blindly adopted Al outputs

72. Navigating the Jagged Technological Frontier, supra note 68, at 2 (stud-
ying AI performance with Boston Consulting Group).
73. Id. at 8-15.
74. Id. at 7, 10; see also Karan Girotra, Lennart Meincke, Christian Ter-
wiesch & Karl T. Ulrich, Ideas are Dimes a Dozen: Large Language Models for
Idea Generation in Innovation 1 (Mack Inst. For Tech. Innovation, Working Pa-
per, 2023) (on file with the Minnesota Law Review) (finding that GPT-4 can
generate ideas faster and cheaper than college students at an elite university).
75. Navigating the Jagged Technological Frontier, supra note 68, at 13-15
(requiring GPT to use both quantitative and qualitative data resulted in "a sig-
nificant negative impact" on GPT performance).
76. Id. at 10, 15.
77. Id. at 11 (finding a forty-three percent increase in performance among
those ranked in the bottom half of skill level).
78. Id. at 11 (finding a seventeen percent increase in performance among
those ranked in the top half).
79. Id. at 12; see also Leonard Boussioux, Jacqueline N. Lane, Miaomiao
Zhang, Vladimir Jacimovic & Karim R. Lakhani, The Crowdless Future? How
Generative Al Is Shaping the Future of Human Crowdsourcing 1 (Aug. 8, 2023)
(unpublished manuscript) (on file with the Minnesota Law Review) (similarly
finding that GPT-4 may decrease some forms of creativity and novelty compared
to purely human outputs).

2024]
165

MINNESOTA LAW REVIEW

suffered a decrease in performance compared to those not using
Al assistance at all.80

In sum, the literature to date suggests that Al holds real
promise 
to 
effectively assist with lawyering and 
other
knowledge-based tasks, but also comes with some well-docu-
mented shortcomings. 81 GPT-4 and other LLMs sometimes hal-
lucinate sources and sometimes fail to interpret sources accu-
rately. 82 In addition, there are indications from several studies
that the lowest-skilled workers benefit the most from Al assis-
tance, with Al providing no benefit to or even possibly a negative
effect on the performance of highly skilled humans.83

Our study aims to move the literature forward by evaluating
the effect of GPT-4 assistance, in terms of both quality and effi-
ciency, on four different lawyering tasks that are representative
of the types of tasks a junior attorney might be asked to perform.

II. METHODOLOGY

We recruited students from the University of Minnesota
Law School in April 2023 to participate in our study over Sum-
mer of 2023.84 Well over 100 students expressed interest in par-
ticipating in the study. 85 We initially enrolled the first sixty such

80. Navigating the Jagged Technological Frontier, supra note 68, at 17
("Professionals who had a negative performance when using AI tended to
blindly adopt its output and interrogate it less." (citation omitted)).
81. 
See supra notes 48-80 and accompanying text (detailing AI's capabili-
ties and shortcomings).
82. 
See Dahl, Magesh, Suzgun & Ho, supra note 2, at 8-11 (describing hal-
lucinations in the legal context); Nay et al., supra note 50, at 3, 8 (demonstrating
inaccuracies when LLMs interpret tax law based on the CFR and the U.S. Code).
83. 
See, e.g., Al Assistance in Legal Analysis, supra note 8, at 12-13, 17
(studying AT use on law exams).
84. 
The University of Minnesota Law School is one of the top law schools in
the country, currently ranked sixteenth in the U.S. News ranking of law schools.
2024 Best Law Schools, U.S. NEWS (2024), https://www.usnews.com/best
-graduate-schools/top-law-schools/law-rankings [https://perma.cc/TG6H
-9HER].
85. 
One of the co-authors sent a recruiting email to the entire University of
Minnesota Law School student body in April 2023. The email explained that we
were recruiting "current JD students, including class of 2023 graduates, for par-
ticipation in a study that examines the use of artificial intelligence tools, specif-
ically GPT-4, to assist with basic lawyering tasks." To participate in the study,
students or graduates would need to be available to work for up to fifteen hours
total during June 2023. The email also noted that the work could be completed

166
[109:147

LAWYERING IN THE AGE OF AI1

volunteers and placed the remaining volunteers on a waitlist. 86

Over the duration of the study, twenty-two of the participants
dropped out because they were unable to complete the entirety
of the experiment; as they did so, we replaced them with new
participants from the waitlist to ensure that we achieved
roughly the target number of sixty study participants. Ulti-
mately fifty-nine students completed the experiment.
During the enrollment process, we gathered basic infor-
mation about study participants, including their first-semester
first-year law school GPA and their anticipated graduation
year. 87 We then randomly sorted these participants into two
thirty-person groups and confirmed that these two groups were
roughly balanced with respect to graduation year and first-se-
mester law school grade point average.
Study participants completed the experiment remotely, on
their own schedule, from June to early August of 2023. Initially,
they completed three online training modules that we developed
and taught on how to use GPT-4 effectively in legal analysis. 88

Doing so required students to watch approximately two hours of
training videos and to complete several short exercises using
GPT-4. The training included both general techniques on how to
prompt GPT-4 effectively (for example, by breaking down legal
analysis into pieces and supplying relevant legal rules or
sources) and how to use it specifically in litigation and transac-
tional settings. It focused on how to apply active lawyering skills
while using Al, rather than mechanically relying on the output
of GPT-4. For example, we instructed participants to first assess

remotely and on participants' own time-schedules and that participants who
completed the study would receive $300 in compensation for their time.
86. This experimental design was approved by the University of Minne-
sota's Institutional Review Board (IRB). Participants agreed to participate after
reviewing and agreeing to an IRB-approved consent form.
87. 
We also collected contact information, including email and mailing ad-
dresses, and screened for prior enrollment in two classes that disqualified inter-
ested individuals from enrolling in the study because assigned study tasks over-
lapped with projects in those courses.
88. This training drew heavily on previous work by two of us. See generally
Daniel Schwarcz & Jonathan H. Choi, AI Tools for Lawyers: A Practical Guide,
108 MINN. L. REV. HEADNOTES 1 (2023) [hereinafter AI Tools for Lawyers].
These materials have served as the basis for numerous practical training ses-
sions that we have conducted for real lawyers in a variety of settings, including
Continuing Legal Education presentations, presentations for in-house legal
teams, and presentations for lawyers working at large law firms.

2024]
167

MINNESOTA LAW REVIEW

assignments on their own before using GPT-4 to generate an-
swers. Additionally, the training required participants to prac-
tice these skills by using GPT-4 to answer sample problems. Sec-
tion A of the Appendix provides additional information about the
training materials used.
After completing the training, the participants then com-
pleted four basic lawyering tasks, representing a range of com-
mon tasks for entry-level lawyers.
The first assignment involved drafting a complaint for a fic-
tional client to be filed in federal court on the basis of Section
1983, intentional interference with a business relationship, and
malicious prosecution. Participants were not required to perform
independent legal research for this task; they were provided with
the elements of each cause of action in order to draft the com-
plaint. The maximum time permitted for this task was five
hours.
The second task required drafting a simple contract between
a homeowner and housepainter. Participants were provided with
the material terms of the contract and instructed to write the
contract in plain English with a length not to exceed two pages.
Participants were instructed to spend no more than two hours
on this task.
The third assignment required participants to draft a short
section of an employee handbook that explains employees' rights
under federal and state (Minnesota) law to take breaks in order
to pump breastmilk for a child. This task required legal research,
as participants were not provided with the relevant statutes.
Participants were instructed to limit their work product to a sin-
gle page and spend no more than one hour on this task.
The fourth and final task involved a fictional client with a
potential product liability issue-namely, whether the client
should be advised to place a warning label on a product when the
product contains an allergen. The task required participants to
read four provided cases but did not require independent legal
research to complete. Each participant drafted a legal memoran-
dum to the client offering legal analysis and advice on how best
to proceed. Participants were instructed to spend no more than
five hours on this task. Section B of the Appendix contains addi-
tional information about these assignments.
In addition to submitting their work product, each partici-
pant was asked to track the time they spent completing each

168
[109:147

LAWYERING IN THE AGE OF AI1

task, and that time allocation was recorded separately from the
work product so that it would not influence grading in any way.
Participants were compensated at a flat rate for their study
participation in order to discourage participants from spending
more time than necessary on a task in order to maximize their
compensation. Participants also received the following instruc-
tions for each task:

You should approach the assignment as if you are a junior attorney
who has been asked to produce work for a fee-sensitive client. While
you can take up to the maximum time allotment to complete the task,
you should stop working at the point where you would feel comfortable
submitting your work product to a supervising attorney, given that
your client would prefer to minimize the amount they pay for your work
product. If you reach the end of the maximum time allocation and have
not finished, you should simply turn in the work product you were able
to produce within the allotted time. Do not spend any more than the
maximum time on any assignment.
The participants were divided between two groups: Group A
and Group B. Each participant, whether assigned to Group A or
Group B, was required to complete all four tasks. However, each
group was instructed to use the assistance of GPT-4 on two of
the four tasks, and to refrain from using GPT-4 or any other type
of Al for the remaining two tasks. Specifically, Group A used
GPT-4 for the contract drafting and complaint drafting tasks,
while Group B used GPT-4 for the employee handbook and client
memo tasks.
To provide access to GPT-4 to participants, we created a cen-
tral ChatGPT "clone" website using the GPT-4 API, and gave
students access to that website. 89 This clone website had a
nearly identical user interface and used the same system prompt
as the real ChatGPT Plus with GPT-4.
After all study participants had completed the four tasks in
the experiment, we graded all participant work product anony-
mously, with no knowledge of participant identity or GPA, GPT
use, or time spent on task. Grades were assigned based on grad-
ing standards and norms at the University of Minnesota Law
School, where each study investigator has taught, but were not
adjusted or "curved" in any manner. Each task was graded in its

89. 
Most people can access GPT-4 by creating a paid ChatGPT Plus account
on the OpenAl website. However, it was not administratively possible to create
such an account for each study participant without requiring participants to
outlay cash on the subscriptions themselves.

2024]
169

MINNESOTA LAW REVIEW

entirety by a single investigator using a pre-determined grading
rubric to help ensure consistency.
At the completion of the experiment, all participants were
asked to take an anonymous survey regarding their experience.
Although the survey was anonymous on a per-respondent basis,
we tracked responses separately for Groups A and B, allowing
us to register how each group felt on average about their respec-
tive assignments. We pre-registered our methods and hypothe-
ses prior to analyzing our results; the pre-registration statement
is archived with the Open Science Foundation.9 0

III. RESULTS

Overall, we found that access to Al caused little average im-
provement on the quality of output in lawyering tasks but a sub-
stantial increase in speed of completion. However, the boost in
quality from Al assistance depended on baseline: participants
who had the worst performance without assistance from GPT-4
received the largest quality benefits, with little quality benefit to
participants who were capable of producing high-quality work on
their own. In contrast, the improvement in speed was largely
consistent among participants. When surveyed on their impres-
sions, participants reported positive impressions of the Al, in-
cluding positive reviews for the AI's impact on both speed and
quality. Respondents indicated that their ability to use Al im-
proved over the course of the experiment and that they were
more likely to use Al tools in the future as a result of the exper-
iment. Finally, respondents accurately assessed the tasks for
which Al was most helpful even without knowledge of their
grades on the various tasks.
Table 1 below shows statistics for the grades received and
time taken for each task.91 It shows that the differences are rel-
atively small in magnitude. Access to GPT-4 had the largest pos-
itive effect for contract drafting, where the difference in grade it

90. 
See Jonathan H. Choi, Amy B. Monahan & Daniel Schwarcz, The Use
of Artificial Intelligence to Assist with Basic Lawyering Tasks, OPEN SCI.
FRAMEWORK (Aug. 23, 2023), https://osf.io/n5saz [https://perma.cc/NJ29-G2V8].
See generally Jason M. Chin & Kathryn Zeiler, Replicability in Empirical Legal
Research, 17 ANN. REv. L. SOC. & SCI. 239, 243 (2021) (discussing the benefits
of pre-registering a data collection and analysis plan in the context of empirical
legal research).
91. 
All confidence intervals in this Article were generated using empirical
bootstraps with 10,000 iterations.

170
[109:147

LAWYERING IN THE AGE OF AI1

generated was approximately two thirds of the difference be-
tween a B and a B+. The results also show substantial variation
between tasks. On the client memo and employee handbook
task, respondents saw, on average, a near zero effect on perfor-
mance from using GPT-4.

Table 1: Average Performance at Tasks with and
Without GPT-4 (Grade on 4.0 Scale)

With
No GPT-4 
WPt4 
Diff. 
P-
(Std. Dev.) (St 
(95% CI) 
value

Complaint 
3.14 
3.31 
0.17 
0.0862
Drafting 
(0.59) 
(0.50) 
(-0.03, 0.37)
Contract 
3.00 
3.24 
0.24 
0.0060
Drafting 
(0.56) 
(0.40) 
(0.07, 0.41)
Employee 
3.20 
3.26 
0.07 
0.3532
Handbook 
(0.41) 
(0.39) 
(-0.07, 0.21)
Client 
2.92 
2.85 
-0.07 
0.5980
Memo 
(0.69) 
(0.76) 
(-0.34, 0.18)

Figure 1 through Figure 4 below depict the simple distribu-
tion of grades on tasks for groups with and without Al assis-
tance. These Figures are density plots, presenting the number of
participants (on the y-axis) who received each grade (on the x-
axis).92 Figure 18 through Figure 21 in the Appendix show the
bootstraps for the difference in means for groups with and with-
out access to GPT, showing that only contract drafting showed a
statistically significant increase in performance at the ninety-
five percent level.

92. 
All figures in this Article were generated using the SciPy package in
Python. Density plots were generated with Gaussian Kernel Density Estimation
(used for irregular data distributions) through the gaussiankde package in
SciPy, which applies Scott's Rule to determine bandwidth. See generally Adri-
ano Z. Zambom & Ronaldo Dias, A Review of Kernel Density Estimation with
Applications to Econometrics, 5 INT'L ECONOMETRIC REV. 20, 29-33 (2013) (dis-
cussing methods of determining the smoothing parameter for kernel density es-
timation).

2024]
171

172
MINNESOTA LAW REVIEW
[109:147

Figure 1: Quality Distributions with and Without
AI-Complaint Drafting

No GP'T
With GPT
0.7 -
Mean (No GP1T)

-
Mean (With GPT)

0.6

0.5

0.4-

0.3

0.2

0.1

0.0 
0.5 
1,0 
1.5 
2.0 
2.5 
3.0 
3.5 
4.0
Grade

Figure 2: Quality Distributions with and Without
AI-Contract Drafting

0.8 
No GPT
With GPT
- Mean (No CPT)
0.7 
- Mean (With GPT)

0.6

0.5

E0.4

0.3

0.2

0.1

0.5 
1.0 
1.5
G.ud
Grade
4.0

LAWYERING IN THE AGE OF AI1

Figure 3: Quality Distributions with and Without
AI-Employee Handbook

No GPT
With GPT
-
Mean (No GPT)
0.8 
M 
GPT

0.5 
L0 
1.5 
2.0
Grade
2.5
3.0 
3.5 
4.0

Figure 4: Quality Distributions with and Without AI-
Client Memo

No GPT
With GPT
-
Mean (No OPT)
05 -- Mean (Withb GPT)

0.4

0.3

0.2

0.1

0$0 0.5
1.0 
1.5 
2.0
Grade
2.5 
3.0 
3.5 
4.0

0.4

0.2

2024]
173

MINNESOTA LAW REVIEW

Table 2 below depicts the effect of access to GPT on the
amount of time taken on each task. These results are more deci-
sive, showing large and consistent decreases in the amount of
time taken on each task. Interestingly, the largest gain in speed
(in percentage terms) occurs in the task for which GPT-4 was the
most useful in terms of grade improvement (contract drafting),
and the smallest gain in speed occurs in the task for which GPT-
4 was the least useful (client memo).

Table 2: Average Time Taken on Tasks with and
Without GPT-4 (Minutes)

No 
With

Task 
GPT-4 
GPT-4 
Difference 
% 
p-
(Std. 
(Std. 
(95% CI) 
Diff. 
value
Dev.) 
Dev.)

Complaint 
160.69 
122.00 
-38.77 
24.1 
0.0018

Drafting 
(72.38) 
(66.80) 
(-64.00, -13.36)

Contract 
69.72 
47.59 
-22.40 
32.1 
0.0000

Drafting 
(32.00) 
(31.09) 
(-33.71, -10.91)

Employee 
37.24 
29.41 
-7.84 
21.1 
0.0000

Handbook 
(9.55) 
(13.42) 
(-12.03, -3.74)

Client 
244.41 
215.69 
-28.75 
11.8 
0.0152

Memo 
(58.03) 
(72.96) 
(-52.59, -5.05)

174
[109:147

2024]
LAWYERING IN THE AGE OF AI
175

Figure 5 through Figure 8 below show the distributions of
the amount of time that participants took on each task. Figure
22 through Figure 25 in the Appendix show bootstraps for the
differences in means between groups, showing that the decrease
in the time participants took on every task is statistically signif-
icant at the ninety-five percent level.

Figure 5: Time Distributions with and Without AI-
Complaint Drafting

No GPT
'With GPT
0.00Menn 
(No GPT)
Mea n (With GPT)

0.004

0.002
oooi

)0001-

400
Time (Minutes)

MINNESOTA LAW REVIEW
[109:147

Figure 6: Time Distributions with and Without AI-
Contract Drafting

No GPT
With GPT
-
Mean (No GPT)
Mean (With GPT)

0.012

0.010

0.008

0.006

0.004

0.002

0.000

Time (Minutes)

Figure 7: Time Distributions with
Employee Handbook

0.035

0.030

0.025

20.020

0.015

0.010

0.005

0.000,

and Without Af-

No GPT
With GPT
-
Mean (No GPT)
- Mean (With GPT)

Time (Minutes)

176

160

] AWYERING IN THE AGE OF AI1

Figure 8: Time Distributions with
Client Memo

0.008

-

0.008

0.005

0.001

0.002

0.001

0.O0~i
OM( 
~ 
t 
) 
ZU 
Z)

TIiime, 
1;;il te 0

and Without AI-

No CPT
Vvith( iT

~ 
¶ 
n ( ~o CPT)
Mean (WiTh (WE)

300 
~3~() 
40()

In addition to raw results comparing the groups that did and
did not have access to GPT-4, we can also evaluate how the effect
of Al assistance on performance and time taken varied within
each group. Namely, we can test whether the boost provided by
GPT-4 was larger for participants who performed better without
access to GPT-4. To conduct this comparison, we graph perfor-
mance at one task against performance at another task. Recall
that each participant completed two tasks with the aid of GPT-4
and two tasks without access to the Al. We should expect that
performance at one legal task should somewhat predict perfor-
mance at any other legal task. Thus, we can first take each par-
ticipant's grade at one task they conducted without GPT-4
(graphed on the x-axis) and compare that against their perfor-
mance at the other task without GPT-4 (graphed on the y-axis).
This creates a baseline that we can use as a control to establish
how replicable performance is in the absence of access to Al,
shown as the blue line in Figures 9 through 12 below. Conceptu-
ally, if performance is perfectly correlated between tasks, this
line should be a forty-five-degree angle where x =y. The graphs
are separated based on which task was used as Task 2.

2024]
177

MINNESOTA LAW REVIEW

We can then take the two tasks that each participant com-
pleted without access to Al and use them to graph another line,
showing how their performance on a task without GPT-4 (on the
x-axis) predicts performance with access to GPT-4 (on the y-axis).
This is the red line in the figures below. 9 3 For each of the follow-
ing Figures, Task 2 is held constant for each graph, while Task
1 includes participants' performance on the other relevant tasks.
Thus, given each participant's actual grade on a different task
(located on the x-axis), the corresponding point on the blue line
on the y-axis is their expected grade on Task 2 without GPT-4's
assistance, and the corresponding point on the red line on the y-
axis is their expected grade with GPT-4's assistance. This
means, for instance, that if the red line is consistently higher
than the blue line, the expected benefit from using GPT-4 is pos-
itive regardless of baseline skill level.
Most importantly, the relative slopes of the red and blue
lines tell us whether or not GPT-4 acts as an equalizing force. If
Al assistance flattens the distribution of performance, the red
line will be flatter than the blue line; if Al has no effect on the
distribution of performance, the red line should run parallel to
the blue control line. The difference in the slopes of the blue and
red lines measures the extent to which access to GPT-4 flattens
performance.

93. 
The range of the treatment and control lines on the x-axis differ for
some of the graphs, because the range of grades awarded to students differed
by task, and the tasks available to serve as the treatment and control groups
differ depending on the task that is being studied.

178
[109:147

2024] 
LAWYERING IN THE AGE OF AI 
179

Figure 9: Task 1 vs. Task 2 Grades-
Complaint Drafting

4.0
-
No GPT
With GPT

3.0

' 2.5

S2.0

SL.5

1.0

0.5

0 
.0 
0.5 
1.0 
1.5 
2.0 
2.5 
3.0 
3.5 
4.0
Grade (Task 1)

Figure 10: Task 1 vs. Task 2 Grades-
Contract Drafting

.0- No GPT
-With GPT
3.5

3.0

S2.0

LO
z1.5

1.0

0.5

0 
.0 
0.5 
1.0 
1.5 
2.0 
2.5 
3.0 
3.5 
4.0
Grade (Task 1)

180 
MINNESOTA LAW REVIEW 
[109:147

Figure 11: Task 1 vs. Task 2 Grades-
Employee Handbook

4.0
-
No GPT
- With GPT
3.5

3.0

'R 2.5

02.0

C5 1.5

1.0

0.5

4.0 
0.5 
1.0 
1.5 
2.0 
2.5 
3.0 
3.5 
4.0
Grade (Task 1)

Figure 12: Task 1 vs. Task 2 Grades-Client Memo

4.0 -
No GPT
-
With GPT
3.5

3.0

9 2.5

2.0

c 1.5

1.0

0.5

0 .0 
0.5 
1.0 
1.5 
2.0 
2.5 
3.0 
3.5 
4.0
Grade (Task 1)

LAWYERING IN THE AGE OF AI1

As the Figures show, where GPT-4 assistance provided
some benefit, that benefit was unequally distributed. On the
tasks where GPT-4 was most useful (the contract drafting and
complaint drafting tasks) the slope of the line with access to GPT
is substantially flatter than the line without, indicating that
GPT-4 provides a greater boost to low performers than high per-
formers. On the tasks where GPT-4 had near zero effect on per-
formance (the client memo and employee handbook tasks) the
slopes of the treatment and control lines are almost identical,
indicating that access to GPT-4 had roughly the same impact re-
gardless of baseline performance-that is, no impact.
In sum, where assistance from GPT-4 is beneficial at all, it
seems to benefit the worst performers the most, providing little
or no benefit to top performers. Table 3 below confirms that, for
the tasks on which Al assistance was most useful (Complaint
Drafting and Contract Drafting) the differences in slopes are
large and statistically significant at the ninety-five percent level.

Table 3: Slope of Performance Between
Tasks 1 and 2 (Grade)

Task 
No GPT 
With GPT 
Difference
(95% CI) 
(95% CI) 
(95% CI)
Complaint 
0.66 
0.16 
0.50
Drafting 
(0.35, 0.95) 
(0.00, 0.28) 
(0.20, 0.84)
Contract 
0.56 
0.19 
0.37
Drafting 
(0.33, 0.80) 
(-0.06, 0.20) 
(0.22, 0.74)
Employee 
0.01 
0.06 
-0.05
Handbook 
(-0.21, 0.19) 
(-0.03, 0.21) 
(-0.33, 0.13)
Client 
0.29 
0.25 
0.01
Memo 
(-0.64, 0.48) 
(0.25, 0.75) 
(-1.16, 0.06)

We can conduct the same sort of analysis for the effect of Al
assistance on the amount of time taken to complete each task,
shown in Figures 13 through 16 below. Because each task took a
different amount of time on average, we scaled the raw minutes
spent by dividing them by the mean minutes spent per task
(whether with GPT-4 or without), in order to be able to aggregate
different tasks into Task 1 and to make the slopes directly com-
parable. Although access to GPT-4 consistently decreased the
time taken on each task (the red lines are consistently below the

2024]
181

MINNESOTA LAW REVIEW

blue lines), they are generally parallel, indicating no leveling ef-
fect on the amount of time taken depending on the baseline
amount of time taken. The one exception is contract drafting,
where there is a difference in slopes, although it is not statisti-
cally significant at the ninety-five percent level. Our results
therefore suggest that GPT-4 has the potential to reduce time
spent on tasks for lawyers of all ability levels.

Figure 13: Task 1 vs. Task 2 Time-
Complaint Drafting

2.0

1.0

afl

0.0
0Scled 
0 
T 10 
(s 11.)

No GPT
With GPT

182
[109:147

2024] 
LAWYERING IN THE AGE OF AI 
183

Figure 14: Task 1 vs. Task 2 Time-Contract Drafting

-
No GPT
With GPT

2.0

x 1.5

1.0

0

0.5

0.0
0.0
0.5 
1.0 
1.5 
2.0
Scaled Time (Task 1)

Figure 15: Task 1 vs. Task 2 Time-
Employee Handbook

-
No GPT
16 -
With GPT

1.4

0.6

0.4

0.2

0.0
2.0
1.0 
1.5
Scaled Time (Task 1)

184 
MINNESOTA LAW REVIEW 
[109:147

Figure 16: Task 1 vs. Task 2 Time-Client Memo

-No c PT
l. 
- Wi hGPT

1.2

r-0.8

0.4

0.5 
1.u 
1.5
Scaled Time (Task 1)
Q00
2.0

LAWYERING IN THE AGE OF AI8

Table 4 reflects these results.

Table 4: Slope of GPT-4 on Performance (Grade)

Task 
No GPT 
With GPT 
Difference
(95% CI) 
(95% CI) 
(95% CI)
Complaint 
0.63 
0.60 
0.03
Drafting 
(0.39, 0.90) 
(0.26, 0.88) 
(-0.32, 0.48)
Contract 
0.74 
0.40 
0.34
Drafting 
(0.52, 0.96) 
(0.12, 0.75) 
(-0.08, 0.68)
Employee 
0.28 
0.34 
-0.06
Handbook 
(0.05, 1.03) 
(0.16, 0.45) 
(-0.30, 0.71)
Client 
0.32 
0.29 
0.03
Memo 
(0.07, 0.58) 
(0.18, 0.38) 
(-0.22, 0.31)

Finally, we surveyed study participants on their perceptions
of GPT-4 based on the assignments. The survey questions asked
participants to report their perceptions of the impact GPT-4 ac-
cess had on the quality of their work and the speed with which
they were able to complete tasks. They were also asked to rate
their perceived helpfulness of GPT-4 for each individual assign-
ment. In addition, participants were asked about whether they
thought their skill using GPT-4 improved over the course of the
experiment, whether having access to GPT-4 improved their per-
sonal satisfaction with work assignments, and various questions
aimed at measuring their interest in using GPT-4 to assist with
legal work in the future.

Survey Questions
(a) For the assignments on which you had access to GPT-4,
to what extent did this access impact the quality of the
work that you completed for these assignments?
(b) For the assignments on which you had access to GPT-4,
to what extent did this access impact the speed with
which you could complete the assignments?
(c) For the assignments on which you had access to GPT-4,
to what extent did this access impact the personal satis-
faction that you experienced in completing these assign-
ments?

2024]
185

MINNESOTA LAW REVIEW

(d) To what extent did you find that your ability to use GPT-
4 effectively for legal drafting improved over the course of
the experiment?
(e) How did your experience in this experiment impact the
extent to which you anticipate using tools like GPT-4 for
legal work in the future?
(f) To what extent did you find access to GPT-4 to be helpful
for the complaint drafting assignment specifically?
(g) To what extent did you find access to GPT-4 to be helpful
for the contract drafting assignment specifically?
(h) To what extent did you find access to GPT-4 to be helpful
for the Employee Handbook drafting assignment specifi-
cally?
(i) To what extent did you find access to GPT-4 to be helpful
for the Legal Memo drafting assignment specifically?

Figure 17: Survey Results by Question

5

-

4-

3-

S2-

1-

0-
(a) 
(b)
(c)
(d)
(e)
Questions

SSurvey A
Survey B

-
~

I
I

Survey

0-

I

k

k

11
I
I

186
[109:147

(#) 
(,) 
(h) 
6)

LAWYERING IN THE AGE OF AI1

Participants responded to these questions using a Likert
scale with 5 values: substantially no, somewhat no, neither yes
nor no, somewhat yes, and substantially yes (with appropriate
modification based on the wording of the specific question). The
results are interesting along several different dimensions. First,
recall that Group A and Group B had access to GPT-4 on differ-
ent assignments, and that Group A used GPT-4 for the tasks on
which it was generally most effective (contract drafting and com-
plaint drafting). Consistent with those assignments, Group A re-
ported on average that GPT-4 had a larger effect both on the
quality and speed of their work. Participants in Group A also
reported a larger boost to personal satisfaction when provided
access to GPT-4. Both groups reported that their ability to use
GPT-4 improved over the course of the assignments and that
participating in the study made them more likely to use GPT-4
for future work. Finally, respondents accurately perceived how
useful GPT-4 was for specific tasks. In fact, the ordinal ranking
of the impact of Al assistance on task performance exactly cor-
responds with the ranking of how useful participants perceived
Al to be on each task, with contract drafting ranked the highest
and the client memo ranked the lowest.

IV. LIMITATIONS, ASSUMPTIONS, AND ROBUSTNESS
CHECKS
Although we attempted to design our experiment as cleanly
as possible, we inevitably made assumptions or design choices
that could potentially limit the robustness or validity of our find-
ings. We describe them here to appropriately frame our results.
First, our experiment had a relatively small sample size,
with fifty-nine participants each completing four tasks. Many
studies in the literature on human-computer interaction collect
far larger samples in order to maximize statistical power; for ex-
ample, Noy and Zhang gathered a sample of 453 participants for
their study of AI's effect on professional writing tasks. 94 The
tradeoff is that to keep costs manageable, Noy and Zhang (like
many other scholars) recruited participants from a low-cost
online survey provider, gave them virtually no training, and had
them complete simple, short tasks.

94. 
Noy & Zhang, supra note 70, at 187.

2024]
187

MINNESOTA LAW REVIEW

In contrast, we chose to prioritize external validity rather
than statistical power. We recruited upper-level law students ra-
ther than laypeople, designed realistic lawyering tasks that took
an average of 463.5 minutes (7.725 hours) for participants to
complete, and provided several hours of training prior to task
completion. Scaling the sample size would have ballooned the
cost of the study to hundreds of thousands of dollars. However,
our choice to focus on external validity comes at the cost of pre-
cision, and due to the small sample size, our estimates are gen-
erally noisier than we would like.
A second set of limitations relates to the assignment of
tasks. All participants completed their tasks in the same order,
because we did not want the treatment effect of Al assistance to
be confounded with ordering effects-if, for example, we reor-
dered the tasks so that all participants first completed two tasks
without Al assistance and then two tasks with assistance, per-
formance improvements might be attributable to increased fa-
miliarity with the tasks rather than the Al assistance itself.
However, because the tasks were always completed in the same
order, it is possible that the ordering interacted with the treat-
ment (Al assistance) in unforeseen ways. For example, it is pos-
sible that Al was less useful for the later tasks because Al assis-
tance is more valuable when participants are "fresh." While we
do not find this explanation particularly likely, future research
could delve further into this issue.
Relatedly, we assigned all participants into one of two
groups rather than conducting full randomization. We did this
because it made the experiment easier to administer and in or-
der to guarantee that each participant completed two tasks with
Al assistance and two tasks without. (When recruiting for the
study, we promised to allow all participants the opportunity to
contrast their own performance with and without Al.) However,
this structure makes it especially important that we conduct ef-
fective randomization such that the two groups are identical, so
that any differential in their performance can be attributed
solely to Al assistance. Otherwise, any differences between
treatment and control with respect to each of the tasks could be
driven by differences between the groups themselves.
To validate that Group A and Group B were correctly ran-
domized, we compare whether the two groups match on observ-
ables. We collected individual-specific data for class year and
first-year first-semester grade point average. We did not collect

188
[109:147

LAWYERING IN THE AGE OF AI1

other demographic information out of concerns about anonymity.
Table 5 provides information about individual characteristics,
including means and standard deviations, as well as the differ-
ence between the two groups. The differences have p-values of
0.44 for class year and 0.92 for grade point average and do not
suggest any statistically significant differences between the two
groups.
Table 5: Group A and Group B
Individual Characteristics

Group A 
Group B 
Diff. (95% CI)
Class 
2024.38 
2024.52 
0.14
Year 
(0.68) 
(0.69) 
(-0.48, 0.21)
1L Fall 
3.35 
3.34 
0.01
GPA 
(0.36) 
(0.35) 
(-0.17, 0.19)

In addition, we conducted Kolmogorov-Smirnov tests to es-
timate the likelihood that the class years for Group A and Group
B, and the grade point averages for Group A and Group B, were
drawn from the same distribution. The Kolmogorov-Smirnov
statistic for class year was 0.14 (p = 0.95) and for grade point
average was 0.10 (p = 1.00), again not suggesting any difference
between the two groups.
Although Group A and Group B appear to have been effec-
tively randomized, our grouping methodology has one further
implication, specifically for the discussion accompanying Figure
9 through Figure 16. Recall that each of those figures contained
a line representing a control (the predicted grade in a specific
task without Al assistance based on the participant's grade in
another task completed without Al assistance) as well as a treat-
ment (the predicted grade in a specific task with Al assistance
based on the participant's grade in another task completed with-
out Al assistance). Recall as well that we are looking specifically
at the difference in slopes between these two lines. Because each
group completed a different set of tasks without Al assistance,
we assume that, on average, performance on each task predicts
performance on other tasks equally well.

2024]
189

MINNESOTA LAW REVIEW

Third, we implicitly make the stable unit treatment value
assumption (SUTVA),95 including the assumption that the per-
formance of the participants in the control group does not differ
in light of their assignment to the treatment group on other
tasks. It is possible that this assumption is violated to some ex-
tent. For example, participants completing tasks without the as-
sistance of Al might subconsciously expect that their perfor-
mance on unassisted tasks should be worse in comparison to
tasks where they have access to Al and therefore might exert
less effort on those tasks than they would have outside of an ex-
perimental setting, where they were simply completing unas-
sisted Al tasks alone.
There is some evidence to suggest that SUTVA holds against
this possibility. Intuitively, students participated in the experi-
ment in part to gauge how much their productivity would im-
prove when given access to Al. They would only receive the ben-
efit of a meaningful comparison if they exerted full effort, giving
them some incentive not to shirk. In addition, using time spent
completing each task as a proxy for effort, the students spent
more time on the tasks without Al assistance, not less, suggest-
ing that any subconscious shirking was marginal.
Fourth, participants in our study were all students or recent
graduates of a highly selective law school who expressed interest
in participating in a study evaluating the use of Al for legal
tasks.96 As a result, our study participants likely reflect a higher
skill level than those of an average law student or recent gradu-
ate and may also possess greater technological proficiency and
comfort than the average lawyer or law student. Some partici-
pants may have had some prior exposure to using generative Al
to complete legal tasks.
Fifth, the tasks assigned to study participants were not per-
fectly representative of tasks that a junior lawyer would face.
While we believe that they accurately capture certain key skills,
they were simplified in various ways. The client memo did not
require independent research, for example, and the contract
drafting exercise had material terms specified and had a very

95. 
See Donald B. Rubin, Which Ifs Have Causal Answers, 81 J. AM. STAT.
ASSoC. 961, 961 (1986) (providing a technical mathematical definition of
SUTVA).
96. 
See U.S. NEWS, supra note 84 (ranking the University of Minnesota
Law School at sixteenth in the U.S. News ranking).

190
[109:147

LAWYERING IN THE AGE OF AI1

modest scope. Certainly, further study of AI-assistance on more
sophisticated lawyering tasks is warranted.
Finally, our instructions regarding the time spent on assign-
ments might also create conditions that would not be perfectly
replicated in real world scenarios. Recall that participants were
given a maximum amount of time they could spend on each in-
dividual assignment but were instructed to submit the assign-
ment when they would feel comfortable turning it in to a super-
vising attorney. Participants were provided with a flat rate of
compensation for their completion of the study, thereby creating
an economic incentive to spend as little time as possible on the
given tasks. In the real world, under time-based client billing,
lawyers have an economic incentive to spend as much time as
possible on a task in order to maximize revenue. It maybe, there-
fore, that our findings regarding efficiency will not translate to
real world settings. We believe, however, that there are disci-
plining factors in the real world, including market competition
and client pressure, that limit the amount of time a lawyer can
reasonably expend on a given task, making our study design a
reasonable facsimile of the time pressures faced by a lawyer.

V. IMPLICATIONS

Our results have broad implications for the future of lawyer-
ing. Section A of this Part develops these implications by contex-
tualizing our results within the rapidly accelerating develop-
ment of generative Al technology, both in the legal domain and
more generally. This technological development, Section A sug-
gests, means that our results are likely to significantly under-
state the future potential of Al to impact the work of lawyers.
Given this reality, Section B develops the normative implications
of our results for lawyers, purchasers of legal services, judges,
law schools, and law students. For all of these actors, the bottom
line is that generative Al is likely to substantially impact law-
yering in the near term, meaning that thoughtful preparation
for this eventuality should begin now.

A. IMPLICATIONS FOR THE FUTURE OF LEGAL SERVICES

Our findings show that providing law students with general
purpose and widely available generative Al tools like GPT-4 and
a limited amount of training can substantially improve the effi-
ciency with which they complete certain legal tasks without

2024]
191

MINNESOTA LAW REVIEW

adversely affecting (or even slightly improving) the quality of
that work product. Moreover, they suggest that young lawyers
provided with access to Al to facilitate their work accurately ap-
preciate the benefits of Al for certain tasks, find that access to
Al tends to enhance their work satisfaction when it comes to
such tasks, and generally become more enthusiastic about using
Al to facilitate their work as they gain experience doing so.
Standing alone, these results suggest that generative Al will
almost certainly become a vital tool for many lawyers in the near
future, comparable 
to more familiar legal-tech tools like
Westlaw, Lexis, and e-discovery software. 97 Indeed, this trend
has already begun, with some lawyers and law firms proactively
embracing generative AI.98 For less proactive lawyers and firms,
our results suggest that the embrace of Al will likely be driven
by competitive dynamics, as legal services providers that em-
brace Al can charge lower rates or deliver more, or higher qual-
ity, results than competitors who avoid Al assistance.
The implications of our results become substantially more
striking, however, when they are considered in light of the cur-
rent pace of innovation in Al generally, and legal Al in particu-
lar. This is because our results are likely to substantially under-
state the future potential of Al to aid in the provision of legal
services in at least three different respects.
First, and most importantly, whereas our results focused on
the impact of GPT-4 on the provision of legal services, numerous
more specialized generative Al tools for lawyers are already
widely available, and many more are under development. 99

97. 
See supra Part I (describing the evolution of legal technology tools, in-
cluding searchable online databases like Westlaw and Lexis).
98. 
See, e.g., Kate Beioley & Cristina Criddle, Allen & Overy Introduces AI
Chatbot to Lawyers in Search of Efficiencies, FIN. TIMES (Feb. 14, 2023), https://
www.ft.com/content/baf68476-5b7e-4078-9b3e-ddfce710a6e2 [https://perma.cc/
63WN-VX32] (discussing the introduction of an AI chatbot for contract drafting
at Allen & Overy); Emily Hinkley, Mishcon de Reya Is Hiring an Engineer' to
Explore How Its Lawyers Can Use ChatGPT, LEGAL CHEEK (Feb. 16, 2023),
https://www.legalcheek.com/2023/02/mishcon-de-reya-is-hiring-an-engineer-to
-explore-how-its-lawyers-can-use-chatgpt 
[https://perma.cc/3ZR6-CPLU] 
(not-
ing Mischon de Reya's LinkedIn job ad posting for a "GPT Legal Prompt Engi-
neer" to work with lawyers).
99. For instance, the firm Casetext recently launched a product known as
CoCounsel, which "does document review, deposition preparation, contract
analysis, and timeline creation in minutes." How GenAI Can Enhance Your Le-
gal Work Without Compromising Ethics, THOMSON REUTERS (Apr. 17, 2024),

192
[109:147

LAWYERING IN THE AGE OF AI1

Currently available law-specific tools offer lawyers vastly supe-
rior capabilities than the general-purpose AIs like GPT-4 that
we used in our experiment. These tools improve performance
predominantly by marrying generative AIs like GPT-4 with in-
telligent prompt-engineering and Retrieval Augmented Genera-
tion (RAG), which incorporates legal source material. Intelligent
prompt engineering bakes into legal tech platforms prompting
strategies that are tested and customized to produce useful re-
sults for specific types of legal tasks. 100 RAG, the latter ap-
proach, allows generative AIs to retrieve relevant content from
large legal databases and to use this material to inform its re-
sponses. 101 Combined, these two techniques substantially reduce
hallucinations and improve the quality of AI-generated out-
put.102
A second way in which our results understate the potential
of Al to improve the efficiency of legal services is that our study
participants had limited experience using this technology. In to-
tal, participants in our study received a few hours of online

https://legal.thomsonreuters.com/blog/how-genai-can-enhance-your-legal-work
-without-compromising-ethics [https://perma.cc/58B6-3L4X]. Within months of
CoCounsel's launch, the legal tech giant Thomson Reuters purchased Casetext
for $650 Million. See, e.g., REUTERS, supra note 23.
100. 
For general literature on prompt engineering, see Dils, How to Use
ChatGPT. Advanced Prompt Engineering, WGMI MEDIA (July 20, 2023), https://
wgmimedia.com/how-to-use-chatgpt-advanced-prompt-engineering 
[https://
perma.cc/FXY4-FDU7]. See generally Tyler Cowen & Alexander T. Tabarrok,
How to Learn and Teach Economics with Large Language Models, Including
GPT (George Mason Univ., Working Paper No. 23-18, 2023) (on file with the
Minnesota Law Review) (offering advice on engineering prompts). For prompt-
engineering advice that is specific to the legal setting, see AI Tools for Lawyers,
supra note 88.
101. 
See generally Patrick Lewis et al., Retrieval-Augmented Generation for
Knowledge-Intensive NLP Tasks, 33 ADVANCES NEURAL INFO. PROCESSING SYS.
9459 (2020). For discussion of how tools like Casetext use RAG, see With AI,
You Get What You Give, THOMSON REUTERS (Aug. 2, 2023), https://casetext
.com/blog/prompt-engineering-best-ai-output [https://perma.cc/EE6N-F9E9]
("By connecting GPT-4 to a database of reliable legal sources, we're able to
ground its output in real-world knowledge rather than leaving it to rely only on
its own memory.").
102. 
One interesting and untested question is whether and to what extent
widespread use of legal AIs might result in homogenized work product and a
decrease in the creativity of legal analysis. The graders for our study did not
code for work product similarity among those who completed tasks with the as-
sistance of AI, but anecdotally they did not notice "cookie cutter" work product,
perhaps because participants edited Al output prior to submission.

2024]
193

MINNESOTA LAW REVIEW

training before attempting to use this technology to craft an-
swers to two of the four assignments they completed while par-
ticipating in the study.103 Not surprisingly, participants did not
believe that this training fully equipped them to use generative
Al effectively and efficiently, as illustrated by their survey re-
sults indicating that their ability to use Al improved over the
course of the experiment.10 4 By contrast, as lawyers and law stu-
dents use generative Al in their practice, they will naturally tend
to become more adept at using it effectively and efficiently.105
A third and final reason that our results understate the
transformative potential of Al in legal services is that the capa-
bilities of generative AI-which we measured in the summer of
2023-are continuing to rapidly accelerate. 106 To illustrate,
GPT-4, which OpenAI released in March 2023, is significantly
better at legal analysis than GPT-3.5, the model that open Al
released only several months earlier in late 2022.107 Similarly,
the capabilities of GPT-4 at the time of this writing (January,
2024) are significantly improved relative to the version that was
available to our participants during the experiment in the

103. 
See supra Part II (describing training of study participants).
104. 
See supra Part III (discussing survey results of study participants).
105. 
See AI Tools for Lawyers, supra note 88, at 5 ("The quickest route to
proficiency with LLMs is the same route to Carnegie Hall: practice, practice,
practice.").
106. 
See The Great Acceleration: CIO Perspectives On Generative AI, MIT
TECH. REV. (July 18, 2023), https://www.technologyreview.com/2023/07/18/107
6423/the-great-acceleration-cio-perspectives-on-generative-ai 
[https://perma.cc/
9YHW-VPVZ] (discussing the revolutionary impact of generative AI).
107. 
See, e.g., Katz, Bommarito, Gao, & Arredondo supra note 2, at 7 (pre-
senting results by legal subject area); AI Assistance in Legal Analysis, supra
note 8 (discussing exam performance); GPT-4's Law School Grades, supra note
48 (same). For examples discussing ChatGPT performance, see Lo, supra note
63, at 5-6 (presenting GPT-3.5 results); David A. Wood et al., The ChatGPT
Artificial Intelligence Chatbot: How Well Does It Answer Accounting Assessment
Questions?, 38 ISSUES ACCT. EDUC. 81, 82-83 (2023) (presenting ChatGPT re-
sults as applied to accounting-specific content); Nori, King, McKinney, Carignan
& Horvitz, supra note 56 (discussing GPT-4's abilities to solve medical prob-
lems); Alejandro Lopez-Lira & Yuehua Tang, Can ChatGPT Forecast Stock
Price Movements? Return Predictability and Large Language Models 1 (Feb.
28, 2024) (unpublished manuscript) (on file with the Minnesota Law Review)
(examining ChatGPTs ability to forecast returns for the stock market with
news headlines).

194
[109:147

LAWYERING IN THE AGE OF AI1

Summer of 2023.108 For instance, due to model limitations, our
participants were required to copy and paste blocks of text from
cases or statutes into prompts, and could not use text longer than
two to three pages without receiving error messages. Several
participants informally complained about this limitation and
noted that it slowed them down. With the current model of GPT-
4, however, these limitations would not exist because of the AI's
significantly expanded context window and its Retrieval into
Platform capabilities, which OpenAI introduced in November
2023. LLMs are almost certain to continue to improve in the com-
ing years due to increases in model size and complexity and con-
tinuing innovation in the underlying Al architecture.
Not only do our results suggest that generative Al will pro-
duce significant efficiencies across a broad range of legal ser-
vices, but they also imply that these efficiencies will be distrib-
uted unevenly across practice areas, task types, and lawyer skill
levels. This conclusion follows from two of our bottom-line find-
ings. First, the boost in quality experienced by participants was
higher for participants with a lower baseline skill set than for
those with a higher baseline skill set.109 This result is consistent
both with some of our own prior work in the legal arena, as well
as with a number of high-profile studies examining how access
to Al impacts the quality of work product outside of the legal
arena for workers such as professional writers, customer service
agents, and medical professionals. 110 Given the relative

108. 
Briefly, these improvements include significant increases in the model's
"context window," Retrieval Augmented Generation capabilities that allow us-
ers to upload documents (including cases and statutes), and customizable GPTs
that users can build with natural language and publish for others. See New
Models and Developer Products Announced at DevDay, OPENAI (Nov. 6,
2023), https://openai.com/blog/new-models-and-developer-products-announced
-at-devday [https://perma.cc/T8V4-H4XC].
109. 
See supra Part III.
110. 
See AI Assistance in Legal Analysis, supra note 8 (reporting "significant
variation in how useful AT assistance was to students depending on their base-
line performance," with "worst-performing students benefit[ing] enormously
from AT, with gains of approximately 45 percentile points," while "the best-per-
forming students received worse grades when given access to AT, experiencing
declines of approximately 20 percentile points"). For literature outside of the
legal setting finding uneven quality gains from access to AI based on the base-
line skill of workers, see Noy & Zhang, supra note 70, at 187 (finding that giving
college-educated professionals access to AT improved the performance of less-
skilled workers more than high-skilled workers); Erik Brynjolfsson, Danielle Li

2024]
195

MINNESOTA LAW REVIEW

homogeneity of our participants, however, further study is war-
ranted to determine the extent of Al quality improvement on a
broader range of lawyer skill levels.
Here too, our results are likely to understate the extent to
which access to generative Al will have variable effects for dif-
ferent subsets of lawyers across different practice areas. This is
because participants in our study represented a very narrow and
relatively homogenous subset of the legal profession: current or
just-graduated students at the University of Minnesota Law
School in the summer of 2023. All such students, of course,
gained admission to the law school, meaning that they almost
uniformly performed exceptionally well, both with respect to
their college grades and the LSAT examination. The range of
baseline skillsets possessed by legal professionals in general var-
ies much more dramatically than was the case for our study par-
ticipants. This point is mitigated by the fact that participants in
our study were disproportionately inexperienced relative to av-
erage legal professionals, but only moderately so given that our
focus was on relatively simple legal tasks that would tend to be
assigned to junior attorneys.
Second, we found that Al enhanced the quality of partici-
pants' work product significantly more for some tasks (contract
drafting in particular) than others, where it had limited or no
effect on quality (legal memo and employee handbook). This re-
sult is also consistent with some of our own prior research, which
found that providing humans with Al produced significant gains
in accuracy with respect to simple multiple-choice questions,
limited quality gains for straight-forward legal essays, and no
average gains in quality with respect to student answers to com-
plex and advanced legal essay questions.n
1 
It may also be the

& Lindsey R. Raymond, Generative AI at Work 2-4 (Nat'l Bureau of Econ. Rsch.,
Working Paper No. 31161, 2023) (finding that giving customer service agents
access to AI improved the capabilities of less-skilled agents more than highly-
skilled agents). See also Falling Asleep at the Wheel, supra note 71 (finding that
giving professional recruiters access to high-quality AI harmed humans' ability
to assess job applications relative to giving them access to lower quality AI
tools).
111. 
AI Assistance in Legal Analysis, supra note 8, at 5-6 (finding that AT
produced significant gains in quality when provided to undergraduates answer-
ing basic law school style questions, minimal average gains in quality with re-
spect to undergraduate answers to straight-forward legal essays, and less still
with respect to upper level law students' answers to more complex legal ques-
tions).

196
[109:147

LAWYERING IN THE AGE OF AI1

case, given our participant population, that Al provided the
greatest benefit for those tasks participants were least familiar
with. While this appears a reasonable hypothesis, we are some-
what skeptical that this distinction has large explanatory power,
given that most participants would be unfamiliar with employee
handbook drafting, and likely had some exposure to contract
drafting.
Once again, the uneven average impact of Al on quality
across task types is likely to be understated by our results. That
is because all four of the legal tasks we selected for the study
necessarily shared certain features given our experimental de-
sign: they required a written work product, necessitated little if
any independent research, could be completed in between one
and five hours of time, and were reasonably appropriate for law
students. These constraints, of course, do not apply to the im-
mense range of tasks that real lawyers may need to complete.
The features of some lawyer tasks-such as negotiating complex
deal terms or crafting high-stakes legal briefs-almost certainly
make them less amenable to assistance from Al. Meanwhile,
many other legal tasks are likely to be much more dramatically
impacted by the availability of Al than those that we focused on
in our experimental setting. One important example involves the
simple act of summarizing large and complex documents, such
as deposition transcripts. General purpose AIs are particularly
adept at summarizing complex and dense material, and special-
ized Al tools like CoCounsel use basic prompt engineering strat-
egies to improve the reliability and verifiability of these ef-
forts.11 2 Anecdotal reports from lawyers indicate that these tools
can perform certain summarization tasks that would ordinarily
take a young associate hours in a matter of minutes, while pro-
ducing more reliable output. 113

112. 
See What It Takes to Build an AI Legal Assistant Lawyers Can Rely on,
CASETEXT (May 12, 2023) [hereinafter What It Takes], https://casetext.com/
blog/building-an-ai-legal-assistant-lawyers-can-trust [https://perma.cc/UR8K
-5J78] (discussing prompt engineering and refining CoCounsel's skills).
113. AI Set to Save Professionals 12 Hours Per Week by 2029, TJHoMsON REU-
TERS, https://www.thomsonreuters.com/en/press-releases/2024/july/ai-set-to
-save-professionals -12-hours-per-week-by-2029.html [https://perma.cc/4Q6Y
-NX5C] ("Survey respondents predict AI to free up to 12 hours per week within
the next five years, with four hours per week saved in the next year alone 
the
equivalent of adding an additional colleague for every 10 team members. For a
U.S. lawyer, this could translate to an additional $100,000 in billable hours.").

2024]
197

MINNESOTA LAW REVIEW

Another interesting aspect of our findings is that partici-
pants were not only able to accurately assess how useful GPT-4
was at each task, but also that participants reported increased
satisfaction when completing tasks with access to GPT-4. With
respect to the first finding, this suggests that law firms can be
relatively confident that they can trust their lawyers to know
when Al will or will not be useful to them in completing a task,
rather than having strict controls on Al usage. While the second
finding regarding increased satisfaction may at first glance seem
a relatively minor point, law firms would do well to take note. In
an era where lawyer dissatisfaction and burnout are wide-
spread,114 a tool that has the potential to increase lawyer well-
being, presumably by reducing or eliminating the burden of rel-
atively tedious work, is one that is worth taking seriously.
In sum, when considered in light of current trends in the
development of generative Al as well as prior research, our re-
sults suggest that the practice of law is on the precipice of signif-
icant-and potentially foundational-change 
and transfor-
mation. This change will, however, occur unevenly across legal
domains and practice areas.
Importantly, these predictions concern only the first-order
impacts of generative Al on the legal profession: legal technolo-
gies built on generative Al will become a vital and potentially
transformative tool for a broad range of lawyers. The higher-or-
der impacts of this reality are, of course, much harder to predict.
Will demand for legal services increase or decrease? Will firms
alter the range of legal services that they send to outside counsel
relative to the tasks that they perform in-house? Will lawyer pay
become higher, lower, or more uneven? And what impact will all
of the above have on the demand and supply of lawyers and law
students? Our empirical results offer limited guidance on these
questions, other than to suggest that the assumption that the

114. 
See, e.g., Jacquelyn Palmer & Linda Ouyang, Analysis: Survey Finds
Lawyer Burnout Rising, Well-Being Falling, BLOOMBERG LAW (June 28, 2021),
https://www.bloomberglaw.com/bloomberglawnews/bloomberg-law-analysis/
X15S722S000000?bnanews _filter=bloomberg-law-analysis#jcite [https://
perma.cc/64BX-DQES] (reporting that short-term job satisfaction was down
while rates of burnout were up, particularly among junior and mid-level associ-
ates); Nat'l Task Force on Lawyer Well-Being, The Path to Lawyer Well-Being:
Practical Recommendations for Positive Change, AM. BAR ASS'N 7 (Aug. 2017),
https://www.americanbar.org/content/dam/aba/images/abanews/ThePathTo
LawyerWellBeingReportRevFINAL.pdf [https://perma.cc/F4U8-JEZZ] (report-
ing low rates of well-being among early career lawyers and law students).

198
[109:147

LAWYERING IN THE AGE OF AI1

future will resemble the past is likely tenuous, at best, and that
further study is clearly warranted.

B. 
NORMATIVE IMPLICATIONS

Lawyers, judges, clients, law schools, and law students will
all need to adjust over the coming years as tools that incorporate
generative Al become a reality of legal practice. Of course, both
the pace and the character of this innovations remain deeply un-
certain. But our results provide some helpful context regarding
how individual actors within the legal system can and should
adapt to this transformation in the near term.

1. Lawyers and Law Firms

Our results strongly suggest that lawyers and law firms
should be proactively exploring how best to incorporate genera-
tive Al tools into their practice. Of course, many law firms are
already doing just that. For instance, in March of 2023, the
global law firm DLA Piper announced that it would incorporate
CoCounsel, one of the leading generative Al tools for lawyers,
into its practice. 115 Numerous other large law firms have also
embraced this tool in recent months, though many have been re-
luctant to publicly acknowledge this. 116 Other large global law
firms-including Allen & Overy-have incorporated a competing
generative Al tool, Harvey, into their practice. 117 Still other
firms have taken a different approach, hiring their own Al

115. 
Press Release, DLA Piper to Utilize CoCounsel, The Groundbreaking
AI Legal Assistant Powered by OpenAI Technology (Mar. 15, 2023), https://
www.dlapiper.com/en-us/news/2023/03/dla-piper-to-utilize-cocounsel-the
-groundbreaking-ai-legal-assistant-powered-by-openai-technology [https://
perma.cc/8XDM-BALJ].
116. 
See Press Release, Casetext, Top Global Law Firm DLA Piper An-
nounces Addition of CoCounsel to Enhance Practice and Client Services (Mar.
23, 2023), https://casetext.com/blog/law-firm-dla-piper-announces-casetext
-cocounsel 
[https://perma.cc/YG8B-W2SW] 
(listing other firms that have
adopted CoCounsel).
117. 
Charlotte Johnstone, MacFarlanes Joins List of Firms Adopting Harvey
AI, LAW.COM (Sept. 21, 2023), https://www.law.com/international-edition/2023/
09/21/macfarlanes-joins-list-of-firms-adopting-harvey-ai [https://perma.cc/RH
S6-ETVE1.

2024]
199

MINNESOTA LAW REVIEW

experts to develop proprietary and firm-specific generative AIs
that are not available to competitors. 1 18

Although this trend is already evident in large law firms, at
least some smaller law firms and solo practitioners have also be-
gun exploring how to incorporate generative Al into their work,
with mixed results. The most notorious such example involved a
New York lawyer who relied on ChatGPT to author a brief with-
out double-checking the resulting output. 119 The generative Al
proceeded to hallucinate the existence of several cases, and then
to insist on questioning from the lawyer that these cases were
real. 120 Not surprisingly, the unwitting lawyer was publicly ex-
coriated by the judge in a hearing that was reported on widely
by the media and that drew widespread attention from the
bar.121
Rather than suggesting that small lawyers and law firms
should avoid generative Al tools, the New York case-when con-
sidered in light of our own results and prior research-can and
should serve as a cautionary tale against uncritically using gen-
erative Al to practice law. There are numerous well-known risks
that come along with using generative Al as a tool for legal anal-
ysis, and the lawyers in that case ignored all of them. But small
lawyers and law firms that interpret this incident to suggest the
need to avoid generative Al reach precisely the wrong conclu-
sion. Like any other tool, generative Al can be misused.
The lesson to draw from this case, when considered in con-
cert with the results of this study and prior evidence, is that law-
yers and law firms that use generative Al tools must develop
systems and procedures for doing so effectively. At the very least,
these systems should include (i) confirming the veracity of any
factual statements or characterizations of legal source materials

118. 
See Lance Eliot, Prestigious Symposium on AI Lawyering Reveals Keen
Insights Including the Ardent Debate on Whether to Use Generative AI in Law
School Education, FORBES (Oct. 17, 2023), https://www.forbes.com/sites/lance
eliot/2023/10/17/prestigious-symposium-on-ai-lawyering-reveals-keen-insights
-including-the-ardent-debate-on-whether-to-use-generative-ai-in-law-school
-education [https://perma.cc/D2M6-NSNW].
119. 
See Benjamin Weiser, Here's What Happens when Your Lawyer Uses
ChatGPT, N.Y. TIMES (May 27, 2023), https://www.nytimes.com/2023/05/27/
nyregion/avianca-airline-lawsuit-chatgpt.html [https://perma.cc/F62R-484L].
120. Id.
121. 
See id. ("The discussion now among the bar is how to avoid exactly what
this case describes,' Mr. Gillers said. 'You cannot just take the output and cut
and paste it into your court filings."').

200
[109:147

LAWYERING IN THE AGE OF AI2

made by AIs; (ii) experimenting with different prompting strat-
egies when using general purpose AIs, including few-shot and
grounded prompting; 122 (iii) assessing legal issues and tasks in-
dependently of Al; and (iv) avoiding entering any confidential
information into general purpose AIs that do not include trust-
worthy assurances of confidentiality.123 Al will be more useful in
some practice areas than others, and lawyers should take the
time to become familiar with it to use it most effectively.

2. Legal Clients

The potential for generative Al to significantly improve the
efficiency of legal work should be welcome news to many clients.
But rather than relying on market forces alone to decrease the
cost of legal work product or increase the quality, we believe that
our results suggest that clients should be proactive in asking
their attorneys how they make use of generative Al and what
impact that has on the quality and cost of the resulting legal ser-
vices.
Despite the fiduciary nature of the attorney-client relation-
ship, like all principal-agent relationships, this relationship is
characterized by various potential conflicts of interest.124 Chief
among them, of course, is the incentive of lawyers to spend more
time performing legal work so as to increase the fees that they
can charge. 125 Some lawyers may be inclined to accomplish this
simply be resisting incorporating generative AI into their

122. 
Few-shot prompting involves providing the AI model with examples of
good responses that it can use to shape its response. See Michael Bullwinkle

&

Eric Urban, Prompt Engineering Techniques, MICROSOFT LEARN (Sept. 5, 2024),
https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/advanced
-prompt-engineering?pivots=programming-language-chat-completions 
[https://
perma.cc/2CYC-4VCG] (describing few-shot as providing examples "to give ad-
ditional context to the model"). Grounded prompting involves providing the AT
model with relevant sources. Id. (describing giving a "model data to draw its
responses from" as grounding).
123. 
See AI Tools for Lawyers, supra note 88, at 20-21 (discussing confiden-
tiality issues).
124. 
See Dennis M. O'Dea, The Lawyer-Client Relationship Reconsidered:
Methods for Avoiding Conflicts of Interest, Malpractice Liability, and Disquali-
fication, 48 GEO. WASH. L. REv. 693, 730-32 (1980) (discussing the need for
standards to avoid conflicts and adverse representation).
125. 
See Lisa G. Lerman, A Double Standard for Lawyer Dishonesty: Billing
Fraud Versus Misappropriation, 34 HOFSTRA L. REv. 847, 848-49 (2006) (dis-
cussing lawyer dishonesty regarding finances and unequal disciplinary enforce-
ment).

2024]
201

MINNESOTA LAW REVIEW

workflows, citing some of the risks of this technology described
above. Others may explain to clients that their use of generative
Al has allowed them to invest their scarce time into other ways
of protecting the clients' interests. Of course, how convincing
these answers are will depend on innumerable factors; but many
clients who do not closely monitor how their lawyers' legal work
product and billing practices are impacted by generative Al may
end up paying more for less relative to their competitors.
An alternative approach for legal clients is to shift the bal-
ance of work that is outsourced to law firms rather than being
produced in-house. 126 The efficiencies associated with generative
Al are virtually certain to shift the calculations associated with
this make-buy decision. Most obviously, generative Al should al-
low clients to complete a larger percentage of routine legal work
in-house. Additionally, the uncertainty that generative Al intro-
duces in how long legal work should take also counsels in favor
of moving relatively routine work from external counsel to in-
house, as that shift should allow firms to better calibrate these
expectations internally, where principal-agent problems are re-
duced.
These dynamics may well play out differently in adversarial
settings, like high-stakes litigation. In litigation, both plaintiffs
and defendants can use generative Al tools to increase the effi-
ciency with which they produce relevant work product. As such,
it is not clear that these efficiencies can or will result in an over-
all reduction in the optimal amount of time necessary to litigate
a case, given the expectation that this technology may free up
time for one's opponent to strengthen their case. Similar dynam-
ics apply to fields like transactional contract negotiation, where
Al might simply allow both sides to a deal to dig deeper and cre-
ate ever-more-detailed contracts. In other words, competitive dy-
namics make it harder for clients to calibrate how access to gen-
erative Al should impact their legal bills, particularly with
respect to domains like high-stakes litigation or corporate mer-
gers and acquisitions where outcomes matter much more than
the size of the legal bills.

126. 
See John Armour & Mari Sako, AI-Enabled Business Models in Legal
Services: from Traditional Law Firms to Next-Generation Law Companies, 7 J.
PROS. & ORG. 27, 27 (2020) (evaluating how the adoption of AI in the legal ser-
vices will impact the structure of law firms generally, including the extent to
which clients will choose to develop new forms of expertise internally).

202
[109:147

LAWYERING IN THE AGE OF AI2

3. Judges
In the wake of several recent high-profile stories of lawyers
using ChatGPT to produce legal filings with significant errors, 127

many judges have adopted formal policies regarding the use of
generative Al by lawyers practicing before them. An increasing
number of judges, for instance, require lawyers to disclose
whether they used generative Al to help them write legal fil-
ings. 128 Other judges go further, requiring lawyers to specially
certify the accuracy of any filings for which generative Al has
been used. 129 And several judges have even prohibited lawyers
that practice before them from using any generative Al to assist
them with writing legal filings.130
In our view, our results suggest that such aggressive at-
tempts to limit or complicate lawyers' use of generative Al are
misguided. 131 Generative Al has the capacity to allow lawyers to

127. 
See, e.g., Ella Lee, Michael Cohen Gave Lawyer Fraudulent Case Cita-
tions Generated by AI, THE HILL (Dec. 29, 2023), https://thehill.com/regulation/
court-battles/4381736-michael-cohen-gave-lawyer-fraudulent-case-citations
-generated-by-ai [https://perma.cc/95UW-ET66] (revealing in court documents
that Michael Cohen had given his attorney fake legal cases); Larry Neumeister,
Lawyers Submitted Bogus Case Law Created by ChatGPT. A Judge Fined Them
$5,000, ASSOCIATED PRESS (July 22, 2023), https://apnews.com/article/artificial
-intelligence-chatgpt-fake-case-lawyers-d6ae9fa79d0542db9e1455397aef381c
[https://perma.cc/8CUH-R2P9] (reporting a federal judge fining two lawyers for
fictitious legal research).
128. 
See Odia Kagan, Federal Judges Start Cracking Down on the Use of
Artificial Intelligence in Court Filings, Fox ROTHSCHILD (Dec. 11, 2023), https://
dataprivacy.foxrothschild.com/2023/12/articles/artificial-intelligence/federal
-judges-start-cracking-down-on-the-use-of-artificial-intelligence-in-court
-filings [https://perma.cc/MZ7M-WSD4] 
(discussing proposed and existing AI
disclosure rules in federal courts).
129. 
See Shweta Watwe, Judges Reflect on GenAI Use One Year After
ChatGPT's Debut, BLOOMBERG LAW (Nov. 28, 2023), https://news.bloomberg
law.com/litigation/judges-reflect-on-genai-use-one-year-after-chatgpts-debut
[https://perma.cc/L34B-NFYR] (highlighting additional certifications required
by some judges when AT is used).
130. 
See Megan Cerullo, Texas Judge Bans Filings Solely Created by AI After
ChatGPTMade up Cases, CBS NEWS (June 2, 2023), https://www.cbsnews.com
/news/texas-judge-bans-chatgpt-court-filing [https://perma.cc/YEJ4-QEWB]
(describing a Texas judge's rules on AT usage).
131. 
It is certainly possible that the development of generative AI will im-
pact judges' own drafting of their judicial opinions as well. See Richard M. Re,
Artificial Authorship and Judicial Opinions, 92 GEO. WASH. L. REV. (forthcom-
ing 2024) (manuscript at 11) (on file with the Minnesota Law Review) (specu-
lating that generative AI may significantly impact the quantity and quality of
judicial opinions).

2024]
203

MINNESOTA LAW REVIEW

better serve their clients by producing work product more effi-
ciently, thus reducing barriers to justice. 132 Imposing special re-
strictions on lawyers' use of this technology not only tends to
counteract this salutary effect, but also to stigmatize the use of
generative Al more generally. While lawyers can of course use
this technology irresponsibly to produce fabricated citations or
source material, the possibility of such malpractice is hardly lim-
ited to generative Al. To the contrary, new technologies ranging
from e-discovery platforms to searchable legal databases create
their own distinct risks of malpractice. These risks, as well as
virtually all other risks of attorney misconduct, have historically
been regulated by general rules of professional conduct that are
not tied to specific legal technologies or subject areas. 133 Just as
these general rules of professional responsibility have been flex-
ible enough to deter and penalize past misuses of legal technol-
ogy, so too are they flexible enough to deter and penalize the in-
appropriate use of generative Al by lawyers today.134

4. Law Schools and Law Students

Given the potential of generative Al to impact the practice
of law, it is no wonder that law schools across the country are
grappling with how to incorporate Al into their curricula. 135

132. 
See Roberts, supra note 1, at 6 ("Rule 1 of the Federal Rules of Civil
Procedure directs the parties and the courts to seek the 'just, speedy, and inex-
pensive' resolution of cases [and many] AI applications indisputably assist the
judicial system in advancing those goals." (quoting FED. R. CIV. P. 1)).
133. 
See generally Jon J. Lee, A New Approach to Attorney Regulation, 65
B. C. L. REV. 1625 (2024) (noting that rules governing attorney misconduct have
historically been general in nature).
134. Indeed, the infamous New York lawyer who used ChatGPT to produce
fabricated citations was sanctioned under Rule 11 by the presiding judge. See
Sara Merken, New York Lawyers Sanctioned for Using Fake ChatGPT Cases in
Legal Brief, REUTERS (June 26, 2023), https://www.reuters.com/legal/new-york
-lawyers-sanctioned-using-fake-chatgpt-cases-legal-brief-2023-06-22 [https://
perma.cc/T588-53Q3] (describing the sanctions a lawyer received for using
ChatGPT to draft a legal brief).
135. 
See, e.g., Joseph Landau & Ron Lazebnik, Law Schools Must Embrace
AI, NAT'L L. J. (July 10, 2023), https://www.law.com/nationallawjournal/2023/
07/10/needs-edit-law-schools-must-embrace-ai [https://perma.cc/X4BU-YNAC];
Kristen Baginski & Celeste Pometto DiNicola, AI Goes to Law School, LEX-
ISNEXIS (Dec. 12, 2023), https://www.lexisnexis.com/community/insights/legal/
b/thought-leadership/posts/ai-goes-to-law-school [https://perma.cc/C2F7-Q8RG]
("Law students will soon be actual lawyers so there will be an expectation that
those students can use relevant legal AT tools to be efficient and effective

204
[109:147

LAWYERING IN THE AGE OF AI2

Historically, shifts in legal technology have only had a limited
effect on legal training, which is particularly true when it comes
to first-year law students, who have long studied the same man-
datory curriculum, which is typically taught to them through
some form of Socratic instruction. 136 Although recent decades
have seen important adaptations to this approach-from more
inclusive Socratic questioning, 137 to an increased focus on statu-
tory interpretation, 1 38 to increased opportunities for formative
feedback1s 9-none 
of these changes have fundamentally altered
the character of legal education, particularly in the first-year of
law school.
In our view, this consistency in basic legal pedagogy
properly reflects a consistency in the basic features of effective
legal reasoning.140 Not even technological change as significant
as generative Al is likely to alter this reality any time soon. To
the contrary, effectively using Al to craft legal arguments re-
quires many of the same basic legal and analytical skills as other
forms of lawyering, including a capacity to question initial

practitioners. This means teaching students how to use AI to support critical
thinking and evaluation, collaboration and communication, assessment and
feedback.").
136. 
See L. Danielle Tully, What Law Schools Should Leave Behind,
2022 UTAH L. REV. 837, 837 (2022) (lamenting the lack of change in legal edu-
cation in recent decades notwithstanding common calls for fundamental re-
form); Rachel Gurvich, L. Danielle Tully, Laura A. Webb, Alexa Z. Chew, Jane
E. Cross & Joy Kanwar, Reimagining Langdell's Legacy: Puncturing the Equi-
librium in Law School Pedagogy, 101 N. C. L. REV. F. 118, 118 (2022) ("For more
than 150 years, legal education has largelyfollowed the course charted by Chris-
topher Columbus Langdell when he became dean of Harvard Law School in
1870.").
137. 
Jamie R. Abrams, Legal Education's Curricular Tipping Point Toward
Inclusive Socratic Teaching, 49 HOFSTRA L. REV. 897, 898 (2021) (advocating
for an inclusive form of Socratic instruction that is "student-centered, skills-
centered, client-centered, and community-centered").
138. 
See generally Abbe R. Gluck, The Ripple Effect of "Leg-Reg" on the Study
of Legislation & Administrative Law in the Law School Curriculum, 65 J. LEGAL
EDUC. 121 (2015) (exploring how the increasingly common practice of Legisla-
tion and Regulation during law students' 1L year impacts the upper-level law
school curriculum).
139. 
See generally Daniel Schwarcz & Dion Farganis, The Impact of Individ-
ualized Feedback on Law Student Performance, 67 J. LEGAL EDUC. 139 (2017)
(reporting that providing formative feedback to first-year law students on mid-
term exams improved students' performance in their other first-year classes).
140. 
See, e.g., Cass R. Sunstein, On Analogical Reasoning, 106 HARV. L. REV.
741, 742 (1993) (exploring the distinctive nature of legal reasoning).

2024]
205

MINNESOTA LAW REVIEW

answers, confirm the accuracy of arguments and sources, organ-
ize issues clearly, and assess the strength of alternative argu-
ments. 14 1

For these reasons, law schools should consider substantially
limiting the use of generative Al in certain law school classes,
particularly classic first-year classes like Contracts and Torts.
Because generative Al does not impact the nature of legal rea-
soning, it need not alter the way that such reasoning is taught
by instructors or demonstrated by students, particularly intro-
ductory law students. 142 In many ways, this pedagogical ap-
proach should be familiar: for instance, introductory math stu-
dents are universally taught to add, subtract, multiply and
divide without the aid of calculators, as mastering these basic
skills is essential for most forms of higher math.143
However, our results suggest that accomplishing this goal
requires law schools to proactively limit access to generative Al
during student assessments. That is because they demonstrate
that generative Al can not only empower law students to craft
legal work product significantly more quickly (a skill that is typ-
ically rewarded on timed law school exams), but also that it can
disproportionately improve the quality of that work product for
less-skilled students. Our prior work has demonstrated that this
is true not only for the practical legal tasks that we focused on
in this experiment, but also for a range of different types of law
school exams.144 Thus there is a risk that students will use Al as
a crutch rather than developing crucial lawyering skills early in
their careers. In addition, Al assistance will tend to compress the
distribution of grades in traditional law school exams and make
it more difficult for professors to provide individualized feed-
back.
Given current technology, law professors who intend to limit
access to Al must place hard technological limits or employ ag-
gressive proctoring. 145 Relying instead on honor codes is simply

141. 
See AI Tools for Lawyers, supra note 88, at 4.
142. 
See id.
143. 
See Erin McCauliff, The Calculator in the Elementary Classroom: Mak-
ing a Useful Tool out of an Ineffective Crutch, CONCEPT, Apr. 4, 2004, at 1, 2.
144. 
See A Assistance in Legal Analysis, supra note 8, at 5.
145. 
See Julianne Hill, Profs Trade Notes as Law Schools Write Generative
AI Policies, ABA J. (Jan. 2, 2024), https://www.abajournal.com/web/article/law
-profs-trade-notes-as-law-school-write-generative-ai-policies [https://perma.cc/

206
[109:147

LAWYERING IN THE AGE OF AI2

impractical given the current power of widely accessible genera-
tive Al tools. 146 This is especially so because there are currently
no reliable tools available for identifying content produced by
generative Al, meaning that law schools and professors cannot
reliably detect cheating. 147 All of this means that cheating
among a non-trivial number of students is inevitable when in-
structors rely only on an honor code to prevent student use of
generative Al. Over time, we fear that such cheating among a
handful of students would spread as students who were initially
inclined to follow the rules begin to feel like "suckers" for doing
so, and thus eventually deciding to cheat themselves. 14 8

While law schools might restrict student access to genera-
tive Al tools in some classes, we believe that law schools should
simultaneously develop upper-level classes that explicitly train
students on how to use generative AI tools effectively. This con-
clusion is buttressed by our survey results indicating that par-
ticipants reported that their ability to use AT effectively in-
creased markedly over the course of the experiment, that
participating in the experiment increased their interest in using
AT in their future work, and that using this tool also increased
their personal satisfaction.149 It is also supported by the differ-
ential impact of AI on quality across the different task types;
whereas students interested in some practice areas may rightly
believe that it would not be a good use of their law school credits
to take a class that focuses significant attention on using gener-
ative AT, other students may rightly reach the opposite conclu-
sion depending on their career aspirations and interests.

2JHV-N5WP] (describing different law schools' efforts to revise their academic
integrity codes in response to generative artificial intelligence).
146. 
Id. (discussing the increasing availability of generative AI tools).
147. 
See, e.g., Zhengyuan Jiang, Jinghuai Zhang & Neil Zhenqiang Gong,
Evading Watermark Based Detection of AI-Generated Content (Nov. 21, 2023)
(unpublished manuscript) (on file with the Minnesota Law Review) (discussing
the difficulty of detecting AI-generated text even if sophisticated technological
techniques for "watermarking" such text is attempted).
148. 
See Daniel Houser, Stefan Vetter & Joachim Winter, Fairness and
Cheating, 56 EUROPEAN ECON. REV. 1645, 1645 (2012) (reporting the results of
an experiment suggesting that "individuals who believe they were treated un-
fairly in an interaction with another person are more likely to cheat in a subse-
quent unrelated game"); Scott S. Wiltermuth, Cheating More when the Spoils
Are Split, 115 ORGANIZATIONAL BEHAV. & HUM. DECISION PROCESSES 157, 157
(2011) ("We cheat because we think others are cheating .... ").
149. 
See supra Part III (describing survey results of participants).

2024]
207

MINNESOTA LAW REVIEW

The quantity and scope of these classes should of course vary
by school and context, though law schools with students who are
more interested in or likely to provide legal services to individu-
als or cost-sensitive clients should be particularly aggressive in
developing these course offerings. So too should law schools that
focus on producing "practice-ready" attorneys who are less likely
to receive extensive on-the-job training early in their career.1 50

Although the supply of instructors who are comfortable teaching
classes on how to use generative Al in the law may be limited at
first, we suspect that this pool of potential instructors will grow
as does the use of generative Al in practice. Moreover, a virtue
of generative Al tools is that those with significant legal exper-
tise may be better positioned than they initially believe to learn
how to use these tools effectively along with their students. 151

CONCLUSION

We conducted the first randomized controlled trial to evalu-
ate LLM assistance with basic lawyering tasks. We found small
and variable improvements to the quality of work product but
large and consistent improvements to speed. Moreover, we found
that when Al provides a boost to quality at all, the boost to qual-
ity (but not speed) inversely correlates with baseline perfor-
mance, with a substantial improvement for the worst performers
but no improvement for the best. Finally, we found that partici-
pants accurately perceived how useful Al assistance was on each
task and reported positive impressions from using Al at legal
tasks. These findings suggest that Al could substantially trans-
form the legal profession, streamlining tasks, improving lawyer
satisfaction, and improving the performance of lower-skilled at-
torneys.

150. 
See Jason G. Dykstra, Beyond the "Practice Ready" Buzz: Sifting
Through the Disruption of the Legal Industry to Divine the Skills Needed by New
Attorneys, 11 DREXEL L. REV. 149, 214 (2018) ("[S]tudents must emerge from
law school both ready for practice and prepared to immediately generate reve-
nue, whether they ply their practice-ready skills as contract attorneys, associ-
ates, in-house counsel, or solo practitioners.").
151. 
See AI Tools for Lawyers, supra note 88, at 4 (arguing that many of the
tools traditionally required to be an effective lawyer are also useful in effectively
using AI to help produce legal work product).

208
[109:147

LAWYERING IN THE AGE OF AI2

APPENDIX

A. TRAINING MATERIALS
Prior to completing the four required tasks, participants
completed an online training module that we developed and
taught on how to use GPT-4 effectively in legal analysis.152 This
training involved watching three pre-recorded videos, totaling
approximately two hours in length, and completing several short
exercises requiring the use of GPT-4 to answer simple legal ques-
tions. 153 Training was split into three sub-areas. The first cov-
ered general principles on using Al effectively in legal research
and writing. 154 Among other things, it provided participants
with an overview of basic prompting techniques that prior re-
search had shown to be effective in legal analysis, such as sup-
plying the Al with relevant legal rules or source materials within
prompts. 155 Second, the training covered basic techniques for

152. This training drew heavily on previous work by two of us. See generally
AI Tools for Lawyers, supra note 88.
153. Most people can access GPT-4 by creating a paid ChatGPT Plus account
on the OpenA website. However, it was not administratively possible to create
such an account for each study participant without requiring participants to
outlay cash on the subscriptions themselves. We instead created a central
ChatGPT "clone" website using the GPT-4 API and gave students access to that
website. This clone website had a nearly identical user interface and used the
same system prompt as the real ChatGPT Plus.
154. 
These general principles included the following key pieces of advice: (i)
think about any legal problem first-develop your own basic instincts about key
issues, principles, and parameters of work product you will need to produce;
(ii) start prompts by giving Al context that it should use to approach a question
(i.e., "You are an experienced litigator."); (iii) use Al to refine an initial assess-
ment of a project by asking it to produce an outline, identify key issues, or pro-
duce a first draft (in the case of shorter assignments); (iv) chunk up the elements
of an outline, the issues, and application of rules into bite-sized bits, and ask Al
to analyze each bit, adjusting the level of generality based on the problem and
quality of answers; (v) provide Al with all the key details that a person would
need to accomplish the prior step; (vi) iterate by providing additional details
that you may have left out, such as by asking Al to alter elements that do not
look good, or asking Al to elaborate on elements that do look promising; (vii) pro-
vide Al with relevant source materials, including cases, statutes, contract pa-
rameters, etc.; and (viii) do not rely on Al to conduct specific legal research
or identify specific legal source material unless you confirm the veracity of that
material.
155. 
See AI Assistance in Legal Analysis, supra note 8, at 22 (discussing
prompting strategies for Al usage). For a review of the computer science litera-
ture on these prompting strategies, see for example Prompt Engineering,

2024]
209

MINNESOTA LAW REVIEW

using Al effectively in litigation-oriented settings, covering top-
ics such as using Al to summarize and apply primary sources
like caselaw and statutes.156 The third and final portion of the
training focused on using Al to draft transaction-oriented work
product, such as contracts, highlighting AI's capacity to mimic
the format, style, and structure of sample transactional materi-
als and to help identify alternative terms, unanticipated risks,
and ambiguities in initial drafts.1 57

B. ASSIGNMENTS

We selected the four assignments that we gave to partici-
pants to be representative of the types of tasks that junior law-
yers perform. These assignments were as follows:

OPENAI PLATFORM, https://platform.openai.com/docs/guides/prompt
-engineering [https://perma.cc/J2MV-MJ7D] (explaining OpenA's recom-
mended prompting strategies); Alan D. Thompson, Microsoft Bing Chat (Syd-
ney/GPT-4), LIFE ARCHITECT (Feb. 22, 2023), https://lifearchitect.ai/bing-chat
[https://perma.cc/H4NR-ATD8] (describing Microsoft Bing's implementation of
OpenA and its prompts); Cowen, supra note 100 (providing tips and guidance
for the usage of AI in economics problems). See generally What It Takes, supra
note 112 (detailing the work done behind the scenes in the creation of an AT
legal assistant); Jason Wei et al., Chain-of-Thought Prompting Elicits Reason-
ing in Large Language Models, 35 ADVANCES NEURAL INFO. PROCESSING SYS.
24824 (2022) (discussing the usage of chain of thought models in AT learning);
Tom B. Brown et al., Language Models Are Few-Shot Learners, 33 ADVANCES
NEURAL INFO. PROCESSING SYS. 1877 (2020) (testing Al models in few-shot set-
tings); Baolin Peng et al., Check Your Facts and Try Again: Improving Large
Language Models with External Knowledge and Automated Feedback (Mar. 8,
2023) (unpublished manuscript) (on file with the Minnesota Law Review) (ex-
ploring strategies to reduce Al hallucinations and generate better results).
156. This training suggested that participants: (i) independently review
source material briefly; (ii) ask GPT-4 to summarize specific cases and statutes
by copying and pasting that material into GPT-4 (and breaking it up into chunks
if it is too long; (iii) ask GPT-4 any relevant follow-up questions focusing in on
elements of reasoning, issues, or facts that are most relevant; (iv) ask GPT-4 to
quote from the relevant source material in any of its explanations so you can
verify it; and (v) use GPT-4 to analogize or distinguish cases to specific fact pat-
tern/scenario, highlighting key issues.
157. 
More specifically, this portion of the training emphasized that Al can
help: (i) mimic the format/style/structure of any sample transactional material;
(ii) incorporate specific deal terms or parameters into transactional documents
if the terms are provided; (iii) identify potential risks to address and ambiguities
in deal terms; (iv) help issue-spot potential additional terms to add to an agree-
ment; and (v) help further develop/specify terms, or identify alternative ways of
drafting that can favor one particular side in the transaction.

210
[109:147

LAWYERING IN THE AGE OF AI2

(1) Legal Memo Assignment

Chris Smith was known in his community as an uncannily
talented grill master, in part because of his excellent homemade
barbeque sauce, a family recipe. After years of friends suggesting
that he make money on his family recipe, Smith decided to mar-
ket it commercially.
Smith contracted with ABC Food Company to design a hot
and spicy version of his sauce for commercial sales. ABC will also
manufacture, market and distribute the sauce. Fran Jones, a de-
veloper at ABC, was put in charge of the project. Jones wants to
design the sauce using serrano peppers for added spiciness, as
she believes the serrano is perfect for making Smith's recipe spic-
ier without taking away from the original flavor. However, Jones
is concerned about using serrano peppers because she knows,
from personal experience, that some people are allergic to it.
Jones has seen each of two friends break into rashes upon eating
the peppers. In addition, a study commissioned by the American
Hyper Allergy Association of America! (AHAAA!) has projected
that up to 1% of Americans may have a propensity for allergic
reaction to the pepper. This reaction will likely take the form of
a rash in most of the pepper-sensitive population, but the reac-
tion could involve an acute and therefore potentially life-threat-
ening increase in blood pressure in a subset of that population.
As a first-year associate lawyer for ABC, it falls to you to
determine the legal implications of using the serrano pepper in
Smith's barbeque sauce. There are a number of common law and
statutory issues presented. ABC is aware that both federal food
and drug law, and statutory enactments in various states includ-
ing ABC's home state of Ohio, may preempt or at least supple-
ment common law. But you have been asked for now to examine
only the question whether a warning is required to avoid strict
liability under Restatement (Third) of Torts: Products Liability
§ 2, cmt. k, and Restatement (Second) of Torts § 402A, cmts. h, i,
and especially j.
One of your colleagues, a third-year associate, has already
done extensive research into the case law on this matter (the four
most illustrative cases she found are included below). ABC for
now does not want additional research. Your assignment is to
review the four cases your colleague has already found, and then
to write an objective, predictive memo for ABC on the specific
topic of whether ABC needs to put a warning on the barbeque

2024]
211

MINNESOTA LAW REVIEW

sauce label if it wants to include serrano peppers as an ingredi-
ent in the Smith sauces, and also wants to avoid a risk of strict
liability for failure to warn.
ABC and Smith are located in Ohio, and any initial distri-
bution of Smith's sauce will likely take place in Ohio for test-
marketing purposes.

Relevant cases
Crislip v. TCH Liquidating Co., 52 Ohio St. 3d 251 (1990)
Mills v. Giant of Maryland, LLC, 508 F.3d 11 (D.C. Cir. 2007)
Livingston v. Marie Callender's, Inc., 72 Cal. App. 4th 830 (Cal.
Ct. App. 1999)
Adelman-Tremblay v. Jewel Companies, Inc., 859 F.2d 517 (7th
Cir. 1988)

(2) Contract Drafting Assignment
Jill Jackson wants to employ Mary Monte to paint four
rooms (living room, dining room, kitchen, and downstairs bath-
room) in her home. She is willing to pay for all materials, includ-
ing paint, brushes, etc. immediately upon presentation of re-
ceipts and pay $3,000 total when the job is completed. She
anticipates that the job will not require any primer, but that all
surfaces will need two coats. The color of all trim will be Sherwin
Williams "bright white" and the color of all walls will be Sherwin
Williams "shadow gray." Jill wants the work done no later than
6 weeks from the date of the contract, because only a week later
she will be hosting her son's graduation party. She is willing to
pay 20% of the $3,000 upon execution, and the remainder when
the work is done to her satisfaction. Please draft a contract fa-
vorable to the homeowner, which is in plain English. Both par-
ties are located in the state of Minnesota. The contract should be
no more than two pages single-spaced (12-point type, 1" mar-
gins).

(3) Employee Handbook Assignment

Sergio and Stella are software developers based in Minne-
apolis, MN. They started Code Castle LLC two years ago and
have run it themselves since then. Now, with more work than
they can handle, Sergio and Stella have hired three employees
and expect to hire more next year. Starting next week, Maria
and Mo will join them as full-time developers and Mattias will

212
[109:147

LAWYERING IN THE AGE OF AI2

be the office manager. Code Castle purchased an "off-the-shelf'
employee handbook that they've been using, but they have real-
ized it is missing some information they believe is important to
cover. They have hired your firm to help them revise the hand-
book to include various topics not included in the basic handbook
they purchased.
One topic they would like added to the handbook is employee
breastfeeding accommodations. This particular topic arose be-
cause Maria has a 3-month-old baby and Sergio and Stella want
to be sure they understand what they need to do to accommodate
Maria pumping breastmilk while at work.
Your supervising attorney has asked you to draft a section
to add to the employee handbook that explains an employee's
rights under applicable law to pump breastmilk while at work.
Please research relevant state and federal law and provide a
draft of the requested section. Please make sure the section is no
longer than one page.

(4) Complaint Drafting Assignment

Unlike the first three assignments, elements of the com-
plaint-drafting assignment are occasionally re-used by the in-
structor who designed it. As such, that instructor has requested
that we not publicly disseminate the full content of the assign-
ment. In brief, however, this assignment requires students to
draft a legal complaint for a federal court based on a two-page
memo from a client describing how his restaurant and bar expe-
rienced unfair treatment by the local police and other authori-
ties. The memo includes numerous details, some of which are
quite relevant to establishing a potential civil cause of action,
and others of which are either less relevant or completely irrele-
vant. The memo also specifies four particular legal theories that
the complaint could assert and provides students with the un-
derlying elements of these causes of action. It does not contain
any details regarding the appropriate form or content of a com-
plaint under the Federal Rules of Civil Procedure.

C. GRAPHS OF DIFFERENCES IN MEANS

The following Figures show the distribution of differences in
mean grade on each task, as well as the differences in the time
taken for each task, between the group with and without access

2024]
213

214 
MINNESOTA LAW REVIEW 
[109:147

to GPT. The distributions were generated by calculating means
on bootstrapped distributions, with 10,000 iterations.

Figure 18: Difference in Grade with Access to AI-
Complaint Drafting

5 
(5 
Confidenc Interval

3.0

2.5

2.0

LO

0.5

0.0 
0.2
Grade Difference
0.4 
0.6
--0.2

LAWYERING IN THE AGE OF AI2

Figure 19: Difference in Grade with Access to AI-
Contract Drafting

-0.1 
0.0 
0.1 
0.2 
0.3
Grade Difference

With GPT
Mean
95% Confidence Interval

0.4 
0.5 
0.6

Figure 20: Difference in Grade with Access to AI-
Employee Handbook

5 
.95% Confidence Interval

4

3

2-

0
UJ.U 
U1~)
Grade Difference

4

3

2

02

2024]
215

-0.2
0.2 
0.3

MINNESOTA LAW REVIEW
[109:147

Figure 21: Difference in Grade with Access to AI-
Client Memo

-o.f 
-o.» 
U.
Grade Difference

With GPT
Mean
95% Confidence Interval

0.2 
0.4

Figure 22: Difference in Time Taken with Access to
AI-Complaint Drafting

2With GPiT time diff
0.030 
Mean
95% Confidence Interval

0.025

/

0.020

0.015

0.010

0.000-100
-bU 
-4U 
-zU
Time Difference (Minutes)
0 
20

216

3.0

2.5

2.0

Q 1.5

1.0

0.5

0.0

2024] 
LAWYERING IN THE AGE OF AI 
217

Figure 23: Difference in Time Taken with Access to
AI-Contract Drafting

Wij 
G;PT time diff
Mean
95% Confidence Interval

-ou 
-0u 
-Iu
Time Difference (Minutes)

Figure 24: Difference in Time Taken with Access to
AI-Employee Handbook

Widh GlPT uime~diff
\lean
975 Confidence Interval

-15.0 
-12.5 
-10.0 
-7.5 
-5.0 
-2.5
Time Difference (Minutes)
0.0

0.07

0.06

0.05

>,0.04

0.03

0.02

0.01

0.00

0.17

0.150

0.125

' 0.100

0.075

0.050

0.025

0.000

-40
0

218 
MINNESOTA LAW REVIEW 
[109:147

Figure 25: Difference in Time Taken with Access to
AI-Client Memo

W,ith GP'T timcx 
diff
Mean-
0.030 
95% Confidence Interval

0.025

0.020

0.015

0.010

0.005

0.000
20