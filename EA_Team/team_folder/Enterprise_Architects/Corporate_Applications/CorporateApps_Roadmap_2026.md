# Enterprise Architecture Roadmap

**Domain:** Corporate Applications
**Portfolio Architect:** Corporate Applications EA
**Version:** 1.0
**Last Updated:** 2026-02-07
**Planning Horizon:** 2026 - 2029

---

## 1. Domain Overview

### 1.1 Scope & Boundaries
The Corporate Applications domain encompasses all enterprise systems that support Cenovus Energy's corporate functions: Finance, Human Resources, Supply Chain & Procurement, Legal & Compliance, and Corporate Collaboration. This includes the core SAP ERP landscape, HR management platforms, financial planning tools, procurement and contract management systems, and the Microsoft 365 collaboration suite.

**In Scope:**
- SAP ECC 6.0 and S/4HANA (FI/CO, MM, PM, PS, HR)
- SAP oil and gas modules (JVA, PRA, Royalty Management)
- Workday HCM (core HR, payroll, talent, workforce planning)
- Financial Planning & Analysis (Anaplan)
- Treasury Management (Kyriba)
- Tax compliance (Thomson Reuters ONESOURCE)
- Procurement & Contract Management (SAP Ariba, Icertis CLM)
- Microsoft 365 / SharePoint / Teams / Power Platform
- GRC & Compliance (SAP GRC, OneTrust)
- Enterprise Content Management (OpenText)

**Out of Scope:**
- Upstream production & drilling applications (Upstream Applications domain)
- Downstream refining & marketing systems (Downstream Applications domain)
- Integration middleware and MDM (Enterprise Applications domain)
- Infrastructure, cloud hosting, and cybersecurity (respective domains)

### 1.2 Strategic Alignment
This roadmap supports the following Cenovus Energy strategic pillars:

| Corporate Strategy Pillar | Corporate Applications Alignment |
|---------------------------|----------------------------------|
| Operational Excellence | SAP S/4HANA migration to standardize and automate business processes |
| Cost Discipline | SaaS rationalization and application consolidation to reduce total cost of ownership |
| ESG & Regulatory Compliance | Automated GRC reporting, emissions tracking integration, regulatory compliance tooling |
| Workforce of the Future | Workday modernization for talent management, workforce analytics, and employee experience |
| Digital Transformation | Power Platform citizen development, intelligent automation, AI-assisted finance operations |

### 1.3 Key Stakeholders
| Stakeholder | Role | Business Unit |
|-------------|------|---------------|
| VP Finance & Controller | Executive sponsor for SAP S/4HANA and financial systems | Finance |
| VP Human Resources | Executive sponsor for Workday and talent platforms | Human Resources |
| VP Supply Chain & Procurement | Business lead for Ariba and procurement systems | Supply Chain |
| General Counsel | Sponsor for CLM and GRC platforms | Legal |
| CIO / VP Information Technology | IT executive oversight, budget authority | IT |
| Director, IT Enterprise Applications | IT delivery lead for corporate systems | IT |
| Director, Financial Planning & Analysis | Business lead for Anaplan and financial reporting | Finance |
| Manager, JV Accounting | Business lead for SAP JVA and partner accounting | Finance |
| Director, Land & Regulatory | Business lead for land management and royalty systems | Land |
| IT Senior Leadership Team | Roadmap approval and investment governance | IT |

## 2. Current State Assessment

