                                                     Extrinsic Dielectric Response due to Domain Wall Motion in Ferroelectric BaTiO3
                                                             Ashok Gurung,1 Mohammad Fatin Ishtiyaq,2 S. Pamir Alpay,1, 2 John Mangeri,3 and Serge Nakhmanson1, 2
                                                             1) Department of Physics, University of Connecticut, Storrs, Connecticut 06269, USA
                                                             2) Department of Materials Science & Engineering, and Institute of Materials Science, University of Connecticut,

                                                             Storrs, Connecticut 06269, USA
                                                             3) Center for Atomic-scale Materials Design (CAMD), Department of Physics,

                                                             Technical University of Denmark, Anker Engelunds Vej 101 2800 Kongens Lyngby,
                                                             Denmark
                                                             (*Electronic mail: serge.nakhmanson@uconn.edu)
                                                             (*Electronic mail: ashok.gurung@uconn.edu)




arXiv:2407.20354v1 [cond-mat.mtrl-sci] 29 Jul 2024
                                                             (Dated: 31 July 2024)
                                                             BaTiO3 (BTO) is a prototypical perovskite ferroelectric, whose dielectric permittivity and loss spectra — which are
                                                             strongly temperature and frequency dependent — include contributions from inhomogeneous polarization patterns,
                                                             with polar domain walls (DWs) being the most common types. In order to elucidate how DWs influence dielectric
                                                             response, we utilized a continuum approach based on the Landau-Ginzburg theory to model field-dependent properties
                                                             of polydomain tetragonal phase of BTO near room temperature and above. A system with 180◦ DWs was evaluated as
                                                             a case study, with both position-resolved and volume-averaged dielectric susceptibility and loss computed at different
                                                             temperatures for a range of applied field frequencies and amplitudes. Our results demonstrate that cooperative dipole
                                                             fluctuations in the vicinity of the DW provide a large (extrinsic) contribution to the system dielectric response relative
                                                             to the intrinsic contribution stemming from within the domain. Dynamics of the DW profile fluctuations under applied
                                                             field can be represented by a combination of breathing and sliding vibrational motions, with each exhibiting distinct
                                                             dependence on the field frequency and amplitude. The implications of this behavior are important for understanding
                                                             and improving control of coupled functional properties in ferroelectric materials, including their dielectric, electrome-
                                                             chanical, and electrooptical responses. Furthermore, this investigation provides a computational benchmark for future
                                                             studies and can be readily extended to other topological polarization patterns in ferroelectrics.




                                                                                                                   1
                                                                                                                                    2

I.   INTRODUCTION

   Domain walls (DWs) are ubiquitous in ferroic materials, profoundly influencing their functional behavior1,2 . Their topological
patterns, mutual orientations, energetics, dynamics and density greatly affect the process of hysteretic switching. Furthermore,
the same DW characteristics impose an organic sense of length scale on the host system, which in turn gives rise to a vari-
ety of interesting effects that can manifest themselves either with or without an applied field. Among these effects are large
contributions to piezoelectric3–5 or piezomagnetic responses, second-harmonic generation6 , anisotropic magnetoresistance7–9 ,
unexpected magnetoelectric couplings9–11 , enhanced conductivity12–14 , or even onset of superconductivity in adjacent magnetic
layers15 .
   In ferroelectrics, DWs form boundary phases between areas with different orientations of spontaneous electric polarization Ps .
Nanostructured ferroelectrics can exhibit a rich assortment of polarization textures, with rotating components of electric dipoles
forming chiral, vortex, skyrmionic or other patterns16–19 . The presence of such patterns can underpin novel or unexpected
material behavior, e.g., negative capacitance20,21 or second-harmonic generation enhancement22 . Strong influence of the system
microstructure2,23 , as well as applied electric, mechanical, thermal and other conditions on the shape and evolution of the
polarization texture can provide even more levers for controlling and fine-tuning the system properties and performance.
   A characteristic of paramount importance for ferroelectric compounds (as well as most electroactive materials in general) is
the system small-signal dielectric susceptibility, i.e., a property that involves fluctuations ∆P about the equilibrium Ps under a
weak (subswitching or subcoercive) oscillating electric field E. Since the early 1960s, researchers have attempted to identify
the influence of DWs on the system dielectric response2,3,24–32 . For weak applied fields, the fluctuations of polarization are
small and DWs are assumed to be vibrating. Such extrinsic contribution to the system small-signal permittivity can usually be
measured by applying a bias voltage that causes the underlying domain patterns to experience irreversible transformations due
to nonlinear switching27,30,31 .
   It is expected that this extrinsic contribution associated with the DW presence can comprise a significant portion of the total di-
electric response signal2,31–33 . Since typical ferroelectric samples host a range of different DW orientations and densities (as well
as a variety of different grain and grain-boundary shapes and orientations in the case of polycrystalline ceramics2,23,34 ), a unified
theoretical description of dielectric response in such complicated structures remains elusive — especially so for atomistic-scale
methodologies that would require large supercells and approximations that describe finite temperature behavior. Nonetheless,
density functional theory and molecular dynamics simulations by Liu and Cohen33 showed that polar dipoles at 90◦ and 180◦
DWs in tetragonal PbTiO3 at room temperature are much more responsive to applied fields, relative to dipoles located deep
within the domain. By parsing out the local contribution due to the DW, these authors demonstrated that its dielectric suscepti-
bility can exceed the intrinsic monodomain one by 2–6 times. This result agrees well with the earlier theoretical models proposed
by Fousek24 and Arlt et al27 based on a quasiparticle approximation of rigid motion of the DW plane.
   Recent observations from position-resolved scanning impedance microscopy13 suggest that vibrational DW motion in ferro-
