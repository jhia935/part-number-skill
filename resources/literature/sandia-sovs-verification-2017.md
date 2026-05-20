                                                                                                        SAND2017-12933R




                                                              Operated for the U.S. Department of Energy by
                                                 National Technology and Engineering Solutions of Sandia, Inc.
                                                                    Albuquerque, New Mexico 87185




 date: November 16, 2017

   to: Distribution



 from: Brian Lester (1554)



subject: Verification of the Skorohod-Olevsky Viscous Sintering (SOVS) Model



      1    Introduction
      Sintering refers to a manufacturing process through which mechanically pressed bodies of
      ceramic (and sometimes metal) powders are heated to drive densification thereby removing
      the inherit porosity of green bodies [1]. As the body densifies through the sintering process,
      the ensuing material flow leads to macroscopic deformations of the specimen and as such
      the final configuration differs from the initial. Therefore, as with any manufacturing step,
      there is substantial interest in understanding and being able to model the sintering process
      to predict deformation and residual stress. Efforts in this regard have been pursued for face
      seals [2], gear wheels [3], and consumer products like wash-basins [4].

      To understand the sintering process, a variety of modeling approaches have been pursued at
      different scales [5]. At the mesoscale, kinetic Monte Carlo (KMC) simulations have been of
      interest both to study the kinetics of densification and impact of microstructural features as
      well as calibrate higher scale models [6, 7, 8]. At the continuum (macro-)scale of interest for
      production of parts like those listed above, a variety of three-dimensional constitutive models
      (e.g. [9, 10, 2, 11, 12]) have been postulated. In general, the formulations are motivated
      by the specifics and kinetics of different sintering types (i.e. solid-state [2], liquid [9], or
      viscous [10, 11]) and modeling terms and functions are constructed by assumptions regarding
      specific mechanisms.

      One particular formulation of interest has been the Skorohod-Olevsky viscous sintering
      (SOVS) model popularized by Olevsky [10]. This model has been used (and extended)
      to model the manufacturing process of different systems (e.g. [12, 13, 4]). This constitutive
      representation includes a viscous, non-linear formulation. Thus, analyzing continuum level
      problems through the finite element method requires appropriate integration schemes for the
      local constitutive behavior and sufficient spatial and temporal discretizations of the global



                                Exceptional Service in the National Interest
Distribution                                 –2–                          November 16, 2017

problem to resolve desired features. Constitutive implementations based on a semi-implicit
formulation of McHugh and Riedel [9] have been used by many analysts [12] while others
have leveraged features of commercial software [13]. Both the accuracy and robustness of
the constitutive integration scheme as well as the complexity of the finite element problem
can dictate required discretizations. In some efforts, difficulties in appropriately resolving
temporal and spatial fields have been noted. For instance, as part of their efforts verifying
and validating the SOVS model, Argüello et al. [12] (Section III.(2)) note,


      “However, it was found that the details of the deformation could not be ade-
      quately captured without a fairly fine mesh... From this it can be inferred that
      the curvature (and presumably warpage, etc.) cannot be captured in this model
      without significant mesh refinement. Therefore problems in which the accurate
      predictions of the details of the deformation of the part are sought will be com-
      putational intensive, requiring either long run-times or perhaps requiring the use
      of massively parallel computing.”


Such an observation regarding the difficulty of using the SOVS (or other) sintering models
can hinder the adoption and utilization of corresponding models. However, it is important
to note that the investigation of Argüello et al. [12] used both a legacy finite element code
(JAS3D) and the legacy constitutive implementation scheme of McHugh and Riedel [9].
Here, the possibility of mitigating these issues have been addressed by (i) proposing and
implementing a new, fully implicit integration scheme, and (ii ) investigating the possibility
that such techniques can aid in both the spatial and temporal convergence characteristics
of the global finite element problem. Section 2 briefly presents the SOVS sintering model
and both legacy (McHugh-Riedel) and new (implicit) numerical implementation. Section 3
uses these implementations to revisit both constitutive verification (Section 3.1) and the
bilayer bar verification (Section 3.2) problems of Argüello et al. [12]. Some conclusions and
recommendations towards future research are given in Section 4.


2     Model
Before proceeding to the verification exercises, the SOVS model used in these studies is pre-
sented here for completeness. The specific theoretical form is given in Section 2.1 while both
the existing McHugh-Riedel and new implicit integration scheme are discussed in Section 2.2.

2.1   Theoretical Model

The Skorohod-Olevsky viscous sintering (SOVS) model is a continuum mechanics based
model for the 3D evolution of a powder-based material [10] undergoing the sintering process
(see [2, 11, 12] for examples of utilization). In the case of the linear viscosity assumption,
the inelastic (sintering) strain rate, ε̇in
                                         ij , may be written as,
Distribution                                         –3–                           November 16, 2017


                                               σij0      σkk − 3σs (ρ)
                                 ε̇in
                                   ij =                +               δij ,                         (1)
                                          2η0 (θ) φ (ρ) 18η0 (θ) ψ (ρ)

in which σij , σij0 , and (1/3) σkk are the Cauchy stress, deviatoric stress, and pressure that
are related via σij = σij0 + (1/3) σkk δij while η0 , φ, and ψ are the shear viscosity of the fully
dense skeleton phase, normalized shear viscosity, and normalized bulk viscosity1 and σs is
the sintering stress. In addition to the Cauchy stress, the material state is also described by
the temperature, θ, and relative density, ρ = ρt /ρT , where ρt is the density at time “t” and
ρT is the theoretical density.

The general dependencies assumed here for the viscosities and sintering stress are denoted in
Eqn. 1. Other research efforts have expanded the dependencies of these functions and various
functional representations for each of the different terms have been proposed by modelers to
capture different characteristics (see [2, 11, 12] for some examples). Here, the emphasis is
on numerical performance and behavior the forms selected, studied, and verified by Arüello
et al. [12] are used. These forms are given by,


                                                                      ρb2
                             φ (ρ) = a1 ρb1 ,              ψ (ρ) = a2        ,                       (2)
                                                                  (1 − ρ)c2
                            σs (ρ) = σs0 σ̄s (ρ) ,        σ̄s (ρ) = a3 ρb3 ,                         (3)
                                         2             
                                            θ            θ
                            η0 (θ) = a4            + b4        + c4 ,                                (4)
                                           θ0            θ0

with ai , bi and ci all being fitting coefficients, θ0 is a reference temperature, and σs0 is the
local sintering stress given by σs0 = 3α/r0 with α being the surface tension and r0 the average
grain size. The surface tension and average grain size are assumed to be known and constant
such that σs0 is a fitting parameter.

Finally, an evolution equation for the relative density is needed. To this end, conservation
of mass provides an expression of the form,


                                                 ρ̇ = −ρε̇in
                                                          kk .                                       (5)

2.2      Numerical Implementation

As with any 3D constitutive model intended for use with finite element codes, an accu-
rate, robust, and efficient numerical routine is needed. Substantial effort has been made
in developing robust return mapping algorithms [14, 15, 16, 17, 18] for plasticity based on
1
    The theoretical derivation assumes a two phase system composed of a bulk skeleton and void phase. See
    Olevsky [10] for details of the theory.
Distribution                                            –4–                                 November 16, 2017

operator splitting [19]. A key feature of such implementations is the separation of the elastic
and plastic response. Specifically, in (visco-)plasticity the magnitude of the inelastic, plas-
tic strain increment is given by a consistency parameter (commonly the equivalent plastic
strain increment) that is found by enforcement of the consistency relation2 . Dependence on
stress in then brought in through the direction of inelastic deformation and satisfaction of
the consistency constraint.

