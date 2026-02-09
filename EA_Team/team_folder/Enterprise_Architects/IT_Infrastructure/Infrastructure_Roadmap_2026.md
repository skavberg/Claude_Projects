# Enterprise Architecture Roadmap - IT Infrastructure

**Domain:** IT Infrastructure
**Portfolio Architect:** IT Infrastructure Enterprise Architect
**Version:** 1.0
**Last Updated:** 2026-02-07
**Planning Horizon:** 2026 - 2029

---

## 1. Domain Overview

### 1.1 Scope & Boundaries
The IT Infrastructure domain at Cenovus Energy encompasses all foundational technology platforms that support corporate and operational technology environments across the integrated oil and gas value chain. This includes:

- **Data Centres**: Calgary corporate data centre, disaster recovery facility, and colocation presence at a third-party facility (e.g., Rogers/Shaw Calgary)
- **Networking**: Corporate WAN/LAN, SD-WAN connecting field sites (Christina Lake, Foster Creek, Sunrise, Lloydminster thermal/conventional assets, Lima and Toledo refineries), MPLS backbone, and internet edge
- **Compute & Storage**: VMware virtualization clusters, physical server fleet, SAN (Dell PowerStore/EMC), NAS (NetApp), and hyperconverged infrastructure (Dell VxRail)
- **End-User Computing**: Corporate laptops/desktops (Windows 11), mobile devices (iOS/Android), VDI (VMware Horizon) for field and contractor workers, printing/scanning
- **SCADA/OT Convergence**: IT/OT network demarcation, data historians (OSIsoft PI), OT DMZ architecture, and secure remote access to operational technology environments at upstream and downstream sites

**Out of Scope**: Cloud platforms (owned by IT Cloud EA), cybersecurity tooling (owned by IT Cyber Security EA), application-layer software (owned by respective Application EAs).

### 1.2 Strategic Alignment
This domain supports Cenovus Energy's corporate strategy in the following ways:

| Corporate Priority | Infrastructure Alignment |
|---|---|
| Safe & reliable operations | Resilient OT/IT infrastructure ensuring continuous SAGD and refining operations |
| Cost discipline & efficiency | Infrastructure rationalization, hybrid cloud right-sizing, and technical debt reduction |
| Digital transformation | Modern end-user computing, SD-WAN for field connectivity, edge computing at well pads |
| ESG & emissions reduction | Infrastructure power efficiency, data centre consolidation to reduce carbon footprint |
| Integration of acquired assets | Standardize infrastructure across legacy Husky Energy assets still undergoing integration |

### 1.3 Key Stakeholders
| Stakeholder | Role | Business Unit |
|---|---|---|
| VP, Information Technology | IT Executive Sponsor | Corporate IT |
| Director, IT Operations | Infrastructure Delivery Lead | IT Operations |
| Manager, Network Services | Network Operations | IT Operations |
| Manager, Data Centre & Compute | Server & Storage Operations | IT Operations |
| Manager, End-User Services | Desktop & Mobility | IT Operations |
| Director, OT & Automation | OT Systems Owner | Operations Technology |
| VP, Oil Sands Operations | Business Stakeholder - Upstream | Oil Sands |
| VP, Conventional Operations | Business Stakeholder - Conventional | Conventional |
| VP, US Manufacturing | Business Stakeholder - Refining | Downstream (Lima/Toledo) |
| Chief Information Security Officer | Security & Compliance | IT Security |

## 2. Current State Assessment

