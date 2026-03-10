# Slide 1

## 2026 LAWS5151Dr Alan Davidson

Electronic Signatures

---

# Slide 2

## Introduction

Introduction 
Traditional signatures {231}

---

# Slide 3

## Traditional signatures

!! Couldn't write these notes down in time.

Lemayne v Stanley (1682) 3 Lev 1; 83 ER 545
Ellis v Smith (1754) 1 Ves Jun 11 at 12; 30 ER 205
Knight v Crockford (1794) 1 Esp NPC 190; 170 ER 324
Lobb v Stanley (1844) 5 QB 574; 114 ER 1366
Evans v Hoare [1892] 1 QB 593 PTO
R v Moore; Ex Parte Myers (1884) 10 VLR 332 (Later)



knight v Crockford
- I [name] agree to sign this

Evans v hoare;
- Defendants name at top, defendant's name in body.
- Justice stresses importance of intention of the signature, whether in the body, at the beginning or at the end.
PDO

---

# Slide 4

## Introduction

**Dunning & Smith v Roberts 35 Barb. 463 (1862)** 

(manipulations of a telegraph operator, upon the oral instructions of a person to send a dispatch for him, are the equivalent to a signing by that person within the Statute of Frauds)*


**Howley v Whipple, 48 N.H. 487** -  Electronic Signature in 1869 

Private key encryption (symmetrical)
Public key encryption (asymmetrical)

Electronic signatures
Digitised signatures
Digital signatures {244}


---

# Slide 5

## Electronic Signature

No definition in Australian Acts
However, consider:
"electronic signature" means any letters, characters, numbers or other symbols in digital form attached to or logically associated with an electronic record, and executed or adopted with the intention of authenticating or approving the electronic record”

**Legal Services Board v Forster [2009] VSC 645:** 
Electronic signature is recognised as "not necessarily the writing in of a name, but maybe any mark which identifies it as the act of the party.”



---

# Slide 6

## Singapore legislative scheme

Singapore - “Secure electronic signature”  18(1)  If, through the application of a specified security procedure, or a commercially reasonable security procedure agreed to by the parties involved, it can be verified that an electronic signature was, at the time it was made —
	(a)	unique to the person using it;
	(b)	capable of identifying such person;
	(c)	created in a manner or using a means under the sole control of the person using it; and
	(d)	linked to the electronic record to which it relates in a manner such that if the record was changed the electronic signature would be invalidated,
such signature is treated as a secure electronic signature.


---

# Slide 7

## European Union eIDAS regulations (electronic Identification, Authentication and Trust Services)

