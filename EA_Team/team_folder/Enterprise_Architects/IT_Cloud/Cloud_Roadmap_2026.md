# Enterprise Architecture Roadmap - IT Cloud

**Domain:** IT Cloud (AWS & Azure)
**Portfolio Architect:** IT Cloud Portfolio Architect
**Version:** 1.0
**Last Updated:** 2026-02-07
**Planning Horizon:** 2026 - 2029

---

## 1. Domain Overview

### 1.1 Scope & Boundaries
This domain covers all cloud platform services consumed by Cenovus Energy across Amazon Web Services (AWS) and Microsoft Azure, including:

- **AWS**: Landing zones (Control Tower), workload hosting (EC2, ECS, EKS), analytics services (EMR, Redshift, Athena, Glue), IoT for field/SAGD operations (IoT Core, Greengrass), S3 data lakes, and serverless compute (Lambda)
- **Azure**: Microsoft 365 ecosystem, Entra ID (Azure AD) for hybrid identity, Azure DevOps for CI/CD pipelines, Azure Data Factory, Power Platform, and Azure Arc for hybrid management
- **Hybrid Cloud Strategy**: Multi-cloud governance, workload placement framework, cloud interconnects (Direct Connect, ExpressRoute), and on-premises-to-cloud integration
- **Cloud-Native Services**: Container orchestration, serverless architectures, managed databases (RDS, Aurora, Azure SQL), event-driven architectures (EventBridge, Service Bus)
- **FinOps**: Cloud cost optimization, showback/chargeback models, Reserved Instances, Savings Plans, and Azure Reservations

**Out of scope:** On-premises data centre infrastructure (owned by IT Infrastructure domain), cybersecurity tooling selection (owned by IT Cyber Security domain), application-level business logic (owned by respective application domains).

### 1.2 Strategic Alignment
Cenovus Energy's corporate strategy focuses on safe, reliable operations, cost discipline, and responsible resource development. The cloud domain supports this through:

- **Operational Excellence**: Cloud-hosted SCADA data analytics and IoT telemetry to improve SAGD steam-oil ratio and production optimization
- **Cost Discipline**: FinOps practices to manage cloud spend; right-sizing workloads to reduce total cost of ownership
- **Digital Transformation**: Enabling advanced analytics, machine learning, and GenAI workloads that require elastic compute
- **Workforce Enablement**: M365 and Azure-based collaboration tools for a distributed workforce across oil sands sites, refineries, and the Calgary head office
- **Sustainability Reporting**: Cloud-hosted ESG data platforms to meet regulatory disclosure requirements (Canadian Securities Administrators, SEC climate rules)
- **Resilience & Business Continuity**: Multi-region cloud architectures ensuring operational continuity for critical production and trading systems

### 1.3 Key Stakeholders
| Stakeholder | Role | Business Unit |
|-------------|------|---------------|
| VP, Information Technology | Executive Sponsor | IT |
| Director, IT Infrastructure & Operations | Operational Partner | IT |
| Director, IT Security & Compliance | Security Governance | IT |
| Manager, Cloud Operations | Day-to-Day Operations Lead | IT |
| VP, Production Operations | Business Consumer - Upstream | Oil Sands & Conventional |
| VP, Downstream Operations | Business Consumer - Downstream | Refining & Upgrading |
| Director, Finance & Planning | FinOps & Cost Governance | Finance |
| Director, Supply Chain | Business Consumer - SCM | Supply Chain |
| Director, HSE & Sustainability | ESG Data Consumer | HSE |

## 2. Current State Assessment

