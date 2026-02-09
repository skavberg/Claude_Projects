# Enterprise Architecture Roadmap

**Domain:** Enterprise Applications (Integration, MDM, BI/Reporting, GIS, Document Management)
**Portfolio Architect:** Enterprise Applications Portfolio Architect
**Version:** 1.0
**Last Updated:** 2026-02-07
**Planning Horizon:** 2026 - 2029

---

## 1. Domain Overview

### 1.1 Scope & Boundaries
The Enterprise Applications domain spans the cross-cutting platforms and services that enable data flow, data quality, analytics, geospatial intelligence, and document management across Cenovus Energy. This domain does not own individual business applications (those belong to Corporate, Upstream, and Downstream domains) but owns the integration fabric, master data layer, enterprise reporting ecosystem, geospatial platforms, and document/knowledge management that connect them.

**In Scope:**
- Integration platforms (iPaaS, API management, ESB, event brokers)
- Master Data Management (materials, vendors, customers, wells, facilities, cost centres)
- Enterprise Reporting & Business Intelligence (Power BI, data warehouse, data lake analytics)
- GIS & Geospatial (ArcGIS, well/pipeline mapping, land management, spatial analytics)
- Document Management (SharePoint Online, OpenText, engineering document management)
- Enterprise Search & Knowledge Management

**Out of Scope:**
- Business application internals (SAP, Avocet, OSIsoft PI configuration)
- Infrastructure hosting (owned by IT Infrastructure / Cloud domains)
- Data science / ML model development (owned by AI domain)

### 1.2 Strategic Alignment
This domain directly supports Cenovus Energy's corporate strategy through:
- **Operational Excellence:** Reliable integration ensures production data flows from wellhead through to trading desks and financial reporting without manual intervention or data reconciliation gaps.
- **Capital Discipline:** Rationalized integration and MDM reduce duplicate data entry, reduce error rates in regulatory reporting, and lower total cost of ownership.
- **Safety & ESG:** Accurate master data for wells, facilities, and pipelines supports regulatory compliance (AER, CER) and environmental reporting obligations.
- **Digital Transformation:** API-first integration and self-service BI enable business agility and reduce time-to-insight for operational and strategic decisions.

### 1.3 Key Stakeholders
| Stakeholder | Role | Business Unit |
|-------------|------|---------------|
| VP, IT | Executive Sponsor | IT |
| Director, Data & Analytics | BI & Data Governance | IT |
| Director, IT Operations | Integration Operations | IT |
| Manager, Supply Chain | MDM - Materials & Vendors | Corporate Services |
| Manager, Land & Regulatory | GIS & Land Data | Upstream |
| Manager, Production Operations | Production Data Integration | Upstream |
| Manager, Refining Operations | Downstream Data Integration | Downstream |
| Controller, Financial Reporting | Financial Data & Reporting | Finance |
| Manager, HSE & Regulatory | ESG & Compliance Reporting | Corporate |
| Manager, Trading & Marketing | Trading Data Integration | Commercial |

## 2. Current State Assessment

### 2.1 Application Portfolio

#### Integration Platforms
| Application | Business Capability | Functional Capability | Status | Health |
|-------------|--------------------|-----------------------|--------|--------|
| MuleSoft Anypoint Platform | Enterprise Integration | iPaaS, API Management | Production | Yellow |
| IBM MQ | Message Queuing | Reliable messaging for SAP/legacy | Production | Yellow |
| Azure Service Bus | Cloud Messaging | Event-driven integration for Azure workloads | Production | Green |
| SAP PI/PO | ERP Integration | SAP-centric B2B and system integration | Production | Red |
| Azure API Management (APIM) | API Gateway | External API exposure and throttling | Production | Green |
| TIBCO BusinessWorks | Legacy Integration | Legacy point-to-point integrations | Sunset | Red |

#### Master Data Management
| Application | Business Capability | Functional Capability | Status | Health |
|-------------|--------------------|-----------------------|--------|--------|
| SAP MDG (Master Data Governance) | Material & Vendor Master | MDM workflows for SAP master data | Production | Yellow |
| Custom Well Master (SQL Server) | Well & Facility Master | Well header, UWI, facility hierarchy | Production | Red |
| geoSCOUT | Well Data Reference | Commercial well data | Production | Green |
| Quorum WellView | Well Data Management | Drilling & completions well master | Production | Yellow |

