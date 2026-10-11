ROBOTRAITS Versioning and Release Policy

Project: PITN.ai / ROBOTRAITS / ROBOAGENTIC
Author: Aaron Bailot
Organization: PowerInTheNumbers.ai
IP Record: IP-011
Version: 3.1.0
Date: 2026-10-11
Copyright: © 2026 Aaron Bailot / PowerInTheNumbers.ai. All rights reserved.

1. Purpose

This policy defines the versioning, release identification, change tracking, and preservation procedures for the ROBOTRAITS trait-based robotic intelligence ontology.

ROBOTRAITS uses explicit semantic versioning to maintain stable identifiers, document changes, and support reproducible ontology releases throughout the PITN.ai and ROBOAGENTIC ecosystem.

2. Version Format

ROBOTRAITS follows the format:

MAJOR.MINOR.PATCH

Example:

3.1.0

MAJOR: Introduces incompatible semantic changes, removes established terms, or changes established meaning.
MINOR: Introduces backward-compatible classes, properties, trait dimensions, or validation capabilities.
PATCH: Corrects definitions, documentation, metadata, or compatible validation details without changing established semantics.
3. Release Identifiers

Persistent vocabulary namespace:

https://w3id.org/robotraits#

Versioned ontology:

https://w3id.org/robotraits/ontology/3.1.0

Versioned SHACL shapes:

https://w3id.org/robotraits/shapes/3.1.0

Git release tag:

robotraits-v3.1.0

Each published release must identify its ontology version, associated validation shapes, documentation, and release evidence.

4. Release Components

A ROBOTRAITS release includes the following project artifacts:

ontology/robotraits.ttl
ontology/robotraits-shapes.ttl
ontology/robotraits-example.ttl
docs/NAMESPACE.md
docs/PROVENANCE.md
docs/VERSIONING.md
docs/ONTOLOGY-SPECIFICATION.md
docs/ROBOTRAITS-ROBOPARTS-INTEGRATION.md
IP-NOTICE.md
IP-011_ROBOTRAITS_TRAIT_ONTOLOGY.md
NOTICE.md
CHANGELOG.md
5. Change Management

Every substantive change must be recorded with:

Change identifier or commit reference.
Date recorded.
Author or contributor.
Affected ontology terms and documents.
Description and technical rationale.
Compatibility classification.
Relevant validation results.

Existing Git history and release artifacts must be preserved as part of the development record.

6. Semantic Compatibility

The following principles govern compatibility:

Established class and property identifiers remain stable.
New trait dimensions should follow existing naming and definition conventions.
Deprecated terms must retain documented historical references.
Changes to value scales or constraint semantics must be explicitly documented.
Trait profiles must identify their own versions independently of ontology releases.
ROBOPARTS component identifiers remain separate from ROBOTRAITS behavioral profile identifiers.
Safety and authorization requirements take precedence over trait preferences.
7. Validation and Release Evidence

Each release records the results of:

RDF and Turtle syntax validation.
OWL ontology consistency checks.
OWL profile checks, where applicable.
SHACL validation against the published example dataset.
Semantic compatibility review.
SHA-256 checksums for release artifacts.

Validation status must reflect the actual execution results associated with the release.

8. Release Preservation

For each release, preserve:

Exact release files.
Git commit identifier.
Version tag and signature, when used.
Release notes.
Validation reports.
SHA-256 checksum manifest.
Attribution and provenance records.
Applicable license and notice files.

Published releases must not be silently replaced with different contents under the same version identifier.

9. Intellectual Property and Attribution

Original ROBOTRAITS ontology materials, project-specific semantic definitions, validation rules, and documentation are attributed to the PITN.ai / ROBOTRAITS / ROBOAGENTIC initiative and Aaron Bailot / PowerInTheNumbers.ai, as documented in the project's authorship and provenance records.

IP Record: IP-011_ROBOTRAITS_TRAIT_ONTOLOGY.md

Copyright © 2026 Aaron Bailot / PowerInTheNumbers.ai. All rights reserved.

10. Document Control

Document: docs/VERSIONING.md
Project: PITN.ai / ROBOTRAITS / ROBOAGENTIC
Version: 3.1.0
Author: Aaron Bailot
Organization: PowerInTheNumbers.ai
Date: 2026-10-11

Copyright © 2026 Aaron Bailot / PowerInTheNumbers.ai. All rights reserved.