For the current SOVS sintering model, such a separation is not evident. Specifically, through
Eqn. 1 it is evident that the direction and magnitude of inelastic strain depends directly on
the stress state. Thus, conventional routines like those in the previous citations cannot
be used to integrate this model, and a different approach is needed. In the literature and
previous versions, the SOVS model was integrated using a “semi-implicit” formulation put
forth by McHugh and Riedel [9] that was based on a prior viscoplastic creep implementation
of Peirce et al. [20]. In the two decades since these efforts, recent work has focused on
developing new algorithms for the robust, implicit solution of constitutive models (see [17,
18]). Here both the conventional McHugh and Riedel and a fully implicit integration scheme
are described to explore the relative capabilities.

Given the small strain and time-dependent nature of the formulation in the proceeding
section a hypoelastic scheme is used. For a constitutive model integrated from t = tn to
tn+1 , via loadings of total strain increments dεij = εn+1
                                                       ij  − εnij and prescribed temperature
steps dθ = θn+1 − θn , the stress may be integrated as,



                                         σijn+1 = σijn + dσij ,                                                (6)
                                                            dεkl − dεin
                                                                              
                                         dσij = Cijkl                kl           ,                            (7)


with Cijkl the fourth order stiffness tensor (assumed isotropic). The remaining state variables
may be integrated as,


                                            in(n+1)         in(n)
                                           εij         = εij        + dεin
                                                                        ij ,                                   (8)
                                                 n+1        n
                                                 ρ     = ρ + dρ.                                               (9)


where,


                                                        in(n)            in(n+1)
                                  dεin
                                    ij = (1 − β) ε̇ij           ∆t + β ε̇ij           ∆t,                     (10)
                                    dρ = (1 − β) ρ̇n ∆t + β ρ̇n+1 ∆t,                                         (11)
2
    In rate-independent formulations, this revolves around satisfaction of the yield surface, f , being zero during
    inelastic deformation (f (t) = 0). For viscoplasticity, a variety of similar concepts are invoked.
Distribution                                      –5–                                November 16, 2017

and β ∈ [0, 1] is an integration constant and ∆t = tn+1 − tn . With the values at t = tn
known, the difference in the two approaches is associated with the question of determining
the rates at t = tn+1 .

McHugh-Riedel (MR) Implementation [9]

For the McHugh-Riedel “semi-implicit” approach, the updated rates of stain variable relation
are essentially determined by performing a Taylor-series expansion of the terms about their
values at t = tn ,



                        in(n+1)         in(n) ∂ ε̇in
                                                  ij        ∂ ε̇in
                                                                ij      ∂ ε̇in
                                                                            ij
                      ε̇ij        =   ε̇ij +         dσkl +        dρ +        dθ,                     (12)
                                              ∂σkl           ∂ρ          ∂θ
                                             ∂ ρ̇       ∂ ρ̇ ∂ ρ̇
                          ρ̇n+1 = ρ̇n +           dσij + dρ + dθ.                                      (13)
                                            ∂σij        ∂ρ   ∂θ

In this case, the derivates are evaluated at t = tn . Inserting Eqns. 12 and 13 into Eqns. 10
and 11 and using Eqn. 7 produces the following system of equations,


                                      ∂ ε̇in
                                          ij               in(n)       ∂ ε̇in
                                                                           ij
                         L−1
                          ijkl dσkl + β∆t    dρ = dεij − ε̇ij ∆t − β∆t        dθ,                      (14)
                                       ∂ρ                               ∂θ
                                         
                 ∂ ρ̇                ∂ ρ̇                        ∂ ρ̇
           −β∆t       dσij + 1 − β∆t         dρ = ρ̇n ∆t + β∆t dθ,                                     (15)
                ∂σij                 ∂ρ                          ∂θ

where,

                                                             ∂ ε̇in
                                                                 ij
                                      L−1
                                       ijkl = Sijkl + β∆t           ,                                  (16)
                                                             ∂σkl

with Sijkl = C−1
              ijkl being the fourth order compliance tensor. Solving for dσij and dρ yields,




                      ρ̇n ∆t + β∆t ∂∂θρ̇ dθ + β∆t ∂σ
                                                   ∂ ρ̇
                                                         Lijkl dεkl − ε̇kl ∆t − β∆t ∂∂θ
                                                                                     ε̇kl
                                                                                               
                                                      ij
                                                                                          dθ
               dρ =                                                       ∂ ε̇in
                                                                                                   ,   (17)
                                      1 − β∆t ∂∂ρρ̇ + (β∆t)2 ∂σ
                                                              ∂ ρ̇
                                                                 ij
                                                                    Lijkl ∂ρkl
                                              ∂ ε̇in          ∂ ε̇in
                                                                      
                                  in(n)           kl              kl
          dσij   = Lijkl dεkl − ε̇kl ∆t − β∆t        ∆θ − β∆t        dρ .                              (18)
                                               ∂θ              ∂ρ
Distribution                                           –6–                                             November 16, 2017

Implicit Implementation

A fully implicit approach may be pursued by again considering Eqns. 8-11 but instead of
using a Taylor expansion of the rates at t = tn+1 an iterative solution technique is used to
directly solve for them. To this end, Eqns. 10 and 11 are recast in residual form as,


                          ε                                   in(n)                    in(n+1)
                         rij = −dεin
                                  ij + (1 − β) ε̇ij                   ∆t + β ε̇ij                ∆t,                (19)
                              ρ                           n                n+1
                          r         = −dρ + (1 − β) ρ̇ ∆t + β ρ̇                   ∆t.                              (20)


A key to this approach is initializing the various variables appropriately to enable convergence
to the solution. In rate-independent elastic-plastic routines, this is typically done in an elastic
predictor-inelastic corrector scheme in which all input deformations are assumed to be elastic
and initializing all inelastic, plastic terms to their values at the previous converged time-steps
(see [21]). Such a scheme is complicated for the current routine due to (i ) the loss of complete
separation between elastic and inelastic deformations as indicated by Eqn. 1 and (ii ) the
possibility of substantial inelastic deformation even under low/no-load (as indicated by the
verification exercises of [12]). The second point indicates that trial deformations could lead
to excessive trial stress necessitating use of line-search [17] or trust-region [18] augmentations
of the constitutive routines to achieve convergence. An alternative that could alleviate this
issue is to invert the concept and try an “inelastic predictor-elastic corrector” type scheme.
In the proposed approach, this concept is achieved by setting,


                                                                              
                (k=0)                           in(k=0)                (k=0)
               σij       =        σijn ,      ε̇ij      = ε̇ˆin
                                                             ij       σij          ,                                (21)
               in(k=0)                                                                                  (k=0)
            dεij         = dεij ,              ρ(k=0) = ρn ,                   ρ̇(k=0) = −ρ(k=0) ε̇kk           ,   (22)


in which k denotes the inelastic correction increment. Some of these selections are debatable
given item (i ) above. To concretely resolve this issue, some consideration of the initial
guesses and impact on convergence properties would likely be needed.

To find the updated material state at t = tn+1 , the state variables must be incrementally
updated until convergence is achieved as measured by sufficient reduction in the residuals.
In the current work, a merit function, m, of the form,

                                               ρ 2  2        !
                                          1    r      E    ε ε
                                       m=           +     rij rij ,                                                 (23)
                                          2    ρ0     σs0

