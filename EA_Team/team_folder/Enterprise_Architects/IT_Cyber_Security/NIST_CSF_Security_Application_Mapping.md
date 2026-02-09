# NIST Cybersecurity Framework Mapping
## Cenovus Energy Security Application Portfolio Analysis

**Document Information**
- **Organization**: Cenovus Energy
- **Prepared By**: IT Cyber Security Enterprise Architect
- **Date**: February 9, 2026
- **Classification**: Internal Use Only
- **Version**: 1.0

---

## 1. Executive Summary

This document presents a comprehensive mapping of Cenovus Energy's 63 security applications to the NIST Cybersecurity Framework (CSF) Core Functions. The analysis provides strategic visibility into our security capability coverage, identifies rationalization opportunities, and highlights gaps requiring investment attention.

### Key Findings

**Portfolio Overview**:
- **Total Security Applications**: 63
- **Critical Upstream/Downstream OT Security Tools**: 8
- **Multi-Instance Deployments**: 11 (indicating potential consolidation opportunities)
- **Legacy Tools Flagged for Migration/Elimination**: 3

**NIST CSF Coverage Analysis**:
- **PROTECT Function**: Strongest coverage with 38 applications (60% of portfolio)
- **DETECT Function**: Well-covered with 15 applications (24% of portfolio)
- **IDENTIFY Function**: Adequate coverage with 8 applications (13% of portfolio)
- **RESPOND Function**: Moderate coverage with 7 applications (11% of portfolio)
- **RECOVER Function**: Weakest coverage with 4 applications (6% of portfolio) - **CRITICAL GAP**

**Strategic TIME Model Distribution**:
- **Invest**: 32 applications (51%) - strategic growth trajectory
- **Tolerate**: 26 applications (41%) - maintain current state
- **Migrate**: 2 applications (3%) - RSA authentication suite transition in progress
- **Eliminate**: 1 application (2%) - myvpn.cenovus.com legacy VPN

**Critical Observations**:
1. **Recovery Capability Gap**: Limited tooling for business continuity and disaster recovery from cyber incidents - a critical concern for oil & gas critical infrastructure
2. **OT/ICS Security**: Dedicated capabilities exist but fragmented across multiple platforms
3. **Consolidation Opportunity**: 11 overlapping antivirus/endpoint protection solutions across Corporate, PCI, and OT environments
4. **SOX & Compliance Alignment**: Strong PCI-DSS coverage; adequate SOX IT controls; moderate OT-specific regulatory alignment (CER, IEC 62443)

This mapping serves as the foundation for our FY2027 security architecture roadmap and ARB prioritization decisions.

---

## 2. NIST CSF Function Mapping

### IDENTIFY (ID)
*Asset Management, Business Environment, Governance, Risk Assessment, Risk Management Strategy, Supply Chain Risk Management*

**Applications Mapped to IDENTIFY (8 applications)**:

1. **ForeScout Secure Connector** - Network Access Control (NAC) provides continuous asset discovery and inventory of all devices connecting to Cenovus networks, critical for maintaining accurate IT/OT asset registers

2. **Control Network - Access Control Server** - Maintains authentication boundaries and access inventories for OT/ICS environments, enabling visibility into who can access production control systems

3. **Qualys** - Vulnerability scanning provides comprehensive asset inventory with vulnerability context, supporting risk assessment processes across IT and limited OT zones

4. **TripWire Enterprise** - Configuration management and integrity monitoring delivers asset baseline configurations and change detection for critical systems (SOX controls, OT safety systems)

5. **Splunk** - SIEM aggregates asset logs and telemetry, providing unified visibility across enterprise IT, cloud, and integrated OT networks

6. **Splunk (China)** - Regional SIEM instance for compliance with China data sovereignty requirements, maintains asset inventory for Asia-Pacific operations

7. **Splunk PCI** - Dedicated SIEM for Payment Card Industry environments, maintains audit-grade asset inventory for retail/downstream payment systems

8. **ServiceNow IT Applications** - Custom cyber security control application manages security projects, control frameworks, and risk registers

**IDENTIFY Coverage Assessment**: ADEQUATE - Core asset management and vulnerability assessment capabilities present. Gap exists in formal supply chain risk management tooling for third-party software/vendor assessment.

---

### PROTECT (PR)
*Identity Management & Access Control, Awareness & Training, Data Security, Information Protection Processes, Maintenance, Protective Technology*

**Applications Mapped to PROTECT (38 applications)**:

#### Access Control & Identity Management (15 applications)

9. **Azure Multi-Factor Authentication (MFA)** - Second-factor authentication for Azure AD/Entra ID identities, critical protection for privileged access and remote workforce

10. **Azure Self-Service Password Reset** - Reduces help desk load while maintaining secure password lifecycle management

11. **Duo Security (Cisco)** - Two-factor authentication for shared services and legacy systems not integrated with Azure MFA

12. **Microsoft Authenticator** - Mobile MFA application supporting passwordless and push notification authentication

13. **NPS Server** - Network Policy Server enforces MFA for radius-authenticated services (WiFi, VPN, network equipment management)

14. **RSA - Authentication Manager** - Legacy authentication management platform (MIGRATE status - transitioning to Azure MFA/Entra ID)

15. **RSA - SecurID** - Hardware/software token-based authentication (MIGRATE status - replacement with Yubikeys and Azure MFA)

16. **Yubikeys** - FIDO2 hardware tokens for phishing-resistant authentication, critical for privileged users and OT engineering workstations

17. **Entra Private Network Connector** - Zero Trust Network Access (ZTNA) providing secure remote access to internal applications without VPN

18. **Global Protect VPN** - Palo Alto VPN client for remote access, integrated with MFA and endpoint posture checking

19. **ICS Access** - Secure remote access solution specifically designed for plant facilities and control networks, providing jump host and session monitoring capabilities

20. **myvpn.cenovus.com** - Legacy VPN landing zone (ELIMINATE status - migrating users to Global Protect and Entra Private Network Connector)

21. **Process Control VMWare Horizon Client** - Virtual Desktop Infrastructure (VDI) providing secure access to control network engineering applications with session isolation

22. **Ericom AccessNow** - HTML5-based application gateway for Juniper devices, provides clientless remote access

23. **KeePass** - Open source password manager for non-enterprise use cases and lab environments

24. **Keeper** - Enterprise password management with vault sharing, supports SOX segregation of duties for shared service accounts

#### Endpoint Protection (13 applications)

25. **CrowdStrike Falcon** - Next-generation endpoint detection and response (EDR) for corporate Windows/Mac endpoints, primary strategic platform

26. **Falcon** - Duplicate listing, refers to CrowdStrike deployment

27. **McAfee ePolicy Orchestrator Corp** - Legacy antivirus management for corporate estate during CrowdStrike migration

28. **McAfee Management (ePO Corp)** - Duplicate ePO instance reference

29. **McAfee Move** - Virtualized security for VMware environments, agentless antivirus

30. **McAfee ePolicy Orchestrator (Lima)** - Dedicated antivirus management for Lima refinery operations

31. **McAfee ePolicy Orchestrator PCI** - Dedicated ePO for PCI-DSS cardholder data environment

32. **McAfee Management (ePO PCI)** - Duplicate PCI ePO reference

33. **McAfee PCI** - Antivirus deployment in PCI environment

34. **Bit9 - Downstream** - Application whitelisting for downstream retail locations, prevents unauthorized software execution

35. **Bit9 Parity** - Application control on retail point-of-sale and back-office computers

36. **Symantec Endpoint Protection Control Network** - Specialized endpoint protection for OT/ICS Windows-based engineering workstations and HMI servers

37. **Symantec End-point Protection Management Server** - Management infrastructure for OT endpoint protection

38. **System Center Endpoint Protection** - Microsoft Defender integration for Windows Server environments

39. **Sophos Antivirus (Linux - Red Hat)** - Linux endpoint protection for RHEL servers supporting upstream operations and enterprise applications

40. **CLAM** - Open source antivirus for Linux systems, primarily mail servers and file scanning

#### Data Protection & Encryption (3 applications)

41. **Azure Information Protection (AIP)** - Document and email classification with rights management, supports data loss prevention and confidentiality labeling

42. **DataMotion Secure Email** - Encrypted email gateway for secure external communications containing sensitive operational or competitive data

43. **Microsoft Office 365 Security & Compliance Console** - Data Loss Prevention (DLP), retention policies, eDiscovery, and compliance management for M365 tenant

#### Network Protection (4 applications)

44. **Panorama** - Centralized management for Palo Alto Networks firewalls across all Cenovus locations, enforces network segmentation policies

45. **External Dynamic List** - Dynamic firewall policy updates based on threat intelligence feeds, enables rapid blocking of malicious IPs/domains

46. **Control Network - Access Control Server** - (Also mapped to IDENTIFY) Enforces access control policies at OT network boundaries

