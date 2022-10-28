% ECC-Pilot documentation master file, created by `sphinx-quickstart`.
% You can adapt this file completely to your liking, but it should at least
% contain the root `toctree` directive.

# European Campus Card Pilot: Project Documentation

```{attention}
This document is a work in progress.
Structure and content may change a lot within the next days / weeks.

Version 0.0.1dev

```
% Abstract

Project and Requirement Documentation for the "**European Campus Card**" **Pilot Project** by the EUGLOH Work Package - Campus Life.
Providing a digitized card pilot for European Higher Education Institutions - *A Campus Card for Interoperable Services* - and a Framework for additional digitized service cards.

```{note}
This project aims at specifying a new, better version of the [European Student Card](https://europeanstudentcard.eu/) ({term}`ESC`) idea, in such a way, that it actually provides an baseline for interoperable services and fulfils the vision of the European Student Card Initiative ({term}`ESCI`).

The major differences:

* not student exclusive --> It aims on all persons (roles) at Higher Education Institutions or even all Education Institutions as the difference in {term}`ISCED`-Level 6-8 to lower level might not make a huge difference. --> Student ID, Employee ID, Affiliate ID, Alum ID, maybe also Pupil ID
* aim to issue the cards as wallet passes into smartphones
* not to integrate all services into one card, but provide a core card / pass and additional cards / passes for legacy services
* it is not limited to Students at European Union Member states --> Focus on [Erasmus+ Partner Institutions / Countries](https://erasmus-plus.ec.europa.eu/programme-guide/part-a/eligible-countries), but may extend to all Countries worldwide similar to other edu-Services like: eduRoam, eduGAIN, ...

```{todo}
Decision on a good / better Project Name / Branding together with relevant political stakeholders

Potential Project / Branding Names:
* **eduCard**
* **eduPass**
* **eduCampusCard**
* **eduCampusPass**
* **eduCampusID**
* **European Campus Card**
* **Erasmus+ Campus Card**
* **Campus ID**

so it could end up in **eduCampusCard Student ID** and **eduCampusCard Employee ID** with specific translations (for example in German that could go as *eduCampusCard Dienstausweis* or *eduCampusCard Mitarbeiterausweis* )
```




```{hint}
This Document / Documentation define requirements, therefor the key words "**MUST**", "**REQUIRED**", "**SHALL**", "**MUST NOT**", "**SHALL NOT**", "**SHOULD**", "**RECOMMENDED**", "**SHOULD NOT**", "**NOT RECOMMENDED**", "**MAY**", and "**OPTIONAL**" in this document are to be interpreted as described in [RFC 2119](https://datatracker.ietf.org/doc/html/rfc2119).
```

## Background

The European Commission and the Erasmus+ Program has defined a roadmap for digitalization and interoperable service provisioning within the european education system.

Within this roadmap and vision several projects have been defined and funded to standardize a European Student Card ({term}`ESC`).
This project has been lead by Student Unions of several member states, most notable .
The defined "European Student Card" specification neither reflects the needs of the Higher Education Institutions nor does it really provide any interoperability.
Additionally, the provided specification documents and implemented elements conflicts with {term}`GDPR` requirements and have a lot IT-security issues.

```{warning}
We do **NOT** recommend any Higher Education Institution to implement the current **European Student Card** Specification of the [European Student Card Project](https://europeanstudentcard.eu/) / [ESC-Tension Project](https://www.esc-tension.eu/).
```

## Goals of this project - a "European Campus Card"

The vision of the "European Student Card" is valid and great.
This project group honors the vision and tries to provide an alternative specification that would provide an interoperable baseline.

### Key Concepts

Identity Documents based on plastic cards are not a good base for interoperable service provision.
Chip cards and smart cards, are limited.
They have a limited memory, and storing data / applications on those cards differ by the providers.
Also interoperability does not reside within the cards, as almost any technology provider has different internal standards to store and secure data on the card, *interoperability is done on the reader side*.

Modern smartphones have **Wallet** functions build into the operating system and could store almost an unlimited number of cards / passes and data.
Also smartphones are the essential working tool for students and most university employees.

The approach of "Integrated Chip Cards", to store multiple service specific applications within one card is not valid anymore.
Within Smartphone Wallets the approach of "***one card per service***" has more benefits.

Service provider on and off campus does have different needs and existing technologies, especially with legacy systems, so issuing one service card per service is a better approach.

Additionally most service providers does not provide their services to students exclusively.
Multiple customer / consumer groups exists, that could uses those services.
The European Campus Card does reflect this by opening the system to all roles.

A majority of service providers, especially off campus, do offer services and discounts to members of Higher Education Institutions.
They often only need a affiliation status verification or prove of entitlement, sometimes scoped to certain institutions.
For Higher Education Institutions themselves, their Identity Management Systems is the "**point-of-truths**".
Key elements of those IDM Systems are standardized with {term}`LDAP`-Schemata: [eduPerson](https://wiki.refeds.org/display/STAN/eduPerson) and [SCHema for ACademia](https://wiki.refeds.org/display/STAN/SCHAC) ({term}`SCHAC`).
Those Schema define a common set of attributes used by almost all {term}`HEI`s.

The {term}`eduPerson` specification defines an enumeration of permissible values for roles: [eduPersonAffiliation](https://wiki.refeds.org/display/STAN/eduPerson+2021-11#eduPerson202111-eduPersonAffiliation)

* faculty
* student
* staff
* alum
* member
* affiliate
* employee
* library-walk-in

Those eight roles contain seven values for natural persons and one for technical devices.
The roles have a logical structure and hierarchy:

```{mermaid}
graph TD

    student
    staff
    faculty
    member
    alum
    affiliate

    staff --> employee
    faculty --> employee

    student ---> member
    employee --> member
```

Within an institution most often the following four roles have a relevance for identification documents / cards:

* student
* employee
* affiliate
* alum

The problem is, a natural person could have multiple accounts for an login - connected to an Identity Management System.
For each account at an institution zero to seven eduPersonAffiliation roles could be assigned.
So a natural person could have multiple roles and even the same role in multiple institutions, so scoped affiliations are potentially important.

```{mermaid}
graph TD

   person[Natural Person]
   account[Account]
   role[Role]
   pass[Pass / Card]

   person -- 1..n --> account
   account -- 1..0-7 --> role
   person -. 1..n .-> role

   account -- 1..n --> pass
   role --. 1..n .-> pass

```

Linking of multiple accounts is a necessary thing.

## Contents

```{toctree}
---
maxdepth: 3
name: mastertoc
caption: Table of contents
---

project/index.md

requirements/index.md

```


```{toctree}
---
maxdepth: 3
name: backlogtoc
caption: Backlog of still unstructered content
glob:
---

backlog/*
backlog/**/*

```

## Appendix

* {ref}`todolist`
* {ref}`glossary`
* {ref}`genindex`
%* {ref}`modindex`
%* {ref}`search`

```{toctree}
---
maxdepth: 3
hidden:
name: appendixtoc
caption: Appedix
---

todolist.md
glossary.md
contributing/docs.md

```
