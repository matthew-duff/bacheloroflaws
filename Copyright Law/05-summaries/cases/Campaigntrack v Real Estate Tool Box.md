[[Copyright Law/03-sources/cases/Campaigntrack Pty Ltd v Real Estate Tool Box Pty Ltd [2021] FCA 809]]

**Citation**: [2021] FCA 809

**Campaigntrack Pty Ltd v Real Estate Tool Box Pty Ltd** [2021] FCA 809

## Facts

- Campaigntrack purchased the intellectual property rights to "DreamDesk," a cloud-based real estate marketing software, from Dream Desk Pty Ltd (DDPL) to shut it down and transition its clients to Campaigntrack's platform.
    
- The original developer of DreamDesk, an independent contractor named Mr. David Semmens, subsequently created a competing system called "Real Estate Tool Box" (Toolbox) for a former DreamDesk client, Biggin & Scott.
    
- During the rapid two-month development of Toolbox, Mr. Semmens utilized Git repositories and database migration scripts to transition data from DreamDesk to Toolbox.
    
- Campaigntrack discovered identical source code, Database Works, and Table Works within the new Toolbox system.

- Upon being investigated, Mr. Semmens deliberately deleted Git commits, overwrote computers, and deleted emails to hide his development history.
    
- Biggin & Scott and its executives had explicitly instructed Mr. Semmens to build the new system without breaching any third-party intellectual property.
    

## Procedural History

Campaigntrack initiated proceedings in the Federal Court of Australia as the court of first instance. The applicant alleged primary copyright infringement and breach of confidence against the developer (Mr. Semmens) and secondary infringement (authorisation), alongside breach of contract and undertakings, against the software's new clients and former owners (Biggin & Scott, RETB, DDPL, and associated directors). This judgment determined liability separately from quantum.

## Issue

Whether the developer infringed Campaigntrack’s copyright by reproducing a substantial part of the DreamDesk source code and database structures to build the Toolbox system, and whether the clients who commissioned the new software authorised that infringement.

## Holding

The Federal Court held that Mr. Semmens was liable for primary copyright infringement and breach of confidence for reproducing substantial parts of the DreamDesk source code, database structures, and PDF templates. The Court held that the remaining respondents (Biggin & Scott, DDPL, and their directors) were **not liable** for authorising the infringement, nor were they liable for breach of contract or breach of undertakings.

## Rule of Law

Under the _Copyright Act 1968_ (Cth), a computer program or compilation (such as a database schema) is an original literary work. Copyright is infringed when a "substantial part" of that original work is reproduced without a license. Furthermore, under s 36(1A), holding a party liable for "authorising" an infringement requires demonstrating that the party had the power to prevent the act and possessed the requisite mental element—specifically, knowing or having reason to suspect that the infringing act was likely to be done.

## Reasoning

**Subsistence and Ownership:** The Court found that the DreamDesk source code, specific PHP files, database schema, and PDF templates possessed the requisite "independent intellectual effort" to qualify as original literary works. Campaigntrack rightfully owned these works following its purchase agreement with DDPL.

**Primary Infringement and Spoliation of Evidence:** The Court relied on expert evidence showing identical code and database structures between DreamDesk and early versions of Toolbox. Because Mr. Semmens deliberately destroyed and altered digital evidence, the Court applied the _omnia praesumuntur contra spoliatorem_ maxim (all things are presumed against a despoiler). This allowed the Court to draw strong negative inferences that the destroyed evidence would have proven the source code was directly copied and subsequently modified to hide the theft.

**Authorisation of Infringement:** Relying on _Roadshow Films Pty Ltd v iiNet Ltd_, the Court determined that authorisation means to "sanction, approve, countenance." Biggin & Scott and its directors explicitly instructed Mr. Semmens _not_ to infringe on Campaigntrack's IP. They lacked the technical expertise to audit the code and trusted Semmens to build it legally. Because they neither knew nor had reason to suspect the infringement, they lacked the mental element required for authorisation. Similarly, DDPL and its director were unaware of Mr. Semmens' rogue actions and were not vicariously liable for his independent breaches.