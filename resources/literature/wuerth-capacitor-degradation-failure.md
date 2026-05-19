     2.7. Capacitor Degradation and Failure Mechanisms: Exploring Different
                           Causes Across Technologies

                                                    Lukas Hölscher,
                   Würth Elektronik eiSos GmbH & Co.KG, Max-Eyth-Straße 1, 74638 Waldenburg

                                                 Jon Izkue Rodriguez,
                   Würth Elektronik eiSos GmbH & Co.KG, Max-Eyth-Straße 1, 74638 Waldenburg

                                                     Frank Puhane,
                   Würth Elektronik eiSos GmbH & Co.KG, Max-Eyth-Straße 1, 74638 Waldenburg


                                                       ABSTRACT


Capacitors are among the most failure-prone components in many electronic systems. In power supplies and other
continuously operating power electronic equipment, capacitor failure is often the primary cause of system malfunction.
Two distinct concepts are frequently referenced sometimes interchangeably in technical literature: capacitor degradation
(or wear-out) and total failure.
Capacitor Degradation (Wear-Out): This refers to the progressive deterioration of key characteristics, particularly
capacitance and equivalent series resistance (ESR), which may be mission-critical. This process is often non-linear and
tends to accelerate over time due to continued operation under worsening conditions.
Total Failure: Often represented through statistical models such as Failure in Time (FIT) rates and Mean Time Between
Failures (MTBF), total failure may or may not result from prior degradation and/or operating conditions.
This paper summarizes the various causes of both degradation and total failure, analyzing why specific environmental
factors impact certain capacitor types while leaving others largely unaffected.



                                                    INTRODUCTION

Metallized Film Capacitors


Film capacitors are often designed as wound capacitors. In general, there is a distinction based on the structure of the
electrodes. On the one hand, there are the metal film capacitors, in which a metal film essentially alternates with a film
of insulating material, resulting in a three-layer structure when unwound, with the dielectric in the middle. On the other
hand, the majority of film capacitors are manufactured with metallized films. [1, pp. 208-209]
In this process, dielectric films are coated with a thin metal film. These dielectric foils can be made of paper or plastic.
MKP film capacitors are characterized by a high dielectric strength of around 650 V per µm of base film and a very low
dissipation factor of around 0.025 %. [1, p. 216]. A Typical value for the dielectric strength of polypropylene is 400 V
per µm.
                                        Figure 1: Construction of a MKP DC-Link Film Capacitor
The structure of such a capacitor is illustrated in Figure 1 using the WCAP-FTDB DC-Link film capacitor from Würth
Elektronik. The vapor-deposited films are wound tightly with a slight offset (see Figure 1). The plastic box is filled with
a synthetic resin coating, e.g. to protect the winding from moisture. The inductance of the winding is short-circuited by
the complete end contact, resulting in a capacitor with good self-resonance behavior. [1, p. 211]

Electrolytic Capacitors


Most electrolytic capacitors are based on the dielectric aluminum oxide or tantalum oxide. [2, p. 1963]
The basic structure of a radial electrolytic capacitor is illustrated below. It essentially consists of two layers of
aluminum foil with a layer of paper in between. This system is then wound and impregnated with electrolyte. The coil is
placed in an aluminum can, which is sealed with a rubber stopper. A baseplate is added for the SMT mounting
technology.




                            Seperator Paper with Liquid Electrolyte




                                  Figure 2: Construction of a hybrid polymer aluminum capacitor
The layers of the aluminum electrolytic capacitor are composed as follows: The dielectric is formed by an Al2O3 layer.
This can be produced by anodic oxidation on the surface of an aluminum foil. Only part of the aluminum is converted
into an oxide layer by anodic oxidation, which is why the other part acts as an anode. [2, p. 1963]
In addition to classic aluminum electrolytic capacitors, aluminum-polymer and aluminum-hybrid-polymer capacitors
are also used in many areas.
  Figure 3: Internal structure of (left) aluminum electrolytic liquid, (mid) aluminum hybrid polymer and (right) aluminum polymer
                                                               capacitors
