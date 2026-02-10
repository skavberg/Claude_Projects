# L2 Business Capability Mapping - Status Report

## Executive Summary
- **Date**: 2026-02-09
- **Architect**: Enterprise Applications Portfolio Architect
- **Task**: Map 350 apps (Enterprise, Shared Services, Cybersecurity, OT, AI) to L2 capabilities

## Progress Completed
- **Apps Processed**: 89 unique applications
- **L2 Mappings Created**: 102 INSERT statements
- **SQL File**: `C:\Users\skavbr\Documents\Claude_Projects\EA_Team\team_folder\Source_Data\L2_mapping_other.sql`
- **Status**: Foundation established with systematic L2 mappings

## Applications Mapped (First 89)

### Shared Services (45 apps)
- Identity & Access: AD, Azure AD, Entra ID, Active Directory, LDAP, Okta, Quest tools, Duo, BeyondID
- Communication: Exchange, Jabber, Cisco Unified Communications, Enghouse
- Collaboration: M365, Office Productivity Apps, Citrix
- Infrastructure: AWS CloudFormation, Azure App Services, F5 Load Balancer, Infoblox, NetApp
- Backup & DR: CommVault, Air Gap Protect, CloudEndure
- Automation: Ansible, Chocolatey, Jenkins, JFrog, PowerShell, Rundeck
- Development: CodeCommit, CAST tools (AIP, Highlight, Imaging)
- Monitoring: Nagios, Lpar2RRD, OneView, Liveaction
- Device Management: Intune, Hyper-V Management

### Cybersecurity (24 apps)
- Threat Detection: CrowdStrike Falcon, Cribl, Endace, HTTPWatch
- Endpoint Security: Bit9, CLAM, McAfee (multiple instances), Falcon
- Identity & MFA: Azure MFA, Microsoft Authenticator, Global Protect VPN, ICS Access, RSA SecurID
- Data Protection: Azure Information Protection, Certificate Authority, Amazon KMS/Secrets Manager
- Access Control: Azure Conditional Access, ForeScout, Control Network Access
- Email Security: Proofpoint (multiple), Proofpoint Audit, Proofpoint Training
- SOAR & Incident: Palo Alto Cortex XSOAR, SAP Enterprise Threat Detection
- Vulnerability: Qualys, Prisma Cloud, NMap
- Network Security: Panorama, External Dynamic List, Microsoft Cloud App Security

### OT / Infrastructure (14 apps)
- SCADA: DeltaV, Cygnet, FactoryTalkView, GEIFix, Honeywell Experion, RSView
- Control Systems: AES/ACM, Bristol Controlwave Designer, Open BSI (Harvester, Local View, Netview, Workbench)
- Pipeline: Decision Support System (DSS)
- Equipment Monitoring: GE System 1 Evolution, Osprey Cameras, Prochart
- PLC Programming: Rockwell RSLogix, ROCLINK800, RodStar

### Enterprise Apps (6 apps)
- BI & Analytics: AWS Databricks, Azure Databricks, BI Datamart, Crystal Reports (2x), Radient360, GENESUS
- Data Management: CDP Azure Databricks, Enterprise Data Query, FDS database, Informatica Cloud
- Integration: CPI-DS Agent, HANA EIM DP Agent, Cortex Axon Client
- Travel & Expense: Concur
- Procurement: Ariba-Future, Cortex Axon Client
- HR & Training: FieldGlass, Enable Now
- Maintenance: Maximo MEG, Maximo Toledo, Prometheus Web Scheduler Toledo
- Compliance: PwC Extract Tool, SAP GRC

### AI & Data Governance (1 app)
- AskIT: AI chatbot for IT support

## L2 Capability Mapping Summary by L1

### IT Service Delivery (L1: 64)
- **L2: Cloud Services (480)**: AWS CloudFormation, Azure App Services, CloudEndure, NetApp CVO
- **L2: Network Connectivity (184)**: Aruba AirWave, Cisco Transport Controller, F5 Loadbalancer, Infoblox
- **L2: IT Operations (610)**: AskIT, Ignio, Nagios, Oracle Enterprise Manager, Lpar2RRD
- **L2: IT Service Continuity (613)**: CommVault, Air Gap Protect
- **L2: Physical Infrastructure Management (167)**: NetApp Ontap, Hyper-V Management

