# L2 Business Capability Mapping - WAVE 2 Summary

**Date:** 2026-02-09
**Architect:** Enterprise Applications Portfolio Architect
**Project:** L2 Business Capability Mapping - Wave 2

---

## Executive Summary

Successfully completed WAVE 2 of the L2 business capability mapping, covering **233 unique applications** across Enterprise, Shared Services, Cybersecurity, OT, and AI Governance domains. This represents the remaining unmapped applications after WAVE 1 (which mapped 102 apps).

---

## Scope Coverage

### Applications by Business Unit

| Business Unit | Application Count | Primary Focus |
|--------------|------------------|---------------|
| **Apps - Shared Services** | ~120 | Infrastructure, networking, device management, print services, VDI, OS management |
| **Cyber Security Operations** | ~45 | Endpoint protection, SIEM, IDS/IPS, MFA, vulnerability scanning, email security |
| **Business - OT (BST/LOB)** | ~40 | SCADA systems, DCS, HMI, equipment monitoring, facilities control |
| **Apps - Enterprise** | ~25 | SAP modules, BI/analytics, data integration, testing, EAM, finance |
| **Business - HMGP (BST/LOB)** | 3 | Pipeline SCADA, leak detection, alarm management |
| **Apps - Data and AI Governance** | 1 | Data marketplace and governance |

---

## L2 Capability Distribution

### Top L2 Capabilities Mapped

1. **Equipment Monitoring & Control (412)** - 35 OT/SCADA applications
2. **Cyber Protection (372)** - 42 cybersecurity applications
3. **IT Operations (610)** - 38 shared services applications
4. **Device Management (357)** - 18 endpoint management applications
5. **Network Connectivity (184)** - 12 networking applications
6. **Physical Infrastructure Management (167)** - 10 infrastructure applications
7. **Cyber Detection (370)** - 9 SIEM/IDS applications
8. **BI & Analytics (431)** - 10 analytics/reporting applications
9. **Integration Architecture (565)** - 8 integration/middleware applications
10. **Build & Automation Tools (433)** - 5 DevOps applications

### Key Mapping Patterns

#### Shared Services Applications
- **IT Infrastructure**: Mapped to L2 capabilities under "IT Service Delivery" (610, 167, 184)
- **Communication Tools**: Mapped to "Communication & End User Computing" (238, 482, 357)
- **DevOps Tools**: Mapped to "Build & Automation Management" (433, 421, 271)
- **Directory Services**: Mapped to "Cyber Protection" (372)

#### Cybersecurity Applications
- **Endpoint Security**: McAfee, Symantec → Cyber Protection (372)
- **SIEM/Logging**: Splunk, Windows Event Collector → Cyber Detection (370)
- **MFA/Identity**: RSA, Okta, Microsoft Authenticator → Cyber Protection (372)
- **Vulnerability Scanning**: Qualys, Prisma Cloud → Cyber Risk Identification (374)
- **Email Security**: Proofpoint → Cyber Protection (372)
- **Compliance**: SOXHUB, Proofpoint Audit → Cyber Governance (371)

#### OT/SCADA Applications
- **SCADA Systems**: Honeywell Experion, Open BSI, RSView → Equipment Monitoring & Control (412)
- **PLC Programming**: Rockwell RSLogix, Schneider Unity Pro → Equipment Monitoring & Control (412)
- **Pipeline SCADA**: Lloyd SCADA systems → Pipeline Management (220) / Pipeline Integrity (180)

#### Enterprise Applications
- **SAP Modules**:
  - ECC/S/4HANA → Maintenance Planning (270), General Accounting (309), Procurement (209)
  - Analytics: SAC, BOBJ, BW → BI & Analytics (431)
  - Integration: CPI, PO, SLT → Integration Architecture (565)
  - GRC → Cyber Governance (371)
- **HCM Systems**: Workday, SuccessFactors → Performance Management (179), HR Operations (222)
- **Testing Tools**: Tosca, qTest → App Development (421)

---

## File Locations

### Source Files
- **BCM Hierarchy**: `C:\Users\skavbr\Documents\Claude_Projects\EA_Team\team_folder\Source_Data\bcm_L1_L2_hierarchy.csv`
- **Unmapped Apps**: `C:\Users\skavbr\Documents\Claude_Projects\EA_Team\team_folder\Source_Data\apps_unmapped_L2_other.csv`

