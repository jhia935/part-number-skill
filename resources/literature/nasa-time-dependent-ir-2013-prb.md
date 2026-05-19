To be published in American Physical Society Physical Review B journal and on nepp.nasa.gov.



Time-Dependent Insulation Resistance Degradation in Multilayer Ceramic
Capacitors with Base-Metal Electrodes
       Donhang (David) Liu

       ASRC Federal Space and Defense, Inc.
       7515 Mission Drive, Suite 200, Seabrook, MD 20706
       Work performed for NASA Goddard Space Flight Center
       8800 Greenbelt Road, Greenbelt, Maryland, 20771, USA


   Insulation resistance degradation in Ni-BaTiO3 multilayer ceramic capacitors has been
   characterized by the measurement of time to failure and DC leakage current as a function
   of stress time under highly accelerated life stress test conditions. The leakage current-time
   dependence follows an exponential law, and a characteristic growth time τSD can be
   determined. A greater value of τSD represents a slower IR degradation process. Oxygen
   vacancy migration and localization at the grain boundary region has resulted in the
   reduction of the Schottky barrier height and has been found to be the main reason for IR
   degradation in Ni-BaTiO3 capacitors. The reduction of barrier height as a function of time
   follows an exponential relation of 𝜙𝜙(𝑡𝑡) = 𝜙𝜙(0)e−2Κt , where degradation rate constant
              𝐸𝐸𝑘𝑘
   𝐾𝐾 = 𝐾𝐾0 𝑒𝑒 −𝑘𝑘𝑘𝑘 is inverse to the mean time to failure (MTTF) and can be simply determined
   using an Arrhenius plot. For oxygen vacancy electromigration, a lower barrier height 𝜙𝜙(0)
   will favor a slow IR degradation process, but a lower 𝜙𝜙(0) will also promote electronic
   conduction and will accelerate IR degradation. As a result, a moderate barrier height 𝜙𝜙(0)
   (and therefore a moderate IR value) with a longer MTTF (smaller degradation rate
   constant 𝐾𝐾) will result in a minimized IR degradation process and the most improved
   reliability in Ni-BaTiO3 multilayer ceramic capacitors.

I. INTRODUCTION
Time-dependent degradation in insulation resistance (IR) related to oxygen vacancy migration has
been considered to be the primary cause of reliability degradation of multilayer ceramic capacitors
(MLCCs) with base-metal electrodes (BME). The behavior is characterized by a slow increase in
the leakage current under an applied direct-current (DC) field stress. In order to reveal IR
degradation in a time-efficient manner, MLCCs are often degraded under highly accelerated life
stress testing conditions (HALST) with different temperatures and applied voltages. Previous
investigation of the IR degradation has shown that the degradation may be caused by three possible



                                                  1
To be published in American Physical Society Physical Review B journal and on nepp.nasa.gov.


factors for BaTiO3-based BME MLCCs: the dielectric layer, the BaTiO3 grain boundaries, and
the Ni-BaTiO3 internal electrode interfaces. 1-4

Unlike traditional BaTiO3-based MLCCs with precious-metal electrodes (PMEs), BME MLCCs
are co-fired in a reducing atmosphere to avoid oxidation of the electrodes. Despite the reoxidation
process, there are still a large number of oxygen vacancies that are accommodated in the BaTiO3
dielectric layers.   The failure mechanism of BME MLCCs is thought to be dominated by
electromigration of oxygen vacancies through the grain boundaries in the dielectric layers.5–8
Waser et al. 9-12 studied the IR degradation in ambient-fired SrTiO3 ceramic and acceptor-doped
single crystal SrTiO3. The results showed that IR degradation begins with oxygen vacancy
electromigration toward the cathode with respect to time, field, and temperature. Segregation of
defects and dopants is found at the grain boundaries during the sintering process and results in the
formation of space charge layers at the grain boundaries. The formation of double Schottky
depletion layers at the grain boundaries of ceramic BaTiO3 and their impact on the properties of
BaTiO3 ceramics was first proposed by Heywang13 in order to explain the unique positive
temperature coefficient of resistance (PTCR) behavior around the Curie temperature, which only
existed in the donor-doped semiconducting BaTiO3 ceramics. Based on this model, the depletion
barriers are formed because of the electron trapping by acceptor states at grain boundaries.
Jonker14-15 later extended the Heywang model, considering the influence of ferroelectric
polarization on resistivity below the Curie temperature. In BaTiO3-based MLCCs, the depletion
layers are believed not only to be depleted of electron carriers and therefore to be highly resistive,
but also to act as electrical barriers against oxygen vacancy electromigration and thus to slow down
the degradation process.2, 10, 16-17 Although both high resistance depletion layers at grain boundaries
and at electrode interfaces limit the electrical conduction of electrons and the transport of oxygen
vacancies across dielectric layers, oxygen vacancy migration is blocked by electrode interfaces,
and a majority of oxygen vacancies are trapped at the electrode interface region and are neutralized
by the reduction of Ti4+ near the cathode. This agrees with a later-published work about the
computational analysis of local atomic configuration and energy at grain boundaries as a result of
the coordination numbers of Ti4+ in the region.18

In this paper, the IR degradation in Ni-BaTiO3 MLCCs was investigated for two commercial BME
capacitors with different reliability levels from the same manufacturer. The capacitors are forced


                                                   2
To be published in American Physical Society Physical Review B journal and on nepp.nasa.gov.


to degrade under HALST conditions at different temperatures and applied voltages. The leakage
currents of the capacitors are monitored and recorded as a function of the stress time until the
capacitors failed electrically. The time-dependence of the leakage current has been found to fit
well to an exponential relationship. A time-dependent Schottky barrier layer model has been
developed with respect to oxygen vacancy migration and localization at grain boundaries. A
temperature-dependent degradation rate constant has been used to describe the IR degradation in
BME MLCCs. The constant is simply an inverse to the MTTF and can be determined in a simple
Arrhenius plot.