is used to assess convergence.
                      √        Here, E is the elastic modulus, and ρ0 is the initial relative
density. Specifically, m is used as a convergence criteria. This form represents a scaled,
unweighted merit function that simultaneously assesses performance of both residuals instead
Distribution                                     –7–                                  November 16, 2017

of separate tolerances. The scaling coefficients, 1/ρ0 and E/σs0 , are introduced to ensure
equal contribution of both residuals to the merit function. The selection and impact of these
coefficients for elastic-plastic models has been explored in [18].
To iterate and find the solution, a standard Newton-Raphson scheme is used in which in-
crements of the state variables are found by solving the system of equations formed when
linearizing the residuals in terms of the solution variables (see [22]). This approach results
in a system of equations as,


                         ε(k)                         ∂ ε̇in
                                                          ij
                      −rij      = L−1
                                   ijkl ∆σ   kl + β∆t        ∆ρ,                                   (24)
                                                       ∂ρ
                                                                     
                                         ∂ ρ̇                    ∂ ρ̇
                      −rρ(k)    = β∆t         ∆σij + −1 + β∆t           ∆ρ,                        (25)
                                        ∂σij                     ∂ρ

where ∆σij and ∆ρ are increments in stress and relative density, respectively, such that,


                                      σijk+1 = σijk + ∆σijk ,                                      (26)
                                      ρk+1 = ρk + ∆ρk .                                            (27)

The various derivatives and terms are evaluated using updated state terms rather than
previously converged values. Solving the system comprised of Eqns. 24 and 25 yields,


                                                       ∂ ρ̇         ε
                                            −rρ + β∆t ∂σ  ij
                                                             Lijkl rkl
                         ∆ρ =                                            ∂ ε̇in
                                                                                  ,                (28)
                                  −1 + β∆t ∂∂ρρ̇ − (β∆t)2 ∂σ ∂ ρ̇
                                                                ij
                                                                   Lijkl ∂ρkl
                                                     ∂ ε̇in
                                                                 
                                          ε              kl
                        ∆σij    = −Lijkl rkl + β∆t          ∆ρ .                                   (29)
                                                      ∂ρ

3    Results
To assess the capabilities of the formulations and assess the impact of the proposed fully
implicit schemes, the constitutive verification and bilayer bar structural verification exercises
used by Argüello et al. [12] are studied. The former is presented in Section 3.1 while the
latter is investigated in Section 3.2. For both studies, the “Continuum Mechanics” set of
model parameters corresponding to 0.2µm ZnO power given by Argüello et al. [12] (originally
coming from [10]) are used. The model parameters are given in Table 1 while E = 123.7
GPa and a Poisson ratio, ν, of ν = 0.356 is used.
For these studies, both the McHugh-Riedel (denoted “MR”) and new implicit approach (re-
ferred to as “New” in following for convenience) were implemented in the Sierra/SolidMechanics [23].
All simulations were then performed with Sierra/SolidMechanics.
Distribution                                             –8–                           November 16, 2017

                      a1       1 (-)           b1        2 (-)
                      a2      2/3 (-)          b2        3 (-)        c2       1 (-)
                      a3       1 (-)           b3        2 (-)
                      a4   517 (GPa-s)         b4    -1066 (GPa-s)    c4    564 (GPa-s)
                      α    1.27 (J/m2 )        r0       1 (µm)

      Table 1: SOVS Model Parameters [10, 12] for a 0.2µm ZnO powder used in this work


3.1      Constitutive Verification

As a first step to verify the constitutive implementation, the verification exercises of Argüello
et al. [12] are considered. These exercises comprise of two problems: free-sinter and sinter-
forge. The first problem corresponds to a no-load condition with a prescribed temperature
profile while the second is associated with the same temperature history but with a constant
1 MPa tensile load. For both problems, the assumed temperature profile is that of a constant
                                                                                               ◦C
linear ramp from θ (t = 0) = 750◦ C to θ (t = tf ) = 1000◦ C at a constant ramp rate of 5 min
such that tf = 3000 s. In the following, these problems are simulated with a single finite
element to eliminate any impacts of a structural problem and test the specific constitutive
implementation.

For the free-sinter case, by assuming no-load (σij = 0) and using Eqns. 1 and 5 while
substituting expressions Eqns. 2–4 the rate of change of the density may be written,

                                             a3 σs0 b3 −b2 +1
                                      ρ̇ =          ρ         (1 − ρ)c2 ,                           (30)
                                             2a2 η0

which with parameters given in Table 1 yields the simplified expression for normalized poros-
ity, ξ = 1 − ρ,

                                                           3σs0 ξ
                                                    ξ˙ = −        ,                                 (31)
                                                            4η0

that can be analytically integrated in time by the solution given by Argüello et al. [12]. For
the sinter-forge case, no analytical solution may be found. As such, the normalized porosity
is numerically integrated3 via [12],

                                                    σξ        3σs0 ξ
                                        ξ˙ =              2 −        ,                              (32)
                                               4η0 (1 − ξ)     4η0

where σ is the applied uniaxial stress (1 MPa tensile load for the given case).
3
    A simple forward Euler scheme is used with ∆t = 0.6s.
Distribution                                                                                –9–                                                               November 16, 2017

Results of the verification exercises presenting the evolution of the relative densities with
temperature are given in Fig. 1 for both the free-sinter and sinter-forge cases using the
McHugh-Riedel (MR) and new implicit (New) implementation with β = 1.0. Two temporal
discretizations are considered; one coarse with 5 uniform time steps corresponding to ∆t =
600s and one fine of 200 uniform time steps with ∆t = 15 s. From the results of Fig. 1 it can
be seen that with the smaller time steps (Fig. 1b) both formulations reproduce the (semi-)
analytical formulations very well, while differences are noted at the coarser scale (Fig. 1a).
With respect to the larger time steps for the new implicit implementation, the actual density
is always lower than the analytical forms, while in the case of the McHugh-Riedel model the
relative density is initially greater before crossing the reference solution and ending up with
a smaller relative density.


                          0.70                                                                                              0.70
                                  Analytical - Free        Semi-Analytical - Forge                                                  Analytical - Free        Semi-Analytical - Forge
                                  Free (New)               Forge (New)                                                              Free (New)               Forge (New)
                          0.65    Free (MR)                Forge (MR)                                                       0.65    Free (MR)                Forge (MR)




Relative Density, ρ (-)                                                                           Relative Density, ρ (-)
                          0.60                                                                                              0.60



                          0.55                                                                                              0.55



                          0.50                                                                                              0.50



                          0.45                                                                                              0.45
                            750      800         850        900         950          1000                                     750      800         850        900         950          1000
                                               Temperature ( ◦ C)                                                                                Temperature ( ◦ C)

                                              (a) ∆t = 600s                                                                                     (b) ∆t = 15s

Figure 1: Evolution of the relative density, ρ, through the free-sinter and sinter-forge prob-
lems with loading increments of (a) ∆t = 600s and (b) ∆t = 15s. Numerical results with
both the McHugh-Riedel (MR) and new implicit implementation (New) are presented. In
all cases, β = 1.0.

To further consider the impact of the time step size on performance, convergence studies for
both the free-sinter (Fig. 2a) and sinter-forge (Fig. 2b) problems are presented in Figure 2.
Results for both the McHugh-Riedel and implicit scheme are presented with β = 0.5 and
β = 1.0. The relative error considered in these studies is in terms of the final relative density
of the numerical results versus the reference, (semi-) analytical results. It is important to
highlight that the error is not integrated over loading and merely reflects the final state.
Nonetheless, for the current discussion the use of this metric seems more than sufficient to
discuss the relative performance.

