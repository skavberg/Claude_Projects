# Physics Team — Project Status
**Last updated:** 2026-02-07, Session 2

## Team
- **team-lead** — Session coordinator
- **team-leader** — Task coordination and workflow management
- **doc-agent** — LaTeX document specialist, arXiv compliance, only agent that publishes to output/
- **graphic-agent** — Figures, diagrams, illustrations (directed by doc-agent only)
- **math-agent** — Derivations, proofs, equations
- **physics-agent** — Literature, references, physics research

## Current Project
**Paper:** "The Universe as a Condensate"
**Foundation:** Based on the mathematics of the Planck field (reference Paper 3)
**Foundation:** Based on the architectural framework: "The Observable Universe as a Condensate Expanding into a Universal Protofluid"
**Status:** Session 2 — Draft paper v01 created from architectural framework; team ready for derivation work

## Reference Papers (by Robin Skavberg)
Located in `team_folder/doc-agent/reference_docs/`:

1. **01_Mechanical_Route_to_G/** — "A Mechanical Route to G: Matching Field Stress-Energy to the Einstein-Hilbert Coupling"
   - Zenodo: https://zenodo.org/records/18496765
   - Files: V8.tex, V8-V01.01.tex, PDF

2. **02_Gravitational_Coupling/** — "A Mechanical Extension of General Relativity: The Singularity in Equilibrium"
   - Zenodo: https://zenodo.org/records/18393278
   - DOI: 10.5281/zenodo.18393278
   - Files: .tex, PDF

3. **03_Planck_Field_Hulse_Taylor/** — "Planck Field - Resolving Hulse-Taylor Binary"
   - Zenodo: https://zenodo.org/records/18462909
   - Files: PDF only (no tex source)

## Folder Structure
```
team_folder/
  doc-agent/
    draft_papers/        — WIP paper drafts
    meeting_minutes/     — Session notes (LaTeX)
    reference_docs/      — Three Skavberg reference papers
  graphic-agent/         — Draft figures
  math-agent/            — Derivations, proofs
  physics-agent/         — Research, literature
  team-leader/           — Coordination

output/
  papers/                — Final arXiv PDFs and .tex
  references/            — Bibliography and .bib
  figures/               — Final figures
```

## Rules
- Only doc-agent writes to `output/`
- Only doc-agent directs graphic-agent on figure creation
- All collaboration happens in `team_folder/`

## Session 1 Action Items
- [x] All agents: Read the three reference papers (especially Paper 3 — Planck field)
- [x] doc-agent: Set up draft paper in `draft_papers/`
- [ ] math-agent: Review Planck field math, prepare for derivations
- [ ] physics-agent: Prepare literature and supporting references
- [ ] graphic-agent: Stand by for figure requests

## Session 2 — Kickoff
**Focus:** Deriving the mathematics for the observable universe as a Bose-Einstein condensate expanding within a universal fluid.

**Draft paper:** `team_folder/doc-agent/draft_papers/universal_condensate_draft_v01.tex` (923 lines)
- Built from the architectural framework with full team collaboration markers
- Contains TODO placeholders for: math-agent (derivations), physics-agent (literature), graphic-agent (figures)
- Appendices A-D ready for math-agent to fill: Rankine-Hugoniot, impedance matching, sound horizon integrals, tensor-mode propagation
- 10 figure placeholders marked for graphic-agent
- All three prior Skavberg papers cited

### Session 2 Action Items
- [x] doc-agent: Build formal draft v01 from architectural framework
- [ ] math-agent: Begin filling derivations (Appendices A-D, inline equations)
- [ ] physics-agent: Expand literature review, add observational constraints
- [ ] graphic-agent: Await figure requests from doc-agent