### 2.1 Application Portfolio
| Application | Business Capability | Functional Capability | Status | Health |
|-------------|--------------------|-----------------------|--------|--------|
| SAP ECC 6.0 (EHP 8) | Financial Management, Supply Chain, Asset Management | General Ledger, AP/AR, Cost Accounting, Materials Management, Plant Maintenance, Project Systems | Production | Yellow |
| SAP JVA (Joint Venture Accounting) | Joint Venture Management | JV billing, cash calls, partner netting, AFE management | Production | Yellow |
| SAP PRA (Production & Revenue Accounting) | Revenue Management | Production allocation, revenue distribution, royalty calculation | Production | Yellow |
| SAP HR / HCM | Workforce Administration (legacy) | Personnel admin, org management, Canadian payroll (being sunset) | Sunset | Red |
| SAP GRC 12.0 | Risk & Compliance | Access risk analysis, segregation of duties, process control | Production | Green |
| SAP Ariba | Procurement | Strategic sourcing, contract management, supplier management, P2P | Production | Green |
| SAP BPC 10.1 | Financial Planning | Budgeting, forecasting, financial consolidation | Production | Yellow |
| Workday HCM | Human Capital Management | Core HR, payroll, benefits, compensation, recruiting, learning | Production | Green |
| Workday Adaptive Planning | Workforce Planning | Headcount planning, compensation budgeting | Emerging | Green |
| Anaplan | Financial Planning & Analysis | Revenue forecasting, cost modelling, scenario planning | Production | Green |
| Kyriba | Treasury Management | Cash management, bank connectivity, payment factory, FX exposure | Production | Green |
| Thomson Reuters ONESOURCE | Tax Compliance | Corporate tax provisioning, tax return preparation, indirect tax | Production | Green |
| Icertis CLM | Contract Lifecycle Management | Contract authoring, obligation tracking, clause library | Production | Green |
| OpenText Extended ECM | Enterprise Content Management | Document management, records management, SAP content integration | Production | Yellow |
| Microsoft 365 (E5) | Corporate Collaboration | Exchange, Teams, SharePoint, OneDrive, Power Platform | Production | Green |
| Power Platform | Citizen Development & Automation | Power Apps, Power Automate, Power BI, Copilot Studio | Emerging | Green |
| OneTrust | Privacy & Compliance | Privacy management, cookie consent, DSAR automation | Production | Green |
| SAP SuccessFactors (partial) | Learning & Performance (legacy) | LMS module only (being consolidated into Workday) | Sunset | Red |
| Lotus Notes (legacy) | Legacy Collaboration | Legacy workflow apps, forms (handful of remaining apps) | Sunset | Red |
| Maximo (legacy) | Asset Management (partial) | Work orders for select downstream sites (being consolidated into SAP PM) | Sunset | Yellow |

### 2.2 Technology Stack
| Layer | Technology | Version | End of Support |
|-------|-----------|---------|----------------|
| ERP Core | SAP ECC 6.0 EHP 8 | EHP 8 | 2027 (mainstream), 2030 (extended) |
| ERP Target | SAP S/4HANA | 2025 FPS02 (target) | Current |
| Database (current) | SAP HANA | 2.0 SPS07 | 2030 |
| HR Platform | Workday | Current SaaS (bi-annual releases) | N/A (SaaS) |
| Procurement | SAP Ariba | Current SaaS | N/A (SaaS) |
| Financial Planning | Anaplan | Current SaaS | N/A (SaaS) |
| Treasury | Kyriba | Current SaaS | N/A (SaaS) |
| CLM | Icertis | Current SaaS | N/A (SaaS) |
| Content Management | OpenText Extended ECM | 23.4 | 2027 |
| Collaboration | Microsoft 365 E5 | Current SaaS | N/A (SaaS) |
| GRC | SAP GRC | 12.0 | Aligned with ECC/S4 |
| Tax | Thomson Reuters ONESOURCE | Current SaaS | N/A (SaaS) |
| Middleware | SAP BTP / Integration Suite | Current SaaS | N/A (SaaS) |

### 2.3 Strengths
- Workday HCM fully deployed with strong adoption across all Canadian and US operations
- SAP Ariba providing mature procure-to-pay automation with supplier network connectivity
- Anaplan delivering flexible financial modelling capability for commodity-sensitive planning
- Microsoft 365 E5 well-adopted with Teams as primary collaboration platform
- Kyriba Treasury providing consolidated cash visibility across all operating entities
- Icertis CLM live and providing value for high-volume surface land and service agreements
- Strong SAP COE with deep knowledge of oil and gas specific modules (JVA, PRA)