Figure 3 illustrate the basic layer structure of the technologies mentioned above.
The main difference here is that a liquid electrolyte is used in classic aluminum electrolytic capacitors (also known as
electrolytic capacitors) and a conductive polymer is used in aluminum polymer capacitors.
Capacitors with conductive polymer are specified by various manufacturers with significantly higher permissible ripple
currents compared to classic aluminum electrolytic capacitors. This can be attributed to the fact that polymer capacitors
and also aluminum hybrid polymer capacitors have a significantly lower ESR (equivalent series resistance) than classic
aluminum electrolytic capacitors.
The aluminum hybrid polymer capacitor is manufactured very similarly to the polymer capacitor, but the winding of the
hybrid polymer capacitor is additionally impregnated with electrolyte.


Supercapacitors (EDLC)

Electric Double Layer Capacitors (EDLCs) are a common type within the family of components known as
Supercapacitors (sometimes referred to as ultracapacitors or gold capacitors by certain manufacturers). Their structure
is, in some respects, similar to that of electrolytic capacitors, featuring a winding of pre-treated aluminum foils with
separator paper in between.




                                 Figure 4: Internal structure of an electric double layer capacitor
The internal structure of an EDLC (see Figure 4) consists of two porous carbon-based electrodes with extremely high
surface area. These electrodes are separated by a thin, ion-permeable separator soaked in an electrolyte. When voltage is
applied, ions from the electrolyte accumulate at the interface between the electrode surface and the electrolyte, forming
electric double layers. This structure allows for rapid charge and discharge without chemical reactions, enabling high
power density and long cycle life.


MLCC


Ceramic capacitors form a wide range of capacitors with different properties. Ceramics are generally understood to be
an inorganic, polycrystalline body that is created by a firing process at high temperatures. MLCCs (Mulitlayer Ceramic
Capacitor) are considered in this work. A schematic structure is shown in Figure 5. These consist of a uniform ceramic
block with comb-like sintered electrodes, which are contacted on the front side by fired metallizations [1].




                       Figure 5: Internal construction of a class I multilayer ceramic capacitor (MLCC)


MLCCs can be broadly categorized into Class 1 and Class 2 types, with Class 3 no longer in use. This classification is
primarily based on the type of ceramic material employed in their construction [1]:
Class 1 MLCCs utilize ceramics with a relatively low dielectric constant, typically ranging from approximately εᵣ = 13
to 500. These capacitors are known for their high stability and precision. Key characteristics include an almost linear
temperature dependence of capacitance, a very low temperature coefficient of approximately ±30 ppm/K, and negligible
aging effects. Additionally, Class 1 MLCCs exhibit no significant voltage dependence in their capacitance, have low
dielectric losses (tanδ ≈ 0.001), maintain small capacitance tolerances, and offer very high insulation resistance. These
properties make them ideal for applications requiring high accuracy and stability.
In contrast, Class 2 MLCCs are based on ferroelectric ceramics and are characterized by a much higher dielectric
constant, typically in the range of εᵣ = 700 to 15,000. These capacitors are designed for applications where higher
volumetric efficiency is needed. However, they exhibit a non-linear dependence of capacitance on both voltage and
temperature, and their temperature coefficient can vary by several percentage points per Kelvin. Class 2 MLCCs also
experience significant aging effects and have a higher loss factor (approximately tanδ ≈ 0.03). Despite these drawbacks,
they still maintain high insulation resistance and can provide extremely high volumetric capacitance, making them
suitable for general-purpose and high-capacitance applications.
                                         FAILURE RATE OF CAPACITORS

Definition


The Mean Time between Failures describes the average time between two failures of a system. Similarly, there is also
the Failure in Time (FIT) specification. This describes failures per billion operating hours and is reciprocal to the MTBF
specification. [3, p. 4]



                                                                10!                                   (1)
                                                    𝑀𝑇𝐵𝐹 =
                                                                𝐹𝐼𝑇

                                                             10!                                      (2)
                                                    𝐹𝐼𝑇 =
                                                            𝑀𝑇𝐵𝐹




FIT/MTBF Calculation (Telcordia Standard)

There are various ways of assessing the reliability of systems. One of these is to calculate the MTBF according to the
Telcordia Technologies Special Report SR-332. [4] These failure rates can be applied to electronic products. In
particular, this approach has been significantly influenced by companies in the telecommunications industry. Failure
rates are not constant, they follow a bathtub curve as shown in Figure 6:




                                         Figure 6: Bathtub curve for failure rates [5]
