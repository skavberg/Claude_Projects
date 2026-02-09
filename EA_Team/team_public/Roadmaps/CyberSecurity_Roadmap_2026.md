# Enterprise Architecture Roadmap

**Domain:** IT Cyber Security
**Portfolio Architect:** IT Cyber Security Portfolio Architect
**Version:** 1.0
**Last Updated:** 2026-02-07
**Planning Horizon:** 2026 - 2029

---

## 1. Domain Overview

### 1.1 Scope & Boundaries

The IT Cyber Security domain encompasses all security architecture, tools, processes, and standards that protect Cenovus Energy's information assets, operational technology environments, and digital infrastructure. This includes:

- **Identity & Access Management (IAM):** Microsoft Entra ID (Azure AD), Privileged Access Management (PAM), Multi-Factor Authentication (MFA), Single Sign-On (SSO), service account governance
- **Zero Trust Architecture:** Identity-centric security model, micro-segmentation, continuous verification, conditional access policies
- **OT/ICS Security:** Security for SCADA systems, Distributed Control Systems (DCS), Programmable Logic Controllers (PLCs), and safety instrumented systems across upstream production facilities (oil sands, thermal, conventional) and downstream refining/upgrading operations
- **Network Security:** Next-gen firewalls, IDS/IPS, SD-WAN security, DNS security, web proxy/filtering, network access control
- **Security Operations:** SIEM/SOAR platforms, Endpoint Detection & Response (EDR/XDR), vulnerability management, threat intelligence, incident response
- **Data Protection:** Data Loss Prevention (DLP), encryption (at rest, in transit), data classification, certificate management, digital rights management
- **Application Security:** Secure SDLC, SAST/DAST scanning, API security, container security
- **Governance, Risk & Compliance (GRC):** Security policy management, risk assessments, compliance frameworks (SOX, Alberta PIPA, CER pipeline regulations, IEC 62443)

**Out of Scope:** Physical security (badge access, cameras) managed by Corporate Security; business continuity/disaster recovery planning (managed by IT Infrastructure with security input).

### 1.2 Strategic Alignment

| Cenovus Strategic Priority | Cyber Security Alignment |
|---------------------------|--------------------------|
| Safe & reliable operations | OT/ICS security program protects safety-critical control systems at oil sands, refining, and pipeline facilities |
| Operational excellence & cost discipline | Security automation reduces manual effort; consolidated tooling reduces licensing costs |
| Digital transformation & innovation | Zero Trust architecture enables secure cloud adoption, remote work, and digital oilfield initiatives |
| Regulatory compliance | Security controls meet SOX IT General Controls, Alberta PIPA, CER pipeline cyber requirements, IEC 62443 |
| ESG & responsible development | Protecting critical infrastructure from cyber threats supports environmental and safety commitments |
| Integration synergies (post-Husky) | Unified security tooling and standards across legacy Cenovus and Husky environments |

### 1.3 Key Stakeholders

| Stakeholder | Role | Business Unit |
|-------------|------|---------------|
| CISO | Executive sponsor, risk owner | IT Security |
| VP, Information Technology | IT strategic direction | IT Leadership |
| Director, IT Security Operations | Operational security delivery | IT Security |
| Director, OT/Automation | OT environment owner | Operations Technology |
| Manager, Identity & Access Management | IAM service delivery | IT Security |
| VP, Upstream Operations | Oil sands & conventional operations | Upstream |
| VP, Downstream Operations | Refining & upgrading operations | Downstream |
| Director, Internal Audit | SOX compliance oversight | Finance |
| Legal & Privacy Officer | Privacy & regulatory compliance | Legal |
| EA Team Leader | Architecture governance | IT Architecture |
| IT Infrastructure Portfolio Architect | Network, data centre, hybrid cloud security dependencies | IT Architecture |
| IT Cloud Portfolio Architect | Cloud security posture, CSPM, CWPP | IT Architecture |

---