electric hexagonal manganites can be regarded as a sliding displacement of a ‘rigid’ DW profile combined with a (lower energy)
breathing oscillation of the profile thickness. This description of DW dynamics in applied fields is natural, since analogous
behavior has long been studied in ferromagnets35–39 . However, specific roles such DW sliding and breathing modes play in the
extrinsic dielectric response of ferroelectrics are yet to be determined as relatively few investigations have been conducted in
this area40–42 .
   In this work, we report the results of a comprehensive numerical study of dielectric response of a generic ferroelectric system
with DWs utilizing a continuum-scale approach based on the Landau-Ginzburg theory. We have chosen BaTiO3 (BTO) as an
example due to an abundance of information on its DW-related properties in bulk, thin film and nanostructural forms18,43,44 , as
well as due to an availability of accurate free energy parameterizations for this popular material. Near room temperature and
up to the Curie temperature, TC = 393 K44 , BTO is tetragonal (space group P4mm), permitting six symmetrically equivalent
polar-domain variants with polarization aligned along the C4 axes of the cubic unit cell. Therefore, in this temperature range,
polarization textures including 90◦ and 180◦ DWs are most common. Here, we focused on the 180◦ DW texture, as in BTO it
involves a change in a single component of the Ps vector between the neighboring domains (i.e., is Ising-like in character45 ) and
it does not require large simulation volumes for conducting calculations. In the frequency realm, we concentrated on sub-THz
bands, which are of interest for microwave electronics applications46,47 . At these probing frequencies, (soft) optical phonon
resonances are not strongly excited48,49 and, therefore, dielectric susceptibility spectra are considered relaxational and well
represented by underdamped equations of motion24 .
   For the most interesting case of longitudinal (E || P) induced fluctuations, by evaluating local or position-dependent dielec-
tric response, we show that contributions from the DW region to the system dielectric susceptibility are nearly two orders of
magnitude larger, compared to the intrinsic contributions from the ‘domain proper,’ which is in qualitative agreement with pre-
vious observations. We also demonstrate that, as expected, this local enhancement of the dielectric susceptibility is strongly
temperature dependent and grows sharply as the temperature approaches TC . At room temperature, for characteristic relaxation
frequency (i.e., position of the dielectric loss peak) of the monodomain system located at ∼500 GHz we find the analogous
frequency associated with the 180◦ DW vibration at around 10 GHz. Furthermore, the DW vibration can be decomposed into
a combination of sliding and breathing motions, similar to those observed in ferromagnets35–39 , with the two vibrational modes


     Distribution A. Approved for public release: distribution unlimited. (AFRL–2024–4036) Date Approved 07–24–2024.
                                                                                                                                   3

exhibiting distinct dependencies on the external field frequency and amplitude. From these insights, we can conclude that, in
general, extrinsic contributions to the local weak-field dielectric susceptibility from the DWs may deviate appreciably from those
of the ‘domain proper’ (or monodomain bulk), depending sensitively on the DW orientation and type, which in turn stipulate the
nature and intensity of relaxational processes occurring within the wall under applied field.
   Naturally, in a large sample that may also be polycrystalline, many DWs in multiple different orientations are present, and
therefore any single DW contribution to the dielectric response is likely to be washed out. Still, the simple problem considered
here that involves a response from a single DW can serve as a useful benchmark for evaluating such extrinsic contributions to
the total dielectric susceptibility during subcoercive electric loading. The presented modeling approach can be generalized to
other ferroic materials (based on availability of appropriate Landau-type free-energy parameterizations50 ), other types and orien-
tations of DWs (e.g., for orthorhombic and rhombohedral BTO phases at lower temperatures45 ), or for studies of nanostructured
materials displaying more interesting topological polarization ordering patterns16,18,19,51 .


II.   METHODS

A.    Governing equations

  In the thermodynamic limit, the total free energy F of a ferroelectric system with a volume Ω can be represented by a linear
combination of energy terms corresponding to different physical processes and interactions:
                                                  Z
                                        F(T ) =       [ fbulk (T ) + fwall + felastic + fstrictive ] d 3 r.                      (1)
                                                  Ω

Here fbulk (T ) is the temperature-dependent bulk Landau-type expansion of the ferroelectric ordering energy density at temper-
ature T , fwall is the energy density arising from local gradients of the polarization field P distribution near DWs, felastic is the
linear elastic energy density, and fstrictive is accounting for the electrostrictive coupling between P and total strain field tensor
ε = 21 (∇ · u + (∇ · u)t ), with u being the elastic displacement field. The specific form and numerical parameterization of the
total-free energy expression used in this work is obtained from Ref. [52].
   Time evolution of the polarization field P(r,t) under applied electric field E was obtained as a solution of the time-dependent
Landau-Ginzburg-Devonshire (TDLGD) equation:
                                                               ∂ P δ F(T )
                                                          −Γ      =        − E,                                                  (2)
                                                               ∂t    δP
where Γ is a time-scale coefficient associated with dynamics of P on the energy surface and the subsequent damping force
corresponding to the interaction with defects or the finite temperature anharmonic phonon continuum (see Sec. II C for further
discussion of this coefficient). When E ≡ −∇Φ is zero, Eq. (2) is diffusive in nature, with solutions for P produced by the
process of a gradient descent on the system energy surface towards a local or global minimum. However, a nonzero E provides a
driving force that can oppose the action of stochastic forces associated with the variational derivative of F(T ), which can result
in underdamped oscillatory behavior of P for certain amplitudes of (oscillating) E and choices of Γ. For every time step in the
evolution of Eq. (2), the mechanical equilibrium equation ∇ : σ = 0 was also solved, where σ = C : ε is the total elastic stress
field tensor and C is the fourth-rank elastic stiffness tensor. In addition, we assumed that Eq. (2) is satisfied electrostatically
at every time step by solving the associated Poisson equation ε∇2 Φ = −∇ · P. The isotropic quantity ε ≃ 10 ε0 represents
a background dielectric constant due to core-electrons, which is a typical approximation employed in such continuum-scale
simulations52 .


