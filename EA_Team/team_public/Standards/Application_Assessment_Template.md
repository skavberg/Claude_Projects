# Application Assessment Intake Template

**Document ID:** AAT-2026-001
**Author:** Enterprise Architecture Team
**Domain:** Enterprise Architecture -- Application Portfolio
**Date:** 2026-02-08
**Version:** 1.0
**Status:** Draft
**Owner:** IT Architecture Team Leader
**Organization:** Cenovus Energy

**Related Documents:**
- Application Functional Capability Model Framework (AFCM-2026-001)
- Business Capability Model (BCM)

---

## Purpose

This template supports a two-phase application assessment process:

1. **Phase 1 -- Intake (Section A):** The requesting business unit or application owner provides basic inventory information about the applications to be assessed.
2. **Phase 2 -- Research (Section B):** The Enterprise Architecture team researches each application and documents its functional capabilities, strengths, gaps, and strategic fit using the Application Functional Capability Model Framework.

The output of this process is a standardized, comparable view of applications across the Cenovus portfolio that supports rationalization, gap analysis, and investment decisions.

---

## Section A: Application Inventory (User Intake)

**Instructions:** Fill in one row per application. Provide as much information as you have available. The EA team will validate and supplement this information during research. If you are uncertain about a field, provide your best estimate and add a note in the Notes column.

| Application Name | Vendor | Version | Deployment Model | Primary Business Unit | Primary Business Capability (BCM Ref) | Number of Users (approx.) | Annual Cost (approx.) | Status | Notes / Context |
|-----------------|--------|---------|-----------------|----------------------|---------------------------------------|--------------------------|----------------------|--------|----------------|
| | | | SaaS / On-Prem / Hybrid / Cloud IaaS | Upstream / Downstream / Corporate / Enterprise | [BCM ID or name] | | $ | Production / Emerging / Sunset / Proposed | |

### Example Rows (for guidance)

| Application Name | Vendor | Version | Deployment Model | Primary Business Unit | Primary Business Capability (BCM Ref) | Number of Users (approx.) | Annual Cost (approx.) | Status | Notes / Context |
|-----------------|--------|---------|-----------------|----------------------|---------------------------------------|--------------------------|----------------------|--------|----------------|
| OSIsoft PI System | AVEVA (Schneider Electric) | PI Server 2023 R2 | On-Prem | Enterprise | Production Monitoring & Optimization | 850 | $1,200,000 | Production | Enterprise historian; deployed at all major facilities. AVEVA acquisition from OSIsoft. Evaluating PI Cloud (AVEVA Data Hub) migration. |
| SAP S/4HANA | SAP SE | S/4HANA 2023 | On-Prem (Azure hosted) | Enterprise | Financial Management / Supply Chain | 2,500 | $8,500,000 | Production | Core ERP. Upgraded from ECC 6.0 in 2024. Modules: FI/CO, MM, PM, PS, JVA. Hosted on Azure IaaS. |
| Petrel | SLB (Schlumberger) | 2023.1 | On-Prem | Upstream | Reservoir Characterization | 120 | $2,800,000 | Production | Primary subsurface interpretation platform. Used by geoscience team. Integrated with ECLIPSE reservoir simulator. |
| Power BI | Microsoft | Service (SaaS) | SaaS | Enterprise | Business Intelligence & Analytics | 1,800 | $450,000 | Production | Enterprise BI platform. Connected to PI, SAP, and data lake. Premium capacity licensed. |
| Cority | Cority | 2024.1 | SaaS | Enterprise | Health, Safety & Environment | 3,200 | $600,000 | Emerging | Replacing legacy HSE system. Phased rollout -- incident management live, industrial hygiene in progress. |

---

## Section B: Research Output Template (EA Team)

**Instructions for EA Team:** For each application from Section A, conduct research and complete the following profile. Use the Application Functional Capability Model Framework (AFCM-2026-001) to assign functional capability IDs. Use the Business Capability Model (BCM) to assign business capability IDs. Consult vendor documentation, industry analyst reports (Gartner, Forrester, IDC), peer company references, and internal SMEs.

### Application Research Profile

For each application, copy and complete the following template:

---