## 2. Current State Assessment

### 2.1 Application Portfolio

| Application | Business Capability | Functional Capability | Status | Health |
|-------------|--------------------|-----------------------|--------|--------|
| Microsoft Entra ID (Azure AD) | Identity Management | Directory services, SSO, conditional access, MFA | Production | Green |
| CyberArk Privileged Access Security | Privileged Access Management | Privileged credential vaulting, session recording, JIT access | Production | Yellow |
| Microsoft Sentinel | Security Event Monitoring | Cloud-native SIEM, log aggregation, analytics, automated response | Production | Green |
| Microsoft Defender for Endpoint | Endpoint Protection | EDR, threat detection, automated investigation & response | Production | Green |
| Microsoft Defender for Cloud | Cloud Security | CSPM, CWPP, cloud workload protection across Azure & AWS | Production | Green |
| Palo Alto Networks (PA-Series) | Network Security | Next-gen firewall, IPS, URL filtering, threat prevention | Production | Green |
| Palo Alto Prisma Access | Secure Remote Access | SASE/SSE, ZTNA for remote workforce | Production | Green |
| Zscaler Internet Access | Web Security | Secure web gateway, cloud proxy, SSL inspection | Production | Yellow |
| Tenable.io | Vulnerability Management | Vulnerability scanning, asset discovery, risk prioritization | Production | Yellow |
| Claroty xDome | OT Security Monitoring | OT asset discovery, threat detection, vulnerability management for ICS | Production | Yellow |
| Proofpoint Email Protection | Email Security | Email gateway, anti-phishing, sandboxing, DMARC enforcement | Production | Green |
| Sailpoint IdentityNow | Identity Governance | Access certifications, lifecycle management, role mining | Production | Yellow |
| Netskope CASB | Cloud Access Security | Shadow IT discovery, DLP for SaaS, CASB | Production | Yellow |
| Varonis Data Security | Data Protection | Data classification, access analytics, insider threat detection | Production | Yellow |
| ServiceNow SecOps | Security Operations | Vulnerability response workflows, security incident management | Production | Green |
| Qualys SSL Labs / Venafi | Certificate Management | TLS/SSL certificate lifecycle, PKI management | Production | Yellow |
| KnowBe4 | Security Awareness | Phishing simulation, security awareness training | Production | Green |
| Legacy McAfee ePO | Endpoint Protection (Legacy) | Legacy AV management for remaining Husky endpoints | Sunset | Red |
| Legacy Fortinet FortiGate | Network Security (Legacy) | Legacy firewalls at select downstream facilities | Sunset | Red |

### 2.2 Technology Stack

| Layer | Technology | Version | End of Support |
|-------|-----------|---------|----------------|
| Identity Provider | Microsoft Entra ID | Current (SaaS) | N/A - Evergreen |
| PAM | CyberArk Privilege Cloud | 13.x | 2027-Q2 (upgrade planned) |
| SIEM | Microsoft Sentinel | Current (SaaS) | N/A - Evergreen |
| EDR/XDR | Microsoft Defender for Endpoint P2 | Current (SaaS) | N/A - Evergreen |
| Firewall (Primary) | Palo Alto PAN-OS | 11.1 | 2028-Q4 |
| SASE/ZTNA | Palo Alto Prisma Access | 3.x | N/A - Evergreen |
| Web Proxy | Zscaler Internet Access | Current (SaaS) | N/A - Evergreen |
| Vulnerability Scanner | Tenable.io | Current (SaaS) | N/A - Evergreen |
| OT Security | Claroty xDome | 4.x | 2028-Q1 |
| Email Security | Proofpoint Email Protection | Current (SaaS) | N/A - Evergreen |
| IGA | SailPoint IdentityNow | Current (SaaS) | N/A - Evergreen |
| Legacy AV | McAfee ePO | 5.10 | 2025-12-31 (EOL passed) |
| Legacy Firewall | Fortinet FortiOS | 6.4 | 2025-09-30 (EOL passed) |

