                                      LLNL-JRNL-820428




Towards understanding particle
rigid-body motion during
solid-state sintering


R. P. SHI, M. Wood, T. W. HEO, B. Wood, J. C.
Ye


March 11, 2021


Journal of the European Ceramic Society
Disclaimer

This document was prepared as an account of work sponsored by an agency of the United States
government. Neither the United States government nor Lawrence Livermore National Security, LLC,
nor any of their employees makes any warranty, expressed or implied, or assumes any legal liability or
responsibility for the accuracy, completeness, or usefulness of any information, apparatus, product, or
process disclosed, or represents that its use would not infringe privately owned rights. Reference herein
to any specific commercial product, process, or service by trade name, trademark, manufacturer, or
otherwise does not necessarily constitute or imply its endorsement, recommendation, or favoring by the
United States government or Lawrence Livermore National Security, LLC. The views and opinions of
authors expressed herein do not necessarily state or reflect those of the United States government or
Lawrence Livermore National Security, LLC, and shall not be used for advertising or product
endorsement purposes.
       Towards understanding particle rigid-body motion during solid-state sintering
              Rongpei Shi*, Marissa Wood, Tae Wook Heo, Brandon C. Wood, Jianchao Ye

Materials Science Division, Lawrence Livermore National Laboratory, Livermore, CA 94550,

USA.


*Corresponding E-mail: shi7@llnl.gov


Abstract
A quantitative understanding of particle rigid body (RB) motion that inherently accompanies grain
boundary (GB) diffusion is highly desirable to understand and control the dynamic interplay between
coarsening and densification during solid state sintering. By computer simulation using a multi-phase-field
approach, we analyze systematically the roles played by each of these processes at different stages of the
shrinkage of the internal pore in a three-particle green body as a function of particle size as well as
thermodynamic and kinetic factors of interfaces. We demonstrate that particle RB translation promotes both
neck growth, and pore rounding and shrinkage. Moreover, the forces acting at GBs and pulling neighboring
particles towards one another dynamically evolve as particles fuse. In contrast, particle RB rotation has no
contribution to pore shrinkage. The translation force acting on an individual particle varies with not only
its size, but also the number and sizes of its neighboring particles.

Keywords: sintering, phase-field modeling, microstructure stability, coarsening, densification




                                                       1
1. Introduction
Sintering is a processing technique for producing density-controlled materials and components from metal
or ceramic powders by applying thermal energy [1]. Although practiced for over 28,000 years, sintering
has continually found new applications [2-4]. For example, new energy systems, such as solar cells [5] and
nuclear reactors[6], are critically contingent on sintered structures. Other examples include the fabrication
of dental crowns and bridges using additive computer-driven sintering routes [7], and the production of
porous tissue scaffolds for biomedical implants using custom laser sintering[8]. Most recently, there has
been considerable interest and effort in pushing forward the sintering of thin printed electronic structures,
thermoelectric junctions and long-lasting oil and gas drilling tools (e.g., bonded sintered diamond and
cemented carbides[9]). Finally, sintering is a key step in the development of ceramic-based solid-state
electrolytes that are critical for new batteries with improved energy efficiency and safety [10, 11]. There is
no doubt that the applications of sintering in the fabrication of advanced materials for both structural and
functional applications will continue to expand for many years to come [12]. Consequently, a fundamental
understanding of sintering mechanisms and the processing/microstructure relationship is highly desirable
for engineering desired microstructures for optimal properties targeting specific applications.

Sintering is driven by the reduction of surface free energy of a consolidated mass of particles and results in
a redistribution of material in the contact surfaces between powder particles [1, 13, 14]. During sintering,
the microstructure progression goes from particles in contact to a dense, nearly pore-free compact. The
bonding process dynamically interacts with the continuously evolving microstructure via several concurrent
mass transport processes. Transport mechanisms detail the paths by which the atoms move upon sintering.
Since pores are large accumulations of vacancies, transport mechanisms describe vacancy migration and
annihilation. Specifically, vacancies and atoms move along particle surface (i.e., surface diffusion), across
pores (i.e., vapor transport through evaporation and condensation), along grain boundaries (GBs) (i.e., GB
diffusion), and through the lattice (volume diffusion), as is schematically illustrated in Fig. 1(a) for a system
of three particles during sintering [1]. In addition, vacancies may couple with dislocations via plastic flow
and dislocation climb.

Transport mechanisms during sintering can be classified into two categories [1, 13, 15]: surface transport
and bulk transport. The distinction is made based on whether or not the mass transport leads to densification.
Surface transport mechanisms lead to neck growth without a change in particle spacing (i.e., no
densification, Fig. 1(b)) and thus are non-densifying in that the mass flow originates and terminates at the
particle surface. In other words, the atoms are rearranged with no annihilation of vacancies involved. Vapor
transport, surface diffusion and lattice diffusion from the particle surfaces to the neck (see mechanisms 1,
2, and 3 in Fig. 1(a)) are the major contributors to surface transport-controlled sintering. By contrast, bulk


                                                       2
transport mechanisms promote not only neck growth but also densification (see Fig. 1(c)). The paths involve
vacancy flow from the neck surface to the interparticle GB, which produces densification since a layer of
atoms moves in the opposite direction to the contact between the particles, thereby allowing the centers to
approach each other as the sintering bond grows. GB diffusion and lattice diffusion from the GB to the pore
(see mechanisms 4 and 5) are the most important densifying mechanisms in polycrystalline ceramics.
Plastic flow by dislocation motion (see mechanism 6) also leads to neck growth and densification but is
more common in the sintering of metal powders. Clearly, GBs are the source of materials transport for
densification in crystalline powder compacts and GB diffusion appears to dominate the densification of
many crystalline materials.

A cooperative GB accommodation of rigid-body motion is implied in the densifying path. Densification
results from vacancy annihilation at GBs that act as a vacancy sink. The chemical potential of an atom is
higher at GBs than at neck surfaces (which have higher negative curvatures), leading to a diffusional flux
of atoms from GBs to nearby neck regions. This is equivalent to a vacancy flux directed to the GB regions
under the assumption that vacancies are the only type of point defects present in the system. The over-
saturated vacancies are then annihilated by dislocations at GBs, producing an effective force that pulls
neighboring particles toward one another through rigid-body (RB) translation and rotation. The approach
of neighboring particle centers through RB motion reduces interparticle spacing and thus plays an important
role in the densification of powder compacts.

It is well known that sintering involves competition between the coarsening and densification of particles.
Surface diffusion dominates at early stages of sintering and causes coarsening and neck growth without
densification, whereas GB and bulk diffusion are more important at the intermediate stage or at high
temperature, leading to densification. As such, quantification of the effect of particle RB motion
accompanying GB diffusion and its influence on the interplay between coarsening and densification is a
prerequisite to develop a comprehensive understanding of the physics underlying mass transport during
sintering and to achieve better control of the sintering process. However, due to the dynamic interplay
between the evolution of a heterogeneous microstructure (morphology and spatial distribution of solid
grains and pores) and mass transport along the various paths mentioned above, it remains challenging to
develop a quantitative understanding of the influence of particle RB motion by experimental study alone.
A physics-based sintering model must accurately capture all stages of sintering, as well as the transitions
from one to another. This requires incorporating a variety of concurrent physical processes mentioned
above. Nevertheless, most of the existing theoretical models for solid–state sintering subdivide the
treatments into specific combinations of the sintering stages and mass transport mechanisms[16], such as



                                                    3
surface diffusion during initial stage sintering or GB diffusion during intermediate stage sintering. Thus,
these models are incapable of capturing the influence of particle RB motion at various stages of sintering.

Based on gradient thermodynamics, the phase-field approach (also called the diffuse-interface approach)
offers an ideal framework to deal rigorously and realistically with these challenges [6, 7, 17-27]. In this
approach, the total free energy (including the chemical, interfacial energy, and elastic strain energy if there
is any) of an arbitrary heterogeneous system is formulated as a function of both the local chemical and
structural states and their spatial variations (gradient)[28]. Microstructure evolution is driven by the
reduction of total free energy through diffusion and structural relaxation and is described by the spatial and
temporal evolution of the phase fields. One appealing feature of this method is that the various diffusion
paths involved in sintering can be naturally taken into account by the dependence of the diffusivities on the
microstructure features of the powder compact through phase-field variables without a need to explicitly
track the interfaces, including surfaces and GBs[17]. The contributions from particle RB motion to mass
flux can also be accounted for by introducing advection terms in both the Cahn–Hilliard nonlinear diffusion
equation for conserved density fields and the time-dependent Ginzburg–Landau (i.e., Allen–Cahn)
structural relaxation equation for non-conserved structural order parameters [17, 25, 29]. Several variants
of phase-field model for solid-state sintering have been formulated and applied to study microstructure
evolution and densification during different types of sintering. Insights from phase-field simulations of
sintering pave the way for a better understanding of solid-state sintering [20-22, 25, 26], yet details about
the role of particle RB translation and rotation at various stages of sintering and their individual and
combined contributions compared with non-densifying mass transport mechanisms remain unclear.

