# Enterprise Architecture Roadmap

**Domain:** Downstream Applications
**Portfolio Architect:** Downstream Applications EA
**Version:** 1.0
**Last Updated:** 2026-02-07
**Planning Horizon:** 2026 - 2029

---

## 1. Domain Overview

### 1.1 Scope & Boundaries
The Downstream Applications domain encompasses all technology systems supporting Cenovus Energy's downstream operations, including:

- **Refining & Upgrading Operations** -- Process control (DCS), advanced process control (APC), refinery planning and scheduling, and process simulation at the Lima (Ohio), Superior (Wisconsin), and Toledo (Ohio) refineries, as well as the Christina Lake and Foster Creek upgraders
- **Manufacturing Execution** -- MES, batch management, production accounting, yield tracking, and production reporting
- **Pipeline & Transportation** -- Pipeline SCADA, nomination and scheduling, pipeline integrity management, and crude/product logistics
- **Marketing & Trading** -- Crude marketing, product trading, energy trading and risk management (ETRM), and contract management
- **Quality & Lab** -- LIMS, quality management, blending optimization, and product certification
- **Environmental & Regulatory** -- Emissions tracking, environmental monitoring, regulatory compliance reporting (EPA, AER, ECCC), and carbon management

**Boundaries:** This domain interfaces with but does not own: upstream production systems (Upstream Applications EA), SAP ERP financial modules (Corporate Applications EA), enterprise integration middleware (Enterprise Applications EA), OT network infrastructure (IT Infrastructure EA), and OT cybersecurity (IT Cyber Security EA).

### 1.2 Strategic Alignment
This domain supports Cenovus Energy's corporate strategy in the following ways:

| Corporate Priority | Downstream Technology Alignment |
|---|---|
| Operational Excellence | APC optimization, digital twin deployment, MES real-time visibility |
| Safety & Reliability | Integrated DCS/SIS lifecycle management, alarm rationalization |
| ESG & Emissions Reduction | Continuous emissions monitoring, carbon tracking, flare management |
| Margin Optimization | ETRM enhancement, refinery LP planning, blending optimization |
| Cost Discipline | Application rationalization, cloud migration for non-OT workloads |
| Digital Transformation | Industry 4.0 adoption, predictive maintenance, AI-driven analytics |

### 1.3 Key Stakeholders
| Stakeholder | Role | Business Unit |
|---|---|---|
| VP Refining Operations | Executive Sponsor | Downstream Operations |
| Lima Refinery Manager | Site Operations Lead | Lima Refinery |
| Superior Refinery Manager | Site Operations Lead | Superior Refinery |
| Toledo Refinery Manager | Site Operations Lead | Toledo Refinery |
| VP Marketing & Trading | Trading & Commercial Lead | Crude Marketing / Products |
| Director Pipeline Operations | Transportation Lead | Pipeline & Logistics |
| Director Process Engineering | Engineering Lead | Downstream Engineering |
| Director HSE | Safety & Environment Lead | Health, Safety & Environment |
| IT Director Downstream | IT Delivery Lead | IT |
| OT Manager | OT Infrastructure Lead | IT / OT Convergence |

## 2. Current State Assessment

### 2.1 Application Portfolio
| Application | Business Capability | Functional Capability | Status | Health |
|---|---|---|---|---|
| Honeywell Experion PKS | Refinery Process Control | DCS - Lima & Superior | Production | Green |
| Yokogawa CENTUM VP | Refinery Process Control | DCS - Toledo | Production | Yellow |
| Honeywell Profit Controller | Advanced Process Control | APC - Multivariable Control | Production | Yellow |
| AspenTech Aspen HYSYS | Process Engineering | Process Simulation & Modelling | Production | Green |
| AspenTech PIMS-AO | Refinery Planning | Linear Programming / Planning | Production | Green |
| AspenTech Orion (Aspen Unified) | Refinery Scheduling | Production Scheduling | Production | Yellow |
| AVEVA PI System (OSIsoft) | Data Historian | Real-time & Historical Process Data | Production | Green |
| Honeywell PHD | Data Historian (Legacy) | Historical Process Data - Superior | Production | Red |
| AVEVA MES | Manufacturing Execution | Production Tracking & Reporting | Production | Yellow |
| Emerson Syncade (partial) | Batch Management | Batch Execution - Specialty Products | Production | Yellow |
| Openlink Endur | Trading & Risk Mgmt | ETRM - Crude & Products | Production | Yellow |
| SAP IS-Oil | Logistics & Settlement | Nomination, Scheduling, Settlement | Production | Yellow |
| LabWare LIMS | Lab Information Mgmt | Sample Mgmt, Quality Testing | Production | Green |
| Spirent (TopTech) TankMaster | Tank Gauging | Inventory Management | Production | Green |
| ABB Ability Symphony Plus | Pipeline SCADA | Pipeline Monitoring & Control | Production | Green |
| Quorum Pipeline Manager | Pipeline Scheduling | Nomination & Scheduling | Production | Yellow |
| Sphera SpheraCloud | Environmental Compliance | Emissions Tracking & Reporting | Production | Green |
| Intelex EHSQ | EHS Management | Incident, MOC, Inspection Mgmt | Production | Green |
| Schneider Electric SimSci PRO/II | Process Simulation (Legacy) | Simulation - Toledo (Legacy) | Sunset | Red |
| Custom VBA/Access Tools | Various | Ad-hoc Reporting & Calculations | Production | Red |