### 2.4 Gaps & Pain Points
| # | Gap | Business Impact | Priority |
|---|-----|-----------------|----------|
| 1 | SAP ECC 6.0 approaching end of mainstream support (2027) | Risk of unsupported core ERP; blocks adoption of S/4HANA innovations | Critical |
| 2 | SAP BPC 10.1 end of life; no clear financial consolidation path post-migration | Finance consolidation process at risk; manual workarounds increasing | High |
| 3 | JV Accounting custom ABAP code (~1,200 custom objects) complicates S/4HANA migration | Significant remediation effort; risk of functional regression during conversion | Critical |
| 4 | Legacy Lotus Notes apps (12 remaining) with no modern equivalent | Manual processes, knowledge loss risk, security vulnerabilities | Medium |
| 5 | OpenText ECM version approaching end of support; content migration needed | Document access and compliance risk | High |
| 6 | No integrated ESG / emissions reporting tool linked to financial systems | Manual data gathering for sustainability reporting; risk of regulatory non-compliance | High |
| 7 | SAP SuccessFactors LMS and Workday Learning overlap creating user confusion | Duplicate systems, inconsistent training records, wasted license cost | Medium |
| 8 | Limited Power Platform governance; citizen-developed apps lack lifecycle management | Shadow IT risk, data quality issues, unsupported business-critical apps | Medium |
| 9 | Maximo still running at select downstream sites alongside SAP PM | Duplicate CMMS, inconsistent maintenance data, integration overhead | Medium |
| 10 | No AI/ML-assisted capabilities in finance close, AP invoice processing, or procurement | Missed efficiency gains versus industry peers | Medium |

### 2.5 Technical Debt
| Item | Risk | Effort to Remediate | Priority |
|------|------|---------------------|----------|
| 1,200+ custom ABAP objects in SAP ECC | S/4HANA migration blocker; upgrade regression risk | High (12-18 months remediation) | Critical |
| SAP BPC on NetWeaver 7.5 | End-of-life platform; no path to S/4HANA embedded analytics | Medium (6-9 months to migrate to SAC Planning) | High |
| Lotus Notes legacy apps (12 apps) | Unsupported platform, security risk, no mobile access | Low-Medium (3-6 months to replatform to Power Platform) | Medium |
| SAP Fiori launchpad not deployed | Users stuck on SAP GUI; poor user experience | Medium (phased rollout 6-12 months) | Medium |
| OpenText ECM on 23.4 (EOL 2027) | Content access and compliance risk post-EOS | Medium (6-9 months for cloud migration) | High |
| Unmanaged Power Platform environments | Ungoverned citizen apps may contain sensitive data or break silently | Low (2-3 months for governance framework) | Medium |
| SAP SuccessFactors LMS redundant to Workday Learning | Duplicate license cost, user confusion | Low (3-4 months to decommission and migrate content) | Medium |

## 3. Future State Vision

### 3.1 Target Architecture
The target state for Corporate Applications at Cenovus Energy envisions:

**Core ERP:** SAP S/4HANA (on-premise or private cloud edition) as the single financial and operational backbone, with clean core principles -- minimizing custom ABAP in favor of SAP BTP side-by-side extensions. Oil and gas specific capabilities (JVA, PRA, Royalty) fully converted to S/4HANA equivalents or partner solutions.

**HR:** Workday as the single HCM platform covering core HR, payroll, recruiting, learning, talent, and workforce planning. No residual SAP HCM or SuccessFactors modules.

**Finance & Planning:** SAP Analytics Cloud (SAC) Planning replacing BPC for financial consolidation and group reporting. Anaplan retained for operational FP&A. Kyriba retained for treasury. ONESOURCE retained for tax.

**Procurement & Contracts:** SAP Ariba for procure-to-pay and strategic sourcing. Icertis CLM for contract lifecycle management. Tight integration between Ariba, Icertis, and S/4HANA via SAP BTP Integration Suite.

**Collaboration & Productivity:** Microsoft 365 as the enterprise collaboration platform. Power Platform with formal governance as the citizen development platform. Microsoft Copilot integrated for productivity.

