---
title: 'Hytera v Motorola'
tags:
  - 'copyright-infringement'
  - 'originality-test'
  - 'aggregate-copying'
  - 'software-expression'
summary: 'The case clarifies that copyright infringement in evolving software requires showing substantial copying of original expression, not just functional elements, and that the totality of copied material must be considered for each work.'
figures:
  - 'Hytera v Motorola'
cases:
  - 'Hytera v Motorola Solutions Inc [2017] FCAFC 168; (2024) 308 FCR 68'
statutes:
  - 'Corporations Act 2001 (Cth)'
  - 'Copyright Act 1968 (Cth)'
jurisdiction: 'Australia'
assessment_relevance: 'This note helps students grasp key copyright infringement tests in software cases, useful for exam essays on substantiality and originality.'
---
[[Copyright Law/03-sources/cases/Hytera Communications Corporation Ltd v Motorola Solutions Inc 308 FCR 68]]

**Citation**: [2024] FCAFC 168; (2024) 308 FCR 68

### Facts
Motorola Solutions Inc (Motorola) developed source code for digital mobile radios (DMRs) as part of its "Matrix" project, commencing in 2003. Hytera Communications Corporation Ltd (Hytera) was developing competing DMR devices but by late 2007 its project was in disarray. Hytera recruited Mr GS Kok, a senior Motorola employee on the Matrix project, who in turn recruited 12 further engineers from Motorola. At trial, Hytera admitted that ex-Motorola engineers brought Motorola documents and computer code to Hytera without authorisation and used them to develop Hytera's firmware. The primary judge characterised Hytera's actions as "substantial industrial theft" and "industrial scale harvesting" of Motorola's source code. Motorola commenced Australian proceedings (2017) alleging patent infringement; it added copyright infringement claims (2018) after discovering Hytera's source code during the patent proceeding. Motorola alleged Hytera infringed copyright in its DMR source code by importing and making available devices containing firmware that reproduced or adapted a substantial part of that code.

### Issue
(1) Whether, for a work that builds on earlier versions of itself, the copyright owner must show that the copied parts were "original" in the sense of not having been copied from earlier iterations developed by the author.
(2) Whether the primary judge erred by considering whether *small segments* of copied code, in isolation, formed a substantial part of the Motorola Works, rather than whether the *totality* of copied code for each work was substantial.
(3) Whether the primary judge erred by applying two separate tests (materiality and originality) and by focusing exclusively on the *functional significance* of copied code to the operation of the DMR, rather than on the *originality* of the expression.

### Held
(1) No. It is not necessary for the copyright owner to show that the copied parts were original in the sense of not having been copied from earlier iterations of the work.
(2) Yes. The question is whether, for each Motorola Work, the *totality* of Motorola source code copied by Hytera was a substantial part of that work.
(3) Yes. There is only one statutory question (substantial part). Substantiality is determined by reference to the *originality* of the code—the creative and intellectual contribution to its form of expression (including structure, choice and sequencing of commands)—not by whether the code is functionally material to device operation.

Hytera's appeal was dismissed. Motorola's cross-appeal was allowed in part (grounds 2 and 3), but a further hearing was required to determine copyright infringement applying the correct methodology.

### Reasoning
- **Originality of copied parts**: The Full Court applied *SW Hart*, *Autodesk (No 2)*, *Data Access* and *IceTV*. For works that evolve over time (e.g. software with successive releases), it is the work as a whole that must be original; the copyright owner need not trace the originality of each copied segment to exclude material derived from the author's own earlier iterations.
- **Totality of copied code**: The primary judge assessed whether individual segments of Hytera code—each copied from a Motorola Work—formed a substantial part of that work. The correct approach is to consider whether, for each Motorola Work, *all* of the Motorola source code that Hytera copied (considered collectively) constituted a substantial part.
- **Substantial part—quality, not functionality**: The primary judge treated "materiality" (functional significance to DMR operation) and "originality" as two separate requirements. Drawing on *Data Access* and Mason CJ in *Autodesk (No 2)*, the Court held that for functional works such as computer programs, "essential" or "material" means essential to the *work as an original expression*, not essential to the *operation* of the device. Substantial part is assessed by the originality of what is taken—the creative and intellectual contribution to the form of expression, including structure and the choice and sequencing of commands.

### Significance
*Hytera v Motorola* clarifies several aspects of copyright infringement in computer software under Australian law:

1. **Iterative works**: Copyright owners need not prove that each copied portion is original vis-à-vis the author's own earlier versions of the work.
2. **Aggregation of copying**: When multiple segments are copied from a work, substantiality is assessed by reference to the *totality* of what was taken from that work, not each segment in isolation.
3. **Substantial part in software**: For computer programs, the substantial part inquiry focuses on the *originality of the expression*—creative and intellectual contribution to form—not on whether the code is functionally critical to the device. This rejects a "but for" or operational-essentiality test.

The case arose in the context of large-scale unauthorised use of source code by former employees and reinforces that copyright protects the form of expression of software, not merely its functional outcomes.

---