### 2.2 Technology Stack
| Layer | Technology | Version | End of Support |
|---|---|---|---|
| DCS - Lima/Superior | Honeywell Experion PKS | R520 | 2032 |
| DCS - Toledo | Yokogawa CENTUM VP | R6.09 | 2029 |
| APC | Honeywell Profit Controller | R470 | 2028 |
| Process Simulation | AspenTech Aspen HYSYS | V14 | 2028 |
| Planning (LP) | AspenTech PIMS-AO | V14 | 2028 |
| Historian - Primary | AVEVA PI System | 2023 R2 | 2028 |
| Historian - Legacy | Honeywell PHD | 8.2 | 2026 (EOL) |
| MES | AVEVA MES | 2023 | 2028 |
| ETRM | Openlink Endur | V18 | 2027 |
| LIMS | LabWare LIMS | 8.x | 2029 |
| Pipeline SCADA | ABB Symphony Plus | 3.1 | 2030 |
| Env. Compliance | Sphera SpheraCloud | SaaS | N/A (SaaS) |
| Server OS (OT DMZ) | Windows Server | 2019 | 2029 |
| Database (OT apps) | Microsoft SQL Server | 2019 | 2030 |
| Database (ETRM) | Oracle Database | 19c | 2027 |

### 2.3 Strengths
- Mature DCS infrastructure at Lima and Superior with Honeywell Experion standardization
- AVEVA PI System deployed as enterprise historian providing unified data access across sites
- Strong AspenTech planning/scheduling suite well integrated with refinery operations
- LabWare LIMS provides robust quality management across all refinery sites
- Sphera and Intelex SaaS platforms reduce maintenance overhead for compliance
- Experienced OT operations teams with deep process knowledge
- Established OT/IT DMZ architecture following Purdue model

### 2.4 Gaps & Pain Points
| # | Gap | Business Impact | Priority |
|---|---|---|---|
| 1 | Honeywell PHD historian at Superior approaching end-of-life | Risk of data loss, no vendor support for patches | Critical |
| 2 | Endur ETRM on aging version (V18); Oracle 19c nearing end of support | Trading desk operational risk, compliance gaps | Critical |
| 3 | No unified digital twin across refinery sites | Inability to simulate cross-refinery optimization | High |
| 4 | Fragmented MES deployment -- AVEVA MES at Lima only, manual tracking elsewhere | Inconsistent production reporting, yield leakage | High |
| 5 | APC controllers degraded -- many Profit Controller apps offline or underperforming | Lost margin opportunity estimated $3-5M/year per refinery | High |
| 6 | Legacy custom VBA/Access tools for blending and scheduling calculations | No audit trail, single-person dependency, data integrity risk | High |
| 7 | Limited pipeline integrity data integration with GIS and EAM | Siloed integrity data, manual correlation for dig programs | Medium |
| 8 | No AI/ML platform for predictive maintenance on rotating equipment | Reactive maintenance approach, unplanned downtime | Medium |
| 9 | Environmental data still requires manual aggregation for EPA reporting | Labour-intensive quarterly reporting, error-prone | Medium |
| 10 | Lack of real-time crude assay tracking from wellhead through processing | Sub-optimal crude blending at refinery gate | Medium |

