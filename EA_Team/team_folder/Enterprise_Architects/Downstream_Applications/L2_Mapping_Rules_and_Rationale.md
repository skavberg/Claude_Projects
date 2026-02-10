# Downstream Applications L2 Mapping Rules and Rationale

**Date:** February 9, 2026
**Author:** Downstream Applications Portfolio Architect
**Purpose:** Document mapping logic for L2 business capability assignments

---

## Mapping Principles

### 1. Specificity over Generality
- Always map to the **most specific L2 sub-capability** available
- Example: AORA → "Maintain Master Data (Production)" (L2 599) NOT just "Production Accounting" (L1 99)

### 2. Multiple Mappings for Multi-Function Apps
- Applications serving multiple business functions receive multiple L2 mappings
- Example: AORA serves both production accounting (599) AND inventory management (453)
- Each mapping includes distinct justification in notes field

### 3. Primary Role Focus
- All mappings use `capability_role = 'Primary'`
- Applications directly enable the L2 capability (not just supporting/related)

### 4. Parent L1 Consistency
- L2 mappings must fall under the application's existing L1 parent capability
- If app has no current L1 mapping, determine best-fit L1 first, then select appropriate L2(s)

---

## Application Type Mapping Guide

### Production Accounting & Inventory Systems

**App Type:** Yield accounting, volumetric reconciliation (AORA, HOOS PRD)

**L1 Parent:** 99 - Production Accounting, 109 - Manage Product Storage & Inventory

**L2 Mappings:**
- **599 - Maintain Master Data (including Ownership changes)** - Tracks production volumes, receipts, sales
- **453 - Calculate Actual Storage & Inventory Volumes** - Reconciles tank levels, performs stock loss control

**Rationale:** These systems perform dual role of accounting for what was produced (599) and reconciling physical inventory (453). Both L2 capabilities are Primary functions.

**Example SQL:**
```sql
-- AORA tracks production AND inventory
INSERT INTO app_business_capability VALUES (108, 599, 'Primary', 'AORA tracks production volumes...');
INSERT INTO app_business_capability VALUES (108, 453, 'Primary', 'Calculates and tracks actual storage...');
```

---

### Process Simulation & Optimization

**App Type:** Process modeling software (Aspen HYSYS, Petro SIM, Promax)

**L1 Parent:** 86 - Process/Facilities Optimization

**L2 Mappings:**
- **193 - Process Modelling & Simulation** - Rigorous steady-state/dynamic modeling
- **195 - Optimize & Improve Operations** - "What-if" scenarios, performance improvement

**Rationale:** Modeling tools are used both for simulation (193) and operational optimization (195). If app is primarily used for design vs operations, may map only to 193.

**Decision Tree:**
- Used for unit design/new projects ONLY → 193 only
- Used for operations troubleshooting/optimization → 193 + 195
- Real-time optimization (APC) → 195 + 412 (Equipment Monitoring & Control)

---

### Commodity Trading Platforms

**App Type:** CTRM systems (Allegro Horizon, Canadian Industrial Products)

**L1 Parent:** 112 - Commodity Trading, 153 - Market Risk Management, 40 - Settlement

**L2 Mappings:**
- **157 - Physical Trade Execution** - Entering and managing physical commodity deals
- **234 - Trade Reporting** - Compliance reporting, trade confirmations
- **303/337/339 - Settle Crude/Gas/Products** - Invoice generation, payment processing
- **532 - Measure Risk** - Mark-to-market, VaR calculation
- **188 - Perform Position Analysis** - Open position reports, exposure analysis

**Rationale:** Modern CTRM platforms are comprehensive, supporting full deal lifecycle from execution through settlement and risk. Map to all L2s the specific instance actively uses.

**Variant Examples:**
- **Allegro (Nat Gas)** → 157, 234, 532, 188 (natural gas physical + financial)
- **Allegro (Derivatives)** → 416 (Exchange Trades), 234, 532, 189 (P&L) - no settlement (cleared)
- **Allegro (CDN RP)** → 157, 303, 532, 173 (inventory visibility) - refined products