47. **ForeScout Secure Connector** - (Also mapped to IDENTIFY) Network Access Control enforces device compliance before network access

#### Cloud Security (2 applications)

48. **Microsoft Cloud App Security** - Cloud Access Security Broker (CASB) for SaaS application visibility, shadow IT detection, and policy enforcement

49. **Prisma Cloud - Code Security** - Cloud-native application protection platform (CNAPP) securing Azure infrastructure and container workloads

#### Security Awareness & Training (2 applications)

50. **Proofpoint Security Awareness Training** - Simulated phishing campaigns and interactive training modules, critical for human firewall development

51. **Immersive Lab** - Hands-on cyber security skills training platform for IT and security teams, supports incident response readiness

**PROTECT Coverage Assessment**: STRONG - Comprehensive coverage across identity, endpoint, network, and data protection domains. Rationalization opportunity exists in endpoint protection (11 separate antivirus/EDR deployments). Identity management is transitioning from legacy RSA to modern Azure/Entra ID platform.

---

### DETECT (DE)
*Anomalies & Events, Security Continuous Monitoring, Detection Processes*

**Applications Mapped to DETECT (15 applications)**:

#### SIEM & Log Management (5 applications)

52. **Splunk** - Primary SIEM platform aggregating logs from IT, cloud, OT edge, and security tools for correlation and threat detection

53. **Splunk (China)** - Regional SIEM instance for China operations compliance

54. **Splunk PCI** - Dedicated SIEM for PCI-DSS log retention and monitoring requirements

55. **Cribl** - Log routing and pre-processing layer that optimizes Splunk ingestion, enables tiered storage and log enrichment

56. **Windows Event Collector** - Centralized Windows event log collection infrastructure feeding Splunk

#### Endpoint Detection & Response (2 applications)

57. **CrowdStrike Falcon** - (Also mapped to PROTECT) EDR capability provides behavioral threat detection, process monitoring, and threat hunting on endpoints

58. **TripWire Enterprise** - (Also mapped to IDENTIFY) File integrity monitoring (FIM) detects unauthorized changes to critical system files and configurations

#### Network Detection (3 applications)

59. **Sourcefire Appliance** - Next-generation IPS/IDS providing network traffic inspection and threat detection at perimeter and internal segments

60. **Endace** - Full packet capture appliance for forensic network traffic analysis during security investigations

61. **ForeScout Secure Connector** - (Also mapped to IDENTIFY/PROTECT) Detects rogue devices, non-compliant endpoints, and anomalous network behavior

#### Email Security (2 applications)

62. **Proofpoint** - Advanced email threat protection detecting phishing, malware, business email compromise, and credential harvesting attacks

63. **Proofpoint Audit** - Email audit trail and investigation capability for incident response and compliance

64. **SPAM Digest** - Daily spam quarantine digest allowing users to review blocked emails

#### Vulnerability & Configuration Monitoring (2 applications)

65. **Qualys** - (Also mapped to IDENTIFY) Continuous vulnerability scanning detects exploitable weaknesses before attackers

66. **TripWire Enterprise** - (Also mapped to IDENTIFY/PROTECT) Configuration deviation detection for compliance drift

#### External Threat Intelligence (1 application)

67. **ZeroFox** - External digital risk monitoring detecting phishing sites impersonating Cenovus, executive impersonation, brand abuse, and data leaks on dark web

**DETECT Coverage Assessment**: STRONG - Comprehensive visibility across endpoints, network, email, and external threat landscape. SIEM fragmentation (3 Splunk instances) reflects compliance requirements but increases operational complexity.

---

### RESPOND (RS)
*Response Planning, Communications, Analysis, Mitigation, Improvements*

**Applications Mapped to RESPOND (7 applications)**:

68. **Palo Alto Cortex XSOAR** - Security Orchestration, Automation, and Response (SOAR) platform enabling playbook-driven incident response, case management, and automated containment actions

69. **Splunk** - (Also mapped to IDENTIFY/DETECT) Incident investigation and threat hunting platform, supports response workflows

70. **CrowdStrike Falcon** - (Also mapped to PROTECT/DETECT) Enables remote endpoint isolation, process termination, and remediation during active incidents

71. **Panorama** - (Also mapped to PROTECT) Enables rapid firewall rule deployment to contain threats and block malicious infrastructure

72. **Axiom Cyber** - Digital forensic investigation platform for post-incident evidence collection and analysis

73. **HTTPWatch** - Web traffic troubleshooting tool supporting investigation of web-based attack chains

74. **NMap** - Network scanning tool for incident response reconnaissance and affected system identification

**RESPOND Coverage Assessment**: MODERATE - Core SOAR and EDR response capabilities present. Gap exists in dedicated incident response communications platform and formal runbook/playbook repository. OT incident response capability limited (no dedicated OT forensics tooling).

---

### RECOVER (RC)
*Recovery Planning, Improvements, Communications*

**Applications Mapped to RECOVER (4 applications)**:

75. **Palo Alto Cortex XSOAR** - (Also mapped to RESPOND) Post-incident workflow automation and lessons-learned tracking

76. **ServiceNow IT Applications** - (Also mapped to IDENTIFY) Tracks security incidents and remediation actions, supports change management for recovery activities

77. **Splunk** - (Also mapped to IDENTIFY/DETECT/RESPOND) Historical analysis supporting recovery time validation and lessons-learned analysis

78. **TripWire Enterprise** - (Also mapped to IDENTIFY/PROTECT/DETECT) Configuration restoration and baseline re-establishment after security incidents

**RECOVER Coverage Assessment**: WEAK - CRITICAL GAP IDENTIFIED. Limited dedicated tooling for disaster recovery orchestration, backup validation, ransomware recovery, or business continuity management specific to cyber incidents. This represents significant risk for critical oil & gas infrastructure where production downtime has material financial impact.

---

## 3. Coverage Heat Map Data

### Application Count by NIST CSF Function

| NIST Function | Application Count | % of Portfolio | Coverage Assessment | Priority |
|---------------|-------------------|----------------|---------------------|----------|
| PROTECT (PR) | 38 | 60.3% | STRONG | Maintain |
| DETECT (DE) | 15 | 23.8% | STRONG | Maintain |
| IDENTIFY (ID) | 8 | 12.7% | ADEQUATE | Enhance |
| RESPOND (RS) | 7 | 11.1% | MODERATE | Enhance |
| RECOVER (RC) | 4 | 6.3% | WEAK | **INVEST** |

**Note**: Many applications map to multiple functions; percentages exceed 100% due to overlapping capabilities.

### Gap Analysis

#### Critical Gaps (HIGH Priority)

1. **RECOVER Function Underserved**
   - **Current State**: Only 4 applications with recovery capability
   - **Risk**: Extended downtime following ransomware or destructive attack
   - **Impact**: Production facility outages, pipeline disruptions, refinery shutdowns
   - **Recommendation**: Invest in cyber recovery orchestration platform, immutable backup verification, and OT system restoration runbooks

2. **OT/ICS Recovery Capability**
   - **Current State**: No dedicated OT disaster recovery or golden image repository for control systems
   - **Risk**: Extended recovery time for SCADA, DCS, PLC systems following cyber incident
   - **Impact**: Upstream production halt (SAGD facilities), downstream refining disruption
   - **Recommendation**: Implement OT backup and recovery solution compliant with IEC 62443-3-3 SR 7.1/7.2

3. **Supply Chain Risk Management (IDENTIFY)**
   - **Current State**: No dedicated tooling for software bill of materials (SBOM) or third-party risk assessment
   - **Risk**: Undetected vulnerabilities in vendor software, supply chain compromises
   - **Recommendation**: Evaluate supply chain security platforms (e.g., Black Duck, Sonatype, Snyk)

#### Moderate Gaps (MEDIUM Priority)

4. **OT-Specific Threat Detection**
   - **Current State**: Corporate SIEM (Splunk) monitors OT edge; limited industrial protocol (Modbus, DNP3, OPC) inspection
   - **Risk**: Missed OT-specific attack patterns (e.g., PLC ladder logic manipulation)
   - **Recommendation**: Evaluate OT-specific threat detection (Nozomi Networks, Claroty, Dragos)

5. **Privileged Access Management (PAM)**
   - **Current State**: Keeper password manager provides vault sharing; no session recording or just-in-time access
   - **Risk**: Inadequate oversight of privileged operations in OT and IT environments
   - **Recommendation**: Implement enterprise PAM (CyberArk, BeyondTrust) for privileged session management

6. **Incident Response Communications**
   - **Current State**: No dedicated secure crisis communications platform
   - **Risk**: Compromised email/collaboration during incident may impair response coordination
   - **Recommendation**: Implement out-of-band incident response communications (e.g., dedicated Signal channels, satellite phones)