### 2.3 Strengths

- Strong Microsoft security ecosystem foundation (Entra ID, Sentinel, Defender suite) providing integrated visibility
- OT security monitoring established with Claroty xDome across major upstream and downstream facilities
- CyberArk PAM deployed for IT privileged accounts with session recording
- Cloud-delivered security services (SaaS-based SIEM, EDR, email) reduce infrastructure overhead
- Dedicated CISO and security operations team with 24/7 managed detection and response (MDR) partnership
- Security awareness program achieving >90% phishing simulation pass rates
- Conditional access policies enforcing MFA for all cloud application access

### 2.4 Gaps & Pain Points

| # | Gap | Business Impact | Priority |
|---|-----|-----------------|----------|
| G1 | Incomplete OT network segmentation - flat networks persist at some legacy facilities | A compromise in one OT zone could propagate to safety systems; regulatory risk under CER | Critical |
| G2 | PAM not extended to OT service accounts and shared credentials on SCADA/DCS systems | Unmonitored privileged access to safety-critical systems; SOX audit finding risk | Critical |
| G3 | Legacy McAfee and Fortinet assets past end-of-life at former Husky downstream sites | Unpatched security infrastructure; no vendor support for critical vulnerabilities | High |
| G4 | Identity governance (SailPoint) not fully integrated with SAP and upstream field apps | Manual access provisioning/deprovisioning; orphaned accounts; SOX ITGC deficiency risk | High |
| G5 | No unified API security or application security testing program | APIs proliferating with cloud/mobile initiatives without security validation | High |
| G6 | Data classification and DLP policies inconsistently applied across endpoints and cloud | Sensitive data (reservoir data, financial, personal) may be exfiltrated without detection | Medium |
| G7 | OT vulnerability management immature - no regular patching cadence for ICS | Known CVEs in PLCs and DCS remain unaddressed; potential for safety incidents | High |
| G8 | Limited cyber incident response capability specific to OT/ICS environments | OT incidents handled ad-hoc; no OT-specific playbooks or tabletop exercises | High |
| G9 | Zscaler and Prisma Access overlap - dual SASE/SSE investments creating confusion | Redundant licensing costs; inconsistent policy enforcement for remote users | Medium |
| G10 | No formal DevSecOps pipeline for cloud-native application development | Security scanning not embedded in CI/CD; vulnerabilities found late in lifecycle | Medium |

### 2.5 Technical Debt

| Item | Risk | Effort to Remediate | Priority |
|------|------|---------------------|----------|
| McAfee ePO on ~800 legacy Husky endpoints | No vendor patches; blind spot for EDR coverage | Medium - migrate to Defender for Endpoint | Critical |
| Fortinet FortiGate at 3 downstream facilities | EOL firmware; no IPS signature updates | Medium - replace with Palo Alto PA-series | Critical |
| Legacy on-premises Active Directory domain controllers (Husky forest) | Kerberos attack surface; forest trust complexity | High - consolidate to single Entra ID tenant | High |
| Manual security exception tracking in spreadsheets | No audit trail; exceptions never reviewed/expired | Low - migrate to ServiceNow SecOps | Medium |
| VPN concentrators for OT remote access | Full network tunnel access; no micro-segmentation | Medium - replace with ZTNA for OT | High |
| Shared service accounts in OT (200+ unmanaged) | No accountability; credential reuse across systems | Medium - onboard to CyberArk; implement individual accounts | Critical |

---

## 3. Future State Vision

### 3.1 Target Architecture

The target state for Cenovus Energy's cyber security architecture is a **mature, Zero Trust-based security posture** that provides:

**Identity-Centric Security:**
- All access (IT and OT) governed by strong identity verification with Microsoft Entra ID as the unified identity provider
- Privileged access managed through CyberArk with just-in-time (JIT) elevation for both IT and OT environments
- Full identity lifecycle automation via SailPoint integrated with SAP, upstream, and downstream applications
- Passwordless authentication adopted for standard users (FIDO2, Windows Hello for Business)