II. EXPERIMENTAL PROCEDURE
Two commercial Ni-BaTiO3 MLCCs from the same manufacturer were used for this investigation.
One of them (BME A) is an automotive-grade MLCC device that was qualified per AEC-Q200, a
specification that was developed by the Automotive Electronics Council for passive components
to be used in the harsh automotive environment. The other capacitor (BME B) is a commercial
off-the-shelf product with thin dielectric layers and a high number of dielectric layers designed for
high volumetric efficiency applications. Prior to electrical characterization, both capacitors were
processed for construction and microstructural characterizations. Results are summarized in Table
I.

                             Table I. Construction and Microstructural Information
                              of the Ni-BaTiO3 MLCCs Used in This Investigation
                                      No. of Dielectric         Dielectric     Avg. Grain Size   No. of Dielectric
     Capacitor ID     Specifications
                                           Layers             Thickness (µm)        (µm)         Layers per Grain
 BME A              0.47uF, 50V, 0805        98                    6.39             0.377             16.95
 BME B              4.7uF, 16V, 0805         261                   2.49            0.230              10.83



A 20-position printed circuit board (PCB) testing card was used for the characterization of BME
capacitors throughout this study. All capacitors were convention solder-reflow attached on the
testing card prior to testing. The soldering reflow condition complied with MIL-PRF-55681. No-
clean solder paste with RMA (rosin mildly activated) flux was used. Only one reflow cycle was
applied. After assembly, all capacitors were subject to an electrical test for capacitance, dielectric
loss at 1 kHz, to make sure all units on the board were electrically normal.




                                                          3
To be published in American Physical Society Physical Review B journal and on nepp.nasa.gov.


The leakage current as a function of stress time was monitored in-situ and recorded every 1-3
seconds for each capacitor until the leakage current reached the failure criterion of 100 µA, used
for all stress levels in this study. A series resistor was connected to each capacitor being tested,
for the purposes of current limiting and the reading of the leakage current.

III. RESULTS AND DISCUSSION

A. Characterization of time-dependent leakage current
(1) Failure criterion of degradation
When IR degradation is accelerated under HALST conditions, a certain value of IR or a value of
leakage current must be used as the failure criterion at which the time to failure (TTF) can be
determined. Per MIL-PRF-123, the BaTiO3-based MLCCs for high-reliability applications were
built with a minimum dielectric thickness of 25 µm when the rated voltage is over 50V. In this
case, the leakage current level was very low, even under HALST conditions. The MLCC was
considered a failure when IR at a given stress condition degraded three to four orders below its
initial value.19-20 Waser et al. have also defined characteristic lifetime tch at which the leakage
current has risen one decade above its minimum value to evaluate the degradation rate.10 With the
progress in Ni-BaTiO3 MLCC development, the dielectric thickness was reduced significantly,
even below one micron. As a result, the leakage current has increased significantly, and Ni-BaTiO3
MLCCs are considered to have failed at a fairly low IR value. Some reports define the TTF as the
time at which IR is degraded to a value of 500 kΩ,21-22 1,000 kΩ,23 or 90% of its initial value4 ,
while others set a constant leakage current limit at 100 µA for all of the stress conditions being
used.24-28 After reviewing most of the failure criteria that have been used for determining the TTF
of BaTiO3 MLCCs, this study uses a single current limit of 100 µA to determine the TTF for all
stress levels and for all MLCC samples, based on the following considerations:

During the accelerated life testing, each MLCC was connected in series to a current-limiting
resistor with a DC power supply. The voltage drop across the series resistor was measured and
used to calculate the leakage current of the capacitor. MLCCs with greater dielectric thicknesses
usually require a higher applied voltage to generate enough failures within a reasonable period of
stress time, and the 100 µA limit will result in a higher IR value at a given TTF. On the other
hand, MLCCs with thinner dielectric layers often require a lower applied voltage for degradation

                                                  4
To be published in American Physical Society Physical Review B journal and on nepp.nasa.gov.


and result in a lower IR value for a failure. Since the voltage drop on the current-limiting resistor
depends on the current value, a leakage current higher than 100 µA can result in a voltage drop on
the current-limiting resistor of more than 5% of the overall applied voltage. Although this voltage
drop can be reduced if a smaller-value resistor is used, the voltage value reading on a small resistor
may be too low to ensure the accuracy of the IR measurement. For example, when an MLCC with
a 100 kΩ resistor was accelerated at 150V, the voltage drop will be 100 kΩ∙100µA = 10V, which
is 6.7% of the total applied voltage. For a 1 kΩ resistor, the voltage drop is only 0.1V across the
resistor, which may be too low to show the details of the leakage changing with the stress time. In
this study, the values of the resistor are chosen such that the maximum voltage drop at the resistor
will be no more than 3% of the applied voltage under all stress conditions.
(2) Characteristics of leakage current
FIG. 1 shows measured leakage current data as a function of applied voltage and temperature for
BME A and BME B. All capacitors had a near-linear increase with time to a certain point, and
then some of them failed with a catastrophic failure process, characterized by a time-accelerating
increase in leakage current; others, however, maintained the near-linear increase until 100 µA was
reached. Further details about the characterization of the failure patterns and the method to
determine the acceleration factors have been discussed previously.28

Although the leakage data shown in FIG. 1 appear to be linear for most of the stress time measured,
the curve-fitting results have shown that the exponential form of

                                                        𝑡𝑡−𝑡𝑡0
                                                    �            �
                                     𝐼𝐼 = 𝐼𝐼(𝑡𝑡0 )𝑒𝑒 𝜏𝜏𝑆𝑆𝑆𝑆 ,                                        (1)

actually fits most of the leakage data better than a linear form. In Eq. (1), I is the measured leakage
current, I (t0) is the leakage value at t=t0, and τSD is a characteristic exponential growth time.

FIG. 2 shows curve-fitting results using Eq. (1) for two capacitor samples with different failure
patterns. The C13 with a near-linear increase in leakage fits very well to Eq. (1). Although C7
shows a catastrophic failure characterized by a rapid leakage current increase, the majority of the
leakage data still fit well to Eq. (1), and a comparable τSD to C13 is obtained.




                                                          5
To be published in American Physical Society Physical Review B journal and on nepp.nasa.gov.




FIG. 1. Measured leakage current as a function of stress time for BME A (right), tested at 155°C and
250V (5.0x rated voltage); and for BME B (left), tested at 165°C and 72V (4.5x rated voltage). One early
failure unit was found for the BME A group. The arrow indicates an early failure unit.