---

### Maintenance & Reliability Systems

**App Type:** CMMS, APM, integrity management (GE APM, DamageWeb, CMX)

**L1 Parent:** 31 - Maintenance & Reliability

**L2 Mappings:**
- **427 - Asset Reliability Management** - Predictive maintenance, RCM, FMEA
- **206 - Preventative Maintenance** - PM work orders, scheduled inspections
- **388 - Facility Integrity Management** - Corrosion monitoring, RBI, fitness-for-service
- **168 - Process Integrity Management** - PSM, PSSR, HAZOP tracking
- **318 - Rotating Equipment Management** - Vibration analysis, alignment, condition monitoring
- **562 - Inspection** - NDE, visual inspection data collection
- **564 - Instrumentation Repair** - Calibration, loop testing

**Decision Matrix:**

| System Type | Primary L2s |
|-------------|-------------|
| **CMMS (work order system)** | 206 (Preventative Maintenance), 270 (Work Order Planning) |
| **APM (analytics platform)** | 427 (Asset Reliability), 388 (Facility Integrity) |
| **Corrosion tracking** | 388 (Facility Integrity), 562 (Inspection) |
| **Vibration analysis** | 318 (Rotating Equipment), 427 (Asset Reliability) |
| **Calibration system** | 564 (Instrumentation Repair), 406 (Engineering Info Mgmt) |

**Example:**
- **DamageWeb** → 388 (identifies damage mechanisms), 562 (guides inspection methods)
- **CMX Professional** → 564 (calibration tracking), 231 (compliance performance)

---

### Laboratory Information Systems

**App Type:** LIMS, COA, quality control (Matrix Gemini, Baytek COA)

**L1 Parent:** 96 - Lab Services Management

**L2 Mappings:**
- **571 - In-House Lab Testing** - Sample analysis, test result entry
- **294 - Sample Results Management** - Result approval, out-of-spec handling
- **293 - Sample Collections Management** - Sample registration, chain of custody

**Rationale:** Most LIMS span all three L2s. If app only handles subset of workflow, map accordingly.

**Specialty Systems:**
- **COA generation only** (Baytek) → 571 (testing workflow), 294 (results management)
- **Portable analyzer sync** (NitonConnect) → 571 only
- **Chromatograph data system** (Maxum) → 571 only

---

### Transportation & Logistics

**App Type:** TMS, rail/truck logistics, pipeline SCADA

**L1 Parent:** 81 - Product Movement, 114 - Transport Management, 47 - Pipeline Management

**L2 Mappings:**

**Terminal Management:**
- **551 - Manage Terminal Movements** - Loading/unloading operations
- **453 - Calculate Actual Storage & Inventory** - Tank gauging, inventory reconciliation

**Rail/Truck:**
- **360 - Dispatch Management** - Route optimization, driver assignment
- **552 - Manage Terminal/Storage Movements & Volumes** - Bill of lading, shipment tracking

**Pipeline:**
- **220 - Pipeline Operations** - SCADA control, line balancing
- **539 - Manage Pipeline Nominations & Allocations** - Shipper nominations, volume allocation

**Example Decision:**
- **Bourque Logistics** → 552 (YardMaster yard mgmt), 551 (RAILTRAC fleet tracking), 360 (dispatch)
- **TMS TopTech** → 551 (terminal operations), 453 (inventory calculation)
- **IPS (pipeline)** → 220 (operations), 539 (nominations)

---

### Retail & Point of Sale

**App Type:** POS systems, payment processing, site management

**L1 Parent:** 33 - Execute & Monitor Commercial Sales & Operations, 40 - Settlement

**L2 Mappings:**
- **157 - Physical Trade Execution** - POS transaction capture (retail is a "trade")
- **199 - Pay** - Payment processing, card authorization
- **549 - Manage Settlement Disputes** - Back-office reconciliation