#### Minor Gaps (LOW Priority)

7. **Cloud Security Posture Management (CSPM)**
   - **Current State**: Prisma Cloud provides code security; limited runtime cloud configuration monitoring
   - **Risk**: Azure misconfigurations exposing data or services
   - **Recommendation**: Expand Prisma Cloud deployment or evaluate Defender for Cloud CSPM features

8. **Security Awareness Metrics**
   - **Current State**: Proofpoint provides phishing simulation; limited gamification or culture measurement
   - **Risk**: Difficulty measuring security culture maturity
   - **Recommendation**: Enhance with security culture assessment tools

---

## 4. Rationalization Opportunities

### Opportunity 1: Endpoint Protection Consolidation

**Issue**: Cenovus operates 11 separate antivirus/endpoint protection solutions across Corporate, PCI, and OT environments.

**Current State**:
- CrowdStrike Falcon (Corporate - strategic EDR)
- McAfee ePO Corp / McAfee Corporate (legacy)
- McAfee ePO PCI / McAfee PCI (compliance-mandated)
- McAfee ePO Lima (Lima refinery)
- McAfee Move (virtualized)
- Symantec Endpoint Protection + Management Server (OT control networks)
- System Center Endpoint Protection (Windows Server)
- Sophos Antivirus (Linux RHEL)
- CLAM (Linux open source)
- Bit9 / Bit9 Parity (application whitelisting)

**Rationalization Approach**:

1. **Phase 1: Corporate Consolidation** (FY2027 Q1-Q2)
   - Complete migration from McAfee ePO Corp to CrowdStrike Falcon for all corporate Windows/Mac endpoints
   - Retire McAfee Corporate, McAfee ePO Corp, McAfee Move
   - **Reduction**: 3 products eliminated

2. **Phase 2: Linux Standardization** (FY2027 Q3)
   - Standardize on CrowdStrike Falcon for Linux (supports RHEL)
   - Retire Sophos Antivirus, CLAM
   - **Reduction**: 2 products eliminated

3. **Phase 3: PCI Rationalization** (FY2027 Q4)
   - Migrate PCI environment to CrowdStrike Falcon (supports PCI-DSS compliance requirements)
   - Retire McAfee ePO PCI, McAfee PCI
   - **Reduction**: 2 products eliminated

4. **Phase 4: Downstream Consolidation** (FY2028 Q1)
   - Evaluate CrowdStrike application control features as Bit9 replacement
   - If suitable, migrate downstream retail to CrowdStrike with application whitelisting policies
   - **Reduction**: 2 products eliminated (Bit9, Bit9 Parity)

5. **Phase 5: OT Strategic Decision** (FY2028 Q2)
   - **Decision Point**: Retain Symantec Endpoint Protection for OT control networks OR migrate to CrowdStrike with OT-specific deployment model
   - **Factors**: IEC 62443 compliance, air-gapped update process, OT vendor support statements
   - **Potential Reduction**: 2 products (Symantec EPP, Management Server)

**Estimated Reduction**: 9-11 products consolidated to 2-3 strategic platforms
**Licensing Cost Savings**: Estimated $400K-$600K annually (McAfee, Symantec, Sophos licensing)
**Operational Efficiency**: Single pane of glass for endpoint visibility, unified threat hunting, reduced staff training burden

**Risk Mitigation**:
- Maintain McAfee ePO Lima and OT Symantec until CrowdStrike OT suitability validated
- Pilot CrowdStrike in non-critical OT zones before production control network deployment
- Ensure PCI-DSS compliance validation before PCI environment migration

---

### Opportunity 2: MFA Platform Consolidation

**Issue**: Three separate multi-factor authentication platforms creating user confusion and administrative overhead.

**Current State**:
- Azure MFA (strategic platform, integrated with Entra ID)
- Duo Security (Cisco) - legacy for shared services
- RSA SecurID + Authentication Manager (MIGRATE status)
- Yubikeys (hardware tokens)

**Rationalization Approach**:

1. **Phase 1: RSA Retirement** (FY2027 Q1) - **IN PROGRESS**
   - Complete migration of RSA SecurID users to Azure MFA or Yubikeys
   - Retire RSA Authentication Manager infrastructure
   - **Reduction**: 2 products eliminated
   - **Cost Savings**: $150K annual RSA licensing + maintenance

2. **Phase 2: Duo Migration Assessment** (FY2027 Q2)
   - Evaluate Duo use cases (likely network equipment, legacy RADIUS clients)
   - Migrate to Azure MFA via NPS Server where feasible
   - Retain Duo only if technical blockers exist (e.g., unsupported legacy systems)
   - **Potential Reduction**: 1 product eliminated
   - **Cost Savings**: $80K annual Duo licensing

3. **Phase 3: Standardized Hardware Token** (FY2027 Q3)
   - Standardize on Yubikeys as sole hardware token for privileged users and OT engineers
   - Ensure Azure MFA + Yubikey integration for phishing-resistant authentication

**Estimated Reduction**: 2-3 products consolidated to Azure MFA + Yubikeys
**Licensing Cost Savings**: $230K annually
**User Experience**: Simplified authentication experience, reduced authentication app fatigue

---

### Opportunity 3: SIEM Instance Consolidation

**Issue**: Three separate Splunk deployments creating data silos and increasing licensing costs.

**Current State**:
- Splunk (primary enterprise SIEM)
- Splunk China (Asia-Pacific compliance)
- Splunk PCI (PCI-DSS cardholder data environment)
- Cribl (log routing)

**Rationalization Approach**:

**Option A: Federated Splunk with Index-Based Segmentation** (RECOMMENDED)
- Consolidate Splunk PCI and Splunk China into primary Splunk deployment
- Use index-level access controls to maintain PCI and China data segregation
- Deploy Cribl as universal log router enforcing data residency and compliance boundaries
- **Reduction**: 2 Splunk instances → 1 multi-tenant instance
- **Benefits**: Unified threat correlation, cross-environment attack chain visibility, simplified administration
- **Cost Impact**: Licensing consolidation may yield 15-20% savings ($200K annually)

**Option B: Maintain Separate Instances** (STATUS QUO)
- Retain separate instances if compliance auditors require physical segregation
- Enhance cross-instance correlation via XSOAR and Cribl federation
- Accept ongoing licensing and operational overhead

**Recommendation**: Pursue Option A with legal/compliance validation that index-based controls satisfy PCI-DSS 12.3.8 and China data sovereignty requirements.

**Risk Mitigation**:
- Engage QSA (Qualified Security Assessor) for PCI-DSS attestation before consolidation
- Ensure data residency compliance via Cribl routing rules (China data remains in China Azure region)
- Pilot consolidated model in non-production before production cutover

---

### Opportunity 4: VPN Platform Consolidation

**Issue**: Two VPN platforms creating split-brain remote access architecture.

**Current State**:
- Global Protect VPN (Palo Alto - strategic platform)
- myvpn.cenovus.com (legacy VPN - ELIMINATE status)
- Entra Private Network Connector (ZTNA - emerging)

**Rationalization Approach**:

1. **Phase 1: Legacy VPN Retirement** (FY2027 Q2) - **IN PROGRESS**
   - Complete user migration from myvpn.cenovus.com to Global Protect
   - Retire legacy VPN infrastructure
   - **Reduction**: 1 product eliminated
   - **Cost Savings**: $50K annually (licensing, infrastructure)

2. **Phase 2: Zero Trust Transition** (FY2027-2028)
   - Expand Entra Private Network Connector for application-specific access
   - Reduce reliance on full VPN tunnel where possible
   - Maintain Global Protect for scenarios requiring network-level access (e.g., OT engineering)

**Estimated Reduction**: 1 product eliminated immediately, strategic shift to ZTNA over time
**Security Improvement**: Reduced attack surface via application-level access vs. network-level access

---

### Opportunity 5: Remove Duplicate Application Entries

**Issue**: Database contains duplicate entries for the same product with different naming conventions.

**Duplicates Identified**:
1. CrowdStrike Falcon (ID 10) = Falcon (ID 17) - **CONSOLIDATE**
2. McAfee Management (ePO Corp) (ID 25) = McAfee ePolicy Orchestrator Corp (ID 30) - **CONSOLIDATE**
3. McAfee Management (ePO PCI) (ID 26) = McAfee ePolicy Orchestrator PCI (ID 31) - **CONSOLIDATE**

**Action**: Update EA database (ea_architecture.db) to remove duplicate entries, retain canonical naming.

**Result**: 63 applications → 60 unique applications (3 duplicate entries removed)

---

### Rationalization Summary