FIG. 2. Examples of curve-fitting using Eq. (1) for two BME B capacitor samples with different failure
patterns. Both appear to fit well to the exponential form of Eq. (1).

In general, a larger value of τSD indicates a slower degradation process. The meaning of 𝜏𝜏𝑆𝑆𝑆𝑆 can
be illustrated by the following example:

Let I1 and I2 be the leakages at t1 and t2, respectively, for a slow degradation failure. If one
         𝐼𝐼
assumes 𝐼𝐼2 = 2, then Eq. (1) can be rewritten as:
          1



                                     𝐼𝐼2      𝑡𝑡 −𝑡𝑡       ∆𝑡𝑡
                                             � 2 1�      �      �
                                         = 𝑒𝑒 𝜏𝜏𝑆𝑆𝑆𝑆 = 𝑒𝑒 𝜏𝜏𝑆𝑆𝑆𝑆 = 2,
                                     𝐼𝐼1
and


                                                    6
To be published in American Physical Society Physical Review B journal and on nepp.nasa.gov.

                                                    ∆𝑡𝑡
                                           𝜏𝜏𝑆𝑆𝑆𝑆 = 𝑙𝑙𝑙𝑙(2) ≈ 1.4427 ∙ ∆𝑡𝑡,                       (2)


where ∆t is the time at which the leakage current doubles its value. The greater the value of 𝜏𝜏𝑆𝑆𝑆𝑆 ,
the longer the time span of a degradation failure.

(3) Determination of average 𝝉𝝉𝑺𝑺𝑺𝑺 (〈𝝉𝝉𝑺𝑺𝑺𝑺 〉) and MTTF
To repeat the curve-fitting step using Eq. (1) and to record the TTF at 100 µA, all TTF and τSD
data can be determined. Table II summarizes the TTF and 𝜏𝜏𝑆𝑆𝑆𝑆 data for BME B at 165°C and 72V.
When the leakage current of each MLCC is recorded during the accelerated IR degradation, the
TTF and parameter 𝜏𝜏𝑆𝑆𝑆𝑆 that characterizes the IR degradation rate can both be obtained at a given
stress level.

                Table II. TTF and 𝜏𝜏𝑆𝑆𝑆𝑆 Determined from FIG. 1 for BME B at 165°C and 72V
                             Cap ID on
                           testing board
                                                   TTF (min)                  𝜏𝜏𝑆𝑆𝑆𝑆 (min)
                               C15                   377.26                    1741.10
                               C12                   614.70                    1789.10
                               C16                   712.00                    1705.20
                               C19                   723.40                    1832.80
                               C14                   749.30                    1849.21
                               C10                   766.34                    1881.41
                               C18                   793.25                    1803.03
                                C4                   805.29                    1935.94
                               C17                   866.30                    1866.25
                                C3                   908.27                    2278.60
                                C9                   953.18                    2204.88
                                C2                  1112.39                    2158.85
                                C8                  1124.51                    2104.98
                                C6                  1163.47                    2149.60
                                C0                  1203.19                    2216.00
                                C7                  1235.54                    2426.76
                               C13                  1302.47                    2263.55
                               C11                  1425.38                    2410.67
                                C1                  1515.23                    2574.77
                                C5                  1583.30                    2506.14




                                                          7
To be published in American Physical Society Physical Review B journal and on nepp.nasa.gov.


𝜏𝜏𝑆𝑆𝑆𝑆 has been found to decrease with decreasing TTF, but at a much slower rate, indicating that for
the majority of the time, the capacitors have a similar degradation rate. It has also been noticed
that 𝜏𝜏𝑆𝑆𝑆𝑆 is always longer than TTF. This is true for all of the BME MLCCs from this manufacturer
that have been investigated.

The MTTF can be determined from the Weibull plot of TTF data shown in Table II as:
                                    𝑀𝑀𝑀𝑀𝑀𝑀𝑀𝑀 = 𝜂𝜂𝜂𝜂(1 + 𝛽𝛽 −1 ),                                      (3)

where slope β is the dimensionless shape parameter whose value is often characteristic of the
particular failure mode, η is the scale parameter that represents the point at which 63.2% of the
population has failed, and Γ(x) is the gamma function of x. (Note, for example, that Γ (1+1/β)
ranges from 0.887 to 0.900 as β ranges from 2.5 to 3.5.)

The scale parameter η from the Weibull plot of all 𝜏𝜏𝑆𝑆𝑆𝑆 data shown in Table II is designated to the
average value of 〈𝜏𝜏𝑆𝑆𝑆𝑆 〉. For BME B at 165oC and 72V, the following values were obtained: MTTF
= 998.04 minutes and 〈𝜏𝜏𝑆𝑆𝑆𝑆 〉 = 2189.61 minutes, respectively. The MTTF and 〈𝜏𝜏𝑆𝑆𝑆𝑆 〉 of all MLCC
samples under various stress conditions can be obtained as well if the procedure described above
is repeated.

B. Time-dependent depletion layer height 𝝓𝝓(𝒕𝒕)
Although the formation of a double Schottky barrier layer at a grain boundary as shown in FIG. 3
was initially proposed to explain the PTCR effect in donor-doped semiconducting BaTiO3
ceramics13-15, the same barrier depletion layer model has also been suggested to explain the IR
degradation in Ni-BaTiO3 MLCCs 2, 4. The typical barrier height can be expressed as

                                                     𝑒𝑒 2 𝑁𝑁𝑑𝑑 𝑑𝑑2
                                              𝜙𝜙 =                 ,
                                                       2𝜀𝜀0 𝜀𝜀𝑟𝑟
where Nd is the donor concentration, d is the depletion layer thickness, e is the electron charge,
and 𝜀𝜀0 𝜀𝜀𝑟𝑟 is the dielectric constant. The electro-neutrality condition in the depletion layer satisfies
the following condition:13

                                                     𝑛𝑛𝑠𝑠
                                             𝑑𝑑 =         ,                                           (4)
                                                    2𝑁𝑁𝑑𝑑




                                                       8
To be published in American Physical Society Physical Review B journal and on nepp.nasa.gov.


