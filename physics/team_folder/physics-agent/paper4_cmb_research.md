# Paper 4: CMB Power Spectrum and Perturbations - Research Compilation

## Context: BEC Condensate Cosmology Framework

From Paper 1, the key elements relevant to CMB physics are:

1. **Transient energy component**: u_mech(a) with Gaussian profile centered at a_c ~ 10^{-3}
2. **Equation of state**: w_mech(a) = -1 + ln(a/a_c)/(3*sigma_mech^2)
3. **BEC parameters**: m ~ 10^{-22} eV, healing length xi ~ 1 kpc
4. **Sound speed**: c_s = c (relativistic limit)
5. **Modified Friedmann equation**: Standard form but with additional energy component
6. **Sound horizon**: May be modified by u_mech(a) presence

The transient component u_mech(a) is similar in spirit to Early Dark Energy (EDE) models, peaking at a characteristic scale factor and potentially affecting the sound horizon at recombination.

---

## 1. CMB in Early Dark Energy and Modified Expansion Models

### 1.1 How Early Dark Energy Affects CMB Spectra

Early Dark Energy (EDE) refers to a component that contributes a non-negligible fraction of the total energy density before recombination, then dilutes rapidly afterward. This is phenomenologically similar to the u_mech(a) component in the BEC framework.

**Key effects on CMB:**

1. **Acoustic Peak Positions**: EDE increases H(a) before recombination, reducing the sound horizon r_s. Since peak positions scale as l ~ pi*d_A/r_s, reduced r_s shifts peaks to higher l (smaller angular scales) for fixed angular diameter distance d_A. However, the degeneracy with other parameters makes this complex.

2. **Peak Heights and Ratios**: Modified expansion history changes the driving of acoustic oscillations. The first peak height is sensitive to the matter-radiation equality epoch. EDE presence shifts the effective equality, modifying peak ratios.

3. **Damping Tail**: Silk damping depends on the photon diffusion scale r_d, which scales with the integrated photon mean free path. EDE changes H(a), modifying r_d and thus the damping envelope.

4. **Lensing Amplitude**: CMB lensing depends on the integrated matter distribution along the line of sight. Modified expansion affects structure growth, changing the lensing amplitude A_L.

5. **ISW Effect**: The Integrated Sachs-Wolfe effect depends on the time evolution of gravitational potentials. EDE modifies this, particularly near recombination.

### 1.2 Key Papers on EDE and CMB

#### Poulin et al. (2019) - EDE Implementation

**Citation:**
V. Poulin, T. L. Smith, T. Karwal, and M. Kamionkowski, "Early Dark Energy Can Resolve The Hubble Tension," Phys. Rev. Lett. **123**, 231301 (2019). [arXiv:1811.04083]

**Key findings:**
- Proposed EDE as a resolution to the H_0 tension
- EDE contributes ~10% of energy density around z ~ 3000-5000 (a ~ 10^{-4} to 10^{-3})
- Implemented as an oscillating scalar field with potential V(phi) ~ [1 - cos(phi/f)]^n
- Sound speed c_s^2 depends on the potential; for n=3, c_s^2 ~ 1 at the peak
- Best-fit: f_EDE(z_c) ~ 0.1, log10(z_c) ~ 3.5
- Shifts H_0 from ~67 to ~72 km/s/Mpc while maintaining good CMB fit

**Implementation in CLASS/CAMB:**
- EDE implemented as a fluid with time-varying w(a) and c_s^2(a)
- Requires modification of background.c (or equivalent)
- Perturbation equations need c_s^2, w, and anisotropic stress sigma
- Available in CLASS through hi_class or AxionCAMB

#### Hill et al. (2020) - EDE and S_8 Tension

**Citation:**
J. C. Hill, E. McDonough, M. W. Toomey, and S. Alexander, "Early dark energy does not restore cosmological concordance," Phys. Rev. D **102**, 043507 (2020). [arXiv:2003.07355]

**Key findings:**
- EDE resolves H_0 tension but exacerbates S_8 tension
- Adding EDE increases sigma_8 by ~5-10%
- S_8 = sigma_8 * sqrt(Omega_m/0.3) increases from ~0.83 to ~0.88
- This worsens agreement with weak lensing surveys (KiDS, DES) which find S_8 ~ 0.76
- Concludes EDE is not a complete solution to cosmological tensions

**Implications for BEC framework:**
- If u_mech(a) behaves like EDE, similar S_8 increase expected
- Need to check if BEC's small-scale suppression (from healing length xi) can compensate
- The Jeans-like cutoff at scale k_J ~ 1/(xi) could reduce sigma_8

#### Smith, Poulin, Amin (2020) - Oscillating Scalar Fields

**Citation:**
T. L. Smith, V. Poulin, and M. A. Amin, "Oscillating scalar fields and the Hubble tension: a resolution with novel signatures," Phys. Rev. D **101**, 063523 (2020). [arXiv:1908.06995]

