# Enterprise Architecture Roadmap

**Domain:** Upstream Applications
**Portfolio Architect:** Upstream Applications EA
**Version:** 1.0
**Last Updated:** 2026-02-07
**Planning Horizon:** 2026 - 2029

---

## 1. Domain Overview

### 1.1 Scope & Boundaries
The Upstream Applications domain covers all technology solutions supporting Cenovus Energy's upstream oil and gas operations, spanning:
- **Drilling & Completions** - Well planning, directional drilling, completions design, well cost tracking, and drilling performance analytics
- **Production Operations** - Production surveillance and optimization, artificial lift management, facility operations, and production accounting
- **Reservoir Management** - Reservoir simulation, decline curve analysis, reserves estimation, geological and geophysical (G&G) interpretation
- **Field Data Capture** - SCADA systems, PI historian data infrastructure, field mobility applications, and IoT sensor networks
- **Well Lifecycle Management** - Well integrity tracking, regulatory compliance reporting, well abandonment planning and execution
- **Oil Sands Operations** - SAGD (Steam-Assisted Gravity Drainage) optimization at Foster Creek and Christina Lake, steam-oil ratio (SOR) management, CSS (Cyclic Steam Stimulation) operations, and surface mining support at legacy assets

This domain interfaces with IT Infrastructure (for SCADA/OT network convergence), Cyber Security (for OT security posture), AI/ML (for production optimization models), and Enterprise Applications (for integration with SAP and enterprise reporting).

### 1.2 Strategic Alignment
This domain directly supports the following Cenovus Energy corporate strategic priorities:
- **Operational Excellence** - Reduce operating costs per barrel through production optimization, predictive maintenance, and automated surveillance
- **Safe & Reliable Operations** - Improve well integrity management and process safety through real-time monitoring and automated alarming
- **Sustainability & ESG** - Enable emissions monitoring, steam efficiency optimization, and regulatory compliance reporting for GHG reduction targets
- **Digital Transformation** - Modernize legacy subsurface and production workflows with cloud-enabled analytics, mobile field operations, and AI-assisted decision support
- **Portfolio Optimization** - Provide integrated data platforms that enable rapid asset evaluation, development planning, and capital allocation decisions

**EA Team Goals 2026 Alignment:**
This roadmap addresses the following domain-specific goals from the EA Team Goals 2026:
- **U-1:** Publish Upstream Applications domain roadmap (drilling, completions, production, reservoir) - Target Q2
- **U-2:** Complete application-to-capability mapping for upstream domain - Target Q2
- **U-3:** Assess field data capture architecture and edge computing opportunities - Target Q3
- **U-4:** Define integration architecture between upstream apps and enterprise platforms - Target Q3
- **U-5:** Identify AI/ML opportunities in production optimization and reservoir modelling - Target Q3

This roadmap also contributes to the following cross-domain initiatives:
- **Initiative A: IT/OT Convergence Architecture** (with Infrastructure, Cyber Security, Downstream Apps) - SCADA/OT modernization, IEC 62443 compliance, OPC UA migration (Section 4.1, SCADA initiatives)
- **Initiative C: AI-Enabled Operations** (with AI, Downstream Apps, Enterprise Apps) - Production optimization PoC, SAGD digital twin, autonomous well control (Section 4.1, Production Optimization and SAGD Digital Twin initiatives)
- **Initiative D: Enterprise Integration Modernization** (with Enterprise Apps, Cloud, Corporate Apps, Downstream Apps) - Azure Data Factory deployment, PPDM data models (Section 4.1, Unified Data Integration Layer)

**Objective 4 (Application Rationalization):** This roadmap identifies 7 rationalization actions (Section 4.3) contributing to the KR4.3 target of 10% reduction in redundant application count.

### 1.3 Key Stakeholders
| Stakeholder | Role | Business Unit |
|-------------|------|---------------|
| VP, Thermal Operations | Executive Sponsor | Oil Sands Operations |
| VP, Conventional & Offshore | Executive Sponsor | Conventional & Offshore |
| Director, Drilling & Completions | Business Lead | Well Delivery |
| Director, Production Engineering | Business Lead | Production Operations |
| Director, Reservoir Engineering | Business Lead | Subsurface |
| Director, Geoscience | Business Lead | Subsurface |
| Manager, Production Surveillance | Key User | Production Operations |
| Manager, SCADA & Instrumentation | Key User / OT Lead | Field Operations |
| Manager, IT Delivery (Upstream) | IT Delivery Partner | IT |
| IT Security Architect | Cross-Domain Partner | IT Cyber Security |
| AI/ML Portfolio Architect | Cross-Domain Partner | IT AI/ML |