From the results of Fig. 2, it may be observed that the behaviors of the two problems are
very similar. Specifically, error decreases with time-step size (as would be expected) and in
general the β = 1.0 cases have errors that are higher than β = 0.5. This difference can be
attributed to what is essentially numerical error in integrating the response through time.
Distribution                                                                 –10–                                                             November 16, 2017



                       100                                                                            100
                                 β =1.0 (New)            β =1.0 (MR)                                           β   =1.0 (New)            β   =1.0 (MR)
                       10-1      β =0.5 (New)            β =0.5 (MR)                                  10-1     β   =0.5 (New)            β   =0.5 (MR)




((|ρ −ρ |)/ρ ) = (-)                                                           ((|ρ −ρ |)/ρ ) = (-)
           tf
                       10-2                                                               tf
                                                                                                      10-2

           ref t                                                                          ref t
                       10-3                                                                           10-3
           ref                                                                            ref
                       10-4                                                                           10-4
            num                                                                            num

                       10-5                                                                           10-5

                       10-6                                                                           10-6

                       10-7 1                                                                         10-7 1
                          10                       102                 103                               10                        102                    103
                                            Time Step, ∆t (s)                                                               Time Step, ∆t (s)
                                          (a) Free-sinter                                                                 (b) Sinter-forge

Figure 2: Error convergence of the (a) free-sinter and (b) sinter-forge in terms of time step
size. Error is given in terms of the relative difference of the final relative density to the
(semi-) analytical references. Results for the new implicit (New) and McHugh-Riedel (MR)
numerical schemes are given with β = 0.5, 1.0.


Along this line, in the results of Fig. 1 it can be seen that the densification rate (ρ̇) decreases
through loading. As such, with β = 1.0, dρ will leverage this lower end-of-step rate yielding
lower relative densities. This fact is reflected in the new implicit results of Fig. 1a in which
the numerically determined density is continually lower than the reference solutions. In
comparing the performance of the semi-implicit McHugh-Riedel implementation and those
of the new implicit scheme, little difference can be noted with β = 1.0. Some small decrease
in the final error can be noted at larger time-steps with β = 1.0 but the differences are
small and by considering Fig. 1a this may be potentially be associated with choise of error
metric. When β = 0.5, the new implicit scheme shows smaller errors than the existing
McHugh-Riedel implementation for both the free-sinter and sinter-forge and all time-steps.
In fairness, the errors of either implementation are small.

3.2                           Bilayer Bar

With the constitutive implementations verified in Section 3.1, the next step is to assess per-
formance for structural problems. To this end the bilayer bar problem of Argüello et al. [12]
is used. Note that slightly different geometries and parameter sets were used for purposes
of verification and validation in the work of [12]. Here as the numerical implementation and
not model form, is of interest, the previous validation is still applicable. Thus, only the
geometry corresponding to the verification exercises is considered, and the only parameter
set used is that of Table 1. It should also be pointed out that while Argüello et al. [12] detail
modifications to JAS3D needed to assess global convergence of this problem given the lack
of external loading, no such issues/modifications were needed for the current study.

Conceptually, the bilayer bar problem is very similar to the classic bimaterial strip example.
Distribution                                  –11–                           November 16, 2017

Specifically, a bar comprised of two sections of the same material, but different initial relative
densities, is uniformally heated. The solidification problem produces different contractions in
the two layers leading to a macroscopic bending. Although no-load conditions are maintained
on the exterior of the specimen, the variable material state will produce stresses along the
interface and interior. For the current study, ρupper
                                                   0   = 0.47 and ρlower
                                                                     0    = 0.57 and the same
                                                                        ◦
thermal profile as in the verification studies is used (θ (t = 0) = 750 C → θ (t = 3000s) =
                                       ◦C
1000◦ C at a constant ramp rate of 5 min  ).

The bilayer bar geometry is schematically represented in Fig. 3. Specific dimensions are
taken from [12] and are L = 7 mm, W = 4 mm, and Hu = Hl = 1.125 mm such that
H = 2.250 mm. The unit vectors êx , êy , and êz correspond to directions X, Y, and Z while
three points (pts. 2, 4, and 6) are marked in Fig. 3 and correspond to points used by Argüello
et al. [12] whose displacements (in the Z direction) were quantities of interest. Given the lack
of external load and geometry, quarter symmetry is used in this problem. Specifically, only
the darker shaded quarter in Fig. 3 is meshed and modeled. Symmetry conditions in the êz
and êx were imposed on the respective planes while a single node (at bar center along the
bottom edge) is fixed in the through thickness (êy ) direction to prevent the corresponding
rigid body mode.




                  Figure 3: Schematic of the bilayer bar problem geometry.


To study the impact of spatial and temporal discretizations, a series of meshes were con-
structed and then simulated with a variety of time-step sizes. To create the different meshes,
the desired number of elements in the through thickness direction was specified and the
characteristic mesh size was then determined by the total height (H) divided by the desired
number of elements. This dimension was used as a nominal mesh size and the entire geom-
etry was seeded with uniform hex elements. In what follows, the different meshes will be
referred to by the nominal number of through thickness elements. Meshes were constructed
with 8, 12, 20, and 32 through thickness elements corresponding to models with 672, 2,508,
Distribution                                  –12–                          November 16, 2017

11,160, and 44,800 elements, respectively. Selective deviatoric [23] elements were used. The
four meshes were each simulated with six different time discretizations involving different
number of fixed, uniform time-steps. Specifically, time-steps of ∆t = 15, 30, 60, 120, 300
and 600 s were used corresponding to simulations with 200, 100, 50, 25, 10, and 5 uniform
loading steps. For use as a reference comparison in later discussions, the problem was also
run using a 36 through thickness element mesh (64,512 elements) and 400 evenly spaced
increments of ∆t = 7.5s. For the reference case, a fully implicit case of β = 1.0 was used.

Convergence

The ability of the coarse meshes to reproduce results of the fine discretizations is considered
in Fig. 4. This comparison is made by investigating the macroscopic quantities of interest
used by Argüello et al. [12]; namely the displacements in the êz direction, denoted w, at nodes
2, 4, and 6. These results are given for the coarse mesh (8 through-thickness elements) with
time-steps of ∆t = 600s and ∆t = 15s along with the reference simulation. Figures 4a
and 4c presents the results for the legacy McHugh-Riedel implementation with β = 0.5 and
β = 1.0, respectively, while the complementary results with the new scheme are given in
Figs. 4b and 4d. From these results, it may be observed that in all cases good accuracy is
obtained with ∆t = 15 s. For the coarser time scale, ∆t = 600 s, the new implementation
with β = 0.5 shows similar level accuracy levels to the fine time scale. The other three
cases, however, all show substantial error with this reduced number of time-steps. As with
the previous constitutive verifications, the new implementation at β = 1.0 underpredicts the
final deformation. The existing McHugh-Riedel implementation results for β = 0.5 and 1.0
both produce final displacements approximately 10% higher than the reference case.

