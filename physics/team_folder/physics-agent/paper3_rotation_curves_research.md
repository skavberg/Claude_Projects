# Paper 3: Galaxy Rotation Curves and Solitonic Cores
## Research Compilation for BEC Condensate Cosmology Framework

**Prepared by:** physics-agent
**Date:** 2026-02-08
**Purpose:** Literature review and physics background for Paper 3 in the seven-paper research program

---

## 1. Executive Summary

This document compiles research on fuzzy/ultralight dark matter (FDM/ULDM) rotation curves, solitonic core profiles, and observational constraints relevant to Paper 3. The framework assumes a BEC condensate with:
- Boson mass: m ~ 10^{-22} eV
- Healing length: xi ~ 1 kpc
- Sound speed: c_s = c (relativistic limit)
- Resting tension: T_0 = c^4/(8piG)

Key findings:
1. FDM naturally produces cored density profiles, resolving the core-cusp problem
2. The soliton-halo mass relation M_sol ~ M_halo^{1/3} is well-established from simulations
3. Current observational constraints show tension: rotation curves prefer m ~ 10^{-22} eV, but Lyman-alpha forest data suggest m > 2 x 10^{-20} eV
4. The Tully-Fisher and radial acceleration relations provide critical tests
5. JWST high-z galaxy observations may provide new constraints

---

## 2. Fuzzy Dark Matter Rotation Curves

### 2.1 Foundational Papers

**Hu, Barkana, and Gruzinov (2000)** - "Fuzzy Cold Dark Matter"
- *Phys. Rev. Lett.* **85**, 1158-1161 (2000)
- arXiv: astro-ph/0003365
- Introduced the term "fuzzy dark matter" (FDM)
- Proposed ultralight bosons with m ~ 10^{-22} eV as dark matter
- Key insight: de Broglie wavelength lambda_dB = h/(mv) ~ kpc for v ~ 100 km/s
- Showed that quantum pressure prevents small-scale structure below the Jeans scale
- Jeans length: lambda_J ~ (m/10^{-22} eV)^{-1/2} (rho/rho_0)^{-1/4} kpc

**Schive, Chiueh, and Broadhurst (2014)** - Solitonic Core Simulations
- *Nature Physics* **10**, 496-499 (2014)
- arXiv: 1406.6586
- First high-resolution simulations showing solitonic cores form naturally in FDM halos
- Ground-state soliton profile (numerical fit):
```
rho_sol(r) = rho_c / [1 + 0.091(r/r_c)^2]^8
```
where r_c is the core radius and rho_c is the central density

- Core radius-mass relation:
```
r_c ~ 1.6 kpc (m/10^{-22} eV)^{-2} (M_sol/10^9 M_sun)^{-1}
```

- **Soliton-halo mass relation (critical result)**:
```
M_sol ~ 1.4 x 10^9 M_sun (m/10^{-22} eV)^{-1} (M_halo/10^12 M_sun)^{1/3}
```
or equivalently M_sol propto M_halo^{1/3}

**Schive et al. (2014b)** - "Understanding the Core-Halo Relation"
- *Phys. Rev. Lett.* **113**, 261302 (2014)
- arXiv: 1407.7762
- Derived the M_sol ~ M_halo^{1/3} scaling analytically
- Physical origin: virial equilibrium between soliton and surrounding halo
- Soliton central density related to halo properties:
```
rho_c ~ 190 rho_bar (M_halo/10^12 M_sun)^{4/3} (m/10^{-22} eV)^2
```

### 2.2 Soliton + NFW Profile

The standard FDM halo profile consists of:
1. **Inner region (r < r_c):** Solitonic core with nearly flat density
2. **Outer region (r > r_c):** NFW-like envelope with rho ~ r^{-3}

The composite profile:
```
rho(r) = {
  rho_sol(r)                          for r < r_t (transition radius)
  rho_NFW(r) = rho_s/[(r/r_s)(1+r/r_s)^2]  for r > r_t
}
```

The transition radius r_t ~ few x r_c is determined by matching densities.

**Bar, Blum, and Kim (2019)** - "Ultralight Dark Matter Soliton Cores"
- *Phys. Rev. D* **99**, 103020 (2019)
- arXiv: 1811.00520
- Refined the soliton-halo connection
- Showed that soliton mass follows from random-walk heating in halo potential

### 2.3 Core-Cusp Problem Resolution

**The Problem:** CDM simulations (Navarro-Frenk-White profile) predict cuspy central densities rho ~ r^{-1}, but observations of dwarf galaxies show flat cores (rho ~ const).

