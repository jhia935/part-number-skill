TECHNICAL
PAPER



The Effects of ESR and ESL
in Digital Decoupling Applications

Jeffrey Cain, Ph.D.
KYOCERA AVX Components Corporation


Abstract
It is common place for digital integrated circuits to operate at
switching frequencies of 100 MHz and above, even at the circuit board
level. As these frequencies continue to increase, the parasitic of the
decoupling capacitors must be considered. A study on the effects of
equivalent series resistance (ESR) and equivalent series inductance
(ESL) in a typical digital decoupling application is presented. Utilizing
SPICE, it can be shown that the ESR and ESL of chip capacitors can
dramatically alter the voltage seen by the integrated circuit (IC). By
changing the values of the parasitics and comparing the results to
the ideal case for a variety of frequencies, some common decoupling
design rules are formulated.
                   THE EFFECTS OF ESR AND ESL IN
                  DIGITAL DECOUPLING APPLICATIONS
                                                by Jeffrey Cain, Ph.D.
                                         KYOCERA AVX Components Corporation


Introduction                                                   Perhaps the most difficult device to model is the
                                                            IC chip. As in most CMOS circuitry, the chip only
   The use of monolithic capacitors to decouple digital     draws current when the transistors are switching and
circuitry is certainly nothing new [1,2]. But as micro-     only a leakage current during the "0" or "1" state. No
processor clock speeds increase, what appears to be         two different ICs have the same amount of transis-
daily, the need to better understand the parasitic          tors, so the amount of current drawn, the number of
effects of capacitors in the decoupling of integrated       gate capacitors to be charged and the rate at which
circuits (ICs) becomes more important. Instead of           the gate capacitors are charged varies greatly. Some
studying one particular type, such as a ceramic chip,       IC vendors actually publish models of the µprocessor
tantalum chip or any other type of surface mount            as in [3]. To keep the results of this work as general
capacitor, this work focuses on the general behavior        as possible, the IC will be modeled as a simple cur-
of these devices. By doing this, the designer can make      rent sink. The slew rate and the maximum current
informed decisions on which capacitor value and type        can easily be varied by choosing such a device. The
to use for a given application. This work does not          waveform for a 100 MHz, 0.5A/ns waveform is shown
cover the effects on capacitance such as voltage and        in Figure 2.
temperature dependencies, as it is assumed that the
designer knows the capacitance for the given envi-                            1.2
ronmental and bias conditions.
   The simplest equivalent circuit for a capacitor can                        1.0



                                                                Current (A)
be most generally realized as                                                 0.8
                                                                              0.6
                                                                              0.4
                                                                              0.2
             C        ESL           ESR
                                                                               0
                                                                                    0             20         40               60
                                                                                                   Time (ns)
with the magnitude of the impedance given as

    ZC = 冑            (
             ESR2 + ␻ESL -
                           1
                         ␻Cc
                             2
                                     )             [1]                              Figure 2. Typical IC current waveform.


                                                               Finally, the complete modeling circuit used for this
where ␻ is 2␲f. There are much more complicated             work is shown in Figure 3. This is a very simplified
models that can be created, especially with tantalum        circuit from the actual case, but it helps to under-
capacitors, but for most general purposes the above         stand the effects of the capacitors located closest to
model does the job.                                         the IC. One needs to keep in mind that the circuit in
   As many ways there are to mount a decoupling             Figure 3 concerns itself with only one power/ground
capacitor near an IC, is a many ways to model the           pin of the IC. Today's high performance ICs contain
interconnect between the power supply and the IC.           as many as 300 pairs of power/ground pin sets.
The number of "ways" is probably infinite and so for
this work a typical case for a multi-layered printed
circuit board (PCB) is used. Due to the small imped-
ance from the power supply to the decoupling capaci-
tor (due to the power/ground planes imbedded in the
PCB), the inductance of a typical via/pad connection
is around 400 pH. The value for the inductance from
the capacitor to the IC can vary dramatically, depend-
ing on the line width, layer thickness, dielectric con-
stant of the PCB, etc. For this work, a value of 1 nH
was chosen for the inductance of the interconnect
between the cap and the IC. Once again this value                                       Figure 3. Decoupling circuit model.
can vary widely and to cover all the variations of this
value is beyond the scope of this work.

CARTS 97: 17th Capacitor and Resistor Technology
Symposium, 24-27 March 1997.
Choosing A Decoupling Capacitor                              Effects of ESR on Decoupling
The Ideal Case                                                  Using the circuit in Figure 3, let's examine the
  One method proposed [2] to choose a decoupling             effects of ESR on the arc voltage swing over the