**Content Management:** OpenText migrated to cloud-native or replaced with Microsoft Purview / SharePoint Premium for content services, integrated with S/4HANA.

**GRC & Compliance:** SAP GRC migrated to cloud-native (SAP Cloud IAG or embedded S/4HANA GRC). OneTrust retained for privacy. New ESG reporting tool integrated with S/4HANA and operational data.

**AI & Automation:** SAP Joule and Microsoft Copilot embedded across platforms. Intelligent automation in AP invoice processing, journal entry anomaly detection, and procurement analytics.

### 3.2 Guiding Principles
1. **Clean Core:** Minimize custom code in SAP S/4HANA; extend via SAP BTP side-by-side extensions and APIs.
2. **SaaS-First:** Prefer SaaS solutions over on-premise where data sovereignty and latency requirements allow.
3. **Best-of-Suite with Strategic Best-of-Breed:** Leverage SAP and Microsoft platform synergies; allow best-of-breed only where clear functional superiority exists (e.g., Workday for HCM, Anaplan for FP&A).
4. **One Platform Per Capability:** Eliminate redundant applications; one system of record per business capability.
5. **Integration over Point-to-Point:** All integrations route through SAP BTP Integration Suite or Azure Integration Services; no direct database links.
6. **Data as an Asset:** Master data ownership defined per domain; golden records maintained in MDM with distribution to consuming systems.
7. **AI-Augmented Processes:** Embed AI/ML capabilities into existing workflows rather than deploying standalone AI tools.

### 3.3 Target Application Portfolio
| Application | Business Capability | Functional Capability | Change |
|-------------|--------------------|-----------------------|--------|
| SAP S/4HANA | Financial Management, Supply Chain, Asset Management | GL, AP/AR, Cost Accounting, MM, PM, PS, JVA, PRA | Replace (from ECC) |
| SAP S/4HANA Cloud for Group Reporting | Financial Consolidation | Statutory consolidation, intercompany elimination, group reporting | Replace (from BPC) |
| SAP Analytics Cloud (SAC) Planning | Financial Planning | Budgeting, forecasting, planning scenarios | Replace (from BPC) |
| SAP Fiori Launchpad | User Experience | Role-based UX for all SAP transactions | New |
| SAP BTP (Business Technology Platform) | Extension & Integration | Custom extensions, integrations, analytics, AI | New |
| SAP GRC (Cloud or embedded) | Risk & Compliance | Access governance, process control, audit management | Enhance |
| SAP Ariba | Procurement | Sourcing, P2P, supplier management | Retain |
| Workday HCM | Human Capital Management | Core HR, payroll, benefits, recruiting, learning, talent | Retain |
| Workday Adaptive Planning | Workforce Planning | Headcount planning, compensation budgeting | Enhance |
| Anaplan | Financial Planning & Analysis | Revenue forecasting, operational modelling | Retain |
| Kyriba | Treasury Management | Cash management, payments, FX | Retain |
| Thomson Reuters ONESOURCE | Tax Compliance | Tax provisioning, returns, indirect tax | Retain |
| Icertis CLM | Contract Lifecycle Management | Contract authoring, obligations, analytics | Retain |
| Microsoft 365 (E5) + Copilot | Collaboration & Productivity | Email, Teams, SharePoint, Copilot AI | Enhance |
| Power Platform (governed) | Citizen Development | Power Apps, Power Automate, Copilot Studio | Enhance |
| Microsoft Purview / SharePoint Premium | Content Management | Document management, records, content AI | Replace (from OpenText) |
| ESG Reporting Tool (TBD - evaluate Persefoni, Salesforce Net Zero, SAP SFC) | ESG & Sustainability Reporting | Emissions tracking, ESG disclosure, regulatory reporting | New |
| SAP SuccessFactors LMS | Learning (legacy) | LMS | Retire |
| Lotus Notes (legacy apps) | Legacy Collaboration | Workflow apps | Retire |
| Maximo (downstream sites) | Asset Management | CMMS | Retire |
| SAP BPC 10.1 | Financial Planning (legacy) | Budgeting, consolidation | Retire |
| OpenText Extended ECM | Content Management (legacy) | Document management | Retire |
| SAP ECC 6.0 | ERP (legacy) | All ECC functions | Retire (post S/4 go-live) |

