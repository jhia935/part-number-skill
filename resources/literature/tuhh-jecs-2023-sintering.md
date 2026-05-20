                                                         Journal of the European Ceramic Society 43 (2023) 4939–4949


                                                                   Contents lists available at ScienceDirect


                                                  Journal of the European Ceramic Society
                                                      journal homepage: www.elsevier.com/locate/jeurceramsoc


Original article

Efficient modelling of ceramic sintering processes: Application to bilayers
and membranes
Hao Shi a ,∗, Diletta Giuntini a,b , Hans van Dommelen a , Marc G.D. Geers a , Joris J.C. Remmers a
a
    Department of Mechanical Engineering, Eindhoven University of Technology, 5612 AZ, Eindhoven, The Netherlands
b
    Institute of Advanced Ceramics, Hamburg University of Technology, D-21073, Hamburg, Germany



ARTICLE                 INFO                               ABSTRACT

Keywords:                                                  The constitutive relation of Skorohod and Olevsky for viscous sintering is utilized to model the shrinkage
Continuum modelling                                        and relative density evolution during the sintering process of ceramics. A new implicit integration scheme
Solid state sintering                                      is presented and implemented. The computational cost is drastically reduced by combining this integration
Skorohod Olevsky Viscous Sintering (SOVS)
                                                           scheme with a solid-like shell element formulation, which also enables a faster and more accurate description
model
                                                           of shape distortions, especially for thin geometries. The characterization and identification of the material
Implicit integration
Bilayer ceramic
                                                           viscosity is also improved via the Aquilanti–Mundim deformed Arrhenius description. The model robustness is
FEM                                                        examined with a spectrum of benchmark tests: ZnO sintering experiments from previous studies, as well as new
Lanthanum tungstate                                        lanthanum tungstate sintering tests. The model predictions for both dimensional shrinkage and relative density
                                                           evolution are very accurate using the newly proposed material viscosity functions. The model improvements
                                                           offer the possibility to simulate long-time sintering processes with higher accuracy and significantly reduced
                                                           computational efforts.



1. Introduction                                                                                    Sintering can be modelled at different length scales with sev-
                                                                                               eral methods: the Finite Element Method (FEM) at the continuum
    Ceramics are ubiquitous in our lives, from tableware to advanced                           (macro)-scale [14,17–24], the Discrete Element Method (DEM) [25–
and functional ceramics deployed in batteries, electronics, catalytic                          31], the Phase-Field Method (PFM) [32–38] and the kinetic Monte
components, and thermal engines. A key step in the manufacturing of                            Carlo (kMC) [39–42] at the meso/particle scale, or the combination of
ceramics is solid-state sintering, upon which mass transfer mechanisms                         kMC/DEM and FEM in multiscale approaches [43]. DEM has the advan-
lead to reducing porosity in a compacted powder, resulting in the                              tage of being mesh-free and of simulating the motion and morphology
densification and shrinkage of the part [1]. Many issues can occur                             changes of each particle. However, this method typically assumes
during this process: non-uniform densification and micro-cracking [2–                          spherical particles and relies on a semi-empirical micro-mechanical
4]; lack of control of the final microstructure and associated me-                             model that needs micro-scale experiments for accurate parameter deter-
chanical properties [5–7]; shrinkage anisotropy and inhomogeneous                              mination. It is also computationally demanding, due to the small time
microstructures (particularly relevant with the advent of powder-based                         steps needed to resolve the contacts/collisions among particles, making
additive manufacturing (AM) processes [8–11]); distortions and crack-                          the modelling of realistic, long-duration sintering processes almost
ing in composites [12–14]. The latter becomes particularly relevant
                                                                                               unfeasible. The phase-field method relies on free energy minimization
in thin geometries, such as bi- and tri-layer membranes, which are
                                                                                               principles, and kinetic evolution equations. It is a good platform to
receiving increasing attention for catalytic applications, where the vari-
                                                                                               model material flow and grain morphology evolution, capturing phe-
ations of properties can be fine-tuned through their thickness [5,7,15].
                                                                                               nomena at the particle length scale, such as neck and grain growth. It
Understanding and controlling each material’s shrinkage behaviour
                                                                                               is, nevertheless, equally or sometimes even more computationally de-
and stress state during sintering is essential to tackle these problems.
                                                                                               manding than DEM, since it requires adaptive meshing at inter-particle
However, most sintering processes are designed based on costly and
                                                                                               contacts to fully resolve the concentration gradients during material
inefficient trial-and-error approaches. There is thus substantial interest
                                                                                               diffusion. The kinetic Monte Carlo simulations are computationally less
in the development of robust, reliable and efficient predictive modelling
frameworks for sintering processes [16].                                                       expensive and also capture microstructural features, but their reliability


     ∗ Corresponding author.
      E-mail addresses: h.shi1@tue.nl (H. Shi), d.giuntini@tue.nl (D. Giuntini), j.a.w.v.dommelen@tue.nl (H. van Dommelen), m.g.d.geers@tue.nl (M.G.D. Geers),
j.j.c.remmers@tue.nl (J.J.C. Remmers).