#### Enterprise Reporting & BI
| Application | Business Capability | Functional Capability | Status | Health |
|-------------|--------------------|-----------------------|--------|--------|
| Microsoft Power BI (Premium) | Self-Service BI | Dashboards, operational reporting | Production | Green |
| Azure Synapse Analytics | Data Warehouse | Enterprise data warehouse | Production | Green |
| Azure Data Lake Storage Gen2 | Data Lake | Raw & curated data storage | Production | Green |
| Azure Data Factory | Data Pipeline | ETL/ELT orchestration | Production | Green |
| SSRS (SQL Server Reporting Services) | Legacy Reporting | Paginated reports for Finance & Regulatory | Production | Yellow |
| Spotfire (TIBCO) | Engineering Analytics | Reservoir & production analytics | Production | Yellow |
| SAP BW/4HANA | SAP Reporting | Finance, supply chain, HR reporting from SAP | Production | Yellow |

#### GIS & Geospatial
| Application | Business Capability | Functional Capability | Status | Health |
|-------------|--------------------|-----------------------|--------|--------|
| Esri ArcGIS Enterprise | GIS Platform | Mapping, spatial analysis, web maps | Production | Green |
| ArcGIS Online (AGOL) | Cloud GIS | Field data collection, public map sharing | Production | Green |
| IHS Accumap / geoSCOUT | Well Mapping | Regulatory well data, land grid | Production | Green |
| Petrosys | Subsurface Mapping | Seismic, geological mapping | Production | Yellow |
| Custom Pipeline GIS (ArcGIS) | Pipeline Integrity | Pipeline routing, integrity data | Production | Yellow |

#### Document Management
| Application | Business Capability | Functional Capability | Status | Health |
|-------------|--------------------|-----------------------|--------|--------|
| SharePoint Online (M365) | Enterprise Collaboration | Document storage, team sites, wikis | Production | Green |
| OpenText Content Server | Enterprise Document Management | Controlled engineering documents, records retention | Production | Yellow |
| Aconex (Oracle) | Capital Project Documents | Engineering deliverables, transmittals | Production | Green |
| Documentum (legacy) | Legacy Records | Historical engineering records | Sunset | Red |

### 2.2 Technology Stack
| Layer | Technology | Version | End of Support |
|-------|-----------|---------|----------------|
| iPaaS | MuleSoft Anypoint (CloudHub 2.0) | 4.6 | Current |
| Message Broker | IBM MQ | 9.3 | 2027-12 |
| Cloud Messaging | Azure Service Bus | Current | Evergreen |
| Legacy ESB | TIBCO BusinessWorks | 5.x | 2024-12 (expired) |
| SAP Integration | SAP PI/PO | 7.5 | 2027-12 (extended) |
| API Gateway | Azure API Management | Current | Evergreen |
| MDM | SAP MDG on S/4HANA | 2023 FPS02 | 2027 |
| Data Warehouse | Azure Synapse Analytics | Current | Evergreen |
| Data Lake | Azure Data Lake Gen2 | Current | Evergreen |
| ETL | Azure Data Factory | V2 | Evergreen |
| BI | Power BI Premium | Current | Evergreen |
| BI (Legacy) | SSRS | SQL Server 2019 | 2030-01 |
| Analytics | Spotfire | 14.x | 2027-06 |
| GIS | ArcGIS Enterprise | 11.2 | 2028-12 |
| DMS | OpenText Content Server | 23.3 | 2028-06 |
| DMS (Legacy) | Documentum | 7.x | 2025-03 (expired) |

### 2.3 Strengths
- Strong Azure analytics foundation (Synapse, ADF, ADLS Gen2, Power BI) with growing adoption
- MuleSoft provides modern API-led integration capability with reusable assets
- ArcGIS platform well-established with mature GIS team and enterprise licensing
- Power BI adoption is high across business units with established governance model
- SharePoint Online well-integrated with M365 ecosystem

