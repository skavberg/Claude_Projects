# Solution Design Review Checklist

**Procedure ID:** PROC-EA-003
**Owner:** IT Architecture Team Leader
**Version:** 1.0
**Effective:** 2026-02-08
**Related Procedure:** PROC-EA-001 (Architecture Review Board Procedure)

---

## Purpose

This checklist is used by Portfolio Architects when performing pre-review of solution designs prior to ARB presentation. It ensures that all critical dimensions of a proposed solution are evaluated consistently and that the ARB receives a well-assessed submission. The reviewing Portfolio Architect must complete all applicable sections below and attach this checklist to the ARB submission package.

---

## Review Information

| Field | Value |
|---|---|
| **Solution / Project Name** | |
| **Requestor** | |
| **Reviewing Portfolio Architect** | |
| **Review Date** | |
| **Target ARB Date** | |
| **Domain** | |
| **Review Iteration** | First / Resubmission |

---

## 1. Strategic Alignment

| # | Check | Status |
|---|---|---|

- [ ] **1.1 Domain Roadmap Alignment** -- The proposed solution aligns with the published roadmap for the relevant technology domain. Any deviations are documented and justified.
- [ ] **1.2 Corporate Strategy Alignment** -- The solution supports one or more stated corporate strategic objectives (e.g., operational excellence, cost discipline, safe and reliable operations, energy transition readiness).
- [ ] **1.3 EA Guiding Principles** -- The design adheres to the Enterprise Architecture guiding principles (e.g., buy before build, cloud-first, reuse over redundancy, simplification, data as an asset). Any exceptions are explicitly called out with rationale.
- [ ] **1.4 Business Capability Mapping** -- The solution has been mapped to the relevant business capabilities and does not introduce unnecessary capability overlap.
- [ ] **1.5 Stakeholder Endorsement** -- Business sponsor and relevant domain stakeholders have endorsed the strategic intent of the solution.

**Portfolio Architect Notes (Strategic Alignment):**

> _Enter observations, concerns, or conditions here._

---

## 2. Architecture Compliance

### Technology Standards

- [ ] **2.1 Technology Standards Adherence** -- All proposed technologies (platforms, languages, frameworks, databases, middleware) are on the approved technology standards list or have a documented exception request.
- [ ] **2.2 Version Currency** -- Proposed technology versions are current and supported. No end-of-life or end-of-support components are introduced without a documented remediation timeline.
- [ ] **2.3 Vendor Strategic Alignment** -- Technology choices align with strategic vendor relationships (e.g., Microsoft/Azure, SAP, ServiceNow, OSIsoft/AVEVA).

### Integration Architecture

- [ ] **2.4 API-First Design** -- The solution exposes and consumes functionality through well-defined APIs where applicable. API standards (REST, versioning, OpenAPI specification) are followed.
- [ ] **2.5 Event-Driven Patterns** -- Where asynchronous processing is appropriate, event-driven patterns are employed using approved platforms (e.g., Azure Event Grid, Service Bus, Kafka).
- [ ] **2.6 Integration Platform Usage** -- Integrations are routed through the enterprise integration platform rather than point-to-point connections. Any direct integrations are justified and documented.
- [ ] **2.7 OT/IT Integration** -- If the solution involves Operational Technology data, the integration approach respects the OT/IT boundary, uses approved data historians and gateway patterns, and does not introduce uncontrolled connectivity into OT networks.

### Data Architecture

- [ ] **2.8 Master Data Alignment** -- The solution consumes and respects authoritative sources for master data entities (e.g., well master, equipment hierarchy, cost centre, vendor master from SAP). No new master data stores are introduced without Data Governance approval.
- [ ] **2.9 Data Ownership and Stewardship** -- Data ownership, classification, and stewardship responsibilities are defined for any new data entities created by the solution.
- [ ] **2.10 Data Lineage and Quality** -- Data lineage from source to consumption is documented. Data quality requirements and validation rules are specified.
- [ ] **2.11 Analytics and Reporting** -- If the solution produces data for analytics, it integrates with the enterprise data platform (e.g., Azure Synapse / Databricks lakehouse) rather than creating isolated data silos.

### Security Architecture