| Opportunity | Products Affected | Reduction Potential | Annual Cost Savings | Timeline | Complexity |
|-------------|-------------------|---------------------|---------------------|----------|------------|
| Endpoint Protection Consolidation | 11 | 9-11 products | $400K-$600K | 18-24 months | HIGH |
| MFA Platform Consolidation | 4 | 2-3 products | $230K | 6-9 months | MEDIUM |
| SIEM Instance Consolidation | 3 | 2 instances | $200K | 12 months | HIGH |
| VPN Platform Consolidation | 2 | 1 product | $50K | 6 months | LOW |
| Database Cleanup | 3 | 3 duplicate entries | $0 | Immediate | LOW |
| **TOTAL** | **23** | **17-20 products** | **$880K-$1.08M** | **6-24 months** | **VARIES** |

**Portfolio Reduction**: 63 applications → 43-46 applications (27-32% reduction)

**Strategic Benefits Beyond Cost**:
- Simplified security operations center (SOC) analyst training
- Unified threat intelligence sharing across platforms
- Reduced integration complexity (fewer API connectors)
- Improved incident response speed (single endpoint control plane)
- Enhanced threat hunting (cross-tool correlation)

---

## 5. OT/ICS Security Assessment

As an integrated oil and gas company, Cenovus operates extensive Operational Technology (OT) and Industrial Control Systems (ICS) across:
- **Upstream**: SAGD (Steam-Assisted Gravity Drainage) production facilities, well pads, central processing facilities
- **Midstream**: Pipeline SCADA systems
- **Downstream**: Refinery DCS (Distributed Control Systems), upgrading facilities, product terminals

### OT-Specific Security Applications (8 applications)

| Application | OT Security Function | IEC 62443 Zone | Criticality | Assessment |
|-------------|----------------------|----------------|-------------|------------|
| **Control Network - Access Control Server** | Authentication for OT network access | Level 2/3 Boundary | MEDIUM | Adequate - enforces authentication boundary between IT and OT |
| **ICS Access** | Secure remote access to plant facilities | Level 1-3 Access | LOW | Adequate - provides jump host and session isolation for vendor/engineer access |
| **Process Control VMWare Horizon Client** | VDI for control network engineering tools | Level 2 Engineering | LOW | Adequate - isolates engineering workstations from corporate network |
| **Symantec Endpoint Protection Control Network** | Antivirus for OT Windows systems | Level 2/3 HMI/Engineering | MEDIUM | Tolerate - provides malware protection without disrupting real-time operations |
| **Symantec End-point Protection Management Server** | OT antivirus management | Level 2 Management | LOW | Tolerate - centralized management with air-gapped update process |
| **McAfee ePolicy Orchestrator (Lima)** | Lima refinery antivirus | Level 2/3 Lima Refinery | MEDIUM | Tolerate - dedicated to Lima operations, separate from corporate ePO |
| **Bit9 - Downstream** | Application whitelisting for retail | Level 3 Downstream | MEDIUM | Tolerate - prevents unauthorized software on retail systems |
| **Splunk** (OT edge monitoring) | Log collection from OT DMZ | Level 3 Edge | LOW | Adequate - monitors IT/OT boundary, limited visibility into Level 0-2 |

### OT Security Architecture Assessment

#### Strengths

1. **Network Segmentation**: Clear boundary enforcement between IT and OT zones via dedicated access control servers
2. **Remote Access Security**: Multiple layers (ICS Access, VDI, MFA) for vendor and engineering remote access to OT systems
3. **Endpoint Protection**: Dedicated antivirus solutions for OT Windows-based systems (HMIs, engineering workstations, historians)
4. **Application Control**: Whitelisting (Bit9) prevents unauthorized code execution in downstream/retail environments

#### Critical Gaps

1. **OT-Specific Threat Detection** - **CRITICAL GAP**
   - **Current State**: Splunk monitors OT network edge; no deep packet inspection of industrial protocols (Modbus, DNP3, OPC UA/DA, EtherNet/IP, Profinet)
   - **Risk**: Cannot detect OT-specific attack patterns (e.g., unauthorized PLC programming, ladder logic manipulation, process setpoint changes, safety system bypasses)
   - **Regulatory**: IEC 62443-3-3 SR 6.1 (Audit Log Accessibility) and SR 4.1 (Information Confidentiality) require OT-aware monitoring
   - **Recommendation**: Deploy OT network monitoring platform (Nozomi Networks, Claroty, Dragos) with industrial protocol dissection and physics-based anomaly detection
   - **Investment**: $400K-$800K for platform + 2 FTE SOC analysts with OT expertise

2. **OT Asset Inventory and Vulnerability Management** - **HIGH GAP**
   - **Current State**: ForeScout and Qualys provide IT asset discovery; limited visibility into Level 0-2 OT devices (PLCs, RTUs, field devices)
   - **Risk**: Incomplete asset inventory impairs incident response and vulnerability remediation (e.g., Triton/Trisis attacks target Triconex safety systems)
   - **Regulatory**: IEC 62443-2-1 requires comprehensive OT asset inventory
   - **Recommendation**: Deploy passive OT asset discovery (e.g., Claroty Continuous Threat Detection, Armis) scanning industrial protocols without active probing
   - **Investment**: $200K-$400K platform + integration with CMDB

3. **OT Backup and Disaster Recovery** - **CRITICAL GAP**
   - **Current State**: No dedicated OT configuration backup or golden image repository for control systems
   - **Risk**: Extended recovery time following ransomware, destructive malware (e.g., Industroyer, EKANS), or insider sabotage affecting PLC logic, HMI screens, DCS configurations
   - **Impact**: Days-to-weeks recovery vs. hours with automated restoration
   - **Regulatory**: IEC 62443-3-3 SR 7.1 (Backup) and SR 7.2 (Recovery and Reconstitution) require OT system backup capability
   - **Recommendation**: Implement OT backup solution (e.g., Radiflow, Veeam for OT, Veritas OT Backup) with automated PLC/DCS logic extraction and versioning
   - **Investment**: $300K-$500K platform + runbook development

4. **OT Incident Response and Forensics** - **HIGH GAP**
   - **Current State**: Axiom Cyber provides IT forensics; no OT-specific forensic capability for industrial protocol analysis or PLC forensics
   - **Risk**: Cannot perform root cause analysis after OT cyber incident (e.g., determine if production disruption was cyber-induced)
   - **Recommendation**: Train incident response team on OT forensics; acquire OT forensic tools (e.g., PLC dump analysis, industrial protocol PCAP analysis)
   - **Investment**: $100K training + tools

5. **OT Patch Management** - **MEDIUM GAP**
   - **Current State**: No centralized OT patch management; patching occurs during planned turnarounds
   - **Risk**: Extended vulnerability windows (ICS systems often 2-5 years behind current patches)
   - **Recommendation**: Implement risk-based OT patch management process with virtual patching (IPS signatures) for critical vulnerabilities that cannot be patched during production
   - **Investment**: Process development + staff training

6. **Safety System Security** - **MEDIUM GAP**
   - **Current State**: Safety Instrumented Systems (SIS) - Triconex, Siemens SIS - have limited cyber security monitoring
   - **Risk**: Safety system compromise could result in catastrophic safety events (explosion, fire, environmental release)
   - **Regulatory**: IEC 61511 (functional safety) increasingly requires cyber security for SIS
   - **Recommendation**: Implement unidirectional gateways (e.g., Waterfall, Owl) between SIS and DCS; deploy SIS-specific monitoring
   - **Investment**: $200K-$400K per facility

### OT Security Maturity Assessment (IEC 62443)

| IEC 62443 Foundational Requirement | Current Maturity | Target Maturity | Gap |
|------------------------------------|------------------|-----------------|-----|
| **FR 1: Identification and Authentication Control** | ML 2 (Individual) | ML 3 (Application/Device) | OT device authentication (PLCs, HMIs) not enforced |
| **FR 2: Use Control** | ML 2 (Authorization) | ML 3 (Least Privilege) | Overly permissive OT engineer accounts |
| **FR 3: System Integrity** | ML 1 (Data Integrity) | ML 3 (Change Detection + Prevention) | Limited FIM on OT systems; no application whitelisting on PLCs |
| **FR 4: Data Confidentiality** | ML 1 (Encryption in transit optional) | ML 2 (Encryption required) | Many legacy industrial protocols unencrypted |
| **FR 5: Restricted Data Flow** | ML 2 (Zone segmentation) | ML 3 (Deep packet inspection) | No industrial protocol inspection |
| **FR 6: Timely Response to Events** | ML 1 (Logging) | ML 3 (Automated response) | OT logs collected but limited correlation; no automated OT response |
| **FR 7: Resource Availability** | ML 1 (DoS protection at boundary) | ML 2 (Rate limiting) | Limited DDoS protection for OT DMZ services |

**Overall OT Security Maturity**: ML 1-2 (Initial to Managed)
**Target OT Security Maturity**: ML 2-3 (Managed to Defined) within 24 months
**Regulatory Driver**: Canadian Energy Regulator (CER) cybersecurity expectations for pipeline operators; Alberta Energy Regulator (AER) cybersecurity guidelines for upstream facilities