## 4. Transition Roadmap

### 4.1 Roadmap Swimlanes

#### Near Term (0-12 months: Q1 2026 - Q4 2026)
| Initiative | Description | Dependencies | Status |
|-----------|-------------|--------------|--------|
| S/4HANA Readiness Assessment | Complete SAP Readiness Check, custom code analysis (1,200 objects), data volume assessment, and fit-to-standard workshops for FI/CO, MM, PM, PS | SAP licensing agreement signed | In Progress |
| S/4HANA JVA/PRA Assessment | Detailed analysis of oil & gas modules (JVA, PRA, Royalty) for S/4HANA compatibility; evaluate partner solutions (e.g., SAP Joint Venture Accounting for S/4) | S/4 Readiness Assessment | Planning |
| Custom Code Remediation (Phase 1) | Begin remediation of critical custom ABAP: simplification database adaptations, deprecated API replacements | Custom code analysis complete | Planning |
| SAP BPC to SAC Planning Migration | Migrate budgeting and forecasting from BPC 10.1 to SAP Analytics Cloud Planning | SAC Planning licenses procured | In Progress |
| Lotus Notes App Retirement | Replatform remaining 12 Lotus Notes apps to Power Platform / SharePoint | Power Platform governance framework | In Progress |
| SuccessFactors LMS Decommission | Migrate learning content and history to Workday Learning; decommission SF LMS | Workday Learning module active | Planning |
| Power Platform Governance Framework | Implement DLP policies, environment strategy, CoE Starter Kit, ALM for citizen-developed apps | M365 E5 licensing in place | In Progress |
| ESG Reporting Tool RFP | Evaluate and select ESG reporting platform; run proof-of-concept with shortlisted vendors | ESG data inventory complete | Planning |
| Microsoft Copilot Pilot | Deploy M365 Copilot to 500 pilot users (Finance, HR, Legal); measure adoption and ROI | M365 E5 + Copilot licensing | In Progress |
| OpenText Cloud Migration Assessment | Evaluate migration path: OpenText Cloud Edition vs. Microsoft Purview/SharePoint Premium | Content inventory and classification | Planning |

#### Medium Term (12-24 months: Q1 2027 - Q4 2027)
| Initiative | Description | Dependencies | Status |
|-----------|-------------|--------------|--------|
| S/4HANA System Conversion (Phase 1) | Convert SAP ECC to S/4HANA for FI/CO, MM, PM, PS modules; deploy SAP Fiori for key roles | Custom code remediation Phase 1 complete; sandbox/dev conversion tested | Planning |
| S/4HANA JVA Conversion | Convert JV Accounting to S/4HANA; deploy new JV settlement and partner accounting processes | JVA assessment complete; S/4 Phase 1 stable | Planning |
| S/4HANA Group Reporting | Implement S/4HANA Cloud for Group Reporting to replace BPC consolidation | S/4HANA Phase 1 live; SAC Planning live | Planning |
| SAP BTP Extensions Build-out | Develop key side-by-side extensions on SAP BTP: custom pricing, AFE approval workflows, partner portal | S/4HANA Phase 1 live; BTP subscription active | Planning |
| Maximo Decommission | Migrate remaining downstream Maximo work orders and asset data to SAP PM on S/4HANA | S/4HANA PM module live | Planning |
| OpenText ECM Migration/Replacement | Execute content migration to target platform (cloud OpenText or SharePoint Premium) | Assessment complete; target platform selected | Planning |
| ESG Reporting Platform Implementation | Deploy selected ESG tool; integrate with S/4HANA (emissions data), Workday (social metrics), operational systems | Tool selected; integration architecture approved | Planning |
| Intelligent AP Automation | Deploy AI-assisted invoice processing (SAP Business AI or Kofax) for accounts payable | S/4HANA FI module live; AP volume baseline | Planning |
| Microsoft Copilot Enterprise Rollout | Expand Copilot to all eligible users; deploy Copilot Studio for custom business agents | Pilot results reviewed; governance model in place | Planning |