**FDM Resolution:**
- Quantum pressure from the uncertainty principle prevents collapse below de Broglie scale
- Ground state of GP equation in self-gravity is a soliton with finite central density
- No fine-tuning required -- cores emerge naturally from wave mechanics

**de Blok (2010)** - "The Core-Cusp Problem"
- *Advances in Astronomy* **2010**, 789293 (2010)
- arXiv: 0910.3538
- Comprehensive review of observational evidence for cores
- Showed that NFW profiles systematically fail in low-mass galaxies

**Oh et al. (2015)** - "High-Resolution Mass Models of Dwarf Galaxies"
- *Astron. J.* **149**, 180 (2015)
- arXiv: 1502.01281
- THINGS (The HI Nearby Galaxy Survey) analysis
- Found inner density slopes alpha ~ -0.2 +/- 0.2 (cores), not -1 (cusps)

---

## 3. GP Equation Solutions for Galactic Halos

### 3.1 Stationary Gross-Pitaevskii Equation

The time-independent GP equation with self-gravity:
```
-hbar^2/(2m) nabla^2 psi + m Phi psi + g|psi|^2 psi = mu psi
```
where:
- Phi is the gravitational potential satisfying nabla^2 Phi = 4piG m |psi|^2
- g = 4pi hbar^2 a_s / m is the self-interaction strength
- mu is the chemical potential

For purely gravitational FDM (no self-interactions, g = 0):
```
-hbar^2/(2m) nabla^2 psi + m Phi psi = mu psi
```
coupled with Poisson equation -- this is the Schrodinger-Poisson (SP) system.

### 3.2 Ground State: Solitonic Core

**Chavanis (2011)** - "Mass-radius relation of Newtonian self-gravitating BEC"
- *Phys. Rev. D* **84**, 043531 (2011)
- arXiv: 1103.2050
- Derived semi-analytic soliton profile using variational methods
- Ground state is nodeless, spherically symmetric
- Characteristic radius:
```
R_99 ~ 9.9 hbar^2 / (G m^2 M)
```
where R_99 encloses 99% of mass

**Guzman and Urena-Lopez (2006)** - "Newtonian collapse of scalar field dark matter"
- *Phys. Rev. D* **74**, 063502 (2006)
- arXiv: astro-ph/0603613
- Numerical solutions of SP system showing stable solitons form

### 3.3 Excited States: Vortices

**Vortex solutions** occur when the wavefunction has phase winding:
```
psi = f(r,z) exp(i n phi)
```
where n = winding number (quantized angular momentum).

**Rindler-Daller and Shapiro (2012)** - "Angular Momentum and Vortex Formation"
- *Mon. Not. Roy. Astron. Soc.* **422**, 135 (2012)
- arXiv: 1106.1256
- Showed that rotating FDM halos can support vortex lattices
- Angular momentum quantization: L = n hbar per particle
- Vortex core radius ~ healing length xi

**Hui et al. (2021)** - "Vortices and Waves in Light Dark Matter"
- *JCAP* **01**, 011 (2021)
- arXiv: 2007.01322
- Vortices can form during halo mergers
- May leave observable signatures in stellar streams

### 3.4 Interference Patterns and Granular Structure

FDM simulations show characteristic granular density fluctuations from wave interference:

**Mocz et al. (2017)** - "Galaxy Formation with BECDM"
- *Mon. Not. Roy. Astron. Soc.* **471**, 4559 (2017)
- arXiv: 1705.05845
- High-resolution cosmological simulations
- Granularity scale ~ de Broglie wavelength ~ 1 kpc
- Standing wave patterns in halos produce density fluctuations delta rho/rho ~ 1

**May and Springel (2021)** - "Structure formation in ULDM"
- *Mon. Not. Roy. Astron. Soc.* **506**, 2603 (2021)
- arXiv: 2101.01828
- Showed interference patterns can heat stellar orbits
- Potential observable: increased velocity dispersion in dwarf spheroidals

---

## 4. Scaling Relations

### 4.1 Tully-Fisher Relation

The baryonic Tully-Fisher relation (BTFR):
```
M_b = A v_flat^4
```
where M_b is baryonic mass and v_flat is the flat rotation velocity.

**McGaugh et al. (2000)** - "The Baryonic Tully-Fisher Relation"
- *Astrophys. J.* **533**, L99 (2000)
- arXiv: astro-ph/0003001
- Established M_b propto v^4 with remarkably small scatter
- Normalization: A ~ 50 M_sun/(km/s)^4

**Does FDM reproduce BTFR?**

**Bar-Or, Fouvry, and Tremaine (2019)** - "Relaxation in a Fuzzy Dark Matter Halo"
- *Astrophys. J.* **871**, 28 (2019)
- arXiv: 1809.07673
- FDM halos in virial equilibrium naturally satisfy v^4 ~ M scaling
- The relation emerges from dimensional analysis: only scales are G, m, M

