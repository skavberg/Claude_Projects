# NIST Cybersecurity Framework Mapping
## Security Application Portfolio Analysis

---

**CENOVUS ENERGY INC.**
**IT Architecture - Enterprise Architecture**
**Internal Use Only**

---

## Document Control

| **Attribute** | **Details** |
|---------------|-------------|
| **Document Title** | NIST Cybersecurity Framework Mapping: Security Application Portfolio Analysis |
| **Document ID** | EA-CYBERSEC-2026-001 |
| **Version** | 1.0 DRAFT |
| **Classification** | Internal Use Only |
| **Date** | February 9, 2026 |
| **Author** | IT Cyber Security Enterprise Architect |
| **Reviewed By** | Documentation Specialist (formatting) |
| **Approval Status** | DRAFT - Pending CISO Review |
| **Distribution** | CISO, CIO, Architecture Review Board (ARB), Team Leader, Portfolio Architects |
| **Next Review Date** | August 2026 (6-month cycle) |

### Document Version History

| **Version** | **Date** | **Author** | **Changes** |
|-------------|----------|------------|-------------|
| 1.0 DRAFT | February 9, 2026 | IT Cyber Security EA | Initial analysis and NIST CSF mapping |

### Document Approvals

| **Role** | **Name** | **Signature** | **Date** |
|----------|----------|---------------|----------|
| **CISO** | [Pending] | | |
| **CIO** | [Pending] | | |
| **ARB Chair** | [Pending] | | |

---

## Table of Contents