capacitor lies in the fact that we know:                     capacitor. Keep in mind that this work concentrates
                                                             on the overall view of ESR in general, as opposed to
                                                    (2)      specific devices. The current sink used here is the
Q = CV                                                       same as in Figure 2 and the capacitor value is 0.1µF.
                                  and                                                    3.5




                                                                  Ripple Voltage (3.3)
 dQ      ∆V                                                                              3.4
    =I=C                                            (3)
 dt      ∆t
                                                                                         3.3
       ∆t
C=I                                                 (4)                                  3.2
       ∆V
                                                                                         3.1
That is to say, for a desired maximum ripple voltage,                                       0       20               40       60
⌬V, a switching time of ⌬t and a peak current of I, the                                                  Time (ns)
minimum decoupling capacitor needed is C.
                                                                                           ESR=1.0 Ohms              ESR=0.1 Ohms
    There are a couple of interesting observations
from [4]. The first being that the needed capacitance                                      ESR=0.01 Ohms
is indirectly proportional to the ripple voltage. This
comes as no big surprise. However, [4] also states           Figure 5. Effects of ESR on ripple voltage of 0.1µF capacitor.
that the faster one can switch the current in the IC,
the less decoupling capacitance is needed. In an ideal
world this may be true, but the addition of parasitic           As Figure 5 clearly shows, the greater the ESR of
inductance and resistance can easily override this           a device, an increase in the ripple voltage for a given
aspect of equation [4], as will be demonstrated later.       cap value is seen. This is directly related to the RC
    If the ideal case of [4] is used in the circuit of       time constant of the capacitor and is something that
Figure 3, with no parasitic inductance or resistance,        has been known by switch-mode power supply
the resulting waveform is very close to ideal. As            designers for a long time. Decreasing the resistance,
example we will use a 0.01, 0.1 and 1µF capacitor to         decreases the ripple.
decouple a 0.5A/ns current sink with a peak current             Another test of interest involves the slew rate and
of 1A. Using [3], the resulting voltage should be            frequency of the IC current sink on the decoupling
around 50mV for the 0.01µF case and the Spice                voltage. Figure 6 shows the resulting voltage ripple
results shown in Figure 4.                                   using a 0.1µF capacitor, with an ESR of 1⍀ and a
    As is plainly shown in Figure 4, the ideal equation      maximum current of 1 A. The 1W is chosen to accen-
[4] for the voltage is already breaking down, because        tuate the effects on the ripple voltage. The current
of the introduction of the trace inductances between         sink is set for 25, 50 and 100 MHz, with rise times of
the capacitor and the IC.                                    0.5, 0.25 and 0.125 A/ns, respectively. While the indi-
                                                             rect relationship of [4] holds, the effect of the ESR on
                   3.45                                      the circuit keeps the ripple voltage from being the
                    3.4                                      ideal case. Once again the RC time constant comes
                                                             into play, with the lower frequency clock speeds pro-
                   3.35                                      ducing less ripple.

         Voltage
                    3.3

                   3.25
                    3.2
                   3.15
                       0       20      40    60
                               Time (ns)
                      0.01µF      0.1µF     1µF

    Figure 4. Ripple voltage on ideal decoupling capacitor
                  using a 0.01, 0.1 and 1µF.
                               3.5                                                   Effects of ESL on Decoupling
                                                                                        Another important parameter of the decoupling
                                                                                     capacitor is the parasitic inductance. As the industry
                               3.4                                                   switched from leaded to surface mount devices, the



     Ripple Voltage (V)
                                                                                     idea of lower inductance as an aide in decoupling first
                                                                                     became noticed. Now, there are specific, surface
                               3.3                                                   mount capacitors whose device physics lend them-
                                                                                     selves to a lower equivalent series inductance. Once
                                                                                     again, to keep this paper away from specific devices
                                                                                     and concentrating on general capacitor construction
                               3.2                                                   rules, only changes in parasitic inductance will be
                                                                                     examined.
                                                                                        The first and most obvious case to be examined is
                               3.1                                                   for a given capacitance, ESR and IC current wave-
                                  0             10               20             30   form, how does the ripple voltage seen by the IC
                                                 Time (ns)                           change. Using the circuit described in Figure 3, with
                                     100MHz, 0.5A/ns             50MHz, 0.25A/ns     a capacitor of 0.1µF, an ESR of 0.1⍀ and a slew rate
                                                                                     of 2A/ns on the IC current, the results using different
                                     25MHz, 0.125A/ns
                                                                                     parasitic inductances are shown in Figure 8. As is
Figure 6. Slew rate and frequency effects of the current sink.                       plainly shown, given constant cap and ESR values, an
              Capacitance = 0.1µF, ESR = 1⍀                                          increase in inductance will give an increase in the rip-
                                                                                     ple voltage.
   As a final example of the result ESR on ripple volt-                                                   3.6