where 𝑛𝑛𝑠𝑠 is the concentration of trapped electrons at grain boundary acceptor states (cm-2). The
𝜙𝜙 can be re-written as

                                                                   𝑒𝑒 2 𝑛𝑛𝑠𝑠2
                                                            𝜙𝜙 =                .                            (5)
                                                                 8𝜀𝜀0 𝜀𝜀𝑟𝑟 𝑁𝑁𝑑𝑑

Above the Curie temperature, the dielectric constant obeys the Curie-Weiss law,


                                                           𝜀𝜀𝑟𝑟 = C/(𝑇𝑇 −θ),                                 (6)

where θ = 380𝐾𝐾 and C≈1.2×105 is the Curie-Weiss constant.14, 29 Combining Eqs. (5) and (6)
gives rise to
                                                 𝑒𝑒 2 𝑛𝑛𝑠𝑠2     𝑒𝑒 2 𝑛𝑛𝑠𝑠2 (𝑇𝑇 − θ)
                                        𝜙𝜙 =                  =                     .                        (7)
                                               8𝜀𝜀0 𝜀𝜀𝑟𝑟 𝑁𝑁𝑑𝑑      8𝜀𝜀0 𝐶𝐶 · 𝑁𝑁𝑑𝑑

Eq. (7) has been often used to estimate the grain boundary barrier height in semiconducting BaTiO3
ceramics.34, 38 In Ni-BaTiO3 MLCCs, Nd is mainly determined by the bulk concentration of ionized
oxygen vacancies. Although oxygen vacancies migrate under an applied DC field and the weakly
bonded electrons can be trapped by the surface acceptor states, the value of d in Eq. (3) is often in
the submicron range, indicating that Nd >> ns. Therefore, one can assume that Nd(t)≈Nd(0), and is
independent on time. Therefore,

                                    𝑑𝑑𝑑𝑑(𝑡𝑡) 𝑑𝑑     𝑒𝑒 2 𝑛𝑛𝑠𝑠2          𝑒𝑒 2 𝑑𝑑𝑛𝑛𝑠𝑠 (𝑡𝑡)
                                            = �                  �=                      .
                                       𝑑𝑑𝑑𝑑  𝑑𝑑𝑑𝑑 8𝜀𝜀0 𝜀𝜀𝑟𝑟 𝑁𝑁𝑑𝑑    4𝜀𝜀0 𝜀𝜀𝑟𝑟 𝑁𝑁𝑑𝑑 𝑑𝑑𝑑𝑑

                          𝑑𝑑𝑛𝑛𝑠𝑠 (𝑡𝑡)
In order to determine        𝑑𝑑𝑑𝑑
                                        the following facts were considered: 1) 𝑛𝑛𝑠𝑠 (𝑡𝑡) is trapped electrons at
surface acceptor states in the grain boundary regions. The negative space charge due to trapped
electrons is compensated by the formation of a positive space charge region near the grain
boundary, which behaves like a depletion barrier layer to electron conduction. 2) The
computational analysis on the trapping of oxygen vacancies at grain boundaries with respect to
local atomic configuration and energy shows that grain boundaries attract oxygen vacancies and
trap them at specific sites at which local cation density is lower than in the grain interior.30




                                                                    9
To be published in American Physical Society Physical Review B journal and on nepp.nasa.gov.




FIG. 3. Schematic illustration of the formation of a double Schottky barrier around the grain boundary of
a BaTiO3 ceramic capacitor.

3) Since oxygen vacancies behave like donors, they possess positive space charges when ionized.
The same positive space charge in a barrier layer at a grain boundary will thus act as a resistance
for positively charged oxygen vacancy diffusion in a polycrystalline BaTiO3 dielectric. As a result,
when an ionized oxygen vacancy migrates under a DC field and reaches the barrier layer, it has a
tendency to become trapped there. The electro-neutrality condition requires that the weakly
bonded two electrons that are moving in a conduction band now have to be localized in order to
make the trapped oxygen vacancy neutralize and to become part of the crystalline structure. When
Kroger and Vink symbols are used31, the process can be simply described by

                                               𝑉𝑉𝑂𝑂•• = 𝑉𝑉𝑂𝑂 + 2𝑒𝑒 ′ .                                        (8)

As previously reported, the localized electrons that compensate the 𝑉𝑉𝑂𝑂•• localization can be
trapped with the reduction of Ti ions surrounding the 𝑉𝑉𝑂𝑂•• as 𝑇𝑇𝑇𝑇 4+ + 𝑒𝑒′ → 𝑇𝑇𝑇𝑇 3+ , and 𝑇𝑇𝑇𝑇 3+ + 𝑒𝑒′ →
𝑇𝑇𝑇𝑇 2+ .4 The reduction of Ti4+ will now reduce the positive space charge in the positively charged
depletion layer and reduce the barrier height. Since the barrier height is balanced by the trapped
electrons in surface acceptor states 𝑛𝑛𝑠𝑠 (𝑡𝑡), the reduction in barrier height will lower the Fermi
level at grain boundary and then will reduce the 𝑛𝑛𝑠𝑠 (𝑡𝑡). However, with a further increase of
localized electrons as more 𝑉𝑉𝑂𝑂•• are trapped and neutralized, the electrical negative feature
of 𝑛𝑛𝑠𝑠 (𝑡𝑡) will further retard the localization of electrons and reduce the localization rate of 𝑉𝑉𝑂𝑂•• .




                                                      10
To be published in American Physical Society Physical Review B journal and on nepp.nasa.gov.