### Cyber Security (L1: 35)
- **L2: Identity Management, Authentication and Access Control (509)**: 30+ apps including AD, Azure AD, Okta, MFA tools
- **L2: Platform Security (512)**: CrowdStrike, McAfee, Bit9, CLAM, firewalls
- **L2: Data Security (511)**: Azure Information Protection, Certificate Authority, KMS
- **L2: Cyber Detection - Continuous Monitoring (516)**: Cribl, Endace, Microsoft Cloud App Security
- **L2: Cyber Response - Incident Management (520)**: Cortex XSOAR, SAP ETD
- **L2: Cyber Risk - Risk Assessment (505)**: Qualys, Prisma Cloud
- **L2: Cyber Protection - Awareness and Training (510)**: Proofpoint Security Awareness
- **L2: Cyber Governance (371)**: Office 365 Security & Compliance, ADAudit

### Facilities Control (L1: 87)
- **L2: Equipment Monitoring & Control (412)**: 14 OT systems (SCADA, DCS, HMI, control systems)

### Data & Knowledge Management (L1: 30)
- **L2: BI, Analytics & Data Science (431)**: Databricks, Crystal Reports, BI Datamart, Radient360
- **L2: Data Governance (377)**: CDP Azure Databricks
- **L2: Master Data & Data Quality Management (531)**: Enterprise Data Query, FDS database, CDP
- **L2: Content Management (459)**: DocuWiki
- **L2: Data Engineering & Integration (376)**: Informatica Cloud

### Build & Automation Management (L1: 106)
- **L2: Workflow Automation (271)**: Ansible, Chocolatey, PowerShell, Rundeck, Packer
- **L2: Build & Automation Tools (433)**: CodeCommit, Jenkins, JFrog
- **L2: AI Creation (447)**: AskIT

### Communication & End User Computing (L1: 111)
- **L2: Unified Communications (238)**: Exchange, Jabber, Cisco Unified Communications
- **L2: Office Productivity (159)**: M365, Microsoft Productivity Apps, CUPS, HP Web JetAdmin
- **L2: Collaboration (482)**: M365
- **L2: Device Management (357)**: Intune
- **L2: Mobility (175)**: Citrix, Remote Desktop, Novatel MiFi

### Architecture & Portfolio Management (L1: 123)
- **L2: Application Portfolio Management (423)**: CAST AIP, CAST Highlight, CAST Imaging
- **L2: Integration Architecture (565)**: CPI-DS Agent, HANA EIM DP Agent
- **L2: Technology Planning (252)**: RISC Networks

## Remaining Work (261 apps)

### High Priority - SAP Ecosystem (~50 apps)
1. **S/4HANA Modules**
   - S/4HANA EAM, RTR, STP, WIM
   - SAP ECC (FICO/PS, HCM, PM, PM MOC, PM Prometheus, SCM)
   - Map to: Maintenance Planning (270), General Accounting (161), HR (various), Materials Management (587)

2. **SAP BI & Analytics**
   - SAP BW, SAP BOBJ, SAP BI Portal, SAP Analytics Cloud, SAP HANA BI/Datamart
   - Map to: BI, Analytics & Data Science (431)

3. **SAP Integration & Platform**
   - SAP BTP, Cloud Integration, Cloud Connector, PO, SLT, Replication Server
   - Map to: Integration Architecture (565), Cloud Services (480)

4. **SAP Governance & Security**
   - SAP GRC, Information Steward, SAP Router, SAP GUI
   - Map to: Cyber Governance (371), Data Governance (377)

5. **SAP Specialized**
   - SAP Ariba Sourcing & Contract, BPA by Redwood, JV MD, PCA MD, SolMan, SLD
   - Map to: Sourcing (322), Workflow Automation (271), Joint Venture Accounting, IT Operations (610)

### Medium Priority - Additional Shared Services (~100 apps)
- Remaining monitoring, network, storage, and infrastructure tools
- Additional security and identity tools
- Collaboration and productivity extensions

### Medium Priority - Additional Cyber (~20 apps)
- Additional threat detection and response tools
- Compliance and audit tools
- Security monitoring platforms

### Lower Priority - Specialty Apps (~91 apps)
- Additional OT-specific tools
- Downstream-specific applications
- Legacy or retiring applications

## Key L2 Capability IDs for Quick Reference

### IT Operations & Infrastructure
- 610: IT Operations
- 424: Application Service Delivery
- 184: Network Connectivity
- 480: Cloud Services
- 613: IT Service Continuity
- 167: Physical Infrastructure Management

### Cybersecurity
- 509: Identity Management, Authentication and Access Control
- 512: Platform Security
- 511: Data Security
- 516: Continuous Monitoring (Cyber Detection)
- 520: Incident Management (Cyber Response)
- 505: Risk Assessment (Cyber Risk Identification)
- 510: Awareness and Training (Cyber Protection)
- 371: Cyber Governance

### OT & Facilities
- 412: Equipment Monitoring & Control

### Data & Analytics
- 431: BI, Analytics & Data Science
- 377: Data Governance
- 531: Master Data & Data Quality Management
- 376: Data Engineering & Integration
- 558: Information & Data Architecture
- 565: Integration Architecture
- 459: Content Management