https://doi.org/10.1016/j.jeurceramsoc.2023.03.053
Received 13 January 2023; Received in revised form 16 March 2023; Accepted 26 March 2023
Available online 5 April 2023
0955-2219/© 2023 The Author(s). Published by Elsevier Ltd. This is an open access article under the CC BY license (http://creativecommons.org/licenses/by/4.0/).
H. Shi et al.                                                                                                  Journal of the European Ceramic Society 43 (2023) 4939–4949


strongly depends on the reconstruction of the initial 3D material                     Linear elasticity
microstructure, which is in most cases cumbersome to obtain. The finite
element method is, instead, particularly advantageous: it has a lower                    The stress state 𝝈 is connected to the elastic strain 𝜺𝑒 via Hooke’s
computational cost and relies on well-established continuum theories                  Law:
of sintering. It enables reliable simulations of arbitrarily complex-
shaped macro-scale components. This becomes particularly valuable                     𝝈 = 4 𝑪 ∶ 𝜺𝑒 = 𝜆tr(𝜺𝑒 )𝑰 + 2𝜇𝜺𝑒                                                 (3)
for additively manufactured and composite parts, and for multilayered                         4
membranes, which typically do not shrink isotropically.                               with 𝑪 - the fourth order stiffness tensor, and 𝜆, 𝜇 - the Lamé coeffi-
    Most continuum-based theories are phenomenological, and they                      cients.
model the shrinkage of a green body during sintering via inelastic
strains. A well-established theory is the Skorohod–Olevsky Viscous                    Linear viscous formulation of the SOVS model
Sintering (SOVS) model [19]. It is based on the concepts of generalized
viscous flow of porous bodies, and it is derived from a thermodynam-                     The original SOVS constitutive equation in its linear form
ical consistent continuum mechanics framework. A broad spectrum of                    reads [19]:
applications, extensions, and refinements of the SOVS model is avail-
                                                                                             [             ]
able in the literature [10,23,24,44,45], also proposing refined material              𝝈 = 2𝜂 𝜙 ̇𝜺′𝑖 + 𝜓 ̇𝑒𝑰 + 𝑃𝐿 𝑰                               (4)
viscosity functions [46], and incorporating micro-scale information
via kMC parameters or grain growth functions [47]. Most of these                      or in the inelastic (sintering) strain rate form:
works implement the SOVS equations into commercial FEM software,                               𝝈′   tr(𝝈) − 3𝑃𝐿
as nonlinear constitutive models and ODE subroutines [2,14,21,48,49].                 ̇𝜺𝑖 =       +             𝑰                                                     (5)
                                                                                              2𝜂𝜙      18𝜂𝜓
The software is however not publicly accessible, and the numerical
                                                                                      where 𝝈 is the Cauchy stress tensor, 𝝈 ′ the deviatoric stress tensor, ̇𝜺′𝑖
methods used to solve the governing equations are not always fully
disclosed. Open access and flexible model implementations are thus                    the deviatoric inelastic strain rate tensor, 𝑒̇ = tr( ̇𝜺𝑖 ) trace of inelastic
called for. To the best of the authors’ knowledge, there are only few                 strain rate tensor or volume shrinkage rate, 𝜂 the viscosity of the
attempts [47,50] to implement the SOVS theory in open and/or in-                      fully dense skeleton (powder) phase, 𝜙 the normalized shear viscosity,
house developed FEM codes, and to subsequently evaluate the influence                 𝜓 the normalized bulk viscosity, 𝑃𝐿 the (effective) volume sintering
of solution algorithms on the models’ accuracy and performance.                       stress1 [24,51].
    This work aims at developing a computationally efficient and ver-                     The main terms of Eqs. (4) and (5) depend on temperature and
satile, (able to handle arbitrary geometries and materials) modelling                 relative density as follows [39,42,52]:
platform that accurately predicts the evolution of powder compacts
during sintering towards their final geometries. The article is thus struc-           𝜙(𝜌) = 𝜌2                                                                       (6)
tured as follows: Section 2 gives a brief introduction to the SOVS model,
including a new method for the characterization of the viscosity of the                           2 𝜌3
                                                                                      𝜓(𝜌) =                                                                          (7)
powder material during sintering; the improved numerical integration                              3 1−𝜌
scheme and its implementation are discussed in Section 3, followed                                3𝛼 2
by an introduction to solid-like shell elements (Section 4); results are              𝑃𝐿 (𝜌) =       𝜌                                                                (8)
                                                                                                  𝑟𝑝
discussed in Section 5, followed by conclusions and outlook (Section 6).
                                                                                      where 𝜌 is the relative density (equivalent to solid volume fraction), the
2. SOVS model formulation                                                             ratio between bulk and skeleton densities 𝜌𝑏 ∕𝜌𝑠𝑘𝑒𝑙𝑒𝑡𝑜𝑛 , reaches 1 for the
                                                                                      fully sintered body; 𝜌𝑏 is the bulk density, the ratio between the solid
    The Skorohod–Olevsky viscous sintering (SOVS) model is a con-                     mass and the total volume of geometry including the internal voids
tinuum mechanics-based modelling framework capturing the stress,                      𝑀𝑠 ∕𝑉𝑡 . The normalized bulk and shear viscosities are functions of the
strain and density evolution of a powder based material undergoing                    porosity and are derived using the hydrodynamic analogy to the theory
sintering, given that the constitutive behaviour of the powder material               of elasticity. The sintering stress 𝑃𝐿 is defined as directly proportional
is specified. It is a phenomenological model whereby a porous medium                  to the material’s surface tension, 𝛼, and inversely proportional to the
is considered as a two-phase material that includes a porous body                     powder particle radius, 𝑟𝑝 , and it is thus a local function or surface
skeleton phase and a void phase. The skeleton is assumed to consist of
                                                                                      tension acting at the single pore’s interface, while it also has a relative
individual particles having a general nonlinear viscous incompressible
                                                                                      density dependency to account for the macroscopic averaged effects of
behaviour, and the voids are homogeneously distributed within the
                                                                                      all the pores in the considered domain [19,24].
medium. As a consequence, the overall response is isotropic. We focus
on the free (pressureless) sintering of μm-sized powders of functional
oxides that are relevant for membrane and multilayered components                     Evolution of the relative density
(0.2 μm ZnO and 1.1 μm LaWO54 ). For this case, a linear viscous
description for the constitutive behaviour of the powder is appropriate,                The volume shrinkage rate is connected to the relative density
since the non-linear viscous behaviour only becomes dominant for                      employing the following continuity equation:
pressure-assisted sintering and/or when the particle size is in the nm
range [19,23,24].                                                                     𝜌̇ = −𝜌𝑒̇                                                                       (9)

Strain decomposition                                                                  Material viscosity dependency on temperature — quadratic function

   The material behaviour is described by a standard decomposition of
                                                                                         Olevsky et al. [42] proposed to describe the material viscosity
the total strain field 𝜺 into its elastic component 𝜺𝑒 and inelastic/viscous
component 𝜺𝑖 :                                                                        dependency on temperature with a quadratic equation as given in

𝜺 = 𝜺𝑒 + 𝜺𝑖                                                             (1)
                                                                                         1
with its equivalent rate form:                                                             Note that the sintering stress is defined as the hydrostatic (compressive)
                                                                                      stress which can stop the shrinkage when it is imposed in the opposite
̇𝜺 = ̇𝜺𝑒 + ̇𝜺𝑖                                                          (2)           direction, and thus represents the internal driving force magnitude (𝑃𝐿 ≥ 0).


                                                                               4940
H. Shi et al.                                                                                                 Journal of the European Ceramic Society 43 (2023) 4939–4949


Eq. (10).                                                                                 As with any 3D constitutive model intended for use with finite
          𝑇       𝑇                                                                   element codes, an accurate, robust, and efficient numerical routine is
𝜂(𝑇 ) = 𝑎( )2 + 𝑏    +𝑐                                                (10)           needed. For the current SOVS sintering model, Eq. (5) reveals that the
          𝑇0      𝑇0
                                                                                      direction and magnitude of inelastic strain depend directly on the stress
with 𝑇0 - the initial/starting ambient temperature of the sintering
                                                                                      state. Thus, conventional routines as used in visco-plasticity models
process; 𝑎, 𝑏 and 𝑐 are coefficients of the temperature function. To
                                                                                      cannot be directly utilized. Here, we implement the SOVS model using
determine the coefficients of a specific material, i.e. ZnO powder, the
                                                                                      a fully implicit Euler time integration scheme with variable reductions
procedure involves multiple cyclic loading sintering experiments.
                                                                                      to explore predictability and computational efficiency.

Material viscosity dependency on temperature - Arrhenius functions                    Implicit scheme for time integration

    Although the material viscosity function expressed as in Eq. (10)                     From Eqs. (2), (5), (9) we have three unknown state variables, 𝜺𝑒 ,
can capture well the viscosity evolution in certain temperature ranges                𝜺𝑖 and 𝜌, which needed to be solved for in both space and time.2 The
during sintering, it is in general not fully representative of the physics            evolution of these state variables is governed by a system of ODEs. It
underlying the sintering process, i.e. its thermal activation. This poly-             can be expressed in a general form:
nomial approximation is empirically based on the measured viscosity
during solid state sintering of ZnO powder, but it is not immediately                 𝑋̇ =  (𝑋, 𝜉)                                                   (13)
                                                                                      ̃        ̃
generalizable to the more complex material behaviour occurring during
                                                                                      where 𝑋 is the column of unknown variables, decomposed as following:
sintering, e.g., liquid phase formation, phase transformations, etc. The                      ̃
adopted Arrhenius-type description is, instead, capturing the thermal
activation aspects, and it is of more general applicability, also in terms                ⎡𝜺𝑒 ⎤
of sintering temperature ranges.                                                      𝑋 = ⎢ 𝜺𝑖 ⎥                                                                   (14)
                                                                                      ̃   ⎢ ⎥
    Reiterer et al. [46] proposed to describe the material viscosity’s                    ⎣𝜌⎦
dependency on temperature through a classical Arrhenius-type func-                    𝜉 in Eq. (13) is a placeholder for the external state variables that vary
tion, and it has been used for modelling the bilayer sintering of cerium              independently of the SOVS model, e.g., the temperature 𝑇 . 𝜺𝑒 and 𝜺𝑖
gadolinium oxide (CGO) powder [21]. Torresani et al. [11] recently                    are elastic and inelastic strain tensors, but for the implementation we
proposed a simpler method for determining the material viscosity,                     use Voigt notation and result in two sub-columns with length 6.
using the shrinkage data from mechanical dilatometry combined with
a quadratic Arrhenius function. Here, we propose to use the Aquilanti–                Backward Euler integration scheme
Mundim deformed Arrhenius function [52], which is flexible and ver-
satile in describing the temperature dependency over a wide range.                       In one timestep, 𝛥𝑡 = 𝑡𝑛+1 − 𝑡𝑛 :
    Assuming the material’s shrinkage is isotropic during free sintering,
the trace of inelastic strain rate tensor 𝑒̇ can be directly calculated from          𝑋 𝑛+1 = 𝑋 𝑛 + 𝛥𝑡 (𝑋 𝑛+1 , 𝜉 𝑛+1 )                                           (15)
                                                                                      ̃       ̃          ̃
the displacement field and time span measured via dilatometry. The                    Then the corresponding residual is:
material viscosity can then be estimated by combining Eqs. (5), (7) and
(8):                                                                                  (𝛥𝑋) = 𝛥𝑋 − 𝛥𝑡 (𝑋 + 𝛥𝑋, 𝜉 + 𝛥𝜉)                                            (16)
                                                                                          ̃    ̃        ̃    ̃
     1 1−𝜌 𝛼                                                                          with
𝜂=                                                                     (11)
     4 𝜌 𝑟𝑝 𝑒̇
                                                                                           ⎡𝛥𝜺𝑒 ⎤
     Once the material viscosity is calculated from the dilatometry                   𝛥𝑋 = ⎢ 𝛥𝜺𝑖 ⎥
                                                                                       ̃   ⎢ ⎥
shrinkage data using Eq. (11), the temperature data from the same                          ⎣ 𝛥𝜌 ⎦
experiment can also be exploited to reveal the relationship of 𝜂(𝑇 ),
                                                                                      and
which is still in the form of discrete data points. For the sake of
convenience, we use the reciprocal of the normalized temperature                               ⎡𝒇 𝜺𝑒 ⎤
𝑇 ∗ , which is defined as 1∕𝑇 ∗ = 1∕𝑇 − 1∕𝑇𝑇 , with 𝑇𝑇 defined as                      (𝛥𝑋) = ⎢ 𝒇 𝜺𝑖 ⎥
                                                                                          ̃    ⎢ ⎥
transition/characteristic temperature at which the sintering starts and                        ⎣ 𝑓𝜌 ⎦
the material viscosity drops drastically. Then, the deformed Arrhenius                    This set of residual equations, Eq. (16), is solved using the Newton–
function is finally used to describe the material viscosity dependency                Raphson procedure. To apply the Newton–Raphson procedure on this
on temperature [52] using these discrete experimental data points                     set of equations, the 13 unknowns in 𝑋 have to be solved in an iterative
(replacing the relationship shown in Eq. (10)):                                                                               ̃
                                                                                      manner, which requires a computationally costly inversion of a 13 × 13
                    ( −𝛾 )    [      𝛾 ]𝑑
                                           1                                          Jacobian matrix in each iterative solve step (the Newton–Raphson
𝜂(𝑇 ∗ ) = 𝜂0 exp𝑑        = 𝜂0 1 − 𝑑                                 (12)              iteration steps within one single timestep). In addition, this iterative
                   𝑅𝑇 ∗             𝑅𝑇 ∗
                                                                                      solution routine has to be performed on each material/integration point
Here, the coefficient 𝑅 is the universal gas constant, 𝜂0 and 𝛾 (same
                                                                                      within every element of the mesh to obtain a correct stress response.
units as 𝑅𝑇 ∗ ) are material-dependent constants, and 𝑑 is the deformed
                                                                                      Accordingly, the computational cost grows rapidly when one has to
parameter. Note that in the limit of 𝑑 → 0, 𝛾 → 𝐸𝑎 (activation energy),
                                                                                      deploy a finer mesh to resolve the geometry in more detail. Therefore,
the standard Arrhenius function is recovered.
                                                                                      we propose to first eliminate the relative density (1 unknown 𝛥𝜌) from
                                                                                      the solution routine via explicit calculations. Next, the inelastic strain is
3. Numerical integration scheme and implementation                                    reduced from 6 unknowns to 1 unknown by assuming isotropic shrink-
                                                                                      age behaviour. This assumption is also valid for complex geometry or
    In current study, an in-house FEM code/software, namely ‘‘DAWN’’                  loading conditions made of the same isotropic material. Finally, the
is used. This is a C++ finite element code that comprises a variety of                remaining 7 unknowns (6 components from the elastic strain 𝛥𝜺𝒆 and
element formulations, materials and solver techniques, most of which
are not available in commercial or open-source codes. The methods
proposed here are nevertheless general and can be applied to any FEM                    2
                                                                                          The elastic and inelastic strain are tensors, each has 6 independent scalar
software, both commercial and open source.                                            values, thus 13 scalar unknown values in total.


                                                                               4941
H. Shi et al.                                                                                                                Journal of the European Ceramic Society 43 (2023) 4939–4949


                                                                                                     alternative numerical integration methods. In Section 5.2, the perfor-
                                                                                                     mance and accuracy of the numerical model is assessed by comparing
                                                                                                     the numerical results obtained with the two element types with exper-
                                                                                                     imental data on a bilayer bar. In Section 5.3, the model’s accuracy in
                                                                                                     predicting the differential shrinkage-induced bending behaviour of lay-
                                                                                                     ered materials is validated by comparing the numerical outcomes with
                                                                                                     experimental data from the literature on the sintering of bilayer discs,
                                                                                                     with quadratic viscosity function given by Eq. (10). Finally, in Sec-
                                                                                                     tion 5.4, the broad applicability of the model is assessed by extending
                                                                                                     it to another functional ceramic material (lanthanum tungstate) with
                                                                                                     the Aquilanti–Mundim deformed Arrhenius viscosity function given by
                                                                                                     Eq. (12) in Section 2. The model predictions are quantitatively verified
                                                                                                     with a simple sintering experiment that covers the entire heating,
Fig. 1. Geometry of the eight nodes solid-like shell element [56,57]. Each geometrical
                                                                                                     holding and cooling stages.
node 𝑖 contains three degrees of freedom: [𝑢𝑥 , 𝑢𝑦 , 𝑢𝑧 ]𝑖 and each internal node 𝑗 has one
degree of freedom 𝑤𝑗 .
                                                                                                     5.1. Verification of model implementation with analytical solutions

                                                                                                         Inspired by the SOVS model verification published in [47], a simple
1 inelastic strain 𝛥𝑒) is further reduced to a single unknown 𝛥𝑒, using
                                                                                                     test case with two identical solid elements (8-nodes Hexahedron) is
the linearity between stress 𝝈 ′ and strain deviators 𝜺′𝑖 . The derivations
                                                                                                     used for the first verification step, as given in Fig. 2. The material here
are explained in detail in Appendix. After the determination of the
                                                                                                     is a powder compact of 0.2 μm ZnO particles, in line with Olevsky
change of inelastic strain, the change of elastic strain can be calculated
                                                                                                     et al. [39,42] and Argüello et al. [47]. The material and sintering
from the change of total strain, and the material’s stress state can be
                                                                                                     bilayer disc parameters are 𝐸 = 123.7 GPa, 𝜈 = 0.356, 𝛼 = 1.27 J/m2 ,
determined.
                                                                                                     𝑟𝑝 = 0.2 μm. The starting and ending temperatures of the sintering
                                                                                                     process are 𝑇0 = 750 ◦ C and 𝑇𝑒𝑛𝑑 = 1000 ◦ C. The heating ramp is
4. Solid-like shell element
                                                                                                     5 ◦ C/min. For this case study, the viscosity is expressed according to
                                                                                                     the quadratic form proposed by Olevsky et al. as given in Eq. (10), with
    Advanced ceramic manufacturing processes nowadays incorporate                                    𝑎 = 51.7 × 1010 Pa⋅s, 𝑏 = −106.6 × 1010 Pa⋅s, and 𝑐 = 56.4 × 1010 Pa⋅s [42].
complex structures and geometries, such as composite materials, mul-                                 The initial relative density is 𝜌0 = 47%. The left bottom node is fully
tilayered materials, 3D-printed complex shapes, thin layered catalytic                               constrained and the two elements are subjected to symmetry boundary
ceramic membranes, etc., requiring a suitable element for the finite                                 conditions along their x-z and y-z planes. Two loading cases are studied
element modelling of their sintering behaviour. Conventional linear                                  here: free sintering with no externally applied stress and sintering with
solid (Small Strain Continuum — SSC) elements, e.g., eight nodes                                     5 MPa tensile stress applied on the top surface (𝑧-direction).
hexahedral element, show an overly stiff behaviour when used in thin                                     For the free sintering case, the externally applied stress field is zero,
domains applications (Poisson thickness locking [53]) due to a constant                              thus Eq. (4) is simply expanded and results in the following governing
strain distribution in the thickness direction. An alternative is the                                equation of relative density evolution:
Solid-Like Shell (SLS) element [54,55], for which an additional set of
                                                                                                            3𝑃𝐿0 (1 − 𝜌)
internal degrees of freedom is used to add a quadratic term to the                                   𝜌̇ =                                                                         (17)
displacement field in the thickness direction, the internal ‘stretch’ of                                      4𝜂(𝑇 )
the element, as shown in Fig. 1. Three translational degrees of freedom                              with 𝑃𝐿0 = 3𝛼𝜌20 ∕𝑟𝑝 and 𝜂(𝑇 ) given by Eq. (10).
are defined at each node as for typical solid elements, and four internal                                The closed form solution of Eq. (17), i.e. relative density evolution,
degrees of freedom are established at the through-thickness edges of                                 is then given as reported in [47],
the element to account for the internal stretching, which yields a fully                                                     {         [            (            )]}
                                                                                                                (1 − 𝜌0 )        3        2      −1   2𝐶0 𝑡 + 𝐵0
three-dimensional bending strain field.                                                              𝜌(𝑡) = 1 −           exp − 𝑃𝐿0 √         tan       √
                                                                                                                   𝐹             4        𝑄0               𝑄0
    The corresponding strain field varies linearly over the thickness                                           {          [            (      )]}
instead of being constant, and Poisson thickness locking is avoided.                                                3         2           𝐵
Additionally, the SLS element is a true 3D solid element that allows for                               𝐹 = exp − 𝑃𝐿0 √            tan−1 √ 0
                                                                                                                    4         𝑄0            𝑄0
a 3D constitutive relation, which is typically not possible for the other
2D or pseudo-3D shell element formulations. It has been shown that the                               𝑄0 = 4𝐴0 𝐶0 − 𝐵02                                                            (18)
solid-like shell element can be used for modelling laminate structures                               𝐴0 = 𝑎 + 𝑏 + 𝑐
by either stacking multiple elements or by modelling multiple layers                                         10      5
                                                                                                     𝐵0 = 𝑎      +𝑏
within one element [56–58]. In the latter situation, the element is                                         60𝑇0    60𝑇0
divided into several sub-domains, each of which has different material                                        25
                                                                                                     𝐶0 = 𝑎
parameters. Both conventional volume elements and solid-like shell                                          3600𝑇02
elements are here used with the SOVS material model, to explore
                                                                                                     with the values of 𝑎, 𝑏, 𝑐 and 𝑇0 as specified above.
the feasibility, performance and efficiency of the sintering modelling
                                                                                                        For the sintering case with applied stress, a tensile stress is applied
framework.
                                                                                                     along the 𝑧-direction (𝜎𝑧𝑧 = 5 MPa, 𝜎𝑥𝑥 = 𝜎𝑦𝑦 = 0), and the continuity
                                                                                                     equation of the relative density evolution is given by
5. Results and discussion
                                                                                                             𝜎𝑧𝑧 1 − 𝜌 3𝑃𝐿0 (1 − 𝜌)
                                                                                                     𝜌̇ =             −                                                           (19)
    The SOVS sintering model described in the previous Sections Sec-                                        4𝜂(𝑇 ) 𝜌2    4𝜂(𝑇 )
tion 2 & 3 with both original and reduced integration schemes is                                     The solution for Eq. (19) is found with an explicit Runge–Kutta (RK45)
implemented into our in-house FEM software ‘‘DAWN’’. In Section 5.1,                                 method, with error control of the fourth-order method, and steps using
the accuracy of the model implementation is verified with a test case on                             the fifth-order accurate formula (local extrapolation is done). The time
two elements, by comparing the numerical results with a closed-form                                  step 𝛥𝑡 is chosen as 6 s, which is sufficiently small to give accurate
analytical solution as well as a semi-analytical solution obtained via                               integration results. The relative density evolution of the ZnO powder

                                                                                              4942
H. Shi et al.                                                                                                              Journal of the European Ceramic Society 43 (2023) 4939–4949




Fig. 2. Model verification by comparison of a two-element domain sintering shrinkage prediction with the analytical solution. Left: Geometry of the two-element domain. Right:
Relative density evolution during sintering of ZnO with different loading conditions (free sintering and sintering with 5 MPa tensile stress). Lines are analytical solutions and points
are simulation outputs. A time step 𝛥𝑡 = 30 s corresponds to a temperature step 𝛥𝑇 = 2.5 ◦ C (with heating rate 5 ◦ C/min).


compact during sintering is shown in Fig. 2. An excellent agreement                                   Table 1
                                                                                                      Sintering of ZnO bilayer bar: Garino’s experimental data [59] vs.
between analytical, semi-analytical and the numerical solution is found,
                                                                                                      simulation outcomes obtained using solid-like shell (SLS) elements.
confirming the accuracy of the simplified implicit integration scheme.
                                                                                                        Dimensions            Exp.                 Sim.                  Error
If the time step is reduced from 𝛥𝑡 = 30 s to 6 s, the difference between                               [mm]                  @ 1000 ◦ C           @ 1000 ◦ C            [%]
simulation and analytical solution is negligible. Unless otherwise spec-
                                                                                                        L                     6.70                 6.67                  0.4
ified, the time step 𝛥𝑡 = 30 s will be used for the following analyses,                                 W                     3.89                 3.73                  3.3
as the error is small and the computational cost reduces by a factor of                                 H                     2.15                 2.06                  3.6
5. For the case of sintering with an applied tensile stress, as expected,
the shrinkage is slower than in the free sintering case, due to the tensile
stress acting in the opposite direction of the (effective) volume sintering
                                                                                                SSC elements (bottom right) have same meshes with 928 8-node hex-
stress.
                                                                                                ahedrons. The final bilayer bar curvature obtained with SLS elements
                                                                                                agrees well with the experimental outcome: the upper layer has a lower
5.2. Benchmark test: model performance using solid and shell elements
                                                                                                initial relative density, which leads to faster shrinkage compared to
                                                                                                the bottom layer, resulting in the final upward bending. The results
    The previous section proves the fidelity of the model implemen-
                                                                                                obtained with SSC elements, instead, show almost no bending, due to
tation at the element (integration points) level. To test the model
                                                                                                the locking of the linear elements, even with a relatively fine mesh.
validity in real-scale sintering processes and the performance of the
                                                                                                The simulated final relative density is also different in the two cases.
implementation with shell elements, a larger scale and more complex
                                                                                                A clear relative density gradient is observed in the SLS case, along
study domain is used. A relevant test case that was also studied in
                                                                                                the thickness (z) direction, with increasing relative density towards
previous works [42,47,59], is the sintering of a bilayer bar [59]. The
                                                                                                the concave (upper) surface. This gradient is not observed in the SSC
same material as in Section 5.1 is considered (ZnO), but this time
                                                                                                case, and the final relative densities remain uniformly distributed in
in two layers with different initial relative densities, which leads to
                                                                                                each layer. Even though the reference literature study does not report
differential shrinkage rates. The bilayer bar consists of two rectangular
                                                                                                the final relative densities of each layer, the experimentally measured
blocks with initial length 𝐿 = 8.049 mm; width 𝑊 = 3.89 mm and
                                                                                                dimensions after sintering can be used for further validation [47,50,59].
equal thickness of upper and lower layer 𝐻𝑢 = 𝐻𝑙 = 1.316 mm (taken
                                                                                                The results are summarized in Table 1. A very good agreement between
from [59]), as given in Fig. 3. The upper and lower layer have initial
relative densities of 47% and 57%, respectively. The sintering process                          experiments and simulations is obtained, with an error range between
parameters (heating rate, temperature range, etc.) are identical to those                       0.4 and 3.4%, which is comparable with the error range (0.1 to 4.0%)
in the case of the two-element model of Section 5.1. Note that the                              obtained in previous studies [47,59].
geometry in Fig. 3 only represents a quarter of the original geometry                               To obtain such accurate results, however, a fine mesh with 46080
and symmetry boundary conditions are applied at the x-z and y-z                                 solid elements was previously needed for the same bilayer bar sim-
planes.                                                                                         ulation, with a resulting computational cost (CPU time) in the order
    To compare the computational cost for the different element types                           of 105 seconds [47]. This is more than a day of simulation time, thus
(solid element versus solid-like shell element), the bilayer bar test-case                      much longer than the 50-min sintering process time. In this work, the
shown here is simulated using both element types. The SLS element                               simulations are performed with 928 SLS elements and the improved
has 8 nodes on the element boundaries and 4 additional internal nodes                           time integration scheme. The computational cost is reduced by 3 orders
along the thickness direction to model the stretching (Fig. 1), and it                          of magnitude, resulting in a CPU time of 43.49 s, without sacrificing
is thus much more suitable to simulate bending problems, as required                            accuracy. Moreover, the memory needed for the sintering simulations
here.                                                                                           is also drastically reduced, since the number of elements is decreased
    The results of numerical simulations with SLS and SSC elements                              by a factor of approx. 50. This opens the pathway towards simulating
are compared with experimental data from the literature [42,59], as                             long holding-time sintering processes without the demand of large
shown in Fig. 3. Both simulations using SLS elements (bottom left) and                          computational infrastructures.

                                                                                         4943
H. Shi et al.                                                                                                            Journal of the European Ceramic Society 43 (2023) 4939–4949




Fig. 3. Sintering of a ZnO bilayer. Top left: sintering experiment of bilayer bar ZnO at 1000 ◦ C [42]. Top right: initial geometry and relative density of the bilayer bar: 𝜌𝑢 = 47%
and 𝜌𝑙 = 57%. Bottom: deformed configurations using Solid-Like Shell/SLS (left) and solid/SSC (right) elements.
Source: Reproduced with permission from John Wiley and Sons.


5.3. Prediction of differential shrinkage: Sintering of bilayered ZnO discs                          Table 2
                                                                                                     Sintering of ZnO bilayer disc: Garino’s experimental data [59] vs.
                                                                                                     simulation outcomes obtained using solid-like shell (SLS) elements.
    The bilayer bar investigated in the previous section has an aspect
                                                                                                      Dimensions            Exp.                 Sim.                 Error
ratio (length/thickness) of around 3 and the differential shrinkage-                                  [mm]                  @ 925 ◦ C            @ 925 ◦ C            [%]
induced bending behaviour is not fully representative of many appli-
                                                                                                      RT                    7.62                 7.33                 3.0
cations. In line with [47], to better evaluate the bending behaviour of                               RB                    7.83                 7.75                 0.9
such bilayered components, thin geometries with higher aspect ratios                                  HE                    1.63                 1.59                 2.1
are more appropriate, such as the ZnO bilayer disc sintering experiment                               HC                    2.72                 2.57                 7.6
by Garino [47,59]. Fig. 4 shows this case study, with a bilayered disc
with an aspect ratio of around 9. The disc consists of two layers with
an initial radius 𝑅 = 9.525 mm and equal thickness of the upper and
                                                                                               in Table 2. The bilayer disc simulations capture the shrinkage very
lower layer, 𝐻𝑢 = 𝐻𝑙 = 1 mm. The upper and lower layers have initial
                                                                                               accurately in both radial and thickness directions, with an error ranging
relative densities of 47% and 57%, respectively. The sintering process
                                                                                               from 0.9 to 3%. The prediction of disc bending is less accurate (7.6%
parameters (heating rate, temperature range, etc.) are identical to those
                                                                                               error) but still much smaller than the 13.7% error obtained in previous
of the bilayer bar case in the previous subsection. Similarly, symmetry
                                                                                               studies that using solid elements [47,59]. The final dimensions of radii
boundary conditions are applied, using 1536 SLS elements to reduce                             (𝑅𝑇 and 𝑅𝐵 ) and edge thickness 𝐻𝐸 are somewhat smaller than those
the computational cost. The simulation results relative to 925 ◦ C are                         obtained experimentally in Garino’s experiments, indicating a small
shown in Fig. 4, revealing the displacement in the z direction (dZ) and                        over-prediction of the overall shrinkage. Although the error for the
the relative density. The displacement dZ increases along the radial                           centre thickness (𝐻𝐶 ) is smaller than in previous studies, the overall
direction, with a minimum of −0.38 mm at the centre of the disc,                               bending behaviour is still underestimated. A potential reason for this
and reaching a maximum of 1 mm at the bottom edge. As expected,                                underestimation is the viscosity function for ZnO (and in [47,50]),
a more prominent bending is observed here compared to the bilayer                              which is taken from [42] directly, and which might underestimate the
bar case. As for the relative density field, a similar increasing gradient                     experimental viscosity of ZnO. Another possible cause could be the
along the z direction is also observed, with density values lower in                           inaccurate initial relative density of each layer before sintering, which
each layer compared to the bilayer bar. However, a relative density                            could easily lead to the mismatches observed here.
gradient is now also observed along the radial direction. The relative
density increases slightly from the centre to the edge of the quarter disc.                    5.4. Predicting the shrinkage of LWO powder compacts with a new viscosity
This small gradient along the radial direction is expected to be caused                        characterization method
by the stress state: higher tensile stress at the bottom centre surface
due to upward bending, thus hindering the shrinkage and leading to                                For a thorough verification of the new viscosity characterization
a lower final relative density. This agrees well with the lower final                          approach proposed in Section 2 and its versatility, we have conducted
relative density obtained from the previous element test under 5 MPa                           a new set of sintering experiments, focused on accurate measurements
tensile load. To quantify the overall sintering shrinkage, we monitor                          of both shrinkage and relative density changes during the process.
four characteristic geometrical parameters, defined in the bottom right                        The material is another functional oxide powder: lanthanum tungstate
of Fig. 4: centre thickness 𝐻𝐶 (bending), bottom radius 𝑅𝐵 (radial                             (LaWO54 ), which is currently particularly relevant for catalytic mem-
shrinkage of lower layer), top radius 𝑅𝑇 (radial shrinkage of the upper                        branes.
layer) and edge thickness 𝐻𝐸 (shrinkage in the thickness direction).                              Lanthanum tungstate powder (LaWO54 ) is first uni-axially com-
    These dimensions are extracted from the simulation outcomes at                             pressed (40 kPa) into cylindrical pellets and then hydro-statically com-
925 ◦ C and compared with the experimental values, as summarized                               pressed (400 MPa) to induce isotropic compaction. The resulting pellet

                                                                                        4944
H. Shi et al.                                                                                                            Journal of the European Ceramic Society 43 (2023) 4939–4949




Fig. 4. Modelled shrinkage and bending of bilayered ZnO disc during sintering. Top left: initial (quarter) geometry bilayer of the simulation domain, with relative densities in the
two layers 𝜌𝑢 = 47% and 𝜌𝑙 = 57%. Top right: Displacement field in the 𝑧-direction at 925 ◦ C. Bottom left: Relative density distribution at 925 ◦ C. Bottom right: Final geometry
after bending, with centre thickness 𝐻𝐶 , bottom radius 𝑅𝐵 , top Radius 𝑅𝑇 and edge thickness 𝐻𝐸 [59].




          Fig. 5. Left: LaWO54 pellet before and after sintering. Right: Densification/shrinkage of LaWO54 pellet vs. sintering temperature, as measured by dilatometry.


has an initial relative density of 59.7%, as shown in Fig. 5. The LaWO54
powder has median particle size 𝑟𝑝 = 1 μm, theoretical density 𝜌𝑠 =
6.64 g/cm3 , surface tension 𝛼 = 1 J/m2 , Young’s modulus 𝐸 = 130
GPa and Poisson’s ratio 𝜈 = 0.24. The sintering process is conducted
with a mechanical dilatometer (Netzsch - DIL402C) and consists of the
following stages: (i) heating stage, 𝑇0 = 25 ◦ C to 𝑇 = 1500 ◦ C at
2 ◦ C/min; (ii) holding stage, 𝑇 = 1500 ◦ C for 720 mins; (iii) cooling
stage, 𝑇𝑒𝑛𝑑 = 𝑇0 = 25 ◦ C at −2 ◦ C/min. The final sintered part is also
shown in Fig. 5. The long holding stage allows to reach the final stage of
sintering, i.e. approaching full density. This experimental setting offers
the possibility to validate the model predictions not only in terms of
dimensional changes (as most previous studies did) but also in terms
of the evolution of relative density throughout the whole sintering
process. The shrinkage, dL/L0 , with respect to sintering temperature
that is given in Fig. 5.
    The viscosity evolution of LaWO54 and the corresponding viscosity
functions, based on Eq. (12), are given in Fig. 6. To construct the Ar-
rhenius model, we use the normalized temperature 1∕𝑇 ∗ = 1∕𝑇 − 1∕𝑇𝑇                           Fig. 6. Viscosity (𝜂) of LaWO54 as a function of temperature, plotted with respect to
(defined in Section 2), with 𝑇𝑇 defined as the transition temperature at                      the reciprocal of normalized temperature (1∕𝑇 ∗ ), as determined from dilatometry. The
which the sintering starts and the material viscosity drops drastically.                      lines correspond to the deformed Arrhenius functions, Eq. (12), with 𝜂0 = 2.975 × 1013
                                                                                              Pa⋅s; 𝑑 = −2.791, 𝛾 = 7965 kJ/mol for temperature below 𝑇𝑇 and 𝑑 = −0.226, 𝛾 = 665
For the LaWO54 used here, 𝑇𝑇 is 1005 ◦ C, resulting in 1∕𝑇 ∗ < 0 when                         kJ/mol for temperature above 𝑇𝑇 . 𝑇𝑇 = 1005 ◦ C is determined from the maximum
the sintering temperature is higher than the transition temperature,                          value of viscosity during sintering.
i.e. when 𝑇 > 1005 ◦ C.
    For temperatures below 𝑇𝑇 (1∕𝑇 ∗ > 0), the viscosity of LaWO54
stays almost constant around 3 × 1013 Pa⋅s, but increases to around

                                                                                       4945
H. Shi et al.                                                                                                          Journal of the European Ceramic Society 43 (2023) 4939–4949




Fig. 7. Left: Initial and final simulated geometry of the pellet, before and after the 2196-min sintering process. The colour bar indicates the displacement [mm] in the thickness
(z) direction. 3888 solid elements are used, with symmetry boundary conditions along the x-z and y-z planes. Right: Relative density evolution during sintering of LaWO54 pellet
- experiments vs. simulation. Inset: SEM image of the final sintered LaWO54 pellet microstructure.


1 × 1014 Pa⋅s when 1∕𝑇 ∗ is getting close to zero. For temperatures above                          Table 3
                                                                                                   Sintering of LaWO54 pellet: experiment vs. simulation.
𝑇𝑇 (1∕𝑇 ∗ > 0), the viscosity decreases from a maximum value to around
1 × 1010 Pa⋅s with increasing sintering temperature 𝑇 . The deformed Ar-                            Dimensions                Exp.               Sim.               Error
                                                                                                    [mm]                                                            [%]
rhenius function 𝜂(𝑇 ) adequately captures the viscosity dependency on
                                                                                                    R                         8.10               7.98               1.5
temperature. The initial increase followed by a decrease of the viscosity
                                                                                                    H                         5.68               5.84               3.0
could be caused by different material phases at different temperatures.
As studied in [60], at temperature below 𝑇𝑇 , the powder pellet may
have the La2 O3 phase embedded with LaWO54 phase, and this La2 O3
phase transforms into LaWO54 phase with increasing temperature, in                           points per element. The final pellet dimensions after sintering for both
line with the initial increase of the viscosity. While for temperatures                      experiments and simulations are summarized in Table 3. The model
above 𝑇𝑇 , the solid state sintering process is activated and the material                   slightly overestimates the shrinkage in the radial direction (1.5% error)
starts to flow, i.e. a decrease in viscosity is observed. Note that in the                   and underestimates the shrinkage in the thickness direction instead
low temperature branch (1∕𝑇 ∗ > 0), the activation energy 𝛾 strongly                         (2.9% error). These small discrepancies can arise from the small stress
depends on the amount of data included in this range since at lower                          applied by the dilatometer’s push-rod in the experiments. Even though
temperatures sintering has not started yet. Here, the upper limit is set                     free sintering is conducted, in the dilatometer the push-rod needs to be
as 1∕𝑇 ∗ ≤ 0.0003. The low-temperature branch is included in Fig. 7 for                      in contact with the surface of the pellet throughout the whole sintering
                                                                                             process, and thus a small force (25 cN) is applied along the thickness
completeness, but at 𝑇 < 800 ◦ C (1∕𝑇 ∗ > 0.0003 or 𝑡 > 400 mins) almost
                                                                                             direction.
no sintering shrinkage happens.
                                                                                                 The relative density changes in experiments and simulations are also
    In addition to the heating stage, holding and cooling stages are
                                                                                             compared in Fig. 7. According to dilatometry data (blue circles), the
also involved in the viscosity analysis. During the holding stage, the
                                                                                             relative density, 𝜌, increases from 59.7% to 95.2% after the cooling
temperature is held constant at 1500 ◦ C, and thus Eq. (12) cannot                           stage, at 𝑡 = 2196 mins. The simulation (dashed line) adequately
capture the viscosity changes that are associated with microstructural                       captures the evolution of the relative density throughout the whole
(and potentially phase) changes under isothermal conditions, as it only                      sintering process, giving a final relative density prediction of 95.7%,
gives a single viscosity value at a given temperature. The viscosity                         and thus resulting in a 0.4% error compared to the experiments. Even
increases as the sintering proceeds during the isothermal holding, while                     with a relatively long holding time (12 h), the shrinkage process
pores keep shrinking. In the final stage of sintering, grain growth                          appears to stop before the pellet reaches its full density. To investigate
occurs, and viscosity can strongly depend on grain size and other                            the dominating mechanism behind this, the final sintered pellet is
microstructural features. To accurately determine the grain growth and                       polished and scanned using SEM with a 1 kV accelerating voltage. The
additional microstructural changes during material sintering, thorough                       inset of Fig. 7, a representative micrograph, reveals a large-sized pore,
experimental campaigns would be required. Therefore, we instead pro-                         surrounded by fully densified LaWO54 . Such large-sized, spherical pores
pose to add this additional dependency on the microstructure evolution                       are well-known to be a cause of incomplete densification due to ex-
indirectly, by adding a dependency of viscosity on the relative density                      tremely slow shrinkage kinetics [61,62]. Furthermore, the final density
during holding: 𝜂(𝜌) = 𝜂(𝑇 ∗ ) ⋅ 10(𝜌−𝜌0 )∕𝛥𝜌∗𝛽 with 𝜌0 = 92%, 𝛥𝜌 = 0.02,                    of the sintered pellets has been measured via two different methods:
𝛽 = 1.33, whereby the coefficients are obtained from dilatometry data.                       geometry-based, i.e. as weight/volume ratio (black filled circle) and
During the cooling stage, the viscosity increases again with decreasing                      via the Archimedes method (brown filled circle). Although the final
temperature, and thus the deformed Arrhenius function can be applied                         relative density from the Archimedes method is slightly higher than
                                                                                             that from the geometry-based method, the outcomes of both methods
again.
                                                                                             are consistent with the model predictions, further proving the validity
    Given this viscosity formulation, LaWO54 properties and sintering
                                                                                             of the proposed modelling method. Note that measuring the initial/final
process parameters, the simulation is implemented with a quarter pellet
                                                                                             relative density accurately is not always as easy as in the case presented
and the appropriate symmetry conditions, as shown in Fig. 7. The
                                                                                             here, since many sintering applications involve binders, additives other
geometry after sintering is also given, with the displacement field in                       than ceramics or require a porous final microstructure, such as for cat-
the 𝑧-direction (dZ), in the same figure. The displacement dZ decreases                      alytic membranes and substrates, fuel cells, battery electrodes, etc. [5].
smoothly with the height and reaches a minimum of −1.1 mm (max-                              In these cases, the characterization of initial/final relative densities,
imum shrinkage) at the top of the pellet. The other two displacement                         both with and without differential shrinkage, becomes non-trivial.
fields, dX and dZ, show a similar trend. Since in this case, the pellet                      Therefore, a robust, reliable and computationally tractable modelling
is homogeneous, no differential shrinkage is expected, and thus 8-node                       framework that can predict the density evolution during the sintering
SSC elements are used instead of SLS elements. This further reduces                          of any powder material becomes particularly valuable for successful
the computational cost, thanks to the lower number of integration                            process implementation, optimization and design of experiments.

                                                                                      4946
H. Shi et al.                                                                                                 Journal of the European Ceramic Society 43 (2023) 4939–4949


6. Conclusions and outlook                                                          Appendix. Reduction             and        implementation          of     implicit
                                                                                    solution scheme
    The linear-viscous case of the SOVS model, based on the theories
of irreversible deformation (flow) of porous bodies, was implemented                    From Eq. (16) we need to minimize the residual and iteratively solve
in FEM code. A novel improved and simplified implicit integration                   13 unknown state variables every timestep for the set of implicit equa-
scheme for the state variables was proposed to avoid the inverse                    tions proposed. This means at each timestep and at each integration
of the Jacobian at each integration point using a staggered implicit                point, Eq. (16) needs to be solved to reach local convergence. This it
solution scheme, resulting in a reduction factor of 50 (using the same              will quickly lead to high computational costs once 3D solid elements
solid element) to 1000 (using the solid-like shell element) in terms of             and/or longer total simulation times are employed, which is typically
computational cost. The modelling strategy was verified by comparing                the case for a traditional free sintering process. Therefore, a reduction
the simulated relative density evolutions to analytical solutions, as well          of the implicit equations is applied such that only 1 unknown state
as to sintering experiments. The utilization of solid-like shell elements           variable needs to be solved at every timestep at the integration points.
with the SOVS constitutive model of sintering opened the possibility
of predicting bending and distortion problems in bilayers induced by                A.1. Implicit equation associated with elastic strain
differential shrinkage, which are common in the manufacturing of
components for energy and electronics applications, with a relatively                   The residual of the elastic strain results from the strain decomposi-
small computational cost. As an example, the computation cost (CPU                  tion Eq. (1),
time) of the benchmark simulation of Garino’s bilayer bar experi-
ment [47] was reduced by approximately three orders of magnitude,                   𝒇 𝜺𝑒 = 𝛥𝜺𝑒 + 𝛥𝜺𝑖 − 𝛥𝜺                                                          (1A)
enabling the simulation of hours-long sintering processes with a normal
laptop/computer in short time frames.                                               A.2. Implicit equation associated with inelastic strain
    Apart from Garino’s bilayer bar experiment, Garino’s bilayer disc
experiment, which is close to real applications, was also simulated for                The residual of the inelastic strain is then formed from the general
a quantitative comparison. The agreement between simulated results                  implicit solution routine Eq. (15)
and experiments is good, with the differences/errors up to 4% and                                                          𝝈′      tr(𝝈) − 3𝑃𝐿
8% for the bilayer bar and disc experiments, respectively. To further               𝒇 𝜺𝑖 = 𝛥𝜺𝑖 − 𝛥𝑡𝜺̇ 𝑖 𝑡+𝛥𝑡 = 𝛥𝜺𝑖 − 𝛥𝑡       − 𝛥𝑡             𝑰                   (2A)
                                                                                                                          2𝜂𝜙         18𝜂𝜓
improve the accuracy, a new sintering experiment was carried out
using a ceramic material that is particularly relevant in bilayer and                  Note that all the time dependent variables (𝝈, 𝑃𝐿 , 𝜂, 𝜓) refer to the
membrane processing for energy applications (catalysis for hydrogen                 unknown values at the next time step, i.e. 𝑡 + 𝛥𝑡.
generation): LaWO54 . A new method to determine the temperature and
micro-structure influence on the material viscosity was proposed and                A.3. Evolution of relative density
validated with this independent sintering experiment. Unlike previous
studies that focused mainly on the heating stage of sintering, our                     From Eq. (9), the change of density can be derived within one
sintering experiment and simulation covered the full cycle: heating,                timestep, leading to its residual form:
holding and cooling stages. The simulation accurately predicted the                 𝑓𝜌 = 𝛥𝜌 + 𝜌𝑡+𝛥𝑡 𝛥𝑒                                                             (3A)
final dimensions of sintered pellet with errors up to around 3%. Fur-
thermore, the relative density evolution predicted by the simulations               where 𝛥𝑒 is the trace of the change of inelastic strain tensor tr(𝛥𝜺𝑖 ).
was also compared to experimental values that originate from different                 As 𝛥𝜌 can be expressed as a function of 𝛥𝜺𝑖 , we could explicitly
measurement methods, confirming the agreement and accuracy of the                   calculate the density evolution and eliminate this unknown from the
proposed model.                                                                     solution routine. Integrating Eq. (9) over 𝛥𝑡:
    These SOVS model developments open pathways towards fast, ac-
                                                                                    𝜌𝑡+𝛥𝑡 = 𝜌𝑡 exp (𝛥𝑒)                                                            (4A)
curate and versatile continuum scale simulations of a multitude of
sintering processes. The differential shrinkage during co-sintering of
                                                                                    A.4. Elimination of the inelastic strain
bilayer or even trilayer parts with different materials or porosity levels
in each layer can now be smoothly simulated in virtual frameworks.
                                                                                        Combining Eqs. (1A), (2A) and (3A), it is more efficient to remove
Further improvements in the model details, e.g. to incorporate micro-
                                                                                    part of the unknowns and keep only two variables for solving: 𝛥𝜺𝑒
features such as grain growth, will be studied in more detail in future
                                                                                    and tr(𝛥𝜺𝑖 ). Then from Eqs. (1A) and (2A), we obtain a new system
works.
                                                                                    of equations:
Declaration of competing interest                                                   ⎧                 𝝈′    1
                                                                                    ⎪𝒇 𝜺𝑒 = 𝛥𝜺𝑒 + 𝛥𝑡 2𝜂𝜙 + 3 𝛥𝑒𝑰 − 𝛥𝜺
                                                                                    ⎨              tr(𝝈)−3𝑃𝐿                                                       (5A)
    The authors declare that they have no known competing finan-
                                                                                    ⎪𝑓𝑒 = 𝛥𝑒 − 3𝛥𝑡 18𝜂𝜓
cial interests or personal relationships that could have appeared to                ⎩
influence the work reported in this paper.                                              For brevity, we hide the parameter dependencies in the above set
                                                                                    of equations. All the parameters are evaluated based on the dependent
Acknowledgements
                                                                                    state variable’s values at the next timestep, e.g., 𝝈(𝜌𝑡+𝛥𝑡 ), 𝑃𝐿 (𝜌𝑡+𝛥𝑡 ),
                                                                                    𝜂(𝑇 𝑡+𝛥𝑡 , 𝜌𝑡+𝛥𝑡 ), 𝜓(𝜌𝑡+𝛥𝑡 ), while the relative density 𝜌(𝛥𝑒) is given by
    The financial support through the ‘‘AMAZING’’ project (grant no.
TKITOEAmazing) from Dutch top consortia for Knowledge and Innova-                   Eq. (4A).
tion programme Energy and Industry (TKI E&I) is gratefully acknowl-                     In order to obtain simple and clear derivatives, Eq. (5A) can be
edged. The authors would like to thank Dr. Wendelin Deibert and                     rewritten as,
                                                                                    {
Prof. Wilhelm Albert Meulenberg (Institute of Energy and Climate Re-                   𝒇 𝜺𝑒 = 𝛥𝜺𝑒 + 𝛥𝑡𝐴𝝈 ′ + 13 𝛥𝑒𝑰 − 𝛥𝜺
search, Materials Synthesis and Processing, Forschungszentrum Jülich,                                                                                      (6A)
                                                                                       𝑓𝑒 = 𝛥𝑒 − 3𝛥𝑡[𝐵tr(𝝈) − 𝐶]
Germany) for providing the materials for the experimental validation
steps. The authors would also like to thank MSc. Michel Drazkowsky                  where
and Prof. Arian Nijmeijer (Inorganic Membranes, University of Twente,                                 1
                                                                                    ⎧𝐴(𝜌𝑡+𝛥𝑡 (𝛥𝑒)) = 2𝜂𝜙
the Netherlands) for their support with pressing and sintering experi-              ⎪                  1
ments. The Institute for Sustainable Process Technology (ISPT) is also              ⎨𝐵(𝜌𝑡+𝛥𝑡 (𝛥𝑒)) = 18𝜂𝜓
                                                                                    ⎪
acknowledged for the help in coordinating the project.                              ⎩𝐶(𝜌𝑡+𝛥𝑡 (𝛥𝑒)) = 3𝐵(𝜌𝑡+𝛥𝑡 (𝛥𝑒)) ⋅ 𝑃𝐿

                                                                             4947
H. Shi et al.                                                                                                               Journal of the European Ceramic Society 43 (2023) 4939–4949


A.5. Solving scheme of reduced system of implicit equations                                       [3] J.-M. Missiaen, Solid-state spreading and sintering of multiphase materials,
                                                                                                      Mater. Sci. Eng. A 475 (1–2) (2008) 2–11, http://dx.doi.org/10.1016/j.msea.
                                                                                                      2007.01.160.
    In Eq. (6A), we have 7 unknowns with 𝛥𝑒 and 𝛥𝜺𝑒 that con-                                     [4] C. Djangang, A. Elimbi, U. Melo, G. Lecomte, C. Nkoumbou, J. Soro, J.-P. Bonnet,
sists of 6 independent strain components. To solve them using the                                     P. Blanchart, D. Njopwouo, Sintering of clay-chamotte ceramic composites for
Newton–Raphson method, one needs to construct a 7 × 7 Jacobian:                                       refractory bricks, Ceram. Int. 34 (5) (2008) 1207–1213, http://dx.doi.org/10.
                                                                                                      1016/j.ceramint.2007.02.012.
       𝜕𝑓       𝜕𝑓
   ⎡ 𝜺𝑒     𝜺𝑒
               ⎤                                                                                  [5] W. Deibert, M.E. Ivanova, W.A. Meulenberg, R. Vaßen, O. Guillon, Preparation
          𝜕𝛥𝑒 ⎥
𝑱 =⎢ 𝑒
    𝜕𝛥𝜺                                                                                               and sintering behaviour of La5.4WO12-𝛿 asymmetric membranes with optimised
   ⎢ 𝑒𝜕𝑓  𝜕𝑓 𝑒 ⎥                                                                                      microstructure for hydrogen separation, J. Membr. Sci. 492 (2015) 439–451,
   ⎣ 𝜕𝛥𝜺𝑒 𝜕𝛥𝑒 ⎦
                                                                                                      http://dx.doi.org/10.1016/j.memsci.2015.05.065.
where                                                                                             [6] W. Deibert, F. Schulze-Küppers, E. Forster, M.E. Ivanova, M. Müller, W.A.
                                                                                                      Meulenberg, Stability and sintering of MgO as a substrate material for Lanthanum
𝜕𝒇 𝜺𝑒                     1                                                                           Tungstate membranes, J. Eur. Ceram. Soc. 37 (2) (2017) 671–677, http://dx.doi.
      = 4 𝑰 + 2𝛥𝑡𝜇𝐴(4 𝑰 − 𝑰 ⊗ 𝑰)
𝜕𝛥𝜺𝑒                      3                                                                           org/10.1016/j.jeurceramsoc.2016.09.033.
𝜕𝒇 𝜺𝑒                                                                                             [7] K. Leonard, W. Deibert, M.E. Ivanova, W.A. Meulenberg, T. Ishihara, H.
        1        𝜕𝐴 𝜕𝜌 ′                                                                              Matsumoto, Processing ceramic proton conductor membranes for use in
      = 𝑰 + 𝛥𝑡          𝝈
𝜕𝛥𝑒     3        𝜕𝜌 𝜕𝛥𝑒                                                                               steam electrolysis, Membranes 10 (11) (2020) 339, http://dx.doi.org/10.3390/
 𝜕𝑓𝑒                                                                                                  membranes10110339.
      = −3𝛥𝑡𝐵(2𝜇 + 3𝜆)𝑰                                                                           [8] M. Jurisch, T. Studnitzky, O. Andersen, B. Kieback, 3D screen printing for the
𝜕𝛥𝜺𝑒
                [                       ]                                                             fabrication of small intricate Ti-6Al-4V parts, Powder Metall. 58 (5) (2015)
 𝜕𝑓𝑒              𝜕𝐵 𝜕𝜌          𝜕𝐶 𝜕𝜌                                                                339–343, http://dx.doi.org/10.1179/0032589915Z.000000000255.
      = 1 − 3𝛥𝑡          tr(𝝈) −
 𝜕𝛥𝑒              𝜕𝜌 𝜕𝛥𝑒         𝜕𝜌 𝜕𝛥𝑒                                                           [9] S.L. Sing, W.Y. Yeong, F.E. Wiria, B.Y. Tay, Z. Zhao, L. Zhao, Z. Tian, S.
                                                                                                      Yang, Direct selective laser sintering and melting of ceramics: A review, Rapid
For all the terms inside Jacobian:                                                                    Prototyp. J. 23 (3) (2017) 611–623, http://dx.doi.org/10.1179/0032589915Z.
𝜕𝜌𝑡+𝛥𝑡                                                                                                000000000255.
        = −𝜌𝑡 exp(−𝛥𝑒) = −𝜌𝑡+𝛥𝑡                                                                  [10] E. Torresani, D. Giuntini, C. Zhu, T. Harrington, K.S. Vecchio, A. Molinari, R.K.
 𝜕𝛥𝑒                                                                                                  Bordia, E.A. Olevsky, Anisotropy of mass transfer during sintering of powder
 𝜕𝜙
        = 2𝜌𝑡+𝛥𝑡                                                                                      materials with pore–particle structure orientation, Metall. Mater. Trans. A 50
𝜕𝜌𝑡+𝛥𝑡                                                                                                (2) (2019) 1033–1049, http://dx.doi.org/10.1007/s11661-018-5037-x.
 𝜕𝜓          2 𝜌2 (2𝜌 − 3)                                                                       [11] E. Torresani, R. German, R. Huff, E. Olevsky, Influence of gravity on sintering
        =−                                                                                            of 3D-printed powder components, J. Am. Ceram. Soc. 105 (1) (2022) 131–146,
𝜕𝜌 𝑡+𝛥𝑡      3 (𝜌 − 1)2
                                                                                                      http://dx.doi.org/10.1111/jace.18056.
    𝜕𝐴         1                                                                                 [12] G. Largiller, L. Dong, D. Bouvard, C.P. Carry, A. Gabriel, Constitutive modeling
        =−
    𝜕𝜙       2𝜂𝜓 2                                                                                    of the behaviour of cermet compacts during reaction sintering, Powder Technol.
    𝜕𝐵          1                                                                                     208 (2) (2011) 496–502, http://dx.doi.org/10.1016/j.powtec.2010.08.049.
        =−                                                                                       [13] G. Largiller, D. Bouvard, C.P. Carry, A. Gabriel, J. Müller, T. Staab, Deformation
    𝜕𝜓       18𝜂𝜙2
                                                                                                      and cracking during sintering of bimaterial components processed from ceramic
   𝜕𝐴     𝜕𝐴 𝜕𝜙 𝜕𝜌                                                                                    and metal powder mixes. Part I: Experimental investigation, Mech. Mater. 53
        =
  𝜕𝛥𝑒     𝜕𝜙 𝜕𝜌 𝜕𝛥𝑒                                                                                   (2012) 123–131, http://dx.doi.org/10.1016/j.mechmat.2012.04.002.
   𝜕𝐵     𝜕𝐵 𝜕𝜓 𝜕𝜌                                                                               [14] G. Largiller, L. Dong, D. Bouvard, C.P. Carry, A. Gabriel, Deformation and
        =                                                                                             cracking during sintering of bimaterial components processed from ceramic and
  𝜕𝛥𝑒     𝜕𝜓 𝜕𝜌 𝜕𝛥𝑒
                                                                                                      metal powder mixes. Part II: Numerical simulation, Mech. Mater. 53 (2012)
  𝜕𝑃𝐿     6𝛼
        =     𝜌                                                                                       132–141, http://dx.doi.org/10.1016/j.mechmat.2012.05.012.
    𝜕𝜌     𝑟𝑝                                                                                    [15] T.T. Molla, R. Bjørk, E. Olevsky, N. Pryds, H.L. Frandsen, Multi-scale modeling
  𝜕𝑃𝐿     𝜕𝑃𝐿 𝜕𝜌                                                                                      of shape distortions during sintering of bi-layers, Comput. Mater. Sci. 88 (2014)
        =                                                                                             28–36, http://dx.doi.org/10.1016/j.commatsci.2014.02.041.
  𝜕𝛥𝑒       𝜕𝜌 𝜕𝛥𝑒                                                                               [16] J. Rojek, S. Nosewicz, M. Maździarz, P. Kowalczyk, K. Wawrzyk, D. Lumelskyj,
   𝜕𝐶           𝜕𝐵         𝜕𝑃
        = 3𝑃𝐿        + 3𝐵 𝐿                                                                           Modeling of a sintering process at various scales, Procedia Eng. 177 (2017)
  𝜕𝛥𝑒          𝜕𝛥𝑒         𝜕𝛥𝑒                                                                        263–270, http://dx.doi.org/10.1016/j.proeng.2017.02.210.
                                                                                                 [17] K.-i. Mori, K. Osakada, T. Hirano, Finite element simulation of nonuniform
A.6. Elimination of the elastic strain                                                                shrinkage during sintering of ceramic products, in: Hot Isostatic Pressing—Theory
                                                                                                      and Applications, Springer, 1992, pp. 29–34, http://dx.doi.org/10.1007/978-94-
                                                                                                      011-2900-8_5.
   As the deviatoric part of 𝜺𝑖 is linear with the stress deviator, Eq. (6A)                     [18] H. Zipse, Finite-element simulation of the die pressing and sintering of a ceramic
can be further reduced to only a single scalar unknown 𝛥𝑒.                                            component, J. Eur. Ceram. Soc. 17 (14) (1997) 1707–1713, http://dx.doi.org/
   Using Eq. (2):                                                                                     10.1016/S0955-2219(97)00037-X.
                                                                                                 [19] E.A. Olevsky, Theory of sintering: From discrete to continuum, Mater. Sci. Eng.
                                                                                                      R 23 (2) (1998) 41–100, http://dx.doi.org/10.1016/S0927-796X(98)00009-6.
tr(𝛥𝝈) = (3𝜆 + 2𝜇)tr(𝛥𝜺 − 𝛥𝜺𝑖 )                                                  (7A)
                                                                                                 [20] T. Kraft, H. Riedel, Numerical simulation of solid state sintering; Model and
                                                                                                      application, J. Eur. Ceram. Soc. 24 (2) (2004) 345–361, http://dx.doi.org/10.
Putting into Eq. (6A), we obtain:
                                                                                                      1016/S0955-2219(03)00222-X.
              [                ]
𝑓𝑒 = 𝛥𝑒 − 3𝛥𝑡 𝐵tr(𝝈 𝑡+𝛥𝑡 ) − 𝐶                                                                   [21] T.T. Molla, H.L. Frandsen, R. Bjørk, D.W. Ni, E. Olevsky, N. Pryds, Modeling
              [                       ]                                                               kinetics of distortion in porous bi-layered structures, J. Eur. Ceram. Soc. 33 (7)
   = 𝛥𝑒 − 3𝛥𝑡 𝐵tr(𝝈 𝑡 ) + 𝐵tr(𝛥𝝈) − 𝐶                                            (8A)                 (2013) 1297–1305, http://dx.doi.org/10.1016/j.jeurceramsoc.2012.12.019.
              [                                       ]                                          [22] A. Al-Qudsi, M. Kammler, A. Bouguecha, C. Bonk, B.-A. Behrens, Comparison
   = 𝛥𝑒 − 3𝛥𝑡 𝐵tr(𝝈 𝑡 ) + 𝐵(3𝜆 + 2𝜇)tr(𝛥𝜺 − 𝛥𝜺𝑖 ) − 𝐶
                                                                                                      between different numerical models of densification during solid-state sintering
Then the tangent can be derived as:                                                                   of pure aluminium powder, Prod. Eng. 9 (1) (2015) 11–24, http://dx.doi.org/
                                                                                                      10.1007/s11740-014-0574-7.
𝜕𝑓𝑒           [
                𝜕𝐵                             𝜕𝐵                                                [23] D. Giuntini, I.W. Chen, E.A. Olevsky, Sintering shape distortions controlled
    = 1 − 3𝛥𝑡       tr(𝝈 𝑡 ) + (3𝜆 + 2𝜇)tr(𝛥𝜺)
𝜕𝛥𝑒             𝜕𝛥𝑒                            𝜕𝛥𝑒                                                    by interface roughness in powder composites, Scr. Mater. 124 (2016) 38–41,
                                                 ]                               (9A)
                                   𝜕𝐵       𝜕𝐶                                                        http://dx.doi.org/10.1016/j.scriptamat.2016.06.024.
              −(3𝜆 + 2𝜇)(𝐵 +          𝛥𝑒) −                                                      [24] D. Giuntini, E.A. Olevsky, Sintering stress of nonlinear viscous materials, J. Am.
                                  𝜕𝛥𝑒       𝜕𝛥𝑒
                                                                                                      Ceram. Soc. 99 (11) (2016) 3520–3524, http://dx.doi.org/10.1111/jace.14550.
                                                                                                 [25] C.L. Martin, D. Bouvard, S. Shima, Study of particle rearrangement during
References
                                                                                                      powder compaction by the Discrete Element Method, J. Mech. Phys. Solids 51
                                                                                                      (4) (2003) 667–693, http://dx.doi.org/10.1016/S0022-5096(02)00101-1.
 [1] R. German, Sintering: From Empirical Observations to Scientific Principles,                 [26] A. Wonisch, O. Guillon, T. Kraft, M. Moseler, H. Riedel, J. Rödel, Stress-induced
     Butterworth-Heinemann, 2014.                                                                     anisotropy of sintering alumina: Discrete element modelling and experiments,
 [2] A. Zavaliangos, J. Missiaen, D. Bouvard, Anisotropy in shrinkage during sintering,               Acta Mater. 55 (15) (2007) 5187–5199, http://dx.doi.org/10.1016/j.actamat.
     Sci. Sinter. 38 (1) (2006) 13–25, http://dx.doi.org/10.2298/SOS0601013Z.                         2007.05.038.


                                                                                          4948
H. Shi et al.                                                                                                                Journal of the European Ceramic Society 43 (2023) 4939–4949


[27] C.L. Martin, H. Camacho-Montes, L. Olmos, D. Bouvard, R.K. Bordia, Evolution                 [46] M.W. Reiterer, K.G. Ewsuk, J.G. Argüello, An Arrhenius-type viscosity function
     of defects during sintering: Discrete element simulations, J. Am. Ceram. Soc. 92                  to model sintering using the Skorohod Olevsky viscous sintering model within
     (7) (2009) 1435–1441, http://dx.doi.org/10.1111/j.1551-2916.2009.03014.x.                         a finite element code, J. Am. Ceram. Soc. 89 (6) (2006) 1930–1935, http:
[28] T. Rasp, C. Jamin, A. Wonisch, T. Kraft, O. Guillon, Shape distortion and                         //dx.doi.org/10.1111/j.1551-2916.2006.01041.x.
     delamination during constrained sintering of ceramic stripes: Discrete element               [47] J.G. Argüello, M.W. Reiterer, K.G. Ewsuk, Verification, performance, validation,
     simulations and experiments, J. Am. Ceram. Soc. 95 (2) (2012) 586–592, http:                      and modifications to the SOVS continuum constitutive model in a nonlinear
     //dx.doi.org/10.1111/j.1551-2916.2011.04939.x.                                                    large-deformation finite element code, J. Am. Ceram. Soc. 92 (7) (2009)
[29] S. Nosewicz, J. Rojek, K. Pietrzak, M. Chmielewski, Viscoelastic discrete element                 1442–1449, http://dx.doi.org/10.1111/j.1551-2916.2009.03008.x.
     model of powder sintering, Powder Technol. 246 (2013) 157–168, http://dx.doi.                [48] D. Giuntini, E.A. Olevsky, C. Garcia-Cardona, A.L. Maximenko, M.S. Yurlova, C.D.
     org/10.1016/j.powtec.2013.05.020.                                                                 Haines, D.G. Martin, D. Kapoor, Localized overheating phenomena and optimiza-
[30] S. Nosewicz, J. Rojek, M. Chmielewski, K. Pietrzak, Discrete element modeling of                  tion of spark-plasma sintering tooling design, Materials (Basel, Switzerland) 6 (7)
     intermetallic matrix composite manufacturing by powder metallurgy, Materials                      (2013) 2612–2632, http://dx.doi.org/10.3390/ma6072612.
     12 (2) (2019) 281, http://dx.doi.org/10.3390/ma12020281.                                     [49] T.T. Molla, D.W. Ni, R. Bulatova, R. Bjørk, C. Bahl, N. Pryds, H.L. Frandsen,
[31] B. Hugonnet, J.M. Missiaen, C.L. Martin, C. Rado, Effect of contact alignment                     Finite element modeling of camber evolution during sintering of bilayer struc-
     on shrinkage anisotropy during sintering: Stereological model, discrete element                   tures, J. Am. Ceram. Soc. 97 (9) (2014) 2965–2972, http://dx.doi.org/10.1111/
     model and experiments on NdFeB compacts., Mater. Des. 191 (2020) 108575,                          jace.13025.
     http://dx.doi.org/10.1016/j.matdes.2020.108575.                                              [50] B.T. Lester, Verification of the Skorohod-Olevsky Viscous Sintering (SOVS)
[32] Y.U. Wang, Computer modeling and simulation of solid-state sintering: A phase                     Model, Tech. Rep., Sandia National Lab.(SNL-NM), Albuquerque, NM (United
     field approach, Acta Mater. 54 (4) (2006) 953–961, http://dx.doi.org/10.1016/                     States), 2017, http://dx.doi.org/10.2172/1411315.
     j.actamat.2005.10.032.                                                                       [51] K. Shinagawa, Micromechanical modelling of viscous sintering and a constitutive
[33] J. Deng, A phase field model of sintering with direction-dependent diffusion,                     equation with sintering stress, Comput. Mater. Sci. 13 (4) (1999) 276–285,
     Mater. Trans. 53 (2) (2012) 385–389, http://dx.doi.org/10.2320/matertrans.                        http://dx.doi.org/10.1016/S0927-0256(98)00132-3.
     M2011317.                                                                                    [52] V. Aquilanti, K.C. Mundim, M. Elango, S. Kleijn, T. Kasai, Temperature depen-
[34] S. Biswas, D. Schwen, J. Singh, V. Tomar, A study of the evolution of                             dence of chemical and biophysical rate processes: Phenomenological approach
     microstructure and consolidation kinetics during sintering using a phase field                    to deviations from Arrhenius law, Chem. Phys. Lett. 498 (1) (2010) 209–213,
     modeling based approach, Extreme Mech. Lett. 7 (2016) 78–89, http://dx.doi.                       http://dx.doi.org/10.1016/j.cplett.2010.08.035.
     org/10.1016/j.eml.2016.02.017.                                                               [53] M. Bischoff, E. Ramm, Shear deformable shell elements for large strains and
[35] K. Chockalingam, V.G. Kouznetsova, O. van der Sluis, M.G.D. Geers, 2D Phase                       rotations, Internat. J. Numer. Methods Engrg. 40 (23) (1997) 4427–4449,
     field modeling of sintering of silver nanoparticles, Comput. Methods Appl. Mech.                  http://dx.doi.org/10.1002/(SICI)1097-0207(19971215)40:23%3C4427::AID-
     Engrg. 312 (2016) 492–508, http://dx.doi.org/10.1016/j.cma.2016.07.002.                           NME268%3E3.0.CO;2-9.
[36] S. Biswas, D. Schwen, V. Tomar, Implementation of a phase field model                        [54] H. Parisch, A continuum-based shell theory for non-linear applications, Internat.
     for simulating evolution of two powder particles representing microstructural                     J. Numer. Methods Engrg. 38 (11) (1995) 1855–1883, http://dx.doi.org/10.
     changes during sintering, J. Mater. Sci. 53 (8) (2018) 5799–5825, http://dx.doi.                  1002/nme.1620381105.
     org/10.1007/s10853-017-1846-3.                                                               [55] F. Hashagen, J. Schellekens, R. De Borst, H. Parisch, Finite element procedure
[37] J. Hötzer, M. Seiz, M. Kellner, W. Rheinheimer, B. Nestler, Phase-field simulation                for modelling fibre metal laminates, Compos. Struct. 32 (1–4) (1995) 255–264,
     of solid state sintering, Acta Mater. 164 (2019) 184–195, http://dx.doi.org/10.                   http://dx.doi.org/10.1016/0263-8223(95)00083-6.
     1016/j.actamat.2018.10.021.                                                                  [56] J.J.C. Remmers, R. De Borst, G. Wells, Analysis of delamination growth with dis-
[38] R. Termuhlen, X. Chatzistavrou, J.D. Nicholas, H.-C. Yu, Three-dimensional phase                  continuous solid-like shell elements, in: Proceedings of the Fifth World Congress
     field sintering simulations accounting for the rigid-body motion of individual                    on Computational Mechanics, WCCM V, Vienna University of Technology,
     grains, Comput. Mater. Sci. 186 (2021) 109963, http://dx.doi.org/10.1016/j.                       Austria, 2002.
     commatsci.2020.109963.                                                                       [57] J.J.C. Remmers, G.N. Wells, R. de Borst, A solid-like shell element allowing
[39] E. Olevsky, V. Rikare, T.J. Garino, M.V. Braginsky, Simulation of Sintering of                    for arbitrary delaminations, Internat. J. Numer. Methods Engrg. 58 (13) (2003)
     Layered Structures, Tech. Rep., Sandia National Lab.(SNL-NM), Albuquerque, NM                     2013–2040, http://dx.doi.org/10.1002/nme.907.
     (United States), 2000.                                                                       [58] F. Hashagen, R. de Borst, Numerical assessment of delamination in fibre metal
[40] V. Tikare, M. Braginsky, E.A. Olevsky, Numerical simulation of solid-state                        laminates, Comput. Methods Appl. Mech. Engrg. 185 (2–4) (2000) 141–159,
     sintering: I, sintering of three particles, J. Am. Ceram. Soc. 86 (1) (2003) 49–53,               http://dx.doi.org/10.1016/S0045-7825(99)00256-X.
     http://dx.doi.org/10.1111/j.1151-2916.2003.tb03276.x.                                        [59] J. Arguello, V. Tikare, T. Garino, M. Braginsky, Three-Dimensional Simulation of
[41] M. Braginsky, V. Tikare, E. Olevsky, Numerical simulation of solid state sintering,               Sintering Using a Continuum Modeling Approach, Sandia National Laboratories,
     Int. J. Solids Struct. 42 (2) (2005) 621–636, http://dx.doi.org/10.1016/j.ijsolstr.               2003.
     2004.06.022.                                                                                 [60] A. Magrasó, R. Haugsrud, Effects of the La/W ratio and doping on the struc-
[42] E.A. Olevsky, V. Tikare, T. Garino, Multi-scale study of sintering: A review, J.                  ture, defect structure, stability and functional properties of proton-conducting
     Am. Ceram. Soc. 89 (6) (2006) 1914–1922, http://dx.doi.org/10.1111/j.1551-                        lanthanum tungstate La 28-x W 4+x O 54+𝛿 . A review, J. Mater. Chem. A 2
     2916.2006.01054.x.                                                                                (32) (2014) 12630–12641, http://dx.doi.org/10.1039/C4TA00546E.
[43] K. Wawrzyk, P. Kowalczyk, S. Nosewicz, J. Rojek, A constitutive model and                    [61] C. Manière, E. Saccardo, G. Lee, J. McKittrick, A. Molinari, E.A. Olevsky, Swelling
     numerical simulation of sintering processes at macroscopic level, AIP Conf. Proc.                 negation during sintering of sterling silver: An experimental and theoretical
     1922 (1) (2018) 030011, http://dx.doi.org/10.1063/1.5019045.                                      approach, Results Phys. 11 (2018) 79–84, http://dx.doi.org/10.1016/j.rinp.2018.
[44] T.T. Molla, N. Pryds, R. Bjørk, Modeling Macroscopic Shape Distortions during                     08.035.
     Sintering of Multi-Layers, Technical University of Denmark, 2014.                            [62] C. Manière, S. Chan, G. Lee, J. McKittrick, E.A. Olevsky, Sintering dilatometry
[45] D. Giuntini, X. Wei, A.L. Maximenko, L. Wei, A.M. Ilyina, E.A. Olevsky,                           based grain growth assessment, Results Phys. 10 (2018) 91–93, http://dx.doi.
     Initial stage of free pressureless spark-plasma sintering of vanadium carbide:                    org/10.1016/j.rinp.2018.05.014.
     Determination of surface diffusion parameters, Int. J. Refract. Met. Hard Mater.
     41 (2013) 501–506, http://dx.doi.org/10.1016/j.ijrmhm.2013.06.009.




                                                                                           4949
