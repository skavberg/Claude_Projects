# Cenovus Energy - IT Architecture Team RACI Matrix

**Document Owner:** Process Advisor, IT Architecture Team
**Effective Date:** February 2026
**Review Cycle:** Semi-annual (next review: August 2026)
**Classification:** Internal - IT Architecture Team
**Version:** 1.0

---

## Purpose

This RACI matrix defines accountability and responsibility assignments for all core Enterprise Architecture governance processes within the IT Architecture team at Cenovus Energy. It ensures clarity of roles across the team's EA and SA groups for each process, reducing ambiguity and supporting consistent execution.

This document should be read alongside the [IT Architecture Team Charter](../TEAM_CHARTER.md).

---

## Legend

| Code | Meaning | Definition |
|------|---------|------------|
| **R** | Responsible | Performs the work. Executes the task or activity. Multiple roles may share responsibility. |
| **A** | Accountable | Ultimately answerable for the correct completion of the work. Only one role per process. Signs off on deliverables. |
| **C** | Consulted | Provides input, expertise, or review before or during the work. Two-way communication. |
| **I** | Informed | Kept up to date on progress or outcomes. One-way communication (after the fact). |
| **-** | Not Involved | No defined role in this process. |

---

## Role Abbreviations

| Abbreviation | Role |
|---|---|
| **TL** | Team Leader (Chief Architect) |
| **PA-Infra** | Portfolio Architect - IT Infrastructure |
| **PA-Cloud** | Portfolio Architect - IT Cloud (AWS & Azure) |
| **PA-Cyber** | Portfolio Architect - IT Cyber Security |
| **PA-AI** | Portfolio Architect - IT Artificial Intelligence |
| **PA-Corp** | Portfolio Architect - Corporate Applications |
| **PA-Up** | Portfolio Architect - Upstream Applications |
| **PA-Down** | Portfolio Architect - Downstream Applications |
| **PA-Ent** | Portfolio Architect - Enterprise Applications |
| **SA Lead** | Solution Architect Lead |
| **Doc Spec** | Documentation Specialist |
| **Proc Adv** | Process Advisor |

For readability, the eight Portfolio Architects are represented individually where assignments differ by domain and collectively as **PA (All)** or **PA (Domain)** where assignments are uniform or domain-specific.

---

## 1. Architecture Review Board (ARB)

Bi-weekly governance forum that reviews new application requests, solution designs, exception requests, and architecture deviations. The ARB is the primary decision gate for technology investments at Cenovus.

| Activity | TL | PA (Domain) | PA (Other) | SA Lead | Doc Spec | Proc Adv |
|---|---|---|---|---|---|---|
| Set ARB agenda and schedule | A | C | - | C | I | R |
| Chair ARB meetings | A/R | - | - | - | - | - |
| Present domain-specific items to the board | I | R | I | C | - | - |
| Present solution designs for ARB review | C | C | - | R | - | - |
| Provide cross-domain impact assessment | A | R | C | C | - | - |
| Record ARB decisions and action items | I | - | - | - | R | C |
| Publish ARB minutes and outcomes | A | I | I | I | R | C |
| Track ARB action item completion | I | - | - | - | - | A/R |
| Manage exception and deviation requests | A | C | - | C | - | R |
| Report ARB metrics to IT Senior Leadership | A/R | - | - | - | - | C |

---

## 2. New Application Request (NAR) Process

Intake, assessment, and approval workflow for any new application or SaaS product proposed for introduction into the Cenovus technology environment.

| Activity | TL | PA (Domain) | PA (Other) | SA Lead | Doc Spec | Proc Adv |
|---|---|---|---|---|---|---|
| Receive and log new application request | I | I | - | - | - | A/R |
| Validate request completeness | - | - | - | - | - | A/R |
| Assign request to domain PA | A/R | I | - | - | - | C |
| Conduct initial domain assessment | A | R | - | C | - | - |
| Assess security and compliance posture | I | C | - | - | - | - |
| -- (IT Cyber Security review) | I | R *(PA-Cyber)* | - | - | - | - |
| Evaluate cloud/hosting requirements | I | C | - | C | - | - |
| -- (IT Cloud review) | I | R *(PA-Cloud)* | - | - | - | - |
| -- (IT Infrastructure review) | I | R *(PA-Infra)* | - | - | - | - |
| Check for application duplication/overlap | A | R | C | C | - | - |
| Prepare NAR recommendation for ARB | A | R | - | C | - | C |
| Approve/reject at ARB | A/R | C | C | C | I | I |
| Communicate decision to requestor | A/R | C | - | - | - | I |
| Update application portfolio register | I | C | - | - | R | - |
| Archive NAR documentation | I | - | - | - | A/R | - |

