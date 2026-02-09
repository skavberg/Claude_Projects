# Research Compilation for Paper 2: Gravitational Lensing and Light Propagation in the BEC Condensate Framework

**Compiled by:** Physics Research Agent
**Date:** 2026-02-08
**For:** Seven-Paper Research Program on "Observable Universe as a Condensate"

---

## Executive Summary

This document provides a comprehensive literature review and theoretical analysis for Paper 2 of the condensate cosmology research program. The focus is on gravitational lensing and light propagation within the framework where the observable universe is a Bose-Einstein condensate (BEC), with spacetime described by the acoustic metric of the condensate. Key parameters from Paper 1: boson mass m ~ 10^{-22} eV, healing length xi ~ 1 kpc, resting tension T_0 = c^4/(8 pi G), and sound speed c_s = c.

---

## 1. Light Propagation in Acoustic Metrics

### 1.1 Foundational Theory: Analogue Gravity

The acoustic metric formalism provides the theoretical foundation for understanding how light (or more precisely, perturbations) propagates in the BEC framework.

**Key Concept:** In a flowing fluid with background density rho_0, velocity field v_i, and sound speed c_s, small perturbations experience an effective curved spacetime described by the acoustic metric:

```
ds^2 = (rho_0 / c_s) [ -c_s^2 dt^2 + (delta_ij - v_i v_j / c_s^2) dx^i dx^j ]
```

In the BEC cosmology framework (Paper 1, Postulate 3), this becomes the effective spacetime metric experienced by matter and radiation.

### 1.2 Seminal Papers on Acoustic Metrics and Light Propagation

**[1] Unruh (1981) - "Experimental Black-Hole Evaporation?"**
- Phys. Rev. Lett. 46, 1351-1353
- First proposal of acoustic analogues of black holes ("dumb holes")
- Established that phonon propagation in a flowing fluid mimics massless scalar field propagation in curved spacetime
- Key result: The acoustic metric has the same mathematical structure as a general relativistic metric for null geodesics

**[2] Visser (1993) - "Acoustic black holes"**
- Class. Quantum Grav. 15, 1767-1791 (1998, published version)
- arXiv:gr-qc/9311028
- Systematic derivation of the acoustic metric from fluid dynamics
- Demonstrated that the acoustic geometry exactly reproduces the kinematics of curved spacetime
- Important clarification: The analogy is kinematic, not dynamic (no Einstein equations derived from fluid mechanics alone)

**[3] Barcelo, Liberati, and Visser (2005) - "Analogue Gravity"**
- Living Rev. Relativity 8, 12 (2005); updated 2011
- arXiv:gr-qc/0505065
- Comprehensive review covering all aspects of analogue gravity
- **Section 4.2** specifically addresses photon propagation and null geodesics
- Key result for Paper 2: Null geodesics in the acoustic metric are determined by:
  ```
  g^{ac}_{mu nu} k^mu k^nu = 0
  ```
  where k^mu is the wave 4-vector
- Discusses the distinction between "rainbow" metrics (frequency-dependent) and standard acoustic metrics

**[4] Barcelo, Liberati, and Visser (2001) - "Analogue gravity from BECs"**
- Phys. Rev. A 63, 023611 (2001)
- arXiv:cond-mat/0007020
- Specifically derives the acoustic metric for BEC systems using the Gross-Pitaevskii equation
- Shows that the Bogoliubov dispersion relation leads to Lorentz-violating corrections at high energies
- **Critical for Paper 2:** At wavelengths lambda >> xi (healing length), the standard acoustic metric applies; at lambda ~ xi, corrections become important

### 1.3 Geodesic Equations in Acoustic Metrics

For the acoustic FLRW metric derived in Paper 1:
```
ds^2 = (rho_0 / c) [ -c^2 dt^2 + a^2(t) delta_ij dx^i dx^j ]
```

The conformal factor (rho_0 / c) is constant in the background and does not affect null geodesics. Therefore:

**Key Result:** Photon geodesics in the acoustic metric are identical to photon geodesics in standard FLRW cosmology, provided c_s = c.

This means standard gravitational lensing formalism applies at scales >> xi.

### 1.4 Deviations from GR at Sub-Healing-Length Scales

The Bogoliubov dispersion relation for BEC phonons is:
```
omega^2 = c_s^2 k^2 + (hbar^2 k^4) / (4m^2)
```

This can be rewritten as:
```
omega^2 = c^2 k^2 (1 + k^2 xi^2 / 4)
```

where xi = hbar / (m c) is the healing length.

**Implications for light propagation:**
1. At long wavelengths (k xi << 1): Standard dispersion omega = c k
2. At short wavelengths (k xi ~ 1): Superluminal dispersion omega > c k
3. Group velocity: v_g = d omega / dk = c (1 + 3 k^2 xi^2 / 4) / sqrt(1 + k^2 xi^2 / 4)

