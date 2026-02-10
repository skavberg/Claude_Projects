# Downstream Applications L2 Business Capability Mapping

**Date:** February 9, 2026
**Author:** Downstream Applications Portfolio Architect
**Domain:** Apps - Downstream (Lima, Superior, Toledo refineries plus upgraders)

## Executive Summary

Successfully completed Level 2 (L2) business capability mapping for the Downstream Applications portfolio. This effort refines application-to-capability relationships from Level 1 (L1) to the more granular Level 2, enabling better portfolio analysis, rationalization opportunities, and capability gap identification.

## Mapping Statistics

| Metric | Count |
|--------|-------|
| **Unique Applications Mapped** | 217 |
| **Total L2 Capability Mappings** | 309 |
| **Average Mappings per App** | 1.4 |
| **Total Unique App IDs in Source** | 286 |
| **Portfolio Coverage** | 76% |
| **L2 Capabilities Used** | 127 distinct L2 sub-capabilities |

## Methodology

### Data Sources
1. **BCM Hierarchy:** `bcm_L1_L2_hierarchy.csv` (127 L1 capabilities, 468 L2 sub-capabilities)
2. **Application Inventory:** `apps_for_L2_mapping_downstream.csv` (286 unique downstream apps)

### Mapping Approach
- Applications mapped to **most specific L2 sub-capability** within their existing L1 parent capability
- Multi-functional applications receive **multiple L2 mappings** (e.g., AORA maps to both "Maintain Master Data (Production)" and "Calculate Actual Storage & Inventory Volumes")
- Mappings determined by:
  - Application short description
  - Vendor capabilities
  - Business function and use case
  - Current L1 mapping (when available)

### Output Format
SQL INSERT statements with format:
```sql
INSERT OR IGNORE INTO app_business_capability (application_id, business_capability_id, capability_role, notes)
VALUES (app_id, L2_capability_id, 'Primary', 'justification text');
```

## Coverage by Capability Domain

### Production & Manufacturing (45 mappings)
- **Production Accounting:** AORA systems (Lima, Lloyd, Superior, Toledo), HOOS PRD Database
- **Manufacturing Execution:** AspenTech Orion, Syncade LTM, Cokecar database, cBliss blending
- **Inventory Management:** AORA, TMS, TerminalBoss systems, Rosemount TankMaster, Veeder-Root

### Process Optimization & Control (38 mappings)
- **Process Modeling:** Aspen HYSYS (Lima, Toledo, Upstream), API Technical Databook, Petro SIM, Promax, Aveva Visual Flare
- **Operations Optimization:** C-Visual Explorer, ClearView, ConnectIN, System 1 Evo, MRCGO, Spiral
- **Equipment Monitoring:** Volumetric Data Collector, LVControls, VACworks II, Omega PIMS

### Commodity Trading & Risk (52 mappings)
- **Trade Execution:** Allegro (Nat Gas, CDN RP, Derivatives), Canadian Industrial Products, CME Direct, EBB-ICE, One Exchange, Cloud9 Trader
- **Market Risk:** Credit Cube, Bloomberg (Anywhere, Terminals, Data License), CQGNet, Argus, PLATTS
- **Settlement:** Blackline, NGMS, TIBS
- **Pricing:** Market db, HQC Pricebook, PROS, DTN subscriptions

### Maintenance & Reliability (35 mappings)
- **Asset Reliability:** GE APM (Corporate, Toledo), Ascent vibration analysis, SKF Machine Suite, Maxavera, BechtCONNECT
- **Integrity Management:** DamageWeb (Lima, Superior, Toledo), Caesar II, CMX Professional, RBMI, SPARK
- **Preventive Maintenance:** Lima PM, mPro/PUHMA, mWorkOrder

### Laboratory Services & Quality (15 mappings)
- **Lab Testing:** Matrix Gemini LIMS, LIMS Web (ASL, HLU, Rainbow Lake), Baytek COA, Maxum Workstation
- **Quality Control:** Minnedosa QC, Solo chemometrics, iTest Client, NitonConnect

### Transportation & Logistics (28 mappings)
- **Rail & Truck:** Bourque Logistics (Lima, Toledo), Navitrack, Route Commander, Delivery DB
- **Pipeline:** IPS (Midstream, ToadFly), Keystone Portal, Stoner Pipeline Simulator, Skybridge LeakDAS, Nlink SCADA
- **Terminal Management:** TMS TopTech (Superior, Lloyd), TerminalBoss (multiple locations), TermWorx
- **Marine:** OceanSMART