### 2.5 Technical Debt
| Item | Risk | Effort to Remediate | Priority |
|---|---|---|---|
| Honeywell PHD legacy historian | System failure, no vendor support | Medium -- migrate tags to PI System | Critical |
| SimSci PRO/II Toledo legacy simulation | Unsupported, results diverge from HYSYS | Low -- retire and migrate models to HYSYS | High |
| Custom VBA/Access blending tools | Data loss, no version control, key-person risk | Medium -- replace with Aspen Blend Optimizer | High |
| Endur V18 on Oracle 19c | Oracle extended support costs, patch lag | High -- major upgrade to Endur V21+ on Oracle 23c | Critical |
| Windows Server 2016 on select OT servers | End of extended support | Medium -- OS upgrade with DCS patch compatibility | High |
| Manual data bridges (CSV exports between ETRM and SAP) | Reconciliation errors, settlement delays | Medium -- implement API/middleware integration | Medium |

## 3. Future State Vision

### 3.1 Target Architecture
The target state for Downstream Applications envisions a **connected, intelligent refining ecosystem** built on these architectural pillars:

1. **Unified Process Data Fabric** -- AVEVA PI System as the single enterprise historian across all sites, feeding a cloud-based analytics layer (Azure Data Explorer) for advanced analytics and digital twins
2. **Integrated Planning-Scheduling-Execution Chain** -- AspenTech suite (PIMS-AO, Aspen Unified, APC) tightly integrated with AVEVA MES for closed-loop planning to execution
3. **Modern ETRM Platform** -- Endur upgraded to current release with cloud-hosted analytics, integrated with SAP S/4HANA for settlement and with real-time market data feeds
4. **Site-Wide MES Standardization** -- AVEVA MES deployed consistently at Lima, Superior, and Toledo for production accounting, yield tracking, and quality release
5. **AI-Enabled Operations** -- Predictive maintenance models on critical rotating equipment, AI-assisted APC tuning, and anomaly detection on process and environmental data
6. **Automated Environmental Compliance** -- Continuous emissions monitoring data flowing automatically to Sphera for EPA/ECCC reporting, with carbon intensity tracking per barrel
7. **Converged OT/IT Security** -- All OT applications aligned with IEC 62443 and integrated with enterprise SOC monitoring

### 3.2 Guiding Principles
1. **OT Reliability First** -- Never compromise process safety or control system availability for enterprise integration goals
2. **Standardize Across Sites** -- Converge on single application platforms per function to reduce support complexity and enable cross-site optimization
3. **Data as a Strategic Asset** -- Expose process and operational data securely to enterprise analytics layers; eliminate manual data transcription
4. **Cloud Where Appropriate** -- Analytics, reporting, and non-real-time workloads migrate to Azure; DCS, SCADA, and safety systems remain on-premise
5. **Vendor Consolidation** -- Prefer extending existing vendor relationships (AspenTech, AVEVA, Honeywell) over introducing new technology stacks
6. **Security by Design** -- Every new downstream application must comply with OT cybersecurity standards (IEC 62443, NIST CSF) from initial design

### 3.3 Target Application Portfolio
| Application | Business Capability | Functional Capability | Change |
|---|---|---|---|
| Honeywell Experion PKS | Refinery Process Control | DCS - All US Refineries | Retain |
| Yokogawa CENTUM VP | Refinery Process Control | DCS - Toledo | Retain (evaluate long-term) |
| AspenTech DMC3 | Advanced Process Control | Next-gen APC | Replace (Profit Controller) |
| AspenTech Aspen HYSYS + Digital Twin | Process Engineering | Simulation & Digital Twin | Enhance |
| AspenTech PIMS-AO | Refinery Planning | LP Planning | Retain |
| AspenTech Aspen Unified PIMS | Refinery Scheduling | Integrated Planning/Scheduling | Enhance |
| AVEVA PI System + PI Cloud | Data Historian | Enterprise Historian + Cloud Analytics | Enhance |
| Honeywell PHD | Data Historian (Legacy) | -- | Retire |
| AVEVA MES | Manufacturing Execution | Site-wide MES (all refineries) | Enhance (expand) |
| Openlink Endur V21+ | Trading & Risk Mgmt | ETRM - Modern Platform | Enhance (major upgrade) |
| SAP S/4HANA (IS-Oil functions) | Logistics & Settlement | Nomination, Scheduling, Settlement | Enhance (migrate from ECC) |
| LabWare LIMS | Lab Information Mgmt | Quality & Sample Mgmt | Retain |
| AspenTech Aspen Blend Optimizer | Blending | Gasoline/Diesel Blending Optimization | New |
| ABB Ability Symphony Plus | Pipeline SCADA | Pipeline Monitoring & Control | Retain |
| Quorum Pipeline Manager | Pipeline Scheduling | Nomination & Scheduling | Retain |
| Sphera SpheraCloud | Environmental Compliance | Emissions & Carbon Tracking | Enhance |
| Intelex EHSQ | EHS Management | Incident, MOC, Inspection Mgmt | Retain |
| Azure Data Explorer + Databricks | Operational Analytics | Predictive Maintenance, AI/ML | New |
| SimSci PRO/II | Process Simulation (Legacy) | -- | Retire |
| Custom VBA/Access Tools | Various | -- | Retire |

