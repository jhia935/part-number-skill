          HIGH CV MLCC DC/AC BIAS AGEING
           CAPACITANCE LOSS EXPLAINED
                                  Tomas Zednicek Ph.D.,
                  president of EPCI European Passive Components Institute
                                tom@passive-components.eu

update:23.9.2019 based 2nd PCNS Passive Components Networking Symposium 10-13th
September 2019, Bucharest, Romania Hot Panel Discussion inputs



                                       1. Introduction
MLCC capacitors are dominating today’s capacitor market enabling high grade of electronics
miniaturization. The continuous downsizing and use of higher and higher dielectric constant
materials for MLCC class II capacitors has however resulted in worsening of some electrical
parameters such as capacitance drop at DC voltage operating conditions. Thus, in consequence,
what can be considered as an enabling technology for consumer and wearable applications may
pose some risk if used in critical applications such as automotive, safety, medical or industrial
sector, that are also in need for continuous miniaturization.

Understanding of this behaviour in the worst-case application conditions is necessary for
reliable designs. Capacitance loss data are available from MLCC manufacturers today as
“typical” performance in simulation softwares or product datasheets. However, critical safety
electronic system designers are looking for “guaranteed” characteristics to be able to count with
the “worst case” scenario. Aim of this article is to explain basics, provide some guidelines on
MLCC class II capacitance loss phenomenon, suggest some design rules, recommendations and
initiate discussion within the passive components industry.

The past PCNS 2019 Passive Components Networking Symposium [1] introduced MLCC
Class II DC BIAS & Ageing Capacitance Loss as the Hot Panel Discussion Topic by five
MLCC manufacturers (AVX Corporation, Kemet Electronics, Murata Electronics Europe,
Samsung Electro-Mechanic, Wuerth Elektronik) and Continental Automotive as the end
automotive user representative at the round table open discussion.

                                2. Technical Background
2.1. MLCC Capacitance Ageing with Time

The MLCC class II capacitors are using BaTiO3 ferroelectric materials as a high dielectric
constant material to achieve its very high capacitance values in small dimensions. Downside of
this material is its strong dependency on operating conditions – namely loss of capacitance –
with DC Voltage (DC BIAS), AC Voltage, temperature and ageing with time. In addition, piezo
noise may degrade smoothing capabilities of these capacitors at certain condition.

BaTiO3 has a cubic crystal structure above the Curie temperature (approx. 125°C or more), but
below the Curie temperature it turn into a different crystal structure (tetragonal) that creates a
dipole, respectively domains of dipoles with different dipole orientations that reduces its
original polarization and thus reduces its capacitance values (spontaneous polarization, no
voltage applied). The dielectric grain size/shape/distribution may impact number of dipoles and
domains and thus the level of capacitance loss. As this structure changes with time, dielectric
constant is reduced and over time, the capacitance will continue to decline.




                Table 1. MLCC typical aging and referee time. source: Kemet

Capacitance Ageing effect depends to MLCC dielectric type and it is constant per time decade
(so the process slow down exponentially). Typical values see Table 1 above.

As the capacitance decrease with time and it’s important to remove some of the other “short
term” mechanisms impact, the reference time for capacitance value reading and its tolerances
is set with some time delay.

Various manufacturers use different time, but the most common reference points are 48h or
1000hrs as also shown in table 3. with note that manufacturers are measuring capacitance with
one day or twenty-four hours after “last heat” that is also in accordance to MIL specification
conditions. (Re)heating to Curie temperature “reset” the structure and returns capacitance
value to its initial value.

2.2. MLCC Capacitance with Temperature

Depending to the dielectric type, capacitance change with temperature – see Fig.1. This is
well defined per international standards and even the dielectric class is indicating the
temperature stability including its tolerance field as shown in Table 1.




 Fig 1. Capacitance change with temperature for selected ceramic dielectric types; source:
                                      Wikipedia
2.3. MLCC Class II Capacitance with DC BIAS

Some of the BaTiO3 dipoles are blocked by DC voltage and it cannot move further with small
AC voltage changes resulting in loss of capacitance. Capacitance loss due to DC BIAS is the
most important contributor for real capacitance value at the operating conditions.

The level of Capacitance loss (number of blocked dipoles) is proportional to the DC field
(V/mm), thus capacitor with thinner dielectric and higher volts per dielectric thickness exposure
will exhibit higher capacitance loss with DC BIAS. Type and structure of the dielectric (grain
size, shape, distribution, impurities) may have also a significant impact to the capacitance loss
level.