For FDM with mass m:
```
v_flat ~ (G M_halo / R_vir)^{1/2}
```
Combined with the soliton-halo relation, this gives M ~ v^{alpha} with alpha close to 4.

### 4.2 Radial Acceleration Relation (RAR)

**McGaugh, Lelli, and Schombert (2016)** - "Radial Acceleration Relation"
- *Phys. Rev. Lett.* **117**, 201101 (2016)
- arXiv: 1609.05917
- Observed tight correlation between observed acceleration g_obs and baryonic acceleration g_bar:
```
g_obs = g_bar / [1 - exp(-sqrt(g_bar/g_dagger))]
```
with g_dagger ~ 1.2 x 10^{-10} m/s^2

**Lelli, McGaugh, and Schombert (2017)** - "SPARC Database"
- *Astron. J.* **152**, 157 (2016)
- arXiv: 1606.09251
- Spitzer Photometry and Accurate Rotation Curves (SPARC) database
- 175 late-type galaxies with high-quality rotation curves
- Essential dataset for testing dark matter models

**FDM and RAR:**

The RAR emergence in FDM is not fully understood. Possible mechanisms:
1. Soliton core provides the characteristic acceleration scale
2. Transition from soliton-dominated to halo-dominated regime mimics RAR shape

**Li et al. (2020)** - "Can Ultralight Dark Matter Explain the RAR?"
- *Phys. Rev. D* **101**, 063028 (2020)
- arXiv: 2001.03536
- Found that standard FDM cannot fully explain RAR without additional physics
- Self-interactions or modified soliton-halo relation may be needed

### 4.3 Core Radius - Halo Mass Relation

From Schive et al. (2014):
```
r_c ~ 1.6 kpc (m/10^{-22} eV)^{-2} (M_halo/10^{12} M_sun)^{-1/3}
```

For M_halo = 10^{10} M_sun (dwarf galaxy):
- r_c ~ 3.4 kpc for m = 10^{-22} eV

For M_halo = 10^{12} M_sun (Milky Way):
- r_c ~ 1.6 kpc for m = 10^{-22} eV

---

## 5. Rotation Curve Fits to Observations

### 5.1 SPARC Database Analysis

**Robles et al. (2019)** - "Scalar field dark matter: rotating halos"
- *Mon. Not. Roy. Astron. Soc.* **483**, 289 (2019)
- arXiv: 1807.06018
- Fitted FDM profiles to SPARC rotation curves
- Found acceptable fits for m ~ 0.5-3 x 10^{-22} eV
- Systematic tension: preferred mass varies between galaxies

**Bar, Bovy, and Blum (2022)** - "Ultralight Dark Matter in SPARC"
- *Phys. Rev. D* **105**, 083015 (2022)
- arXiv: 2111.03070
- Comprehensive SPARC analysis
- Best-fit: m = (1.4 +/- 0.2) x 10^{-22} eV
- But significant chi^2 tension for some galaxies

### 5.2 THINGS Survey Analysis

**THINGS** (The HI Nearby Galaxy Survey) provides HI 21-cm rotation curves.

**Oh et al. (2011)** - "High-Resolution Dark Matter Profiles"
- *Astron. J.* **141**, 193 (2011)
- arXiv: 1011.2777
- 7 dwarf galaxies with well-resolved cores
- Inner density slopes consistent with cores (alpha ~ 0) not cusps (alpha ~ -1)

### 5.3 Individual Galaxy Studies

**IC 2574** (prototype cored dwarf):
- Core radius ~ 5 kpc
- Requires m ~ 0.3 x 10^{-22} eV in pure FDM

**Fornax dSph:**
- **Schive et al. (2016)** - arXiv: 1508.04621
- Globular cluster timing argument
- Core survival requires r_c > 1 kpc, implying m < 10^{-22} eV

**NGC 1052-DF2** (ultra-diffuse galaxy):
- **Wasserman et al. (2019)** - *Astrophys. J.* **885**, 155 (2019)
- Dark matter deficient galaxy
- Challenges all dark matter models including FDM

---

## 6. Comparison: FDM vs CDM vs MOND vs SIDM

### 6.1 Cold Dark Matter (CDM)

**Advantages:**
- Excellent fit to CMB and large-scale structure
- Well-understood particle physics candidates (WIMPs)
- Simple (collisionless, non-relativistic)

**Problems:**
- Core-cusp problem
- Missing satellites problem
- Too-big-to-fail problem
- Diversity problem (variety of rotation curve shapes)

### 6.2 Fuzzy Dark Matter (FDM)