**IT/OT Convergence Security:**
- Purdue Model-aligned network segmentation enforced at all upstream and downstream facilities with Palo Alto NGFW
- Claroty xDome providing full OT asset visibility, vulnerability management, and threat detection across all sites
- OT-specific incident response playbooks integrated with IT SOC via Microsoft Sentinel
- Secure remote access to OT environments through ZTNA (replacing legacy VPN) with session recording
- IEC 62443 zone/conduit model implemented for all new and retrofitted ICS environments

**Unified Security Operations:**
- Microsoft Sentinel as the consolidated SIEM/SOAR with custom analytics rules for oil & gas OT use cases
- Microsoft Defender XDR providing unified endpoint, email, identity, and cloud app protection
- Automated vulnerability management lifecycle from Tenable scanning through ServiceNow SecOps remediation
- Threat intelligence feeds (industry ISAC - ONG-ISAC, MS Threat Intelligence) integrated into detection

**Data & Application Security:**
- Microsoft Purview for unified data classification, DLP, and information protection
- DevSecOps pipeline with SAST/DAST/SCA scanning integrated into CI/CD
- API security gateway for all external and partner-facing APIs

**Rationalized Tooling:**
- Consolidated SASE/SSE to a single platform (Palo Alto Prisma Access) - Zscaler retired
- Legacy McAfee and Fortinet fully decommissioned
- Single Entra ID tenant with legacy AD forests decommissioned

### 3.2 Guiding Principles

1. **Zero Trust - Never trust, always verify:** All access requests are authenticated, authorized, and encrypted regardless of network location. No implicit trust based on network perimeter.
2. **Secure the process, not just the technology:** Security controls must align with oil and gas operational workflows; security must never compromise safety of personnel or process safety systems.
3. **Defense in depth for critical infrastructure:** Multiple overlapping security layers protect safety-critical and production-critical OT systems. Apply IEC 62443 security levels proportional to consequence of compromise.
4. **Automate and orchestrate:** Reduce mean time to detect (MTTD) and mean time to respond (MTTR) through automated detection, enrichment, and response playbooks.
5. **Risk-based prioritization:** Security investments prioritized by business risk and consequence of compromise, with highest priority to safety-critical OT systems and regulated data (SOX, PIPA).
6. **Consolidate and simplify:** Reduce security tool sprawl; prefer platform consolidation within the Microsoft and Palo Alto ecosystems to reduce integration complexity and licensing cost.
7. **Compliance by design:** Security architecture inherently satisfies SOX ITGC, Alberta PIPA, CER pipeline cyber regulations, and IEC 62443 requirements.

### 3.3 Target Application Portfolio

