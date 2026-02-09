# Cenovus Energy -- Business Capability Model (BCM)

| Field               | Value                                              |
|---------------------|----------------------------------------------------|
| **Document**        | Business Capability Model -- ServiceNow CMDB Source |
| **Version**         | 2.0                                                |
| **Status**          | Approved                                           |
| **Source**          | ServiceNow CMDB (`cmdb_ci_business_capability`)    |
| **Owner**           | Enterprise Architecture, Corporate IT              |
| **Sponsor**         | VP Enterprise Architecture & Digital               |
| **Classification**  | Internal -- Cenovus Energy                         |
| **Created**         | 2025-06-15                                         |
| **Last Updated**    | 2026-02-08                                         |
| **Review Cycle**    | Annual (next review: 2027-Q1)                      |
| **Applicable Scope**| All Cenovus business units, subsidiaries, and JVs  |

---

## Table of Contents

1. [Introduction](#1-introduction)
2. [How to Use This BCM](#2-how-to-use-this-bcm)
3. [Visual Summary -- Level 1 Capability Map](#3-visual-summary----level-1-capability-map)
4. [Capability Hierarchy -- L1 / L2 / L3](#4-capability-hierarchy----l1--l2--l3)
   - 4.1 Asset Development
   - 4.2 Reservoir Engineering
   - 4.3 Geology & Geophysics
   - 4.4 Well Management
   - 4.5 Project Delivery
   - 4.6 Reclamation & Remediation
   - 4.7 Site Operations Management
   - 4.8 Maintenance Management
   - 4.9 Resource Management
   - 4.10 Supply & Logistics
   - 4.11 Marketing & Trading
   - 4.12 Optimization
   - 4.13 Manufacturing & Processing
   - 4.14 Commercial Products
   - 4.15 Retail
   - 4.16 Supply Chain Management
   - 4.17 Financial Management
   - 4.18 Human Resources
   - 4.19 Information Technology
   - 4.20 Strategic Management
   - 4.21 Health & Safety
   - 4.22 Environment & Sustainability
   - 4.23 Legal
   - 4.24 Research & Development
   - 4.25 Governance & Compliance
   - 4.26 Workplace & Real Estate
5. [Capability Count Summary](#5-capability-count-summary)
6. [Cross-Reference: BCM to Application Functional Capability Framework](#6-cross-reference-bcm-to-application-functional-capability-framework)
7. [Governance & Change Management](#7-governance--change-management)

---

## 1. Introduction

A **Business Capability Model (BCM)** is a structured, hierarchical representation of
**what** an organization does -- independent of how it is done, who does it, or what
technology supports it. Capabilities are expressed as stable constructs that change far
less frequently than organizational structures, business processes, or application
portfolios.

### Source of Truth -- ServiceNow CMDB

This Business Capability Model is **sourced directly from the ServiceNow Configuration
Management Database (CMDB)**, specifically from the `cmdb_ci_business_capability` table.
The CMDB serves as the authoritative system-of-record for all business capabilities at
Cenovus Energy. Any modifications to capability names, descriptions, hierarchy, or
ordering must be made in ServiceNow first; this document is a rendered view of that
data as of **2026-02-08**.

The export contained **621 total capability records** organized across three hierarchy
levels:

| Level   | Purpose                                          | Count |
|---------|--------------------------------------------------|-------|
| **L1**  | Strategic grouping (hierarchy_level = 0)         | 26    |
| **L2**  | Major business function (hierarchy_level = 1)    | 127   |
| **L3**  | Discrete, measurable capability (hierarchy_level = 2) | 468   |

### Hierarchy Levels

- **L1 (hierarchy_level = 0):** Top-level strategic capability groups with no parent.
  These represent the broadest organizational functions.
- **L2 (hierarchy_level = 1):** Major business functions nested under an L1 parent.
  Each L2 capability supports a specific aspect of its parent L1 domain.
- **L3 (hierarchy_level = 2):** Discrete, measurable capabilities nested under an L2
  parent. These are the most granular capabilities tracked in the CMDB.

---

## 2. How to Use This BCM

| Use Case                              | How the BCM Helps                                                                                              |
|---------------------------------------|----------------------------------------------------------------------------------------------------------------|
| **Application Portfolio Rationalization** | Map every application to the capabilities it supports; identify redundancy, gaps, and over-investment.       |
| **Investment Prioritization**         | Heatmap capabilities by strategic importance, maturity, and investment level to guide capital allocation.       |
| **M&A / Divestiture Analysis**        | Compare acquirer and target capability maps to find synergies, overlaps, and capability gaps.                  |
| **Organizational Design**             | Align organizational units to capabilities; identify shared-service candidates.                                |
| **Digital Transformation Planning**   | Identify capabilities ripe for digitization, automation, or advanced analytics.                                |
| **Vendor & Solution Evaluation**      | Evaluate vendor offerings against the capability map to ensure fit and avoid scope creep.                      |
| **Risk & Compliance Mapping**         | Overlay regulatory obligations onto capabilities to ensure complete coverage of compliance requirements.       |
| **Data Architecture Alignment**       | Map business data domains to the capabilities that create, read, update, and consume them.                     |

### Reading the Model

- Each capability is numbered hierarchically: **L1.L2.L3** (e.g., 4.2.3 = Well
  Management > Well Design & Planning > Well Type).
- L1 and L2 capabilities include descriptions where available in ServiceNow. L3
  capabilities include descriptions only if they were populated in the CMDB export.
- The model is intentionally **technology-agnostic** -- separate mapping artefacts
  connect applications, data, and technologies to capabilities.

---

## 3. Visual Summary -- Level 1 Capability Map

```
+===========================================================================================+
|                     CENOVUS ENERGY -- BUSINESS CAPABILITY MAP (ServiceNow CMDB)           |
+===========================================================================================+
|                                                                                           |
|  UPSTREAM / FIELD OPERATIONS                                                              |
|  =========================================================================================|
|                                                                                           |
|  +------------------+  +------------------+  +------------------+  +------------------+   |
|  | 1. ASSET         |  | 2. RESERVOIR     |  | 3. GEOLOGY &     |  | 4. WELL          |   |
|  |    DEVELOPMENT   |  |    ENGINEERING   |  |    GEOPHYSICS    |  |    MANAGEMENT    |   |
|  +------------------+  +------------------+  +------------------+  +------------------+   |
|  +------------------+  +------------------+  +------------------+  +------------------+   |
|  | 5. PROJECT       |  | 6. RECLAMATION & |  | 7. SITE OPS      |  | 8. MAINTENANCE   |   |
|  |    DELIVERY      |  |    REMEDIATION   |  |    MANAGEMENT    |  |    MANAGEMENT    |   |
|  +------------------+  +------------------+  +------------------+  +------------------+   |
|  +------------------+                                                                     |
|  | 9. RESOURCE      |                                                                     |
|  |    MANAGEMENT    |                                                                     |
|  +------------------+                                                                     |
|                                                                                           |
|  MIDSTREAM / DOWNSTREAM / COMMERCIAL                                                      |
|  =========================================================================================|
|                                                                                           |
|  +------------------+  +------------------+  +------------------+  +------------------+   |
|  | 10. SUPPLY &     |  | 11. MARKETING &  |  | 12. OPTIMIZATION |  | 13. MANUFACTURING|   |
|  |     LOGISTICS    |  |     TRADING      |  |                  |  |     & PROCESSING |   |
|  +------------------+  +------------------+  +------------------+  +------------------+   |
|  +------------------+  +------------------+                                               |
|  | 14. COMMERCIAL   |  | 15. RETAIL       |                                               |
|  |     PRODUCTS     |  |                  |                                               |
|  +------------------+  +------------------+                                               |
|                                                                                           |
|  CORPORATE / ENABLING CAPABILITIES                                                        |
|  =========================================================================================|
|                                                                                           |
|  +------------------+  +------------------+  +------------------+  +------------------+   |
|  | 16. SUPPLY CHAIN |  | 17. FINANCIAL    |  | 18. HUMAN        |  | 19. INFORMATION  |   |
|  |     MANAGEMENT   |  |     MANAGEMENT   |  |     RESOURCES    |  |     TECHNOLOGY   |   |
|  +------------------+  +------------------+  +------------------+  +------------------+   |
|  +------------------+  +------------------+  +------------------+  +------------------+   |
|  | 20. STRATEGIC    |  | 21. HEALTH &     |  | 22. ENVIRONMENT  |  | 23. LEGAL        |   |
|  |     MANAGEMENT   |  |     SAFETY       |  |     & SUSTAIN.   |  |                  |   |
|  +------------------+  +------------------+  +------------------+  +------------------+   |
|  +------------------+  +------------------+  +------------------+                         |
|  | 24. RESEARCH &   |  | 25. GOVERNANCE & |  | 26. WORKPLACE &  |                         |
|  |     DEVELOPMENT  |  |     COMPLIANCE   |  |     REAL ESTATE  |                         |
|  +------------------+  +------------------+  +------------------+                         |
|                                                                                           |
+===========================================================================================+
```

---

## 4. Capability Hierarchy -- L1 / L2 / L3

---

### 1. Asset Development

> *Ability to manage, interpret and use geological, reservoir and production models along with economic models to plan and manage full field development and expansion.*

#### 1.1 Portfolio Development
*Ability to manage, interpret and use of geological, reservoir, production, cost, tariff, GHG and constraint models along with economic models to plan and optimize full field asset development.
Including:
. Full field development planning
. Economic modeling
. Scenario planning & portfolio management
. Capital management
. Business case development & opportunity management*

- 1.1.1 Full Field Planning
- 1.1.2 Capacity Planning
- 1.1.3 Decision Analysis
- 1.1.4 Economic Models
- 1.1.5 Scenario Planning
- 1.1.6 Capital Management

#### 1.2 Bus.Development, Exploration, Acquisition
*Ability to manage, interpret and use geological, reservoir and production models along with economic models to plan and manage full field development and expansion outside of oilsands or conventional assets.
Capability includes:
. Light oil conventional/unconventional exploration
. CO2 sequestration opportunities
. Peer reviews
. Emerging asset portfolio management
. Acquisition and Divestiture evaluation
. Acquisition and mergers
Note - there is a linkage between this capability and the Divestment capability in the Exit layer.*

- 1.2.1 Light Oil, Conventional/Unconventional Exploration
- 1.2.2 CO2 Sequestration Opportunities
- 1.2.3 Peer Reviews
- 1.2.4 Emerging Asset Portfolio Management
- 1.2.5 A&D Evaluations
- 1.2.6 Acquisitions & Mergers

#### 1.3 Competitor Analysis
*Ability to gather, interpret and make competitor information consumable.*

*(No L3 capabilities)*

#### 1.4 Land Management
*Ability to track assets and agreements related to surface access and wells by managing the details related to leases, assignments, contracts, divisions of interest, delay rentals, special obligations, royalty burdens, working interests, etc. This capability also includes tracking assets, agreements and relevant negotiations related to mineral rights.
Capability includes:
. Land Negotiations
. Mineral Rights Leases, Agreements & Licence Management
. Surface Land Leases & Agreements
. Land Asset Reporting
. Lease & Royalty Payments
. Lease Inventory
. Regulatory & Partner Reporting*

- 1.4.1 Land Negotiations
- 1.4.2 Mineral Rights, Leases & Agreements
- 1.4.3 Surface Land Leases & Agreements
- 1.4.4 Reporting (Regulatory, Partner, Land Asset, Lease Inventory
- 1.4.5 Lease Royalty Payments

---

### 2. Reservoir Engineering

> *Ability to manage, interpret and use reservoir characteristics and properties along with geological models to simulate, plan and optimize reservoir performance.*

#### 2.1 Reservoir Development
*Ability to manage, interpret and use reservoir characteristics and properties along with geological models to form an accurate initial view of resource potential.
Capability includes:
. Well/pad/pod planning
. Exploitation design
. Base simulation
. Reserves assessment
. Well spacing optimization*

- 2.1.1 Well/Pad/Pod Planning
- 2.1.2 Exploitation Design
- 2.1.3 Base Simulation
- 2.1.4 Reserves Assessment
- 2.1.5 Well Spacing Optimization

#### 2.2 Reservoir Optimization
*Ability to manage, interpret and use reservoir characteristics and properties along with geological models, surveillance data and production history to optimize the full lifecycle value of producing wells/pads and implement long term optimization strategies.
Capability includes:
. Base & redevelopment forecasting
. Late life management
. History matching
. Steam optimization
. Liner design
. Source/disposal optimization
. Data analytics*

- 2.2.1 Base & Redevelopment Forecasting
- 2.2.2 Late Life Management
- 2.2.3 History Matching
- 2.2.4 Steam Optimization
- 2.2.5 Liner Design
- 2.2.6 Source / Disposal Optimization
- 2.2.7 Data Analytics

#### 2.3 Reservoir Services Management
*Ability to advance understanding of exploitation techniques and tools to assist reservoir and production engineers in understanding reservoir responses.
Capability includes:
. Simulation process
. Simulation software maintenance
. Analytic forecasting
. PVT analysis
. Geomechanics*

- 2.3.1 Simulation Process
- 2.3.2 Simulation Software Maintenance
- 2.3.3 Analytical Forecasting
- 2.3.4 PVT Analysis
- 2.3.5 Geomechanics

---

### 3. Geology & Geophysics

> *Ability to manage, interpret and use subsurface rock information to plan and execute well, pad and pod placement for optimal reservoir drainage and to optimize geological reservoir understanding.
> Information consumed includes seismic, log, core and drilling data.*

#### 3.1 Geological Development
*Ability to manage, interpret and use subsurface information to form an accurate initial view of a reservoirs.
Capability includes:
. Development Planning: Resource Progression, Long Range Planning, Pad Planning, Well Planning
. Well log / core analysis
. 3D seismic interpretation and integration
. Facies interpretation
. Geomodelling
. Geological mapping
. Oil in place volumes
. Scope planning*

- 3.1.1 Development Planning
- 3.1.2 Well Log / Core Analysis
- 3.1.3 3D Seismic Interpretation & Integration
- 3.1.4 Facies Interpretation
- 3.1.5 Geomodelling
- 3.1.6 Oil in Place Volumes (Development)
- 3.1.7 Scope Planning
- 3.1.8 Stripling Mud Analysis

#### 3.2 Geological Optimization
*Ability to manage, interpret and use subsurface information to optimize geological reservoir understanding.
Capability includes:
. Oil in place volumes
. Well redevelopment
. Reservoir surveillance
. 4D seismic interpretation and integration
. Short term production/completions optimization and troubleshooting*

- 3.2.1 Oil in Place Volumes (Optimization)
- 3.2.2 Well Redevelopment
- 3.2.3 Reservoir Surveillance
- 3.2.4 4D Seismic Interpretation & Integration
- 3.2.5 Short Term Production / Completions Optimization & Troubleshooting

#### 3.3 Geological Execution
*Ability to manage, interpret and use of subsurface information to plan and execute well placement.
Capability includes:
. Well planning and placement
. Geosteering
. Geological operations and reporting*

- 3.3.1 Well Planning & Placement
- 3.3.2 Geosteering
- 3.3.3 Geological Operations & Reporting

#### 3.4 Geological Info Management
*Ability to collect and manage Geological and Geophysical information in a consistent and consumable way.
Capability includes:
. Data management
. Data integration
. Analytics*

- 3.4.1 G&G Data Management
- 3.4.2 G&G Data Integration
- 3.4.3 G&G Analytics

#### 3.5 Seismic Management
*Ability to manage the acquisition of seismic data and its related processing and sizing, risk & resource assessment.
Capability includes:
. 2D seismic planning
. 3D seismic planning
. Field capture
. Seismic processing
. Seismic interpretation
. Geophysical information management*

- 3.5.1 2D Seismic Planning
- 3.5.2 3D Seismic Planning
- 3.5.3 Field Capture
- 3.5.4 Seismic Processing
- 3.5.5 Seismic Interpretation
- 3.5.6 Geophysical Information Management

---

### 4. Well Management

> *Ability to plan, execute and close out a well.*

#### 4.1 Well Information Management
*Ability to create, maintain, organize and archive data and information regarding wells.*

- 4.1.1 WIM Process Management
- 4.1.2 WIM Data Management
- 4.1.3 WIM Data Integration
- 4.1.4 WIM Data Analytics

#### 4.2 Well Design & Planning
*Ability to enable the processes and engineering applications for well analysis, well design and well modeling of individual oil & gas wells.
Capability includes:
. Down hole schematics and well logs
. The designing, executing, and analyzing of preliminary well tests on well performance
. Flow calculations used for correlations of flow pattern, liquid holdup and pressure drop
. Deliverables such as Wells Development Alternatives, Wells Concept Selection, Wells Program, Wells Design and Wells Execution Plans.*

- 4.2.1 Well Licensing
- 4.2.2 Casing Potential
- 4.2.3 Well Type
- 4.2.4 Well Depth Estimation
- 4.2.5 Well Sections Crossed
- 4.2.6 Well Pad Design
- 4.2.7 Earthworks Design
- 4.2.8 Site Survey
- 4.2.9 Well Application Maps
- 4.2.10 Well Locations

#### 4.3 Site Preparation
*Ability to support drilling programs by conducting heavy civil construction, including site earthworks and concrete construction.
Capability includes:
. Site scouting & surveying
. Land clearing
. Site grading, heavy excavation and site preparation
. Soil stabilization
. Road construction & maintenance
. Underground utilities (storm, water, sanitary sewer)
. Erosion control
. Landslide repair and mitigation*

- 4.3.1 Well Pad Tie-in
- 4.3.2 Well Pad Expansion
- 4.3.3 Initial Well Pad
- 4.3.4 Earthworks Execution

#### 4.4 Well Drilling
*Ability to provide drilling schedules and manage execution of drilling plans, milestones and activities from spud through to rig release.
Capability includes:
. Processes and tools that provide drilling schedules and allow assignment of resources to each activity
. Project plans, milestones and dependencies of drilling activities
. Drilling-control systems (geo steering) for real-time borehole adjustments, optimization and automation as well as storing logs of drilling operations
. Deliverables include the Well Report*

- 4.4.1 Well Assignments
- 4.4.2 Vertical Well Drilling
- 4.4.3 Directional Drill
- 4.4.4 Horizontal Well Drilling

#### 4.5 Well Completion
*Ability to set-up a new well for production (from rig release to tie in), performs review of activities performed, and provides turnover processes and documentation. This capability also includes well servicing and interventions carried out on a well during, or at the end, of its productive life which alter the state of the well, provide well diagnostics, and/or manage the production of the well.
Capability includes:
. Processes that make a well ready for production (or injection)
. Preparing the bottom of the hole to the required specifications, running in the production tubing and its associated down hole tools as well as perforating and stimulating, as required
. The process of running in and cementing the casing
. Review and turnover processes
. Work Overs, as required
. Pre-completion activities and activities performed periodically through the well's lifecycle.
. Deliverables such as Well Handover documents*

- 4.5.1 Well Suspension
- 4.5.2 Workover
- 4.5.3 Step Out
- 4.5.4 Reactivation
- 4.5.5 Production
- 4.5.6 Resumption
- 4.5.7 Recomplete
- 4.5.8 Intervention

#### 4.6 Well Testing & Analytics
*Tests and analyzes well performance, covers Assay Management (manages data around liquids and gasses and all related properties and measurements).
Capability includes:
. Allowing users to search, view, analyze and edit product data
. Reviewing underlying laboratory measurements (when linked with Laboratory Information Management System)
. Generating simulations and optimization based on a commercial fractionation model
. Developing product assay configured to the refinery operations suitable for planning & scheduling tools
. Sharing of information within a group of companies from a central assay management centre
. The consolidation of disparate business processes into a single, compliant platform with comprehensive reporting, surveillance and networking capabilities*

- 4.6.1 Pressure Testing
- 4.6.2 Rate Testing
- 4.6.3 Fluid Analysis
- 4.6.4 Mud Gas Analysis

#### 4.7 Well Abandonment
*Supports the abandonment of a well, covers regulatory requirements related to environmental protection and public safety, and manages all activities from identification, wellbore abandonment and surface abandonment.
Capability includes:
. Lease expiration or business requirement for abandonment
. Regulatory requirements related to environmental protection and public safety
. Well identification
. Wellbore abandonment and surface abandonment
Note, software used in this capability is very similar to the software tools used in Well Drilling & Completions related capabilities.*

- 4.7.1 Abandonment
- 4.7.2 Uphole/Downhole Potentials
- 4.7.3 Water Source/Injection Potentials

---

### 5. Project Delivery

> *Ability to conduct engineering analysis, prioritization, design and planning of issues and opportunities, and construction and commissioning activities for operating and planned facilities.*

#### 5.1 Facility Design
*Ability to conduct Process & Project Engineering analysis, prioritization, design and planning of process issues and opportunities for operating and planned facilities.
Capability includes:
. Process modelling
. Equipment & instrument sizing
. Process feasibility studies
. Debottlenecking
. Capacity planning
. Economic analysis
. Demand intake & prioritization
. Initial scoping
. Detailed engineering
. Project scheduling
. Cost estimating
. Project controls*

- 5.1.1 Process Modelling
- 5.1.2 Equipment & Instrument Sizing
- 5.1.3 Process Feasibility Studies
- 5.1.4 Debottlenecking
- 5.1.5 Capacity Planning
- 5.1.6 Economic Analysis
- 5.1.7 Demand Intake & Prioritization
- 5.1.8 Initial Scoping
- 5.1.9 Detailed Engineering
- 5.1.10 Project Scheduling
- 5.1.11 Cost Estimation
- 5.1.12 Project Controls

#### 5.2 Offshore Design

*(No description in ServiceNow)*

- 5.2.1 Detail Marine Engineering Civil Design
- 5.2.2 Offshore Drill Design
- 5.2.3 Topside Design

#### 5.3 Offshore Tow-out & Installation

*(No description in ServiceNow)*

- 5.3.1 Marine Transport Provisioning
- 5.3.2 Tow-out Topside/CGS
- 5.3.3 Installation Topside

#### 5.4 Facility Construction
*Ability to manage physical construction of facilities (operating and planned) including but not limited to plants, offsites and camps, and includes all activities from earthworks up to pre-commission.
Capability includes:
 . Construction planning
 . Constructability analysis
 . Detailed scheduling
 . Construction management
 . RFI/RFC management
 . Progress management*

- 5.4.1 Construction Planning
- 5.4.2 Constructability Analysis
- 5.4.3 Detailed Sheduling
- 5.4.4 Construction Management
- 5.4.5 RFI/RFC Management
- 5.4.6 Progress Management

#### 5.5 Offshore Construction Management

*(No description in ServiceNow)*

- 5.5.1 Topside Fabrication & Construction
- 5.5.2 Offshore Drill Construction

#### 5.6 Offshore Subsea Preparation

*(No description in ServiceNow)*

- 5.6.1 Marine Risk Installation
- 5.6.2 Dredging
- 5.6.3 Subsea Tieback

#### 5.7 Facility Commission & Handover
*Ability to manage commissioning activities for facilities (operating and planned).
Capability includes:
 . Commissioning analysis
 . Detailed scheduling
 . Activity coordination
 . Deficiency management
 . Commissioning orchestration*

- 5.7.1 Commissioning Analysis
- 5.7.2 Detailed Scheduling
- 5.7.3 Activity Coordination
- 5.7.4 Deficiency Management
- 5.7.5 Commissioning Orchestration
- 5.7.6 Onshore/Offshore Commissioning & Hookup

---

### 6. Reclamation & Remediation

> *(No description in ServiceNow)*

#### 6.1 Asset Retirement Management
*Includes divestment planning through to asset marketing, vendor engagement and administrative closure.
Capability includes:
. The supports for longer term capital allocation and planning decisions based on fluctuating commodity prices
. Shifting energy politics and supply
. Demand economics
. Note - there is a strong linkage between this capability and the Acquisition capability in Explore's Asset Development group.*

*(No L3 capabilities)*

#### 6.2 Asset Reclamation Management
*Supports the identification and management of addressing surface reclamation issues and subsurface contamination.
Capability includes:
. Operational work activities
. Work to obtain regulatory certificates
. Regulatory audits.*

*(No L3 capabilities)*

#### 6.3 Site Remediation Management

*(No description in ServiceNow)*

*(No L3 capabilities)*

---

### 7. Site Operations Management

> *Ability to support day to day safe and sustainable operations of producing assets (facilities/plant/wells) by utilizing tangible (sensors, humans, equipment) and non-direct means.*

#### 7.1 Operations Planning
*Ability to integrate management, coordination and execution of required primary and supporting operational activities and resources in support of optimized asset production.
Capability includes:
. Outage Planning
. Technology Integration
. Cost Mgmt
. Chemical Inventory
. Throughput Mgmt
. Energy Mgmt*

- 7.1.1 Outage Planning
- 7.1.2 Technology Integration
- 7.1.3 Cost Management
- 7.1.4 Chemical Inventory
- 7.1.5 Throughput Management
- 7.1.6 Energy Management

#### 7.2 Facilities Control
*Ability to execute process control for whole areas through DCS manipulation (Distributed Control System) and area operator direction. This capability includes enormous data amount collection, custom trends watching and setpoints (pressure, temperature, flow, balance, ratio, etc.) and control schemas (manual, automatic, cascade, etc.) adjustments to optimize the area throughput safely and efficiently.
Capability includes:
. DCS Operations
. Fluid Volume Mgmt
. Troubleshooting
. Bypass Control
. Alarm Mgmt
. Production Interruption Reporting
. Well Targets Mgmt*

- 7.2.1 Equipment Monitoring & Control -- *Enables the processes and applications to monitor, report, and analyze process control systems, and field data capture used in managing real-time and ongoing operations. Capability includes: Field Data Capture or Supervisory Control & Data Acquisition (SCADA) and Advanced Process Control (APC); the control of operations of units and equipment via set points, notifications and alerts as well as providing centralized system monitoring in real-time; control actions performed automatically by Remote Terminal Units (RTUs) or by programmable logic controllers (PLCs); allowing operators to change the set points and enable alarm conditions; feedback control loops; APC's multi-variable controllers for maintaining processes at their optimal operating point; process stabilization by controlling the dynamic relationships between variables; web-based interfaces for viewing or changing controller configurations; the assessment of model accuracy; allows implementation of targets from production planning and scheduling.*
- 7.2.2 Fluid Volume Management
- 7.2.3 Troubleshooting
- 7.2.4 Bypass Control
- 7.2.5 Alarm Management
- 7.2.6 Production Interruption Reporting
- 7.2.7 Production Targets Management

#### 7.3 Maintenance & Turn Around

*(No description in ServiceNow)*

*(No L3 capabilities)*

#### 7.4 Process/Facilities Optimization
*Ability to investigate candidate opportunities to improve production, stability and operational costs. This is a deeper level of optimization compared to the physical process or control room optimization. Engineers evaluate changing conditions, history, bottlenecks and new requirements. Engineering principles are used to change allowances, setpoints, materials, equipment and/or flows to redesign their system while maintaining process safety.
Capability includes:
. DCS Engineering
. Process Engineering
. Facility Engineering
. Maintenance Engineering
. Production Info Mgmt*

- 7.4.1 Process Modelling & Simulation -- *Ability to manage the conceptual design, optimization, business planning, asset management and performance monitoring necessary in plant operations. Capability includes: supporting process design, equipment sizing, and preliminary cost estimation within one environment; configuring complex, multi-unit simulations to incorporate key units; performing "what-if" scenarios using kinetic based models to quantify effect of changes to feedstock and key process operating conditions; providing data vectors for maintenance of product models, such as liquid propane (LP).*

#### 7.5 Operations Management
*Supports the planning, scheduling and execution of operator rounds, or shifts, as part of operating a producing asset (facility, plant or well).
Capability includes:
. Safe Operations
. The management of available resources and assignments based on skills and clearance for specific areas or types for work
. Planning of operator rounds with information on routes, equipment data
. Log book to archive narratives on operator rounds, shifts or specific equipment
. Assignment of actions from the log book to resources
. The management of a full workflow around work orders and related activities allowing capture of work requests and prioritization
. The planning of work activities by matching work requests to available resources and the transformation into concrete work orders
. The approval process including cost approval, work permits and safety regulations
. The capture of the actuals from work orders including involved resources, materials / equipment used and actual costs*

- 7.5.1 Safe Operations
- 7.5.2 Operations Monitoring -- *Ability to perform daily work using auditory, tactile, visual, and olfactory senses within plant and field. This capability includes collecting information through data collection routes, daily rounds and required sampling. It also includes recording collected information for shift handover. Capability includes: Daily Rounds, Reading Collection, Samples (Take/Test), Shift Logs, Troubleshooting, Fluids Movement, Physical Process Adjustments.*
- 7.5.3 Optimize & Improve Operations -- *Optimizes operations through the leveraging of regional improvement initiatives and extending to other areas of the company to improve corporate safety, production, and efficiency. Capability includes: Optimizing and improving operations such as artificial lift (rod pumping) optimization analyses, Opportunity Identification, Improving surface operations as part of technical excellence, Deliverables such as Operational Feasibility Assessments, Opex Estimates and Value Improving Practices (VIP) Plans. Note: Optimize & Improve Operations capability typically leverages Project Simulation activities which expand unit operations from simulator output to equipment models using proprietary mapping technology and then calculates preliminary sizes for the enhanced equipment items.*

#### 7.6 Control of Work
*Ability to provide integrated management of business-critical maintenance processes, made up of hazard identification and Risk Assessment (RA), Permit to Work (PTW) and Isolation Management (IM).
Capability includes:
. Permitting
. Isolation Management
. Hazard Management
. SimOps - simultaneous operations*

- 7.6.1 Permitting
- 7.6.2 Isolation Management
- 7.6.3 Hazard Management
- 7.6.4 Simultaneous Operations

#### 7.7 Field Data Capture
*Ability to collect production, operations, and compliance data from the field in a variety of ways.*

*(No L3 capabilities)*

---

### 8. Maintenance Management

> *Ability to maintain the reliability and integrity of operating assets.*

#### 8.1 Maintenance Planning
*Ability to create, maintain and review actionable plans to maintain facilities.
Capability includes:
.Work Order planning
.Turnaround planning
.Equipment mgmt
.Rental mgmt
.Inventory mgmt
.Spares mgmt*

- 8.1.1 Work Order Planning
- 8.1.2 Turnround Planning
- 8.1.3 Equipment Management
- 8.1.4 Rental Management
- 8.1.5 Inventory Management (Maintenance)
- 8.1.6 Spares Management

#### 8.2 Maintenance & Reliability
*Ability to maintain information and history on facilities (equipment, gear, piping, pipelines, instrumentation and process) to assess failure and degradation risks so that changes, swaps or repairs can be made before major issues occur.
Capability includes:
.Asset reliability mgmt
.Preventative-Maintenance program
.Engineering Information mgmt
.Pipeline integrity mgmt
.Facility integrity mgmt
.Electrical integrity mgmt
.Process integrity mgmt
.Rotating equip mgmt*

- 8.2.1 Asset Reliability Management
- 8.2.2 Preventative Maintenance
- 8.2.3 Engineering Information Management
- 8.2.4 Pipeline Integrity Management
- 8.2.5 Facility Integrity Management
- 8.2.6 Electrical Integrity Management
- 8.2.7 Process Integrity Management
- 8.2.8 Rotating Equipment Management

#### 8.3 Physical Maintenance
*Ability to daily assess current conditions of active and dormant assets, rectifying issues, ensuring consistent proper function. This capability assumes work within facilities (plant and wells).
Capability includes:
. Inspection
. Troubleshooting
. Instrumentation repair
. Electrical repair
. Mechanical repair
. Rotating equipment repair*

- 8.3.1 Inspection
- 8.3.2 Equipment Troubleshooting
- 8.3.3 Instrumentation Repair
- 8.3.4 Electrical Repair
- 8.3.5 Mechanical Repair
- 8.3.6 Rotating Equipment Repair

---

### 9. Resource Management

> *Ability to manage various site resources required to support operations, maintenance, construction, drilling, completions, earthworks and other teams.*

#### 9.1 Resource Scheduling
*Ability to schedule resources and equipment for use in the field.
Capability includes:
. Scheduling of required staff & contractors
. Tracking of location for assets and resources
. Loaner equipment
. Gannt overview of equipment dependencies
. Cost allocation for assets and equipment usage*

- 9.1.1 Required Staff & Contractor Scheduling
- 9.1.2 Asset & Resource Location Tracking
- 9.1.3 Loaner Equipment
- 9.1.4 Equipment Dependency Planning
- 9.1.5 Cost Allocations for Assets & Equipment Usage

#### 9.2 Travel & Accommodation
*Ability to support the processes, utilities, tools and equipment to plan, coordinate and manage site based travel & accommodation (Camps); including places to stay, waste management, power generation, potable water and catering, housekeeping & janitorial, maintenance, logistics & transportation, etc.
This capability also supports overall corporate commercial travel and fleet management.*

- 9.2.1 Site Based Travel & Accomodation
- 9.2.2 Corporate Commerical Travel & Fleet Management
- 9.2.3 Offshore Accomodations Support Vessel
- 9.2.4 Offshore Personnel Logistics Management

#### 9.3 Dispatch Management
*Ability to optimize trucking routes and movement of all large loads into and within our operating areas.
Capability includes:
. Facilities Fluid Transfer
. Waste Hauling
. Chemical Receiving
. Solvent Receiving
. Weigh Scale Mgmt
. Construction Load Receiving
. Well Delivery Load Support*

- 9.3.1 Facilities Fluid Transfer
- 9.3.2 Waste Hauling
- 9.3.3 Chemical Receiving
- 9.3.4 Solvent Receiving
- 9.3.5 Weigh Scale Management
- 9.3.6 Construction Load Receiving
- 9.3.7 Well Delivery Load Support

#### 9.4 Lab Services Management
*Ability to operate laboratory services, manage laboratory collection, analyses (internal and external) and information dissemination.
Capability includes:
. In-House Lab Testing
. External Lab Mgmt
. Sample Results Mgmt
. Sample Collection Mgmt
. Lab Services Mgmt*

- 9.4.1 In-House Lab Testing
- 9.4.2 External Lab Testing
- 9.4.3 Sample Results Management
- 9.4.4 Sample Collections Management
- 9.4.5 Lab Service Management

#### 9.5 Certification Management
*Ability to identify and manage "unique to site" operators and maintenance personnel competencies. This capability includes tracking of personnel competency based on shifts worked in specific areas or on specific equipment.
Capability includes:
. Training & Qualification
. Orientations
. Tickets & Credentials
. Competency & Assurance*

- 9.5.1 Training & Qualification
- 9.5.2 Orientation
- 9.5.3 Tickets & Credentials
- 9.5.4 Competency & Assurance

---

### 10. Supply & Logistics

> *(No description in ServiceNow)*

#### 10.1 Supply Management

*(No description in ServiceNow)*

- 10.1.1 Receive Production Forecasts
- 10.1.2 Forecast Condensate
- 10.1.3 Forecast Offshore Crude Production
- 10.1.4 Forecast Natural Gas Production
- 10.1.5 Forecast Power
- 10.1.6 Forecast Annual Renewable Fuels & Carbon Credits

#### 10.2 Product Movement
*Ability to enable configuration, monitoring and tracking of stored oil movements between tanks, terminal units and cut-off inventory of tanks.
Capability includes:
. Information from a real-time database and a relational-database, that performs automatic monitoring and control of any tank or flow
. Transfer order generation and the monitoring / control of operations between units, docks, feed tanks, product tanks, and intermediate storage tanks, as well as pipeline and marine shipments
. Nominations of materials entering and leaving the facility
. The controls on every step involved in shipping even before the vessel docks.*

- 10.2.1 Manage Terminal/Storage Movements & Volumes
- 10.2.2 Manage Blended Inventory
- 10.2.3 Manage Month End Volumes & Volumetric Plan

#### 10.3 Transport Management
*Ability to manages truck and rail transport scheduling and dispatch needed for specific production strategies and operational schedules. May also include dispatch of auxiliary equipment, water trucks, crew lineup, fuel service, inventory reporting and payload analysis.
Capability includes:
. Onboard systems linking the vehicle to a central management system via cellular or other wireless technology
. The tracking of current position of a vehicle via GPS and providing the location to a central fleet management or logistics scheduling solution
. Automated tracking details like mileage and fuel consumption
. Unloading of products only at specified locations and with the exact volume specified in transport order
. Remote vehicle disabling systems that can prevent an engine from starting, prevent movement of a vehicle and stop or slow an operating vehicle.
Ability to Manage Terminals: Monitors progress of product movements in and out of terminal and compares stock levels in terminal tank farms to demand levels.
Ability to Manage Harbours: Provides ocean terminal and traffic management services. Often serves as the interface between third party, pipeline and harbor terminal processes at ports of departure and arrival around the world.*

- 10.3.1 Dispatch Management
- 10.3.2 Manage Terminal Movements
- 10.3.3 Manage Harbours

#### 10.4 Pipeline Management & Change
*Ability to manage schedules for pipeline operations and maintenance including pipeline integrity systems for viewing, monitoring, and control.
Capability includes:
. The creation and tracking of nominations to reconcile them with movements
. Data or supports accounting of product movements and invoicing of services
. Simulation of pipelines to analyze potential routing and improve layout or configuration of the pipeline.*

- 10.4.1 Pipeline Operations
- 10.4.2 Manage Pipeline Nominations & Allocations -- *Ability to verifies and confirms nominations and allocation of actual volumes with shippers and operators. Capability includes: Providing imbalance control including OBAs, nominations, allocation schemes or confirmations.*

#### 10.5 Distribution Planning & Scheduling
*Ability to plan the distribution and movement scheduling of crude, semi-finished and finished products from refineries to terminals and on to retail stations (or B2B clients) using pipelines, ships, rail or trucks.
Capability includes:
. Generating a distribution plan across sites, modes of transportation and over multiple time periods optimizing related costs / fees and transportation lead time
. Identifying long/short balances by product, region and location using demand forecast & production plans.
. Developing scenarios and performs "what-if" analysis
. Supporting spot, term and exchange agreements in order to evaluate all make-or-buy options
. Monitoring inventories and costs in terminals
. Evaluating alternative sourcing locations and exchanges
. Optimizing truck loading and replenishment plans for secondary distribution
. Developing a proportional dispatch plan to reduce overstock of slow moving items.
. Providing visibility of logistics, costs, inventories, product quality, shipment status, etc.
. Managing available pipelines, ships, barges, rail or trucks and related networks / routes.
. Ensuring that constraints regarding product quality assurance, safety considerations, resource availability, etc. are considered in the creation of daily schedules.*

- 10.5.1 Plan Distribution and Product Movements
- 10.5.2 Manage Truck Demand and Planned Usage
- 10.5.3 Manage Rail Demand and Planned Usage
- 10.5.4 Manage Pipeline Demand Planned Usage
- 10.5.5 Manage Marine Demand and Planned Usage
- 10.5.6 Evaluate Alternatives & Perform What-If Analysis
- 10.5.7 Identify Balance Misalignment using Demand Forecasting & Production Plan

#### 10.6 Manage Product Storage & Inventory

*(No description in ServiceNow)*

- 10.6.1 Calculate Actual Storage & Inventory Volumes
- 10.6.2 Provide Visibility of Product & Storage Inventory

---

### 11. Marketing & Trading

> *(No description in ServiceNow)*

#### 11.1 Forecast & Demand Management
*Ability to manage the sales forecasting process and generates an integrated view of forecasted demand based on multiple inputs throughout the organization and external sources.
Capability includes:
. Defining sales goals and guiding various downstream functions including sales & operations planning
. Reporting revenues by account, opportunity, product line, project, partner, division, organization and / or employee
. Enabling analysis of sales trends and areas in the demand forecast model that may need to be realigned to improve forecast accuracy.
. Performing 'what-if' simulations of the supply-demand balance based on specified scenarios (e.g. sales increases)
. Monitoring and reviewing industry, government, and board proposals with a focus on the impact to the company's position
. Managing recurring revenues, multiple currencies and supporting robust currency conversion
. May include collaborative functioning to allow ground level users to update the forecast based on specific time period or event driven sales activity.*

- 11.1.1 Market Fundamentals Forecasting
- 11.1.2 Market Analysis
- 11.1.3 Dynamic Forward Trading
- 11.1.4 Position Hedging
- 11.1.5 Geographical Arbitrage
- 11.1.6 Intra Plan Trading

#### 11.2 Commodity Trading
*Ability to buy and sell oil and gas on a day to day and long term basises.*

- 11.2.1 Pre-Trade Analysis
- 11.2.2 Trade Approvals
- 11.2.3 Strategy Approvals
- 11.2.4 Physical Trade Execution
- 11.2.5 Trade Modifications
- 11.2.6 Exchange Trades
- 11.2.7 Environment/Renewables Deals
- 11.2.8 Trade Reporting

#### 11.3 Pricing & Quoting
*Ability to deliver incremental gross profits from better pricing.
Capability includes:
. A single, more efficient pricing system applicable to all channels of trade
. Providing a way to measure competitor strength and deal with new entrants to the market
. Ensuring consistency of pricing across the network with zero pricing errors
. Enabling visibility of, and more rapid response to, the competitive landscape.*

- 11.3.1 Manage Published Prices
- 11.3.2 Align Price View/Assumptions
- 11.3.3 Manage Price Forecast
- 11.3.4 Analyze Price Variance
- 11.3.5 Validate Spot Prices

#### 11.4 Settlement
*Ability to reconcile trades and related payment activities.
Capability includes:
. Statements for producers, invoices for end users and other customers, and the execution of trade payment
. Payee matching as part of anti-fraud
. Back office functions that manage inventory and stock levels of all wet and dry products
. Product management administering different product categories
. Enhanced reporting (e.g. customizable shift & day reports, consolidated reports by day, etc.).*

- 11.4.1 Settle Crude
- 11.4.2 Settle Natural Gas
- 11.4.3 Settle Products & Intermediaries
- 11.4.4 Settle Other Commodities
- 11.4.5 Settle 3rd Party Vessel & Pipeline Payments
- 11.4.6 Settle Financial Over the Counter Trades
- 11.4.7 Settle Exchange Trades
- 11.4.8 Settle Railcars & Trucks
- 11.4.9 Settle Vessels & Barges
- 11.4.10 Settle Terminals & Leased Storage
- 11.4.11 Settle First Purchaser/Leases/Equity
- 11.4.12 Settle Brokers
- 11.4.13 Manage Settlement Disputes
- 11.4.14 Manage Settlement Documentation

#### 11.5 Customer Relationship Management
*Ability to covers the manner in which the company interacts and engages its customers. Underlying processes include "Initiate Relationship", "Build Relationship", and "Maintain Relationship".
Capability includes:
. The implementation of a strategy to reward loyal and important customers
. Reward and benefit programs to the customer
. Handling of all inbound contacts
. The administration of one database for all inbound contacts.*

- 11.5.1 Partner Relationship Management -- *Ability to strategically manage business relationships with partner companies who process and sell corporate product.*
- 11.5.2 Manage Counterparty Information
- 11.5.3 Manage Contracts

#### 11.6 Market Risk Management

*(No description in ServiceNow)*

- 11.6.1 Maintain Book Structure
- 11.6.2 New Product Approval
- 11.6.3 Manage Delegation of Authority
- 11.6.4 Setup & Manage Price Curves
- 11.6.5 Perform Day & Month End Processes
- 11.6.6 Manage Risk Limits
- 11.6.7 Measure Risk
- 11.6.8 Monitor Risk Policy Compliance
- 11.6.9 Perform Position Analysis
- 11.6.10 Perform P&L Analysis
- 11.6.11 Manage & Run Risk Scenarios
- 11.6.12 Conduct Advanced Analytics
- 11.6.13 Manage Risk Reporting
- 11.6.14 Manage Volatilities & Correlations

#### 11.7 Credit Risk Management
*Ability to analyze the risks inherent in commodity trading on a real-time basis including calculating position and exposure, profit and loss (P&L), risk analytics, VaR calculations and "what-if"-analyses. Included within this capability are credit risk reviews.
Capability includes:
. Commodity trading and risk management on a real-time basis including calculating position and exposure, identifying hedging options and settling hedging deals
. Industry and market data feeds from various sources to understand pricing, directionality and volatility
. Real-time P&L, risk analytics, VaR calculations and "what-if"-analyses
. Security measures, audit trails and internal controls to help make sure that trading and supply operations pass internal audits
. Deliverables such as Credit Risk Reviews, which are conducted on a periodic basis, as well as Swaps, Options and Financial Futures.*

- 11.7.1 Initial & Ongoing Counterparty Credit Reviews
- 11.7.2 Manage Credit Parties
- 11.7.3 Manage Credit Limits
- 11.7.4 Manage Inbound & Outbound Collateral
- 11.7.5 Calculate Credit Exposure
- 11.7.6 Forecast & Validate Derivative Margining
- 11.7.7 Monitor & Analyze Credit
- 11.7.8 Advanced Credit Risk Analytics
- 11.7.9 Credit Valuation Adjustments
- 11.7.10 Manage Credit Risk Reporting

---

### 12. Optimization

> *(No description in ServiceNow)*

#### 12.1 Optimize Supply, Manafacturing, Distribution

*(No description in ServiceNow)*

*(No L3 capabilities)*

---

### 13. Manufacturing & Processing

> *(No description in ServiceNow)*

#### 13.1 Plan Manufacturing
*Models production assets across various operating facilities and storage terminals in order to optimize operations and schedule production.
Capability includes:
. Supply & demand balancing, inventory management, movement scheduling, nominations management, exchange management and cost optimization
. Decision support for product volumes, transportation planning and economic analysis of the buy vs. make vs. trade vs. exchange and export/import alternatives
. Data visualization, reporting, and alerting capabilities for strategic planning as well as operational conditions
. Production Scheduling (simulates & schedules production processes)
. Scheduling and optimization of refining activities, including crude receipts, process operations, product blending and product shipping
. Improvements to the processes associated with physical operations - such as scheduling and optimization of operations across product receipts, product blending, product shipping, etc.
. Multiple users sharing the same view of the schedule, which improves coordination between various schedulers with view to other departments
. Changes to the schedule that are managed, and updates are provided to all users
. A combination of three typical approaches to scheduling: simulation, linear programming and expert systems to provide an event based operating plan for execution support.*

*(No L3 capabilities)*

#### 13.2 Schedule Manufacturing

*(No description in ServiceNow)*

*(No L3 capabilities)*

#### 13.3 Execute Manufacturing, Blending & Processing

*(No description in ServiceNow)*

*(No L3 capabilities)*

#### 13.4 Refinery Optimization

*(No description in ServiceNow)*

*(No L3 capabilities)*

---

### 14. Commercial Products

> *(No description in ServiceNow)*

#### 14.1 Commercial Products Strategy & Planning

*(No description in ServiceNow)*

- 14.1.1 Sales Channel Planning
- 14.1.2 Forecasting & Demand Management
- 14.1.3 Sales Development Portfolio

#### 14.2 Commercial Site Management

*(No description in ServiceNow)*

*(No L3 capabilities)*

#### 14.3 Execute & Monitor Commercial Sales & Operations

*(No description in ServiceNow)*

- 14.3.1 Contracts Management
- 14.3.2 Update Counterparty Information
- 14.3.3 Convey Counterparty
- 14.3.4 Terminate Contract
- 14.3.5 Monitor Contract Expiry
- 14.3.6 Create New Counterparty
- 14.3.7 Terminate Counterparty
- 14.3.8 Create New/Update Contract
- 14.3.9 Manage Carrier Contracts (Heavy Oil)
- 14.3.10 Annual GT & C Notification (Cdn A&IP Only)

---

### 15. Retail

> *(No description in ServiceNow)*

#### 15.1 Point of Sale System

*(No description in ServiceNow)*

*(No L3 capabilities)*

#### 15.2 Forecourt & Pump Control

*(No description in ServiceNow)*

*(No L3 capabilities)*

#### 15.3 Payment

*(No description in ServiceNow)*

*(No L3 capabilities)*

#### 15.4 Merchandising

*(No description in ServiceNow)*

*(No L3 capabilities)*

#### 15.5 Network Management

*(No description in ServiceNow)*

*(No L3 capabilities)*

#### 15.6 Cards Management

*(No description in ServiceNow)*

*(No L3 capabilities)*

---

### 16. Supply Chain Management

> *Ability to manage the flow of goods and services from suppliers to facility delivery and operational teams.*

#### 16.1 Supply Management Planning & Budgeting
*Ability to define materials demand, produce plan and required budget to support overall materials supply for the organization.
Capability includes:
. Requirement and Organization Assessment
. Category Strategy Development*

- 16.1.1 Requirement & Organization Assessment
- 16.1.2 Category Strategy Development

#### 16.2 Procurement/Payment Management
*Ability to request, purchase, receive, pay for, and perform accounting for goods and services.
Capability includes:
. Procure
. Receiving
. Pay*

- 16.2.1 Procure
- 16.2.2 Receiving
- 16.2.3 Pay

#### 16.3 Sourcing & Contracting
*Ability to analyze requirement, request quotation and negotiate a contract for best products and services, based on previously established sourcing strategy.
Capability includes:
. Sourcing
. Contracting*

- 16.3.1 Sourcing
- 16.3.2 Contracting

#### 16.4 Supplier Management
*Ability to identify, evaluate and engage with existing or potential new suppliers for purposes of delivering specific services or products to an organization or its constituents.
Including
. Supplier Lifecycle Management
. Supplier Relationship Management*

- 16.4.1 Supplier Lifecycle Management
- 16.4.2 Supplier Relationship Management

#### 16.5 Materials Management
*Ability to plan and determine total material requirements and manage inventory level across operating locations.
Capability includes:
. Planning
. Inventory Management
. Warehouse Management
. Logistics Management*

- 16.5.1 Planning
- 16.5.2 Inventory Management (Materials)
- 16.5.3 Warehouse Management
- 16.5.4 Logistics Management

#### 16.6 Supply Chain Risk Management & Data Integrity
*Ability to implement and manage risks along the supply chain based on continuous data and risk assessment, with the objective of reducing vulnerability and ensuring continuity.
Capability includes:
. Risk Management
. Data Integrity*

- 16.6.1 Supply Chain Risk Management
- 16.6.2 Supply Chain Data Integrity

---

### 17. Financial Management

> *Ability to plan, direct, monitor, organize, control, and report on the monetary aspects and resources of the organization.*

#### 17.1 General Accounting & Budgeting
*Ability to address critical financial functions such as accounting, accounts payable, accounts receivable, collections, budgeting, forecasting, working capital management, etc.
Capability includes:
. Manage general invoicing and payment enablement
. Joint venture equity accounting
. Reporting analysis, consolidations
. Account reconciliations
. Perform month-end close
. Rerform transaction processing
. Maintain master data (including JV)
. Budgeting and forecasting*

- 17.1.1 Manage General Invoicing & Payment Enablement
- 17.1.2 Joint Venture Equity Accounting
- 17.1.3 Reporting Analysis, Consolidation
- 17.1.4 Account Reconcilliation
- 17.1.5 Perform Month-End Close
- 17.1.6 Perform Transaction Processing
- 17.1.7 Maintain Master Data (including JV)
- 17.1.8 Budgeting & Forecasting

#### 17.2 Capital Asset Management
*Ability to track and manage all aspects of capital valuation and related depreciation expenses.
Capability includes:
. Perform fixed asset accounting
. Perform project accounting
. Allocate capital budget*

- 17.2.1 Perform Fixed Asset Accounting
- 17.2.2 Perform Project Accounting
- 17.2.3 Allocate Capital Budget

#### 17.3 Tax Management
*Ability to provide financial functions relating to tax management within all the different tax jurisdictions.
Capability includes:
. Plan and manage use taxes
. Property taxes
. Income taxes
. Tax relationships for entities
. Tax reporting
. Tax compliance
. Tax provisioning*

- 17.3.1 Plan & Manage Usage Taxes
- 17.3.2 Property Taxes
- 17.3.3 Income Taxes
- 17.3.4 Tax Relationships for Entities
- 17.3.5 Tax Reporting
- 17.3.6 Tax Compliance
- 17.3.7 Tax Provisioning

#### 17.4 Treasury Management
*Ability to address management of cash and financing, ensuring safety of principal and sufficient liquidity.
Capability includes:
. Manage cash accounts
. Disbursements
. Manage liquidity
. Manage debt
. Manage investments*

- 17.4.1 Manage Cash Accounts
- 17.4.2 Disbursements
- 17.4.3 Manage Liquidity
- 17.4.4 Manage Debt
- 17.4.5 Manage Investments

#### 17.5 Production Accounting
*Ability to deliver critical production information by performing daily mass balancing and reconciliation using data on opening and closing inventories, receipts, shipments, transfers, process unit charges and yield data.
Capability includes:
. Maintain master data (including ownership changes)
. Process and receive revenue distributions
. Manage royalties
. Monitor production loss*

- 17.5.1 Maintain Master Data (including Ownership changes)
- 17.5.2 Process & Receive Revenue Distribution
- 17.5.3 Manage Royalties
- 17.5.4 Monitor Production Loss

#### 17.6 Commodity Accounting

*(No description in ServiceNow)*

- 17.6.1 Manage Accounting Treatments
- 17.6.2 Manage Commodity Tax Setup (Locations)
- 17.6.3 Update Deferred Taxes (US)
- 17.6.4 Manage Accruals for Manufacturing Trades
- 17.6.5 Manage Cash Allocation
- 17.6.6 Manage Inventory Valuation
- 17.6.7 Manage Mid-Month Forecast
- 17.6.8 Apply Accounting Policy & Procedures
- 17.6.9 Manage Commodity Tax Setup (Product)
- 17.6.10 Manage Netbacks
- 17.6.11 Manage AR/AP (Actuals)
- 17.6.12 Manage Trading Sub-Ledger
- 17.6.13 Manage Inventory Accruals
- 17.6.14 Manage Inter-Departmental Profit/Expense (IDPE)
- 17.6.15 Manage Commodity Tax Exemptions
- 17.6.16 ManageYear End Commodity Tax US.
- 17.6.17 Manage Accruals
- 17.6.18 Manage True-Ups
- 17.6.19 Manage Inventory Reconcilliation
- 17.6.20 Manage Month-End
- 17.6.21 Manage Month-End Close (Day 1)

#### 17.7 Joint Venture Accounting

*(No description in ServiceNow)*

*(No L3 capabilities)*

---

### 18. Human Resources

> *Ability to assess, mentor, compensate, terminate, and otherwise coordinate individuals who have, plan to have, or have had a legal agreement with the organization, which includes compensation and other benefits, on a temporary or permanent basis.*

#### 18.1 Talent Acquisition
*Ability to acquire skilled workers to meet organizational needs.
Capability includes:
. Recruitment
. Workforce Planning
. Campus and Fuel Programs
. Position Management*

- 18.1.1 Recruitment
- 18.1.2 Workforce Planning
- 18.1.3 Campus & Fuel Program
- 18.1.4 Position Management

#### 18.2 Talent Management
*Ability to processes to onboard, develop, motivate, and retain high-performing employees.
Capability includes:
. Performance Management
. Feedback
. 360 Reviews
. Succession Planning*

- 18.2.1 Performance Management
- 18.2.2 Feedback
- 18.2.3 360 Reviews
- 18.2.4 Succession Planning

#### 18.3 Total Rewards
*Ability to establish a compensation range and compensation criteria for a given job including monetary and non-monetary value to be exchanged for the work done and role played by a human resource.
Capability includes:
. Compensation
. Benefits
. Pension
. Payroll*

- 18.3.1 Compensation
- 18.3.2 Benefits
- 18.3.3 Pensions
- 18.3.4 Payroll

#### 18.4 People Experience
*Ability to encapsulate what people encounter and observe over the course of their tenure at an organization.
Capability includes:
. Onboarding
. Offboarding
. Veteran Hiring
. Physical and Mental Health
. Indigenous
. Meeting and Events*

- 18.4.1 Onboarding
- 18.4.2 Offboarding
- 18.4.3 Veteran Hiring
- 18.4.4 Physical & Mental Health
- 18.4.5 Indigenous
- 18.4.6 Meeting & Events

#### 18.5 Organizational Development
*Ability to changes and improve processes and structures that are part of Human Resource responsibility, incl. processes and systems related to performance management, talent management, diversity and employee wellness. Capability includes:
. COMS
. Controls and Reporting
. Job Profiles*

- 18.5.1 COMS
- 18.5.2 Controls & Reporting
- 18.5.3 Job Profiles

#### 18.6 Professional Development
*Ability to manage employee's professional development.
Capability includes:
. Learning Management
. Curriculum Management
. Technical Development
. Leadership Development
. Mentoring*

- 18.6.1 Learning Management
- 18.6.2 Curriculum Management
- 18.6.3 Technical Development
- 18.6.4 Leadership Development
- 18.6.5 Mentoring

#### 18.7 HR Operations/Enablement
*Ability to perform administrative services, recruitment, job analysis, and employee relationship management; and ability to provide guidance and empower employees to continue to learn, develop, and get the necessary training to continue providing quality results.
Capability includes:
. Internal HR Support
. Reporting and Analytics
. Data Governance
. Request Prioritization
. People Services
. Taken Acquisition
. HR Business Partners
. Workforce Planning*

- 18.7.1 Internal HR Support
- 18.7.2 Reporting & Analytics
- 18.7.3 HR Data Governance
- 18.7.4 Request Prioritization
- 18.7.5 People Services
- 18.7.6 HR Business Partners

---

### 19. Information Technology

> *Ability to assess, deploy and operate digital technologies that store, retrieve, transmit and manipulate data or information.
> \* Leverage IT Resources to effectively meet business needs for Information Technology systems.
> \* Proficiency in Identifying, Deploying and Maintaining Information Technology systems.
> \* Technical knowledge and ability to effectively deliver and support IT processes and services.*

#### 19.1 IT Strategy & Governance

*(No description in ServiceNow)*

- 19.1.1 IT Strategy -- *Alignment with business goals; Enable agility and adaptability of information technology services and process to meet changing business needs; Plan for and manage technology change over time; Identify and support adoption of enabling technologies.*
- 19.1.2 Demand Management -- *Demand Intake; Evaluation Workflows; Demand Prioritization; Demand funding.*
- 19.1.3 Service Planning -- *Service Identification; Service need alignment; Service rightsizing and prioritization.*
- 19.1.4 IT Cost Management -- *Cost Efficiency; Budgeting and Financial Planning; Asset and Resource cost optimization; Cost control and allocation; IT Financial Reporting.*
- 19.1.5 IT Governance & Compliance -- *Identify Roles and Responsibilities for IT activities; Define Policies and Guidelines for IT Operations; Standardized IT processes and Workflows; Monitor and manage IT activities; Measure IT performance; Monitor compliance with IT applicable policies, guidelines and processes.*

#### 19.2 Architecture & Portfolio Management
*- Architecture Principles, Practices, Processes and Execution
- Strategic Portfolio Management*

- 19.2.1 Enterprise & Solution Architecture -- *Capability Based Planning; Business Capability Mapping; Strategic Alignment of technology to capability; IT estate visioning; Conceptual solution design; Logical solution design and approval; Technology Selection; Technology Standards.*
- 19.2.2 Information & Data Architecture -- *Data Domains; Data Modeling & Design; Conceptual, Logical & Physical Models; Standards & Conventions.*
- 19.2.3 Integration Architecture -- *Integration & Interoperability; Data centric, Application centric, Event Centric; Integration Governance.*
- 19.2.4 Technology Planning -- *Business Application & Technology Roadmaps; Technology Platform identification and selection; Technology succession planning; Enabling technology planning and evolution.*
- 19.2.5 IT Standards Management -- *Technology Standards Library; Architecture Decisions Library; Technology Selection Process; Technology Reference Architectures; Technology Certification.*
- 19.2.6 Application Portfolio Management -- *Application Discovery; Application Dependency Analysis; Application Asset Management; Application Usage; Application Data Flows and Dependencies; Application Lifecycle Management.*
- 19.2.7 Technology Portfolio Management -- *Technology Discovery; Technology Dependency Analysis; Technology Asset Management; Technology Lifecycle Management.*

#### 19.3 Cyber Security
*- Govern (GV): establish, communicate and monitor cyber security risk management strategy, policy and expectations
- Identify (ID): understand cyber security risks
- Protect (PR): use safeguards to manage CVE's cyber security risks
- Detect (DE): detect and analyze possible cyber security attacks and compromises
- Respond (RS): action detect cyber security incidents
- Recover (RC): restore digital assets and operations affected by a cyber security incident*

- 19.3.1 Cyber Governance -- *Govern (GV): Organizational Context (GV.OC); Risk Management Strategy (GV.RM); Roles, Responsibilities and Authorities (GV.RR); Policy (GV.PO); Oversight (GV.OV); Cybersecurity Supply Chain Risk Management (GV.SC).*
- 19.3.2 Cyber Risk Identification -- *Identify (ID): Asset Management (ID.AM); Risk Assessment (ID.RA); Improvement (ID.IM).*
- 19.3.3 Cyber Protection -- *Protect (PR): Identity Management, Authentication and Access Control (PR.AA); Awareness and Training (PR.AT); Data Security (PR.DS); Platform Security (PR.PS); Technology Infrastructure Resilience (PR.IR).*
- 19.3.4 Cyber Detection -- *Detect (DE): Continuous Monitoring (DE.CM); Adverse Event Analysis (DE.AE).*
- 19.3.5 Cyber Response -- *Respond (RS): Incident Management (RS.MA); Incident Analysis (RS.AN); Incident Response Reporting and Communication (RS.CO); Incident Mitigation (RS.MI).*

#### 19.4 IT Project Management
*- Application of Project Management to IT projects specifically.
- Planning, Scheduling, Resourcing, Execution, Change Management, etc.*

- 19.4.1 Resource Allocation -- *Human and Non-Human Resource Management; Resource allocation; Resource tracking; Resource Optimization; Technical Skill Management.*
- 19.4.2 IT Project Delivery -- *Project Planning and Scheduling; Project Risk Management; Project Budgeting and Cost Control; Stakeholder communication and Reporting; Quality Assurance and Control; Change Management.*
- 19.4.3 IT Project Cost Management
- 19.4.4 ROI Analysis -- *Project cost of ownership including sustainment costs over time; Actual vs projected cost analysis; Goal and Benefit Realization.*
- 19.4.5 Data Management Technology -- *Database Inventory; Data Profiling; Data Warehousing & Business Intelligence Governance; Data Lake; Data Marts; Operational Data Stores; Data Storage Technology; Data Archive; Data Technology Security.*
- 19.4.6 Data Engineering & Integration -- *Data Pipeline and Modeling, Design and Governance; Conceptual, Logical and Physical Models; Standards and Conventions; Integration and Interoperability; Data Centric, Application Centric and Event Centric; Integration Governance.*

#### 19.5 Data & Knowledge Management
*DIKW Hierarchy:
- Data: Raw, individual facts, figures, signals or measurements which indicate something specific, but which are not organized in any way
- Information: Process, contextualized, categorized, calculated data
- Knowledge: Know-how, concept, idea, experience, insight
- Wisdom: Knowledge applied.
Structured Data: Data that is organized into a formatted structure (rows and columns), often stored in databases.
Unstructured Data: Data that does not have a predefined format or structure, such as text files, images, videos, and social media posts.
Semi-structured Data: Data that is partially structured, often containing tags or markers to separate data elements.
Geospatial Data: Data about the locations and shapes of geographic features and the relationships between them.
Data Storage and Data Organization Technologies.*

- 19.5.1 Data Governance -- *Data Management Maturity; Business Cultural Development; Data Literacy; Data & Information Standards & Policies; Data Stewards; Data Security Governance; Data Access Management; Data Security & Privacy (HIPPA, PCI, PII, SOX PPIEDA, GDPR).*
- 19.5.2 Master Data & Data Quality Management -- *Plan Data Quality; Data Manipulation; Data Quality Governance; Data Quality Metrics; Master and Reference Data Governance.*
- 19.5.3 Metadata Management -- *Metadata Management Architecture; Semantics and metadata; Identification, types; Metadata solutions (Business Glossary); Metadata governance; Taxonomy; Catalog; Data Lineage.*
- 19.5.4 Geospatial Data Management -- *Assess, transfer, transform, manage, overlay, process and display geographical information; Integrate data from sources into map projections in multiple dimensions; Visualize current geographical areas and project future changes; Create, manage and project multiple information layers into a variety of views.*
- 19.5.5 BI, Analytics & Data Science -- *BI Querying & Reporting Delivery; Self Service Analytics; Storyboarding; Data Visualization; Personalization; Data Mashups; Operational Intelligence; Data Sharing; Social Analytics; Advanced Analytics; Mobile Analytics; Data Exploration & Pre-processing; Machine Learning; Unsupervised and Supervised Learning; Overfitting & Regularization; Model Evaluation and Model Interpretability.*
- 19.5.6 Content Management -- *Data Classification & Retention; Protecting sensitive data and information; Confidentiality including data marking; Records Management; Content Management; Physical Documents; Electronic Documents; Document & Content Governance.*
- 19.5.7 Search -- *Contextual; Spatial; Business Intelligence; Full Text; Meta Data, Master Data & Reference Data Search.*

#### 19.6 IT Vendor & License Management
*- Management of IT Vendors beyond standard Supply Chain considerations
- Inventory and License management for IT products and technologies
- Contract Management and Service Level Agreements*

- 19.6.1 IT Vendor Relationship Management -- *Vendor Contact Management; Vendor Engagement Management; Vendor Status; Vendor Relationship Development.*
- 19.6.2 IT Inventory Management -- *License and subscription management; Volume management.*
- 19.6.3 IT Contract Management -- *Vendor Service Level Agreements; Vendor Statements of Work; Software License Contract Management; Hardware purchase and support Contract Management; Data Center Contract Management; Data Subscriptions; Cyber Contract Management; Telecomms Contract Management; Managed Services/Outsourcing.*

#### 19.7 Build & Automation Management
*- Processes, Standards and Tooling for building any digital asset or automation, including workflows, process automation, application components, customization and integration code, etc.
- Design management, architecture visualization, code generation, storage and version control, build processes and automation.
- Build asset management, digital asset deployment management and automation.
- AI creation, training, deployment and control.*

- 19.7.1 Workflow Automation -- *Long running business process automation; Combinatorial workflow automation; Workflow Automation platforms and tooling.*
- 19.7.2 Productivity Enhancement -- *Personal Productivity extensions and enhancements; Personal Productivity automation; Team enhancements and automation; Citizen Development.*
- 19.7.3 App Development -- *Processes and Standards; Frameworks and Languages; Tooling and Automation.*
- 19.7.4 AI Creation -- *AI Frameworks; AI Creation Development, Build, Training and Deployment Tooling; AI Monitoring and Control Frameworks and Tooling.*
- 19.7.5 Build & Automation Tools -- *Development and Build Tooling Standardization across Development and Build domains; Source and Version Management; Continuous Integration and Continuous Deployment (CI/CD) tooling standardization and optimization.*
- 19.7.6 Application & Automation Platforms -- *Language and Technology Framework Platforms; Automation Technology Platforms; No Code, Low Code Frameworks and Platforms.*

#### 19.8 Communication & End User Computing
*\* End User Devices including Mobile
\* End User Computing Platforms including Mobile
\* Personal Communications including Mobile
\* Office Productivity Applications including Mobile*

- 19.8.1 Device Management -- *Device Selection; Device Configuration; Device Logistics; Device Testing & Deployment; Device Connectivity; Device Security, Access and Authentication; Device Operating System Management.*
- 19.8.2 Unified Communications -- *Real Time Communication (IM, Voice, Video, Presence); Non Real Time Communication (EMail, SMS, Voice Mail, Fax); Consistent User Experience.*
- 19.8.3 Office Productivity -- *Standardized Productivity Applications; Standardized Document Creation, Editing and Viewing Experience; Document Management; Standardized EUC Technology Policy (DLP, Access, Classification, etc).*
- 19.8.4 Collaboration -- *Standardized Collaboration Tools; Situational Access (e.g. Intrinsically Safe, Hands Free, Video, Voice, Pen, Text, Photo, Document, Wearable); Online Presence, Availability and Discovery; Hybrid Work Experience.*
- 19.8.5 Mobility -- *Mobile Device Management; Mobile Application Packaging and Deployment; Mobile Security & Authentication; Mobile Application Integration; Mobile Analytics and Insights; Mobile Collaboration Tools; Mobile Cloud Services; Mobile User Experience.*

#### 19.9 IT Service Delivery
*- IT Service Catalog
- IT Service Delivery Management
- IT Operations Management*

- 19.9.1 Application Service Delivery -- *Application Availability to SLA; User Access; Application Integrity; Application Accessibility; Application Service Catalog; Application Release & Deployment Management.*
- 19.9.2 IT Operations -- *Resource Management (operating assets); Monitoring & Incident Management; Capacity Planning & Optimization; Automation & AI Operations; Performance Tuning & Troubleshooting; Service Request & Provisioning; Service Desk, Workflow & User Support; Self Service.*
- 19.9.3 Network Connectivity -- *Connectivity as a Service; Quality of Service; Site & Location Connectivity; Service Connectivity; Individual Connectivity; Resource and Service Accessibility; Connectivity Service Catalog.*
- 19.9.4 Cloud Services -- *Infrastructure as a Service (IaaS); Platform as a Service (PaaS); Data as a Service (DaaS); Integration as a Service (iPaaS); Software as a Service (SaaS); Cloud Service Catalog.*
- 19.9.5 Physical Infrastructure Management -- *Physical Deployment & Configuration; Physical Asset Management & Security; Monitoring & Alerting; IT Asset Lifecycle Management; IT Asset Logistics; Physical Infrastructure Service Catalog.*
- 19.9.6 IT Service Continuity -- *Change Control; Backup & Restore; High Availability; Service Failover & Recovery; Identify and Monitor Service Interruption.*

---

### 20. Strategic Management

> *(No description in ServiceNow)*

#### 20.1 Strategic Planning
*Ability to define organization's objectives or direction, and determine, at a high level, the allocation of its resources towards it.*

*(No L3 capabilities)*

#### 20.2 Economic Assessment
*Ability to deliver economic assessment at both the strategic and prospect levels of screening.
Capability includes:
. At the exploratory stage, initial economic observations of a possible oil reserve, prospect level scoping, land acquisition exploration, and pilot delineation of oil fields as part of demonstrating commercial viability
. Appraisal planning and commercial assessment activities typically performed at a high level of detail as part of the initial stages in the decision making process
. Assessments that consider the full lifecycle view of the prospect including capital allocation / expenditure, resource allocations, operating costs and anticipated sales volumes, future commodity market prices, royalty and tax requirements, etc.
. At the development stage, assessment of a producing asset in addition to economic analysis of commercial and field development plans and the results to date
. Appraisals and commercial assessment activities typically performed in detail throughout the asset's life cycle
. Assessments that consider the current and future view of the asset including current and predicted sales volumes, etc.
. Deliverables such as Opportunity or Prospect Assessments, Opportunity Economics, Play Development Plans, Commercial Assessments and Appraisal Plans, Exit Strategies*

*(No L3 capabilities)*

#### 20.3 Reserves Management
*Ability to model and estimate reserves to assist in making investment decisions such as whether to continue to explore in an area, to develop a property, to hold or sell a property, etc. Also supports financial statements and performance in the determination of the depletion provision and future recoverability of capitalized costs, and assists in assessing the value of related oil and gas activities and predicting future cash flows.
Capability includes:
. Day-to-day reports to monitor reserves
. Archives and snapshots to show reserve history and track performance against key indicators
. Tracking of changes for improved transparency in reserves reporting and auditing
. Reports needed for year-end disclosures and regulatory (such as EIA23, NI-51-101, etc.)
. Unconventional reserves reporting requirements.*

*(No L3 capabilities)*

#### 20.4 Performance Management
*Ability to capture the planned performance and actual results for key activities/results to manage and optimize business performance across a single enterprise or within a specific business unit.
Capability includes:
. The planned performance and actual results for key activities identified by Executive (e.g. well tie ins, production volumes and financials)
. Resource allocation and understanding of business value drivers
. Executive level dashboards and performance scorecards that visualize data on company wide business metrics and key performance indicators (KPIs)
. Maximized shareholder value from increased ability to make strategic decisions based on current and past (trend) information
. Results and outcomes
. Reduced cycle time for reporting and increased reporting quality
. Note - this capability shares dashboards and scorecards with BI & Analytics capability which covers business unit and asset level metrics.*

*(No L3 capabilities)*

#### 20.5 Enterprise Risk Management
*Ability to manage consolidated enterprise risk and provide a common understanding and classification of risk management practices across the organization.
Capability includes:
. Alignment of risk culture, organization decision frameworks (both financial and operational) and related processes
. Risk categories such as financial and credit risk, political and country risk, risk to business operations and license to operate, etc.
. Management of consolidated enterprise risk levels, from identification through to remediation, sharing and transfer, reduction (such as buying insurance) or acceptance
. Common understanding and classification of risks management practices across the organization (Marketing Risk Management covers risks associated with market volatility)
. Deliverables such as Risk Assessments.*

*(No L3 capabilities)*

#### 20.6 BI & Analytics
*Ability to analyze data and present actionable information to help the business make more informed decisions.
Capability includes:
. Predictive and prescriptive analytics
. Ad hoc analysis and querying, enterprise reporting, online analytical processing (OLAP), mobile and real-time BI, etc.
. Business level dashboards and performance scorecards that visualize data on business metrics and key performance indicators (KPIs)
. Department and business unit reports that visualize data on business metrics and key performance indicators
. Analyses to locate Acquisition and Divestiture (A&D) targets or merger opportunities as well as strategic partners for coveted assets or intellectual property (IP)
. Accelerated and improved decision making, optimized internal business processes, increased operational efficiency, new sources of revenues, and competitive advantages over business rivals
. Supports to identify market trends and spot business problems that need to be addressed
. Note - this capability shares dashboards and scorecards with the Performance Management capability which covers executive and company wide metrics.*

*(No L3 capabilities)*

---

### 21. Health & Safety

> *Ability to keep employees safe at work by developing internal and following governmental EHS policies, and ability to sustainably operate to protect environment.*

#### 21.1 Personal Safety
*Ability to identifies worksite/facility hazards, manages effective work site practices, and establishes a healthy work environment.
Capability includes:
. The safety, health and welfare of people engaged in work activities for the organization
. Risk identification, incident response, training and awareness as well as regulatory and stakeholder engagements specific to health and safety activities
. Developing and implementing awareness of HSE&SR principles throughout the organization while ensuring related competence among employees
. Deliverables such as HSE Execution Strategies and Plans as well as Operational HSE Plans.*

*(No L3 capabilities)*

#### 21.2 Incident Management

*(No description in ServiceNow)*

*(No L3 capabilities)*

#### 21.3 Emergency Management
*Ability to maintain effective emergency management, emergency response, and business continuity plans, maximizes human response, and ensures access to appropriate physical, material & human resources in order to minimize impacts of an emergency event.
Capability includes:
. The plans and processes to ensure effective response to spills or other unplanned events
. Root cause identification, lessons learned and future event prevention
. Scenario modelling and plan testing
. Integration with supply chain and inventory management.*

*(No L3 capabilities)*

#### 21.4 Industrial Hygiene

*(No description in ServiceNow)*

*(No L3 capabilities)*

#### 21.5 Process Safety
*Ability to establishes a Process Safety culture, enable understanding of the hazards and risk, ensure safe operations and maintenance of operations that pose risk, and investigate/review incidents for improvements and learnings.
Capability includes:
. HAZOP (hazard and operability) and PHA (process hazard analysis) evaluations and assessments
. Failure mode and effects analysis (FMEA), safety integrity levels (SIL), and layer of protection analysis (LOPA)
. The management of process safety audits
. Capture, management and reporting of incidents and problems as well as their corrective actions.*

*(No L3 capabilities)*

#### 21.6 Health & Safety Reporting
*Ability to define, exchange, publish and track relevant EHSR information with internal stakeholders and external regulatory bodies.*

*(No L3 capabilities)*

---

### 22. Environment & Sustainability

> *(No description in ServiceNow)*

#### 22.1 Environmental Management
*Ability to manage the environmental aspects of company operations in all phases of the business, minimizes the impact on the natural environment, and conducts business in compliance with all relevant environmental legislation, regulations, and industry best practices.
Capability includes:
. The monitoring, measuring, documenting and controlling emissions output
. Environmental portfolio management and information flow across the enterprise
. Reports to meet external and internal environmental reporting requirements
. Continuous air emissions (CEMS), fugitive emissions (LDAR), water, waste, CFC's and greenhouse gas emission monitoring, management and reporting
. Key deliverables such as a Preliminary Environmental Impact Assessment (EIA) and Final EIA.*

- 22.1.1 Manage Land
- 22.1.2 Manage Water
- 22.1.3 Manage Air Emissions
- 22.1.4 Manage Waste
- 22.1.5 Manage Bio-Life

#### 22.2 Regulatory Compliance

*(No description in ServiceNow)*

- 22.2.1 Manage Regulatory Compliance & Regulations
- 22.2.2 Manage Regulatory Applications and Filings
- 22.2.3 Manage Regulatory & Environmental Audits
- 22.2.4 Track Compliance Performance
- 22.2.5 Manage Land Compliance
- 22.2.6 Manage Well Regulatory Compliance (including Inactive)

#### 22.3 Stakeholder Engagement

*(No description in ServiceNow)*

- 22.3.1 Manage Corporate Communications
- 22.3.2 Manage Crisis Communications
- 22.3.3 Hold an Event
- 22.3.4 Develop Leadership Communications
- 22.3.5 Establish Brand Guidelines
- 22.3.6 Engage External Stakeholders
- 22.3.7 Develop Content

#### 22.4 Sustainability

*(No description in ServiceNow)*

*(No L3 capabilities)*

#### 22.5 Social Responsibility
*Ability to identify, assess and manage the social risk and the impact of business decisions and operations.
Capability includes:
. The engagement and creation of a positive relationship with the society and communities wherever the company operates
. Topics generally relating to license to operate.*

*(No L3 capabilities)*

---

### 23. Legal

> *Ability to effectively deal with the law.*

#### 23.1 Corporate Governance, Compliance & Disclosure

*(No description in ServiceNow)*

*(No L3 capabilities)*

#### 23.2 External Counsel Management

*(No description in ServiceNow)*

*(No L3 capabilities)*

---

### 24. Research & Development

> *(No description in ServiceNow)*

#### 24.1 Technology Development
*Ability to create new or improved exploitation concepts and techniques, that can provide a competitive advantage for the company. This capability includes both reservoir and facility technology development.
Capability includes:
. New exploitation techniques
. Lab/core testing
. Technology pilots
. Analytics*

- 24.1.1 New Exploitation Techniques
- 24.1.2 Lab/Core Testing
- 24.1.3 Technology Pilots
- 24.1.4 Analytics

---

### 25. Governance & Compliance

> *(No description in ServiceNow)*

#### 25.1 Audit & Compliance
*Ability to evaluate, manage, and update processes to ensure compliance with mandated corporate activities, regulatory/ legislative requirements, contractual obligations, and industry standards.
Capability includes:
. The ability of the enterprise to conform with stated requirements as defined in law, regulations, contracts, strategies, policies, etc.
. Assessments of compliance via audit (either internally or independently)
. Calculation of risks and potential costs of non-compliance compared against projected expenses to achieve compliance
. Prioritization, funding and initiation of any corrective actions
. Administration and management of compliance management processes, plus stage gates, to ensure the organization is adhering to the latest regulatory requirements
. Requirements of SOX, HIPAA, OSHA, Basel II, environmental regulatory compliance, Non-Disclosure Agreement (NDA) compliance and HR policies
. The support of other capabilities such as: Appraisal (Reserves Management); Well and Facility Delivery (Design); Operations; Marketing (Financial Transactions); HSE & SR; Financial Management, etc.
. Deliverables such as a Regulatory & Permits Strategy or Plan, and Regulatory Approvals.*

*(No L3 capabilities)*

#### 25.2 Action Tracking
*Ability to capture, manage and report actions within defined workflows and escalation procedures. Is sometimes also known as a ticket management system. Note, HSE&SR related action tracking of incidents and problems are covered in the Process Safety capability.
Capability includes:
. Requests such as building maintenance, IT service and change requests, catering arrangements
. Governance tracking such as audit findings and related actions
. Correspondence management such as receipt, assignment and outcomes of requests for information.*

*(No L3 capabilities)*

#### 25.3 Business & Technical Assurance
*Ability to manage the quality and due diligence on technical work performed and related key business activities. Includes such items as planning, documenting, setting targets/specifications, QA reviews, quality control, inspection and monitoring.
Capability also includes:
. Demonstration of due diligence and decision support
. Quality Management frameworks like 9001: 2000 and their associated processes
. Target planning and setting
. Quality assurance (QA) and quality control (QC)
. Product specifications, quality manuals, sampling procedures, etc.
. Quality checks of designs and plans
. Documentation of quality checks and audits
. Test equipment with equipment data, maintenance schedules and calibration scheduling
. Deliverables such as Technical Assurance reviews, Operations & Maintenance manuals, Operations acceptance documents and Opex estimates*

*(No L3 capabilities)*

#### 25.4 Government & Stakeholder Relations
*Ability to manage the effort to identify, meet, participate, listen and respond to, understand and involve external groups, individuals, or regulating bodies that can affect, or that can be affected by, operational activities and business decisions.
Capability includes:
. The identification and capture of government's processes, policy development and regulations, participation in government committees, or the identification and management of expectations of critical stakeholder group(s)
. The successful passage of regulatory and permitting processes, managing multiple stakeholder communities, and supporting consensus with mutually beneficial outcomes across either standard operations or through the passage of critical capital spend projects
. Primary government departments such as US DOE, Natural Resources Canada
. Intergovernmental boards or consortiums comprised of peers from the petroleum industry (such as API, CAPP and temporary pipeline task forces) who seek to coordinate and unify petroleum policies while stabilizing the related product markets for the efficient, economic and regular supply of petroleum to consumers, a steady income to producers and a fair return on capital for those investing in the industry
. Boards such as FERC, NEB, AER, and AUC
. Developing, maintaining and enhancing interactions and relationships with the investment and shareholder communities with reporting to the company's Board of Directors and conducting investor management meetings
. Interaction with stakeholder communities which, on occasion, relates to coming engagements and betterment programs
. Deliverables such as Stakeholder Management and Communication Plans*

*(No L3 capabilities)*

#### 25.5 Project Management
*Ability to plan and coordinate day-to-day activities of capital projects and manages risk and economics thorough schedules, cost analyses, and assessment of changes.
Capability includes:
. The management of capital projects
. Project control services with typical estimating, scheduling, planning and cost management activities
. Producing estimates based on P50 and P90 levels of confidence
. Project risk and economics through advanced schedule and cost analyses and assessment of changes
. Views of project performance to date with ability to drill down to details
. Individual or cross-project KPIs to facilitate project performance management
. Deliverables such as Project Funding & Finance Assessments, Project Charters and related Upstream Project Management (UPM) documents, Design Basis Memorandums (DBMs), Operational Finance Plans during execute/build processes, etc.*

*(No L3 capabilities)*

#### 25.6 Military Management
*Ability to support coordination of Oil & Gas operations with military activities on the Cold Lake Air Weapons Range (CLAWR) through consultation, communication, access control & movement with Military & Industry.
Capability includes:
. Access Control & DCAARs
. Off-Road Movement Control
. Industry Emergency Coordination
. Communication with Military & Industry*

- 25.6.1 Access Control and DCAARs
- 25.6.2 Off-Road Movement Control
- 25.6.3 Industry Emergency Coordination
- 25.6.4 Communication with Military & Industry

---

### 26. Workplace & Real Estate

> *(No description in ServiceNow)*

#### 26.1 Building Management
*Ability to support the processes and tools to acquire, negotiate and ensure the health, safety and maintenance of a non-producing built structure (i.e. not a facility).
Capability includes:
. Disposal activities at end of commercial life
. The control of services like heating/cooling, lighting, shutters, electric power, security and surveillance
. The management of physical risk by providing central security via physical card access and fault monitoring
. Courier and shipping services
. The creation of usage-based profiles to ensure an effective and efficient use of the building
. Other building management services that are typical in corporate or regional headquarters.*

- 26.1.1 Real Estate Portfolio Organization
- 26.1.2 Lease Management
- 26.1.3 Space Optimization
- 26.1.4 Building Services Management

---

## 5. Capability Count Summary

| L1 # | Level 1 Capability                           | L2 Count | L3 Count |
|-------|----------------------------------------------|----------|----------|
| 1     | Asset Development                            | 4        | 17       |
| 2     | Reservoir Engineering                        | 3        | 17       |
| 3     | Geology & Geophysics                         | 5        | 25       |
| 4     | Well Management                              | 7        | 37       |
| 5     | Project Delivery                             | 7        | 35       |
| 6     | Reclamation & Remediation                    | 3        | 0        |
| 7     | Site Operations Management                   | 7        | 21       |
| 8     | Maintenance Management                       | 3        | 20       |
| 9     | Resource Management                          | 5        | 25       |
| 10    | Supply & Logistics                           | 6        | 23       |
| 11    | Marketing & Trading                          | 7        | 60       |
| 12    | Optimization                                 | 1        | 0        |
| 13    | Manufacturing & Processing                   | 4        | 0        |
| 14    | Commercial Products                          | 3        | 13       |
| 15    | Retail                                       | 6        | 0        |
| 16    | Supply Chain Management                      | 6        | 15       |
| 17    | Financial Management                         | 7        | 48       |
| 18    | Human Resources                              | 7        | 32       |
| 19    | Information Technology                       | 9        | 50       |
| 20    | Strategic Management                         | 6        | 0        |
| 21    | Health & Safety                              | 6        | 0        |
| 22    | Environment & Sustainability                 | 5        | 18       |
| 23    | Legal                                        | 2        | 0        |
| 24    | Research & Development                       | 1        | 4        |
| 25    | Governance & Compliance                      | 6        | 4        |
| 26    | Workplace & Real Estate                      | 1        | 4        |
|       | **TOTAL**                                    | **127**  | **468**  |

**Grand Total: 26 L1 + 127 L2 + 468 L3 = 621 capabilities**

---

## 6. Cross-Reference: BCM to Application Functional Capability Framework

### How the BCM Connects to Application Functional Capabilities

The **Business Capability Model (BCM)** and the **Application Functional Capability
Framework** serve complementary but distinct purposes within the Cenovus Enterprise
Architecture practice:

| Artefact                          | Describes                                    | Perspective         |
|-----------------------------------|----------------------------------------------|---------------------|
| **Business Capability Model**     | What the business does (stable, noun-based)  | Business / Strategic |
| **Application Functional Capability Framework** | What applications do (functional features) | Technology / Solution |

The two frameworks are connected through a **mapping relationship**:

1. **Business Capabilities drive demand.** Each L2/L3 business capability represents a
   business need that must be supported by one or more application functional capabilities.

2. **Application Functional Capabilities supply support.** Application functional
   capabilities describe the features and functions that software applications provide
   to fulfil business capability needs.

3. **The mapping reveals coverage, gaps, and redundancy.** By mapping application
   functional capabilities to business capabilities, the Enterprise Architecture team
   can identify:
   - **Coverage:** Which business capabilities are well-served by applications.
   - **Gaps:** Business capabilities with no or inadequate application support.
   - **Redundancy:** Multiple applications providing overlapping functional capabilities
     for the same business capability (rationalization candidates).
   - **Transformation priorities:** Business capabilities that are critical but supported
     by aging, unsupported, or manual solutions.

4. **ServiceNow as the integration point.** Both the BCM (via `cmdb_ci_business_capability`)
   and the application portfolio are managed in ServiceNow CMDB. This enables automated
   mapping, reporting, and governance through the ServiceNow platform, ensuring consistency
   between the two frameworks.

### Recommended Usage

- When evaluating a new application or solution, map its functional capabilities to
  the BCM to confirm it addresses a genuine business capability need.
- When performing application portfolio rationalization, use the BCM-to-application
  mapping to identify overlapping coverage areas.
- When building a technology roadmap, align planned investments to the business
  capabilities they will enhance or enable.

---

## 7. Governance & Change Management

### Source of Truth

This Business Capability Model is **sourced from and governed through the ServiceNow
CMDB** (`cmdb_ci_business_capability` table). The markdown document is a rendered
export and should be regenerated whenever material changes are made in ServiceNow.

### Ownership

| Role                                 | Responsibility                                                        |
|--------------------------------------|-----------------------------------------------------------------------|
| **VP Enterprise Architecture**       | Executive sponsor; approves changes to L1 structure.                  |
| **Chief Architect**                  | Model custodian; manages change requests and annual review.           |
| **Domain Architects**                | Validate L2/L3 accuracy within their domains.                        |
| **Business Capability Owners**       | Business leaders accountable for individual L1/L2 capability areas.  |
| **Architecture Review Board (ARB)**  | Ratifies material changes; ensures structural integrity.             |

### Change Process

1. Any stakeholder may submit a **Capability Change Request** (add, modify, retire,
   merge, split) to the Enterprise Architecture team.
2. The change is made in **ServiceNow CMDB** by the Chief Architect or a designated
   Domain Architect. All changes are tracked through ServiceNow change management
   and audit history.
3. Material changes (L1 or L2 structural changes) are presented to the **Architecture
   Review Board (ARB)** for approval before being committed in ServiceNow.
4. Minor changes (L3 additions, name refinements, description updates) may be approved
   by the Chief Architect and the relevant Domain Architect directly in ServiceNow.
5. After changes are committed in ServiceNow, this markdown document is regenerated
   from the updated CMDB export to maintain alignment.

### Review Cadence

- **Annual Full Review** -- Every Q1, the full BCM is reviewed in ServiceNow against
  strategic plans, organizational changes, and new regulatory requirements.
- **Quarterly Check-in** -- Domain Architects flag any emerging gaps or overlaps via
  ServiceNow workflows.
- **Event-Driven Updates** -- Triggered by M&A activity, major reorganization, or new
  regulatory mandates. Changes are processed through ServiceNow change management.

---

*End of Document -- Generated from ServiceNow CMDB export on 2026-02-08*
