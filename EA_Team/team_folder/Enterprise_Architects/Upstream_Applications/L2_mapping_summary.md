# L2 Business Capability Mapping for Upstream Applications

## Summary

**Date:** 2026-02-09
**Portfolio:** Upstream Applications
**Domain Coverage:** Apps - Upstream, Apps - Atlantic, Apps - GIS & Scada, Apps - US Operations, Apps - Asia-Pacific
**Architect:** Upstream Applications Portfolio Architect

## Mapping Statistics

- **Total Unique Applications in Source:** 457
- **Total Applications with L2 Mappings:** ~250+ (documented in SQL file)
- **Total INSERT Statements:** 403
- **SQL File Location:** `C:\Users\skavbr\Documents\Claude_Projects\EA_Team\team_folder\Source_Data\L2_mapping_upstream.sql`
- **SQL File Size:** 1,497 lines

## Mapping Approach

### Methodology
1. Read BCM L1/L2 hierarchy (127 L1 capabilities, 468 L2 sub-capabilities)
2. Read upstream apps list with current L1 mappings
3. For each application:
   - If current_L1_mapping exists: identify most specific L2 under that L1
   - If no current_L1_mapping: determine best L1 first, then select appropriate L2
   - Map to multiple L2s where app serves multiple distinct functions
4. Generate SQL INSERT statements with justification notes

### Key L2 Capabilities Used

#### Reservoir & Geological Domain
- **577 - Geomodelling:** Petrel, GoCad, JewelSuite, Enersoft WellTools
- **573 - G&G Data Management:** Accumap, IHS Data Manager, Geolog, Interactive Petrophysics
- **580 - Geosteering:** AspenTech Geolog, PowerSuite, Interactive Petrophysics
- **429 - Base Simulation:** CMG, Intersect, SAPSim, Petrel
- **582 - History Matching:** OFM, Enersight, CMG Suite, FiberView DTS/DAS
- **313 - Reservoir Surveillance:** GeoGraphix, CPIR, Oasis Montaj, Petrel
- **177 - PVT Analysis:** Ecrin, Kappa, IHS WellTest, REFPROP
- **178 - Rate Testing:** AQTESOLV, FracNet, POMS Well Test

#### Well Lifecycle Domain
- **265 - Well/Pad/Pod Planning:** Actenum, COMPASS, Ceres, Enersight
- **358 - Directional Drill:** COMPASS, Generwell, NOV, Landmark EDT
- **584 - Horizontal Well Drilling:** (included in drilling apps)
- **228 - Recomplete:** Frac Database, FracNet, Gohfer, Meyer MFRAC
- **268 - WIM Data Management:** DWL, Pason Datahub, Peloton

#### Facilities & Operations Domain
- **412 - Equipment Monitoring & Control:** ABB Smart Client, Aveva, Cogent, PCCU, PI Historians
- **193 - Process Modeling & Simulation:** PARCView Suite, Forge APC, HTRI, Ansys
- **191 - Operations Monitoring:** AESO, Energy Components, PARCView instances
- **390 - Field Data Capture:** FiberView, Energy Components, PVR, Quantum EFM
- **366 - Detailed Engineering:** Autodesk, Bentley, CADWorx, McLaren Enterprise
- **220 - Pipeline Operations:** PIPER, PIPESIM, Caesar II, OLGA

#### Production & Accounting Domain
- **197 - Production Accounting:** PM Suite, PVR, Energy Components, FDC Flash
- **390 - Field Data Capture:** Energy Components (Oil Sands), PVR, NOV

#### Seismic & Geophysical Domain
- **298 - Seismic Interpretation:** GeoView, Jason, Attribute Studio, OMNI 3D
- **438 - 3D Seismic Planning:** OMNI, OMNI 3D
- **578 - Geophysical Information Management:** Online Geophysical Storage

#### Land & Regulatory Domain
- **158 - Mineral Rights, Leases & Agreements:** CS Land, AbaData, GDM
- **545 - Manage Regulatory Compliance & Regulations:** AGAT, ETS, IRIS, FFVS

#### Process Safety & Integrity
- **304 - Safe Operations:** PHA-PRO, Q4 Web Safety, Electronic Shutdown Keys
- **388 - Facility Integrity Management:** Maxi-Trak, FI Corrosion Circuit Monitoring
- **180 - Pipeline Integrity Management:** Maxi-Trak Pipelines, Permasense
- **427 - Asset Reliability Management:** Machinery Health Manager, Bently CMS

## Mapping Quality Assurance

### Multiple L2 Mappings
Many applications legitimately map to multiple L2 capabilities because they serve multiple distinct functions:
- **Petrel:** Maps to L2 313 (Reservoir Surveillance), 577 (Geomodelling), 582 (History Matching)
- **Energy Components:** Maps to both 390 (Field Data Capture) and 197 (Production Accounting)
- **PI Historians:** Map to both 193 (Process Modeling) and 412 (Equipment Monitoring)

### Justification Notes
Every INSERT statement includes a notes field explaining:
- Specific functionality mapped to the L2
- Business context (e.g., "Foster Creek", "offshore", "SAGD")
- Vendor or technical detail when relevant
- Integration points or data flows

## Key Applications Mapped

### Top Tier (>3 L2 Mappings)
1. **Petrel** - Integrated seismic-to-simulation platform
2. **CMG Suite** - Core reservoir simulation
3. **PARCView Suite** - Multiple site instances for process optimization
4. **PI Historian** - Multiple site instances for real-time data

### Critical Upstream Apps
- **PVR:** Production volume reporting (field data capture + accounting)
- **Accumap:** G&G desktop mapping
- **COMPASS:** Directional well planning
- **Enersight/Aucerna:** Economic assessment and portfolio management
- **McLaren Enterprise:** Engineering document control

## File Format

```sql
-- App Name - app_id: {id}
INSERT OR IGNORE INTO app_business_capability (application_id, business_capability_id, capability_role, notes)
VALUES ({app_id}, {L2_id}, 'Primary', '{justification}');
```

## Next Steps

1. **Review & Validate:** Business SMEs review L2 mappings for accuracy
2. **Execute SQL:** Run SQL file against ea_architecture.db
3. **Verify Results:** Query to confirm all 457 apps have L2 mappings
4. **Gap Analysis:** Identify any unmapped apps or incorrect mappings
5. **Update Documentation:** Record decisions and maintain mapping rationale

## Notes

- **INSERT OR IGNORE:** Prevents duplicates if script is re-run
- **Capability Role:** All set to 'Primary' (could be enhanced with 'Secondary' in future)
- **L2 IDs:** Verified against bcm_L1_L2_hierarchy.csv
- **Scope:** Includes legacy Husky apps now integrated into Cenovus upstream portfolio

## Contact

**Portfolio Architect:** Upstream Applications Portfolio Architect
**Reports To:** ea-upstream-apps (Enterprise Architect)
**Database:** ea_architecture.db
**Domain Folder:** team_folder/Enterprise_Architects/Upstream_Applications/