If we assume ∆𝑛𝑛𝑂𝑂 is the electron concentration that has been localized to make the trapped 𝑉𝑉𝑂𝑂••
neutral, ∆𝑛𝑛𝑂𝑂 should meet the following conditions: at t = 0, ∆𝑛𝑛𝑂𝑂 (0) = 0, and at t→ ∞, ∆𝑛𝑛𝑂𝑂 =
𝑛𝑛𝑠𝑠 (0), i.e., all trapped electrons at t = 0 in the surface acceptor states 𝑛𝑛𝑠𝑠 (0) will eventually be fully
compensated by the localized electrons that neutralize the trapped 𝑉𝑉𝑂𝑂•• . However, with a further
increase of ∆𝑛𝑛𝑂𝑂 as more 𝑉𝑉𝑂𝑂•• are trapped and neutralized, the electrically negative feature of 𝑛𝑛𝑠𝑠 (𝑡𝑡)
will further retard the localization of electrons and reduce the localization rate of ∆𝑛𝑛𝑂𝑂 . Therefore,
the change of ∆𝑛𝑛𝑂𝑂 as a function of t can be expressed by a first-order reaction according to the
reaction rate theory32

                                    𝑑𝑑∆𝑛𝑛𝑂𝑂 (𝑡𝑡)
                                                 = 𝐾𝐾(𝑡𝑡)[𝑛𝑛𝑠𝑠 (0) − ∆𝑛𝑛𝑂𝑂 (𝑡𝑡)],
                                       𝑑𝑑𝑑𝑑

and

                                    ∆𝑛𝑛𝑂𝑂 (𝑡𝑡)                      𝑡𝑡
                                               𝑑𝑑∆𝑛𝑛𝑂𝑂 (𝑡𝑡)
                                �                               = � −𝐾𝐾(𝑡𝑡)𝑑𝑑𝑑𝑑                            (9)
                                  ∆𝑛𝑛𝑂𝑂 (0) ∆𝑛𝑛𝑂𝑂 (𝑡𝑡)−𝑛𝑛𝑠𝑠 (0)    0


where K(t) is the degradation rate constant and 𝑛𝑛𝑠𝑠 (0) − ∆𝑛𝑛𝑂𝑂 (𝑡𝑡) = 𝑛𝑛𝑠𝑠 (𝑡𝑡) is the trapped electron
concentration at surface acceptor states at time t. If ∆𝑛𝑛𝑂𝑂 (𝑡𝑡) is only balanced by 𝑛𝑛𝑠𝑠 (𝑡𝑡) near the
                                      𝐸𝐸𝑘𝑘
Fermi level, 𝐾𝐾(𝑡𝑡) = 𝐾𝐾 = 𝐾𝐾0 𝑒𝑒 −𝑘𝑘𝑘𝑘 can be simplified as a time-dependent constant in which 𝐸𝐸𝑘𝑘 is
the activation energy that is required for 𝑉𝑉𝑂𝑂•• to electromigrate and to be neutralized at a grain
boundary region per Eq. (8) and k is the Boltzmann constant. Since ∆𝑛𝑛𝑂𝑂 (0) = 0, Eq. (9) finally
yields

                                                 𝑛𝑛𝑠𝑠 (0)−∆𝑛𝑛𝑂𝑂 (𝑡𝑡)
                                                                     = 𝑒𝑒 −K𝑡𝑡 ,
                                                        𝑛𝑛𝑠𝑠 (0)
and

                                             ∆𝑛𝑛𝑂𝑂 (𝑡𝑡) = 𝑛𝑛𝑠𝑠 (0)(1 − 𝑒𝑒 −K𝑡𝑡 ),                         (10)

the remaining trapped electrons in acceptor states can be simply expressed according Eq. (10) as
                          𝑛𝑛𝑠𝑠 (0) − ∆𝑛𝑛𝑂𝑂 (𝑡𝑡) = 𝑛𝑛𝑠𝑠 (0) − 𝑛𝑛𝑠𝑠 (0)(1 − 𝑒𝑒 −K𝑡𝑡 ) = 𝑛𝑛𝑠𝑠 (0)𝑒𝑒 −K𝑡𝑡 .

Combining Eqs. (5) and (10) yields a time-dependent barrier height



                                                              11
To be published in American Physical Society Physical Review B journal and on nepp.nasa.gov.


                                        𝑒𝑒 2 [𝑛𝑛𝑠𝑠 (0) − ∆𝑛𝑛𝑂𝑂 (𝑡𝑡)]2
                               𝜙𝜙(𝑡𝑡) =                               = 𝜙𝜙(0)e−2Κt .                       (11)
                                                    8𝜀𝜀0 𝜀𝜀𝑟𝑟 𝑁𝑁𝑑𝑑

This relation indicates that the barrier height will exponentially decrease with time due to the
oxygen vacancy migration and localization at grain boundaries.

C. Determination of degradation rate constant K
The measurement of I-V characteristics of ceramic BaTiO3 inside the grain interior and at the grain
boundary has shown that under an applied field of 100 kV/cm, the current density inside the grain
and at the grain boundary can differ by several orders of magnitude. The difference increases
significantly as temperature increases.33 It is the grain boundary that holds the high resistivity of
the ceramic BaTiO3. If all grain boundaries inside a dielectric layer are assumed to have a uniform
barrier height 𝜙𝜙(𝑡𝑡), the time-dependent resistivity 𝜌𝜌(𝑡𝑡) of an MLCC can be simply written as
                                                                       𝜙𝜙(𝑡𝑡)
                                                                      �       �
                                              𝜌𝜌(𝑡𝑡) = 𝜌𝜌0 𝑒𝑒 𝑘𝑘𝑘𝑘 ,                                       (12)

where 𝜌𝜌0 is the resistivity of the grain. According to Eq. (1), the time-dependent current density
of an MLCC 𝑗𝑗(𝑡𝑡) is
                                                         𝑡𝑡−𝑡𝑡0              𝐸𝐸
                                                     �            �
                                    𝑗𝑗(𝑡𝑡) = 𝑗𝑗(𝑡𝑡0 )𝑒𝑒 𝜏𝜏𝑆𝑆𝑆𝑆 =                  ,
                                                                           𝜌𝜌(𝑡𝑡)
or
                                                       𝐸𝐸 −�𝑡𝑡−𝑡𝑡    0�
                                           𝜌𝜌(𝑡𝑡) =          𝑒𝑒 𝜏𝜏𝑆𝑆𝑆𝑆 ,                                   (13)
                                                    𝑗𝑗(𝑡𝑡0 )