In consequence, the capacitance loss level may increase with higher CV density (high
capacitance in small dimensions) and it may be part number and manufacturer specific. See
figure 2. below as an example of 10μF 6.3V MLCC X7R 0805 case capacitance loss with DC
BIAS differences between three manufacturers. The loss at rated voltage can vary from -35%
to -65% and even at more likely used derated conditions at 3.3V it can be from -12 to -32%,
that may result in quite significant in-circuit performance among different manufacturers.




   Figure 2. Capacitance loss with DC BIAS on 10μF 6.3V MLCC X7R 0805 case by three
              different vendors; source: EPCI using manufacturers’ datasheets

It may be of critical importance to evaluate such characteristics when qualifying alternative
MLCC manufacturer under the current tight supply market situation.

The drop of capacitance due to DC BIAS is not happening immediately, but some time is needed
for slower dipoles to be completely blocked. Thus, we can see some fast-immediate drop of
capacitance at time close to zero after DC Voltage plug in, and some additional drop within
tenth of minutes to hour(s) to get to final capacitance drop level. See Figure 3.

Once all dipoles are blocked there is no further significant impact of DC voltage in longer
timeframe. The capacitance value still continues to decrease per every decade by spontaneous
polarisation as discussed in chapter 1., but this phenomenon is not linked to applied DC voltage.
MLCC manufacturers use to talk about behaviour of the capacitor in decades … so what
happens in first decade, second decade etc. as this is directly link to physical mechanisms and
its impact to overall performance.
Example of the capacitance drop with time can be seen in Figure 3. sourced by Panasonic in
their example of tantalum polymer capacitance stability versus MLCC.




      Figure 3. Capacitance drop with time under DC Voltage BIAS; source: Panasonic

The Capacitance loss with DC BIAS effect can be reduced by using a physically larger case
size design that reduces V/mm electrical field exposed to the dielectric. See Fig.4 as an example
of capacitance loss with DC BIAS voltage comparison on 10μF 6.3V X5R between 0805 and
0603 case sizes. Another choice, if applicable, is to use a higher-grade dielectric type material
such as moving from X5R to X7R or X7R to X8R or tighter tolerance field e.g. moving from
X7R to X7P types (as per Table 2.). See Fig.5 as an example of capacitance loss with DC BIAS
on 1uF 6.3V 0402 capacitor comparison between X5R and X7R types.

                                   Capacitance DC BIAS loss dependence to CASE SIZE
                                      0
                                   -0.1
                                   -0.2                               0603 10uF 6.3V X5R


                       dC/C [%]
                                   -0.3                               0805 10uF 6.3V X5R
                                   -0.4
                                   -0.5
                                   -0.6
                                   -0.7
                                   -0.8
                                   -0.9
                                          0       2          4            6            8
                                                        DC BIAS [V]


   Fig.3 example of 0805 vs 0603 10μF 6.3V X5R capacitance loss with DC BIAS voltage

                                  Capacitance DC BIAS loss to DIELECTRIC TYPE
                                   0%
                                  -10%                                X5R 0402 1uF 6.3V
                                  -20%                                X7R 0402 1uF 6.3V


                      dC/C [%]
                                  -30%
                                  -40%
                                  -50%
                                  -60%
                                  -70%
                                  -80%
                                          0      2           4             6               8
                                                        DC BIAS [V]


   Fig.4 example of X5R vs X7R capacitance loss with DC BIAS voltage on 1uF 6.3V 0402
2.4. MLCC Class II Capacitance with AC Voltage

Ferroelectric materials (BaTiO3) exhibit some hysteresis in polarization as a function of electric
field that is causing MLCC capacitance dependency also to AC voltage. The level depends
mainly to the dielectric type as shown in Figure 6.




Figure 6. Capacitance change with AC voltage by different dielectric types; source: Murata

The reference standard capacitor AC volt measure conditions are set to 1Vrms at 1kHz and
room temperature. Nevertheless, there are number of MLCC capacitor applications that are
operating at significantly lower AC voltage such as 10mV. In this case we can expect
capacitance drop of capacitance due to the small AC voltage in range of additional -5 to -15%.