To consider the convergence characteristics of the two algorithms more concretely, Fig. 5
presents a time-convergence study for the two different implementations at β = 0.5 and 1.0
for the 8-through thickness element cases. Error is assessed in terms of the relative difference
of the final displacement in the êz direction of node 6 (w6 ) versus the reference case. From
Fig. 5 it is clear that the “New” implementation, with either β, shows superior convergence
characteristics versus that of the legacy McHugh-Riedel. As would be expected from Fig. 4,
the β = 0.5 cases demonstrate substantially better accuracy than their counterparts at larger
time-steps. Improvement with increasing number of load increments, however, eventually
saturate and at the ∆t = 30 s case the β = 1.0 case overtakes β = 0.5.

Figures 4 and 5 highlight the capabilities of the two implementations to capture the defor-
mation fields. These results, however, do not provide any information on the stress fields;
another important result in any mechanical analysis. To this end, Fig. 6 presents the aver-
age stress in the êx direction for the top and bottom layers indicated in Fig. 3. Although
generally similar results were obtained with respect to the deformation fields between the
numerical formulations, vastly different responses are noted in Fig. 6. With β = 1.0 (Figs. 6c
and 6d), similar responses can be noted. Specifically, the new implementation converges for
all of the different time-steps to very similar average stress levels. The existing McHugh-
Riedel formulation converges towards comparable stress levels but larger number of load
increments are needed to achieve those values. The β = 0.5 cases, on the other hand, exhibit
Distribution                                                                             –13–                                                  November 16, 2017



                0.20                                                                                        0.20



                0.15                                                                                        0.15




Displacement (mm)                                                                           Displacement (mm)
                0.10                                                                                        0.10



                0.05                                                                                        0.05
                                    ∆ =600 s
                                w2 , t                ∆ =600 s
                                                  w4 , t                   ∆ =600 s
                                                                       w6 , t                                                   ∆ =600 s
                                                                                                                           w2 , t                 ∆ =600 s
                                                                                                                                             w4 , t                     ∆ =600 s
                                                                                                                                                                   w6 , t
                                w2 ,∆t =15 s      w4 ,∆t =15 s         w6 ,∆t =30 s                                             ∆ =15 s
                                                                                                                           w2 , t                 ∆ =15 s
                                                                                                                                             w4 , t                     ∆ =30 s
                                                                                                                                                                   w6 , t
                                 ref                ref                 ref                                                 ref                ref                  ref
                                w2                w4                   w6                                                  w2                w4                    w6
                0.00                                                                                        0.00
                   750    800            850       900           950              1000                         750   800            850       900            950               1000
                                         Temperature, C                                                                             Temperature, C
                         (a) McHugh-Riedel, β = 0.5                                                                        (b) New, β = 0.5


                0.20                                                                                        0.20



                0.15                                                                                        0.15




Displacement (mm)                                                                           Displacement (mm)
                0.10                                                                                        0.10



                0.05                                                                                        0.05
                                    ∆ =600 s
                                w2 , t                ∆ =600 s
                                                  w4 , t                   ∆ =600 s
                                                                       w6 , t                                                   ∆ =600 s
                                                                                                                           w2 , t                 ∆ =600 s
                                                                                                                                             w4 , t                     ∆ =600 s
                                                                                                                                                                   w6 , t
                                w2 ,∆t =15 s      w4 ,∆t =15 s         w6 ,∆t =30 s                                             ∆ =15 s
                                                                                                                           w2 , t                 ∆ =15 s
                                                                                                                                             w4 , t                     ∆ =30 s
                                                                                                                                                                   w6 , t
                                 ref                ref                 ref                                                 ref                ref                  ref
                                w2                w4                   w6                                                  w2                w4                    w6
                0.00                                                                                        0.00
                   750    800            850       900           950              1000                         750   800            850       900            950               1000
                                         Temperature, C                                                                             Temperature, C
                         (c) McHugh-Riedel, β = 1.0                                                                        (d) New, β = 1.0

Figure 4: Evolution of the edge displacements noted in Fig. 3 through the sintering process
using the (a,c) McHugh-Riedel and (b,d) new implicit scheme with ∆t = 600 and 15 s and
(a,b) β = 0.5 and (c,d) β = 1.0. For comparison, results from a reference fine-meshed, small
time-step simulation are also presented.


substantial oscillations and unstable (the new implementation in Fig. 6b) and what seems
to be conditionally stable (McHugh-Riedel, Fig. 6a) responses. In both cases, these issues
are mitigated with decreased time-step sizes but at the finest presented cases (∆t = 7.5 s)
oscillatory behaviors are still clearly present.

Such oscillatory responses have been previously noted with time-dependent creep and vis-
coplastic formulations and are associated with the stability of the time-integration of the
constitutive formulation [24, 25, 26]. The original work of Pierce et al. [20] noted stable
responses for β ≥ 0.5 for their creep formulation and contextualized their observations based
on the analysis of Zienkiewicz and Cormeau [24] and Cormeau [25]. McHugh and Riedel [9]
built upon these observations in their formulation and stated that they exhibited improved
Distribution                                              –14–                                November 16, 2017


                                           100

                                           10-1




                 ((|w6 −w6 |)/w6 ) = (-)
                             tf            10-2
                             t

                      ref
                                           10-3
                      ref
                                           10-4
                      num
                                           10-5

                                           10-6      β   =1.0 (New)     β   =1.0 (MR)
                                                     β   =0.5 (New)     β   =0.5 (MR)
                                           10-7 1
                                              10            102                         103
                                                    Time Step, ∆t (s)
Figure 5: Temporal convergence of the bilayer bar problem with the 8 element through-
thickness mesh with different numerical formulations.



accuracy with β = 0.5 instead of β = 0.0. It must be pointed out that both the viscoplastic
models [20, 25] and liquid-state sintering model of McHugh-Riedel [9] have different formu-
lations from each other and the current viscous sintering model making the applicability of
the previous stability analysis unknown. In their investigation of the SOVS model, Argüello
et al. [12] do not comment on the selected integration parameter. Additionally, neither the
previous reports of McHugh and Riedel [9] or Argüello et al. [12] report on the mechanical
stress fields. Thus, whether or not these issues have been observed before is unknown.

In terms of the relative magnitudes, the stress values observed in all of the results of Fig. 6 are
fairly small (≈< .1 MPa). However, the differences of the free-sinter and sinter-forge cases
in Fig. 1 demonstrate that even seemingly small stress values can impact the deformation
response and highlight the importance of resolving and capturing both the relative density
and stress fields to accurately predict the results of a sintering process. Therefore, even
though the β = 0.5 simulations in Fig. 2 exhibit improved accuracy at larger time-steps,
the corresponding instability in the stress fields mean such integration is not desirable. The
β = 1.0 case does not exhibit such numerical stability problems and acceptable accuracy. As
such, the integration parameter β = 1.0 is used in the remainder of this work and addressing
and analyzing the numerical stability is left to future efforts.

Bearing the choice of integration parameter β = 1.0 in mind, Fig. 7 investigates mesh
convergence and the impact of spatial discretization. Essentially, time convergence studies
like those presented in Fig. 5 are repeated for each mesh using the McHugh-Riedel (Fig. 7a)
and new (Fig. 7b) schemes. In general, lower errors and faster rates of convergence are noted
for the new implicit scheme versus than existing McHugh-Riedel implementation. At larger
Distribution                                                                    –15–                                                           November 16, 2017



                                                                                                      400
                          top
                             ∆t =600s
                         σ̄xx ,                    ∆t =300s
                                                 bot
                                               σ̄xx ,              ∆t =7.5s
                                                                 top
                                                               σ̄xx ,
                                                                                                              top
                                                                                                                 ∆t =600s
                                                                                                             σ̄xx ,                       ∆t =15s
                                                                                                                                        top
                                                                                                                                      σ̄xx ,

                         σ̄ ,∆t =600s             ,∆t =15s     σ̄ ,∆t =7.5s                                      ∆t =600s                 ∆t =15s
                          bot                    top             bot                                          bot                       bot
                  100     xx
                                               σ̄xx              xx                                   300    σ̄xx ,                   σ̄xx ,

                            ,∆t =300s          σ̄ ,∆t =15s                                                      ,∆t =300s                ,∆t =7.5s
                          top                    bot                                                          top                       top
                         σ̄
                          xx                     xx
                                                                                                             σ̄
                                                                                                              xx
                                                                                                                                      σ̄xx

                                                                                                             σ̄ ,∆t =300s             σ̄ ,∆t =7.5s
                                                                                                              bot                       bot
                                                                                                      200     xx                        xx
                   50