**Key findings:**
- Detailed analysis of oscillating scalar field EDE
- Oscillation frequency determines effective w(a) and c_s^2(a)
- For rapid oscillations: w_eff ~ (n-1)/(n+1) for V ~ phi^{2n}
- Sound speed oscillates but averages to c_s^2 ~ (2n-1)/(2n+1)
- Perturbations in EDE field cluster on scales k < k_J(EDE)
- Novel signatures in CMB polarization at high l

**Relevance to BEC framework:**
- u_mech(a) has w_mech(a) = -1 + ln(a/a_c)/(3*sigma^2)
- At a = a_c: w_mech = -1 (cosmological constant-like)
- For a > a_c: w_mech increases, eventually becoming stiff
- For a < a_c: w_mech < -1 (phantom-like)
- This is different from oscillating scalar field behavior
- BEC framework needs its own perturbation treatment

### 1.3 Effect on Acoustic Peaks and Damping Tail

**Acoustic peaks:**
The CMB angular power spectrum has peaks at multipoles:
l_n ~ n * pi * d_A(z_*) / r_s(z_*)

where z_* ~ 1090 is the redshift of last scattering, d_A is the angular diameter distance, and r_s is the sound horizon.

Sound horizon at decoupling:
r_s(z_*) = integral from 0 to a_* of [c_s(a) / (a^2 H(a))] da

where c_s(a) = c / sqrt(3(1 + R(a))) with R = 3*rho_b/(4*rho_gamma).

**EDE effect:** Increasing H(a) at early times reduces r_s, shifting peaks to higher l. To maintain the observed peak positions, other parameters must adjust (n_s, Omega_m h^2).

**Damping tail:**
Silk damping occurs below the photon diffusion scale:
r_d^2 = integral of [c^2 / (a^2 H(a) * n_e * sigma_T)] * (R^2 + 16(1+R)/15) / (6(1+R)^2) da

EDE increases H(a), reducing r_d and thus reducing damping. This preserves more power at high l, creating a distinct signature.

**CMB lensing:**
The lensing potential depends on the integrated Weyl potential:
phi_lens(n) ~ integral of [Phi + Psi] * g(chi) d chi

where g(chi) is the lensing kernel. Modified expansion affects structure growth, changing Phi + Psi.

---

## 2. CMB in Fuzzy Dark Matter Models

### 2.1 Fuzzy Dark Matter (FDM) Overview

Fuzzy dark matter (FDM), also called ultralight axion dark matter or wave dark matter, consists of ultralight bosons with mass m ~ 10^{-22} eV. This is precisely the mass scale suggested by the BEC framework in Paper 1.

**Key features:**
- de Broglie wavelength: lambda_dB ~ h/(m*v) ~ kpc for v ~ 100 km/s
- Jeans/quantum pressure scale: k_J ~ (m * H)^{1/2} / hbar
- Suppression of structure below k_J
- Solitonic cores in halos with radius ~ lambda_dB

### 2.2 Effect on Matter Power Spectrum

The matter power spectrum P(k) is suppressed below the Jeans scale:
P_FDM(k) = T^2(k) * P_CDM(k)

where the transfer function T(k) ~ 1 for k << k_J and T(k) -> 0 for k >> k_J.

Approximate transfer function (Hu et al. 2000):
T(k) = cos(x^3) / (1 + x^8)
where x = 1.61 * (m / 10^{-22} eV)^{1/18} * (k / k_J,eq)

**For m = 10^{-22} eV:**
- k_J ~ 10 h/Mpc at matter-radiation equality
- Half-power at k_1/2 ~ 4 h/Mpc
- Strong suppression for k > 30 h/Mpc

### 2.3 Effect on CMB Lensing

CMB lensing probes the matter distribution at z ~ 0.5-3. FDM suppression of small-scale power reduces the lensing potential:

C_l^{phi phi} = integral of P_m(k, z) * [lensing kernel]^2 dk dz

For m ~ 10^{-22} eV, the suppression is modest at CMB lensing scales (l ~ 100-1000 corresponds to k ~ 0.01-0.1 h/Mpc, well below k_J).

However, for smaller masses or combined with other probes, constraints can be derived.

### 2.4 Hlozek et al. Constraints from Planck

**Citation:**
R. Hlozek, D. Grin, D. J. E. Marsh, and P. G. Ferreira, "A search for ultralight axions using precision cosmological data," Phys. Rev. D **91**, 103512 (2015). [arXiv:1410.2896]

**Key findings:**
- Used Planck 2013 + WMAP polarization + ACT/SPT high-l
- Constrained ultralight axion fraction Omega_a/Omega_DM as function of mass
- For m ~ 10^{-22} eV: Omega_a/Omega_DM < 0.05 (95% CL)
- For m ~ 10^{-24} eV: Omega_a/Omega_DM < 0.01
- Primary constraint comes from matter power spectrum shape via CMB lensing