The “AC voltage hysteresis” is also “re-settable” by heating of the capacitor to Curie
temperature.

2.5. Summary of MLCC class II capacitance loss behaviour in operating conditions.

MLCC class II capacitors are offering very high level of energy density in miniature sizes that
is enabling wide range of modern digital devices. On the other hand, the high capacitance
density is “compensated” by inferior electrical parameters that may or may not be critical in the
specific application area.

There is an multiplication effect of operating conditions that may cause significant loss of
capacitance on MLCC Class II capacitors in real application conditions.

for example – if you select a X5R 0805 10uF 6.3V capacitor as 5V coupling capacitor in
operating amplifier the capacitor may exhibit (depending to manufacturer):

   •   -60% drop of capacitance due to DC voltage 5V close to 6.3V maximum rated voltage
       (as per typical data provided by manufacturer)
   •   -15% drop of capacitance due to AC voltage being 10mV (as per typical data provided
       by manufacturer)
    •   -10% drop of capacitance due to operating temperature (as per specification sheet)
    •   -5% drop of capacitance each time decade (as per specification sheet)

The total capacitance value at actual condition is then defined as multiplications of the
capacitance drop factors.

Cactual = Crated * F DCV drop * F ACV drop * F temp drop * F ageing drop

In example above

Cactual = 10uF * 0.4 * 0.85 * 0.9 * 0.95 = 2.9uF

The actual capacitance value of the 10uF 6.3V MLCC X5R capacitor at the operating condition
above is expected to be 2.9 uF.

However, in such operating conditions the real capacitance value can be as low as 10%
depending to the specific PN design and manufacturer. Designers of electronic devices has to
count with such behaviour and it is always good idea to check the manufacturer datasheets,
simulations and its detail specification. Leading MLCC manufacturers are providing
sophisticated on-line simulation models, where designers can enter its operating conditions and
the software will generate typical plots on the selected part.

2.6. How trustful are the manufacturers’ simulation data ?

This sub-chapter follows experimental work by I.Novak at col. [2] carried in 2011 on multiple
MLCC X5R and X7R vendors.

The Figure 7. compare MLCC 1uF 0603 X5R and X7R 16V vendor data with measured data at
reference conditions 500 mVrms AC bias at 100 Hz and room temperature.

Not all of the vendors state the conditions (temperature, AC bias, frequency) for their DC bias
data, but our 500 mVrms AC bias data seemed to be more likely matching the vendor conditions
than the 10 mVrms data set.

Vendor-B and Vendor-C have very good agreement between measured and vendor-predicted
capacitance drop. Data for Vendor-A and Vendor-F show bigger differences, and both
predictions underestimate the capacitance loss.

As an important note, it has to be add, that manfacturers are continuously improving their
software simulation tools and its accuracy. The data presented in Figure 7 are reflecting
situation as present in year 2011.
Figure 7. Comparison of capacitance % vs bias 1uF 0603 X5R and X7R 16V, at 100 Hz and
 500 mV AC. Green triangle markers indicate vendor data; blue line shows measured data.
                    Source: I.Novak; electrical-integrity.com, 2011
                3. How this may impact electronic HW designs

Ceramic capacitors are widely used in today’s electronic circuits. Many of them find
applications in power conversion and distribution networks. In high-speed data links they are
used as DC-blocking capacitors and occasionally as part of RC terminations. Analog circuits
also use them for timing and DC blocking applications.

3.1. Capacitors in power supplies

Power electronic systems require some minimum capacitance value for IC safe operational
mode. In case of voltage drop under the cut off value it may result in the power supply
mulfunction and critical power loss failures. This very important especially for safet critical
applications.

MLCC X5R or X7R capacitors are favourite choice for many miniature power designs due to
its downsizing, low ESR, low ESL and high ripple current capability. However the capacitance
loss due to the DC Bias Aging impact may result in significant loss of its capacitance value.
The phenomen is dependent on various parameters impacting the internal electrical field
strength and thus PN and manufacturer specific.

Qualifying a new vendor, using qualified part at different applications conditions without a
background knowledge and data can lead to a catastrophic system failures. Figure 8 shows
capacitance drop with time example of three different manufacturers of the same PN. Blue and
black vendors were originally qualified by the end user, red vendor was add under a risk of line
stop due to the MLCC shortage market situation and resulted in system failures.




      Figure 8. 10uF 6.3V X5R MLCC capacitance drop example of 3 different vendors