| Application | Business Capability | Functional Capability | Change |
|-------------|--------------------|-----------------------|--------|
| Microsoft Entra ID | Identity Management | Unified IdP, SSO, MFA, conditional access, passwordless | Enhance |
| CyberArk Privilege Cloud | Privileged Access Management | IT + OT PAM, JIT elevation, session recording, secrets management | Enhance |
| Microsoft Sentinel | Security Event Monitoring | SIEM/SOAR for IT and OT, automated playbooks | Enhance |
| Microsoft Defender XDR | Endpoint & Threat Protection | Unified XDR across endpoint, email, identity, cloud apps | Enhance |
| Microsoft Defender for Cloud | Cloud Security | CSPM, CWPP, DevOps security posture | Enhance |
| Palo Alto Networks (PA-Series) | Network Security | NGFW, IPS, OT micro-segmentation | Enhance |
| Palo Alto Prisma Access | Secure Access (SASE) | Consolidated SASE/SSE, ZTNA for IT and OT remote access | Enhance |
| Tenable.io / Tenable.ot | Vulnerability Management | Unified IT + OT vulnerability management | Enhance |
| Claroty xDome | OT Security Monitoring | OT asset inventory, threat detection, secure remote access | Enhance |
| Proofpoint Email Protection | Email Security | Advanced email threat protection | Retain |
| SailPoint IdentityNow | Identity Governance | Full lifecycle, access certifications, SAP integration | Enhance |
| Microsoft Purview | Data Protection | Data classification, DLP, information protection (replaces Varonis + Netskope DLP functions) | New |
| ServiceNow SecOps | Security Operations | Vulnerability response, security incident management, exception tracking | Enhance |
| Venafi TLS Protect | Certificate Management | Automated certificate lifecycle, PKI | Enhance |
| KnowBe4 | Security Awareness | Phishing simulation, training | Retain |
| Snyk / GitHub Advanced Security | Application Security | SAST, SCA, container scanning in CI/CD | New |
| Zscaler Internet Access | Web Security | Cloud proxy | Retire |
| Netskope CASB | Cloud Access Security | CASB/DLP | Retire |
| Varonis Data Security | Data Protection | Data classification, analytics | Retire |
| McAfee ePO | Endpoint Protection (Legacy) | Legacy AV | Retire |
| Fortinet FortiGate | Network Security (Legacy) | Legacy firewall | Retire |

---

## 4. Transition Roadmap

### 4.1 Roadmap Swimlanes

#### Near Term (0-12 months: 2026)

| Initiative | Description | Dependencies | Status |
|-----------|-------------|--------------|--------|
| **Legacy endpoint migration** | Migrate remaining ~800 McAfee ePO endpoints to Microsoft Defender for Endpoint; decommission McAfee infrastructure | Endpoint inventory, IT Infrastructure team support | In Progress |
| **Legacy firewall replacement** | Replace 3 Fortinet FortiGate deployments at downstream facilities with Palo Alto PA-series | OT change management windows, IT Infrastructure team | Planned |
| **OT PAM Phase 1** | Onboard top-50 critical OT service accounts to CyberArk; eliminate shared credentials on Tier 1 safety systems | Claroty asset inventory, OT team cooperation | Planned |
| **OT network segmentation Phase 1** | Implement Purdue Model Level 3/3.5 DMZ segmentation at 2 priority upstream facilities (Christina Lake, Foster Creek) | Palo Alto NGFW deployment, OT network assessment | Planned |
| **SailPoint-SAP integration** | Integrate SailPoint IdentityNow with SAP S/4HANA for automated joiner/mover/leaver provisioning | SAP team, HR data feed, Corporate Apps architect | Planned |
| **SASE consolidation assessment** | Complete technical evaluation and business case for consolidating Zscaler + Prisma Access to single SASE platform | Vendor discussions, IT Infrastructure team | Planned |
| **OT incident response playbooks** | Develop OT-specific incident response playbooks and conduct tabletop exercise with operations teams | OT team, CISO, external ICS incident response partner | Planned |
| **Security exception management** | Migrate security exceptions from spreadsheets to ServiceNow SecOps with automated expiry workflows | ServiceNow platform team | Planned |
| **Entra ID tenant consolidation planning** | Plan and design migration of legacy Husky AD forest into primary Cenovus Entra ID tenant | IT Infrastructure, all application teams | Planned |

#### Medium Term (12-24 months: 2027)