B.    Stationary 180◦ DWs at zero applied field

   For the geometrical model of the system volume Ω, we utilized a quasi-1D rectilinear shape with real-space dimensions of 40
× 1 × 1 nm. The [100], [010], [001] crystallographic directions of the perovskite BTO unit cell were oriented along the ‘global’
x, y, z cartesian axes of the computational volume. The governing equations discussed in Sec. II A were discretized within Ω
utilizing a finite-element method (FEM) approach with hexahedral elements. Specifically, the F ERRET package53,54 , based on
the open-source Multiphysics Object-Oriented Simulation Environment (MOOSE) framework55 , was used to conduct all the
FEM-based simulations described below. 3D periodic boundary conditions were applied to the system field variables P(r,t) and
u(r,t), leveraging the global strain approach for the latter56 . Sine profile initial conditions were chosen for P(r,t = 0), leading
to the formation of two 180◦ DWs oriented along the long side of Ω upon energy minimization of Eq. (2) in zero applied field E.
The 40 nm length of the computational volume was found to be sufficient to treat the neighboring DWs as mostly non-interacting
entities. The system was considered converged when the relative change of F between consecutive time steps fell below 10−8 .


      Distribution A. Approved for public release: distribution unlimited. (AFRL–2024–4036) Date Approved 07–24–2024.
                                                                                                                                                          4

   Multiple relaxations of the system with 180◦ DWs for the zero applied field were conducted for different temperatures, which
ranged from room temperature (RT) to ∼380 K, producing DW profiles with different thickness. We found that for elevated
temperatures of above ∼320 K, discretization meshes with a step of 0.5 nm were optimal for achieving fast convergence, while
for temperatures in the vicinity of RT, due to the DW profiles being more narrow, meshes with a step of 0.333 nm were preferred.
A representative converged ground state of P(r) at RT is displayed in Fig. 1(a), showing one of the two x-oriented DWs. The color
map represents the magnitude of the polar vector |P|, which is equivalent to |Pz | for the 180◦ DW with the chosen orientation.
The DW profile is Ising-like in character, i.e., the up (+ẑ) and down (−ẑ) oriented polar domains are separated by a region where
|P| tends to zero.




FIG. 1. (a) An equilibrium 180◦ DW profile at RT in the absence of external applied field E. The longitudinal direction of the field application
during the dielectric response evaluation is also shown in the upper right corner of the panel. Contour plots of position-dependent longitudinal
(E || Pz ẑ) dielectric susceptibility at RT as a function of the applied field frequency f : (b) real part χ ′ (x, f ) and (c) imaginary part χ ′′ (x, f ).
The x axis is common for all the three panels, with its zero mark coincident with the location of the DW profile center, Pz(x ≡ 0) = 0, in the
absence of the applied field. Similar plots can be obtained for other temperatures.




C.    Evaluation of the dielectric response

   Under an applied electric field signal of the form of a harmonic wave with angular frequency ω, E = E0 eiωt , we consider
fluctuations of the induced polarization ∆P ≡ P − Ps . In case of a weak, subcoercive applied field |E0 | ≪ |EC |, we can assume
that |∆P| ≪ |Ps | and that the shape of the polarization fluctuation signal is also harmonic, but includes a phase delay θ with
that of E, i.e., ∆P = ∆P0 ei(ωt+θ ) . The linear dielectric susceptibility tensor can then be decomposed into real and imaginary
components, respectively, as

                                                           ∆Pj0                               ∆Pj0
                                                 χ ′jk =       0
                                                                 cos(θ ) and       χ ′′jk =            sin(θ ),                                         (3)
                                                           ε0 Ek                              ε0 Ek0


     Distribution A. Approved for public release: distribution unlimited. (AFRL–2024–4036) Date Approved 07–24–2024.
                                                                                                                                         5

where ε0 is the vacuum permittivity and j, k are Cartesian indices. Therefore, by computing and tracking the shape of the ∆P(t)
signal for a sufficient number of cycles, Eqs. (3) can be fit as a function of the applied field frequency f = ω/2π, providing
information about both real and imaginary parts of the system dielectric response.
   The developed methodology presented here and in our previous investigation57 allows us to evaluate the response of the system
polarization to applied electric fields on both local and global levels. In the first case, the polarization fluctuations are computed
at specific points in coordinate space, providing the induced polarization as a function of position, ∆P(r), which in turn yields
position-dependent or local estimates for χ ′jk ( f , r) and χ ′′jk ( f , r). In the second case, local ∆P(r) fluctuations can be averaged
over Ω, which includes both domain and DW regions, thus producing volume-averaged or global estimates for χ ′jk ( f ) and χ ′′jk ( f )
that lose their dependence on r. For mapping out the χ ′ and χ ′′ frequency dependencies, we employed a nonlinear least-squares
curve-fitting approach based on the trust-region reflective method, which is a robust algorithm for fitting large sparse problems
with bounds58,59 .
   In this and previous investigation57 , we found that the value of the (scalar) time relaxation parameter Γ merely influences
the time scale of the relaxation, while leaving all other features of the dispersion curves (thermal, spatial, or otherwise) intact.
Here, we chose Γ = 3.33 × 10−4 kg m3 s−1 C−2 , so that the natural relaxation frequency of the homogeneous monodomain
system, or equivalently the point when χ ′ ( f ) = χ ′′ ( f ), is located approximately at 500 GHz. This is a reasonable approximation
considering dielectric response measurements provide a similar characteristic relaxation frequency in cubic BTO of around 300
GHz60 , whereas below TC it can be as large as 800 GHz due to mixed order-disorder / displacive nature of the phase transition49 .
   For the applied field directions, we probed all three symmetrically inequivalent possibilities, i.e., a longitudinal case of