---

## 3. Conceptual Design Development and Review

High-level architectural blueprint produced early in a project lifecycle to establish scope, key components, integration points, and alignment with EA roadmaps before detailed solution design begins.

| Activity | TL | PA (Domain) | PA (Other) | SA Lead | Doc Spec | Proc Adv |
|---|---|---|---|---|---|---|
| Initiate conceptual design engagement | A | C | - | R | - | - |
| Gather business requirements and context | I | C | - | R | - | - |
| Develop conceptual design document | C | C | - | A/R | - | - |
| Ensure alignment with domain roadmap | A | R | - | C | - | - |
| Ensure alignment with EA standards | C | R | - | C | - | C |
| Verify integration with adjacent domains | I | C | R *(affected)* | C | - | - |
| Conduct security architecture review | I | R *(PA-Cyber)* | - | C | - | - |
| Conduct cloud architecture review | I | R *(PA-Cloud)* | - | C | - | - |
| Perform internal peer review | A | R | C | R | - | - |
| Submit conceptual design to ARB | A | C | - | R | - | I |
| ARB approval of conceptual design | A/R | C | C | C | I | I |
| Publish approved conceptual design | I | - | - | I | A/R | - |
| Maintain conceptual design template | I | - | - | C | A/R | - |

---

## 4. Solution Design Development and Review

Detailed, implementable architecture design that translates the approved conceptual design into specific technology selections, configuration details, data flows, and deployment specifications.

| Activity | TL | PA (Domain) | PA (Other) | SA Lead | Doc Spec | Proc Adv |
|---|---|---|---|---|---|---|
| Assign solution architect to project | C | C | - | A/R | - | - |
| Develop detailed solution design | C | C | - | A/R | - | - |
| Select technology components and products | C | R | C *(affected)* | R | - | - |
| Define integration and data flow architecture | I | C | C *(affected)* | A/R | - | - |
| Define infrastructure and deployment model | I | R *(PA-Infra, PA-Cloud)* | - | C | - | - |
| Incorporate security controls and patterns | I | R *(PA-Cyber)* | - | C | - | - |
| Incorporate AI/ML components (if applicable) | I | R *(PA-AI)* | - | C | - | - |
| Conduct solution design peer review | A | R | C *(affected)* | R | - | C |
| Submit solution design to ARB | A | C | - | R | - | I |
| ARB approval of solution design | A/R | C | C | C | I | I |
| Handoff to project delivery team | I | C | - | A/R | - | - |
| Publish approved solution design | I | - | - | I | A/R | - |
| Maintain solution design template | I | - | - | C | A/R | - |

---

## 5. TCO / Financial Viability Analysis

Total Cost of Ownership modelling and financial viability assessment that supports business case development, covering capital expenditure, operating expenditure, licensing, cloud consumption, support costs, and decommissioning.

| Activity | TL | PA (Domain) | PA (Other) | SA Lead | Doc Spec | Proc Adv |
|---|---|---|---|---|---|---|
| Initiate TCO analysis request | A | C | - | R | - | - |
| Define cost model scope and assumptions | A | R | C *(affected)* | R | - | - |
| Estimate infrastructure and hosting costs | I | R *(PA-Infra, PA-Cloud)* | - | C | - | - |
| Estimate licensing and subscription costs | I | R | - | C | - | - |
| Estimate integration and middleware costs | I | R *(PA-Ent)* | - | C | - | - |
| Estimate security tooling costs | I | R *(PA-Cyber)* | - | C | - | - |
| Estimate AI/ML platform costs (if applicable) | I | R *(PA-AI)* | - | C | - | - |
| Consolidate multi-year TCO model | C | C | - | A/R | - | - |
| Develop financial viability recommendation | A | C | - | R | - | - |
| Review TCO with IT Finance / FinOps | A | C | - | R | - | - |
| Present TCO at ARB (if required) | A | C | - | R | - | I |
| Publish TCO report | I | - | - | I | A/R | - |
| Maintain TCO template and cost benchmarks | I | C | - | C | A/R | - |