### 2.1 Application Portfolio
| Application / Service | Business Capability | Functional Capability | Status | Health |
|----------------------|--------------------|-----------------------|--------|--------|
| AWS Control Tower (Landing Zone) | IT Governance | Multi-account management, guardrails | Production | Green |
| AWS IoT Core + Greengrass | Production Optimization | Field telemetry ingestion from SAGD well pads | Production | Yellow |
| AWS S3 Data Lake | Enterprise Data Management | Centralized raw/curated data storage | Production | Green |
| AWS EMR / Glue | Data Analytics | Big data processing, ETL pipelines | Production | Yellow |
| AWS Redshift | Business Intelligence | Enterprise data warehouse | Production | Green |
| AWS EC2 / ECS | Workload Hosting | Application compute (various workloads) | Production | Green |
| AWS Lambda | Event Processing | Serverless compute for event-driven workloads | Production | Green |
| Azure Entra ID (Azure AD) | Identity & Access | Hybrid identity, SSO, MFA, conditional access | Production | Green |
| Microsoft 365 (E5) | Workforce Collaboration | Email, Teams, SharePoint, OneDrive | Production | Green |
| Azure DevOps | Software Delivery | CI/CD pipelines, repos, artifact management | Production | Green |
| Power Platform | Citizen Development | Power Apps, Power Automate, Power BI | Production | Yellow |
| Azure Data Factory | Data Integration | Cloud-based ETL/ELT orchestration | Production | Green |
| Azure Arc | Hybrid Management | On-prem server management via Azure portal | Emerging | Yellow |
| AWS SageMaker | Machine Learning | ML model training and deployment | Emerging | Yellow |
| Amazon Bedrock | Generative AI | Foundation model access for GenAI use cases | Emerging | Yellow |

### 2.2 Technology Stack
| Layer | Technology | Version / SKU | End of Support |
|-------|-----------|---------------|----------------|
| Identity | Azure Entra ID | P2 | Evergreen |
| Collaboration | Microsoft 365 | E5 | Evergreen (annual renewal) |
| Landing Zone | AWS Control Tower | v3.x | Evergreen |
| Compute | AWS EC2 | Various (m6i, c6i, r6i) | Current generation |
| Containers | AWS ECS / Fargate | Current | Evergreen |
| Kubernetes | AWS EKS | 1.29 | Dec 2025 (upgrade needed) |
| Data Lake | AWS S3 + Lake Formation | Current | Evergreen |
| Data Warehouse | AWS Redshift Serverless | Current | Evergreen |
| ETL | AWS Glue | 4.0 | Evergreen |
| Serverless | AWS Lambda | Python 3.11, Node 20 | Python 3.11 EOL Oct 2027 |
| IoT | AWS IoT Core + Greengrass | v2.x | Evergreen |
| CI/CD | Azure DevOps | Cloud (SaaS) | Evergreen |
| Low-Code | Power Platform | Current | Evergreen |
| Networking | AWS Direct Connect + Azure ExpressRoute | 10 Gbps / 1 Gbps | Contract renewal 2027 |

### 2.3 Strengths
- Mature AWS landing zone with multi-account structure (production, staging, sandbox, shared services) enforced via Control Tower guardrails
- Entra ID P2 deployed enterprise-wide with conditional access policies and MFA, providing strong hybrid identity foundation
- Established S3 data lake architecture supporting upstream production analytics and downstream operational reporting
- M365 E5 deployed across the enterprise with Teams adoption exceeding 90%
- FinOps practice initiated with AWS Cost Explorer and monthly cost review cadence
- Direct Connect and ExpressRoute circuits providing reliable hybrid connectivity from Calgary data centre to both clouds
- Azure DevOps standardized as the enterprise CI/CD platform with pipeline templates for common workloads

### 2.4 Gaps & Pain Points
| # | Gap | Business Impact | Priority |
|---|-----|-----------------|----------|
| 1 | No unified multi-cloud governance framework; AWS and Azure managed independently | Inconsistent policies, duplicated effort, compliance risk | High |
| 2 | IoT data pipeline from SAGD well pads has latency and reliability issues in remote locations | Delayed production optimization decisions | High |
| 3 | EKS cluster on outdated Kubernetes version; no automated upgrade lifecycle | Security vulnerabilities, potential compliance gaps | High |
| 4 | No formal FinOps tooling or automated anomaly detection for cloud spend | Unplanned cost overruns, lack of business unit chargeback accuracy | Medium |
| 5 | Power Platform governance is weak; citizen-developed apps lack lifecycle management | Shadow IT risk, data leakage potential | Medium |
| 6 | Limited disaster recovery testing for cloud-hosted workloads | Unknown RTO/RPO compliance for critical systems | Medium |
| 7 | GenAI adoption is ad-hoc; no enterprise guardrails for foundation model usage | Data privacy risk, inconsistent model governance | High |
| 8 | Lack of cloud-native observability stack; monitoring fragmented across CloudWatch, Azure Monitor, and on-prem tools | Slow incident response, poor cross-cloud visibility | Medium |
| 9 | Data lake lacks formal data cataloguing and data quality framework | Analysts spend significant time finding/validating data | Medium |
| 10 | No formalized cloud migration factory for remaining on-prem workloads | Slow migration velocity, extended data centre dependency | Low |