E || [001] || Pz ẑ, as well as both transverse cases E || [100] ⊥ Pz ẑ and E || [010] ⊥ Pz ẑ. We found that both transverse modes
do not produce DW vibration excitations due to the Ising-like nature of the z-axis oriented wall profile. Therefore, in what
follows we present the results associated only with the longitudinal mode DW excitations, i.e., χ ′ = χzz′ and χ ′′ = χzz′′ , which
exhibit the most interesting physical behavior.


III.    RESULTS

   We start the discussion of the produced results with an evaluation of the position-dependent longitudinal dielectric suscepti-
bility of the system at RT as a function of the applied field frequency f , with its real part χ ′ (x, f ) and imaginary part χ ′′ (x, f ),
presented in panels (b) and (c), respectively, of Fig. 1. In panel (b), we clearly observe a large increase in the real part of the
dielectric susceptibility near and at the center of the DW, reaching almost 60 times of the low-frequency intrinsic (monodomain)
             ′
response χmono    ( f → 0) ≈ 200. The same behavior is found in panel (c) the imaginary part of the DW-associated dielectric sus-
ceptibility, i.e., the extrinsic dielectric loss peak. For the intrinsic (monodomain) loss peak positioned around 500 GHz [by our
choice of the time relaxation parameter Γ], the DW-associated loss peak occurs at around 10 GHz. Interestingly, at the exact cen-
ter of the DW, the real part of the dielectric susceptibility becomes slightly negative — as shown in panel (b) by orange-yellow
colors — at around 300 GHz, which may indicate the presence of a retardation effect where E has already switched direction
while ∆P has not. Furthermore, in both cases we find that the extent of the local extrinsic contribution to χ ′ and χ ′′ is limited in
space to about ±1 nm away from the DW center, which is a slightly larger region than that is conventionally defined by the DW
thickness (that is usually obtained by fitting a hyperbolic tangent function to the stationary DW profile45 ).
   Turning to the thermal dependence of the system dielectric response, we present real and imaginary parts of the volume-
averaged dielectric susceptibility in panels (a) and (b), respectively, of Fig. 2. As the system temperature increases towards
TC , the governing thermodynamic potential F(T ) becomes ‘softer,’ thus allowing for stronger fluctuations ∆P under the applied
field. Furthermore, as the temperature increases, the DW regions become wider. In the inset to panel (a), we show the stationary
DW thickness 2δ as a function of temperature. Our calculations for both utilized meshes are in reasonable agreement with
results of Ref. [45] at lower T , but deviate from them towards thicker walls, as the temperature is increased. E.g., according to
our calculations, δ (T = 380 K) ≃ 2δ (RT).
   The increase in DW thickness with growing temperature implies an equivalent expansion in the width of areas associated with
the extrinsic dielectric response, which is reflected in the aggressive enlargement of the respective parts of the volume-averaged
dielectric susceptibility curves for both χ ′ and χ ′′ , as is shown in Fig. 2. We should mention that, since our simulation volume
contains two DWs separated by 20 nm, these results are presented for a DW volume fraction vDW = 2(2δ )/40. We find that
the volume-averaged χ ′ generally follows the rule of mixtures, i.e., it roughly scales as vDW χDW       ′                ′
                                                                                                             + (1 − vDW )χmono for any
considered f , as discussed in Ref. [33]. Similar aggregate dielectric response curves for subcoercive fields, showing two plateau
regions in the χ ′ ( f ) dependence accompanied by two peaks in the χ ′′ ( f ) dependence, have been obtained in Ref. [61] using the
phase-field approach for the case of generic tetragonal phase 90◦ DWs.
   The final stage of this study involved a deeper look at the dynamics of DW motion under weak applied electric field, including
an assessment of any dependencies on the field amplitude |E0 |. Specifically we utilized the following expression to represent the
time evolution of the DW profile:

                                                 Pz (x) = Pzs tanh [δb (x − δs )] + ∆Pz .                                              (4)


       Distribution A. Approved for public release: distribution unlimited. (AFRL–2024–4036) Date Approved 07–24–2024.
                                                                                                                                           6




FIG. 2. Thermal dependence of the system volume-averaged dielectric susceptibility. Real (a) and imaginary (b) parts of the dielectric
susceptibility [shown in solid lines with circle markers] as a function of frequency at three different temperatures T = 298, 330, 350 K. The
intrinsic contribution is also included in the form of dashed lines with star markers. The inset depicts the temperature dependence of the
computed thickness 2δ of the stationary 180◦ DW profile. Data from Ref. [45] is provided for comparison.


Here, δα (t), α = s, b are the amplitudes of the sliding and breathing DW vibrational modes, respectively, described in the same
spirit as in the DW dynamics studies of ferromagnetic systems35–39 . For harmonically oscillating |∆P(t)|, both amplitudes can
also be fitted to harmonic functions: δα (t) ≡ δα0 ei(ωα t+θα ) [note that ωα , θα can be different from ω, θ ].
   We illustrate the dependence of the DW breathing and sliding mode amplitudes on frequency in panels (a) and (c) of Fig. 3.