- [ ] **2.12 Zero Trust Principles** -- The solution follows Zero Trust principles: verify explicitly, use least-privilege access, and assume breach. Network segmentation and micro-segmentation are applied where appropriate.
- [ ] **2.13 Identity and Access Management** -- Authentication and authorization leverage the corporate IAM platform (Azure AD / Entra ID). Role-based access control (RBAC) is defined. No local accounts or shared credentials are introduced.
- [ ] **2.14 Encryption** -- Data is encrypted at rest and in transit using approved encryption standards. Key management follows corporate policy (e.g., Azure Key Vault, HSM where required).
- [ ] **2.15 Security Review Engagement** -- The Information Security team has been engaged or is scheduled for a security assessment of the solution.

### Cloud Architecture

- [ ] **2.16 Landing Zone Compliance** -- The solution deploys into the approved Azure landing zone structure with correct subscription, resource group, and tagging conventions.
- [ ] **2.17 FinOps Practices** -- Cloud cost estimation has been performed. Resource right-sizing, auto-scaling, reserved instances, and cost alerting are addressed. FinOps tagging is applied for chargeback/showback.
- [ ] **2.18 Cloud-Native Design** -- The solution uses platform-as-a-service (PaaS) and serverless options where appropriate rather than defaulting to infrastructure-as-a-service (IaaS). Justification is provided if IaaS is selected.
- [ ] **2.19 Multi-Region / Geo-Redundancy** -- The solution's approach to geographic redundancy is documented and appropriate for the criticality tier. DR region pairing follows Azure best practices.

**Portfolio Architect Notes (Architecture Compliance):**

> _Enter observations, concerns, or conditions here._

---

## 3. Solution Quality

### Non-Functional Requirements

- [ ] **3.1 Performance Requirements** -- Performance targets (response time, throughput, batch processing windows) are defined, measurable, and traceable to business requirements.
- [ ] **3.2 Scalability** -- The solution's scalability approach (horizontal, vertical, auto-scaling) is documented and tested or validated against projected growth over a 3-5 year horizon.
- [ ] **3.3 Availability and SLA** -- Target availability (e.g., 99.9%, 99.95%) is stated and the architecture supports it. Single points of failure have been identified and mitigated or accepted.
- [ ] **3.4 Disaster Recovery** -- RTO (Recovery Time Objective) and RPO (Recovery Point Objective) are defined and achievable with the proposed architecture. DR procedures and failover mechanisms are documented.
- [ ] **3.5 Backup and Retention** -- Backup strategy, schedule, and retention periods are defined and aligned with corporate data retention policy.

### Operational Readiness

- [ ] **3.6 Monitoring and Observability** -- The solution integrates with corporate monitoring tools (e.g., Azure Monitor, Dynatrace, Splunk). Application and infrastructure health dashboards are planned.
- [ ] **3.7 Alerting** -- Alert thresholds, escalation paths, and notification channels are defined. Alerts are actionable and tied to runbook procedures.
- [ ] **3.8 Support Model** -- The operational support model (L1/L2/L3) is defined. Roles, responsibilities, SLAs for incident response, and on-call requirements are documented.
- [ ] **3.9 Logging and Audit Trail** -- Logging standards are followed. Audit trails for security-relevant and business-critical events are captured and retained per policy.

### Deployment Architecture

- [ ] **3.10 CI/CD Pipeline** -- A continuous integration and continuous deployment pipeline is defined using approved tooling (e.g., Azure DevOps, GitHub Actions). Manual deployment steps are minimized.
- [ ] **3.11 Infrastructure-as-Code** -- Infrastructure provisioning is codified (e.g., Terraform, Bicep, ARM templates) and version-controlled. No manually provisioned infrastructure for production environments.
- [ ] **3.12 Environment Strategy** -- Non-production environments (Dev, Test, UAT, Staging) are defined with appropriate isolation and data masking for sensitive data.
- [ ] **3.13 Rollback Strategy** -- A rollback or roll-forward strategy is documented for failed deployments. Database migration rollback is addressed.

**Portfolio Architect Notes (Solution Quality):**

> _Enter observations, concerns, or conditions here._

---

## 4. Risk and Compliance

### Security Risk

- [ ] **4.1 Threat Model** -- A security threat model (e.g., STRIDE) has been completed or is planned for the solution. Key threats and mitigations are documented.
- [ ] **4.2 Vulnerability Management** -- The solution includes provisions for vulnerability scanning, patching cadence, and dependency management (e.g., Dependabot, container image scanning).
- [ ] **4.3 Penetration Testing** -- Penetration testing is planned prior to production deployment for externally facing or high-risk solutions.