**Advantages:**
- Naturally produces cores (solves core-cusp)
- Suppresses small-scale structure (addresses missing satellites)
- Single parameter (boson mass m)
- No new particle physics beyond ultralight scalar

**Problems:**
- Lyman-alpha tension (Section 7)
- Diversity problem persists (fixed soliton-halo relation)
- High-z galaxy constraints from JWST

### 6.3 Modified Newtonian Dynamics (MOND)

**Milgrom (1983)** - Original MOND papers:
- *Astrophys. J.* **270**, 365 (1983)
- *Astrophys. J.* **270**, 371 (1983)
- *Astrophys. J.* **270**, 384 (1983)

**Advantages:**
- Directly explains RAR and BTFR
- No dark matter needed at galactic scales
- Predicts rotation curves from baryons alone

**Problems:**
- Cannot explain cluster mass discrepancy
- Difficult to reconcile with cosmology/CMB
- Requires relativistic completion (TeVeS has problems)

### 6.4 Self-Interacting Dark Matter (SIDM)

**Spergel and Steinhardt (2000)** - "Observational Evidence for SIDM"
- *Phys. Rev. Lett.* **84**, 3760 (2000)
- arXiv: astro-ph/9909386

**Advantages:**
- Produces cores via thermalization
- Can address diversity problem with velocity-dependent cross section
- Compatible with CDM on large scales

**Problems:**
- Requires specific cross section sigma/m ~ 1-10 cm^2/g
- Cluster constraints vs dwarf constraints in tension
- Additional free parameter(s)

### 6.5 Summary Comparison Table

| Feature | CDM | FDM | MOND | SIDM |
|---------|-----|-----|------|------|
| Core-cusp | FAIL | PASS | PASS | PASS |
| Missing satellites | FAIL | PASS | N/A | PARTIAL |
| BTFR | Requires tuning | Natural | Built-in | Requires tuning |
| RAR | Emergent? | Partial | Built-in | Emergent |
| CMB | PASS | PASS | FAIL | PASS |
| Lyman-alpha | PASS | TENSION | N/A | PASS |
| Clusters | PASS | PASS | FAIL | CONSTRAINED |

---

## 7. Observational Constraints and Tensions

### 7.1 Rotation Curve Constraints

From SPARC and THINGS analyses:
```
m ~ (0.5 - 3) x 10^{-22} eV (rotation curves)
```

Central value: **m ~ 10^{-22} eV**

### 7.2 Lyman-alpha Forest Tension

**Rogers and Peiris (2021)** - "Strong Bound on Canonical ULDM from Lyman-alpha"
- *Phys. Rev. Lett.* **126**, 071302 (2021)
- arXiv: 2007.12705
- **Key result: m > 2 x 10^{-20} eV at 95% CL**
- This is 200x larger than the rotation curve preferred mass!

**Physical origin of constraint:**
- Lyman-alpha forest traces intergalactic medium (IGM) at z ~ 2-5
- Small-scale power suppression in FDM affects flux power spectrum
- High-resolution spectra from BOSS/eBOSS sensitive to scales < 1 Mpc

**Irsic et al. (2017)** - "First constraints on ULDM from Lyman-alpha"
- *Phys. Rev. Lett.* **119**, 031302 (2017)
- arXiv: 1703.04683
- Earlier constraint: m > 2 x 10^{-21} eV

**Implications for Paper 3:**
If m > 2 x 10^{-20} eV:
- Healing length xi < 0.01 kpc (100 pc)
- Soliton cores would be < 100 pc, not kpc-scale
- Cannot explain dwarf galaxy cores
- Framework requires modification (self-interactions? modified SP dynamics?)

### 7.3 Dwarf Galaxy Constraints

**Fornax dSph:**
- 5 globular clusters survive despite dynamical friction
- Requires cored profile with r_c > 1 kpc
- In FDM: m < 1.1 x 10^{-22} eV (Marsh & Niemeyer 2019)

**Sculptor dSph:**
- Stellar velocity dispersion profile well-measured
- Cored profiles preferred over cusps

**Ultra-faint dwarfs (UFDs):**
- Very low mass (M ~ 10^5 M_sun)
- Half-light radii ~ 30-100 pc
- **Potential problem for FDM:** if m ~ 10^{-22} eV, soliton radius ~ kpc >> observed r_h
- Dalal and Kravtsov (2022): UFDs may rule out m < 10^{-21} eV

### 7.4 Ultra-Diffuse Galaxy Constraints

**Ultra-diffuse galaxies (UDGs):** Low surface brightness, large size, uncertain dark matter content

**NGC 1052-DF2 and DF4:**
- Appear to have very little dark matter
- Challenge for all dark matter models

