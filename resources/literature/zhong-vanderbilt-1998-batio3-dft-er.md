                                                               Temperature-dependent dielectric




arXiv:cond-mat/9802208v1 [cond-mat.mtrl-sci] 19 Feb 1998
                                                            response of BaTiO3 from first principles
                                                                              Alberto Garcı́a∗ and David Vanderbilt†
                                                                         ∗
                                                                          Departamento de Fı́sica Aplicada II, Universidad del Paı́s Vasco
                                                                            Apdo. 644, 48080 Bilbao, Spain, email: wdpgaara@lg.ehu.es
                                                                            †
                                                                              Department of Physics and Astronomy, Rutgers University
                                                             136 Frelinghuysen Road, Piscataway, NJ 08854-8019, USA, email: dhv@physics.rutgers.edu




                                                               Abstract. Monte Carlo simulations with an effective Hamiltonian parametrized from
                                                               first principles are performed to study the dielectric response of BaTiO3 as a function
                                                               of temperature, with particular emphasis on the behavior of the dielectric constant
                                                               near the transition from the ferroelectric tetragonal phase to the paraelectric cubic
                                                               phase.



                                                              The peculiar dielectric properties of ferroelectric materials stem from the coupling
                                                           of the electric field to polar distortions of the crystal lattice. In one common
                                                           scenario, the progressive softening of a lattice vibrational mode in the neighborhood
                                                           of a phase transition brings about a dramatic rise in the value of the dielectric
                                                           constant. The resulting very large relative permitivities (in the thousands range)
                                                           have found important technological applications. From a practical point of view,
                                                           however, the development of materials with a desired response faces the difficulty
                                                           of trying to separate experimentally the influences of many effects: composition,
                                                           structure, domain configuration, etc. There are also open theoretical issues such as
                                                           whether the relevant phase transitions are indeed associated to the above-mentioned
                                                           “soft-mode” (and are thus of “displacive” character) or exhibit “order-disorder”
                                                           characteristics. The use of first-principles calculations can help in both fronts. They
                                                           allow the study of the response of a system under “controlled” conditions that would
                                                           be very difficult or impossible to realize in the laboratory. Besides, they provide a
                                                           microscopic view of the materials which is simply not available experimentally and,
                                                           unlike simplified models, they are tailored to the detailed chemical composition of
                                                           the system.
                                                              In the last few years much progress has been made in the computational study of
                                                           ferroelectric materials through the use of effective Hamiltonians which contain the
                                                           physically relevant degrees of freedom of the structure. The effective Hamiltoni-
                                                           ans are constructed on the basis of first-principles calculations, and the statistical
                                                           mechanics of the system is then studied by Monte Carlo simulation. Calculations
of the phase transition sequence [1] and ferroelectric domain walls [2] in BaTiO3 ,
and of the ferroelectric transition in PbTiO3 [3], have proved the usefulness of this
approach.
   In this work we present the first calculations of the temperature-dependent di-
electric response of the perovskite BaTiO3 from first principles, with particular
emphasis on the behavior of the dielectric tensor in the vicinity of the phase tran-
sition from the tetragonal ferroelectric to the cubic paraelectric phase.
   The basic ingredient of the Metropolis Monte Carlo algorithm is the generation of