This also consists of the early failures: here the failure rate is very high but decreases quickly. The standard assumes
that this period covers the first 10,000 hours. In other words, just over a year. Steady state describes a period in which
the failure rates are almost constant. The standard assumes a period of around 20 years.
As an example we look at the failure rate for electrolytic capacitors according to the Telcordia standard. Four different
curves are specified, which differ according to the different stress levels. The stress level is defined as follows in Eq.
(3):
                                                        𝑉"##$%&',)* + 𝑉#&"+,,*                              (3)
                                         𝑠𝑡𝑟𝑒𝑠𝑠[%] =
                                                                  𝑉𝑟




                                    FIT Values for Aluminum Capacitors
         30

         25

         20
                                                                                                                  stress 100%
   FIT   15
                                                                                                                  stress 70%
         10                                                                                                       stress 50%

         5                                                                                                        stress 30%

         0
              0          20            40             60             80             100               120
                                               Temperature [°C]


                           Figure 7: FIT Values for Aluminum Capacitors of Würth Elektronik [5] [4]


Assuming an operating point of 100% nominal voltage and 80 °C, this means that the FIT rate is 13. This value is a
median value. The value for MTBF is then calculated by (1) to approx. 8781 years. This makes it clear at first glance
that this value differs greatly from the service life of electrolytic capacitors.
The MTBF is a measure of the statistical reliability of a large number of systems or components. It therefore differs
from the specification of a lifetime. The lifetime refers to a specific system or component and, using the example of
capacitors, describes how long these components can be operated until they exceed or fall below limit values in relation
to their capacitance or loss specifications. [5]
With regard to capacitors, or more specifically: electrolytic capacitors, it is explicitly pointed out that these components
often switch to the wear-out phase within the first 20 years (assumption for the steady state phase). The standard states
that the failure rates in this case are only valid for the steady state period. [4, p. 57]
Other technologies are covered in the Telcordia standard too, but this is not shown in this paper. Please refer to the FIT
and MTBF document of the respective manufacture or to the Telcordia standard.
The Telcordia standard also does not define exactly when a capacitor is considered to have failed. In contrast, capacitor
manufacturers specify limit values for the capacitors as part of their service life estimation. For this reason, the
degradation mechanisms of different capacitors are discussed in more detail in the next chapter.


                                  DEGRADATION AND LIFETIME ESTIMATION

Aluminum Electrolytic Capacitors


The aging of aluminum electrolytic capacitors and aluminum hybrid polymer capacitors can generally be described
using the Arrhenius equation [6]:

                                                       %!"# &(%# ()%)      𝑉, 0#
                                            𝐿!". = 𝐿$ 2      +$       %        '                                           (4)
                                                                          𝑉-./
                                                      𝐿!". = 𝐿$ 𝐾% 𝐾1 𝐾0                                                    (5)



Where 𝐿- is the initially specified service life. This service life is specified in the manufacturer's data sheets. The
following table is given as an example.




  Figure 8: One example of the lifetime information from the datasheet of one Aluminum Electrolytic Capacitor (Würth Elektronik
          P.N. 865080740005). The permitted degradation during the endurance accelerated test is compiled in this table.
The difference between the maximum specified temperature 𝑇."/ and the sum of the ambient temperature 𝑇/ and the
self-heating Δ𝑇 forms the temperature factor in the above formula. The voltage factor is formed from the nominal
voltage 𝑉0 and the applied voltage 𝑉."/ and the exponent 𝑉/ .
The self-heating due to the ripple current in connection with the ESR of the capacitor is represented by Δ𝑇. The formula
can be divided into a pure temperature factor 𝐾1 and a ripple current factor 𝐾2 . This is shown in formula (5). [6]
Aluminum-polymer capacitors cannot dry out due to the use of a solid material. In this case, ageing is essentially based
on a temperature-dependent change in the materials used. The service life is determined by the following equation:

                                                                     %!"# &%#
                                                  𝐿!".&23". = 𝐿$ 10    4$                                                   (6)