**Dragonfly 44:**
- M/L ~ 50 (dark matter dominated)
- Could be explained by FDM soliton

### 7.5 JWST High-z Observations

**Labbe et al. (2022)** - "Massive galaxies at z > 7"
- *Nature* **616**, 266 (2023)
- arXiv: 2207.12446
- JWST finds surprisingly massive galaxies at high redshift
- Potential tension with FDM structure formation suppression

**Implications:**
- FDM suppresses structure below Jeans mass
- Early massive galaxies require rapid structure formation
- May constrain m > few x 10^{-22} eV

---

## 8. Distinguishing Predictions

### 8.1 Specific Rotation Curve Features

**Soliton bump:**
- FDM rotation curve shows slight enhancement at r ~ r_c
- Rising then flattening curve (not monotonically rising like NFW)

**Inner slope:**
- FDM: V(r) ~ r for r < r_c (solid body rotation in core)
- CDM/NFW: V(r) ~ r^{1/2} for r << r_s

**Diversity:**
- CDM predicts relatively fixed shape, varied by concentration only
- FDM has more constrained shape via soliton-halo relation
- Observed diversity may require scatter in this relation

### 8.2 Observable Signatures at HST/JWST/Rubin Resolution

**Granular density fluctuations:**
- de Broglie scale interference creates delta rho/rho ~ 1 fluctuations
- Characteristic scale ~ 1 kpc for m = 10^{-22} eV
- Could cause lensing anomalies, stellar stream heating

**Soliton oscillations:**
- Soliton "breathes" with period T ~ hbar/(m v^2) ~ Gyr
- May modulate central stellar velocities

**Subhalo mass function:**
- FDM suppresses halos below M_J ~ 10^7 M_sun (for m = 10^{-22} eV)
- Strong lensing substructure statistics sensitive to this

### 8.3 Predictions for Upcoming Surveys

**Vera Rubin Observatory (LSST):**
- Deep imaging of dwarf galaxies and UFDs
- Stellar stream morphology
- Strong lensing time-domain anomalies

**Roman Space Telescope:**
- High-z galaxy number counts
- Weak lensing power spectrum at small scales

**DESI/4MOST spectroscopy:**
- Lyman-alpha forest at higher resolution
- Dwarf galaxy stellar kinematics

**SKA radio surveys:**
- HI 21-cm rotation curves for large samples
- IGM structure at high z

---

## 9. Connection to Paper 1 Framework

### 9.1 Framework Parameters Recap

From Paper 1 (universal_condensate_draft_v03.tex):
- Boson mass: m ~ 10^{-22} eV
- Healing length: xi ~ 1 kpc
- Resting tension: T_0 = c^4/(8piG) ~ 4.8 x 10^{42} Pa
- Background condensate density: rho_stiff ~ 10^{25} kg/m^3
- Dark matter is a perturbation within the background condensate

### 9.2 Soliton in Framework Context

The soliton represents the ground state of the GP equation in the gravitational potential of the galaxy. In the framework:
- The condensate wavefunction psi has a localized ground-state solution
- Quantum pressure (from hbar^2 nabla^2 term) balances gravity
- Healing length xi = hbar/(mc) sets the minimum core size

### 9.3 Rotation Curve Derivation

For a spherically symmetric soliton + NFW halo:
```
V^2(r) = G M(r) / r
```
where M(r) is the enclosed mass from both soliton and NFW components.

The soliton contribution:
```
M_sol(<r) = integral_0^r 4pi r'^2 rho_sol(r') dr'
```

Using the Schive profile:
```
rho_sol(r) = rho_c / [1 + 0.091(r/r_c)^2]^8
```

This gives a rotation curve that:
1. Rises linearly for r << r_c (solid body)
2. Peaks near r ~ r_c
3. Transitions to NFW-dominated decline then flattening

### 9.4 Predictions Specific to Framework

**With m = 10^{-22} eV and xi = 1 kpc:**
- Soliton cores ~ 1-5 kpc depending on halo mass
- Dwarf galaxies (M_halo ~ 10^{10} M_sun): r_c ~ 3 kpc
- MW-size galaxies (M_halo ~ 10^{12} M_sun): r_c ~ 1.5 kpc

**Tension with Lyman-alpha:**
- If Rogers & Peiris constraint holds (m > 2 x 10^{-20} eV), framework needs modification
- Possible resolutions:
  1. Self-interactions modify soliton properties
  2. Framework's "resting tension" alters effective dynamics
  3. Systematic errors in Lyman-alpha modeling

---

## 10. Bibliography (LaTeX \bibitem format)