#### [Application Name]

| Field | Details |
|-------|---------|
| **Application Name** | |
| **Vendor & Product URL** | |
| **Product Category** | e.g., ERP, SCADA, Historian, GIS, RPA, BI, EAM, ETRM, ECM |
| **Functional Capabilities (AFCM IDs)** | [List all applicable capability IDs from the AFCM framework] |
| **Business Capabilities Enabled (BCM IDs)** | [List all applicable BCM IDs] |
| **Deployment Options** | SaaS / On-Prem / Hybrid / Cloud-Hosted |
| **Licensing Model** | Per user / Per device / Enterprise / Consumption-based / Perpetual + Maintenance |
| **Oil & Gas Industry Adoption** | Widespread / Moderate / Niche |
| **EA Recommendation** | Strategic / Tactical / Evaluate / Sunset |

**Key Features Summary:**
- [bullet points]

**Integration Capabilities:**
- [Protocols, APIs, connectors, and systems it integrates with]

**Strengths (EA Perspective):**
- [bullet points]

**Gaps / Limitations:**
- [bullet points]

**Alternatives / Competitors:**
- [bullet points]

---

### Example 1: OSIsoft PI System (AVEVA PI)

| Field | Details |
|-------|---------|
| **Application Name** | OSIsoft PI System (now AVEVA PI) |
| **Vendor & Product URL** | AVEVA (Schneider Electric) -- https://www.aveva.com/en/products/aveva-pi-system/ |
| **Product Category** | Operational Historian / Real-Time Data Infrastructure |
| **Functional Capabilities (AFCM IDs)** | 1.1, 1.2, 1.4, 1.11, 2.1, 2.2, 2.4, 2.7, 4.6, 4.7, 4.9, 4.11, 10.2, 10.3, 10.6, 10.7, 10.10 |
| **Business Capabilities Enabled (BCM IDs)** | Production Monitoring, Production Optimization, Facility Operations, Environmental Monitoring, Asset Performance Management, Process Safety |
| **Deployment Options** | On-Prem (PI Server), Cloud (AVEVA Data Hub / PI Cloud), Hybrid |
| **Licensing Model** | Per tag (data point) + per named user for visualization tools; enterprise agreements available |
| **Oil & Gas Industry Adoption** | Widespread -- industry standard historian deployed at over 90% of major O&G companies globally |
| **EA Recommendation** | Strategic |

**Key Features Summary:**
- High-performance time-series data collection, storage, and retrieval optimized for operational data
- PI Data Archive provides compressed, high-fidelity storage of millions of data points per second
- PI Asset Framework enables contextualization of raw data into asset-centric models with hierarchies and calculations
- PI Vision provides browser-based real-time dashboards and trend displays
- PI Integrator for Azure and AWS enables streaming of operational data to cloud analytics platforms
- Supports 450+ native interfaces/connectors for SCADA, DCS, PLC, and other OT systems
- AVEVA Data Hub (cloud) provides SaaS historian with OCS (OPC Cloud Storage) for cloud-first deployments
- PI Notifications enables event-triggered alerts based on data conditions

**Integration Capabilities:**
- OPC-UA, OPC-DA, OPC-HDA native connectivity
- Modbus, DNP3, and proprietary DCS protocols via dedicated interfaces
- REST API (PI Web API) for modern application integration
- JDBC/ODBC connectivity for SQL-based access
- PI Integrator for Business Analytics (exports to relational databases, Power BI, Tableau)
- PI Integrator for Azure Event Hubs, AWS IoT SiteWise
- PI-to-PI connectivity for multi-site replication
- SDK (.NET) for custom application development

**Strengths (EA Perspective):**
- Unmatched breadth of OT system connectivity with 450+ interfaces -- minimizes custom integration work
- Proven at enterprise scale with 10+ million tag deployments in large O&G companies
- PI Asset Framework provides a semantic layer that bridges raw OT data and business context
- Strong data compression (typically 10:1) enables cost-effective long-term data retention
- Industry standard -- broad ecosystem of partners, consultants, and trained personnel
- Cloud migration path via AVEVA Data Hub does not require rip-and-replace of on-prem infrastructure
- PI Web API provides RESTful access enabling integration with modern analytics and AI/ML platforms