---

## 6. EA Roadmap Management

Each Portfolio Architect maintains a domain roadmap showing current state, transition architecture, and future state. Roadmaps are reviewed quarterly to ensure alignment with the Cenovus IT Strategic Plan and corporate business strategy.

| Activity | TL | PA (Domain) | PA (Other) | SA Lead | Doc Spec | Proc Adv |
|---|---|---|---|---|---|---|
| Set roadmap planning cycle and timeline | A/R | I | I | I | I | C |
| Develop and maintain domain roadmap | A | R | - | C | - | - |
| Align roadmap with IT Strategic Plan | A/R | R | - | C | - | - |
| Align roadmap with business unit priorities | A | R | - | - | - | - |
| Identify cross-domain dependencies | A | R | C *(affected)* | C | - | - |
| Conduct quarterly roadmap review | A/R | R | C | C | I | C |
| Consolidate enterprise-wide roadmap view | A/R | C | C | C | R | - |
| Identify and escalate roadmap conflicts | A/R | R | C | C | - | I |
| Publish updated roadmaps | A | I | I | I | R | - |
| Report roadmap progress to IT Senior Leadership | A/R | C | - | - | - | C |
| Track roadmap milestones and delivery status | A | R | - | - | - | R |

---

## 7. Architecture Decision Records (ADR)

Formal documentation of significant architectural decisions, their context, rationale, alternatives considered, and consequences. ADRs create an institutional memory for the team and provide traceability for technology choices.

| Activity | TL | PA (Domain) | PA (Other) | SA Lead | Doc Spec | Proc Adv |
|---|---|---|---|---|---|---|
| Identify decision requiring an ADR | C | R | - | R | - | C |
| Draft ADR document | C | R | - | R | - | - |
| Circulate ADR for peer review | I | R | C *(affected)* | R | - | - |
| Approve ADR | A/R | C | C | C | - | I |
| Publish ADR to decision record repository | I | - | - | - | A/R | - |
| Maintain ADR index and cross-references | I | - | - | - | A/R | C |
| Conduct periodic ADR relevance review | A | C | - | C | - | R |
| Supersede or retire outdated ADRs | A/R | R | - | R | - | C |
| Maintain ADR template | I | - | - | C | A/R | C |

---

## 8. Standards Development and Publication

Creation, review, approval, and publication of technology standards, reference architectures, and design patterns that govern technology choices across Cenovus.

| Activity | TL | PA (Domain) | PA (Other) | SA Lead | Doc Spec | Proc Adv |
|---|---|---|---|---|---|---|
| Identify need for new or updated standard | A | R | C | C | - | C |
| Research industry standards and best practices | I | R | C | C | - | - |
| Draft standard or reference architecture | C | R | C *(affected)* | C | - | - |
| Circulate draft for team review | I | R | C | C | C | C |
| Incorporate feedback and finalize | A | R | - | C | - | - |
| Approve standard for publication | A/R | C | C | C | I | I |
| Format and publish to standards repository | I | - | - | - | A/R | - |
| Communicate new standard to IT organization | A/R | C | - | C | I | C |
| Monitor standard adoption and compliance | A | R | - | C | - | R |
| Conduct periodic standards review (annual) | A | R | C | C | - | R |
| Retire or supersede obsolete standards | A/R | R | I | C | R | C |

---

## 9. Technology Evaluation and Vendor Assessment

Structured evaluation of new technologies, platforms, and vendor products to determine their suitability, maturity, risk, and fit within the Cenovus architecture landscape. Includes proof-of-concept coordination.

