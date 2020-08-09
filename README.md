# EPUS-M
Epics, Projects, & User Stories Manager - QA DevOps Training Camp Project (Week 6 Submission)

## Contents

[TOC]

### Resources: 

- Presentation: https://docs.google.com/presentation/d/1tlpwhA0d7l_0pts1pIkOo-qNS3IXXAeEnSfSEwgLxoQ/edit?usp=sharing
- JIRA: 
- Website: http://34.105.203.3:5000/
- GitHub: https://github.com/CaelTintreach/MPUS (Please also refer to EPUS-M and PEUS-Manager under the same user as previous repos for the same project)
- Risk Assessment: https://docs.google.com/spreadsheets/d/1BxxjTdANJl7eVp3kVqjHzK4UzO-UIaAIJUsvgh1SCZM/edit?usp=sharing

### Brief

Our overall objective with the project was to create a CRUD application with utilisation of supporting tools, methodologies, and technologies that encapsulate all core modules covered during training. 

#### Additional Requirements

We also had to work with the following requirements outlined:

- A Trello board (or equivalent Kanban board tech) with full expansion on user stories, use cases, tasks needed to complete the project. 
- A relational database used to store data persistently for the project, this database must contain at least 2 tables within. To demonstrate understanding, it is also required to model a relationship.
- Clear documentation from a design phase describing the architecture used for the project as well as a detailed risk assessment.
- A functional CRUD application created in Python, following best practices and design principles, that meets the requirements set on your Kanban board.
- Fully designed test suites for the application created as well as automated tests for validation of the application. High test coverage in the backend must be provided as well as consistent reports and evidence to support a TDD approach.
- A functioning front-end website and integrated API's, using Flask.
- Code fully integrated into a Version Control System using the Feature-Branch model which will subsequently be built through a CI server and deployed to a cloud-based virtual machine.

All elements above should be completed before adding additional functionality. 

#### Selected Method & Technologies

To achieve the above I decided to create a simple Project, Epic, & User Story Manager application which stores required information in a relational database using the following technologies.

##### Selected Technologies

- Kanban Board - JIRA
- Relational Database - MySQL
- Documentation - Typora & Draw.io
- Application Creation - Python
- Website Creation - Flask
- Version Control System - GitHub
- CI Server - Jenkins

##### Selected Methods

- Create a project (satisfies 'Create' requirement) that stores
  - Stores a ProjectID (Primary Key)
  - ProjectName
  - CompletedStatus
- Create a user story (satisfies 'Create' requirement) which links to an epic and project as many-to-one relationship (satisfies relational requirement)
  - UStoryID
  - EpicID
  - UStoryName
  - AsAField
  - IWantField
  - ToSoField
  - CompletedStatus
- View and update user stories and projects.
- Delete user stories and projects.

### Architecture

#### Database Structure

Seen below is the previous and current entity relationship diagram (ERD) which demonstrates the structure of the database. 

#### Early ERD

![EPUS M V1](C:\Users\Clifford\Downloads\EPUS M V1.png)

#### Final ERD

![Final ERD](C:\Users\Clifford\Downloads\Final ERD.png)

As seen in the above ERDs, the application went through a reiteration later into the project as part of a general optimisation toward building a more reliable MVP product for the deadline. By removing the Epics table and slimming down the columns in the User Stories table, the project was reduced to something more in line with the requirements while also retaining all key functionality. Further to this, the project can be freely expanded to include new functionality in later versions are part of feature driven development.

### CI Pipeline

Refer to the below diagram to see the development CI pipeline that the application has been built in and is designed to run on.

![CI Pipeline](C:\Users\Clifford\Downloads\CI Pipeline.png)

### Risk Assessment Retrospective

Please see included risk assessment link for the initial risk assessment and RAR.md for the retrospective.

### Test Guide

Please see included testguide.md.

### Known Errors

#### Updating User Stories

As of time of writing, there is an unknown bug preventing the user from progressing from updating the user stories page. Probable cause states this bug was found after changing endpoints but reversion did not resolve the issue. 

##### Failed Tests

As a result of the above bug, two units will now consistently fail. These failures can currently be considered expected behaviour until the bug is corrected. However, care must be taken to check that all other tests pass if building the application.

### Acknowledgements

- QAC for training provided
- Luke Benson for acting as trainer and guidance
- July 2020 DevOps Cohort for assistance in debugging

### License

```python
MIT License

Copyright (c) [2020] [Clifford McKinney]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```