**Gaps / Limitations:**
- Per-tag licensing model can become expensive at scale -- cost management requires governance
- Legacy interfaces (pre-acquisition) can be complex to configure and maintain
- PI Vision (browser-based) lags behind modern BI tools in self-service analytics richness
- Cloud offering (AVEVA Data Hub) is less mature than on-prem PI Server -- feature parity gap remains
- AVEVA's post-acquisition product strategy has introduced uncertainty around roadmap direction
- Limited native advanced analytics -- typically requires export to external ML/analytics tools
- No built-in process simulation or digital twin capability -- requires integration with complementary tools

**Alternatives / Competitors:**
- Honeywell Uniformance PHD -- strong in refining and petrochemical
- AspenTech InfoPlus.21 (IP.21) -- strong in chemicals, increasingly in upstream
- AVEVA Historian (legacy Wonderware) -- different product line within AVEVA, consolidation expected
- InfluxDB / TimescaleDB -- open-source time-series databases; viable for greenfield IoT but lack OT interface breadth
- AWS IoT SiteWise / Azure Data Explorer -- cloud-native alternatives gaining traction but less mature for OT

---

### Example 2: SAP S/4HANA

| Field | Details |
|-------|---------|
| **Application Name** | SAP S/4HANA |
| **Vendor & Product URL** | SAP SE -- https://www.sap.com/products/erp/s4hana.html |
| **Product Category** | Enterprise Resource Planning (ERP) |
| **Functional Capabilities (AFCM IDs)** | 1.1, 1.4, 1.6, 2.1, 2.2, 2.7, 2.10, 3.1, 3.4, 3.5, 3.7, 4.1, 4.2, 4.5, 4.8, 6.1, 6.2, 6.5, 6.7, 11.1, 11.7, 12.1, 12.2, 12.3, 12.4, 12.5, 12.6, 12.7, 12.8, 12.9, 12.10, 12.11, 12.12, 13.1, 13.2, 13.3, 13.8, 14.1, 14.3, 14.5, 15.1, 15.2 |
| **Business Capabilities Enabled (BCM IDs)** | Financial Management, Procurement, Supply Chain Management, Asset Maintenance, Project Cost Management, Joint Venture Administration, Production Accounting, Treasury Management, Tax Management, Human Capital Management |
| **Deployment Options** | On-Prem, Private Cloud (RISE with SAP), Public Cloud (SAP BTP) |
| **Licensing Model** | Named user (professional, limited professional, employee self-service) + engine-based for specific modules; enterprise agreements with volume discounts |
| **Oil & Gas Industry Adoption** | Widespread -- dominant ERP in upstream and integrated O&G; used by most major and large independent producers |
| **EA Recommendation** | Strategic |

**Key Features Summary:**
- In-memory HANA database platform eliminates separate data warehouse for many reporting needs
- Fiori UX provides modern, role-based user experience across devices
- Joint Venture Accounting (JVA) module purpose-built for O&G partnership accounting
- Production Revenue Accounting supports complex royalty and revenue distribution
- SAP Asset Manager and Plant Maintenance (PM) provide maintenance management capabilities
- SAP BTP (Business Technology Platform) provides integration, extension, and AI/ML services
- Embedded analytics with real-time operational reporting directly from transactional data
- SAP Ariba integration for procurement and supplier management

**Integration Capabilities:**
- SAP Integration Suite (formerly CPI) for cloud-to-cloud and cloud-to-on-prem integration
- RFC/BAPI/IDoc for classic SAP-to-SAP integration
- OData and REST APIs for modern integrations via SAP Gateway
- EDI (EDIFACT, X12) via SAP B2B Integration
- SOAP web services for legacy integrations
- SAP Event Mesh for event-driven architecture patterns
- Pre-built integrations with SAP ecosystem (SuccessFactors, Ariba, Concur, Fieldglass)
- Certified partner connectors for SCADA historians (PI, PHD) and industry applications