## 4. Transition Roadmap

### 4.1 Roadmap Swimlanes

#### Near Term (0-12 months) -- 2026
| Initiative | Description | Dependencies | Status |
|---|---|---|---|
| PHD Historian Retirement | Migrate all Superior historian tags from Honeywell PHD to AVEVA PI System; decommission PHD servers | PI System capacity expansion; OT network readiness | Planned |
| APC Revitalization Phase 1 | Audit all APC controllers across Lima and Superior; re-commission top-10 highest-value applications | Process engineering resource allocation; turnaround windows | Planned |
| SimSci PRO/II Retirement | Migrate remaining Toledo simulation models from PRO/II to Aspen HYSYS; retire PRO/II licenses | Process engineering model validation | Planned |
| Endur ETRM Upgrade Assessment | Complete detailed assessment, vendor scoping, and business case for Endur upgrade from V18 to V21+ | Trading desk availability for requirements gathering | Planned |
| VBA/Access Replacement Phase 1 | Identify and prioritize all custom VBA/Access tools; begin replacement of top-5 critical tools with supported solutions | Business user requirements; solution selection | Planned |
| OT Server OS Upgrades | Upgrade remaining Windows Server 2016 OT application servers to Windows Server 2022 | DCS/application compatibility testing; turnaround scheduling | Planned |
| PI Cloud Connect Pilot | Deploy AVEVA PI Cloud Connect at Lima refinery to stream historian data to Azure for analytics proof of concept | Azure subscription; OT cybersecurity review | Planned |

#### Medium Term (12-24 months) -- 2027
| Initiative | Description | Dependencies | Status |
|---|---|---|---|
| Endur ETRM Major Upgrade | Execute Endur upgrade to V21+ with Oracle 23c migration; implement API integration with SAP | Endur assessment complete; Oracle DBA readiness; SAP integration team | Planned |
| AVEVA MES Expansion - Superior | Deploy AVEVA MES at Superior refinery for production accounting and yield tracking | MES design standards from Lima deployment; Superior site readiness | Planned |
| APC Modernization - DMC3 Pilot | Pilot AspenTech DMC3 next-generation APC on 2-3 units at Lima; evaluate vs. Profit Controller | AspenTech licensing; process engineering capacity | Planned |
| Aspen Blend Optimizer Deployment | Implement Aspen Blend Optimizer for gasoline and diesel blending at Lima and Superior | LIMS integration; quality spec data migration | Planned |
| Digital Twin Phase 1 | Deploy Aspen HYSYS-based digital twin for Lima crude unit and FCC complex | PI System data feed; process model calibration | Planned |
| Predictive Maintenance Pilot | Deploy Azure-based predictive maintenance models for compressors and pumps at Lima | PI Cloud data pipeline; maintenance history from SAP PM | Planned |
| Environmental Data Automation | Automate CEMS data flow from PI System to Sphera for EPA Subpart reporting | PI System tag configuration; Sphera API setup | Planned |

#### Long Term (24-36 months) -- 2028-2029
| Initiative | Description | Dependencies | Status |
|---|---|---|---|
| AVEVA MES Expansion - Toledo | Deploy AVEVA MES at Toledo refinery; achieve site-wide MES standardization | Superior MES deployment lessons learned | Planned |
| DMC3 Full Rollout | Complete migration from Profit Controller to AspenTech DMC3 across all refinery sites | DMC3 pilot results; capital approval | Planned |
| Digital Twin Enterprise Rollout | Expand digital twin capability to all major process units across Lima, Superior, and Toledo | Phase 1 success; model library development | Planned |
| Pipeline Integrity Data Integration | Integrate pipeline integrity data with GIS (Esri ArcGIS) and SAP PM for risk-based inspection planning | GIS platform readiness (Enterprise Applications EA) | Planned |
| Real-time Crude Assay Tracking | Implement wellhead-to-refinery crude quality tracking using inline analyzers and PI System | Upstream Applications EA collaboration; analyzer procurement | Planned |
| AI-Assisted Refinery Optimization | Deploy ML models for refinery-wide optimization leveraging digital twins and real-time data | Digital twin maturity; data science team capacity | Planned |
| SAP S/4HANA IS-Oil Migration | Migrate SAP IS-Oil downstream logistics functions as part of enterprise S/4HANA transformation | Corporate Applications EA S/4HANA program | Planned |