a sequence of states which are distributed according to the Boltzmann probability
Probj = exp(−βU j ), where U j is the energy of the state j and β = (kT )−1 . A state
jn+1 is added to the sequence after state jn on the basis of a transition probability
π(n, n + 1) = min{1, exp[β(U jn − U jn+1 )]}. In our method the energy U of the
system is represented by means of an effective Hamiltonian Heff which is basically
a Taylor expansion of the energy surface around the high-symmetry cubic perovskite
structure. Heff is written in terms of the dynamical variables which are relevant to
the low-energy distortions: the amplitudes {u} of the local modes (three degrees
of freedom per unit cell) which represent the “soft” transverse optical phonon and
are directly related to the polarization P of the crystal [4] [P = (Z ∗ /V ) u,
                                                                                      P

where Z ∗ is the mode effective charge and V is the cell volume]; a set {v} of
displacement variables representing the acoustic modes; and the six components
of the homogeneous strain η. The parameters of the energy expansion, including
those for the on-site local-mode self-energy, the interaction between local modes
(both short-range and dipole-dipole), the elastic energy, and the local mode-elastic
coupling, are computed using highly accurate first-principles LDA calculations with
Vanderbilt ultrasoft pseudopotentials [5]. More details about the construction of
the effective Hamiltonian can be found in Ref. [1]. The extension of the standard
Metropolis Monte Carlo algorithm to include the effects of stress σ and electric field
E involves replacing the Boltzmann probability factor exp(−βU j ) by exp[−β(U j −
V0 σν ηνj − Ei Pij )] in the acceptance criterion for state j (here Pi = V Pi is the ith
component of the net dipole moment of the crystal and V0 is the volume for zero
strain). For a given temperature, stress, and field, the strain η and the mode
variables are allowed to fluctuate, their average values determining the strain and
net polarization of the system. This extended framework has recently been used
to study the piezoelectric response of BaTiO3 as a function of temperature, and to
illustrate the influence of electric fields on the phase diagram of this material [6].
   Here, we use this approach to compute the dielectric response of the cubic and
the tetragonal (ferroelectric) phases of BaTiO3 . The tetragonal phase is stable from
approximately 278K to 403K and exhibits a spontaneous polarization that we take
to be along the z axis. The linear dielectric response coefficients (dielectric tensor)
are given, in S.I. units, by εij = ε0 (1 + χij ), where χij is the dimensionless dielectric
susceptibility defined by
                       !                  !
             1 ∂Pi         1   ∂Pi        1
       χij =            ≃              =      β (hPi Pj i − hPi ihPj i) .              (1)
             ε0 ∂Ej σ,T   V ε0 ∂Ej σ,T   V ε0
FIGURE 1. Average polarization vs. electric field for the cubic phase of BaTiO3 at a rescaled
temperature of 500K. Solid triangles and open circles and squares represent the z, x, and y
components of the polarization, respectively.



The approximate equality reflects the neglect of the field derivative of the vol-
ume [7]. Here the averages are to be computed using the extended Boltzmann
factor defined above [8]. According to these equations, one could either compute
the linear dielectric response from direct calculations of the average polarization as
a function of electric field (“direct approach”), or from an analysis of the statistical
correlation between polarization components (“correlation approach”).
   As an example of the direct approach, we show in Fig. 1 the results of a series
of simulations for the cubic phase in which an electric field of progressively greater
magnitude is applied along the z direction. For each field value, the simulation box
(a cube with 10 × 10 × 10 = 1000 unit cells) was allowed to equilibrate for 2×104
Monte Carlo sweeps (MCS) [9] and polarization averages were taken over another
2×104 MCS. A fit to the Pz vs. Ez curve in the linear region corresponding to field
strengths up to approximately 150 kV/cm can be used to extract the dielectric
susceptibility. For higher fields, nonlinear effects are clearly present. It is important
to realize that the nonlinearity is not put in explicitly, as the only extra term in the
simulation is −Ei ∆Pi , which is linear in the field. The nonlinearity appears through
the terms of higher order in the local mode variables {u} (and their coupling to the
strain) in the effective Hamiltonian. A closer analysis of these effects could form
the starting point of an investigation of the nonlinear dielectric response in this
material.
FIGURE 2. Probability histograms for the local mode components in the tetragonal phase,
obtained from a run with 3×105 MCS and an L = 14 simulation box (rescaled temperature: 355
K). The vertical scale is arbitrary.



   The computation of linear response coefficients from the correlation approach