**Rationale:** Retail POS systems execute physical product sales (157) and process payments (199). Back-office systems also reconcile to financial systems (549).

**Component Breakdown:**
- **POS terminal** (POSitouch, Storepoint POS) → 157, 199
- **Authorization server** → 157 (transaction storage), 199 (payment routing)
- **Site management** (SMS) → 157 (sales tracking), 549 (settlement recon)
- **Card management** (Ackroo, VistaExpress) → 199 only

---

### Environmental, Health & Safety

**App Type:** Emissions tracking, process safety, emergency response

**L1 Parent:** 34 - Environmental Management, 147 - Control of Work, 27 - Military Management

**L2 Mappings:**

**Environmental:**
- **621 - Manage Air Emissions** - Emissions monitoring, air permit compliance
- **524 - Manage Water** - Water treatment, discharge monitoring
- **523 - Manage Waste** - Waste tracking, disposal management
- **545 - Manage Regulatory Compliance & Regulations** - Environmental permit tracking

**Process Safety:**
- **304 - Safe Operations** - Process safety management, MOC, SIS management
- **581 - Hazard Management** - HAZOP, PHA, what-if analysis
- **588 - Isolation Management** - LOTO, energy isolation

**Emergency Response:**
- **557 - Industry Emergency Coordination** - Emergency response planning, drills
- **621 - Manage Air Emissions** (for plume modeling tools like ALOHA/Cameo)

**Examples:**
- **Honeywell Safety Suite** → 304 (safe operations), 168 (process integrity)
- **CNotes ASM** → 304 (abnormal situation mgmt), 191 (shift handover ops monitoring)
- **Aloha/Cameo** → 621 (air emissions plume), 557 (emergency coordination)

---

### Data, Analytics & Integration

**App Type:** BI platforms, data integration, document management

**L1 Parent:** 30 - Data & Knowledge Management, 79 - IT Strategy & Governance

**L2 Mappings:**

**BI/Reporting:**
- **431 - BI, Analytics & Data Science** - Dashboards, self-service analytics, ML
- **307 - Reporting & Analytics** (HR context) - Standard reports, KPIs

**Data Integration:**
- **376 - Data Engineering & Integration** - ETL, data pipelines, API integration
- **555 - G&G Data Integration** - Geoscience data (upstream primarily)

**Document/Content:**
- **459 - Content Management** - Document repositories, records management, ECM
- **297 - Search** - Full-text search, metadata search

**Geospatial:**
- **579 - Geospatial Data Management** - GIS, mapping, spatial analysis

**Examples:**
- **Crystal Reports Server** → 431 (BI and analytics reporting)
- **Denodo** → 376 (data virtualization integration), 555 (data integration)
- **Cascade** → 459 (document management), 191 (operations document workflow)
- **Mapper, Google Maps API** → 579 (geospatial data)

---

### Project & Capital Management

**App Type:** Project scheduling, cost management

**L1 Parent:** 105 - Capital Asset Management, 62 - IT Project Management, 83 - Facility Design

**L2 Mappings:**
- **186 - Project Scheduling** - CPM scheduling, Gantt charts, resource loading
- **612 - IT Project Delivery** - IT project planning and execution
- **165 - Perform Project Accounting** - Project cost tracking, commitments
- **450 - Allocate Capital Budget** - Capital forecasting, AFE management
- **366 - Detailed Engineering** - Engineering deliverables during FEED/detailed design

**Examples:**
- **Primavera P6 (refinery)** → 186 (project scheduling for capital projects)
- **Primavera P6 (CVE IT)** → 612 (IT project delivery)
- **EcoSys** → 165 (project accounting), 450 (capital budget allocation)

---

### Personnel & Certification

**App Type:** Training, certification tracking, workforce management

**L1 Parent:** 101 - Certification Management, 92 - Professional Development