### 2.4 Gaps & Pain Points
| # | Gap | Business Impact | Priority |
|---|-----|-----------------|----------|
| 1 | No unified enterprise well master - data fragmented across custom SQL, WellView, geoSCOUT | Inconsistent well counts in regulatory reporting; manual reconciliation | Critical |
| 2 | TIBCO BusinessWorks past end-of-support with 45+ active integrations | Security risk; no vendor patches; fragile point-to-point connections | Critical |
| 3 | SAP PI/PO approaching end-of-support; migration to SAP Integration Suite not started | Risk to SAP B2B integrations (EDI, PIDX for procurement) | High |
| 4 | No enterprise event-driven architecture - systems rely on batch polling | Delayed production data propagation; stale trading positions | High |
| 5 | Documentum past end-of-support with 2M+ engineering records | Compliance risk for records retention; inaccessible legacy documents | High |
| 6 | Manual data pipelines for ESG/emissions reporting - spreadsheet-driven | Risk of misstatement; audit findings; delays in regulatory submissions | High |
| 7 | Spotfire usage declining; engineers moving to Power BI without subsurface support | Loss of specialized engineering analytics capability | Medium |
| 8 | Limited API governance - no consistent API versioning, lifecycle management, or developer portal | Integration fragility; slow onboarding of new consumers | Medium |
| 9 | OpenText requires on-premises infrastructure; not cloud-aligned | Operational overhead; misaligned with cloud-first strategy | Medium |

### 2.5 Technical Debt
| Item | Risk | Effort to Remediate | Priority |
|------|------|---------------------|----------|
| TIBCO BusinessWorks 5.x (45 integrations) | High - unsupported, security exposure | Large - requires re-implementation on MuleSoft | Critical |
| Custom Well Master (SQL Server 2016) | High - single developer dependency, no DR | Large - requires MDM platform selection & migration | Critical |
| Documentum 7.x (2M+ records) | Medium - unsupported, read-only access still needed | Large - migration to OpenText or SharePoint archive | High |
| SAP PI/PO legacy interfaces (120+ ICOs) | Medium - approaching end-of-support | Large - migrate to SAP Integration Suite or MuleSoft | High |
| SSRS reports (200+ reports) | Low - still supported but outdated UX | Medium - migrate to Power BI paginated reports | Medium |
| Spotfire licenses (underutilized) | Low - cost leakage | Small - consolidate or let expire | Low |

## 3. Future State Vision

### 3.1 Target Architecture
The future state Enterprise Applications architecture is centred on five pillars:

1. **API-Led Integration:** MuleSoft as the primary iPaaS with Azure Integration Services (Service Bus, Event Grid, API Management) for Azure-native workloads. All new integrations are API-first with published contracts. SAP Integration Suite handles SAP-specific B2B.

2. **Unified Master Data:** A governed enterprise MDM platform (SAP MDG extended or Informatica MDM) providing golden records for wells, facilities, materials, vendors, customers, and cost centres. Single source of truth consumed by all downstream systems.

3. **Modern Analytics Platform:** Azure Synapse + Data Lake as the enterprise data platform. Power BI as the single enterprise BI standard. Medallion architecture (bronze/silver/gold) with domain-specific data products. Self-service analytics with guardrails.

4. **Spatial Intelligence:** ArcGIS Enterprise as the GIS platform of record, integrated with the enterprise data platform. Real-time asset tracking, pipeline integrity dashboards, and ESG spatial analytics.

5. **Cloud-First Document Management:** SharePoint Online as the primary collaboration and document platform. OpenText migrated to cloud (OpenText Cloud Edition) for controlled engineering documents. Legacy Documentum records archived and decommissioned.

### 3.2 Guiding Principles
1. **API-First:** Every new system capability is exposed as a managed API before direct database or file integration is considered.
2. **Master Data as a Product:** Master data domains are treated as data products with defined owners, SLAs, and quality metrics.
3. **Cloud-Preferred:** New platform investments favour cloud/SaaS over on-premises. On-prem is justified only for latency-sensitive OT/SCADA integration.
4. **Reuse Over Rebuild:** Integration assets (APIs, connectors, data pipelines) are catalogued and reused. No duplicate integrations.
5. **Self-Service with Guardrails:** Business users can build reports, explore data, and create maps within governed frameworks - no shadow IT.
6. **Data Flows Follow Business:** Integration patterns mirror Cenovus business processes (wellhead to trading desk to financial close) rather than technology silos.

