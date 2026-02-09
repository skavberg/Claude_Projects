# Cenovus Energy - IT Architecture Team Goals 2026

**Document Owner:** IT Architecture Team Leader (Chief Architect)
**Effective Date:** January 2026
**Review Cycle:** Quarterly
**Status:** DRAFT

---

## 1. Strategic Objectives

The following objectives align the IT Architecture team with Cenovus Energy's corporate strategy, industry imperatives, and IT Senior Leadership direction for 2026.

### Objective 1: Accelerate Cloud Modernization and Hybrid Infrastructure Optimization

**Rationale:** Cenovus operates a complex hybrid estate spanning on-premises data centres, SCADA/OT networks, and cloud platforms (AWS & Azure). Rationalizing workloads across these environments reduces operating cost, improves resilience, and enables faster time-to-value for digital initiatives.

**Key Results:**
- KR1.1: Complete current-state assessment of all Tier-1 and Tier-2 applications and publish migration/modernization disposition for each (Retain, Rehost, Refactor, Replace, Retire) by end of Q2.
- KR1.2: Publish updated IT Infrastructure and Cloud domain roadmaps with aligned transition architectures by end of Q1.
- KR1.3: Reduce infrastructure technical debt backlog by 20% (measured by ARB-tracked items) by end of Q4.
- KR1.4: Establish FinOps governance model and reporting cadence for AWS and Azure spend, achieving 15% improvement in cloud cost efficiency by end of Q4.

**Primary Owners:** PA-Infrastructure, PA-Cloud

---

### Objective 2: Strengthen Cyber Security Posture Across IT and OT Environments

**Rationale:** As an integrated oil and gas operator, Cenovus faces significant cyber risk across both corporate IT and operational technology (SCADA, DCS, field devices). Regulatory expectations (CSA, NERC CIP alignment), insurance requirements, and threat landscape evolution demand a mature, Zero Trust-aligned security architecture.

**Key Results:**
- KR2.1: Publish the Cyber Security domain roadmap including Zero Trust maturity model and OT security reference architecture by end of Q1.
- KR2.2: Complete threat modelling for top 10 critical business applications and publish risk mitigation architectures by end of Q2.
- KR2.3: Establish Identity & Access Management (IAM) target architecture supporting converged IT/OT identities by end of Q3.
- KR2.4: Achieve Architecture Review Board (ARB) gate compliance for security review on 100% of new application requests throughout 2026.

**Primary Owner:** PA-Cyber Security

---

### Objective 3: Establish AI/ML Governance and Enable Responsible Adoption

**Rationale:** AI and GenAI present significant opportunities for Cenovus in areas such as predictive maintenance, reservoir modelling, production optimization, and corporate productivity. A governed approach ensures value realization while managing risk around data privacy, model reliability, and regulatory compliance.

**Key Results:**
- KR3.1: Publish the AI domain roadmap and GenAI governance framework (acceptable use, model risk, data classification) by end of Q1.
- KR3.2: Define and publish AI/ML platform reference architecture (covering data pipelines, model training, inference, monitoring) by end of Q2.
- KR3.3: Identify and support 3-5 high-value AI use cases across upstream, downstream, and corporate domains with conceptual designs by end of Q3.
- KR3.4: Establish AI Centre of Excellence operating model with architecture guardrails by end of Q4.

**Primary Owner:** PA-Artificial Intelligence

---

### Objective 4: Rationalize the Application Portfolio and Strengthen Capability Mapping

**Rationale:** Cenovus's application estate spans upstream (drilling, production, reservoir), downstream (refining, upgrading, trading), corporate (ERP, HR, Finance), and enterprise (integration, MDM, reporting) domains. A clear application-to-capability map drives rationalization, reduces redundancy, and informs investment decisions.

**Key Results:**
- KR4.1: Complete application-to-functional-capability and application-to-business-capability mapping for all Tier-1 and Tier-2 applications by end of Q2.
- KR4.2: Publish domain roadmaps for Corporate, Upstream, Downstream, and Enterprise Applications portfolios by end of Q2.
- KR4.3: Identify and present rationalization opportunities (consolidation, retirement, replacement) yielding at least 10% reduction in redundant application count by end of Q3.
- KR4.4: Complete TCO and Financial Viability assessments for top 5 rationalization candidates by end of Q4.

**Primary Owners:** PA-Corporate Apps, PA-Upstream Apps, PA-Downstream Apps, PA-Enterprise Apps

---

### Objective 5: Mature EA Governance, Standards, and Team Operating Model