3.2. Paralleled Capacitors (source:[2])

The application, where the DC and AC bias dependence of MLCCs may need to be taken into
account is, when we use MLCCs of different capacitance values in parallel (Figure 9).

If the capacitors are assumed to be ideal, as shown on the left of the figure, all what we need to
do is to sum up the different capacitances as they change with DC and AC bias. When their
parasitics are also taken into account, the changes of the series and parallel resonances need to
be considered as well. The change of capacitances will shift the series and parallel resonances
to higher values and Q may also change slightly. If the relative rate of capacitance change is
the same for all capacitors, what we get is mainly a shift of the impedance profile to higher
frequencies and higher Q at the resonances.




Figure 9. Equivalent schematic diagram of two parallel-connected capacitors. Left: without
parasitics. Right: with parasitics.

The worst case occurs, when some of the paralleled capacitances decrease, while some others
either don’t or actually might increase, perhaps due to the AC bias conditions.

Such a scenario is illustrated with measured data in Figure 10. Two capacitors were parallel
connected in the test fixture: a 1uF 0603-size 16V X7R from one vendor and a 47uF 1206-size
6.3V X5R part from other vendor. The minimum around 1 MHz is from the series resonance
frequency of the 47uF part. The minimum around 7 MHz is the series resonance frequency of
the 1uF part. The peak around 4 MHz is the anti-resonance between the capacitance of the 1uF
part and inductance of the 47uF part. Note that all three resonances move towards higher
frequencies, indicating that the capacitances of both parts decrease with increasing DC bias.




    Figure 10. Impedance magnitude of two parallel-connected MLCCs of different kinds.
3.3. Capacitors in LC filters (source: [2])

Probably one of the worst situations is when multiple components joined in the same network,
react to DC and AC biases in opposite directions. A typical scenario of this kind is when we
use series inductors or ferrite beads for enhanced filtering, followed by shunt capacitors.




Figure 11: Equivalent schematics of a PI filter with series ferrite element and parallel MLCC
at the output. Left: setup with no DC current bias through L1. Right: setup with DC current
bias through L1.

If this filter circuit has to handle substantial DC current and the inductive element is not properly
sized, its inductance may drop due to the DC current flowing through the part. If at the same
time the filtered DC voltage reduces the capacitance of the MLCC part at the output of the filter,
we end up with reduced inductance and reduced capacitance, resulting in a significant shift of
the filter’s cutoff frequency. This effect was tested with the circuit shown in Figure 11.

The circuit under test was a simple PI filter, composed of two bypass capacitors and a series
ferrite bead. The C1 capacitor on the input side of the filter was a 390uF 16V electrolytic type
bulk capacitor with little or no DC and AC bias dependence to mimic a low value of input feed
impedance. The C2 capacitor on the output was a 47uF 6.3V X5R 1206-size MLCC. The L1
series element was a commercially available ferrite bead, rated for 2A maximum current.




 Figure 12: The two plots show the cumulative transfer responses of the circuit from Fig.11.
 Left plot: bias range limited to 0-4V and 0-1A. Right plot: bias range is 0-16V and 0-1.5A.
The plot in Figure 12 show all the measured data traces. The plot on the left has the DC bias
voltage and current limited to the reasonable ranges of 0-4V and 0-1A, respectively. The 4V
and 1A DC bias limits are 63% and 50% of the rated 6.3V and 2A limits, respectively.

There are two ranges marked on the plot along the two axes: the range of transfer-function
magnitude variation at 260 kHz is 50 dB; the range of frequency variation at the -50 dB level
is approximately 3.2 : 1. The plot on the right shows all traces for the full measured 0-16V bias
voltage and 0-1.5A bias current ranges. There are two ranges marked on this plot, too: at 260
kHz the transfer-function magnitude variation is 68 dB; the range of frequency variation at the
-50 dB level is approximately 7.2 : 1.

     4. How to measure capacitance with BIAS in mass volume
The obvious task from designers is to get the worst case MLCC class II capacitance drop at
referenced conditions as the basic for their design considerations. As mentioned in previous
chapters, manufacturers are continuously improving ther simulation online tools, where typical
plots at operating conditions can be simulated to provide information of the capacitor behaviour
at the required environment.