### 2.1 Application Portfolio
| Application / Platform | Business Capability | Functional Capability | Status | Health |
|---|---|---|---|---|
| VMware vSphere 7.0 | IT Service Delivery | Server Virtualization & Compute | Production | Yellow |
| Dell PowerStore / EMC Unity | IT Service Delivery | Block & File Storage | Production | Green |
| NetApp ONTAP (AFF/FAS) | IT Service Delivery | File Storage & NAS | Production | Green |
| Dell VxRail (HCI) | IT Service Delivery | Hyperconverged Compute & Storage | Production | Green |
| Cisco Catalyst / Nexus | Network Connectivity | Campus & Data Centre Switching | Production | Yellow |
| Cisco ISR/ASR Routers | Network Connectivity | WAN Routing | Production | Yellow |
| Cisco Meraki SD-WAN | Network Connectivity | Field Site WAN Optimization | Emerging | Green |
| Palo Alto PA-Series | Network Security | Firewall & Network Segmentation | Production | Green |
| F5 BIG-IP | Application Delivery | Load Balancing & WAF | Production | Yellow |
| VMware Horizon 8 | End-User Computing | Virtual Desktop Infrastructure | Production | Green |
| Microsoft Intune / SCCM | End-User Computing | Device Management & Patching | Production | Yellow |
| OSIsoft PI System | Operational Data Management | Real-Time Data Historian (OT) | Production | Green |
| Solarwinds Orion | IT Operations Management | Network & Infrastructure Monitoring | Production | Red |
| ServiceNow ITSM | IT Service Management | Incident, Change, Asset Management | Production | Green |
| Commvault Backup & Recovery | Data Protection | Backup, Restore, Archival | Production | Yellow |
| Zscaler Internet Access | Secure Connectivity | Cloud-Based Secure Web Gateway | Production | Green |

### 2.2 Technology Stack
| Layer | Technology | Version / Model | End of Support |
|---|---|---|---|
| Hypervisor | VMware vSphere | 7.0 U3 | Nov 2027 (extended) |
| HCI | Dell VxRail | VxRail 8.x (vSAN 8) | Active support |
| SAN Storage | Dell PowerStore | PowerStore 3200T | Active support |
| NAS Storage | NetApp AFF A400 | ONTAP 9.13 | Active support |
| Core Switching | Cisco Nexus 9000 | NX-OS 10.3 | Active support |
| Campus Switching | Cisco Catalyst 9300 | IOS-XE 17.x | Active support |
| Legacy Campus Switching | Cisco Catalyst 3850 | IOS-XE 16.x | Oct 2026 |
| WAN Routers | Cisco ISR 4400 | IOS-XE 17.x | Mixed (some EoL 2027) |
| SD-WAN | Cisco Meraki MX | Current firmware | Active support |
| Firewall | Palo Alto PA-5200 | PAN-OS 11.x | Active support |
| Load Balancer | F5 BIG-IP i5800 | BIG-IP 16.1 | Dec 2026 |
| VDI | VMware Horizon | 8.x (2306) | Active support |
| Endpoint OS | Microsoft Windows | 11 23H2 | Active support |
| Backup | Commvault | v2024 | Active support |
| Monitoring | SolarWinds Orion | 2023.4 | Active support (trust concern) |
| Device Mgmt | Microsoft Intune + SCCM | Co-management | SCCM transitioning to Intune |

### 2.3 Strengths
- Robust OT data historian platform (OSIsoft PI) with deep integration into upstream SAGD operations and downstream refining process control
- Established SD-WAN rollout to field sites improving connectivity and reducing MPLS costs
- Solid VDI infrastructure enabling secure remote access for field engineers and contractors
- ServiceNow ITSM platform providing mature IT service management and asset tracking
- Strong Palo Alto firewall architecture with network segmentation between IT and OT environments
- Dell VxRail HCI adoption reducing data centre footprint and operational complexity