### 4.2 Key Milestones
| Milestone | Target Date | Dependencies |
|---|---|---|
| PHD Historian fully decommissioned | Q3 2026 | PI System migration complete |
| Endur upgrade business case approved | Q4 2026 | Assessment and vendor negotiations |
| All legacy VBA/Access tools retired | Q4 2027 | Replacement solutions deployed |
| Endur V21+ in production | Q2 2027 | Upgrade execution and UAT |
| AVEVA MES operational at all 3 US refineries | Q4 2028 | Phased MES rollout |
| APC fully modernized to DMC3 | Q2 2029 | Site-by-site migration |
| Digital twin operational for all major process units | Q4 2029 | Model development and calibration |

### 4.3 Application Rationalization Plan
| Application | Action | Target Date | Savings |
|---|---|---|---|
| Honeywell PHD | Retire | Q3 2026 | $150K/yr maintenance + support |
| SimSci PRO/II | Retire | Q2 2026 | $80K/yr license costs |
| Custom VBA/Access tools (est. 25+) | Retire | Q4 2027 | Risk reduction; $200K/yr labour |
| Honeywell Profit Controller | Replace (with DMC3) | Q2 2029 | Net neutral (modern platform) |
| Multiple point-solution spreadsheets | Consolidate into MES/BI | Q4 2028 | $100K/yr labour savings |

## 5. Investment Summary
| Initiative | CapEx | OpEx (Annual) | Priority | Year |
|---|---|---|---|---|
| PHD to PI System Migration | $400K | $0 (absorbed into existing PI) | Critical | 2026 |
| APC Revitalization Phase 1 | $600K | $50K | High | 2026 |
| SimSci PRO/II Retirement | $100K | -$80K (savings) | High | 2026 |
| OT Server OS Upgrades | $350K | $0 | High | 2026 |
| PI Cloud Connect Pilot | $200K | $120K | Medium | 2026 |
| Endur V21+ Upgrade (incl. Oracle) | $3.5M | $200K net increase | Critical | 2027 |
| AVEVA MES Expansion (Superior) | $1.8M | $250K | High | 2027 |
| DMC3 APC Pilot | $500K | $100K | High | 2027 |
| Aspen Blend Optimizer | $800K | $150K | High | 2027 |
| Digital Twin Phase 1 | $1.2M | $180K | Medium | 2027 |
| Predictive Maintenance Pilot | $400K | $200K (Azure) | Medium | 2027 |
| AVEVA MES Expansion (Toledo) | $1.5M | $250K | High | 2028 |
| DMC3 Full Rollout | $2.0M | $300K | High | 2028-2029 |
| Digital Twin Enterprise Rollout | $2.5M | $350K | Medium | 2028-2029 |
| **Total Estimated** | **$15.85M** | **$2.07M incremental** | | **2026-2029** |

## 6. Risks & Dependencies
| Risk/Dependency | Type | Likelihood | Impact | Mitigation |
|---|---|---|---|---|
| Turnaround schedule conflicts with OT upgrades | Risk | High | High | Align all OT work with planned turnaround windows; maintain hot-standby approaches |
| AspenTech licensing cost escalation | Risk | Medium | High | Negotiate enterprise license agreement; evaluate competitive alternatives as leverage |
| OT cybersecurity incident during system migration | Risk | Low | Critical | Follow IEC 62443 change management; staged rollouts with rollback plans |
| Insufficient OT/IT integration resources | Risk | High | Medium | Cross-train IT staff on OT systems; engage system integrator partners |
| Endur upgrade complexity (data migration, customizations) | Risk | Medium | High | Engage Openlink professional services; comprehensive UAT with trading desk |
| SAP S/4HANA migration timeline shifts | Dependency | Medium | Medium | Design Endur integration with abstraction layer to support both ECC and S/4HANA |
| AVEVA PI Cloud data sovereignty/residency requirements | Risk | Low | Medium | Confirm Azure Canada region compliance; engage Legal and Cybersecurity |
| Upstream Applications crude quality data availability | Dependency | Medium | Medium | Coordinate with Upstream EA on wellhead analyzer and data standards |
| OT vendor (Honeywell/Yokogawa) resource availability | Risk | Medium | Medium | Book vendor resources early; maintain internal DCS competencies |
| Regulatory changes to emissions reporting requirements | Risk | Medium | Medium | Maintain flexible Sphera configuration; monitor EPA and ECCC regulatory pipeline |