**Rationale:** The Architecture team must operate with consistent processes, clear governance gates, standardized templates, and transparent decision-making. This builds trust with stakeholders and ensures architectural coherence across all domains.

**Key Results:**
- KR5.1: Publish and operationalize the EA Governance Process (ARB cadence, review gates, escalation paths) by end of Q1.
- KR5.2: Complete and publish all standard templates (Conceptual Design, Solution Design, TCO, ADR, New App Request, EA Roadmap) by end of Q1.
- KR5.3: Conduct quarterly Architecture Review Board sessions with documented decisions and ADRs throughout 2026.
- KR5.4: Establish EA metrics dashboard tracking portfolio health, technical debt, standards compliance, and ARB throughput by end of Q2.
- KR5.5: Achieve 90% stakeholder satisfaction score in mid-year and year-end surveys on EA engagement quality.

**Primary Owners:** Team Leader, Documentation Specialist, Process Advisor

---

## 2. Domain-Specific Goals

### 2.1 IT Infrastructure (PA-Infrastructure)

| # | Goal | Target Date |
|---|------|-------------|
| I-1 | Publish current-state Infrastructure architecture (data centres, networking, compute, storage, EUC, SCADA/OT convergence) | Q1 |
| I-2 | Define future-state reference architecture for hybrid infrastructure | Q2 |
| I-3 | Assess and document SCADA/OT network convergence architecture and risk posture | Q2 |
| I-4 | Develop data centre consolidation/optimization roadmap | Q3 |
| I-5 | Publish end-user computing modernization strategy | Q3 |
| I-6 | Reduce infrastructure-related ARB technical debt items by 20% | Q4 |

### 2.2 IT Cloud - AWS & Azure (PA-Cloud)

| # | Goal | Target Date |
|---|------|-------------|
| C-1 | Publish Cloud domain roadmap covering AWS and Azure platform strategies | Q1 |
| C-2 | Define cloud-native reference architectures (landing zones, guardrails, networking) for both AWS and Azure | Q1 |
| C-3 | Establish FinOps operating model with cost allocation, tagging standards, and reporting | Q2 |
| C-4 | Complete cloud readiness assessment for Tier-1/Tier-2 workloads and publish migration dispositions | Q2 |
| C-5 | Define hybrid cloud integration patterns (on-prem to cloud connectivity, data residency) | Q3 |
| C-6 | Achieve 15% cloud cost efficiency improvement through right-sizing and reserved capacity planning | Q4 |

### 2.3 IT Cyber Security (PA-Cyber Security)

| # | Goal | Target Date |
|---|------|-------------|
| S-1 | Publish Cyber Security domain roadmap with Zero Trust maturity model | Q1 |
| S-2 | Develop OT Security reference architecture for SCADA/DCS environments | Q1 |
| S-3 | Complete threat modelling for top 10 critical applications | Q2 |
| S-4 | Publish IAM target architecture (IT/OT identity convergence) | Q3 |
| S-5 | Define security architecture patterns for cloud workloads (AWS & Azure) | Q3 |
| S-6 | Enforce 100% ARB security gate compliance for new application requests | Ongoing |

### 2.4 IT Artificial Intelligence (PA-AI)

| # | Goal | Target Date |
|---|------|-------------|
| A-1 | Publish AI domain roadmap and GenAI governance framework | Q1 |
| A-2 | Define AI/ML platform reference architecture (data pipelines, training, inference, monitoring) | Q2 |
| A-3 | Identify and develop conceptual designs for 3-5 high-value AI use cases | Q3 |
| A-4 | Establish AI Centre of Excellence operating model with architecture guardrails | Q4 |
| A-5 | Define data classification and model risk management standards for AI/GenAI | Q2 |

### 2.5 Corporate Applications (PA-Corporate Apps)

| # | Goal | Target Date |
|---|------|-------------|
| CA-1 | Publish Corporate Applications domain roadmap (SAP/ERP, HR, Finance, Supply Chain) | Q2 |
| CA-2 | Complete application-to-capability mapping for all corporate applications | Q2 |
| CA-3 | Assess SAP landscape and define S/4HANA readiness or alternative strategy | Q3 |
| CA-4 | Identify rationalization opportunities in corporate tools (collaboration, productivity) | Q3 |
| CA-5 | Complete TCO analysis for top corporate application rationalization candidates | Q4 |

### 2.6 Upstream Applications (PA-Upstream Apps)