**Updated constraints (Hlozek et al. 2018):**
R. Hlozek, D. J. E. Marsh, and D. Grin, "Using the Full Power of the Cosmic Microwave Background to Probe Axion Dark Matter," Mon. Not. R. Astron. Soc. **476**, 3063-3085 (2018). [arXiv:1708.05681]

- Planck 2015 data gives: m > 10^{-24} eV (95% CL) if axions are all DM
- For m = 10^{-22} eV: allows Omega_a ~ Omega_DM with marginal tension

**Implications for BEC framework:**
- m ~ 10^{-22} eV is marginally consistent with Planck CMB constraints
- Additional suppression from BEC healing length xi ~ 1 kpc may be constrained
- Need detailed comparison of FDM vs BEC suppression patterns

---

## 3. Sound Horizon Modifications

### 3.1 How u_mech(a) Affects r_s

The sound horizon at decoupling is:
r_s(a_*) = integral from 0 to a_* of [c_s(a') / (a'^2 H(a'))] da'

where:
- c_s = c / sqrt(3(1 + R)) with R = 3*Omega_b*a / (4*Omega_gamma)
- H(a) = H_0 * sqrt(Omega_r/a^4 + Omega_m/a^3 + Omega_Lambda + Omega_mech(a))

The BEC transient component contributes:
Omega_mech(a) = (u_mech(a) / rho_crit) / H_0^2

With Gaussian profile:
u_mech(a) = u_0 * exp[-(ln(a) - ln(a_c))^2 / (2*sigma^2)]

**Effect on r_s:**
Adding u_mech increases H(a) during the epoch a ~ a_c, reducing the integrand and thus reducing r_s.

### 3.2 Analytic Estimate of Delta r_s / r_s

For small perturbations, we can estimate:
Delta r_s / r_s ~ - integral of [f_mech(a') / (2 H(a')^2)] * [c_s(a') / (a'^2 H(a'))] da' / r_s

where f_mech = u_mech / (3 H^2 / 8*pi*G) is the fractional energy density in u_mech.

**Order of magnitude:**
If f_mech(a_c) ~ 0.1 (10% of energy density at peak) and the Gaussian width sigma ~ 0.5 in log(a):

Delta r_s / r_s ~ -f_mech * sigma * (c_s(a_c) / (a_c * H(a_c))) / r_s
                ~ -0.1 * 0.5 * (contribution from epoch a_c) / (total integral)

For a_c ~ 10^{-3} (z_c ~ 1000, near recombination), the contribution is significant:
Delta r_s / r_s ~ -0.01 to -0.05 (i.e., 1-5% reduction)

**Numerical estimate from EDE literature:**
Poulin et al. (2019) find f_EDE ~ 0.1 at z_c ~ 3500 gives:
- Delta r_s / r_s ~ -0.03 (-3%)
- This shifts H_0 from 67 to 72 km/s/Mpc

### 3.3 Connection to H_0 Tension Resolution

The H_0 tension is:
- Planck (CMB): H_0 = 67.4 +/- 0.5 km/s/Mpc
- SH0ES (local): H_0 = 73.0 +/- 1.0 km/s/Mpc

The CMB constrains the angular scale theta_* = r_s(z_*) / d_A(z_*), not H_0 directly.

To increase inferred H_0:
1. Reduce r_s(z_*) [EDE approach]
2. Reduce d_A(z_*) [late-time modifications]
3. Both

**Sound horizon approach (EDE/u_mech):**
Reducing r_s while keeping theta_* fixed requires reducing d_A proportionally.
d_A(z) = integral from 0 to z of [c / H(z')] dz'

Reducing r_s by 3% and adjusting other parameters can increase H_0 to ~72 km/s/Mpc.

### 3.4 Current r_s Measurements

**Planck 2018:**
r_s(z_drag) = 147.09 +/- 0.26 Mpc (Lambda CDM)
where z_drag ~ 1060 is the baryon drag epoch.

**BAO measurements:**
BAO observations measure r_s * H(z) / c and r_s / d_A(z).

BOSS DR12 (Alam et al. 2017):
- z = 0.38: D_V/r_s = 10.23 +/- 0.17
- z = 0.51: D_V/r_s = 13.36 +/- 0.21
- z = 0.61: D_V/r_s = 15.72 +/- 0.26

Assuming Lambda CDM expansion, these imply r_s ~ 147 Mpc, consistent with Planck.

**EDE/modified expansion:**
If r_s is reduced to ~140 Mpc, BAO distances must be reinterpreted, potentially giving different D_V values.

---

## 4. Perturbation Theory for the Transient Component

### 4.1 Does u_mech Have Density Perturbations?

In the BEC framework, u_mech(a) arises from boundary dynamics at the condensate-protofluid interface. The key question is whether this component carries perturbations or is a smooth background.

**Scenarios:**

1. **Smooth background (no perturbations):**
   - u_mech is homogeneous, only affecting expansion
   - Perturbation equations unchanged except for modified H(a)
   - Simplest implementation

2. **Perturbed component (like scalar field EDE):**
   - u_mech has density contrast delta_mech
   - Sound speed c_s,mech^2 determines clustering
   - Anisotropic stress sigma_mech possible

**BEC interpretation:**
The transient energy u_mech represents kinetic/potential energy in the expanding boundary layer. If this boundary has structure (e.g., vortices, ripples), perturbations exist.

Given the GP equation origin, perturbations should follow the quantum pressure / healing length physics:
- Perturbations suppressed below k < 1/xi ~ 1/kpc ~ 1000 Mpc^{-1}
- At CMB scales (k ~ 0.001-0.1 Mpc^{-1}), u_mech should cluster like dust

### 4.2 Sound Speed and Anisotropic Stress

For a general fluid component, perturbation equations require:
- Sound speed: c_s^2 = delta P / delta rho
- Anisotropic stress: (rho + P) * sigma = -(k^2) * Pi_s (shear)

**For u_mech with w_mech(a) = -1 + ln(a/a_c)/(3*sigma^2):**

The adiabatic sound speed is:
c_s,ad^2 = w - (d ln w)/(d ln a) / (3(1+w))

At a = a_c where w = -1:
c_s,ad^2 is ill-defined (w = -1 makes denominator zero)

For a near a_c:
w ~ -1 + (ln(a/a_c))/(3*sigma^2)
dw/d(ln a) = 1/(3*sigma^2)

c_s,ad^2 = w - [1/(3*sigma^2)] / [3(1 + w)]

As w -> -1, c_s,ad^2 -> -1 - [1/(3*sigma^2)] / [3*epsilon] where epsilon -> 0
This diverges, indicating the adiabatic approximation breaks down.

**Physical interpretation:**
For scalar field EDE, c_s^2 = 1 (canonical kinetic term) or c_s^2 = k^2/(k^2 + m^2) (massive field).

For BEC u_mech, the sound speed should be set by the condensate physics:
c_s^2 = c^2 (relativistic limit, from Postulate 4)

**Anisotropic stress:**
Scalar fields have no anisotropic stress (sigma = 0) to linear order.
BEC may have anisotropic stress from:
- Quantum pressure gradients
- Vortex contributions
- Boundary effects

For simplicity, assume sigma_mech = 0 initially.

### 4.3 Coupling to Photon-Baryon Fluid

The photon-baryon fluid obeys:
d delta_gamma / dt + (4/3) * theta_gamma / a = 0
d theta_gamma / dt + H * theta_gamma = k^2 * (delta_gamma/4 + Phi) + ...

where Phi is the gravitational potential determined by:
k^2 * Phi = -4*pi*G*a^2 * sum_i [rho_i * delta_i + 3*(rho_i + P_i)*theta_i/k^2]

**Effect of u_mech perturbations:**
If delta_mech != 0, it contributes to Phi:
Delta(k^2 Phi) = -4*pi*G*a^2 * u_mech * delta_mech / c^2

This modifies the gravitational driving of acoustic oscillations.

**For smooth u_mech (delta_mech = 0):**
Only the background H(a) is modified, changing the timing of oscillations.

### 4.4 Comparison to Standard Scalar Field EDE

**Scalar field EDE (Poulin et al.):**
- Field phi obeys Klein-Gordon: phi'' + 2*H*phi' + dV/dphi = 0
- Perturbations: delta_phi obeys perturbed KG equation
- Sound speed: c_s^2 = 1 (canonical)
- Anisotropic stress: sigma = 0

**BEC u_mech:**
- Derived from GP equation, not independent field equation
- Sound speed: c_s^2 = c^2 (relativistic BEC)
- May have different clustering behavior due to quantum pressure
- Equation of state w(a) differs from oscillating field

**Key differences:**
1. EDE has w ~ 1/3 during oscillations; u_mech has w varying continuously through -1
2. EDE clusters on all scales; u_mech may be suppressed below healing length
3. EDE perturbations well-defined; u_mech perturbation treatment needs development

---

## 5. Boltzmann Code Requirements

### 5.1 Modifications to CLASS/CAMB

To compute CMB spectra with u_mech(a), the following modifications are needed:

**Background module:**
1. Add u_mech(a) to total energy density:
   rho_total = rho_r + rho_m + rho_Lambda + u_mech(a)/c^2

2. Implement Gaussian profile:
   u_mech(a) = u_0 * exp(-(ln(a/a_c))^2 / (2*sigma^2))

3. Compute w_mech(a) for equation of state:
   w_mech = -1 + ln(a/a_c) / (3*sigma^2)

4. Modify Hubble parameter:
   H^2 = (8*pi*G/3) * (rho_r + rho_m + rho_Lambda + u_mech/c^2)

**Perturbation module:**
1. Add u_mech perturbation equations (if perturbed):
   delta_mech' = -(1 + w_mech) * (theta_mech - 3*Phi') - 3*H*(c_s^2 - w_mech)*delta_mech
   theta_mech' = -H*(1 - 3*w_mech)*theta_mech + k^2*c_s^2*delta_mech/(1+w_mech) + k^2*Phi

2. Set sound speed: c_s^2 = 1 (or parameterize)
3. Set anisotropic stress: sigma_mech = 0

**Initial conditions:**
- Adiabatic: delta_mech = (1 + w_mech) * delta_tot
- Isocurvature: delta_mech = delta_mech,iso (if u_mech has independent origin)

### 5.2 Existing Implementations

**AxionCAMB:**
- Implements ultralight axion dark matter
- Can handle oscillating scalar fields
- Source: https://github.com/dgrin1/axionCAMB

**hi_class (Horndeski CLASS):**
- Implements general scalar-tensor theories
- Can handle EDE as special case
- Source: https://github.com/miguelzuma/hi_class_public

**CLASS with EDE:**
- Patches available from Poulin et al.
- Implements axion-like EDE with potential V ~ (1 - cos(phi/f))^n
- Source: https://github.com/PoulinV/AxiCLASS

**For BEC u_mech:**
Need custom implementation since w_mech(a) differs from standard EDE.

### 5.3 Parameters for MCMC

**Standard Lambda CDM parameters (6):**
1. Omega_b h^2 - baryon density
2. Omega_c h^2 - cold dark matter density
3. 100*theta_s - angular size of sound horizon
4. tau - optical depth to reionization
5. ln(10^10 A_s) - primordial amplitude
6. n_s - scalar spectral index

**Additional u_mech parameters (3-4):**
7. f_mech(a_c) - fractional energy density at peak
8. log10(a_c) - scale factor at peak (or log10(z_c))
9. sigma - width in log(a)
10. c_s,mech^2 - sound speed (optional, may fix to 1)

**Derived parameters:**
- H_0 - derived from theta_s and background
- sigma_8 - derived from perturbation evolution
- r_s(z_drag) - derived from background
- S_8 = sigma_8 * sqrt(Omega_m/0.3)

### 5.4 Planck 2018 Best-Fit Parameters

**Lambda CDM best-fit (Planck TT,TE,EE+lowE+lensing):**
- Omega_b h^2 = 0.02237 +/- 0.00015
- Omega_c h^2 = 0.1200 +/- 0.0012
- 100*theta_MC = 1.04092 +/- 0.00031
- tau = 0.0544 +/- 0.0073
- ln(10^10 A_s) = 3.044 +/- 0.014
- n_s = 0.9649 +/- 0.0042

**Derived:**
- H_0 = 67.36 +/- 0.54 km/s/Mpc
- Omega_m = 0.3153 +/- 0.0073
- sigma_8 = 0.8111 +/- 0.0060
- S_8 = 0.832 +/- 0.013
- r_s(z_drag) = 147.09 +/- 0.26 Mpc

---

## 6. Current Constraints and Tensions

### 6.1 Planck 2018 Best-Fit Lambda CDM

**Citation:**
Planck Collaboration (N. Aghanim et al.), "Planck 2018 results. VI. Cosmological parameters," Astron. Astrophys. **641**, A6 (2020). [arXiv:1807.06209]

Key results summarized in Section 5.4 above.

### 6.2 H_0 Tension Current Status

**Planck (CMB, early universe):**
H_0 = 67.4 +/- 0.5 km/s/Mpc

**SH0ES (Cepheids + SNe Ia, local universe):**
H_0 = 73.04 +/- 1.04 km/s/Mpc (Riess et al. 2022)

**Citation:**
A. G. Riess et al., "A Comprehensive Measurement of the Local Value of the Hubble Constant with 1 km/s/Mpc Uncertainty from the Hubble Space Telescope and the SH0ES Team," Astrophys. J. Lett. **934**, L7 (2022). [arXiv:2112.04510]

**Tension:**
(73.04 - 67.36) / sqrt(1.04^2 + 0.54^2) = 5.7 / 1.17 = 4.9 sigma

**Other local measurements:**
- TRGB (Freedman et al. 2021): H_0 = 69.8 +/- 1.7 km/s/Mpc
- Strong lensing time delays (H0LiCOW): H_0 = 73.3 +/- 1.8 km/s/Mpc
- Megamasers (Pesce et al. 2020): H_0 = 73.9 +/- 3.0 km/s/Mpc

**Implications for BEC framework:**
If u_mech(a) reduces r_s by ~3-5%, H_0 can increase to ~72-73 km/s/Mpc.

### 6.3 S_8 Tension

**S_8 definition:**
S_8 = sigma_8 * sqrt(Omega_m / 0.3)

**Planck (CMB):**
S_8 = 0.832 +/- 0.013

**Weak lensing surveys:**
- KiDS-1000 (Heymans et al. 2021): S_8 = 0.759 +/- 0.024
- DES Y3 (Abbott et al. 2022): S_8 = 0.776 +/- 0.017
- HSC Y1 (Hikage et al. 2019): S_8 = 0.804 +/- 0.032

**Tension:**
(0.832 - 0.759) / sqrt(0.013^2 + 0.024^2) = 0.073 / 0.027 = 2.7 sigma

**Implications for BEC framework:**
- EDE typically increases S_8, worsening tension
- BEC healing length xi ~ 1 kpc suppresses small-scale power
- This could reduce sigma_8, potentially helping with S_8 tension
- Need detailed calculation of matter power spectrum suppression

### 6.4 DESI BAO Results

**Citation:**
DESI Collaboration (A. Adame et al.), "DESI 2024 VI: Cosmological Constraints from the Measurements of Baryon Acoustic Oscillations," arXiv:2404.03002 (2024).

**Key results:**
DESI Year 1 BAO measurements across redshift range 0.1 < z < 4.2.

Combined with CMB (Planck + ACT):
- H_0 = 68.52 +/- 0.62 km/s/Mpc (Lambda CDM)
- Omega_m = 0.295 +/- 0.015

**Evidence for evolving dark energy:**
DESI data prefer w0-wa model over cosmological constant at ~2.5 sigma:
- w_0 = -0.45 +/- 0.21
- w_a = -1.79 +/- 0.65

This suggests dark energy equation of state was less negative (closer to matter) in the past.

**Implications for BEC framework:**
- BAO data constrain r_s * H(z) / c and r_s / d_A(z)
- Modified expansion from u_mech affects these combinations
- DESI preference for evolving w may be consistent with residual effects of u_mech at late times

---

## 7. Bibliography (BibTeX Format for LaTeX)

```latex
\begin{thebibliography}{99}

% === CMB and Early Dark Energy ===

\bibitem{Poulin2019}
V.~Poulin, T.~L.~Smith, T.~Karwal, and M.~Kamionkowski,
``Early Dark Energy Can Resolve The Hubble Tension,''
\emph{Phys.\ Rev.\ Lett.}\ \textbf{123}, 231301 (2019).
[arXiv:1811.04083]

\bibitem{Hill2020}
J.~C.~Hill, E.~McDonough, M.~W.~Toomey, and S.~Alexander,
``Early dark energy does not restore cosmological concordance,''
\emph{Phys.\ Rev.\ D}\ \textbf{102}, 043507 (2020).
[arXiv:2003.07355]

\bibitem{Smith2020}
T.~L.~Smith, V.~Poulin, and M.~A.~Amin,
``Oscillating scalar fields and the Hubble tension: a resolution with novel signatures,''
\emph{Phys.\ Rev.\ D}\ \textbf{101}, 063523 (2020).
[arXiv:1908.06995]

\bibitem{Knox2020}
L.~Knox and M.~Millea,
``Hubble constant hunter's guide,''
\emph{Phys.\ Rev.\ D}\ \textbf{101}, 043533 (2020).
[arXiv:1908.03663]

\bibitem{Karwal2016}
T.~Karwal and M.~Kamionkowski,
``Dark energy at early times, the Hubble parameter, and the string axiverse,''
\emph{Phys.\ Rev.\ D}\ \textbf{94}, 103523 (2016).
[arXiv:1608.01309]

\bibitem{Agrawal2019}
P.~Agrawal, F.-Y.~Cyr-Racine, D.~Pinner, and L.~Randall,
``Rock 'n' Roll Solutions to the Hubble Tension,''
\emph{Phys.\ Dark Universe}\ \textbf{42}, 101347 (2019).
[arXiv:1904.01016]

% === Fuzzy Dark Matter ===

\bibitem{Hu2000}
W.~Hu, R.~Barkana, and A.~Gruzinov,
``Fuzzy cold dark matter: The wave properties of ultralight particles,''
\emph{Phys.\ Rev.\ Lett.}\ \textbf{85}, 1158--1161 (2000).
[arXiv:astro-ph/0003365]

\bibitem{Hlozek2015}
R.~Hlozek, D.~Grin, D.~J.~E.~Marsh, and P.~G.~Ferreira,
``A search for ultralight axions using precision cosmological data,''
\emph{Phys.\ Rev.\ D}\ \textbf{91}, 103512 (2015).
[arXiv:1410.2896]

\bibitem{Hlozek2018}
R.~Hlozek, D.~J.~E.~Marsh, and D.~Grin,
``Using the Full Power of the Cosmic Microwave Background to Probe Axion Dark Matter,''
\emph{Mon.\ Not.\ R.\ Astron.\ Soc.}\ \textbf{476}, 3063--3085 (2018).
[arXiv:1708.05681]

\bibitem{Marsh2016}
D.~J.~E.~Marsh,
``Axion Cosmology,''
\emph{Phys.\ Rep.}\ \textbf{643}, 1--79 (2016).
[arXiv:1510.07633]

\bibitem{Schive2014}
H.-Y.~Schive, T.~Chiueh, and T.~Broadhurst,
``Cosmic structure as the quantum interference of a coherent dark wave,''
\emph{Nature Phys.}\ \textbf{10}, 496--499 (2014).
[arXiv:1406.6586]

\bibitem{Hui2017}
L.~Hui, J.~P.~Ostriker, S.~Tremaine, and E.~Witten,
``Ultralight scalars as cosmological dark matter,''
\emph{Phys.\ Rev.\ D}\ \textbf{95}, 043541 (2017).
[arXiv:1610.08297]

% === CMB Physics ===

\bibitem{Planck2018}
Planck Collaboration (N.~Aghanim \emph{et al.}),
``Planck 2018 results. VI. Cosmological parameters,''
\emph{Astron.\ Astrophys.}\ \textbf{641}, A6 (2020).
[arXiv:1807.06209]

\bibitem{Planck2018Lensing}
Planck Collaboration (N.~Aghanim \emph{et al.}),
``Planck 2018 results. VIII. Gravitational lensing,''
\emph{Astron.\ Astrophys.}\ \textbf{641}, A8 (2020).
[arXiv:1807.06210]

\bibitem{Hu1997}
W.~Hu and M.~White,
``CMB anisotropies: Total angular momentum method,''
\emph{Phys.\ Rev.\ D}\ \textbf{56}, 596--615 (1997).
[arXiv:astro-ph/9702170]

\bibitem{Hu2002}
W.~Hu and S.~Dodelson,
``Cosmic Microwave Background Anisotropies,''
\emph{Ann.\ Rev.\ Astron.\ Astrophys.}\ \textbf{40}, 171--216 (2002).
[arXiv:astro-ph/0110414]

% === H_0 Tension ===

\bibitem{Riess2022}
A.~G.~Riess \emph{et al.},
``A Comprehensive Measurement of the Local Value of the Hubble Constant with 1 km/s/Mpc Uncertainty from the Hubble Space Telescope and the SH0ES Team,''
\emph{Astrophys.\ J.\ Lett.}\ \textbf{934}, L7 (2022).
[arXiv:2112.04510]

\bibitem{Freedman2021}
W.~L.~Freedman,
``Measurements of the Hubble Constant: Tensions in Perspective,''
\emph{Astrophys.\ J.}\ \textbf{919}, 16 (2021).
[arXiv:2106.15656]

\bibitem{Verde2019}
L.~Verde, T.~Treu, and A.~G.~Riess,
``Tensions between the Early and the Late Universe,''
\emph{Nature Astron.}\ \textbf{3}, 891--895 (2019).
[arXiv:1907.10625]

\bibitem{DiValentino2021}
E.~Di~Valentino \emph{et al.},
``In the realm of the Hubble tension -- a review of solutions,''
\emph{Class.\ Quant.\ Grav.}\ \textbf{38}, 153001 (2021).
[arXiv:2103.01183]

% === S_8 Tension ===

\bibitem{KiDS2021}
C.~Heymans \emph{et al.} (KiDS Collaboration),
``KiDS-1000 Cosmology: Multi-probe weak gravitational lensing and spectroscopic galaxy clustering constraints,''
\emph{Astron.\ Astrophys.}\ \textbf{646}, A140 (2021).
[arXiv:2007.15632]

\bibitem{DES2022}
T.~M.~C.~Abbott \emph{et al.} (DES Collaboration),
``Dark Energy Survey Year 3 results: Cosmological constraints from galaxy clustering and weak lensing,''
\emph{Phys.\ Rev.\ D}\ \textbf{105}, 023520 (2022).
[arXiv:2105.13549]

% === BAO ===

\bibitem{DESI2024}
DESI Collaboration (A.~Adame \emph{et al.}),
``DESI 2024 VI: Cosmological Constraints from the Measurements of Baryon Acoustic Oscillations,''
\emph{arXiv:2404.03002} (2024).

\bibitem{BOSS2017}
S.~Alam \emph{et al.} (BOSS Collaboration),
``The clustering of galaxies in the completed SDSS-III Baryon Oscillation Spectroscopic Survey: cosmological analysis of the DR12 galaxy sample,''
\emph{Mon.\ Not.\ R.\ Astron.\ Soc.}\ \textbf{470}, 2617--2652 (2017).
[arXiv:1607.03155]

% === Boltzmann Codes ===

\bibitem{CLASS}
D.~Blas, J.~Lesgourgues, and T.~Tram,
``The Cosmic Linear Anisotropy Solving System (CLASS) II: Approximation schemes,''
\emph{J.\ Cosmol.\ Astropart.\ Phys.}\ \textbf{07}, 034 (2011).
[arXiv:1104.2933]

\bibitem{CAMB}
A.~Lewis, A.~Challinor, and A.~Lasenby,
``Efficient computation of cosmic microwave background anisotropies in closed Friedmann-Robertson-Walker models,''
\emph{Astrophys.\ J.}\ \textbf{538}, 473--476 (2000).
[arXiv:astro-ph/9911177]

\bibitem{AxionCAMB}
D.~Grin, R.~Hlozek, D.~J.~E.~Marsh, and P.~G.~Ferreira,
``An Effective Fluid Description of Ultralight Axions,''
GitHub repository: https://github.com/dgrin1/axionCAMB

% === Textbooks and Reviews ===

\bibitem{Dodelson2020}
S.~Dodelson and F.~Schmidt,
\emph{Modern Cosmology}, 2nd ed.
(Academic Press, San Diego, 2020).

\bibitem{Mukhanov2005}
V.~Mukhanov,
\emph{Physical Foundations of Cosmology}
(Cambridge University Press, Cambridge, 2005).

\bibitem{Weinberg2008}
S.~Weinberg,
\emph{Cosmology}
(Oxford University Press, Oxford, 2008).

\end{thebibliography}
```

---

## 8. Summary and Key Points for Paper 4

### 8.1 Main Findings

1. **u_mech(a) is analogous to Early Dark Energy (EDE):** The transient component with Gaussian profile near a_c ~ 10^{-3} will have similar effects to EDE on CMB observables.

2. **Sound horizon reduction:** If u_mech contributes ~10% of energy density near recombination, r_s could be reduced by ~3-5%, potentially resolving the H_0 tension.

3. **S_8 tension risk:** Like EDE, u_mech may increase sigma_8, worsening the S_8 tension with weak lensing surveys. However, the BEC healing length suppression could compensate.

4. **Perturbation treatment needed:** The equation of state w_mech(a) differs from standard EDE. Need to determine:
   - Whether u_mech has perturbations (smooth vs. perturbed)
   - Sound speed c_s^2 (likely = c^2 in BEC limit)
   - Anisotropic stress (likely = 0)

5. **Boltzmann code implementation:** CLASS/CAMB need modification to include u_mech(a) with its specific w(a) and perturbation properties.

### 8.2 Critical Calculations Needed

1. **Numerical computation of Delta r_s / r_s** for representative values of (u_0, a_c, sigma)

2. **CMB TT, TE, EE power spectra** with u_mech included

3. **Matter power spectrum P(k)** with both u_mech and healing length suppression

4. **MCMC parameter estimation** constraining (f_mech, a_c, sigma) from Planck data

5. **Forecast for H_0 and S_8** in the BEC framework

### 8.3 Falsifiable Predictions

1. **Acoustic peak positions:** Slight shifts from Lambda CDM if r_s modified

2. **Damping tail:** Modified Silk damping from changed H(a)

3. **Small-scale power suppression:** From healing length xi ~ 1 kpc

4. **CMB lensing amplitude:** Reduced if sigma_8 is lower

5. **Specific correlation:** H_0 increase should correlate with particular f_mech, a_c values

---

## 9. Recommended Reading Path

For someone new to this topic:

1. **Start with CMB basics:**
   - Hu & Dodelson (2002) - CMB Anisotropies review
   - Dodelson & Schmidt (2020) - Modern Cosmology textbook, Ch. 8-9

2. **Understand the tensions:**
   - Di Valentino et al. (2021) - Comprehensive review of H_0 tension solutions
   - Verde, Treu & Riess (2019) - Nature Astronomy tensions review

3. **EDE as solution:**
   - Poulin et al. (2019) - Original EDE proposal
   - Hill et al. (2020) - EDE and S_8 tension (critical perspective)
   - Knox & Millea (2020) - Hubble constant hunter's guide

4. **Fuzzy dark matter:**
   - Hui et al. (2017) - Ultralight scalars review
   - Marsh (2016) - Axion cosmology comprehensive review
   - Hlozek et al. (2015, 2018) - CMB constraints

5. **For implementation:**
   - CLASS/CAMB documentation
   - AxiCLASS code from Poulin et al.

---

**Document compiled by:** physics-agent
**Date:** 2026-02-08
**For:** Paper 4: CMB Power Spectrum and Perturbations
**Framework:** BEC Condensate Cosmology
