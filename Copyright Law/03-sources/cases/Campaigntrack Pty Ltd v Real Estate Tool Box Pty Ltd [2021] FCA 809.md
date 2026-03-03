# Federal Court of Australia

Campaigntrack Pty Ltd v Real Estate Tool Box Pty Ltd [2021] FCA 809

## ORDERS

## THE COURT ORDERS THAT:

The parties confer with a view to providing within 14 days agreed orders giving effect to these reasons for judgment and for the further case management of the proceedings.

Note:	Entry of orders is dealt with in Rule 39.32 of the Federal Court Rules 2011.

## REASONS FOR JUDGMENT

## THAWLEY J:

# A  OVERVIEW

The applicant, Campaigntrack Pty Ltd, provides online marketing and sales services to the real estate industry using an online software system known as “Campaigntrack”.  Campaigntrack brought these proceedings against the respondents, alleging, amongst other things, infringement of Campaigntrack’s copyright in the source code of the “DreamDesk” software system.  DreamDesk was a cloud-based real estate marketing system originally created by the third respondent, Mr David Semmens, an experienced software developer.  DreamDesk was in direct competition with Campaigntrack.  Campaigntrack and New Litho Pty Ltd purchased the intellectual property rights in DreamDesk in order to shut down the software and persuade real estate agencies that were using DreamDesk to move to Campaigntrack’s system.

After DreamDesk was sold to Campaigntrack and New Litho, Mr Semmens created another real estate marketing software system called “Real Estate Tool Box” (Toolbox).  Campaigntrack alleged that the Toolbox software reproduced parts of the source code of DreamDesk, thereby infringing Campaigntrack’s copyright.

Mr Semmens was represented when these proceedings were first commenced.  However, during the course of the proceedings, and well before the commencement of the hearing, he continued unrepresented.  The remaining respondents were represented by one legal team.  The respondents other than Mr Semmens are referred to in these reasons collectively as the “represented respondents”:

The first respondent, Real Estate Tool Box Pty Ltd (RETB), was incorporated approximately one month before the Toolbox software went “live”, and was the registrant of the domain name realestatetoolbox.com.au.

The second respondent, Biggin & Scott Corporate Pty Ltd, was the franchisor of the “Biggin & Scott” group of real estate agencies operating in Victoria.  Biggin & Scott used the DreamDesk software before the software was sold to Campaigntrack and New Litho.  Biggin & Scott was also involved in the creation of Toolbox.

The fourth respondent, Dream Desk Pty Ltd (DDPL), owned the intellectual property rights in the DreamDesk software before the software was sold to Campaigntrack and New Litho.

The fifth respondent, Mr Jonathan Meissner, was the sole director and shareholder in DDPL and ran an advertising business, JGM Advertising Pty Ltd.

The sixth respondent, Mr Paul Stoner, was the sole director of RETB and a director of Biggin & Scott.

The seventh respondent, Ms Michelle Bartels (née Page), was the company secretary of RETB and a director of Biggin & Scott.

In addition to asserting infringement of copyright, Campaigntrack made claims for breach of contract against DDPL and Mr Meissner, breach of undertakings given to Campaigntrack by some of the represented respondents and, in equity, for breach of confidence.  Campaigntrack’s claims have been made out against Mr Semmens to the extent indicated below.  In particular, Campaigntrack’s claim for infringement of copyright has been accepted in most respects as against Mr Semmens.  Campaigntrack’s various claims against the remaining respondents have not been made out.

It is necessary to set out the facts in some detail.  Certain legal issues have been determined when addressing the facts given the relevance of these issues to the claims made and the defences to those claims.

# B  THE FACTS

## B.1  The DreamDesk system and relevant terminology

Before setting out the relevant events in the order they occurred, it is useful to know something about the DreamDesk system.  The DreamDesk system was comprised of two principal components relevant for present purposes:

A “web application”: a software application provided to users over the internet, using a computer program or programs executed on a remote server to deliver functionality.  The remote server of the DreamDesk system was a virtual server hosted by Amazon Web Services (AWS).

A “relational database”: a database comprised of tables of data (or records) arranged in columns (or fields) and rows, which included means for “relating” or associating records within the database.  The relational database was also stored on the remote server.

The DreamDesk web application allowed real estate agents to quote, manage, invoice and market real estate campaigns, generate print/online-ready PDF artwork and create email marketing.

The DreamDesk relational database contained the tables of data used by the web application to deliver the functionality to which reference has just been made.  Each database comprised a number of tables.  Each DDPL client, including Biggin & Scott, had its own database.  The DreamDesk relational database was replicated each time an installation was made for a client.

DDPL clients had access to the user-facing interface of the web application, sometimes inelegantly referred to as the “front end”.  Clients did not have access to the underlying source code or to the structure of the relational database.  The source code and the database, stored on the remote server, were protected by a password or key.

It is also useful to explain some terminology.  “Git” is an open-source distributed version control system for source code.  Git allows multiple software developers to work together on a software development project, while maintaining version control of the source code.  Version control is maintained through a “Git repository”.  Multiple software developers, working on the one project, might use a Git repository to coordinate their work in the following manner:

the developer “clones” a copy of the Git repository on his or her local computer;

the developer then makes changes to the source code on his or her local computer;

the developer then “commits” the changes to the local copy of the Git repository;

to share the committed changes, the developer “pushes (up)” the (modified) local copy of the Git repository to the “origin copy” of the Git repository hosted by a Git repository service.  This push merges the developer’s “commits” with the origin copy;

a developer may update his or her local copy of a Git repository by “pulling (down)” commits that have been made to the origin copy since the developer’s local copy was last made.

A Git repository contains the complete history of every change made in the development of the relevant source code or code base.  In addition, information about the migration, creation and deletion of files as well as edits to contents of files is stored.  Mr Semmens used Atlassian’s hosted Git repository offering, which is named “Bitbucket”.  Bitbucket allows a developer to review the history of commits and the history of changes to each file.

In addition to its use as a verb, the word “commit” is also used as a noun, meaning the list of changes made to files and source code created, for example, when a developer commits their changes to their local copy of the Git repository.  A “commit log” is a log summarising the history of commits.  A commit log can be generated from the Git repository.

## B.2  November 2014 to March 2015: Establishment of the DreamDesk venture

In November 2014, Mr Meissner met with Mr Semmens and his business partner, Mr Ewart.  During the meeting, Mr Semmens and Mr Ewart proposed creating a new cloud-based real estate marketing system and sought investment by Mr Meissner to develop the system.  Mr Meissner agreed to fund the venture (the DreamDesk venture).

On 11 March 2015, Mr Semmens, Mr Ewart and Mr Meissner agreed to form a company, DDPL, to pursue the DreamDesk venture.  Mr Meissner was to be the sole director and shareholder.  They also agreed that the shareholding would be divided 40%-40%-20% between Mr Semmens, Mr Ewart and Mr Meissner respectively, once Mr Meissner had recouped his initial investment.  Because of subsequent events, that division of shares never eventuated.

DDPL was incorporated on 12 March 2015 with Mr Meissner as its sole director and shareholder.  The domain name dreamdesk.com.au was transferred from Mr Semmens to DDPL five days later.  Mr Semmens worked on the technical and software development of DreamDesk from about February 2015 and received ongoing payments for his work from DDPL.  Campaigntrack characterised these payments as “salary”, whilst the represented respondents characterised Mr Semmens as being a “contractor” to DDPL.  I do not accept that Mr Semmens was an employee of DDPL.  He was an independent contractor.  There was no suggestion that DDPL withheld tax from the payments made to Mr Semmens, which it would have had to have done if he were an employee.  There was no suggestion that DDPL made contributions to superannuation which, likewise, would have been required if Mr Semmens were an employee.  Mr Semmens issued invoices to DDPL in respect of his work as one would expect of a contractor.  Whether or not Mr Semmens complied with relevant GST requirements is not determinative.  The relationship between the parties, assessed objectively as a whole, is one of principal and contractor, not one of employer and employee.  Although certain documents referred to Mr Semmens as being “employed” by DDPL, this reflects an ordinary use of language even if it is a use of language which might tend to be avoided by lawyers if trying to describe a relationship with precision.  That was not the context.

## B.3  March to August 2015: Biggin & Scott move to DreamDesk

At the beginning of 2015, Biggin & Scott was using the Campaigntrack software in its businesses.  Biggin & Scott had used the Campaigntrack software between 2006 and 2009.  It changed to a different advertising platform called “Advenda Pro” in 2009, and then returned to Campaigntrack in 2013 after it had been incorrectly informed that the company behind Advenda Pro was in perilous financial circumstances.

Between March and May 2015, Mr Stoner was approached by Mr Ewart.  Mr Ewart suggested that Biggin & Scott should consider moving to DreamDesk.  Agreement was ultimately reached for Biggin & Scott to move to the DreamDesk platform.

On 20 May 2015, an agreement entitled “Agreement between Biggin & Scott Corporate Pty Ltd and Dream Desk” (Biggin & Scott – DDPL Agreement) was signed by Mr Stoner (on behalf of Biggin & Scott) and by Mr Meissner (on behalf of DDPL).  The agreement provided:

Biggin & Scott Corporate Pty Ltd agrees to become a client of Dream Desk under the understanding that at all times any templates or data relating to properties and staff put into Dream Desk remains the property of Biggin & Scott Corporate Pty Ltd and or the office that has built an advertisement.

Should Biggin & Scott decide at any stage to cease being a client (leave) Dream Desk all steps available to Dream Desk will be made available to Migrate Biggin & Scott’s templates and property related data to whatever system Biggin & Scott nominates.

Should Dream Desk for whatever reason chose to cease doing business with Biggin & Scott as a group, Migration of all templates and property related data [is] to [be] made available to whomever Biggin & Scott instructs.

Notice period for each company is a minimum of 3 months with all accounts being settled within 4 months from given date.

Biggin & Scott agrees [to] share ideas with Dream Desk that maybe [sic] onsold to other agents or groups under the understanding that they are always available to Biggin & Scott offices.

All price increases must be tabled and discussed 3 months prior to being implemented, Understanding that offices are working 3 months ahead.

Biggin & Scott went “live” with the DreamDesk platform on 17 August 2015.

## B.4  May 2016: Admission of infringement of Process 55’s intellectual property

As described further below, on 26 May 2016, Mr Semmens stated that he had copied an earlier system, “Process 55”, when he developed the DreamDesk system.  Process 55 was a web-based real estate marketing system.  Mr Semmens was involved in the development of Process 55 during his employment with Digital Hive Pty Ltd from 2001 to 2006.

The Digital Hive business, including its intellectual property (which included Process 55), was sold in September 2013 by Digital Hive to The Digital Group Pty Ltd, a company founded by Mr Semmens and his brother-in-law, Mr Farrugia.  Mr Semmens was a director of Digital Hive from 21 January 2005 to 7 April 2006.  Mr Farrugia was also a director.  Mr Stewart joined the venture after it as founded and became a director.  Mr Farrugia and Mr Stewart held the view that Mr Semmens had stolen the intellectual property of Digital Group in the development of the DreamDesk system.

On 26 May 2016, Mr Semmens signed two documents, which both included the following:

I, David Semmens of [redacted address] state that:

(1) I am an officer of Dream Desk Pty Ltd which is a commercial competitor of The Digital Group Pty Ltd and Campaign Track.

(2) Whilst an officer of Dream Desk Pty Ltd, I have deliberately gained access to the private email accounts of Ashley Farrugia CEO The Digital Group and Gavan Stewart Exec Chairman of The Digital Group

(3) Whilst an officer of Dream Desk Pty Ltd, I have deliberately used confidential information and trade secrets and other intellectual property (including but not limited to the ‘Process 55’ system) being the property of TDG and Campaign Track so as to develop the business of Dream Desk Pty Ltd.

(4) Mr Martin Ewart, a person associated with Dream Desk Pty Ltd, is and was at all material times aware of the conduct I have engaged in as described above.

One version of the document also included an extra paragraph which stated:

I acknowledge that the actions admitted above prevent me from continuing any further employment with Dreamdesk Pty Ltd henceforth.

On 28 May 2016, Mr Semmens and Mr Ewart told Mr Meissner that they had been informed that the Digital Group’s intellectual property was being used in the DreamDesk software.  Two days later, Mr Farrugia and Mr Stewart told Mr Meissner that they considered Mr Semmens had used Digital Group’s intellectual property in the development of DreamDesk without authorisation.  Mr Farrugia told Mr Meissner that the intellectual property which was alleged to have been stolen related to the “PDF Distiller”, which Mr Meissner understood enabled the DreamDesk system to produce and edit PDF images, being the images used in real estate marketing campaigns by DreamDesk clients such as Biggin & Scott.

Understandably, Mr Meissner did not want to operate using intellectual property he or DDPL was not authorised or licensed to use.  He decided either to negotiate to buy Process 55 or to sell DreamDesk.

Mr Meissner and Mr Farrugia discussed DDPL buying the intellectual property in the Process 55 system or a joint venture between DDPL and Digital Group.  Those discussions were overtaken by Campaigntrack and New Litho’s negotiations with Digital Group, described next.

## B.5  Late May to July 2016: Negotiations to purchase Process 55; sale of DreamDesk

In May and June 2016, Campaigntrack and New Litho had a number of discussions with Digital Group regarding the possible purchase of the intellectual property rights in the Process 55 system.  These arose because Campaigntrack wished to purchase the rights in both Process 55 and DreamDesk in order to acquire control of the DreamDesk system, to shut it down and to attempt to persuade DDPL clients to move or return to Campaigntrack.  It was ultimately agreed in principle that Campaigntrack and New Litho would purchase the intellectual property rights in Process 55 for $300,000.

Starting with a meeting on 15 June 2016, Mr Meissner and representatives from Campaigntrack and New Litho began to negotiate the sale of DreamDesk.  The question whether DreamDesk’s clients had any rights in respect of data stored in the DreamDesk relational database was not raised at the meeting on 15 June 2016.

From early July 2016, Mr Meissner, Campaigntrack and New Litho negotiated the terms of the agreement for the sale of DreamDesk.  It was eventually agreed that all intellectual property of DDPL relating to the operation of DreamDesk was to be sold to Campaigntrack for $50,000 and there was to be a separate incentive-based arrangement whereby payments would be made to Mr Meissner for securing DreamDesk clients to transition to Campaigntrack.

On 13 July 2016, Mr Meissner and DDPL’s solicitor had a conversation with Campaigntrack’s solicitor regarding a licence to use the intellectual property in the “Dashboard”.  The “Dashboard” was a reference to the homepage or intranet page of the user-facing “front-end” of the DreamDesk system.  This displayed key information to the user.  Campaigntrack’s solicitor summarised the conversation in an email sent to Campaigntrack and New Litho (emphasis in original):

Dear All

I have just spoken to the other side in this matter.

They are happy with the issue of Process 55. Apart from the finer details, there appears to be one final issue. It involves the licence back of th[e] IP [intellectual property] to operate the ‘Dashboard’.

Apparently, Dream Desk want a licence to use the IP needed for the Dashboard so that they can develop it further and commercialise it. They want:

1. An exclusive and irrevocable licence for the Dashboard IP; and

2. For the Dashboard licence to not be conditional on RT [Edgar] and [Biggin & Scott] signing up. i.e. they want to be able to commercialise the Dashboard regardless of whether RT Edgar and B&S sign a deal to use CampaignTRACK.

Basically, they want to keep on trading as if the Dashboard was theirs. You would have to give consideration as to whether you would like to licence the Dashboard to third parties in the future but in any case, the licence will have to be on the basis that CT will also use the technology and provide the Dashboard to whoever wants it.

Has this been discussed, what are your thoughts?

Campaigntrack submitted that Mr Semmens’, Mr Meissner’s and DDPL’s intention to develop the Dashboard further, evidenced by this email, was later put into action by Mr Semmens’ development of the Toolbox system.  Campaigntrack correctly observed that Mr Meissner occasionally referred to the DreamDesk system as a whole as “Dashboard” and that the Toolbox system, whilst under development, was sometimes referred to as “Dashboard” or “Dash”.

On 18 July 2016, Mr Meissner signed the following agreements:

an agreement entitled “Agreement for the Sale of Assets” between, on the one hand, DDPL and him and, on the other, Campaigntrack and New Litho (the DreamDesk sale agreement); and

a “Binding Heads of Agreement” between himself and Campaigntrack and New Litho.

The DreamDesk sale agreement provided for the sale of intellectual property associated with the operation of DreamDesk to Campaigntrack and New Litho.  Clauses 1.1 to 1.4 of the DreamDesk sale agreement provided :

1. 	Sale of intellectual property and business assets

1.1. 	Dream Desk agrees that it will sell to Campaigntrack and New Litho (the “Purchasers”) the DreamDesk Platform and all intellectual property associated with the operation of the DreamDesk Business, including copyright (including any rights to source code), design, patents and trademarks and all rights to the business name of the DreamDesk Business and all domain names registered by Dream Desk, including dreamdesk.com.au (the [“]Intellectual Property”).

1.2. 	The parties acknowledge that the sale of the Intellectual Property does not include Process 55 as that is owned by Digital Group Pty Ltd. The sale does include any intellectual property that Dream Desk may have that is derived from Process 55 or that is separate but used in conjunction with Process 55 for the operation of the DreamDesk Business.

1.3. 	In consideration for the Purchasers purchase of the Intellectual Property the Purchasers will pay to Dream Desk an amount of $50,000.00 (the “Purchase Price”) within 7 days of the date that this agreement becomes binding under clause 5.

1.4. 	All rights, entitlement and interest in and title to the Intellectual Property will pass to the Purchasers on payment of the Purchase Price.

Clauses 2.1 and 2.3 of the DreamDesk sale agreement provided for DDPL to have a licence of the intellectual property for a limited period ending on 3 October 2016:

2. 	Licence of intellectual property

2.1. 	The Purchasers agree that on payment of the Purchase Price and the transfer of title to the Intellectual Property as anticipated by this agreement they will grant to Dream Desk an exclusive Australia wide licence to use the Intellectual Property for the restricted purpose of operating the DreamDesk Business and for the limited period commencing on the date the licence is given until 3 October 2016, unless extended by agreement between the Purchasers and Dream Desk (the “Transition Period”). The Purchasers agree that the licence period will be extended to 1 January 2017 if at least one client of Dream Desk known as RT Edgar and Biggin & Scott enter into agreements on or before 2 September 2016 with Campaigntrack or any entity associated with Campaigntrack for the use of the CampaignTRACK Platform.

…

2.3. 	In addition to the above, the parties agree that if either RT Edgar or Biggin & Scott enter into agreements on or before 2 September 2016 with Campaigntrack or any entity associated with Campaigntrack for the use of the CampaignTRACK Platform, the Purchasers will grant a limited, Australia wide licence to use the Intellectual Property for the restricted purpose of supplying the product currently provided by Dream Desk known as the Dashboard to clients of Dream Desk who are not engaged or associated with the real estate Industry on the following conditions:

2.3.1. 	The Intellectual Property licenced will be only that Intellectual Property that is required for the operation and supply of the Dashboard, including only that source code relating to the Dashboard. Dream Desk will have no licence to use, and no rights to any of the Intellectual Property that is not required for the operation and provision of the Dashboard.

2.3.2. 	The licence will commence on the expiry of the general licence under clause 2.1 on 1 January 2017.

2.3.3. 	If only one of RT Edgar or Biggin & Scott enters into the agreement contemplated by clause 2.3 the licence will be an exclusive licence for a period of five years from the date that such an agreement is entered into and any renewal of the licence will be on terms that it will be a non-exclusive licence. After the expiry of the exclusive licence period the Purchasers will be free to licence the same Intellectual Property to third parties. If both RT Edgar and Biggin & Scott enter into the agreements contemplated by clause 2.3 the licence will be an exclusive licence for a period of five years from the date that the first such agreement is entered into and any renewal of the licence will be on terms that it will be an exclusive licence.

2.3.4. 	The initial term of the licence will be five years. The licence will be renewed on the expiration of the initial term under the same terms if mutually agreed to by the parties. The licence renewal will not be unreasonably withheld by the Purchasers.

2.3.5. 	The licence granted to Dream Desk cannot be used for any existing client of Dream Desk unless agreed to by the Purchasers.

2.3.6. 	The licence will immediately terminate if the business structure or makeup of Dream Desk changes in a material way from the date of these Heads of Agreement or if Dream Desk breaches the terms of the licence.

2.3.7. 	The terms of the licence agreement will not restrict the Purchasers from supplying products and services of the same kind as the Dashboard using the same Intellectual Property that is licenced. The term ‘exclusive’ as referred to in this clause is to be taken to mean that the Purchasers will not grant the same licence to a third party but it does not restrict the Purchasers from exploiting any Intellectual Property in any way.

2.3.8. 	Dream Desk will not be permitted to transfer, assign, sub-licence or otherwise grant rights to third parties to the licenced Intellectual Property unless the Purchasers approve in writing.

On 26 July 2016, Ms Kylie Neal (a consultant to DDPL), gave a presentation via video conference to Campaigntrack staff members.  Ms Neal’s presentation provided a comprehensive demonstration of the DreamDesk system.  Mr Meissner also attended the presentation.

## B.6  30 July to Mid-August 2016: Origins of Toolbox

On 30 July 2016, Mr Semmens made an enquiry with the online software company, Aleyant Systems, LLC, which owned eDocBuilder, a web-based online design, personalisation and variable data publishing system that was designed to be integrated into web to print and other e-commerce systems.  The online enquiry was in the following terms:

On 2 August 2016, Mr Semmens discussed his eDocBuilder enquiry with an Aleyant representative, Mr Jeffrey Protheroe, through an online demonstration/conference.  I infer, including from events described later, that the point of the enquiry was to determine whether eDocBuilder might be used in a new system intended to have the same essential functionality as DreamDesk.  As will become apparent, I also conclude that the new system (Toolbox) was developed by first copying substantial parts, probably the whole, of the source code of DreamDesk.

On 3 August 2016, Mr Semmens met with Mr Stoner at Biggin & Scott’s head office.  Mr Semmens told Mr Stoner that he could create a system with similar functionality to DreamDesk and Campaigntrack and asked whether Mr Stoner would be interested in him developing the system.  At the meeting, Mr Stoner (the CEO of Biggin & Scott) showed Mr Semmens a letter dated 3 August 2016, on Biggin & Scott letterhead.  The letter, which had been written and signed by Mr Stoner, provided (errors in original):

David Semmens

You are instructed to build a web to print delivery system that does not breach any other companies IP or ownership, in particular Dream Desk or Campaign Track.

All products used should be off the shelf products owed by 3rd parties with a licence agreement or able to be used through open code or any other industry standard that classes the use as open (can not be claimed)

All fields should match industry standard so as to be delivered as per their specs and able to match our CRM’s in particular Box & Dice.

In simple terms we do not want any thing used that can be claimed as owned by the 2 companies above.

We are happy with E-DOC being used as the PDF delivery system as long as it can deliver our finished adds as per Biggin & Scott style guide. Please continue with the building of these templates.

With regards to property data that offices are loading into the Dream Desk system please arrange to migration scripts of this data to be loaded into the New E-doc templates to minimise as much disruption as possible.

We have an agreement in place with Jon Meisner regarding office and property data to which Jon assures me our clients and offices data is and always will be ours and is not part of his deal.

Mr Stoner had handwritten his and Mr Semmens’ name at the foot of the letter.  Mr Stoner signed the letter above his name.  Mr Semmens did not sign the letter.  In cross-examination, Mr Semmens accepted that he discussed the letter with Mr Stoner. He could not recall whether he was provided with a signed copy of the letter during the meeting.

I infer from the terms of the letter, and the fact that Mr Semmens was looking into eDocBuilder, that the development of a new system (ultimately Toolbox) was already underway at the time Mr Stoner wrote the letter.  It is also clear from the terms of the letter that Mr Stoner knew that it was proposed that the new system would use eDocBuilder.

Mr Stoner gave the following evidence in cross-examination:

So you say that this was the instruction that you gave Mr Semmens on 3 August 2016, to build a Web to Print delivery system that does not breach any other company’s IP or ownership, in particular, Dream Desk or Campaigntrack?---Yes.

And you say that you did that without knowledge of what I have taken you to in relation to Process 55?---Yes.

Other than what Mr Ewart said to you about a “problem”?---So on this date, I knew that Dream Desk was – had been, well, I’m not sure if it had been purchased or was being purchased.

You didn’t know or you did know?---I’m not sure. Well, I’m not sure if it had been purchased by then. But on that date, I knew that, who had bought it or was buying it and what the future looked like.

…

Why include “Breach any other company’s IP” if the only knowledge you had was that of the Dream Desk sale?---Well, that’s what their issue was, that they had breached Process 55’s IP.

Well, I think, the evidence you gave us, was you were only aware, very broadly, of what Mr Ewart had told you?---That’s in May, this is August.

So you – the evidence you give is that you became more familiar with the situation relating to Mr Semmens from May to August 2016. Is that correct?---Absolutely.

…

You knew there was a problem with Process 55 and the use of Process 55 by Dream Desk, did you not?----At that stage, yes. On 3 August.

…

You appreciated that there was real risk that Mr Semmens might infringe another company’s IP?---No. I would have to say, “No”. I trust David.

Well, why would you put in – you instructed to:

Build a Web to Print delivery system that does not breach any other company’s IP or ownership, in particular, Dream Desk or Campaigntrack.

?---Just to make it clear, I don’t want any crossovers with anything.

…

And the only basis for putting in an instruction, Mr Stoner, is that you were concerned about the possibility that he would use code belonging to Dream Desk or Campaigntrack? — It’s possible. But I don’t think that’s my meaning.

Campaigntrack submitted that “Mr Stoner knew there was a real risk that, in developing the new system, Mr Semmens might infringe the intellectual property rights of DDPL or Campaigntrack”.  Campaigntrack also submitted that “Mr Stoner’s denials that he did not appreciate the risk of infringement, and that he was not seeking to address that risk by the instructions in [his letter], are simply not credible in light of his answers in cross-examination, and should be rejected”.

In the context of the events which had occurred, including the fact that – to Mr Stoner’s knowledge – Mr Semmens had admitted to using Process 55 in developing DreamDesk, it was hardly surprising that Mr Stoner would seek an assurance from Mr Semmens that he would not infringe the intellectual property rights of others in building a web to print delivery system.  I am satisfied that Mr Stoner trusted Mr Semmens not to infringe the intellectual property rights of DDPL or Campaigntrack in developing the new system.  I conclude that Mr Stoner did not want Mr Semmens to misuse intellectual property belonging to others in developing the new system.

Ms Bartels did not see the instruction letter.  However, she was informed of the substance of it by Mr Stoner.  Ms Bartels left it to Mr Semmens to determine the specifications of the new system.  Campaigntrack referred to the following evidence given in Ms Bartels’ affidavit (Campaigntrack’s emphasis):

In August 2016, I was informed by Paul Stoner that he had been approached by David Semmens in relation to the development of a new online advertising system that did not have any software or information in it that it should not have … I trusted David enough that he would not make a mistake in terms of using material in the new system that should not be used.

Campaigntrack submitted that “[t]he deontic words — ‘should not have’, ‘mistake’ and ‘should not be used’ — show that Ms Bartels was aware that Mr Semmens had been accused of misusing the intellectual property in the Process 55 system, and that she was aware of the risk of infringement in the development of the new system” and that “[t]he word ‘enough’ shows that her trust in him was not unqualified; that she had some reservations about him”.  I accept that Ms Bartels is likely to have known that Mr Semmens had admitted to using Process 55 in DreamDesk and that this had caused problems.  I conclude that Ms Bartels did not want Mr Semmens to misuse intellectual property belonging to others in developing the new system.