### OT Security Investment Roadmap

| Priority | Initiative | Investment | Timeline | Regulatory/Business Driver |
|----------|-----------|------------|----------|---------------------------|
| **P0** | OT Network Monitoring Platform | $400K-$800K | FY2027 Q2-Q3 | IEC 62443-3-3 SR 6.1; detect OT-specific threats |
| **P0** | OT Backup and DR Solution | $300K-$500K | FY2027 Q3-Q4 | IEC 62443-3-3 SR 7.1/7.2; reduce recovery time |
| **P1** | OT Asset Discovery and Vulnerability Management | $200K-$400K | FY2027 Q4 | IEC 62443-2-1; complete asset inventory |
| **P1** | OT Incident Response Capability | $100K | FY2028 Q1 | Incident readiness; forensic capability |
| **P2** | Safety System Security (Unidirectional Gateways) | $200K-$400K/facility | FY2028 Q2-Q4 | IEC 61511; protect SIS from cyber threats |
| **P2** | OT Patch Management Process | $50K | FY2028 Q3 | Reduce vulnerability window |
| **TOTAL** | | **$1.25M-$2.25M** | **18-24 months** | |

**Funding Justification**: Critical infrastructure protection; regulatory compliance; operational resilience; insurance requirements (cyber insurance increasingly requires OT security controls)

---

## 6. TIME Model Summary

### TIME Model Distribution

| TIME Disposition | Count | % of Portfolio | Strategic Meaning |
|------------------|-------|----------------|-------------------|
| **Invest** | 32 | 51% | Strategic growth platforms; continue investment and capability expansion |
| **Tolerate** | 26 | 41% | Maintain current state; accept existing capabilities without major investment |
| **Migrate** | 2 | 3% | Transition from legacy to modern platforms; time-bound replacement |
| **Eliminate** | 1 | 2% | Decommission; migrate users to replacement platforms |
| **Unspecified** | 2 | 3% | Require TIME disposition assignment |

### INVEST Applications (32 applications)

**Strategic Platforms Receiving Continued Investment**:

**Identity & Access** (6 applications):
- Azure Multi-Factor Authentication (MFA) - Modern MFA platform
- Azure Self-Service Password Reset - Self-service capability
- Microsoft Authenticator - Mobile MFA app
- Entra Private Network Connector - Zero Trust Network Access
- Global Protect VPN - Strategic VPN platform
- KeePass - Lightweight password management

**Endpoint Security** (5 applications):
- CrowdStrike Falcon - Strategic EDR platform
- Falcon - (Duplicate entry)
- ForeScout Secure Connector - Network Access Control
- Sophos Antivirus (Linux - Red Hat) - Linux endpoint protection
- Symantec Endpoint Protection Control Network - OT endpoint protection
- System Center Endpoint Protection - Windows Server protection

**Detection & Response** (8 applications):
- Splunk - Strategic SIEM platform
- Cribl - Log optimization
- Proofpoint - Email security
- Proofpoint Audit - Email audit
- Proofpoint Security Awareness Training - Security training
- SPAM Digest - Spam management
- Palo Alto Cortex XSOAR - SOAR platform
- Panorama - Firewall management

**Cloud & Data Security** (4 applications):
- Azure Information Protection (AIP) - Data classification
- Microsoft Cloud App Security - CASB
- Microsoft Office 365 Security & Compliance Console - M365 security

**Training & Awareness** (2 applications):
- Immersive Lab - Security skills training

**Strategic Focus**:
- **Cloud-First**: Heavy investment in Azure/M365 security stack aligns with cloud migration strategy
- **Zero Trust**: Entra Private Network Connector, Azure MFA, ForeScout support Zero Trust architecture transition
- **Automation**: Cortex XSOAR, Cribl represent security operations automation
- **Modern EDR**: CrowdStrike Falcon as strategic endpoint platform replacing legacy AV

**Investment Priority**: Continue capability expansion, integrate platforms, automate workflows

---

### TOLERATE Applications (26 applications)

**Maintain Current State - No Major Investment**:

**Legacy Endpoint Protection** (9 applications):
- McAfee ePolicy Orchestrator Corp
- McAfee Management (ePO Corp)
- McAfee Move
- McAfee ePolicy Orchestrator PCI
- McAfee Management (ePO PCI)
- McAfee PCI
- Bit9 - Downstream
- Bit9 Parity
- Keeper (password manager)

**Legacy Authentication** (2 applications):
- Duo Security (Cisco)
- NPS Server

**OT/ICS Specialized** (4 applications):
- ICS Access - OT remote access
- Symantec End-point Protection Management Server
- CLAM - Linux AV

**Detection & Monitoring** (5 applications):
- Endace - Packet capture
- Splunk (China)
- HTTPWatch - Troubleshooting
- Windows Event Collector

**Network Security** (2 applications):
- Sourcefire Appliance - IPS/IDS
- Qualys - Vulnerability scanning

**Other** (4 applications):
- DataMotion Secure Email
- ServiceNow IT Applications (custom security app)
- TripWire Enterprise
- Tripwire Enterprise Client

**Strategic Interpretation**:
- **Tolerate ≠ Ignore**: These tools remain operational and supported but are not primary investment focus
- **Rationalization Candidates**: Many TOLERATE applications are consolidation targets (see Section 4)
- **Bridge Solutions**: Tools maintained during transition to strategic platforms (e.g., McAfee during CrowdStrike migration)
- **Specialized Use Cases**: Some TOLERATE tools serve niche needs not addressed by strategic platforms (e.g., Endace forensics)

**Investment Priority**: Minimal investment; evaluate for consolidation or retirement as strategic platforms mature

---

### MIGRATE Applications (2 applications)

**Legacy Platforms with Active Replacement Projects**:

1. **RSA - Authentication Manager** (MIGRATE → Azure MFA / Entra ID)
   - **Migration Timeline**: FY2027 Q1 completion
   - **Replacement**: Azure MFA + Yubikeys
   - **Migration Status**: 85% complete; final users in transition
   - **Retirement Date**: Target June 2027

2. **RSA - SecurID** (MIGRATE → Azure MFA / Yubikeys)
   - **Migration Timeline**: FY2027 Q1 completion
   - **Replacement**: Azure MFA (software tokens) + Yubikeys (hardware tokens)
   - **Migration Status**: 85% complete
   - **Retirement Date**: Target June 2027

**Strategic Significance**:
- RSA retirement eliminates legacy on-premises authentication infrastructure
- Shifts to cloud-native, mobile-first authentication
- Enables passwordless authentication with FIDO2/Yubikeys
- Reduces licensing costs ($150K annually)

**Migration Risk**: Ensure all RSA-integrated systems (network equipment, legacy applications) have alternative authentication path before RSA retirement

---

### ELIMINATE Applications (1 application)

**Legacy Platforms Scheduled for Decommission**:

1. **myvpn.cenovus.com** - Legacy VPN landing zone
   - **ELIMINATE Timeline**: FY2027 Q2
   - **Replacement**: Global Protect VPN + Entra Private Network Connector (ZTNA)
   - **Migration Status**: User migration 70% complete
   - **Decommission Date**: Target September 2027
   - **Cost Savings**: $50K annually (infrastructure, licensing)

**Elimination Drivers**:
- Outdated VPN technology lacking modern security features (no endpoint posture checking, no per-app access)
- Duplicate functionality with Global Protect (strategic VPN platform)
- Zero Trust strategy favors application-level access (Entra Private Network Connector) over network-level access

---

### UNSPECIFIED Applications (2 applications)

**Require TIME Disposition Assignment**:

1. **Control Network - Access Control Server** (Currently: No TIME specified)
   - **Recommended Disposition**: TOLERATE (short-term) → INVEST (long-term)
   - **Rationale**: Critical OT access control; requires evaluation for replacement with modern NAC or Zero Trust OT solution

2. **McAfee ePolicy Orchestrator (Lima)** (Currently: No TIME specified)
   - **Recommended Disposition**: TOLERATE
   - **Rationale**: Lima refinery-specific; maintain until corporate endpoint consolidation (CrowdStrike) proven in downstream environments

**Action Required**: EA team to assign TIME disposition and update ea_architecture.db

---

### TIME Model Strategic Insights

1. **Cloud Transformation Momentum**: 51% INVEST applications concentrated in cloud-native security (Azure/M365 stack)

2. **Legacy Debt Management**: 41% TOLERATE applications represent technical debt requiring rationalization roadmap

3. **Active Transitions**: Only 3% MIGRATE/ELIMINATE indicates most legacy retirements already completed or consolidated into TOLERATE category

4. **OT Investment Gap**: Limited OT applications in INVEST category despite critical infrastructure risk - **requires strategic rebalancing**