| Initiative | Description | Dependencies | Status |
|-----------|-------------|--------------|--------|
| **OT PAM Phase 2** | Extend CyberArk to all OT service accounts (~200); implement individual operator accounts for DCS/SCADA access | Phase 1 completion, OT change management | Planned |
| **OT network segmentation Phase 2** | Extend Purdue Model segmentation to remaining upstream facilities and all 3 downstream refining/upgrading sites | Phase 1 lessons learned, capital approval | Planned |
| **SASE consolidation execution** | Migrate from Zscaler to Palo Alto Prisma Access (or vice versa based on assessment); retire duplicate platform | Assessment completion, change management | Planned |
| **Microsoft Purview deployment** | Deploy Microsoft Purview for data classification, sensitivity labelling, and DLP across M365, endpoints, and cloud; retire Varonis and Netskope DLP | Data classification taxonomy, business stakeholder buy-in | Planned |
| **DevSecOps pipeline** | Implement Snyk/GitHub Advanced Security for SAST, SCA, and container scanning in Azure DevOps CI/CD pipelines | Cloud Platform team, development teams | Planned |
| **Passwordless Phase 1** | Roll out FIDO2 security keys and Windows Hello for Business for corporate users; reduce password reliance | Entra ID conditional access updates, endpoint hardware | Planned |
| **OT vulnerability management program** | Formalize OT vulnerability management using Tenable.ot with risk-based prioritization and maintenance window patching | Claroty integration, OT maintenance scheduling | Planned |
| **Entra ID consolidation execution** | Execute AD forest consolidation; migrate legacy Husky accounts and applications to primary Entra ID tenant | Application compatibility testing, all business units | Planned |
| **Sentinel OT analytics** | Deploy custom Microsoft Sentinel analytics rules and workbooks for OT/ICS threat detection using Claroty data connector | Claroty xDome, Sentinel workspace | Planned |

#### Long Term (24-36 months: 2028-2029)

| Initiative | Description | Dependencies | Status |
|-----------|-------------|--------------|--------|
| **OT network segmentation Phase 3** | Implement micro-segmentation within OT zones (Level 1/2 separation) at highest-risk facilities | Phase 2 completion, safety system assessment | Planned |
| **ZTNA for OT remote access** | Replace legacy VPN concentrators for OT vendor/contractor remote access with ZTNA solution with session recording | OT PAM Phase 2, vendor relationship management | Planned |
| **AI-driven security operations** | Deploy AI/ML-based anomaly detection in Sentinel; automate Tier 1 SOC triage and response using SOAR playbooks | Sentinel maturity, SOC process maturity | Planned |
| **Passwordless Phase 2** | Extend passwordless to field/plant workers using mobile-based authentication; explore wearable authentication for OT environments | Phase 1 completion, OT user experience assessment | Planned |
| **API security gateway** | Deploy centralized API security gateway for all external-facing and partner APIs | API inventory, Cloud Platform team | Planned |
| **Continuous compliance automation** | Automated evidence collection for SOX ITGC, IEC 62443, and CER cyber audits using GRC platform integration | GRC platform, audit requirements mapping | Planned |
| **IEC 62443 certification** | Achieve IEC 62443-3-3 compliance certification for Tier 1 OT environments (Christina Lake, Lloydminster upgrader) | All OT security initiatives | Planned |

### 4.2 Key Milestones

| Milestone | Target Date | Dependencies |
|-----------|-------------|--------------|
| McAfee ePO fully decommissioned | 2026-Q2 | Endpoint migration completion |
| Fortinet FortiGate fully decommissioned | 2026-Q3 | Palo Alto deployment at 3 sites |
| OT PAM Phase 1 - 50 critical accounts onboarded | 2026-Q4 | CyberArk OT integration |
| Purdue Model segmentation at 2 upstream facilities | 2026-Q4 | NGFW deployment, OT assessment |
| SailPoint-SAP integration live | 2026-Q3 | SAP team readiness |
| SASE platform consolidated to single vendor | 2027-Q2 | Assessment completion, migration |
| Entra ID tenant consolidation complete | 2027-Q4 | Application migration, testing |
| OT PAM Phase 2 - all 200 accounts onboarded | 2027-Q3 | Phase 1 lessons learned |
| Microsoft Purview DLP operational; Varonis/Netskope retired | 2027-Q4 | Data classification deployment |
| DevSecOps pipeline operational for all cloud apps | 2027-Q3 | CI/CD integration |
| OT segmentation complete at all major facilities | 2028-Q2 | Phase 2 completion |
| Legacy VPN for OT replaced with ZTNA | 2028-Q4 | ZTNA deployment |
| IEC 62443 compliance assessment complete | 2029-Q2 | All OT security initiatives |