As things stood at 3 August 2016, Mr Semmens had until 3 October 2016 to develop the new system.  This was because the licence to use the DreamDesk system, granted by Campaigntrack to DDPL under the DreamDesk sale agreement, would end on 3 October 2016.  Campaigntrack observed that the evidence suggested that the DreamDesk system was created over a period longer than 2 months, namely beginning in February 2015 and going live for Biggin & Scott on 17 August 2015.

On 5 August 2016, Mr Semmens received an email confirming the creation of an eDocBuilder account.  Two similar versions of a welcome email from eDocBuilder were in evidence.  The version of this email placed into evidence by Mr Semmens was in the following form:

From: “Aleyant Systems Support” <support@aleyant.com>

Subject: [140-1F367834-0A49] Welcome to eDocBuilder, JGM Advertising!

Date: 5 August, 2016 6:03:32 am GMT+8

To: david@jgmadvertising.com.au

Cc: jprotheroe@aleyant.com

Reply-To: “Aleyant Systems Support” <support@aleyant.com>

WELCOME!

Thank you for your order! Your account has been set up. Below you will find important information to access the system, and to take advantage of the services available to you. Please keep this email for future reference and share it with all staff that will be working in eDocBuilder!

The following is a summary of your order:

eDocBuilder Professional

----------------------------------------------------------------------

EDOCBUILDER ADMIN

----------------------------------------------------------------------

eDocBuilder Admin: http://creator-sg.edocbuilder.com

Your master login info:

User: ********

Password: *******

GETTING STARTED

…

Another version of this email was provided on 24 November 2016 by Mr Stoner to his solicitor, who provided a copy of the email to Campaigntrack’s solicitors.  This version of the email indicated it was sent at the same time and included almost identical content to the email placed into evidence by Mr Semmens.  The only difference was that Mr Semmens’ JGM Advertising email address was not in the “To” field, which instead included Mr Stoner’s Biggin & Scott email address.  The User and Password fields were also different in that they referred to Mr Stoner’s Biggin & Scott email address, and the password “JlbMSTea”:

From: “Aleyant Systems Support” <support@aleyant.com>

Subject: [140-1F367834-0A49] Welcome to eDocBuilder, JGM Advertising!

Date: 5 August, 2016 6:03:32 am GMT+8

To: pstoner@bigginscott.com.au

Cc: jprotheroe@aleyant.com

Reply-To: “Aleyant Systems Support” <support@aleyant.com>

WELCOME!

Thank you for your order! Your account has been set up. Below you will find important information to access the system, and to take advantage of the services available to you. Please keep this email for future reference and share it with all staff that will be working in eDocBuilder!

The following is a summary of your order:

eDocBuilder Professional

----------------------------------------------------------------------

EDOCBUILDER ADMIN

----------------------------------------------------------------------

eDocBuilder Admin: http://creator-sg.edocbuilder.com

Your master login info:

User: pstoner@bigginscott.com.au

Password: JlbMSTea

GETTING STARTED

…

Campaigntrack also put into evidence a document printed from the Toolbox Git repository which indicated that the username and password for the template for eDocBuilder was “david@jgmadvertsing.com.au” and “JlbMSTea”.

Mr Stoner gave evidence that the reason for the two similar emails was that he wanted his own login to the eDocBuilder:

Is the evidence you give his Honour that this email was received by you from Aleyant system support, or was this email changed before you sent it on to Mr Maletic?---I think in memory of all this, the original one that I was sent was a login called “David” and I wanted my own login.

…

Well, was that you? Did you make that change?---No. I wanted – I remember with this very clearly I wanted to send Mr Maletic a login with my name on it, and my password - - -

…

MR GREEN: You can’t explain any reason why those details now appear in an email that has an identical time, can you?---As I said before, when David sent me the original one, I wanted my own.

So did you change the – did you change the details of the user and the password from the asterisked version?---I didn’t change anything.

Did you communicate with anyone asking for a change?---No.

…

… Because, as I said, the first one that I was sent had David who is the login. I called David straightway and said, “I need an email with me as the login and I need my own password, login and password.”

Campaigntrack submitted that the last statement “should be understood as an instruction by Mr Stoner to Mr Semmens to edit the [eDocBuilder] Welcome Email”, noting that Mr Stoner forwarded the edited email to Mr Maletic of Mills Oakley (who acted for Biggin & Scott) for the purpose of providing the document to an independent expert.  The independent expert was engaged in November 2016 to determine whether there was any potential copying from the DreamDesk system.  Campaigntrack submitted that the Court should find that Mr Stoner, Biggin & Scott and RETB wanted to convey a false impression that Mr Stoner and Biggin & Scott had registered to use eDocBuilder, independently of DreamDesk and JGM Advertising.

The first email set out at [47] above does not identify a username and password at all.  It is unlikely this was the form of the email sent to Mr Semmens.  The original email to Mr Semmens would have identified the username and password.  I do not accept that the email as received by Mr Semmens was in the form identified at [47] above.  I conclude that the original email referred to the username and password as “david@jgmadvertsing.com.au” and “JlbMSTea” respectively.  It is possible that two emails (or more) were sent by Aleyant at precisely the same time to different email addresses providing different usernames and passwords.  However, this was not Mr Stoner’s explanation or Mr Semmens’ explanation.  On balance, I conclude that Mr Semmens changed the content of the email he had received from Aleyant.

I do not conclude that Mr Stoner instructed Mr Semmens to alter the 5 August 2016 email as such.  However, the events do reflect adversely on Mr Stoner’s credibility.  Mr Stoner did not give evidence that he was sent an email from Aleyant on 5 August 2016.  There was no evidence to suggest that Mr Stoner considered he had been given his own username and password on or around 5 August 2016.  No evidence or reason was given why Mr Stoner would want or require his own username and password.  Mr Stoner gave evidence that he might have tried his (purported) login details once, but that he could not recall whether they worked.  Mr Stoner denied that he provided the second version of the email to “hide Mr Semmens’ involvement in Real Estate Tool Box”.  It is likely that Mr Stoner wanted his own login details to be created in order to provide those details to Campaigntrack’s solicitor so as not to provide them a document which indicated the involvement of Mr Semmens in the relevant events.

Mr Semmens most likely started to develop the Toolbox system on his local computer on about 9 August 2016.  The first commit to the Toolbox Git repository (the Dashboard Vault1 Repository) was made by Mr Semmens on 26 August 2016.  The time stamp of the files in the first commit showed that the first file was created on a local computer on 9 August 2016.  Mr Semmens kept source code on his local computer whilst initially developing the code and used Bitbucket once he was to be assisted by other developers (Mr Gallagher and Mr Zhang) so they could share code between themselves.

It is likely that Mr Semmens started to develop the Toolbox system on his local computer at DreamDesk/JGM Advertising’s offices.  The local computer on which initial development occurred has not been able to be located.  In cross-examination, Mr Semmens said he discarded, overwrote or gave away old computers.

From 16 August 2016 to 19 September 2016, Mr Semmens ran a number of “migration scripts” in respect of the DreamDesk database.  This was the subject of unchallenged evidence given by Mr Allen, a software developer who had previously been employed by Campaigntrack and who was engaged by Campaigntrack’s solicitors to provide technical assistance for the present proceedings.  The migration scripts did not copy source code; they only copied data from one database to another database.  The first migration script, run on 16 August 2016, was unsuccessful but, at least by 30 August 2016, some had been successfully run.  The migration scripts copied database records from DreamDesk to a database at the domain “dash.vault1.net”.  I infer that “dash.vault1.net” was the database for the Toolbox system.  I draw that inference because: a login page to the Toolbox system was available when “dash.vault1.net” was entered into an internet browser; the Toolbox repository was named “Dashboard Vault1”; and “Dashboard” or “Dash” was the project name for the Toolbox system.

Migration scripts (not all of which were successful) were run in respect of the DreamDesk database for:

Biggin & Scott: on 16 and 23 August and 2, 8, 12, 17 and 19 September 2016;

RT Edgar: on 16 and 17 August 2016; and

Jellis Craig: on 17 to 19 and 26 to 30 August 2016.

Mr Semmens accepted that he ran the migration scripts.  In cross-examination, Mr Semmens stated that Mr Meissner had instructed him to “export the client’s data out” or give the client their data, but later clarified:

Was it Mr Meissner?---He would have just said give the client their data, I’m not sure. I don’t think he would have said synchronise their data.

Mr Semmens stated Ms Bartels may have told him to keep the client data up to date.  He did not think any instruction was given to him by Mr Stoner in relation to client data.

I infer from the events which had occurred to this point, including the development of Toolbox and the running of the migration scripts, that Biggin & Scott was not intending to remain with Campaigntrack if at all possible, but was progressing its objective of setting up its own system.

It is important to appreciate, as Mr Semmens emphasised in submissions, that the running of migration scripts only transferred a client’s data from one database to another.  The data so transferred was not the intellectual property of Campaigntrack.

Campaigntrack initially submitted that the running of the migration scripts “meant that there was a reproduction of the structure, the database structure, in the program itself” and that the running of the scripts necessarily copied the structure of the underlying database and contained the data structures.  It was submitted that the “migration scripts are a way in which one can create the data structures through programmatic means, through running a program”.  Campaigntrack submitted:

HIS HONOUR: So, but – and what does that mean, though? Doesn’t that mean – doesn’t running the migration scripts mean that you’re taking the data for Biggin & Scott? No.

MR GREEN: Yes, you’re copying the data structures.

HIS HONOUR: For Biggin & Scott’s - - -

MR GREEN: Well, you’re copying the databases.

…

HIS HONOUR: Are migration scripts always data?

MR GREEN: Migration scripts – the migration scripts always include the reproduction of the databases – the reproduction of the structure into which the migration – the data is then put.

Eventually, however, it became clear that the running of migration scripts does not necessarily involve a reproduction of the database structure.  After asking what evidence supported these submissions and observing that the evidence the Court was then taken to did not appear to support the submissions, it became apparent that all that could be put was that the migration scripts showed that the databases into which the data was copied were structurally the same (or very similar).  This might indicate that Mr Semmens modelled the Toolbox database structure from the DreamDesk database structure, but the running of the migration scripts was not a means by which the database structures themselves were copied.

Mr Semmens submitted, and I accept, that the migration scripts simply transferred the client’s data that the client owned.  The running of the migration scripts did not, of itself, copy any intellectual property of Campaigntrack.

In cross-examination, Mr Semmens was asked about why he ran migration scripts in respect of Jellis Craig, when Jellis Craig was not involved in the Real Estate Tool Box venture:

And then you ran further migration scripts in respect of Jellis Craig on 17 and 19 August. Again, they were still with Dream Desk, weren’t they?---They were, yes.

And there was no basis for doing that on your - - -?---Yes.

- - - asserted basis that you were trying to move client data?---Yes, I can’t recall why I did Jellis Craig, there was actually no need to do Jellis Craig at all.

There was absolutely no need to do Jellis Craig?---No, no.

Except for the fact that you were building a replica system of Dream Desk, weren’t you?---Well, if you call Tool Box – I was building Tool Box, yes.

The applicant submitted that the inclusion of Jellis Craig in the migration scripts demonstrated that the respondents’ true objective was to maximise the prospects that existing DreamDesk clients would move to Toolbox after DreamDesk was shutdown.

In light of Mr Stoner’s instruction letter at [38] above, which stated “please arrange to migration scripts of this data to be loaded into the New E-doc templates to minimise as much disruption as possible”, I accept that Mr Stoner knew about the migration scripts in respect of Biggin & Scott data.  It is likely that Ms Bartels also knew.

Mr Semmens gave evidence that he did not tell Ms Bartels or Mr Stoner that he ran the migration scripts on the RT Edgar and Jellis Craig data:

So, is the evidence you give now that you had conversations with each of Mr Meissner and Ms Stoner and possibly – sorry, Ms Bartels and possibly Mr Stoner about what should be done with the RT Edgar and Jellis Craig data. Is that right?---No. No, I wouldn’t have discussed RT Edgar and Jellis Craig data with them.

I accept that Mr Semmens copied the RT Edgar and Jellis Craig data in order to maximise the prospect of obtaining RT Edgar and Jellis Craig as clients of Toolbox should the opportunity later arise.  I am not satisfied that Mr Stoner or Ms Bartels knew that Mr Semmens had run migration scripts to copy the data of RT Edgar or Jellis Craig.

## B.7  Mid to Late-August: Biggin & Scott consider software providers; sale of Process 55

Mr Stoner gave evidence that, in about mid-August 2016, he decided that, if the Toolbox venture were to go ahead it should be done through “a separate and different company” to Biggin & Scott.

On about 18 August 2016, Ms Keys of Campaigntrack met with Ms Bartels to discuss whether Biggin & Scott would transition to Campaigntrack.  Ms Keys gave an account of the conversation in which she stated she recalled Ms Bartels as having said that Biggin & Scott was “happy to agree terms with you but [we] just don’t want our business disturbed” in the context of stating that Biggin & Scott did not want DreamDesk shut down whilst they were entering spring, Biggin & Scott’s busiest time of the year.  I accept that Ms Bartels sought to convey that Biggin & Scott were considering moving to Campaigntrack, whilst at the same time seeking to develop the new Toolbox system.

From 18 August 2016 until 6 September 2016, Biggin & Scott made enquiries with, and received offers from, other providers of online advertising systems, including Excel (Australasia) Pty Ltd and RealHub.  Presentations were made to Biggin & Scott by both Excel (on 19 and 26 August 2016) and RealHub (on 5 September 2016).  Mr Stoner gave evidence that these proposals were made in the course of Biggin & Scott exploring other options for online advertising systems.  Campaigntrack submitted that Biggin & Scott’s interest in other systems was not a “bona fide interest”, but rather was done to: (a) obtain pricing information in order to price the Toolbox system competitively; and (b) feign interest in Campaigntrack so that Campaigntrack would keep the DreamDesk system operational.  It is probable that there were a number of reasons for the enquiries.  The likelihood is that Mr Stoner’s preference was that the new system would be operational by 3 October 2016 (when the “licence-back” granted by Campaigntrack to DDPL was due to end), but that – if it was not – another service provider might be required.  The likelihood is that Mr Stoner’s least preferred option was to use Campaigntrack.

No doubt the enquiries with Excel and RealHub also provided pricing information and insights into the functionality of the Excel and RealHub software which might have been relevant and useful if the new system, Toolbox, was commercialised.  I doubt that the enquiries were made with the object of “feigning interest in Campaigntrack”, although I accept that, at this time, Biggin & Scott conveyed to Campaigntrack that it was actively considering using Campaigntrack’s system when that was its least preferred option.

In August 2016, Digital Group, Campaigntrack, New Litho and their respective directors executed an agreement entitled “Agreement for the Sale of ‘Process 55’” (Process 55 sale agreement).  From the date of completion of the agreement, being 25 August 2016, Campaigntrack and New Litho became owners of “the whole of Process 55”, including its source code and intellectual property rights.

## B.8  26 August to Early September 2016: Early development of Toolbox

As noted earlier, the first commit to the Toolbox Git repository (the Dashboard Vault1 repository) was made by Mr Semmens on 26 August 2016.  A total of eight commits to the Toolbox repository were made on this day.  As also noted earlier, migration scripts for Jellis Craig were run on 26 August 2016.

On 1 September 2016, Ms Neal wrote an email (from “kylie@askthephantom.com.au”) to Ms Bartels, Ms Melissa Fato of RT Edgar and “accountservices9999@yahoo.com”, an email address being used by Mr Meissner.  The email stated (emphasis in original, paragraph numbering added):

[1] Morning Ladies, (cc: Jon)

[2] This is my business email, best to use this for non-DD-related matters.

[3] Just some updates for you:

[3.1] Jon has not received details of extension; he will forward when he does and advise CT to deal direct from here on in.

[3.2] Reviewing Jon’s agreement, it appears the worst possible shutoff date is 3/10/16 - TBC by Jon’s solicitor.

[3.3] It also appears that the extension to 1/1/17 is contingent upon ‘one of the DD clients known as RT Edgar or Biggin & Scott’ signing with CT. For me that’s pretty vague and could be a single office/entity. TBC by Jon’s solicitor.

[3.4] Today I’m working on:

[3.4.1] some alternate business continuity plans

[3.4.2] reallocating resource from DD to work on new platform (which will mean minimising non-essential changes and putting them right into the new platform)

[3.4.3] project plan for new platform

[3.5] The first hurdle is to register the business/domain - are we any closer from your perspective? What’s the next action on this?

[3.6] Call if you need me.

[3.7] K

[3.8] Kylie Neal

[3.9] M: [redacted mobile number]

RT Edgar’s involvement in Toolbox ceased a short time after this email.

I accept the submission advanced by Campaigntrack that it is likely that Mr Meissner was aware of the development of the Toolbox system by DDPL and JGM Advertising staff – see: [1] “(cc: Jon)”.  Mr Meissner denied that he controlled the email address “accountservices9999@yahoo.com”.  Whether or not Mr Meissner controlled the email address, I accept that he was using it at the relevant time.

Campaigntrack observed in submissions that Mr Meissner had agreed to use his “best endeavours” to persuade Biggin & Scott and RT Edgar to return to Campaigntrack’s system, as contemplated by cl 2.7 of the Binding Heads of Agreement.  Campaigntrack submitted that the 1 September 2016 email showed that Mr Meissner (and Ms Neal, DDPL and JGM Advertising) were attempting to advance Biggin & Scott’s and RT Edgar’s interests in the Toolbox venture, by:

seeking to extend the licence to use the DreamDesk system beyond the original 3 October 2016 deadline, so as to maximise the available time for development of the Toolbox system: at [3.1]-[3.3];

actively developing a project plan for the Toolbox system: at [3.4.1], [3.4.3]; and

allocating resources away from the development of the DreamDesk system to the development of the Toolbox system: at [3.4.2].

Campaigntrack also observed that, although the respondents appear to have created a detailed project plan for the development of the Toolbox system, none of the respondents put the Toolbox project plan into evidence or discovered any such plan.

Campaigntrack submitted that Ms Neal’s use of alternative email addresses (she did not use her DreamDesk email and she contacted Mr Meissner at the “acountservices9999” address) suggested that Mr Meissner, Ms Neal, DDPL and JGM Advertising “wished to act surreptitiously in their involvement in the development of the Toolbox system”.  I accept that Ms Neal wanted to use different email addresses for work on the Toolbox system.

## B.9  5-7 September 2016: Variation of DreamDesk agreements; payment of purchase price

The DreamDesk sale agreement and the Binding Heads of Agreement were varied on 5 September 2016, in respect to the mechanism for incentive-based arrangement for securing DreamDesk clients to transition to Campaigntrack.

On 6 or 7 September 2016, Campaigntrack and New Litho paid the purchase price of $50,000 under the DreamDesk sale agreement.  On 7 September 2016, the CEO of New Litho, Mr Watts, sent an email to Mr Meissner and Ms Keys attaching the remittance advices for the payments to DDPL, and asking for the passwords that were to be provided as part of the handover of DreamDesk:

Jon,

Please find attached the remittances for the $50,000. $25000 from each party.

Now that payment is finalised, can you please instruct David Semmens to provide the following information to us via email as per clause 1.6:

1. Amazon webservices password

2. Administrator password to Dream Desk platform

3. Management passwords

4. Client logins for all clients

5. Any passwords for day to day operation of dream desk

6. Passwords and access details required for management and configuration of Dream Desk;

If you could CC me in on the request to David, I’m happy to chat with him if he has any questions. I’d like to sit down with him for a few hours and go through how the system is set up and managed as well.

Is Ewart out of the office?

## B.10  Mid-September 2016: Ongoing development of Toolbox; relationship between Biggin & Scott and Campaigntrack deteriorates

On 8 September 2016, a number of emails were exchanged between Ms Neal and Ms Bartels (copied to Mr Semmens and Mr Stoner) regarding the media vendor integration (MVI) of data between the real estate agency’s customer relationship management system supplied by “Box+Dice” and the agency’s advertising system (eg DreamDesk or Toolbox).  The emails refer to “the new system”, which I infer was a reference to the Toolbox system.  The email chain included:

From: Kylie Neal [mailto:kylie@dreamdesk.com.au]

Sent: Thursday, 8 September 2016 4:12 PM

To: Michelle Page <mpage@bigginscott.com.au>

Cc: David Semmens <david@dreamdesk.com.au>; Paul Stoner <pstoner@bigginscott.com.au>

Subject: Re: MVI (Box & Dice)

When offices have MVI turned on (in its current incarnation) OFIs [open for inspections] are entered into B+D and they sync to DD.

--------------------------------------------------------------------------------

On Thursday, September 8, 2016, Michelle Page <mpage@bigginscott.com.au> wrote:

OK – is that being set up in the new system?

--------------------------------------------------------------------------------

From: Kylie Neal [mailto:kylie@dreamdesk.com.au]

Sent: Thursday, 8 September 2016 4:19 PM

To: Michelle Page <mpage@bigginscott.com.au>

Cc: David Semmens <david@dreamdesk.com.au>; Paul Stoner <pstoner@bigginscott.com.au>

Subject: Re: MVI (Box & Dice)

Yes, but the first priority is to have offices able to place ads/orders. MVI is not guaranteed for day 1 but is a very early priority - Dave [I infer, Semmens] advises that it won’t be arduous to recreate, but the basics need to be available first. Happy to go through the plan/priorities if you wish.

On 9 September 2016, Mr Stoner sent an email to unnamed parties (although the recipients are likely to have included Mr Neil Pearson of Printco), with the subject line “structure”.  Printco was a printing business that printed display boards for Biggin & Scott.  It is likely that other recipients of the email were ABC (a display board company) and Mr Semmens.  The email included (paragraph numbering added):

[1] Hi Guys

[2] Proposed structure for new co

[3] Name AGENT TOOL BOX
Biggin & Scott
Printco
ABC
To own 70%
At a costs of $35,000 each

[4] David Seamans [sic] and partners 30%
At a costs of $30,000

[5] I think we need to be open to JV’s with larger groups along the lines of white labelling the system on a 50/50 basis
And also prepared to take on other investors should the need arise.

[6] We are currently sourcing a longer term for the platform 10 years at this stage so to be confirmed

[7] Where the team will sit is an issue as we cannot have one company being able to be see another’s pricing.
We need to agree on this and quick. David may have a solution.

[8] Our objective is to get the system finished with Biggin & Scott using it by not later than October 3rd 2016 stage one
As B&S are bringing in revenue this helps on a few levels but obviously part of start-up few is to help run the team until we pick up
A few new clients.

[9] Biggin & Scott are happy for others to see how their work flow is happening.

[10] Reasoning behind Printco and ABC being partners is two fold
Both have strong relationships with clients whilst at the same time can elevate some ongoing cost by introducing a system
Which covers full web to print capabilities, Boards, brochures, stationary, papers, edm’s, intranet.

[11] First year each partner of the 70% must bring in at least the equivalent of what Biggin & Scott brings in production fee wise.

[12] Obviously if close not a problem but I think we need a taking the piss rule. Should this not happen under p[er]forming partner must offer shares back.

[13] Printco and ABC get full access of the system to offer to their clients obviously.

[14] Paul Stoner and Michelle page [Bartels] available to help get deals across the line should it be needed.

[15] If in agreement let’s get this set up with the rules as above and go for it.

[16] Dave will have a system presentation ready for us next week.

[17] Cheers
Paul Stoner
Chief Executive Officer

[Biggin & Scott signature block]

Campaigntrack emphasised the following matters about the email, which I accept as accurate:

First, Mr Stoner was writing in his capacity as CEO of Biggin & Scott and as one of the prospective venturers: at [3], [17].

Secondly, Biggin & Scott and its partners (Printco and ABC) were to take a controlling 70% interest in the venture, while Mr Semmens and his partners were to take a minority 30% interest: at [3]-[4].

Thirdly, Mr Stoner’s and Biggin & Scott’s “objective” was to finish the Toolbox system and to have Biggin & Scott offices on the system by 3 October 2016 (at [8]), being the end-date of the “licence-back” to DDPL to use the DreamDesk system under the DreamDesk sale agreement.

Fourthly, Mr Stoner, Ms Bartels and Biggin & Scott were taking an active role to ensure the success of the Toolbox venture by: bringing in production fee revenue from Biggin & Scott offices (at [8], [11]); sharing information about usage of the Toolbox system by Biggin & Scott offices (at [9]); and Mr Stoner and Ms Bartels being available to persuade customers to move to the Toolbox system: at [14].

On 12 to 13 September 2016, Mr Wentao Zhang and Mr David Gallagher made their first commits to the Toolbox Git repository.  Mr Zhang is a software developer who was employed by Mr Meissner’s company, JGM Advertising, from 1 July 2016 to 6 October 2016.  His “team leader” was Mr Gallagher, a DDPL consultant, who also worked on the development of the Toolbox system.  Mr Zhang produced documents under subpoena.  According to time sheets which he produced, by at least 8 September 2016, Mr Zhang was working on the development of the Toolbox System which was referred to as “Dashboard”.  He continued working on the development of Toolbox until at least 3 February 2017.  Whilst Mr Gallagher and Mr Zhang helped develop the software, Mr Semmens described himself as the “main developer” of the Toolbox system.

On 14 September 2016, Ms Bartels met with Ms Keys and Mr Dean of Campaigntrack in South Yarra.  Ms Bartels showed Ms Keys and Mr Dean various functions and features of the DreamDesk system which she considered valuable, in particular the Electronic Data Management (EDM) function which was not a part of the Campaigntrack system.  In her affidavit, Ms Bartels stated she did this “in the hope that [Campaigntrack] would keep [DreamDesk] alive for Biggin & Scott so we did not ultimately have to go down the track of launching a new system”.  Ms Bartels asked Ms Keys not to shut down DreamDesk and stated that she recalled Ms Keys stating that Campaigntrack did not “want to interrupt your business but we will shut DreamDesk down”.  I think it unlikely that, by this time, Ms Bartels did not want to launch the Toolbox system which was in the process of being developed.

According to Ms Keys, Ms Bartels said words to the following effect at the meeting:

Everything is pretty much set for Biggin and Scott to come back to Campaigntrack. The only issue is whether Campaigntrack could accommodate having an intranet feature? … I just need some time to go over the contract. I think that, at this point, it is just a matter of going through the contract and finalising the pricing. I also need reassurance that we keep the intranet page. … You have been great for not shutting [DreamDesk] down immediately.

I prefer Ms Keys account of the meeting.  It is more likely in the context of the established surrounding circumstances.

RETB was incorporated on 15 September 2016.  Mr Stoner became its sole director and 95% shareholder.  Ms Bartels became its sole company secretary and 5% shareholder.

The Toolbox venture was operated by a trust (RETB Unit Trust), for which RETB was the corporate trustee.  The RETB Unit Trust was established on 1 October 2016.

Mr Stoner confirmed that Mr Pearson or Printco made a $35,000 investment into the Toolbox venture.  It is likely that Biggin & Scott and ABC also invested in the Toolbox venture.

By mid-September 2016, Campaigntrack had not yet received the passwords it needed to operate the DreamDesk software.  Those had been requested on 7 September 2016 – see [83] above.  Mr Meissner was on a cruise ship in Alaska from 6 to 19 September 2016 and Campaigntrack had difficulty getting in contact with him.  On 16 September 2016, Ms Neal from DDPL sent the following email to Ms Keys regarding Mr Meissner’s whereabouts:

Hi Therese,

Just an update regarding Jon’s whereabouts.

Dave said that you are anxiously awaiting contact from Jon. He’s on a cruise ship in Alaska at the moment, and incommunicado.

He’ll be back on dry land Sunday/Monday [18/19 September 2016] if you email him I’m sure he will be in touch then.

If I can assist with anything in the meantime please let me know.

Mr Meissner gave evidence that before he left on his trip, he left Ms Neal and Mr Semmens in charge of turning the DreamDesk system off and giving it to Campaigntrack and negotiating the terms of any extension of the licence to use DreamDesk.  Campaigntrack submitted that it should be inferred that Mr Meissner, Ms Neal and Mr Semmens deliberately delayed the handover process for two weeks, for the purpose of maximising the time to develop the Toolbox system and to seek to remove traces of the DreamDesk system from the Toolbox system.

Ms Neal’s email of 16 September 2016 to Ms Keys is odd.  As noted earlier, on 1 September 2016, Ms Neal had sent an email saying she was “cc[-ing]: Jon” and the cc-ed email address was “accountservices9999@yahoo.com”.  On 16 September 2016, Mr Meissner sent an email received by Mr Watts from the email address “accountservices9999@yahoo.com” saying he was sending the email from the account of “an Aussie resident of the US” whom he had met on the cruise and that it was not his email address.  The email stated:

Sorry everyone

Since sept 6 I have been off the air ie phone and Internet wise

What they told me about ships was incorrect nothing works

I am back in Chicago on Monday and hopefully will be able to respond to any emails messages I have received

I am lucky to have met an Aussie resident of the US who has let me send this email on her account

Do not respond as it obviously is not my email address

Jon

I accept that Mr Meissner had difficulties being contacted whilst overseas.  However, I conclude that Mr Meissner could have been contacted on 16 September 2016 by email.

On 21 September 2016, Mr Stoner emailed Ms Keys (Campaigntrack), copying Mr Meissner and Ms Bartels, stating that he was concerned that DreamDesk would be shut off (paragraph numbering added, typographical errors in original):

[1] Dear Therese [Keys], Tim [Dean] and Jon [Meissner]

[2] I am writing this email in the hope that we can all sort something out with regards to the Biggin & Scott group and the current situation we find our selves in after CT and Active pipe taking over or selling Dream Desk which as of today I am not [too] sure which it is.

[3] A conversation had on Monday of this week [19 September] with Tim and Therese has made me extremely nervous and concerned that either the system will be turned off or Dream Desk staff will be no longer after the 3rd of October 2016.

[4] I feel that I need to put forward my situation as simply a client using a system that has been taken over or in the process of being taken over.

[5] To date we have been happy to have conversations with respect to considering CT as our web to print solution but am extremely worried about the level of increased charges.
Currently we are able to achieve through Dream Desk a level of production fees that we and our offices believe are fair for us and our suppliers, should we move forward with CT on current increases

$12 per page delivery fee for print of our ABODE magazine that does not currently exist

$15 per board order file delivery that does not currently exist

10% or $20 per print file delivery that does not currently exist

Which ever way I look at it the CT (campaign track) contract will increase our productions fees per property or across the board by 50-70% once the cost are passed on.

[6] During our meeting at RT EDGAR it was mentioned that you would handle this matter as good corporate citizens which as mentioned earlier in the week I have relied on.

[7] We also discussed the delicate timing being during our busiest time of the year which is extremely concerning to me. All rumours put forward to date are in accurate but again I ask you to understand how big a deal this is to have 34 offices change during the busiest time of the year-- this I am struggling with personally.

[8] When I consider the above increases it causes me a great deal of stress, as to position these cost with our offices would take time which we simply do not have and to say no results in Dream desk being turned off leaving Biggin & Scott with out a web to print system at the busiest time of the year with little to no warning or time to make other arrangements.

[9] At this stage we are very seriously considering going manual with suppliers help and a Mac operator in our office as we simply do not have the time or feel that we will be given time to work this out.

[10] I ask in good faith that we be given some normal or standard terms to exit Dream Desk maybe as per CT contract terms 90 days.

[11] In simple terms we are a customer of a system that has been bought by CT to close down to protect its position and I feel we need to be given some time. We are not your enemy just realestate agents using a system.

[12] As you will see above I have copied in our solicitors Mills Oakley whom are aware of the contracts and will be involved should Biggin & Scott fall victim to any thing that may damage our business through no fault of ours.

The applicant emphasised the following aspects of this communication:

First, Mr Stoner was seeking to convey the impression that Campaigntrack was putting Biggin & Scott in a difficult position commercially and that, if Campaigntrack turned the system off on 3 October 2016, Biggin & Scott had little option but to “go manual”: at [7]-[9].

Secondly, Mr Stoner did not refer to the 3-month contractual notice period under the Biggin & Scott – DDPL Agreement dated 20 May 2015: cf [10].  Instead, Mr Stoner sought to exit on Campaigntrack’s terms: at [10].  This was despite Mills Oakley, who were “aware of the contracts”, being copied to the email: at [12].  Mr Stoner’s failure to refer to the Biggin &Scott – DDPL Agreement was submitted to be inconsistent with the reliance in these proceedings by the represented respondents on that agreement as justifying the migration of the data from DreamDesk.

Thirdly, Mr Stoner was seeking to convey the impression that he was a mere customer of the DreamDesk system, not a key venturer in the development of a competing system: at [11].

As to these matters:

I accept that Mr Stoner sought to convey the impression contended and that this was not accurate because Mr Stoner considered that he would likely have available a competing system which, even if not fully functional, would be sufficiently operational to avoid “going manual”.

I do not regard the failure to mention the Biggin & Scott – DDPL Agreement as significant.  That agreement provided for a notice of period of 3 months if either party wished to bring the contractual arrangement between them to an end.  It also provided that, if DDPL chose to cease to do business with Biggin & Scott as a group, migration of all templates and property related data was to be made available to whomever Biggin & Scott instructed.  There was no express time limit with respect to migration of data.  I do not regard it is as surprising that Mr Stoner did not rely on the term about 3 months’ notice with respect to use of the system as a whole, which is different to DDPL permitting migration of data.

I accept that Mr Stoner’s communication did not convey that he was, together with others, developing a competing system and that his comments to Campaigntrack were intended to convey that his interests were more confined than they really were.

It was put to Mr Stoner that the purpose of his 21 September 2016 email was to “buy time” for Biggin & Scott until the Toolbox system became operational, a proposition which Mr Stoner denied:

… You were looking to build your own system and you were trying to buy time with Campaigntrack until you knew that the system was going to be operational?---Your opinion.

I’m putting that to you, Mr Stoner?---No.

Despite Mr Stoner’s evidence, it is probable that at least one of the purposes of the email was to “buy time” and it is likely that the time was being sought in order to further develop, or complete the development of, the Toolbox system.

Mr Meissner emailed Ms Keys and Mr Dean on 22 September 2016 stating:

I have been copied in on emails from Paul re our current predicament

Without making judgements or entering into discussions on the

Correctness of statements can I request the following

We would like an extension of 4 weeks to use the platform and would request you to indicate a fee payable now that RT Edgar is no longer using the platform and it would appear that CT has already had discussions with Jellis Craig in relation to ongoing services, which we at Dream Desk are unaware of

We initially agreed to $5000 per month when we were dealing with all clients

I await your response

Jon

Also on 22 September 2016, Mr Semmens provided Ms Keys with access to the cloud service on which the DreamDesk virtual server was stored.  Mr Allen gave evidence that the migration scripts – which had last been run on 19 September 2016 – had been deleted from this virtual server, indicating that, at some time between 19 and 22 September 2016, Mr Semmens deleted the migration scripts from the DreamDesk system.

## B.11  Campaigntrack and New Litho learn about Toolbox

On the evening of the 22 September 2016, Mr Watts discovered that RETB had been incorporated, that the domain realestatetoolbox.com.au was registered in RETB’s name, that the domain realestatetoolbox.com.au resolved to the IP address 54.206.72.241 and that when that IP address was entered into a browser, it resolved to a login page for the DreamDesk system.  Mr Watts sent screenshots of the realestatetoobox.com.au website to Ms Keys, Mr Timm (a director and the chief technology officer of Campaigntrack) and Mr Dean.

On 23 September 2016, Mr Timm asked Mr Allen to investigate and work out if there was any code in the Toolbox system that had been copied from the DreamDesk system.  Having discovered the “dash.vault1.net” domain in the migration scripts, Mr Allen entered dash.vault1.net into an internet browser.  It resolved to a webpage for the Toolbox system.  Mr Allen then confirmed that both realestatetoolbox.com.au and dash.vault1.net resolved to the same IP address (54.206.72.241).  Based on these “commonalities” and his experience as a computer programmer and software developer, Mr Allen concluded that, unless a proxy re-direction server or IP load balancer was being used, on 23 September 2016, the DreamDesk system and the Toolbox system were being run on the same computer, namely, the computer at the IP address 54.206.72.241.  I conclude that the DreamDesk system and the Toolbox system were being run on the same computer.  I infer that the computer was Mr Semmens’ computer.

On 26 September 2016, Mr Stoner emailed Ms Keys and Mr Meissner, advising that Biggin & Scott would not be entering into a contract with Campaigntrack, asking for four weeks before Biggin & Scott’s access to DreamDesk was cut off, and requesting Campaigntrack’s “help with the transition”:

Dear Therese [Keys] and Jon [Meissner]

As requested we have been in discussions with Campaign Track since being notified that Campaign Track had bought Dream Desk, last week we decided that due to the increases in production fees for ourselves and our suppliers we would not be entering into a contract with Campaign Track at this stage.

Biggin & Scott wish to give 4 weeks’ notice effective from today 26th September making the 24th October 2016 our last day with Dream desk with regards to our web to print solution.

Your help with the transition would be much appreciated.

Mr Meissner replied to Mr Stoner, cc-ing in Ms Keys:

Paul

I understand your decision, but am sorry that it has come to this.

Unfortunately the decision, re an extension, is not ours to make, and I have already asked Campaign Track to extend our Licence of the system until the end of October ie October 27th.

I await CT decision.

I will advise ASAP when we receive notification.

Once again can I take this opportunity to sincerely apologise for the mess we have placed the Biggin & Scott network in.

Mr Meissner gave evidence that, on 26 September 2016, he received a phone call from Ms Keys in which she asked questions including “Why doesn’t Campaigntrack have access to the Dreamdesk system?” and “Why doesn’t Campaigntrack have access to the Biggin & Scott data?”.

After speaking to Ms Neal and Mr Semmens, Mr Meissner sent a text to Ms Keys saying: first, that he had “instructed Kylie and David to fix the access this morning”; and, secondly, “[o]bviously client data is not ours so cannot be shared by CT with others as agreed”.

On 27 September 2016, Ms Keys responded by email, deferring to their lawyers’ advice and stating that Campaigntrack still had “not received the Amazon web server”.  Mr Meissner responded:

In all our emails

You have requested access to live sight

Which I arranged yesterday urgently

I did not know til now that you had not got Amazon access

I will get David to provide first thing Tommorrow [sic]

I am not playing games but as I am overseas and having to rely on others to carry out my wishes I can only assume that my wishes are carried out to the letter

I will fix this again finally in the morning.

On 27 September 2016, Mr Stoner repeated his request for DreamDesk to be kept live for four weeks:

Dear Therese and Jon

I am yet to hear from you with respect to the below email, but believe Jon has asked for an extension.

I was also very interested to hear from Jellis Craig today during a meeting that they will be continuing with the DREAM DESK system with no interruption.

I repeat Biggin & Scott acted in good faith during our discussions believing we could come to an agreement and have not received notice at any stage from either DREAM DESK or Campaign Track that the system will be turned off or not available.

So again we ask that we be given 4 weeks to make other arrangements. 24th October 2016.

On 28 September 2016, Mr Allen had a phone call with Mr Semmens, during which Mr Allen asked for the DreamDesk Git repository.  Mr Semmens at first told Mr Allen that they did not have a Git repository, but eventually gave Mr Allen access to the DreamDesk Git repository (the DreakDesk Git Repository).  Mr Allen gave evidence that there were certain commits and branches that had been deleted from the DreakDesk Git Repository.  Mr Semmens stated that he could not remember if he had deleted the commits and branches, but that he did remember having conversations with Mr Gallagher regarding removing some of the files and passwords to which they did not want Campaigntrack to have access.  I conclude that Mr Semmens did delete certain commits and branches from the DreakDesk Git Repository.

Mr Semmens said the reason why the commits and branches were deleted was because “there’s files in there that were irrelevant that I didn’t want [Campaigntrack] having, there’s passwords, there was scripts in there with, you know, passwords that linked to other servers I didn’t want them to have”.

The DreakDesk Git Repository was related to the DreamDesk system.  The deleted branches in the DreakDesk Git Repository were named “live” and “Development”.  I infer that the deleted branches contained commits relating to “live” and “development” versions of the DreamDesk system or the Toolbox system.

In cross-examination, Mr Semmens said:

You know that in these proceedings, an important question which his Honour needs to decide is when certain things occurred in terms of software development, do you agree with that proposition?---I do.

And of critical importance to that would be just – would be the use of a repository with times and timestamps on it that would tell you when certain events occurred, and certain developments took place. Do you agree with that?---Yes, I do.

… I am asking you about you agreeing with the proposition I put to you, which is – [that it] was next to impossible, very difficult or next to impossible, to work out when certain things occurred absent a reliable repository?---Yes, without it, yes, it would be difficult. Virtually impossible.

Well, it would be not just difficult, it would be next to impossible, wouldn’t it?---Yes.

I accept that Mr Semmens’ deletions of commits and branches from the DreakDesk Git Repository made it “virtually impossible” for Campaigntrack to prove when certain things occurred, in particular various development pathways of the DreamDesk system.

Campaigntrack’s case was that the DreamDesk system was copied and then progressively modified in an endeavour for it not to be possible (or for it to be difficult) to establish that the new system was one which had been created by first copying DreamDesk.

## B.12  30 September to October 2016: Copying of files from DreamDesk system; preparation for DreamDesk being shut off

On 30 September 2016, Mr Semmens first committed a computer program named “SyncController” to the Toolbox Git repository.  The SyncController facilitated the copying of records from certain tables in the DreamDesk database for Biggin & Scott to corresponding target tables in the Toolbox Git repository.  Mr Semmens committed further versions of SyncController to the Toolbox Git repository on 5 October and 11 October 2016.

SyncController operated, in effect, like the migration scripts, except that it resided in the Toolbox system rather than in the DreamDesk system.

On 3 October 2016, Biggin & Scott, through its solicitors Mills Oakley, asked Campaigntrack for an extension of the DreamDesk licence until 17 October 2016.  Mills Oakley stated that Biggin & Scott confirmed it was willing to provide to Campaigntrack certain undertakings.

On 3 October 2016, Mr Allen found evidence of RSYNC commands being run on the production server of the DreamDesk system.  An RSYNC command is a command to copy files from one location to another.  The production server is the server used to provide the DreamDesk system to customers.

On 4 October 2016, Mr Allen installed a software named “sudoreplay” on the production server of the DreamDesk system, to record and allow playback of a user’s activity on the server.  The videos logged by the sudoreplay software showed:

on 5 October 2016, the running of an RSYNC command for files in a sub-folder “images”, found in a sub-folder for Whitford Property.  Whitford Property was a real estate agency operating in Victoria;

on 5 October 2016, the running of an RSYNC command for files in a sub-folder for Biggin & Scott;

on 6 October 2016, the running of an RSYNC command for files in a sub-folder “images”, found in a Biggin & Scott subfolder; and

on 10 October 2016, the running of an RSYNC command for files in a sub-folder “approved”, found in a Biggin & Scott subfolder.

All of the above RSYNC commands copied files to an identified target folder, which included the word “toolbox”, at an identical IP address.  In cross-examination, Mr Semmens stated that he ran the RSYNC commands.

Mr Semmens was also asked whether he had any right to copy Whitford Property’s files:

Do you accept that you didn’t have any right to transfer the files of Whitford Property at the time at which you transferred it on 5 October 2016?---That was a client of Print Co’s, which I just took a copy of so we had – if they ever asked for it, simply - - -

You accept, don’t you, that you had no entitlement from anyone to take that data?---Well, I was – again, it would have been ..... the dates of this. But once being told to synchronise all the client data or make sure it’s available for the client, I wouldn’t have thought it was an issue.

As to this cross-examination and as noted below, in an email to someone at Biggin & Scott on 5 October 2016, Mr Semmens wrote: “Also I will be [sic] setup whitford tonight so we can give printco access”.

The sudoreplay videos also captured the deletion, on 5 and 6 October 2016, of the RSYNC commands from the bash history on the production server of the DreamDesk system.  The bash history stores the history of user commands entered at the command prompt.  The command to access the bash history was also deleted.  Mr Semmens confirmed in cross-examination that he was the one who deleted commands from the bash history.

Campaigntrack submitted that it should be inferred that Ms Bartels on behalf of Biggin & Scott instructed Mr Semmens to delete RSYNC commands from the DreamDesk system, so Campaigntrack would not suspect Biggin & Scott was not returning to Campaigntrack’s system.  I do not draw that inference.  I accept that Mr Semmens did not want Campaigntrack to know what he had done, but I do not accept that he had received any instruction in that respect from Ms Bartels.

On 5 October 2016, Campaigntrack’s solicitors emailed a document headed “Undertaking as to use of IP of Dream Desk” to Mr Meissner.  The proposed undertaking was in the following terms:

Dream Desk, Meissner and Semmins [sic] undertake and agree that they individually or jointly with any other person or entity will not use, market, sell, copy, duplicate or in any way enable or facilitate the development of any system by making use of any of the intellectual property which comprises and/or relates to the system of Dream Desk, which is now owned by Campaigntrack Pty Ltd to the extent that they will not permit, now or at any time in the future, access by any third party to the system known as Dream Desk for any use other than its ordinary permissible use.

Dream Desk, Meissner and Semmins [sic] also undertake and agree that they will immediately cause to be returned to Campaigntract [sic] Pty Ltd, or if unable to be returned then destroyed so as to render useless, any of Dream Desks[’] intellectual property or code which has already been copied, duplicated or otherwise provided to any third party or entity of any description whatsoever.

Mr Meissner replied to Campaigntrack’s solicitors on the same day.  Mr Meissner’s email included:

I agree to all re Meissner,

but have no authority, nor was it part of any previous discussion, in relation to David Semmins [sic].

Semmins [sic] never owned the IP, and never has used it unless under Dream Desk authority.

The Dream Desk IP was sold to CT and as such no part can, or ever was used, by others.

As of the cutoff time no part of the IP has been used, copied etc in any other process.

As discussed I am overseas and cannot print or sign any Documents and as such this email should be used as my acceptance on Meissner and Dream Desk matters.

Also I presume the $5000 fee is monthly and only a % will be payable for October

Later in the evening on 5 October 2016, Campaigntrack’s solicitor sent a draft undertaking to Mills Oakley.  The draft undertaking was in the same form as that sent to Mr Meissner, except that it was required to be executed by Biggin & Scott, RETB, Mr Stoner and Ms Bartels.  The covering email from Campaigntrack’s solicitor stated:

We are instructed to provide you with the attached undertaking for your consideration. We understand that your client has made a request to extend our clients grant of a licence to access to Dream Desk.

Firstly, we are instructed that our client is willing to afford an extension on the basis of receiving undertakings from Dream Desk Pty Ltd and associated persons as well as seeking the attached undertaking from your client and associated persons and entities. Our client has made a similar request of Dream Desk Pty Ltd. While Dream Desk Pty Ltd and Mr Meissner have agreed to the undertaking, Mr Meissner has indicated that Dream Desk Pty Ltd will cease providing access to its web to print clients from midnight on 10 October 2016. Our client has made no such stipulation. Our client has requested payment of the licence fee and the undertakings to be provided.

In the circumstances, we ask that you confirm that your clients and associated persons and entities are willing to provide undertakings in the form of the attached?

As outlined in the email from Campaigntrack’s solicitor, the offer of the extension of the licence was conditioned on the receipt of the undertakings from DDPL and “associated persons” and Biggin & Scott and “associated persons and entities”.  The offer did not name Mr Semmens, nor any of the other contractors or employees of DDPL.

Mr Stoner and Ms Bartels signed the undertaking on behalf of Biggin & Scott, RETB and themselves on 6 October 2016.  Mr Stoner gave evidence that he was not aware that Mr Semmens had also been asked to give an undertaking.  It was Mr Stoner’s understanding that, by giving the undertaking, Biggin & Scott would be granted an extension of the licence to access DreamDesk until 17 October 2016.

Mr Semmens did not sign the undertaking requested of him.  He gave the following evidence in cross-examination:

Were you told by anyone not to give the undertaking, Mr Semmens?---No.

You were not?---No.

That’s your truthful evidence?---Yes.

You didn’t have a discussion with Mr Stoner about giving an undertaking after he sent an email to you on 6 October 2016 at 9.43 am?---We – possibly we discussed it, but I wouldn’t have – yes, I wouldn’t have signed it because it was, you know, restricting my work. The undertaking that I read pretty much restricted me from working in the industry, so I was never going to sign it.

Which undertaking are you referring to, Mr Semmens?---The one that Therese [Keys] sent me.

When was the last time you read that undertaking, Mr Semmens?---A long time ago. Well, sorry, I should say that’s the way I interpreted it, I did not want to sign it, I didn’t want to have any restrictions.

Do you accept that if the undertaking didn’t do that then you’re mistaken in your recollection?---I’m not mistaken, my recollection is what I said.

All right. Sorry, your Honour, I just have to – we will just find the undertaking, Mr Semmens, just bear with me for a moment. And I should say for the benefit of ..... the undertaking which was sought from this witness, of course. We’re just looking for it at the moment, I will continue?---Regardless of what it said; if it was from Campaigntrack, I would not have signed it, simple as that.

And why is that, Mr Semmens?---Because they are the most deceptive, evil company I’ve ever come across in my entire life.

On 5 to 6 October 2016, Ms Neal and Mr Semmens exchanged emails with the subject “Re: Today”.  At least one email in the chain was copied to Mr Meissner and persons at DDPL and JGM Advertising.  Mr Stoner and Ms Bartels were also copied.  In an email copied to Mr Meissner on 6 October 2016, Ms Neal asked Mr Semmens:

Also re endpoint, there will only be one for realestatetoolbox so does it matter that the one you’ve given is for the bs subdomain?

Campaigntrack submitted that this email chain, taken with the previous emails received by Mr Meissner and with the number of Mr Meissner’s staff involved in the development of Toolbox suggest that Mr Meissner was aware of, and involved in, Biggin & Scott’s transition away from DreamDesk.  I accept that Mr Meissner was aware that Biggin & Scott was not intending to agree to use the system offered by Campaigntrack and that it was developing its own system.

The email chain “Re: Today” also included the following email sent by Mr Semmens:

On Wednesday, October 5, 2016, David Semmens <david@dreamdesk.com.au> wrote:

Great thanks

…

Working On OFIs at the moment

Wendy is just playing with it I gave her a quick run through

Also I will be setup [sic] whitford tonight so we can give printco access

new MVI endpoint api.realestatetoolbox.com.au

if B&D can change after 5pm Friday

Campaigntrack submitted, and I accept, that Mr Semmens’ statement that he “will … setup whitford tonight” should be understood as referring to the running of the RSYNC command for Whitford Property.

Campaigntrack also submitted, and I also accept, that Mr Semmens’ statement in the “Re: Today” email chain that he was “Working On OFIs [open for inspections] at the moment” should be taken as a reference to the SyncController committed to the Toolbox Git repository by Mr Semmens on the same day.  Mr Semmens had added a “syncOFIs” function which, if executed, deleted all records of the “ofis” table of the Toolbox database, and copied all records of the “ofi” table in the DreamDesk database for Biggin & Scott to the “ofis” table of the Toolbox database.

On around 6 October 2016, Ms Bartels created artwork for different advertising materials, working from about 8pm to around 3am to 4am, because she was concerned to ensure that, if access to DreamDesk was shut off, then something could be up and running with Biggin & Scott’s artwork within minutes:

On 7 October 2016, Ms Bartels sent an email to Mr Semmens, copied to Mr Stoner, with the subject line “tool box”.  The email stated:

Hi Dave

See you Monday (I will bring my drive and then you can show me how to allocate templates)

How did you go with brochures today?

I will put all templates onto Drop Box and share them [with] you

How did Ian go with Mail cards today?

Box & Dice will let me know Monday re: MVI

What about OFI’s?

I will let offices know Tuesday afternoon what is happening

I will let offices know Tuesday afternoon to order stationery now

I will speak with your contact re: Stationery set up

Have a great weekend

The “Ian” referred to in this email was Mr Ian Adams, an employee at Mr Meissner’s company JGM Advertising.

In cross-examination, Ms Bartels confirmed that the stationary set-up referred to in the above email referred to a printer “who was located across the road from where Real Estate Tool Box or where Dream Desk was operating in Mulgrave”.  Campaigntrack submitted that according to its company search, RETB has never had a principal place of business in Mulgrave, whereas DDPL’s principal place of business has always been in Mulgrave.  Campaigntrack submitted, and I accept, that I should infer from this statement together with the other facts referred to earlier that the Toolbox system was developed within DDPL’s offices in Mulgrave.

On 7 October 2016, Campaigntrack’s solicitor sent an email to Mills Oakley indicating there had been problems with procuring one party (namely, Mr Semmens) to sign the undertaking referred to at [129] above.  The email included:

I confirm that I am presently seeking instructions from my client with regard to the extension. While an undertaking has been requested to be provided by Mr Meissner and other parties, Mr Meissner has not yet procured one party to sign the undertaking requested. Further, payment of the licence fee has been requested and at the present time, we are unaware of any payment having been received.

We will keep you informed of progress in relation to the above. In the meantime, we have been asked by our client to enquire what system your client is moving over to. The purpose of that request is in order for our client to gauge whether there would be any possible reasons for the resistance to the provision of the undertaking requested.

Approximately three hours later, Campaigntrack’s solicitors wrote to Mills Oakley, confirming that the DreamDesk licence would not be extended beyond 10 October 2016.  The email included:

I am writing to confirm that based on our present instructions the licence for Dream Desk will not be extended beyond 10 October 2016. The reasons for this are that:

1. 	Our client has not received an undertaking executed by David Semmins [sic];

2. 	Our client has not received payment for the licence fee either for the full month or for any lesser period, which in any event had not been agreed; and

3. 	We have not received any indication directly from Mr Meissner that he has an intention contrary to the position previously stated that is that Dream Desk would be shut down on 10 October 2016.

Our client made clear to Mr Meissner the basis upon which the extension of the licence would be granted and our clients requests have not been complied with. All of the above matters are matters which are beyond our clients control and accordingly have led to the decision set out above.

On 10 October 2016, Ms Neal sent an email to Mr Ben White of Bambra Press, a printing business, with the subject line “Test file”:

Hi Ben,

Michelle [Bartels] tells me that you’re up to speed with the demise of Dreamdesk and Biggin & Scott’s new W2P venture, Real Estate Toolbox.

We’re currently testing the Toolbox, with a view to cutting the offices over this week. (sssssshhh .... not everyone is aware yet)

We’re keen to make sure that the artwork we’re sending you is now print-ready, so would you mind taking a look at this - as a first example - and providing your feedback?