While this modified Arrhenius model fit the temperature dependency, research [7] include a relative humidity
dependency alongside temperature in polymer capacitors, where we may include the more recent hybrid polymer
capacitors. In [7] we see how the exposure to elevated temperature and humidity caused an increase in both ESR and
leakage current in tested solid polymer capacitors. The increase in ESR is attributed to the loss of conductivity of the
PEDOT polymer layer.
In the specific case of H-Chip type polymer aluminum capacitors, also called Multilayer Polymer Capacitors, testing at
high temperature and high humidity (like 85°C / 85%) showed consistent acceleration of failure times as well as failure
modes [8]. Capacitance drop was followed by an increase of leakage current. Due to the different construction and
sealing enclosure, such results should not be assumed to apply for cylindrical “canned” polymer or hybrid polymer
aluminum capacitors.
In experiments using hybrid polymer aluminum electrolytic capacitors, a dependency of bias voltage was reported in [9]
to be approximately 25% increased lifetime when rated voltage was applied.

Metallized Film Capacitor


Various ageing models of film capacitors are collected in the review paper [10]: These include the Arrhenius model and
diverse methods to correct it. Since various factors such as temperature and voltage have a somewhat smaller effect
when applied simultaneously than when the factors are multiplied alone, one model known as Eyring law is used to
generalize Arrhenius to many factors other than temperature [11]. Furthermore, [12] describe an ageing law based on
electrochemical corrosion and investigates degradation due to high ripple currents.
However, analyses aimed at developing a standardized service life formula for film capacitors show that the ageing
parameters can vary significantly depending on the manufacturer, even if the specifications are the same. This can be
seen in [12]. At the same time, some manufacturers indicate lifetime curves in the format shown in Figure 9.
                Figure 9: Example for the expected Lifetime / derating graph from the datasheet of WCAP-FTDB


In addition to models that primarily take pulse voltages into account, there are also papers that deal with the influence of
AC voltage, temperature and humidity. In [13] this is particularly considered in relation to safety capacitors. These
components are designed for particularly good self-healing properties. Therefore, these components are only metallized
with a very thin metallization layer of a few nm. Since these components are operated with AC voltage, the critical
failure mechanism is electrochemical corrosion under AC load and humid environmental conditions. It is a particularly
critical mechanism as some applications require stable capacitance values under harsh environmental conditions. These
include, for example, automotive applications or low power applications where the capacitor is part of a capacitive
power supply. [13]

MLCC


In the last decades two events have shaped the reliability of consumer-grade MLCCs: The transition to Base-Metal-
Electrodes (BME) from more expensive Precious-Metal-Electrodes (PME) and the increasing trend of miniaturization
with high capacitance density components [14].
BME MLCCs, while offering higher volumetric efficiency, are more susceptible to insulation resistance degradation
due to oxygen vacancy electromigration under electric fields. In contrast, PME MLCCs, processed in oxidizing
atmospheres, exhibit more stable long-term reliability. The burn-in process, commonly used for screening, has been
shown to negatively impact BME MLCCs by inducing irreversible defect migration. Additionally, BME capacitors are
more sensitive to electrode morphology, where discontinuities and roughness can significantly elevate local electric
fields and leakage currents. These factors necessitate advanced modeling and quality assessment techniques, such as
TSDC (thermally stimulated depolarization current) and physics-based machine learning, to ensure BME MLCC
reliability in high-reliability applications. [15]
According to [16], the degradation mechanism in BaTiO₃-based BME MLCCs under dc bias is primarily driven by the
electromigration of oxygen vacancies toward the cathode, resulting in asymmetric oxygen distributions within grains
and across grain boundaries. As a result, the activation energy for conduction is reduced and insulation resistance
degrades over time, ultimately compromising device reliability.
On the other hand, the trend for smaller and lighter electronic devices specially in consumer products drive the demand
for high density MLCC packaging. This is sometimes referred to as high CV value (Capacitance * Voltage), which is
achieved by both decreasing the dielectric thickness and increasing the number of electrodes. Highly accelerated
lifetime testing (HALT) with high temperatures and high voltage over specification have determined that the probability
of failure is inversely proportional to dielectric thickness [17]. It has been proposed to establish a minimum requirement
for dielectric thickness for each given voltage rating to prevent early failure in high reliability applications.
From the external (environmental) factors affecting MLCC reliability, the most significant are those that cause cracking
(sometimes also called micro-cracking) in the ceramic structure: During manufacturing component handling and
thermal shock during soldering, and after soldering PCB flexing and other mechanical stress during testing or mounting
in the application [18].




                     Figure 10: Two cross-section images of MLCCs with cracking (Würth Elektronik eiSos).
           Left: high voltage low density 33 nF, 500 V rated, size 1206. Right: High density 1 µF, 25 V rated, size 0805.