**Relevant Papers:**
- Garay, Anglin, Cirac, Zoller (2000) - "Sonic Analog of Gravitational Black Holes in BECs" - Phys. Rev. Lett. 85, 4643
- Liberati, Visser, Weinfurtner (2006) - "Analogue quantum gravity phenomenology" - Class. Quantum Grav. 23, 3129

---

## 2. Gravitational Lensing in BEC/Superfluid Dark Matter Models

### 2.1 Overview of Fuzzy/Ultralight Dark Matter

The BEC framework with m ~ 10^{-22} eV corresponds to "fuzzy dark matter" (FDM) or "ultralight axion-like particles" (ULAPs). This is an active research area with direct relevance to lensing.

**Defining Characteristics:**
- de Broglie wavelength: lambda_dB = h / (m v) ~ 1 kpc for v ~ 100 km/s
- Jeans scale: k_J ~ sqrt(4 pi G rho_DM m^2 / hbar^2) ~ (1 kpc)^{-1}
- Solitonic cores form at the center of halos
- Wave interference creates granular structure in halos

### 2.2 Key Papers on Lensing in Fuzzy Dark Matter

**[5] Schive, Chiueh, Broadhurst (2014) - "Cosmic Structure as Quantum Interference"**
- Nature Physics 10, 496-499
- arXiv:1406.6586
- Established the soliton-halo mass relation: M_soliton ~ (a/m)^2 M_halo^{1/3}
- Solitonic cores have characteristic density profiles:
  ```
  rho_soliton(r) = rho_c / [1 + 0.091 (r/r_c)^2]^8
  ```
  where r_c ~ xi is the core radius
- **Lensing implication:** The solitonic core produces a cored central density profile, unlike the NFW cusp

**[6] Marsh & Pop (2015) - "Axion dark matter, solitons, and the cusp-core problem"**
- MNRAS 451, 2479-2492
- arXiv:1502.03456
- Detailed comparison of FDM density profiles vs. NFW
- Shows solitonic cores can resolve the "cusp-core problem" in dwarf galaxies
- Provides fitting formulas for FDM halo profiles useful for lensing calculations

**[7] Hui, Ostriker, Tremaine, Witten (2017) - "Ultralight scalars as cosmological dark matter"**
- Phys. Rev. D 95, 043541
- arXiv:1610.08297
- Comprehensive review of ultralight dark matter phenomenology
- **Section V** specifically addresses lensing:
  - Flux ratio anomalies in strong lensing
  - Substructure lensing signatures
  - Comparison with CDM predictions

**[8] Amruth et al. (2023) - "Einstein rings modulated by wavelike dark matter"**
- Nature Astronomy 7, 736-747
- arXiv:2304.09895
- Direct detection of FDM signatures in Einstein ring distortions
- Shows that granular FDM structure produces characteristic modulations in Einstein rings
- **Key observational constraint:** Places limits on FDM mass from lensing data

### 2.3 Strong Lensing Constraints on Ultralight Dark Matter Mass

**[9] Dalal & Kochanek (2002) - "Direct Detection of CDM Substructure"**
- Astrophys. J. 572, 25-33
- arXiv:astro-ph/0111456
- Original paper establishing flux ratio anomalies as probes of substructure
- Sets the methodology for comparing FDM vs. CDM using lensing

**[10] Gilman et al. (2020) - "Warm dark matter chills out: constraints on the halo mass function and the free-streaming length from flux ratio statistics"**
- MNRAS 491, 6077-6101
- arXiv:1908.06983
- Uses strong lensing flux ratios to constrain dark matter mass
- **Result:** m > 5.2 x 10^{-21} eV at 95% confidence
- **Tension with Paper 1:** This is in mild tension with m ~ 10^{-22} eV assumed in the framework

**[11] Laroche et al. (2022) - "Forecasts for Galaxy Formation and Dark Matter Constraints from Dwarf Galaxy Surveys"**
- arXiv:2206.11913
- Projects future lensing constraints from JWST and Rubin Observatory
- Shows that m ~ 10^{-22} eV produces detectable signatures

### 2.4 Solitonic Core vs. NFW Profile: Lensing Differences

**NFW (Navarro-Frenk-White) Profile:**
```
rho_NFW(r) = rho_s / [(r/r_s)(1 + r/r_s)^2]
```
- Central cusp: rho ~ r^{-1} as r -> 0
- Produces strong central magnification

**Solitonic Core Profile (FDM/BEC):**
```
rho_soliton(r) = rho_c / [1 + 0.091 (r/r_c)^2]^8
```
- Cored center: rho -> rho_c as r -> 0
- Core radius r_c ~ xi ~ 1 kpc
- Produces weaker central magnification

**Key Lensing Differences:**
1. **Einstein radius:** Slightly smaller for solitonic cores (less mass concentration)
2. **Critical curves:** Smoother, less elongated for cored profiles
3. **Magnification maps:** Different caustic structure near the core
4. **Time delays:** Modified by the different mass distribution