Herein, by using a multi-phase-field model, we analyzed quantitatively, for the first time, the individual
effects from particle RB motion (including translation and rotation) on microstructure evolution and
densification kinetics at various stages of sintering as a function of particle size. It is found that particle RB
translation leads to a faster densification (by promoting neck formation while preserving driving force for
further neck growth and pore(s) elimination). In contrast, RB rotation has no influence on densification of
spherical powder particles. RB translation dominates at the beginning and the initial intermediate stages of
sintering. Smaller particles enable faster sintering due to enhanced RB particle motion.

The rest of paper is organized as follows: In Section 2, a three-dimensional (3D) multi-phase-field model
is formulated. In Section 3, the model is employed to investigate the details of the entire sintering process
and to identify the relative contributions from particle RB motion (translation and rotation) to
microstructure evolution and densification at various stages of the sintering, as well as their dependence on
powder size. In Section 4, the roles played by each of these mass transport mechanisms and their interplay
at different stages during sintering are analyzed. The main findings are summarized in Section 5.

                                                        4
2. Methods
2.1. Multi-phase-field model for sintering
A multi-phase-field (MPF) model is formulated to gain a better understanding of the mass transport and
microstructure evolution during sintering. As a generalized approach to treat multiple (N > 2) coexisting
phases, the multi-phase-field (MPF) method is capable of treating an arbitrary number of individual phases
that interact at triple or higher order junctions [28, 30-33]. An arbitrary sintering microstructure consists of
a mixture of grains of solid phase and pores of vapor phase in a powder pellet and can be characterized by
a density field 𝜌(𝐫) representing the relative mass density, and (𝑁 + 1) long-range order (LRO) parameter
fields. In MPF framework, each solid particle is assumed to be a crystalline grain with an unique orientation
and is assigned a unique LRO, 𝜙! (𝐫) (𝛼 = 1 … 𝑁), where 𝑁 denotes the total number of particles in a
green body [17, 29, 34]. The spatial distribution of the surrounding vapor phase is described by a specific
LRO namely 𝜙!"#$% (𝐫). The phase fields, {ϕ& }, define local volume fractions of all the phases present
and, by definition, follow an additional constraint ∑'$%
                                                     &"% ϕ& (𝐫) = 1 at any given grid point in the

computational domain [28]. The bracket denotes the ensemble of all phases. 𝐫 denotes the spatial
coordinate.

The total free energy functional is an integral of the bulk chemical free energy density, 𝑓 ()*+ , and the
interfacial energy density, 𝑓 ,-./ , over the system volume:

                                  ℱ(𝜌, {𝜙! }) = ∫ 𝑑𝐫 9𝑓 ,-./ ({𝜙! }) + 𝑓 ()*+ (𝜌, {𝜙! }):                   (1)

The bulk chemical free energy density is given by
                                  𝑓 ()*+ (𝜌, {𝜙! }) = ∑'$%
                                                       &"% ϕ& (𝐫)f& [𝜌(𝐫)]                                  (2)
where f! [𝜌(𝐫) ]represents the free-energy density of the 𝛼 "# phases given by
                                            f! [𝜌(𝐱)] = ∆𝑓$ 𝑉%&' [𝜌 − 𝜌($ ])                                (3)
                             $
with 𝜌($ = 1(𝛼 = 1 … 𝑁) and 𝜌(*+,' = 0 for the solid and vapor phases, respectively. Note that
the free energy density 𝑓 .#/0 (𝜌( , {𝜙( }) has a minima at 8𝜌(*'…+ = 1, 𝜙( = 1, 𝜙23( = 09 and
8𝜌(*+,' = 0, 𝜙(*+,' = 1, 𝜙23( = 09 for the solid and vapor phases, respectively. Such a free
energy density provides an equilibrium state corresponding to a solid phase of crystalline grains
of different crystallographic orientations and a vapor phase of both internal pores and the
surrounding atmosphere. ∆𝑓$ is a constant and 𝑉% is the molar volume (assumed to be a constant).
Based on the gradient thermodynamics [35], the interfacial energy density is defined by the gradients of the
phase-fields and the potential functions:
                                                         '$%      0
                                  𝑓 ,-./ ({ϕ& }) = ∑'$%         !"
                                                    &"% ∑34& >− 2 ∇ϕ& ∙ ∇ϕ3 + ω&3 Cϕ& ϕ3 CD                 (4)

                                                       5
where κ&3 and ω&3 are the gradient energy coefficients of and potential energy humps across the interface
between the 𝛼 and 𝛽 phases, and they together determine the interfacial energy σ&3 and boundary width
Λ&3 .

The temporal and spatial evolution of the density and phase fields are governed by Cahn-Hilliard
generalized diffusion equation and the time-dependent Ginzburg-Landau equation (Allen-Cahn),
respectively, both of which are further modified by introducing an advection term accounting for the
contribution from particle rigid-body motion. Such a treatment essentially separates the mass flux into two
distinct contributions from diffusion[17], 𝐉 𝐝𝐢𝐟𝐟 , and rigid-body motion, 𝐉 𝐚𝐝𝐯 , in the continuity equation as
follows:

                                  :;                                               <=
                                        = −∇ ⋅ (𝐉 𝐝𝐢𝐟 + 𝐉 𝐚𝐝𝐯 ) = ∇ ⋅ K𝐷(𝜙, 𝜌)∇         M − ∇ ⋅ N𝜌 𝐯 𝐚𝐝𝐯 P   (5)
                                   :.                                              <;
                                             :>!       %   #!"    &' &*
                                              :.
                                                   "? ∑,
                                                       "-. % A
                                                           $
                                                                    ? B?∇⋅E>) 𝐯)/01 F
                                                                 &() &+
                                                                                                             (6)

In Eq. (5), 𝐷 (𝜙, 𝜌) denotes the diffusivity and is a function of both 𝜙! and 𝜌 [17, 34]:

                                                                         #
                 𝐷 = ℎ(𝜌)𝐷GHIJ + [1 − ℎ(𝜌)]𝐷KLM + 4𝜌(1 − 𝜌)𝐷N + 4𝐷OG ∑#
                                                                      ! ∑PQ! 𝜙! 𝜙P                           (7)
where ℎ(𝜌) is an interpolation function [17],

                                             ℎ(𝜌) = 𝜌R (10 − 15𝜌 + 6𝜌2 )                                     (8)

which is used to distinguish the bulk solid phase from the vapor phase (a shape function), i.e., ℎ(𝜌) = 0 for
the vapor phase and ℎ(𝜌) = 1 for the solid phase. 𝐷GHIJ , 𝐷KLM , 𝐷OG , and 𝐷N characterize diffusivities in
the solid bulk, in the vapor, along GBs and along the free surface, respectively. Note that Eq. (8) accounts
for various diffusion paths involved during sintering (i.e., along surface and GB, through bulk lattice and
vapor) without a need to explicitly track the locations of interfaces, including GBs and powder surfaces.
L&3 is the phase-field mobility (which characterizes the kinetics of structural changes) and W
                                                                                             N is the number
                                          W is different from 𝑁 in Eq. (6), which denotes the total number
of phases that locally coexist. Note that 𝑁
of phases/grains in the system.

2.2. Advective flux due to particle rigid-body (RB) motion
The advective flux, 𝐉 𝐚𝐝𝐯 ≡ 𝜌 𝐯 𝐚𝐝𝐯 , accounts for mass transport arising from RB motion of a local volume
element. Since RB motion consists of both translation and rotation, the advection velocity field, 𝐯 𝐚𝐝𝐯 , is
treated as a sum of the two contribution from all particles involved in the powder compact [17, 34]:

                                  𝐯 𝐚𝐝𝐯 = ∑𝜶 𝐯!LST = ∑𝜶[𝐯V (𝐫, 𝛼) + 𝐯W (𝐫, 𝛼)]                               (9)



                                                           6
where vV (𝐫, 𝛼) and vW (𝐫, 𝛼) represent the velocity fields associated with the translation and rotation of the
𝛼th particle which have been respectively formulated as follows:

                                                        X
                                           𝐯V (𝐫, 𝛼) = Y(!)
                                                         2
                                                            𝐅(𝛼)𝜙(𝐫, 𝛼)                                    (10)

                                               X
                                  𝐯W (𝐫, 𝛼) = Y(!)
                                                3
                                                   𝐓(𝛼) × [𝐫 − 𝐫\ (𝛼)]𝜙(𝐫, 𝛼)                              (11)

where 𝐾V and 𝐾W are the mobilities of the particle translational and rotational movement, respectively.
𝑉(𝛼) ≡ ∫ 𝜙(𝐫, 𝛼)d𝟑 𝐫 defines the volume of the 𝛼 .) particle, and 𝐫\ (𝛼) ≡ ∫ 𝐫 ⋅ 𝜙(𝐫, 𝛼)d𝟑 𝐫⁄𝑉(𝛼)
represents the center of mass of the 𝛼 .) particle. It is worth noting that both force-velocity formulae of Eqs.
(10) and (11) assume an inverse proportionality to the particle volume to ensure a law of inertia for the
whole powder compact, i.e., the center of the mass of the powder compact does not change. This applies to
free sintering (i.e., without constraint) as we consider in the current study.

