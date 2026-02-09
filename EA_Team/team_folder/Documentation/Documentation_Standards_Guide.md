# Documentation Standards Guide

**Organization:** Cenovus Energy Inc.
**Team:** IT Architecture - Enterprise Architecture & Solution Architecture
**Document Owner:** Documentation Specialist
**Version:** 1.0
**Effective Date:** 2026-02-07
**Status:** Approved

---

## 1. Purpose

This guide establishes the documentation standards for the IT Architecture team at Cenovus Energy. It defines naming conventions, version control procedures, the document lifecycle, folder structure, and template usage guidelines. All team members are expected to follow these standards to ensure consistency, traceability, and quality across all architectural artefacts.

---

## 2. Naming Conventions

### 2.1 Document ID Formats

Each document type uses a standard identifier format:

| Document Type | ID Format | Example |
|---|---|---|
| Solution Design | `SD-[YEAR]-[SEQ]` | SD-2026-001 |
| Conceptual Design | `CD-[YEAR]-[SEQ]` | CD-2026-001 |
| Architecture Decision Record | `ADR-[YEAR]-[SEQ]` | ADR-2026-001 |
| Total Cost of Ownership Report | `TCO-[YEAR]-[SEQ]` | TCO-2026-001 |
| New Application Request | `NAR-[YEAR]-[SEQ]` | NAR-2026-001 |
| EA Roadmap | `RM-[DOMAIN]-[YEAR]` | RM-CLOUD-2026 |
| Procedure | `PROC-EA-[SEQ]` | PROC-EA-001 |
| Meeting Minutes | `MM-[YYYY-MM-DD]` | MM-2026-02-07 |

- **YEAR** = Four-digit calendar year (e.g., 2026)
- **SEQ** = Three-digit sequential number, zero-padded (e.g., 001, 002)
- **DOMAIN** = Short domain code (see Section 2.3)

### 2.2 File Naming Convention

All files follow the pattern:

```
[DescriptiveName]_[OptionalQualifier].md
```

Rules:
- Use **PascalCase** with underscores separating major words (e.g., `Solution_Design_Template.md`)
- No spaces in file names
- Use `.md` (Markdown) as the standard file format
- Include the year in roadmap and annual documents (e.g., `Cloud_Roadmap_2026.md`)
- Do not embed version numbers in file names; version control is managed within the document header

### 2.3 Domain Codes

Standard short codes for EA domains:

| Domain | Code | Folder Name |
|---|---|---|
| IT Infrastructure | `INFRA` | IT_Infrastructure |
| IT Cloud | `CLOUD` | IT_Cloud |
| IT Cyber Security | `CYBER` | IT_Cyber_Security |
| IT Artificial Intelligence | `AI` | IT_Artificial_Intelligence |
| Corporate Applications | `CORP` | Corporate_Applications |
| Upstream Applications | `UPSTREAM` | Upstream_Applications |
| Downstream Applications | `DOWNSTREAM` | Downstream_Applications |
| Enterprise Applications | `ENTERPRISE` | Enterprise_Applications |

### 2.4 Folder Naming Convention

- Use **PascalCase** with underscores (e.g., `Decision_Records`, `Meeting_Minutes`)
- Folder names should be descriptive and not abbreviated
- No spaces or special characters

---

## 3. Version Control Procedures

### 3.1 Version Numbering

Documents use a two-part version number: **Major.Minor**

| Change Type | Version Increment | Example |
|---|---|---|
| Initial draft | 0.1 | First working draft |
| Minor edits (typos, formatting, clarifications) | +0.1 | 0.1 to 0.2 |
| Significant content changes during draft | +0.1 | 0.2 to 0.3 |
| First approved version | 1.0 | Approved by ARB or Team Leader |
| Minor updates to approved version | +0.1 | 1.0 to 1.1 |
| Major revision (scope change, re-architecture) | +1.0 | 1.0 to 2.0 |

### 3.2 Change History

Every document must include a change history table in its header or appendix:

```markdown
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | 2026-02-07 | J. Smith | Initial draft |
| 0.2 | 2026-02-14 | J. Smith | Incorporated review feedback |
| 1.0 | 2026-02-21 | J. Smith | Approved by ARB |
```

### 3.3 Version Control Rules

1. **Every save that changes content** should increment the minor version
2. **Approved documents** receive a major version number (1.0, 2.0, etc.)
3. The **Date** field in the document header always reflects the last modification date
4. Previous versions are retained by appending `_vX.X` to archived copies only (the current version file never has a version suffix)
5. The Documentation Specialist maintains the master artefact index with current version numbers