where 𝑗𝑗(𝑡𝑡0 ) is the current density at t = 𝑡𝑡0 and E is the applied field. Combining Eqs. (12) and
(13) results in
                                    𝜙𝜙(𝑡𝑡)                  𝜙𝜙(0)e−2Κt      𝐸𝐸            𝑡𝑡 − 𝑡𝑡0
               𝜌𝜌(𝑡𝑡) = 𝜌𝜌0 𝑒𝑒𝑒𝑒𝑒𝑒 �       � = 𝜌𝜌0 𝑒𝑒𝑒𝑒𝑒𝑒 �            �=       𝑒𝑒𝑒𝑒𝑒𝑒 �−           �,
                                     𝑘𝑘𝑘𝑘                       𝑘𝑘𝑘𝑘      𝑗𝑗(0)              𝜏𝜏𝑆𝑆𝑆𝑆

at a given stress level, E is a constant, so that

                                            𝑡𝑡 − 𝑡𝑡0     𝜙𝜙(0) −2Κt
                                                      ≈−       e    .                                     (14)
                                               𝜏𝜏𝑆𝑆𝑆𝑆     𝑘𝑘𝑘𝑘

Using 〈𝜏𝜏𝑆𝑆𝑆𝑆 〉, the average of 𝜏𝜏𝑆𝑆𝑆𝑆 , to replace 𝜏𝜏𝑆𝑆𝑆𝑆 , and 𝑒𝑒 −𝑥𝑥 ≈ 1 − 𝑥𝑥 when x is small, the integration
of Eq. (14) results in



                                                            12
To be published in American Physical Society Physical Review B journal and on nepp.nasa.gov.

               𝑀𝑀𝑀𝑀𝑀𝑀𝑀𝑀                         𝑀𝑀𝑀𝑀𝑀𝑀𝑀𝑀                       𝑀𝑀𝑀𝑀𝑀𝑀𝑀𝑀
                          𝑡𝑡 − 𝑡𝑡0                       𝜙𝜙(0) −2Κt                     𝜙𝜙(0)
           �                         𝑑𝑑𝑑𝑑 = − �                ·e   𝑑𝑑𝑑𝑑 ≈ − �                (1 − 2𝐾𝐾𝐾𝐾)𝑑𝑑𝑑𝑑,
            0              〈𝜏𝜏𝑆𝑆𝑆𝑆 〉           0          𝑘𝑘𝑘𝑘                0          𝑘𝑘𝑘𝑘



and

                                                1         𝜙𝜙(0)          1
                                                        ≈       �𝐾𝐾 −          �.
                                             2〈𝜏𝜏𝑆𝑆𝑆𝑆 〉    𝑘𝑘𝑘𝑘       𝑀𝑀𝑀𝑀𝑀𝑀𝑀𝑀

This gives rise to
                                       1                𝑘𝑘𝑘𝑘                  𝐸𝐸𝑘𝑘
                                             = 𝐾𝐾 −                 ≈ 𝐾𝐾0 𝑒𝑒 −𝑘𝑘𝑘𝑘 .                             (15)
                                    𝑀𝑀𝑀𝑀𝑀𝑀𝑀𝑀        2𝜙𝜙(0)〈𝜏𝜏𝑆𝑆𝑆𝑆 〉

Eq. (15) is exactly the Prokopowicz-Vaskas equation where applied voltage is a constant!35 The
degradation rate constant K can now be simply determined by an Arrhenius plot using the MTTF
data obtained at various temperatures and at a constant voltage.

Table III summarizes MTTF data at a given voltage and different temperatures for BME A and
BME B. A corresponding Arrhenius plot according to Eq. (15) is shown in FIG. 4. The activation
energy 𝐸𝐸𝑘𝑘 and degradation rate constant K can also be calculated.

                Table III. Calculated MTTF Data from a Weibull Plot of Measured TTF Data
                                Temperature K              MTTF (hours)
                                 BME B at 72V (4.5 times the rated voltage)
                                      408                       384.75
                                      428                        50.50
                                      438                        16.63
                                      448                        6.46
                                BME A at 250V (5.0 times the rated voltage)
                                      428                       546.00
                                      438                       136.80
                                      448                        24.11



Table IV lists the activation energy 𝐸𝐸𝑘𝑘 and constant 𝐾𝐾 at several temperatures for two BME
capacitors. The barrier height 𝜙𝜙(𝑡𝑡) at the time the first catastrophic failure occurred can be
estimated using Eq. (11) and the obtained K values in Table IV. For BME B, a 55% reduction
of 𝜙𝜙(0) can be calculated at 6.3 hour and 165°C when the average leakage current level is ~60 µA

                                                              13
To be published in American Physical Society Physical Review B journal and on nepp.nasa.gov.


(FIG. 1). For BME A, a 70% reduction at 367 hours and 155°C is obtained when the average
leakage current level is ~80 µA. These results clearly show that a smaller value of the degradation
rate constant K results in a slower IR degradation and a larger value of MTTF for the automotive-
grade BME MLCC BME A than for BME B.

                                       0.0
                                       -1.0
                                                         BME B


                         Ln [1/MTTF]
                                       -2.0
                                                                              y = -18.727x + 39.916
                                       -3.0
                                                                                    R² = 0.999
                                       -4.0
                                       -5.0
                                                                     BME A
                                       -6.0
                                              y = -32.616x + 69.53
                                       -7.0         R² = 0.992
                                       -8.0
                                           2.20      2.25      2.30        2.35    2.40     2.45      2.50
                                                                       1000/T

FIG. 4. Arrhenius plots using Eq. (15) and MTTF data in Table IV for BME capacitors BME A and BME
B.

           Table VI. Calculated Degradation Constant per the Curve-Fitting Results in FIG. 4
                                                                           −𝐸𝐸𝑘𝑘
           Part ID                                               𝐾𝐾0 𝑒𝑒 𝑘𝑘𝑘𝑘 (ℎ𝑜𝑜𝑜𝑜𝑜𝑜 −1 )
                                       Ek (eV)       at 398K (125 C) at 428K (155oC)
                                                                 o
                                                                                                   at 438K (165oC)
           BME A                        2.590           8.865E-06             1.711E-03               8.423E-03
           BME B                        1.623           7.953E-04             2.152E-02               5.844E-02


D. IR degradation mechanism due to oxygen vacancy electromigration
According to Eq. (11), the barrier height degrades with an exponential relationship to stress time
and can be expressed as

                                                          𝜙𝜙(𝑡𝑡) = 𝜙𝜙(0)e−2Κt ,
                 −𝐸𝐸𝑘𝑘