### 2.5 Technical Debt
| Item | Risk | Effort to Remediate | Priority |
|------|------|---------------------|----------|
| EKS v1.29 (past EOL) | Security patches not available; compliance audit findings | Medium - upgrade to 1.31+ with blue/green deployment | High |
| Legacy EC2 instances on previous-gen instance types (m5, c5) | ~20% cost premium vs current gen; no Graviton adoption | Medium - re-platform to m7g/c7g (Graviton3) | Medium |
| Orphaned S3 buckets and unused EBS volumes | Unnecessary storage costs (~$15K/month estimated) | Low - scripted cleanup | High |
| Azure AD Connect v1 (legacy sync agent) | Approaching EOL; replaced by Cloud Sync | Low - migrate to Entra Cloud Sync | Medium |
| Multiple standalone AWS accounts not under Control Tower | Inconsistent guardrails, security gaps | Medium - enroll accounts into Control Tower | High |
| Untagged cloud resources (~30% of AWS estate) | FinOps attribution impossible for untagged resources | Medium - enforce tagging policy via SCP | Medium |

## 3. Future State Vision

### 3.1 Target Architecture
The target cloud architecture for Cenovus Energy is a **well-governed multi-cloud environment** that leverages best-of-breed services from AWS and Azure while maintaining a unified governance, security, and cost management framework.

**AWS** serves as the primary platform for:
- Production workload hosting (compute, containers, serverless)
- IoT data ingestion and edge computing for SAGD and conventional operations
- Enterprise data lake, data warehouse, and advanced analytics (including ML/AI)
- High-performance computing for reservoir simulation

**Azure** serves as the primary platform for:
- Enterprise identity (Entra ID) and access management
- Workforce productivity (M365, Power Platform)
- Developer tooling (Azure DevOps)
- Hybrid management of on-premises resources (Azure Arc)

**Key characteristics of the future state:**
- Unified multi-cloud governance using a Cloud Center of Excellence (CCoE) model
- Automated FinOps with real-time dashboards, anomaly detection, and business-unit chargeback
- Enterprise GenAI platform with guardrails, model registry, and approved use-case patterns
- Resilient IoT architecture with edge processing at remote well pad locations
- Cloud-native observability platform providing cross-cloud monitoring and AIOps
- Infrastructure-as-Code (IaC) for all cloud resources with policy-as-code enforcement
- Zero Trust network architecture for cloud workloads

### 3.2 Guiding Principles
1. **Cloud-First, Not Cloud-Only**: New workloads default to cloud unless a justified exception exists (e.g., OT latency requirements, regulatory constraints). Existing on-prem workloads migrate based on business value.
2. **Best-of-Breed Multi-Cloud**: Use AWS for compute/data/IoT workloads and Azure for identity/productivity. Avoid unnecessary duplication of capabilities across clouds.
3. **Govern Centrally, Execute Locally**: The CCoE sets policies and guardrails; delivery teams have autonomy within those boundaries.
4. **Automate Everything**: Infrastructure-as-Code, policy-as-code, CI/CD pipelines, and automated remediation are the default.
5. **Cost Transparency**: Every cloud resource is tagged and attributable to a business unit; FinOps is everyone's responsibility.
6. **Security by Design**: Workloads comply with Zero Trust principles; data classification drives encryption and access controls.
7. **Sustainable by Design**: Prefer regions and instance types with lower carbon intensity; track cloud carbon footprint.