**Strengths (EA Perspective):**
- Broadest functional coverage of any single platform -- reduces integration complexity
- Strong O&G industry-specific functionality (JVA, production accounting, plant maintenance)
- HANA in-memory architecture enables real-time analytics on transactional data
- Mature, well-understood platform with large partner ecosystem and talent pool
- Strong regulatory compliance capabilities (SOX, IFRS, multi-GAAP)
- SAP BTP provides a strategic platform for extensions, integrations, and AI without modifying core
- Clear cloud migration path via RISE with SAP for customers wanting to move off on-prem

**Gaps / Limitations:**
- High total cost of ownership -- licensing, implementation, and ongoing operational costs are significant
- Complexity of customization and upgrade paths -- heavy customization creates long-term technical debt
- Fiori UX adoption is uneven; many transactions still require SAP GUI
- Cloud migration (RISE) requires significant planning and business process standardization
- SAP talent is expensive and increasingly scarce in the Calgary market
- Integration with OT systems (SCADA, historians) requires middleware or partner solutions
- Mobile capabilities are improving but still lag behind purpose-built field applications
- Analytics capabilities, while improving, are less flexible than dedicated BI platforms (Power BI, Tableau)

**Alternatives / Competitors:**
- Oracle Cloud ERP (Fusion) -- strong in financials; less O&G-specific functionality than SAP
- Microsoft Dynamics 365 Finance & Operations -- growing in mid-market O&G; less mature for large integrated companies
- Quorum Software (previously TietoEVRY O&G) -- O&G-specific ERP for production accounting and land
- P2 Energy Solutions (now Quorum) -- production revenue and land management
- Enertia -- O&G-specific ERP for upstream companies
- IFS -- strong in asset-intensive industries; growing O&G presence

---

### Example 3: Petrel (SLB)

| Field | Details |
|-------|---------|
| **Application Name** | Petrel Subsurface Software |
| **Vendor & Product URL** | SLB (formerly Schlumberger) -- https://www.software.slb.com/products/petrel |
| **Product Category** | Subsurface Interpretation & Modelling / E&P Software |
| **Functional Capabilities (AFCM IDs)** | 1.1, 1.2, 2.4, 2.8, 2.9, 7.1, 7.2, 8.1, 8.3, 8.8, 9.1, 9.5, 9.7, 9.9 |
| **Business Capabilities Enabled (BCM IDs)** | Reservoir Characterization, Well Planning, Geological Interpretation, Geophysical Interpretation, Reservoir Simulation, Reserves Estimation, Drilling Engineering, Field Development Planning |
| **Deployment Options** | On-Prem (Windows workstation), Cloud-enabled via DELFI platform |
| **Licensing Model** | Module-based perpetual license + annual maintenance; also available as subscription; token-based licensing for flexible module access |
| **Oil & Gas Industry Adoption** | Widespread -- dominant subsurface interpretation platform globally, used by the majority of E&P companies |
| **EA Recommendation** | Strategic |

**Key Features Summary:**
- Integrated seismic interpretation with 2D/3D seismic visualization and attribute analysis
- Geological modelling including structural framework, facies modelling, and petrophysical property modelling
- Well planning with 3D trajectory design, anti-collision analysis, and casing design
- Reservoir simulation coupling with ECLIPSE (SLB) and INTERSECT for flow simulation
- Decline curve analysis and production forecasting tools
- Uncertainty and risk analysis via Monte Carlo simulation workflows
- DELFI cloud platform provides cloud-based access, collaboration, and AI/ML-augmented workflows
- Data management through Petrel Studio for multi-user, multi-discipline collaboration
- Supports diverse data types: seismic, well logs, core data, production data, surfaces, grids

**Integration Capabilities:**
- Native integration with SLB ecosystem (ECLIPSE, INTERSECT, Techlog, OLGA, Pipesim)
- Ocean plug-in framework for third-party extensions and custom workflows
- WITSML for drilling data exchange
- LAS, DLIS for well log data import
- SEG-Y for seismic data import/export
- RESQML for reservoir model exchange
- DELFI Data Ecosystem for cloud-based data access and sharing
- Limited direct integration with enterprise IT systems (ERP, BI) -- typically requires middleware