where 𝐾𝐾 = 𝐾𝐾0 𝑒𝑒 𝑘𝑘𝑘𝑘 is the degradation rate constant. A slower degradation requires a smaller value
of degradation constant K or a large value of 𝐸𝐸𝑘𝑘 , which is the activation energy required for 𝑉𝑉𝑂𝑂•• to
migrate and to be neutralized near the depletion layer at grain boundaries. Its value can be solely
determined by the MTTF at a given stress level. The large value of 𝐸𝐸𝑘𝑘 also means that the
entrapment of 𝑉𝑉𝑂𝑂•• at grain boundaries may not be an energetically favorable process unless the

                                                                      14
To be published in American Physical Society Physical Review B journal and on nepp.nasa.gov.


barrier height 𝜙𝜙(𝑡𝑡) is high enough to be comparable to 𝐸𝐸𝑘𝑘 . This is the case for BME B, where a
typical barrier height value of 1.30 eV has been reported.4

On the other hand, according to Eq. (14), a slower degradation, characterized by a larger value of
〈𝜏𝜏𝑆𝑆𝑆𝑆 〉, would give rise to a smaller value of 𝜙𝜙(0). This can be understood since a smaller 𝜙𝜙(0)
will promote the continuous electromigration of 𝑉𝑉𝑂𝑂•• without being trapped or localized at a grain
boundary and cause an IR degradation (based on the degradation model proposed here, only those
oxygen vacancies that have been trapped and neutralized will contribute to IR degradation).
However, this is only one part of the equation: 𝜙𝜙(0) also presents the barrier height for the
conduction band electron carriers. A lower 𝜙𝜙(0) will facilitate electron conduction and will
deteriorate the IR as well.        As a result, when electron conduction and oxygen vacancy
electromigration are both taken into account, a moderate barrier height and a smaller K are the
keys for minimal IR degradation in Ni-BaTiO3-based MLCCs. As an important conclusion of this
study, higher IR values may not always result in a larger MTTF, but a slower IR reduction rate
(smaller K) always will. A higher 𝜙𝜙(0) generally means higher resistance and therefore a higher
electrical strength when a DC voltage is applied. This highly localized electric strength is more
likely to cause the thermal-related electrical breakdown of the depletion layer and a reduction in
the reliability life of the MLCCs.

According to Eq. (4), 𝑁𝑁𝑑𝑑 ≫ 𝑛𝑛𝑠𝑠 , only a small fraction of oxygen vacancies will be trapped at the
grain boundaries during the electromigration across the dielectric layer and will cause IR
degradation. The majority of 𝑉𝑉𝑂𝑂•• will continually migrate and eventually reach the dielectric layer
and internal Ni electrode interface, as has been revealed by previously reported electron energy
loss spectroscopy (EELS) and high-resolution transmission electron microscope (HRTEM)
observations.4

Since there is no evidence to show that 𝑉𝑉𝑂𝑂•• can be transferred across the cathode electrode layer,
4, 10
        most 𝑉𝑉𝑂𝑂•• capable of migration will pile up along the Ni-electrode dielectric interface. To
neutralize these vacancies, a significant amount of electrons is required, which can only be
obtained from the cathode electron injection. The energy required for cathode electron injection
must be much smaller than that of the Schottky barrier height at the dielectric-electrode interface
(~1.25 eV36). The high concentration of localized electrons due to the compensation of the pile-


                                                   15
To be published in American Physical Society Physical Review B journal and on nepp.nasa.gov.


up of oxygen vacancies will not only dramatically change the local stoichiometry of BaTiO3
dielectric, but it will also lead to a leakage current increase during IR degradation. This will cause
a local temperature increase and will eventually lead to the breakdown at the Ni-BaTiO3 interface.
The initial failure site of the dielectric-electrode interface was revealed in a recently published
failure analysis work on commercial BME MLCCs.37


IV. SUMMARY AND CONCLUSIONS

Two commercial BME capacitors with different quality levels were degraded under highly
accelerated life test conditions to reveal the time-dependent IR degradation. The leakage current
as a function of stress time was recorded in-situ for every capacitor sample tested. The leakage
current data were found to fit well to an exponential relationship to the stress time and can be
characterized by a characteristic growth time of τSD. τSD is the time at which the leakage current

doubles its value and is therefore a measure of the degradation rate. The larger the value of τSD,
the larger the MTTF.

The double Schottky barrier layer model at the ceramic grain boundary has been used to describe
the resistivity of a BME capacitor. The barrier height 𝜙𝜙(𝑡𝑡) as a function of time has been found
to follow
                                         𝜙𝜙(𝑡𝑡) = 𝜙𝜙(0)e−2Κt ,

                                                          𝐸𝐸𝑘𝑘
where the degradation rate constant 𝐾𝐾 = 𝐾𝐾0 𝑒𝑒 −𝑘𝑘𝑘𝑘 can be determined by the traditional
Prokopowicz-Vaskas equation with respect to MTTF:
                                            1               𝐸𝐸𝑘𝑘
                                                  ≈ 𝐾𝐾0 𝑒𝑒 −𝑘𝑘𝑘𝑘 .
                                         𝑀𝑀𝑀𝑀𝑀𝑀𝑀𝑀

BME MLCCs with a larger MTTF should have a slower degradation rate and thus a smaller value
of K.

On the other hand, the exponential growth time 𝜏𝜏𝑆𝑆𝑆𝑆 determined during curve-fitting of the leakage
current data has been found to relate to barrier height as

                                       𝑡𝑡 − 𝑡𝑡0     𝜙𝜙(0) −2Κt
                                                 ≈−       e    ,
                                          𝜏𝜏𝑆𝑆𝑆𝑆     𝑘𝑘𝑘𝑘

                                                   16
To be published in American Physical Society Physical Review B journal and on nepp.nasa.gov.