| Activity | TL | PA (Domain) | PA (Other) | SA Lead | Doc Spec | Proc Adv |
|---|---|---|---|---|---|---|
| Identify technology for evaluation | C | R | - | C | - | - |
| Define evaluation criteria and scorecard | A | R | C *(affected)* | C | - | C |
| Conduct vendor briefings and demos | I | R | C *(affected)* | C | - | - |
| Assess security posture of technology | I | R *(PA-Cyber)* | - | - | - | - |
| Assess cloud compatibility and cost model | I | R *(PA-Cloud)* | - | - | - | - |
| Assess infrastructure requirements | I | R *(PA-Infra)* | - | - | - | - |
| Assess AI/ML capabilities (if applicable) | I | R *(PA-AI)* | - | - | - | - |
| Coordinate proof-of-concept (PoC) | C | R | C *(affected)* | R | - | - |
| Document evaluation findings | I | R | - | C | C | - |
| Present recommendation to ARB | A | R | C | C | I | I |
| Approve/reject technology for use | A/R | C | C | C | I | I |
| Update technology standards (if approved) | A | R | I | C | R | - |

---

## 10. Application Rationalization

Ongoing analysis of the enterprise application portfolio to identify redundancy, overlap, underutilization, and modernization opportunities. Supports cost optimization and technical debt reduction aligned with Cenovus operational efficiency goals.

| Activity | TL | PA (Domain) | PA (Other) | SA Lead | Doc Spec | Proc Adv |
|---|---|---|---|---|---|---|
| Maintain application portfolio inventory | A | R | - | C | R | - |
| Map applications to business capabilities | A | R | - | C | - | - |
| Map applications to functional capabilities | A | R | - | C | - | - |
| Identify redundant or overlapping applications | A | R | C | C | - | - |
| Analyse application usage and health metrics | I | R | - | C | - | C |
| Develop rationalization recommendations | A | R | C *(affected)* | C | - | - |
| Estimate cost savings and migration effort | C | R | C *(affected)* | R | - | - |
| Present rationalization proposals to ARB | A | R | C | C | I | I |
| Approve rationalization decisions | A/R | C | C | C | I | I |
| Track rationalization execution progress | A | R | - | C | - | R |
| Report rationalization outcomes to leadership | A/R | C | - | - | - | C |
| Update portfolio register post-rationalization | I | C | - | - | A/R | - |

---

## 11. Stakeholder Engagement

Structured engagement with business unit leadership, IT delivery managers, project managers, and IT Senior Leadership to ensure architecture activities remain aligned with business priorities and that architectural guidance is understood and adopted.

| Activity | TL | PA (Domain) | PA (Other) | SA Lead | Doc Spec | Proc Adv |
|---|---|---|---|---|---|---|
| Engage IT Senior Leadership on strategy | A/R | C | - | - | - | - |
| Engage business unit leads on domain needs | A | R | - | - | - | - |
| Engage IT delivery managers on projects | I | R | - | R | - | - |
| Engage project managers on design deliverables | I | C | - | A/R | - | - |
| Represent architecture in IT governance forums | A/R | C | - | C | - | - |
| Maintain stakeholder communication plan | A | - | - | - | - | R |
| Conduct architecture awareness sessions | A | R | - | R | - | C |
| Gather feedback on EA processes and services | A | C | - | C | - | R |
| Report team performance and value delivered | A/R | C | - | C | - | C |
| Manage stakeholder escalations | A/R | R | - | R | - | I |

---

## 12. EA Governance and Compliance Monitoring

Ongoing monitoring and enforcement of architectural governance across the IT organization, including compliance with approved standards, design patterns, ARB decisions, and deviation management.

| Activity | TL | PA (Domain) | PA (Other) | SA Lead | Doc Spec | Proc Adv |
|---|---|---|---|---|---|---|
| Define EA governance framework and policies | A/R | C | C | C | - | R |
| Maintain governance process documentation | A | - | - | - | C | R |
| Monitor compliance with EA standards | A | R | - | C | - | R |
| Monitor compliance with ARB decisions | A | C | - | C | - | A/R |
| Conduct periodic compliance audits | A | C | - | C | - | R |
| Manage architectural exceptions register | A | C | - | C | R | R |
| Track and report exception expiry dates | I | I | - | I | - | A/R |
| Escalate non-compliance to Team Leader | - | C | - | C | - | A/R |
| Define and publish EA KPIs and metrics | A/R | C | - | C | - | R |
| Produce EA governance dashboards | A | - | - | - | C | R |
| Conduct governance retrospectives | A/R | C | C | C | - | R |
| Report governance health to IT Senior Leadership | A/R | - | - | - | - | C |
| Maintain compliance artefact repository | I | - | - | - | A/R | C |

---

## Summary Matrix (Process Level)