### 4.3 Application Rationalization Plan

| Application | Action | Target Date | Savings |
|-------------|--------|-------------|---------|
| McAfee ePO | Retire - replace with Microsoft Defender for Endpoint | 2026-Q2 | ~$150K/yr licensing + infrastructure |
| Fortinet FortiGate (3 sites) | Retire - replace with Palo Alto PA-series | 2026-Q3 | Reduced complexity; unified firewall management |
| Zscaler Internet Access | Retire - consolidate into Prisma Access | 2027-Q2 | ~$400K/yr licensing |
| Netskope CASB | Retire - replace with Microsoft Defender for Cloud Apps + Purview | 2027-Q4 | ~$250K/yr licensing |
| Varonis Data Security | Retire - replace with Microsoft Purview | 2027-Q4 | ~$300K/yr licensing |
| Legacy AD forest (Husky) | Retire - consolidate to Entra ID | 2027-Q4 | Infrastructure costs + operational overhead |
| Legacy VPN concentrators (OT) | Retire - replace with ZTNA | 2028-Q4 | Reduced attack surface; licensing savings |

---

## 5. Investment Summary

| Initiative | CapEx | OpEx (Annual) | Priority | Year |
|-----------|-------|---------------|----------|------|
| Legacy endpoint migration (McAfee to Defender) | $200K | $0 (existing Defender licensing) | Critical | 2026 |
| Legacy firewall replacement (Fortinet to Palo Alto) | $450K | $80K | Critical | 2026 |
| OT PAM Phase 1 (CyberArk OT extension) | $300K | $120K | Critical | 2026 |
| OT network segmentation Phase 1 (2 facilities) | $600K | $50K | Critical | 2026 |
| SailPoint-SAP integration | $250K | $30K | High | 2026 |
| OT incident response development | $150K | $25K | High | 2026 |
| SASE consolidation | $200K | -$400K (savings) | Medium | 2027 |
| OT PAM Phase 2 | $200K | $80K | Critical | 2027 |
| OT segmentation Phase 2 (remaining facilities) | $1.2M | $100K | Critical | 2027 |
| Microsoft Purview deployment | $350K | $200K | High | 2027 |
| DevSecOps pipeline (Snyk/GHAS) | $150K | $180K | Medium | 2027 |
| Passwordless authentication Phase 1 | $200K | $20K | Medium | 2027 |
| Entra ID tenant consolidation | $400K | -$150K (savings) | High | 2027 |
| OT micro-segmentation Phase 3 | $800K | $75K | High | 2028 |
| ZTNA for OT remote access | $300K | $60K | High | 2028 |
| AI-driven SOC automation | $250K | $100K | Medium | 2028 |
| IEC 62443 compliance program | $400K | $50K | High | 2028-2029 |
| **TOTAL (3-Year Program)** | **~$6.4M** | **~$620K net new** | | 2026-2029 |

---

## 6. Risks & Dependencies