Relatively speaking, large cracking planes may create short-circuit conditions or very low insulation resistance, which
may case catastrophic failure or be visible with at plain sight. Other cracking situations and micro-cracking may not
cause an immediate electrical issue, like in the cross-section images in Figure 10. In such cases, long term issues may
arise during operation if the electrodes shift along the cracking plane. Leakage current measurements may not be
adequate to detect it, also at high temperature. A report [18] proposed leakage current testing only after exposure to high
humidity.

Supercapacitors


Like electrolytic capacitors, the wounded electrodes and paper assembly is soaked in a liquid electrolyte and sealed
inside a can to prevent moisture ingress and prevent electrolyte loss. The drying up of the liquid electrolyte is
accelerated by the operating temperature and as such the temperature is the main degradation factor.
But in the case of EDLCs, the applied voltage will play an important role: According to [19] the degradation
mechanism of voltage in Supercapacitors primarily involves side reactions that occur during float charging. Although
EDLCs ideally operate through non-faradaic processes (e.g. like capacitors, without electron transfer happening in the
electrode through electrochemical reactions), prolonged exposure to high voltage leads to irreversible faradaic reactions.
On the positive electrode, electrochemical oxidation consumes oxygen, carbon from the electrode material, and anions
from the electrolyte, forming amorphous films that hinder ion desorption and diffusion. This results in increased
internal resistance and a decline in capacitance. Simultaneously, the negative electrode undergoes electroreduction,
potentially forming similar obstructive layers.
Recent advancements in the modeling of electric double-layer capacitor (EDLC) degradation have highlighted the
limitations of traditional lifetime prediction methods, which often rely on short-term, accelerated aging data. In [20] a
comprehensive study combining long-term endurance measurements at both elevated (65°C) and ambient (24°C)
temperatures with a novel exponential deterioration model is presented. This model incorporates time-dependent
acceleration factors for voltage and temperature, enabling more accurate forecasts of capacitance loss and ESR increase
over operational lifetimes. The findings reveal two distinct degradation phases and demonstrate that commonly used
acceleration factors, such as a constant base of 2 for temperature scaling, may underestimate lifetime under moderate
conditions.
The proposed model not only aligns well with empirical data (achieving mean absolute percentage errors as low as 2%)
but also offers a flexible framework for integrating environmental and operational parameters into lifetime predictions.
By capturing the dynamic nature of degradation rates, the model supports more informed design decisions, such as
component oversizing or voltage derating, to extend service life. These insights are particularly valuable for
applications where reliability and sustainability are critical, reinforcing the need for long-term testing and adaptive
modeling approaches in EDLC reliability engineering.



                                                                                CASE STUDIES

Aluminum Electrolytic Capacitors – measuring electrolyte loss


As mentioned in the previous chapter the service life of electrolytic capacitors is mainly affected by temperature and
applied voltage. High temperatures affects the drying rate of electrolyte in the capacitor and therefore also affect the
capacitance. The manufacturers therefore carry out endurance tests in which the component parameters must not deviate
more than specified in the data sheets (see Figure 8).
To answer the question about the effect of electrolyte loss, the endurance test was performed with additional
intermediate capacitance measurements as well as precise weight measurements. The test was carried out on 10 samples
of the selected THT aluminum electrolytic capacitors of 2200 µF rated capacitance and 10 V of rated voltage.

                                                       0%
                                                                -1%




                 Capacitance and weight change [%]
                                                      -1%
                                                      -2%
                                                      -3%               -4%
                                                      -4%
                                                      -5%                                     -6%
                                                                                                            -6%
                                                      -6%       -5%
                                                      -7%                                                                     -8%
                                                                        -6%
                                                      -8%                                     -7%
                                                                                                            -7%
                                                      -9%
                                                     -10%                                                                    -9%
                                                            0     400         800             1200      1600         2000          2400
                                                                                         Time [h]

                                                                  Average capacitance drift          Average weight change


  Figure 11: Intermediate measurements of capacitance and weight loss during the high temperature test of a 2200 µF / 10 V THT
                                         Capacitor for 2292 hours @ 105 °C and 10 V