### 2.4 Gaps & Pain Points
| # | Gap | Business Impact | Priority |
|---|---|---|---|
| 1 | VMware licensing cost increase post-Broadcom acquisition | Significant OpEx increase projected for 2026-2027 renewal; budget pressure | Critical |
| 2 | Legacy Husky Energy infrastructure not fully standardized | Duplicate tooling, inconsistent monitoring, increased support complexity | High |
| 3 | SolarWinds monitoring platform trust and capability gap | Limited observability, security concerns post-Sunburst; reactive incident detection | High |
| 4 | Aging campus switching at some field offices (Catalyst 3850 EoL) | Risk of unplanned outages at field sites; no vendor support path | High |
| 5 | F5 BIG-IP approaching end of support | Risk of load balancer failures impacting production web applications | Medium |
| 6 | Limited edge computing at upstream well pads | Inability to process OT data locally; latency for real-time decision making | Medium |
| 7 | SCCM to Intune co-management transition incomplete | Mixed device management creating patching gaps and compliance inconsistency | Medium |
| 8 | Backup infrastructure not optimized for hybrid cloud workloads | Increasing cloud workloads lack integrated backup; RPO/RTO compliance risk | Medium |
| 9 | No unified network automation / intent-based networking | Manual network changes are slow and error-prone across 150+ field sites | Low |
| 10 | Wi-Fi 6 upgrade incomplete at corporate and major field sites | Bandwidth constraints for mobile and IoT devices | Low |

### 2.5 Technical Debt
| Item | Risk | Effort to Remediate | Priority |
|---|---|---|---|
| VMware vSphere 7.0 (Broadcom licensing) | High OpEx risk; vendor lock-in | High - evaluate alternatives or negotiate | Critical |
| SolarWinds Orion monitoring stack | Security risk, limited capabilities | Medium - replace with modern observability | High |
| Cisco Catalyst 3850 switches (30+ units at field sites) | EoL Oct 2026; no patches, no support | Medium - hardware refresh program | High |
| F5 BIG-IP i5800 appliances | EoS Dec 2026; no security patches | Medium - migrate to F5 rSeries or cloud LB | Medium |
| Legacy Husky SCADA network segments | Inconsistent segmentation; integration gap | High - requires OT coordination | Medium |
| Windows 10 holdouts in field (approx. 200 devices) | EoS Oct 2025 (already past) | Low - accelerate device refresh | High |
| Commvault legacy media servers | Aging hardware; slow recovery times | Low - consolidate to modern backup appliances | Medium |

## 3. Future State Vision

### 3.1 Target Architecture
By 2029, Cenovus Energy's IT Infrastructure will be a **hybrid, software-defined, and automated** platform delivering resilient services across corporate, field, and refinery environments:

- **Hybrid Compute**: A right-sized on-premise footprint using next-generation HCI (potentially non-VMware alternatives such as Nutanix AHV or Microsoft Azure Stack HCI) complemented by cloud IaaS for burst and non-critical workloads
- **Software-Defined Networking**: Full SD-WAN deployment to all field sites with intent-based networking in corporate campus and data centre, enabling zero-touch provisioning and automated policy enforcement
- **Modern Observability**: Replacement of SolarWinds with a unified observability platform (e.g., Datadog, Dynatrace, or Elastic Observability) covering infrastructure, network, and OT telemetry
- **Edge Computing at Well Pads**: Ruggedized edge compute (Dell PowerEdge XR / HPE Edgeline) deployed at key upstream sites for local OT data processing, reducing latency and enabling real-time analytics
- **Fully Cloud-Managed End-User Computing**: Complete migration from SCCM to Microsoft Intune for endpoint management, with Windows Autopilot for zero-touch provisioning
- **Modernized OT/IT Convergence**: Purdue Model Level 3.5 DMZ fully standardized across all upstream and downstream sites, with secure data flow from OT historians to enterprise analytics platforms
- **Automated Data Protection**: Cloud-integrated backup solution with immutable storage, automated DR testing, and consistent RPO/RTO across on-premise and cloud workloads