𝐅(𝛼) and 𝐓(𝛼) are the translational and torque forces acting on the 𝛼 .) particle about its mass center and
can be respectively formulated as:

                                           𝐅(𝐫, 𝛼) = ∫ d𝐅(𝐫, 𝛼)                                            (12)

                                  𝐓(𝐫, 𝛼) = ∫[𝐫 − 𝐫\ (𝐫, 𝛼)] × d𝐅(𝐫, 𝛼)                                    (13)

d𝐅(𝐫, 𝛼) represents the density of an effective local force acting on the GB of the 𝛼 .) particle, which can
be formulated in terms of the phase field order parameters as follows: (the effective force at GBs is caused
by the mass density change at GBs)

                          d𝐅(𝐫, 𝛼) = 𝜅 ∑PQ!(𝜌 − 𝜌* )〈𝜙(𝛼)𝜙(𝛽)〉[∇𝜙(𝛼) − ∇𝜙(𝛽)]d𝟑 𝐫                          (14)

where 𝜌* is a constant characterizing the equilibrium value of mass density at a GB. Note that the force
originates from the variation of mass density with respect to 𝜌* and vanishes if 𝜌 = 𝜌* . 𝜅 is a stiffness
constant that correlates the force magnitude to the vacancy over-saturation at GBs that causes density
variation.

Eq. (14) essentially serves as a mathematical device that connects neighboring grains with a layer of “elastic
glue” that maneuvers to maintain an equilibrium mass density at GBs [17]. Consequently, the neighboring
particles could be either pulled closer or pushed further apart according to the mass density variation at
their mutual GBs. Eq. (14) has two key features: The first feature is the threshold operation 〈𝜙(𝛼)𝜙(𝛽)〉
employed to identify the GB region between the 𝛼 .) and 𝛽.) particles through LROs, which is formulated
as:


                                                       7
                                                 1, if 𝜙(𝛼)𝜙(𝛽) ≥ 𝑐,
                                   〈𝜙(𝛼)𝜙(𝛽)〉 = d                                                             (15)
                                                   0, otherwise

where 𝑐 is a critical value in identifying GBs through the product between 𝜙(𝛼) and 𝜙(𝛽). Such operation
excludes the region around the neck surface where the value of 𝜙(𝛼)𝜙(𝛽) does not completely vanish
while 𝜌(𝐫) significantly drops below the equilibrium value. The second feature is the gradient operation,
∇𝜙(𝛼) − ∇𝜙(𝛽), that ensures an action-reaction law between any pair of neighboring particles indexed by
𝛼 and 𝛽, (i.e., the local forces between neighboring particles indexed 𝛼 and 𝛽 are equal in magnitude but
opposite in direction).