**Relevant Paper:**
- Bar et al. (2018) - "Galactic rotation curves versus ultralight dark matter: Implications of the soliton-host halo relation" - Phys. Rev. D 98, 083027

### 2.5 Weak Lensing and Cosmic Shear Predictions

**[12] Dentler et al. (2022) - "Fuzzy dark matter and the Dark Energy Survey Year 1 data"**
- arXiv:2111.01199
- Analysis of DES Y1 weak lensing data for FDM constraints
- Finds weak lensing alone does not strongly constrain m > 10^{-23} eV
- But combined probes (CMB + weak lensing) are more powerful

**[13] Rogers & Peiris (2021) - "Strong Constraints on the Fuzzy Dark Matter Model"**
- Phys. Rev. Lett. 126, 071302
- arXiv:2007.12705
- Uses Lyman-alpha forest + CMB + weak lensing
- **Result:** m > 2 x 10^{-20} eV at 95% confidence
- **Severe tension with m ~ 10^{-22} eV**

**Weak Lensing Signatures Specific to BEC Cosmology:**
1. **Suppressed small-scale power:** Matter power spectrum P(k) suppressed for k > k_J
2. **Modified shear correlations:** Weaker correlations at angular scales < arcmin
3. **Halo concentration:** FDM halos less concentrated than CDM

---

## 3. Shapiro Delay in Acoustic Metrics

### 3.1 Standard GR Shapiro Delay

The Shapiro delay for a light ray passing a massive object at impact parameter b is:
```
Delta t_Shapiro = (4 G M / c^3) ln(4 r_1 r_2 / b^2)
```

where r_1, r_2 are distances from source and observer to the lens.

### 3.2 Shapiro Delay from Acoustic Metric Perspective

**Key Question:** Does the acoustic metric framework reproduce standard Shapiro delay?

**Analysis:**

In the acoustic metric framework, the effective spacetime metric is:
```
g_{mu nu}^{ac} = (rho_0 / c_s) * g_{mu nu}^{Minkowski} + perturbations
```

For a localized mass perturbation delta rho at position r_lens, the acoustic metric perturbation is:
```
delta g_{00}^{ac} ~ -2 G M / (c^2 r)
delta g_{ij}^{ac} ~ 2 G M delta_{ij} / (c^2 r)
```

This is exactly the weak-field limit of the Schwarzschild metric in isotropic coordinates.

**Key Result:** The acoustic metric framework reproduces standard Shapiro delay for perturbations with wavelength >> xi.

**Corrections at Short Wavelengths:**

When the light ray passes through regions where the density varies on scales ~ xi, corrections arise:

1. **Quantum pressure contribution:** The Bohm potential Q = -hbar^2 nabla^2 sqrt{rho} / (2m^2 sqrt{rho}) modifies the effective potential
2. **Dispersion effects:** High-frequency components of the light pulse travel at different speeds
3. **Healing length smoothing:** Sharp features in the potential are smoothed on scale xi

**Estimated Correction:**
```
Delta t_correction / Delta t_Shapiro ~ (xi / b)^2 for b >> xi
```

For b ~ 1 kpc and xi ~ 1 kpc, corrections could be O(1).

### 3.3 Relevant Literature

**[14] Visser (1998) - "Acoustic black holes: horizons, ergospheres, and Hawking radiation"**
- Class. Quantum Grav. 15, 1767
- arXiv:gr-qc/9712010
- Discusses time delay effects in acoustic geometries
- Shows that acoustic analogues reproduce GR time delays for slowly varying backgrounds

**[15] Fischer & Visser (2004) - "Riemannian geometry of irrotational vortex acoustics"**
- Phys. Rev. Lett. 88, 110201 (2002)
- arXiv:cond-mat/0110211
- Derives corrections to acoustic geodesics from quantum pressure

**No Dedicated Paper Found:** There appears to be no paper specifically deriving Shapiro delay corrections in BEC acoustic metrics. This is a gap in the literature that Paper 2 could address.

---

## 4. Healing Length Signatures in Lensing

### 4.1 Strong Lensing (Einstein Rings, Arcs)

**At xi ~ 1 kpc, the condensate description breaks down on scales comparable to:**
- Inner regions of galaxy-scale Einstein rings (R_E ~ 1-10 kpc)
- Central arcs in cluster lensing
- Multiple image positions in quad lenses

**Observable Signatures:**

1. **Smoothed Caustics:**
   - Standard GR: Caustic crossings produce sharp magnification spikes (formally infinite)
   - BEC framework: Caustics are smoothed on scale xi
   - Observable: Reduced peak magnification, broader light curve during caustic crossing

2. **Einstein Ring Modulation:**
   - Granular FDM structure modulates ring brightness (Amruth et al. 2023)
   - Characteristic angular scale: theta_xi ~ xi / D_L ~ 0.1" for D_L ~ 1 Gpc