This data is obtained for RT, while the applied field strength ranges from 0.4 to 2.0 kV/cm. We can assign both types of DW
motion critical frequencies fα , that are independent of the value of the applied field, beyond which their amplitudes decay to
zero. In panel (b) of Fig. 3, we show how fb and fs align with the features of the volume-averaged χ ′ and χ ′′ dispersion curves.
Remarkably, each critical frequency corresponds to an inflection point, or a kink, on the χ ′ ( f ) curve, which is a center of a
narrow region where the system ‘jumps’ from one plateau to the next – revealing exactly how each DW motion contributes to the
dielectric response of the system and where such contribution ‘shuts off’. (Obviously, since fb ≪ fs , the breathing vibrational
mode ‘shuts off’ at much lower frequencies than the sliding mode.)
   Under the growing applied field strength — up to the limit of 2 kV/cm, above which we no longer observe harmonic ∆P(t)
oscillations — the amplitudes of sliding and breathing motion increase, but the shape of their dependency on the field magnitude
is not the same. As shown in the inset to Fig. 3(a), for the lowest frequencies probed, the breathing mode amplitude has a
quadratic dependence on the magnitude of the field, whereas the sliding mode dependence is roughly linear. We also point out
that the values of δb0 are on the order of a few pm, while those of δs0 can be tens of pm. This result agrees well with empirical
estimates dating back to Kittel’s Letter on this topic in 195162 , where he estimated the subswitching sliding mode amplitudes
in BTO to be on the order of a few % of the lattice constant length. Such a quantitative agreement is usually not expected for
Landau-based models but nevertheless we mention it here.




     Distribution A. Approved for public release: distribution unlimited. (AFRL–2024–4036) Date Approved 07–24–2024.
                                                                                                                                             7




FIG. 3. Applied field strength dependence of the system volume-averaged dielectric susceptibility and the DW sliding and breathing vibra-
tional mode amplitudes at RT. Real [solid lines] and imaginary [dashed lines] parts of the dielectric susceptibility as a function of frequency
for a number of different applied field amplitudes E ≡ |E0 | are shown in the middle panel (b). DW breathing mode amplitude δb0 and sliding
mode amplitude δs0 as a function of frequency for a number of different applied field amplitudes E are shown in the top panel (a) and bottom
panel (c), respectively. Critical frequencies fb and fs , marking out the complete decay of the amplitude of the corresponding DW vibrational
mode, are highlighted by dashed red lines. The inset depicts the dependence of δb0 and δs0 on E for f → 0.


IV.   DISCUSSION

   By utilizing underdamped equations of motion for the system polarization field, we have characterized the extrinsic dielectric
response of 180◦ DWs in BTO in the subcoercive applied field limit. Our results confirm the current understanding that DW
regions provide a large overall contribution to the dielectric susceptibility of the system (≈ 60 times that of the intrinsic response
at RT). The enhancements were localized to the region surrounding the DW that extends slightly beyond the conventional (geo-
metrical) definition of its thickness. By sampling the thermal dependence of the dielectric response, we revealed that its extrinsic
part grows sharply due to the softening of the system energy potential as T → TC and the zero-field DW thickness becomes wider.
Finally, we decomposed the DW vibrational motion into sliding and breathing modes, and showed that both of these have unique



      Distribution A. Approved for public release: distribution unlimited. (AFRL–2024–4036) Date Approved 07–24–2024.
                                                                                                                                  8

field frequency and amplitude dependencies, thus providing distinct contributions to the response of the system. Our assumption
of underdamped motion of P implies that it does not exhibit inertial effects where the polarization would have dynamics analo-
gous to magnons63,64 . Nonetheless, the presented results are mostly valid within the probed frequency interval, while accounting
for the inertial effects would constitute a next-level approximation to the underlying theory of dielectric response.
   Building on the results of our previous work57 , this study is a step forward in understanding the small-signal inhomogeneous
dynamics of ferroelectric polarization at the continuum level, and it can be readily generalized and extended to a number of
other systems and more complex polar topologies. For example, in the case of [110]-oriented (or equivalent) 90◦ DW, its
twisting motion (which is not relevant for the longitudinal excitations evaluated here) should also be considered39,65 . We point
out that, upon field cycling, dynamical (twisting) products of P × ∂ P/∂t must be nonzero, giving rise to magnetic fields and thus
making the DW regions dynamically magnetoelectric66 . Corresponding experiments to investigate this effect have already been
proposed65 .


ACKNOWLEDGMENTS

A.G., S.P.A. and S.N. gratefully acknowledge the Air Force Research Laboratory, Materials and Manufacturing Directorate
(AFRL/RXMS) for support via Contract No. FA8650–21–C5711. J.M. thanks Pavel Marton (FZU) for some early stimulating
discussions on the topic.


REFERENCES

1 G. Catalan, J. Seidel, R. Ramesh, and J. F. Scott, “Domain wall nanoelectronics,” Rev. Mod. Phys. 84, 119 (2012).
2 J. Schultheß, G. Picht, J. Wang, Y. A. Genenko, L.-Q. Chen, J. E. Daniels, and J. Koruza, “Ferroelectric polycrystals: Structural

   and microstructural levers for property-engineering via domain-wall dynamics,” Prog. Mater. Sci 136, 101101 (2023).