### 3.2 Guiding Principles
1. **Hybrid by design** - Workloads are placed where they run best (on-prem, cloud, edge) based on latency, cost, data sovereignty, and operational requirements
2. **Automate everything repeatable** - Network changes, server provisioning, patching, and backup verification are automated to reduce human error and accelerate delivery
3. **Secure by default** - All infrastructure follows zero-trust principles with microsegmentation, encrypted transport, and least-privilege access
4. **Operational resilience** - Infrastructure is designed for N+1 redundancy at critical sites with documented and tested disaster recovery procedures
5. **Vendor diversification** - Reduce single-vendor lock-in (especially post-Broadcom VMware) by evaluating multi-hypervisor and open-standards-based approaches
6. **Sustainable operations** - Optimize power consumption, consolidate footprint, and prefer energy-efficient hardware to support Cenovus ESG commitments

### 3.3 Target Application Portfolio
| Application / Platform | Business Capability | Functional Capability | Change |
|---|---|---|---|
| Nutanix AHV / Azure Stack HCI | IT Service Delivery | Server Virtualization & Compute | Replace (VMware vSphere) |
| Dell PowerStore (Next Gen) | IT Service Delivery | Block & File Storage | Retain & Enhance |
| NetApp ONTAP (AFF C-Series) | IT Service Delivery | File Storage & NAS | Enhance (refresh) |
| Dell VxRail / Nutanix NX | IT Service Delivery | Hyperconverged Compute & Storage | Retain or Replace |
| Cisco Catalyst 9300/9400 | Network Connectivity | Campus & Data Centre Switching | Retain (refresh legacy) |
| Cisco Nexus 9000 (ACI) | Network Connectivity | Data Centre Fabric | Enhance (ACI adoption) |
| Cisco Meraki / Catalyst SD-WAN | Network Connectivity | Full SD-WAN to All Field Sites | Enhance (expand) |
| Palo Alto PA-Series (Next Gen) | Network Security | Firewall & Microsegmentation | Retain & Enhance |
| F5 rSeries / Cloud LB | Application Delivery | Load Balancing & WAF | Replace (F5 BIG-IP i-Series) |
| VMware Horizon / Azure Virtual Desktop | End-User Computing | Virtual Desktop Infrastructure | Evaluate (potential hybrid VDI) |
| Microsoft Intune (standalone) | End-User Computing | Unified Endpoint Management | Enhance (retire SCCM) |
| Datadog / Elastic Observability | IT Operations Management | Unified Observability & Monitoring | Replace (SolarWinds Orion) |
| AVEVA PI Server (OSIsoft successor) | Operational Data Management | Real-Time Data Historian (OT) | Retain & Enhance |
| Veeam / Cohesity | Data Protection | Modern Backup with Cloud Tiering | Replace (Commvault legacy) |
| Zscaler ZIA + ZPA | Secure Connectivity | SASE / Secure Access Service Edge | Enhance |
| Dell PowerEdge XR / HPE Edgeline | Edge Computing | OT Edge Processing at Well Pads | New |

## 4. Transition Roadmap

### 4.1 Roadmap Swimlanes

#### Near Term (0-12 months) - 2026
| Initiative | Description | Dependencies | Status |
|---|---|---|---|
| VMware licensing strategy | Evaluate Broadcom VMware ELA renewal vs. migration to Nutanix AHV or Azure Stack HCI; conduct POC | IT Cloud EA alignment; procurement | In Progress |
| SolarWinds replacement | RFP and selection of modern observability platform; begin deployment in corporate data centre | IT Cyber Security EA review; vendor selection | Planned |
| Catalyst 3850 field switch refresh | Replace 30+ EoL Catalyst 3850 switches at field sites with Catalyst 9300 | Network team capacity; field site scheduling | Planned |
| F5 BIG-IP migration | Migrate from BIG-IP i5800 to F5 rSeries or evaluate cloud-native load balancing | Application team coordination | Planned |
| Windows 10 device elimination | Complete refresh of remaining ~200 Windows 10 devices in field to Windows 11 | End-user services; supply chain | In Progress |
| Intune standalone migration | Complete SCCM to Intune migration; decommission SCCM infrastructure | Microsoft licensing; endpoint team | In Progress |
| SD-WAN Phase 2 expansion | Extend Cisco Meraki SD-WAN to remaining conventional well sites (50+ locations) | WAN circuit provisioning; Telus/Bell coordination | Planned |