In Figure 11 the mean values of the measurements are shown over time. It can be seen that the weight decreases in a
certain way parallel to the capacitance.
Furthermore, the specification end-of-life (endurance definition) allow a maximum change in capacitance of 20%
within the lifetime of 2000 hours. It is noticeable that the mean capacitance drop is well below this value.

Aluminum Polymer and Aluminum Hybrid Polymer Capacitors


In the above chapter, the aim is to calculate the service life based on temperature and voltage. However, especially with
aluminum polymer or aluminum hybrid polymer capacitors, humidity also has an effect on the parameters of the
capacitor. In addition to the leakage current, the ESR changes significantly according to [8] while the Capacitance value
barely changes. To show this influence a measurement under 85°C and 85 % relative humidity was performed for
Aluminum Hybrid Polymer Capacitors. The results are shown in Figure 12.
                                         ESR @100kHz 1000h 85°C/85% Load test
                       0.010



                       0.009
                                                                                                            0 Weeks
                                                                                                            1 Weeks


          ESR in Ohm
                       0.008                                                                                2 Weeks
                                                                                                            3 Weeks
                                                                                                            4 Weeks
                       0.007                                                                                5 Weeks
                                                                                                            6 Weeks

                       0.006
                               DUT1   DUT2   DUT3     DUT4      DUT5      DUT6      DUT7      DUT8

        Figure 12: ESR Measurement of a 33 µF / 63 V Aluminum Hybrid Polymer Capacitor @ 85 °C/85% for 1000 hours
It is clear to see that the ESR increases significantly over time. Nevertheless, after the test, the component remains well
below the ESR value specified in the data sheet of 40mΩ. No noticeable drop in capacitance was measured in this
experiment, which is also shown in [8].


Film capacitors under harsh conditions

As described above, metallized film capacitors, which are used for interference suppression, are particularly susceptible
to the combination of humidity, temperature and applied AC voltage unless special precautions are taken.
In Figure 13 is an example of a standard X2 capacitors being tested at 85°C, 85% relative humidity and 230 VAC for
1000 hours. It is important to note, that this component was not designed to endure such operating conditions in the
application as this is a highly accelerated test. In the same test setup THB (Temperature, Humidity, Bias) X2 capacitors
were tested, too. The result shows that the THB components exhibit significantly better behavior. However, it is also
clear that there are major differences between the manufacturers. Dotted lines are standard X2 capacitors. Solid lines are
THB X2 capacitors.




 Figure 13: Capacitance drop during the 85/85 Test with X2 boxed metalized PP film capacitors from different manufacturers with
                                                    and without THB rating
It is clear to see that the capacitance already drops very sharply at the beginning, until it drops only slightly from around
250 h. With regard to the ESR (not shown in Figure 13), it appears to increase sharply from 700 h. However, the ESR
already increases after the first 100 h. This is an indication that these environmental conditions lead to strong changes in
the component after only a short time.


Multilayer Ceramic Capacitors – long term capacitance loss due to DC-Bias polarization


Although the wear-out mechanisms of multilayer ceramic capacitors (MLCCs) were discussed in the previous chapter,
such degradation is generally not expected under normal operating conditions. Another phenomenon often cited is the
so-called aging of MLCCs. For Class II MLCCs, this is typically characterized by a capacitance loss of approximately
2–5% per decade of time, beginning 24 hours after a thermal reset above the Curie temperature [21]. While this effect is
noteworthy, it does not significantly impact performance in practical applications. Under actual operating conditions (in
the presence of DC and AC signals), the capacitance drift induced by these signals tends to dominate.
Among the various polarization-related effects influencing MLCC performance, the voltage-dependent capacitance
variation is quantitatively the most significant. A long-term effect associated with this dependency has been observed
and characterized [22]. As shown in Figure 14, the rate of stabilization increases with higher DC bias levels, likely due
to enhanced polarization of the dielectric material under stronger electric fields.




 Figure 14: Measured relative capacitance vs time for three different DC voltages in reference to VRated of ceramic capacitor Würth
                                    Elektronik 885012209073 (10 µF, 50 V, 1210 size). [22]
