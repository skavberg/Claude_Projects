# EA Governance Process - Cenovus Energy

**Process Owner:** IT Architecture Team Leader
**Version:** 1.0
**Effective Date:** 2026-02-07

---

## 1. Architecture Review Board (ARB)

### Purpose
The ARB provides governance over new technology introductions, solution designs, and architectural decisions to ensure alignment with Cenovus Energy's IT strategy and standards.

### Cadence
- Bi-weekly standing meeting
- Ad-hoc sessions for urgent requests

### Participants
- Team Leader (Chair)
- Relevant Portfolio Architect(s)
- Solution Architect (presenting)
- IT Senior Leadership representative (as needed)
- Business stakeholder (as needed)

### Review Types
| Type | Trigger | Required Artefacts |
|------|---------|-------------------|
| New Application Request | New software purchase or build | NAR Form, Vendor Assessment |
| Conceptual Design Review | New project initiation | Conceptual Design Document |
| Solution Design Review | Pre-implementation gate | Solution Design Document, TCO Report |
| Architecture Exception | Deviation from standards | Exception Request with justification |
| Roadmap Review | Quarterly cycle | Updated Domain Roadmap |

### Decision Outcomes
- **Approved** - Proceed as designed
- **Conditionally Approved** - Proceed with stated conditions
- **Returned** - Revise and resubmit
- **Rejected** - Do not proceed; rationale documented

## 2. New Application Request Process

```
Requestor submits NAR form
        |
        v
Portfolio Architect assesses
(portfolio overlap, strategic fit,
 security, integration, cost)
        |
        v
ARB Review & Decision
        |
    +---+---+---+
    |   |   |   |
  Approved  Conditional  Returned  Rejected
    |       |            |         |
    v       v            v         v
  Proceed  Address      Revise    Document
  to SD    conditions   & resubmit rationale
```

## 3. Solution Design Lifecycle

```
1. Conceptual Design  -->  ARB Review (Gate 1)
        |
2. Solution Design    -->  ARB Review (Gate 2)
        |
3. TCO & Financial    -->  Finance Review
   Viability Report
        |
4. Implementation     -->  Architecture oversight
        |
5. Post-Implementation --> Lessons learned, portfolio update
   Review
```

## 4. EA Roadmap Governance

### Annual Cycle
- **Q1:** Roadmap refresh aligned to corporate planning
- **Q2:** Mid-year progress review
- **Q3:** Investment planning for next fiscal year
- **Q4:** Year-end assessment and carry-forward items

### Quarterly Reviews
Each Portfolio Architect presents domain roadmap status:
- Initiatives completed / in progress / deferred
- New items identified
- Risk and dependency updates
- Budget utilization

## 5. Standards & Decision Records

### New Standard Proposal
1. Portfolio Architect drafts standard
2. Peer review by EA team
3. ARB approval
4. Published to `team_public/Standards/`

### Architecture Decision Records
1. Decision identified during design or review
2. ADR drafted using template
3. Reviewed by relevant Portfolio Architect(s)
4. Approved by Team Leader
5. Published to `team_public/Decision_Records/`

## 6. Stakeholder Engagement Model

| Stakeholder Group | EA Engagement | Frequency |
|-------------------|---------------|-----------|
| IT Senior Leadership | Strategy alignment, roadmap reviews | Monthly |
| IT Delivery Managers | Project support, design reviews | As needed |
| Business Unit Leads | Capability mapping, initiative intake | Quarterly |
| Vendors / Partners | Technology assessments, POCs | As needed |
| Security & Compliance | Security reviews, risk assessments | Per project |