High-level view showing the primary Accountable and Responsible roles for each process.

| # | Process | Accountable | Primary Responsible |
|---|---------|------------|-------------------|
| 1 | Architecture Review Board (ARB) | Team Leader | Team Leader (chair), PA (Domain), Process Advisor (admin) |
| 2 | New Application Request (NAR) | Team Leader | PA (Domain), Process Advisor (intake) |
| 3 | Conceptual Design | SA Lead | SA Lead, PA (Domain) |
| 4 | Solution Design | SA Lead (design), TL (approval) | SA Lead, PA (Domain) |
| 5 | TCO / Financial Viability | SA Lead (analysis), TL (approval) | SA Lead, PA (Domain) |
| 6 | EA Roadmap Management | Team Leader | PA (Domain) |
| 7 | Architecture Decision Records | Team Leader (approval) | PA (Domain), SA Lead |
| 8 | Standards Development | Team Leader (approval) | PA (Domain) |
| 9 | Technology Evaluation | Team Leader (approval) | PA (Domain), SA Lead |
| 10 | Application Rationalization | Team Leader | PA (Domain), SA Lead |
| 11 | Stakeholder Engagement | Team Leader | PA (Domain), SA Lead, Process Advisor |
| 12 | EA Governance & Compliance | Team Leader | Process Advisor, PA (Domain) |

---

## Notes

### General Principles

1. **Single Accountability:** Each process has exactly one Accountable role. The Team Leader (Chief Architect) holds ultimate accountability for all EA processes as the team's senior leader. Where the SA Lead is shown as Accountable, this is delegated accountability for design-delivery activities.

2. **Domain Assignment:** When a process is triggered by a request or project, the "PA (Domain)" refers to the Portfolio Architect whose domain is most directly affected. The Team Leader assigns domain ownership when it is ambiguous or spans multiple domains.

3. **Cross-Domain Consultation:** "PA (Other)" or "C *(affected)*" indicates that Portfolio Architects from adjacent or affected domains must be consulted. For example, a new upstream application that requires cloud hosting will involve PA-Up as the primary domain architect with PA-Cloud and PA-Cyber consulted.

4. **Cyber Security Review:** PA-Cyber is consulted or responsible on every process that introduces new technology, changes data flows, or modifies the security posture. This is non-negotiable given Cenovus's critical infrastructure obligations under Canadian energy sector regulations.

5. **Documentation Specialist** is responsible for the publication, indexing, and template maintenance of all architectural artefacts but is not involved in the technical content development.

6. **Process Advisor** owns the governance machinery: scheduling, intake, tracking, metrics, compliance monitoring, and process improvement. The Process Advisor does not make architectural decisions.

### Oil and Gas Specific Considerations

7. **OT/IT Convergence:** Architecture decisions affecting operational technology (SCADA, DCS, field instrumentation) require mandatory consultation with PA-Infra and PA-Cyber due to safety and regulatory implications at Cenovus upstream and downstream facilities.

8. **Regulatory Compliance:** Designs touching production reporting, emissions monitoring, pipeline integrity, or financial reporting systems require additional compliance review steps. The Process Advisor coordinates with Cenovus's Regulatory and Compliance teams as needed.

9. **FinOps Integration:** TCO analyses for cloud-hosted solutions must include PA-Cloud for consumption modelling and alignment with Cenovus's FinOps practice.

10. **SAP Ecosystem:** Changes to SAP or SAP-adjacent systems (Corporate Applications domain) often have enterprise-wide integration impacts. PA-Corp and PA-Ent must both be engaged on such requests.

### Escalation Path

11. Disputes regarding RACI assignments or process ownership are escalated to the Team Leader for resolution.

12. If the Team Leader is unavailable, the SA Lead acts as delegate for ARB and design approvals. Portfolio-level governance decisions are deferred until the Team Leader returns.

### Document Maintenance

13. This RACI matrix is reviewed semi-annually by the Process Advisor and approved by the Team Leader.

14. Material changes to team structure, processes, or governance scope require an out-of-cycle revision.

15. All team members are responsible for flagging gaps or conflicts in RACI assignments to the Process Advisor.

---

*Last updated: February 8, 2026*
*Prepared by: Process Advisor, IT Architecture Team*
*Approved by: Team Leader (Chief Architect), IT Architecture Team*