age, Figure 7 shows the response when the ESR is
kept constant at 0.1⍀ and the cap is changed. The dif-                                                    3.5
ference in the response between the 0.1 and 1.0µF
capacitors is minimal and any increase in capacitance
                                                                                                          3.4



                                                                                         Ripple Voltage
value does not lower the ripple voltage seen at the
IC. This is in direct contrast to the ideal response
given in [4] and shown in Figure 7. One should not                                                        3.3
make the mistake extra cap is harmful, as the added
charge helps for lower frequency noise. The addition
of the resistance to the capacitor allows the device to                                                   3.2
deliver only as much charge as the controlled by the
RC time constant of the capacitor.                                                                        3.1
                                3.4
                                                                                                           3
                                                                                                            0              20               40                 60
                                                                                                                                Time (ns)
                               3.35                                                                                ESL = 100pH              ESL = 500pH
                                                                                                                   ESL = 1000pH



              Ripple Voltage
                                                                                                           Figure 8. Effects of ESL on ripple voltage.
                                3.3

                                                                                        The above results should come as no great sur-
                                                                                     prise, but what about the effect of slew rate. Using
                               3.25                                                  the same cap and ESR values and choosing a para-
                                                                                     sitic inductance of 500 pH, Figure 9 shows the effect
                                                                                     of three different slew rates; .05, 1 and 2 A/ns. Using
                                                                                     the simple formula
                                3.2
                                      0         20               40        60
                                                     Time (ns)                                             di
                                                                                      V=L
                                                                                                           dt                                            [6]
                                          1µF          0.1µF          0.01µF

    Figure 7. Effect of constant ESR on IC ripple voltag
                                                                                     one cannot solve for the peak voltage across the
                    for 0.01, 0.1 and 1µF.                                           capacitor. The capacitive part of the device makes
                                                                                     equation [6] useless. This is why measurement tech-
                                                                                     niques to solve for the inductance of a capacitor by
                                                                                     switching a voltage across the cap should be exam-
                                                                                     ined carefully.
Conclusions                                                                          One needs to look very closely at the parasitic
                                                                                  inductance of the localized decoupling caps, as this
   This paper demonstrates the use of SPICE to sim-                               can effect the voltage ripple even more than the
ulate the decoupling of an integrated circuit device,                             resistance. This is especially true on the rising and
using the full electrical model for a capacitor. For a                            falling edges of the IC, as one would expect. Using
given capacitance value, the increase of the ESR in                               equation [6] is a good start, but this is for only one
that device will cause an increase in the ripple voltage                          power/ground pin set, and the effects of connecting
seen by the IC. The ripple voltage cannot be                                      multiple capacitors in parallel should be considered.
decreased by increasing capacitance (the ideal case),
                     3.8                                                          Bibliography
                                                                                  [1] R. K. Keenan, Decoupling and Layout of Digital
                     3.6                                                              Printed Circuits, 1985.



    Ripple Voltage
                     3.4                                                          [2] A. Martin, "Decoupling Basics", AVX Technical
                                                                                      Bulletin.
                     3.2
                                                                                  [3] Pentium Pro Processor Power Distribution
                     3.0                                                              Guidelines, Intel Application Note, AP-523,
                                                                                      Nov. 1995.
                     2.8
                           0               20               40               60
                                                Time (ns)
                                                                                  [4] LCX Designers Guide, Chap. 1 National
                                                                                      Semiconductor, #585359-001, 1995.
                                  2 A/ns          1 A/ns         0.5 A/ns

                               Figure 9. Slew rate effects on ESL.


once the equivalent series resistance is added. A good
rule of thumb is to keep the reciprocal of the time
greater than the operating frequency, or:

1/␶ = 1/ESR*C ~> ƒ.                                                         [7]
         NORTH AMERICA                                                                              ASIA
        Tel: +1 864-967-2150                                                                 Tel: +65 6286-7555

        CENTRAL AMERICA                                 EUROPE                                     JAPAN
       Tel: +55 11-46881960                      Tel: +44 1276-697000                       Tel: +81 740-321250


NOTICE: Specifications are subject to change without notice. Contact your nearest KYOCERA AVX Sales Office for the latest
specifications. All statements, information and data given herein are believed to be accurate and reliable, but are presented without
guarantee, warranty, or responsibility of any kind, expressed or implied. Statements or suggestions concerning possible use of our
products are made without representation or warranty that any such use is free of patent infringement and are not recommendations
to infringe any patent. The user should not assume that all safety measures are indicated or that other measures may not be required.   WWW.KYOCERA-AVX.COM
Specifications are typical and may not apply to all applications.