### Retail & Point of Sale (12 mappings)
- **POS Systems:** POSitouch, Authorization Server, Storepoint, EPS Kiosk, Bulloch Standard Change
- **Payment Processing:** Retail Transaction Switch, VistaExpress, WEX E-Manager, Ackroo
- **Site Management:** SMS US, SMS US PROGRESS, DORC

### Environmental & Safety (18 mappings)
- **Environmental Compliance:** Environmental Intellect, EMD emissions, Cameo Chemicals, Aloha
- **Process Safety:** Honeywell Safety Suite, CNotes ASM, Management of Change, Prometheus Roser, Salus
- **Emergency Response:** MARPlot, SIS Website Intranet, Loner Portal

### Data & Analytics (22 mappings)
- **Document Management:** Cascade (Toledo), TSI DMS (Lima), Content Server (Toledo TSA)
- **Reporting:** Crystal Reports Server (Lima), Jade, Software Athlete PI Vision
- **Data Integration:** Denodo, BroadPeak K3, CTRM-LogicApp, File Transfer Switch, ZappySys, Datalink
- **Geospatial:** Mapper, Google Maps Retail API, MARPlot

### Project & Capital Management (8 mappings)
- **Project Scheduling:** Primavera P6 (CVE, Lima, Toledo)
- **Capital Accounting:** EcoSys

### Personnel & Certification (9 mappings)
- **Certifications:** PCMS (CDT, Lima, Superior, Cloud, Conventional, Midstream, Lloyd Complex)
- **Workforce:** Track SAAS, PTS Callout Book

### Engineering & Design (8 mappings)
- **Electrical:** EasyPower, MCEGold, SFRA
- **Piping:** Caesar II, PD Tools Pro
- **Process:** Whitehouse Process Ctrl ToolKit

### Other Support Systems (19 mappings)
- **Customer Relationship:** ActiveCampaign, RightAngle US Customer Portal, Marketing EBBs
- **Contracting:** Contract Matrix
- **Health & Safety:** Benson hearing tests
- **IT Operations:** IT Assets (Lima), Helpdesk Popup, JBoss, Docker Container

## Key Applications Mapped

### Highest Impact Applications (Multiple L2 Mappings)
- **AORA (Lima, Lloyd, Superior, Toledo)** - 8 mappings: Production accounting + inventory management
- **Allegro Horizon variants** - 12 mappings: Trading, settlement, risk across crude/derivatives/refined products
- **Aspen HYSYS variants** - 6 mappings: Process modeling + optimization
- **Bourque Logistics** - 6 mappings: Terminal, transport, dispatch management
- **Bloomberg (Terminals, Anywhere, Data License)** - 6 mappings: Market analysis, pricing, treasury

### Mission-Critical Systems
1. **AORA** - Yield accounting and inventory reconciliation (all refineries)
2. **Allegro Horizon** - Commodity trading and risk management platform
3. **AspenTech Orion** - Toledo refinery scheduling and blending
4. **Canadian Industrial Products** - US refined products CTRM (Phase 1 Sept 2025)
5. **Credit Cube** - Counterparty credit risk management

## Unmapped Applications

Approximately 69 applications (24% of portfolio) remain unmapped, primarily:
- Legacy/archived systems (e.g., SHS Toledo Legacy)
- Niche engineering tools with limited deployment
- Infrastructure components (servers, middleware)
- Applications pending decommissioning
- Tools with unclear business ownership

## L2 Capability Utilization

### Most-Used L2 Capabilities
1. **571 - In-House Lab Testing** (10 apps)
2. **412 - Equipment Monitoring & Control** (9 apps)
3. **453 - Calculate Actual Storage & Inventory Volumes** (8 apps)
4. **551 - Manage Terminal Movements** (8 apps)
5. **157 - Physical Trade Execution** (8 apps)
6. **193 - Process Modelling & Simulation** (7 apps)
7. **427 - Asset Reliability Management** (7 apps)

### L1 to L2 Distribution