| # | Goal | Target Date |
|---|------|-------------|
| U-1 | Publish Upstream Applications domain roadmap (drilling, completions, production, reservoir) | Q2 |
| U-2 | Complete application-to-capability mapping for upstream domain | Q2 |
| U-3 | Assess field data capture architecture and edge computing opportunities | Q3 |
| U-4 | Define integration architecture between upstream apps and enterprise platforms | Q3 |
| U-5 | Identify AI/ML opportunities in production optimization and reservoir modelling | Q3 |

### 2.7 Downstream Applications (PA-Downstream Apps)

| # | Goal | Target Date |
|---|------|-------------|
| D-1 | Publish Downstream Applications domain roadmap (refining, upgrading, pipeline, trading) | Q2 |
| D-2 | Complete application-to-capability mapping for downstream domain | Q2 |
| D-3 | Assess process control and manufacturing execution system (MES) architecture | Q3 |
| D-4 | Define integration architecture between downstream apps and enterprise platforms | Q3 |
| D-5 | Evaluate digital twin opportunities for refining and upgrading operations | Q4 |

### 2.8 Enterprise Applications (PA-Enterprise Apps)

| # | Goal | Target Date |
|---|------|-------------|
| E-1 | Publish Enterprise Applications domain roadmap (integration, MDM, reporting, GIS) | Q2 |
| E-2 | Define enterprise integration platform strategy (API management, iPaaS, ETL) | Q2 |
| E-3 | Develop master data management (MDM) target architecture | Q3 |
| E-4 | Assess enterprise reporting and analytics platform architecture | Q3 |
| E-5 | Define GIS platform strategy aligned with upstream and downstream spatial data needs | Q4 |

---

## 3. Cross-Domain Collaboration Initiatives

These initiatives require coordinated effort across multiple Portfolio Architect domains:

### Initiative A: IT/OT Convergence Architecture
**Domains:** Infrastructure, Cyber Security, Upstream Apps, Downstream Apps
**Objective:** Develop a unified architecture framework for safe, secure convergence of IT and OT networks, addressing SCADA, DCS, and field device integration while maintaining security boundaries.
**Deliverables:**
- IT/OT convergence reference architecture
- Security zone model (Purdue model alignment)
- Shared monitoring and alerting architecture
**Target:** Q3 2026

### Initiative B: Cloud-First Application Modernization Program
**Domains:** Cloud, Infrastructure, Corporate Apps, Enterprise Apps
**Objective:** Define the cloud migration and modernization strategy for corporate and enterprise applications, including landing zone design, data residency controls, and hybrid connectivity.
**Deliverables:**
- Application migration wave plan
- Cloud landing zone architecture (AWS + Azure)
- Hybrid connectivity reference architecture
**Target:** Q2-Q3 2026

### Initiative C: AI-Enabled Operations
**Domains:** AI, Upstream Apps, Downstream Apps, Enterprise Apps
**Objective:** Identify and architect AI/ML solutions for operational improvement across upstream production, downstream refining, and enterprise analytics.
**Deliverables:**
- AI use case catalogue (prioritized)
- Data pipeline architecture for operational AI
- Conceptual designs for top 3 use cases
**Target:** Q3 2026

### Initiative D: Enterprise Integration Modernization
**Domains:** Enterprise Apps, Cloud, Corporate Apps, Upstream Apps, Downstream Apps
**Objective:** Modernize the enterprise integration layer to support API-first, event-driven patterns and reduce point-to-point integration sprawl.
**Deliverables:**
- Integration platform target architecture
- API management standards and governance
- Integration pattern catalogue
**Target:** Q2-Q4 2026

### Initiative E: Unified Security and Identity Architecture
**Domains:** Cyber Security, Cloud, Infrastructure, All Application Domains
**Objective:** Establish a unified identity and access management architecture that spans cloud, on-premises, and OT environments under a Zero Trust model.
**Deliverables:**
- Zero Trust architecture blueprint
- Unified IAM target architecture
- Privileged access management model for IT and OT
**Target:** Q3 2026

---

## 4. Quarterly Milestones

### Q1 2026 (January - March)

| Milestone | Owner | Status |
|-----------|-------|--------|
| Publish EA Team Goals 2026 | Team Leader | In Progress |
| Operationalize EA Governance Process (ARB cadence, gates) | Process Advisor | Pending |
| Publish all standard templates | Documentation Specialist | In Progress |
| Publish Infrastructure domain roadmap | PA-Infrastructure | Complete |
| Publish Cloud domain roadmap (AWS & Azure) | PA-Cloud | Complete |
| Publish Cyber Security domain roadmap (incl. OT security) | PA-Cyber Security | Pending |
| Publish AI domain roadmap and GenAI governance framework | PA-AI | Pending |
| Conduct Q1 Architecture Review Board | Team Leader | Pending |