http://bs.realestatetoolbox.com.au//storage/8537/production/43637.pdf

Thanks very much for your help, and give me a call if you have any questions.

In the evening of 10 October 2016, Biggin & Scott’s access to DreamDesk was cut off.  That evening, Ms Bartels sent an email to all users of the DreamDesk system at Biggin & Scott offices with the subject line “Dream Desk has been shut down by Campaign Track”.  The email stated:

Hi All

All Directors have been advised by Paul Stoner and below is notification of Dream Desk Web to Print solution which has been shut down without notice tonight.

3 weeks ago we became aware that Campaign Track had aggressively tracked down the owner of a piece of IP in the Dream Desk web to print solution and bought it off them for a large sum of money. The purchase was made with one intention, to shut down Dream Desk as a competitor.

We entered into negotiations with Campaign track which have now stopped due to a major increase in productions fees, not only for us but also our suppliers. One example was we would have to pay $12 per page production fee for the magazine, at this stage we stopped our negotiations and asked for time to exit the system. Another example was 20% or $20 dollars on every print order.

Things very quickly got legal with all kinds of threats and requests that we simply cannot agree to.

As of this morning we had another 7 days on dream desk after numerous legal letters back and forth but at the very last minute this afternoon Campaign Track turned the system off without notice.

Obviously we have had something being done in the back ground which will be sent through to you tonight or first thing in the morning. The new company is called Real Estate Tool Box with the same team and their phone number is [redacted]. We have managed to get most of the information across into the new system but tomorrow will tell.

Please be aware:

Biggin & Scott will never deal with Campaign Track or New Litho and arrangements will be put in place to restrict active pipe moving forward.

This is not the perfect situation but this gives you an idea of the type of business’s these people are running.

The Toolbox system went live on the same day.

On 11 October 2016, Mr Semmens added a modified “syncOFIs” function to the Toolbox Git repository which, when executed, deleted all records of the “ofis” table of the database at jgm.dreamdesk.com.au, and copied all records of the “ofis” table of the Toolbox database to the “ofis” table of the database at jgm.dreamdesk.com.au.  Campaigntrack was not previously aware of, and did not receive control of, the subdomain jgm.dreamdesk.com.au.  Campaigntrack submitted that given the name of subdomain “jgm.dreamdesk.com.au”, it should be inferred that Mr Semmens was running a copy of the DreamDesk system at jgm.dreamdesk.com.au; and that given the date on which the modified “syncOFIs” function was committed to the Toolbox Git repository, the purpose of the copy of the DreamDesk system was to generate PDF artwork containing OFI details after Campaigntrack had shut down Biggin & Scott’s access to the DreamDesk system.

I accept that this inference should be drawn.  It is supported by the fact that in the email chain on 8 September 2016 referred to at [84] above, Ms Neal wrote that, using integration with Box+Dice, OFI details are entered into the Box+Dice customer relationship management system, those details are synchronised to the DreamDesk system, and the same synchronisation was planned for the Toolbox system.  In the email chain of 5 and 6 October 2016 referred to at [135] to [137] above, Ms Bartels wrote that Mr Semmens had said that the Toolbox system’s integration with Box+Dice could be done by Friday 7 October 2016.  I accept that that Mr Semmens was running a copy of the DreamDesk system on 11 October 2016.

Campaigntrack shut the DreamDesk system down completely by the end of October 2016.

## B.13  November 2016 to May 2017: Modification of DreamDesk files

In November 2016, the parties agreed that an independent forensic IT expert, Mr Geri, would inspect the Toolbox system and report on whether there was any potential copying from the DreamDesk system.

On 24 November 2016, in response to Mr Geri’s request for “[a] copy or access to the GitHub repository which is responsible for the log of all changes made to the development of Real Estate Toolbox”, Mills Oakley provided Campaigntrack’s solicitor with a commit log file, “git_commit_log.txt”.  The independent court appointed expert, Mr Taylor, later identified multiple differences between the Toolbox Git repository and the commit log file, git_commit_log.txt, including:

233 instances where the author name “David S <david@dreamdesk.com.au>” had been replaced with “David S <semkins74@gmail.com>”;

54 instances where the commit descriptions had been changed; and

five commit descriptions containing the word “rename” had been replaced with different descriptions.

In cross-examination, Mr Stoner gave evidence that he told Mr Semmens that he did not want DreamDesk “mentioned in anything” and that he did not give instructions to tamper with the commit log file:

You’re aware, in broad terms, that Mr Allen says that the commit log subtext git_log_commit.txt file is – doesn’t correspond with the Git repository?---I’m aware of those words, yes.

Did you have a conversation with Mr Semmens in which he told you that he made changes to that document?---I – I do recall, when all of this happened, I gave clear instructions to David to remove any mention of Dream Desk. And, I think, he removed his Dream Desk credentials, is my understanding.

So the evidence you give is that you told Mr Semmens before handing over the git_committ_log.txt file to Mills Oakley to provide to Ms McLean, to make a change to his credentials, the information in that file?---No. No. That’s not it, at all. When – David was building the system, I made very clear, I didn’t want Dream Desk mentioned in anything.

…

So if the git – if the git repository had information showing Dream Desk and the git_commit_log.txt file had been changed to semmkins74@gmail.com, you – that was something that you asked David – Mr Semmens, to change?---I – I didn’t ask him to change it but he let me know that he had changed it because he had the email address in there of Dream Desk.

Campaigntrack submitted that the changes were made by Mr Semmens to convey a false impression that Mr Semmens worked on the development of the Toolbox system in his private capacity, unrelated to his role at DDPL (amending the author names), and that the Toolbox system was independently created, as opposed to being based on the DreamDesk system (amending the “rename” commits).  Campaigntrack submitted that the Court should conclude that this was done on Mr Stoner’s, Biggin & Scott’s and RETB’s instructions.  I conclude that Mr Stoner and Biggin & Scott did not want Toolbox to be based in any way on intellectual property related to DreamDesk and did not want there to be any argument that it was so related or references to DreamDesk from which such an argument could be made.  It was for that reason that Mr Stoner did not want DreamDesk to be “mentioned in anything”.  I conclude that Mr Semmens realised that there was mention of DreamDesk, or some similar description, in the Toolbox system which he wished to conceal.  I do not conclude that he took the steps identified earlier on the instruction of any other person.

I accept Mr Stoner’s evidence that he did not ask Mr Semmens to change the commit file.

By an email on 24 November 2016, Mills Oakley also provided Mr Geri with a zip file “app.zip”, in response to Mr Geri’s request for a copy of the code responsible for “front end” functionality.  The files in the “app.zip” folder were drawn from two different sources, dashboard.vault1.net and bs.realestatetoolbox.com.au.  Mr Semmens gave evidence in cross-examination that this was because he had shown Mr Geri multiple versions of the Toolbox system.  The applicant submitted that Mr Semmens’ motivation was in fact to “seek to create a false impression of the content” of Toolbox, and to conceal different versions of the Toolbox system in existence.

There was no suggestion in Mills Oakley’s covering email or covering letter that the “app.zip” file contained different versions of the Toolbox system.  Neither was there any suggestion to that effect in Mr Semmens’ first affidavit where he gave evidence about the creation of “app.zip”.  Nor did Mr Semmens give evidence in his first affidavit that he had shown different versions of the Toolbox system to Mr Geri during Mr Geri’s first inspection of Toolbox.

Between April to June 2017, Mr Semmens deleted his “semkins74@gmail.com” Bitbucket account.  He did not make a copy or backup of any data held in this Bitbucket account before he deleted it.  In his Expert Report, Mr Taylor stated that Mr Semmens had informed him that he had deleted the Bitbucket account in June 2017, after the commencement of the current proceedings.  In cross-examination, Mr Semmens stated that he deleted his Bitbucket account in late April 2017, before the commencement of the present proceedings.

On 16 May 2017, Mr Semmens sent the following email to Ms Keys:

As you know I have been contracted by Active Pipe to look after Jellis Craigs EDMs using the Dream Desk platform (Jellis Craig is the only Client using this)

This letter is asking me to

… immediately cease use of and access to any DreamDesk intellectual property;

… deliver up to [Campaigntrack] all copies of substantial parts of the DreamDesk intellectual property within [Mr Semmens’] possession, custody and control ensuring that no copy or duplicate is retained;

Unless I am advised by Campaign track to disregard the attached letter by the end of business today I will be shutting down that server and deleting any files, data and backups of the platform

The applicant submitted that Mr Semmens did, in fact, carry out his threat of “deleting any files, data and backups of the platform”: see [164] to [168] below.

## B.14  June 2018: RETB ceases to trade; REDHQ takes its place

RETB ceased to trade, and ceased to use the Toolbox system, in about June 2018.

Biggin & Scott began to use a new system in about April 2018, called Real Estate Digital HQ Pty Ltd (REDHQ).  Biggin & Scott, Ms Bartels and Mr Stoner’s family company all hold interests in REDHQ.  Mr Semmens is REDHQ’s chief technology officer.

## B.15  Early 2019: Mr Semmens’ failure to provide information to the independent expert

For the purposes of the preparation of Mr Taylor’s expert report, Mr Semmens provided Mr Taylor with a Microsoft Surface laptop, a generic desktop computer and his Amazon Web Services and “semkins74@gmail.com” gmail accounts.  Mr Semmens stated that he had discarded or overwritten any further computer systems used in the development of the DreamDesk and Toolbox systems.

On 27 May 2019, Mr Taylor searched for and forensically preserved emails from Mr Semmens’ “semkins74@gmail.com” email account, containing certain search terms.  Analysis of the preserved emails containing the word “toolbox” showed:

no emails in the period 4 May 2016 to 10 October 2016;

emails from realestatetoolbox.com.au from 11 October 2016.

Campaigntrack submitted that, in the circumstances, it should be inferred that Mr Semmens had deleted emails containing the word “toolbox” from his “semkins74@gmail.com” account in the period 4 May 2016 to 10 October 2016, that is, during the development of the Toolbox system.  I accept that inference should be drawn.

During Mr Taylor’s document gathering, Mr Semmens confirmed that he had used two different gmail accounts during the development of software in relation to this proceeding, “semkins74@gmail.com” and one other that he referred to as a “DreamDesk gmail account”, in respect of which he could no longer recall the login details.  At the hearing, Mr Semmens was able to access an email sent to the email account david@dreamdesk.com.au.  Campaigntrack submitted that it should be inferred that Mr Semmens deliberately withheld the “david@dreamdesk.com.au” email account from Mr Taylor, in order to prevent forensic preservation of emails in that account.

Given the evidence as a whole, I conclude that Mr Semmens altered or purposefully deleted some files and accounts, and disposed of computers, in order to prevent access to files by Campaigntrack through compulsory processes available to Campaigntrack in the present proceedings.

# C  COPYRIGHT INFRINGEMENT CLAIMS

## C.1	General principles

### C.1.1  Infringement

By reason of s 36(1) of the Copyright Act, copyright in a work is infringed by a person who is not the owner of the copyright if the person does any act “comprised in the copyright” without the licence of the owner of the copyright.  Section 36(1) provides:

Subject to this Act, the copyright in a literary, dramatic, musical or artistic work is infringed by a person who, not being the owner of the copyright, and without the licence of the owner of the copyright, does in Australia, or authorizes the doing in Australia of, any act comprised in the copyright.

Under s 13, an act comprised in the copyright in a literary work includes:

any act that the owner of the copyright has the exclusive right to do; and

the exclusive right to authorise a person to do that act.

Section 14(1)(a) provides that “a reference to the doing of an act in relation to a work … shall be read as including a reference to the doing of that act in relation to a substantial part of the work”.

Section 10 defines “literary work” as including:

(a)	a table, or compilation, expressed in words, figures or symbols; and

(b)	a computer program or compilation of computer programs.

A “computer program” is “a set of statements or instructions to be used directly or indirectly in a computer to bring about a certain result” – s 10(1) of the Copyright Act; see generally: Data Access Corporation v Powerflex Services Pty Ltd (1999) 202 CLR 1 at [34]-[36]; Dais Studio Pty Ltd v Bullet Creative Pty Ltd (2007) 165 FCR 92 at [36]; CA Inc v ISI Pty Ltd (2012) 201 FCR 23 at [140]-[141].

A literary work includes “a table, or compilation, expressed in words, figures or symbols”: s 10(1) of the Copyright Act.  However, copyright does not protect mere facts, ideas or information contained in a table or compilation.  As was said in IceTV Pty Ltd v Nine Network Australia Pty Ltd (2009) 239 CLR 458 at [28] (citations omitted):

Copyright does not protect facts or information.  Copyright protects the particular form of expression of the information, namely the words, figures and symbols in which the pieces of information are expressed, and the selection and arrangement of that information.  That facts are not protected is a crucial part of the balancing of competing policy considerations in copyright legislation.  The information/expression dichotomy, in copyright law, is rooted in considerations of social utility.  Copyright, being an exception to the law’s general abhorrence of monopolies, does not confer a monopoly on facts or information because to do so would impede the reading public’s access to and use of facts and information.  Copyright is not given to reward work distinct from the production of a particular form of expression.

An “artistic work” includes, relevantly, “a painting, sculpture, drawing, engraving or photograph, whether the work is of artistic quality or not”: s 10(1) of the Copyright Act.  Whether a work will be recognised as an artistic work as a drawing is highly fact-specific and the measure is whether the work has a visual rather than semiotic function: Elwood Clothing Pty Ltd v Cotton On Clothing Pty Ltd (2008) 172 FCR 580 at [50]; see also [53]-[55], [57], [60]-[62] (Lindgren, Goldberg and Bennett JJ).

### C.1.2  Subsistence and originality

Section 32 of the Copyright Act provides for when copyright subsists in an original work.  It draws a distinction between unpublished and published works:

32  Original works in which copyright subsists

(1) 	Subject to this Act, copyright subsists in an original literary, dramatic, musical or artistic work that is unpublished and of which the author:

(a) 	was a qualified person at the time when the work was made; or

(b)	if the making of the work extended over a period—was a qualified person for a substantial part of that period.

(2) 	Subject to this Act, where an original literary, dramatic, musical or artistic work has been published:

(a)  	copyright subsists in the work; or

(b)  	if copyright in the work subsisted immediately before its first publication—copyright continues to subsist in the work;

if, but only if:

(c)  	the first publication of the work took place in Australia;

(d)  	the author of the work was a qualified person at the time when the work was first published; or

(e)  	the author died before that time but was a qualified person immediately before his or her death.

(3)  	Notwithstanding the last preceding subsection but subject to the remaining provisions of this Act, copyright subsists in:

(a)  	an original artistic work that is a building situated in Australia; or

(b)  	an original artistic work that is attached to, or forms part of, such a building.

(4)  	In this section, qualified person means an Australian citizen or a person resident in Australia.

The various matters to which s 32 direct attention are important to the determination of whether there has been infringement, notwithstanding that there might be a general admission of subsistence.  As Gummow, Hayne and Heydon JJ observed in IceTV at [105]:

A generally expressed admission or concession by one party to an infringement action of subsistence of and title to copyright may not overcome the need for attention to these requirements when dealing with the issues immediately in dispute in that action.  This litigation provides an example.  The exclusive rights comprised in the copyright in an original work subsist by reason of the relevant fixation of the original work of the author in a material form.  To proceed without identifying the work in suit and without informing the inquiry by identifying the author and the relevant time of making or first publication, may cause the formulation of the issues presented to the court to go awry.

Originality was explained in IceTV at [33] by French CJ, Crennan and Kiefel JJ as meaning that the work originated with an author, that it was not merely copied from another work and that its creation involved some independent intellectual effort.  Their Honours said (emphasis in original, citations omitted):

… Originality for this purpose requires that the literary work in question originated with the author and that it was not merely copied from another work.  It is the author or joint authors who bring into existence the work protected by the Act.  In that context, originality means that the creation (ie the production) of the work required some independent intellectual effort, but neither literary merit nor novelty or inventiveness as required in patent law.

Gummow, Hayne and Heydon JJ noted that copyright requires that the literary or artistic work originate with a human author (IceTV at [98]); see also Telstra Corporation Ltd v Phone Directories Company Pty Ltd (2010) 194 FCR 142) and stated at [99] (citations omitted):

Where a literary work is brought into such existence by the efforts of more than one individual, it will be a question of fact and degree which one or more of them have expended sufficient effort of a literary nature to be considered an author of that work within the meaning of the Act.  If the work be protected as a “compilation”, the author or authors will be those who gather or organise the collection of material and who select, order or arrange its fixation in material form.

The phrase “sufficient effort of a literary nature” in IceTV at [99] should not be understood differently from “some independent intellectual effort”: JR Consulting & Drafting Pty Ltd v Cummings (2016) 329 ALR 625 at [260].

The assessment of originality is done by reference to the whole of the identified work, and not identifiable elements within it, although there may be a separate issue as to whether identifiable elements within a larger work are themselves an “original work”: Coogi Australia Pty Ltd v Hysport International Pty Ltd (1998) 86 FCR 154 at 172.

### C.1.3  The exclusive rights

Section 31(1)(a) of the Copyright Act 1968 (Cth) provides that copyright in relation to a “work” is the exclusive right to do certain acts in relation to that work, including the right to reproduce it in a material form and to communicate the work to the public.  It includes:

31  Nature of copyright in original works

(1)	For the purposes of this Act, unless the contrary intention appears, copyright, in relation to a work, is the exclusive right:

(a)	in the case of a literary, dramatic or musical work, to do all or any of the following acts:

(i)	to reproduce the work in a material form;

…

(iv)	to communicate the work to the public …

## C.1.3.1  Reproduction

As noted, s 31(1) identifies the “exclusive rights” and includes the exclusive right to reproduce the work in a material form: s 31(1)(a)(i).  The term “material form” includes “any form (whether visible or not) of storage of the work, or a substantial part of the work or adaptation, (whether or not the work or adaptation, or a substantial part of the work or adaptation, can be reproduced)”: s 10(1).

Reproduction requires a sufficient degree of objective similarity between the copyright work and the alleged infringing work and some causal connection between their forms.  In SW Hart & Co Pty Ltd v Edwards Hot Water Systems (1985) 159 CLR 466 at 472, Gibbs CJ (with whom Mason and Brennan JJ agreed) stated (some citations omitted):

The notion of reproduction, for the purposes of copyright law, involves two elements — resemblance to, and actual use of, the copyright work, or, to adopt the words which appear in the judgment of Willmer LJ in Francis Day & Hunter Ltd v Bron [[1963] Ch 587 at p 614], “a sufficient degree of objective similarity between the two works” and “some causal connection between the plaintiffs’ and the defendants’ work”.  Lord Reid said in Ladbroke (Football) Ltd v William Hill (Football) Ltd:

Broadly, reproduction means copying, and does not include cases where an author or compiler produces a substantially similar result by independent work without copying.  And, if he does copy, the question whether he has copied a substantial part depends much more on the quality than on the quantity of what he has taken.

(See also [1964] 1 WLR, at pp 283, 288 and 293; [1964] 1 All ER, at pp 473, 477 and 481.)  In the same case, Lord Evershed said, “that what amounts in any case to substantial reproduction … cannot be defined in precise terms but must be a matter of fact and degree”.

As the represented respondents submitted, access to the copyright work is not to be equated with copying.  Access is necessary, but not sufficient.  This follows from the requirement that there be an “actual use of” the copyright work: SW Hart.  Copying can be conscious or subconscious – see: Francis Day & Hunter Ltd v Bron [1963] Ch 587 at 614 (Willmer LJ), 619 (Upjohn LJ) and 625 (Diplock LJ); Clarendon Homes (Aust) Pty Ltd v Henley Arch Pty Ltd (1999) 46 IPR 309 at [39] (Heerey, Sundberg and Finkelstein JJ).  Copying may be inferred on the basis of similarities which “are so striking as to preclude the possibility of the defendant having arrived at the same result independently”: Clarendon Homes at [15].

If reproduction is established, the next step is to ask whether the whole work or “a substantial part” was copied: Ancher, Mortlock, Murray & Woolley Pty Ltd v Hooker Homes Pty Ltd (1971) 20 FLR 481 at 494 (Street J); Gold Peg International Pty Ltd v Kovan Engineering (Aust) Pty Ltd (2005) 225 ALR 57 at [179] (Crennan J).  The statutory requirement that the part of a work taken must be substantial assumes there may be some measure of legitimate appropriation: IceTV at [157].  Reproduction of an unoriginal part of an original whole will not be an infringement: Ladbroke (Football) Ltd v William Hill (Football) Ltd [1964] 1 All ER 465 at 481; approved in Autodesk Inc v Dyason (No 2) (1993) 176 CLR 300 at 305 (Mason CJ, in dissent); Data Access at [83]-[84] (Gleeson CJ, McHugh, Gummow and Hayne JJ); IceTV at [37].  Whether a selection or arrangement of elements constitutes a substantial part of a work depends on the degree of originality of that selection or arrangement: IceTV at [43]; see also at [170].

In relation to computer programs, there may be a “need for some process of qualitative abstraction of the material features of the computer program in question”: IceTV at [158]-[159]; see also ObjectiVision at [643]-[644] (Burley J).  However, that may not be necessary where one can identify copying of specific source code the functionality of which is known or established.

If a person does no more than reproduce “data” or “related information” which are not relevant to the statements or instructions to be used directly or indirectly in a computer in order to bring about a certain result, the person will be unlikely to have reproduced a substantial part of the computer program: JR Consulting at [271], citing Data Access at [86].

The starting point for application of the provisions and a consideration of whether copyright has been infringed through reproduction is the identification of the work in which copyright subsists.  In Metricon Homes Pty Ltd v Barrett Property Group Pty Ltd (2008) 248 ALR 364 at [23], the Full Court noted that the correct approach in a copyright infringement case is to:

identify the work in suit in which copyright subsists – see further: IceTV at [15] (French CJ, Crennan and Kiefel JJ);

identify in the alleged infringing work the part taken (that is, derived or copied) from the work in suit; and

determine whether the part taken constitutes a substantial part of the work in suit.

The relevant exclusive right is the right to reproduce the work in a material form.  Difficulties in proving the precise content of the infringing work will not protect against a conclusion of infringement through reproduction so long as it is properly established that a substantial part of the relevant work was reproduced without authority of the owner of the copyright.

## C.1.3.2  Communication

Section 31(1) also identifies the right to communicate the work to the public as an exclusive right: s 31(1)(a)(iv).  Section 10(1) provides that “communicate” means “make available online or electronically transmit …”.  Accordingly, communication covers two classes of acts: electronically transmitting (for example, sending or receiving over the internet); and making available online (for example, putting on a website or including in a download service).  The phrase “to the public” means “to the public within or outside Australia”: s 10(1).

A communication, other than a “broadcast” (defined in s 10) is “taken to have been made by the person responsible for determining the content of the communication” – see: s 22(6).  By s 22(6A), a person “is not responsible for determining the content of a communication merely because the person takes one or more steps for the purpose of … gaining access to what is made available online by someone else in the communication” or “receiving the electronic transmission of which the communication consists”.

## C.2  The works in suit and subsistence

Campaigntrack sued on the copyright in the following works (which are referred to collectively as the DreamDesk Works):

Source Code Works: the literary works comprised in the source code for the DreamDesk system;

Database Work: the DreamDesk database as a literary work;

Table Works: the literary works comprised in the tables in the DreamDesk database;

Menu Work: the literary work comprised in the menu for the DreamDesk system;

PDF Works: the literary or artistic works comprised in the PDFs in the “client_data” folder.

### C.2.1  Source Code Works

The Source Code Works case was put on two bases:

First, Campaigntrack contended that the source code of the DreamDesk system as a whole was a “computer program” within the meaning of the Copyright Act, because it was “a set of statements or instructions to be used directly or indirectly in a computer in order to bring about a certain result”: s 10(1).

Secondly, Campaigntrack contended that each of the following PHP files within the source code of the DreamDesk system was a “computer program” within the meaning of the Copyright Act: “src\Functions\edms.php” (EDMS PHP), “views\adhoc-edit.php” (Adhoc Edit PHP), and “views\adhoc-edit2.php” (Adhoc Edit 2 PHP), because they also were “a set of statements or instructions to be used directly or indirectly in a computer in order to bring about a certain result”: s 10(1).

The “computer” was the virtual server on which the DreamDesk system ran.

As to the first way in which the case was put, the “certain result” was the provision of the functions of the DreamDesk system (for example: marketing real estate campaigns, generating print and online-ready PDF artwork) to the real estate agent users via the user-facing interface.

As to the second way in which the case was put, the “certain result” brought about by the individual PHP files was described in Mr Taylor’s first report, as follows:

EDMS PHP: loaded a template file from storage on the host web server; searched for fields in the template file; inserted relevant information into the fields in the template file with content retrieved from the database; loaded an additional template file; and displayed information in a read-only state;

Adhoc Edit PHP: loaded a template file from storage on the host web server; located fields within the template; inserted relevant information into the template file with content retrieved from the database; auto-completed property data in a text box; displayed the information in an editable format; rendered HTML code to display agent, contact and office details from pre-populated lists; resized and rendered images; allowed the selection of two contacts for a listing; produced iframes (which displayed a page within a page); and populated agent data from a database;

Adhoc Edit 2 PHP: loaded a template file from storage on the host web server; inserted relevant information into the template file with content retrieved from a data source; auto-completed property data in a text box; displayed the information in an editable format; rendered HTML code to display agent, contact and office details from prepopulated lists; produced iframes (which displayed a page within a page); populated agent data from a database; auto-completed office names of the “select office” menu.

## C.2.1.1  Source code works as a whole

The represented respondents accepted that copyright subsisted in the source code of the DreamDesk system as a whole, but not in relation to the three PHP files.

## C.2.1.2  The three PHP files: EDMS PHP, Adhoc Edit PHP and Adhoc Edit 2 PHP

I accept that a subset of statements or instructions may constitute a “computer program” within the meaning of the Copyright Act, notwithstanding that the subset also forms part of a larger set of statements or instructions that, as a whole, constitute a “computer program”.  I also accept that this is possible where the subset relies on other statements or instructions to bring about the “certain result”.  As Bennett J said in CA Inc at [142] and [147] (emphasis in original):

[142] 	The fact that the CA URT Macros require the participation of other components in order to bring about a result in the mainframe computer does not disqualify the CA URT Macros from being a “computer program” (Dais at [31], [35], [39]). ISI’s approach would, as CA contends, exclude from the definition of “computer program” a “set of statements or instructions” that require other components in order to bring about a result. It seems that this would, in effect, exclude all sets of statements or instructions written in any code other than object code because all source code requires another program to compile or assemble the source code into object code before producing any result. The definition of “computer program” does not exclude such statements or instructions, as is evident from the words “to be used … indirectly in a computer in order to bring about a certain result” (emphasis added).

..

[147] 	…The fact that a larger group of statements or instructions of which the identified set of statements or instructions forms part may also bring about that result does not preclude the identified set of statements or instructions from being a “computer program”, provided that it meets all of the requirements of the definition. As Jessup J observed in Dais at [31], “[a]s a matter of ordinary language, a thing might be used to bring about a certain result notwithstanding that it is but a component in a collection or sequence of things which together bring about the result”.

Whether a subset of a larger set of instructions is itself a “computer program” on the particular facts includes a consideration of whether the subset “can fairly be regarded as so separable from the material with which it is collocated as itself to constitute an ‘original … work’ for the purposes of s 32 of the Act”: Coogi at 172.  As the Full Court stated in Acohs Pty Ltd v Ucorp Pty Ltd (2012) 201 FCR 173 at [56]:

In the context of literary works that are computer programs, it is possible that a routine, or perhaps even an information tag, if it is original, sufficiently substantial and functionally separate from the entirety of the program of which it forms a part, might constitute a separate copyright work: see the observations in Powerﬂex Services Pty Ltd v Data Access Corporation (No 2) (1997) 75 FCR 108 at 127.

I am satisfied that the three PHP files fall within the meaning of “computer program”, notwithstanding the role of each file as a component of a larger computer program or set of instructions.  I reach that conclusion having regard to the separate function each plays within the operation of the DreamDesk system as a whole, being a function of sufficient substance for each file to be regarded as itself an “original work”.

The represented respondents advanced lengthy submissions challenging subsistence in (and ownership of) the three PHP files as individual computer programs.  The represented respondents observed that Mr Semmens was not asked about the three PHP files in cross-examination, with the result that Campaigntrack’s case “should fail in limine”.  The represented respondents put forward four “main possibilities” as to when the PHP files might have been written:

while Mr Semmens was at Digital Hive;

while Mr Semmens was at Digital Group;

while Mr Semmens was at DDPL;

before Mr Semmens was at DDPL, but that they may have been modified for use by Biggin & Scott in the DreamDesk system.

The represented respondents submitted that there was “[n]o evidence to substantiate the premise” that Mr Semmens wrote the PHP files whilst at DDPL.  It was submitted that “[i]f anything, the evidence weighs against the proposition that Mr Semmens wrote them, as original works, when he was a contractor at Dream Desk” and that “[i]f he had been working with electronic direct mail functionality from his time at Digital Hive (if not earlier), the likelihood is that he re-used what he knew”.

I reject the represented respondents’ submissions in this respect.  Campaigntrack established what it reasonably could having regard to the information that it was able to obtain.  If Mr Semmens had wanted to give evidence that the PHP files were not written whilst at DDPL or that they were “re-used” from earlier work, he could have said so – cf: Blatch v Archer (1774) 1 Cowp 63; Commercial Union Assurance Co of Australia Ltd v Ferrcom Pty Ltd (1991) 22 NSWLR 389; Australian Securities and Investments Commission v Hellicar (2012) 247 CLR 345.  The represented respondents could have asked questions of Mr Semmens in cross-examination; they asked none.  There was no obligation on the part of Campaigntrack to cross-examine on the issue in light of the content of the evidence, in particular Mr Taylor’s report, and the silence of Mr Semmens on the issue.  Mr Semmens was in the represented respondents’ camp and had provided to some of them, and been provided by some of them with, assistance throughout the proceedings.  Accepting that the “main possibilities” put forward are theoretically possible, they are in the nature of conjecture and there is an insufficient evidentiary basis to draw a conclusion that any of them reflects reality.  Given the evidentiary silence on the part of the represented respondents and Mr Semmens on the issue, weighed against the evidence which Campaigntrack was able to adduce, the inference I draw is that the PHP files were created as original works by Mr Semmens whilst at DDPL.

### C.2.2  Database Work and Table Works

A database can be a “literary work” and is a “compilation” within the meaning of the Copyright Act – see: the definition of “literary work” in ss 10(1) and 10(2A)(a); IceTV at [72], [99].

The text form of the Database Work was in evidence.  Visually, the Database Work comprised a particular database “schema” or structure.  I accept that the Database Work was the product of some intellectual effort and was relevantly original.

The Database Work included a number of “tables”.  Campaigntrack asserted that copyright subsisted in 18 tables (the “Table Works”), namely tables described in the following way: “Agents”, “Listings”, “Marketing”, “Media bookings”, “Media extras”, “Offices”, “Office groups”, “OFI”, “Properties”, “Template Items”, “Template Selections”, “Templates”, “Media Items”, “EDM Templates”, “EDM Campaigns”, “EDM dyn content”, “Marketing Items” and “Images” – see: [14A(a)] of the Further Amended Statement of Claim (FASOC); Ex 16, tab C1.

A “table” is capable of being a literary work – see: the definition of “literary work” in s 10(1) of the Copyright Act.  A subset of the Table Works in the Database Work was represented diagrammatically, in text form and in electronic form.  An example of a subset of the tables represented diagrammatically is as follows:

The following is a diagrammatic representation of the “agents” Table Work in the Database Work:

Each Table Work comprised a collection of material arranged in columns and rows (individual data records).  Each Table Work included at least three characteristics: (1) the table name; (2) the column heading (“Column Names”); and (3) constraints on the formatting of data in each row (“Data Type”): “int(n)” (integers up to “n” digits in length) or “varchar(n)” (variable characters up to “n” characters in length).

The represented respondents challenged the subsistence of copyright in the Table Works on a number of bases.

First, the represented respondents challenged the subsistence of copyright in the tables as works separate from the Database Work because “they had no independent or separate existence in material form as an empty grid or Excel spreadsheet … divorced from the property-related data they contained”.  As a matter of principle, there is no difficulty in a table within a database itself constituting a “literary work” in which copyright might subsist – see, by analogy [199]-[200] above.  I accept that the tables were “literary works” in their own right:

Mr Semmens created the database schema on a computer (which he no longer had at a time which permitted it to be examined) before uploading it to AWS, meaning it existed separately to the DreamDesk system.

Mr Allen was able to extract selected Table Works from the database, indicating each was a separate work and not necessarily dependent on other works.

Mr Taylor had no difficulty identifying each Table Work as an individual work and each was able to be visually represented as a discrete table, as one would expect.

Secondly, the represented respondents submitted that there was “no evidence of originality stemming from a human author to sustain the subsistence of copyright”.  It was submitted that:

Mr Semmens was not asked about any particular table in cross-examination.  The submission included that, if it was going to be put that the selection, order and arrangement of each of the tables and their constituent fields was “original” in the requisite sense, it should have been put to Mr Semmens, but was not.

There was no direct evidence of the time, process, deliberation, creativity, thought or consideration by which any of these tables was brought into existence.  There was no evidence of “independent intellectual effort” or “sufficient effort of a literary nature” with respect to the gathering of information, or its selection, ordering and arrangement in its fixation in material form.

The contemporaneous documents did not support a finding of originality because the commercial and factual context was of the collection, storage and use of property-related data by real estate agents for the marketing of property.  In this regard, reference was made to contemporaneous communications which indicated an overlap between the content of the pleaded tables and other tables used to facilitate computer programs used in the real estate industry.  Reference was made in this regard to Customer Relationship Management (CRM) systems which track and manage customers and properties for real estate agents, including photos and floor plans.  Reference was also made to the fact that agencies, such as Biggin & Scott, inputted “data relating to properties” to the DreamDesk system and that those agencies retained that “property related data”.

Other documents did not support a finding of originality.  Reference was made in this regard to documents for realestate.com.au (covering the period 2004 to 2014) and Domain (dated 14 June 2018 and thus not contemporaneous) which typically required property-related data which overlapped with the kinds of data contained in the tables.

Mr Timm’s evidence did not support originality.  Mr Timm accepted that the data fields for the tables corresponded to the “core data” and “core functionality” in a system that “generate[s] artwork” and these tables “store property data, they store booking data”.  His evidence included that the data fields referred to “common data that we would store for real-estate agents in such a system” in respect of the “Agents” table.  He accepted, for example, that the tables contained data fields and entries which were:

“all quite standard” and, in relation to the fields for social media entries, “if they weren’t essential in 2016, they’re, certainly, essential now”: see Hearing Transcript (“T”) 128.18 and T 128.43-45 re the “Offices” table;

“nothing earth shattering” and where the “columns [were] consistent” with “the type of information that you would expect in a system developed to provide functionality of Web to Print services by reference to a database that stored client and content information relevant to the marketing and promotion of real estate”: T 129.46-47 and T 130.40-44 re the “OFI” [Open for Inspections] table;

“common”, “central pieces of information that real estate agents have to gather and include, both, in their CRMs and for their marketing platforms”, “every day and common pieces of information that [you] would need and you would expect to see in a database of this kind”, “all fields that … would be needed to market a property” and “common data for that kind of information to be stored [in 2015 and now]”: T 132.42-44, T 133.4-7, T 133.12-14, T 134.35-39, T 136.15-21 re the “Properties” table;

To the extent the tables related to EDM (namely Electronic Direct Mail) functionality, these were not original because they were likely based on what Mr Semmens knew from his time at Digital Hive and Digital Group.

A common thread in the represented respondents’ submissions was the failure to cross-examine Mr Semmens and what was said to be a lack of evidence of “independent intellectual effort” or “sufficient effort of a literary nature” to support the originality of the Database Work or the Table Works.  I reject these submissions for the following reasons.

First, Mr Semmens was the person who produced the Database Work and the Table Works.  As to the tables, these required time to develop and contain at least some complexity even if many of the fields are ones which would be expected to be found in connection with a computer program, with an associated database, of the relevant functionality.  As to the Database Work, this comprised over 110 tables and, it is to be inferred, took considerable time to develop.  The inference is properly drawn from the nature of the Database Work and Table Works themselves that intellectual effort was required and expended.  Mr Semmens could have, but did not, adduce evidence that no or insufficient intellectual effort was required.

Secondly, it is not to the point that various tables recorded certain kinds of information (data) that real estate agencies would have an interest in recording in the selling of real estate or even that such information was necessary to be recorded in order to provide appropriate functionality in the commercial context (for example, furnishing information necessary to take advantage of services offered by Domain or realestate.com.au).  The point is that intellectual effort was required, and I infer expended by Mr Semmens, on:

the selection, arrangement and ordering of multiple tables within the Database Work and the specific relational connections between tables – see, for example: T 130.12-16, T 132.35-40);

within each Table Work, the choice of table name, the choice of column (field) name, the internal arrangement/ordering of the columns (fields), the choice of constraints on data formatting (data type) and so on; and

choices in the expression of the Table Works, as confirmed by the evidence of Mr Timm.  By way of example, Mr Timm gave the following evidence at T 130.27-36 (emphasis added):

Again, common in the - - -?---Yes. We would call [the field “ofi_status” in the “OFI” table] “deleted” and store the time when it was deleted, in our database. But it’s - - -

Right?--- - - - that’s another way of doing it.

It’s just – I just want to, so is this the position in Campaigntrack you do it differently?---Yes.

And in Dream Desk, whoever came up with this structure decided to do it in this particular way?---Yes.

At T 133.18-28:

And, then, we have rows 222 and 223 [the fields “prAuctionDate” and “prAuctionTime” of the “Properties” table] for the possibility of if it’s going to be an auction?---Yes.

Again, common piece of information that you would expect to see in a - - -?---Yes. The information is common. I’m surprised to see that option, date and time, as two separate columns when it could be a date-time value as it was in the other photo, but - - -

Nothing - - -?---It doesn’t make any functional difference.

Just that you – just that you wouldn’t do it that way?---I wouldn’t do it that way.

At T 134.35-39:

… And – and again, these are all – they are all items that you would expect to see in a database designed for service to real estate agents for the online promotion of property?---Yes, these are all fields that I would – you would be needed to market a property. I would expect to see some of these maybe split out into separate tables, but I guess the required – data that’s required for marketing a property.

At T 135.11-14:

… Yes. The reason I mentioned that I expect to see some of this split out is because of the nature of, obviously, [the “properties” table] is a very long table already and there’s many different items. So for me, it makes sense to have a separate table for this kind of content. The data, itself, is needed.

In connection with the argument that the fields were ones which overlapped with those required by other participants in the real estate industry, and the reliance on industry documents, the represented respondents referred to the application programming interface (API) and XML documentation from PortPlus (a CRM system), realestate.com.au and Domain, which typically required certain information.

Campaigntrack referred in this regard to the following evidence given by Mr Timm regarding the operation of Campaigntrack’s current system (not its system in 2016 or the DreamDesk system) (emphasis added):

… [T]hese days I would say that for the majority of our customers, we have integrated with their various CRM systems to make that data flow through automatically for them.

And when you say “integrated”, is that by the use of an application programming interface of some kind?---That’s right, yes.

And does that have a – does that particular – is that a customised API for you, or is it a third party software?---The API is – it varies depending on the system. So an API – just to explain in detail – is – is the interface for a program to talk to a program in the same way the user interface is the interface in which the user talks to the program. So an API is a layer of obstruction [sic] to – to our software, or to another piece of software, that then those two pieces of software could talk to each other. So it’s something we develop as an – as an additional interface for programs to talk to us.

So it’s a way of making sure that when you move the data from one piece of software to another it gets sent to the right spot?---Correct.

…

And if [the artwork is] going to go online, do you contact each of the various sites separately in order to publish that material online?---Yes. In the same way there is an integration with the CRMs if they want to list on realestate.com.au or domain, we have a feed from our system to those systems to publish those listings.

And when you say, “a feed from your system to that system” what feed is that?---That’s an XML based feed, which is a form of describing data.

Just on XML, is the – an XML[’]s primary purpose is to serve as a means of sharing information between information systems that could have very different architectures. Is that right?---That’s right, yes.

And it’s a – it has kind of become – becomes a kind of … de facto standard, is that right?---XML, itself, is a standard. And then every provider, be it realestate.com.au develops their own specification of XML.

Right?---Defining what fields they would choose to accept and what they are named and what the – in the same way of in the database we describe the data, the XML describes how those systems want to receive that data.

Right. And so if you want to – if you want to make sure that your system will easily upload onto realestate.com.au, you have to make sure that it complies with realestate.com.au’s XML guidelines. Is that right?---We have to conform to the XML spec when generating that XML feed, yes.

As Campaigntrack submitted, this evidence shows that neither an API nor an XML specification prescribes or dictates the data structure of a database of an information system.  The data structure design is left to the creativity of the developer (as the author of the relevant database schema).  Rather:

an API is used for data communication, so that data from the sending information system (for example, a CRM system) goes into “the right spot” of the receiving information system (for example, Campaigntrack’s system), so that the two systems can communicate appropriately;

an XML specification describes the types and format of the data the receiving information system (for example, realestate.com.au or Domain) is prepared to accept in the form of an XML-based feed.  It does not prescribe or dictate the data structure of the sending information system (for example, Campaigntrack’s system).  The two systems could have very different architectures.

Further, as Campaigntrack submitted, the fact that the DreamDesk system could be compatible with multiple CRM systems and real estate advertising portals suggests that its data structure is original.  I also note that Mr Timm’s evidence supports a conclusion of originality given that Mr Timm would have done certain things a different way.

There was no direct evidence that Mr Semmens copied, let alone merely copied, anything from realestate.com.au or Domain or their technical documents.  The evidence did not establish that the particular expression of the Database Work or the Table Works was “essentially dictated” by requirements related to realestate.com.au or Domain – see: University of Sydney v ObjectiVision Pty Ltd (2019) 148 IPR 1 at [482].

As to the submission that the tables relating to the EDM functionality, being the “EDM Templates”, “EDM Campaigns” and “EDM dyn content” table, were copied by Mr Semmens from Digital Hive or Digital Group’s tables, the inference fairly arises that they were not and Mr Semmens was capable of establishing the contrary, but adduced no evidence to suggest this was the case.

I accept that the Database Work and the Table Works were original and constituted literary works in which copyright subsisted.

### C.2.3  Menu Work

Campaigntrack also pleaded that it was the owner of copyright in “the menu for the DreamDesk website”.  The DreamDesk system included various menus, the whole of which was described as the “Menu Work”.  The Menu Work formed part of the web-based user-facing interface that allowed users to navigate and interact with the DreamDesk system.  The Menu Work was represented in text form and visually.  There were 10 dropdown menus represented by screenshots in the evidence: Ex 16, tab C3.  Further screenshots were also in evidence at Ex 18 tab 27.  An example is as follows:

The represented respondents submitted that the various drop-down menus were not, of themselves, original.  The point was perhaps best made by reference to a drop down menu identifying the 24 hours in the day, ordered in the way one would expect (chronologically).

It might be that a collection of menus (including ones lacking originality), being a compilation, might be shown to be a literary work separate to the computer program as a whole.  However, the evidence in this case is insufficient for that conclusion to be drawn.  The evidence does not show that there was a “Menu Work” or a “menu for the DreamDesk website” which was something sufficiently separate from the source code itself as to be regarded as something in which copyright could subsist independently of copyright in the whole computer program.  Further, the evidence did not establish, and I would not infer, that the individual menus were created through the intellectual effort of Mr Semmens when creating DreamDesk.  The individual menus might just as easily have come from a program or third party application.  In any event, the case was not pleaded on the basis of the various dropdown menus each constituting a literary work and the evidence did not establish them as individually constituting literary works.

I do not accept that there was a Menu Work which was a “literary work” separate to the whole of the computer program.

### C.2.4  PDF Works

The applicant alleged in para 14A(e) of the FASOC that it owned copyright that subsisted in:

PDFs, being literary works, or in the alternative, artistic works (being drawings) in which copyright has subsisted at all material times and continues to subsist, being PDFs held in the “client_data” folder, which included:

(A)	PDF Proofs of advertising material for properties; and

(B)	Artwork Templates.

It was alleged that Mr Semmens or Mr Gallagher were the authors (jointly or individually) of the PDFs: see para 14A (second appearing) of the FASOC.

The PDF Works included PDF templates that were used to generate approved artwork.  A screenshot example of a PDF template is as follows:

The PDF templates contained information specifying the location of variable page elements along with relevant properties such as font size, colour and/or image scaling.  This information permitted the computer program to insert data into the variable page elements and generate an output PDF based on the design of the PDF template.  Ultimately, the PDF Works claim related to 668 PDFs, being the PDFs in the “client_data” folder of the DreamDesk system.

The represented respondents submitted that:

when Biggin & Scott moved from using Advenda Pro to using Campaigntrack in 2013, Mr Russell Perkins (then of OzePrint) handled the transition;

Campaigntrack helped its clients (being real estate agencies and agents) build libraries of templates according to those agencies’ style guides and branding, together with their logos and details;

Campaigntrack’s standard terms and conditions “would seem to place ownership of templates (and data) with the client”;

Biggin & Scott entered into the Biggin & Scott – DDPL Agreement on 20 May 2015 with DDPL which covered Biggin & Scott’s templates and property-related data;

Mr Perkins sent Biggin & Scott artwork to DreamDesk in the months up to June 2015;

Biggin & Scott started using DreamDesk on 17 August 2015;

thus, what began with Biggin & Scott using its templates with Advenda Pro, then moved through Biggin & Scott using its templates with Campaigntrack and ended with Biggin & Scott using its templates with DreamDesk.

Campaigntrack contended these submissions should be rejected because:

Biggin & Scott refused to sign the draft contract presented by Campaigntrack, such that – whatever those terms and conditions provided – they were not agreed;

Mr Watts’ evidence was that, on 25 June 2015, he found Mr Perkins “had been actively sending artwork and ordering information to DreamDesk”.  The artwork and ordering information were not in evidence.  Nor was there any evidence that those things were the PDF Works in suit.  There was no evidence of the extent of Mr Perkins’ “exfiltration”;

there was no evidence that the Biggin & Scott templates in Advenda Pro were the same documents as the Biggin & Scott templates used in Campaigntrack’s system, which in turn were the same documents as the PDF Works in suit;

the represented respondents, including Biggin & Scott, could have adduced, but did not adduce, evidence to that effect.  It is inconsistent with Ms Bartels’ communication to Excel on 3 September 2016:

… My biggest frustration in the past with Campaign Track or even Advenda was waiting 6 weeks for a template to be built or being told NO we can’t do that. The benefits of being with Dream Desk is we’ve been able to create a world of Biggin & Scott at ease. …

nor did the represented respondents ask questions in cross-examination to prove that the templates in Advenda Pro were the same as the templates used in Campaigntrack’s system and the PDF works in suit;

the fact that Biggin & Scott and DDPL signed their agreement in May 2015, and Biggin & Scott started using the DreamDesk system in August 2015, indicates that there was a three-month on-boarding period.  This supports a conclusion that Biggin & Scott’s templates in the DreamDesk system (the PDF Works) had to be created separately from whatever templates Biggin & Scott had been using in Advenda Pro and Campaigntrack’s system.

The represented respondents next submitted that it was not possible on the evidence to make a finding as to subsistence of copyright in any of the 668 PDFs as either a literary work or an artistic work because:

there was no identifiable author or authors (assuming an author or authors existed) and it is not known whether those person(s) were “qualified persons” within the meaning of the Copyright Act;

it was not known whether each of the 668 PDFs was original;

it was not known when each of the 668 PDFs was first fixed in material form;

it was not known if and, if so, when each of the 668 PDFs was published.

As to the matters in (a): First, I infer that Mr Semmens was the author of the 668 PDFs.  Mr Semmens was the developer and author of the DreamDesk system as a whole.  A number of the PDF Works included a default address of “11 Dave Street, Mooroolbark”.  Mr Semmens’ former address was “11 [redacted], Mooroolbark”.  Mr Semmens’ first name is David.  I infer that the default address was Mr Semmens’ choice.  I further infer, including from the absence of any denial or evidence on the topic from Mr Semmens, that Mr Semmens created the templates.  Secondly, there was no dispute that Mr Semmens was a “qualified person”.  Mr Semmens was resident in Australia at the time of the handover of the DreamDesk system to Campaigntrack in September 2016 and at all material times before then and since – see: ss 32(1)(a), (2)(d) and (4) of the Copyright Act.

As to the matters in (b), (c) and (d): I also conclude that the 668 PDFs were original and that they were fixed in material form at some point between 20 May 2015 and 17 August 2015.  None of the respondents’ witnesses (Mr Semmens, Mr Meissner, Mr Stoner and Ms Bartels) gave any evidence to impugn the originality of the PDF Works.  None of them said Mr Semmens was not the author of the PDF Works.  This was evidence readily available to Mr Semmens.  None of them gave reliable evidence to the effect that the PDF Works were mere copies of earlier templates or templates previously used by Biggin & Scott in different systems.  This was evidence which was readily available to Biggin & Scott.

The represented respondents also submitted that the DreamDesk sale agreement, between Campaigntrack/New Litho and DDPL/Mr Meissner, properly construed, did not assign copyright in each of the 668 PDFs as separate copyright works.  This argument ultimately boiled down to a contention that the contract should have expressly identified each and every possible separate work, forming part of DreamDesk as a whole, in order for the intellectual property rights in works which might be capable of being separate works to be assigned.  Clause 1.1 of the DreamDesk sale agreement provided:

1.1. 	Dream Desk agrees that it will sell to Campaigntrack and New Litho (the “Purchasers”) the DreamDesk Platform and all intellectual property associated with the operation of the DreamDesk Business, including copyright (including any rights to source code), design, patents and trademarks and all rights to the business name of the DreamDesk Business and all domain names registered by Dream Desk, including dreamdesk.com.au (the [“]Intellectual Property”).

This clause effected an assignment of all of the intellectual property associated with the operation of the DreamDesk Business, which plainly included the PDF Works and any other works capable of themselves constituting literary or artistic works associated with the operation of the DreamDesk Business.

I accept that the PDF Works were “literary works” in three senses:

in the general sense, as a work, expressed in writing, intended to afford information or instruction on the generation of output PDFs: Computer Edge Pty Ltd v Apple Computer Inc (1968) 161 CLR 171 at 182, 201;

in the “compilation” sense, as a work resulting from the collection, selection, arrangement and ordering of materials (blocks for insertion of text and images) expressed in words, figures or symbols: definition of “literary work” in s 10(1) of the Copyright Act; IceTV at [72], [99];

in the “computer program” sense, as “set[s] of statements or instructions to be used directly or indirectly in a computer in order to bring about a certain result”, namely the generation of output PDFs: definition of “computer program” in s 10(1) of the Copyright Act.

The PDF Works were possibly also “artistic works” within the meaning of the Copyright Act, as “drawings”, but nothing additional turns on their characterisation as such.  Copyright subsisted in the PDF Works.

## C.3  Ownership

### C.3.1  Source code as a whole

There was no dispute between the parties that copyright in the source code for the DreamDesk system as a whole as a “computer program” was owned by Campaigntrack.

The represented respondents disputed ownership of copyright in the remaining works for a number of reasons, including submissions that:

the DreamDesk sale agreement between Campaigntrack/New Litho and DDPL/Mr Meissner only assigned the copyright in the source code for the DreamDesk system as a whole as at 30 August 2016 or as at 5 September 2016 and not copyright in other works which might form a subset of the source code or work associated with the operation of DreamDesk;

in amplification of the first submission, the DreamDesk sale agreement did not purport to assign copyright in the three PHP files or in the Database Work or Table Works or Menu Work;

the DreamDesk sale agreement did not include any work related to EDM functionality;

under the Biggin & Scott – DDPL Agreement dated 20 May 2015, the PDF Works were owned by Biggin & Scott.

### C.3.2  Construction of clause 1.1 of the DreamDesk sale agreement

As to the first three of the submissions set out immediately above, the DreamDesk sale agreement was broadly expressed.  The sale was of “the DreamDesk Platform and all intellectual property associated with the operation of the DreamDesk Business”.  Clause 1.1 provided:

1.1. 	Dream Desk agrees that it will sell to Campaigntrack and New Litho (the “Purchasers”) the DreamDesk Platform and all intellectual property associated with the operation of the DreamDesk Business, including copyright (including any rights to source code), design, patents and trademarks and all rights to the business name of the DreamDesk Business and all domain names registered by Dream Desk, including dreamdesk.com.au (the [“]Intellectual Property”).

The term “DreamDesk Business” was defined in Recital A as follows:

A. 	Dream Desk, trading the business of DreamDesk, owns and operates a cloud based software business providing vendor paid advertising management and file delivery to real estate agents and their advertising suppliers (known as web-to-print) and the provision of electronic direct mail (“EDM”) to the real estate sector (the “DreamDesk Business”). Dream Desk operates the DreamDesk Business trading under the ABN 56 604 719 735.

The term “DreamDesk Platform” was defined as the online platform operated by DreamDesk in its business, namely the DreamDesk system.

The surrounding circumstances were that Campaigntrack sought to acquire full control of the DreamDesk system, in order to shut it down and to attempt to persuade DreamDesk clients (including Biggin & Scott and RT Edgar) to move or return to Campaigntrack’s system.

Reasonable businesspeople would not have understood from cl 1.1, construed in the context of the agreement as a whole and the surrounding circumstances known to the parties, that the sale was confined to a particular version of the DreamDesk system as a whole and nothing else – see: Electricity Generation Corporation v Woodside Energy Ltd (2014) 251 CLR 640 at [35]; Mount Bruce Mining Pty Limited v Wright Prospecting Pty Limited (2015) 256 CLR 104 at [46]-[49].  The construction advanced by the represented respondents, if correct, would mean that DreamDesk could still sell copyright in the source code to an immediately preceding version to some other person to commercialise, defeating the whole purpose underlying the parties’ transaction.

It does not matter that the DreamDesk sale agreement did not expressly refer to assignment of copyright in the three PHP files or in the Database Work or Table Works or Menu Work or in relation to work related to EDM functionality.  To the extent these were literary works, any copyright in them was “associated with the operation of the DreamDesk Business” and was assigned to Campaigntrack by cl 1.1 of the agreement.

The fourth contention referred to above is addressed at [254]–[255] below.

### C.3.3  The three PHP files: EDMS PHP, Adhoc Edit PHP and Adhoc Edit 2 PHP

The represented respondents submitted that the Process 55 sale agreement did not include any assignment of any EDM files, relying on the definition of “Process 55” in cl 1 of the agreement:

an on-line platform … which:

(i) 	is a user friendly online art production and media management system that builds marketing material, including media advertisements and composites, media schedules, brochures, flyers, signage, stationery;

(ii) 	produces low resolution previews and print ready, high resolution art “on the fly” in real time and edits, crops and provides compositing functionality for block advertisements;

(iii) 	places electronic orders with suppliers, uploads supplier data, tracks production in real time and can be customised and programmed to meet individual user requirements; and

(iv) 	provides a suite of administrative functions whereby users may manage levels of user access, media rates and data and provides flexibility by allowing graphics to be edited by the user.

This submission was directed, at least in part, to a submission that ownership of copyright in the PHP files could not have been transferred to Campaigntrack under the Process 55 sale agreement if Mr Semmens created the PHP files when he was at Digital Hive.  It is unnecessary to reach a conclusion in respect of the submission because I have earlier concluded that copyright in the PHP files subsisted in DDPL.  In any event, I do not accept the underlying premise that the PHP files related only to EDM functionality, albeit they related to EDM functionality.

Ownership of the intellectual property rights in the three PHP files was transferred to Campaigntrack under the DreamDesk sale agreement.  Contrary to the submission advanced for the represented respondents, no reasonable businessperson would have understood that the sale was intended to exclude anything to do with EDM functionality, particularly given the express reference to EDM in the definition of “DreamDesk Business” – see [244] above.  The DreamDesk sale agreement expressly assigned copyright in “all intellectual property associated with the operation of the DreamDesk Business”.  The agreement assigned copyright in the PHP files.

### C.3.4  Database Work, Table Works and Menu Work

The DreamDesk sale agreement, properly construed, assigned copyright in the Database Work, the Table Works and the Menu Work to the extent that each constituted work in which copyright was capable of subsisting and did subsist.

### C.3.5  PDF Works

The represented respondents submitted that “under the agreement between Dream Desk and Biggin & Scott [dated 20 May 2015], the templates were owned by Biggin & Scott”.  The agreement between Biggin & Scott and DreamDesk provided (emphasis added):

Biggin & Scott Corporate Pty Ltd agrees to become a client of Dream Desk under the understanding that at all times any templates or data relating to properties and staff put into Dream Desk remains the property of Biggin & Scott Corporate Pty Ltd and or the office that has built an advertisement.

This agreement is to the effect that, to the extent Biggin & Scott in fact put templates and data into the DreamDesk system, the templates and data would remain the property of Biggin & Scott; they were not assigning their rights in templates and data to DreamDesk.  However, the present question is about the PDF Works which I have concluded were created by Mr Semmens while working at DDPL.  It might be that, to the extent data was put in by Biggin & Scott, that data remained the property of Biggin & Scott.  The same would be true of any template put in by Biggin & Scott.  But a template created by Mr Semmens for Biggin & Scott would not be covered by this clause and could not, on any view, “remain” the property of Biggin & Scott.

## C.4 The alleged infringing work

The infringing work was pleaded to be a “software system known as Real Estate Tool Box”: FASOC [4(b)].  The thrust of the defence by the represented respondents was that two versions of the “software system known as Real Estate Tool Box” comprised source code which was not proved to have been copied from the source code of DreamDesk.  The two versions were “toolbox_old” and “toolbox_current”, respectively dated 10 February 2017 and 23 October 2017.  These were produced by Mr Semmens as zip files in compliance with the Court’s orders for production made on 18 October 2017.

The principal underlying fallacy in the represented respondents’ defence in this respect was the false assumption that Campaigntrack’s case was that the works produced by Mr Semmens pursuant to the 18 October 2017 orders were what demonstrated infringement.

Campaigntrack pleaded that “[o]n a date or dates presently unknown, but at least before 23 September 2016, Mr Semmens reproduced and/or authorised the reproduction of one or more of the literary works comprising the source code for the DreamDesk website in Australia”: FASOC [47].  The orders made by the Court on 18 October 2017 required production of an operating version and a copy of all the source code for the Toolbox system as at the date of those orders and (to the extent possible) as at 16 August 2016, 15 September 2016 and 23 September 2016.  The “toolbox_old” and “toolbox_current” zip files (10 February 2017 and 23 October 2017) were produced by Mr Semmens in response.

The instructions to Mr Taylor, which had been negotiated between the parties and agreed to by the respondents, asked him to compare the respective source codes from the DreamDesk and Toolbox systems as at 16 August 2016, 15 September 2016 and 23 September 2016, or as near to those dates as was possible.  Mr Allen compared the PHP files from the DreamDesk system in their forms before 26 August 2016 and the “helpers” PHP file from the Toolbox system as at 26 August 2016.

Campaigntrack’s case was that the Toolbox system was developed from the DreamDesk system, namely by copying it and progressively altering it.  According to Campaigntrack, Toolbox was progressively developed from the DreamDesk system by DreamDesk/JGM Advertising staff, at DreamDesk/JGM Advertising’s offices and it was important to focus on the early versions of the Toolbox system in August and September 2016, not versions (to the extent they were in fact versions of Toolbox source code) many months later.  These earlier versions were more likely than later versions to furnish evidence of the fact that the source code had been copied.

Mr Taylor was appointed under r 23.01 of the Federal Court Rules 2011 (Cth) as a Court expert to report on various matters set out in instructions given to him, as agreed between the parties.  As noted above, one of his tasks was to compare versions of DreamDesk with versions of the Toolbox system as at 16 August 2016, 15 September 2016 and 23 September 2016.  Mr Taylor recorded that the first commit of files to the Dashboard Vault1 Repository was on 26 August 2016 at 2:02 pm.  He examined that source code together with source code committed on 15 September 2016 and 23 September 2016 for the purposes of comparing it with the DreamDesk source code created on 30 August 2016.

Mr Taylor was also asked to compare source code in particular files and to report on the functionality of any matching code.

Without setting out Mr Taylor’s findings in detail, it is sufficient to note that there were many lines of source code which matched exactly: Taylor Report [6.14] to [6.15].  Mr Taylor also reported on the functionality of the matching code.  He expressed the opinion, which I accept as a correct reflection of what in fact occurred, that substantial parts of the matching code in the Toolbox system had been copied from DreamDesk.  An example of Mr Taylor’s findings and conclusions is as follows:

6.15 	Paragraph 28 of the Order instructs me to outline the number of duplicated lines of code from each of the files listed in the table section 6.14, provide an explanation of the different functions the duplicated code undertakes, identify whether the code is found in whole or in part within DreamDesk, and give an opinion on whether it suggests copying or some other explanation. In response to these questions:

(a) 	Analysis of the DreamDesk file “src\Functions\edms.php” shows it contains 183 lines of code, (excluding blank lines).  Analysis of the Real Estate Tool Box file “app\Http\helpers.php” showed it contains 353 lines of code (excluding blank lines). The two files were compared and 179 lines of code were identified to exactly match. Print screens of the files are displayed in Exhibit PT-8 with the matching lines of code highlighted.

(i) 	The matching lines of code have the following functionality:

The loading of a template file from storage on the host web server

The searching for fields in the template file

The insertion of relevant information into the fields in the template file with content retrieved from a data source

The loading of an additional template file within the ‘prop’ case statement

The display of information in a read only state.

(ii) 	It is my opinion that this code has been copied. This opinion is based on the following:

The number of duplicated lines of code

The order of the case statements within the switch statement being the same

The field format and field names being the same

The variable names being the same

The comments being the same.

The represented respondents submitted that the Court should conclude that the alleged infringing work was one of the versions of Toolbox in 2017, namely “toolbox_old” or “toolbox_current” which were relevantly the same: Taylor Report [6.12].  One difference between the August 2016 version of Toolbox obtained by Mr Taylor and that in “toolbox_old” and “toolbox_current” was that the 2017 versions did not contain the folder “resources\views\edms” or the three files “edit.blade.php”, “index.blade.php” and “show.blade.php”: Taylor Report [6.27(b)].

I am not satisfied that “toolbox_old” or “toolbox_current” would provide appropriate comparators for determining whether the DreamDesk source code was reproduced.  The zip files were created by Mr Semmens.  As Campaigntrack submitted:

“toolbox_old” was said to be dated 10 February 2017; however, the version of “helpers.php” in “toolbox_old” matched the versions as at 18 October 2016, 8 December 2016 and 9 February 2017, but not the version as at 10 February 2017 at 4:41pm because the latter had 115 lines of code added back;

“toolbox_current” was said to be dated 23 October 2017; however, the version of “helpers.php” in “toolbox_current” most closely matched the Git repository versions as at 18 October 2016, 8 December 2016 and 9 February 2017 but not the version of “helpers.php” as at 6 June 2017which had 146 additional lines of code.

The fact that the evidence did not address whether the versions of source code produced by Mr Semmens pursuant to the Court’s order for production (namely “toolbox_old” and toolbox_current”) contained source code identical to (or copied from) DreamDesk does not answer the question whether the DreamDesk source code as a whole (or a substantial part of it) was reproduced or whether the remaining works in issue were reproduced.

## C.5  Infringement

### C.5.1  Primary and secondary infringement

As noted earlier (in Section C.1.1 above), by reason of s 36(1) of the Copyright Act, copyright in a work is infringed by a person who is not the owner of the copyright who does any act “comprised in the copyright” without the licence of the owner of the copyright.  Section 13 provides that an act comprised in the copyright in a literary work includes any act that the owner of the copyright has the exclusive right to do and the exclusive right to authorise a person to do that act.

Accordingly, s 36 provides for two causes of action: “primary infringement”, namely direct infringement by the “doing [of] … any act comprised in the copyright”; and “secondary infringement”, namely the authorisation of the doing of the act or acts comprised in the copyright constituting the primary infringement: Roadshow Films Pty Ltd v iiNet Ltd (No 2) (2012) 248 CLR 42 at [93].

Section 36(1A) of the Copyright Act provides that, in determining for the purposes of s 36(1) whether or not a person has authorised the doing in Australia of any act comprised in the copyright in a work, without the licence of the owner of the copyright, the matters that must be taken into account include the following:

the extent (if any) of the person’s power to prevent the doing of the act concerned;

the nature of any relationship existing between the person and the person who did the act concerned;

whether the person took any reasonable steps to prevent or avoid the doing of the act, including whether the person complied with any relevant industry codes of practice.

The word “authorise” has its ordinary meaning of “sanction, approve, countenance”: University of New South Wales v Moorhouse (1975) 133 CLR 1 at 12 (Gibbs J) and 20 (Jacobs J); Roadshow Films at [48]-[51] and [125].  In Moorhouse at 12, Gibbs J stated (footnotes omitted):

The word “authorize”, in legislation of similar intendment to s 36 of the Act, has been held judicially to have its dictionary meaning of “sanction, approve, countenance”: Falcon v Famous Players Film Co; Adelaide Corporation v Australasian Performing Right Association Ltd.  It can also mean “permit”, and in Adelaide Corporation v Australasian Performing Right Association Ltd “authorize” and “permit” appear to have been treated as synonymous.  A person cannot be said to authorize an infringement of copyright unless he has some power to prevent it: Adelaide Corporation v Australasian Performing Right Association Ltd.  Express or formal permission or sanction, or active conduct indicating approval, is not essential to constitute an authorization; “Inactivity or ‘indifference, exhibited by acts of commission or omission, may reach a degree from which an authorization or permission may be inferred’”: Adelaide Corporation v Australasian Performing Right Association Ltd.  However, the word “authorize” connotes a mental element and it could not be inferred that a person had, by mere inactivity, authorized something to be done if he neither knew nor had reason to suspect that the act might be done.  Knox CJ and Isaacs J referred to this mental element in their dissenting judgments in Adelaide Corporation v Australasian Performing Right Association Ltd.  Knox CJ held that indifference or omission is “permission” where the party charged (amongst other things) “knows or has reason to anticipate or suspect that the particular act is to be or is likely to be done”.  Isaacs J apparently considered that it is enough if the person sought to be made liable “knows or has reason to know or believe” that the particular act of infringement “will or may” be done.  This latter statement may be too widely expressed: cf Sweet v Parsley.  It seems to me to follow from these statements of principle that a person who has under his control the means by which an infringement of copyright may be committed — such as a photocopying machine — and who makes it available to other persons, knowing, or having reason to suspect, that it is likely to be used for the purpose of committing an infringement, and omitting to take reasonable steps to limit its use to legitimate purposes, would authorize any infringement that resulted from its use.  Cases such as Mellor v Australian Broadcasting Commission and Winstone v Wurlitzer Automatic Phonograph Company of Australia Pty Ltd are consistent with this view.  Although in some of the authorities it is said that the person who authorizes an infringement must have knowledge or reason to suspect that the particular act of infringement is likely to be done, it is clearly sufficient if there is knowledge or reason to suspect that any one of a number of particular acts is likely to be done, as for example, where the proprietor of a shop installs a gramophone and supplies a number of records any one of which may be played on it: Winstone v Wurlitzer Automatic Phonograph Company of Australia Pty Ltd.

Whether a person authorised an infringing act depends upon the proper inference to be drawn from all the facts of the case.  It is wrong to take from the expression “sanction, approve, countenance” one element, such as “countenance”, and by fixing upon the broadest dictionary meaning of that word to seek to expand the core notion of authorise: Roadshow Films at [125] (Gummow and Hayne JJ).  The facts and circumstances identified in s 36(1A) must be considered, but these do not limit what should be considered: Roadshow Films at [135].  As Gummow and Hayne JJ said (about the cognate subsection in s 101 of the Copyright Act dealing with, particularly, cinematograph films) at [135]:

Section 101(1A) is so drawn as to take an act of primary infringement and ask whether or not a person has authorised that act of primary infringement.  In answering that question there will be “matters” that must be taken into account.  These include, but are not conﬁned to, the matters identiﬁed in paras (a), (b) and (c).  Was there any relationship that existed between the primary infringer and the (alleged) secondary infringer?  If so, what was its nature (para (b))?  Did the secondary infringer have power to prevent the primary infringement; if so, what was the extent of that power (para (a))?  Other than the exercise of that power, did the secondary infringer take any reasonable steps to prevent the primary infringement, or to avoid the commission of that infringement (para (c))?

### C.5.2  Campaigntrack’s submissions in respect of inferences

In addition to the evidence referred to earlier, Campaigntrack relied upon various authorities relevant to the weight which might be given to evidence, the inferences which might be drawn from an absence of evidence and the lines of reasoning which might be employed where a party does not call a witness or is shown to have lost or destroyed relevant evidence.

Campaigntrack relied upon Blatch v Archer and Jones v Dunkel (1959) 101 CLR 298 in submitting:

Campaigntrack and New Litho bought the intellectual property rights in the DreamDesk system from DDPL and relied on Mr Meissner and Mr Semmens to hand over the materials that embodied those rights.  DDPL was the predecessor-in-title.

Mr Semmens was the developer of the DreamDesk system and facts about its development were largely, if not exclusively, in Mr Semmens’ knowledge.

Mr Semmens did not give evidence about his development of the Toolbox system, except for tendering certain material relating to eDocBuilder materials in reply.  The eDocBuilder was not the Toolbox system; at its highest, the eDocBuilder was a system that integrated with the Toolbox system.

RETB, Biggin & Scott, DDPL, Mr Stoner, Ms Bartels and Mr Semmens did not introduce into evidence or discover the project plan for Toolbox referred to in Ms Neal’s email of 1 September 2016.

Mr Semmens did not produce the local computer used to develop the Toolbox system in the period 9 to 20 August 2016, before the first commit to a Git repository.

The persons at DDPL and JGM Advertising who were involved in the planning, development and testing of the Toolbox system (particularly Mr Gallagher, Mr Zhang and Ms Neal) were not called by any of the respondents to give evidence, and the failure to call them was unexplained.  Mr Gallagher and Mr Zhang were available to give evidence, as demonstrated by their responses to subpoenas issued to them.

I do not regard the failure to produce the project plan as particularly significant.  It may be that there was no formal written project plan.  If there had been, it is likely that it would have been referred to in other communications.  I do not, therefore, regard the matter in (4) above as persuasive.

On the other hand, I accept that knowledge of the development of the Toolbox system lay principally with Mr Semmens, Mr Gallagher, Mr Zhang and Ms Neal.  Mr Semmens did not explain the development in a manner which would give confidence, when assessed against that material which the applicant was able to establish, that Toolbox was not developed by reproducing DreamDesk.  I have weighed the applicant’s and respondents’ evidence by reference to that which “it was in the power of one side to have produced, and in the power of the other to have contradicted” – see: Blatch v Archer at [65]; Plaintiff M47/2018 v Minister for Home Affairs (2019) 265 CLR 285 at [40].

Campaigntrack also relied on Rosebanner Pty Ltd v EnergyAustralia (2009) 223 FLR 406 at [455]-[458], in which Ward J described the maxim omnia praesumuntur contra spoliatorem in the following terms:

[455] 	The High Court in Allen v Tobias (1958) 98 CLR 367 at 375, adopted the statement of this maxim given in The Ophelia [1916] 2 AC 206:

If anyone by a deliberate act destroys a document which, according to what its contents may have been, would have told strongly either for him or against him, the strongest possible presumption arises that if it had been produced it would have told against him; and even if the document is destroyed by his own act, but under circumstances in which the intention to destroy evidence may fairly be considered rebutted, still he has to suffer. He is in the position that he is without the corroboration which might have been expected in his case.

[456] 	There is some divergent judicial opinion on the nature of the inference to be drawn, whether it is limited to matters which could likely have been established by the evidence which has been destroyed or withheld or whether presumptions will be raised against the spoliator on all issues which are not otherwise positively proved. Of course, even if the more limited application of the maxim is accepted, adverse inferences as to credit may be drawn from deliberate spoliation of evidence.

[457] 	There is also some historic divergence as to the amount (if any) of “wrongdoing” or fault required to enliven the maxim; ie whether the blameworthiness requires malus animus or mala fides (Delany v Tenison (1757) 1 ER 1559), or whether it is sufficient for the presumption to be available that it cannot be shown that the destruction of evidence was proper or justifiable: Gray v Haig (1855) 52 ER 587.

[458] 	The passage of The Ophelia approved by the High Court would seem to suggest that even bona fide destruction can nevertheless have negative consequences, by stating that even where “the intention to destroy evidence may fairly be considered rebutted, still [the destroyer of evidence] has to suffer. He is in the position that he is without the corroboration which might have been expected in his case”.

The applicant submitted that the reasoning suggested by the maxim omnia praesumuntur contra spoliatorem should be adopted because:

Mr Semmens deleted the migration scripts, instructed by Ms Bartels and Biggin & Scott;

Mr Semmens deleted certain commits and branches from the DreakDesk Git Repository on 28 September 2016, which made it “virtually impossible” to work out what and when certain things happened;

Mr Semmens deleted the RSYNC commands, instructed by Ms Bartels and Biggin & Scott;

Mr Semmens tampered with git_commit_log.txt, on Mr Stoner’s, Biggin & Scott’s and RETB’s instructions;

Mr Semmens edited the eDocBuilder welcome email dated 6 August 2016, on Mr Stoner’s instructions;

Mr Semmens discarded, overwrote and gave away old computers, likely after his receipt of Campaigntrack’s letter of demand;

Mr Semmens deleted his previous “semkins74@gmail.com” Bitbucket account;

Mr Semmens deleted or withheld access to the commits to “The Daves” Bitbucket account;

Mr Semmens deleted emails containing the word “toolbox” from his “semkins74@gmail.com” email account in the period 4 May 2016 to 10 October 2016, being the period in which the Toolbox system was being developed;

Mr Semmens deleted emails from his “david@dreamdesk.com.au” email account in the last two years while this proceeding was on foot;

Mr Meissner deleted emails and other documents in a manner contrary to his stated position of keeping records for seven years; and

Mr Semmens withheld the “david@dreamdesk.com.au” account from Mr Taylor’s forensic preservation process.

As to these matters:

I accept that Mr Semmens deleted the migration scripts: see [104] above.  I do not accept he was instructed to do so by Ms Bartels or Biggin & Scott.  I conclude that the migration scripts merely operated to copy data.  I conclude that Mr Semmens deleted the migration scripts because he did not want Campaigntrack to know that he had copied the data.  There was no infringement of copyright in copying the data.  I do not regard the deletion of the migration scripts as destroying evidence which would have assisted Campaigntrack in establishing its case.

I accept that Mr Semmens deleted certain commits and branches from the DreakDesk Git Repository before he gave Mr Allen access to the repository on 28 September 2016 and that this made it “virtually impossible” to work out what and when certain things happened – see: [113]-[117] above.  I accept that this made it more difficult for Campaigntrack to establish its case.  I infer that the deletion was at least in part implemented to prevent Campaigntrack having available evidence which would disclose that copying of the DreamDesk system or parts of it had taken place.

I accept Mr Semmens deleted the RSYNC commands – see: [127] above.  I do not accept that he was instructed to do so by Ms Bartels or Biggin & Scott.  I conclude that the RSYNC commands which had been carried out merely operated to copy data.  I conclude that Mr Semmens deleted the RSYNC commands because he did not want Campaigntrack to know that he had copied data.  There was no infringement of copyright in copying the data.  I do not regard the deletion of the RSYNC commands as destroying evidence which would have assisted Campaigntrack in establishing its case.

I accept that Mr Semmens altered git_commit_log.txt – see: [153] above.  I do not accept that this was done on the instructions of Mr Stoner, Biggin & Scott or RETB – see: [154]-[156] above.  I accept that Mr Semmens did this for purposes which included preventing Campaigntrack having available evidence which would disclose, or at a minimum from which it could be inferred, that certain copying from the DreamDesk system had taken place.

I accept that Mr Semmens edited the eDocBuilder welcome email – see: [52] above.  I do not accept that this was done on Mr Stoner’s instructions, although I accept that Mr Stoner had wanted his own login.  I do not consider that the editing of this email had the effect of removing evidence which may have assisted Campaigntrack in establishing its case.

I accept that Mr Semmens discarded, overwrote or gave away old computers and that it is likely that he did so either after his receipt of Campaigntrack’s letter of demand or at a time when he considered it desirable in order to make it more difficult for Campaigntrack to establish its case – see: [55] and [164] above.  I accept that the old computers were likely to have contained information relevant to whether there had been an infringement of copyright (or breach of confidence).

I accept that Mr Semmens deleted his previous “semkins74@gmail.com” Bitbucket account in June 2017, after commencement of this proceeding, and that he did not make a backup of its contents before deleting it – see: [159] above.  I accept that this account was likely to have contained information relevant to whether there had been an infringement of copyright (or breach of confidence).

I infer that “The Daves” Bitbucket account was one used by or referring to both Mr Semmens and Mr Gallagher.  The commit log for the Toolbox repository on 26 August 2016 contained multiple references to “The Daves” Bitbucket account.  It is likely that it contained information relevant to Toolbox given that Mr Semmens and Mr Gallagher were both working on the development of Toolbox.  The Bitbucket account was not produced by Mr Semmens to the court appointed expert Mr Taylor.  I conclude that Mr Semmens either deleted or withheld access to the “The Daves” Bitbucket account.  I accept that this account was likely to have contained information relevant to whether there had been an infringement of copyright (or breach of confidence).

It is likely that Mr Semmens deleted emails containing the word “toolbox” from his “semkins74@gmail.com” email account in the period 4 May 2016 to 10 October 2016, being the period in which the Toolbox system was being developed – see: [166] above.

I accept, as Mr Semmens confirmed in cross-examination, that Mr Semmens deleted emails from his “david@dreamdesk.com.au” email account in the last two years while this proceeding was on foot.  I accept that it is likely some of these emails contained information relevant to the proceedings.

I do not accept that Mr Meissner deliberately deleted emails and other documents with an object of removing available evidence or that he did so carelessly or unreasonably; and

I accept that Mr Semmens withheld the “david@dreamdesk.com.au” account from Mr Taylor’s forensic preservation process.  I accept that it is likely some of the emails in this account contained information relevant to the proceedings.

### C.5.3  Mr Semmens

As against Mr Semmens, Campaigntrack’s case was:

First, Mr Semmens reproduced or authorised the reproduction of a substantial part of each of the Source Code Works, the Database Work, the Table Works, the Menu Work and the PDF Works: FASOC [20]-[22], [29]-[31], [38]-[40], [47]-[49], [58]-[60].

Secondly, in the user’s use of the Toolbox system, Mr Semmens authorised the reproduction of a substantial part of the Source Code Works, the Database Work, the Table Works and the Menu Work: FASOC [53]-[57].

Thirdly, in his loading, editing or modification of the Toolbox system, Mr Semmens reproduced a substantial part of the Source Code Works, the Database Work, the Table Works and the Menu Work: FASOC [57A]-[57C], 2nd [57D].

## C.5.3.1  Primary acts of infringement

Mr Semmens was the “main developer” of the Toolbox system.  The first commit to the Toolbox repository was made by him on 26 August 2016 and I conclude he was the sole developer of the Toolbox system up to that time.  I accept that he reproduced a substantial part of the Source Code Works as a whole and of the three PHP files.  I reach this conclusion principally on the basis of the evidence of Mr Taylor which established that identical source code to that in DreamDesk was found in Toolbox.  It is also an inference which arises from the circumstances in which Toolbox was developed, set out in detail above.

Assessing the evidence as a whole, I conclude that Mr Semmens copied the whole or substantial parts of the DreamDesk source code (and system) and then proceeded to modify it or have developers (Mr Gallagher and Mr Zhang) modify it under his supervision.  The modifications included the following:

First, instead of using Process 55, which was based on “PDFLib” and had been used in the DreamDesk system to build the marketing material, Mr Semmens substituted eDocBuilder.  One reason for this was that Mr Semmens’ use of Process 55 in DreamDesk had given rise to the dispute with Digital Hive and Mr Semmens’ acknowledgement that he had improperly used the intellectual property (which included Process 55) of others.

Secondly, unlike DreamDesk he used Laravel as the relevant framework for the source code.  Both DreamDesk and Toolbox were written in PHP.  Laravel is a PHP framework used to develop web applications.  As mentioned, it was established that parts of the source code in Toolbox were identical to source code in DreamDesk.  To the extent that the three PHP files referred to earlier were not entirely identical (in that not all lines of code were present in both the compared files in DreamDesk and Toolbox), those parts which were not identical may have been contained in some other file or location because the Laravel framework required or enabled parts of source code to be located differently to the location in the DreamDesk framework.  The inference arises from Mr Taylor’s report that this occurred.

Thirdly, certain file names were altered and certain code may have been added or substituted.

On balance, I conclude that a reproduction of a substantial part of the DreamDesk source code as a whole occurred at least in early August 2016 when Mr Semmens first began developing Toolbox.  Reproductions also occurred when the Toolbox system then being developed was first committed by Mr Semmens to the Git repository on 26 August 2016.  Reproductions occurred when the system was used, loaded, edited or modified by Mr Semmens during the process of development.  The use of the system caused the source code to be copied into memory and run.  The source code was also copied when a developer downloads source code from, or commits source code to, the Git repository.

As noted earlier, Mr Semmens admitted to running the migration scripts and the RSYNC commands.  Campaigntrack submitted that I should conclude from this that Mr Semmens reproduced the Database Work, the Table Works and the PDF Works.  I do not accept that the running of migration scripts or the RSYNC commands had the effect of reproducing the Database Work, the Table Works or the PDF Works.  Although Campaigntrack repeatedly submitted that it did have this consequence, I understood Campaigntrack ultimately to have accepted that both of these actions had the effect only of copying data.