This long-term effect does not belong in the scope of this work, because this effect is reversible by applying a
temperature over the Curie temperature, a process by which the polarized structure of the dielectric will reset. While
this is not a wear-out mechanism, it is still interesting to consider it as a capacitance drop that may cause issues after
just some hundreds of hours of continued operation if the capacitance drops below certain thresholds. Therefore, the
long-term DC bias dependency should be considered in reliability assessments.


Supercapacitors – Electric Double Layer Capacitors over very long time


One noticeable issue overall in the literature is the reliance on accelerated test to measure the effect of different factors
by performing tests at exaggeratedly harsh conditions for the capacitors. Most commonly, high temperature is used to
accelerate wear-out to more practical time frames. Specially in the field of academic research, the limited available time
in dissertations like PhDs or Master Thesis, as well as the temporary nature of some professorship/research tenures
explain the overwhelming preference for highly accelerated life testing (HALT).
Accelerated testing is reasonable specially for quality assessment checks like the endurance test for electrolytic
capacitors, although it might skew some results due to incorrect acceleration models and ignore some of the other
factors that might affect operating life in the field.
One exception of this trend is the ongoing experiment performed on many Würth Elektronik Supercapacitors as
collected by R. Kalbitz’s work [20]. A number of samples were connected to the rated voltage of 2.7 V and let at room
temperature for over 4 years to reproduce the typical configuration of a backup storage based on Supercapacitors.




   Figure 15: Median relative capacitance (left) and ESR (right) vs. time for different batches of capacitor types tested at room
temperature, i.e. 24°C, and permanently applied DC voltage of 2.7 V. The semitransparent area marks the 10th percentile and 90th
                                                        percentile. [20]
One interesting finding that can be extracted by the measurements over time overview in the Figure 15 is that while the
fastest degradation happens in the first 2000 to 3000 hours, the rate of wear-out changes over time. Clearly, the rate of
ESR increase gets slower after about 10000 hours which is more than one year. Another result is that the distribution of
values is relatively large (specially ESR in 3 F capacitors) although consistent over time, which points out that the
differences between parts are due to fabrication differences and not different wear-out severity.



                                            SUMMARY AND CONCLUSIONS


This paper shows the differences between a calculation of the statistical failure rate according to the Telcordia standard
and the lifetime calculation. It becomes clear that an individual lifetime estimation is necessary for electrolytic
capacitors and metalized film capacitors.
In a specific application, we can consider that a “practical End of Life” happens when the capacitor is not able to fulfill
its intended purpose (mostly filtering, decoupling, coupling or energy storage) in the connected electrical system. This
failure to operate may be caused by either a degradation of the key parameters (most commonly capacitance and series
resistance) or a more sudden change in its properties which may cause the capacitor to act like a short or open circuit.
As we have seen, the causes and mechanisms that produce these failure scenarios depend on the capacitor technology.
The variety of dielectric materials as well as manufacturing processes is a consequence of the considerable diversity of
applications and requirements where capacitors are used.
Recently, more researchers ([15] , [23]) are creating and proposing methods using physical-based machine learning to
create predictions that incorporate more stress factors and reduce the measurement time to create quality assessment of
production batches.
                                                         REFERENCES


[1] L. Stiny, Passive elektronische Bauelemente: Aufbau, Funktion, Eigenschaften, Dimensionierung und Anwendung,
    Wiesbaden: Springer Vieweg, 2019.
[2] F. Zach, Leistungselektronik: Ein Handbuch, Wiesbaden: Springer Vieweg, 2022.
[3] M. Berwardt, M. Kreuzpaintner, A. Frehland, B. Stoll, W. Neumärker, R. Gradischnig, C. Gu, B. Schob, S. Roberts, T. Uludag
    and B. Waser, "Mythos MTBF - Korrekte Interpretation einer hilfreichen Maßzahl für Schaltnetzteile," ZVEI e.V. Verband der
    Elektro- und Digitalindustrie, 2023.
[4] I. Telcordia Technologies, Reliability Prediction Procedure for Electronic Equipment, 2011.
[5] Würth Elektronik eiSos GmbH & Co.KG, "WE Standard: WES_FIT-Reliability Data," [Online]. Available: https://www.we-
    online.com/files/pdf1/fit-rate_mtbf_reliability-data.pdf. [Accessed 27 Mai 2025].