#### Medium Term (12-24 months) - 2027
| Initiative | Description | Dependencies | Status |
|---|---|---|---|
| Hypervisor migration (if applicable) | Execute migration from VMware vSphere to selected alternative (Nutanix/Azure Stack HCI) for non-critical workloads | POC results from 2026; application compatibility testing | Planned |
| Observability platform full rollout | Extend new monitoring platform to all field sites, OT DMZ, and network infrastructure | Phase 1 completion; agent deployment | Planned |
| Edge computing pilot | Deploy ruggedized edge compute at 3-5 SAGD well pad sites (Christina Lake, Foster Creek) | OT team collaboration; IT Cloud EA for edge-cloud integration | Planned |
| Network automation / IaC | Implement Cisco DNA Center or Ansible-based network automation for campus and WAN provisioning | SD-WAN completion; network team training | Planned |
| Data centre consolidation study | Assess consolidation of secondary DC / DR site leveraging cloud DR capabilities | IT Cloud EA; business continuity team | Planned |
| Husky legacy infrastructure standardization | Complete migration of remaining Husky Energy infrastructure to Cenovus standards | Cross-domain coordination | Planned |
| Wi-Fi 6E upgrade | Upgrade corporate offices and major field facilities to Wi-Fi 6E (Cisco Catalyst 9136/9166) | Facilities coordination; cabling upgrades | Planned |

#### Long Term (24-36 months) - 2028-2029
| Initiative | Description | Dependencies | Status |
|---|---|---|---|
| Full hypervisor migration completion | Complete migration of all workloads to target hypervisor platform; decommission VMware | Application compatibility; testing completion | Planned |
| Edge computing scale-out | Expand edge compute to 15-20 upstream sites; integrate with cloud analytics and AI/ML pipelines | Edge pilot results; IT AI EA coordination | Planned |
| Intent-based networking (IBN) | Full IBN deployment with Cisco ACI in data centres and DNA Center campus-wide | Network automation maturity; staff training | Planned |
| Next-gen data protection | Implement immutable backup with cloud tiering; automated DR testing and compliance reporting | Backup platform selection; cloud integration | Planned |
| OT/IT convergence Phase 2 | Extend standardized Purdue Model DMZ to all remaining downstream and conventional sites | IT Cyber Security EA; OT team | Planned |
| DC power & cooling optimization | Modernize data centre cooling (liquid cooling for HCI), target PUE improvement from 1.6 to 1.3 | Facilities; capital budget | Planned |

### 4.2 Key Milestones
| Milestone | Target Date | Dependencies |
|---|---|---|
| VMware alternative POC complete | Q2 2026 | Vendor engagement; lab environment |
| SolarWinds replacement vendor selected | Q1 2026 | RFP completion; security review |
| All Windows 10 devices retired | Q2 2026 | Device procurement; field scheduling |
| Catalyst 3850 field refresh complete | Q4 2026 | Hardware delivery; field maintenance windows |
| SD-WAN deployed to all field sites | Q4 2026 | Circuit provisioning |
| SCCM fully decommissioned | Q3 2026 | Intune migration completion |
| New observability platform in production (corporate) | Q3 2026 | Platform deployment; integration |
| Hypervisor migration decision finalized | Q4 2026 | POC evaluation; cost analysis |
| Edge computing pilot operational | Q2 2027 | Hardware deployment; OT integration |
| Full observability rollout to field + OT | Q4 2027 | Agent deployment; OT security approval |
| Husky legacy infrastructure fully standardized | Q2 2027 | Cross-team coordination |
| Hypervisor migration complete (all workloads) | Q4 2028 | Application testing; change management |
| Intent-based networking operational | Q2 2029 | Network automation maturity |