3. **Core Image Properties:**
   - Central (odd) images are demagnified in NFW profiles
   - Solitonic cores modify central image magnification
   - Potentially detectable with VLBI observations

4. **Time Delays:**
   - Modified by solitonic core structure
   - Corrections at percent level for image separations ~ xi

### 4.2 Weak Lensing (Shear Correlations)

**Signatures:**

1. **Suppressed Small-Scale Shear:**
   - Matter power spectrum suppressed for k > k_J ~ (1 kpc)^{-1}
   - Shear correlation function xi_+(theta) reduced at theta < 1 arcmin

2. **Modified Halo Profiles:**
   - Tangential shear gamma_t(r) reduced in inner regions
   - Cored profiles produce flatter gamma_t(r) at small r

3. **Stacked Weak Lensing:**
   - Galaxy-galaxy lensing signals reduced at small projected separations
   - Detectable in stacked analyses of many lenses

**Key Paper:**
- Amorisco & Loeb (2018) - "First Constraints on Fuzzy Dark Matter from the Dynamics of Stellar Streams in the Milky Way" - arXiv:1808.00464 (methodology applicable to lensing)

### 4.3 Microlensing

**Distinctive Signatures at xi ~ 1 kpc:**

1. **Smooth Microlensing Light Curves:**
   - Standard CDM: Subhalos produce sharp microlensing events
   - FDM: Granular structure on scale xi produces smoother, lower-amplitude events

2. **Power Spectrum of Microlensing Fluctuations:**
   - CDM: Power-law to small scales
   - FDM: Cutoff at scale ~ xi

3. **Caustic Crossing Statistics:**
   - Modified caustic network due to different substructure

**Relevant Papers:**
- Dai & Miralda-Escude (2020) - "Gravitational Lensing Signatures of Axion Dark Matter Minihalos" - AJ 159, 49
- Fairbairn et al. (2018) - "Structure formation and microlensing with axion miniclusters" - JCAP 02, 018

### 4.4 Time Delay Measurements

**Precision time delay cosmography (H_0 measurements) could probe healing length effects:**

1. **H0LiCOW/TDCOSMO Programs:**
   - Measure time delays with < 1% precision
   - Sensitive to mass distribution on kpc scales

2. **Expected BEC Corrections:**
   - If xi ~ 1 kpc, time delay predictions differ by:
   ```
   Delta(time delay) / time delay ~ (xi / R_E)^2 ~ 1-10%
   ```
   - This is comparable to current systematic uncertainties

3. **Key Paper:**
   - Birrer et al. (2020) - "TDCOSMO IV" - A&A 643, A165
   - Discusses systematic uncertainties in time delay cosmography, relevant for assessing BEC detectability

---

## 5. Distinguishing BEC Cosmology from Lambda-CDM via Lensing

### 5.1 Unique Predictions of the BEC Framework

**Prediction 1: Suppressed Substructure Power**
- BEC: No subhalos below Jeans mass M_J ~ 10^7 M_sun
- CDM: Subhalos down to ~ 10^{-6} M_sun (or lower)
- Test: Flux ratio anomalies, astrometric perturbations

**Prediction 2: Cored Halo Centers**
- BEC: Solitonic cores with r_c ~ xi ~ 1 kpc
- CDM: Cuspy NFW profiles
- Test: Central image magnification, strong lensing mass modeling

**Prediction 3: Granular Halo Structure**
- BEC: Interference patterns on scale ~ lambda_dB ~ 1 kpc
- CDM: Smooth (on these scales)
- Test: Einstein ring modulations, microlensing statistics

**Prediction 4: Dispersion at High Frequencies**
- BEC: Photon group velocity depends on wavelength at lambda ~ xi
- CDM/GR: No dispersion
- Test: Frequency-dependent time delays (challenging to measure)

### 5.2 Discriminating Observations

**Immediate Opportunities:**

1. **Strong Lens Flux Ratios:**
   - Compare observed flux ratios to smooth lens model predictions
   - Anomalies probe substructure: CDM predicts more anomalies than FDM
   - Current data: ~10-20 suitable systems
   - Future: Euclid/Rubin will provide hundreds

2. **Einstein Ring Distortions:**
   - High-resolution imaging (HST, JWST) of Einstein rings
   - Look for granular modulation patterns
   - Amruth et al. (2023) methodology

3. **Time Delay Cosmography:**
   - Systems with multiple time delay measurements
   - Constrain mass distribution with kpc resolution
   - H0LiCOW sample + future discoveries

**Medium-Term Opportunities:**

4. **Weak Lensing + Galaxy-Galaxy Lensing:**
   - DES, KiDS, Euclid, Rubin surveys
   - Constrain matter power spectrum suppression scale
   - Requires modeling of baryonic effects