#### Long Term (24-36 months: Q1 2028 - Q4 2028)
| Initiative | Description | Dependencies | Status |
|-----------|-------------|--------------|--------|
| S/4HANA Conversion (Phase 2) | Complete remaining modules: PRA (Production Revenue Accounting), Royalty, advanced Plant Maintenance | Phase 1 stable; PRA assessment complete | Planning |
| SAP ECC Decommission | Retire SAP ECC 6.0 environment after full S/4HANA conversion and parallel run validation | S/4HANA Phase 2 complete; data archival done | Planning |
| SAP GRC Cloud Migration | Migrate GRC from on-premise to Cloud Identity Access Governance (IAG) or S/4HANA embedded | S/4HANA stable; IAG licensing | Planning |
| AI-Augmented Finance Close | Deploy ML-based journal entry anomaly detection, automated account reconciliation, predictive close analytics | S/4HANA live; SAC Analytics active | Planning |
| Procurement Analytics & AI | Implement spend analytics, supplier risk scoring, and contract intelligence using Ariba + Icertis AI | Ariba/Icertis stable; data quality baseline | Planning |
| Workday Advanced Analytics | Deploy Workday Prism Analytics for workforce planning models, attrition prediction, DEI analytics | Workday data maturity; People Analytics team | Planning |
| BPC 10.1 Decommission | Retire SAP BPC after SAC Planning and S/4HANA Group Reporting fully operational | SAC Planning live; Group Reporting live | Planning |
| Power Platform Advanced Scenarios | Scale Copilot Studio custom agents for IT service desk, field operations support, HR self-service | Copilot enterprise rollout complete; governance mature | Planning |

### 4.2 Key Milestones
| Milestone | Target Date | Dependencies |
|-----------|-------------|--------------|
| S/4HANA Readiness Assessment complete | Q2 2026 | SAP engagement |
| SAP BPC to SAC Planning migration go-live | Q3 2026 | SAC Planning build/test |
| Lotus Notes fully retired | Q4 2026 | Power Platform replatforming |
| SuccessFactors LMS decommissioned | Q3 2026 | Workday Learning content migration |
| Power Platform governance framework live | Q2 2026 | CoE Starter Kit deployment |
| ESG reporting tool selected | Q3 2026 | RFP evaluation complete |
| S/4HANA Phase 1 go-live (FI/CO, MM, PM, PS) | Q2 2027 | System conversion; custom code remediation |
| S/4HANA JVA conversion go-live | Q4 2027 | JVA fit-to-standard; Phase 1 stable |
| OpenText ECM migrated/replaced | Q3 2027 | Target platform build |
| ESG reporting platform go-live | Q4 2027 | Integration build; data feeds |
| S/4HANA Phase 2 go-live (PRA, Royalty) | Q2 2028 | PRA remediation; Phase 1 stable |
| SAP ECC 6.0 decommissioned | Q4 2028 | Full S/4HANA conversion validated |
| SAP BPC 10.1 decommissioned | Q4 2028 | SAC Planning + Group Reporting live |