### 3.3 Target Application Portfolio
| Application | Business Capability | Functional Capability | Change |
|-------------|--------------------|-----------------------|--------|
| MuleSoft Anypoint Platform | Enterprise Integration | iPaaS, API management, API portal | Enhance |
| Azure Integration Services | Cloud Integration | Event-driven messaging, cloud-native APIs | Enhance |
| SAP Integration Suite | SAP Integration | SAP B2B (EDI, PIDX), SAP-to-SAP | New (replaces SAP PI/PO) |
| SAP MDG (S/4HANA) | Material & Vendor Master | MDM for SAP objects | Retain |
| Enterprise Well Master (MDM platform) | Well & Facility Master | Golden record for wells, facilities, UWIs | New (replaces custom SQL) |
| Azure Synapse Analytics | Data Warehouse | Enterprise DW, data lakehouse | Retain |
| Azure Data Lake Gen2 | Data Lake | Medallion architecture data storage | Retain |
| Microsoft Fabric | Unified Analytics | Data engineering, lakehouse, real-time analytics | New |
| Power BI (Premium/Fabric) | Enterprise BI | All operational & strategic reporting | Enhance |
| ArcGIS Enterprise | GIS Platform | Mapping, spatial analytics, web apps | Enhance |
| SharePoint Online | Enterprise Collaboration | Documents, wikis, knowledge management | Retain |
| OpenText Cloud Edition | Engineering Document Management | Controlled documents, records retention | New (replaces on-prem OpenText) |
| TIBCO BusinessWorks | Legacy Integration | - | Retire |
| SAP PI/PO | SAP Integration | - | Retire |
| Documentum | Legacy DMS | - | Retire |
| SSRS | Legacy Reporting | - | Retire |
| Spotfire | Engineering Analytics | - | Retire (replace with Power BI) |
| IBM MQ | Message Queuing | Retained for SAP messaging only | Retain (limited scope) |

## 4. Transition Roadmap

### 4.1 Roadmap Swimlanes

#### Near Term (0-12 months: 2026)
| Initiative | Description | Dependencies | Status |
|-----------|-------------|--------------|--------|
| TIBCO Decommission Phase 1 | Migrate top 20 critical TIBCO integrations to MuleSoft; establish migration patterns and testing framework | MuleSoft capacity expansion | In Progress |
| Enterprise Well Master - Discovery & Design | Business requirements, vendor evaluation (SAP MDG extension vs. Informatica), data quality assessment of existing well data | Data Governance Council endorsement | Planning |
| API Governance Framework | Publish API design standards, versioning policy, lifecycle management. Deploy MuleSoft Exchange as API catalog | None | Planning |
| Documentum Archive & Decommission | Migrate active records to OpenText; archive historical records to Azure Blob cold storage; decommission Documentum | OpenText capacity, records classification | In Progress |
| ESG Reporting Data Pipeline | Build automated data pipelines for GHG emissions, water usage, and flaring data from source systems to Power BI ESG dashboards | Source system API availability (PI, SAP) | Planning |
| Power BI Governance Refresh | Update Power BI workspace governance, implement deployment pipelines, establish data certification process | None | Planning |
| ArcGIS Enterprise 11.3 Upgrade | Upgrade ArcGIS Enterprise to latest version; enable ArcGIS Knowledge for asset network analysis | IT Infrastructure support | Planning |
| Microsoft Fabric Pilot | Pilot Microsoft Fabric for real-time analytics with production operations data (daily production volumes) | Azure tenant configuration | Planning |