2.3. Simulation set-up
All simulations were performed using a system having a volume of 96∆x × 96∆y × 96∆z with the spatial
step size ∆x = ∆y = ∆z = 𝑙^ = 25 𝑛𝑚 unless mentioned otherwise. Zero flux boundary conditions were
used along all three dimensions. Both GB and surface energies were assumed to be isotropic, and the
energy of each GB between any two different particles was further assumed to be the same. The energies
used in the current study for GBs between different particles and powder surfaces are 0.68 and 1.0 J⁄m2 ,
respectively unless mentioned otherwise. For the interface between arbitrary 𝛼 and 𝛽 phase, the boundary
width Λ&3 = 6𝑙^ . The gradient energy coefficients κ&3 and potential energy hump ω&3 can be computed
by κ&3 = 8𝜎!P Λ&3 ⁄𝜋 2 and ω&3 = 4 𝜎!P ⁄Λ&3 , respectively. Other model parameters include: the
reference chemical mobility in the simulation 𝐷GHIJ = 1.5 × 10?2^ mol2 ⁄(J ⋅ s ⋅ m) , ∆𝑓^ =
5 × 10_ J⁄mol (Eq. (3)) and molar volume 𝑉` = 1 × 10?a mR ⁄mol . As motivated by several studies[17,
21, 34], we consider GB and surface diffusion to be the active mass transport mechanisms by setting
N𝐷KLM , 𝐷GHIJ , , 𝐷OG , 𝐷N P = (10?% , 10^ , 10% , 102 )𝐷GHIJ . The governing equations (Eqs. (5) and (6)) are also
nondimensionalized with respect to the computational grid size 𝑙^ and energy barrier ∆𝑓. The values of
                                                WGHIJ = 1.50 × 10?2 , κ~!P = 7.78 × 10?2 and 5.32 ×
reduced parameters used in the simulations are: 𝐷
10?2 for surface and grain boundary, respectively. ω
                                                   • !P = 1.00 × 10?2 and 7.29 × 10?R for surface and
                                                                           WV and 𝐾
grain boundary, respectively. 𝜅 = 1, 𝜌* = 0.9816 and 𝑐 = 0.14 in Eq. (14). 𝐾      WW will be specified in
the Results section. 𝐿ƒ&3 is set to 1.08 to guarantee a diffusion-controlled sintering process.

We first started from a green body that consists of three spherical particles that have point contacts with
each other. Such a three-particle geometry is schematically shown in Fig. 2(c), where three equal-sized
spherical particles are centered at the vertices of an equilateral triangle located in the YZ plane through the
center of the 3D simulation box. The radius of each particle is characterized by 𝑅! = 𝑅 (𝛼 = 1 … 3). Such
a spatial arrangement of the three particles leads to an internal pore with three cusps (a starting triangular



                                                        8
shape shaded in gray, Fig. 2(d)). The sintering kinetics can be monitored by tracking the temporal evolution
of the internal pore shrinkage metric, which is defined by:

                                                               b(V)
                                          Shrinkage = 1 − b(^)                                            (16)

where 𝐴(0) and 𝐴(𝑡) denote the cross-sectional areas of the pore (projected on the YZ plane through the
center of the simulation box) at time 0 and 𝑡, respectively.

3. Simulation results
In this section, the multi-phase-field model is employed to examine the individual physical processes (in
particular, surface and bulk mass transport) and their interplay that affects sintering neck growth, pore
shrinkage and densification kinetics. In view of the complex nature of the sintering process, we first
examine the surface and mass transport processes separately and then explore the consequence of their
interaction, as well as their powder size dependence.

3.1. Sintering without densification
We start by considering the sintering of three particles (with size 𝑅 = 0.45 𝜇𝑚) involving surface mass
transport processes alone. Note that grain boundary diffusion also operates in this case, but the attendant
particle RB motion is excluded. Figs. 3(a)-(d) (top row) show the morphological evolution of the three
particles and the internal pore in the middle of them during sintering. To better understand the mass
transport along each path above upon sintering, the spatial distribution and temporal evolution of the
diffusion flux 𝐉 𝐝𝐢𝐟𝐟 (𝐫) in 3D are shown in the second row (Figs. 3(e)-(h)), in which the diffusion fluxes are
visualized as red cones with their size proportional to the magnitude of the flux. The 2D contours of the
three particles (solid green lines at which the values of 𝜙c = 0.5, 𝑖 = 1 … 3) are also superimposed to
indicate the location of the surface and GBs (Figs. 3(e)-(h)). Moreover, the diffusion flux is also shown on
2D cross sections through the powder compact in the third row (Figs. 3(i)-(l)) in the YZ plane and in the
bottom row (Figs. 3(m)-(p)) in the XZ plane (both planes section through the center of the simulation box),
respectively. In the YZ plane, the sintering necks between any two neighboring particles can be clearly
seen, while in the XZ plane, only the sintering neck formed between particle 1 (in green) and particle 2
(red) is visible (see the upper particle in Figs. 3(m)-(p)). Also shown on two bisection planes are the
corresponding contours of the projected density fields (𝜌 = 0.5).

Sintering initiates at the point contacts between particles (Fig. 2(c)). The early stage of sintering is
characterized by the formation of sinter necks that bond these particles. The sinter necks are saddle surfaces
due to the presence of a mixture of both concave and convex curvatures (i.e., the sinter neck is concave
(curved inward), while the particle surface is convex (curved outward)). Spatial distribution of the diffusion


                                                        9
flux indicates that mass transport is most active near the powder surfaces close to sintering necks, followed
by along the GBs, in agreement with the findings from classical sintering theory as well as molecular
dynamics simulations of sintering processes[36]. In particular, diffusional flux is directed towards the
concave regions (i.e., necks, Fig.3(i)), leading to the formation of sintering necks with material transported
from the nearby convex particle surface. This occurs because the chemical potential of atoms below a
convex surface is higher than that of atoms below a concave surface. In the meantime, a GB emerges at the
contact plane (Fig. 3(e)). At this stage, the neck size is so small that each neck grows independently. As an
example, the neck between particles 1 and 2 (the upper circle in Fig. 3(m)) is still physically separated from
particle 3 (i.e., the circle on the bottom).

As sintering progresses, neighboring necks continue to enlarge and start to overlap with each other. The
GB area in the neck increases as the neighboring necks impinge (Fig. 3(f)). As can be seen from Fig. 3(n),
the contour lines (𝜌 = 0.5) at the bottom of the upper circle and the top of the lower one become elongated
towards each other and eventually merge to bind both circles (see Fig. 3(o)). During this stage, the pore is
still open but shrinks continuously. This occurs because a diffusion flux exists from GBs to the nearby pore
where the three necks meet (Figs. 3(j) and (k)), and GBs act as fast diffusion pathways. As a result, the
region where the GB emerges at a surface becomes smoother as well. By the final stage of sintering, the
spherical pore continues to shrink and eventually disappears, and a complete closure of the internal pore in
the YZ plane is reached. (see Figs. 3(d), 3(h) and 3(l)).

The simulation results in Fig. 3 clearly show that sintering involves a dynamic interplay between
microstructure evolution and mass transport processes. Coupled with the mass transport processes are the
various geometric stages (e.g., neck growth, pore rounding and shrinkage) traversed during sintering. The
spatial variation of curvature on the powder surface gives a chemical potential gradient that directs mass
flow into the sintering bond. The deposited atoms change the neck size and shape. In turn, the concomitant
reduction in curvature and surface area influences the flux, as can be seen from the reduced the magnitude
of the flux vector as sintering proceeds (Fig. 3(i)-(l)).

The temporal evolution of the pore shrinkage metric experiences two major changes in slope before
reaching a complete closure of the internal pore (Fig. 4(a)). The changes in slope indicate that the simulation
captures three different regimes and the transition from one to another during the sintering process. In
general, there is no clear distinction between sintering stages since the geometric progression varies from
point to point in the microstructure. However, based on Fig. 4(a), the whole pore shrinkage during sintering
can be divided into three overlapping stages: initial, intermediate, and final. The initial stage is characterized
by the formation of necks between particles (see Figs. 4(b)-(f)). In the intermediate stage, neighboring
grains impinge to round the pore in the middle, leading to progressive smoothing of its surface. The final

                                                       10
stage involves the closure of the internal pore. As will be further discussed in Section 4.3, each regime is
governed by different physical processes: The initial stage is dominated by surface relaxation, which is then
taken over by GB spreading in the intermediate stage. Moreover, the reduced magnitude of slope over the
three consecutive stages indicates increasingly slower kinetics as sintering proceeds.

It should be noted here that the closure of the internal pore is not caused by the densification between
particles wherein the inter-particle spacing is reduced. Instead, it is caused by the growth of the sintering
necks (i.e., GBs) between any two neighboring particles, which leads to the elimination of the internal pore.
To allow for pore shrinkage through particle densification, particle RB motion should be considered as
presented in the section below.

3.2. Sintering with densification through rigid-body motion of particles
In addition to shape change by non-densifying diffusion, each particle may move as a rigid body associated
with densifying mass transport through GB diffusion. Since particle RB motion consists of both translation
and rotation, their individual contributions to microstructure evolution and densification kinetics are
investigated separately in this section.

3.2.1. The role of particle translational motion

Figure 5 presents the results of particle translational motion. The 3D morphological evolution of three
particles and the internal pores upon reaching a complete closure of the internal pore (within 𝑡 = 0 − 3 𝑠)
are presented in the first column. Neck growth leads to an increase in the area of GBs between particle (and
contact angle (i.e., dihedral angle 2𝜙) at the triple-phase junctions as well as the shrinkage of the internal
pore, as can be seen from Figs. 5(a), (d) and (g). To analyze the influence of particle translational motion,
the spatial distribution and temporal evolution of the attendant advective flux in both 3D and 2D (XY cross-
section) are presented in the second and third column, respectively. The direction of advective fluxes within
each particle indicate that particle translational motion would lead the centers of each particle to approach
each other. Besides diffusional flux toward the internal pore through surface and GBs as mentioned in
Section 3.1, advective flux also moves mass inside the solid and deposits it in the pore (i.e., the flux bring
mass to fill the internal pore), thereby accelerating the shrinkage of the internal pore. As shown in Figs.
5(c), (f) and (i), owing to the substantial neck growth assisted by particle translational motion towards each
other, the internal pore quickly becomes spherical and closed within first three seconds, along with the
significant reduction in surface curvature as pointed out by the arrows. It is also found that the magnitude
of advective flux reduces as sintering proceeds, as indicated by the reduced sizes of both arrows (2D) and
cones (3D) over time. Thus, similar to non-densifying mass transport, the contribution from particle
translational motion varies with sintering stages and reduces as sintering progresses.


                                                     11
                                                                                                       WV s are
To further explore the influence of particle translation, the kinetics of pore shrinkage for different 𝐾
                       WV characterizes the mobility of particle translational motion (𝐾
compared in Fig. 6(a). 𝐾                                                               WV = 0 indicates the
                                                                                              WV > 0) shortens
absence of particle translation). Apparently, consideration of particle translational motion (𝐾
the time needed for a full collapse of the internal pore under otherwise identical conditions. In particular,
                    WV increases to a value of 0.5 but is relatively unchanged at larger 𝐾
𝑡d decreases as the 𝐾                                                                    WV s (Fig. 6(b)). The

plateau region indicates that the closure of the internal pore requires other cooperative physical process(es)
with particle translation as particles fuse (see discussion at Section 4.2).

Besides pore shrinkage kinetics, particle translational motion is also found to affect the morphological
                                                                                           WV = 0.5 and
evolution of the particles. Fig. 6(c) compares the 2D contour of the density (𝜌 = 0.5) for 𝐾
WV = 0.0. At the selected time moment (𝑡 = 3 𝑠), the internal pore has completely collapsed for 𝐾
𝐾                                                                                               WV = 0.5,
                                W = 0.0. In addition, the triple junction for 𝐾
while it still remains open for 𝐾                                             WV = 0.5 is less concave (i.e.,
                    W = 0.0. This comparison suggests that particle RB motion bring particles closer to
larger 2𝜙) than for 𝐾
each other and thus promotes sintering neck growth and the shrinkage of the internal pore.

In order to understand the varying magnitudes of advective flux during sintering (see the third column in
Fig. 5), we analyzed the density of the translational forces (i.e., 𝐅(𝐫, 𝛼) in Eq. (12) normalized by the
volume of the 𝛼 .) particle) that lead to particle translational motion. The result is shown in Fig. 6(e) for
                        WV s. Note that the forces acting on particles 1 and 2 have the same magnitude but
particle 3 at different 𝐾
different directions. It is seen that the force starts to develop (once the threshold value is reached and the
GB can be identified, see Eq. (15)) and increases sharply until reaching a maximum, and then decays and
eventually vanishes (which explains the reduced advective flux over time as shown in Figs. 5(c), (f) and
               WV , the maximum in the force density is reached at an early stage of sintering, as highlighted
(i)). For each 𝐾
by an open circle (Fig. 6(f)). The results indicate that the maximum force magnitude increases with
           WV , but it takes a longer time for the force to reach the maximum for a smaller 𝐾
decreasing 𝐾                                                                                WV . This occurs
because the velocity (i.e., the product of force and mobility as calculated by Eq. (10)) of particle translation
                                                                                                WV s (see Fig.
that brings the mass density at GBs to reach the equilibrium value 𝜌e is much faster for larger 𝐾
6(d)).

3.2.2. The role of particle RB rotation

In this section, the individual influence of particle RB rotation is considered by incorporating the advective
                                                                                                 WW s are shown
flux corresponding to rotation in Eqs. (5) and (6). The kinetics of pore shrinkage for different 𝐾
              WW characterizes the mobility of particle rotational motion ( 𝐾
in Fig. 7(a). 𝐾                                                             WW = 0 in the absence of particle
                                                                                WW . To validate this finding,
rotation). The densification kinetics appear to be independent of the choice of 𝐾


                                                      12
                                                                                          WW = 0), where 𝑡d
the influence of particle RB rotation on pore shrinkage kinetics is quantified by 𝑡d ⁄𝑡d (𝐾
        WW = 0) denote the time to reach a complete pore closure with and without considering rotation,
and 𝑡d (𝐾
                                                                    WW = 0) < 1 ) or suppress (if
respectively. Particle RB rotation would either enhance (if 𝑡d ⁄𝑡d (𝐾
        WW = 0) < 1) the pore shrinkage. The results are shown in Fig. 7(b) for different values of 𝐾
𝑡d ⁄𝑡d (𝐾                                                                                           WW , where
                                              WW = 0) from 1 is less than 2.5%, indicating that particle
the maximum deviation of the value of 𝑡d ⁄𝑡d (𝐾
rotation does not contribute to the shrinkage kinetics of the internal pore.

To explore the underlying physics of this finding, advection flux in 3D corresponding to particle RB rotation
at an intermediate time moment is visualized in Fig. 7(c). Additionally, the advective flux associated with
rotation is projected on three different XZ planes at different locations along the Y-axis (as indicated by the
three dashed lines in the YZ cross-section in Fig. 7(d)), which are shown from left to right Figs. 7(e-g). It
can be seen that the advective flux enters and exits the neck region with the same magnitude. In other words,
no net mass from the inside of the solid particle is deposited at the neck region or in the pores during particle
RB rotation. As a result, particle rotation does not contribute to the shrinkage of the internal pore. Note that
the advective flux due to particle rotation is normal to the YZ cross-section. Thus, the flux shown in the YZ
cross-section is the diffusional flux.

3.3. The influence of particle size on pore closure kinetics
One of the paradigms of sintering theory is that a reduction in particle size enhances the sintering kinetics
or reduces the sintering temperature. A great deal of independent experiments have demonstrated the strong
particle size dependence of sintering kinetics. However, the physical origins of the observed trends remain
incompletely understood in terms of the individual and combined contributions from non-densifying and
densifying mass transport processes. The size dependence of sintering kinetics has been primarily ascribed
to the increase in both the driving force (through changes in curvature) and kinetics (through decrease in
the length of diffusion path) associated with reduction in particle size, which both lead to faster sintering.
Even though it has been recognized that rigid-body motion plays a nontrivial role in the densification of
sintered powder pellets [17, 34], the particle size dependence of this effect is not yet completely understood.
In this section we demonstrate that beyond reproducing experimental trends, one advantage of the model is
the ability to discern which physical parameters dominate the observed behavior. Along these lines, we
systematically analyzed the individual roles of different mass transport mechanisms in sintering kinetics as
a function of particle size. Considering that particle rotation has no influence on pore shrinkage kinetics
(see section 3.2.2), only the contribution from particle translation is considered below.

First, the size dependence of the non-densifying mechanism is addressed. Fig. 8(a) shows the pore shrinkage
kinetics for three different powder sizes when the surface transport mechanism alone is operating. It is clear


                                                       13
that the magnitudes of the slopes for each stage of pore shrinkage increase with decreasing particle size. As
a result, 𝑡d decreases with reduced particle size.

It is noted that clusters of small particles reach final stage sintering first, while regions of large particles
might still be in the initial stage. For particles of 𝑅 = 300 𝑛𝑚, the growth of sintering necks continues
even after closure of the internal pore at 𝑡 = 2.0 𝑠 (see the comparison of density profile at 𝑡 = 2.0 and
10.0 𝑠 in Fig. 8(b)), which indicates that at this moment the neck size has not yet reached a thermodynamic
equilibrium. In contrast, for particles of 𝑅 = 600 𝑛𝑚, a complete closure of the internal pore is not
achieved even at 𝑡 = 16.0 𝑠 (see Fig. 8(d)). Instead, the pore shrinkage stagnates at a fraction of ~0.55
when the time reaches 𝑡 = 14 𝑠. Without a densifying mass transport mechanism operating, pore closure
can only be achieved if there exists neck growth. The stagnation of neck growth indicates that the neck size
has reached a thermodynamic equilibrium (i.e., 𝑋 = 2𝑅 sin 𝜙, see Fig. 1). Further migration of the grain
boundary would require an increase in its area, making the process energetically unfavorable. This is
supported by the observation that a much longer sintering time (e.g., 𝑡 = 40 𝑠) does not change either neck
size or the dihedral angle at the triple junction line.

In particular, the diffusion flux at an intermediate time point (𝑡 = 1.0 𝑠) is shown in Figs. 8(c) and 8(f) for
𝑅 = 300 𝑛𝑚 and 600 𝑛𝑚, respectively. Note that at the selected time, for the smaller particles sintering
has already reached its final stage, while for the larger ones sintering is still at its early stage (see Fig. 8(a)).
Thus, comparing the sizes of the arrows, we conclude that small particles sinter with enhanced diffusional
flux.

Second, Fig. 9(a) shows the pore shrinkage kinetics for three different powder sizes when non-densifying
and densifying mass transport mechanisms operate simultaneously during sintering. Compared with Fig.
8(a), particle translation promotes pore closure for all three different particle sizes. Pore closure is
completed within a shorter time for particles of size 𝑅 = 300 and 450 𝑛𝑚. Additionally, pore closure can
be achieved for 𝑅 = 600 𝑛𝑚 when particle RB translation operates during sintering. Fig. 9(b) demonstrates
temporal evolution of the translational force magnitude acting on particle 3 for different sizes. The most
significant variation of force occurs within [0~1] 𝑠 (Fig. 9(c)), in which the maximum in the force
magnitude for each particle size is highlighted as an open circle. Clearly, the maximum force magnitude
increases with decreasing particle size. As a result, the neighboring smaller particles are pulled towards one
another by the force with increased magnitude, leading to enhanced densification. This is also manifested
by the increased magnitude of the advective flux (larger arrow size) for smaller particles (see Figs. 9(d) and
(e) for a comparison of the advective flux for particles with two different sizes at a time moment indicated
by the vertical dashed line in Fig. 9(c)).


                                                          14
According to Eq. (10), the velocity for particle rigid-body motion among particles is inversely proportional
to the particle volume, rather than the particle size as for the diffusion flux. Our quantitative results clearly
indicate that the advective flux is more sensitive to the particle size than the diffusion flux (see the difference
in advective fluxes in Figs. 8c and 8f for particle sizes of 𝑅 = 300 𝑛𝑚 and 𝑅 = 600 𝑛𝑚 , respectively).

Finally, it is noted that the initial area of the internal pore in the three-particle green body is, 𝐴^ = √3𝑅2 −
𝜋𝑅2 ⁄4. Thus, 𝐴^ is proportional to the square of the radius and decreases with decreasing particle radius.
A smaller pore takes less time to be eliminated than a larger one.

In summary, there are three factors responsible for the observed dependence of sintering kinetics on particle
size (i.e., smaller particle sizes promote faster sintering). First, the diffusive flux (driven by the spatial
variation of curvature on the particle surface) is inversely proportional to the particle radius. Second, the
advective flux or velocity is inversely proportional to the particle volume, resulting in a larger advective
flux/velocity for a smaller particle (see Figs. 8c and 8d). Third, the initial pore size is directly proportional
to the square of the particle size, indicating that a smaller pore takes less time to be eliminated than a larger
one.

4. Discussion
Sintering involves multiple simultaneous physical processes, including diffusion along various paths and
particle rigid-body motions (translations and rotation) that are associated with GB diffusion and result in
densification. Coupled with these mass transport pathways are the various geometric stages that evolve
during sintering, including neck growth and the concomitant reduction in curvature and surface area, as
well as pore rounding, shrinkage and closure. The simulation results above clearly demonstrate that the
interplay among these processes varies with sintering stage as well as with particle size. Depending on the
relative contributions from these factors, the relationship between coarsening and densification can be
determined. The phase-field model naturally incorporates all of the above-mentioned processes and factors
during sintering within a unified formalism in a physically consistent way. Beyond reproducing the
experimental trends, one advantage of the model is the ability to allow for a quantitative understanding of
each of the processes at different stages of sintering.

4.1. The effect of surface diffusion and GB diffusion on pore shrinkage
We identify the individual roles of surface diffusion and GB diffusion in the process of pore closure by
systematically varying both thermodynamic (e.g., surface and GB energies) and kinetic (surface and GB
diffusivities) factors related to these two processes.




                                                         15
Figure 10(a) shows pore shrinkage kinetics for different surface diffusivities 𝐷f s, which are varied from
5.0 𝐷OG to 50 𝐷OG (i.e., 50.0 𝐷GHIJ to 500.0 𝐷GHIJ ) while keeping all other parameters unchanged. The
slopes (see Fig. 10(b) for the early stage) for each stage of pore shrinkage increase with increasing 𝐷f s,
thereby shortening 𝑡d . Fig. 10(c) summarizes 𝑡d for different 𝐷f s, which shows that as 𝐷g increases by a
factor of 10 (50.0 𝐷GHIJ to 500.0 𝐷GHIJ ), 𝑡d reduces by a factor of 8.7 (from 15.1 𝑠 to 1.7 𝑠). It is also noted
that 𝑡d decreases sharply as 𝐷N increases to ~100 × 𝐷GHIJ , but further reduction slows down at larger
values of 𝐷g s. This trend indicates that pore shrinkage kinetics are enhanced by fast surface diffusion and
that surface diffusion also requires other cooperative processes to achieve complete pore closure.

Figure 11 (a) shows pore shrinkage kinetics for different GB diffusivities 𝐷OG s, which are varied from
0.1 𝐷g to 3.0 𝐷g (i.e., 10.0 𝐷GHIJ to 300.0 𝐷GHIJ ) while keeping all other parameters unchanged. It can be
seen that the slopes for the initial stage seem to be independent of 𝐷OG (see Fig. 11(b)), indicating that this
stage is essentially dominated by surface diffusion (see Fig. 10(b) for a comparison). As sintering proceeds
to the intermediate stage, the differences in pore shrinkage kinetics start to develop, with larger slope
magnitudes for increasing 𝐷OG . Figure 11(c) summarizes 𝑡d as a function of 𝐷OG and shows that as 𝐷OG
increases by a factor of 30, 𝑡d decreases by a factor of 1.7. Thus, neck growth kinetics are much more
sensitive to surface diffusion (see Figs. 10(c) and 11(c) for a comparison).

Considering that sintering is driven by surface energy reduction and is accompanied by the formation of
sintering necks and thus the increase of grain boundary areas between particles, we further examine the
dependence of sintering kinetics on surface energy (𝜎f ) and grain boundary energy (𝜎OG ). Fig. 12(a) shows
the pore shrinkage kinetics for different 𝜎f values, which are increased from 1.0 × 𝜎OG to 2.2 × 𝜎OG while
keeping all other parameters unchanged. Similar to surface diffusivity, 𝑡d first decreases sharply with
increasing 𝜎g but further reduction is slowed down at larger values of 𝜎g s. In total, as 𝜎f increases by a
factor of 1.67 (from 1.32 𝜎OG to 2.20 𝜎OG ), 𝑡d decreases by a factor of 2.65 (from 9.32 𝑠 to 3.52 𝑠 ).
Besides pore shrinkage kinetics, surface energy 𝜎g also dictates the morphology of pores and grains. At
thermodynamic equilibrium, the forces must balance at the junction where the surfaces of the pores meet
the GB, which leads to 𝜎OG = 2𝜎g cos 𝜙, where 2𝜙 is the dihedral angle (see Fig. 1(b)). Clearly, 𝜙 becomes
larger for larger 𝜎g , as shown in Fig. 12(c), wherein the contours of the density field are compared for two
surface energies at 𝑡 = 10 𝑠 (note that the internal pore has not yet reached a complete closure at this time
point for 𝜎g = 1.0 × 𝜎OG ).

Fig. 13(a) shows the pore shrinkage kinetics for different GB energies, 𝜎OG , which are reduced from
1.00 × 𝜎g to 0.25 × 𝜎g . All other parameters are kept the same except that 𝜎g is increased from 0.68 to
1.00 J⁄m2 . The differences in pore shrinkage kinetics for different 𝜎OG values start to develop only when

                                                       16
sintering progresses into the intermediate stage. The increase of 𝜎g leads to much faster closure of the
internal pore as compared to the case in Fig. 12(c) wherein 𝜎OG = 1.0 × 𝜎g = 0.68 J⁄m2 . In total, 𝜎OG
increases by a factor of 4.0 (from 0.25 𝜎OG to 1.00 𝜎OG ), while 𝑡d increases by a factor of 2.68 (from
4.50 𝑠 to 12.05 𝑠). Clearly, 𝑡d is more sensitive to the increase of 𝜎g than to the reduction of 𝜎OG .

The parametric studies above make clear the variation of the dominant mechanisms with the stages of
sintering. The initial stage of pore shrinkage during sintering is characterized by neck growth. On the one
hand, the increasing thermodynamic driving force (i.e., surface energy) and kinetic mobility (i.e., surface
diffusivity) promote neck growth. On the other hand, the actual neck volume in the initial stage is relatively
small. As such, the thermodynamic and kinetic factors associated with grain boundaries have trivial
influence on pore shrinkage kinetics at this stage. As the sintering progresses and the GB area in the necks
increases while the surface area decreases, GB diffusion starts to overtake surface diffusion. In this stage,
reducing GB energy and increasing GB diffusivity promote neck growth. However, GB diffusion requires
cooperative surface diffusion, for example, to avoid building hillocks where the GB emerges at a surface.

4.2. The effect of non-densifying and densifying mass transport mechanisms on pore shrinkage
It is noticed that, in the absence of particle translation, a complete closure of the internal pore does not
occur when the particle size is large enough, e.g., 𝑅 = 600 𝑛𝑚 in the current study (see Figs. 8(a) and (g)).
In contrast, the presence of particle RB translation helps to close the internal pore under otherwise identical
conditions. This occurs because the densification promotes neck growth and thus preserves a high capillary
driving force for sintering. The difference in pore shrinkage behaviors emphasizes the importance in
accounting for the contribution from RB motion when evaluating the competition between coarsening and
densification during sintering.

                                                                     WV (i.e., the mobility of particle
It is also noted that the reduction in 𝑡d seems to be independent of 𝐾
                                          WV beyond 0.5. In order to evaluate the relative contribution from
translational motion) at larger values of 𝐾
non-densifying and densifying mass transport to pore shrinkage kinetics, computational experiments are
designed in which both surface and GB diffusivity are varied systematically while keeping all other
parameters the same. Fig. 14(a) shows the pore shrinkage kinetics for three different 𝐷g values in the case
   WV = 1.0. Like the previous case in Section 4.1, increasing 𝐷g increases the magnitude of the slope for
of 𝐾
each pore shrinkage stage, thereby reducing 𝑡d . Thus, the finding about the influence of surface diffusivity
𝐷g on pore shrinkage is still valid in the presence of particle RB motion. Note that the value of 𝐷g does not
change the magnitude of maximum translational force (Fig 14(c)). Instead, the reduced 𝐷g delays the time
it takes for the translational force to reach its maximum (Figs 14(c) and (d)). As a neck grows between two
particles in contact, there is a concomitant variation in mass density at the GB that results in translational


                                                      17
forces (see Eq. (14)) pulling neighboring particles closer to each other. Fast surface diffusion facilitates
mass transport and thus particle translation. It is clear that surface diffusion and particle translation are
complementary to each other in promoting neck growth. The former induces the variation of mass density
across the GBs between neighboring particles, which in turn generates forces that pull these particles closer
to each other. Also, the density of translational force becomes relatively small as the pore shrinkage moves
into its second stage wherein GB diffusion becomes more important.

                                                                                                    WV = 1.0.
Fig. 14(e) shows pore shrinkage kinetics for three different GB diffusivities, 𝐷OG , in the case of 𝐾
Similar to the absence of particle RB translation, pore shrinkage starts to be influenced by GB diffusion
only when it moves into the intermediate stage (see Fig. 14(f)). Different from surface diffusion, GB
diffusion affects neither the translational force nor its temporal evolution (Figs. 14(g) and (h)). This is the
                                    WV . For relatively small values of 𝐾
case for relatively large values of 𝐾                                   WV (see Fig. 6(a) and (d) for 𝐾
                                                                                                      WV =
0.01~0.1), however, the translational force can persist as the pore shrinkage goes into the intermediate
stage wherein GB diffusion becomes operative. Therefore, a large mobility of particle translation (e.g.,
WV = 1.0 in the current study) may help to bypass the initial stage, thereby reducing the coarsening or
𝐾
surface diffusion of particles and preserving a high capillary driving force for the subsequent sintering.

4.3. The influence of particle size asymmetry
The green body considered in all the simulations above consists of three identical spherical particles in
point contact with each other. A realistic green body contains a broad distribution of initial particle sizes
and a particle may be in contact with other particles of different sizes. Using the three-particle green body
as an example, we analyze how differences in particle size influence the RB motion between them. Along
this line, the radius of particle 3 is modified to be 𝑅R = 300 and 600 𝑛𝑚, while the radii of particles 1 and
2 are kept unchanged (𝑅% = 𝑅2 = 450 𝑛𝑚). Fig. 15(a) shows pore shrinkage kinetics for three different 𝑅R
values. Reducing 𝑅R alone increases the magnitude of the slope for each stage of pore shrinkage. As a
result, 𝑡d decreases from 4.11 𝑠 to 1.77 𝑠 as 𝑅R is reduced from 600 𝑛𝑚 to 300 𝑛𝑚. Fig. 15 (b) shows the
temporal evolution of the density of translational force acting on particle 3 with three different sizes. It can
be clearly seen that the maximum of force density (indicated by open circles) is larger for smaller particles.
In contrast, for the particles neighboring particle 3, the translational force (e.g. for particle 1 𝑅% = 450 𝑛𝑚)
increases with the size of its neighboring particle 3 (Fig. 15(c)), which is manifested by the increased arrow
size with increasing 𝑅R (see the comparison between Fig. 15(d) for 𝑅R = 300 and (e) for 𝑅R = 600 𝑛𝑚).

The difference in 𝑅R also modifies the direction of advective flux in particles 1 and 2 (Fig. 15(d) and (e)).
Thus, the value of 𝑅R affects both the magnitude and direction of the translational forces acting on its
neighboring particles. This finding suggests that the green body characteristics (e.g., particle size and


                                                      18
distribution) could be optimized to improve the sintering kinetics or reduce the sintering temperature, since
particle size distribution determines the number and size of neighboring particles for each particle and thus
the magnitude and direction of the translational force acting on it. The developed phase-field model is well
suited for identifying the optimum distribution(s).

The influence of particle size asymmetry on the particle rotational motion is also investigated and the results
are presented in Fig. 16. The radius of particle 3 is modified to be 𝑅R = 300 𝑛𝑚 while keeping the radii of
                                                                        WW is then varied from 0.01 to 10.0
the other two particles the same. The mobility of the rotational motion 𝐾
                                      WW s on pore shrinkage kinetics is summarized in Fig. 16(a). The
and the influence of the variation of 𝐾
                                 WW = 0) for different 𝐾
deviations of the values 𝑡d ⁄𝑡d (𝐾                     WW s from 1 fall within 2.5%-5%, indicating that for

spherical particle aggregates, particle RB rotation has no influence on sintering kinetics, regardless of the
particle size distribution.

4.4. Limitations of the model
All the simulations are performed for a green body that consists of three particles in point contact with each
other, and a single internal pore surrounded by the particles. However, a realistic green body is likely to
contain a large number of particles (and thus pores) with a broad distribution of sizes and shapes. As such,
the current study has ignored the process of grain growth (driven by the reduction of total grain boundary
energy), the pore-boundary interactions, and the pore-pore interactions, as well as their influence on the
dynamic interplay between densification and coarsening.

Besides particle size, it should be noted that there are many other processing parameters that influence
densification and coarsening, including packing configuration and density of the green body, temperature
profile (such as heating rate, sintering temperature and time duration, cooling rate), and the presence of
sintering agents. However, we expect that the essential physical mechanisms and the relationships identified
in our simplified model will not qualitatively change. As an example, we consider the sintering behavior of
a more realistic green body that contains 1024 particles (Fig. 17(a)) with the size distribution informed by
experimental measurements (Fig. 17(b)). Fig. 17(c) shows the temporal evolution of the translational forces
acting on three randomly selected particles. Particles 1 (Dark red) and 2 (Yellow) are located on the green
body surface while particle 3 is embedded in the green body interior. The results indicate that the
development of forces on these three particles follow the same trend as observed in Fig. 6(e) and 9(b). The
differences lie in several fluctuations in the force magnitude in the downhill portions of the three curves.
The fluctuations occur because in a realistic green body, a particle is in contact with more than two
neighboring particles that experience both coarsening and RB translation and thus a grain boundary could
be perturbated by grain growth and/or pore/GB interaction. A more detailed analysis of microstructure


                                                      19
evolution (that involves concomitant densification, pore rounding, and grain growth as shown in Figs 17(d)-
(f)) during sintering is forthcoming but is beyond the scope of this paper.

The densification of a sintering compact is accommodated by particles’ rigid body motion, which are
accounted for phenomenologically by introducing an advective mass flux with an adjustable parameter (i.e.,
mobility) that accounts for the time scale associated with particle RB motion. The mobilities (𝐾W and 𝐾V )
have been assumed to be isotropic and independent of grain boundary characters. The effect of GB
microstates on the defect-GB mediated particle RB motions and sintering kinetics are thus ignored in the
current study.

5. Conclusion
A multi-phase-field model has been developed to investigate the interplay between coarsening and
densification in solid-state sintering that considers simultaneously mass transport along different paths
(including surface diffusion, grain boundary (GB) diffusion, bulk diffusion, vapor transport) and
microstructure evolution (including neck growth, pore rounding and shrinkage) as well as the cooperative
rigid body (RB) motions (translation and rotation) of particles as they fuse. The simulation results have
shown clearly the entire process leading to the complete closure of the internal pore in a three-particle green
body, and demonstrated the couplings among diffusion along different paths, neck growth with attendant
increase of GB area, pore rounding and shrinkage, and particle RB motions involved in different stages of
the process. The relative contribution of each of the processes changes as the sintering progresses and the
interplay among them depends on both thermodynamic and kinetic factors of the interfaces (surface and
grain boundaries) as well as the particle size. Detailed findings include:

    1. The shrinkage of the internal pore consists of three consecutive stages: initial stage for neck
        formation, intermediate stage for neck growth (increase of GB area) and pore rounding, and the
        final stage for pore closure. Surface transport and GB transport dominate in the initial and
        intermediate stages, respectively.
    2. Particle RB translation promotes both neck growth and pore shrinkage by transporting mass from
        the grain interior to GB and pore regions.
    3. Particle RB translation forces dynamically evolve as the particles fuse and dominate at the initial
        and early intermediate stages of neck growth.
    4. The force acting on an individual particle varies with not only its size, but also the number and
        sizes of the neighboring particles.
    5. Particle RB rotation does not contribute to either neck growth or the shrinkage of the internal pore
        among spherical particles, since the associated advective mass flux enters and leaves the pore


                                                      20
        region with the same magnitude. This finding stands irrespective of particle size distribution, at
        least for spherical particles.
    6. Three factors are identified that contribute to enhanced sintering kinetics due to reduced particle
        size: initial pore size (area), diffusion flux, and advective flux due to particle RB translation. The
        first and last factors are inversely proportional to the square and cube of the particle size,
        respectively.
    7. Surface transport (e.g., surface diffusion) and particle RB motion cooperatively promote neck
        growth. The former initiates neck formation and growth, which in turn leads the latter to become
        operative, thereby enhancing further neck growth and preserving the driving force for sintering.

Although most simulations have been carried out for a green body that consists of three spherical particles,
the findings above are not expected to change qualitatively in a realistic green body with thousands of
particles with a broad size distribution. The findings greatly advance our fundamental understanding of the
interplay between the densification and coarsening processes involved in solid-state sintering and may find
immediate application in the optimization of green body characteristics to improve sintering kinetics and
microstructure.

Acknowledgement
This work was performed under the auspices of the U.S. Department of Energy by Lawrence Livermore
National Laboratory under Contract DE-AC52-07NA27344 and supported by the Office of Laboratory
Directed Research and Development under project tracking code 20-ER-018. The authors acknowledge
financial support from the U.S. Department of Energy (DOE), Office of Energy Efficiency and Renewable
Energy (EERE), Vehicle Technologies Office (VTO) through the Advanced Battery Materials Research
(BMR) and Applied Battery Research (ABR) programs.




                                                     21
References:
[1] R. German, Sintering: from empirical observations to scientific principles, Butterworth-
Heinemann2014.
[2] A. Mostafaei, A.M. Elliott, J.E. Barnes, F. Li, W. Tan, C.L. Cramer, P. Nandwana, M. Chmielus, Binder
jet 3D printing—Process parameters, materials, properties, modeling, and challenges, Progress in Materials
Science (2020) 100707.
[3] C. Wang, W. Ping, Q. Bai, H. Cui, R. Hensleigh, R. Wang, A.H. Brozena, Z. Xu, J. Dai, Y. Pei, C.
Zheng, G. Pastel, J. Gao, X. Wang, H. Wang, J.-C. Zhao, B. Yang, X. Zheng, J. Luo, Y. Mo, B. Dunn, L.
Hu, A general method to synthesize and sinter bulk ceramics in seconds, Science 368(6490) (2020) 521.
[4] Z. Chen, Z. Li, J. Li, C. Liu, C. Lao, Y. Fu, C. Liu, Y. Li, P. Wang, Y. He, 3D printing of ceramics: A
review, Journal of the European Ceramic Society 39(4) (2019) 661-687.
[5] J. Weerasinghe, S. Sen, J.M.K.W. Kumari, M.A.K.L. Dissanayake, G.K.R. Senadeera, C.A.
Thotawatthage, M. Ekanayake, R. Zhou, P.J. Cullen, P. Sonar, K. Vasilev, K. Ostrikov, Efficiency
enhancement of low-cost metal free dye sensitized solar cells via non-thermal atmospheric pressure plasma
surface treatment, Solar Energy 215 (2021) 367-374.
[6] I. Greenquist, M.R. Tonks, Y. Zhang, Review of sintering and densification in nuclear fuels: Physical
mechanisms, experimental results, and computational models, Journal of Nuclear Materials 507 (2018)
381-395.
[7] R. Galante, C.G. Figueiredo-Pina, A.P. Serro, Additive manufacturing of ceramics for dental
applications: A review, Dental Materials 35(6) (2019) 825-846.
[8] X. Wang, S. Xu, S. Zhou, W. Xu, M. Leary, P. Choong, M. Qian, M. Brandt, Y.M. Xie, Topological
design and additive manufacturing of porous metals for bone scaffolds and orthopaedic implants: A review,
Biomaterials 83 (2016) 127-141.
[9] J. García, V. Collado Ciprés, A. Blomqvist, B. Kaplan, Cemented carbide microstructures: a review,
International Journal of Refractory Metals and Hard Materials 80 (2019) 40-68.
[10] M. Wood, X. Gao, R. Shi, T.W. Heo, J.A. Espitia, E.B. Duoss, B.C. Wood, J. Ye, Exploring the
relationship between solvent-assisted ball milling, particle size, and sintering temperature in garnet-type
solid electrolytes, Journal of Power Sources 484 (2021) 229252.
[11] S. Ramakumar, C. Deviannapoorani, L. Dhivya, L.S. Shankar, R. Murugan, Lithium garnets:
Synthesis, structure, Li+ conductivity, Li+ dynamics and applications, Progress in Materials Science 88
(2017) 325-411.
[12] R.K. Bordia, S.-J.L. Kang, E.A. Olevsky, Current understanding and future research directions at the
onset of the next century of sintering science and technology, Journal of the American Ceramic Society
100(6) (2017) 2314-2352.
[13] S.-J.L. Kang, Sintering: densification, grain growth and microstructure, Elsevier2004.
[14] M.N. Rahaman, Ceramic processing and sintering, CRC press2017.
[15] R.M. German, Coarsening in Sintering: Grain Shape Distribution, Grain Size Distribution, and Grain
Growth Kinetics in Solid-Pore Systems, Critical Reviews in Solid State and Materials Sciences 35(4) (2010)
263-305.
[16] R.M. German, Sintering: Modeling, in: K.H.J. Buschow, R.W. Cahn, M.C. Flemings, B. Ilschner, E.J.
Kramer, S. Mahajan, P. Veyssière (Eds.), Encyclopedia of Materials: Science and Technology, Elsevier,
Oxford, 2001, pp. 8643-8647.
[17] Y.U. Wang, Computer modeling and simulation of solid-state sintering: A phase field approach, Acta
Materialia 54(4) (2006) 953-961.
[18] S. Biswas, D. Schwen, H. Wang, M. Okuniewski, V. Tomar, Phase field modeling of sintering: Role
of grain orientation and anisotropic properties, Computational Materials Science 148 (2018) 307-319.
[19] X. Zhang, Y. Liao, A phase-field model for solid-state selective laser sintering of metallic materials,
Powder Technology 339 (2018) 677-685.
[20] B. Dzepina, D. Balint, D. Dini, A phase field model of pressure-assisted sintering, Journal of the
European Ceramic Society 39(2) (2019) 173-182.

                                                    22
[21] J. Hötzer, M. Seiz, M. Kellner, W. Rheinheimer, B. Nestler, Phase-field simulation of solid state
sintering, Acta Materialia 164 (2019) 184-195.
[22] Y. Yang, O. Ragnvaldsen, Y. Bai, M. Yi, B.-X. Xu, 3D non-isothermal phase-field simulation of
microstructure evolution during selective laser sintering, npj Computational Materials 5(1) (2019) 81.
[23] I. Greenquist, M. Tonks, M. Cooper, D. Andersson, Y. Zhang, Grand potential sintering simulations
of doped UO2 accident-tolerant fuel concepts, Journal of Nuclear Materials 532 (2020) 152052.
[24] I. Greenquist, M.R. Tonks, L.K. Aagesen, Y. Zhang, Development of a microstructural grand potential-
based sintering model, Computational Materials Science 172 (2020) 109288.
[25] R. Termuhlen, X. Chatzistavrou, J.D. Nicholas, H.-C. Yu, Three-dimensional phase field sintering
simulations accounting for the rigid-body motion of individual grains, Computational Materials Science
186 (2021) 109963.
[26] X. Wang, L. Yuan, L. Li, C.O. Yenusah, Y.H. Xiao, L. Chen, Multi-scale phase-field modeling of
layer-by-layer powder compact densification during solid-state direct metal laser sintering, Materials &
Design (2021) 109615.
[27] H. Ravash, L. Vanherpe, J. Vleugels, N. Moelans, Three-dimensional phase-field study of grain
coarsening and grain shape accommodation in the final stage of liquid-phase sintering, Journal of the
European Ceramic Society 37(5) (2017) 2265-2275.
[28] I. Steinbach, Phase-field models in materials science, Modelling and Simulation in Materials Science
and Engineering 17(7) (2009) 073001.
[29] A. Kazaryan, Y. Wang, B.R. Patton, Generalized phase field approach for computer simulation of
sintering: incorporation of rigid-body motion, Scripta Materialia 41(5) (1999) 487-492.
[30] I. Steinbach, F. Pezzolla, A generalized field method for multiphase transformations using interface
fields, Physica D: Nonlinear Phenomena 134(4) (1999) 385-393.
[31] I. Steinbach, M. Apel, Multi phase field model for solid state transformation with elastic strain, Physica
D: Nonlinear Phenomena 217(2) (2006) 153-160.
[32] R. Shi, D.P. McAllister, N. Zhou, A.J. Detor, R. DiDomizio, M.J. Mills, Y. Wang, Growth behavior
of γ'/γ'' coprecipitates in Ni-Base superalloys, Acta Materialia 164 (2019) 220-236.
[33] R. Shi, C. Shen, S.A. Dregia, Y. Wang, Form of critical nuclei at homo-phase boundaries, Scripta
Materialia 146 (2018) 276-280.
[34] F. Abdeljawad, D.S. Bolintineanu, A. Cook, H. Brown-Shaklee, C. DiAntonio, D. Kammler, A. Roach,
Sintering processes in direct ink write additive manufacturing: A mesoscopic modeling approach, Acta
Materialia 169 (2019) 60-75.
[35] J.W. Cahn, J.E. Hilliard, Free Energy of a Nonuniform System. I. Interfacial Free Energy, The Journal
of Chemical Physics 28(2) (1958) 258-267.
[36] A. Moitra, S. Kim, S.G. Kim, S.J. Park, R. German, M.F. Horstemeyer, Atomistic Scale Study on
Effect of Crystalline Misalignment on Densification during Sintering Nano Scale Tungsten Powder,
Advances in Sintering Science and Technology: Ceramic Transactions (2009) 149-160.




                                                      23
