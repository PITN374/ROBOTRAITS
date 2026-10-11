ROBOTRAITS Versioning and Release Policy

Project: PITN / ROBOTRAITS / ROBOAGENTIC
Originating organization: PowerInTheNumbers.ai
Originating author: Aaron Bailot
IP record: IP-011
Proposed ontology release: 3.1.0
Documentation date: 2026-10-11

1. Purpose

This policy defines how ROBOTRAITS ontology versions, semantic identifiers, validation rules, documentation, and release artifacts are identified and maintained.

Versioning preserves the integrity, reproducibility, and traceability of the PITN / ROBOTRAITS / ROBOAGENTIC project.

2. Semantic Versioning

ROBOTRAITS uses the following version format:

MAJOR.MINOR.PATCH

MAJOR: Introduces incompatible changes to established vocabulary semantics, identifiers, or data structures.
MINOR: Adds backward-compatible classes, properties, trait dimensions, or functionality.
PATCH: Introduces backward-compatible corrections, clarifications, or maintenance changes.

Every published release must identify its version and document the changes from the preceding release.

3. Proposed Release

The proposed ontology release is:

3.1.0

Proposed versioned ontology identifier:

https://w3id.org/robotraits/ontology/3.1.0

Proposed versioned SHACL identifier:

https://w3id.org/robotraits/shapes/3.1.0

These identifiers must correspond to the actual published release artifacts.

4. Persistent Vocabulary Identifiers

The persistent vocabulary namespace is:

https://w3id.org/robotraits#

The preferred vocabulary prefix is rt:.

Existing class, property, and trait identifiers should remain stable across compatible releases. Changes to their meanings must be documented, and deprecated terms must remain traceable through explicit deprecation metadata.

5. Release Contents

Each release should preserve:

The core OWL ontology in Turtle format.
SHACL validation shapes.
Example agent and trait-profile data.
Ontology specification and namespace documentation.
Intellectual property and provenance records.
Release notes and changelog.
Technical validation reports.
SHA-256 checksums for the released artifacts.
6. Validation Requirements

Before a release is designated validated, the project should record the actual results of:

RDF/Turtle syntax validation.
OWL 2 profile and ontology consistency checks.
SHACL validation against the published example data.
Semantic review of classes, properties, domains, ranges, and constraints.
Verification that release metadata and version identifiers agree.

Validation status must reflect executed tests and recorded results.

7. Release Identification

Release tags should follow a consistent naming convention.

Example:

robotraits-v3.1.0

Each tag should identify the exact commit containing the release files. Signed tags may be used to strengthen release authenticity and traceability.

8. Changelog Requirements

CHANGELOG.md records notable changes to the ontology, validation shapes, documentation, integration mappings, and release process.

Each release entry should include:

Version number.
Publication date.
Release status.
Added vocabulary terms.
Modified or deprecated terms.
Validation results.
Relevant migration notes.
9. Historical Preservation

Previously published releases should remain available for comparison and reproducibility.

The project should not rewrite or backdate historical commits to imply earlier publication. Corrections and later findings should be recorded through new commits and release notes.

10. Intellectual Property Attribution

Versioned ROBOTRAITS releases form part of the documented PITN / ROBOTRAITS / ROBOAGENTIC project record.

Original project materials are attributed according to the project's IP notices, provenance records, contributor documentation, and applicable licensing terms.

Project attribution: PITN / PowerInTheNumbers.ai
Originating author: Aaron Bailot
Related record: IP-011_ROBOTRAITS_TRAIT_ONTOLOGY.md

End of document.