## 2. Current State Assessment

### 2.1 Application Portfolio
| Application | Business Capability | Functional Capability | Status | Health |
|-------------|--------------------|-----------------------|--------|--------|
| Petrel (Schlumberger) | Reservoir Characterization | Geological & geophysical modelling, seismic interpretation | Production | Green |
| INTERSECT / Eclipse (SLB) | Reservoir Simulation | Thermal reservoir simulation (SAGD/CSS), history matching | Production | Yellow |
| OFM (SLB) | Production Surveillance | Decline curve analysis, production data management, forecasting | Production | Yellow |
| Avocet (SLB) | Production Operations | Production accounting, well allocation, field data validation | Production | Yellow |
| Prosper / GAP / MBAL (Petroleum Experts) | Well & Network Modelling | Well performance modelling, nodal analysis, network optimization | Production | Green |
| WellView (Peloton / Pason) | Drilling Operations | Daily drilling reports, well cost tracking, time-depth analysis | Production | Green |
| OpenWells (SLB) | Completions Design | Completions program design, equipment tracking, post-job analysis | Production | Yellow |
| PI System (OSIsoft / AVEVA) | Real-Time Data | Historian, real-time data infrastructure, sensor data management | Production | Green |
| PI Vision / PI AF | Operations Dashboards | Real-time visualization, asset framework, KPI dashboards | Production | Green |
| Spotfire (TIBCO) | Analytics & Visualization | Production analytics, ad-hoc reporting, engineering dashboards | Production | Green |
| AccuMap / geoSCOUT | Land & Well Data | Well data retrieval, mapping, regulatory well data | Production | Yellow |
| IHS Harmony (S&P) | Reserves Estimation | Decline curve analysis, reserves booking, type curve generation | Production | Green |
| SAP PM / EAM | Maintenance Management | Preventive maintenance scheduling, work order management | Production | Green |
| Matrikon OPC (Honeywell) | SCADA Integration | OPC data aggregation, SCADA to PI connectivity | Production | Yellow |
| Field Mobility (Custom) | Field Data Capture | Mobile well site inspections, field readings, safety observations | Production | Red |
| GHG Emissions Tracker (Custom) | Environmental Reporting | Fugitive emissions tracking, regulatory GHG reporting | Production | Yellow |
| Well Integrity (Custom/Excel) | Well Integrity Management | Casing inspection records, annular pressure tracking, risk ranking | Production | Red |

### 2.2 Technology Stack
| Layer | Technology | Version | End of Support |
|-------|-----------|---------|----------------|
| Reservoir Simulation | Eclipse / INTERSECT | 2023.1 | Ongoing (license renewal) |
| G&G Platform | Petrel | 2023.2 | Ongoing |
| Production Data | OFM | 2022.2 | 2026 Q4 (migration needed) |
| Historian | PI System (AVEVA) | 2023 R2 | Ongoing |
| SCADA RTU | Allen-Bradley, ABB | Various | Mixed - some EOL |
| Database Layer | Oracle 19c, SQL Server 2019 | Various | Oracle 19c: 2027-04, SQL 2019: 2030-01 |
| Integration | OSIsoft PI Connectors, Matrikon OPC | Various | Ongoing |
| Visualization | Spotfire 12.x | 12.5 | 2027 |
| Field Mobility | Xamarin-based custom app | 1.8 | EOL (Xamarin sunset by Microsoft) |
| Desktop OS (Engineering) | Windows 11 | 23H2 | Ongoing |

### 2.3 Strengths
- Mature PI System historian deployment with high-fidelity real-time data across thermal and conventional assets
- Strong Petrel/Eclipse subsurface modelling capability with experienced G&G and reservoir engineering teams
- Well-established SLB toolset integration (Petrel-Eclipse-OFM) providing end-to-end subsurface workflows
- Production accounting workflows in Avocet are standardized across all business units
- Spotfire analytics platform provides flexible self-service analytics for engineering teams
- PI AF asset framework is well-structured, enabling consistent KPI calculation across facilities