### 4.3 Application Rationalization Plan
| Application | Action | Target Date | Savings (Estimated Annual) |
|---|---|---|---|
| SolarWinds Orion | Retire - Replace with modern observability platform | Q3 2026 | $150K (licensing) + risk reduction |
| VMware vSphere (Broadcom) | Migrate - Move to Nutanix AHV or Azure Stack HCI | Q4 2028 | $1.2M - $2M (licensing delta) |
| SCCM (ConfigMgr) | Retire - Complete migration to Intune standalone | Q3 2026 | $200K (server infrastructure + licensing) |
| F5 BIG-IP i5800 | Replace - Migrate to F5 rSeries or cloud LB | Q4 2026 | $80K (reduced hardware maintenance) |
| Commvault legacy media servers | Consolidate - Migrate to modern backup platform | Q2 2027 | $120K (hardware + tape reduction) |
| Legacy Husky monitoring tools | Retire - Consolidate into enterprise standard | Q2 2027 | $100K (duplicate licensing) |
| Windows 10 holdout devices | Retire - Replace with Windows 11 hardware | Q2 2026 | Risk reduction (unsupported OS) |

## 5. Investment Summary
| Initiative | CapEx (Estimated) | OpEx Annual (Estimated) | Priority | Year |
|---|---|---|---|---|
| VMware alternative POC & migration | $3.0M | $800K (net reduction) | Critical | 2026-2028 |
| SolarWinds replacement (observability) | $500K | $350K | High | 2026 |
| Catalyst 3850 field switch refresh | $600K | $0 (within existing support) | High | 2026 |
| F5 BIG-IP replacement | $300K | $60K | Medium | 2026 |
| SD-WAN Phase 2 expansion | $400K | $100K (circuit savings offset) | High | 2026 |
| Windows 10 device refresh | $250K | $0 | High | 2026 |
| Intune migration (SCCM decommission) | $100K | -$200K (savings) | Medium | 2026 |
| Edge computing pilot (5 sites) | $350K | $50K | Medium | 2027 |
| Network automation (DNA Center / Ansible) | $250K | $80K | Medium | 2027 |
| Wi-Fi 6E corporate/field upgrade | $450K | $0 | Low | 2027 |
| DC power & cooling optimization | $800K | -$150K (energy savings) | Low | 2028-2029 |
| **Total (3-year horizon)** | **~$7.0M** | **~$1.1M net annual** | | 2026-2029 |

## 6. Risks & Dependencies
| Risk / Dependency | Type | Likelihood | Impact | Mitigation |
|---|---|---|---|---|
| Broadcom VMware pricing increases beyond forecast | Risk | High | High | Accelerate alternative hypervisor evaluation; maintain negotiation leverage with multi-vendor strategy |
| Field site access constraints (weather, turnarounds) for hardware refresh | Risk | Medium | Medium | Coordinate with operations planning; align with spring/fall maintenance windows |
| OT team resistance to IT-driven changes in OT DMZ | Risk | Medium | High | Joint working group with OT & Automation; respect Purdue Model boundaries; involve IT Cyber Security EA |
| Vendor supply chain delays for network and compute hardware | Risk | Medium | Medium | Maintain strategic spares inventory; pre-order critical components with 6-month lead time |
| Staff skills gap for new hypervisor platform | Risk | Medium | Medium | Training program and vendor professional services during migration; retain VMware skills during transition |
| IT Cloud EA roadmap alignment for hybrid compute placement | Dependency | - | High | Regular sync with IT Cloud Portfolio Architect; joint architecture decision records |
| IT Cyber Security EA approval for observability platform in OT zones | Dependency | - | High | Early engagement in vendor selection; security architecture review |
| IT AI EA coordination for edge compute + ML workload requirements | Dependency | - | Medium | Joint edge computing working group; shared requirements gathering |
| Telecommunications carrier readiness for SD-WAN circuits at remote sites | Dependency | - | Medium | Engage Telus/Bell early; identify sites requiring satellite/LTE backup |
| Capital budget approval for multi-year infrastructure renewal | Dependency | - | Critical | Build strong business case with TCO analysis; align with corporate capital planning cycle |