---

## 4. Document Lifecycle

### 4.1 Lifecycle Stages

All architectural documents progress through the following stages:

```
Draft --> In Review --> Approved --> [Superseded | Retired]
```

| Status | Description | Permissions |
|---|---|---|
| **Draft** | Work in progress; not yet ready for formal review | Author may edit freely |
| **In Review** | Submitted for peer review and/or ARB review | Edits require author coordination |
| **Approved** | Formally accepted through governance process | Changes require new version and re-approval |
| **Superseded** | Replaced by a newer version or document | Read-only; reference only |
| **Retired** | No longer applicable; archived | Read-only; retained for audit trail |

### 4.2 Status-Specific Rules

**Draft**
- Author sets status to "Draft" when creating the document
- Document ID is assigned at creation time to ensure traceability
- May be shared informally for early feedback

**In Review**
- Author sets status to "In Review" when submitting for formal review
- Reviewer comments are collected and addressed
- Author increments version with each revision during review

**Approved**
- Status set to "Approved" after ARB or Team Leader sign-off
- Version number advances to next whole number (e.g., 0.5 becomes 1.0)
- Published to the appropriate `team_public/` folder

**Superseded**
- When a new version of a document is approved, the prior approved version is marked "Superseded by [New Document ID or version]"
- ADRs use the format "Superseded by ADR-XXXX"

**Retired**
- Documents no longer relevant are marked "Retired" with a retirement date
- Retired documents remain in the repository for historical reference

### 4.3 Approval Authority

| Document Type | Approval Authority |
|---|---|
| Solution Design | Portfolio Architect + Team Leader + IT Senior Leadership |
| Conceptual Design | Portfolio Architect + Team Leader |
| ADR | Portfolio Architect + Team Leader |
| TCO Report | Portfolio Architect + Team Leader + IT Finance |
| NAR | Portfolio Architect + Team Leader + ARB Chair |
| EA Roadmap | Team Leader + IT Senior Leadership |
| Procedures | Team Leader |

---

## 5. Folder Structure Guide

### 5.1 Top-Level Structure

```
EA_Team/
|
+-- team_folder/              (Internal team working area)
|   +-- TEAM_CHARTER.md
|   +-- Documentation/        (Documentation standards, indexes, guides)
|   +-- Enterprise_Architects/
|   |   +-- IT_Infrastructure/
|   |   +-- IT_Cloud/
|   |   +-- IT_Cyber_Security/
|   |   +-- IT_Artificial_Intelligence/
|   |   +-- Corporate_Applications/
|   |   +-- Upstream_Applications/
|   |   +-- Downstream_Applications/
|   |   +-- Enterprise_Applications/
|   +-- Solution_Architects/
|   +-- Process_Advisory/
|
+-- team_public/              (Published artefacts - approved and shared)
|   +-- Standards/            (Approved templates and standards)
|   +-- Decision_Records/     (Approved ADRs)
|   +-- Roadmaps/            (Published domain roadmaps)
|   +-- Solution_Designs/     (Approved solution designs)
|   +-- Process/             (Governance process documentation)
|   +-- Procedures/          (Operational procedures)
|
+-- Working/                  (Active working area)
    +-- Meeting_Minutes/      (ARB and team meeting minutes)
    +-- team_goals/           (OKRs and team goals tracking)
```

### 5.2 Folder Usage Rules

| Folder | Purpose | Who Writes Here |
|---|---|---|
| `team_folder/Documentation/` | Documentation standards, indexes, guides | Documentation Specialist |
| `team_folder/Enterprise_Architects/[Domain]/` | Draft domain artefacts (roadmaps, analyses) | Portfolio Architects |
| `team_folder/Solution_Architects/` | Draft solution designs and working documents | Solution Architects |
| `team_folder/Process_Advisory/` | Draft process documents and governance materials | Process Advisor |
| `team_public/Standards/` | Approved templates and reference standards | Documentation Specialist (publish) |
| `team_public/Decision_Records/` | Approved ADRs | Portfolio Architects (publish after approval) |
| `team_public/Roadmaps/` | Approved domain roadmaps | Portfolio Architects (publish after approval) |
| `team_public/Solution_Designs/` | Approved solution designs | Solution Architects (publish after approval) |
| `team_public/Process/` | Approved governance processes | Process Advisor (publish after approval) |
| `team_public/Procedures/` | Approved operational procedures | Process Advisor (publish after approval) |
| `Working/Meeting_Minutes/` | Meeting notes and action items | Any team member |
| `Working/team_goals/` | OKRs, goals, and progress tracking | Team Leader |