The online simulation tools may be sufficient for many kind of consumer electronics operating
at standard environment. Nevertheless, mission critical system designers can not rely on
„typical“ data plots and requiry 100% „guaranteed“ point of the capacitance value. Interest to
use high CV MLCC in safety automotive, defence or medical system is increasing under the
continuous electronics miniaturisation requirements.

Manufacturers, on the other hand, can guarantee only what they can 100% measure in mass
manufacturing.

There are two general ways how to measure Capacitance with DC BIAS: Direct and Indirect
capacitance measurement.

4.1. Direct capacitance measurement

The direct measurement that is used today in mass manufacturing by most of MLCC
manufacturers is based on LCR bridge measure meters build into a 100% electrical parameter
testers. The bridges, contacting systems and el.tester design must ensure the appropriate test
accuracy, speed, reliability and lifetime to be able to measure high quantity of the manufactured
MLCC capacitors of all kinds and sizes.

Typical LCR bridges used by el.tester manufactures is a class of HP4263B measure bridges
(Fig.13) that are used to measure Capacitance, Impedance, DF or ESR values at frequencies
from 100Hz to 1MHz.




                          Figure 13. HP4263B LCR measure bridge
While measure parameters of the bridge are satisfying needs for electrical parameters fast and
reliable measurement, the DC BIAS conditions are limited to maximum 2V. This comply to
standard capacitance reference conditions: Frequency 1kHz or 120Hz AC Voltage: 0.5 or 1.1V
AC volt and BIAS of 2V DC.

The LCR bridges can also accept some level of external BIAS, but mostly the value is limited.
In case the HP4263B bridge the maximum BIAS level is just 2.5V. More expensive bridges can
operate with higher external voltages, but often limited to 50V maximum.

Additional factor that complicates Capacitance with higher DC BIAS measurement is a
charging time. Depanding to the capacitance value of the measured part, some time constant
delay has to be applied before measurement to allow capacitor to be fully charged. This may be
other complication for adoption of capacitance measurement at el.tester as there may be only
few (tenth)milliseconds time slot for the measurement not to reduce the tester speed and
throughput significantly.

4.2. Indirect (transient) capacitance measurement

Capacitor charging and discharging characteristics are depending to its capacitance value.
Charging current is following the basic equation:

                    𝑑𝑑𝑑𝑑
        𝐼𝐼 = C 𝑑𝑑𝑑𝑑
                                     where, I = charging current
                                            dV/dt = voltage increase
                                            C = capacitance

Thus in case of stable voltage increase dV/dt capacitance value can be calculated based on the
measured current value.




               Figure 14. Transient indirect capacitance measurement methods

The indirect capacitance method during transient as shown in Figure 14 can be theoretically
applicable during measurement of leakage current at rated voltage that is usually part of todays
MLCC capacitors 100% electrical measurements in mass production.
Capacitance (and ESR) values can be also evaluated from a discharging characteristics as
shown in Figure 15. [3]




 Figure 15. Capacitance and ESR measurements from discharge characteristics; source [3]

Under the constant discharging current, the Capacitance and ESR values can be calculated from
equations:




The main challenge of the indirect capacitance measurement here would be to evaluate its
correlation to the Capacitance versus DC BIAS characteristics applicable to wide range of types
and case sizes. Also cost for electrical tester modifications may be of consideration for realistic
implementation into mass manufacturing.



                          SUMMARY & CONCLUSION
Over the past years, multi-layer ceramic capacitors have undergone significant improvements.
The volumetric density has increased several folds. This unfortunately resulted in a big increase
in DC and AC bias sensitivity for many parts. In particular, X5R and X7R parts, which
previously showed only modest bias dependence, exhibit significant capacitance drops.
The increased bias dependence creates additional challenges for users during the design and
validation phase, and increases design complexity, since filters with otherwise identical filtering
requirement now may require different component selection if they need to work in different
bias environments.
To help the users, all major vendors today supply at least DC bias information with their MLCC
parts and simulation tools under continuous improvement in complexity and accuracy.
Nevertheless, so far the capacitance versus BIAS data available from manufactures are based
on typical characteristics as 100% mass production volume capacitance under the high DC
BIAS measurement present a considerable technical and economical challenge for MLCC
manufacturers.

                                      FUTURE STEPS
There is continuous effort to find a common industry approach on handling of MLCC class II
DC Bias issues, especially among the automotive industry. Thus, the next proposed step is to
involve AECQ-200 committee members in discussions to recommend a common approach
between electronic designers / customers and manufacturers across the industry.

