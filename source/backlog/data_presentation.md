# Data and presentation

From a HEI perspective branding and design of an identification document / a card is important.
On the other hand for service providers a common set on data is required.

A European Campus Card should appear within the wallet as a card with an individual design per {term}`HEI`.
Each {term}`HEI` should be able to add three logos:

* {term}`HEI`-Logo
* European Campus Card Logo (maybe a specific logo per card type and international scope --> European Union, Erasmus+ Counties, global scope)
* An Alliance Logo

Some background design image and the Name of the Institution.

For each Person the following data should be provided:

* name
  * given name / given names
  * surname
* photo
* date of birth
* validity dates

Within the DEUinfo Application as a core set of data, the following attributes should be provided:

* A Version Information (?)
* schacHomeOrganization - Information about the issuing {term}`HEI`
* Campus Card Identifier - A UUID specific for the schacHomeOrganization to lookup additional data and online check of validity
* a PKI certificate / certificate chain

* potential offline readable data
  * European Student Identifier ({term}`ESI`) (for students)
  * {term}`HEI` Employee Identifier (for employee)
  * ORCID (for faculty)
  * eduPersonAffiliation / eduPersonScopedAffiliation
  * eduPersonPrimaryAffiliation
  * eduPersonAssurance Class
  * Validity dates
  * {term}`ISCED`-Level (6, 7, 8 for students)