3 N. Bassiri-Gharb, I. Fujii, E. Hong, S. Trolier-McKinstry, D. V. Taylor,      and D. Damjanovic, “Domain wall contributions to
   the properties of piezoelectric thin films,” J. Electr. Ceram. 19, 49–67 (2007).
 4 K. Wada, K. Yako, K. Yokoo, H. Kakemoto, and T. Tsurumi, “Domain Wall Engineering in Barium Titanate Single Crystals

   for Enhanced Piezoelectric Properties,” Ferroelectrics 334, 17–27 (2006).
 5 T. Sluka, A. K. Tagantsev, D. Damjanovic, M. Gureev, and N. Setter, “Enhanced electromechanical response of ferroelectrics

   due to charged domain walls,” Nature Comm. 3, 748 (2012).
 6 S. I. Bozhevolnyi, J. Hvam, K. Pedersen, F. Laurell, H. Karlsson, T. Skettrup, and M. Belmonte, “Second-harmonic imaging

   of ferroelectric domain walls,” Appl. Phys. Lett. 73, 1814–1816 (1998).
 7 M. Viret, Y. Samson, P. Warin, A. Marty, F. Ott, E. Søndergård, O. Klein, and C. Fermon, “Anisotropy of Domain Wall

   Resistance,” Phys. Rev. Lett. 85, 3962 (2000).
 8 R. Danneau, P. Warin, J. P. Attané, I. Petej, C. Beigné, C. Fermon, O. Klein, A. Marty, F. Ott, Y. Samson, and M. Viret,

   “Individual Domain Wall Resistance in Submicron Ferromagnetic Structures,” Phys. Rev. Lett. 88, 157201 (2002).
 9 Q. He, C.-H. Yeh, J.-C. Yang, G. Singh-Bhalla, C.-W. Liang, P.-W. Chiu, G. Catalan, L. Martin, Y.-H. Chu, J. Scott, et al.,

   “Magnetotransport at domain walls in BiFeO3 ,” Phys. Rev. Lett. 108, 067203 (2012).
10 M. Giraldo, Q. N. Meier, A. Bortis, D. Nowak, N. A. Spaldin, M. Fiebig, M. C. Weber, and T. Lottermose, “Magnetoelectric

   coupling of domains, domain walls and vortices in a multiferroic with independent magnetic and electric order,” Nature Comm.
   12, 3093 (2021).
11 X. Li, Y. Yun, A. S. Thind, Y. Yin, Q. Li, W. Wang, A. T. N’Diaye, C. Mellinger, X. Jiang, R. Mishra, and X. Xu, “Domain-wall

   magnetoelectric coupling in multiferroic hexagonal YbFeO3 films,” Sci. Rep. 13, 1755 (2023).
12 A. Suna, O. E. Baxter, J. P. V. McConville, A. Kumar, R. G. P. McQuaid, and J. M. Gregg, “Conducting ferroelectric domain

   walls emulating aspects of neurological behavior,” Appl. Phys. Lett. 121, 222902 (2022).
13 X. Wu, U. Petralanda, L. Zheng, Y. Ren, R. Hu, S.-W. Cheon, S. Artyukhin, and K. Lai, “Low-energy structural dynamics of

   ferroelectric domain walls in hexagonal rare-earth manganites,” Sci. Adv. 3, e1602371 (2017).
14 M. Zahn, E. Beyreuther, I. Kiseleva, A. S. Lotfy, C. J. McCluskey, J. R. Maguire, A. Suna, M. Rusing, J. M. Gregg, and

   L. M. Eng, “Equivalent-circuit model that quantitatively describes domain-wall conductivity in ferroelectric LiNbO3 ,” Phys.
   Rev. Appl. 24, 024007 (2024).
15 Z. Yang, M. Lange, A. Volodin, R. Szymczak, and V. V. Moshchalkov, “Domain-wall superconductivity in superconduc-

   tor–ferromagnet hybrids,” Nature Mater. 3, 793–798 (2004).
16 S. Cherifi-Hertel, H. Bulou, R. Hertel, G. Taupier, K. D. Dorkenoo, C. Andreas, J. Guyonnet, I. Gaponenko, K. Gallo, and

   P. Paruch, “Non-Ising and chiral ferroelectric domain walls revealed by nonlinear optical microscopy,” Nature Comm. 8, 15768
   (2017).
17 S. Fusil, J.-Y. Chauleau, X. Li, J. Fischer, P. Dufour, C. Léveillé, C. Carrétéro, N. Jaouen, M. Viret, A. Gloter, and V. Garcia,

   “Polar Chirality in BiFeO3 Emerging from A Peculiar Domain Wall Sequence,” Adv. Elec. Mater. 8, 2101155 (2022).


    Distribution A. Approved for public release: distribution unlimited. (AFRL–2024–4036) Date Approved 07–24–2024.
                                                                                                                              9

18 J. M. Gregg, “Exotic Domain States in Ferroelectrics:     Searching for Vortices and Skyrmions,” Ferroelectrics 433, 74–87
   (2012).
19 S. Das, Y. L. Tang, Z. Hong, M. A. P. Gonçalves, M. R. McCarter, C. Klewe, K. X. Nguyen, F. Gómez-Ortiz, P. Shafer,

   E. Arenholz, V. A. Stoica, S.-L. Hsu, B. Wang, C. Ophus, J. F. Liu, C. T. Nelson, S. Saremi, B. Prasad, A. B. Mei, D. G.
   Schlom, J. Íñiguez, P. Garciía-Ferández, D. A. Muller, L.-Q. Chen, and R. Ramesh, “Observation of room-temperature polar
   skyrmions,” Nature 568, 368–372 (2019).
20 P. Zubko, J. C. Wojdeł, M. Hadjimichael, S. Fernandez-Pena, A. Sené, I. Luk’yanchuk, J.-M. Triscone, and J. Íñiguez,

   “Negative capacitance in multidomain ferroelectric superlattices,” Nature 534, 524–528 (2016).
21 S. Das, Z. Hong, V. A. Stoica, M. A. P. Gonçalves, Y. T. Shao, E. Parsonnet, E. J. Marksz, S. Saremi, M. R. McCarter,

   A. Reynoso, C. J. Long, A. M. Hagerstrom, D. Meyers, V. Ravi, B. Prasad, H. Zhou, Z. Zhang, H. Wen, F. Gómez-Ortiz,
   P. García-Fernández, J. Bokor, J. Íñiguez, J. W. Freeland, N. D. Orloff, and R. Ramesh, “Local negative permittivity and
   topological phase transition in polar skyrmions,” Nature Mater. 20, 194–201 (2021).