**Strengths (EA Perspective):**
- Most comprehensive subsurface interpretation platform on the market -- covers geology, geophysics, and reservoir engineering in a single environment
- Strong multi-discipline workflow integration reduces data transfer friction between geoscience disciplines
- Ocean plug-in ecosystem extends functionality and enables custom workflows
- DELFI cloud platform provides a path toward cloud-native subsurface workflows and AI/ML integration
- Dominant market position means broad availability of trained professionals and industry best practices
- Active R&D investment with regular feature releases and AI/ML integration (e.g., seismic interpretation AI)

**Gaps / Limitations:**
- Computationally intensive -- requires high-performance workstations with dedicated GPUs
- Steep learning curve for new users across the full breadth of modules
- SLB vendor lock-in risk -- deep integration with SLB ecosystem creates switching costs
- Limited interoperability with non-SLB simulation tools (competitor reservoir simulators)
- DELFI cloud adoption is slower than expected due to data sovereignty concerns and cost
- Licensing model complexity -- module-based licensing makes cost management challenging
- Desktop-centric architecture; cloud-native Petrel is still evolving on the DELFI platform
- No direct integration with enterprise systems (ERP, BI, data lakes) -- requires custom ETL

**Alternatives / Competitors:**
- Halliburton Landmark DecisionSpace 365 -- primary competitor; strong in well planning and drilling
- Emerson (Paradigm) Geolog / SKUA-GOCAD -- strong in geological modelling
- CGG Hampson-Russell -- strong in seismic reservoir characterization and AVO analysis
- S&P Global Kingdom -- lighter-weight interpretation tool; popular with smaller E&P companies
- TIBCO Spotfire (with O&G add-ons) -- some analytics overlap but not a subsurface modelling replacement

---

## Section C: Instructions

### Step-by-Step Process

This section describes the end-to-end process for conducting an application assessment using this template and the Application Functional Capability Model Framework.

#### Step 1: Initiate the Assessment

The application owner, business unit lead, or IT relationship manager initiates the assessment by contacting the Enterprise Architecture team. Common triggers include:
- Annual application portfolio review cycle
- New application request (reference NAR process)
- Technology rationalization initiative
- M&A integration assessment
- Cloud migration planning
- Budget optimization exercise

#### Step 2: User Completes Section A (Application Inventory)

**Who:** The requestor (application owner, business unit representative, or IT relationship manager).

**What to do:**
1. Copy the Section A table for each application to be assessed.
2. Fill in every column to the best of your knowledge:
   - **Application Name:** Use the official product name as recognized by the vendor.
   - **Vendor:** Current vendor name. Note acquisitions if relevant (e.g., "AVEVA (formerly OSIsoft)").
   - **Version:** Current deployed version at Cenovus. If unknown, state "Unknown".
   - **Deployment Model:** Select one: SaaS, On-Prem, Hybrid, or Cloud IaaS. "Hybrid" means components run both on-prem and in the cloud. "Cloud IaaS" means the application is installed on cloud-hosted infrastructure (e.g., Azure VM) but is not SaaS.
   - **Primary Business Unit:** Which business unit primarily uses or sponsors this application.
   - **Primary Business Capability (BCM Ref):** Reference the Cenovus Business Capability Model. If you do not know the BCM ID, describe the business function in plain language and the EA team will map it.
   - **Number of Users:** Approximate count of active users. Include a note if this includes contractors or external users.
   - **Annual Cost:** Approximate annual cost including licensing, subscription, maintenance, and support. Exclude one-time implementation costs unless stated otherwise.
   - **Status:** Select one: Production (in active use), Emerging (being deployed), Sunset (planned for retirement), or Proposed (not yet purchased).
   - **Notes / Context:** Any additional context that would help the EA team understand the application's role, history, planned changes, or known issues.
3. Submit the completed Section A to the Enterprise Architecture team via the designated intake channel.

#### Step 3: EA Team Reviews and Validates Section A

**Who:** Assigned Portfolio Architect from the EA team.

**What to do:**
1. Review the submitted inventory for completeness and accuracy.
2. Clarify any ambiguities with the requestor.
3. Validate vendor names, versions, and deployment models against known records.
4. Confirm scope -- which applications will proceed to full research in Section B.
5. Assign priority and target completion dates for Section B research.

