# Cenovus Energy - IT Architecture Team Charter

**Organization:** Cenovus Energy Inc.
**Location:** Calgary, Alberta, Canada
**Industry:** Oil & Gas (Integrated - Upstream & Downstream)
**Team:** IT Architecture - Enterprise Architecture & Solution Architecture

---

## Mission Statement

The IT Architecture team provides strategic technology leadership, governance, and solution design services to Cenovus Energy. We align IT investments with business strategy, ensure architectural coherence across all technology domains, and enable the digital transformation of our oil and gas operations from wellhead to market.

## Team Structure

### Enterprise Architects (EA) Group
Portfolio Architects who own domain-level architecture, roadmaps, and governance:

| Domain | Scope |
|--------|-------|
| IT Infrastructure | Data centres, networking, compute, storage, end-user computing, SCADA/OT convergence |
| IT Cloud | AWS & Azure cloud platforms, hybrid cloud strategy, cloud-native services, FinOps |
| IT Cyber Security | Zero Trust architecture, OT security, identity & access management, threat modelling |
| IT Artificial Intelligence | ML/AI platforms, data science infrastructure, GenAI governance, intelligent automation |
| Corporate Applications | HR, Finance, Supply Chain, ERP (SAP), corporate collaboration tools |
| Upstream Applications | Drilling, completions, production, reservoir management, field data capture |
| Downstream Applications | Refining, upgrading, pipeline/transportation, marketing & trading systems |
| Enterprise Applications | Integration platforms, master data management, enterprise reporting, GIS |

### Solution Architects (SA) Group
Solution Architects who translate EA direction into implementable designs for projects and initiatives.

### Supporting Roles
- **Documentation Specialist** - Maintains architectural artefacts, templates, and knowledge base
- **Process Advisor** - Ensures EA governance processes, review gates, and standards compliance

## Core Functions

### 1. Application-to-Capability Mapping
- Map all applications to **Functional Capabilities** (what the application does)
- Map all applications to **Business Capabilities** (what business outcome it supports)
- Maintain the enterprise application portfolio with current-state and future-state views

### 2. Conceptual Design & Solution Architecture
- Develop conceptual designs for new projects and initiatives
- Create detailed solution designs using standard templates
- Conduct architecture review boards (ARB) for new application requests

### 3. Financial Analysis
- Develop **Total Cost of Ownership (TCO)** analyses for proposed solutions
- Produce **Financial Viability Reports** covering capital, operating, and run costs
- Support business case development with technology cost modelling

### 4. EA Roadmaps & Strategy
- Each Portfolio Architect maintains a domain roadmap (current state, transition, future state)
- Roadmaps align to the IT Strategic Plan and Cenovus corporate strategy
- Engage business stakeholders and IT managers relevant to each domain

### 5. Governance & Standards
- Approve or reject new application requests through the ARB process
- Maintain technology standards, reference architectures, and design patterns
- Publish and enforce architectural decision records (ADRs)

### 6. Stakeholder Engagement
- Team Leader interfaces with IT Senior Leadership to shape enterprise IT strategy
- Portfolio Architects engage business unit leads and IT delivery managers
- Regular reporting on architectural health, technical debt, and rationalization opportunities

## Governance Framework

```
IT Senior Leadership
        |
   Team Leader (Chief Architect)
        |
   +----+----+
   |         |
   EA Group  SA Group
   |         |
   Portfolio  Solution
   Architects Architects
```

## Key Deliverables

- Enterprise Architecture Roadmaps (per domain)
- Conceptual Design Documents
- Solution Design Documents
- Total Cost of Ownership Reports
- Financial Viability Assessments
- Architecture Decision Records
- Application Portfolio & Capability Maps
- Technology Standards & Reference Architectures
- New Application Request Approvals
- Meeting Minutes & Status Reports

## Working Agreements

- All designs follow standard templates in `team_public/Standards/`
- Decision records are published to `team_public/Decision_Records/`
- Meeting minutes are stored in `Working/Meeting_Minutes/`
- Team goals and OKRs are tracked in `Working/team_goals/`
- Roadmaps are published to `team_public/Roadmaps/`