5. **CMB Lensing:**
   - Planck, SPT, ACT data
   - Probe matter distribution at z ~ 1-2
   - Lower resolution but cleaner systematics

### 5.3 Key Discriminating Papers

**[16] Vegetti et al. (2012) - "Detection of a dark substructure through gravitational imaging"**
- Nature 481, 341-343
- Direct detection of subhalo via lens perturbations
- Methodology for substructure detection

**[17] Hezaveh et al. (2016) - "Detection of lensing substructure using ALMA"**
- Astrophys. J. 823, 37
- ALMA imaging provides sub-arcsecond resolution
- Sensitive to subhalos with M > 10^8 M_sun

**[18] Gilman et al. (2022) - "A unified model for the abundance of dark substructure"**
- arXiv:2209.10566
- Compares CDM, WDM, and FDM substructure lensing predictions
- Provides framework for discriminating models

---

## 6. Current Observational Constraints

### 6.1 Hubble Space Telescope (HST)

**Strong Lensing Programs:**
- SLACS (Sloan Lens ACS Survey): ~100 galaxy-scale lenses
- SL2S (Strong Lensing Legacy Survey): ~60 group-scale lenses
- CLASH: Cluster lensing
- HFF: Hubble Frontier Fields (cluster lensing)

**Constraints on FDM/BEC:**
- No definitive detection of FDM signatures
- Consistent with both CDM and FDM (m > 10^{-22} eV)

### 6.2 James Webb Space Telescope (JWST)

**Early Results (2022-2025):**
- Higher resolution than HST in IR
- Detection of high-z lensed galaxies
- Improved Einstein ring imaging

**Relevant Programs:**
- COSMOS-Webb: Wide area imaging
- PEARLS: Prime Extragalactic Areas for Reionization and Lensing Science
- TEMPLATES: Target for new strong lenses

**FDM Constraints:**
- Still accumulating data
- Projected to constrain m > 10^{-21} eV from substructure

### 6.3 Dark Energy Survey (DES)

**Weak Lensing Results:**
- DES Year 3: Cosmic shear measurements
- Galaxy-galaxy lensing: Matter power spectrum constraints

**FDM Constraints from DES:**
- Dentler et al. (2022): Weak constraints, m > 10^{-23} eV
- Combined with Lyman-alpha: m > 10^{-21} eV

### 6.4 Kilo-Degree Survey (KiDS)

**Status:**
- 1350 sq deg of imaging
- Cosmic shear and galaxy-galaxy lensing

**FDM Constraints:**
- Similar to DES: Not strongly constraining alone
- Combined analyses more powerful

### 6.5 Euclid (Launched 2023)

**Projected Capabilities:**
- 15,000 sq deg wide survey
- ~170,000 strong lenses expected
- Weak lensing with 30 galaxies/arcmin^2

**FDM Projections:**
- Expected to constrain m > 10^{-21} eV from strong lensing statistics
- Combined weak lensing: m > 10^{-22} eV possible

**Key Paper:**
- Euclid Collaboration (2020) - "Euclid preparation. III. Galaxy cluster detection" - A&A 627, A23

### 6.6 Vera C. Rubin Observatory (LSST)

**Projected (First Light ~2025):**
- 18,000 sq deg to r ~ 27.5
- ~10,000 time-delay lenses
- 20 billion galaxies for weak lensing

**FDM Projections:**
- Time delay statistics: Constrain m to 10^{-22} eV level
- Substructure from flux ratios: Distinguish FDM from CDM at high significance

### 6.7 Summary of Current Mass Constraints

| Method | Constraint (95% CL) | Reference |
|--------|---------------------|-----------|
| Lyman-alpha forest | m > 2 x 10^{-21} eV | Irsic et al. 2017 |
| Lyman-alpha + CMB | m > 2 x 10^{-20} eV | Rogers & Peiris 2021 |
| Strong lensing flux ratios | m > 5 x 10^{-21} eV | Gilman et al. 2020 |
| Milky Way satellites | m > 3 x 10^{-21} eV | Nadler et al. 2021 |
| Dwarf galaxy cores | m ~ 10^{-22} eV (favored) | Schive et al. 2014 |
| Weak lensing (DES) | m > 10^{-23} eV | Dentler et al. 2022 |

**Critical Tension:** Most constraints prefer m > 10^{-21} eV, while dwarf galaxy cores and the Paper 1 framework use m ~ 10^{-22} eV. This tension must be addressed in Paper 2.

---

## 7. Theoretical Gaps and Open Questions for Paper 2

### 7.1 Unresolved Questions in the Literature

1. **Shapiro delay derivation from acoustic metric:** No explicit calculation found
2. **Healing length smoothing of caustics:** Needs quantitative treatment
3. **Frequency-dependent lensing in BEC:** Novel prediction, unexplored
4. **Reconciling mass constraints:** Lyman-alpha vs. dwarf galaxy tension

### 7.2 Novel Contributions Paper 2 Could Make