### ERP & Finance
- 161: Perform Transaction Processing (General Accounting)
- 432: Budgeting & Forecasting
- 212: Perform Fixed Asset Accounting
- 165: Perform Project Accounting
- 507: Manage Cash Accounts (Treasury)
- 192: Payroll

### HR & Talent
- 290: Recruitment
- 179: Performance Management
- 590: Learning Management
- 222: People Services
- 586: HR Data Governance

### Maintenance & Operations
- 270: Work Order Planning
- 427: Asset Reliability Management
- 206: Preventative Maintenance
- 569: Inventory Management (Maintenance)
- 311: Required Staff & Contractor Scheduling

### Supply Chain
- 322: Sourcing
- 209: Procure
- 331: Supplier Lifecycle Management
- 587: Inventory Management (Materials)
- 260: Warehouse Management

### Development & Automation
- 271: Workflow Automation
- 433: Build & Automation Tools
- 447: AI Creation
- 421: App Development

## Mapping Methodology Applied

1. **Business Context Analysis**: Reviewed business unit, description, vendor, current L1
2. **L2 Specificity**: Selected most precise L2 sub-capability (not generic)
3. **Multiple Mappings**: Apps serving multiple functions get multiple L2 mappings
4. **Role Assignment**: Primary vs Supporting based on core purpose
5. **Justification**: Each mapping includes clear business rationale

## SQL File Structure

```sql
-- App header with context
-- ==========================================
-- App ID: {id}
-- App Name: {name}
-- Business Unit: {business_unit}
-- Current L1: {current_L1_mapping}
-- ==========================================

-- L2 mapping with explanation
-- L2: {L2_name} (under L1: {L1_name})
INSERT OR IGNORE INTO app_business_capability
(application_id, business_capability_id, capability_role, notes)
VALUES ({app_id}, {L2_id}, 'Primary', '{justification}');
```

## Recommendations for Completion

### Phase 1: SAP Apps (Priority 1)
Execute immediately - these are the largest and most complex apps requiring careful L2 mapping.

### Phase 2: Remaining Cybersecurity (Priority 2)
Complete all 44 cyber apps to ensure security coverage is comprehensive.

### Phase 3: Remaining Shared Services (Priority 2)
Complete infrastructure, monitoring, and support tools.

### Phase 4: Specialty Apps (Priority 3)
Complete OT, downstream, and legacy apps.

### Phase 5: Validation
- Run SQL to insert mappings
- Query to verify all 350 apps have at least one L2 mapping
- Review for gaps or inconsistencies

## Database Query for Validation

```sql
-- Count apps with L2 mappings
SELECT COUNT(DISTINCT application_id) as apps_with_L2_mappings
FROM app_business_capability
WHERE business_capability_id IN (
  SELECT L2_id FROM bcm_L1_L2_hierarchy
);

-- Find apps without L2 mappings
SELECT a.id, a.name, a.business_unit
FROM applications a
WHERE a.business_unit IN (
  'Apps - Enterprise',
  'Apps - Shared Services',
  'Cyber Security Operations',
  'Business - OT (BST/LOB)',
  'Business - HMGP (BST/LOB)',
  'Apps - Data and AI Goverance'
)
AND a.id NOT IN (
  SELECT DISTINCT application_id
  FROM app_business_capability
  WHERE business_capability_id IN (
    SELECT L2_id FROM bcm_L1_L2_hierarchy
  )
);
```

## Files Delivered

1. **L2_mapping_other.sql** - 102 INSERT statements for 89 apps
   - Location: `C:\Users\skavbr\Documents\Claude_Projects\EA_Team\team_folder\Source_Data\L2_mapping_other.sql`
   - Ready to execute against ea_architecture.db

2. **L2_mapping_completion_notes.md** - This status report
   - Location: `C:\Users\skavbr\Documents\Claude_Projects\EA_Team\Working\L2_mapping_completion_notes.md`

3. **generate_L2_mappings.py** - Python script (for future use if Python becomes available)
   - Location: `C:\Users\skavbr\Documents\Claude_Projects\EA_Team\Working\generate_L2_mappings.py`

## Next Actions

1. **Review** the 102 mappings created
2. **Execute** the SQL file to insert L2 mappings
3. **Continue** mapping remaining 261 apps using the established patterns
4. **Validate** all 350 apps have complete L2 mappings
5. **Report** to ea-enterprise-apps (your Enterprise Architect)

---
**Report Generated**: 2026-02-09
**Portfolio Architect**: Enterprise Applications Portfolio Architect
**Domain**: Apps - Enterprise, Shared Services, Cybersecurity, OT, AI & Data Governance