### 2.4 Gaps & Pain Points
| # | Gap | Business Impact | Priority |
|---|-----|-----------------|----------|
| 1 | Well integrity management relies on Excel spreadsheets and disconnected records | Risk of regulatory non-compliance (AER Directive 036); inability to proactively identify well integrity risks across the portfolio | Critical |
| 2 | Field mobility app built on Xamarin is end-of-life; poor offline capability | Field operators revert to paper-based data capture; delayed data entry into systems of record | High |
| 3 | OFM version is aging; no cloud deployment; limited SAGD analytics capability | Production engineers spend excessive time on manual data preparation; poor SOR trending at scale | High |
| 4 | No integrated production optimization platform linking PI data, well models, and facility constraints | Sub-optimal artificial lift settings, reactive rather than proactive production management | High |
| 5 | SCADA infrastructure has mixed-age RTUs with inconsistent cybersecurity posture | OT security vulnerabilities; potential for unmonitored access to field control systems | High |
| 6 | Siloed data across drilling (WellView), completions (OpenWells), and production (Avocet/OFM) | No single well lifecycle view; engineers manually correlate data across multiple systems | Medium |
| 7 | GHG emissions tracking tool is custom-built with limited auditability | Risk of misreporting under federal Output-Based Pricing System; manual data reconciliation | Medium |
| 8 | Limited adoption of cloud for subsurface computing workloads | Long queue times for reservoir simulation runs; scaling limited to on-premises HPC capacity | Medium |

### 2.5 Technical Debt
| Item | Risk | Effort to Remediate | Priority |
|------|------|---------------------|----------|
| Excel-based well integrity tracking | Regulatory non-compliance, data loss | High - requires new application procurement and data migration | Critical |
| Xamarin field mobility app (EOL framework) | No vendor support, security patches unavailable | High - full rewrite required on modern framework (.NET MAUI or PWA) | High |
| Legacy OFM on-premises deployment | Growing maintenance burden, limited scalability | Medium - migration to SLB cloud or replacement with modern surveillance platform | High |
| Oracle 19c databases approaching EOL (Apr 2027) | Unsupported database platform | Medium - upgrade to Oracle 23c or migrate to SQL Server / cloud-managed DB | Medium |
| Aging SCADA RTUs (pre-2015 vintage) | Cybersecurity vulnerabilities, no encryption support | High - phased hardware refresh across 200+ well pads | Medium |
| Custom Python scripts for production data ETL | Undocumented, single-person dependency | Low - refactor into managed integration platform (e.g., Azure Data Factory) | Medium |
| Matrikon OPC servers on Windows Server 2016 | OS approaching extended support end | Low - OS upgrade and OPC UA migration | Low |

## 3. Future State Vision

### 3.1 Target Architecture
The target architecture for Upstream Applications is a **cloud-enabled, data-centric platform** that provides:

1. **Unified Well Lifecycle Platform** - A single source of truth for well data from planning through drilling, completions, production, and abandonment, replacing siloed systems with an integrated data backbone.

2. **Real-Time Production Optimization** - Closed-loop optimization connecting PI historian data, well and network models (Prosper/GAP), and AI/ML-driven recommendations to maximize production while minimizing steam consumption (SOR) and operating costs.

3. **Cloud-Enabled Subsurface Computing** - Petrel and reservoir simulation workloads running on cloud HPC (Azure HPC or AWS), enabling elastic scaling for simulation campaigns and reducing on-premises infrastructure.

4. **Modern Field Mobility** - Progressive Web App (PWA) or .NET MAUI-based field application with robust offline-first capability, replacing the legacy Xamarin app, integrated with PI System and SAP PM for seamless field-to-office data flow.

5. **Digital Well Integrity Management** - Purpose-built well integrity management system (e.g., Sword Perform, Xodus WIMS, or SLB eWIM) replacing spreadsheet-based tracking, with automated risk ranking and AER Directive 036 compliance reporting.

6. **Emissions Intelligence** - Integrated emissions monitoring connecting SCADA/PI data to an auditable GHG reporting platform, supporting continuous emissions monitoring (CEM) and methane detection programs.

7. **Hardened OT/IT Convergence** - SCADA infrastructure modernized to OPC UA standards with IEC 62443-compliant security zones, segmented networks, and encrypted communications.