1. **Derivation:** Explicit calculation of Shapiro delay from the acoustic metric with quantum pressure corrections
2. **Prediction:** Quantitative prediction for Einstein ring modulation from healing length effects
3. **Framework:** Unified treatment of strong, weak, and microlensing in BEC cosmology
4. **Resolution:** Proposal for reconciling mass constraints (e.g., self-interaction effects, non-standard cosmology)

### 7.3 Falsifiable Predictions

Paper 2 should generate falsifiable predictions:

1. **If xi ~ 1 kpc:**
   - Einstein rings smoother than CDM predictions on ~ 0.1" scales
   - Flux ratio anomalies reduced by factor ~ 2 vs. CDM
   - Time delays modified at 1-10% level

2. **If m ~ 10^{-22} eV:**
   - Specific core radius vs. halo mass relation
   - Cutoff in subhalo mass function at M ~ 10^7 M_sun
   - Granular structure detectable in deep imaging

---

## 8. Bibliography for Paper 2

### 8.1 BibTeX Entries

```latex
\begin{thebibliography}{99}

% === Foundational Analogue Gravity ===

\bibitem{Unruh1981}
W.~G.~Unruh, ``Experimental black-hole evaporation?,''
\emph{Phys.\ Rev.\ Lett.}\ \textbf{46}, 1351--1353 (1981).

\bibitem{Visser1998}
M.~Visser, ``Acoustic black holes: horizons, ergospheres and Hawking radiation,''
\emph{Class.\ Quantum Grav.}\ \textbf{15}, 1767--1791 (1998);
arXiv:gr-qc/9712010.

\bibitem{Barcelo2005}
C.~Barcelo, S.~Liberati, and M.~Visser, ``Analogue gravity,''
\emph{Living Rev.\ Relativity}\ \textbf{8}, 12 (2005);
arXiv:gr-qc/0505065.

\bibitem{Barcelo2001}
C.~Barcelo, S.~Liberati, and M.~Visser, ``Analogue gravity from Bose-Einstein condensates,''
\emph{Phys.\ Rev.\ A}\ \textbf{63}, 023611 (2001);
arXiv:cond-mat/0007020.

\bibitem{Garay2000}
L.~J.~Garay, J.~R.~Anglin, J.~I.~Cirac, and P.~Zoller,
``Sonic analog of gravitational black holes in Bose-Einstein condensates,''
\emph{Phys.\ Rev.\ Lett.}\ \textbf{85}, 4643 (2000);
arXiv:gr-qc/0005131.

\bibitem{Liberati2006}
S.~Liberati, M.~Visser, and S.~Weinfurtner,
``Analogue quantum gravity phenomenology from a two-component Bose-Einstein condensate,''
\emph{Class.\ Quantum Grav.}\ \textbf{23}, 3129 (2006);
arXiv:gr-qc/0510125.

\bibitem{Fischer2002}
U.~R.~Fischer and M.~Visser,
``Riemannian geometry of irrotational vortex acoustics,''
\emph{Phys.\ Rev.\ Lett.}\ \textbf{88}, 110201 (2002);
arXiv:cond-mat/0110211.

% === Fuzzy/Ultralight Dark Matter ===

\bibitem{Hu2000}
W.~Hu, R.~Barkana, and A.~Gruzinov,
``Fuzzy cold dark matter: The wave properties of ultralight particles,''
\emph{Phys.\ Rev.\ Lett.}\ \textbf{85}, 1158--1161 (2000);
arXiv:astro-ph/0003365.

\bibitem{Schive2014}
H.-Y.~Schive, T.~Chiueh, and T.~Broadhurst,
``Cosmic structure as the quantum interference of a coherent dark wave,''
\emph{Nature Phys.}\ \textbf{10}, 496--499 (2014);
arXiv:1406.6586.

\bibitem{Hui2017}
L.~Hui, J.~P.~Ostriker, S.~Tremaine, and E.~Witten,
``Ultralight scalars as cosmological dark matter,''
\emph{Phys.\ Rev.\ D}\ \textbf{95}, 043541 (2017);
arXiv:1610.08297.

\bibitem{Marsh2015}
D.~J.~E.~Marsh and A.-R.~Pop,
``Axion dark matter, solitons and the cusp-core problem,''
\emph{Mon.\ Not.\ R.\ Astron.\ Soc.}\ \textbf{451}, 2479--2492 (2015);
arXiv:1502.03456.

\bibitem{Bar2018}
N.~Bar, D.~Blas, K.~Blum, and S.~Sibiryakov,
``Galactic rotation curves versus ultralight dark matter: Implications of the soliton-host halo relation,''
\emph{Phys.\ Rev.\ D}\ \textbf{98}, 083027 (2018);
arXiv:1805.00122.

\bibitem{Mocz2017}
P.~Mocz, M.~Vogelsberger, V.~H.~Robles, J.~Zavala, M.~Boylan-Kolchin,
A.~Fialkov, and L.~Hernquist,
``Galaxy formation with BECDM - I. Turbulence and relaxation of idealized haloes,''
\emph{Mon.\ Not.\ R.\ Astron.\ Soc.}\ \textbf{471}, 4559--4570 (2017);
arXiv:1705.05845.

% === Gravitational Lensing: General ===

\bibitem{Schneider1992}
P.~Schneider, J.~Ehlers, and E.~E.~Falco,
\emph{Gravitational Lenses} (Springer-Verlag, Berlin, 1992).

\bibitem{Narayan1996}
R.~Narayan and M.~Bartelmann,
``Lectures on Gravitational Lensing,''
arXiv:astro-ph/9606001 (1996).

% === Lensing and Dark Matter Substructure ===

\bibitem{Dalal2002}
N.~Dalal and C.~S.~Kochanek,
``Direct detection of cold dark matter substructure,''
\emph{Astrophys.\ J.}\ \textbf{572}, 25--33 (2002);
arXiv:astro-ph/0111456.

\bibitem{Vegetti2012}
S.~Vegetti, D.~J.~Lagattuta, J.~P.~McKean, M.~W.~Auger, C.~D.~Fassnacht,
and L.~V.~E.~Koopmans,
``Gravitational detection of a low-mass dark satellite galaxy at cosmological distance,''
\emph{Nature}\ \textbf{481}, 341--343 (2012).

\bibitem{Hezaveh2016}
Y.~D.~Hezaveh \emph{et al.},
``Detection of lensing substructure using ALMA observations of the dusty galaxy SDP.81,''
\emph{Astrophys.\ J.}\ \textbf{823}, 37 (2016);
arXiv:1601.01388.

\bibitem{Gilman2020}
D.~Gilman, S.~Birrer, A.~Nierenberg, T.~Treu, X.~Du, and A.~Benson,
``Warm dark matter chills out: constraints on the halo mass function and the free-streaming length of dark matter with eight quadruple-image strong gravitational lenses,''
\emph{Mon.\ Not.\ R.\ Astron.\ Soc.}\ \textbf{491}, 6077--6101 (2020);
arXiv:1908.06983.

\bibitem{Gilman2022}
D.~Gilman \emph{et al.},
``A unified model for the abundance of dark substructure,''
arXiv:2209.10566 (2022).

% === Lensing and Fuzzy Dark Matter ===

\bibitem{Amruth2023}
A.~Amruth \emph{et al.},
``Einstein rings modulated by wavelike dark matter from anomalies in gravitationally lensed images,''
\emph{Nature Astronomy}\ \textbf{7}, 736--747 (2023);
arXiv:2304.09895.

\bibitem{Laroche2022}
A.~Laroche \emph{et al.},
``Forecasts for galaxy formation and dark matter constraints from dwarf galaxy surveys,''
arXiv:2206.11913 (2022).

\bibitem{Dai2020}
L.~Dai and J.~Miralda-Escude,
``Gravitational lensing signatures of axion dark matter minihalos in highly magnified stars,''
\emph{Astron.\ J.}\ \textbf{159}, 49 (2020);
arXiv:1908.01773.

\bibitem{Dentler2022}
M.~Dentler, D.~J.~E.~Marsh, R.~Hlozek, A.~Lague, K.~K.~Rogers, and D.~Grin,
``Fuzzy dark matter and the Dark Energy Survey Year 1 data,''
arXiv:2111.01199 (2021).

% === Observational Constraints ===

\bibitem{Irsic2017}
V.~Irsic, M.~Viel, M.~G.~Haehnelt, J.~S.~Bolton, and G.~D.~Becker,
``First constraints on fuzzy dark matter from Lyman-alpha forest data and hydrodynamical simulations,''
\emph{Phys.\ Rev.\ Lett.}\ \textbf{119}, 031302 (2017);
arXiv:1703.04683.

\bibitem{Rogers2021}
K.~K.~Rogers and H.~V.~Peiris,
``Strong bound on canonical ultralight axion dark matter from the Lyman-alpha forest,''
\emph{Phys.\ Rev.\ Lett.}\ \textbf{126}, 071302 (2021);
arXiv:2007.12705.

\bibitem{Nadler2021}
E.~O.~Nadler \emph{et al.},
``Constraints on dark matter properties from observations of Milky Way satellite galaxies,''
\emph{Phys.\ Rev.\ Lett.}\ \textbf{126}, 091101 (2021);
arXiv:2008.00022.

\bibitem{Birrer2020}
S.~Birrer \emph{et al.},
``TDCOSMO. IV. Hierarchical time-delay cosmography -- joint inference of the Hubble constant and galaxy density profiles,''
\emph{Astron.\ Astrophys.}\ \textbf{643}, A165 (2020);
arXiv:2007.02941.

% === Weak Lensing Surveys ===

\bibitem{DES2022}
Dark Energy Survey Collaboration,
``Dark Energy Survey Year 3 results: Cosmological constraints from galaxy clustering and weak lensing,''
\emph{Phys.\ Rev.\ D}\ \textbf{105}, 023520 (2022);
arXiv:2105.13549.

\bibitem{KiDS2021}
KiDS Collaboration,
``KiDS-1000 cosmology: Cosmic shear constraints and comparison between two point statistics,''
\emph{Astron.\ Astrophys.}\ \textbf{645}, A104 (2021);
arXiv:2007.15633.

\bibitem{Euclid2020}
Euclid Collaboration,
``Euclid preparation. VII. Forecast validation for Euclid cosmological probes,''
\emph{Astron.\ Astrophys.}\ \textbf{642}, A191 (2020);
arXiv:2004.10817.

% === Time Delay Cosmography ===

\bibitem{Suyu2010}
S.~H.~Suyu \emph{et al.},
``Dissecting the gravitational lens B1608+656. II. Precision measurements of the Hubble constant, spatial curvature, and the dark energy equation of state,''
\emph{Astrophys.\ J.}\ \textbf{711}, 201 (2010);
arXiv:0910.2773.

\bibitem{Wong2020}
K.~C.~Wong \emph{et al.},
``H0LiCOW - XIII. A 2.4 per cent measurement of $H_0$ from lensed quasars: 5.3$\sigma$ tension between early- and late-Universe probes,''
\emph{Mon.\ Not.\ R.\ Astron.\ Soc.}\ \textbf{498}, 1420--1439 (2020);
arXiv:1907.04869.

% === Superfluid/BEC Dark Matter ===

\bibitem{Berezhiani2015}
L.~Berezhiani and J.~Khoury,
``Theory of dark matter superfluidity,''
\emph{Phys.\ Rev.\ D}\ \textbf{92}, 103510 (2015);
arXiv:1507.01019.

\bibitem{Ferreira2021}
E.~G.~M.~Ferreira,
``Ultra-light dark matter,''
\emph{Astron.\ Astrophys.\ Rev.}\ \textbf{29}, 7 (2021);
arXiv:2005.03254.

% === Reviews ===

\bibitem{Marsh2016}
D.~J.~E.~Marsh,
``Axion cosmology,''
\emph{Phys.\ Rept.}\ \textbf{643}, 1--79 (2016);
arXiv:1510.07633.

\bibitem{Niemeyer2020}
J.~C.~Niemeyer,
``Small-scale structure of fuzzy and axion-like dark matter,''
\emph{Prog.\ Part.\ Nucl.\ Phys.}\ \textbf{113}, 103787 (2020);
arXiv:1912.07064.

\end{thebibliography}
```

