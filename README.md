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
* [License](#license)

## A3 Planning

A3 planning is a technique created by Toyota and Lean manufacturing. The idea
is to focus on a problem and convey all the information necessary in an A3 
size of paper (11.69 x 16.53 inches). However,  it's not the size of the paper 
that is important but rather the approach to solving the problem and
conveying the right information to the people that need it.

### Background (PLAN)

This spike is to allow the developers free experimentation to prototype
putting together a Concourse pipeline that produces a Baked PDF.
The pipeline can be trigger however the developer sees fit.
The resulting PDF can be saved wherever the develper sees fit.
 
### Current condition (PLAN)

[cnx-recipes][cnx-recipes] provides most of the functionality
needed to produce a PDF.
This uses [cnx-archive][cnx-archive],
which acts as a typical backend web application.
It exposes a web API that we use to acquire content for producing a PDF.

(Legacy PDF generation is not worth discussing.)

### Goal / Target Condition (PLAN)

We know how it is architected at the moment is developer focused,
but we are choosing to ignore that in favor of virtically slicing
our idealistic goals with that of constrained resources and time.

1. A PDF is produced for the requested book
1. The PDF is put somewhere it can be accessed (for analysis purposes only)
1. The pipeline doesn't clog concourse.openstax.org

### Root Cause Analysis (PLAN)

Textbook developers would like to automate the generation of PDFs using HTML, because doing this by hand is boring.

### Epics, Stories, and Task Cards (DO)

* [Spike to Deliver PDF with Concourse](https://github.com/openstax/cnx/issues/723)
 
### Confirmation (CHECK)

- Given a book, when a request is made to produce a Baked PDF then produce the Baked PDF.
- Given a produced PDF, when the PDF is completely put togetehr, then put it in place where it can be retrieved.


<!-- Given ... when ... then ... -->


### Follow up (ACT)


## License

This software is subject to the provisions of the GNU Affero General
Public License Version 3.0 (AGPL). See license.txt for details.
Copyright (c) 2019 Rice University