Five manufacturers (AVX Corporation, Kemet Electronics, Murata Electronics Europe,
Samsung Electro-Mechanic, Wuerth Elektronik) and Continental Automotive, as the end
automotive user representative, discussed this topic during the round table open discussion at
PCNS Passive Components Networking Symposium in September 10-13th 2019 in Bucharest,
Romania. Outcome of the panel discussion is summarised in “Open letter to AECQ-200
committee about MLCC class II Capacitance DC BIAS issues” and together with this paper it
is submitted for discussion at AECQ-200 platform.



                                       REFERENCES

[1] www.epci.eu/pcns

[2] I.Novak et col.; “DC and AC Bias Dependence of MLCC Capacitors Including Temperature
Dependence”; DesignCon East 2011; http://electrical-integrity.com. Re-published under author’s
permission on passive-components.eu website:

https://passive-components.eu/dc-and-ac-bias-dependence-of-mlcc-capacitors-including-
temperature-dependence/

[3] C.Ionescu et col.; „Evaluation of Active Balancing Circuits for Supercapacitors”; PCNS 2019
Romania; https://epci.eu/evaluation-of-active-balancing-circuits-for-supercapacitors/
                    APPENDIX – Future Specification Guidelines
                       (for discussion at AEC-Q200 board)
Future procurement specification, in ideal case, would define at least one point of the
Capacitance versus DC BIAS characteristics that could be “guaranteed” for the selected part.

Procurement specification proposal to be agreed between customer and supplier:

Capacitance loss guaranteed not to exceed XX% (for example -70%)1 at 100%2 of rated
voltage, measured at reference conditions: after 12hrs3 post last de-ageing and DC BIAS
voltage applied at least for 10hrs4 at RT, 1kHz and 1VAC.

The supplier shall also provide typical Capacitance loss with DC-BIAS Ageing charts or link
to an on-line simulation tool. Additionally to the graphs the supplier shall provide a tolerance
band for the graphs which can be guaranteed by the supplier. Such specification would help
designers to see some fixed capacitance loss guaranteed working point and evaluate the worst
case at the edge operating conditions.

Customer Designer Guidelines:

If you discover that a particular capacitor is unsuitable due to capacitance loss as defined in the
specification above, you have the following options:

     •    You can check if lower Capacitance DC loss / piezo suppression series is available by
          a manufacturer (need check with purchasing team as this can be more expensive part or
          single source)
     •    Use a larger capacitance value so that when the capacitance loss is considered, you still
          have enough capacitance for the required functionality. Note: higher values may have
          even worse DC bias characteristics due to even higher CV factor. This also may be an
          issue of distortion in large-signal AC, and likely will just make the problem worse and
          may not lead to the problem solving.
     •    Use a physically larger package size. This would reduce V/mm electrical stress and thus
          reduces also DC BIAS capacitance loss dependency. So, if you have enough room in
          your design, moving one step up in case size, for example from 0402 to 0603, 0603 to
          0805 or a 1210 will significantly reduce the issue.
     •    If applicable you can consider using more stable dielectric type such as moving from
          X5R to X7R, from X7R to X8R dielectric type or tighter tolerance field such as from
          X7R to X7P types. (multi-sourcing and price increase options to be checked)
     •    Use a different capacitor type. Sometimes, you won’t be able to escape the DC bias
          issue or piezo issues at all. In this case, consider looking at a different capacitor type,
          such as an aluminum hybrid if you have enough board space or a tantalum polymer
          capacitor that may provide low profile, high CV and stable option.

Notes:
     1.   The level of defined maximum capacitance loss may be a part number specific, the actual value or some more detail guideline, if
          possible, to introduce some general rules to be discussed with manufacturers.
     2.   The cap loss reference DC BIAS is suggested to 100% of rated voltage, but it can be changed upon discussion with manufacturers.
     3.   12 or 24hrs measurement after last heat/deaging is a standard time used also in MIL standards to define state of the dielectric after
          the last “reset”.
     4.   10hours of DC applied as reference selected in respect to decades behaviour references that is used by MLCC manufacturers …
          what is happening in first, second, third decade …etc. 1hour may not be sufficient in some cases to see all slow polarization to
          happen and need to add some safety, thus 10hours (or more) is set as the reference point.
