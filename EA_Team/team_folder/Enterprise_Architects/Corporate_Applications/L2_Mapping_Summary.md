# Corporate Applications L2 Business Capability Mapping
## Summary Report

**Date Generated:** 2026-02-09
**Portfolio Architect:** Corporate Applications Portfolio Architect
**Domain:** Apps - Corporate (SAP, HR, Finance, Supply Chain, M365, Legal, Compliance, HSE)

---

## Mapping Statistics

- **Total Applications Mapped:** 237 unique corporate applications
- **Total L2 Capability Mappings:** 283 INSERT statements
- **Average Mappings per Application:** 1.2 L2 capabilities
- **SQL File Size:** 1,078 lines
- **SQL File Location:** `C:\Users\skavbr\Documents\Claude_Projects\EA_Team\team_folder\Source_Data\L2_mapping_corporate.sql`

---

## Methodology

### Source Data
1. **BCM Hierarchy:** `bcm_L1_L2_hierarchy.csv`
   - 127 L1 capabilities
   - 468 L2 sub-capabilities

2. **Application Inventory:** `apps_for_L2_mapping_corporate.csv`
   - 397 application-to-L1 mappings (some apps mapped to multiple L1s)
   - Filtered to unique applications for L2 refinement

### Mapping Approach
For each application, the mapping considered:
- **Application Name & Description:** Primary indicator of functionality
- **Vendor Information:** Context for technology stack and purpose
- **Current L1 Mapping:** Starting point for L2 sub-capability selection
- **Business Context:** Corporate domain knowledge (ERP, HR, finance, etc.)

Applications were mapped to:
- **Primary L2 Capability:** Main business function supported
- **Secondary L2 Capabilities:** Additional functions where applicable

---

## Coverage by Domain

### Enterprise Resource Planning (ERP)
- SAP ECC/S4HANA core modules
- Financial accounting and reporting
- Production and revenue accounting
- Capital asset management
- Joint venture accounting

### Human Capital Management (HCM)
- Workday HCM (performance, payroll, compensation, recruiting)
- Benefits administration (health, wellness, pensions)
- Talent management and succession planning
- Learning management systems
- Employee engagement and surveys

### Supply Chain & Procurement
- Procurement execution and sourcing
- Contract lifecycle management
- Materials and inventory management
- Supplier relationship management
- Fleet and transportation management

### Finance & Treasury
- Treasury and cash management (Kyriba, bank portals)
- Tax compliance and reporting (OneSource, RBC filing)
- Budgeting and forecasting
- Royalty and revenue accounting
- General ledger and transaction processing

### Legal & Compliance
- Contract management (Contraxx)
- Regulatory compliance tracking
- Corporate governance (Boardvantage, GEMS)
- Intellectual property management (IPfolio)
- Privacy and data protection (OneTrust)

### Environmental, Health & Safety (HSE)
- Incident management (Intelex)
- Emissions tracking and reporting
- Environmental compliance
- Industrial hygiene and occupational health
- Safety data sheets and chemical management

### Information Technology
- Enterprise content management (OpenText CDMS/EDMS)
- Business intelligence and analytics (Power BI, Spotfire, RStudio)
- Cybersecurity tools (Axiom, Immersive Lab, Keeper)
- IT service management and operations
- Application development and DevOps (GitLab, Automation Anywhere)

### Corporate Communications & Engagement
- Digital signage and corporate displays
- External websites and stakeholder portals
- Mass notification systems (Everbridge)
- Survey and feedback tools (Qualtrics)
- Social responsibility programs (Benevity)

### Operations & Facilities
- Camp and accommodation management (INNfinity platform)
- Travel and transportation logistics
- Building and physical security (C-CURE, Avigilon)
- Emergency management and response
- Military coordination (CLAWR systems)

---

## Key L2 Capabilities Utilized

### Most Common L2 Mappings (Top 15)
1. **Content Management (459)** - Document and ECM systems
2. **Performance Management (179)** - HR talent systems
3. **BI, Analytics & Data Science (431)** - Analytics platforms
4. **Safe Operations (304)** - Safety and security systems
5. **Perform Transaction Processing (161)** - Financial systems
6. **Procurement (209)** - Supply chain execution
7. **Regulatory Compliance & Regulations (545)** - Compliance tracking
8. **Production Accounting (599)** - Revenue and royalty systems
9. **Learning Management (590)** - Training and development
10. **Treasury Management (507)** - Cash and treasury operations
11. **Office Productivity (159)** - M365 and productivity tools
12. **Data Management Technology (378)** - Data platforms
13. **Cyber Detection/Protection (370-372)** - Security tools
14. **Benefits (430)** - Employee benefits administration
15. **Travel & Accommodation (348/464)** - Corporate travel