### 3.3 Target Application Portfolio
| Application / Service | Business Capability | Functional Capability | Change |
|----------------------|--------------------|-----------------------|--------|
| AWS Control Tower (Landing Zone) | IT Governance | Multi-account management | Enhance - add all accounts, strengthen SCPs |
| AWS IoT Core + Greengrass v2 | Production Optimization | Field telemetry (SAGD, conventional) | Enhance - edge ML, offline resilience |
| AWS S3 Data Lake + Lake Formation | Enterprise Data Management | Data lake with cataloguing & governance | Enhance - add data quality framework |
| AWS Redshift Serverless | Business Intelligence | Enterprise data warehouse | Retain |
| AWS EKS (Kubernetes) | Workload Hosting | Container orchestration | Enhance - automated version lifecycle |
| AWS SageMaker | Machine Learning | ML model training & serving | Enhance - MLOps pipeline |
| Amazon Bedrock + Guardrails | Generative AI | Enterprise GenAI platform | New - establish enterprise GenAI platform |
| AWS Graviton-based Compute | Workload Hosting | Cost-optimized ARM compute | New - migrate eligible workloads |
| Azure Entra ID | Identity & Access | Hybrid identity, governance | Enhance - Entra Cloud Sync, Verified ID |
| Microsoft 365 (E5) | Workforce Collaboration | Productivity suite | Retain |
| Azure DevOps | Software Delivery | CI/CD, repos, artifacts | Retain |
| Power Platform (Managed Environments) | Citizen Development | Low-code with governance | Enhance - managed environments, DLP |
| Datadog / Grafana Cloud | Observability | Cross-cloud monitoring & AIOps | New - unified observability platform |
| CloudHealth / FOCUS | FinOps | Cost management & chargeback | New - automated FinOps tooling |
| HashiCorp Terraform Cloud | IaC | Multi-cloud infrastructure provisioning | New - enterprise IaC platform |
| Azure Arc | Hybrid Management | Unified on-prem + cloud management | Enhance - extend to OT servers |
| Legacy on-prem app servers | Various | Various legacy workloads | Migrate / Retire (phased) |

## 4. Transition Roadmap

### 4.1 Roadmap Swimlanes

#### Near Term (0-12 months) - Q1 2026 through Q4 2026
| Initiative | Description | Dependencies | Status |
|-----------|-------------|--------------|--------|
| EKS Version Lifecycle Automation | Upgrade EKS to v1.31+; implement automated upgrade pipeline with blue/green strategy | Azure DevOps pipeline templates | Planned |
| Multi-Cloud Governance Framework | Establish CCoE operating model; define unified tagging taxonomy, naming conventions, and policy-as-code baseline | Stakeholder alignment with IT Security | Planned |
| FinOps Foundation | Deploy CloudHealth (or equivalent); implement tagging enforcement via AWS SCPs; deliver first chargeback report to business units | Tagging taxonomy from governance initiative | Planned |
| Orphaned Resource Cleanup | Script and execute cleanup of unused S3 buckets, EBS volumes, and unattached ENIs | FinOps tooling for identification | Planned |
| Entra Cloud Sync Migration | Replace legacy Azure AD Connect with Entra Cloud Sync for hybrid identity synchronization | Entra ID P2 licensing (in place) | Planned |
| Power Platform Managed Environments | Enable managed environments; deploy DLP policies; inventory existing citizen apps | Entra ID governance integration | Planned |
| GenAI Guardrails & Governance | Define acceptable use policy for GenAI; deploy Amazon Bedrock with Guardrails for approved use cases; establish model registry | IT Security approval, data classification | Planned |
| IoT Edge Resilience (Phase 1) | Deploy Greengrass v2 with local ML inference at 5 pilot SAGD well pads; implement store-and-forward for connectivity gaps | OT team coordination, edge hardware procurement | Planned |
| Control Tower Account Enrollment | Enroll remaining standalone AWS accounts into Control Tower; apply baseline SCPs | Account owner coordination | Planned |
| Graviton Migration (Wave 1) | Migrate non-production workloads to Graviton3 (m7g/c7g) instances for cost and sustainability benefits | Application compatibility testing | Planned |