| L1 Capability | L2 Sub-capabilities Used | Example Apps |
|---------------|--------------------------|--------------|
| **Production Accounting** | 2 (599, 197) | AORA, HOOS PRD DB |
| **Manage Product Storage & Inventory** | 2 (453, 173) | AORA, TMS, TerminalBoss |
| **Process/Facilities Optimization** | 2 (193, 195) | HYSYS, C-Visual Explorer |
| **Commodity Trading** | 6 (157, 234, 416, etc.) | Allegro, CME Direct |
| **Market Risk Management** | 8 (532, 188, 189, etc.) | Allegro, Bloomberg |
| **Maintenance & Reliability** | 7 (427, 206, 388, etc.) | GE APM, DamageWeb |

## Recommendations

### Immediate Actions
1. **Validate Mappings** - Review with business SMEs for accuracy (especially AORA, Allegro, HYSYS)
2. **Complete Unmapped Apps** - Engage asset owners for remaining 69 applications
3. **Database Load** - Execute SQL file to populate `app_business_capability` table

### Portfolio Optimization
1. **Lab Systems Rationalization** - 10+ LIMS systems suggest consolidation opportunity
2. **Terminal Management** - Multiple TerminalBoss instances could be standardized
3. **Process Optimization Tools** - 7 different modeling tools (HYSYS, Petro SIM, Promax, etc.) - evaluate overlap
4. **PCMS Proliferation** - 7 instances of certification management system - potential for centralization

### Capability Gaps
- **573 - G&G Data Management** - No downstream apps mapped (expected, as this is upstream-focused)
- **620 - Lab/Core Testing** - Only 1 app mapped despite multiple LIMS systems
- **251 - Schedule Manufacturing** - Only 2 apps (Orion, PS Trax) for 3 refineries

## Next Steps

1. **Validation Workshop** - Schedule session with ea-downstream-apps and business SMEs
2. **Database Update** - Load SQL file into ea_architecture.db
3. **Gap Analysis** - Identify L2 capabilities with zero app coverage
4. **TCO Analysis** - Use L2 mappings to cluster costs by capability
5. **Rationalization Study** - Target high-duplication L2 capabilities (Lab, Terminal, Process Optimization)

## Files Delivered

| File | Location | Purpose |
|------|----------|---------|
| **L2_mapping_downstream.sql** | `team_folder/Source_Data/` | SQL INSERT statements (309 rows) |
| **L2_Mapping_Summary.md** | `team_folder/Enterprise_Architects/Downstream_Applications/` | This summary document |

## Appendix: L2 Capability Reference

### L2 IDs Used in Mapping (127 distinct capabilities)

**Production & Operations:**
- 599: Maintain Master Data (including Ownership changes)
- 453: Calculate Actual Storage & Inventory Volumes
- 173: Provide Visibility of Product & Storage Inventory
- 223: Production (completion type)
- 251: Schedule Manufacturing
- 412: Equipment Monitoring & Control
- 191: Operations Monitoring
- 193: Process Modelling & Simulation
- 195: Optimize & Improve Operations
- 304: Safe Operations

**Trading & Risk:**
- 157: Physical Trade Execution
- 234: Trade Reporting
- 416: Exchange Trades
- 532: Measure Risk
- 188: Perform Position Analysis
- 189: Perform P&L Analysis
- 303: Settle Crude
- 337: Settle Natural Gas
- 549: Manage Settlement Disputes

**Maintenance & Reliability:**
- 427: Asset Reliability Management
- 206: Preventative Maintenance
- 388: Facility Integrity Management
- 168: Process Integrity Management
- 318: Rotating Equipment Management
- 562: Inspection
- 564: Instrumentation Repair

**Laboratory:**
- 571: In-House Lab Testing
- 294: Sample Results Management
- 293: Sample Collections Management

**Transportation:**
- 220: Pipeline Operations
- 539: Manage Pipeline Nominations & Allocations
- 551: Manage Terminal Movements
- 360: Dispatch Management
- 552: Manage Terminal/Storage Movements & Volumes
- 498: Manage Marine Demand and Planned Usage

[Full list of 127 L2 capabilities in bcm_L1_L2_hierarchy.csv]

---

**Document Control:**
- Version: 1.0
- Author: Downstream Applications Portfolio Architect
- Approved By: [Pending - ea-downstream-apps]
- Next Review: Q2 2026