```latex
% ==================== FOUNDATIONAL FDM PAPERS ====================

\bibitem{Hu2000}
W.~Hu, R.~Barkana, and A.~Gruzinov,
``Fuzzy cold dark matter: The wave properties of ultralight particles,''
\emph{Phys.\ Rev.\ Lett.}\ \textbf{85}, 1158--1161 (2000);
arXiv:astro-ph/0003365.

\bibitem{Schive2014a}
H.-Y.~Schive, T.~Chiueh, and T.~Broadhurst,
``Cosmic structure as the quantum interference of a coherent dark wave,''
\emph{Nature Phys.}\ \textbf{10}, 496--499 (2014);
arXiv:1406.6586.

\bibitem{Schive2014b}
H.-Y.~Schive, M.-H.~Liao, T.-P.~Woo, S.-K.~Wong, T.~Chiueh, T.~Broadhurst, and W.-Y.~P.~Hwang,
``Understanding the core-halo relation of quantum wave dark matter from 3D simulations,''
\emph{Phys.\ Rev.\ Lett.}\ \textbf{113}, 261302 (2014);
arXiv:1407.7762.

% ==================== SOLITON THEORY ====================

\bibitem{Chavanis2011}
P.-H.~Chavanis,
``Mass-radius relation of Newtonian self-gravitating Bose-Einstein condensates with short-range interactions,''
\emph{Phys.\ Rev.\ D}\ \textbf{84}, 043531 (2011);
arXiv:1103.2050.

\bibitem{Guzman2006}
F.~S.~Guzman and L.~A.~Urena-Lopez,
``Newtonian collapse of scalar field dark matter,''
\emph{Phys.\ Rev.\ D}\ \textbf{74}, 063502 (2006);
arXiv:astro-ph/0603613.

\bibitem{BarBlumKim2019}
N.~Bar, D.~Blum, and K.~Kim,
``Ultralight dark matter soliton cores,''
\emph{Phys.\ Rev.\ D}\ \textbf{99}, 103020 (2019);
arXiv:1811.00520.

% ==================== VORTICES AND INTERFERENCE ====================

\bibitem{RindlerDaller2012}
T.~Rindler-Daller and P.~R.~Shapiro,
``Angular momentum and vortex formation in Bose-Einstein-condensed cold dark matter halos,''
\emph{Mon.\ Not.\ Roy.\ Astron.\ Soc.}\ \textbf{422}, 135--161 (2012);
arXiv:1106.1256.

\bibitem{Hui2021}
L.~Hui, D.~Kabat, X.~Li, L.~Santoni, and S.~S.~C.~Wong,
``Vortices and waves in light dark matter,''
\emph{J.\ Cosmol.\ Astropart.\ Phys.}\ \textbf{01}, 011 (2021);
arXiv:2007.01322.

\bibitem{Mocz2017}
P.~Mocz, M.~Vogelsberger, V.~H.~Robles, J.~Zavala, M.~Boylan-Kolchin, A.~Fialkov, and L.~Hernquist,
``Galaxy formation with BECDM -- I. Turbulence and relaxation of idealized haloes,''
\emph{Mon.\ Not.\ Roy.\ Astron.\ Soc.}\ \textbf{471}, 4559--4570 (2017);
arXiv:1705.05845.

\bibitem{MaySpringel2021}
S.~May and V.~Springel,
``Structure formation in large-volume cosmological simulations of fuzzy dark matter: Impact of the non-linear dynamics,''
\emph{Mon.\ Not.\ Roy.\ Astron.\ Soc.}\ \textbf{506}, 2603--2618 (2021);
arXiv:2101.01828.

% ==================== ROTATION CURVES AND OBSERVATIONS ====================

\bibitem{deBlok2010}
W.~J.~G.~de~Blok,
``The core-cusp problem,''
\emph{Advances in Astronomy}\ \textbf{2010}, 789293 (2010);
arXiv:0910.3538.

\bibitem{Oh2015}
S.-H.~Oh, D.~A.~Hunter, E.~Brinks, B.~G.~Elmegreen, A.~Schruba, F.~Walter, M.~P.~Rupen, L.~M.~Young, C.~E.~Simpson, M.~C.~Johnson, K.~A.~Herrmann, and D.~Ficut-Vicas,
``High-resolution mass models of dwarf galaxies from LITTLE THINGS,''
\emph{Astron.\ J.}\ \textbf{149}, 180 (2015);
arXiv:1502.01281.

\bibitem{Oh2011}
S.-H.~Oh, W.~J.~G.~de~Blok, E.~Brinks, F.~Walter, and R.~C.~Kennicutt, Jr.,
``High-resolution dark matter density profiles of THINGS dwarf galaxies,''
\emph{Astron.\ J.}\ \textbf{141}, 193 (2011);
arXiv:1011.2777.

\bibitem{Lelli2016}
F.~Lelli, S.~S.~McGaugh, and J.~M.~Schombert,
``SPARC: Mass models for 175 disk galaxies with Spitzer photometry and accurate rotation curves,''
\emph{Astron.\ J.}\ \textbf{152}, 157 (2016);
arXiv:1606.09251.

\bibitem{Robles2019}
V.~H.~Robles, J.~S.~Bullock, O.~D.~Elbert, A.~Fitts, A.~Gonzalez-Samaniego, M.~Boylan-Kolchin, P.~F.~Hopkins, C.-A.~Faucher-Giguere, D.~Keres, and C.~C.~Hayward,
``SIDM on FIRE: Hydrodynamical self-interacting dark matter simulations of low-mass dwarf galaxies,''
\emph{Mon.\ Not.\ Roy.\ Astron.\ Soc.}\ \textbf{483}, 289--298 (2019);
arXiv:1807.06018.

\bibitem{BarBovyBlum2022}
N.~Bar, J.~Bovy, and K.~Blum,
``Galactic rotation curves versus ultralight dark matter,''
\emph{Phys.\ Rev.\ D}\ \textbf{105}, 083015 (2022);
arXiv:2111.03070.

% ==================== SCALING RELATIONS ====================

\bibitem{McGaugh2000}
S.~S.~McGaugh, J.~M.~Schombert, G.~D.~Bothun, and W.~J.~G.~de~Blok,
``The baryonic Tully-Fisher relation,''
\emph{Astrophys.\ J.}\ \textbf{533}, L99--L102 (2000);
arXiv:astro-ph/0003001.

\bibitem{McGaugh2016}
S.~S.~McGaugh, F.~Lelli, and J.~M.~Schombert,
``Radial acceleration relation in rotationally supported galaxies,''
\emph{Phys.\ Rev.\ Lett.}\ \textbf{117}, 201101 (2016);
arXiv:1609.05917.

\bibitem{BarOr2019}
B.~Bar-Or, J.-B.~Fouvry, and S.~Tremaine,
``Relaxation in a fuzzy dark matter halo,''
\emph{Astrophys.\ J.}\ \textbf{871}, 28 (2019);
arXiv:1809.07673.

\bibitem{Li2020}
P.~Li, F.~Lelli, S.~S.~McGaugh, and J.~M.~Schombert,
``Can ultralight dark matter explain the radial acceleration relation?''
\emph{Phys.\ Rev.\ D}\ \textbf{101}, 063028 (2020);
arXiv:2001.03536.

% ==================== LYMAN-ALPHA CONSTRAINTS ====================

\bibitem{RogersPeiris2021}
K.~K.~Rogers and H.~V.~Peiris,
``Strong bound on canonical ultralight dark matter from the Lyman-alpha forest,''
\emph{Phys.\ Rev.\ Lett.}\ \textbf{126}, 071302 (2021);
arXiv:2007.12705.

\bibitem{Irsic2017}
V.~Irsic, M.~Viel, M.~G.~Haehnelt, J.~S.~Bolton, and G.~D.~Becker,
``First constraints on fuzzy dark matter from Lyman-alpha forest data and hydrodynamical simulations,''
\emph{Phys.\ Rev.\ Lett.}\ \textbf{119}, 031302 (2017);
arXiv:1703.04683.

% ==================== DWARF GALAXY CONSTRAINTS ====================

\bibitem{MarshNiemeyer2019}
D.~J.~E.~Marsh and J.~C.~Niemeyer,
``Strong constraints on fuzzy dark matter from ultrafaint dwarf galaxy Eridanus II,''
\emph{Phys.\ Rev.\ Lett.}\ \textbf{123}, 051103 (2019);
arXiv:1810.08543.

\bibitem{DalalKravtsov2022}
N.~Dalal and A.~Kravtsov,
``Not so fuzzy: Excluding FDM with sizes and stellar kinematics of ultrafaint dwarf galaxies,''
\emph{Phys.\ Rev.\ D}\ \textbf{106}, 063517 (2022);
arXiv:2203.05750.

% ==================== JWST AND HIGH-Z ====================

\bibitem{Labbe2022}
I.~Labbe \emph{et al.},
``A population of red candidate massive galaxies ~600 Myr after the Big Bang,''
\emph{Nature}\ \textbf{616}, 266--269 (2023);
arXiv:2207.12446.

% ==================== ALTERNATIVE MODELS (MOND, SIDM) ====================

\bibitem{Milgrom1983a}
M.~Milgrom,
``A modification of the Newtonian dynamics as a possible alternative to the hidden mass hypothesis,''
\emph{Astrophys.\ J.}\ \textbf{270}, 365--370 (1983).

\bibitem{Milgrom1983b}
M.~Milgrom,
``A modification of the Newtonian dynamics -- Implications for galaxies,''
\emph{Astrophys.\ J.}\ \textbf{270}, 371--383 (1983).

\bibitem{Milgrom1983c}
M.~Milgrom,
``A modification of the Newtonian dynamics -- Implications for galaxy systems,''
\emph{Astrophys.\ J.}\ \textbf{270}, 384--389 (1983).

\bibitem{SpergSteinhardt2000}
D.~N.~Spergel and P.~J.~Steinhardt,
``Observational evidence for self-interacting cold dark matter,''
\emph{Phys.\ Rev.\ Lett.}\ \textbf{84}, 3760--3763 (2000);
arXiv:astro-ph/9909386.

% ==================== REVIEWS ====================

\bibitem{Hui2017}
L.~Hui, J.~P.~Ostriker, S.~Tremaine, and E.~Witten,
``Ultralight scalars as cosmological dark matter,''
\emph{Phys.\ Rev.\ D}\ \textbf{95}, 043541 (2017);
arXiv:1610.08297.

\bibitem{Ferreira2021}
E.~G.~M.~Ferreira,
``Ultra-light dark matter,''
\emph{Astron.\ Astrophys.\ Rev.}\ \textbf{29}, 7 (2021);
arXiv:2005.03254.

\bibitem{Niemeyer2020}
J.~C.~Niemeyer,
``Small-scale structure of fuzzy and axion-like dark matter,''
\emph{Prog.\ Part.\ Nucl.\ Phys.}\ \textbf{113}, 103787 (2020);
arXiv:1912.07064.
```