| Risk/Dependency | Type | Likelihood | Impact | Mitigation |
|-----------------|------|-----------|--------|------------|
| OT change management resistance - operations teams reluctant to accept security changes in production environments | Risk | High | High | Early engagement with operations; align changes with turnaround/maintenance windows; demonstrate safety benefits |
| Legacy Husky infrastructure complexity greater than assessed | Risk | Medium | High | Thorough discovery and assessment; phased approach with rollback capability |
| Skilled cybersecurity resource shortage in Calgary market | Risk | High | Medium | Partner with MSSPs for specialized OT security; invest in training; leverage Microsoft/Palo Alto professional services |
| CER pipeline cyber regulation changes (pending federal requirements) | Risk | Medium | High | Proactive alignment with IEC 62443 and NIST CSF; monitor regulatory developments through industry associations |
| Microsoft licensing cost increases affecting security suite economics | Risk | Medium | Medium | Enterprise agreement negotiation; maintain optionality with multi-vendor capabilities |
| OT network segmentation causing operational disruptions | Risk | Medium | Critical | Extensive pre-implementation testing; passive monitoring before enforcement; safety system isolation guaranteed |
| Dependency on IT Infrastructure team for network changes | Dependency | High | Medium | Joint planning sessions; shared resource allocation; escalation path through EA Team Leader |
| Dependency on IT Cloud team for Azure security configuration | Dependency | High | Medium | Aligned roadmaps; joint architecture reviews; shared responsibility model documentation |
| SAP S/4HANA migration timeline affecting SailPoint integration | Dependency | Medium | Medium | Coordinate with Corporate Applications architect; phase integration with SAP migration milestones |
| Supply chain cyber attack on OT vendor/equipment | Risk | Medium | Critical | Vendor risk assessments; software bill of materials (SBOM) requirements; network segmentation limiting blast radius |
| Merger/acquisition activity requiring additional integration | Risk | Low | High | Modular, standards-based architecture; documented integration playbook from Husky experience |

---

## 7. Governance & Review

- **Roadmap review frequency:** Quarterly
- **Next review date:** 2026-05-01
- **Approval authority:** EA Team Leader + CISO + VP Information Technology
- **Architecture Review Board (ARB):** All new security tool acquisitions and significant architecture changes require ARB approval
- **Security Architecture Review:** Monthly review of active initiatives with IT Security Operations
- **OT Security Steering Committee:** Quarterly review with OT/Automation and Operations leadership
- **Compliance Review:** Semi-annual alignment check with Internal Audit for SOX ITGC and CER requirements
- **Vendor Strategic Reviews:** Annual reviews with Microsoft, Palo Alto Networks, CyberArk, and Claroty

---

## 8. Appendices

### A. Reference Frameworks & Standards

| Framework | Application |
|-----------|-------------|
| NIST Cybersecurity Framework (CSF) 2.0 | Overall security program maturity measurement |
| IEC 62443 | OT/ICS security architecture and zone/conduit modelling |
| NIST SP 800-82 Rev 3 | Guide to OT security for industrial control systems |
| CIS Controls v8 | IT security baseline controls |
| MITRE ATT&CK (Enterprise + ICS) | Threat detection use case development |
| Zero Trust Maturity Model (CISA) | Zero Trust architecture progression tracking |
| SOX Section 404 | IT General Controls for financial reporting systems |
| Alberta PIPA | Personal information protection requirements |
| CER Onshore Pipeline Regulations | Pipeline cyber security requirements |

### B. Capability Maturity Assessment (NIST CSF)

| Function | Current Maturity | Target Maturity (2029) |
|----------|-----------------|----------------------|
| Identify | 2.5 - Risk Informed | 3.5 - Repeatable |
| Protect | 2.5 - Risk Informed | 3.5 - Repeatable |
| Detect | 3.0 - Repeatable | 4.0 - Adaptive |
| Respond | 2.0 - Risk Informed | 3.5 - Repeatable |
| Recover | 2.0 - Risk Informed | 3.0 - Repeatable |
| Govern (new in CSF 2.0) | 2.0 - Risk Informed | 3.5 - Repeatable |

### C. Vendor Landscape

- **Primary Security Platform:** Microsoft (Identity, SIEM, EDR/XDR, Cloud Security, Data Protection)
- **Network Security Platform:** Palo Alto Networks (NGFW, SASE/SSE)
- **Privileged Access:** CyberArk
- **OT Security:** Claroty
- **Identity Governance:** SailPoint
- **Email Security:** Proofpoint
- **Vulnerability Management:** Tenable
- **Security Awareness:** KnowBe4
- **IT Service Management:** ServiceNow (SecOps module)
- **Application Security:** Snyk / GitHub Advanced Security (planned)