requires only one simulation at zero field, although relatively long runs (of at least
105 MCS) are needed to obtain good statistics. Also, the quality of the calculated
correlations should improve with the size of the simulation box (recall that the
relations in Eq. 1 are strictly valid only in the thermodynamic limit). We have
therefore performed our calculations using larger boxes, with 12 × 12 × 12 = 1728
(L = 12) and 14 × 14 × 14 = 2744 (L = 14) unit cells. Figure 2 shows histograms
for the averages of the three components of the local mode in the tetragonal phase,
computed with an L = 14 box and 3×105 MCS. The profiles are quite clean and
gaussian-looking. The diagonal components of χ (which are the relevant ones for the
tetragonal and cubic phases) are related to the width of the statistical distribution
of the corresponding component of P, and thus to the standard deviation of the
system-average of the local mode amplitudes. Wider distributions (such as those
for the x and y components in Fig. 2) indicate larger values for the corresponding
components of the dielectric tensor.
   Note that the correlation method provides information about the whole ten-
sor from a single run, which is particularly economical when dealing with lower-
symmetry phases. In these cases the use of the direct method becomes more cum-
bersome. For example, the determination of χ33 and χ11 for the tetragonal phase
would involve two separate series of direct calculations, for varying Ez and Ex ,
FIGURE 3. Constant-stress dielectric susceptibility for the tetragonal and cubic phases of
BaTiO3 . Solid circles are experimental data from Ref. [12]. Open symbols represent computed
values, plotted vs. rescaled temperature (see text). Triangles are from direct P vs. E simulations,
and circles and squares are from correlation analysis with L = 12 and L = 14 boxes, respectively.



respectively. In the latter, extra care would be needed at temperatures close to the
transition to ensure that a transverse field does not cause a switch of the sponta-
neous polarization from the z to the x direction.
   Before presenting our results we must discuss an important point regarding the
temperature scale. An effective Hamiltonian based on a finite Taylor expansion
of the energy should not be expected to reproduce perfectly the behavior of the
material at relatively high temperatures. In particular (see Ref. [1]) the theoretical
transition temperatures are progressively shifted downwards with respect to the
true ones [10], the agreement worsening as the temperature increases. This shift
might be related to the neglect of higher order terms in the interaction between
local modes in Heff , as transition temperatures depend basically on the details of
the interaction (as a simple example, recall the Ising model, for which Tc is propor-
tional to the spin-spin coupling J) [11]. In order to provide a better comparison of
our results to experiment, we have therefore linearly rescaled the theoretical tem-
peratures so that the end points of the range of stability of the tetragonal phase
coincide with the experimental Tc ’s. The rescaling is also extrapolated into the
range of stability of the cubic phase. By fixing the points at which phase transi-
tions occur, we are able to focus on the consequences of lattice instability for the
dielectric response. The more important, low-energy regions of the energy surface,
FIGURE 4. Fit of the inverse susceptibility to a Curie-Weiss form. Solid triangles are experi-
mental data from Ref. [12]. Open circles and squares represent values computed from correlation
analysis with L = 12 and L = 14 boxes, respectively.



which are correctly parametrized by our Heff , presumably play the most important
role in determining this response.
   Figure 3 shows the computed constant-stress dielectric susceptibility for the cu-
bic and tetragonal phases, together with recent experimental data [12] for the low-
frequency dielectric response of BaTiO3 [13]. The agreement is excellent, with the
simulations reproducing in detail all the features of the observed behavior, including
the large anisotropy of the dielectric tensor in the tetragonal phase. Our data from
the direct simulation of the P vs. E curves (cubic phase only) and statistical corre-
lation with various box sizes are comparable within the aforementioned limitations
of a finite simulation box. Near the transition temperature Tc the pseudo-divergent
behavior of χ33 can be approximated to a Curie-Weiss form χ−1   33 = C(T −T0 ), where
T0 is a temperature close but not identical to Tc (Figure 4). The fitted values of
the Curie temperature T0 extracted from the tetragonal and cubic phases are very
similar, reflecting the fact that the transition is only weakly first-order. The values
of the Curie-Weiss constants above and below the transition are not related in a
simple way in a first-order transition, but are predicted from mean-field arguments
(Landau theory [14]) to satisfy Cbelow = −2Cabove for a second-order transition. Sim-
ulations with a three-dimensional φ4 model [15] (which could be seen as a simplified
form of our effective Hamiltonian) have shown that this mean-field relationship be-
tween the C constants is only valid in the limit of a pure displacive phase transition,
and that |Cbelow |/2Cabove increases with the degree of order-disorder character. Our
data (and experiment) show that |Cbelow |/2Cabove ≃ 4. Assuming the deviations
from mean-field behavior are similar for our Heff and the φ4 model, this result
would be consistent with the analysis in Ref. [1] pointing to a relatively strong
order-disorder character of the cubic-tetragonal transition in BaTiO3 .
   In conclusion, we have shown how the temperature-dependent dielectric response