1. [Executive Summary](#1-executive-summary)
   - 1.1 [Key Findings](#11-key-findings)
   - 1.2 [Critical Observations](#12-critical-observations)

2. [NIST CSF Function Mapping](#2-nist-csf-function-mapping)
   - 2.1 [IDENTIFY Function](#21-identify-function)
   - 2.2 [PROTECT Function](#22-protect-function)
   - 2.3 [DETECT Function](#23-detect-function)
   - 2.4 [RESPOND Function](#24-respond-function)
   - 2.5 [RECOVER Function](#25-recover-function)

3. [Coverage Heat Map Analysis](#3-coverage-heat-map-analysis)
   - 3.1 [Application Distribution](#31-application-distribution)
   - 3.2 [Gap Analysis](#32-gap-analysis)

4. [Rationalization Opportunities](#4-rationalization-opportunities)
   - 4.1 [Endpoint Protection Consolidation](#41-endpoint-protection-consolidation)
   - 4.2 [MFA Platform Consolidation](#42-mfa-platform-consolidation)
   - 4.3 [SIEM Instance Consolidation](#43-siem-instance-consolidation)
   - 4.4 [VPN Platform Consolidation](#44-vpn-platform-consolidation)
   - 4.5 [Database Cleanup](#45-database-cleanup)
   - 4.6 [Rationalization Summary](#46-rationalization-summary)

5. [OT/ICS Security Assessment](#5-otics-security-assessment)
   - 5.1 [OT-Specific Security Applications](#51-ot-specific-security-applications)
   - 5.2 [Architecture Assessment](#52-architecture-assessment)
   - 5.3 [OT Security Maturity](#53-ot-security-maturity)
   - 5.4 [Investment Roadmap](#54-investment-roadmap)

6. [TIME Model Analysis](#6-time-model-analysis)
   - 6.1 [TIME Distribution](#61-time-distribution)
   - 6.2 [INVEST Applications](#62-invest-applications)
   - 6.3 [TOLERATE Applications](#63-tolerate-applications)
   - 6.4 [MIGRATE Applications](#64-migrate-applications)
   - 6.5 [ELIMINATE Applications](#65-eliminate-applications)
   - 6.6 [Strategic Insights](#66-strategic-insights)

7. [Prioritized Recommendations](#7-prioritized-recommendations)
   - 7.1 [Priority 0: Critical](#71-priority-0-critical)
   - 7.2 [Priority 1: High](#72-priority-1-high)
   - 7.3 [Priority 2: Medium](#73-priority-2-medium)
   - 7.4 [Priority 3: Low](#74-priority-3-low)
   - 7.5 [Investment Summary](#75-investment-summary)

8. [Appendix: Full Application Mapping](#8-appendix-full-application-mapping)
   - 8.1 [Complete Mapping Table](#81-complete-mapping-table)
   - 8.2 [Database Cleanup Actions](#82-database-cleanup-actions)
   - 8.3 [Conclusion](#83-conclusion)

---

## 1. Executive Summary

This document presents a comprehensive mapping of Cenovus Energy's 63 security applications to the NIST Cybersecurity Framework (CSF) Core Functions. The analysis provides strategic visibility into our security capability coverage, identifies rationalization opportunities, and highlights gaps requiring investment attention.

### 1.1 Key Findings

#### Portfolio Overview

- **Total Security Applications**: 63
- **Critical Upstream/Downstream OT Security Tools**: 8
- **Multi-Instance Deployments**: 11 (indicating potential consolidation opportunities)
- **Legacy Tools Flagged for Migration/Elimination**: 3

#### NIST CSF Coverage Analysis

| **NIST Function** | **Application Count** | **% of Portfolio** | **Coverage Assessment** |
|-------------------|----------------------|-------------------|------------------------|
| **PROTECT (PR)** | 38 | 60% | STRONG |
| **DETECT (DE)** | 15 | 24% | STRONG |
| **IDENTIFY (ID)** | 8 | 13% | ADEQUATE |
| **RESPOND (RS)** | 7 | 11% | MODERATE |
| **RECOVER (RC)** | 4 | 6% | **WEAK - CRITICAL GAP** |

#### Strategic TIME Model Distribution

| **Disposition** | **Count** | **% of Portfolio** | **Strategic Meaning** |
|-----------------|-----------|-------------------|----------------------|
| **Invest** | 32 | 51% | Strategic growth platforms |
| **Tolerate** | 26 | 41% | Maintain current state |
| **Migrate** | 2 | 3% | RSA authentication transition |
| **Eliminate** | 1 | 2% | Legacy VPN decommission |

#### Financial Opportunity

**Rationalization Potential**: $880K - $1.08M annual savings through consolidation
**Investment Required**: $3.25M - $6.4M over 24 months
**Net 3-Year ROI**: Positive (savings + avoided incident costs exceed investment)

### 1.2 Critical Observations

1. **Recovery Capability Gap (CRITICAL)**
   Limited tooling for business continuity and disaster recovery from cyber incidents - a critical concern for oil and gas critical infrastructure. Only 4 applications support recovery functions, with no dedicated cyber disaster recovery orchestration or OT system restoration capability.

2. **OT/ICS Security Maturity**
   Dedicated OT security capabilities exist but are fragmented across multiple platforms. Critical gaps in OT-specific threat detection, asset inventory, backup/recovery, and incident response create unacceptable risk for upstream production facilities and downstream refining operations.

3. **Consolidation Opportunity**
   11 overlapping antivirus/endpoint protection solutions across Corporate, PCI, and OT environments represent significant rationalization opportunity with estimated annual savings of $400K-$600K through standardization on CrowdStrike Falcon platform.

4. **SOX and Compliance Alignment**
   Strong PCI-DSS coverage through dedicated security infrastructure; adequate SOX IT controls via TripWire and segregated environments; moderate OT-specific regulatory alignment (CER, IEC 62443) requiring investment.

**Purpose**: This mapping serves as the foundation for our FY2027 security architecture roadmap and Architecture Review Board (ARB) prioritization decisions.

---

## 2. NIST CSF Function Mapping

The NIST Cybersecurity Framework organizes security capabilities into five core functions: IDENTIFY, PROTECT, DETECT, RESPOND, and RECOVER. This section maps each of Cenovus Energy's 63 security applications to their primary functions.

### 2.1 IDENTIFY Function

**Core Purpose**: Asset Management, Business Environment, Governance, Risk Assessment, Risk Management Strategy, Supply Chain Risk Management

**Application Count**: 8 applications

#### Applications Mapped to IDENTIFY

1. **ForeScout Secure Connector**
   Network Access Control (NAC) provides continuous asset discovery and inventory of all devices connecting to Cenovus networks, critical for maintaining accurate IT/OT asset registers.

2. **Control Network - Access Control Server**
   Maintains authentication boundaries and access inventories for OT/ICS environments, enabling visibility into who can access production control systems.

3. **Qualys**
   Vulnerability scanning provides comprehensive asset inventory with vulnerability context, supporting risk assessment processes across IT and limited OT zones.

4. **TripWire Enterprise**
   Configuration management and integrity monitoring delivers asset baseline configurations and change detection for critical systems (SOX controls, OT safety systems).

5. **Splunk**
   SIEM aggregates asset logs and telemetry, providing unified visibility across enterprise IT, cloud, and integrated OT networks.

6. **Splunk (China)**
   Regional SIEM instance for compliance with China data sovereignty requirements, maintains asset inventory for Asia-Pacific operations.

7. **Splunk PCI**
   Dedicated SIEM for Payment Card Industry environments, maintains audit-grade asset inventory for retail/downstream payment systems.

8. **ServiceNow IT Applications**
   Custom cyber security control application manages security projects, control frameworks, and risk registers.

#### Coverage Assessment

**IDENTIFY Coverage**: ADEQUATE

**Strengths**: Core asset management and vulnerability assessment capabilities are present across IT, PCI, and OT edge environments.

**Gap Identified**: No formal supply chain risk management tooling for third-party software/vendor assessment or Software Bill of Materials (SBOM) generation.

---

### 2.2 PROTECT Function

**Core Purpose**: Identity Management & Access Control, Awareness & Training, Data Security, Information Protection Processes, Maintenance, Protective Technology

**Application Count**: 38 applications (60% of portfolio)

#### Access Control & Identity Management (15 applications)

9. **Azure Multi-Factor Authentication (MFA)**
   Second-factor authentication for Azure AD/Entra ID identities, critical protection for privileged access and remote workforce.

10. **Azure Self-Service Password Reset**
    Reduces help desk load while maintaining secure password lifecycle management.

11. **Duo Security (Cisco)**
    Two-factor authentication for shared services and legacy systems not integrated with Azure MFA.

12. **Microsoft Authenticator**
    Mobile MFA application supporting passwordless and push notification authentication.

13. **NPS Server**
    Network Policy Server enforces MFA for radius-authenticated services (WiFi, VPN, network equipment management).

14. **RSA - Authentication Manager**
    Legacy authentication management platform (MIGRATE status - transitioning to Azure MFA/Entra ID).

15. **RSA - SecurID**
    Hardware/software token-based authentication (MIGRATE status - replacement with Yubikeys and Azure MFA).

16. **Yubikeys**
    FIDO2 hardware tokens for phishing-resistant authentication, critical for privileged users and OT engineering workstations.

17. **Entra Private Network Connector**
    Zero Trust Network Access (ZTNA) providing secure remote access to internal applications without VPN.

18. **Global Protect VPN**
    Palo Alto VPN client for remote access, integrated with MFA and endpoint posture checking.

19. **ICS Access**
    Secure remote access solution specifically designed for plant facilities and control networks, providing jump host and session monitoring capabilities.

20. **myvpn.cenovus.com**
    Legacy VPN landing zone (ELIMINATE status - migrating users to Global Protect and Entra Private Network Connector).

21. **Process Control VMWare Horizon Client**
    Virtual Desktop Infrastructure (VDI) providing secure access to control network engineering applications with session isolation.

22. **Ericom AccessNow**
    HTML5-based application gateway for Juniper devices, provides clientless remote access.

23. **KeePass**
    Open source password manager for non-enterprise use cases and lab environments.

24. **Keeper**
    Enterprise password management with vault sharing, supports SOX segregation of duties for shared service accounts.

#### Endpoint Protection (13 applications)

25. **CrowdStrike Falcon**
    Next-generation endpoint detection and response (EDR) for corporate Windows/Mac endpoints, primary strategic platform.

26. **Falcon**
    [Duplicate listing - refers to CrowdStrike deployment]

27. **McAfee ePolicy Orchestrator Corp**
    Legacy antivirus management for corporate estate during CrowdStrike migration.

28. **McAfee Management (ePO Corp)**
    [Duplicate ePO instance reference]

29. **McAfee Move**
    Virtualized security for VMware environments, agentless antivirus.

30. **McAfee ePolicy Orchestrator (Lima)**
    Dedicated antivirus management for Lima refinery operations.

31. **McAfee ePolicy Orchestrator PCI**
    Dedicated ePO for PCI-DSS cardholder data environment.

32. **McAfee Management (ePO PCI)**
    [Duplicate PCI ePO reference]

33. **McAfee PCI**
    Antivirus deployment in PCI environment.

34. **Bit9 - Downstream**
    Application whitelisting for downstream retail locations, prevents unauthorized software execution.

35. **Bit9 Parity**
    Application control on retail point-of-sale and back-office computers.

36. **Symantec Endpoint Protection Control Network**
    Specialized endpoint protection for OT/ICS Windows-based engineering workstations and HMI servers.

37. **Symantec End-point Protection Management Server**
    Management infrastructure for OT endpoint protection.

38. **System Center Endpoint Protection**
    Microsoft Defender integration for Windows Server environments.

39. **Sophos Antivirus (Linux - Red Hat)**
    Linux endpoint protection for RHEL servers supporting upstream operations and enterprise applications.

40. **CLAM**
    Open source antivirus for Linux systems, primarily mail servers and file scanning.

#### Data Protection & Encryption (3 applications)

41. **Azure Information Protection (AIP)**
    Document and email classification with rights management, supports data loss prevention and confidentiality labeling.

42. **DataMotion Secure Email**
    Encrypted email gateway for secure external communications containing sensitive operational or competitive data.

43. **Microsoft Office 365 Security & Compliance Console**
    Data Loss Prevention (DLP), retention policies, eDiscovery, and compliance management for M365 tenant.

#### Network Protection (4 applications)

44. **Panorama**
    Centralized management for Palo Alto Networks firewalls across all Cenovus locations, enforces network segmentation policies.

45. **External Dynamic List**
    Dynamic firewall policy updates based on threat intelligence feeds, enables rapid blocking of malicious IPs/domains.

46. **Control Network - Access Control Server**
    [Also mapped to IDENTIFY] Enforces access control policies at OT network boundaries.

47. **ForeScout Secure Connector**
    [Also mapped to IDENTIFY] Network Access Control enforces device compliance before network access.

#### Cloud Security (2 applications)

48. **Microsoft Cloud App Security**
    Cloud Access Security Broker (CASB) for SaaS application visibility, shadow IT detection, and policy enforcement.

49. **Prisma Cloud - Code Security**
    Cloud-native application protection platform (CNAPP) securing Azure infrastructure and container workloads.

#### Security Awareness & Training (2 applications)

50. **Proofpoint Security Awareness Training**
    Simulated phishing campaigns and interactive training modules, critical for human firewall development.

51. **Immersive Lab**
    Hands-on cyber security skills training platform for IT and security teams, supports incident response readiness.

#### Coverage Assessment

**PROTECT Coverage**: STRONG

**Strengths**: Comprehensive coverage across identity, endpoint, network, and data protection domains. Strong cloud security posture with Azure/M365 security stack integration.

**Rationalization Opportunity**: 11 separate antivirus/EDR deployments across Corporate, PCI, and OT environments represent consolidation opportunity.

**Modernization Progress**: Identity management is actively transitioning from legacy RSA to modern Azure/Entra ID platform with FIDO2/Yubikey support.

---

### 2.3 DETECT Function

**Core Purpose**: Anomalies & Events, Security Continuous Monitoring, Detection Processes

**Application Count**: 15 applications (24% of portfolio)

#### SIEM & Log Management (5 applications)

52. **Splunk**
    Primary SIEM platform aggregating logs from IT, cloud, OT edge, and security tools for correlation and threat detection.

53. **Splunk (China)**
    Regional SIEM instance for China operations compliance with data sovereignty requirements.

54. **Splunk PCI**
    Dedicated SIEM for PCI-DSS log retention and monitoring requirements.

55. **Cribl**
    Log routing and pre-processing layer that optimizes Splunk ingestion, enables tiered storage and log enrichment.

56. **Windows Event Collector**
    Centralized Windows event log collection infrastructure feeding Splunk.

#### Endpoint Detection & Response (2 applications)

57. **CrowdStrike Falcon**
    [Also mapped to PROTECT] EDR capability provides behavioral threat detection, process monitoring, and threat hunting on endpoints.

58. **TripWire Enterprise**
    [Also mapped to IDENTIFY] File integrity monitoring (FIM) detects unauthorized changes to critical system files and configurations.

#### Network Detection (3 applications)

59. **Sourcefire Appliance**
    Next-generation IPS/IDS providing network traffic inspection and threat detection at perimeter and internal segments.

60. **Endace**
    Full packet capture appliance for forensic network traffic analysis during security investigations.

61. **ForeScout Secure Connector**
    [Also mapped to IDENTIFY/PROTECT] Detects rogue devices, non-compliant endpoints, and anomalous network behavior.

#### Email Security (3 applications)

62. **Proofpoint**
    Advanced email threat protection detecting phishing, malware, business email compromise, and credential harvesting attacks.

63. **Proofpoint Audit**
    Email audit trail and investigation capability for incident response and compliance.

64. **SPAM Digest**
    Daily spam quarantine digest allowing users to review blocked emails.

#### Vulnerability & Configuration Monitoring (2 applications)

65. **Qualys**
    [Also mapped to IDENTIFY] Continuous vulnerability scanning detects exploitable weaknesses before attackers.

66. **TripWire Enterprise**
    [Also mapped to IDENTIFY/PROTECT] Configuration deviation detection for compliance drift.

#### External Threat Intelligence (1 application)

67. **ZeroFox**
    External digital risk monitoring detecting phishing sites impersonating Cenovus, executive impersonation, brand abuse, and data leaks on dark web.

#### Coverage Assessment

**DETECT Coverage**: STRONG

**Strengths**: Comprehensive visibility across endpoints, network, email, and external threat landscape. Strong SIEM correlation capabilities with Splunk.

**SIEM Fragmentation**: Three Splunk instances (Corporate, China, PCI) reflects compliance requirements but increases operational complexity and licensing costs.

**OT Gap**: Limited industrial protocol visibility (Modbus, DNP3, OPC UA/DA) - corporate SIEM monitors OT edge but cannot detect OT-specific attack patterns.

---

### 2.4 RESPOND Function

**Core Purpose**: Response Planning, Communications, Analysis, Mitigation, Improvements

**Application Count**: 7 applications (11% of portfolio)

#### Applications Mapped to RESPOND

68. **Palo Alto Cortex XSOAR**
    Security Orchestration, Automation, and Response (SOAR) platform enabling playbook-driven incident response, case management, and automated containment actions.

69. **Splunk**
    [Also mapped to IDENTIFY/DETECT] Incident investigation and threat hunting platform, supports response workflows.

70. **CrowdStrike Falcon**
    [Also mapped to PROTECT/DETECT] Enables remote endpoint isolation, process termination, and remediation during active incidents.

71. **Panorama**
    [Also mapped to PROTECT] Enables rapid firewall rule deployment to contain threats and block malicious infrastructure.

72. **Axiom Cyber**
    Digital forensic investigation platform for post-incident evidence collection and analysis.

73. **HTTPWatch**
    Web traffic troubleshooting tool supporting investigation of web-based attack chains.

74. **NMap**
    Network scanning tool for incident response reconnaissance and affected system identification.

#### Coverage Assessment

**RESPOND Coverage**: MODERATE

**Strengths**: Core SOAR platform (Cortex XSOAR) provides playbook automation and case management. EDR capabilities (CrowdStrike) enable rapid endpoint containment.

**Gaps Identified**:
- No dedicated incident response communications platform (risk of compromised email/collaboration during incident)
- Limited formal runbook/playbook repository management
- OT incident response capability limited - no dedicated OT forensics tooling for industrial protocol analysis or PLC forensics

---

### 2.5 RECOVER Function

**Core Purpose**: Recovery Planning, Improvements, Communications

**Application Count**: 4 applications (6% of portfolio) - **CRITICAL GAP**

#### Applications Mapped to RECOVER

75. **Palo Alto Cortex XSOAR**
    [Also mapped to RESPOND] Post-incident workflow automation and lessons-learned tracking.

76. **ServiceNow IT Applications**
    [Also mapped to IDENTIFY] Tracks security incidents and remediation actions, supports change management for recovery activities.

77. **Splunk**
    [Also mapped to IDENTIFY/DETECT/RESPOND] Historical analysis supporting recovery time validation and lessons-learned analysis.

78. **TripWire Enterprise**
    [Also mapped to IDENTIFY/PROTECT/DETECT] Configuration restoration and baseline re-establishment after security incidents.

#### Coverage Assessment

**RECOVER Coverage**: WEAK - **CRITICAL GAP IDENTIFIED**

**Critical Deficiency**: Limited dedicated tooling for:
- Disaster recovery orchestration from cyber incidents
- Backup validation and immutable backup storage
- Ransomware recovery capabilities
- Business continuity management specific to cyber incidents
- OT system restoration (PLC logic, DCS configurations, HMI screens)

**Risk Impact**: This represents significant risk for critical oil and gas infrastructure where production downtime has material financial impact. Extended recovery times could result in:
- Days-to-weeks upstream production facility outages
- Downstream refinery disruptions with significant revenue impact
- Pipeline operational disruptions affecting product delivery
- Potential safety system compromise during recovery operations

**Regulatory Concern**: Gap creates potential non-compliance with SOX business continuity requirements and IEC 62443-3-3 SR 7.1/7.2 (Backup and Recovery).

---

## 3. Coverage Heat Map Analysis

### 3.1 Application Distribution

The following table summarizes application coverage across NIST CSF functions:

| **NIST Function** | **Application Count** | **% of Portfolio** | **Coverage Assessment** | **Priority** |
|-------------------|----------------------|-------------------|------------------------|--------------|
| **PROTECT (PR)** | 38 | 60.3% | STRONG | Maintain |
| **DETECT (DE)** | 15 | 23.8% | STRONG | Maintain |
| **IDENTIFY (ID)** | 8 | 12.7% | ADEQUATE | Enhance |
| **RESPOND (RS)** | 7 | 11.1% | MODERATE | Enhance |
| **RECOVER (RC)** | 4 | 6.3% | **WEAK** | **INVEST** |

**Note**: Many applications map to multiple functions; percentages exceed 100% due to overlapping capabilities.

### 3.2 Gap Analysis

#### Critical Gaps (HIGH Priority)

**1. RECOVER Function Underserved**

**Current State**: Only 4 applications with recovery capability; no dedicated cyber disaster recovery orchestration.

**Risk**: Extended downtime following ransomware or destructive attack (e.g., EKANS, Industroyer). Recovery time could extend to days-to-weeks versus hours with proper tooling.

**Impact**:
- Upstream production facility outages (SAGD facilities)
- Pipeline disruptions affecting product delivery
- Downstream refinery shutdowns with $5M-$15M daily revenue impact

**Recommendation**: Invest in cyber recovery orchestration platform (e.g., Zerto Cyber Resilience, Commvault DR, Rubrik), immutable backup validation, and OT system restoration runbooks.

**Investment Required**: $500K-$800K

---

**2. OT/ICS Recovery Capability**

**Current State**: No dedicated OT disaster recovery solution or golden image repository for control systems (PLCs, DCS, SCADA).

**Risk**: Extended recovery time for control systems following cyber incident. Manual PLC reprogramming could take days-to-weeks versus hours with automated restoration.

**Impact**:
- Upstream production halt at SAGD facilities
- Downstream refining disruption
- Safety system restoration delays

**Recommendation**: Implement OT backup and recovery solution compliant with IEC 62443-3-3 SR 7.1/7.2 (e.g., Radiflow, Veeam for OT, Veritas OT Backup) with automated PLC logic extraction and versioning.

**Investment Required**: $300K-$500K

---

**3. Supply Chain Risk Management (IDENTIFY Function)**

**Current State**: No dedicated tooling for software bill of materials (SBOM) analysis or third-party risk assessment.

**Risk**: Undetected vulnerabilities in vendor software; supply chain compromises (e.g., SolarWinds-style attacks); limited visibility into OT vendor software components.

**Recommendation**: Evaluate supply chain security platforms (e.g., Black Duck, Sonatype, Snyk) for SBOM generation and continuous vulnerability monitoring.

**Investment Required**: $150K-$250K

---

#### Moderate Gaps (MEDIUM Priority)

**4. OT-Specific Threat Detection**

**Current State**: Corporate SIEM (Splunk) monitors OT edge zones. Limited industrial protocol (Modbus, DNP3, OPC UA/DA, EtherNet/IP) deep packet inspection capability.

**Risk**: Cannot detect OT-specific attack patterns such as:
- Unauthorized PLC programming or ladder logic manipulation
- Process setpoint changes outside normal parameters
- Safety system bypasses
- Industrial protocol abuse

**Regulatory Context**: IEC 62443-3-3 SR 6.1 (Audit Log Accessibility) and SR 4.1 (Information Confidentiality) require OT-aware monitoring.

**Recommendation**: Evaluate OT network monitoring platforms with industrial protocol dissection and physics-based anomaly detection (e.g., Nozomi Networks, Claroty, Dragos).

**Investment Required**: $400K-$800K platform + 2 FTE SOC analysts with OT expertise

---

**5. Privileged Access Management (PAM)**

**Current State**: Keeper password manager provides vault sharing capability. No privileged session recording or just-in-time access provisioning.

**Risk**: Inadequate oversight of privileged operations in OT and IT environments; potential SOX control weakness for shared administrative accounts.

**Recommendation**: Implement enterprise PAM solution (e.g., CyberArk, BeyondTrust) with session recording, just-in-time access, and credential rotation.

**Investment Required**: $300K-$500K

---

**6. Incident Response Communications**

**Current State**: No dedicated secure crisis communications platform separate from corporate email/collaboration tools.

**Risk**: During a cyber incident, corporate email and collaboration platforms may be compromised, impaired, or unavailable, preventing effective incident response coordination.

**Recommendation**: Implement out-of-band incident response communications capability (e.g., dedicated Signal/WhatsApp channels with pre-distributed credentials, satellite phones for critical responders).

**Investment Required**: $50K-$100K

---

#### Minor Gaps (LOW Priority)

**7. Cloud Security Posture Management (CSPM)**

**Current State**: Prisma Cloud provides code security (CNAPP); limited runtime cloud configuration monitoring and compliance validation.

**Risk**: Azure misconfigurations could expose data or services. Lack of continuous compliance validation against CIS Azure benchmarks.

**Recommendation**: Expand Prisma Cloud CSPM deployment or evaluate Microsoft Defender for Cloud CSPM features for comprehensive Azure posture management.

**Investment Required**: $50K-$100K

---

**8. Security Awareness Metrics**

**Current State**: Proofpoint provides phishing simulation and training modules. Limited gamification, culture measurement, or behavioral analytics.

**Risk**: Difficulty measuring security culture maturity and identifying high-risk user populations requiring additional training.

**Recommendation**: Enhance security awareness program with culture assessment tools and behavioral analytics.

**Investment Required**: $30K-$50K

---

## 4. Rationalization Opportunities

The security application portfolio contains significant duplication and overlap, particularly in endpoint protection, authentication, and SIEM platforms. Consolidation presents substantial cost savings and operational efficiency opportunities.

### 4.1 Endpoint Protection Consolidation

**Issue**: Cenovus operates 11 separate antivirus/endpoint protection solutions across Corporate, PCI, and OT environments.

#### Current State

- CrowdStrike Falcon (Corporate - strategic EDR)
- McAfee ePO Corp / McAfee Corporate (legacy)
- McAfee ePO PCI / McAfee PCI (compliance-mandated separation)
- McAfee ePO Lima (Lima refinery)
- McAfee Move (virtualized antivirus)
- Symantec Endpoint Protection + Management Server (OT control networks)
- System Center Endpoint Protection (Windows Server)
- Sophos Antivirus (Linux RHEL)
- CLAM (Linux open source)
- Bit9 / Bit9 Parity (application whitelisting downstream/retail)

#### Rationalization Roadmap

**Phase 1: Corporate Consolidation** (FY2027 Q1-Q2)

**Action**: Complete migration from McAfee ePO Corp to CrowdStrike Falcon for all corporate Windows/Mac endpoints.

**Products Eliminated**: 3 (McAfee Corporate, McAfee ePO Corp, McAfee Move)

**Timeline**: 6 months

---

**Phase 2: Linux Standardization** (FY2027 Q3)

**Action**: Standardize on CrowdStrike Falcon for Linux (supports RHEL distributions).

**Products Eliminated**: 2 (Sophos Antivirus, CLAM)

**Timeline**: 3 months

---

**Phase 3: PCI Rationalization** (FY2027 Q4)

**Action**: Migrate PCI cardholder data environment to CrowdStrike Falcon after PCI-DSS compliance validation.

**Products Eliminated**: 2 (McAfee ePO PCI, McAfee PCI)

**Timeline**: 3 months (includes QSA attestation)

**Risk Mitigation**: Engage Qualified Security Assessor (QSA) for PCI-DSS compliance validation before migration.

---

**Phase 4: Downstream Consolidation** (FY2028 Q1)

**Action**: Evaluate CrowdStrike application control features as Bit9 replacement for downstream retail locations and point-of-sale systems.

**Products Eliminated**: 2 (Bit9, Bit9 Parity) - if CrowdStrike application whitelisting meets downstream security requirements

**Timeline**: 6 months (includes pilot and validation)

---

**Phase 5: OT Strategic Decision** (FY2028 Q2)

**Decision Point**: Retain Symantec Endpoint Protection for OT control networks OR migrate to CrowdStrike with OT-specific deployment model.

**Evaluation Factors**:
- IEC 62443 compliance validation
- Air-gapped update process for isolated OT zones
- OT vendor support statements for EDR on ICS networks
- Performance impact testing on real-time control systems

**Products Eliminated**: 2 (Symantec EPP, Management Server) - if migration approved

**Timeline**: 9-12 months (includes extensive pilot in non-critical OT zones)

**Risk Mitigation**: Pilot CrowdStrike in non-critical OT zones before production control network deployment. Maintain Symantec for safety-critical systems until validation complete.

---

#### Consolidation Benefits

**Estimated Product Reduction**: 9-11 products consolidated to 2-3 strategic platforms (CrowdStrike primary, potential Symantec retention for OT)

**Annual Licensing Cost Savings**: $400K-$600K (McAfee, Symantec, Sophos, Bit9 licensing eliminated)

**Operational Efficiency**:
- Single pane of glass for endpoint visibility across enterprise
- Unified threat hunting and incident response capability
- Reduced staff training burden (one EDR platform vs. four separate technologies)
- Simplified integration with SOAR (Cortex XSOAR) and SIEM (Splunk)
- Consistent policy enforcement across all environments

---

### 4.2 MFA Platform Consolidation

**Issue**: Three separate multi-factor authentication platforms creating user confusion and administrative overhead.

#### Current State

- Azure MFA (strategic platform, integrated with Entra ID)
- Duo Security (Cisco) - legacy for shared services
- RSA SecurID + Authentication Manager (MIGRATE status - 85% complete)
- Yubikeys (hardware tokens for privileged users)

#### Rationalization Roadmap

**Phase 1: RSA Retirement** (FY2027 Q1) - **IN PROGRESS**

**Current Status**: 85% migration complete

**Action**:
- Complete migration of remaining RSA SecurID users to Azure MFA or Yubikeys
- Identify and remediate final RSA-integrated systems (likely network equipment, legacy applications)
- Decommission RSA Authentication Manager infrastructure

**Products Eliminated**: 2 (RSA SecurID, RSA Authentication Manager)

**Cost Savings**: $150K annual RSA licensing + maintenance

**Timeline**: 3 months

**Target Retirement Date**: June 2027

---

**Phase 2: Duo Migration Assessment** (FY2027 Q2)

**Action**:
- Evaluate Duo use cases (likely network equipment, legacy RADIUS clients, shared services)
- Migrate to Azure MFA via NPS Server where technically feasible
- Retain Duo only if technical blockers exist for specific legacy systems

**Products Eliminated**: 1 (Duo Security) - contingent on technical feasibility

**Cost Savings**: $80K annual Duo licensing

**Timeline**: 6 months (includes technical validation)

---

**Phase 3: Standardized Hardware Token** (FY2027 Q3)

**Action**:
- Standardize on Yubikeys as sole hardware token for privileged users and OT engineers requiring phishing-resistant authentication
- Ensure Azure MFA + Yubikey FIDO2 integration for passwordless authentication

**Timeline**: 3 months

---

#### Consolidation Benefits

**Estimated Product Reduction**: 2-3 products consolidated to Azure MFA + Yubikeys

**Annual Licensing Cost Savings**: $230K

**User Experience Improvements**:
- Simplified authentication experience (single MFA platform)
- Reduced authentication app fatigue
- Passwordless authentication capability with FIDO2/Yubikeys
- Modern mobile-first authentication

---

### 4.3 SIEM Instance Consolidation

**Issue**: Three separate Splunk deployments creating data silos and increasing licensing costs.

#### Current State

- Splunk (primary enterprise SIEM for Corporate IT and OT edge)
- Splunk China (Asia-Pacific compliance with data sovereignty requirements)
- Splunk PCI (PCI-DSS cardholder data environment)
- Cribl (log routing and optimization layer)

#### Rationalization Options

**Option A: Federated Splunk with Index-Based Segmentation** (RECOMMENDED)

**Approach**:
- Consolidate Splunk PCI and Splunk China into primary Splunk deployment
- Use Splunk index-level access controls to maintain PCI and China data segregation
- Deploy Cribl as universal log router enforcing data residency and compliance boundaries
- Implement role-based access control (RBAC) ensuring PCI data accessible only to authorized personnel

**Benefits**:
- Unified threat correlation across all environments
- Cross-environment attack chain visibility (e.g., lateral movement from Corporate to PCI)
- Simplified administration (single Splunk cluster vs. three independent instances)
- Reduced licensing costs through volume consolidation

**Estimated Reduction**: 2 Splunk instances consolidated into 1 multi-tenant instance

**Cost Impact**: Licensing consolidation may yield 15-20% savings (~$200K annually)

**Compliance Requirements**:
- Engage Qualified Security Assessor (QSA) for PCI-DSS 12.3.8 attestation validating logical segregation meets cardholder data protection requirements
- Engage legal counsel for China data sovereignty validation ensuring index-based controls satisfy local data residency laws

**Risk Mitigation**:
- Pilot consolidated model in non-production environment
- Validate RBAC controls prevent unauthorized PCI data access
- Ensure Cribl routing rules enforce China data residency (data remains in China Azure region)

**Timeline**: 12-15 months (includes compliance validation, pilot, and production cutover)

---

**Option B: Maintain Separate Instances** (STATUS QUO)

**Approach**:
- Retain three separate Splunk instances if compliance auditors require physical segregation
- Enhance cross-instance correlation via Cortex XSOAR federation and Cribl data sharing
- Accept ongoing licensing and operational overhead

**When to Choose**: If PCI QSA or China legal counsel mandate physical segregation beyond logical controls.

---

#### Recommendation

Pursue Option A (Federated Splunk) with formal compliance validation. If validation fails, fall back to Option B with enhanced correlation.

---

### 4.4 VPN Platform Consolidation

**Issue**: Two VPN platforms creating split-brain remote access architecture.

#### Current State

- Global Protect VPN (Palo Alto - strategic platform with MFA integration and endpoint posture checking)
- myvpn.cenovus.com (legacy VPN - ELIMINATE status)
- Entra Private Network Connector (Zero Trust Network Access - emerging strategic direction)

#### Rationalization Roadmap

**Phase 1: Legacy VPN Retirement** (FY2027 Q2) - **IN PROGRESS**

**Current Status**: 70% user migration complete

**Action**:
- Complete user migration from myvpn.cenovus.com to Global Protect VPN
- Identify and migrate remaining users (likely legacy system dependencies)
- Retire legacy VPN infrastructure

**Products Eliminated**: 1 (myvpn.cenovus.com)

**Cost Savings**: $50K annually (infrastructure, licensing, support)

**Timeline**: 6 months

**Target Decommission Date**: September 2027

---

**Phase 2: Zero Trust Transition** (FY2027-2028)

**Strategic Direction**: Shift from network-level VPN access to application-level Zero Trust Network Access (ZTNA).

**Action**:
- Expand Entra Private Network Connector for application-specific access where feasible
- Reduce reliance on full VPN tunnel in favor of least-privilege application access
- Maintain Global Protect VPN for scenarios requiring network-level access (e.g., OT engineering access to control networks, network management)

**Timeline**: 18-24 months (phased application onboarding)

---

#### Consolidation Benefits

**Estimated Product Reduction**: 1 product eliminated immediately (legacy VPN)

**Security Improvements**:
- Reduced attack surface via application-level access vs. network-level access
- Enhanced visibility into user access patterns (application-specific vs. broad network access)
- Improved compliance posture (least-privilege access principle)

---

### 4.5 Database Cleanup

**Issue**: Enterprise Architecture database (ea_architecture.db) contains duplicate entries for the same products with different naming conventions, artificially inflating application count.

#### Duplicates Identified

1. **CrowdStrike Falcon (ID 10) = Falcon (ID 17)**
   **Action**: Retain ID 10 ("CrowdStrike Falcon"), remove ID 17

2. **McAfee Management (ePO Corp) (ID 25) = McAfee ePolicy Orchestrator Corp (ID 30)**
   **Action**: Retain ID 30 (canonical name), remove ID 25

3. **McAfee Management (ePO PCI) (ID 26) = McAfee ePolicy Orchestrator PCI (ID 31)**
   **Action**: Retain ID 31 (canonical name), remove ID 26

#### Result

**Before Cleanup**: 63 applications
**After Cleanup**: 60 unique applications (3 duplicate entries removed)

**Action Required**: Update ea_architecture.db to remove duplicate entries and establish naming convention standards to prevent future duplication.

---

### 4.6 Rationalization Summary

| **Opportunity** | **Products Affected** | **Reduction Potential** | **Annual Cost Savings** | **Timeline** | **Complexity** |
|-----------------|----------------------|------------------------|------------------------|--------------|----------------|
| Endpoint Protection Consolidation | 11 | 9-11 products | $400K-$600K | 18-24 months | HIGH |
| MFA Platform Consolidation | 4 | 2-3 products | $230K | 6-9 months | MEDIUM |
| SIEM Instance Consolidation | 3 | 2 instances | $200K* | 12-15 months | HIGH |
| VPN Platform Consolidation | 2 | 1 product | $50K | 6 months | LOW |
| Database Cleanup | 3 | 3 duplicate entries | $0 | Immediate | LOW |
| **TOTAL** | **23** | **17-20 products** | **$880K-$1.08M** | **6-24 months** | **VARIES** |

*SIEM consolidation savings contingent on compliance validation approval

#### Portfolio Reduction Impact

**Current State**: 63 applications
**Target State**: 43-46 applications
**Reduction**: 27-32% portfolio rationalization

#### Strategic Benefits Beyond Cost Savings

- Simplified security operations center (SOC) analyst training (fewer platforms to master)
- Unified threat intelligence sharing across integrated platforms
- Reduced integration complexity (fewer API connectors and custom integrations)
- Improved incident response speed (single endpoint control plane for containment)
- Enhanced threat hunting capability (cross-tool correlation in unified platforms)
- Reduced vendor management overhead (fewer contracts, renewals, support relationships)

---

## 5. OT/ICS Security Assessment

As an integrated oil and gas company, Cenovus operates extensive Operational Technology (OT) and Industrial Control Systems (ICS) critical to production, transportation, and refining operations:

- **Upstream**: SAGD (Steam-Assisted Gravity Drainage) production facilities, well pads, central processing facilities
- **Midstream**: Pipeline SCADA systems for crude oil and product transportation
- **Downstream**: Refinery Distributed Control Systems (DCS), upgrading facilities, product terminals, retail locations

### 5.1 OT-Specific Security Applications

The following 8 applications provide dedicated OT/ICS security capabilities:

| **Application** | **OT Security Function** | **IEC 62443 Zone** | **Criticality** | **Assessment** |
|-----------------|-------------------------|-------------------|----------------|----------------|
| **Control Network - Access Control Server** | Authentication boundary enforcement for OT network access | Level 2/3 Boundary | MEDIUM | Adequate - enforces authentication boundary between IT and OT; prevents unauthorized access to production control systems |
| **ICS Access** | Secure remote access to plant facilities and control systems | Level 1-3 Access | LOW | Adequate - provides jump host capability and session isolation for vendor/engineer remote access to OT networks |
| **Process Control VMWare Horizon Client** | VDI for control network engineering applications | Level 2 Engineering | LOW | Adequate - isolates engineering workstations from corporate network; prevents malware lateral movement |
| **Symantec Endpoint Protection Control Network** | Antivirus for OT Windows systems (HMIs, engineering workstations, historians) | Level 2/3 HMI/Engineering | MEDIUM | Tolerate - provides malware protection without disrupting real-time operations; requires air-gapped update process |
| **Symantec End-point Protection Management Server** | OT antivirus management infrastructure | Level 2 Management | LOW | Tolerate - centralized management with air-gapped update process suitable for OT constraints |
| **McAfee ePolicy Orchestrator (Lima)** | Lima refinery antivirus deployment | Level 2/3 Lima Refinery | MEDIUM | Tolerate - dedicated to Lima refinery operations; separate from corporate ePO |
| **Bit9 - Downstream** | Application whitelisting for retail/downstream locations | Level 3 Downstream | MEDIUM | Tolerate - prevents unauthorized software execution on retail point-of-sale and back-office systems |
| **Splunk** (OT edge monitoring) | Log collection from OT DMZ and IT/OT boundary | Level 3 Edge | LOW | Adequate - monitors IT/OT network boundary; limited visibility into Level 0-2 process control networks |

### 5.2 Architecture Assessment

#### Strengths

1. **Network Segmentation**
   Clear boundary enforcement between IT and OT zones via dedicated access control servers. Prevents unauthorized lateral movement from corporate network into production control systems.

2. **Remote Access Security**
   Multiple security layers (ICS Access jump hosts, VDI, MFA) for vendor and engineering remote access to OT systems. Reduces risk of compromised remote access credentials.

3. **Endpoint Protection**
   Dedicated antivirus solutions for OT Windows-based systems (HMIs, engineering workstations, historians) with air-gapped update processes appropriate for OT operational constraints.

4. **Application Control**
   Application whitelisting (Bit9) prevents unauthorized code execution in downstream/retail environments, mitigating malware and ransomware risk.

#### Critical Gaps

**1. OT-Specific Threat Detection** - **CRITICAL GAP**

**Current State**: Splunk monitors OT network edge zones. No deep packet inspection of industrial protocols (Modbus, DNP3, OPC UA/DA, EtherNet/IP, Profinet, IEC 61850).

**Risk**: Cannot detect OT-specific attack patterns including:
- Unauthorized PLC programming or ladder logic manipulation (e.g., Stuxnet-style attacks)
- Process setpoint changes outside normal operational parameters
- Safety system bypasses or disablement
- Historian data manipulation
- Industrial protocol abuse or replay attacks

**Regulatory Context**: IEC 62443-3-3 SR 6.1 (Audit Log Accessibility) and SR 4.1 (Information Confidentiality) require OT-aware monitoring with industrial protocol visibility.

**Recommendation**: Deploy OT network monitoring platform with industrial protocol dissection and physics-based anomaly detection (e.g., Nozomi Networks, Claroty, Dragos).

**Investment**: $400K-$800K for platform + 2 FTE SOC analysts with OT security expertise

**Regulatory Driver**: Canadian Energy Regulator (CER) cybersecurity expectations for pipeline operators; IEC 62443 compliance

---

**2. OT Asset Inventory and Vulnerability Management** - **HIGH GAP**

**Current State**: ForeScout and Qualys provide IT asset discovery and vulnerability scanning. Limited visibility into Level 0-2 OT devices (PLCs, RTUs, field instruments, DCS controllers).

**Risk**:
- Incomplete asset inventory impairs incident response and remediation (cannot rapidly identify affected systems)
- Unknown vulnerability exposure in OT devices (e.g., critical vulnerabilities in Triconex safety systems, as exploited by Triton/Trisis malware)
- Inability to assess patch status or firmware versions for OT equipment

**Regulatory Context**: IEC 62443-2-1 (Security Program Requirements) mandates comprehensive OT asset inventory including firmware versions, network connections, and security configurations.

**Recommendation**: Deploy passive OT asset discovery solution using industrial protocol analysis without active scanning (e.g., Claroty Continuous Threat Detection, Armis, or integrated with OT monitoring platform). Integrate OT asset inventory with ServiceNow CMDB.

**Investment**: $200K-$400K platform + CMDB integration

---

**3. OT Backup and Disaster Recovery** - **CRITICAL GAP**

**Current State**: No dedicated OT configuration backup solution or golden image repository for control systems. PLC logic, DCS configurations, and HMI screens are not systematically backed up or version-controlled.

**Risk**: Extended recovery time following ransomware, destructive malware (e.g., Industroyer, EKANS), or insider sabotage affecting:
- PLC ladder logic and function blocks
- HMI screens and operator interfaces
- DCS control strategies and regulatory loops
- SCADA configuration databases
- Historian configurations

**Impact**: Days-to-weeks manual recovery process vs. hours with automated restoration. Production downtime costs $5M-$15M per day for major facilities.

**Regulatory Context**: IEC 62443-3-3 SR 7.1 (Backup) and SR 7.2 (Recovery and Reconstitution) require OT system backup capability with tested restoration procedures.

**Recommendation**: Implement OT backup solution with automated PLC/DCS logic extraction, configuration versioning, and restoration runbooks (e.g., Radiflow, Veeam for OT, Veritas OT Backup).

**Investment**: $300K-$500K platform + runbook development and testing

---

**4. OT Incident Response and Forensics** - **HIGH GAP**

**Current State**: Axiom Cyber provides IT digital forensics capability. No OT-specific forensic tools for industrial protocol analysis, PLC memory dump analysis, or control system forensics.

**Risk**: Cannot perform root cause analysis after OT cyber incident, including:
- Determining if production disruption was cyber-induced vs. operational issue
- Analyzing PLC memory dumps for malicious code or logic modifications
- Reconstructing industrial protocol communications during incident
- Identifying attack vectors and lateral movement within OT networks

**Recommendation**:
- Train incident response team on OT forensics (e.g., SANS ICS515: ICS Visibility, Detection, and Response)
- Acquire OT forensic tools for PLC dump analysis and industrial protocol PCAP analysis
- Develop OT incident response playbooks integrated with Cortex XSOAR

**Investment**: $100K for training + tools

---

**5. OT Patch Management** - **MEDIUM GAP**

**Current State**: No centralized OT patch management process. Patching occurs during planned turnarounds and maintenance windows, typically annually or bi-annually.

**Risk**: Extended vulnerability windows (ICS systems often remain 2-5 years behind current patches due to operational constraints and vendor testing requirements).

**Recommendation**: Implement risk-based OT patch management process with:
- Vulnerability prioritization based on exploitability and operational impact
- Virtual patching via IPS signatures for critical vulnerabilities that cannot be patched during production
- Coordinated patching during planned turnarounds with pre-tested configurations

**Investment**: Process development + staff training (~$50K)

---

**6. Safety System Security** - **MEDIUM GAP**

**Current State**: Safety Instrumented Systems (SIS) - including Triconex and Siemens safety PLCs - have limited cyber security monitoring. SIS networks typically connected to DCS for operational data sharing.

**Risk**: Safety system compromise could result in catastrophic safety events including:
- Inability to execute emergency shutdown (ESD) procedures
- False activation of safety systems causing unnecessary production shutdown
- Disablement of safety interlocks allowing unsafe operating conditions
- Potential for explosion, fire, or environmental release

**Regulatory Context**: IEC 61511 (Functional Safety - SIS) increasingly requires cyber security controls for safety systems. Convergence of safety and security standards.

**Recommendation**:
- Implement unidirectional gateways (data diodes) between SIS and DCS networks (e.g., Waterfall Security, Owl Cyber Defense)
- Deploy SIS-specific change detection and configuration monitoring
- Prioritize critical facilities (SAGD production facilities, refineries) with high consequence of failure

**Investment**: $200K-$400K per facility; ~$1M-$2M total for 5 critical facilities

---

### 5.3 OT Security Maturity

The following assessment evaluates Cenovus OT security maturity against IEC 62443 Foundational Requirements:

| **IEC 62443 Foundational Requirement** | **Current Maturity Level** | **Target Maturity Level** | **Gap Description** |
|---------------------------------------|---------------------------|--------------------------|---------------------|
| **FR 1: Identification and Authentication Control** | ML 2 (Individual authentication) | ML 3 (Application/Device authentication) | OT device authentication (PLCs, HMIs) not consistently enforced; relies on network segmentation |
| **FR 2: Use Control** | ML 2 (Authorization enforced) | ML 3 (Least Privilege) | Overly permissive OT engineer accounts with broad access; insufficient segregation of duties |
| **FR 3: System Integrity** | ML 1 (Data integrity monitoring) | ML 3 (Change Detection + Prevention) | Limited file integrity monitoring on OT systems; no application whitelisting on industrial controllers |
| **FR 4: Data Confidentiality** | ML 1 (Encryption optional) | ML 2 (Encryption required) | Many legacy industrial protocols transmit data unencrypted (Modbus TCP, DNP3) |
| **FR 5: Restricted Data Flow** | ML 2 (Zone segmentation) | ML 3 (Deep packet inspection) | Network segmentation enforced but no industrial protocol deep packet inspection or anomaly detection |
| **FR 6: Timely Response to Events** | ML 1 (Logging implemented) | ML 3 (Automated response) | OT logs collected at edge but limited correlation and threat detection; no automated OT-aware response |
| **FR 7: Resource Availability** | ML 1 (DoS protection at boundary) | ML 2 (Rate limiting and resource management) | Limited distributed denial-of-service (DDoS) protection for OT DMZ services; no industrial protocol rate limiting |

**Overall OT Security Maturity**: ML 1-2 (Initial to Managed)
**Target OT Security Maturity**: ML 2-3 (Managed to Defined) within 24 months

**Regulatory Drivers**:
- Canadian Energy Regulator (CER) cybersecurity expectations for pipeline operators
- Alberta Energy Regulator (AER) cybersecurity guidelines for upstream facilities
- IEC 62443 industrial automation security standards (increasingly required by insurance providers)

---

### 5.4 Investment Roadmap

The following prioritized roadmap addresses critical OT security gaps over 18-24 months:

| **Priority** | **Initiative** | **Investment** | **Timeline** | **Regulatory/Business Driver** |
|-------------|---------------|---------------|-------------|-------------------------------|
| **P0** | OT Network Monitoring Platform | $400K-$800K | FY2027 Q2-Q3 | IEC 62443-3-3 SR 6.1; detect OT-specific threats; CER expectations |
| **P0** | OT Backup and Disaster Recovery Solution | $300K-$500K | FY2027 Q3-Q4 | IEC 62443-3-3 SR 7.1/7.2; reduce recovery time from days to hours |
| **P1** | OT Asset Discovery and Vulnerability Management | $200K-$400K | FY2027 Q4 | IEC 62443-2-1; complete asset inventory; vulnerability visibility |
| **P1** | OT Incident Response Capability Development | $100K | FY2028 Q1 | Incident readiness; forensic capability for OT environments |
| **P2** | Safety System Security (Unidirectional Gateways) | $200K-$400K/facility | FY2028 Q2-Q4 | IEC 61511; protect SIS from cyber threats; insurance requirements |
| **P2** | OT Patch Management Process Development | $50K | FY2028 Q3 | Reduce vulnerability exposure window; risk-based patching |
| **TOTAL** | | **$1.25M-$2.25M** | **18-24 months** | |

#### Funding Justification

**Critical Infrastructure Protection**: Cenovus operates critical energy infrastructure subject to nation-state cyber threats and sophisticated adversaries targeting oil and gas sector.

**Regulatory Compliance**: Increasing regulatory expectations (CER, AER, IEC 62443) require enhanced OT security controls.

**Operational Resilience**: Investment reduces production downtime risk and accelerates recovery from cyber incidents, protecting revenue and shareholder value.

**Insurance Requirements**: Cyber insurance providers increasingly require documented OT security controls and incident response capabilities as condition of coverage.

**Estimated ROI**: Prevention of single major OT cyber incident (potential $50M-$100M impact from extended production outage) justifies entire investment multiple times over.

---

## 6. TIME Model Analysis

The TIME model categorizes applications into four strategic dispositions: INVEST (strategic growth platforms), TOLERATE (maintain current state), MIGRATE (time-bound transitions), and ELIMINATE (scheduled decommission).

### 6.1 TIME Distribution

| **TIME Disposition** | **Count** | **% of Portfolio** | **Strategic Meaning** |
|---------------------|-----------|-------------------|----------------------|
| **Invest** | 32 | 51% | Strategic growth platforms receiving continued investment and capability expansion |
| **Tolerate** | 26 | 41% | Maintain current state; accept existing capabilities without major new investment |
| **Migrate** | 2 | 3% | Time-bound transition from legacy to modern platforms (RSA to Azure MFA) |
| **Eliminate** | 1 | 2% | Scheduled decommission with user migration to replacement platforms |
| **Unspecified** | 2 | 3% | Require TIME disposition assignment during database cleanup |

### 6.2 INVEST Applications

**Total Count**: 32 applications (51% of portfolio)

**Strategic Focus**: Applications receiving continued investment represent Cenovus's security technology future state, with emphasis on cloud-native security, Zero Trust architecture, automation, and modern EDR platforms.

#### Identity & Access (6 applications)

- Azure Multi-Factor Authentication (MFA) - Modern cloud-native MFA platform
- Azure Self-Service Password Reset - Self-service identity capability
- Microsoft Authenticator - Mobile MFA application
- Entra Private Network Connector - Zero Trust Network Access (ZTNA)
- Global Protect VPN - Strategic VPN platform with MFA integration
- KeePass - Lightweight password management for lab/non-enterprise use

#### Endpoint Security (6 applications)

- CrowdStrike Falcon - Strategic EDR platform (replacing legacy McAfee)
- ForeScout Secure Connector - Network Access Control (NAC) and asset discovery
- Sophos Antivirus (Linux - Red Hat) - Linux endpoint protection (consolidation candidate)
- Symantec Endpoint Protection Control Network - OT-specific endpoint protection
- System Center Endpoint Protection - Windows Server protection

#### Detection & Response (8 applications)

- Splunk - Strategic SIEM platform for IT, cloud, and OT edge
- Cribl - Log optimization and routing enabling SIEM efficiency
- Proofpoint - Advanced email threat protection
- Proofpoint Audit - Email investigation and compliance
- Proofpoint Security Awareness Training - Phishing simulation and training
- SPAM Digest - User-facing spam quarantine management
- Palo Alto Cortex XSOAR - Security Orchestration, Automation, and Response (SOAR)
- Panorama - Centralized firewall management

#### Cloud & Data Security (4 applications)

- Azure Information Protection (AIP) - Data classification and rights management
- Microsoft Cloud App Security - Cloud Access Security Broker (CASB)
- Microsoft Office 365 Security & Compliance Console - M365 DLP and compliance

#### Training & Awareness (2 applications)

- Immersive Lab - Hands-on security skills training for SOC analysts and incident responders

#### Strategic Investment Themes

1. **Cloud-First Security**: Heavy investment in Azure/M365 security stack (AIP, Cloud App Security, O365 Security Console, Azure MFA) aligns with enterprise cloud migration strategy.

2. **Zero Trust Architecture**: Entra Private Network Connector, Azure MFA, and ForeScout support Zero Trust security model transition from traditional perimeter-based security.

3. **Security Automation**: Cortex XSOAR and Cribl represent investment in security operations automation, reducing manual analyst workload and improving response speed.

4. **Modern EDR**: CrowdStrike Falcon represents shift from signature-based antivirus to behavioral detection and response, enabling proactive threat hunting.

**Investment Priority**: Continue capability expansion, integrate platforms, automate workflows, and enhance threat detection/response capabilities.

---

### 6.3 TOLERATE Applications

**Total Count**: 26 applications (41% of portfolio)

**Strategic Interpretation**: TOLERATE applications remain operational and supported but are not primary investment focus. Many represent legacy technologies maintained during transitions to strategic platforms or specialized tools serving niche requirements.

**IMPORTANT**: TOLERATE does not mean "ignore" - these applications require ongoing support, patching, and operational maintenance. However, they are candidates for rationalization or eventual retirement as strategic platforms mature.

#### Legacy Endpoint Protection (9 applications)

- McAfee ePolicy Orchestrator Corp (consolidation candidate - migrate to CrowdStrike)
- McAfee Management (ePO Corp) [duplicate entry]
- McAfee Move (virtualized AV - consolidation candidate)
- McAfee ePolicy Orchestrator PCI (consolidation candidate after PCI validation)
- McAfee Management (ePO PCI) [duplicate entry]
- McAfee PCI (consolidation candidate)
- Bit9 - Downstream (retail application whitelisting)
- Bit9 Parity (downstream application control)
- Keeper (enterprise password manager - potential PAM replacement candidate)

#### Legacy Authentication (2 applications)

- Duo Security (Cisco) - legacy MFA for shared services (Azure MFA migration candidate)
- NPS Server - RADIUS MFA enforcement (integrated with Azure MFA)

#### OT/ICS Specialized (3 applications)

- ICS Access - OT remote access (jump host for vendor/engineer access)
- Symantec End-point Protection Management Server - OT antivirus management
- CLAM - Open source Linux antivirus (consolidation candidate - CrowdStrike Linux)

#### Detection & Monitoring (5 applications)

- Endace - Full packet capture for forensic investigations (specialized use case)
- Splunk (China) - Regional SIEM for China compliance (consolidation candidate)
- HTTPWatch - Web traffic troubleshooting tool for incident investigations
- Windows Event Collector - Windows log collection feeding Splunk

#### Network Security (2 applications)

- Sourcefire Appliance - IPS/IDS network threat detection (aging platform)
- Qualys - Vulnerability scanning (limited OT support)

#### Other (4 applications)

- DataMotion Secure Email - Encrypted external email communications
- ServiceNow IT Applications - Custom security control tracking application
- TripWire Enterprise - File integrity monitoring (SOX control)
- Tripwire Enterprise Client - FIM agent deployment

#### Rationalization Opportunity

Many TOLERATE applications are candidates for consolidation identified in Section 4:
- 9 endpoint protection products (McAfee, Bit9, CLAM) consolidate to CrowdStrike
- 2 MFA platforms (Duo, NPS) potentially consolidate to Azure MFA
- 1 SIEM instance (Splunk China) potentially consolidate to primary Splunk

**Investment Priority**: Minimal new investment. Evaluate for consolidation or retirement as strategic platforms mature. Maintain operational support and patching.

---

### 6.4 MIGRATE Applications

**Total Count**: 2 applications (3% of portfolio)

**Definition**: Legacy platforms with active, time-bound replacement projects in progress.

#### RSA Authentication Suite Migration

**1. RSA - Authentication Manager**

**Current Status**: MIGRATE to Azure MFA / Entra ID (85% complete)

**Migration Timeline**: FY2027 Q1 completion (target June 2027)

**Replacement Platform**: Azure Multi-Factor Authentication + Yubikeys

**Migration Progress**: 85% of RSA users migrated. Final users (likely network equipment, legacy applications with RSA integration) require remediation before infrastructure retirement.

**Retirement Date**: Target June 2027

**Annual Cost Savings**: $150K (RSA licensing + maintenance)

---

**2. RSA - SecurID**

**Current Status**: MIGRATE to Azure MFA / Yubikeys (85% complete)

**Migration Timeline**: FY2027 Q1 completion (target June 2027)

**Replacement**:
- Azure MFA with software tokens for standard users
- Yubikeys (FIDO2 hardware tokens) for privileged users and OT engineers requiring phishing-resistant authentication

**Migration Progress**: 85% complete; final hardware token users being transitioned to Yubikeys

**Retirement Date**: Target June 2027

---

#### Strategic Significance

RSA retirement represents significant security architecture modernization:
- Eliminates legacy on-premises authentication infrastructure
- Shifts to cloud-native, mobile-first authentication model
- Enables passwordless authentication capability via FIDO2/Yubikeys
- Reduces annual licensing costs ($150K)
- Improves user experience with modern mobile authenticator

**Critical Action**: Ensure all RSA-integrated systems (network equipment, legacy applications, OT access control systems) have alternative authentication mechanisms validated before June 2027 infrastructure retirement.

---

### 6.5 ELIMINATE Applications

**Total Count**: 1 application (2% of portfolio)

**Definition**: Legacy platforms scheduled for decommission with user migration to replacement platforms.

#### myvpn.cenovus.com - Legacy VPN

**Current Status**: ELIMINATE (user migration 70% complete)

**Elimination Timeline**: FY2027 Q2 (target September 2027)

**Replacement Platforms**:
- Global Protect VPN (Palo Alto) for users requiring network-level access
- Entra Private Network Connector (Zero Trust Network Access) for application-specific access where feasible

**Migration Status**: 70% of users migrated to Global Protect or Entra Private Network Connector. Remaining 30% require application assessment for optimal access method.

**Decommission Date**: Target September 2027

**Annual Cost Savings**: $50K (infrastructure, licensing, support)

#### Elimination Drivers

**Outdated Technology**: Legacy VPN lacks modern security features including:
- No endpoint posture checking (device health validation before network access)
- No per-application access control (broad network access vs. least-privilege)
- No integration with modern identity platforms (Azure AD/Entra ID)

**Duplicate Functionality**: Global Protect provides superior capabilities with MFA integration and endpoint compliance enforcement.

**Zero Trust Strategy**: Enterprise architecture direction favors application-level access (Entra Private Network Connector) over network-level access, reducing attack surface and improving security posture.

---

### 6.6 Strategic Insights

#### 1. Cloud Transformation Momentum

**Observation**: 51% of applications in INVEST category are concentrated in cloud-native security platforms (Azure/M365 security stack).

**Interpretation**: Successful cloud security transformation is underway, with strategic commitment to Microsoft security ecosystem.

**Recommendation**: Continue momentum. Integrate Azure security telemetry with Splunk SIEM and Cortex XSOAR for unified visibility.

---

#### 2. Legacy Technical Debt

**Observation**: 41% TOLERATE applications represent technical debt requiring rationalization roadmap.

**Interpretation**: Significant opportunity to reduce complexity, cost, and operational burden through consolidation.

**Recommendation**: Execute rationalization initiatives in Section 4, targeting $880K-$1.08M annual savings over 18-24 months.

---

#### 3. Active Transition Progress

**Observation**: Only 3% MIGRATE/ELIMINATE indicates most major legacy retirements already completed or consolidated into TOLERATE holding pattern.

**Interpretation**: RSA and legacy VPN represent final major legacy platform eliminations currently in progress. Most other legacy tools consolidated into TOLERATE category awaiting strategic platform maturity.

**Recommendation**: Complete RSA and legacy VPN migrations on schedule (June/September 2027) to close remaining legacy infrastructure gaps.

---

#### 4. OT Investment Gap

**Observation**: Limited OT-specific applications in INVEST category despite critical infrastructure risk and regulatory requirements.

**Interpretation**: OT security investment has not kept pace with IT security investment. Current OT security posture (ML 1-2) below industry best practice and regulatory expectations.

**Recommendation**: Rebalance investment toward OT security capabilities (network monitoring, backup/DR, asset discovery) per Section 5 roadmap ($1.25M-$2.25M over 18-24 months).

---

#### 5. Cost Optimization Opportunity

**Observation**: High TOLERATE application count (26 applications, 41%) presents substantial consolidation opportunity.

**Interpretation**: Rationalization of endpoint protection (11 products), MFA platforms (3 products), and SIEM instances (3 deployments) could yield $880K-$1.08M annual savings.

**Recommendation**: Execute phased consolidation per Section 4 over 18-24 months. Reinvest savings into RECOVER function gaps and OT security capabilities.

---

## 7. Prioritized Recommendations

This section provides actionable recommendations prioritized by urgency and risk impact. All recommendations include investment estimates, timelines, and success metrics.

### 7.1 Priority 0: Critical (Address Immediately - 0-6 Months)

**Priority 0 recommendations address critical capability gaps with immediate business risk or active migration projects requiring completion.**

---

#### Recommendation P0-1: Invest in Cyber Recovery Capability

**NIST Function**: RECOVER

**Issue**: Only 4 applications support RECOVER function. No dedicated cyber disaster recovery orchestration platform or immutable backup validation capability. Current state creates unacceptable risk for critical oil and gas infrastructure.

**Business Risk**:
- Extended production downtime following ransomware or destructive malware attack
- Potential days-to-weeks recovery time vs. hours with proper tooling
- Revenue impact: $5M-$15M per day for major facility outages
- Regulatory compliance gap: SOX business continuity requirements, IEC 62443-3-3 SR 7.1/7.2

**Actions Required**:

1. **Procure and Deploy Cyber Recovery Orchestration Platform**
   - Evaluate and select solution (e.g., Zerto Cyber Resilience, Commvault Disaster Recovery, Rubrik Cyber Recovery)
   - Implement recovery orchestration with automated runbooks

2. **Implement Immutable Backup Validation**
   - Deploy immutable backup storage for critical systems (Active Directory, PAM, SIEM, OT historians)
   - Automate backup validation and recovery testing

3. **Develop OT System Restoration Runbooks**
   - Document recovery procedures for PLC logic, HMI screens, DCS configurations
   - Test restoration procedures in non-production OT environments

**Investment Required**: $500K-$800K (platform + implementation)

**Staffing**: 1 FTE (Disaster Recovery Specialist)

**Timeline**: 6 months to operational capability

**Success Metrics**:
- Recovery Time Objective (RTO) < 24 hours for critical IT systems
- RTO < 72 hours for OT systems
- Quarterly disaster recovery testing with documented results
- Immutable backups validated weekly

**Priority Justification**: Single ransomware incident could result in $50M-$100M revenue impact from extended outage. Investment pays for itself multiple times over by preventing one major incident.

---

#### Recommendation P0-2: Deploy OT Network Monitoring Platform

**NIST Function**: DETECT

**Issue**: No visibility into industrial protocol traffic (Modbus, DNP3, OPC UA/DA, EtherNet/IP). Cannot detect OT-specific attack patterns such as PLC manipulation, safety system compromise, or process setpoint tampering.

**Business Risk**:
- Undetected OT cyber attacks could cause production disruption or safety events
- Upstream SAGD facility compromise could halt production
- Downstream refinery DCS compromise could cause safety incidents
- Regulatory non-compliance: IEC 62443-3-3 SR 6.1, CER cybersecurity expectations

**Actions Required**:

1. **Deploy OT Network Monitoring Solution**
   - Evaluate and select platform with industrial protocol dissection (e.g., Nozomi Networks, Claroty, Dragos)
   - Deploy sensors at IT/OT boundaries and within Level 2-3 OT zones
   - Implement physics-based anomaly detection for process control systems

2. **Integrate with SIEM and SOAR**
   - Configure OT alert forwarding to Splunk SIEM for unified visibility
   - Develop Cortex XSOAR playbooks for OT incident response

3. **Enhance SOC Capability**
   - Hire or train 2 FTE SOC analysts with OT security expertise (SANS ICS training)
   - Develop OT-specific detection use cases and alert rules

**Investment Required**: $400K-$800K (platform) + $300K annually (staffing)

**Timeline**: 6 months to pilot; 12 months to full deployment across all facilities

**Success Metrics**:
- 100% visibility into Level 2-3 OT network traffic across all facilities
- Mean Time to Detect (MTTD) < 30 minutes for OT anomalies
- 95% industrial protocol decoding accuracy
- 2 FTE OT-trained SOC analysts operational

**Regulatory Driver**: IEC 62443-3-3 SR 6.1 (Audit Log Accessibility), Canadian Energy Regulator (CER) cybersecurity expectations for pipeline operators

**Priority Justification**: OT-specific attacks (e.g., Triton/Trisis targeting safety systems, Industroyer targeting power grids) demonstrate critical need for industrial protocol visibility. Current blind spot creates unacceptable safety and operational risk.

---

#### Recommendation P0-3: Complete RSA Authentication Manager Retirement

**NIST Function**: PROTECT

**Issue**: RSA migration 85% complete. Final users blocking infrastructure retirement, resulting in ongoing licensing costs ($150K/year) and security risk from legacy on-premises authentication platform.

**Business Risk**:
- Ongoing annual licensing costs ($150K)
- Security risk from legacy authentication infrastructure
- Technical debt accumulation if retirement delayed

**Actions Required**:

1. **Identify and Migrate Final RSA Users**
   - Inventory remaining RSA-integrated systems (likely network equipment, legacy applications)
   - Validate alternative authentication mechanisms (Azure MFA via NPS Server, Yubikeys)

2. **Provide Hardware Tokens for Privileged Users**
   - Procure and distribute Yubikeys for users requiring hardware token MFA
   - Configure Azure MFA FIDO2 integration

3. **Decommission RSA Infrastructure**
   - Power down RSA Authentication Manager servers by June 2027
   - Remove RSA software from remaining client systems

**Investment Required**: $30K (Yubikeys, migration labor)

**Timeline**: 3 months

**Target Completion**: June 2027

**Success Metrics**:
- Zero RSA authentication events by June 2027
- RSA infrastructure decommissioned and removed from inventory
- $150K annual licensing costs eliminated

**Priority Justification**: Migration 85% complete - final push required to realize cost savings and eliminate legacy infrastructure security risk.

---

### 7.2 Priority 1: High (Address Within 6-12 Months)

**Priority 1 recommendations address significant capability gaps and rationalization opportunities with high ROI.**

---

#### Recommendation P1-4: Execute Endpoint Protection Consolidation

**NIST Function**: PROTECT

**Issue**: 11 separate antivirus/EDR solutions creating operational complexity, high licensing costs, and inconsistent security posture across environments.

**Actions Required**:

**Phase 1: Corporate Consolidation** (FY2027 Q1-Q2)
- Complete McAfee ePO Corp to CrowdStrike Falcon migration for all corporate Windows/Mac endpoints
- Retire McAfee Corporate, McAfee ePO Corp, McAfee Move
- **Products Eliminated**: 3

**Phase 2: Linux Standardization** (FY2027 Q3)
- Standardize on CrowdStrike Falcon for Linux (RHEL support validated)
- Retire Sophos Antivirus, CLAM
- **Products Eliminated**: 2

**Phase 3: PCI Rationalization** (FY2027 Q4)
- Migrate PCI environment to CrowdStrike after PCI-DSS compliance validation with QSA
- Retire McAfee ePO PCI, McAfee PCI
- **Products Eliminated**: 2

**Investment Required**: Neutral (CrowdStrike licensing expansion offset by McAfee/Sophos retirement)

**Timeline**: 12 months for Phases 1-3

**Annual Cost Savings**: $400K-$600K (McAfee, Symantec, Sophos licensing eliminated)

**Success Metrics**:
- < 5 endpoint protection products by end of FY2027
- 100% corporate endpoints on CrowdStrike Falcon
- PCI-DSS compliance validated for CrowdStrike deployment
- Unified threat hunting across all environments

**Priority Justification**: Single pane of glass for endpoint visibility dramatically improves incident response speed and threat hunting capability while generating significant cost savings.

---

#### Recommendation P1-5: Deploy OT Asset Discovery and Vulnerability Management

**NIST Function**: IDENTIFY

**Issue**: Incomplete OT asset inventory. Cannot assess vulnerability exposure for PLCs, RTUs, DCS controllers, and field devices. Slow incident response due to unknown device population.

**Actions Required**:

1. **Deploy Passive OT Asset Discovery**
   - Implement industrial protocol-based passive discovery (no active scanning to avoid operational disruption)
   - Platform options: Claroty Continuous Threat Detection, Armis, or integrated with OT monitoring platform from P0-2

2. **Integrate with CMDB**
   - Configure bidirectional integration between OT asset discovery and ServiceNow CMDB
   - Maintain unified asset inventory across IT and OT environments

3. **Establish OT Vulnerability Management Process**
   - Implement risk-based vulnerability prioritization for OT devices
   - Develop virtual patching strategy (IPS signatures) for vulnerabilities that cannot be patched during production
   - Coordinate patching with planned turnaround schedules

**Investment Required**: $200K-$400K (platform + CMDB integration)

**Timeline**: 6-9 months

**Success Metrics**:
- 95% OT asset discovery accuracy (validated against manual inventory)
- OT vulnerability dashboard operational in Splunk
- Risk-based OT vulnerability management process documented and implemented
- Mean Time to Inventory (MTTI) < 24 hours for new OT devices

**Regulatory Driver**: IEC 62443-2-1 (Security Program Requirements) mandates comprehensive OT asset inventory

**Priority Justification**: Cannot protect or respond to threats affecting unknown assets. OT asset inventory is foundational requirement for all other OT security capabilities.

---

#### Recommendation P1-6: Implement OT Backup and Disaster Recovery

**NIST Function**: RECOVER

**Issue**: No automated OT configuration backup. Recovery from cyber incident requires manual PLC reprogramming, potentially taking days-to-weeks.

**Actions Required**:

1. **Deploy OT Backup Solution**
   - Evaluate and select OT-specific backup platform (e.g., Radiflow, Veeam for OT, Veritas OT Backup)
   - Implement automated extraction of:
     - PLC ladder logic and function blocks
     - DCS control strategies and regulatory loops
     - HMI screens and operator interfaces
     - SCADA configuration databases

2. **Implement Configuration Versioning**
   - Maintain version history of all OT configurations
   - Track changes with approval workflow (change management integration)

3. **Develop and Test Restoration Runbooks**
   - Document restoration procedures for each OT system type
   - Conduct quarterly restoration testing in non-production environments
   - Train OT engineering staff on restoration procedures

**Investment Required**: $300K-$500K (platform + runbook development)

**Timeline**: 9-12 months

**Success Metrics**:
- Weekly automated backups of all critical OT systems
- Successful restoration test within 72 hours (validated quarterly)
- Recovery runbooks documented for 100% of critical OT systems
- Mean Time to Restore (MTTR) < 72 hours for OT systems

**Regulatory Driver**: IEC 62443-3-3 SR 7.1 (Backup) and SR 7.2 (Recovery and Reconstitution)

**Priority Justification**: Production downtime costs $5M-$15M per day. Automated backup and restoration capabilities reduce recovery time from weeks to days/hours, directly protecting revenue.

---

#### Recommendation P1-7: Consolidate MFA Platforms

**NIST Function**: PROTECT

**Issue**: Three separate MFA platforms (Azure MFA, Duo, RSA) creating user confusion, administrative overhead, and excessive licensing costs.

**Actions Required**:

**Phase 1: RSA Retirement** (covered in P0-3)

**Phase 2: Duo Migration Assessment** (FY2027 Q2)
- Inventory Duo use cases (likely network equipment, legacy RADIUS clients)
- Migrate to Azure MFA via NPS Server where technically feasible
- Retain Duo only if technical blockers exist for specific legacy systems

**Phase 3: Standardize on Yubikeys** (FY2027 Q3)
- Yubikeys as sole hardware token standard for privileged users and OT engineers
- Ensure Azure MFA + Yubikey FIDO2 integration for phishing-resistant authentication

**Investment Required**: $50K (migration labor, Yubikeys)

**Timeline**: 9 months (dependent on RSA completion)

**Annual Cost Savings**: $230K ($150K RSA + $80K Duo licensing)

**Success Metrics**:
- < 2 MFA platforms (Azure MFA + Yubikeys only)
- 100% privileged users on phishing-resistant authentication (Yubikeys)
- User satisfaction score > 85% (simplified authentication experience)

**Priority Justification**: Simplified authentication experience improves user productivity while generating substantial cost savings ($230K annually).

---

### 7.3 Priority 2: Medium (Address Within 12-18 Months)

**Priority 2 recommendations enhance security capabilities and reduce operational complexity with moderate risk impact.**

---

#### Recommendation P2-8: Evaluate SIEM Instance Consolidation

**NIST Function**: DETECT

**Issue**: Three Splunk instances (Corporate, China, PCI) creating data silos, increased licensing costs, and operational complexity.

**Actions Required**:

1. **Compliance Validation** (FY2027 Q3)
   - Engage Qualified Security Assessor (QSA) for PCI-DSS 12.3.8 validation of index-based logical segregation
   - Engage legal counsel for China data sovereignty validation of Cribl-enforced data residency controls

2. **If Approved: Consolidate to Federated Splunk** (FY2027 Q4)
   - Consolidate Splunk PCI and Splunk China into primary Splunk deployment
   - Configure index-level access controls for PCI and China data segregation
   - Deploy Cribl as universal log router enforcing compliance boundaries

3. **If Not Approved: Enhance Cross-Instance Correlation**
   - Implement Cortex XSOAR federation across three Splunk instances
   - Enable cross-instance threat correlation via SOAR platform

**Investment Required**: $100K (compliance consulting, configuration, testing)

**Timeline**: 12-15 months (includes compliance validation phase)

**Annual Cost Savings**: $200K (if consolidation approved via licensing volume discounts)

**Success Metrics**:
- Single SIEM instance operational (Option A) OR federated cross-instance correlation via XSOAR (Option B)
- 100% PCI compliance maintained (validated by QSA)
- China data residency compliance maintained (validated by legal)
- Unified threat hunting across all environments

**Priority Justification**: Potential for significant cost savings ($200K annually) and operational efficiency. However, dependent on compliance validation - if consolidation not approved, accept status quo with enhanced correlation.

---

#### Recommendation P2-9: Implement Privileged Access Management (PAM)

**NIST Function**: PROTECT

**Issue**: Keeper password manager provides vault sharing but lacks privileged session recording and just-in-time access provisioning. Potential SOX control weakness.

**Actions Required**:

1. **Procure and Deploy Enterprise PAM Solution**
   - Evaluate and select platform (e.g., CyberArk, BeyondTrust)
   - Implement privileged credential vaulting with automatic rotation

2. **Implement Session Recording**
   - Enable privileged session recording for IT and OT environments
   - Retain session recordings per compliance requirements (SOX, PCI-DSS)

3. **Enable Just-in-Time Access**
   - Implement approval workflows for temporary privileged access
   - Automatic privilege revocation after time window expiration

**Investment Required**: $300K-$500K (platform + integration with Active Directory, OT access control systems)

**Timeline**: 12-18 months

**Success Metrics**:
- 100% privileged sessions recorded
- SOX compliance attestation for privileged account controls
- Just-in-time access operational for 100% of privileged accounts
- Mean Time to Provision (MTTP) < 30 minutes for approved privileged access requests

**Priority Justification**: Addresses SOX control gap for shared administrative accounts. Improves security posture through comprehensive privileged session oversight.

---

#### Recommendation P2-10: Complete Legacy VPN Elimination

**NIST Function**: PROTECT

**Issue**: myvpn.cenovus.com legacy VPN still operational (ELIMINATE status). Ongoing security risk and cost.

**Actions Required**:

1. **Complete User Migration**
   - Migrate remaining 30% of users to Global Protect VPN or Entra Private Network Connector
   - Assess each user for optimal access method (network-level vs. application-level)

2. **Decommission Infrastructure**
   - Power down legacy VPN infrastructure by September 2027
   - Remove from network and asset inventory

**Investment Required**: $20K (migration labor)

**Timeline**: 6 months

**Target Completion**: September 2027

**Annual Cost Savings**: $50K (infrastructure, licensing, support)

**Success Metrics**:
- Zero active connections to myvpn.cenovus.com
- Infrastructure decommissioned by September 2027
- 100% users migrated to Global Protect or Entra Private Network Connector

**Priority Justification**: Final legacy infrastructure elimination. Modernizes remote access architecture with Zero Trust principles.

---

#### Recommendation P2-11: Enhance OT Incident Response Capability

**NIST Function**: RESPOND

**Issue**: Axiom Cyber provides IT forensics. No OT-specific forensic capability for industrial protocol analysis or PLC forensics.

**Actions Required**:

1. **Train Incident Response Team**
   - Send 2-3 IR team members to SANS ICS515 (ICS Visibility, Detection, and Response) or equivalent
   - Obtain specialized OT incident response training

2. **Acquire OT Forensic Tools**
   - PLC memory dump analysis tools
   - Industrial protocol PCAP analysis capability
   - OT-specific forensic toolkits

3. **Develop OT Incident Response Playbooks**
   - Document OT-specific IR procedures in Cortex XSOAR
   - Integrate with OT network monitoring platform (P0-2)
   - Conduct tabletop exercise validating OT IR playbooks

**Investment Required**: $100K (training + tools)

**Timeline**: 12 months

**Success Metrics**:
- IR team capable of performing OT forensics (validated via tabletop exercise)
- OT incident response playbooks documented and tested
- Mean Time to Investigate (MTTI) < 4 hours for OT security incidents

**Priority Justification**: Cannot effectively respond to OT cyber incidents without OT-specific forensic capability. Completes end-to-end OT security capability (detect via P0-2, respond via P2-11, recover via P1-6).

---

### 7.4 Priority 3: Low (Address Within 18-24 Months)

**Priority 3 recommendations provide incremental security improvements with lower risk impact.**

---

#### Recommendation P3-12: Deploy Supply Chain Risk Management Capability

**NIST Function**: IDENTIFY

**Issue**: No tooling for Software Bill of Materials (SBOM) analysis or third-party software risk assessment.

**Actions Required**:

1. **Evaluate and Deploy Supply Chain Security Platform**
   - Assess options: Black Duck, Sonatype, Snyk
   - Integrate with development pipeline for continuous SBOM generation

2. **Establish Vendor Risk Assessment Process**
   - Implement OT vendor risk scoring (particularly for control system vendors)
   - Track third-party software vulnerabilities and end-of-life status

**Investment Required**: $150K-$250K

**Timeline**: 18 months

**Success Metrics**:
- SBOM generated for 100% of custom applications
- Vendor risk scoring operational for OT vendors
- Automated alerts for third-party vulnerabilities in production applications

---

#### Recommendation P3-13: Expand Cloud Security Posture Management (CSPM)

**NIST Function**: PROTECT

**Issue**: Prisma Cloud provides code security. Limited runtime cloud configuration monitoring and compliance validation.

**Actions Required**:

1. **Expand Prisma Cloud CSPM Module**
   - OR evaluate Microsoft Defender for Cloud CSPM features

2. **Implement Continuous Compliance Monitoring**
   - Configure CIS Azure benchmark compliance monitoring
   - Integrate CSPM alerts with Cortex XSOAR for automated remediation

**Investment Required**: $50K-$100K (licensing expansion)

**Timeline**: 12 months

**Success Metrics**:
- 100% Azure subscriptions monitored for misconfigurations
- Automated remediation for high-risk misconfigurations
- CIS Azure benchmark compliance > 95%

---

#### Recommendation P3-14: Implement Safety System Security Controls

**NIST Function**: PROTECT (OT)

**Issue**: Safety Instrumented Systems (SIS) lack cyber security isolation and monitoring. Safety system compromise could result in catastrophic safety events.

**Actions Required**:

1. **Deploy Unidirectional Gateways**
   - Install data diodes (e.g., Waterfall Security, Owl Cyber Defense) between SIS and DCS networks
   - Prioritize critical facilities: SAGD production facilities, refineries with high consequence of failure

2. **Implement SIS-Specific Monitoring**
   - Deploy change detection for SIS configurations
   - Alert on unauthorized SIS programming or configuration changes

**Investment Required**: $200K-$400K per facility; $1M-$2M total for 5 critical facilities

**Timeline**: 24 months (phased by facility criticality)

**Success Metrics**:
- Unidirectional gateways deployed at 5 critical facilities
- SIS change detection operational
- Zero unauthorized SIS configuration changes detected

**Regulatory Driver**: IEC 61511 (Functional Safety) + IEC 62443 (Cybersecurity) convergence

---

#### Recommendation P3-15: Develop Security Metrics and Reporting Dashboard

**NIST Function**: ALL

**Issue**: Limited executive visibility into security posture and program effectiveness.

**Actions Required**:

1. **Develop CISO Dashboard**
   - Implement in PowerBI or Splunk Dashboard Studio
   - Integrate metrics from all security tools (CrowdStrike, Splunk, Proofpoint, etc.)

2. **Implement KRIs and KPIs**
   - Key Risk Indicators (KRIs) aligned to NIST CSF
   - Key Performance Indicators (KPIs) for security operations effectiveness

3. **Automate Board Reporting**
   - Monthly security posture report to executive leadership
   - Quarterly Board of Directors cybersecurity briefing

**Investment Required**: $50K (development, integration, training)

**Timeline**: 12 months

**Success Metrics**:
- Executive dashboard operational with real-time data
- Monthly automated security posture reporting established
- Board cybersecurity briefing materials standardized

---

### 7.5 Investment Summary

The following table summarizes all recommendations with investment requirements, savings potential, and timelines:

| **Priority** | **Recommendation** | **NIST Function** | **Investment** | **Annual Savings** | **Timeline** | **Complexity** |
|-------------|-------------------|------------------|---------------|-------------------|--------------|----------------|
| **P0-1** | Cyber Recovery Capability | RECOVER | $500K-$800K | - | 6 months | HIGH |
| **P0-2** | OT Network Monitoring | DETECT | $400K-$800K | - | 6-12 months | HIGH |
| **P0-3** | RSA Retirement | PROTECT | $30K | $150K/year | 3 months | LOW |
| **P1-4** | Endpoint Consolidation | PROTECT | Neutral | $400K-$600K/year | 12 months | HIGH |
| **P1-5** | OT Asset Discovery | IDENTIFY | $200K-$400K | - | 6-9 months | MEDIUM |
| **P1-6** | OT Backup/DR | RECOVER | $300K-$500K | - | 9-12 months | HIGH |
| **P1-7** | MFA Consolidation | PROTECT | $50K | $230K/year | 9 months | MEDIUM |
| **P2-8** | SIEM Consolidation | DETECT | $100K | $200K/year* | 12-15 months | HIGH |
| **P2-9** | PAM Implementation | PROTECT | $300K-$500K | - | 12-18 months | HIGH |
| **P2-10** | Legacy VPN Elimination | PROTECT | $20K | $50K/year | 6 months | LOW |
| **P2-11** | OT Incident Response | RESPOND | $100K | - | 12 months | MEDIUM |
| **P3-12** | Supply Chain Risk Mgmt | IDENTIFY | $150K-$250K | - | 18 months | MEDIUM |
| **P3-13** | CSPM Expansion | PROTECT | $50K-$100K | - | 12 months | LOW |
| **P3-14** | Safety System Security | PROTECT | $1M-$2M | - | 24 months | HIGH |
| **P3-15** | Security Metrics Dashboard | ALL | $50K | - | 12 months | LOW |
| **TOTAL** | | | **$3.25M-$6.4M** | **$1.03M-$1.18M/year** | **24 months** | |

*SIEM consolidation savings contingent on compliance approval

#### Financial Analysis

**Total Investment Required**: $3.25M - $6.4M over 24 months

**Annual Recurring Savings**: $1.03M - $1.18M per year (from rationalization initiatives)

**Net Investment** (after Year 1 savings): $2.2M - $5.2M over 24 months

**3-Year Total Cost of Ownership**:
- Year 1: $3.25M-$6.4M investment - $1.03M-$1.18M savings = $2.1M-$5.2M net
- Year 2-3: Ongoing savings of $1.03M-$1.18M annually
- 3-Year Net: $0M-$2.9M (near breakeven to positive ROI)

**Intangible Benefits Not Quantified**:
- Avoided incident costs (single major OT incident could cost $50M-$100M in lost production)
- Regulatory compliance (avoiding CER/AER enforcement actions)
- Insurance premium reduction (cyber insurance increasingly requires documented OT security controls)
- Operational efficiency (simplified SOC operations, faster incident response)

**Conclusion**: Investment generates positive 3-year ROI when avoided incident costs and intangible benefits are included.

---

## 8. Appendix: Full Application Mapping

### 8.1 Complete Mapping Table

The following table provides comprehensive mapping of all 63 security applications to NIST CSF functions, business categories, criticality levels, and TIME dispositions:

| **#** | **Application Name** | **NIST Function(s)** | **Business Category** | **Criticality** | **TIME** | **Key Notes** |
|-------|---------------------|---------------------|----------------------|----------------|----------|---------------|
| 1 | Axiom Cyber | RESPOND | Corporate | Low | Invest | Digital forensics investigation; IT-focused; OT forensics gap identified |
| 2 | Azure Information Protection (AIP) | PROTECT | Cyber Sec Ops | Low | Invest | Data classification and rights management; DLP integration with O365 |
| 3 | Azure Multi-Factor Authentication (MFA) | PROTECT | Cyber Sec Ops | High | Invest | Strategic MFA platform; replacing RSA SecurID; cloud-native |
| 4 | Azure Self-Service Password Reset | PROTECT | Cyber Sec Ops | Low | Invest | Reduces help desk load; user experience improvement |
| 5 | Bit9 - Downstream | PROTECT | Downstream | Medium | Tolerate | Application whitelisting retail; consolidation candidate (Phase 4) |
| 6 | Bit9 Parity | PROTECT | Cyber Sec Ops | Medium | Tolerate | Application control retail POS; consolidation candidate (Phase 4) |
| 7 | CLAM | PROTECT | Cyber Sec Ops | Low | Tolerate | Open source Linux AV; consolidation candidate (Phase 2 - migrate to CrowdStrike) |
| 8 | Control Network - Access Control Server | IDENTIFY, PROTECT | Cyber Sec Ops | Medium | Unspecified | OT access control; critical for IT/OT segmentation boundary |
| 9 | Cribl | DETECT | Cyber Sec Ops | Low | Invest | Log optimization and routing; enables SIEM consolidation strategy |
| 10 | CrowdStrike Falcon | PROTECT, DETECT, RESPOND | Cyber Sec Ops | Medium | Invest | Strategic EDR platform; replace McAfee/Symantec (Corporate) |
| 11 | DataMotion Secure Email | PROTECT | Corporate | Low | Tolerate | Encrypted email for external communications with sensitive data |
| 12 | Duo Security (Cisco) | PROTECT | Shared Services | Low | Tolerate | Legacy MFA; evaluate for Azure MFA migration (Phase 2) |
| 13 | Endace | DETECT | Cyber Sec Ops | Low | Tolerate | Full packet capture for forensics; specialized use case |
| 14 | Entra Private Network Connector | PROTECT | Cyber Sec Ops | Low | Invest | Zero Trust Network Access (ZTNA); strategic direction |
| 15 | Ericom AccessNow | PROTECT | Cyber Sec Ops | Low | Unspecified | HTML5 gateway for Juniper; evaluate for ZTNA migration |
| 16 | External Dynamic List | PROTECT | Cyber Sec Ops | Low | Unspecified | Dynamic firewall updates from threat intel; integrated with Panorama |
| 17 | Falcon | PROTECT, DETECT, RESPOND | Cyber Sec Ops | Low | Invest | **DUPLICATE of CrowdStrike Falcon (ID 10)** - consolidate in database |
| 18 | ForeScout Secure Connector | IDENTIFY, PROTECT, DETECT | Cyber Sec Ops | Low | Invest | Network Access Control (NAC); asset discovery + compliance enforcement |
| 19 | Global Protect VPN | PROTECT | Cyber Sec Ops | Medium | Invest | Strategic VPN platform; replacing myvpn.cenovus.com; MFA integrated |
| 20 | HTTPWatch | RESPOND | Cyber Sec Ops | Low | Tolerate | Web traffic troubleshooting for investigations; niche tool |
| 21 | ICS Access | PROTECT | Cyber Sec Ops | Low | Tolerate | OT remote access with jump host; critical for vendor/engineer access |
| 22 | Immersive Lab | PROTECT | Corporate | Low | Invest | Hands-on security training; IR preparedness; SOC analyst skills |
| 23 | KeePass | PROTECT | Corporate | Low | Invest | Open source password manager; lab/non-enterprise use |
| 24 | Keeper | PROTECT | Corporate | Medium | Tolerate | Enterprise password manager; evaluate for PAM replacement |
| 25 | McAfee Management (ePO Corp) | PROTECT | Cyber Sec Ops | Medium | Tolerate | **DUPLICATE of McAfee ePO Corp (ID 30)** - consolidate in database |
| 26 | McAfee Management (ePO PCI) | PROTECT | Shared Services | Medium | Tolerate | **DUPLICATE of McAfee ePO PCI (ID 31)** - consolidate in database |
| 27 | McAfee Move | PROTECT | Cyber Sec Ops | Medium | Tolerate | Virtualized AV; consolidation candidate (Phase 1 - migrate to CrowdStrike) |
| 28 | McAfee PCI | PROTECT | Shared Services | Medium | Tolerate | PCI antivirus; migrate to CrowdStrike after PCI validation (Phase 3) |
| 29 | McAfee ePolicy Orchestrator (Lima) | PROTECT | Shared Services | Medium | Unspecified | Lima refinery antivirus; OT-adjacent; evaluate for migration |
| 30 | McAfee ePolicy Orchestrator Corp | PROTECT | Cyber Sec Ops | Medium | Tolerate | Corporate AV management; migrate to CrowdStrike (Phase 1) |
| 31 | McAfee ePolicy Orchestrator PCI | PROTECT | Shared Services | Medium | Tolerate | PCI AV management; migrate to CrowdStrike after validation (Phase 3) |
| 32 | Microsoft Authenticator | PROTECT | Cyber Sec Ops | Low | Invest | Mobile MFA app; supports passwordless authentication |
| 33 | Microsoft Cloud App Security | PROTECT | Cyber Sec Ops | Low | Invest | CASB for SaaS visibility and control; shadow IT detection |
| 34 | Microsoft Office 365 Security & Compliance Console | PROTECT | Cyber Sec Ops | Low | Invest | M365 DLP, retention, eDiscovery; compliance management |
| 35 | NMap | RESPOND | Cyber Sec Ops | Low | Unspecified | Network scanning for IR and reconnaissance; open source tool |
| 36 | NPS Server | PROTECT | Cyber Sec Ops | Medium | Tolerate | Network Policy Server for RADIUS MFA; Azure MFA integration |
| 37 | Palo Alto Cortex XSOAR | RESPOND, RECOVER | Cyber Sec Ops | Low | Invest | SOAR platform; playbook automation; case management |
| 38 | Panorama | PROTECT, RESPOND | Cyber Sec Ops | Medium | Invest | Centralized firewall management; network segmentation enforcement |
| 39 | Prisma Cloud - Code Security | PROTECT | Cyber Sec Ops | Low | Unspecified | Cloud-native app protection (CNAPP); expand to CSPM |
| 40 | Process Control VMWare Horizon Client | PROTECT | Cyber Sec Ops | Low | Unspecified | VDI for OT engineering; session isolation from corporate network |
| 41 | Proofpoint | DETECT | Cyber Sec Ops | Medium | Invest | Email threat protection; phishing/malware/BEC detection |
| 42 | Proofpoint Audit | DETECT | Cyber Sec Ops | Medium | Invest | Email audit for compliance and investigations |
| 43 | Proofpoint Security Awareness Training | PROTECT | Cyber Sec Ops | Low | Invest | Phishing simulation and training; human firewall development |
| 44 | Qualys | IDENTIFY, DETECT | Cyber Sec Ops | Medium | Tolerate | Vulnerability scanning; limited OT support; IT-focused |
| 45 | RSA - Authentication Manager | PROTECT | Cyber Sec Ops | Low | Migrate | **MIGRATE to Azure MFA** - 85% complete; target retirement June 2027 |
| 46 | RSA - SecurID | PROTECT | Cyber Sec Ops | Low | Migrate | **MIGRATE to Azure MFA + Yubikeys** - 85% complete; target June 2027 |
| 47 | SPAM Digest | DETECT | Cyber Sec Ops | Low | Invest | Proofpoint quarantine digest; user self-service email review |
| 48 | ServiceNow IT Applications | IDENTIFY, RECOVER | Corporate | Medium | Tolerate | Custom security control app; tracks incidents, controls, risk register |
| 49 | Sophos Antivirus (Linux - Red Hat) | PROTECT | Shared Services | Low | Invest | Linux AV; consolidation candidate (Phase 2 - migrate to CrowdStrike Linux) |
| 50 | Sourcefire Appliance | DETECT | Cyber Sec Ops | High | Tolerate | IPS/IDS; network threat detection; aging platform requiring refresh evaluation |
| 51 | Splunk | IDENTIFY, DETECT, RESPOND, RECOVER | Cyber Sec Ops | Low | Invest | Primary SIEM; threat detection; IR investigations; multi-function |
| 52 | Splunk (China) | IDENTIFY, DETECT | Cyber Sec Ops | Medium | Tolerate | Regional SIEM for China compliance; consolidation candidate (compliance-dependent) |
| 53 | Splunk PCI | IDENTIFY, DETECT | Cyber Sec Ops | Medium | Unspecified | PCI-DSS SIEM; consolidation candidate if compliant (QSA validation required) |
| 54 | Symantec End-point Protection Management Server | PROTECT | Shared Services | Low | Invest | OT endpoint management; critical for control network; air-gapped updates |
| 55 | Symantec Endpoint Protection Control Network | PROTECT | Cyber Sec Ops | Medium | Invest | OT endpoint protection; ICS-appropriate AV; retain for OT (Phase 5 decision) |
| 56 | System Center Endpoint Protection | PROTECT | Corporate | Low | Invest | Microsoft Defender integration; Windows Server protection |
| 57 | TripWire Enterprise | IDENTIFY, PROTECT, DETECT, RECOVER | Shared Services | High | Tolerate | File integrity monitoring; SOX control; config baseline; multi-function |
| 58 | Tripwire Enterprise Client | IDENTIFY, PROTECT, DETECT | Shared Services | High | Tolerate | TripWire agent deployment; FIM client |
| 59 | Windows Event Collector | DETECT | Cyber Sec Ops | Low | Tolerate | Windows log collection infrastructure feeding Splunk |
| 60 | Yubikeys | PROTECT | Cyber Sec Ops | Medium | Unspecified | FIDO2 hardware tokens; phishing-resistant MFA; strategic for privileged users |
| 61 | ZeroFox | DETECT | Corporate | Unspecified | Unspecified | External threat intel; brand protection; dark web monitoring; executive impersonation detection |
| 62 | click.cenovus.com | PROTECT | Corporate | High | Invest | Cenovus landing zone; authentication gateway |
| 63 | myvpn.cenovus.com | PROTECT | Corporate | High | Eliminate | **ELIMINATE by Sept 2027** - 70% migrated to Global Protect; decommission target Sept 2027 |

---

### 8.2 Database Cleanup Actions

The following actions are required to correct the Enterprise Architecture database (ea_architecture.db):

#### Duplicate Entries - Remove from Database

1. **Falcon (ID 17)** - Duplicate of CrowdStrike Falcon (ID 10)
   **Action**: Remove ID 17, retain ID 10 as canonical entry

2. **McAfee Management (ePO Corp) (ID 25)** - Duplicate of McAfee ePolicy Orchestrator Corp (ID 30)
   **Action**: Remove ID 25, retain ID 30 as canonical entry with full product name

3. **McAfee Management (ePO PCI) (ID 26)** - Duplicate of McAfee ePolicy Orchestrator PCI (ID 31)
   **Action**: Remove ID 26, retain ID 31 as canonical entry with full product name

**Result**: 63 applications → 60 unique applications (3 duplicates removed)

---

#### Missing TIME Disposition - Assign Values

1. **Control Network - Access Control Server** → **TOLERATE** (short-term) or **INVEST** (if modernizing to Zero Trust NAC)
   Recommended: TOLERATE pending OT access control architecture review

2. **McAfee ePolicy Orchestator (Lima)** → **TOLERATE**
   Lima refinery-specific; maintain until corporate consolidation proven in downstream environments

3. **Ericom AccessNow** → **TOLERATE**
   Maintain for Juniper device access; evaluate for ZTNA migration during P2 timeframe

4. **External Dynamic List** → **INVEST**
   Integrated with Panorama strategic firewall platform; critical threat intel feed

5. **NMap** → **TOLERATE**
   Open source tool for incident response; maintain for IR team toolkit

6. **Prisma Cloud - Code Security** → **INVEST**
   Strategic cloud security platform; expand to CSPM capability (P3-13)

7. **Process Control VMWare Horizon Client** → **TOLERATE**
   OT VDI access; maintain until OT remote access architecture review

8. **Splunk PCI** → **TOLERATE**
   Maintain pending SIEM consolidation compliance validation (P2-8)

9. **Yubikeys** → **INVEST**
   Strategic hardware token standard for phishing-resistant authentication

10. **ZeroFox** → **INVEST**
    External threat intelligence strategic platform

---

#### Missing Criticality - Assign Values

1. **Control Network - Access Control Server** → **MEDIUM**
   OT boundary control; important but redundant controls exist (network segmentation)

2. **ZeroFox** → **LOW**
   External monitoring; important but non-critical to operations

---

#### Recommended Database Update SQL

```sql
-- Remove duplicate entries
DELETE FROM applications WHERE id IN (17, 25, 26);

-- Assign missing TIME dispositions
UPDATE applications SET time_disposition = 'TOLERATE' WHERE id = 8;  -- Control Network ACS
UPDATE applications SET time_disposition = 'TOLERATE' WHERE id = 29; -- McAfee Lima
UPDATE applications SET time_disposition = 'TOLERATE' WHERE id = 15; -- Ericom AccessNow
UPDATE applications SET time_disposition = 'INVEST' WHERE id = 16;   -- External Dynamic List
UPDATE applications SET time_disposition = 'TOLERATE' WHERE id = 35; -- NMap
UPDATE applications SET time_disposition = 'INVEST' WHERE id = 39;   -- Prisma Cloud
UPDATE applications SET time_disposition = 'TOLERATE' WHERE id = 40; -- VMWare Horizon
UPDATE applications SET time_disposition = 'TOLERATE' WHERE id = 53; -- Splunk PCI
UPDATE applications SET time_disposition = 'INVEST' WHERE id = 60;   -- Yubikeys
UPDATE applications SET time_disposition = 'INVEST' WHERE id = 61;   -- ZeroFox

-- Assign missing criticality
UPDATE applications SET criticality = 'MEDIUM' WHERE id = 8;  -- Control Network ACS
UPDATE applications SET criticality = 'LOW' WHERE id = 61;    -- ZeroFox
```

---

### 8.3 Conclusion

This NIST Cybersecurity Framework mapping provides a comprehensive strategic view of Cenovus Energy's 63-application security portfolio. The analysis surfaces critical findings requiring immediate leadership attention and investment prioritization.

#### Key Conclusions

**1. Strong PROTECT and DETECT Coverage**

The portfolio demonstrates mature capabilities in prevention and detection, reflecting years of strategic investment in endpoint security, network protection, and email threat detection. 60% of the portfolio focuses on PROTECT functions, with strong cloud security integration via Azure/M365 security stack.

---

**2. Critical RECOVER Function Gap - Immediate Investment Required**

The most significant finding is weak recovery capability (only 6% of portfolio, 4 applications). This represents critical vulnerability for oil and gas infrastructure where operational downtime has material financial and safety consequences:

- **Financial Impact**: Production downtime costs $5M-$15M per day for major facilities
- **Regulatory Risk**: Potential SOX and IEC 62443 non-compliance
- **Safety Concern**: Extended recovery time increases risk during manual restoration operations

**Immediate Action Required**: Priority 0 investment in cyber recovery orchestration and OT backup/disaster recovery capabilities ($800K-$1.3M total).

---

**3. OT/ICS Security Requires Acceleration**

While basic OT protections exist (access control, endpoint security, network segmentation), critical gaps in OT-specific capabilities create unacceptable risk for upstream and downstream operations:

- **No industrial protocol visibility** (Modbus, DNP3, OPC) - cannot detect OT-specific attacks
- **Incomplete OT asset inventory** - unknown device population impairs incident response
- **No OT backup capability** - recovery requires days-to-weeks of manual PLC reprogramming
- **Limited OT forensics** - cannot perform root cause analysis after OT cyber incidents

**Current OT Security Maturity**: IEC 62443 ML 1-2 (Initial to Managed)
**Target Maturity**: ML 2-3 (Managed to Defined) within 24 months
**Investment Required**: $1.25M-$2.25M over 18-24 months

**Regulatory Drivers**: Canadian Energy Regulator (CER), Alberta Energy Regulator (AER), IEC 62443, insurance requirements

---

**4. Substantial Rationalization Opportunity - $880K-$1.08M Annual Savings**

The portfolio contains significant duplication representing substantial cost reduction potential:

- **11 endpoint protection products** → consolidate to 2-3 platforms ($400K-$600K annual savings)
- **3 SIEM instances** → consolidate to 1 federated instance ($200K annual savings, compliance-dependent)
- **3 MFA platforms** → consolidate to Azure MFA + Yubikeys ($230K annual savings)
- **2 VPN platforms** → eliminate legacy VPN ($50K annual savings)

**Total Portfolio Reduction**: 63 applications → 43-46 applications (27-32% reduction)

**Timeline**: 18-24 months for complete rationalization roadmap execution

---

**5. Cloud Transformation Progress - Continue Momentum**

51% of applications in INVEST category are concentrated in Azure/M365 security stack, demonstrating successful cloud security transformation. Strategic commitment to Microsoft security ecosystem enables:

- Unified identity platform (Azure AD/Entra ID with conditional access)
- Integrated threat intelligence sharing across Microsoft security products
- Cloud-native CASB and data loss prevention capabilities
- Zero Trust architecture enablement via Entra Private Network Connector

**Recommendation**: Continue cloud security investment and integration momentum.

---

**6. TIME Model Rebalancing Required**

Current TIME distribution (51% INVEST, 41% TOLERATE) indicates need for portfolio rebalancing:

- **Shift resources** from 41% TOLERATE applications toward RECOVER function investment
- **Execute active migrations** (RSA retirement, legacy VPN elimination) to eliminate 3% MIGRATE/ELIMINATE applications
- **Rebalance toward OT security** - limited OT applications in INVEST category despite critical infrastructure risk

**Action**: Execute rationalization roadmap over 18-24 months, reinvesting savings into RECOVER and OT security capabilities.

---

#### Strategic Recommendations for Leadership

**For CISO Consideration**:

1. Present Priority 0 recommendations (Cyber Recovery, OT Monitoring, RSA Retirement) to executive leadership for immediate funding approval
2. Establish OT security program with dedicated staff and budget ($1.25M-$2.25M over 18-24 months)
3. Execute endpoint consolidation program to realize $400K-$600K annual savings
4. Engage Architecture Review Board (ARB) for FY2027 security architecture roadmap approval

**For CIO Consideration**:

1. Approve cyber recovery capability investment as critical infrastructure protection ($500K-$800K)
2. Support rationalization initiatives yielding $880K-$1.08M annual savings to fund gap closures
3. Endorse OT security maturity improvement program aligned with regulatory expectations

**For Architecture Review Board**:

1. Prioritize RECOVER function investment in FY2027 portfolio planning
2. Approve OT security capability roadmap with phased investment over 18-24 months
3. Endorse rationalization roadmap with quarterly progress tracking

---

#### Next Steps

1. **Present Findings to Stakeholders** (Week 1-2)
   - CISO executive briefing on critical gaps and investment priorities
   - ARB presentation for roadmap approval
   - Team Leader review for EA portfolio planning integration

2. **Develop Business Cases** (Week 3-6)
   - Priority 0 recommendations (Cyber Recovery, OT Monitoring, RSA Retirement)
   - Detailed ROI analysis including avoided incident costs
   - Regulatory compliance justification (CER, AER, IEC 62443)

3. **Initiate Quick Wins** (Month 2)
   - Complete RSA Authentication Manager retirement (85% done, 3 months to finish)
   - Remove duplicate database entries (immediate - database cleanup)
   - Begin endpoint consolidation Phase 1 (Corporate McAfee to CrowdStrike)

4. **Engage Portfolio Architect** (Month 2-3)
   - pa-cybersecurity for detailed OT security implementation planning
   - Vendor evaluations for OT monitoring platforms (Nozomi, Claroty, Dragos)
   - Compliance validation planning for SIEM consolidation (QSA, legal counsel)

5. **Update Enterprise Architecture Database** (Month 2)
   - Remove 3 duplicate entries (Falcon, McAfee ePO duplicates)
   - Assign missing TIME dispositions for 10 applications
   - Assign missing criticality for 2 applications
   - Validate final application count: 60 unique applications

---

**Document Distribution**:
- CISO (for executive decision and funding approval)
- CIO (for enterprise architecture alignment)
- Architecture Review Board Members (for roadmap approval)
- Team Leader - IT Architecture (for portfolio planning integration)
- Portfolio Architect - Cyber Security (for detailed implementation planning)

**Feedback and Questions**:
Contact IT Cyber Security Enterprise Architect

---

**Document Classification**: Internal Use Only
**Next Review Date**: August 2026 (6-month refresh cycle)

---

**END OF DOCUMENT**

---

*This document was professionally formatted by the Documentation Specialist, IT Architecture - Enterprise Architecture team, Cenovus Energy Inc.*

*Original analysis prepared by: IT Cyber Security Enterprise Architect*
*Formatting completed: February 9, 2026*