---

## Notable Multi-Capability Applications

Several applications support multiple business capabilities:

- **SAP ECC/S4HANA:** Transaction processing, reporting, master data, budgeting
- **Workday:** Performance mgmt, payroll, compensation, recruiting
- **Microsoft 365:** Office productivity, collaboration, communications, content mgmt
- **OpenText ECM:** Content management, document workflow, records retention
- **INNfinity Platform:** Camp management, travel logistics, emergency muster
- **Metrix/Optix:** Production accounting, BI analytics, regulatory reporting
- **Kyriba:** Treasury management, cash accounts, disbursements, liquidity

---

## Data Quality Notes

### Well-Documented Applications
Applications with comprehensive descriptions enabled precise L2 mapping:
- Production accounting systems (Metrix, PAS, Qbyte)
- HSE and compliance tools (Intelex, CATs, Emission Central)
- HR systems (Workday, benefits platforms)
- Treasury and tax systems (Kyriba, OneSource suite)

### Limited Information Applications
Some applications had minimal descriptions, mapped to L2 based on:
- Application name patterns
- Vendor technology stack
- Existing L1 mapping context
- Industry standard use cases

### Archive and Legacy Systems
Many data archives mapped to:
- **Content Management (459)** - Data archiving and retention
- Original application's L2 capability + archive notation

---

## Recommendations

### For Enterprise Architect Review
1. **Validate Multi-Capability Mappings:** Review apps with 2+ L2 mappings for accuracy
2. **Assess Capability Gaps:** Identify L2 capabilities with no supporting applications
3. **Rationalization Opportunities:** Multiple apps supporting same L2 (consolidation targets)
4. **Strategic Alignment:** Ensure critical L2 capabilities have adequate application support

### For Portfolio Management
1. **TCO Analysis:** Use L2 mappings to analyze costs by business capability
2. **Capability-Based Budgeting:** Allocate application costs to specific capabilities
3. **Application Lifecycle:** Plan retirements/replacements at capability level
4. **Investment Planning:** Identify under-invested capabilities requiring new solutions

### Data Governance Next Steps
1. **Ongoing Maintenance:** Update mappings as applications change or retire
2. **New Application Onboarding:** Map to L2 capabilities during demand intake
3. **Business Capability Model Evolution:** Adjust mappings when BCM is updated
4. **Integration with EA Database:** Load mappings into `app_business_capability` table

---

## SQL Execution Instructions

### To Load the Mappings:

```sql
-- Connect to EA database
sqlite3 C:\Users\skavbr\sqlite\ea_architecture.db

-- Execute the mapping file
.read C:\Users\skavbr\Documents\Claude_Projects\EA_Team\team_folder\Source_Data\L2_mapping_corporate.sql

-- Verify results
SELECT COUNT(*) FROM app_business_capability
WHERE business_capability_id IN (SELECT id FROM business_capabilities WHERE level = 'L2');

-- Check applications with no L2 mappings
SELECT a.id, a.name, a.business_unit
FROM applications a
WHERE a.business_unit = 'Apps - Corporate'
AND a.id NOT IN (
    SELECT DISTINCT application_id
    FROM app_business_capability abc
    JOIN business_capabilities bc ON abc.business_capability_id = bc.id
    WHERE bc.level = 'L2'
);
```

---

## Files Delivered

1. **L2_mapping_corporate.sql** (1,078 lines, 283 INSERT statements)
   - Location: `team_folder/Source_Data/L2_mapping_corporate.sql`
   - Ready for database import

2. **L2_Mapping_Summary.md** (This document)
   - Location: `team_folder/Enterprise_Architects/Corporate_Applications/L2_Mapping_Summary.md`
   - Summary and recommendations

---

## Contact

**Portfolio Architect:** Corporate Applications Portfolio Architect
**Reports To:** ea-corporate-apps (Corporate Applications Enterprise Architect)
**Domain:** Apps - Corporate
**Database:** ea_architecture.db
**Query Filter:** `business_unit = 'Apps - Corporate'`

---

*End of Report*
