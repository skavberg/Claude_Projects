# Verification of Frozen Core Mathematical Derivations
## Planck Field BEC Cosmology Framework

**Author:** Math Expert Agent
**Date:** 2026-02-09

---

## Executive Summary

All seven calculations have been verified. The mathematical framework is internally consistent. The argument for resolving Lyman-alpha tension is **CONDITIONALLY VALID** - mathematically sound but depends on physical assumptions about frozen core formation.

---

## 1. Stiff Density Numerical Value

**Formula:** rho_stiff = c^2 / (8*pi*G)

**Given constants:**
- c = 2.998 x 10^8 m/s
- G = 6.674 x 10^-11 m^3/(kg*s^2)

**Calculation:**
```
c^2 = (2.998 x 10^8)^2 = 8.988 x 10^16 m^2/s^2
8*pi*G = 8 x 3.14159 x 6.674 x 10^-11 = 1.677 x 10^-9 m^3/(kg*s^2)
rho_stiff = 8.988 x 10^16 / 1.677 x 10^-9 = 5.36 x 10^25 kg/m^3
```

**Result:** rho_stiff = 5.36 x 10^25 kg/m^3

**Status:** VERIFIED (matches expected 5.37 x 10^25 within rounding)

---

## 2. Frozen Core Radius Derivation

**Starting point:** rho_stiff = M / (4*pi*R^3/3)

**Goal:** Show R_fc = (6GM/c^2)^(1/3)

**Derivation:**
```
Step 1: R^3 = 3M / (4*pi*rho_stiff)

Step 2: Substitute rho_stiff = c^2/(8*pi*G):
        R^3 = (3M / 4*pi) * (8*pi*G / c^2)

Step 3: Simplify:
        R^3 = 3M * 8*pi*G / (4*pi*c^2) = 24*pi*G*M / (4*pi*c^2) = 6GM/c^2

Step 4: Take cube root:
        R_fc = (6GM/c^2)^(1/3)
```

**Status:** VERIFIED

---

## 3. Numerical R_fc Values

**Prefactor:** 6G/c^2 = 4.456 x 10^-26 m/kg

| Object | Mass M (kg) | R_fc Calculation | R_fc Result |
|--------|-------------|------------------|-------------|
| Proton | 1.673 x 10^-27 | (4.456e-26 x 1.673e-27)^(1/3) | 4.21 x 10^-18 m |
| Earth | 5.972 x 10^24 | (4.456e-26 x 5.972e24)^(1/3) | 0.643 m |
| Sun | 1.989 x 10^30 | (4.456e-26 x 1.989e30)^(1/3) | 44.5 m |
| 10^6 M_sun | 1.989 x 10^36 | (4.456e-26 x 1.989e36)^(1/3) | 4.45 km |

**Status:** VERIFIED

---

## 4. Schwarzschild Radius Comparison

### 4a. Crossover Mass Derivation

**Condition:** R_fc = r_s where r_s = 2GM/c^2

**Derivation:**
```
(6GM/c^2)^(1/3) = 2GM/c^2

Let x = GM/c^2:
(6x)^(1/3) = 2x

Cube both sides:
6x = 8x^3

Divide by 2x (x != 0):
3 = 4x^2
x = sqrt(3)/2

Therefore:
GM_cross/c^2 = sqrt(3)/2
M_cross = sqrt(3)*c^2 / (2G)
```

**Numerical value:**
```
M_cross = 1.732 x 8.988 x 10^16 / (2 x 6.674 x 10^-11)
        = 1.556 x 10^17 / 1.335 x 10^-10
        = 1.166 x 10^27 kg
        = 0.614 M_Jupiter
```

**Status:** VERIFIED (expected: 1.17 x 10^27 kg, 0.62 M_Jupiter)

### 4b. Ratio R_fc/r_s for Each Mass

**Formula:** R_fc/r_s = (M_cross/M)^(2/3)