### 3.2 Guiding Principles
1. **Data as an Asset** - Upstream data (well, production, reservoir) must be treated as a strategic asset with clear ownership, quality standards, and governed access
2. **Cloud-First for Compute, Hybrid for Control** - Analytical and simulation workloads migrate to cloud; real-time control (SCADA) remains on-premises with secure hybrid connectivity
3. **Vendor Consolidation** - Prefer extending existing strategic vendor platforms (SLB, AVEVA/OSIsoft, Petroleum Experts) over introducing new vendors to reduce integration complexity
4. **Interoperability via Standards** - Use PPDM, WITSML, PRODML, and OPC UA standards to ensure data portability and reduce vendor lock-in
5. **Security by Design** - All new upstream applications must meet IEC 62443 (OT) and Cenovus cybersecurity standards; no direct SCADA-to-internet connectivity
6. **Mobile-First Field Operations** - Field data capture must work offline with automatic synchronization; reduce paper-based processes to zero

### 3.3 Target Application Portfolio
| Application | Business Capability | Functional Capability | Change |
|-------------|--------------------|-----------------------|--------|
| Petrel (SLB Cloud) | Reservoir Characterization | G&G modelling with cloud HPC burst | Enhance |
| INTERSECT (SLB Cloud) | Reservoir Simulation | Thermal simulation with elastic cloud compute | Enhance |
| Delfi / SLB Digital Platform | Production Surveillance | Cloud-native production data management, replacing OFM | Replace (OFM) |
| Avocet | Production Accounting | Production accounting and allocation | Retain |
| Prosper / GAP / MBAL | Well & Network Modelling | Well performance and network optimization | Retain |
| WellView (Pason) | Drilling Operations | Drilling operations and well cost management | Retain |
| OpenWells (SLB) | Completions Design | Completions design and job records | Retain |
| PI System (AVEVA) | Real-Time Data | Historian and real-time data platform | Retain |
| PI Vision / AVEVA Insight | Operations Dashboards | Cloud-hybrid visualization and analytics | Enhance |
| Spotfire / Power BI | Analytics & Visualization | Engineering analytics (Spotfire retained; Power BI for enterprise reporting) | Retain + New |
| Well Integrity System (TBD) | Well Integrity Management | Digital well integrity, risk ranking, compliance reporting | New |
| Field Mobility App (PWA/.NET MAUI) | Field Data Capture | Offline-capable mobile inspections, readings, safety | Replace (Xamarin) |
| GHG Reporting Platform (TBD) | Environmental Reporting | Auditable emissions tracking, CEM integration | Replace (Custom) |
| IHS Harmony (S&P) | Reserves Estimation | Decline curve analysis, reserves booking | Retain |
| Azure Data Factory / Integration | Data Integration | Managed ETL replacing custom Python scripts | New |
| geoSCOUT | Land & Well Data | Well data retrieval and mapping | Retain (evaluate consolidation with Petrel) |

## 4. Transition Roadmap

### 4.1 Roadmap Swimlanes

#### Near Term (0-12 months: 2026)
| Initiative | Description | Dependencies | Status |
|-----------|-------------|--------------|--------|
| Well Integrity System Selection | RFP and vendor evaluation for digital well integrity management system (Sword Perform, Xodus, SLB eWIM) | None | Planned |
| Field Mobility App Replacement - Phase 1 | Develop PWA-based field mobility app with offline sync; pilot at Foster Creek SAGD operations | IT Cloud (Azure infrastructure), Cyber Security review | Planned |
| OFM to Delfi Migration Assessment | Evaluate SLB Delfi platform as cloud-native replacement for OFM; conduct proof-of-concept with Christina Lake production data | SLB engagement, IT Cloud (connectivity) | Planned |
| SCADA Cybersecurity Assessment | Conduct IEC 62443 gap assessment across all SCADA/OT infrastructure; develop remediation roadmap | IT Cyber Security, OT team | Planned |
| PI System Upgrade to 2025 R1 | Upgrade PI Data Archive and PI AF to latest AVEVA release; enable cloud-hybrid features (AVEVA Data Hub) | IT Infrastructure (server provisioning) | Planned |
| Oracle 19c Upgrade Planning | Assess Oracle database instances supporting upstream apps; plan migration to Oracle 23c or Azure SQL Managed Instance | IT Infrastructure, IT Cloud | Planned |
| Production Optimization PoC | Pilot AI/ML-based production optimization on 50 SAGD well pairs at Foster Creek using PI data + Prosper models | IT AI/ML team, PI System data access | Planned |

