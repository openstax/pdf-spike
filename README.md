# PDF Spike

## Table of Contents

* [A3 Planning](#a3-planning)
  * [Background](#background-plan)
  * [Current Condition](#current-condition-plan)
  * [Goal / Target Condition](#goal--target-condition-plan)
  * [Root Cause Analysis](#root-cause-analysis-plan)
  * [Epics and Task Cards](#epics-stories-and-task-cards-do)
  * [Confirmation](#confirmation-check)
  * [Follow up](#follow-up-act)
* [Bakery](#bakery)
* [Workflow Event Resource](#workflow-event-resource)
* [Workflow Service](#workflow-service)
* [License](#license)

## A3 Planning

A3 planning is a technique created by Toyota and Lean manufacturing. The idea
is to focus on a problem and convey all the information necessary in an A3 
size of paper (11.69 x 16.53 inches). However,  it's not the size of the paper 
that is important but rather the approach to solving the problem and
conveying the right information to the people that need it.

### Background (PLAN)

Given the set of [priorities][roadmap] for Q4 2018 and Q1-Q2 2019 the decision 
was made to hold off on the Refactor Archive (RAP) work in order to deliver a 
[vertical slice][vertical-slice] of the pdf-producer. The pdf-producer is being
created as a UI interface that will allow Content Managers (CMs) and vendors to 
trigger a pipeline job that produces a PDF on demand for QA and publishing purposes. 

### Current condition (PLAN)

Vendors and CMs currently generate PDFs from Legacy. The process involves the 
coupling of PDF generation and publishing from within Legacy. The status of the
PDF generation process is done via a UI known as the [GOB Tool][gob-tool]. The 
tight coupling of PDF generation in Legacy is not efficient for CMs and vendors.

### Goal / Target Condition (PLAN)

To build a [vertical slice][vertical-slice] of the new PDF Producer system that
can deliver value to CMs and vendors as soon as possible and allow the team to 
get fast feedback on the system they are building. Currently, the PDF Producer
system will consist of 3 parts.

1. A concourse pipeline that will use cnx-recipes to generate a PDF. Consumes 
queued jobs from the backend. Updates the backend on progress, completion, and failure.
2. A web api backend used to provide new events to the pipeline, can create new jobs,
and provide information on job progress. 
3. The frontend displays metadata and status information on jobs. The UI used by
users to create new jobs. Main consumer of information from the backend.

[Oct 4th, Spike Document][oct-4-spike-doc] describes the outcome in more detail.

### Root Cause Analysis (PLAN)

We need a way to generate PDFs that have baked-styles applied for testing and 
eventual release to end-users. Content Managers, vendors and potentially, 
ecosystem partners need to be able to generate a PDF that has baked-styles 
applied for testing and eventual release to the public.

### Epics, Stories, and Task Cards (DO)

* [Spike to Deliver PDF with Concourse](https://github.com/openstax/cnx/issues/723)
* [Technical Design Document](https://docs.google.com/document/d/1OjTKqdToVrurQ_RnOzGQdoHHLbe0oiQtbkCmHsdIbEI/edit#)
 
### Confirmation (CHECK)

When a user enters a collection id, version, and content server via a Web UI an 
appropriate PDF is generated and a link exists to download the PDF.

### Follow up (ACT)

## Bakery

[Link](./bakery)

Contains the Concourse pipelines and tasks used to generate the PDF.

## Workflow Event Resource

[README Link](./workflow-service/README.md)

The resource used to trigger the concourse pipeline and also provide information
of the event to be used by the pipeline.

## Workflow Service

[README link](./workflow-service/README.md)

A web application consisting of a [frontend](#workflow-frontend) and 
[backend](#workflow-backend). The Front end is responsible for UI interactions 
with the user, providing event information, and the creation of new events.

## License

This software is subject to the provisions of the GNU Affero General
Public License Version 3.0 (AGPL). See license.txt for details.
Copyright (c) 2019 Rice University


[vertical-slice]: https://medium.com/@thorbjorn.sigberg/the-art-of-vertical-slicing-871ee32600a8
[roadmap]: https://github.com/openstax/cnx/wiki#product-roadmap
[gob-tool]: https://cnx.org/a/content-status/