Simple Electronic Signatures - "data in electronic form which is attached to or logically associated with other data in electronic form and which is used by the signatory to sign."  No form of verification - should only be used between trusted parties. 
Advanced Electronic Signatures - rely on certificates - user authentication, government-issued document, biometric detection checks, and a unique access code for use after the signing process Uses specific platform or delivery service with audit trails, records, and metadata about the transmitted data. Typically certified by a Certification Authority.  
Qualified Electronic Signatures – eg certificate based on public keys - The verification process is designed to prove the identity of the signatory performed by an audited entity, called the qualified trust service provider - maybe multi-faceted to ensure security (may include face-to-face verification - may be undertaken by video chat. 


---

# Slide 8

## Single code – symmetric systems

same key used to encrypt and decrypt
they use a “secret” key - security depends on keeping the key secret

problem: how do you transmit the key securely?

---

# Slide 9

## Public/private key systems

1976 solution - use two different but related keys
one locks and the other unlocks anything sent by its pair (“asymmetric”)
one key is kept secret and the other made public
requires a trusted keeper of the public key 

---

# Slide 10

## 

---

# Slide 11

## 

---

# Slide 12

## 

---

# Slide 13

## Public/private key systems

Step 3: receiver (and only receiver) can use the private key that decrypts (“unlocks”) that message

Step 2: to send a message, sender looks up receiver’s public key and uses it to encrypt (“lock”) message

Step 1: receiver places public key with trusted public authority, and keeps the related secret private key

---

# Slide 14

## Common applications

Protection of information transmitted during electronic banking transactions, such as ATM transactions, EFTPOS purchases, SI-net, VoIP, EBay and many Internet transactions
Encryption of email (eg PGP/GPG - first widely used non-military key)
Encryption of files stored on computers (PGP/GPG) 
Digital signatures

---

# Slide 15

## 

SSL (https) protocol
SSH (secure remote login, tunneling, etc) (public/private authn/authz is optional)
Digtal Signatures – PDF - Debian, Ubuntu and Red Hat Linux DistributionsSigned Applets and jar archive files for Java
S/MIME for signed and/or encrypted email
Internet Key Exchange (IKE) in IPsec for secure low-level TCP/UDP networking
RFC 3161 for authenticated timestamps
A variety of other uses, like digital cash and secure transparent voting (eg trustee keys for Helios)


---

# Slide 16

## Transport Layer Security -Formerly Secure Sockets Layer

TLP (SSL) provides endpoint authentication and communications privacy over the Internet using cryptography 
Typically only the server is authenticated
Mutual authentication requires public key infrastructure – to permit client/server communication to prevent eavesdropping, tampering and message forgery. 

---

# Slide 17

## TLS

- Visa, MasterCard, American Express and many leading financial institutions have endorsed SSL for commerce over the Internet. 
- SI-Net
- Amazon
- eBay


---

# Slide 18

## Controversy?

**Argument for:** Free access to cryptography by the general public enables them to fulfil their right to protect the privacy of their communications, including commercially valuable data

**Argument against:** The government needs to control the use of cryptography to enable eavesdropping on phone calls, email etc as part of its law enforcement activities.


---

# Slide 19


##  www.wassenaar.org/
loose arrangement regaridng weapons regulation.


The Wassenaar Arrangement on Export Controls for Conventional Arms and Dual-Use Goods and Technologies - agreement between certain countries regarding weapons regulation
The Wassenaar Arrangement has been established in order to contribute to regional and international security and stability, by promoting transparency and greater responsibility in transfers of conventional arms and dual-use goods and technologies, thus preventing destabilising accumulations. The aim is also to prevent the acquisition of these items by terrorists.




---

# Slide 20

## Wassenaar Arrangement

Criteria:
Foreign availability outside Participating States. 
The ability to control effectively the export of the goods. 
The ability to make a clear and objective specification of the item 
Controlled by another regime, such as the Australia Group, Nuclear Suppliers Group, or Missile Technology Control Regime 



---

# Slide 21

## Circumvention of Encryption

Electronic
Non-electronic

---

# Slide 22

## Electronic Signatures

What is a signature? 

R v Moore; Ex Parte Myers, (1884) 10 VLR 322 {233} 

- Printed name of the party is enough. The signat

L'Estrange  v Graucob [1934] 2 KB 394 

Stephen Mason, The Law of Electronic Signatures, Online  5th edition 

C Reed, “What is a Signature?” JILT 2000 (3)

- in his most recent argument, he says that what a signature is "is debatable"
- Rubber stamp on it's own will not suffice. with or without seal. Seal is not necessary.

### Notes
security and hacking - what is the worst case scenario?
legal issues
encryption as a security threat
authenticity and proof (EDI)
damaging and defamatory communication
commerce and coins
issuing and control problems
risk allocation and consumer protection

---

# Slide 23

## 

Lemayne v Stanley (1682) 3 Lev 1; 83 ER 545
Ellis v Smith  (1754) 1 Ves Jun 11 at 12; 30 ER 205
Knight v Crockford (1794) 1 Esp N P C 190; 170 ER 324
Lobb v Stanley (1844) 5 QB 574; 114 ER 1366
Evans v Hoare [1892] 1 QB 593

{232}

---

# Slide 24

## 

Lazarus Estates Ltd v Beasley [1956] 1 QB 702 Denning LJ {234}
Joseph Denunzio Fruit Co v Crane 79FSupp 117 (1948)
Smith v Greenville County 188 SC 349 {233}
Jenkyns v Gaisford & Thring (1863) 3 SW & TR 93, 95 {234}

---

# Slide 25

Howley v. Whipple, 48 N.H. 487 -  Electronic Signature in 1869 **
Brewster v Horst & Lachmund Co 60 P 418 (Cal 1900) (statute of frauds satisfied by exchange of telegrams)
A&G Construction Co v Reid Bros Logging Co 547 P 2d 2107 (Alaska 1976) (typed signature on letter)  *
The Anemone [1987] 1 Lloyd's Rep 546** - guarantee case, “the material telex had the sender's name printed on it and was, therefore, signed by the sender”.
Parkesinclair Chemicals (Aust) Pty Ltd v Asia Associates Inc [2000] VSC 362,* [107] (printed signature)

R v Frolchenko (1998) QCA 43 {235}
Doherty v Registry of Motor Vehicles (1998) {235}



---

# Slide 26

## Electronic Transactions Act (Qld) – UN Amendments

If, under a State law, a person’s signature is required, the
requirement is taken to have been met for an electronic
communication if—
(a) a method is used to identify the person and to indicate
the person’s intention in relation to the information
communicated; and
(b) the method used was either:
     (i)  as reliable as appropriate for the purpose for which the electronic communication was generated or communicated, in the light of all the circumstances, including any relevant agreement; or
   (ii)  proven in fact to have fulfilled the functions described in paragraph (a), by itself or together with further evidence; and
(c) Consent


---

# Slide 27

## Email Headers

!! Relevant for assignment.

From: Alan Davidson – a.davidson@law.uq.edu.au

Is it a signature?

Note the elements on the previous slides
- Identity
- Intention
- Method (reliable as appropriate – or – proven in fact)

See [[Assignment Guide]]

---

# Slide 28

## McGuren v Simpson [2004] NSWSC 35 {165}

Based on ETA and common law. 
Quoted Cheshire “This relaxation … offers a striking instance of the way in which legislation may be overlaid by judicial precedent.”
“… the Act ought to be read to accommodate technological change and that, accordingly, the email sent by the plaintiff constitutes a written document.” 
Held to be signed (Of What?)


---

# Slide 29

## Mehta v J Pereira Fernandes SA [2006] EWHC 813 {236} 

**Stephen Mason** - Electronic Evidence and Electronic Signatures 5th ed University of London Press, 2021 (Chap 7 - pp -  (Edition 2 vs edition 4 or 5?)
- Compare his differing opinion through the editions
- He eventually pivots from being adamant it IS a signature to it not being a signature.

Meaning of “Automatic insertion”
Intention
Value of Evans v Hoare – Cave J
“open to debate” (Mason)

---

# Slide 30

Athens Single-Member Court of First Instance 1327/2001 Lyberopoulos J, the president of the court
About writing – but comments on the email address
Treated as a payment order

---

# Slide 31

**SM Integrated Transware Pte Ltd v Schenker Singapore (Pte) Ltd [2005] SGHC 58** 
	There is no doubt that at the time he sent them out, he intended the recipients of the various messages to know that they had come from him. Despite that, he did not find it necessary to identify himself as the sender by appending his name at the end of any of the emails whether the messages were sent to his colleagues or to third parties like Mr Heng. I can only infer that his omission to type in his name was due to his knowledge that his name appeared at the head of every message next to his email address so clearly that there could be no doubt that he was intended to be identified as the sender of such message.

Some argue this was merely identification – not authentication. 

---

# Slide 32

## Disclaimer?


This was a disclaimer that was appended to this email.

…Even though an email signature block and address header has been appended to this email, and despite the Electronic Transactions Act (Qld) or the Electronic Transactions Act (Cth), neither the signature block nor the address header exhibit the senders intention to be bound by an offer previously sent by the intended recipient, unless the email specifically states otherwise.



---

# Slide 33

## Corporations Act 2001 (Cth) since 2022

110A  Technology neutral signing
(1)  A person may sign a document to which this Division applies:
(a)  by signing a physical form of the document by hand; or
(b)  by signing **an electronic form of the document using electronic means;**
if the method of signing satisfies subsection (2).
Note: A document (including a deed) may be executed by or on behalf of a company without the use of paper, parchment or vellum: see subsections 126(6) and 127(3A).
(2)  A **method** of signing satisfies this subsection if:
(a)  the method **identifies the person and indicates the person’s intention in respect of the information recorded in the document; and**
(b)  the method was either:
	(i)  **as reliable as appropriate** for the purpose for which the information was recorded, in light of all the circumstances, including any relevant agreement; or
	(ii)  **proven in fact to have fulfilled the functions described in paragraph (a), by itself or together with further evidence.**
	**(no consent provision)**



Notice there is no consent provision.


---

# Slide 34

## 

**Mayne v Robbins [2009] SADC 58 (2009) (electronic consent orders)**

Islamic Council of South Australia Inc v Australian Federation of Islamic Councils Inc [2009] NSWSC 211 (and CL) Ramzi

Legal Services Board v Forster [2010] VSC 102 (“The signature is typed in as I am away at the moment and don’t have access to a printer.”[36] Stated intent to be bound) (“… has long held that a signature is not necessarily the writing in of a name, but may be any mark which identifies it as the act of the party.”


---

# Slide 35

##  

Luxottica Retail Australia Pty Ltd v 136 Queen Street Pty Ltd [2011] QSC 162 (Footer of email) 
Brown Bros Cabinetworks Pty Ltd v Graham (Civil Claims) [2012] VCAT 70  (“‘typed in’ signature may suffice”[28] - “Mr and Mrs Graham”) 



---

# Slide 36

## Attorney-General (SA) v Corporation of the City of Adelaide [2013] HCA 3  

Solicitor attached a Word document (Certificate) to an email – it had an empty dotted line for the signature, and the solicitor’s name underneath. Certificate was “essential” to make the by-law valid. 

Held: The provision of the electronic certificate from the Microsoft Outlook email box of the legal practitioner together with the statement of his name, sufficiently identified him - an attachment to an email is a signature [23][127][194]…


---

# Slide 37

## Attorney-General (SA) v Corporation of the City of Adelaide [2013] HCA 3 
Relevant High Court case. 

Solicitor sent email necessary to establish company bilaws.

… sending an unsigned word document can be considered as signed where:

(1) there is a dotted line, and underneath there is the person name (and in this case the words “legal practitioner”); 
(2) The email indicated “approval” (see para 23); 
(3)  reliable as was appropriate (see para 127). 


*Note "approval" was used in line with the old act. 

---

# Slide 38

## Bullhead Pty Ltd v Brickmakers Place [2017] VSC 206
-> Past use of an email can be sufficient to identify someone, even if the email address is not obviously identifiable to the person.

Buckland by his electronic signature ‘Brett’ when combined with his email address ‘brett6858@gmail.com’ identified himself and his intention in respect of the information communicated (s 9(1)(a)).

---

# Slide 39

## Click – signature?

IP Address
Gonzalez v Agoda Company Pte Ltd [2017] NSWSC 1133 
[123] – “I consider that the signature on the digital document provided by Ms Gonzalez clicking the “Book Now” button” (by virtue of s 9(1) of the ETA)

Signature not actually necessary in vast majority of contracts. So therefore, this line may just be obiter, as it was not necessary for the finding of the decision. Important, as judge might have been referring to signature in a more colloquial way.

i

---

# Slide 40

## Williams Group Australia Pty Ltd v Crocker [2016] NSWCA 265* 

Guarantee by director
Unremarkable from an electronic commerce viewpoint because the lack of authority should apply equally to electronic signatures
“that may be a matter for the legislature to address” [4]

---

# Slide 41

## Recap - Signature

When is correct form and signature legally obligatory?
Real property transactions
Wills
Cheques
Insurance contracts
Consumer credit transactions
Otherwise - no legal requirement for form and signature in Australia

---

# Slide 42

## LAWS5151Dr Alan Davidson

Electronic Signatures

---