Stress (kPa)                                                                       Stress (kPa)
                                                                                                      100
                    0
                                                                                                        0

                  −50
                                                                                                  −100


               −100                                                                               −200


                                                                                                  −300
                   750          800     850             900   950        1000                        750              800      850             900   950       1000
                                        Temperature, C                                                                         Temperature, C

                           (a) McHugh-Riedel, β = 0.5                                                                       (b) New, β = 0.5



                   40                                                                                  40



                   20                                                                                  20
                                               top
                                                  ∆t =600s
                                              σ̄xx ,              ∆t =60s
                                                                top
                                                              σ̄xx ,
                                                                                                                                      top
                                                                                                                                         ∆t =600s
                                                                                                                                     σ̄xx ,              ∆t =60s
                                                                                                                                                       top
                                                                                                                                                     σ̄xx ,

                                                  ∆t =600s        ∆t =60s                                                                ∆t =600s        ∆t =60s

   Stress (kPa)                                                                        Stress (kPa)
                                               bot              bot                                                                   bot              bot
                                              σ̄xx ,          σ̄xx ,                                                                 σ̄xx ,          σ̄xx ,

                                                 ,∆t =300s       ,∆t =30s                                                               ,∆t =300s       ,∆t =30s
                                               top              top                                                                   top              top
                                              σ̄
                                               xx
                                                              σ̄xx
                                                                                                                                     σ̄
                                                                                                                                      xx
                                                                                                                                                     σ̄xx
                    0                                                                                   0
                                              σ̄ ,∆t =300s    σ̄ ,∆t =30s                                                            σ̄ ,∆t =300s    σ̄ ,∆t =30s
                                               bot              bot                                                                   bot              bot
                                               xx               xx                                                                    xx               xx

                                                 ,∆t =120s       ,∆t =15s                                                               ,∆t =120s       ,∆t =15s
                                               top              top                                                                   top              top
                                              σ̄
                                               xx
                                                              σ̄xx
                                                                                                                                     σ̄
                                                                                                                                      xx
                                                                                                                                                     σ̄xx

                                              σ̄ ,∆t =120s    σ̄ ,∆t =15s                                                            σ̄ ,∆t =120s    σ̄ ,∆t =15s
                                               bot              bot                                                                   bot              bot
                  −20                          xx               xx
                                                                                                      −20                             xx               xx




                  −40                                                                                 −40


                   750          800     850             900   950        1000                          750            800      850             900   950       1000
                                        Temperature, C                                                                         Temperature, C

                           (c) McHugh-Riedel, β = 1.0                                                                       (d) New, β = 1.0
                                                                             top       top
Figure 6: Evolution of the average stress in the top and bottom layers, σ̄xx     and σ̄xx  ,
respectively, through the sintering process using the (a,c) McHugh-Riedel and (b,d) new
implicit scheme and (a,b) β = 0.5 and (c,d) β = 1.0 using different time scales. Note, the
β = 0.5 results use a different vertical axes to highlight their behaviors.


time-steps, little impact on mesh size is seen with either approach. For the McHugh-Riedel
case, this trend is observed over all time-steps and the final displacement measure seems
fairly independent of mesh size. Below ≈ ∆t = 30 s some deviation between the convergence
of the different meshes is observed for the implicit results. Taken together, these results
indicate that potentially more involved error convergence metrics (e.g. an energy norm)
may be needed to more quantitatively assess the convergence rates of the different schemes.
Nonetheless, by comparing the two results it is clear that (i ) a lower level of error may be
achieved by the new scheme for a given spatial and temporal discretization and (ii ) the
limited mesh size dependence indicates that global deformation metrics can be computed by
reasonable meshes and time-steps.
Distribution                                                               –16–                                              November 16, 2017



                          100                                                                          100


                          10-1                                                                         10-1




((|w6 −w6 |)/w6 ) = (-)                                                      ((|w6 −w6 |)/w6 ) = (-)
            tf            10-2                                                           tf            10-2
            t                                                                            t

    ref                                                                          ref
                          10-3                                                                         10-3

    ref                                                                          ref
                          10-4                                                                         10-4

     num                                                                          num
                          10-5                                                                         10-5


                          10-6               8 Elem.      20 Elem.                                     10-6            8 Elem.      20 Elem.
                                             12 Elem.     32 Elem.                                                     12 Elem.     32 Elem.
                          10-7 1                                                                       10-7 1
                             10              102                     103                                  10           102                     103
                                      Time Step, ∆t (s)                                                         Time Step, ∆t (s)
                                   (a) McHugh-Riedel                                                              (b) New

Figure 7: Evolution of the edge displacements noted in Fig. 3 through the sintering process
using the (a) McHugh-Riedel and (b) new implicit scheme with ∆t = 600 and 15 s and
β = 1.0. For comparison, results from a reference fine-meshed, small time-step simulation
are also presented.

The previous convergence studies examine the capabilities of the model and its implemen-
tation to resolve global quantities of interest. Such investigations, however, do not reveal
anything about the ability of these formulations to resolve spatial variations and corre-
sponding details. To this end, Fig. 8 presents field variations of the reference solution and
simulations using the coarse mesh with a large and small time step (∆t = 600 and 10 s
respectively). Only the quarter of the bilayer bar that is simulated is presented in Fig. 8 to
enable seeing the field resolution through the cross-section and enable a closer look at the re-
sults. Specifically, the relative density, σxx , and v (displacement in the vertical, êy direction)
are shown at the end of the simulation. In terms of the stress, although detail is lost due to
the more limited spatial discretization, both the 8 element mesh solutions do a reasonable
job of capturing the stress field in comparison to the reference case. For the relative density
and displacement, a similar statement can be made for the fine time-scale mesh. Differences
can be observed in the displacement and relative density fields when the large time-step is
used. Thus, based on these results it would seem that (i ) details of state variable fields can
be resolved by coarse meshes but (ii ) using appropriate temporal discretizations is necessary
to accurately resolve these fields.

Timing and Scaling

The current proposed integration scheme is focused on introducing a implicit routine of
the constitutive model that relies upon an iterative solution. The existing McHugh-Riedel
approach, while “semi-implicit” in construction, leverages a single step solve to find the
solution variables. Although the previous results highlight the utilization of an implicit
scheme may improve accuracy of the simulation, changing the approach like this is liable
to drive up computational cost. To consider this impact, Fig. 9 presents the relative cost
Distribution                                  –17–                          November 16, 2017




               Ref. (36 Elem ∆t = 7.5s)     8 Elem ∆t = 600 s           8 Elem ∆t = 10 s




   ρ (-)




 σxx (Pa)




  v (m)