of a system can be computed from first principles using an effective Hamiltonian and
Monte Carlo simulations. As an application, we have presented the first calculations
of the dielectric response of BaTiO3 as a function of temperature. The analysis of
the behavior of the dielectric susceptibility in the vicinity of the cubic-tetragonal
transformation gives evidence for a certain degree of order-disorder character in the
transition.
   This work was supported in part by the UPV research grant 060.310-EA149/95
and by the ONR Grant N00014-97-1-0048. We thank J.M. Perez-Mato and Karin
Rabe for useful comments.


                                 REFERENCES

 1. W. Zhong, D. Vanderbilt and K. M. Rabe, Phys. Rev. Lett. 73, 1861 (1994); Phys.
    Rev. B 52, 6301 (1995).
 2. J. Padilla, W. Zhong, and D. Vanderbilt, Phys. Rev. B 53, R5969 (1996)
 3. U. Waghmare and K. Rabe, Phys. Rev. B 55, 6161 (1997).
 4. To relate the net macroscopic polarization to the soft-mode average, thus excluding
    the contributions from other polar modes, is equivalent to assuming that there are
    no anharmonic effects in the dynamics of the other modes, so that their average
    amplitude is zero.
 5. D. Vanderbilt, Phys. Rev. B 41, 7892 (1990).
 6. A. Garcia and D. Vanderbilt, preprint:cond-mat/9712312 (1997).
 7. The linear change in volume is strictly zero by symmetry in the cubic phase, and
    in the tetragonal phase for fields perpendicular to the ferroelectric axis. If an elec-
    tric field is applied along the ferroelectric axis, the longitudinal elongation and the
    transverse contraction are such that the net change in volume is very nearly zero
    (the piezoelectric coefficients satisfy d33 ≃ −2d31 ).
 8. The relationship between χ and the polarization correlations can be simply ob-
    tained by differentiation of the expression ΛhXi = j X j Probj , where Probj is
                                                              P

    the extended Boltzmann factor, Λ is the extended partition function, and X is any
    component of the net polarization.
 9. A Monte Carlo sweep is completed after each local variable is considered for a “flip
    attempt” and each component of the homogeneous strain suffers 2L + 1 attempted
    changes, where L is the linear size of the simulation box.
10. For the rhombohedral to orthorhombic to tetragonal to cubic transition sequence,
    the experimental Tc ’s are respectively 187K, 278K, and 403K, while the theoretical
    ones are 197K, 230K, and 295K.
11. Another possible source of the error in the computed values of transition temper-
    atures is the underestimation by the LDA of the equilibrium lattice constant. The
    simulations are run at a negative effective pressure to compensate for this effect (see
    Ref. [1]).
12. Z. Li, M. Grimsditch, C. M. Foster, and S.-K. Chan, J. Phys. Chem. Solids 57, 1433
    (1996).
13. At high frequencies the strain is not able to follow the polarization and the experi-
    ment measures the constant strain dielectric susceptibility.
14. L. Landau and E. M. Lifshitz, Electrodynamics of Continuous Media (Pergamon,
    Oxford, 1960).
15. S. Radescu, I. Etxebarria, and J.M. Perez-Mato, J. Phys. Cond. Matter 7, 585-95
    (1995)