#### Medium Term (12-24 months: 2027)
| Initiative | Description | Dependencies | Status |
|-----------|-------------|--------------|--------|
| Well Integrity System Implementation | Deploy selected well integrity platform; migrate historical data from Excel/Access databases; integrate with PI System for annular pressure monitoring | Well Integrity System Selection (Near Term) | Planned |
| Field Mobility App Rollout | Roll out PWA field app across all Cenovus upstream assets (thermal, conventional, offshore) | Field Mobility Phase 1 pilot success | Planned |
| OFM Replacement / Delfi Deployment | Migrate production surveillance workflows from OFM to SLB Delfi or equivalent cloud platform | OFM assessment (Near Term), SLB contract | Planned |
| SCADA RTU Refresh - Phase 1 | Replace pre-2015 RTUs at highest-risk facilities with IEC 62443-compliant hardware; deploy OPC UA | SCADA assessment (Near Term), CapEx approval | Planned |
| Cloud HPC for Reservoir Simulation | Enable Petrel and INTERSECT workloads on Azure HPC or AWS for elastic burst computing; reduce on-prem HPC dependency | IT Cloud (Azure/AWS infrastructure) | Planned |
| GHG Reporting Platform Selection & Implementation | Replace custom emissions tracker with commercial platform (e.g., Envizi, Persefoni, or FigBytes); integrate PI data for CEM | ESG team requirements, PI System data | Planned |
| Unified Data Integration Layer | Implement Azure Data Factory for managed ETL pipelines replacing custom Python scripts; establish PPDM-aligned data models | IT Cloud, Enterprise Applications (MDM) | Planned |

#### Long Term (24-36 months: 2028-2029)
| Initiative | Description | Dependencies | Status |
|-----------|-------------|--------------|--------|
| Integrated Production Optimization Platform | Scale AI/ML production optimization across all SAGD and conventional assets; closed-loop with PI System and artificial lift controllers | Production Optimization PoC, AI/ML maturity | Planned |
| SCADA RTU Refresh - Phase 2 | Complete RTU refresh across remaining well pads and facilities; full OPC UA deployment | Phase 1 completion, CapEx | Planned |
| Well Lifecycle Data Platform | Implement unified well data backbone connecting WellView, OpenWells, Avocet, and well integrity system via common data model | Individual system modernizations | Planned |
| Petrel Cloud Migration | Full migration of Petrel workflows to SLB cloud platform; retire on-premises Petrel servers | Cloud HPC deployment, SLB roadmap | Planned |
| Advanced SAGD Digital Twin | Develop comprehensive digital twin for SAGD operations integrating reservoir simulation, surface facility models, and real-time PI data | Multiple upstream system integrations | Planned |
| Autonomous Well Control Pilot | Pilot autonomous artificial lift optimization using edge computing at well sites with AI-driven setpoint adjustments | Production optimization platform, OT security | Planned |

### 4.2 Key Milestones
| Milestone | Target Date | Dependencies |
|-----------|-------------|--------------|
| Well integrity vendor selected | 2026 Q2 | RFP process |
| Field mobility PWA pilot complete at Foster Creek | 2026 Q3 | Development sprint completion |
| SCADA IEC 62443 gap assessment delivered | 2026 Q2 | Cyber Security team availability |
| OFM replacement decision (Delfi vs. alternative) | 2026 Q4 | PoC evaluation |
| Production optimization PoC results reviewed | 2026 Q4 | AI/ML team, PI data access |
| Well integrity system go-live (Phase 1) | 2027 Q2 | Vendor implementation |
| Field mobility app deployed enterprise-wide | 2027 Q3 | Pilot validation |
| Cloud HPC operational for reservoir simulation | 2027 Q2 | IT Cloud infrastructure |
| OFM fully retired | 2027 Q4 | Delfi/replacement stable |
| GHG reporting platform operational | 2027 Q3 | ESG requirements finalized |
| SCADA RTU refresh Phase 1 complete | 2027 Q4 | CapEx, procurement |
| Integrated production optimization at scale | 2028 Q4 | Platform maturity |
| SAGD digital twin operational | 2029 Q2 | Multi-system integration |