### 4.3 Application Rationalization Plan
| Application | Action | Target Date | Savings |
|-------------|--------|-------------|---------|
| SAP ECC 6.0 | Retire (replaced by S/4HANA) | Q4 2028 | Infrastructure cost elimination (~$1.2M/yr) |
| SAP BPC 10.1 | Retire (replaced by SAC Planning + Group Reporting) | Q4 2028 | License + infrastructure (~$350K/yr) |
| SAP SuccessFactors LMS | Retire (consolidated into Workday Learning) | Q3 2026 | License cost (~$180K/yr) |
| Lotus Notes (legacy apps) | Retire (replatformed to Power Platform) | Q4 2026 | License + infrastructure (~$50K/yr) |
| Maximo (downstream) | Retire (consolidated into SAP PM) | Q4 2027 | License + integration maintenance (~$250K/yr) |
| OpenText Extended ECM | Retire or Migrate to Cloud | Q3 2027 | On-premise infrastructure (~$200K/yr); net savings depends on target |
| Miscellaneous shadow IT tools (5-8 point solutions) | Consolidate into Power Platform or existing SaaS | Ongoing 2026-2027 | License + support (~$100K/yr combined) |
| **Total Estimated Annual Savings** | | | **~$2.3M/yr (fully realized by 2029)** |

## 5. Investment Summary
| Initiative | CapEx | OpEx (Annual) | Priority | Year |
|-----------|-------|---------------|----------|------|
| S/4HANA System Conversion (Phase 1 & 2) | $18-25M | $3.5M (post go-live run) | Critical | 2026-2028 |
| S/4HANA JVA/PRA Conversion (included above but called out for scale) | (included in S/4 program) | (included) | Critical | 2027-2028 |
| SAP BPC to SAC Planning Migration | $1.2M | $400K | High | 2026 |
| S/4HANA Group Reporting Implementation | $1.5M | $300K | High | 2027 |
| SAP BTP Extensions & Integration Platform | $2M | $600K | High | 2027-2028 |
| ESG Reporting Platform | $800K-1.2M | $250K | High | 2026-2027 |
| OpenText Migration/Replacement | $1M-1.5M | $200K (cloud hosting) | High | 2027 |
| Microsoft Copilot Rollout | $300K (deployment) | $1.8M (licensing ~5,000 users @ $30/user/mo) | Medium | 2026-2027 |
| Power Platform Governance & Scale-out | $200K | $150K | Medium | 2026 |
| Intelligent AP Automation | $500K | $120K | Medium | 2027 |
| Lotus Notes Retirement | $150K | $0 | Medium | 2026 |
| SuccessFactors LMS Retirement | $100K | $0 | Medium | 2026 |
| **Total (estimated)** | **$26-33M** | **$7.3M (new ongoing)** | | 2026-2028 |

*Note: S/4HANA conversion is the dominant investment. Savings from rationalization (~$2.3M/yr) partially offset increased ongoing SaaS costs.*

## 6. Risks & Dependencies
| Risk/Dependency | Type | Likelihood | Impact | Mitigation |
|-----------------|------|-----------|--------|------------|
| SAP ECC 6.0 end of mainstream support (2027) | Risk | High | Critical | S/4HANA conversion program initiated; extended maintenance contracted as insurance |
| S/4HANA conversion timeline slippage due to JVA/PRA complexity | Risk | Medium | High | Dedicated oil & gas module workstream; engage SAP and SI partners with O&G experience; phase the conversion |
| Custom ABAP remediation exceeds estimated effort (1,200+ objects) | Risk | Medium | High | Early custom code analysis; prioritize by usage and criticality; retire unused objects aggressively |
| Business disruption during S/4HANA cutover | Risk | Medium | High | Phased conversion approach; extensive parallel testing; hypercare support model |
| Key person dependency on SAP COE (JVA/PRA expertise) | Risk | Medium | Medium | Cross-training; engage external partners; document tribal knowledge |
| Workday bi-annual release management overhead | Risk | Low | Medium | Dedicated Workday release manager; regression test automation |
| Microsoft Copilot ROI not realized | Risk | Medium | Medium | Phased rollout with measurable KPIs; pilot before enterprise deployment |
| Data quality issues impacting S/4HANA migration | Risk | Medium | High | Master data cleansing program as prerequisite; MDM alignment with Enterprise Applications domain |
| SAP licensing model changes (RISE with SAP) impact TCO | Risk | Medium | Medium | Engage SAP account team early; model RISE vs. on-premise scenarios |
| Dependency on Enterprise Applications domain for integration platform (BTP/Azure) | Dependency | N/A | High | Joint planning with Enterprise Applications EA; shared BTP roadmap |
| Dependency on Cloud EA for Azure/hosting strategy for S/4HANA | Dependency | N/A | High | Aligned infrastructure planning; joint S/4 hosting decision by Q2 2026 |
| Dependency on Cyber Security EA for S/4HANA security architecture | Dependency | N/A | High | Security architecture review gate in S/4 program; Zero Trust alignment |
| Regulatory changes (Canadian energy regulations, IFRS updates) | Risk | Medium | Medium | Maintain regulatory watch; engage external advisors; agile configuration approach |