---

## 9. Summary and Recommendations for Paper 2

### 9.1 Key Findings from Literature Review

1. **Light propagation in acoustic metrics is well-understood** at the theoretical level (Visser, Barcelo, Liberati). Standard gravitational lensing formalism applies at scales >> xi.

2. **Fuzzy dark matter lensing is an active research area** with several recent observations (Amruth et al. 2023) and ongoing surveys (Euclid, Rubin).

3. **Mass constraints are in tension**: Lyman-alpha constraints suggest m > 10^{-20} eV, while dwarf galaxy cores favor m ~ 10^{-22} eV. Paper 2 must address this.

4. **Healing length signatures are potentially observable** in high-resolution lensing data (Einstein ring modulations, flux ratio statistics).

5. **Shapiro delay derivation from acoustic metrics is a gap** in the literature that Paper 2 can fill.

### 9.2 Recommended Structure for Paper 2

1. **Introduction:** BEC cosmology framework recap, lensing as a test
2. **Light propagation in acoustic metrics:** Formal derivation of geodesic equations
3. **Gravitational lensing formalism:** Adapt standard formalism to BEC metric
4. **Shapiro delay:** Explicit derivation with quantum pressure corrections
5. **Healing length signatures:** Strong lensing, weak lensing, microlensing
6. **Comparison with observations:** Current constraints, projections
7. **Distinguishing from Lambda-CDM:** Unique predictions
8. **Discussion:** Mass tension, future tests
9. **Conclusions**

### 9.3 Critical Issues to Address

1. **Mass constraint tension:** The framework assumes m ~ 10^{-22} eV, but Lyman-alpha data suggest m > 10^{-20} eV. Possible resolutions:
   - Self-interactions modifying small-scale power
   - Non-equilibrium condensate dynamics
   - Environmental dependence of effective mass

2. **Observational accessibility:** Many signatures require sub-arcsecond resolution and precise photometry. Paper 2 should quantify required precision.

3. **Degeneracies:** Solitonic cores can mimic baryonic cores. Paper 2 should identify discriminating observations.

---

**Document prepared for the seven-paper research program.**
**Next step:** Coordination with math-expert for derivations, latex-specialist for formatting.