#### Medium Term (12-24 months: 2027)
| Initiative | Description | Dependencies | Status |
|-----------|-------------|--------------|--------|
| TIBCO Decommission Phase 2 | Migrate remaining 25 TIBCO integrations to MuleSoft; decommission TIBCO | Phase 1 completion | Planned |
| Enterprise Well Master - Implementation | Implement MDM platform for well/facility master data; integrate with geoSCOUT, WellView, SAP, and ArcGIS | Discovery & Design completion | Planned |
| SAP Integration Suite Migration | Migrate SAP PI/PO interfaces to SAP Integration Suite; cover EDI, PIDX, and SAP-to-SAP flows | SAP S/4HANA roadmap alignment | Planned |
| Event-Driven Architecture - Phase 1 | Implement Azure Event Grid + Service Bus for real-time production data events; pilot with production allocation workflow | MuleSoft/Azure integration pattern | Planned |
| SSRS to Power BI Migration | Migrate 200+ SSRS reports to Power BI paginated reports; decommission SSRS | Power BI Governance completion | Planned |
| OpenText Cloud Migration | Migrate OpenText Content Server to OpenText Cloud Edition; decommission on-premises infrastructure | Cloud architecture design | Planned |
| GIS Data Integration Platform | Build ArcGIS-to-Synapse data pipeline for spatial analytics; enable pipeline integrity and ESG spatial reporting | ArcGIS upgrade, Synapse capacity | Planned |
| Data Mesh - Domain Data Products | Define and publish first wave of enterprise data products (production volumes, well master, financial actuals) with documented contracts | Enterprise Well Master, Synapse maturity | Planned |

#### Long Term (24-36 months: 2028-2029)
| Initiative | Description | Dependencies | Status |
|-----------|-------------|--------------|--------|
| Enterprise MDM Expansion | Extend MDM to customer, cost centre, and facility hierarchy domains | Well Master success | Planned |
| Real-Time Analytics Platform | Microsoft Fabric at enterprise scale for real-time operational dashboards (refinery, production, trading) | Fabric pilot success | Planned |
| Unified API Marketplace | MuleSoft Exchange as enterprise API marketplace with self-service onboarding for internal and partner consumers | API Governance maturity | Planned |
| Digital Twin Integration | Integrate GIS, IoT (PI/SCADA), and 3D models for facility digital twins; enable predictive maintenance analytics | ArcGIS, Azure Digital Twins, OT data | Planned |
| Knowledge Graph & Enterprise Search | Deploy AI-powered enterprise search across SharePoint, OpenText, and engineering repositories | Document migration completion | Planned |
| Spotfire Decommission | Complete migration of remaining Spotfire dashboards to Power BI; terminate Spotfire licenses | Power BI subsurface capability | Planned |

### 4.2 Key Milestones
| Milestone | Target Date | Dependencies |
|-----------|-------------|--------------|
| TIBCO Phase 1 complete (20 integrations migrated) | 2026-Q3 | MuleSoft capacity |
| Documentum fully decommissioned | 2026-Q4 | Archive migration |
| API Governance Standards published | 2026-Q2 | None |
| Enterprise Well Master MVP (well header golden record) | 2027-Q2 | Discovery completion |
| SAP PI/PO decommissioned | 2027-Q4 | SAP IS migration |
| TIBCO fully decommissioned | 2027-Q2 | Phase 2 completion |
| OpenText Cloud Edition live | 2027-Q3 | Cloud migration |
| SSRS fully decommissioned | 2027-Q3 | Power BI migration |
| Enterprise MDM operational for 3+ domains | 2028-Q2 | MDM expansion |
| Real-time analytics platform live | 2028-Q4 | Fabric rollout |

### 4.3 Application Rationalization Plan
| Application | Action | Target Date | Savings |
|-------------|--------|-------------|---------|
| TIBCO BusinessWorks 5.x | Retire - migrate to MuleSoft | 2027-Q2 | $350K/yr licensing + $200K/yr support |
| SAP PI/PO | Retire - migrate to SAP Integration Suite | 2027-Q4 | Included in SAP S/4HANA TCO |
| Documentum 7.x | Retire - archive to Azure/OpenText | 2026-Q4 | $180K/yr licensing + $120K/yr infrastructure |
| SSRS (SQL Server Reporting) | Retire - migrate to Power BI | 2027-Q3 | $50K/yr (server consolidation) |
| Spotfire | Retire - migrate to Power BI | 2028-Q4 | $280K/yr licensing |
| Custom Well Master (SQL Server) | Retire - replace with MDM platform | 2027-Q2 | Reduced manual reconciliation ($150K/yr FTE) |
| IBM MQ (partial) | Consolidate - reduce to SAP-only scope | 2028-Q2 | $80K/yr license reduction |

