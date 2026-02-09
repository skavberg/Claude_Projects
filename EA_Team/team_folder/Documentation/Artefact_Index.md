# Master Artefact Index

**Organization:** Cenovus Energy Inc.
**Team:** IT Architecture - Enterprise Architecture & Solution Architecture
**Maintained By:** Documentation Specialist
**Last Updated:** 2026-02-07
**Version:** 1.0

---

## Purpose

This index catalogues all architectural artefacts produced and maintained by the IT Architecture team. It serves as the single source of truth for locating documents, tracking their status, and understanding relationships between artefacts.

---

## 1. Governance Documents

| ID | Document Name | Location | Version | Status | Owner |
|---|---|---|---|---|---|
| -- | Team Charter | `team_folder/TEAM_CHARTER.md` | 1.0 | Approved | Team Leader |
| -- | Documentation Standards Guide | `team_folder/Documentation/Documentation_Standards_Guide.md` | 1.0 | Approved | Documentation Specialist |
| -- | Master Artefact Index | `team_folder/Documentation/Artefact_Index.md` | 1.0 | Approved | Documentation Specialist |
| -- | EA Governance Process | `team_public/Process/EA_Governance_Process.md` | 1.0 | Approved | Team Leader |

---

## 2. Procedures

| ID | Document Name | Location | Version | Status | Owner |
|---|---|---|---|---|---|
| PROC-EA-001 | Architecture Review Board (ARB) Procedure | `team_public/Procedures/Architecture_Review_Procedure.md` | 1.0 | Approved | Team Leader |

---

## 3. Templates (Standards)

All templates are published in `team_public/Standards/`.

| Template Name | File Name | Version | Status | Applicable To |
|---|---|---|---|---|
| Solution Design Template | `Solution_Design_Template.md` | 1.0 | Approved | Solution Architects, Portfolio Architects |
| Conceptual Design Template | `Conceptual_Design_Template.md` | 1.0 | Approved | Solution Architects, Portfolio Architects |
| Architecture Decision Record Template | `Architecture_Decision_Record_Template.md` | 1.0 | Approved | Portfolio Architects |
| Total Cost of Ownership Report Template | `TCO_Report_Template.md` | 1.0 | Approved | Portfolio Architects |
| New Application Request Template | `New_Application_Request_Template.md` | 1.0 | Approved | Requestors, Portfolio Architects |
| EA Roadmap Template | `EA_Roadmap_Template.md` | 1.0 | Approved | Portfolio Architects |

---

## 4. EA Domain Roadmaps

| ID | Domain | Document Name | Location | Version | Status | Portfolio Architect |
|---|---|---|---|---|---|---|
| RM-INFRA-2026 | IT Infrastructure | Infrastructure Roadmap 2026 | `team_folder/Enterprise_Architects/IT_Infrastructure/Infrastructure_Roadmap_2026.md` | 0.1 | Draft | PA - Infrastructure |
| RM-CLOUD-2026 | IT Cloud | Cloud Roadmap 2026 | `team_folder/Enterprise_Architects/IT_Cloud/Cloud_Roadmap_2026.md` | 0.1 | Draft | PA - Cloud |
| RM-CYBER-2026 | IT Cyber Security | -- | -- | -- | Not Started | PA - Cyber Security |
| RM-AI-2026 | IT Artificial Intelligence | -- | -- | -- | Not Started | PA - AI |
| RM-CORP-2026 | Corporate Applications | CorporateApps Roadmap 2026 | `team_folder/Enterprise_Architects/Corporate_Applications/CorporateApps_Roadmap_2026.md` | 0.1 | Draft | PA - Corporate Apps |
| RM-UPSTREAM-2026 | Upstream Applications | -- | -- | -- | Not Started | PA - Upstream Apps |
| RM-DOWNSTREAM-2026 | Downstream Applications | -- | -- | -- | Not Started | PA - Downstream Apps |
| RM-ENTERPRISE-2026 | Enterprise Applications | -- | -- | -- | Not Started | PA - Enterprise Apps |

---

## 5. Architecture Decision Records

| ID | Title | Domain | Location | Status | Date |
|---|---|---|---|---|---|
| *No ADRs published yet* | | | | | |

ADRs will be published to `team_public/Decision_Records/` as they are approved.

---

## 6. Solution Designs

| ID | Project/Initiative | Domain | Location | Version | Status | Author |
|---|---|---|---|---|---|---|
| *No solution designs published yet* | | | | | | |

Approved solution designs will be published to `team_public/Solution_Designs/`.

---

## 7. Conceptual Designs

| ID | Project/Initiative | Domain | Location | Version | Status | Author |
|---|---|---|---|---|---|---|
| *No conceptual designs published yet* | | | | | | |

---

## 8. TCO Reports

| ID | Project/Initiative | Domain | Location | Version | Status | Author |
|---|---|---|---|---|---|---|
| *No TCO reports published yet* | | | | | | |

---

## 9. New Application Requests

| ID | Application | Requestor | Location | Status | Date |
|---|---|---|---|---|---|
| *No NARs submitted yet* | | | | | |

---

## 10. Meeting Minutes

| Date | Type | Location | Key Decisions |
|---|---|---|---|
| *No meeting minutes recorded yet* | | | |

Meeting minutes are stored in `Working/Meeting_Minutes/`.

---

## 11. Folder Structure Summary

```
EA_Team/
+-- team_folder/                          [Internal working area]
|   +-- TEAM_CHARTER.md
|   +-- Documentation/
|   |   +-- Documentation_Standards_Guide.md
|   |   +-- Artefact_Index.md             [This file]
|   +-- Enterprise_Architects/
|   |   +-- IT_Infrastructure/
|   |   |   +-- Infrastructure_Roadmap_2026.md
|   |   +-- IT_Cloud/
|   |   |   +-- Cloud_Roadmap_2026.md
|   |   +-- IT_Cyber_Security/
|   |   +-- IT_Artificial_Intelligence/
|   |   +-- Corporate_Applications/
|   |   |   +-- CorporateApps_Roadmap_2026.md
|   |   +-- Upstream_Applications/
|   |   +-- Downstream_Applications/
|   |   +-- Enterprise_Applications/
|   +-- Solution_Architects/
|   +-- Process_Advisory/
+-- team_public/                          [Published approved artefacts]
|   +-- Standards/
|   |   +-- Solution_Design_Template.md
|   |   +-- Conceptual_Design_Template.md
|   |   +-- Architecture_Decision_Record_Template.md
|   |   +-- TCO_Report_Template.md
|   |   +-- New_Application_Request_Template.md
|   |   +-- EA_Roadmap_Template.md
|   +-- Decision_Records/
|   +-- Roadmaps/
|   +-- Solution_Designs/
|   +-- Process/
|   |   +-- EA_Governance_Process.md
|   +-- Procedures/
|       +-- Architecture_Review_Procedure.md
+-- Working/                              [Active working area]
    +-- Meeting_Minutes/
    +-- team_goals/
```

---

## 12. Index Maintenance

This index is updated by the Documentation Specialist when:
- A new document is created or published
- A document status changes (e.g., Draft to Approved)
- A document is superseded or retired
- The folder structure changes

**Change History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-02-07 | Documentation Specialist | Initial index creation; catalogued all existing artefacts |