### Regulatory Compliance

- [ ] **4.4 SOX Compliance** -- If the solution processes financial data or supports SOX-relevant processes, appropriate controls (access controls, change management, audit logging) are designed in.
- [ ] **4.5 Privacy (PIPA / PIPEDA)** -- If the solution processes personal information, privacy impact assessment requirements have been addressed. Compliance with Alberta PIPA and federal PIPEDA is confirmed.
- [ ] **4.6 Pipeline and Facility Safety** -- If the solution supports pipeline operations or facility safety systems, compliance with applicable regulations (CER, AER, CSA Z662, PSM) is addressed.
- [ ] **4.7 Environmental Reporting** -- If the solution supports emissions tracking, environmental reporting, or carbon management, regulatory reporting requirements (TIER, OBPS) are incorporated.

### OT/IT Considerations

- [ ] **4.8 IEC 62443 Compliance** -- If the solution touches industrial automation and control systems, the design aligns with IEC 62443 security zones and conduits. The Purdue Model or equivalent network segmentation is respected.
- [ ] **4.9 Safety Instrumented Systems** -- The solution does not compromise the independence or integrity of any Safety Instrumented Systems (SIS) or process safety controls (IEC 61511).
- [ ] **4.10 OT Network Isolation** -- No direct pathways from IT networks or cloud services to OT Level 0-2 are introduced. Data flows through approved DMZ/historian architecture.

### Data Sovereignty and Residency

- [ ] **4.11 Data Residency** -- Data residency requirements are identified. Data classified as requiring Canadian residency is stored in Canadian Azure regions (Canada Central / Canada East) or approved on-premises locations.
- [ ] **4.12 Cross-Border Data Transfer** -- Any cross-border data flows (e.g., to US-based SaaS, vendor support access) are identified and assessed against privacy and regulatory requirements.
- [ ] **4.13 Third-Party Data Processing** -- If third parties process Cenovus data, appropriate data processing agreements, security assessments, and contractual protections are in place.

**Portfolio Architect Notes (Risk and Compliance):**

> _Enter observations, concerns, or conditions here._

---

## 5. Financial

- [ ] **5.1 Total Cost of Ownership (TCO)** -- A TCO analysis covering a minimum of 5 years is provided, including implementation, licensing, infrastructure, support, and decommissioning of replaced systems.
- [ ] **5.2 CapEx / OpEx Breakdown** -- Capital and operating expenditure are clearly separated. Cloud consumption costs are categorized appropriately per corporate finance policy.
- [ ] **5.3 License Model Assessment** -- The proposed licensing model (perpetual, subscription, consumption-based, BYOL) is evaluated and the most cost-effective approach for the expected usage is selected.
- [ ] **5.4 Comparison with Alternatives** -- At least two alternatives (including the "do nothing" or "extend current solution" option) have been evaluated with cost and capability comparisons.
- [ ] **5.5 Funding Confirmation** -- Budget allocation and funding source (project capital, sustaining capital, operating budget) are confirmed with Finance.
- [ ] **5.6 Cost Optimization Opportunities** -- Opportunities for cost optimization (reserved instances, dev/test pricing, license consolidation, sunsetting overlapping tools) are identified.

**Portfolio Architect Notes (Financial):**

> _Enter observations, concerns, or conditions here._

---

## 6. Portfolio Impact

- [ ] **6.1 Application Overlap / Duplication Check** -- The enterprise application portfolio has been reviewed to confirm no existing application already provides the proposed capability. ServiceNow CMDB and the application portfolio inventory have been consulted.
- [ ] **6.2 Rationalization Impact** -- The impact on application rationalization targets is assessed. If the solution replaces existing applications, a decommissioning plan and timeline are included.
- [ ] **6.3 Integration Touchpoints** -- All integration touchpoints with existing portfolio applications are identified and mapped. Upstream and downstream system owners have been notified and consulted.
- [ ] **6.4 Shared Services Consumption** -- The solution leverages existing shared services and platforms (e.g., enterprise integration, identity, monitoring, data platform) rather than introducing parallel capabilities.
- [ ] **6.5 Vendor Assessment (New Vendor)** -- If a new vendor is being introduced, a vendor assessment has been performed covering financial viability, strategic fit, support capabilities, security posture, and contractual terms. Procurement and Legal have been engaged.
- [ ] **6.6 Vendor Concentration Risk** -- The solution does not create unacceptable concentration risk with a single vendor. Portability and exit strategy are considered.
- [ ] **6.7 Technology Debt Impact** -- The solution reduces (or at minimum does not increase) the overall technology debt position. Any new technical debt introduced is documented with a remediation plan.