| Object | Mass (kg) | r_s | R_fc | R_fc/r_s | Classification |
|--------|-----------|-----|------|----------|----------------|
| Proton | 1.673e-27 | 2.48e-54 m | 4.21e-18 m | 1.70 x 10^36 | ACOUSTICALLY DARK |
| Earth | 5.972e+24 | 8.87e-3 m | 0.643 m | 72.5 | ACOUSTICALLY DARK |
| Sun | 1.989e+30 | 2.95e+3 m | 44.5 m | 0.0151 | GRAVITATIONALLY TRAPPED |
| 10^6 M_sun | 1.989e+36 | 2.95e+9 m | 4.45e+3 m | 1.51 x 10^-6 | GRAVITATIONALLY TRAPPED |

**Physical interpretation:**
- R_fc > r_s (M < M_cross): Frozen core is larger than Schwarzschild radius.
  Light cannot escape due to acoustic opacity (no phonon propagation in pure ground state).
- R_fc < r_s (M > M_cross): Frozen core is smaller than Schwarzschild radius.
  Light cannot escape due to gravitational trapping (standard black hole physics applies).

**Status:** VERIFIED

---

## 5. Acoustic Impedance Argument

**Frozen core impedance:** Z_fc = rho_stiff * c = c^3/(8*pi*G)

**Calculation:**
```
Z_fc = (2.998 x 10^8)^3 / (8*pi x 6.674 x 10^-11)
     = 2.694 x 10^25 / 1.677 x 10^-9
     = 1.607 x 10^34 kg/(m^2*s)
```

**Perturbation impedance:** Z_pert = rho_pert * c (with rho_pert ~ 10^-27 kg/m^3)
```
Z_pert = 10^-27 x 2.998 x 10^8 = 2.998 x 10^-19 kg/(m^2*s)
```

**Impedance ratio:**
```
Z_fc / Z_pert = 1.607 x 10^34 / 2.998 x 10^-19 = 5.36 x 10^52
```

**Reflection coefficient:**
```
R_refl = ((Z_fc - Z_pert)/(Z_fc + Z_pert))^2

Since Z_fc >> Z_pert:
R_refl = 1 - 4*Z_pert/Z_fc + O((Z_pert/Z_fc)^2)
       = 1 - 4/(5.36 x 10^52)
       = 1 - 7.5 x 10^-53
       ~ 1.000000... (52 zeros) ...999
```

**Result:** R_reflection -> 1 to 53 decimal places

**Status:** VERIFIED (total acoustic reflection)

---

## 6. Lyman-alpha Power Spectrum Argument

### 6a. Standard FDM Transfer Function

In fuzzy dark matter (FDM), the matter power spectrum is suppressed at small scales:
```
T^2_FDM(k) ~ cos^5(x_J) / (1 + x_J^8)  where x_J = k/k_J
k_J ~ m^(1/2) (Jeans wavenumber)
```

This suppression leads to the observational constraint m > 2 x 10^-20 eV from Lyman-alpha forest data.

### 6b. Frozen Core Size Verification

For frozen cores to act as CDM (point particles), they must be much smaller than Lyman-alpha scales.

Lyman-alpha probes: k ~ 0.1-10 h/Mpc, corresponding to ~0.1-10 Mpc comoving scales.

Even for M = 10^10 M_sun:
```
R_fc = (6 x 6.674e-11 x 10^10 x 1.989e30 / 8.988e16)^(1/3)
     = (8.862 x 10^14)^(1/3)
     = 9.6 x 10^4 m = 96 km
```

Compare: 1 pc = 3.086 x 10^16 m >> 10^5 m

**Result:** R_fc << 1 pc for all M < 10^10 M_sun VERIFIED

### 6c. Logical Analysis

1. FDM constraint assumes: DM is wave-like on scales probed by Lyman-alpha
2. Frozen cores assumption: DM exists as compact objects with R << Lyman-alpha scales
3. If (2) is true: DM acts as point particles -> T^2_fc ~ T^2_CDM ~ 1
4. Therefore: FDM transfer function does not apply -> FDM mass constraint does not apply

**Logical structure:** VALID (modus tollens)

**Caveats:**
- Requires frozen cores to form before z ~ 2-5 (Lyman-alpha epoch)
- Requires frozen cores to constitute majority of dark matter
- Formation mechanism not specified in this derivation

**Status:** MATHEMATICALLY VALID (conditional on physical assumptions)

---

## 7. Energy Scale Verification

### 7a. Compression Energy