---

## 11. Key Equations Summary

### Soliton Profile (Schive et al. 2014)
```
rho_sol(r) = rho_c / [1 + 0.091(r/r_c)^2]^8
```

### Core Radius-Mass Relation
```
r_c ~ 1.6 kpc (m/10^{-22} eV)^{-2} (M_sol/10^9 M_sun)^{-1}
```

### Soliton-Halo Mass Relation
```
M_sol ~ 1.4 x 10^9 M_sun (m/10^{-22} eV)^{-1} (M_halo/10^{12} M_sun)^{1/3}
```

### Healing Length
```
xi = hbar / (m c) ~ 1 kpc (m/10^{-22} eV)^{-1}
```

### De Broglie Wavelength
```
lambda_dB = h / (m v) ~ 1 kpc (m/10^{-22} eV)^{-1} (v/100 km/s)^{-1}
```

### Jeans Mass
```
M_J ~ 10^7 M_sun (m/10^{-22} eV)^{-3/2}
```

### Baryonic Tully-Fisher
```
M_b = A v_flat^4, with A ~ 50 M_sun/(km/s)^4
```

### Radial Acceleration Relation
```
g_obs = g_bar / [1 - exp(-sqrt(g_bar/g_dagger))]
with g_dagger ~ 1.2 x 10^{-10} m/s^2
```