**Portfolio Architect Notes (Portfolio Impact):**

> _Enter observations, concerns, or conditions here._

---

## 7. Implementation Readiness

- [ ] **7.1 Resource Requirements** -- Required resources (internal staff, contractors, vendor professional services) are identified with roles, estimated effort, and availability confirmed.
- [ ] **7.2 Skills and Competency** -- The team possesses the necessary skills to implement and support the solution. Training or knowledge transfer plans are in place for any skill gaps.
- [ ] **7.3 Timeline Feasibility** -- The proposed implementation timeline is realistic given resource availability, dependencies, and organizational change capacity. Key milestones and critical path are identified.
- [ ] **7.4 Dependencies** -- External dependencies (other projects, vendor deliverables, infrastructure provisioning, third-party integrations) are identified with mitigation plans for delays.
- [ ] **7.5 Change Management Plan** -- An organizational change management plan is in place covering stakeholder communication, training, user adoption, and transition from current-state processes.
- [ ] **7.6 Testing Strategy** -- A testing strategy is defined covering unit testing, integration testing, performance testing, user acceptance testing, and security testing. Entry and exit criteria are documented.
- [ ] **7.7 Data Migration** -- If data migration is required, the migration strategy, tooling, data cleansing approach, validation criteria, and cutover plan are documented.
- [ ] **7.8 Go-Live and Hypercare** -- Go-live criteria, cutover plan, rollback triggers, and hypercare support period are defined.

**Portfolio Architect Notes (Implementation Readiness):**

> _Enter observations, concerns, or conditions here._

---

## Review Scoring and Recommendation

### Scoring Criteria

Each section (1 through 7) is scored as follows:

| Score | Meaning | Criteria |
|---|---|---|
| **Pass** | Section fully satisfies requirements | All applicable checklist items are confirmed. No outstanding gaps or concerns. |
| **Conditional** | Section has minor gaps that can be resolved | One or more items have identified gaps, but they are addressable before or shortly after ARB with defined action items and owners. |
| **Fail** | Section has material gaps requiring rework | Critical items are unaddressed, the design has fundamental issues in this area, or risk is unacceptable without significant redesign. |

### Section Scores

| Section | Score | Key Conditions / Actions Required |
|---|---|---|
| 1. Strategic Alignment | _Pass / Conditional / Fail_ | |
| 2. Architecture Compliance | _Pass / Conditional / Fail_ | |
| 3. Solution Quality | _Pass / Conditional / Fail_ | |
| 4. Risk and Compliance | _Pass / Conditional / Fail_ | |
| 5. Financial | _Pass / Conditional / Fail_ | |
| 6. Portfolio Impact | _Pass / Conditional / Fail_ | |
| 7. Implementation Readiness | _Pass / Conditional / Fail_ | |

### Overall Recommendation

| Outcome | Criteria |
|---|---|
| **Recommend for ARB Approval** | All sections score Pass. The solution is ready for ARB presentation. |
| **Recommend with Conditions** | No section scores Fail. One or more sections score Conditional, with action items documented below. The solution may proceed to ARB with conditions noted. |
| **Return for Rework** | One or more sections score Fail. The solution must address the identified gaps and resubmit for Portfolio Architect review before scheduling ARB. |

### Conditions and Required Actions

| # | Condition / Action | Owner | Target Date | Status |
|---|---|---|---|---|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |

### Portfolio Architect Sign-Off

| Field | Value |
|---|---|
| **Overall Recommendation** | _Recommend for ARB Approval / Recommend with Conditions / Return for Rework_ |
| **Portfolio Architect Name** | |
| **Signature / Approval** | |
| **Date** | |

---

## Revision History

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | 2026-02-08 | IT Architecture Team | Initial release |