**L2 Mappings:**
- **257 - Tickets & Credentials** - Certification tracking, expiry management
- **590 - Learning Management** - Training courses, completion tracking
- **235 - Training & Qualification** - Competency assessment, qualification matrix
- **426 - Asset & Resource Location Tracking** - Real-time worker location

**Examples:**
- **PCMS (all variants)** → 257 (tickets and credentials)
- **AllegroU** → 590 (learning management for Allegro training)
- **Track SAAS** → 426 (workforce location tracking)

---

## Special Cases & Edge Cases

### Legacy/Archived Systems
**Rule:** Still map if actively used for historical data queries or regulatory retention
**Example:** SHS Toledo Legacy → 191 (Operations Monitoring) with note "(archived, replaced by CNotes)"

### Multi-Site Instances
**Rule:** Each site instance gets its own app record and L2 mapping (may be identical)
**Example:** AORA (Lima), AORA (Toledo), AORA (Superior) - all map to 599 + 453 with site-specific notes

### Vendor Monitoring Tools
**Rule:** Vendor-provided SaaS monitoring (Shell Cat-Check, UOP Process Monitor, ClearView) → 195 (Optimize & Improve)
**Rationale:** These are optimization tools provided by technology licensors

### Terminal Emulators & Middleware
**Rule:** Infrastructure tools that enable access to other apps
- If enabling app access → 424 (Application Service Delivery)
- If pure data integration → 376 (Data Engineering & Integration)
**Example:** AnzioWin → 424, File Transfer Switch → 376

### Retail Pricing Data Feeds
**Rule:** External data subscriptions (DTN, PLATTS, Argus) → 541 (Manage Published Prices) + 529 (Market Analysis)
**Rationale:** These provide pricing data as a service, not execution capability

---

## Validation Checklist

Before finalizing an L2 mapping, verify:

- [ ] **L2 is child of correct L1** - Check bcm_L1_L2_hierarchy.csv
- [ ] **App truly enables the L2** - Not just "related" or "supporting"
- [ ] **Most specific L2 chosen** - Don't stop at L1 level
- [ ] **Notes justify the mapping** - Clear 1-sentence rationale
- [ ] **Multi-function apps have multiple mappings** - Don't force single L2 if app does multiple things
- [ ] **Consistent with similar apps** - All LIMS should map similarly unless different scope

---

## Common Mistakes to Avoid

### ❌ Mapping to L1 instead of L2
**Wrong:** AORA → Production Accounting (L1 99)
**Right:** AORA → Maintain Master Data (L2 599) + Calculate Actual Storage (L2 453)

### ❌ Forcing single L2 for multi-function app
**Wrong:** Allegro → Physical Trade Execution (157) only
**Right:** Allegro → 157, 234, 303, 532, 188 (all L2s it actively supports)

### ❌ Using "Secondary" role for Primary functions
**Wrong:** HYSYS → Process Modelling (193), 'Secondary'
**Right:** HYSYS → Process Modelling (193), 'Primary'

### ❌ Mapping infrastructure to business capabilities
**Wrong:** JBoss → Production Accounting (599)
**Right:** JBoss → Application & Automation Platforms (422)

### ❌ Generic notes without specificity
**Wrong:** "Supports production operations"
**Right:** "Tracks production volumes, receipts, sales and performs yield accounting reconciliation for Lima refinery"

---

## Updates & Maintenance

**Frequency:** Review mappings quarterly or when:
- New applications onboarded
- App functionality significantly changes
- BCM hierarchy updated (new L2s added)
- Portfolio rationalization identifies duplication

**Process:**
1. Identify trigger (new app, functionality change, etc.)
2. Determine affected L1 parent capability
3. Select most specific L2(s) using this guide
4. Update SQL mapping file
5. Notify ea-downstream-apps of change

---

**Document Version:** 1.0
**Last Updated:** 2026-02-09
**Next Review:** 2026-05-09
**Owner:** Downstream Applications Portfolio Architect