### 5.3 Publishing Workflow

1. Author creates/edits document in the appropriate `team_folder/` subdirectory
2. Document goes through review and approval per Section 4
3. Upon approval, the document is copied/published to the corresponding `team_public/` folder
4. The `team_public/` version is the authoritative approved copy
5. The Documentation Specialist updates the Artefact Index when documents are published

---

## 6. Template Usage Guidelines

### 6.1 Available Templates

All templates are located in `team_public/Standards/`:

| Template | File Name | When to Use |
|---|---|---|
| Solution Design | `Solution_Design_Template.md` | Detailed design for a project or initiative, pre-implementation |
| Conceptual Design | `Conceptual_Design_Template.md` | High-level architecture for early project stages |
| Architecture Decision Record | `Architecture_Decision_Record_Template.md` | Recording significant architectural decisions |
| Total Cost of Ownership | `TCO_Report_Template.md` | Financial analysis for proposed solutions |
| New Application Request | `New_Application_Request_Template.md` | Requesting approval for a new application |
| EA Roadmap | `EA_Roadmap_Template.md` | Domain-level architecture roadmap |

### 6.2 Template Usage Rules

1. **Always start from the template.** Copy the template to your working folder before editing
2. **Do not modify the template files** in `team_public/Standards/`. Propose changes to the Documentation Specialist
3. **Complete all mandatory sections.** If a section is not applicable, note "N/A - [reason]" rather than deleting it
4. **Preserve the section numbering.** Do not renumber or reorder sections
5. **Fill in the document header** (ID, Author, Domain, Date, Version, Status) before any other content
6. **Use Markdown tables** as provided in the templates; do not substitute with other formats
7. **Diagrams** should be referenced as links or embedded images; describe them in text if the diagram is not yet available

### 6.3 Template Change Process

To propose a change to a template:
1. Submit a change request to the Documentation Specialist with the proposed modification and rationale
2. Documentation Specialist reviews and prepares an updated template draft
3. The draft is circulated to the EA team for feedback
4. Team Leader approves the template change
5. Updated template is published to `team_public/Standards/` and the Artefact Index is updated

---

## 7. General Writing Standards

### 7.1 Formatting

- Use **Markdown** (.md) for all documents
- Use heading levels consistently: `#` for document title, `##` for major sections, `###` for subsections
- Use tables for structured data (as shown in templates)
- Use bullet lists for enumerations; numbered lists for sequential steps
- Horizontal rules (`---`) separate the header block from the body

### 7.2 Dates

- All dates use **ISO 8601 format: YYYY-MM-DD** (e.g., 2026-02-07)
- Planning horizons use the format "Current Year - Current Year + N" (e.g., 2026-2029)

### 7.3 Currency

- All financial figures are in **Canadian Dollars (CAD)** unless explicitly stated otherwise
- Use thousands separators for figures over 999 (e.g., $1,250,000)

### 7.4 Terminology

- Use "Cenovus Energy" on first reference; "Cenovus" is acceptable thereafter
- Use the domain names exactly as listed in the Team Charter
- Use "artefact" (not "artifact") for consistency with existing documentation
- Use "Portfolio Architect" and "Solution Architect" as formal role titles

### 7.5 Confidentiality

- All architectural documents are classified as **Internal** by default
- Documents containing financial details, security architecture, or vendor-specific pricing should be marked **Confidential**
- Do not include passwords, API keys, or access credentials in any document

---

## 8. Quality Checklist

Before submitting any document for review, verify:

- [ ] Document ID assigned and follows naming convention
- [ ] All header fields completed (Author, Domain, Date, Version, Status)
- [ ] Correct template used as the starting point
- [ ] All mandatory sections completed or marked N/A with reason
- [ ] Tables properly formatted and populated
- [ ] Business capabilities and functional capabilities mapped (where applicable)
- [ ] Financial figures include appropriate detail and currency
- [ ] Risks identified with likelihood, impact, and mitigation
- [ ] Approvals section present with correct roles listed
- [ ] Change history updated
- [ ] No confidential data exposed (credentials, keys, etc.)
- [ ] Spelling and grammar reviewed
- [ ] Cross-references to related documents are accurate

---

## 9. Contact

For questions about documentation standards, template requests, or artefact management, contact the **Documentation Specialist** on the IT Architecture team.

---

*This guide is maintained by the Documentation Specialist and reviewed annually or when significant process changes occur.*