### Q2 2026 (April - June)

| Milestone | Owner | Status |
|-----------|-------|--------|
| Complete Tier-1/Tier-2 application portfolio assessment | All PAs | Pending |
| Publish Corporate, Upstream, Downstream, Enterprise roadmaps | PAs (Apps) | Pending |
| Complete application-to-capability mapping (all domains) | All PAs | Pending |
| Establish FinOps governance model | PA-Cloud | Pending |
| Publish AI/ML platform reference architecture | PA-AI | Pending |
| Establish EA metrics dashboard | Team Leader | Pending |
| Complete threat modelling for top 10 critical apps | PA-Cyber Security | Pending |
| Deliver cloud readiness assessment | PA-Cloud, PA-Infrastructure | Pending |
| Conduct Q2 Architecture Review Board | Team Leader | Pending |

### Q3 2026 (July - September)

| Milestone | Owner | Status |
|-----------|-------|--------|
| Deliver IT/OT convergence reference architecture | Cross-domain | Pending |
| Publish IAM target architecture (IT/OT) | PA-Cyber Security | Pending |
| Identify and present application rationalization opportunities | All PAs (Apps) | Pending |
| Deliver AI use case conceptual designs (3-5 cases) | PA-AI + Apps PAs | Pending |
| Publish integration platform target architecture | PA-Enterprise Apps | Pending |
| Deliver Zero Trust architecture blueprint | PA-Cyber Security | Pending |
| Conduct mid-year stakeholder satisfaction survey | Team Leader | Pending |
| Conduct Q3 Architecture Review Board | Team Leader | Pending |

### Q4 2026 (October - December)

| Milestone | Owner | Status |
|-----------|-------|--------|
| Complete TCO/Financial Viability for top 5 rationalization candidates | All PAs (Apps) | Pending |
| Achieve 20% infrastructure technical debt reduction | PA-Infrastructure | Pending |
| Achieve 15% cloud cost efficiency improvement | PA-Cloud | Pending |
| Establish AI Centre of Excellence operating model | PA-AI | Pending |
| Conduct year-end stakeholder satisfaction survey | Team Leader | Pending |
| Publish annual Architecture Health Report | Team Leader | Pending |
| Conduct Q4 Architecture Review Board | Team Leader | Pending |

---

## 5. Success Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Domain roadmaps published | 8/8 by Q2 | Roadmap documents in team_public/Roadmaps/ |
| Application capability mapping coverage | 100% Tier-1, 80% Tier-2 by Q2 | Portfolio register |
| ARB sessions conducted | 4 (quarterly) | Meeting minutes |
| ARB security gate compliance | 100% | ARB decision records |
| New application requests reviewed | 100% through ARB | ARB log |
| Technical debt backlog reduction | 20% by Q4 | ARB tracking |
| Cloud cost efficiency improvement | 15% by Q4 | FinOps reporting |
| Stakeholder satisfaction | 90% | Survey results |
| Standard templates published | All 6 templates by Q1 | team_public/Standards/ |
| Architecture Decision Records published | Minimum 12 by Q4 | team_public/Decision_Records/ |

---

## 6. Dependencies and Risks

| Risk | Impact | Mitigation |
|------|--------|------------|
| Business stakeholder availability for roadmap input | Delayed roadmaps | Early scheduling, async input via structured questionnaires |
| Competing priorities from IT delivery teams | Reduced ARB compliance | IT Senior Leadership sponsorship, mandatory gate enforcement |
| Rapidly evolving AI/GenAI landscape | Governance framework obsolescence | Quarterly GenAI governance reviews, industry benchmarking |
| OT environment access constraints | Incomplete IT/OT convergence design | Partner with Operations Technology team, joint workshops |
| SAP S/4HANA migration uncertainty | Corporate Apps roadmap gaps | Scenario-based planning (migrate vs. alternative ERP) |
| Cloud cost overruns | FinOps targets missed | Monthly cost reviews, automated alerting, rightsizing sprints |

---

## Approvals

| Role | Name | Date | Signature |
|------|------|------|-----------|
| Chief Architect (Team Leader) | | | |
| IT Senior Leadership Sponsor | | | |

---

*This document is maintained by the IT Architecture Team Leader and reviewed quarterly. Updates are tracked in the team_goals folder.*