### 4.3 Application Rationalization Plan
| Application | Action | Target Date | Savings |
|-------------|--------|-------------|---------|
| OFM (SLB) | Retire - replace with Delfi cloud platform | 2027 Q4 | ~$200K/yr license + server maintenance |
| Field Mobility (Xamarin custom) | Retire - replace with PWA/MAUI app | 2027 Q3 | Reduced development maintenance + improved data quality |
| Well Integrity (Excel/Access) | Retire - replace with commercial WIMS | 2027 Q2 | Risk reduction (regulatory); quantified savings TBD |
| GHG Emissions Tracker (Custom) | Retire - replace with commercial platform | 2027 Q3 | Reduced audit risk + maintenance effort |
| Custom Python ETL scripts | Retire - replace with Azure Data Factory | 2027 Q4 | Reduced single-person dependency risk |
| AccuMap | Evaluate consolidation with geoSCOUT | 2027 Q2 | ~$150K/yr if consolidated to single platform |
| Matrikon OPC (legacy servers) | Modernize - migrate to OPC UA | 2028 Q2 | Reduced OT security risk |

## 5. Investment Summary
| Initiative | CapEx | OpEx (Annual) | Priority | Year |
|-----------|-------|---------------|----------|------|
| Well Integrity System | $800K | $150K | Critical | 2026-2027 |
| Field Mobility App Replacement | $500K | $80K | High | 2026-2027 |
| OFM to Delfi Migration | $400K | $250K (net increase for cloud SaaS) | High | 2026-2027 |
| SCADA Cybersecurity Assessment | $200K | - | High | 2026 |
| SCADA RTU Refresh (Phase 1 + 2) | $3.5M | $100K | High | 2027-2028 |
| PI System Upgrade | $150K | - | Medium | 2026 |
| Production Optimization PoC | $300K | $50K | High | 2026 |
| Cloud HPC for Simulation | $250K | $400K (cloud consumption) | Medium | 2027 |
| GHG Reporting Platform | $350K | $120K | Medium | 2027 |
| Data Integration Layer (ADF) | $200K | $80K | Medium | 2027 |
| Production Optimization at Scale | $600K | $200K | High | 2028 |
| SAGD Digital Twin | $1.2M | $300K | Medium | 2028-2029 |
| **Total Estimated** | **~$8.5M** | **~$1.7M** | | 2026-2029 |

## 6. Risks & Dependencies
| Risk/Dependency | Type | Likelihood | Impact | Mitigation |
|-----------------|------|-----------|--------|------------|
| SLB Delfi platform maturity for SAGD-specific workflows | Risk | Medium | High | Conduct thorough PoC with Christina Lake data before committing; maintain OFM fallback |
| SCADA RTU refresh delays due to supply chain constraints | Risk | Medium | Medium | Early procurement engagement; maintain legacy RTU spare parts inventory |
| OT security incident during modernization transition | Risk | Low | Critical | Phased deployment with rollback capability; IEC 62443 security zones maintained throughout |
| IT Cloud team capacity constraints for upstream workloads | Dependency | Medium | High | Early alignment with Cloud EA roadmap; dedicated cloud landing zone for upstream |
| AI/ML team availability for production optimization PoC | Dependency | Medium | Medium | Secure dedicated data scientist allocation; consider external partner for PoC |
| SLB contract renewal and commercial terms for cloud transition | Dependency | Low | High | Engage procurement early; negotiate cloud migration incentives in contract renewal |
| Budget constraints in low commodity price environment | Risk | Medium | High | Prioritize highest-ROI initiatives (well integrity for compliance, production optimization for revenue); defer discretionary spend |
| Change management resistance from field operations staff | Risk | Medium | Medium | Involve field operators in design; pilot approach with champion sites; demonstrate tangible time savings |
| Oracle 19c EOL (April 2027) database migration complexity | Risk | Low | Medium | Begin assessment in 2026 Q2; test application compatibility with target database platform |
| Regulatory changes (AER, ECCC) requiring system modifications | Risk | Low | Medium | Modular system design; maintain vendor relationships for regulatory update support |

## 7. Governance & Review
- Roadmap review frequency: Quarterly
- Next review date: 2026 Q2 (April 2026)
- Approval authority: Team Leader + IT Senior Leadership
- Architecture Review Board (ARB): All new application procurements and major enhancements require ARB approval
- Stakeholder review: Semi-annual review with VP Thermal Operations and VP Conventional & Offshore
- Change control: Roadmap changes requiring >$500K CapEx or new vendor introduction escalated to IT Senior Leadership