#### Step 4: EA Team Researches and Completes Section B

**Who:** Assigned Portfolio Architect, with support from the EA team and subject matter experts.

**What to do:**
1. For each application in scope, create a research profile using the Section B template.
2. Research the application using the following sources:
   - Vendor website and product documentation
   - Gartner Magic Quadrants, Forrester Wave, and IDC MarketScape reports
   - Industry peer references and case studies
   - Internal Cenovus SME interviews (application administrators, power users, IT support)
   - Existing architecture documentation and integration inventories
3. **Map Functional Capabilities:**
   - Open the Application Functional Capability Model Framework (AFCM-2026-001).
   - Review each of the 15 functional domains.
   - For each domain, determine whether the application provides any of the listed functional capabilities.
   - Record the capability IDs (e.g., 1.1, 2.3, 10.2) in the "Functional Capabilities" field.
   - Be thorough but accurate -- only assign capability IDs where the application genuinely provides the capability, not where it has a superficial or ancillary feature.
   - When in doubt, note the capability as "Partial" with an explanation.
4. **Map Business Capabilities:**
   - Using the Cenovus Business Capability Model (BCM), identify which business capabilities this application enables.
   - Record the BCM IDs or names in the "Business Capabilities Enabled" field.
   - An application may enable multiple business capabilities across different business units.
5. Complete all remaining fields: features, integration, licensing, strengths, gaps, alternatives, industry adoption, and EA recommendation.
6. Assign an **EA Recommendation** using the following definitions:

| Recommendation | Definition |
|---------------|------------|
| **Strategic** | This application is aligned with the target architecture and should receive continued investment. It is the preferred platform for the capabilities it delivers. |
| **Tactical** | This application serves a current need but is not part of the long-term target architecture. It should be maintained but not expanded. A migration path should be planned. |
| **Evaluate** | This application requires further evaluation before a strategic direction is determined. More information is needed about capabilities, costs, alternatives, or business need. |
| **Sunset** | This application should be retired. A replacement has been identified or the business need has been eliminated. A decommissioning plan and timeline should be established. |

#### Step 5: Review and Socialize

**Who:** Portfolio Architect presents to the EA team; findings shared with requestor and stakeholders.

**What to do:**
1. Review completed Section B profiles within the EA team for quality and consistency.
2. Present findings to the requestor and relevant stakeholders.
3. Discuss recommendations, particularly for applications recommended as "Sunset" or "Evaluate".
4. Incorporate feedback and finalize the assessment.
5. Update the enterprise application portfolio repository with the new assessment data.

#### Step 6: Act on Findings

**Who:** EA team in collaboration with business and IT stakeholders.

**What to do:**
1. Feed assessment results into relevant EA processes:
   - **Portfolio rationalization:** Identify redundant applications delivering the same functional capabilities.
   - **Gap analysis:** Identify business capabilities lacking adequate technology support.
   - **Roadmap planning:** Inform domain technology roadmaps with assessment findings.
   - **New application requests:** Use assessments as context when evaluating proposed new applications.
   - **Budget planning:** Provide cost and capability data for IT budget discussions.
2. Track action items and decisions in the Architecture Decision Record (ADR) process.
3. Schedule re-assessment per the governance cycle (typically annual or triggered by significant change).

---

### RACI Summary

| Activity | Requestor / App Owner | Portfolio Architect | EA Team Leader | IT Leadership |
|----------|----------------------|--------------------|--------------------|---------------|
| Complete Section A | **R/A** | C | I | I |
| Validate Section A | C | **R/A** | I | -- |
| Research & Complete Section B | I | **R/A** | C | -- |
| Map Functional Capabilities (AFCM) | -- | **R/A** | C | -- |
| Map Business Capabilities (BCM) | C | **R/A** | C | -- |
| Assign EA Recommendation | -- | **R** | **A** | I |
| Review & Socialize Findings | I | **R** | **A** | I |
| Act on Findings (Rationalization, Roadmap) | C | **R** | **A** | **R** |

R = Responsible, A = Accountable, C = Consulted, I = Informed

---

## Revision History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-02-08 | Enterprise Architecture Team | Initial template creation. |