22 S. Wang, W. Li, C. Deng, Z. Hong, H.-B. Gao, X. Li, Y. Gu, Q. Zheng, Y. Wu, P. G. Evans, J.-F. Li, C.-W. Nan, and Q. Li,

   “Giant electric field-induced second harmonic generation in polar skyrmions,” Nature Comm. 15, 1374 (2024).
23 K. Wolk, R. S. Dragland, E. Chavez-Panduro, L. Richarz, Z. Yan, E. Bourret, K. A. Hunnestad, C. Tzschashel, J. Schultheiß,

   and D. Meier, “Coexistence of multi-scale domains in ferroelectric polycrystals with non-uniform grain-size distributions,”
   arXiv:2401.04654 (2024).
24 J. Fousek, “The contribution of domain walls to the small-signal complex permittivity of BaTiO ,” Czechoslovak J. of Phys.
                                                                                                     3
   B 15, 412–417 (1965).
25 J. Fousek and V. Janoušek, “The Contribution of Domain-Wall Oscillations to the Small-Signal Permittivity of Triglycine

   Sulphate,” Phys. Stat. Sol. 13, 195 (1966).
26 L. Benguigui, “Ferroelectric losses in BaTiO produced by the 90◦ domain walls,” Ferroelectrics 7, 315–317 (1973).
                                                 3
27 G. Arlt, H. Dederichs, and R. Herbiet, “90◦ Domain Wall Relaxation in Tetragonally Distorted Ferroelectric Ceramics,”

   Ferroelectrics 74, 37–53 (1987).
28 R. Herbiet, U. Robels, H. Dederichs, and G. Arlt, “Domain wall and volume contributions to the material properties of PZT

   ceramics,” Ferroelectrics 98, 107–121 (1989).
29 Y. L. Wang, A. K. Tagantsev, D. Damjanovic, and N. Setter, “Giant domain wall contribution to the dielectric susceptibility

   in BaTiO3 single crystals,” Appl. Phys. Lett. 91, 062905 (2007).
30 J. Karthik, A. R. Damodaran, and L. W. Martin, “Effect of 90◦ Domain Walls on the Low-Field Permittivity of PbZr Ti O
                                                                                                                      0.2 0.8 3
   Thin Films,” Phys. Rev. Lett. 108, 167601 (2012).
31 R. Xu, J. Karthik, A. R. Damodaran, and L. W. Martin, “Stationary domain wall contribution to enhanced ferroelectric

   susceptibility,” Nature Comm. 5, 3120 (2014).
32 C. M. Fancher, S. Brewer, C. C. Chung, S. Röhrig, T. Rojac, G. Esteves, M. Deluca, N. Bassiri-Gharb, and J. L. Jones, “The

   contribution of 180◦ domain wall motion to dielectric properties quantified from in situ X-ray diffraction,” Acta Mater. 126,
   36–43 (2017).
33 S. Liu and R. E. Cohen, “Origin of stationary domain wall enhanced ferroelectric susceptibility,” Phys. Rev. B 95, 094102

   (2017).
34 D. M. Marincel, H. Zhang, S. Jesse, A. Belianinov, M. Okatan, S. V. Kalinin, M. Rainforth, I. M. Reaney, C. A. Randal, and

   S. Trolier-McKinstry, “Domain Wall Motion Across Various Grain Boundaries in Ferroelectric Thin Films,” J. Amer. Ceram.
   Soc 98, 1848–1857 (2015).
35 J. C. Slonczewski, “Breathing vibrations of a Néel wall,” J. Appl. Phys. 55, 2536–2538 (1984).
36 R. L. Stamps, A. S. Carriço, and P. E. Wigen, “Domain-wall resonance in exchange-coupled magnetic films,” Ferroelectrics

   55, 10 (1997).
37 K. Matsushita, M. Sasaki, and T. Chawanya, “Swing Casting Boost for Confined Domain Wall Breathing,” J. Phys. Soc. Jpn.

   83, 013801 (2014).
38 M. Mori, W. Koshibae, S.-i. Hikino, and S. Maekawa, “Possible method to observe the breathing mode of a magnetic domain

   wall in the Josephson junction,” J. Phys. Condens. Matter 26, 255702 (2014).
39 P. J. Metaxas, M. Albert, S. Lequeux, V. Cros, J. Grollier, P. Bortolotti, A. Anane, and H. Fangohr, “Resonant translational,

   breathing, and twisting modes of transverse magnetic domain walls pinned at notches,” Phys. Rev. B 93, 054414 (2016).
40 R. P. Jiménez and J. A. Eiras, “Modeling ferroelectric domain walls motion and nonlinear dielectric response,” Ferroelectrics

   569, 295–309 (2020).
41 P. Chen, L. Ponet, K. Lai, R. Cingolani, and S. Artyukhin, “Domain wall-localized phonons in BiFeO : spectrum and selection
                                                                                                        3
   rules,” npj Comp. Mater. 6, 48 (2020).
42 G. Chen, J. Lan, T. Min, and J. Xiao, “Narrow Waveguide Based on Ferroelectric Domain Wall,” Chinese Phys. Lett. 38,

   087701 (2021).
43 A. K. Tagantsev, L. E. Cross, and J. Fousek, Domains in ferroic crystals and thin films, Vol. 13 (Springer, 2010).
44 B. Ertuğ, “The overview of the electrical properties of barium titanate,” American Journal of Engineering Research 2, 1–7

   (2013).


    Distribution A. Approved for public release: distribution unlimited. (AFRL–2024–4036) Date Approved 07–24–2024.
                                                                                                                             10