## 8. Appendices

### A. Capability Map - Upstream Applications

```
Upstream Applications Capability Map
=====================================

SUBSURFACE                    WELL DELIVERY                 PRODUCTION OPERATIONS
+-----------------------+    +-----------------------+    +-----------------------+
| Geological Modelling  |    | Well Planning         |    | Production Surveillance|
| (Petrel)              |    | (WellView)            |    | (OFM -> Delfi)        |
+-----------------------+    +-----------------------+    +-----------------------+
| Geophysical Interp.   |    | Drilling Operations   |    | Production Accounting |
| (Petrel)              |    | (WellView)            |    | (Avocet)              |
+-----------------------+    +-----------------------+    +-----------------------+
| Reservoir Simulation  |    | Completions Design    |    | Artificial Lift Opt.  |
| (Eclipse/INTERSECT)   |    | (OpenWells)           |    | (Prosper/GAP)         |
+-----------------------+    +-----------------------+    +-----------------------+
| Reserves Estimation   |    | Well Cost Tracking    |    | Facility Management   |
| (IHS Harmony)         |    | (WellView/SAP)        |    | (PI System/SAP PM)    |
+-----------------------+    +-----------------------+    +-----------------------+
| Decline Curve Analysis|    | Well Integrity Mgmt   |    | SAGD/SOR Optimization |
| (IHS Harmony/OFM)     |    | (New WIMS)            |    | (PI + ML Platform)    |
+-----------------------+    +-----------------------+    +-----------------------+

FIELD DATA & INTEGRATION      ANALYTICS & REPORTING         ENVIRONMENTAL
+-----------------------+    +-----------------------+    +-----------------------+
| SCADA / RTU           |    | Engineering Analytics  |    | GHG Emissions Tracking|
| (Allen-Bradley/ABB)   |    | (Spotfire)            |    | (New Platform)        |
+-----------------------+    +-----------------------+    +-----------------------+
| Historian / Real-Time |    | Enterprise Reporting  |    | Regulatory Reporting  |
| (PI System)           |    | (Power BI / Spotfire) |    | (AER Compliance)      |
+-----------------------+    +-----------------------+    +-----------------------+
| Field Mobility        |    | Well & Land Data      |    | Methane Detection     |
| (New PWA App)         |    | (geoSCOUT)            |    | (IoT + PI)            |
+-----------------------+    +-----------------------+    +-----------------------+
| OPC / Integration     |    | Dashboards            |    |                       |
| (OPC UA / ADF)        |    | (PI Vision)           |    |                       |
+-----------------------+    +-----------------------+    +-----------------------+
```

### B. Vendor Landscape Summary

| Vendor | Products | Relationship | Contract Renewal |
|--------|----------|-------------|-----------------|
| SLB (Schlumberger) | Petrel, Eclipse, INTERSECT, OFM, OpenWells, Delfi, Avocet | Strategic | 2027 (multi-year ELA) |
| Petroleum Experts (Petex) | Prosper, GAP, MBAL | Strategic | 2026 Q4 |
| AVEVA (Schneider Electric) | PI System, PI Vision, PI AF, AVEVA Data Hub | Strategic | 2027 |
| Pason Systems | WellView | Tactical | 2026 |
| S&P Global | IHS Harmony, geoSCOUT | Strategic | 2027 |
| TIBCO | Spotfire | Tactical (evaluate vs Power BI) | 2026 |
| Honeywell | Matrikon OPC | Tactical | Annual |
| Microsoft | Azure (cloud), Power BI, .NET MAUI | Strategic (via enterprise agreement) | EA renewal cycle |

### C. Integration Architecture (Key Data Flows)

```
SCADA/RTU (Field)
      |
      v (OPC UA)
PI System (Historian)
      |
      +---> PI Vision (Real-Time Dashboards)
      +---> Spotfire / Power BI (Analytics)
      +---> Production Optimization (AI/ML)
      +---> Avocet (Production Accounting)
      |
WellView/OpenWells ---> Well Lifecycle Data Platform ---> Reserves (Harmony)
      |
Petrel/Eclipse <---> Cloud HPC (Azure/AWS)
      |
All Systems ---> Azure Data Factory ---> Enterprise Data Lake ---> SAP / Corporate Reporting
```