## 7. Governance & Review
- **Roadmap review frequency**: Quarterly
- **Next review date**: Q2 2026 (April 2026)
- **Approval authority**: Team Leader (Chief Architect) + IT Senior Leadership
- **Architecture Review Board (ARB)**: All infrastructure changes >$100K require ARB approval
- **Change Advisory Board (CAB)**: Infrastructure changes follow ITIL change management via ServiceNow
- **Reporting cadence**: Monthly infrastructure health dashboard to IT Leadership; quarterly roadmap update to EA Team

## 8. Appendices

### 8.1 Conceptual Architecture - Target State (2029)

```
                         +-------------------+
                         |   Cloud (Azure/   |
                         |   AWS) - IaaS,    |
                         |   DR, Analytics   |
                         +--------+----------+
                                  |
                    +-------------+-------------+
                    |     Zscaler SASE /        |
                    |     SD-WAN Fabric          |
                    +---+-------+-------+-------+
                        |       |       |
              +---------+  +----+----+  +----------+
              | Calgary    | Field    |  | US Refinery|
              | Corporate  | Sites    |  | (Lima/     |
              | DC (HCI)   | (Edge +  |  |  Toledo)   |
              |            |  SD-WAN) |  |            |
              +-----+------+ +---+----+  +-----+-----+
                    |             |              |
              +-----+------+ +---+----+   +-----+-----+
              | Observability| | OT/SCADA|  | OT/SCADA  |
              | Platform     | | PI Hist |  | PI Hist   |
              +--------------+ +---------+  +-----------+
```

### 8.2 Key Vendor Relationships
| Vendor | Products | Contract Renewal | Strategic Importance |
|---|---|---|---|
| Broadcom (VMware) | vSphere, Horizon, vSAN | 2027 (ELA) | Under strategic review |
| Dell Technologies | PowerStore, VxRail, PowerEdge | Ongoing | Strategic partner |
| Cisco | Catalyst, Nexus, Meraki, ISR | Ongoing | Strategic partner |
| NetApp | ONTAP AFF/FAS | Ongoing | Strategic partner |
| Palo Alto Networks | PA-Series firewalls | 2027 | Strategic partner |
| F5 Networks | BIG-IP / rSeries | 2026 (renewal pending) | Tactical |
| Zscaler | ZIA, ZPA | 2027 | Strategic partner |
| AVEVA (OSIsoft) | PI System | Ongoing | Critical OT platform |
| Microsoft | Windows, Intune, M365 | EA renewal 2027 | Strategic partner |
| SolarWinds | Orion (to be replaced) | 2026 | Sunset |

### 8.3 Capability Heat Map Summary
| Capability Area | Maturity | Investment Need | Strategic Priority |
|---|---|---|---|
| Server Virtualization | High (but at risk due to VMware) | High | Critical |
| Storage (SAN/NAS) | High | Low | Maintain |
| Data Centre Networking | High | Medium | Medium |
| Campus/Field Networking | Medium | High | High |
| WAN / SD-WAN | Medium (in transition) | Medium | High |
| Firewall / Network Security | High | Low | Maintain |
| End-User Computing | Medium | Medium | Medium |
| VDI | High | Low | Maintain |
| Infrastructure Monitoring | Low | High | Critical |
| Backup & DR | Medium | Medium | Medium |
| OT/IT Convergence | Medium | Medium | High |
| Edge Computing | Low | High | Medium |
| Network Automation | Low | Medium | Medium |