45 P. Marton, I. Rychetsky,      and J. Hlinka, “Domain walls of ferroelectric BaTiO3 within the Ginzburg-Landau-Devonshire
   phenomenological model,” Phys. Rev. B 81, 144125 (2010).
46 T. Tsurumi, J. Li, T. Hoshina, H. Kakemoto, M. Nakada, and J. Akedo, “Ultrawide range dielectric spectroscopy of BaTiO -
                                                                                                                              3
   based perovskite dielectrics,” Appl. Phys. Lett. 91, 182905 (2007).
47 E. J. Marksz, A. M. Hagerstrom, X. Zhang, N. Al Hasan, J. Pearson, J. A. Drisko, J. C. Booth, C. J. Long, I. Takeuchi, and

   N. D. Orloff, “Broadband, High-Frequency Permittivity Characterization for Epitaxial Ba1−x Srx TiO3 Composition-Spread
   Thin Films,” Phys. Rev. Appl. 15, 064061 (2021).
48 F. Jona and G. Shirane, Ferroelectric Crystals (Dover Publications, Inc., 1962).
49 J. Hlinka, T. Ostapchuk, D. Nuzhnyy, J. Petzelt, P. Kuzel, C. Kadlec, P. Vanek, I. Ponomareva, and L. Bellaiche, “Coexistence

   of the Phonon and Relaxation Soft Modes in the Terahertz Dielectric Response of Tetragonal BaTiO3 ,” Phys. Rev. Lett. 101,
   167402 (2008).
50 J. Mangeri, D. Rodrigues, M. Graf, S. Biswas, O. Heinonen, and J. Íñiguez, “Coupled magnetostructural continuum model

   for multiferroic BiFeO3 ,” Phys. Rev. B 108, 094101 (2023).
51 D. Karpov, Z. Liu, T. dos Santos Rolo, R. Harder, P. V. Balachandran, D. Xue, T. Lookman, and E. Fohtung, “Three-

   dimensional imaging of vortex structure in a ferroelectric nanoparticle driven by an electric field,” Nature Comm. 8, 280
   (2017).
52 J. Hlinka and P. Márton, “Phenomenological model of a 90◦ domain wall in BaTiO -type ferroelectrics,” Phys. Rev. B 74,
                                                                                            3
   104104 (2006).
53 J. Mangeri, Y. Espinal, A. Jokisaari, S. P. Alpay, S. Nakhmanson, and O. Heinonen, “Topological phase transformations and

   intrinsic size effects in ferroelectric nanoparticles,” Nanoscale 9, 1616–1624 (2017).
54 “Ferret: Parallel mesoscale simulations of ferroic and related electronic materials.” https://mangerij.github.io/

   ferret/ (2024), accessed: 2024-07-01.
55 C. J. Permann, D. R. Gaston, D. Andrš, R. W. Carlsen, F. Kong, A. D. Lindsay, J. M. Miller, J. W. Peterson, A. E. Slaughter,

   R. H. Stogner, and R. C. Martineau, “MOOSE: Enabling massively parallel multiphysics simulation,” SoftwareX 11, 100430
   (2020).
56 S. Biswas, D. Schwen, and J. D. Hales, “Development of a finite element based strain periodicity implementation method,”

   Finite Elem. Anal. Des. 179, 103436 (2020).
57 A. Gurung, J. Mangeri, A. M. Hagerstrom, N. D. Orloff, S. Alpay, and S. Nakhmanson, “Modeling structure–properties

   relations in compositionally disordered relaxor dielectrics at the nanoscale,” J. Appl. Phys. 134, 104102 (2023).
58 (2022), S CI P Y V 1.9.3 package in python 3.9.13.
59 N. I. M. Gould, C. Sainvitu, and P. L. Toint, “A Filter-Trust-Region Method for Unconstrained Optimization,” SIAM Journal

   on Optimization 16, 341–357 (2005).
60 I. Ponomareva, L. Bellaiche, T. Ostapchuk, J. Hlinka, and J. Petzelt, “Terahertz dielectric response of cubic BaTiO ,” Phys.
                                                                                                                       3
   Rev. B 77, 012102 (2008).
61 P. Chu, D. P. Chen, Y. L. Wang, Y. L. Xie, Z. B. Yan, J. G. Wan, J.-M. Liu, and J. Y. Li, “Kinetics of 90◦ domain wall

   motions and high frequency mesoscopic dielectric response in strained ferroelectrics: A phase-field simulation,” Sci. Rep. 4,
   5007 (2014).
62 C. Kittel, “Domain Boundary Motion in Ferroelectric Crystals and the Dielectric Constant at High Frequency,” Phys. Rev. 83,

   458 (1951).
63 P. Tang, R. Iguchi, K.-i. Uchia, and G. E. W. Bauer, “Excitations of the ferroelectric order,” Phys. Rev. B 106, L081105

   (2022).
64 G. E. W. Bauer, P. Tang, R. Iguchi, J. Xiao, K. Shen, Z. Zhong, T. Yu, S. M. Rezende, J. P. Heremans, and K. Uchida,

   “Polarization transport in ferroelectrics,” Phys. Rev. Appl. 20, 050501 (2023).
65 D. Juraschek, Q. N. Meier, M. Trassin, S. E. Trolier-McKinstry, C. L. Degen, and N. A. Spaldin, “Dynamical Magnetic Field

   Accompanying the Motion of Ferroelectric Domain Walls,” Phys. Rev. Lett. 123, 127601 (2019).
66 D. M. Juraschek, M. Fechner, A. V. Balatsky, and N. A. Spaldin, “Dynamical multiferroicity,” Phys. Rev. Mater. 1, 014401

   (2017).




    Distribution A. Approved for public release: distribution unlimited. (AFRL–2024–4036) Date Approved 07–24–2024.