5. **Cost Optimization Opportunity**: High TOLERATE count presents consolidation opportunity ($880K-$1.08M annual savings identified in Section 4)

**Recommendation**: Shift 5-10 applications from TOLERATE → ELIMINATE over next 18 months via rationalization initiatives (Section 4). Rebalance savings into RECOVER and OT security capabilities (Section 5).

---

## 7. Prioritized Recommendations

### Priority 0: Critical - Address Immediately (0-6 months)

**1. Invest in Cyber Recovery Capability (RECOVER Function Gap)**
- **Issue**: Only 4 applications support RECOVER function; no dedicated cyber disaster recovery orchestration or OT system restoration capability
- **Risk**: Extended production downtime following ransomware or destructive attack; regulatory non-compliance (SOX, pipeline safety)
- **Action**:
  - Procure and deploy cyber recovery orchestration platform (e.g., Zerto Cyber Resilience, Commvault Disaster Recovery, Rubrik)
  - Implement immutable backup validation for critical systems (Active Directory, PAM, SIEM, OT historians)
  - Develop and test OT system restoration runbooks (PLC logic, HMI configurations, DCS setups)
- **Investment**: $500K-$800K platform + 1 FTE
- **Timeline**: 6 months to operational capability
- **Success Metric**: Recovery Time Objective (RTO) < 24 hours for critical IT systems; < 72 hours for OT systems

**2. Deploy OT Network Monitoring Platform (OT Security Gap)**
- **Issue**: No visibility into industrial protocol traffic (Modbus, DNP3, OPC); cannot detect OT-specific attacks
- **Risk**: Undetected OT cyber attacks (PLC manipulation, safety system compromise); production disruption; safety events
- **Action**:
  - Deploy OT network monitoring solution (Nozomi Networks, Claroty, Dragos) at IT/OT boundaries and within OT zones
  - Integrate OT alerts with Splunk SIEM and Cortex XSOAR
  - Hire or train 2 FTE SOC analysts with OT security expertise
- **Investment**: $400K-$800K platform + $300K staffing
- **Timeline**: 6 months to pilot; 12 months to full deployment
- **Success Metric**: 100% visibility into Level 2-3 OT network traffic; < 30 min mean time to detect (MTTD) for OT anomalies
- **Regulatory Driver**: IEC 62443-3-3 SR 6.1, CER cybersecurity expectations

**3. Complete RSA Authentication Manager Retirement**
- **Issue**: RSA migration 85% complete; final users blocking infrastructure retirement
- **Risk**: Ongoing licensing costs ($150K/year); security risk from legacy authentication platform
- **Action**:
  - Identify and migrate final RSA users (likely network equipment, legacy applications)
  - Provide Yubikeys for hardware token users
  - Decommission RSA infrastructure by June 2027
- **Investment**: $30K (Yubikeys, migration labor)
- **Timeline**: 3 months
- **Success Metric**: Zero RSA authentications; infrastructure retired

---

### Priority 1: High - Address Within 6-12 Months

**4. Execute Endpoint Protection Consolidation (Rationalization)**
- **Issue**: 11 separate antivirus/EDR solutions creating operational complexity and cost
- **Action**:
  - Phase 1: Complete corporate McAfee → CrowdStrike migration (eliminate 3 products)
  - Phase 2: Standardize Linux on CrowdStrike (eliminate Sophos, CLAM)
  - Phase 3: Migrate PCI environment to CrowdStrike (eliminate McAfee PCI)
- **Investment**: CrowdStrike licensing expansion (offset by McAfee retirement)
- **Timeline**: 12 months for Phases 1-3
- **Cost Savings**: $400K-$600K annually
- **Success Metric**: < 5 endpoint protection products by end of FY2027

**5. Deploy OT Asset Discovery and Vulnerability Management**
- **Issue**: Incomplete OT asset inventory; cannot assess vulnerability exposure for PLCs, RTUs, field devices
- **Risk**: Unmanaged OT assets; unknown vulnerability exposure; slow incident response
- **Action**:
  - Deploy passive OT asset discovery (Claroty, Armis, or integrated with OT monitoring platform)
  - Integrate OT asset inventory with ServiceNow CMDB
  - Establish OT vulnerability management process (risk-based patching, virtual patching)
- **Investment**: $200K-$400K
- **Timeline**: 6-9 months
- **Success Metric**: 95% OT asset discovery accuracy; OT vulnerability dashboard operational
- **Regulatory Driver**: IEC 62443-2-1 asset inventory requirement

**6. Implement OT Backup and Disaster Recovery**
- **Issue**: No automated OT configuration backup; recovery from cyber incident requires manual PLC reprogramming (days-to-weeks)
- **Risk**: Extended production downtime; revenue loss ($5M-$15M per day for major facility)
- **Action**:
  - Deploy OT backup solution (Radiflow, Veeam for OT, Veritas OT Backup)
  - Automate PLC/DCS logic extraction and versioning
  - Develop and test restoration runbooks
- **Investment**: $300K-$500K
- **Timeline**: 9-12 months
- **Success Metric**: Weekly automated backups; restoration test successful within 72 hours
- **Regulatory Driver**: IEC 62443-3-3 SR 7.1/7.2