## 5. Investment Summary
| Initiative | CapEx | OpEx (Annual) | Priority | Year |
|-----------|-------|---------------|----------|------|
| TIBCO to MuleSoft Migration (Phase 1 & 2) | $800K | $120K | Critical | 2026-2027 |
| Enterprise Well Master (Discovery + Implementation) | $1.2M | $250K | Critical | 2026-2027 |
| Documentum Decommission & Archive | $400K | -$300K (savings) | High | 2026 |
| API Governance Framework | $150K | $50K | High | 2026 |
| SAP Integration Suite Migration | $600K | $180K | High | 2027 |
| ESG Reporting Data Pipeline | $300K | $80K | High | 2026 |
| Microsoft Fabric Pilot & Rollout | $500K | $350K | High | 2026-2028 |
| OpenText Cloud Migration | $450K | $60K (net increase) | Medium | 2027 |
| SSRS to Power BI Migration | $200K | -$50K (savings) | Medium | 2027 |
| GIS Data Integration Platform | $350K | $100K | Medium | 2027 |
| Event-Driven Architecture Phase 1 | $400K | $120K | Medium | 2027 |
| Digital Twin Integration | $800K | $200K | Medium | 2028-2029 |
| Knowledge Graph & Enterprise Search | $500K | $150K | Low | 2028-2029 |
| **TOTAL** | **$6.65M** | **~$1.31M net** | | 2026-2029 |

## 6. Risks & Dependencies
| Risk/Dependency | Type | Likelihood | Impact | Mitigation |
|-----------------|------|-----------|--------|------------|
| MuleSoft licensing costs escalate with API volume growth | Risk | Medium | High | Negotiate enterprise agreement; evaluate Azure-native alternatives for cloud workloads |
| SAP S/4HANA migration timeline shifts, impacting SAP IS and MDG plans | Dependency | High | High | Decouple SAP IS migration from S/4 where possible; maintain PI/PO extended support |
| Enterprise Well Master requires cross-BU data governance agreement | Risk | Medium | High | Engage Data Governance Council early; appoint Well Data Steward |
| Key MuleSoft/integration developers leave (talent scarcity) | Risk | Medium | High | Cross-train team; document all APIs; use MuleSoft managed services |
| Microsoft Fabric GA features don't meet real-time requirements | Risk | Medium | Medium | Maintain Synapse as fallback; pilot before committing |
| AER/CER regulatory changes require new data pipelines on short notice | Risk | Low | High | Build modular, configurable ESG data pipelines; maintain regulatory data dictionary |
| Documentum migration discovers undocumented records with legal holds | Risk | Medium | Medium | Engage Legal and Records Management before migration; classify before moving |
| Budget constraints defer MDM or Fabric investments | Risk | Medium | High | Phase investments; demonstrate quick wins (well master MVP) to secure continued funding |
| Cloud domain dependency for OpenText and Fabric infrastructure | Dependency | Low | Medium | Align with Cloud Architect on Azure landing zone capacity |

## 7. Alignment to EA Team Goals 2026

### Domain Goals (Section 2.8)
| Goal | Description | Roadmap Coverage | Target |
|------|-------------|------------------|--------|
| E-1 | Publish Enterprise Applications domain roadmap | This document (Sections 1-6) | Q2 2026 |
| E-2 | Define enterprise integration platform strategy | Section 3.1 (Pillar 1: API-Led Integration), Appendix A (Integration Pattern Reference) | Q2 2026 |
| E-3 | Develop MDM target architecture | Section 3.1 (Pillar 2: Unified Master Data), Appendix B (MDM Domain Ownership), Near/Medium-term initiatives | Q3 2026 |
| E-4 | Assess enterprise reporting and analytics platform architecture | Section 3.1 (Pillar 3: Modern Analytics Platform), Appendix C (Power BI Governance), Fabric pilot | Q3 2026 |
| E-5 | Define GIS platform strategy | Section 3.1 (Pillar 4: Spatial Intelligence), GIS application portfolio and initiatives | Q4 2026 |

### Cross-Domain Initiatives

**Initiative B: Cloud-First Application Modernization Program**
- Enterprise Apps contribution: OpenText Cloud migration, Microsoft Fabric deployment, Azure-native integration services
- Dependencies on: PA-Cloud (landing zone), PA-Infrastructure (hybrid connectivity)