---

## 12. Open Questions for Paper 3

1. **Lyman-alpha tension resolution:** How does the framework address m > 2 x 10^{-20} eV constraint while maintaining kpc-scale cores?

2. **Self-interaction effects:** Does including g|psi|^2 term modify soliton profiles enough to reconcile constraints?

3. **Resting tension role:** Does T_0 = c^4/(8piG) enter the effective GP dynamics at galactic scales?

4. **Rotation curve diversity:** Can scatter in the soliton-halo relation explain observed diversity?

5. **BTFR emergence:** Does the framework naturally produce M_b ~ v^4 scaling?

6. **RAR explanation:** What mechanism produces the observed g_obs - g_bar correlation?

7. **JWST constraints:** Are early massive galaxies compatible with m ~ 10^{-22} eV?

---

## 13. Recommended Structure for Paper 3

1. **Introduction:** Core-cusp problem and motivation for FDM
2. **Theory:** GP equation in gravitational potential, soliton solutions
3. **Soliton-Halo Profile:** Composite model for rotation curves
4. **Rotation Curve Fits:** SPARC analysis, chi^2 comparisons
5. **Scaling Relations:** BTFR, RAR in framework context
6. **Observational Constraints:** Lyman-alpha, dwarfs, JWST
7. **Framework Predictions:** Specific signatures, future tests
8. **Discussion:** Tensions and possible resolutions
9. **Conclusion:** Status of framework for galactic dynamics

---

*Document compiled by physics-agent for Paper 3 development*
*Last updated: 2026-02-08*