#### Medium Term (12-24 months) - Q1 2027 through Q4 2027
| Initiative | Description | Dependencies | Status |
|-----------|-------------|--------------|--------|
| Unified Observability Platform | Deploy Datadog or Grafana Cloud for cross-cloud monitoring; integrate CloudWatch, Azure Monitor, and on-prem sources | FinOps approval for tooling spend | Planned |
| IoT Edge Expansion (Phase 2) | Expand Greengrass edge deployment to all SAGD and conventional well pads (~50 sites); integrate with production optimization models | Phase 1 lessons learned, edge hardware rollout | Planned |
| Data Lake Governance & Quality | Implement AWS Lake Formation fine-grained access; deploy data quality framework (Great Expectations or Deequ); establish data catalogue | Data stewardship model from Enterprise Apps domain | Planned |
| Terraform Cloud Enterprise | Roll out Terraform Cloud as the enterprise IaC platform; migrate existing CloudFormation templates; enforce policy-as-code (Sentinel) | CCoE governance framework | Planned |
| Graviton Migration (Wave 2) | Migrate production workloads to Graviton3/4 instances; target 60% Graviton adoption | Wave 1 validation, application testing | Planned |
| Cloud DR Automation | Implement automated disaster recovery for Tier 1 and Tier 2 cloud workloads using AWS Elastic Disaster Recovery and Azure Site Recovery | Business continuity classification (IT Infra domain) | Planned |
| MLOps Pipeline Maturity | Establish SageMaker MLOps pipelines with model versioning, A/B testing, and automated retraining for production ML models | Data lake governance, ML team readiness | Planned |
| Azure Arc for OT | Extend Azure Arc management to refinery and upgrader OT servers for unified patching and compliance visibility | OT/IT convergence strategy (IT Infra domain) | Planned |

#### Long Term (24-36 months) - Q1 2028 through Q4 2028
| Initiative | Description | Dependencies | Status |
|-----------|-------------|--------------|--------|
| Cloud-Native Refactoring | Refactor top 10 monolithic applications to container/serverless architectures on AWS | Application domain roadmaps, developer training | Planned |
| Advanced FinOps & Sustainability | Implement unit economics (cost per barrel produced/refined); integrate cloud carbon footprint into ESG reporting | FinOps maturity, ESG reporting platform | Planned |
| Multi-Region Active-Active | Establish active-active architecture in AWS ca-central-1 and us-east-1 for critical production and trading systems | DR automation maturity, network redesign | Planned |
| Autonomous IoT Operations | Edge-based autonomous control loops for routine SAGD operations (steam trap monitoring, pump optimization) with human-in-the-loop overrides | IoT Phase 2 completion, OT safety validation | Planned |
| Zero Trust Cloud Network | Full implementation of Zero Trust microsegmentation for all cloud workloads; service mesh for inter-service communication | Security architecture, identity maturity | Planned |
| Data Mesh Architecture | Transition from centralized data lake to federated data mesh model with domain-owned data products | Data governance maturity, organizational readiness | Planned |

### 4.2 Key Milestones
| Milestone | Target Date | Dependencies |
|-----------|-------------|--------------|
| CCoE operating model approved and staffed | Q2 2026 | Executive sponsorship |
| All AWS accounts under Control Tower governance | Q3 2026 | Account enrollment initiative |
| First FinOps chargeback report published | Q3 2026 | Tagging enforcement, CloudHealth deployment |
| GenAI enterprise platform (Bedrock) live with first 3 use cases | Q4 2026 | GenAI governance, security approval |
| IoT edge deployment at all SAGD sites complete | Q4 2027 | Phase 1 & 2 execution |
| 60% Graviton adoption across AWS compute | Q4 2027 | Graviton migration waves |
| Unified observability platform operational | Q2 2027 | Tooling procurement |
| Terraform Cloud as sole IaC platform | Q4 2027 | Template migration |
| Cloud-native refactoring of top 10 apps complete | Q4 2028 | Application domain alignment |
| Cloud carbon footprint integrated into ESG reporting | Q2 2028 | Sustainability reporting platform |