Figure 8: Contour plots of fields of ρ (relative density), σxx (stress), and v (êy displacement)
for the reference model and 8 element through thickness mesh at a coarse (∆t = 600s) and
fine (∆t = 10 s) temporal discretization. The results of only the quarter symmetry mesh are
shown to highlight the internal fields. For reference, the out of plane direction is êz and êx
is the horizontal direction (positive pointed to the right).
Distribution                                           –18–                                 November 16, 2017

of the McHugh-Riedel formulation versus the proposed implicit scheme for the 8 element
through-thickness mesh with different time-steps. Note, in the results of Fig. 9, the relative
time of any case is computed by taking the wall-clock time of the specified formulation
and normalizing by its new implicit counterpart. Thus, the normalization times vary with
time-step but not across models.



                                    1.4
                                                                 Unscal. New β =1.0
                                                                 Unscal. New β =0.5
                                                                 MR β =1.0
                                    1.2                          MR β =0.5


                        Rel. Time (-)
                                    1.0


                                    0.8


                                    0.6

                                        101              102                          103
                                                  Time Step, ∆t (s)
Figure 9: Relative timings of the 8 element through thickness problem at different time-
steps. The relative times correspond to the wallclock time of the specified case normalized
by the time of the “New”, scaled, β = 1.0 at the corresponding time-step. “Unscal.” refers
to cases with an unscaled merit function.


From Fig. 9, it is observed that as expected the McHugh-Riedel formulation is faster than
the proposed scheme. At larger time-steps, the speed-up is more than 30% while the impact
decreases with increasing temporal resolution and at the smallest time-step the timing in-
crease is only ≈ 10%. Although faster, from Fig. 7, it may be noted that this 10% speed-up
at ∆t = 15 s also comes with error that is approximately an order of magnitude greater.
Thus, the trade-off between speed-up and accuracy is clear. These results seem independent
of choice of integration parameter, β.

In Section 2.2 it was mentioned that convergence of the material model was assessed via a
scaled merit function. This scaling was introduced to normalize the relative contributions
of the two residuals but also, given the choice of terms, has an added effect of essentially
tightening the convergence criteria versus an unscaled form for a specified tolerance. The
impact of this convergence tightening is also investigated in which the results of using an
unscaled merit function4 are also presented in Fig. 9. At larger time-step cases, the imposed
                                                 
4                                       2
    To be clear, munscaled = (1/2) (rρ ) + rij
                                            ε ε
                                               rij .
Distribution                                                               –19–                                                    November 16, 2017

tighter tolerances means additional iterations are needed to converge in the material model.
For the global simulation time, these additional computations manifest as increased wallclock
time and slower performance. In these cases, ≈20% time savings could be realized by using
an unscaled merit function. Below ∆t = 60 s, different behaviors are noted and much
increased simulation times are needed for convergence.

A possible explanation of the results for the unscaled merit function in Fig. 9 is associated
with the fact that, in essence, the unscaled merit function has a looser convergence criteria
than the form of Eqn. 23. If the tolerance is too loose, the constitutive integrator may return
unconverged, incorrect stress values that make satisfying global equilibrium more difficult.
Such problems, in turn, would require additional global, finite-element iterations and increase
cost. Such an issue could be exacerbated by smaller time-steps and corresponding loadings.
To consider this issue further, Fig. 10 considers the performance of the constitutive model
with different constitutive tolerances. In all previous cases, for both scaled and unscaled
merit functions, a tolerance of 1 × 10−9 was used. Figure 10a presents relative timings
(normalized to the 1 × 10−9 tolerance case) using decreasing convergence criteria. It can be
observed that for tolerances greater than 1 × 10−5 , some small timing improvements may
be noted. The drastic cost increases of Fig. 9, however, are not apparent in those cases but
do appear when the tolerance is 1 × 10−5 ; loosely supporting the previous explanation for
the large relative time increases. Even with the larger relative timings, Fig. 10b presents
time-step convergence studies like those in Fig. 7 and no dependence of the solution quantity
on convergence tolerance is noted.


                                                                                                       100

                 1.4
                                                                                                       10-1




                                                                             ((|w6 −w6 |)/w6 ) = (-)
                 1.2                                                                     tf            10-2
                                                                                         t




 Rel. Time (-)
                                                                                 ref
                                                                                                       10-3
                 1.0
                                                                                 ref
                                                                                                       10-4

                                                                                  num
                 0.8                                                                                   10-5
                                                                                                                Tol. = 1.0 ×10−9         Tol. = 1.0 ×10−6
                        Tol. = 1.0 ×10−8          Tol. = 1.0 ×10−6                                     10-6     Tol. = 1.0 ×10−8         Tol. = 1.0 ×10−5
                 0.6
                        Tol. = 1.0 ×10−7          Tol. = 1.0 ×10−5                                              Tol. = 1.0 ×10−7
                                                                                                       10-7 1
                  101                       102                      103                                  10                 102                            103
                                     Time Step, ∆t (s)                                                               Time Step, ∆t (s)
                             (a) Relative Timings                            (b) Time convergence with 8 element through thick-
                                                                             ness mesh

Figure 10: Impact of constitutive model convergence tolerance on (a) relative simulation
time and (b) time-step convergence for the “New” integration scheme with β = 1.0.
Distribution                                 –20–                          November 16, 2017

4   Conclusion
Continuum constitutive sintering models are needed to predict the response of different ge-
ometries through the sintering process. As such, efficient and accurate implementations of
these models represent a potent tool for the design and analysis of corresponding manufac-
turing stages. One common example of this class of macroscale phenomenological sintering
formulation is the Skorohod-Olevsky viscous sintering (SOVS) model. Existing numerical
implementations rely on a semi-implicit scheme developed for a liquid-stage sintering model
of McHugh-Riedel [9]. A fully implicit scheme represents a potentially enabling capability by
increasing accuracy while reducing cost by requiring lower temporal and spatial discretization
of global boundary value problems.

Such an implicit scheme was proposed and implemented here. Verification of the model was
performed via simple constitutive-level problems and improved accuracy was noted versus
the comparable existing implementation. The bilayer bar problem of Argüello et al. [12]
was then revisited and the performance of both the existing and new implementations was
investigated. Through such exercises, it was shown that the new implicit scheme can resolve
both global deformation and detailed field responses with reasonable mesh and time-step
discretizations. Importantly, these efforts demonstrated that the sintering process can be
captured with affordable simulation cost.

With respect to performance, the new implicit scheme shows improved accuracy, in terms
of both deformation and stress, versus the previous semi-implicit approach. The increased
fidelity does come with higher computational costs of ≈10-30%. Given the improvement
in accuracy, however, the longer simulation times are deemed acceptable. Achieving such
performance necessitates using a backward Euler integration scheme in time reflected via an
integration parameter of β = 1.0. Results presented here showed that although deformation
may be resolved with a value of β = 0.5, unstable, oscillatory responses in stress were noted
that are not only undesirable but also non-physical. As such, only the use of β = 1.0 can
be recommended until additional investigations on the stability properties of the integration
scheme can be undertaken and implemented.

Bearing these results in mind, improvements in both physical fidelity and numerical efficiency
may be achieved through additional studies. With respect to the former, a variety of ex-
tensions to the SOVS model have been proposed incorporating Arrhenius’ type temperature
dependence in the viscosity and/or introduction of the grain size as a variable (e.g. [11, 12]).
In terms of the latter, investigating and understanding the stability issue could enable opti-
mal selection of integration parameters for accuracy and help in selecting appropriate spatial
and temporal discretizations. Similarly, rigorous convergence studies of different boundary
value problems using energy norms could further such understanding. Regardless, the cur-
rent work represents an important first step in implementing macroscale constitutive models
essential for sintering.
Distribution                                –21–                          November 16, 2017