## 7. Governance & Review
- Roadmap review frequency: Quarterly
- Next review date: 2026-05-15
- Approval authority: Team Leader + IT Senior Leadership
- Change management: All roadmap changes above $500K require ARB review
- Stakeholder review: Bi-annual review with VP Refining Operations and VP Marketing & Trading
- OT change advisory: All DCS/SCADA changes reviewed by OT Change Advisory Board

## 8. Appendices

### Appendix A: Capability Map Summary
```
Downstream Business Capabilities
|
+-- Crude Acquisition & Logistics
|   +-- Crude Marketing & Purchasing
|   +-- Pipeline Nomination & Scheduling
|   +-- Crude Receipt & Inventory
|
+-- Refining & Upgrading Operations
|   +-- Process Control (DCS/APC)
|   +-- Process Simulation & Engineering
|   +-- Refinery Planning (LP)
|   +-- Production Scheduling
|   +-- Manufacturing Execution
|   +-- Yield & Loss Accounting
|
+-- Product Quality & Blending
|   +-- Laboratory Analysis (LIMS)
|   +-- Blending Optimization
|   +-- Product Certification
|
+-- Product Marketing & Trading
|   +-- Product Trading (ETRM)
|   +-- Risk Management
|   +-- Contract Management
|   +-- Settlement & Invoicing
|
+-- Environmental & Compliance
|   +-- Emissions Monitoring (CEMS)
|   +-- Regulatory Reporting
|   +-- Carbon Management
|   +-- EHS Incident Management
|
+-- Operational Intelligence
|   +-- Process Data Historian
|   +-- Operational Analytics & Reporting
|   +-- Predictive Maintenance
|   +-- Digital Twins
```

### Appendix B: Integration Architecture (Conceptual)
```
                    Enterprise Zone (IT)
    +---------------------------------------------------+
    | SAP ECC/S4HANA | Endur ETRM | BI/Analytics | Azure |
    +---------------------------------------------------+
                        |  APIs / Middleware
    +---------------------------------------------------+
    |              Enterprise DMZ / PI Cloud             |
    +---------------------------------------------------+
                        |  OT/IT Gateway
    +---------------------------------------------------+
    |                   OT DMZ (Level 3.5)               |
    | PI System | MES | LIMS | Planning/Scheduling       |
    +---------------------------------------------------+
                        |  OPC / Historian
    +---------------------------------------------------+
    |              Site Operations (Level 3)             |
    | Historian Servers | Engineering Workstations        |
    +---------------------------------------------------+
                        |  Control Network
    +---------------------------------------------------+
    |          Process Control (Level 2/1/0)             |
    | DCS | APC | SIS | SCADA | Field Instruments        |
    +---------------------------------------------------+
```

### Appendix C: Vendor Landscape
| Vendor | Products in Use | Relationship Status | Contract Renewal |
|---|---|---|---|
| AspenTech | HYSYS, PIMS-AO, Orion, DMC3 (future) | Strategic Partner | 2027 (enterprise agreement) |
| AVEVA (Schneider) | PI System, MES | Strategic Partner | 2028 |
| Honeywell | Experion PKS, Profit Controller, PHD | Strategic Partner (DCS) | Ongoing (per-site) |
| Yokogawa | CENTUM VP | Tactical (Toledo only) | 2029 |
| ION/Openlink | Endur ETRM | Key Vendor | 2027 |
| LabWare | LIMS | Key Vendor | 2029 |
| ABB | Symphony Plus SCADA | Key Vendor | 2030 |
| Sphera | SpheraCloud | SaaS Vendor | Annual renewal |
| Intelex | EHSQ Platform | SaaS Vendor | Annual renewal |
| Quorum (now Tieto) | Pipeline Manager | Tactical Vendor | 2027 |