### Output Files
- **SQL Mapping Script**: `C:\Users\skavbr\Documents\Claude_Projects\EA_Team\team_folder\Source_Data\L2_mapping_other_wave2.sql`
- **Summary Report**: `C:\Users\skavbr\Documents\Claude_Projects\EA_Team\team_folder\Enterprise_Architects\Enterprise_Applications\L2_Mapping_Wave2_Summary.md`

---

## SQL Script Details

- **Total INSERT Statements**: 233
- **Table**: `app_business_capability`
- **Columns**: `application_id`, `business_capability_id`, `capability_role`, `notes`
- **Capability Role**: All mapped as "Primary"
- **Notes Format**: "App Name - L2 Capability Name - Brief justification"

---

## Mapping Methodology

1. **Analyzed Application Descriptions**: Used short_description, vendor, and business_unit fields
2. **Applied Domain Expertise**:
   - Infrastructure → IT Service Delivery L2s
   - Security → Cyber Security L2s (Governance, Risk ID, Protection, Detection, Response)
   - OT/SCADA → Equipment Monitoring & Control
   - Enterprise Apps → Functional L2s (Finance, HR, Analytics, etc.)
3. **Ensured Completeness**: Mapped ALL 233 unique applications
4. **Used Correct L2 IDs**: Referenced from bcm_L1_L2_hierarchy.csv
5. **Escaped Special Characters**: Single quotes escaped with '' for SQL compatibility

---

## Notable Application Groupings

### SAP Ecosystem (25+ apps)
- Core: ECC, S/4HANA, BW, HANA, Portal, GUI
- Integration: PO, CPI, Cloud Connector, SLT, Replication Server
- Analytics: SAC, BOBJ, BW, HANA BI, HANA Datamart
- Governance: GRC, Information Steward, SolMan
- Infrastructure: Router, Web Dispatcher, TREX, SLD

### Microsoft Ecosystem (15+ apps)
- Productivity: M365, Office Apps, Teams, Visio
- Identity: Authenticator, MFA Server
- Infrastructure: DHCP, SCCM, AD tools
- Security: Cloud App Security, O365 Compliance Console
- OS: Windows 7/10, Server editions

### Cybersecurity Stack (45+ apps)
- Endpoint: McAfee ePO, Symantec, Sophos
- Network: Panorama, Sourcefire, ISE
- SIEM: Splunk (3 instances)
- Email: Proofpoint (3 modules)
- Identity: Okta, RSA, Yubikeys
- Scanning: Qualys, Prisma Cloud, NMap
- Monitoring: Tripwire, Windows Event Collector

### OT/SCADA Portfolio (40+ apps)
- Honeywell Experion, Open BSI suite, Rockwell (RSView, RSLogix)
- Emerson (ROCLINK), Schneider (Unity Pro), Matrikon gateway
- Specialized: Win 911 alarms, RodStar, Prochart, Zedi, eServer
- Pipeline: Lloyd SCADA suite (3 modules)

---

## Next Steps

1. **Execute SQL Script**: Run L2_mapping_other_wave2.sql against ea_architecture.db
2. **Validate Mappings**: Query to confirm all 233 apps now have L2 mappings
3. **Report to EA Lead**: Share completion status with ea-enterprise-apps
4. **Update Dashboard**: Reflect new mapping coverage in EA metrics
5. **Documentation**: Archive this summary in team knowledge base

---

## Statistics Summary

| Metric | Count |
|--------|-------|
| Total Applications Mapped | 233 |
| Total SQL INSERT Statements | 233 |
| Business Units Covered | 6 |
| Unique L2 Capabilities Used | ~45 |
| SAP Applications | 28 |
| OT/SCADA Applications | 40 |
| Cybersecurity Applications | 45 |
| Infrastructure Applications | 90+ |

---

## Quality Assurance

- All application IDs verified against source CSV
- All L2 capability IDs verified against BCM hierarchy
- Single quotes properly escaped in notes field
- INSERT OR IGNORE used to prevent duplicate key errors
- Capability_role consistently set to 'Primary'
- Brief justifications provided for all mappings

---

**Mapping Completed By:** Enterprise Applications Portfolio Architect
**Review Status:** Ready for execution and validation
**Escalation Path:** ea-enterprise-apps (Enterprise Architect)