indicating when temperature and time are constant, 𝜏𝜏𝑆𝑆𝑆𝑆 is inverse to the grain boundary barrier
height 𝜙𝜙(0). This is due to the fact that a smaller 𝜙𝜙(0) will promote the electromigration of 𝑉𝑉𝑂𝑂•• ,
but there will be no entrapment at a grain boundary to cause an IR degradation. However, 𝜙𝜙(0)
is also the barrier for the conduction band electron carriers. A lower 𝜙𝜙(0) will facilitate the
electronic conduction and deteriorate IR as well. When electron conduction and oxygen vacancy
migration are both taken into account, a moderate barrier height 𝜙𝜙(0) and a small degradation rate
                 𝐸𝐸𝑘𝑘
constant 𝐾𝐾0 𝑒𝑒 −𝑘𝑘𝑘𝑘 are crucial for minimal IR degradation in Ni-BaTiO3-based MLCCs.

In conclusion, higher IR values may not always result in an increased MTTF, but a slower rate of
IR degradation, characterized by a smaller K, always will.

Acknowledgements

The author appreciates the NASA Electronic Parts and Packaging (NEPP) program’s support for
this study. The author also expresses his gratitude to Michael Sampson and Bruce Meinhold for
reviewing the manuscript. The author would also like to thank the GSFC Code 562 Parts Analysis
Laboratory for assistance with electrical testing.

References:
 1
      H. Kishi, Y. Mizuno, and H. Chazono, Jpn. J. Appl. Phys., Part 1 42, 1 (2003).
 2
      H. Chazono and H. Kishi, Jpn. J. Appl. Phys., Part 1 40, 5624 (2001).
 3
      G. Y. Yang, G. D. Lian, E. C. Dickey, and C. A. Randall, D. E. Barber, P. Pinceloup, M. A. Henderson, R. A.
      Hill, J. J. Beeson, and D. J. Skamser, J. Appl. Phys., 96, 7492 (2004).
 4
      G. Y. Yang, G. D. Lian, E. C. Dickey, and C. A. Randall, D. E. Barber, P. Pinceloup, M. A. Henderson, R. A.
      Hill, J. J. Beeson, and D. J. Skamser, J. Appl. Phys., 96, 7500 (2004).
 5
      K. Morita, Y. Mizuno, H. Chazono, and H. Kishi, Jpn. J. Appl. Phys., Part 1 41, 6957 (2002).
 6
      H. Chazono and H. Kishi, Key Eng. Mater. 248, 183 (2003).
 7
      D. F. K. Hennings, J. Eur. Ceram. Soc. 21, 1637 (2001).
 8
      K. Albertsen, D. Hennings, and O. Steigelmann, J. Electroceram. 2, 193(1998).
 9
      R. Waser, J. Am. Ceram. Soc. 72, 2234 (1989).
 10
      R. Waser, T. Baiatu, and K. H. Härdtl, J. Am. Ceram. Soc. 73, 1645 (1990).
 11
      R. Waser, T. Baiatu, and K. H. Härdtl, J. Am. Ceram. Soc. 73, 1654 (1990).
 12
      T. Baiatu, R. Waser, and K. H. Härdtl, J. Am. Ceram. Soc. 73, 1663 (1990).
 13
      W. Heywang, J. Am. Ceram. Soc., 47, 484 (1964).
 14
      G. Jonker, Solid State Electron. 7, 895 (1964).


                                                          17
To be published in American Physical Society Physical Review B journal and on nepp.nasa.gov.

 15
       G. Jonker, Mat. Res. Bull., 2, 401 (1967).
 16
       M. Vollman and R. Waser, J. Am. Ceram. Soc. 77, 235 (1994).
 17
       H. Kishi, Y. Mizuno, and H. Chazono, Jpn. J. Appl. Phys., Part 1 42, 1 (2003).
 18
       T. Oyama, N. Wada, H. Takagi, and M. Yoshida, Phys. Rev. B 82, 134107 (2010).
 19
       W. Minford, IEEE Transactions on Components, Hybrids, and manufacturing Tech., 5, 297 (1982).
 20
       H. Pak, and B. Rawal, Proc. SPIE 3235, 362 (1997).
  21
       M. Randall, A. Gurav, D. Skamser, and J. Beeson, CARTS Proceedings, Scottsdale, AZ, 134 (2003).
 22
       J. Yoon, K. Lee, and S. Lee, Tran. On Electrical and Electronic Mater. 10, 1229 (2009).
 23
       M. Cozzolino, CARTS Proceedings, Orlando, FL, 385, (2006).
 24
       T. Ashburn and D. Skamser, Proceedings of the 5th SMTA Medical Electronics Symposium, 124 (2008).
 25
       J. Paulsen and E. Reed, Microelectronics Reliability 42, 815 (2002)
 26
       D. Liu and M. Sampson, CARTS Proceedings, Jacksonville, FL, 45 (2011).
 27
       D. Liu and M. Sampson, CARTS Proceedings, Las Vegas, NV, 59 (2012).
 28
       D. Liu, CARTS Proceedings, Houston, TX, 235 (2013).
 29
       D. Viehland, S. Jang and L. E. Cross, M. Wuttig, Phys. Rev. B 46, 8003 (1992).
 30
       T. Oyama, N. Wada, and H. Takagi, and M. Yoshiya, Physical Review B 82, 134107 (2010).
 31
       F. Kröger and H. J. Vink, in Solid State Physics, 307, (Academic Press, New York, 1956).
 32
       K. Connors, Chemical Kinetics, the study of reaction rates in solution, (VCH Publishers, New York, 1991).
 33
       T. Nakamura, T. Yao, J. Ikeda, N. Kubodera, and H. Takagi, IOP Conf. Series: Materials Science and
       Engineering 18, 2007 (2011).
 34
       E. Brzozowski and M. Castro, Journal of the European Ceramic Society 24, 2499 (2004).
 35
       T. I. Prokopowicz and A. R. Vaskas, Final Report ECOM-90705-F, NTIS AD-864068, (Oct. 1969).
 36
       A. Polotai, I. Fujii, D. Shay, G. Yang, E. Dickey, and C. Randall, J. Am. Ceram. Soc., 91, 2540 (2008).
 37
       R. Weachock and D. Liu, CARTS Proceedings, Houston, TX, 165, (2013).
 38
       J. Illingsworth, H. AI-Allak, and A. Brinkman, J. Phys. D: Appl. Phys. 23, 971 (1990).




                                                          18