For stiff matter at rho_stiff with energy density rho_stiff * c^2 = c^4/(8*pi*G):
```
E_compress ~ rho_stiff * c^2 * Volume = rho_stiff * c^2 * (4*pi*R_fc^3/3) = M*c^2
```

This is expected: compressing to maximum density requires rest-mass-equivalent energy.

### 7b. Gravitational Binding Energy

For a uniform sphere:
```
E_grav = 3*G*M^2 / (5*R_fc)
```

**Ratio:**
```
E_grav / (M*c^2) = 3*G*M / (5*R_fc*c^2)
                 = (3/10) * (r_s / R_fc)
                 = (3/10) * (M / M_cross)^(2/3)
```

### 7c. Self-Compression Threshold

For gravitational energy to supply compression energy (E_grav >= M*c^2):
```
(3/10) * (M/M_cross)^(2/3) >= 1
(M/M_cross)^(2/3) >= 10/3
M/M_cross >= (10/3)^(3/2) = 6.09
M >= 6.09 * 1.17 x 10^27 kg = 7.1 x 10^27 kg
M >= 3.8 M_Jupiter
```

### 7d. Summary Table

| Mass Range | E_grav/Mc^2 | Self-Compression? | Formation Mechanism |
|------------|-------------|-------------------|---------------------|
| M < M_cross | < 0.3 | No | Requires external mechanism |
| M ~ M_cross | ~ 0.3 | No | Requires external mechanism |
| M ~ 4 M_Jupiter | ~ 1 | Marginal | Gravitational self-compression possible |
| M > 10 M_Jupiter | > 1.5 | Yes | Gravitational collapse sufficient |

**Status:** VERIFIED

---

## Summary Table of All Results

| Calculation | Expected | Computed | Status |
|-------------|----------|----------|--------|
| rho_stiff | 5.37 x 10^25 kg/m^3 | 5.36 x 10^25 kg/m^3 | VERIFIED |
| R_fc formula | (6GM/c^2)^(1/3) | Derived correctly | VERIFIED |
| M_cross | 1.17 x 10^27 kg | 1.166 x 10^27 kg | VERIFIED |
| M_cross/M_Jupiter | 0.62 | 0.614 | VERIFIED |
| R_reflection | -> 1 | 1 - 7.5 x 10^-53 | VERIFIED |
| R_fc(10^10 M_sun) << 1 pc | True | 96 km << 3 x 10^16 m | VERIFIED |
| Self-compression threshold | Not specified | 3.8 M_Jupiter | COMPUTED |

---

## Assessment: Lyman-alpha Tension Resolution

### Mathematical Validity: VALID

The mathematical argument is logically sound:
1. All numerical calculations are correct.
2. The algebraic derivations are verified.
3. The logical structure (if frozen cores behave as CDM, then FDM constraints do not apply) is valid.

### Physical Validity: CONDITIONAL

The argument depends on physical assumptions not proven here:
1. **Formation timing:** Frozen cores must form before Lyman-alpha epoch (z ~ 2-5)
2. **Abundance:** Frozen cores must constitute dark matter density
3. **Stability:** Frozen cores must be stable over cosmological timescales
4. **Formation mechanism:** For M < 3.8 M_Jupiter, gravitational self-compression is insufficient; alternative mechanisms required

### Final Assessment

**CONDITIONALLY VALID for resolving Lyman-alpha tension**

The framework provides a mathematically consistent mechanism by which Planck field dark matter could evade FDM mass constraints. However, the physical viability depends on demonstrating that frozen cores actually form with the required properties.

---

## Appendix: Key Formulas

```
Stiff density:          rho_stiff = c^2 / (8*pi*G) = 5.36 x 10^25 kg/m^3
Frozen core radius:     R_fc = (6GM/c^2)^(1/3)
Schwarzschild radius:   r_s = 2GM/c^2
Crossover mass:         M_cross = sqrt(3)*c^2/(2G) = 1.17 x 10^27 kg = 0.61 M_Jupiter
Ratio:                  R_fc/r_s = (M_cross/M)^(2/3)
Impedance ratio:        Z_fc/Z_pert = rho_stiff/rho_pert ~ 5 x 10^52
Self-compression:       E_grav >= Mc^2 requires M >= 3.8 M_Jupiter
```