### 4.3 Application Rationalization Plan
| Application / Service | Action | Target Date | Savings (Annual) |
|----------------------|--------|-------------|-----------------|
| Previous-gen EC2 instances (m5/c5) | Modernize - migrate to Graviton (m7g/c7g) | Q4 2027 | ~$400K (20% compute savings) |
| Orphaned S3 buckets & unused EBS | Retire - scripted cleanup | Q2 2026 | ~$180K |
| Azure AD Connect (legacy sync) | Replace - migrate to Entra Cloud Sync | Q3 2026 | Reduced support overhead |
| Standalone AWS accounts (unmanaged) | Consolidate - enroll in Control Tower | Q3 2026 | Risk reduction, audit savings |
| Multiple monitoring tools (fragmented) | Consolidate - unified observability platform | Q2 2027 | ~$120K (tool consolidation) |
| Legacy CloudFormation templates | Migrate - move to Terraform Cloud | Q4 2027 | Developer productivity gain |
| On-prem app servers (migration candidates) | Migrate - cloud rehost/replatform | Q4 2028 | ~$300K (data centre footprint reduction) |

## 5. Investment Summary
| Initiative | CapEx | OpEx (Annual) | Priority | Year |
|-----------|-------|---------------|----------|------|
| CCoE Establishment & Governance Tooling | $150K | $80K | High | 2026 |
| FinOps Tooling (CloudHealth/FOCUS) | $50K | $120K | High | 2026 |
| EKS Lifecycle Automation | $75K | $30K | High | 2026 |
| GenAI Platform (Bedrock + Guardrails) | $200K | $350K | High | 2026 |
| IoT Edge Expansion (Phase 1 + 2) | $500K | $200K | High | 2026-2027 |
| Unified Observability Platform | $100K | $250K | Medium | 2027 |
| Terraform Cloud Enterprise | $50K | $100K | Medium | 2027 |
| Graviton Migration (Wave 1 + 2) | $100K | -$400K (savings) | Medium | 2026-2027 |
| Cloud DR Automation | $200K | $80K | Medium | 2027 |
| Data Lake Governance & Quality | $150K | $60K | Medium | 2027 |
| Cloud-Native Refactoring (Top 10 Apps) | $800K | $100K | Medium | 2028 |
| Multi-Region Active-Active | $400K | $300K | Low | 2028 |
| **Total** | **~$2.78M** | **~$1.27M** | | 2026-2028 |

*Note: Graviton migration generates net savings of ~$400K/year, partially offsetting new OpEx. FinOps initiatives target 15-20% reduction in overall cloud spend baseline.*

## 6. Risks & Dependencies
| Risk / Dependency | Type | Likelihood | Impact | Mitigation |
|-------------------|------|-----------|--------|------------|
| Cloud spend grows faster than production revenue in downturn scenario | Risk | Medium | High | FinOps automated alerts; pre-purchased commitments (RIs/Savings Plans); shutdown policies for non-prod |
| Skilled cloud engineering talent shortage in Calgary market | Risk | High | High | Invest in training/certification; partner with managed service providers; leverage IaC to reduce toil |
| AWS or Azure major region outage affecting ca-central-1 | Risk | Low | High | Multi-region DR strategy; critical workloads replicate to us-east-1 |
| OT/IT convergence delays affecting IoT edge deployments | Dependency | Medium | Medium | Joint OT/IT steering committee; phased approach starting with non-safety-critical systems |
| Cybersecurity requirements slow cloud adoption velocity | Risk | Medium | Medium | Embed security in CCoE; pre-approved reference architectures; shift-left security in pipelines |
| Regulatory changes to data residency (Canadian data sovereignty) | Risk | Low | High | Default to ca-central-1; monitor regulatory landscape; maintain data residency inventory |
| GenAI model accuracy/hallucination risk in operational decisions | Risk | Medium | High | Human-in-the-loop for all operational GenAI; validation framework; approved use-case registry |
| Vendor lock-in from deep adoption of proprietary cloud services | Risk | Medium | Medium | Prefer open standards where feasible; containerize workloads; abstract with Terraform |
| Data lake quality issues undermine analytics and ML initiatives | Dependency | Medium | High | Data quality framework (Great Expectations); data stewardship; automated profiling |
| IT Infrastructure domain data centre exit timeline | Dependency | Medium | Medium | Coordinate migration planning; maintain hybrid connectivity capacity |