Nevertheless, I conclude from the evidence as a whole that Mr Semmens reproduced a substantial part of each of the Database Work and the Table Works.  I reach that conclusion on the basis of the similarities between the Database Work and the Table Works in each of the DreamDesk system and the Toolbox system.  The substantial similarities are not explained as mere coincidence or because of the fact that the database and tables contained fields for matters one would expect to see in a database and tables created for the intended functionality, even having regard to the fact that many of the fields were logical and necessary for compatibility with other real estate related applications.  I conclude that Mr Semmens reproduced, for the purposes of the Toolbox system, a substantial part of the structure of the DreamDesk Database Work and Table Works before migrating the relevant data from DreamDesk to Toolbox.

In relation to the PDF Works, I am satisfied that Mr Semmens reproduced the PDF Works which, containing templates, was reproduction of more than mere data.  I accept that, in reproducing the PDF Works as a whole, Mr Semmens infringed copyright.

I do not address the Menu Works because, as noted earlier, Campaigntrack did not discharge its onus of establishing that copyright subsisted in the Menu Works.

## C.5.3.2  Authorisation

Campaigntrack submitted that, in addition to his own acts of infringement, Mr Semmens authorised acts by the other developers of the Toolbox system, Mr Gallagher and Mr Zhang.  Campaigntrack submitted:

As the “main developer” of the Toolbox system, it should be inferred (it was submitted) that he set the direction of the development and gave instructions to the other developers.  It should also be inferred that he provided or shared materials, including parts of the DreamDesk system, to the other developers that were copied by them.

Mr Semmens had direct power to prevent the infringement by, for example, not providing or sharing the DreamDesk system with the other developers, removing those parts of the DreamDesk system to which they had existing access, and by requiring them to develop the Toolbox system in a “clean room” scenario: s 36(1A)(a) of the Copyright Act.

As the main developer, Mr Semmens was in a position of supervision and control over the other developers: s 36(1A)(b).  There is no evidence that Mr Semmens took reasonable steps to prevent or avoid the infringement by the other developers: s 36(1A)(c).

Campaigntrack did not specifically identify what primary acts of infringement by Mr Gallagher and Mr Zhang were said to have been authorised by Mr Semmens.  Nevertheless, it is probable that each of them downloaded the Toolbox software (then being developed) from the Git repository and committed the software to the repository after making alterations.  Given that the Toolbox source code contained in the Git repository during the time it was being developed contained a substantial part of source code reproduced from DreamDesk, it follows that the copies of the Toolbox source code downloaded and uploaded by the developers also effected a reproduction of a substantial part of the DreamDesk source code.  Those reproductions were relevantly authorised by Mr Semmens.

Campaigntrack submitted that “[s]imilar reasoning applies to authorisation of infringements by users using the Toolbox system”.  I infer that Biggin & Scott real estate agents used the Toolbox system when it went “live” and for a period thereafter.  The evidence did not reliably establish what the source code of Toolbox was at that point in time or subsequently.  This was not the fault of Campaigntrack which did what it reasonably could in the circumstances to establish that matter.  Nevertheless, on the basis that earlier versions of Toolbox included substantial parts of DreamDesk source code, and having regard to the failure of Mr Semmens to adduce clear evidence of the final version or versions as used by users, I conclude that – when Toolbox went “live” – it more likely than not contained substantial parts of DreamDesk source code, albeit located differently in a new framework.  At that time, Toolbox was also based, in substantial part, on the DreamDesk database and table structures.

The use of the Toolbox system by users causes the source code to be copied into memory and run.  Given the conclusion that the Toolbox system included substantial parts of DreamDesk source code, it follows that use of Toolbox involved a reproduction of a substantial part of the DreamDesk source code.  This reproduction was relevantly authorised by Mr Semmens.  The reproduction of the Database Works and Table Works, which I infer also occurred through the users’ use of Toolbox, was also relevantly authorised by Mr Semmens.

### C5.4  Biggin & Scott, RETB, Mr Stoner and Ms Bartels

As against Biggin & Scott, Campaigntrack’s case was:

First, Biggin & Scott reproduced or authorised the reproduction of a substantial part of the Database Work, the Table Works and the Menu Work: FASOC [23]-[25], [32]-[34], [41]-[43].

Secondly, Biggin & Scott authorised the reproduction of a substantial part of the Source Code Works, the Database Work, the Table Works and the Menu Work in:

the user’s use of the Toolbox system: FASOC [53]-[57].

the loading, editing or modification of the Toolbox system: FASOC [57A], [57D], 2nd appearing.

As against RETB, Campaigntrack’s case was:

First, RETB reproduced or authorised the reproduction of a substantial part of the Source Code Works, the Database Work, the Table Works and the Menu Work: FASOC [26]-[28], [35]-[37], [44](a)-[46], [50](a)-[52].

Secondly, RETB communicated or authorised the communication of a substantial part of the Source Code Works and the Menu Work: FASOC [44](b)-[46], [50](b)-[52].

Thirdly, RETB authorised the reproduction of a substantial part of the Source Code Works, the Database Work, the Table Works and the Menu Work. in:

the user’s use of the Toolbox system: FASOC [53]-[57];

the loading, editing or modification of the Toolbox system: FASOC [57A]- [57D], 2nd appearing.

As against Mr Stoner and Ms Bartels, Campaigntrack’s case was:

First, they authorised the reproduction of a substantial part of the Database Work and the Table Works: FASOC [60E]-[60F], [60H]-[60I], read with FASOC [20], [23], [26], [29].

Secondly, they authorised the reproduction or communication of a substantial part of the Source Code Works and the Menu Work: FASOC [60E]-[60F], [60H]-[60I], read with FASOC: [38], [41], [44], [47], [50].

Thirdly, they authorised the reproduction of a substantial part of the Source Code Works, the Database Work, the Table Works and the Menu Work in:

the user’s use of the Toolbox system: FASOC [60E]-[60F], [60H]-[60I], read with FASOC [53], [54], [56].

the loading, editing or modification of the Toolbox system: FASOC [60E]-[60F], [60H]-[60I], read with FASOC [57B].

## C.5.4.1  Primary acts of infringement

The principal primary acts of infringement on the part of Biggin & Scott and RETB were alleged to be those carried out by Mr Semmens.  Campaigntrack submitted that Mr Semmens acted as agent of Biggin & Scott and RETB:

The instruction letter to Mr Semmens dated 3 August 2016 was sent on Biggin & Scott letterhead and was signed by Mr Stoner as CEO.  Mr Semmens proceeded to develop the Toolbox system.

Noting that Mr Semmens had admitted to commencing as a contractor to RETB on 15 September 2016, it should be concluded that Mr Semmens continued to develop the Toolbox system as an agent of RETB.

Mr Semmens’ primary acts of infringement in developing the Toolbox system should therefore “be attributed to” Biggin & Scott and RETB.

I do not accept that Mr Semmens was acting as “agent” of Biggin & Scott or RETB.  I conclude that he was contracted to produce a new system.  I do not attribute Mr Semmens’ acts of infringement to Biggin & Scott or RETB.  I address below, when dealing with the authorisation case, a contention that RETB communicated (or authorised the communication of) a substantial part of the Source Code Works and the Menu Work.

## C.5.4.2  Authorisation by Biggin & Scott, RETB, Mr Stoner and Ms Bartels

Campaigntrack submitted that Biggin & Scott, RETB, Mr Stoner and Ms Bartels authorised the infringements of the developers and users of the Toolbox system, for the following reasons:

Mr Stoner and Biggin & Scott issued the instruction letter of 3 August 2016 to Mr Semmens.  RETB did not issue any written instructions to Mr Semmens, but it should be inferred that RETB simply adopted the instructions previously given by Mr Stoner and Biggin & Scott.  Mr Stoner and Ms Bartels (and through them, Biggin & Scott and RETB) knew that there was a real risk that, in developing the system, Mr Semmens might infringe the intellectual property rights of DDPL or Campaigntrack.  That risk was heightened by the fact that Mr Stoner and Ms Bartels knew that the Toolbox system was developed by DDPL and JGM Advertising staff, in DDPL/JGM Advertising’s offices.  The risk was also heightened by the very compressed two-month development timeframe they had imposed on Mr Semmens.  It was also heightened by the low cost that they incurred to get the system to “stage 1”, being the stage whereby Biggin & Scott could use the system to do their “normal day-to-day functions”.  Mr Stoner said he asked Mr Semmens for an assurance that Mr Semmens complied with the instruction letter “probably … every two days” and “constantly”: s 36(1A)(c) of the Copyright Act.  Although there was no evidence of this in Mr Stoner’s or Mr Semmens’ affidavits, if it was true, this shows that Mr Stoner had a heightened and constant awareness of the risk of infringement.  Mr Stoner did not give evidence of Mr Semmens’ responses.  Given that Mr Stoner had to ask for assurance repeatedly, it can be inferred that Mr Semmens’ responses did not abate Mr Stoner’s concerns.

Mr Stoner and Ms Bartels (and through them, Biggin & Scott and RETB) repeatedly said they left it to Mr Semmens to develop and run the Toolbox system, including determining its specifications.  Ms Bartels also left it to Mr Semmens to move the data away from the DreamDesk system.  Ms Bartels was involved in monitoring, supervising and participating in the development of the Toolbox system.  Mr Stoner left that to Ms Bartels.  Mr Stoner and Ms Bartels (and through them, Biggin & Scott and RETB) had power to prevent the infringements of the developers and users of the Toolbox system, including by not developing the system, instructing a different developer or using another system (for example: Campaigntrack, Excel or RealHub): s 36(1A)(a).

Biggin & Scott and RETB (and their officers, Mr Stoner and Ms Bartels) were in a contractual relationship with Mr Semmens; they were the commissioning parties, he the developer: s 36(1A)(b).  They had power to instruct him and specify what system he was to build.

Neither Mr Stoner nor Ms Bartels (nor Biggin & Scott nor RETB) conducted any independent audit or verification that the system developed for them did not infringe another company’s intellectual property rights: s 36(1A)(c).  Mr Stoner’s explanation – namely that he did not have the code for the DreamDesk system and did not know Mr Semmens had the code – should be rejected given his other evidence that Mr Stoner knew Mr Semmens was the head developer for DreamDesk.  There was no evidence that Mr Stoner, Ms Bartels, Biggin & Scott or RETB took any other steps to prevent or avoid infringement by the developers and users of the Toolbox system: s 36(1A)(c).

Mr Stoner instructed Mr Semmens to “tamper” with git_commit_log.txt and edit the eDocBuilder welcome email, to convey a false impression to Campaigntrack and hide evidence of infringement.

Mr Stoner paid Mr Semmens’ invoices for the development of the Toolbox system.  Ms Bartels paid for the AWS invoice used to host the Toolbox system.

Mr Stoner, Biggin &Scott or RETB either paid for or loaned money to Mr Semmens for his legal fees.  REDHQ made a further loan to Mr Semmens for his legal fees.

As to these matters:

The instruction letter was issued to Mr Semmens on 3 August 2016.  As noted at [43] above, in the context of the events which had occurred, including the fact that – to Mr Stoner’s knowledge – Mr Semmens had admitted to using Process 55 in developing DreamDesk, it was hardly surprising that Mr Stoner would seek an assurance from Mr Semmens that he would not infringe the intellectual property rights of others in building a new web to print delivery system.  I am satisfied that Mr Stoner trusted Mr Semmens not to infringe the intellectual property rights of DDPL or Campaigntrack in developing the new system.  I conclude that Mr Stoner did not want Mr Semmens to misuse intellectual property belonging to others in developing the new system.  I reach the same conclusion with respect to Ms Bartels.  Mr Stoner and Ms Bartels knew that the software was being developed by DDPL (and by staff who had been or were staff of JGM Advertising), in DDPL or JGM Advertising’s offices.  I do not regard that as establishing, either of itself or cumulatively with other circumstances, authorisation of infringement.  Mr Stoner and Ms Bartels considered Mr Semmens to be a person who had the relevant expertise in building a software system with the relevant functionality.  They considered he could build the system in sufficient time given his expertise.  I conclude that they wanted him to do so and to do so without infringing the intellectual property rights of others.

It is not unusual that Mr Stoner and Ms Bartels left the development of the system to Mr Semmens.  The decision to use Mr Semmens rather than some other person or entity was not surprising.  As mentioned, they knew Mr Semmens had the relevant expertise and familiarity with the kind of product that they wanted.  He was a logical choice for developing the software in the required timeframe, at least provided they were satisfied he would develop the system without infringing the intellectual property rights of others.

I accept that Biggin & Scott and Mr Semmens were in a contractual relationship and that Biggin & Scott could instruct Mr Semmens.  The instructions given were, in essence, to build a computer system with functionality equivalent to DreamDesk and to do so without infringing any person’s intellectual property rights.

I accept that neither Mr Stoner nor Ms Bartels (nor Biggin & Scott nor RETB) conducted any independent audit or verification that the system developed for them did not infringe another company’s intellectual property rights.  However, I do not regard this as establishing, either of itself or cumulatively with other circumstances, authorisation of infringement.  Rather, that is a reflection of the facts that: an instruction had been given not to infringe intellectual property rights; each of Mr Stoner and Ms Bartels trusted there would be no infringement; in all likelihood, neither turned their mind to whether an independent audit should be carried out; and a lack of ready means to carry out an independent audit in the time frame which would have been required.

I do not accept that Mr Stoner instructed Mr Semmens to “tamper” with git_commit_log.txt.  I also do not accept that Mr Stoner instructed Mr Semmens to edit the eDocBuilder welcome email.

I accept that Mr Stoner paid Mr Semmens’ invoices for the development of the Toolbox system and that Ms Bartels paid for the AWS invoice used to host the Toolbox system.  That was to be expected given that Biggin & Scott was instructing Mr Semmens to create a new system.

I accept that Mr Stoner, Biggin & Scott or RETB either paid for or loaned money to Mr Semmens for his legal fees in connection with these proceedings and that REDHQ made a further loan to Mr Semmens for his legal fees.  This is not surprising.  Mr Stoner, Ms Bartels and Mr Semmens were friends.  A successful defence of the proceedings by Mr Semmens would mean that any authorisation case against Mr Stoner, Biggin & Scott and RETB would also fail.  I infer that Mr Semmens was unable to fund legal representation.  I do not regard the assistance given to Mr Semmens as indicating that those who assisted Mr Semmens had earlier authorised him to infringe Campaigntrack’s intellectual property rights.

It was contended that RETB communicated (see [295] above) or authorised the communication of a substantial part of the Source Code Works and the Menu Work.  To the extent communications of a substantial part of the source code were made, Mr Semmens was the person responsible for determining the content of the communications – see: s 22(6) of the Copyright Act.  RETB did not relevantly communicate a substantial part of the source code or “authorise” such a communication.

It was also contended that RETB, Biggin & Scott, Mr Stoner and Ms Bartels authorised the reproduction of a substantial part of the Source Code Works, the Database Work, the Table Works and the Menu Work.  RETB, Biggin & Scott, Mr Stoner and Ms Bartels did not relevantly authorise reproduction of any of the works in issue, either through the user’s use of the Toolbox system or the loading, editing or modification of the Toolbox system.

As noted in the passage from Moorhouse, extracted at [270] above, authorisation connotes a “mental element” and it might be difficult to infer authorisation where the relevant person “neither knew nor had reason to suspect that the act might be done”.  It has not been established that RETB, Biggin & Scott, Mr Stoner or Ms Bartels knew (or that they should reasonably have known) that any of the works had been reproduced in the Toolbox system or that they knew that use by users or the loading, editing or modification of the Toolbox system by developers or others might involve reproduction of a substantial part of the DreamDesk system.  This is not a case where the act of using the Toolbox system was known necessarily to involve an act of reproduction, such as might be the case in providing a photocopier for the purpose of copying library books.  I am not satisfied that Biggin & Scott, RETB, Mr Stoner or Ms Bartels relevantly authorised any infringement, whether of Mr Semmens or of other developers or users.

### C.5.5  DDPL and Mr Meissner

As against DDPL and Mr Meissner, Campaigntrack’s case was that they authorised the reproduction of a substantial part of the Database Work, the Table Works and the PDF Works: FASOC [22A]-[22C], [31A]-[31C], [60A]-[60C].

## C.5.5.1  Primary acts of infringement

Although the case was not pleaded, Campaigntrack submitted that, in moving data from the DreamDesk system, Mr Semmens acted as an agent for DDPL and Mr Meissner.  Campaigntrack referred to Mr Semmens’ evidence that Mr Meissner “would have just said give the client their data”.  From this starting point, Campaigntrack submitted that Mr Semmens’ primary acts of infringement in moving data from the DreamDesk system should be attributed to DDPL and Mr Meissner.  The copying of data was not a pleaded act of infringement and the case was ultimately run on the basis that the mere copying of data was not capable of infringing copyright.

Campaigntrack has not made out any pleaded primary act of infringement on the part of DDPL or Mr Meissner.

## C.5.5.2  Authorisation by DDPL and Mr Meissner

Campaigntrack submitted that DDPL and Mr Meissner authorised the infringements of the Database Work, the Table Works and the PDF Works for the following reasons:

DDPL and Mr Meissner participated in the development of Toolbox through DDPL and JGM Advertising providing staff and resources used to develop the Toolbox system.  DDPL and JGM Advertising paid those staff for their work.

Mr Meissner (and through him, DDPL) instructed Mr Semmens to “give the client their data” and left it to Ms Neal and Mr Semmens to determine when and how the DreamDesk system was going to be turned off.

DDPL or JGM Advertising paid for certain AWS invoices used to host the Toolbox system.

DDPL and Mr Meissner had power to prevent the infringements, including by not engaging the DDPL and JGM Advertising staff to develop the Toolbox system, by not paying for that work and by not paying for the AWS invoices: s 36(1A)(a) of the Copyright Act.

DDPL and Mr Meissner were in an employment (or alternatively consultancy) relationship with Mr Semmens and the other developers: s 36(1A)(b).  Under that relationship, DDPL and Mr Meissner were in the position of employer or principal and could issue instructions.  Mr Semmens followed Mr Meissner’s instructions in relation to the handover of the DreamDesk system.

DDPL and Mr Meissner took no steps to prevent or avoid the infringements of the Database Work, the Table Works and the PDF Works, in the development of the Toolbox system or in the moving data away from the DreamDesk system: s 36(1A)(c).

As to these matters:

I accept that DDPL and Mr Meissner participated in the development of Toolbox through DDPL and JGM Advertising, including by providing staff and resources used to develop the Toolbox system.  Mr Meissner made it plain in his evidence that he was shocked to discover that Mr Semmens had used Process 55 in the development of DreamDesk.  I do not accept that, having been surprised in that way, and having been effectively forced to sell the intellectual property rights in DreamDesk, he then participated in developing a new system, in competition with the purchaser of DreamDesk, in a way which infringed the intellectual property rights just transferred.

Mr Meissner’s (and through him, DDPL’s) instruction to Mr Semmens to “give the client their data” was not an authorisation to infringe intellectual property rights.  I do not regard the manner in which Mr Meissner left Ms Neal and Mr Semmens to turn the DreamDesk system off to indicate an authorisation to infringe intellectual property rights.  It should also be observed that Mr Meissner was overseas for a substantial part of the relevant events, and although he was contactable at least by email, contact was likely to have been sporadic and difficult at various times.

I accept that DDPL or JGM Advertising paid for certain AWS invoices used to host the Toolbox system.  I do not regard that as establishing authorisation to infringe intellectual property rights, either of itself or cumulatively with other circumstances.

I accept that DDPL and Mr Meissner had power to prevent the infringements, including by not engaging the DDPL and JGM Advertising staff to develop the Toolbox system, by not paying for that work and by not paying for the AWS invoices: s 36(1A)(a).  However, I do not accept that Mr Meissner believed that infringements were occurring or that there was anything to prevent.

I do not accept that Mr Semmens was an employee of either DDPL or Mr Meissner.  Mr Semmens was contracted by DDPL.  I accept that DDPL, and Mr Meissner as DDPL’s controller, could issue instructions to Mr Semmens.  I do not accept that instructions were issued to Mr Semmens in terms, express or implied, which requested or required him to infringe any person’s intellectual property rights.  Indeed, I conclude that it was understood by Mr Semmens that Mr Meissner wanted no such thing to occur given the events which had unfolded before the development of the Toolbox system.

I accept that DDPL and Mr Meissner took no steps to prevent or avoid the infringements of the Database Work, the Table Works and the PDF Works, in the development of the Toolbox system or in the moving of data away from the DreamDesk system: s 36(1A)(c).  I conclude that Mr Meissner did not know of any events which called for his (or DDPL’s) intervention.  Mr Semmens had the relevant expertise to develop a new system.  Mr Meissner did not.  Mr Meissner knew that Mr Semmens had admitted to improperly using the intellectual property of others in developing DreamDesk.  In the circumstances, it was reasonable for Mr Meissner to take the view that Mr Semmens would not engage in such conduct again.  The circumstances known to Mr Meissner did not call for some active audit or investigation on his part during the process of development of Toolbox.

The authorisation case against DDPL and Mr Meissner is not made out.

# D  CONFIDENTIAL INFORMATION CLAIMS

Campaigntrack alleged that Mr Semmens, Biggin & Scott, RETB, Mr Stoner and Ms Bartels misused confidential information, being the source code for DreamDesk as a whole or individual source code files: FASOC [106], [110], [113].  It was alleged that Mr Semmens used the information in the development of Toolbox and that each of the other respondents knew or ought to have known that the source code was confidential information of Campaigntrack and New Litho and that the information was used in the development and use of Toolbox: FASOC [107], [112].  The use of the information was alleged to be unauthorised.

Campaigntrack also alleged that the Database Tables and the DreamDesk Database were, and contained, Campaigntrack’s confidential information: FASOC [115].  It was alleged that Mr Semmens copied at least part of the Database Tables and the DreamDesk Database and that he did so at the direction of Mr Meissner, knowing that the information was confidential information.  It was alleged that the Database Tables and the DreamDesk Database were used by Mr Semmens in the development of Toolbox.  It was alleged that each of the other respondents knew the information was confidential information and that each of them knew or ought to have known that the information was used in the development of Toolbox: FASOC [119] to [120B].  It was alleged that each of the respondents misused Campaigntrack’s confidential information.  In so far as the allegations concerned DDPL and Mr Meissner, it was alleged in the alternative that, if they were not directly guilty of misuse of confidential information, they were liable as joint tortfeasors with, and were vicariously responsible for the misuse of confidential information by, Mr Semmens: FASOC [125].  This alternative case hinged upon an allegation that Mr Semmens’ conduct was performed as the servant or agent of Mr Meissner and DDPL or “pursuant to a common design or in concert with” DDPL and Mr Meissner: FASOC [124].

An equitable remedy for breach of confidence will ordinarily be available if confidential information was imparted or obtained in circumstances importing an obligation of confidence and there has been an unauthorised use of that information or an unauthorised use is threatened: Australian Broadcasting Corporation v Lenah Game Meats Pty Ltd (2001) 208 CLR 199 at [30]; Coco v A N Clark (Engineers) Ltd [1969] RPC 41 at 47.

The relevant principles were broadly agreed upon by the parties.  They were recently summarised by Moshinsky J in IPC Global Pty Ltd v Pavetest Pty Ltd (2017) 122 IPR 445:

[189] 	As Finn, Sundberg and Jacobson JJ stated in Optus Networks Pty Ltd v Telstra Corporation Ltd (2010) 265 ALR 281; [2010] FCAFC 21 at [39], the cause of action for breach of confidence has four elements:

(a) 	the information in question must be identified with specificity;

(b) 	it must have the necessary quality of confidence;

(c)	it must have been received by the respondent in circumstances importing an obligation of confidence; and

(d) 	there must be an actual or threatened misuse of the information without the applicant’s consent.

[190] 	The Full Court referred to Smith Kline & French Laboratories (Australia) Ltd v Secretary, Department of Community Services and Health (1990) 22 FCR 73 at 87; 95 ALR 87 at 102–3; 17 IPR 545 at 560–1 per Gummow J. See also Coco v AN Clark (Engineers) Ltd (1968) 1A IPR 587 at 590–1; [1968] FSR 415; [1969] RPC 41 at 47–8; Australian Medic-Care Company Ltd v Hamilton Pharmaceutical Pty Ltd (2009) 261 ALR 501; [2009] FCA 1220 at [632]–[634] per Finn J; Leica Geosystems Pty Ltd v Koudstaal (No 3) (2014) 109 IPR 1; 245 IR 422; [2014] FCA 1129 (Leica Geosystems) at [47]–[48] per Collier J.

[191] 	In relation to the first of the above elements, in O’Brien v Komesaroff (1982) 150 CLR 310; 41 ALR 255, Mason J (with whom Murphy, Aickin, Wilson and Brennan JJ agreed) said (at CLR 326; ALR 266) that “the respondent has consistently failed to identify the particular contents of the documents which he asserts constitute information the confidentiality of which he is entitled to protect. The consequence is that he has failed to formulate a basis on which the court could grant him relief on the assumption that some part or parts of the documents constitute confidential information.”

[192]	In Leica Geosystems, Collier J referred to the observations of Kirby P in Wright v Gasweld Pty Ltd (1991) 22 NSWLR 317; 20 IPR 481, where his Honour identified certain factors relevant to a determination as to whether information is of a confidential nature. Kirby P said (at NSWLR 334; IPR 498–9):

Determining what is confidential involves a decision on a question of fact in each case where that quality is asserted. Considerations which courts have found to be relevant, in particular cases, in determining this question include:

(a) 	The fact that skill and effort was expended to acquire the information ...

(b) 	The fact that the information is jealously guarded by the employer, is not readily made available to employees and could not, without considerable effort and/or risk, be acquired by others ...

(c) 	The fact that it was plainly made known to the employee that the material was regarded by the employer as confidential ...

(d) 	The fact that the usages and practices of the industry support the assertion of confidentiality ... and

(e) 	The fact that the employee in question has been permitted to share the information only by reason of his or her seniority or high responsibility within the employer’s organisation ...

(Case references omitted.)

[193] 	In relation to the third element set out above (the information must have been received by the respondent in circumstances importing an obligation of confidence), in Del Casale v Artedomus (Aust) Pty Ltd (2007) 73 IPR 326; 165 IR 148; [2007] NSWCA 172, Campbell JA (with whom McColl JA agreed), said (at [133]):

The circumstances have to be such that the court can conclude it would have been clear to a reasonable person, on reasonable grounds, that he or she was not free to deal with the information as his or her own, or could only deal with it subject to certain limitations.

I observe that the factors identified by Kirby P set out in the passage extracted in IPC Global at [192] above are not confined or necessarily relevant to the question of whether the information is of a confidential nature.  The matters are, nevertheless, relevant more broadly, including to the question whether the information was imparted or obtained in circumstances importing an obligation of confidence.

Equity will not ordinarily intervene for breach of confidence where there is an adequate remedy at law.  In Streetscape Projects (Australia) Pty Ltd v City of Sydney (2013) 85 NSWLR 196 at [150], Barrett JA (with Meagher and Ward JJA agreeing) examined the extent to which an action for breach of confidence will be available where there are contractual obligations covering the same topic:

There is a question whether an equitable duty of confidence arises against one party and in favour of another where those parties have given and received contractual promises of confidentiality creating equal or greater protection of the same subject matter. The Full Court of the Federal Court, in Optus Networks Pty Ltd v Telstra Corporation Ltd [2010] FCAFC 21; (2010) 265 ALR 281, decided that the two kinds of obligation could co-exist (reference was there made to an earlier case in which a contractual duty was described as “parasitic upon” the equitable duty: Australian Medic-Care Company Ltd v Hamilton Pharmaceuticals Pty Ltd [2009] FCA 1220; (2009) 261 ALR 501 at [628] and [629]). The contrary view was taken by Gordon J in Coles Supermarkets Australia Pty Ltd v FKP Ltd [2008] FCA 1915 at [63], citing the observation of Campbell JA in Del Casale v Artedomus (Aust) Pty Ltd [2007] NSWCA 172; (2007) 73 IPR 326 at [118] that, if there is a contractual obligation covering the topic, there is no occasion for equity to intervene to impose its own obligation (Campbell JA, as a judge of the Equity Division, had expressed similar views in AG Australia Holdings Ltd v Burton [2002] NSWSC 170; (2002) 58 NSWLR 464 at [75] and Mid-City Skin Cancer & Laser Centre Pty Ltd v Zahedi-Anarak [2006] NSWSC 844; (2006) 67 NSWLR 569 at [155]). The approach preferred by Gordon J and Campbell JA accords with the residual nature of the equitable duty as recognised by Deane J in Moorgate Tobacco Company Ltd v Philip Morris Ltd (No 2) at 437–438. Deane J referred to “the equitable jurisdiction to grant relief against an actual or threatened abuse of confidential information not involving any tort or any breach of some express or implied contractual provision, some wider fiduciary duty or some copyright or trade mark right” (emphasis added). It is also consistent with the notion of equity’s “supplementing” role discussed above in relation to fiduciary duties.

In Optus Networks Pty Ltd v Telstra Corporation Ltd (2010) 265 ALR 281, the Full Court held that contractual remedies could co-exist with the equitable duty of confidence where it was possible that common law remedies would not be sufficient:

[34] 	Telstra placed reliance on the observations of Gordon J in Coles Supermarkets Australia Pty Ltd v FKP Ltd [2008] FCA 1915 at [63] (Coles Supermarkets) where her Honour rejected an argument that equitable and legal obligations of confidence can co-exist in reliance on Del Casale v Artedomus (Aust) Pty Ltd (2007) 73 IPR 326; [2007] NSWCA 172 at [118]. There Campbell JA said that “If there was a contractual obligation that covered the topic, there would, of course, be no occasion for equity to intervene to impose its own obligation”. However that does not cover the present case, where Optus wishes to be able to seek an account of profits, and the question is whether the contract permits that. In our view cll 15.6 and 20.22 show that it does.

[35] 	Gordon J relied on Deta Nominees Pty Ltd v Viscount Plastic Products Pty Ltd [1979] VR 167 at 195 for the proposition that equity does not intervene where there is an adequate remedy at law. There Fullagar J, having found that certain confidential information was in the eyes of equity the plaintiff’s property, who was entitled to restrain the defendants from using the information beyond certain limits, went on to say that because the plaintiff was entitled by reason of contract to perpetual injunctions restraining the defendants from manufacturing the goods to which the information related, equity would withhold any further relief for breaches of confidence because the remedies derived from contract were adequate. Those observations are not applicable to the present case because, at this stage, it is not known whether damages will be an adequate remedy. Again, we refer to the contemplation in cl 15.6 that an account of profits is available under the agreement, and to cl 20.22.

…

[38] 	The notion that no equitable duty of confidence arises where there is a comparable contractual duty is opposed to much authority. Dr Dean says that “Equitable protection … may be used in preference to an existing contractual obligation or alongside a contractual obligation”: R Dean, The Law of Trade Secrets and Personal Secrets, 2nd ed, Lawbook, Pyrmont, 2002, at [2.55] where many examples in the case law are recorded. They include Morison v Moat (1851) 9 Hare 241; Robb v Green [1895] 2 QB 315; Mense v Milenkovic [1973] VR 784; Attorney-General v Jonathan Cape Ltd [1976] QB 752 and Nicrotherm Electrical Co Ltd v Percy (1957) 74 RPC 207. See also Australian Medic-Care Co Ltd v Hamilton Pharmaceuticals Pty Ltd (2009) 261 ALR 501; [2009] FCA 1220 at [628]–[629] (Australian Medic-Care) per Finn J and F Gurry, Breach of Confidence, Clarendon Press, Oxford, 1984, pp 39–46.

I accept that Mr Semmens misused confidential information to the extent the claims in copyright are made out against him.  The source code as a whole, the three individual PHP files, the Database Work, the Table Works and the PDFs constituted confidential information.  It does not matter to the claim for breach of confidence that the source code and other works was created or authored by Mr Semmens rather than imparted to him by Campaigntrack.  Mr Semmens knew that the intellectual property associated with DreamDesk, including the source code and other works mentioned, was owned by DDPL and had been sold by DDPL to Campaigntrack.  Mr Semmens held a copy of the source code and other information in circumstances which imposed an obligation of confidence; it was clear to Mr Semmens (and would have been clear to a reasonable person in his position) that he was not free to deal with the information as his own.

Section 115(2) of the Copyright Act provides that the court may grant an injunction and either damages or an account of profits as relief for an infringement of copyright.  Whether any relief should be granted for breach of confidence depends on the relief which should be granted in relation to the legal claims.  I would observe in this regard that the claim for breach of confidence appears to have been advanced in the exclusive jurisdiction, not in the auxiliary jurisdiction as an aid to contractual rights.

I do not accept that any of the other respondents knew Mr Semmens misused confidential information or used Campaigntrack’s confidential information in the development of Toolbox or that any of them misused Campaigntrack’s confidential information.  I do not accept that DDPL and Mr Meissner were “vicariously liable” for Mr Semmens’ breach of confidence or that they had some “common design” or acted “in concert with” Mr Semmens.  Mr Semmens was not an employee of DDPL or Mr Meissner and his breach of confidence was not contemplated, directed or authorised by DDPL or Mr Meissner.  There was no relevant “common design”.  Neither Mr Meissner nor DDPL wanted any misuse (or use at all) of Campaigntrack’s confidential information.  No reasoned basis was articulated by Campaigntrack for recognition of “vicarious liability” in relation to Mr Semmens’ breach of confidence.

# E  CONTRACT CLAIMS

## E.1  The “transfer term” and “assistance term”

The DreamDesk sale agreement included the following terms addressing, respectively, transfer and assistance:

1.5. 	Dream Desk will provide to the Purchasers any document or equipment required by it to effect a transfer of the Intellectual Property on payment of the Purchase Price by the Purchasers.

1.6. 	On payment of the Purchase Price Dream Desk will provide all reasonable assistance that the Purchasers require so as to properly and effectively use, exploit and understand the Intellectual Property, including the imparting of knowledge and the provision of the following information:

1.6.1. 	Amazon Webservices Password

1.6.2. 	Administrator Password to Dream Desk Platform

1.6.3. 	Management Password for Dream Desk

1.6.4. 	Any client logins as requested

1.6.5. 	Any other passwords and access details required for the day-to[-]day operation of Dream Desk

1.6.6. 	Any other passwords and access details required for the management and configuration of Dream Desk

1.6.7. 	Technical and programming assistance as required

These provisions must be read in light of the agreement as a whole.  They are intended to facilitate cll 1.1 and 1.4 which provided:

1.1. 	Dream Desk agrees that it will sell to Campaigntrack and New Litho (the “Purchasers”) the DreamDesk Platform and all intellectual property associated with the operation of the DreamDesk Business, including copyright (including any rights to source code), design, patents and trademarks and all rights to the business name of the DreamDesk Business and all domain names registered by Dream Desk, including dreamdesk.com.au (the [“]Intellectual Property”).

…

1.4. 	All rights, entitlement and interest in and title to the Intellectual Property will pass to the Purchasers on payment of the Purchase Price.

Campaigntrack alleged that, by certain letters, it requested:

assistance from DDPL “to properly and effectively exploit the DreamDesk Copyright Works in this proceeding”; and

the execution of a written assignment of copyright to the extent that DDPL’s ownership was equitable: FASOC [76].

Campaigntrack alleged that these terms were breached by DDPL failing to provide assistance as requested: FASOC [77]-[78].

Campaigntrack’s claim is not made out:

I am not satisfied DDPL failed to provide “assistance” of a kind to which cl 1.6 was directed.  McLean & Associates wrote to Mr Meissner on 31 July 2017 requesting him to provide documents and information, including lists of persons engaged in the development of DreamDesk, for use in these proceedings.  This is not the kind of assistance contemplated by cl 1.6 of the DreamDesk sale agreement.  It was not assistance requested or required properly to exploit the intellectual property.  The request for information, repeated on a number of occasions, was in the nature of a request for discovery and directed to pursuit of the proceedings as then constituted, not exploitation of copyright.  Further, contrary to Campaigntrack’s submission, breach of the “assistance term” is not established by reason of the fact that Mr Meissner was aligned with the other respondents in the proceedings or by his involvement in REDHQ.

Campaigntrack owned copyright in the source code for the DreamDesk system as a whole and in the three PHP files.  Contrary to Campaigntrack’s submission, the fact that Mr Semmens continued to hold copies of the DreamDesk system does not establish breach of the “transfer term”.

## E.2  The “assignment term” and “transfer warranty”

These claims do not arise because they are based on an assumption that DDPL was not, at the time of sale, the owner of the copyright in the relevant intellectual property.  I have concluded that it was.

## E.3  The “password term”

Campaigntrack pleaded that:

It was a term of the DreamDesk Agreement that on payment of the purchase price DDPL would provide all reasonable assistance that the Applicant and New Litho required so as to properly and effectively exploit the Dream Desk Intellectual Property, including by the provision of the following passwords (the Passwords):

(a) 	Amazon Webservices Password;

(b) 	Administrator Password to Dream Desk Platform;

(c) 	Management Password for Dream Desk;

(d) 	Any other passwords and access details required for the day-to[-]day operation of Dream Desk; and

(e) 	Any other passwords and access details required for the management and configuration of Dream Desk,

(the Password Term).

Campaigntrack alleged that the password term was breached because the passwords were not provided “on payment of the purchase price”: FASOC [90].

The purchase price was paid around 7 September 2016.  Mr Meissner was overseas at the time.  The first request for the passwords relied on by Campaigntrack was made on 19 September 2016.  Mr Meissner wrote to Mr Semmens on 20 September 2016 asking him to supply the passwords to Campaigntrack and to provide assistance.  Mr Semmens provided passwords and log-in details on 20, 22 and 23 September 2016.  The second request relied on, which related only to the Amazon web server, was made on 27 September 2016.  Mr Semmens provided access to the Amazon account on 28 September 2016.

Mr Meissner and DDPL admitted in their defence that “there was a delay of about one week in handover”.  Mr Meissner and DDPL submitted that there was no breach because the passwords and access were given promptly when requested.  Campaigntrack submitted that it was not open to make the submission that there was no breach in light of the pleadings which admitted that the passwords were not provided on payment of the purchase price.

The admitted term was that, on payment of the purchase price, DDPL would provide “all reasonable assistance … including by the provision of [various] passwords”.  Breach is not established merely because the passwords were not provided on payment of the purchase price.  DDPL provided reasonable assistance by providing the passwords reasonably promptly after they were requested.  It was reasonable assistance which was to be provided on payment of the purchase price.  The term (and the agreement more generally) must be interpreted in light of the context known to both parties and in accordance with what would be understood by commercial business people.  Campaigntrack had purchased the intellectual property in order to shut DreamDesk down.  That would not occur immediately because Campaigntrack had granted a licence-back.  There was no apparent urgent need for the passwords to be provided on payment of the purchase price.  Reasonable assistance was provided by DDPL on and after payment of the purchase price, including by providing the relevant passwords.

## E.4  The “non-modification term”

Campaigntrack pleaded (and DDPL and Mr Meissner admitted) that:

[i]t was an implied term of the DreamDesk Agreement that on payment of the purchase price, DDPL and Mr Meissner would effect a transfer of the DreamDesk Intellectual Property as it existed as at the date of the DreamDesk Agreement, including without further modification (the Non-Modification Term).

Particulars

(i) 	The Non-Modification Term is implied by fact and/or by law.

Campaigntrack pleaded at [94] of the FASOC:

DDPL failed to effect a transfer of the DreamDesk Intellectual Property as it existed as at the date of the DreamDesk Agreement and engaged in, or authorised, the further modification of the DreamDesk Intellectual Property.

Particulars

(i) 	On or around 16 August 2016, migration scripts were created on the DreamDesk server for each of the Database Tables. The migration scripts and all development history were deleted from the Git Repository on or about 28 September 2016.

(ii) 	The audit logs on DreamDesk were deleted to remove reference to the synchronisation by rsync on or about 5, 6 and 10 October 2016.

(iii) 	Further particulars will be provided during the course of these proceedings and after discovery and other processes have taken place.

There is no dispute that DDPL transferred the source code as a whole.  Mr Meissner and DDPL submitted:

as to source code, what was agreed to be transferred was only copyright in the source code as a whole in the form it existed at the date of the agreement;

the date of the agreement was 5 September 2016;

the agreement was not to transfer copyright in each and every historical “version” that may have existed or that could otherwise be extracted from any repositories, logs, files or servers, because (amongst other things) they were not “referenced in the contract”.

As to these matters:

what was agreed to be transferred included copyright in the source code as a whole and “all intellectual property associated with the operation of the DreamDesk Business”;

the date of the agreement was 18 July 2016, the agreement being later amended;

historical versions of the source code, and versions which post-dated 18 July 2016, constituted “intellectual property associated with the operation of the DreamDesk Business”.  It is to be recalled that DreamDesk continued to use the software for existing clients after the date of agreement under the “licence-back”.  The admitted implied term must be understood in this context, namely that DDPL would continue to use the intellectual property for the period of the licence-back.

This aspect of the case was principally directed to a complaint that modifications were made after 18 July 2016 to “intellectual property associated with the operation of the DreamDesk Business”, namely the running of migration scripts and the deleting of development history and certain audit logs – see particulars extracted at [329] above.

I am satisfied that the migration scripts (which were created on the DreamDesk server), the development history and the audit logs were part of the “intellectual property associated with the operation of the DreamDesk Business”.  None of these were shown to have existed as at the date of the agreement, namely 18 July 2016.

I am satisfied that modifications were made by Mr Semmens to “intellectual property associated with the operation of the DreamDesk Business” after 18 July 2016.  However, these were not modifications “engaged in” or “authorised by” DDPL or Mr Meissner.

It follows that no breach has been established.

## E.5  The “non-access term”

Campaigntrack pleaded (and DDPL and Mr Meissner admitted) that:

[i]t was an implied term of the DreamDesk Agreement that from the date of the DreamDesk Agreement, DDPL and Mr Meissner would not access, or authorise any other person to access, the DreamDesk System, without the licence or authority of the Applicant or New Litho (the Non-Access Term).

Particulars

(i) 	The Non-Access Term is implied by fact and/or by law.

(ii) 	The DreamDesk Agreement provides limited circumstances in which access was permitted.

Campaigntrack pleaded that the DreamDesk system was accessed on a number of occasions without the licence or authority of Campaigntrack or New Litho: FASOC [98].  The particulars provided were:

(i)	The migration scripts and all development history were deleted from the Git Repository by Mr Semmens on or about 28 September 2016.

(ii) 	On around 3 occasions, a person using root user credentials for the DreamDesk server used “rsync” to synchronise the entire “client data” folder for client “1” (Biggin & Scott) between the DreamDesk server and another server with the username “DreamDesk” and “Toolbox”.

(iii) 	The audit logs on DreamDesk were deleted to remove reference to the synchronisation by rsync by Mr Semmens on or about 5, 6 and 10 October 2016.

(iv) 	On or around 18 October 2016, Mr Semmens logged into DreamDesk to disable a user.

(v)	Mr Semmens continued to have access to the DreamDesk system at all material times.

The admitted implied term must be read in the context of the agreement as a whole, which included a “licence-back” until 3 October 2016.

I am not satisfied that either DDPL or Mr Meissner accessed or authorised access to the DreamDesk system after the DreamDesk sale agreement.  I do not accept that Mr Semmens was acting as DDPL’s agent with respect to his access.  It was not directly put to Mr Meissner in cross-examination that he accessed or authorised access to the DreamDesk system after the DreamDesk sale agreement.  Campaigntrack relied on the following cross-examination of Mr Semmens, confined to exfiltration of client data:

Was it Mr Meissner?---He would have just said give the client their data, I’m not sure. I don’t think he would have said synchronise their data.

I do not accept that, if Mr Meissner said the words attributed to him (which was not his evidence), that amounted to authorisation to access the DreamDesk system.

## E.6  The “non-transfer term”

Campaigntrack pleaded:

101A 	It was [a] term of the DreamDesk Agreement that DDPL would not transfer any Intellectual Property required for the operation and supply of the DreamDesk dashboard to any third party, unless the Applicant or New Litho approved in writing.

Particulars

(i) 	Clause 2.3.8 of the Agreement.

101B	DDPL transferred or authorised the transfer of:

(a) 	the whole or part of the Dreamdesk Database;

(b) 	the whole or part of the Dreamdesk Tables; and

(c) 	the whole or part of the DreamDesk PDF files.

Particulars

(i) 	The Applicant repeats the particulars to paragraphs 20, 22A, 29, 31A, 58 and 60A above.

Clause 2.3.8 of the DreamDesk sale agreement was directed to the licence of the intellectual property back to DDPL in the circumstances contemplated by cl 2.3.  Clause 2.3 provided:

2.3. 	In addition to the above, the parties agree that if either RT Edgar or Biggin & Scott enter into agreements on or before 2 September 2016 with Campaigntrack or any entity associated with Campaigntrack for the use of the CampaignTRACK Platform, the Purchasers will grant a limited, Australia wide licence to use the Intellectual Property for the restricted purpose of supplying the product currently provided by Dream Desk known as the Dashboard to clients of Dream Desk who are not engaged or associated with the real estate industry on the following conditions:

2.3.1. 	The Intellectual Property licenced will be only that Intellectual Property that is required for the operation and supply of the Dashboard, including only that source code relating to the Dashboard. Dream Desk will have no licence to use, and no rights to any of the Intellectual Property that is not required for the operation and provision of the Dashboard.

2.3.2. 	The licence will commence on the expiry of the general licence under clause 2.1 on 1 January 2017.

2.3.3. 	If only one of RT Edgar or Biggin & Scott enters into the agreement contemplated by clause 2.3 the licence will be an exclusive licence for a period of five years from the date that such an agreement is entered into and any renewal of the licence will be on terms that it will be a non-exclusive licence. After the expiry of the exclusive licence period the Purchasers will be free to licence the same Intellectual Property to third parties. If both RT Edgar and Biggin & Scott enter into the agreements contemplated by clause 2.3 the licence will be an exclusive licence for a period of five years from the date that the first such agreement is entered into and any renewal of the licence will be on terms that it will be an exclusive licence.

2.3.4. 	The initial term of the licence will be five years. The licence will be renewed on the expiration of the initial term under the same terms if mutually agreed to by the parties. The licence renewal will not be unreasonably withheld by the Purchasers.

2.3.5. 	The licence granted to Dream Desk cannot be used for any existing client of Dream Desk unless agreed to by the Purchasers.

2.3.6. 	The licence will immediately terminate if the business structure or makeup of Dream Desk changes in a material way from the date of these Heads of Agreement or if Dream Desk breaches the terms of the licence.

2.3.7. 	The terms of the licence agreement will not restrict the Purchasers from supplying products and services of the same kind as the Dashboard using the same Intellectual Property that is licenced. The term ‘exclusive’ as referred to in this clause is to be taken to mean that the Purchasers will not grant the same licence to a third party but it does not restrict the Purchasers from exploiting any Intellectual Property in any way.

2.3.8. 	Dream Desk will not be permitted to transfer, assign, sub-licence or otherwise grant rights to third parties to the licenced Intellectual Property unless the Purchasers approve in writing.

Clause 2.3.8 operates as a condition to a licence granted under cl 2.3.  No such licence was granted.  Campaigntrack’s case is, accordingly, misconceived in this respect.

In any event, I do not accept that DDPL transferred or authorised the transfer of the DreamDesk Database, Tables or PDF files.

## E.7  The “licencing warranty”

Campaigntrack’s case with respect to the “licencing warranty” turned on cl 2.6 of the DreamDesk sale agreement which provided:

2.6. 	Dream Desk and Meissner warrant that:

2.6.1. 	Dream Desk has not sold, licenced, transferred, assigned or in any way parted with possession or any right associated with the Intellectual Property.

2.6.2. 	Dream Desk is the sole owner of the Intellectual Property and it is free and able to transfer the Intellectual Property to the Purchasers free of any claim, third party interest or encumbrance.

Campaigntrack pleaded:

In the alternative to paragraphs 11 to 73 above, if (which is not admitted) Biggin & Scott:

(a) 	was the owner of the Biggin & Scott templates and property data; and/or

(b) 	was entitled to the transfer of the Biggin & Scott templates and property data,

by reason of an agreement between DDPL and Biggin & Scott dated 20 May 2015, then:

(c) 	DDPL breached the Assignment Term by reason of being (and to the extent that it is) incapable of transferring all rights, entitlement and interest in the DreamDesk Intellectual Property to the Applicant and New Litho;

(d) 	DDPL breached the Transfer Warranty;

(e) 	Mr Meissner breached the Transfer Warranty:

(f) 	DDPL breached the Licensing Warranty; and

(g) 	Mr Meissner breached the Licensing Warranty.

DDPL did not breach the “licencing warranty”.  It did not part “with possession or any right associated with” the intellectual property by having earlier entered the agreement with Biggin & Scott dated 20 May 2015.  Nor am I satisfied that, by reason of the agreement dated 20 May 2015, DDPL breached the Assignment Term or the Transfer Warranty or that Mr Meissner breached the Transfer Warranty or the Licencing Warranty.

## E.8  The “compliance term”

Campaigntrack pleaded:

133 	On or around 16 July 2016, the Applicant, New Litho, DDPL and Mr Meissner entered into a Heads of Agreement.

Particulars

(i) 	Heads of Agreement between the Applicant, New Litho, DDPL and Mr Meissner dated 18 July 2016, as varied by the Agreement to Vary Agreements between the same parties dated 5 September 2016, (Heads of Agreement).

134	It was a term of the Heads of Agreement that Mr Meissner agreed to do all things reasonably necessary to ensure DDPL complied with its obligations under the DreamDesk Agreement (the Compliance Term).

Particulars

(i) 	Clause 1.3 of the Heads of Agreement.

Clause 1.3 reflected, in express terms, the general rule that each party to a contract agrees by implication to do all things necessary to secure performance of the contract: Secured Income Real Estate (Australia) Ltd v St Martins Investments Pty Ltd (1979) 144 CLR 596 at 607-608 (Mason J, with whom Barwick CJ, Gibbs, Stephen and Aickin JJ agreed).  This claim does not add materially to the other allegations of breach of contract.

# F  BREACH OF UNDERTAKINGS

Campaigntrack’s solicitors sent a proposed undertaking to Mr Meissner on 5 October 2016 – see: [129] to [130] above.  The undertaking was in the following terms:

Dream Desk, Meissner and Semmins [sic] undertake and agree that they individually or jointly with any other person or entity will not use, market, sell, copy, duplicate or in any way enable or facilitate the development of any system by making use of any of the intellectual property which comprises and/or relates to the system of Dream Desk, which is now owned by Campaigntrack Pty Ltd to the extent that they will not permit, now or at any time in the future, access by any third party to the system known as Dream Desk for any use other than its ordinary permissible use.

Dream Desk, Meissner and Semmins [sic] also undertake and agree that they will immediately cause to be returned to Campaigntract [sic] Pty Ltd, or if unable to be returned then destroyed so as to render useless, any of Dream Desks [sic] intellectual property or code which has already been copied, duplicated or otherwise provided to any third party or entity of any description whatsoever.

On 5 October 2016, Mr Meissner sent an email to Campaigntrack’s solicitors agreeing to the undertaking and pointing out that he had no authority to agree to it on behalf of Mr Semmens.  He also noted that he was overseas and stated that his “email should be used as my acceptance”.

Biggin & Scott, RETB, Mr Stoner and Ms Bartels signed an undertaking on 6 October 2016.  The undertaking was, as a matter of substance, in the same terms as that to which Mr Meissner had agreed.

Properly construed the undertaking was primarily concerned with the source code of DreamDesk.  The first paragraph of the undertaking, put simply, constituted an undertaking that the relevant persons and entities would not do certain things or enable the development of a system by providing access to the DreamDesk system for any use other than its ordinary use.  The second paragraph of the undertaking, put simply, constituted an undertaking to return any intellectual property or code already copied.  The term “intellectual property” contained in the undertaking means the same thing as that term bears in the DreamDesk sale agreement.

As against Biggin & Scott, RETB, Mr Stoner and Ms Bartels, Campaigntrack pleaded at FASOC [71]:

It was a term of the Undertaking that Biggin & Scott and RETB agreed and undertook that they would not use, market, sell, copy, duplicate or in any way enable or facilitate the development of any system by making use of any of the intellectual property which comprised or related to the system of Dream Desk.

Campaigntrack alleged in FASOC [72] that Biggin & Scott, RETB, Mr Stoner and Ms Bartels breached the undertakings they provided by reason of the alleged acts of:

copyright infringement in respect of the “Database Tables” (FASOC [23]-[28], [53]-[57D]), the “DreamDesk Database” (FASOC [32]-[37], [53]-[57D]), the “menu for the DreamDesk website” (FASOC [41]-[46], [53]-[57D]), the “source code for the DreamDesk website” (FASOC [50]-[57D]) and by acts of authorisation by Mr Stoner and Ms Bartels (FASOC [60D]-[60I];

misuse of confidential information (FASOC [106], [107] in relation to source code and [115]-[118] in relation to the “Database Tables” and “DreamDesk Database”).

Assuming these breaches fall within the terms of the undertaking, Campaigntrack has not established that any of Biggin & Scott, RETB, Mr Stoner or Ms Bartels committed the alleged breaches.

As against Mr Meissner and DDPL, Campaigntrack pleaded:

103 	It was a term of the DreamDesk Undertaking that DDPL and Mr Meissner would not permit access by any third party to the system known as Dream Desk for any use other than its ordinary permissible purpose.

104 	It was a term of the DreamDesk Undertaking that DDPL and Mr Meissner would not use, market, sell, copy, duplicate or in any way enable or facilitate the development of any system by making use of any of the intellectual property which comprised or related to the system of Dream Desk.

Campaigntrack alleged in FASOC [105] that DDPL and Mr Meissner breached the undertaking by reason of the alleged acts of:

copyright infringement in respect of the “Database Tables” (FASOC [22C], [22D]), the “DreamDesk Database” (FASOC [31C], [31D]) and the “PDF files” (FASOC [60C], [60CA]);

breach of contract in respect of the (admittedly implied) “non-access term” (FASOC [98], [99]);

breach of contract in respect of the “non-transfer term” (cl 2.3.8 of the DreamDesk sale agreement, FASOC [101B]).

None of these breaches have been established.  It is therefore unnecessary to decide if any of the alleged breaches were capable of falling within the terms of the undertaking.

# G  CONCLUSION

On 18 October 2017, an order was made that all issues of liability be determined separately from and before issues of quantum.  The parties should confer with a view to agreeing orders to give effect to these reasons for judgment.

Associate:

Dated:	19 July 2021

## SCHEDULE OF PARTIES