# Enterprise Architecture Process Metrics & KPI Framework

**Cenovus Energy -- IT Architecture Team**
**Document Owner:** Process Advisory Lead, Enterprise Architecture
**Effective Date:** 2026-Q1 (Baseline Launch)
**Review Cycle:** Quarterly
**Classification:** Internal Use Only

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [Metric Definitions by Process Area](#2-metric-definitions-by-process-area)
   - 2.1 Architecture Review Board (ARB)
   - 2.2 New Application Request (NAR) Process
   - 2.3 Conceptual and Solution Design Lifecycle
   - 2.4 TCO / Financial Viability Analysis
   - 2.5 EA Roadmap Management
   - 2.6 Architecture Decision Records (ADR)
   - 2.7 Standards Compliance
   - 2.8 Application Rationalization
   - 2.9 Stakeholder Engagement
3. [Executive Dashboard -- Senior Leadership Roll-Up](#3-executive-dashboard--senior-leadership-roll-up)
4. [EA Maturity Scoring Model](#4-ea-maturity-scoring-model)
5. [Continuous Improvement Recommendations](#5-continuous-improvement-recommendations)
6. [2026-Q1 Baseline Targets](#6-2026-q1-baseline-targets)
7. [Appendix -- Data Collection Sources and Tooling](#7-appendix--data-collection-sources-and-tooling)

---

## 1. Purpose and Scope

This document establishes the measurable Key Performance Indicators (KPIs) that govern the effectiveness, efficiency, and maturity of Enterprise Architecture processes at Cenovus Energy. It applies to all EA governance activities managed by the IT Architecture team across Upstream, Downstream, Midstream, and Corporate IT domains.

### Guiding Principles

- **Measure what matters.** Every KPI must connect to a business outcome: cost avoidance, risk reduction, speed of delivery, or strategic alignment.
- **Keep it collectible.** No metric is defined unless there is a realistic, repeatable way to gather the data with current tooling (ServiceNow, LeanIX/Ardoq, SharePoint, Azure DevOps).
- **Thresholds drive action.** Each metric has a target (green), caution (amber), and critical (red) threshold so that the team knows exactly when to intervene.
- **Transparency over perfection.** Publishing imperfect numbers and improving them quarterly is better than waiting for a perfect data pipeline.

### RACI for Metrics Program

| Role | Responsibility |
|------|---------------|
| VP, Information Technology | Accountable for executive dashboard review |
| Director, Enterprise Architecture | Accountable for overall metrics program |
| EA Process Advisory Lead | Responsible for collection, analysis, and reporting |
| Domain Architects (Upstream, Downstream, Midstream, Corporate) | Responsible for domain-specific data inputs |
| Solution Architects | Responsible for project-level data capture |
| IT PMO | Consulted for project and financial data |
| IT Finance | Consulted for TCO validation |

---

## 2. Metric Definitions by Process Area

---

### 2.1 Architecture Review Board (ARB)

The ARB convenes bi-weekly to review architecture proposals, exception requests, standards deviations, and design approvals. These metrics track whether the board is operating efficiently and adding value.

#### KPI-ARB-01: ARB Throughput Rate

| Attribute | Detail |
|-----------|--------|
| **Description** | Number of agenda items reviewed and dispositioned per ARB session, measured against the number of items submitted. |
| **Formula** | (Items dispositioned in session / Items submitted for session) x 100 |
| **Target (Green)** | >= 90% of submitted items dispositioned per session |
| **Caution (Amber)** | 70% -- 89% |
| **Critical (Red)** | < 70% |
| **Measurement Method** | ARB coordinator tracks items in the SharePoint ARB tracker. Each item is marked Approved, Conditionally Approved, Deferred, or Rejected at session close. |
| **Reporting Frequency** | Monthly (rolling average of 2 sessions) |
| **Owner** | EA Process Advisory Lead |

#### KPI-ARB-02: ARB Cycle Time

| Attribute | Detail |
|-----------|--------|
| **Description** | Elapsed business days from the date an architecture review request is submitted to the date a final disposition is communicated to the requestor. |
| **Formula** | Median calendar days (submission date to disposition date) |
| **Target (Green)** | <= 10 business days |
| **Caution (Amber)** | 11 -- 15 business days |
| **Critical (Red)** | > 15 business days |
| **Measurement Method** | Timestamps captured in ServiceNow RITM workflow for ARB requests. Report generated from ServiceNow Performance Analytics. |
| **Reporting Frequency** | Monthly |
| **Owner** | EA Process Advisory Lead |

#### KPI-ARB-03: ARB Decision Reversal Rate

| Attribute | Detail |
|-----------|--------|
| **Description** | Percentage of ARB decisions that are formally reversed or substantially modified within 90 days of the original ruling. A high reversal rate indicates poor initial analysis or unclear requirements. |
| **Formula** | (Decisions reversed or materially changed within 90 days / Total decisions in period) x 100 |
| **Target (Green)** | < 5% |
| **Caution (Amber)** | 5% -- 10% |
| **Critical (Red)** | > 10% |
| **Measurement Method** | ARB coordinator flags reversals in the ARB tracker. Quarterly review of all decisions older than 90 days. |
| **Reporting Frequency** | Quarterly |
| **Owner** | Director, Enterprise Architecture |

#### KPI-ARB-04: ARB Attendance Rate

| Attribute | Detail |
|-----------|--------|
| **Description** | Percentage of required voting members (or their designated alternates) present at each ARB session. Quorum is 60% of voting members. |
| **Formula** | (Voting members or alternates present / Total voting members) x 100 |
| **Target (Green)** | >= 80% attendance |
| **Caution (Amber)** | 60% -- 79% |
| **Critical (Red)** | < 60% (quorum not met; session should not proceed) |
| **Measurement Method** | Attendance recorded in ARB meeting minutes (SharePoint). |
| **Reporting Frequency** | Monthly |
| **Owner** | EA Process Advisory Lead |

---

### 2.2 New Application Request (NAR) Process

The NAR process governs the intake, evaluation, and disposition of all requests to introduce a new application or SaaS product into the Cenovus technology landscape. It is the primary gate preventing unmanaged application sprawl.

#### KPI-NAR-01: NAR Processing Time

| Attribute | Detail |
|-----------|--------|
| **Description** | Elapsed business days from NAR submission to final recommendation (Approve, Approve with Conditions, Redirect to Existing, or Deny). |
| **Formula** | Median business days (submission to final recommendation) |
| **Target (Green)** | <= 15 business days |
| **Caution (Amber)** | 16 -- 25 business days |
| **Critical (Red)** | > 25 business days |
| **Measurement Method** | ServiceNow RITM timestamps on the NAR catalog item. |
| **Reporting Frequency** | Monthly |
| **Owner** | EA Process Advisory Lead |

#### KPI-NAR-02: NAR Redirect-to-Existing Rate

| Attribute | Detail |
|-----------|--------|
| **Description** | Percentage of NARs where an existing application in the Cenovus portfolio was identified as a suitable alternative, avoiding introduction of a redundant tool. This is a direct measure of EA's value in preventing application sprawl. |
| **Formula** | (NARs redirected to existing application / Total NARs processed) x 100 |
| **Target (Green)** | >= 30% redirect rate (indicates effective portfolio governance) |
| **Caution (Amber)** | 15% -- 29% |
| **Critical (Red)** | < 15% (either redundant apps are being approved, or the portfolio catalog is incomplete) |
| **Measurement Method** | Disposition field on the NAR ServiceNow record. Cross-referenced with application portfolio in LeanIX/Ardoq. |
| **Reporting Frequency** | Quarterly |
| **Owner** | Application Portfolio Lead |

#### KPI-NAR-03: NAR Volume Trend

| Attribute | Detail |
|-----------|--------|
| **Description** | Total number of NARs received per quarter, tracked as a trend line. Used for workload planning and to detect shadow IT pressure. |
| **Formula** | Count of NARs submitted per quarter |
| **Target (Green)** | Trending stable or declining (indicates portfolio is maturing) |
| **Caution (Amber)** | > 20% increase quarter-over-quarter without a known driver (e.g., acquisition) |
| **Critical (Red)** | > 40% increase quarter-over-quarter unexplained |
| **Measurement Method** | ServiceNow reporting on NAR catalog item creation dates. |
| **Reporting Frequency** | Quarterly |
| **Owner** | EA Process Advisory Lead |

#### KPI-NAR-04: NAR Business Satisfaction Score

| Attribute | Detail |
|-----------|--------|
| **Description** | Average satisfaction rating provided by NAR requestors via a post-process survey. Measures whether the business perceives the NAR process as helpful rather than bureaucratic. |
| **Formula** | Average score on a 1--5 Likert scale |
| **Target (Green)** | >= 4.0 |
| **Caution (Amber)** | 3.0 -- 3.9 |
| **Critical (Red)** | < 3.0 |
| **Measurement Method** | Automated survey triggered by ServiceNow workflow upon NAR closure. Results aggregated in Power BI. |
| **Reporting Frequency** | Quarterly |
| **Owner** | EA Process Advisory Lead |

---

### 2.3 Conceptual and Solution Design Lifecycle

This covers the end-to-end lifecycle of architecture artifacts from Conceptual Design through Solution Design, including reviews, approvals, and handoff to delivery teams.

#### KPI-CSD-01: Design Artifact Completion Rate

| Attribute | Detail |
|-----------|--------|
| **Description** | Percentage of projects requiring an architecture design (as defined by the project classification matrix) that have a completed and approved Conceptual or Solution Design document before entering the Build phase. |
| **Formula** | (Projects with approved design artifact before Build / Projects requiring design artifact) x 100 |
| **Target (Green)** | >= 95% |
| **Caution (Amber)** | 80% -- 94% |
| **Critical (Red)** | < 80% |
| **Measurement Method** | Cross-reference Azure DevOps project phase gates with the architecture artifact repository in SharePoint. PMO confirms Build-phase entry dates. |
| **Reporting Frequency** | Monthly |
| **Owner** | Lead Solution Architect |

#### KPI-CSD-02: Design Review Turnaround

| Attribute | Detail |
|-----------|--------|
| **Description** | Elapsed business days from the date a Conceptual or Solution Design is submitted for peer review to the date review comments are returned to the author. |
| **Formula** | Median business days (submission to review completion) |
| **Target (Green)** | <= 5 business days |
| **Caution (Amber)** | 6 -- 10 business days |
| **Critical (Red)** | > 10 business days |
| **Measurement Method** | Tracked via the design review task in Azure DevOps or the SharePoint design workflow. |
| **Reporting Frequency** | Monthly |
| **Owner** | Lead Solution Architect |

#### KPI-CSD-03: Design Defect Escape Rate

| Attribute | Detail |
|-----------|--------|
| **Description** | Number of architecture-related defects or change requests identified during Build, Test, or Production phases that trace back to gaps in the approved Solution Design. |
| **Formula** | Count of architecture-attributed defects per quarter / Total projects with approved designs in quarter |
| **Target (Green)** | < 0.5 defects per project |
| **Caution (Amber)** | 0.5 -- 1.5 defects per project |
| **Critical (Red)** | > 1.5 defects per project |
| **Measurement Method** | Defects tagged with root cause "Architecture Gap" in Azure DevOps. Validated during project retrospectives. |
| **Reporting Frequency** | Quarterly |
| **Owner** | Director, Enterprise Architecture |

#### KPI-CSD-04: Design Reuse Rate

| Attribute | Detail |
|-----------|--------|
| **Description** | Percentage of new Solution Designs that leverage an existing reference architecture or approved design pattern from the EA pattern library. |
| **Formula** | (Designs referencing an existing pattern / Total new designs) x 100 |
| **Target (Green)** | >= 50% |
| **Caution (Amber)** | 30% -- 49% |
| **Critical (Red)** | < 30% |
| **Measurement Method** | Self-reported by Solution Architects on the design submission form (field: "Reference Architecture Used"). Validated during ARB review. |
| **Reporting Frequency** | Quarterly |
| **Owner** | Lead Solution Architect |

---

### 2.4 TCO / Financial Viability Analysis

These metrics track whether architecture decisions are grounded in sound financial analysis, including Total Cost of Ownership over the standard 5-year horizon used at Cenovus.

#### KPI-TCO-01: TCO Analysis Coverage

| Attribute | Detail |
|-----------|--------|
| **Description** | Percentage of projects exceeding the $250K capital threshold that have a completed TCO analysis before funding approval. |
| **Formula** | (Projects with completed TCO analysis / Projects exceeding threshold) x 100 |
| **Target (Green)** | 100% |
| **Caution (Amber)** | 90% -- 99% |
| **Critical (Red)** | < 90% |
| **Measurement Method** | TCO artifacts tracked in the EA SharePoint library. Funding approvals confirmed against IT Finance records and the project intake process. |
| **Reporting Frequency** | Quarterly |
| **Owner** | EA Process Advisory Lead |

#### KPI-TCO-02: TCO Forecast Accuracy

| Attribute | Detail |
|-----------|--------|
| **Description** | Variance between the 5-year TCO estimate produced at the design phase and the actual costs incurred after 12 months of operation. Measured only for projects that have been in production for at least 12 months. |
| **Formula** | ABS((Actual Year-1 cost - Estimated Year-1 cost) / Estimated Year-1 cost) x 100 |
| **Target (Green)** | <= 15% variance |
| **Caution (Amber)** | 16% -- 30% variance |
| **Critical (Red)** | > 30% variance |
| **Measurement Method** | IT Finance provides actuals from SAP. EA compares against the original TCO model stored in SharePoint. Annual reconciliation performed in Q4. |
| **Reporting Frequency** | Annually (with interim spot checks at Q2) |
| **Owner** | EA Process Advisory Lead, in partnership with IT Finance |

#### KPI-TCO-03: Cost Avoidance Attributed to EA

| Attribute | Detail |
|-----------|--------|
| **Description** | Annualized dollar value of costs avoided through EA interventions: NAR redirects, license consolidation recommendations, infrastructure optimization, and cloud right-sizing. This is the primary value metric for the EA team. |
| **Formula** | Sum of documented cost avoidance items (each item requires sign-off from the business sponsor or IT Finance) |
| **Target (Green)** | >= $2M annualized cost avoidance |
| **Caution (Amber)** | $1M -- $1.99M |
| **Critical (Red)** | < $1M |
| **Measurement Method** | Each cost avoidance claim is documented in a standardized template with business sponsor validation. Aggregated quarterly by the EA Process Advisory Lead. |
| **Reporting Frequency** | Quarterly (with annual roll-up for executive reporting) |
| **Owner** | Director, Enterprise Architecture |

---

### 2.5 EA Roadmap Management

EA Roadmaps are maintained per domain (Upstream, Downstream, Midstream, Corporate) and reviewed quarterly. These metrics assess whether roadmaps remain current, aligned, and actionable.

#### KPI-RM-01: Roadmap Currency

| Attribute | Detail |
|-----------|--------|
| **Description** | Percentage of domain roadmaps that have been reviewed and updated within the current quarter. A roadmap is "current" if it was reviewed at the quarterly domain architecture review and any changes were published. |
| **Formula** | (Domain roadmaps reviewed this quarter / Total domain roadmaps) x 100 |
| **Target (Green)** | 100% |
| **Caution (Amber)** | 75% -- 99% (at least 3 of 4 domains) |
| **Critical (Red)** | < 75% |
| **Measurement Method** | Quarterly review meetings are scheduled and tracked in Outlook. Updated roadmaps are version-controlled in SharePoint with a "Last Reviewed" date. |
| **Reporting Frequency** | Quarterly |
| **Owner** | Domain Architects |

#### KPI-RM-02: Roadmap-to-Project Alignment

| Attribute | Detail |
|-----------|--------|
| **Description** | Percentage of active IT projects (from the IT PMO portfolio) that can be traced to a specific initiative on an EA domain roadmap. Projects without roadmap alignment may represent unplanned work or shadow IT. |
| **Formula** | (Active projects with roadmap traceability / Total active IT projects) x 100 |
| **Target (Green)** | >= 80% |
| **Caution (Amber)** | 60% -- 79% |
| **Critical (Red)** | < 60% |
| **Measurement Method** | Quarterly cross-reference between the IT PMO project register (Azure DevOps / Project Online) and the EA roadmap items. Domain Architects validate linkages. |
| **Reporting Frequency** | Quarterly |
| **Owner** | Domain Architects, with IT PMO collaboration |

#### KPI-RM-03: Roadmap Initiative Delivery Rate

| Attribute | Detail |
|-----------|--------|
| **Description** | Percentage of roadmap initiatives scheduled for completion in the current fiscal year that are delivered on time (within one quarter of the target date). |
| **Formula** | (Initiatives delivered on time / Initiatives scheduled for completion this FY) x 100 |
| **Target (Green)** | >= 70% |
| **Caution (Amber)** | 50% -- 69% |
| **Critical (Red)** | < 50% |
| **Measurement Method** | Roadmap initiative status tracked in the EA roadmap tool (LeanIX/Ardoq or SharePoint). Domain Architects update status at quarterly reviews. |
| **Reporting Frequency** | Quarterly |
| **Owner** | Director, Enterprise Architecture |

---

### 2.6 Architecture Decision Records (ADR)

ADRs document significant architecture decisions, their context, options considered, and rationale. These metrics ensure ADRs are being consistently created and remain useful.

#### KPI-ADR-01: ADR Coverage Rate

| Attribute | Detail |
|-----------|--------|
| **Description** | Percentage of architecture decisions made at ARB or during Solution Design that have a corresponding ADR published in the ADR repository. |
| **Formula** | (ADRs published / Architecture decisions requiring documentation) x 100 |
| **Target (Green)** | >= 90% |
| **Caution (Amber)** | 70% -- 89% |
| **Critical (Red)** | < 70% |
| **Measurement Method** | ARB decisions and Solution Design decisions are tracked in the ARB tracker and Azure DevOps respectively. ADRs are stored in the Git-based ADR repository or SharePoint. Cross-reference performed monthly. |
| **Reporting Frequency** | Monthly |
| **Owner** | Lead Solution Architect |

#### KPI-ADR-02: ADR Freshness

| Attribute | Detail |
|-----------|--------|
| **Description** | Percentage of ADRs in "Accepted" status that have been reviewed within the past 12 months to confirm they remain valid and have not been superseded by technology or business changes. |
| **Formula** | (ADRs reviewed within past 12 months / Total ADRs in Accepted status) x 100 |
| **Target (Green)** | >= 80% |
| **Caution (Amber)** | 60% -- 79% |
| **Critical (Red)** | < 60% |
| **Measurement Method** | ADR metadata includes a "Last Reviewed" date. Automated report generated from the ADR repository. |
| **Reporting Frequency** | Quarterly |
| **Owner** | Domain Architects |

#### KPI-ADR-03: ADR Consultation Rate

| Attribute | Detail |
|-----------|--------|
| **Description** | Number of times ADRs are accessed or referenced by project teams (outside the EA team) per quarter. Indicates whether ADRs are actually being used to guide decisions or are shelf-ware. |
| **Formula** | Total unique pageviews or repository clones of ADR content by non-EA users per quarter |
| **Target (Green)** | >= 50 unique accesses per quarter |
| **Caution (Amber)** | 25 -- 49 |
| **Critical (Red)** | < 25 |
| **Measurement Method** | SharePoint analytics or Git repository access logs, filtered to exclude EA team members. |
| **Reporting Frequency** | Quarterly |
| **Owner** | EA Process Advisory Lead |

---

### 2.7 Standards Compliance

Architecture standards (technology standards, security patterns, integration patterns, cloud guardrails) are only effective if they are adopted. These metrics measure compliance and the health of the standards themselves.

#### KPI-SC-01: Standards Compliance Rate

| Attribute | Detail |
|-----------|--------|
| **Description** | Percentage of architecture reviews (ARB submissions and Solution Designs) that are fully compliant with applicable EA standards at first submission. |
| **Formula** | (Reviews compliant at first submission / Total reviews) x 100 |
| **Target (Green)** | >= 75% |
| **Caution (Amber)** | 50% -- 74% |
| **Critical (Red)** | < 50% |
| **Measurement Method** | ARB review checklist includes a "Standards Compliance" field (Compliant / Non-Compliant with exceptions noted). Data captured in the ARB tracker. |
| **Reporting Frequency** | Monthly |
| **Owner** | EA Process Advisory Lead |

#### KPI-SC-02: Exception Request Volume

| Attribute | Detail |
|-----------|--------|
| **Description** | Number of formal standards exception requests submitted per quarter. A moderate volume is healthy (it means teams are aware of standards); excessive volume suggests standards are unrealistic or outdated. |
| **Formula** | Count of exception requests per quarter |
| **Target (Green)** | 5 -- 15 per quarter (healthy awareness) |
| **Caution (Amber)** | 16 -- 25 per quarter |
| **Critical (Red)** | > 25 per quarter OR < 5 per quarter (either over-burdened or standards are being ignored) |
| **Measurement Method** | Exception requests tracked as a specific category in the ARB tracker or ServiceNow. |
| **Reporting Frequency** | Quarterly |
| **Owner** | Director, Enterprise Architecture |

#### KPI-SC-03: Standards Currency

| Attribute | Detail |
|-----------|--------|
| **Description** | Percentage of published EA standards that have been reviewed and reaffirmed or updated within the past 12 months. |
| **Formula** | (Standards reviewed within 12 months / Total published standards) x 100 |
| **Target (Green)** | >= 90% |
| **Caution (Amber)** | 70% -- 89% |
| **Critical (Red)** | < 70% |
| **Measurement Method** | Standards register maintained in SharePoint with "Last Reviewed" metadata. EA Process Advisory Lead audits quarterly. |
| **Reporting Frequency** | Quarterly |
| **Owner** | Domain Architects |

---

### 2.8 Application Rationalization

Application rationalization reduces portfolio complexity, lowers licensing and support costs, and improves the security posture. These metrics track progress on the rationalization program.

#### KPI-AR-01: Application Portfolio Size Trend

| Attribute | Detail |
|-----------|--------|
| **Description** | Total number of applications in the Cenovus IT portfolio, tracked as a trend. The goal is a controlled reduction or at minimum a stabilization, given the industry trend toward consolidation. |
| **Formula** | Count of active applications in LeanIX/Ardoq at quarter end |
| **Target (Green)** | Quarter-over-quarter reduction of >= 2% OR stable with documented justification for growth |
| **Caution (Amber)** | 0% -- 1.9% growth |
| **Critical (Red)** | > 2% growth without approved justification (e.g., acquisition) |
| **Measurement Method** | Application inventory in LeanIX/Ardoq. Reconciled quarterly against ServiceNow CMDB and software asset management records. |
| **Reporting Frequency** | Quarterly |
| **Owner** | Application Portfolio Lead |

#### KPI-AR-02: Rationalization Candidates Actioned

| Attribute | Detail |
|-----------|--------|
| **Description** | Percentage of applications identified as rationalization candidates (Retire, Replace, Consolidate) that have had action taken within the planned timeline. |
| **Formula** | (Candidates actioned on schedule / Total candidates identified) x 100 |
| **Target (Green)** | >= 60% |
| **Caution (Amber)** | 40% -- 59% |
| **Critical (Red)** | < 40% |
| **Measurement Method** | Rationalization backlog maintained in LeanIX/Ardoq with target action dates and status. Reviewed at quarterly domain architecture reviews. |
| **Reporting Frequency** | Quarterly |
| **Owner** | Application Portfolio Lead |

#### KPI-AR-03: Application Health Score Distribution

| Attribute | Detail |
|-----------|--------|
| **Description** | Distribution of applications across health categories: Invest, Maintain, Migrate, Retire (TIME model). The goal is to shift the portfolio toward a higher proportion in "Invest" and "Maintain" categories. |
| **Formula** | Percentage of applications in each TIME category |
| **Target (Green)** | >= 70% in Invest or Maintain |
| **Caution (Amber)** | 55% -- 69% in Invest or Maintain |
| **Critical (Red)** | < 55% in Invest or Maintain |
| **Measurement Method** | TIME classification assigned in LeanIX/Ardoq based on annual application health assessments. Inputs include business criticality, technical health, vendor viability, and security posture. |
| **Reporting Frequency** | Quarterly |
| **Owner** | Application Portfolio Lead |

#### KPI-AR-04: Licensing Cost per Application

| Attribute | Detail |
|-----------|--------|
| **Description** | Average annual licensing and subscription cost per active application. Tracked as a trend to measure whether rationalization is delivering cost efficiency. |
| **Formula** | Total annual licensing spend / Number of active applications |
| **Target (Green)** | Trending downward or stable year-over-year |
| **Caution (Amber)** | 1% -- 10% increase year-over-year |
| **Critical (Red)** | > 10% increase year-over-year |
| **Measurement Method** | Licensing spend data from IT Finance (SAP cost centers). Application count from LeanIX/Ardoq. Reconciled annually. |
| **Reporting Frequency** | Annually (with quarterly estimates) |
| **Owner** | Director, Enterprise Architecture, with IT Finance |

---

### 2.9 Stakeholder Engagement

EA is only effective if business and IT stakeholders trust and engage with the function. These metrics measure the health of that relationship.

#### KPI-SE-01: Stakeholder Satisfaction Score

| Attribute | Detail |
|-----------|--------|
| **Description** | Overall satisfaction of key stakeholders (IT leaders, business technology leads, project managers) with EA services, measured via an annual survey. |
| **Formula** | Average score on a 1--5 Likert scale across all survey respondents |
| **Target (Green)** | >= 4.0 |
| **Caution (Amber)** | 3.0 -- 3.9 |
| **Critical (Red)** | < 3.0 |
| **Measurement Method** | Annual EA stakeholder survey distributed via Microsoft Forms to approximately 40--60 stakeholders across IT and business. Survey covers responsiveness, clarity of guidance, value added, and ease of engagement. |
| **Reporting Frequency** | Annually (with pulse checks at Q2) |
| **Owner** | Director, Enterprise Architecture |

#### KPI-SE-02: Proactive Engagement Rate

| Attribute | Detail |
|-----------|--------|
| **Description** | Percentage of new IT initiatives where the EA team was engaged proactively (i.e., before project funding approval) versus reactively (after the project was already underway). |
| **Formula** | (Initiatives with proactive EA engagement / Total new IT initiatives) x 100 |
| **Target (Green)** | >= 70% |
| **Caution (Amber)** | 50% -- 69% |
| **Critical (Red)** | < 50% |
| **Measurement Method** | EA engagement date compared against project funding approval date in the PMO register. Data reconciled monthly by the EA Process Advisory Lead. |
| **Reporting Frequency** | Quarterly |
| **Owner** | EA Process Advisory Lead |

#### KPI-SE-03: Architecture Consultation Volume

| Attribute | Detail |
|-----------|--------|
| **Description** | Total number of architecture consultations (informal advice requests, design reviews, technology assessments) provided by the EA team per quarter. Indicates demand for EA services. |
| **Formula** | Count of consultations logged per quarter |
| **Target (Green)** | >= 30 per quarter |
| **Caution (Amber)** | 15 -- 29 |
| **Critical (Red)** | < 15 (may indicate EA team is not being sought out) |
| **Measurement Method** | EA team members log consultations in a shared tracking list (SharePoint or Teams tracker). Includes requestor, topic, domain, and time spent. |
| **Reporting Frequency** | Quarterly |
| **Owner** | EA Process Advisory Lead |

#### KPI-SE-04: Business-IT Alignment Score

| Attribute | Detail |
|-----------|--------|
| **Description** | Percentage of EA roadmap initiatives that have documented endorsement from a business sponsor (Director level or above). Measures whether architecture work is aligned with business priorities. |
| **Formula** | (Roadmap initiatives with business sponsor sign-off / Total roadmap initiatives) x 100 |
| **Target (Green)** | >= 80% |
| **Caution (Amber)** | 60% -- 79% |
| **Critical (Red)** | < 60% |
| **Measurement Method** | Business sponsor field populated on roadmap items in LeanIX/Ardoq. Validated at quarterly domain reviews. |
| **Reporting Frequency** | Quarterly |
| **Owner** | Domain Architects |

---

## 3. Executive Dashboard -- Senior Leadership Roll-Up

The following metrics are aggregated into a one-page executive dashboard presented to the VP, Information Technology and IT Senior Leadership Team on a quarterly basis. The dashboard is designed to answer four strategic questions.

### Dashboard Structure

#### Question 1: "Is EA Protecting the Enterprise?"

| Executive Metric | Source KPIs | Quarterly Target |
|-----------------|-------------|-----------------|
| **Cost Avoidance Delivered ($ value)** | KPI-TCO-03 | >= $500K per quarter |
| **Application Portfolio Trend** | KPI-AR-01 | Stable or declining |
| **Standards Compliance Rate** | KPI-SC-01 | >= 75% |

#### Question 2: "Is EA Enabling Speed of Delivery?"

| Executive Metric | Source KPIs | Quarterly Target |
|-----------------|-------------|-----------------|
| **ARB Cycle Time (median)** | KPI-ARB-02 | <= 10 business days |
| **NAR Processing Time (median)** | KPI-NAR-01 | <= 15 business days |
| **Design Review Turnaround (median)** | KPI-CSD-02 | <= 5 business days |

#### Question 3: "Is EA Aligned with Strategy?"

| Executive Metric | Source KPIs | Quarterly Target |
|-----------------|-------------|-----------------|
| **Roadmap Currency** | KPI-RM-01 | 100% |
| **Roadmap-to-Project Alignment** | KPI-RM-02 | >= 80% |
| **Business-IT Alignment Score** | KPI-SE-04 | >= 80% |

#### Question 4: "Is EA Trusted and Used?"

| Executive Metric | Source KPIs | Quarterly Target |
|-----------------|-------------|-----------------|
| **Stakeholder Satisfaction Score** | KPI-SE-01 | >= 4.0 / 5.0 |
| **Proactive Engagement Rate** | KPI-SE-02 | >= 70% |
| **NAR Business Satisfaction** | KPI-NAR-04 | >= 4.0 / 5.0 |

### Dashboard Format

- Delivered as a single Power BI page embedded in the quarterly IT governance deck.
- Each metric is displayed with a traffic-light indicator (green/amber/red), the current value, and a trend arrow (improving, stable, declining).
- Drill-down detail is available by clicking any metric, linking to the underlying process-level data.
- A quarterly commentary section (3--5 sentences) written by the Director, EA accompanies the dashboard to contextualize the numbers.

---

## 4. EA Maturity Scoring Model

The maturity model provides a holistic assessment of EA practice effectiveness at Cenovus. It is scored annually (with a baseline assessment at 2026-Q1 launch) and used to identify capability gaps and prioritize improvement efforts.

### Maturity Levels

| Level | Name | Description |
|-------|------|-------------|
| **1** | **Initial** | EA processes are ad hoc, inconsistent, and person-dependent. No standardized documentation or governance exists. |
| **2** | **Developing** | Core processes are defined and documented but adoption is inconsistent. Metrics collection has begun but is manual and incomplete. |
| **3** | **Defined** | Processes are standardized and consistently followed. Metrics are collected regularly and reported to leadership. Stakeholders are aware of EA services. |
| **4** | **Managed** | Processes are measured, monitored, and actively managed using KPIs. Data-driven decisions are made to improve EA operations. Stakeholder satisfaction is high. |
| **5** | **Optimizing** | EA is a strategic partner to the business. Processes are continuously improved based on feedback and benchmarking. EA proactively identifies opportunities and drives innovation. |

### Scoring Dimensions

Each dimension is scored 1--5 based on evidence gathered during the annual assessment.

| # | Dimension | Description | Weight |
|---|-----------|-------------|--------|
| 1 | **Governance Effectiveness** | ARB functioning, decision quality, stakeholder representation | 15% |
| 2 | **Process Maturity** | Standardization, documentation, and consistency of EA processes (NAR, Design, TCO) | 15% |
| 3 | **Portfolio Management** | Application inventory accuracy, rationalization progress, TIME model adoption | 15% |
| 4 | **Strategic Alignment** | Roadmap currency, business sponsor engagement, project alignment | 15% |
| 5 | **Standards and Compliance** | Standards coverage, compliance rates, exception management | 10% |
| 6 | **Financial Discipline** | TCO analysis coverage, forecast accuracy, cost avoidance tracking | 10% |
| 7 | **Knowledge Management** | ADR coverage, freshness, consultation rate, pattern library | 10% |
| 8 | **Stakeholder Value** | Satisfaction scores, proactive engagement, consultation volume | 10% |

### Composite Maturity Score

```
Composite Score = SUM(Dimension Score x Weight) across all 8 dimensions
```

| Composite Score | Overall Rating |
|----------------|---------------|
| 4.5 -- 5.0 | Optimizing |
| 3.5 -- 4.4 | Managed |
| 2.5 -- 3.4 | Defined |
| 1.5 -- 2.4 | Developing |
| 1.0 -- 1.4 | Initial |

### Assessment Process

1. **Self-Assessment:** Each Domain Architect and the Process Advisory Lead scores their respective dimensions with supporting evidence.
2. **Calibration Session:** The EA leadership team meets to review and calibrate scores, resolving disagreements.
3. **External Validation (optional):** Every two years, engage a third-party consultancy (e.g., Gartner, Info-Tech) to validate the self-assessment.
4. **Publication:** Scores and improvement priorities are published to the IT Senior Leadership Team.

---

## 5. Continuous Improvement Recommendations

### 5.1 Short-Term Improvements (2026-Q1 through Q2)

| # | Recommendation | Rationale | Effort |
|---|---------------|-----------|--------|
| 1 | **Automate ARB and NAR data collection via ServiceNow reporting.** Stop relying on manual SharePoint trackers for cycle time and throughput data. | Reduces data collection burden by approximately 4 hours per month and improves accuracy. | Medium -- requires ServiceNow reporting configuration (2--3 sprints with the ServiceNow team). |
| 2 | **Establish the ADR repository in Azure DevOps Git** with a lightweight template and mandatory metadata fields. | ADRs currently exist in scattered SharePoint files and email threads. A single source of truth is prerequisite for KPI-ADR-01 through KPI-ADR-03. | Low -- template creation and repository setup (1 sprint). |
| 3 | **Launch the post-NAR satisfaction survey** via ServiceNow workflow automation. | KPI-NAR-04 cannot be measured without this survey. Quick win for demonstrating stakeholder-centric thinking. | Low -- survey design and ServiceNow workflow trigger (1 week). |
| 4 | **Conduct the baseline maturity assessment** using the scoring model in Section 4. | Establishes the starting point from which all improvement is measured. Without a baseline, progress cannot be demonstrated. | Low -- 2-day facilitated workshop with the EA team. |

### 5.2 Medium-Term Improvements (2026-Q3 through Q4)

| # | Recommendation | Rationale | Effort |
|---|---------------|-----------|--------|
| 5 | **Integrate LeanIX/Ardoq with ServiceNow CMDB** for real-time application portfolio synchronization. | Eliminates manual reconciliation effort (approximately 20 hours per quarter) and improves KPI-AR-01 accuracy. | High -- integration project (1--2 quarters with vendor support). |
| 6 | **Build the Power BI executive dashboard** with live data connections to ServiceNow, LeanIX/Ardoq, and SharePoint. | Manual dashboard creation consumes approximately 8 hours per quarter and introduces delays. Automation enables real-time visibility. | Medium -- Power BI development (2--3 sprints with the BI team). |
| 7 | **Establish a cost avoidance tracking template and review process** co-owned with IT Finance. | KPI-TCO-03 is the single most important metric for demonstrating EA value. Without a rigorous, finance-endorsed methodology, the numbers will not be credible. | Medium -- process design and IT Finance engagement (1 quarter). |
| 8 | **Conduct the first annual EA stakeholder survey.** | Establishes the baseline for KPI-SE-01. Survey results will directly inform 2027 EA priorities. | Low -- survey design and distribution (2 weeks). |

### 5.3 Long-Term Improvements (2027 and Beyond)

| # | Recommendation | Rationale | Effort |
|---|---------------|-----------|--------|
| 9 | **Benchmark EA metrics against industry peers** via Gartner or Info-Tech research. | Internal targets are estimates until validated against external benchmarks. Benchmarking provides credibility and identifies blind spots. | Medium -- research engagement (annual subscription). |
| 10 | **Introduce predictive analytics** for application lifecycle management (e.g., predicting when applications will transition from "Maintain" to "Migrate" based on vendor roadmaps and technical debt indicators). | Moves EA from reactive to proactive posture. | High -- data science engagement and tooling. |
| 11 | **Extend EA metrics to include sustainability and ESG considerations** (e.g., data center energy efficiency per application, cloud carbon footprint). | Cenovus has public ESG commitments. Connecting EA decisions to sustainability outcomes strengthens the EA value proposition and aligns with corporate strategy. | Medium -- new metric design and data source identification. |

---

## 6. 2026-Q1 Baseline Targets

The following table defines the initial targets for each KPI at program launch. These are intentionally set at the lower end of the "Green" threshold or within the "Amber" range to reflect that the metrics program itself is new. Targets will be recalibrated at the end of Q2 based on actual data.

| KPI ID | KPI Name | Q1 Baseline Target | Notes |
|--------|----------|-------------------|-------|
| KPI-ARB-01 | ARB Throughput Rate | >= 80% | Lower than steady-state target of 90% while process stabilizes. |
| KPI-ARB-02 | ARB Cycle Time | <= 12 business days | Slightly relaxed from 10-day target. |
| KPI-ARB-03 | ARB Decision Reversal Rate | < 10% | Steady-state target is < 5%; Q1 allows calibration. |
| KPI-ARB-04 | ARB Attendance Rate | >= 70% | Building quorum discipline takes time. |
| KPI-NAR-01 | NAR Processing Time | <= 20 business days | Process is still being refined; 15-day target is aspirational for Q1. |
| KPI-NAR-02 | NAR Redirect-to-Existing Rate | >= 20% | Portfolio catalog may be incomplete in Q1. |
| KPI-NAR-03 | NAR Volume Trend | Baseline quarter -- no target | First quarter establishes the baseline count. |
| KPI-NAR-04 | NAR Business Satisfaction | >= 3.5 | Survey launching in Q1; allow adjustment period. |
| KPI-CSD-01 | Design Artifact Completion | >= 85% | Legacy projects may lack retroactive artifacts. |
| KPI-CSD-02 | Design Review Turnaround | <= 7 business days | Slightly relaxed from 5-day steady-state target. |
| KPI-CSD-03 | Design Defect Escape Rate | < 1.5 per project | Baseline measurement; data may be incomplete. |
| KPI-CSD-04 | Design Reuse Rate | >= 30% | Pattern library is still being built out. |
| KPI-TCO-01 | TCO Analysis Coverage | >= 90% | Target remains high; this is a gating requirement. |
| KPI-TCO-02 | TCO Forecast Accuracy | Not measurable in Q1 | Requires 12 months of production data. |
| KPI-TCO-03 | Cost Avoidance Attributed to EA | >= $250K (Q1 only) | Pro-rated quarterly target. Annual target is $2M. |
| KPI-RM-01 | Roadmap Currency | 100% | Q1 coincides with annual roadmap refresh. |
| KPI-RM-02 | Roadmap-to-Project Alignment | >= 60% | Initial mapping will have gaps. |
| KPI-RM-03 | Roadmap Initiative Delivery Rate | Not measurable in Q1 | Requires full fiscal year of data. |
| KPI-ADR-01 | ADR Coverage Rate | >= 70% | ADR repository is being established in Q1. |
| KPI-ADR-02 | ADR Freshness | >= 50% | Many legacy decisions have never been documented as ADRs. |
| KPI-ADR-03 | ADR Consultation Rate | >= 20 accesses | Awareness building is in progress. |
| KPI-SC-01 | Standards Compliance Rate | >= 60% | Teams are still learning the standards. |
| KPI-SC-02 | Exception Request Volume | 3 -- 15 | Lower bound relaxed to 3 as awareness grows. |
| KPI-SC-03 | Standards Currency | >= 70% | Standards review cycle is being initialized. |
| KPI-AR-01 | Application Portfolio Size Trend | Baseline quarter -- no target | Establishes the starting count. |
| KPI-AR-02 | Rationalization Candidates Actioned | >= 40% | Rationalization program is ramping up. |
| KPI-AR-03 | Application Health Score Distribution | >= 55% Invest/Maintain | Initial TIME assessments may be incomplete. |
| KPI-AR-04 | Licensing Cost per Application | Baseline year -- no target | Establishes the starting cost-per-app figure. |
| KPI-SE-01 | Stakeholder Satisfaction Score | Not measurable in Q1 | Annual survey launches in Q2 or Q3. |
| KPI-SE-02 | Proactive Engagement Rate | >= 50% | EA intake process is still being socialized. |
| KPI-SE-03 | Architecture Consultation Volume | >= 15 | Tracking mechanism is new; volume will grow with awareness. |
| KPI-SE-04 | Business-IT Alignment Score | >= 60% | Business sponsor engagement is being formalized. |

---

## 7. Appendix -- Data Collection Sources and Tooling

### Primary Data Sources

| Source System | Data Provided | EA Metrics Supported |
|--------------|---------------|---------------------|
| **ServiceNow** | ARB request workflow, NAR catalog items, exception requests, cycle time timestamps | KPI-ARB-01, ARB-02, NAR-01, NAR-03, NAR-04, SC-02 |
| **LeanIX / Ardoq** | Application portfolio inventory, TIME classifications, roadmap items, business sponsor linkages | KPI-AR-01 through AR-04, RM-01 through RM-03, SE-04 |
| **SharePoint** | ARB meeting minutes, design artifacts, TCO analysis documents, standards register, ADR repository (interim) | KPI-ARB-03, ARB-04, CSD-01, TCO-01, ADR-01, ADR-02, SC-03 |
| **Azure DevOps** | Project phase gates, defect tracking, ADR Git repository (target state) | KPI-CSD-01, CSD-02, CSD-03, CSD-04, ADR-01 through ADR-03 |
| **SAP** | IT cost center actuals, licensing spend | KPI-TCO-02, TCO-03, AR-04 |
| **Power BI** | Dashboard aggregation and visualization | All executive dashboard metrics |
| **Microsoft Forms** | Stakeholder satisfaction survey, NAR satisfaction survey | KPI-SE-01, NAR-04 |

### Data Collection Calendar

| Activity | Frequency | Responsible | Timing |
|---------|-----------|-------------|--------|
| ARB metrics extraction from ServiceNow | Monthly | EA Process Advisory Lead | 1st week of month |
| NAR metrics extraction from ServiceNow | Monthly | EA Process Advisory Lead | 1st week of month |
| Design artifact compliance check | Monthly | Lead Solution Architect | 2nd week of month |
| ADR repository audit | Quarterly | Domain Architects | Last week of quarter |
| Application portfolio reconciliation | Quarterly | Application Portfolio Lead | 2nd month of quarter |
| Roadmap review and alignment check | Quarterly | Domain Architects | Quarterly domain review meetings |
| TCO forecast accuracy reconciliation | Annually | EA Process Advisory Lead + IT Finance | Q4 |
| Stakeholder satisfaction survey | Annually | Director, EA | Q2 or Q3 |
| Maturity model assessment | Annually | EA Leadership Team | Q4 |
| Executive dashboard publication | Quarterly | EA Process Advisory Lead | 3rd week after quarter end |

---

**Document History**

| Version | Date | Author | Change Description |
|---------|------|--------|-------------------|
| 0.1 | 2026-02-08 | Process Advisory Lead | Initial draft -- all KPIs, maturity model, baseline targets |
| | | | |

**Next Review Date:** 2026-04-15 (end of Q1 baseline period)
