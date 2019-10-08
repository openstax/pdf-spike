# Content: Workflow, Transitions & Artifacts

## Table of Contents

* [Workflow](#workflow)
* [Artifacts](#license)
* [License](#license)


## Workflows

The following are workflows for OpenStax content. We transition states to produce high quality content and visually appealing artifacts for the end consumer.

The [OpenStax Workflow](#openstax-workflow) deals with creating and editing content to a reviewed and publically viewable state. The [Outputs workflow](#PDF-workflow) annotates the content and must start in the final state of the *OpenStax Workflow*. These workflows combined create a cohesive behavioral path that Content Managers can follow (and modify as they see fit).

<!-- ### Major states of visibility and access -->

<!-- As previously stated the two major states of visibility and access are Public and Drafting. The Drafting state typically starts with a newly identifyable (e.g. by name 'errata-foo-bar' or uuid) content item makes it visible and accessible to the creator and others in the ACL. (At this time there is no reason a draft needs to blocked from annonymous viewing. TBD) -->

<!-- The Public state is typically seen as the "end state" or publically consumable state, where the content item is visible and accessible by annonymous consumers. -->

<!-- The Public state for OpenStax books is usually the point where a versioned item is created and kept for historic use. Though, this is a technical detail that should not be focused on. It's mentioned here only to bridge the understanding with what currently exists. -->

### OpenStax Workflow

<!-- An item of content is "Public" in its final state of "Accepted Publication" (for legacy content) or "Baked Publication" (all content in the future). When one starts the *Editing workflow* at "Drafting" the item of content is created or copied. That new item of content is then put into the "Drafting" state. -->

An item of content is either created or edited and starts in the *initial state* of [Draft](#draft). From this state the content can be saved without leaving the Drafting state. When the user is ready to have their work reviewed before making it publicly consumable they transition to the [Review](#review) state. Once in the Review state reviewing users can approve the content, which effectively transitions it to the [Public](#public) state.

`Draft -> Review -> Public`

Once in this state, the [Outputs Workflow](#outputs-workflow) can be initiated. Thus allowing the outputs workflow to be kicked off prior to the final [Public](#public) state. (TBD, A state between Review and Public could ensure that the outputs are ready. This would mean that when a piece of content goes public, all of the artifacts go public as well.)


### Outputs Workflow

The Outputs Workflow can be kicked off when the content is in a Review or Public state (aka pre-condition for initializing the workflow). The *output* annotation on the content begins in a [Requested](#requested) *initial state*. Once the annotation has been fulfilled (...technical details) the workflow can transition to the [Review](#outputs-review) state. Once a review (or reviewers) has accepted the output artifact the output annotation transitions to the [Accepted](#accepted) state.

`Requested -> Review -> Accepted`

## States

### Drafting

Available transitions: Reviewing Content, Submission to Publication (with permission)

### Reviewing Content

Available transitions: Submission to Publication

### Submission to Publication

Available transitions: Accepted Publication, Rejected Publication

### Accepted Publication

### Baked Publication

### PDF Artifact Available




## Artifacts

### Raw

### Baked

### PDF

### REX

## License

This software is subject to the provisions of the GNU Affero General
Public License Version 3.0 (AGPL). See license.txt for details.
Copyright (c) 2019 Rice University