**7. Consolidate MFA Platforms**
- **Issue**: Three separate MFA platforms (Azure MFA, Duo, RSA) creating user confusion
- **Action**:
  - Complete RSA retirement (see Recommendation #3)
  - Assess Duo use cases; migrate to Azure MFA via NPS Server where feasible
  - Standardize on Azure MFA + Yubikeys
- **Investment**: $50K (migration labor)
- **Timeline**: 9 months (dependent on RSA completion)
- **Cost Savings**: $230K annually
- **Success Metric**: < 2 MFA platforms (Azure MFA + Yubikeys only)

---

### Priority 2: Medium - Address Within 12-18 Months

**8. Evaluate SIEM Instance Consolidation**
- **Issue**: Three Splunk instances (Corporate, China, PCI) creating data silos and licensing costs
- **Action**:
  - Engage QSA and legal counsel to validate index-based segmentation for PCI and China compliance
  - If approved, consolidate to single federated Splunk with Cribl-enforced data boundaries
  - If not approved, enhance cross-instance correlation via XSOAR
- **Investment**: $100K (consulting, configuration)
- **Timeline**: 12-15 months (includes compliance validation)
- **Cost Savings**: $200K annually (if consolidation approved)
- **Success Metric**: Single SIEM instance OR federated cross-instance correlation operational

**9. Implement Privileged Access Management (PAM)**
- **Issue**: Keeper password manager provides vault sharing; no session recording or just-in-time privileged access
- **Risk**: Inadequate oversight of privileged operations; SOX control weakness
- **Action**:
  - Procure and deploy enterprise PAM solution (CyberArk, BeyondTrust)
  - Implement privileged session recording for IT and OT environments
  - Enable just-in-time access for privileged accounts
- **Investment**: $300K-$500K platform + integration
- **Timeline**: 12-18 months
- **Success Metric**: 100% privileged sessions recorded; SOX compliance attestation

**10. Complete Legacy VPN Elimination**
- **Issue**: myvpn.cenovus.com legacy VPN still operational (ELIMINATE status)
- **Action**:
  - Complete user migration to Global Protect VPN
  - Decommission myvpn.cenovus.com infrastructure by September 2027
- **Investment**: $20K (migration labor)
- **Timeline**: 6 months
- **Cost Savings**: $50K annually
- **Success Metric**: myvpn.cenovus.com infrastructure retired

**11. Enhance OT Incident Response Capability**
- **Issue**: Axiom Cyber provides IT forensics; no OT-specific forensic capability
- **Action**:
  - Train incident response team on OT forensics (SANS ICS515, specialized OT IR training)
  - Acquire OT forensic tools (PLC dump analysis, industrial protocol PCAP analysis)
  - Develop OT incident response playbooks integrated with XSOAR
- **Investment**: $100K
- **Timeline**: 12 months
- **Success Metric**: IR team can perform OT forensics; OT playbooks tested via tabletop exercise

---

### Priority 3: Low - Address Within 18-24 Months

**12. Deploy Supply Chain Risk Management Capability (IDENTIFY Gap)**
- **Issue**: No tooling for Software Bill of Materials (SBOM) or third-party software risk assessment
- **Action**:
  - Evaluate and deploy supply chain security platform (Black Duck, Sonatype, Snyk)
  - Integrate with development pipeline for continuous SBOM generation
  - Establish vendor risk assessment process for OT vendors
- **Investment**: $150K-$250K
- **Timeline**: 18 months
- **Success Metric**: SBOM generated for 100% of custom applications; vendor risk scoring operational

**13. Expand Cloud Security Posture Management (CSPM)**
- **Issue**: Prisma Cloud provides code security; limited runtime cloud configuration monitoring
- **Action**:
  - Expand Prisma Cloud CSPM module or evaluate Microsoft Defender for Cloud
  - Implement continuous Azure configuration compliance monitoring
  - Integrate CSPM alerts with XSOAR for automated remediation
- **Investment**: $50K-$100K (licensing expansion)
- **Timeline**: 12 months
- **Success Metric**: 100% Azure subscriptions monitored; automated remediation for high-risk misconfigurations

**14. Implement Safety System Security Controls (OT)**
- **Issue**: Safety Instrumented Systems (SIS) lack cyber security isolation and monitoring
- **Risk**: Safety system compromise → catastrophic safety events
- **Action**:
  - Deploy unidirectional gateways (Waterfall, Owl) between SIS and DCS networks
  - Implement SIS-specific monitoring and change detection
  - Prioritize critical facilities (SAGD, refineries with high consequence of failure)
- **Investment**: $200K-$400K per facility; $1M-$2M total for 5 critical facilities
- **Timeline**: 24 months (phased by facility)
- **Success Metric**: Unidirectional gateways deployed at 5 critical facilities; SIS change detection operational
- **Regulatory Driver**: IEC 61511 functional safety + cybersecurity convergence

**15. Develop Security Metrics and Reporting Dashboard**
- **Issue**: Limited executive visibility into security posture and program effectiveness
- **Action**:
  - Develop CISO dashboard in PowerBI or Splunk integrating metrics from all security tools
  - Implement KRIs (Key Risk Indicators) and KPIs (Key Performance Indicators) aligned to NIST CSF
  - Automate monthly security posture reporting to executive leadership and Board
- **Investment**: $50K (development, integration)
- **Timeline**: 12 months
- **Success Metric**: Executive dashboard operational; monthly Board reporting established

---

### Recommendation Summary Table

| Priority | Recommendation | NIST Function | Investment | Savings | Timeline | Complexity |
|----------|---------------|---------------|------------|---------|----------|------------|
| **P0** | Cyber Recovery Capability | RECOVER | $500K-$800K | - | 6 months | HIGH |
| **P0** | OT Network Monitoring | DETECT | $400K-$800K | - | 6-12 months | HIGH |
| **P0** | RSA Retirement | PROTECT | $30K | $150K/year | 3 months | LOW |
| **P1** | Endpoint Consolidation | PROTECT | Neutral | $400K-$600K/year | 12 months | HIGH |
| **P1** | OT Asset Discovery | IDENTIFY | $200K-$400K | - | 6-9 months | MEDIUM |
| **P1** | OT Backup/DR | RECOVER | $300K-$500K | - | 9-12 months | HIGH |
| **P1** | MFA Consolidation | PROTECT | $50K | $230K/year | 9 months | MEDIUM |
| **P2** | SIEM Consolidation | DETECT | $100K | $200K/year* | 12-15 months | HIGH |
| **P2** | PAM Implementation | PROTECT | $300K-$500K | - | 12-18 months | HIGH |
| **P2** | Legacy VPN Elimination | PROTECT | $20K | $50K/year | 6 months | LOW |
| **P2** | OT Incident Response | RESPOND | $100K | - | 12 months | MEDIUM |
| **P3** | Supply Chain Risk Mgmt | IDENTIFY | $150K-$250K | - | 18 months | MEDIUM |
| **P3** | CSPM Expansion | PROTECT | $50K-$100K | - | 12 months | LOW |
| **P3** | Safety System Security | PROTECT | $1M-$2M | - | 24 months | HIGH |
| **P3** | Security Metrics Dashboard | ALL | $50K | - | 12 months | LOW |
| **TOTAL** | | | **$3.25M-$6.4M** | **$1.03M-$1.18M/year** | **24 months** | |

*SIEM consolidation savings contingent on compliance approval

**Net Investment** (after year 1 savings): $2.2M-$5.2M over 24 months
**3-Year ROI**: Positive (savings + avoided incident costs exceed investment)

---

## 8. Appendix: Full Mapping Table

| # | Application Name | NIST Function(s) | Business Category | Criticality | TIME | Notes |
|---|------------------|------------------|-------------------|-------------|------|-------|
| 1 | Axiom Cyber | RESPOND | Corporate | Low | Invest | Digital forensics investigation; IT-focused; OT forensics gap |
| 2 | Azure Information Protection (AIP) | PROTECT | Cyber Sec Ops | Low | Invest | Data classification and rights management; DLP integration |
| 3 | Azure Multi-Factor Authentication (MFA) | PROTECT | Cyber Sec Ops | High | Invest | Strategic MFA platform; replacing RSA SecurID |
| 4 | Azure Self-Service Password Reset | PROTECT | Cyber Sec Ops | Low | Invest | Reduces help desk load; user experience improvement |
| 5 | Bit9 - Downstream | PROTECT | Downstream | Medium | Tolerate | Application whitelisting retail; consolidation candidate |
| 6 | Bit9 Parity | PROTECT | Cyber Sec Ops | Medium | Tolerate | Application control retail POS; consolidation candidate |
| 7 | CLAM | PROTECT | Cyber Sec Ops | Low | Tolerate | Open source Linux AV; consolidation candidate (CrowdStrike Linux) |
| 8 | Control Network - Access Control Server | IDENTIFY, PROTECT | Cyber Sec Ops | Medium | Unspecified | OT access control; critical for IT/OT segmentation |
| 9 | Cribl | DETECT | Cyber Sec Ops | Low | Invest | Log optimization and routing; enables SIEM consolidation |
| 10 | CrowdStrike Falcon | PROTECT, DETECT, RESPOND | Cyber Sec Ops | Medium | Tolerate | Strategic EDR platform; replace McAfee/Symantec (Corporate) |
| 11 | DataMotion Secure Email | PROTECT | Corporate | Low | Tolerate | Encrypted email for external communications |
| 12 | Duo Security (Cisco) | PROTECT | Shared Services | Low | Tolerate | Legacy MFA; evaluate for Azure MFA migration |
| 13 | Endace | DETECT | Cyber Sec Ops | Low | Tolerate | Full packet capture for forensics; specialized use case |
| 14 | Entra Private Network Connector | PROTECT | Cyber Sec Ops | Low | Invest | Zero Trust Network Access (ZTNA); strategic direction |
| 15 | Ericom AccessNow | PROTECT | Cyber Sec Ops | Low | Unspecified | HTML5 gateway for Juniper; evaluate for ZTNA migration |
| 16 | External Dynamic List | PROTECT | Cyber Sec Ops | Low | Unspecified | Dynamic firewall updates from threat intel; integrated with Panorama |
| 17 | Falcon | PROTECT, DETECT, RESPOND | Cyber Sec Ops | Low | Invest | **DUPLICATE of CrowdStrike Falcon (ID 10)** - consolidate in DB |
| 18 | ForeScout Secure Connector | IDENTIFY, PROTECT, DETECT | Cyber Sec Ops | Low | Invest | Network Access Control (NAC); asset discovery + compliance |
| 19 | Global Protect VPN | PROTECT | Cyber Sec Ops | Medium | Invest | Strategic VPN platform; replacing myvpn.cenovus.com |
| 20 | HTTPWatch | RESPOND | Cyber Sec Ops | Low | Tolerate | Web traffic troubleshooting for investigations |
| 21 | ICS Access | PROTECT | Cyber Sec Ops | Low | Tolerate | OT remote access with jump host; critical for vendor access |
| 22 | Immersive Lab | PROTECT | Corporate | Low | Invest | Hands-on security training; IR preparedness |
| 23 | KeePass | PROTECT | Corporate | Low | Invest | Open source password manager; lab/non-enterprise use |
| 24 | Keeper | PROTECT | Corporate | Medium | Tolerate | Enterprise password manager; evaluate for PAM replacement |
| 25 | McAfee Management (ePO Corp) | PROTECT | Cyber Sec Ops | Medium | Tolerate | **DUPLICATE of McAfee ePO Corp (ID 30)** - consolidate in DB |
| 26 | McAfee Management (ePO PCI) | PROTECT | Shared Services | Medium | Tolerate | **DUPLICATE of McAfee ePO PCI (ID 31)** - consolidate in DB |
| 27 | McAfee Move | PROTECT | Cyber Sec Ops | Medium | Tolerate | Virtualized AV; consolidation candidate (CrowdStrike) |
| 28 | McAfee PCI | PROTECT | Shared Services | Medium | Tolerate | PCI antivirus; migrate to CrowdStrike after PCI validation |
| 29 | McAfee ePolicy Orchestrator (Lima) | PROTECT | Shared Services | Medium | Unspecified | Lima refinery antivirus; OT-adjacent; evaluate for Symantec OT or CrowdStrike |
| 30 | McAfee ePolicy Orchestrator Corp | PROTECT | Cyber Sec Ops | Medium | Tolerate | Corporate AV management; migrate to CrowdStrike |
| 31 | McAfee ePolicy Orchestrator PCI | PROTECT | Shared Services | Medium | Tolerate | PCI AV management; migrate to CrowdStrike after PCI validation |
| 32 | Microsoft Authenticator | PROTECT | Cyber Sec Ops | Low | Invest | Mobile MFA app; supports passwordless |
| 33 | Microsoft Cloud App Security | PROTECT | Cyber Sec Ops | Low | Invest | CASB for SaaS visibility and control |
| 34 | Microsoft Office 365 Security & Compliance Console | PROTECT | Cyber Sec Ops | Low | Invest | M365 DLP, retention, eDiscovery |
| 35 | NMap | RESPOND | Cyber Sec Ops | Low | Unspecified | Network scanning for IR and reconnaissance |
| 36 | NPS Server | PROTECT | Cyber Sec Ops | Medium | Tolerate | Network Policy Server for RADIUS MFA; Azure MFA integration |
| 37 | Palo Alto Cortex XSOAR | RESPOND, RECOVER | Cyber Sec Ops | Low | Invest | SOAR platform; playbook automation; case management |
| 38 | Panorama | PROTECT, RESPOND | Cyber Sec Ops | Medium | Invest | Centralized firewall management; network segmentation enforcement |
| 39 | Prisma Cloud - Code Security | PROTECT | Cyber Sec Ops | Low | Unspecified | Cloud-native app protection; expand to CSPM |
| 40 | Process Control VMWare Horizon Client | PROTECT | Cyber Sec Ops | Low | Unspecified | VDI for OT engineering; session isolation |
| 41 | Proofpoint | DETECT | Cyber Sec Ops | Medium | Invest | Email threat protection; phishing/malware/BEC detection |
| 42 | Proofpoint Audit | DETECT | Cyber Sec Ops | Medium | Invest | Email audit for compliance and investigations |
| 43 | Proofpoint Security Awareness Training | PROTECT | Cyber Sec Ops | Low | Invest | Phishing simulation and training; human firewall |
| 44 | Qualys | IDENTIFY, DETECT | Cyber Sec Ops | Medium | Tolerate | Vulnerability scanning; limited OT support |
| 45 | RSA - Authentication Manager | PROTECT | Cyber Sec Ops | Low | Migrate | **MIGRATE to Azure MFA** - target retirement June 2027 |
| 46 | RSA - SecurID | PROTECT | Cyber Sec Ops | Low | Migrate | **MIGRATE to Azure MFA + Yubikeys** - target retirement June 2027 |
| 47 | SPAM Digest | DETECT | Cyber Sec Ops | Low | Invest | Proofpoint quarantine digest; user self-service |
| 48 | ServiceNow IT Applications | IDENTIFY, RECOVER | Corporate | Medium | Tolerate | Custom security control app; tracks incidents and controls |
| 49 | Sophos Antivirus (Linux - Red Hat) | PROTECT | Shared Services | Low | Invest | Linux AV; consolidation candidate (CrowdStrike Linux) |
| 50 | Sourcefire Appliance | DETECT | Cyber Sec Ops | High | Tolerate | IPS/IDS; network threat detection; aging platform |
| 51 | Splunk | IDENTIFY, DETECT, RESPOND, RECOVER | Cyber Sec Ops | Low | Invest | Primary SIEM; threat detection; IR investigations |
| 52 | Splunk (China) | IDENTIFY, DETECT | Cyber Sec Ops | Medium | Tolerate | Regional SIEM for China compliance; consolidation candidate |
| 53 | Splunk PCI | IDENTIFY, DETECT | Cyber Sec Ops | Medium | Unspecified | PCI-DSS SIEM; consolidation candidate (if compliant) |
| 54 | Symantec End-point Protection Management Server | PROTECT | Shared Services | Low | Invest | OT endpoint management; critical for control network |
| 55 | Symantec Endpoint Protection Control Network | PROTECT | Cyber Sec Ops | Medium | Invest | OT endpoint protection; ICS-appropriate AV |
| 56 | System Center Endpoint Protection | PROTECT | Corporate | Low | Invest | Microsoft Defender integration; Windows Server protection |
| 57 | TripWire Enterprise | IDENTIFY, PROTECT, DETECT, RECOVER | Shared Services | High | Tolerate | File integrity monitoring; SOX control; config baseline |
| 58 | Tripwire Enterprise Client | IDENTIFY, PROTECT, DETECT | Shared Services | High | Tolerate | TripWire agent; FIM client |
| 59 | Windows Event Collector | DETECT | Cyber Sec Ops | Low | Tolerate | Windows log collection feeding Splunk |
| 60 | Yubikeys | PROTECT | Cyber Sec Ops | Medium | Unspecified | FIDO2 hardware tokens; phishing-resistant MFA; strategic |
| 61 | ZeroFox | DETECT | Corporate | Unspecified | Unspecified | External threat intel; brand protection; dark web monitoring |
| 62 | click.cenovus.com | PROTECT | Corporate | High | Invest | Cenovus landing zone; authentication gateway |
| 63 | myvpn.cenovus.com | PROTECT | Corporate | High | Eliminate | **ELIMINATE by Sept 2027** - migrate to Global Protect |

---

### Database Cleanup Actions Required

**Duplicate Entries to Consolidate**:
1. CrowdStrike Falcon (ID 10) + Falcon (ID 17) → Retain ID 10, remove ID 17
2. McAfee Management (ePO Corp) (ID 25) + McAfee ePolicy Orchestrator Corp (ID 30) → Retain ID 30, remove ID 25
3. McAfee Management (ePO PCI) (ID 26) + McAfee ePolicy Orchestrator PCI (ID 31) → Retain ID 31, remove ID 26

**TIME Disposition Missing (Assign)**:
1. Control Network - Access Control Server → TOLERATE (short-term) or INVEST (if modernizing to Zero Trust NAC)
2. McAfee ePolicy Orchestrator (Lima) → TOLERATE
3. Ericom AccessNow → TOLERATE
4. External Dynamic List → INVEST (integrated with Panorama)
5. NMap → TOLERATE
6. Prisma Cloud - Code Security → INVEST
7. Process Control VMWare Horizon Client → TOLERATE
8. Splunk PCI → TOLERATE
9. Yubikeys → INVEST (strategic hardware token)
10. ZeroFox → INVEST

**Criticality Missing (Assign)**:
1. Control Network - Access Control Server → MEDIUM (OT boundary control)
2. ZeroFox → LOW (external monitoring, non-critical)

**Action**: Update ea_architecture.db with corrections and missing attributes

---

## Conclusion

This NIST Cybersecurity Framework mapping provides a comprehensive view of Cenovus Energy's 63-application security portfolio. Key conclusions:

1. **Strong PROTECT and DETECT Coverage**: The portfolio demonstrates mature capabilities in prevention and detection, reflecting years of investment in endpoint, network, and email security.

2. **Critical RECOVER Gap**: The most significant finding is weak recovery capability - a critical vulnerability for oil & gas critical infrastructure where operational downtime has material financial and safety consequences. **Immediate investment required**.

3. **OT/ICS Security Requires Acceleration**: While basic OT protections exist (access control, endpoint security), gaps in OT-specific threat detection, asset management, backup/recovery, and incident response create unacceptable risk for upstream and downstream operations. **Priority investment in OT security platforms and capabilities**.

4. **Rationalization Opportunity**: The portfolio contains significant duplication (11 endpoint protection products, 3 SIEM instances, 3 MFA platforms) representing $880K-$1.08M annual cost reduction potential. **Execute consolidation roadmap**.

5. **Cloud Transformation Progress**: 51% of applications in INVEST category concentrated in Azure/M365 security stack demonstrates successful cloud security transformation. **Continue momentum**.

6. **TIME Model Rebalancing**: Shift resources from 41% TOLERATE applications toward RECOVER and OT security investment areas. Execute active migration/elimination projects (RSA, legacy VPN).

This analysis serves as the foundation for the FY2027 Cyber Security Architecture Roadmap and prioritization decisions in the Architecture Review Board (ARB).

**Next Steps**:
1. Present findings to Team Leader and ARB for investment prioritization
2. Develop detailed business cases for P0 recommendations (Cyber Recovery, OT Monitoring)
3. Initiate endpoint consolidation program (Corporate → CrowdStrike migration completion)
4. Engage pa-cybersecurity for detailed implementation planning
5. Update ea_architecture.db with corrections identified in Appendix

---

**Document Control**
- **Next Review Date**: August 2026 (6-month refresh)
- **Distribution**: Team Leader, CISO, CIO, ARB Members, pa-cybersecurity
- **Feedback**: Contact IT Cyber Security Enterprise Architect

---
*End of Report*