## 7. Governance & Review
- Roadmap review frequency: Quarterly
- Next review date: Q2 2026 (April)
- Approval authority: Team Leader (Chief Architect) + IT Senior Leadership
- S/4HANA Program governance: Dedicated steering committee with monthly cadence
- Architecture Review Board (ARB): All new corporate application requests reviewed against this roadmap
- Change management: Roadmap changes >$500K or with cross-domain impact require Team Leader approval

## 8. Appendices

### 8.1 Capability Map Summary
**Finance Capabilities:** General Ledger, Accounts Payable, Accounts Receivable, Fixed Assets, Cost Accounting, JV Accounting, Production Revenue Accounting, Royalty Management, Financial Consolidation, Budgeting & Forecasting, Treasury, Tax Compliance, ESG Financial Reporting

**HR Capabilities:** Core HR, Payroll (Canada & US), Benefits Administration, Recruiting & Onboarding, Learning & Development, Performance Management, Compensation, Succession Planning, Workforce Planning, Time & Attendance

**Supply Chain Capabilities:** Strategic Sourcing, Purchase Requisitions, Purchase Orders, Goods Receipt, Invoice Verification, Supplier Management, Contract Management, Inventory Management, Warehouse Management

**Asset Management Capabilities:** Preventive Maintenance, Corrective Maintenance, Work Order Management, Equipment Master, Maintenance Planning, Shutdown/Turnaround Planning

**Collaboration Capabilities:** Email & Calendar, Instant Messaging & Video, Document Collaboration, Intranet & Knowledge Management, Workflow Automation, Citizen Development

**Legal & Compliance Capabilities:** Contract Lifecycle Management, Access Governance, Segregation of Duties, Process Controls, Privacy Management, Regulatory Reporting

### 8.2 Vendor Landscape
| Vendor | Products | Relationship | Contract Renewal |
|--------|----------|-------------|-----------------|
| SAP | ECC, S/4HANA, Ariba, BPC, SAC, GRC, BTP | Strategic Partner | Enterprise agreement - 2028 |
| Workday | HCM, Adaptive Planning | Strategic Partner | Multi-year subscription - 2027 |
| Microsoft | M365, Azure, Power Platform, Copilot | Strategic Partner | Enterprise Agreement - 2027 |
| Anaplan | FP&A Platform | Preferred | Subscription - 2027 |
| Kyriba | Treasury Management | Preferred | Subscription - 2026 (renewal pending) |
| Thomson Reuters | ONESOURCE Tax | Preferred | Subscription - 2027 |
| Icertis | Contract Lifecycle Management | Preferred | Subscription - 2028 |
| OpenText | Extended ECM | Under Review (sunset path) | Maintenance - 2027 |
| OneTrust | Privacy & Compliance | Standard | Subscription - 2027 |

### 8.3 Related EA Domain Roadmaps
- IT Infrastructure Roadmap: Data center strategy impacts S/4HANA hosting decision
- IT Cloud Roadmap: Azure strategy for SAP workloads and SaaS integrations
- IT Cyber Security Roadmap: Zero Trust architecture, IAM for S/4HANA and SaaS applications
- IT AI Roadmap: AI platform strategy for intelligent automation in corporate applications
- Enterprise Applications Roadmap: Integration platform (BTP/Azure), MDM, enterprise reporting
- Upstream Applications Roadmap: Production data feeds to PRA and royalty systems
- Downstream Applications Roadmap: Refining data integration with SAP PM and finance
