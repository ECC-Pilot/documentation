```{comment}
ECC-Pilot documentation master file, created by `sphinx-quickstart`.
You can adapt this file completely to your liking, but it should at least
contain the root `toctree` directive.
```

# European Campus Card Pilot Project's documentation

% Abstract

Project and Requirement Documentation for the "**European Campus Card**" **Pilot Project** by the EUGLOH Work Package - Campus Life.
Providing a digitized card pilot for European Heigher Education Institutions - *A European Campus Card for Interoperable Services* - and a Framework for additional digitized service cards.

This Projects aims at specifing a new, better version of the [European Student Card](https://europeanstudentcard.eu/) ({term}`ESC`) idea, in such a way, that it actually provides an baseline for interoperable services and fulfil the vision of the European Student Card Initiative ({term}`ESCI`).

```{note}
This document is work in progress.
Structure and content may change a lot within the next days / weeks.

```

## Background

The European Commission and the Erasmus+ Program has defined a roadmap for digitalization and interoperable service provisioning withing the european education system.

Within this roadmap and vision several projects as have been defined and funded to standardize a European Student Card ({term}`ESC`).
This project has been lead by Student Unions of several member states, most notable .
The defined "European Student Card" Specification neighter reflects the needs of the Higher Education Institutions nor does it really provide any interoperability.
Additionally the provided specification documents and implemented elements conflicts with {term}`GDPR` requirements and have a lot IT-security issues.

```{warning}
We do not recommend any Heigher Education institution to implement the current European Student Card Specification of the European Student Card Project / ECS-Tension Project.
```

## Goals of this project - a "European Campus Card"

The vision of the "European Student Card" is valid and great.
This project group honors the vision and tries to provide an alternative specification that would provide an interoperable baseline.

### Key Concepts

Identity Documents based on plastic cards are not a good base for interoperable service provision.
Chip cards and smart cards, are limited.
They have a limited memory, and storing data / applications on those cards differ by the providers.
Also interoperability does not reside within the cards, as almost any technology provider has different internal standards to store and secure data on the card, *interoperability is done on the reader side*.

Modern Smartphones have **Wallet** functions build into the operating system and could store almost unlimted number of cards and data.
Also Smartphones are the essential working tool for students and most university employees.

The approach of "Integrated Chip Cards", to store multiple service specific applications within one card is not valid anymore.
Within Smartphone Wallets the approach of "***one card per service***" has more benefits.

Service provider on and off campus does have different needs and existing technologies, especially with legacy systems, so issueing one service card per service is a bester approach.

Additionally most Service Providers does not provide their services to students exlusivly.
Multiple customer / consumer groups exists, that could uses those services.
The European Campus Card does reflect this by opening the system to all roles.

A majority of Service providers, especially off campus, do offer services and discounts to members of Higher Education Institusions.
They often only need a affiliation status verification or prove of entitlement, sometimes scoped to certain institutions.
For Higher Education Institutions themself, their Identity Management Systems is the "**point-of-truths**".
Key elements of those IDM Systems are standardized with {term}`LDAP`-Schematas: [eduPerson](https://wiki.refeds.org/display/STAN/eduPerson) and [SCHema for ACademia](https://wiki.refeds.org/display/STAN/SCHAC) ({term}`SCHAC`).
Those Schema define a common set of attributes used by almost all {term}`HEI`s.

The {term}`eduPerson` specification defines an enumeration of permissible values for roles: [eduPersonAffiliaction](https://wiki.refeds.org/display/STAN/eduPerson+2021-11#eduPerson202111-eduPersonAffiliation)

* faculty
* student
* staff
* alum
* member
* affiliate
* employee
* library-walk-in

Those eight roles contains seven values for natural persons and one for technical devices.
The roles have a logical structure and hierachy:

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



### Deliverables

* API for issueing European Campus Card, containing at least the DEUinfo core application
* API for Service Discovery (central database)
* A Verification System
   * API to verify a card
   * A Smartphone App to verify a card
   * A contactless reader that could verify a card








## Contents

```{toctree}
---
maxdepth: 3
name: mastertoc
caption: Table of contents
---

project/index.md
card/index.md
requirements/index.md

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