Acknowledgements
Sandia National Laboratories is a multimission laboratory managed and operated by Na-
tional Technology and Engineering Solutions of Sandia, LLC., a wholly owned subsidiary of
Honeywell International, Inc., for the U.S. Department of Energy’s National Nuclear Security
Administration under contract DE-NA0003525.


Bibliography
[1] M. N. Rahaman, Sintering of Ceramics, CRC Press, Boca Raton, FL, 2008.

[2] T. Kraft, H. Riedel, Numerical simulation of solid state sintering; model and application,
    Journal of the European Ceramic Society 24 (2004) 345–361.
[3] M. Reiterer, T. Kraft, H. Riedel, Manufacturing of a gear wheel made from reaction
    bonded alumina – numerical simulation of the sinterforming process, Journal of the
    European Ceramic Society 24 (2004) 239–246.
[4] C. Maruccio, P. Bene, A. Gerardi, D. Bardaro, Integration of CAD, CAE, and CAM pro-
    cedures for ceramic components undergoing sintering, Journal of the European Ceramic
    Society 36 (2016) 2263–2275.
[5] M. W. Reiterer, K. G. Ewsuk, An analysis of four different approaches to predict and
    control sintering, Journal of the American Ceramic Society 92 (7) (2009) 1419–1427.
    doi:10.1111/j.1551-2916.2009.03009.x.
[6] V. Tikare, M. Braginsky, E. A. Olevsky, Numerical simulation of solid-state sintering:
    I, sintering of three particles, Journal of the American Ceramic Society 86 (1) (2003)
    49–53.
[7] M. Braginsky, V. Tikare, E. Olevsky, Numerical simulation of solid state sintering,
    International Journal of Solids and Structures 42 (2005) 621–636.
[8] E. A. Olevsky, V. Tikare, T. Garino, Multi-scale study of sintering: a review, Jour-
    nal of the American Ceramic Society 89 (6) (2006) 1914–1922. doi:10.1111/j.1551-
    2916.01054.x.
[9] P. E. McHugh, H. Riedel, A liquid phase sintering model: application to Si3 N4 and
    WC-Co, Acta Materialia 45 (7) (1997) 2995–3003.
[10] E. A. Olevsky, Theory of sintering: from discrete to continuum, Materials Science and
     Engineering R23 (1998) 41–100.
[11] M. W. Reiterer, K. G. Ewsuk, J. G. Argüello, An Arrhenius-type viscosity function to
     model sintering using the Skorohod-Olevsky viscous sintering model within a finite-
     element code, Journal of the American Ceramic Society 89 (6) (2006) 1930–1935.
     doi:10.1111/j.1551-2916.01041.x.
Distribution                                  –22–                          November 16, 2017

[12] J. G. Argüello, M. W. Reiterer, K. G. Ewsuk, Verification, performance, validation,
     and modifications to the SOVS continuum constitutive model in a nonlinear large-
     deformation finite element code, Journal of the American Ceramic Society 92 (7) (2009)
     1442–1449.
[13] T. T. Molla, D. W. Ni, R. Bulatova, R. Bjørk, C. Bahl, N. Pryds, H. L. Frandsen, Finite
     element modeling of camber evolution during sintering of bilayer structures, Journal of
     the American Ceramic Society 97 (9) (2014) 2965–2972. doi:10.1111/jace.13025.
[14] M. Ortiz, E. P. Popov, Accuracy and stability of integration algorithms for elastoplastic
     constitutive relations, International Journal for Numerical Methods in Engineering 21
     (1985) 1561–1576.
[15] M. Ortiz, J. C. Simo, An analysis of a new class of integration algorithms for elastoplastic
     constitutive relations, International Journal for Numerical Methods in Engineering 23
     (1986) 353–365.
[16] A. Pérez-Foguet, F. Armero, On the formulation of closest-point projection algorithms
     in elastoplasticity – part II: Globally convergent schemes, International Journal for
     Numerical Methods in Engineering 53 (2002) 331–374.
[17] W. M. Scherzinger, A return mapping algorithm for isotropic and anisotropic plastic-
     ity models using a line search method, Computer Methods in Applied Mechanics and
     Engineering 317 (2017) 526–553.
[18] B. T. Lester, W. M. Scherzinger, Trust-region based return mapping algorithm for
     implicit integration of elastic-plastic constitutive models, International Journal for Nu-
     merical Methods in Engineering 112 (2017) 257–282. doi:10.1002/nme.5515.
[19] M. Ortiz, P. M. Pinsky, R. L. Taylor, Operator split methods for the numerical solution
     of the elastoplastic dynamic problem, Computer Methods in Applied Mechanics and
     Engineering 39 (1983) 137–157.
[20] D. Peirce, C. F. Shih, A. Needleman, A tangent modulus method for rate dependent
     solids, Computers & Structures 18 (5) (1984) 875–887.
[21] J. Simo, T. Hughes, Computational Inelasticity, Vol. 7 of Interdisciplinary Applied
     Mathematics, Springer-Verlag, New York, NY, 1998.
[22] J. Nocedal, S. J. Wright, Numerical Optimization, 2nd Edition, Springer Series in Op-
     erations Research and Financial Engineering, Springer Science+Businees Media, New
     York, NY, 2006.
[23] Sierra/SM Development Team, Sierra/SM 4.40 user’s guide, SAND Report 2016-2707,
     Sandia National Laboratories, Albuquerque, NM and Livermore, CA (2016).
[24] O. C. Zienkiewicz, I. C. Cormeau, Visco-plasticity – plasticity and creep in elastic solids
     – a unified numerical solution approach, International Journal for Numerical Methods
     in Engineering 8 (1974) 821–845.
Distribution                               –23–                         November 16, 2017

[25] I. Cormeau, Numerical stability in quasi-static elasto/visco-plasticity, International
     Journal for Numerical Methods in Engineering 9 (1975) 109–127.
[26] T. J. R. Hughes, R. L. Taylor, Unconditionally stable algorithms for quasi-static
     elasto/visco-plastic finite element analysis, Computers & Structures 8 (1978) 169–173.
[27] J. C. Simo, S. Govindjee, Non-linear B-stability and symmetry preserving return map-
     ping algorithms for plasticity and viscoplasticity, International Journal for Numerical
     Methods in Engineering 31 (1991) 151–176.
Distribution                           –24–     November 16, 2017

Internal Distribution:

MS-0346   K. Ford                   Org. 1556
MS-0523   K. Ewsuk                  Org. 2631
MS-0836   M. Martinez               Org. 1516
MS-0840   J. Bishop                 Org. 1554
MS-0840   E. Corona                 Org. 1554
MS-0840   H. E. Fang                Org. 1554
MS-0840   B. Lester                 Org. 1554
MS-0840   K. Long                   Org. 1554
MS-0840   B. Reedlunn               Org. 1554
MS-0840   W. Scherzinger            Org. 1554
MS-0845   J. Thomas                 Org. 1542
MS-0878   D. Kammler                Org. 2585
MS-1318   B. van Bloemen Waanders   Org. 1441
MS-1321   V. Tikare                 Org. 1444
MS-1411   F. Abdeljawad             Org. 1864
MS-9042   A. Brown                  Org. 8259