## 7. Governance & Review
- **Roadmap review frequency:** Quarterly (aligned with IT Architecture Review Board cycle)
- **Next review date:** Q2 2026 (April 2026)
- **Approval authority:** Team Leader (Chief Architect) + VP, Information Technology
- **Change management:** Material scope changes require ARB review; budget changes follow IT capital planning process
- **Reporting:** Monthly cloud spend report to IT Leadership; quarterly roadmap progress to IT Steering Committee
- **CCoE cadence:** Bi-weekly CCoE working sessions once established

## 8. Appendices

### Appendix A: AWS Account Structure
```
AWS Organization (Control Tower)
├── Management Account
├── Security OU
│   ├── Log Archive Account
│   └── Audit Account
├── Infrastructure OU
│   ├── Shared Services Account (networking, DNS, transit gateway)
│   └── Network Hub Account
├── Workloads OU
│   ├── Production OU
│   │   ├── Upstream Production Account
│   │   ├── Downstream Production Account
│   │   ├── Data Platform Production Account
│   │   └── Corporate Apps Production Account
│   ├── Staging OU
│   │   └── [Mirror of Production accounts]
│   └── Development OU
│       └── [Mirror of Production accounts]
├── Sandbox OU
│   └── Innovation / Experimentation Accounts
└── Suspended OU
    └── Decommissioned accounts
```

### Appendix B: Cloud Connectivity Architecture
```
Calgary Data Centre
├── AWS Direct Connect (10 Gbps) ──→ AWS ca-central-1
│   └── Transit Gateway ──→ All VPCs
├── Azure ExpressRoute (1 Gbps) ──→ Azure Canada Central
│   └── Virtual WAN Hub ──→ All VNets
└── Site-to-Site VPN (backup) ──→ Both clouds

Field Sites (SAGD / Conventional)
├── Starlink / LTE / Microwave ──→ AWS IoT Core (MQTT)
└── Greengrass Edge Devices ──→ Local processing + store-and-forward
```

### Appendix C: FinOps Maturity Model Target
| FinOps Capability | Current Maturity | Target (2027) |
|------------------|-----------------|---------------|
| Cost Allocation & Tagging | Crawl | Run |
| Forecasting & Budgeting | Crawl | Walk |
| Rate Optimization (RIs/SPs) | Walk | Run |
| Usage Optimization (right-sizing) | Crawl | Walk |
| Anomaly Detection | None | Walk |
| Unit Economics | None | Crawl |
| Organizational Adoption | Crawl | Walk |
| Cloud Sustainability | None | Crawl |

### Appendix D: Vendor Landscape
| Capability | Primary Vendor | Alternative Considered | Decision Rationale |
|-----------|---------------|----------------------|-------------------|
| Public Cloud (Compute/Data) | AWS | Azure, GCP | Established landing zone; IoT and data lake maturity |
| Identity & Productivity | Microsoft Azure / M365 | Google Workspace | Enterprise-wide M365 investment; Entra ID hybrid identity |
| CI/CD | Azure DevOps | GitHub Actions, GitLab | Existing enterprise license; team familiarity |
| IaC | Terraform (HashiCorp) | Pulumi, CloudFormation | Multi-cloud support; industry standard |
| Observability | Datadog (candidate) | Grafana Cloud, Splunk | Cross-cloud support; AIOps capabilities; evaluate in 2027 |
| FinOps | CloudHealth (candidate) | Apptio Cloudability, AWS native | Multi-cloud visibility; FOCUS standard alignment |
| GenAI Foundation Models | Amazon Bedrock | Azure OpenAI Service | AWS primary cloud; model diversity (Anthropic, Meta, Cohere) |