[6] P. Suskis, J. Zakis, A. Suzdalenko, H. Van Khang and R. Pomarnacki, "A Study on Electrolytic Capacitor Aging in Power,"
    IEEE 10th Jubilee Workshop on Advances in Information, Electronic and Electrical Engineering (AIEEE), 2023.
[7] J. Romero, M. H. Azarian and M. Pecht, "Reliability analysis of multilayer polymer aluminum electrolytic capacitors,"
    Microelectronics Reliability, September 2020.
[8] A. Shrivastava, M. Azarian and M. Pecht, "Failure of Polymer Aluminum Electrolytic Capacitors under Elevated Temperature
    Humidity Environments," IEEE TRANSACTIONS ON COMPONENTS, PACKAGING AND MANUFACTURING
    TECHNOLOGY, 2017.
[9] T. Ebel, D. Klingshirn and M. Hammerl, "Lifetime Modelling of Hybrid Polymer Aluminium Electrolytic Capacitors for
    Automotive Use," in Energy Conversion Congress & Expo Europe (ECCE Europe), Darmstadt, Germany, 2024.
[10] A. Gupta, O. P. Yadav, D. DeVoto and J. Major, "A review of degradation behavior and modeling of capacitors," NERL
     Publications.
[11] M. Makdessi, A. Sari and P. Venet, "Metallized polymer filmcapacitors ageing law based on capacitance degradation.,"
     Microelectronics Reliability, 2014.
[12] M. Makdessi, A. Sari, P. Venet, P. Bevilacqua and C. Joubert, "Accelerated Ageing of Metallized Film Capacitors Under High
     Ripple Currents Combined With a DC Voltage," IEEE TRANSACTIONS ON POWER ELECTRONICS, 2015.
[13] H. Li, P. Lewin and J. C. Fothergill, "Aging Mechanisms of X2 Metallized Film Capacitors in a High Temperature and
     Humidity Environment," IEEE International Conference on Dielectrics:, 2016.
[14] T. Zednicek, M. Barta, F. Corbett and J. Frodl, "Capacitor Trends and Challenges," in Passive Components Networking
     Symposium, Bucharest, Romania, 2019.
[15] P. Yousefian and C. A. Randall, "Quality assessment and lifetime prediction of base metal electrode multilayer ceramic
     capacitors: Challenges and opportunities," Power Electronic Devices and Components, vol. 6, 2023.
[16] G. Y. Yang, G. D. Lian, E. Dickey, C. Randall, D. E. Barber, P. Pinceloup, M. Henderson, R. Hill, J. J. Beeson and D. J.
     Skamser, "Oxygen nonstoichiometry and dielectric evolution of BaTiO3. Part II—insulation resistance degradation under
     applied dc bias," J. Appl. Phys, vol. 96, no. 12, 2004.
[17] D. Liu and M. J. Sampson, "Some Aspects of the Failure Mechanism in BaTiO3-Based Multilayer Ceramic Capacitors," in
     CARTS International, Las Vegas, NV, USA, 2012.
[18] A. Teverovsky, "Insulation Resistance and Leakage Currents in MLCCs with Cracks," IEEE Transactions on Components,
     Packaging and Manufacturing Technology, 2014.
[19] R. Nozu, M. Iizuka, M. Nakanishi and M. Kotani, "Investigation of the life process of the electric double layer capacitor,"
     Journal of Power Sources, 2008.
[20] R. Kalbitz, "Evaluation and Modeling of Long-Term Endurance Measurement on Electric Double Layer Capacitors to Increase
     Reliability of Lifetime Predictions," SCIEPublish, 2025.
[21] F. Puhane, "Why does the capacity of MLCCs change? Aging," Würth Elektronik eiSos, 2021.
[22] R. Kalbitz and F. Puhane, "Long and Short Term Voltage Dependence," Würth Elektronik eiSos GmbH & Co. KG, ANP123,
     2024.
[23] H. Liu, T. Claeys, D. Pissoort and G. A. Vandenbosch, "Prediction of Capacitor’s Accelerated Aging Based on Advanced
     Measurements and Deep Neural Network Techniques," IEEE Transactions on Instrumentation and Measurement, vol. 69, no.
     11, 2020.