**Initiative C: AI-Enabled Operations**
- Enterprise Apps contribution: Data pipeline architecture feeding AI/ML platforms from Synapse/Data Lake; API exposure of master data for model training
- Dependencies on: PA-AI (platform architecture), PA-Upstream/Downstream (use case identification)

**Initiative D: Enterprise Integration Modernization (Lead Domain)**
- Enterprise Apps deliverables:
  1. Integration platform target architecture (MuleSoft + Azure Integration Services + SAP IS) -- Q2 2026
  2. API management standards and governance (API design standards, versioning, lifecycle, developer portal) -- Q2 2026
  3. Integration pattern catalogue (API-led, event-driven, batch, B2B, file-based) -- Q2 2026
- Dependencies on: PA-Cloud (Azure services), PA-Corporate Apps (SAP roadmap), PA-Upstream/Downstream (integration requirements)

### Objective 4 Alignment (Application Rationalization)
- KR4.1: Application-to-capability mapping provided in Section 2.1 for all Enterprise Apps portfolio (25+ applications)
- KR4.3: Rationalization plan in Section 4.3 identifies 7 applications for retire/consolidate, targeting reduction in redundant integration and reporting tools
- KR4.4: TCO assessments planned for TIBCO-to-MuleSoft and Enterprise Well Master as top rationalization candidates

## 8. Governance & Review
- Roadmap review frequency: Quarterly
- Next review date: 2026-Q2 (April 2026)
- Approval authority: Team Leader + IT Senior Leadership
- Integration pattern reviews: Monthly (Architecture Review Board)
- Data governance alignment: Quarterly sync with Data Governance Council
- API review gate: All new APIs reviewed before production deployment

## 9. Appendices

### Appendix A: Integration Pattern Reference
| Pattern | Technology | Use Case |
|---------|-----------|----------|
| API-Led (System/Process/Experience) | MuleSoft | New integrations, cross-system data access |
| Event-Driven (Pub/Sub) | Azure Service Bus / Event Grid | Real-time data propagation, IoT/SCADA events |
| Batch ETL/ELT | Azure Data Factory | Data warehouse loading, bulk data movement |
| B2B/EDI | SAP Integration Suite | Vendor EDI (PIDX, cXML), regulatory submissions |
| File-Based (Legacy) | MuleSoft + SFTP | Legacy system integration (transition to API) |

### Appendix B: Master Data Domain Ownership
| Data Domain | Data Steward (Business) | System of Record | MDM Platform |
|-------------|------------------------|-------------------|--------------|
| Materials | Supply Chain Manager | SAP S/4HANA | SAP MDG |
| Vendors | Procurement Manager | SAP S/4HANA | SAP MDG |
| Wells | Production Operations Manager | Enterprise Well Master (future) | TBD |
| Facilities | Asset Management Lead | SAP PM / Enterprise Well Master | TBD |
| Cost Centres | Financial Controller | SAP S/4HANA | SAP MDG |
| Customers | Commercial/Trading Manager | SAP S/4HANA | SAP MDG |
| Land & Mineral Rights | Land Manager | IHS / Land System | Manual (future MDM) |

### Appendix C: Power BI Governance Model
| Workspace Tier | Ownership | Certification | Refresh |
|---------------|-----------|---------------|---------|
| Enterprise (Gold) | IT/BI Team | Certified, endorsed | Scheduled, SLA |
| Departmental (Silver) | Business + IT co-owned | Certified | Scheduled |
| Personal (Bronze) | Individual | Not certified | Manual/on-demand |
| Sandbox | Individual | Not certified | Manual |

### Appendix D: Key Acronyms
| Acronym | Definition |
|---------|-----------|
| AER | Alberta Energy Regulator |
| CER | Canada Energy Regulator |
| EDI | Electronic Data Interchange |
| ESG | Environmental, Social, and Governance |
| GHG | Greenhouse Gas |
| iPaaS | Integration Platform as a Service |
| MDG | Master Data Governance |
| MDM | Master Data Management |
| PIDX | Petroleum Industry Data Exchange |
| UWI | Unique Well Identifier |
