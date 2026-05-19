                                                                                                         Application Note


Switching Regulator Series

The Important Points of Multi-layer Ceramic Capacitor Used
in Buck Converter circuit
Multi-layer Ceramic Capacitor (MLCC) with large-capacitance can be used as smoothing-capacitor in power supply circuits. Compared to other
capacitor types such as an electrolytic capacitor, MLCC differs in frequency characteristics, temperature characteristics, and DC voltage
characteristics. Using unmatched MLCC may not obtain required target characteristics for power supply circuit and may cause abnormal operation.
This application note explains the important points while using MLCC.


                                                                              Figure1 shows frequency characteristics of all major types of
Types of Multi-layer ceramic capacitor (MLCC)                                 capacitors. Ripple voltage of output is expected to become
                                                                              smaller by using MLCC in a power circuit. However in earlier
MLCC can be broadly classified into two types; for temperature                power-IC designs, usage of MLCC with ultra-low ESR was not
compensation and for high-dielectric constant. MLCC for                       considered. Therefore, phase of feedback circuit rotates too
temperature compensation uses Titanium oxide (TiO2) and                       much at high-frequency area, causing power circuit to operate
Calcium zirconate (CaZrO3) as material for its paraelectric.                  unstably and may cause oscillation in worst case. When MLCC
Therefore, it cannot suit for capacitor with large-capacitance as             has to be used at any cost, connecting a low-ohmic resistor more
relative permittivity is small, about 20 to 300. Moreover, since              than 10mΩ in series is recommended, and may deteriorate the
relative permittivity changes linearly with temperature, the                  frequency characteristics.
temperature coefficient can be restricted between +100 to -
4700ppm/°C by adjusting composition of the dielectric material.                                   100
The capacitor for temperature compensation in power circuit is
used in time-constant circuits such as Snubber-circuit and for                                                                   C=47µF
                                                                                                   10
SOFT-START.




                                                                                  Impedance (Ω)
                                                                                                                              AL electrolytic
MLCC for high-dielectric constant uses Barium titanate (BaTiO3)                                     1
as main material for its paraelectic. With its big relative
permittivity of 1,000 to 20,000, it can be capacitor with small in                                0.1                               POSCAP
size and high-capacitance. But, this material changes
tremendously with temperature, so using it for time-constant
circuits needs caution.                                                                       0.01                   OS

In later part, the explanation will focus on high-dielectric constant                                                     Ceramic
                                                                                        0.001
MLCC used as input/output capacitor in a power circuit.
                                                                                            0.0001 0.001         0.01    0.1          1         10
                                                                                                               Frequency (MHz)
Frequency Characteristics
                                                                                              Figure 1. Frequency Characteristics of Capacitors
MLCC has extremely small ESR (Equivalent Series Resistance)
compared to other capacitor types such as electrolytic capacitor.


                       Parameter                    Temperature compensation MLCC                         High-dielectric constant MLCC
            Paraelectric material                  Titanium oxide (TiO2)                                Barium titanate (BaTiO3)
                                                   Calcium zirconate (CaZrO3)
            Relative permittivity                  20 to 300                                            1,000 to 20,000
            Temperature characteristics            +100 to -4700ppm/°C                                  +30 to -82%
            Capacity                               ≤ 0.1µF                                              ≥ 68pF
            Capacitance-change when                Almost no change                                     Changes
            voltage input
            Capacitance-change over time           Almost no change                                     Changes
            Application circuits                   Snubber, Time-constant                               Smoothing power, Decoupling
                                                   High-frequency circuit, Audio                        circuit
                                         Table 1. Characteristics of Laminated Ceramic Capacitor


© 2013, 2020 ROHM Co., Ltd.                                                                                                     No. 62AN089E Rev.002
                                                                        1/4
                                                                                                                                      JANUARY 2020
The Important Points of Multi-layer Ceramic Capacitor Used in Buck Converter circuit                                                    Application Note

Temperature Characteristics
High-dielectric series MLCC with high-capacitance has products
with various temperature characteristics. Table 2 and Figure 2                                      20
                                                                                                                                            B
show typical temperature characteristics. The characteristic                                        10
                                                                                                                                                X7R
curve changes in various ways within the tolerance range of the                                      0




                                                                           Capacitance change (%)
each product. Since the Temperature characteristics are                                             -10
standardized, it’s easy to judge by the capacitor’s type name.                                      -20                                         X7U
                                                                                                                                  X5R
                                                                                                    -30
Products with smaller capacitance tolerance（±15%）, such as
                                                                                                    -40
B, X5R, R, X7R, X8R are recommended for temperature                                                                                     F
characteristics used in the power circuits. The characteristics of                                  -50

X7U, F, Y5V, Z5U, Z5V are inexpensive, but capacitance                                              -60

tolerance (-82%) is large, making it to operate stable only at                                      -70

room     temperature.    Do   not   use   capacitors   with   such                                  -80

characteristics in power circuit as it may cause trouble.                                           -90
                                                                                                          -75 -50 -25    0   25   50   75 100 125 150
Judging from the operating temperature range of application                                                             Temperature (℃)
equipment used, and choosing from B, X5R, R, and X7R
                                                                           Figure 2. Major Temperature Characteristics of High-dielectric
characteristics are recommended.
                                                                                                                    constant type MLCC

                              Basic    Temperature Capacitance
Standard Characteristics
                           temperature     range    tolerance
   JIS           B            20°C      -25～+85°C     ±10%
                X5R                                   ±15%
                X5S                     -55～+85°C     ±22%
   EIA          X5T           25°C                 +22%, -33%
                X6S                                   ±22%
                                       -55～+105°C
                X6T                                +22%, -33%
   JIS           R            20°C     -55～+125°C     ±15%
                X7R                                   ±15%
                X7S                                   ±22%
                                       -55～+125°C
   EIA          X7T           25°C                 +22%, -33%
                X7U                                +22%, -56%
                X8R                    -55～+150°C     ±15%
   JIS           F            20°C      -25～+85°C +30%, -80%
                Y5V                     -30～+85°C +22%, -82%
   EIA          Z5U           25°C                 +22%, -56%
                                       +10～+85°C
                Z5V                                +22%, -82%

 Table 2. Major Temperature Characteristics of High-dielectric
                        constant type MLCC




© 2013, 2020 ROHM Co., Ltd.                                                                                                             No. 62AN089E Rev.002
                                                                     2/4
                                                                                                                                              JANUARY 2020
The Important Points of Multi-layer Ceramic Capacitor Used in Buck Converter circuit                                                                     Application Note

DC Voltage Characteristics
                                                                                                                    10
                                                                                                                                                      10µF, 10V, B
The capacitance value changes by applying DC voltage to high-
                                                                                                                     0
dielectric series type MLCC. This is peculiar only to this capacitor
                                                                                                                   -10




                                                                                          Capacitance change (%)
type and does not happen in other types, such as electrolytic
                                                                                                                                                 3225(1210)
capacitor and temperature-compensation type MLCC.                                                                  -20                           T=2.70mm

Let’s take a look at MLCC of Murata Manufacturing Co., Ltd. as                                                     -30                                    3216(1206)
                                                                                                                                                          T=1.25mm
an example of DC voltage characteristics. Figure 3 shows
                                                                                                                   -40
characteristics of a capacitor with 10µF/10V (B) that differs in
size (L×W). Both of these products are of same 0.95mm                                                              -50
thickness. Tendency of bigger capacitance reduction, with                                                                             3216(1206)
                                                                                                                   -60                T=0.95mm
smaller size part can be observed, when DC voltage is applied.
1608 size capacitor can only be used for 1V even though it is                                                      -70
rated for 10V. Caution is required in confirming the changing                                                      -80
characteristics, when switching to smaller-size capacitors to                                                            0   1    2     3    4 5 6 7            8    9    10
reduce PCB mounting area.                                                                                                                   DC voltage (V)

Figure 4 shows characteristics of 10µF/10V (B) capacitor with                                                                Figure 4. DC voltage characteristics
different thickness (T), and same size (L×W). Tendency of                                                                         Difference in thickness (T)
lesser capacitance reduction, with larger thickness part (bigger
volume) can be observed, when DC voltage is applied. Caution
                                                                                                                   10
is required in confirming the changing characteristics, when
                                                                                                                    0
smaller-thickness of capacitors are used due to PCB height-                                                                           10µF, B, 3216(1216), T=1.80mm
                                                                                                                   -10
restriction in slimmer designs.




                                                                                          Capacitance change (%)
                                                                                                                   -20
                                                                                                                                         16V
Figure 5 shows DC voltage characteristics with capacitors of                                                       -30
different rated-voltages. Both capacitors are of 10µF (B), size
                                                                                                                   -40
3216(1216), thickness 1.80mm. Product with 50V reduces
                                                                                                                   -50
capacitance more than product with 16V rated-voltage, on
                                                                                                                   -60
applying DC voltage.                                                                                                                            50V
                                                                                                                   -70
                                                                                                                   -80
                               10
                                                                                                                   -90
                                0                                                                            -100
                                                            10µF, 10V, B
                               -10                                                                                       0       10         20      30     40        50




      Capacitance change (%)
                                                                                                                                            DC voltage (V)
                               -20
                               -30                                                                                           Figure 5. DC voltage characteristics
                                                                 2012(0805)                                                      Difference in Rated-voltage
                               -40                               T=0.95mm
                               -50                                                       As to choosing the capacitor with higher rated-voltage, does not
                               -60                                                       always guarantee higher performance. Selecting a MLCC simply
                                                            3216(1206)                   by checking only the specification of capacitance and rated-
                               -70                          T=0.95mm
                                         1608(0603)                                      voltage can deteriorate the characteristics of a power circuit.
                               -80       T=0.95mm                                        Always request the manufacturer for detailed characteristics
                               -90                                                       data.
                                     0   1   2   3 4 5 6 7           8      9 10
                                                  DC voltage (V)                         MLCC of Murata Manufacturing Co., Ltd can be easily confirmed
                                                                                         by ‘SimSurfing’, a design support system on their website which
                                     Figure 3. DC voltage characteristics
                                                                                         shares various characteristics. (as of 2020/ January)
                                          Difference in size (L×W)


© 2013, 2020 ROHM Co., Ltd.                                                                                                                               No. 62AN089E Rev.002
                                                                                   3/4
                                                                                                                                                                JANUARY 2020
The Important Points of Multi-layer Ceramic Capacitor Used in Buck Converter circuit                                                        Application Note

Chronological change                                                            Heat generation characteristics
High-dielectric series type MLCC has a characteristic that                      When ripple current (AC, alternating current) flows through a
deteriorates capacitance-value with time. Figure 6 shoes the                    capacitor, the resistor element generates heat and temperature
example of chronological change. “0” represents the point                       of capacitor itself rises. But since MLCC has extremely small
where 24-hours have passed after mounting. Capacitance value                    ESR (equivalent series resistance), amount of heat is less and
decreases linearly when time axis is shown in logarithmic. MLCC                 ripple                     resistance    capability   is   excellent.   Many   MLCC
for temperature-compensation type does not have this kind of                    manufacturers recommend surface temperature to be below
chronological changes.                                                          20°C while usage.

Capacitor with reduced capacitance by chronological change
                                                                                                         100
recovers its capacitance by being heated to more than Curie
temperature (about 125°C) by solder, etc. Also that same                                                                        10µF, 10V, B, 3216 (1206)
capacitor starts chronological change when it cools down to
below Curie temperature.




                                                                                  Temperature rise (℃)
Capacitance calculation for the chronological change is
necessary while designing for long-term active equipment such                                             10

as in industrial application.


                           10

                            5
                                                       B char.                                             1
                            0                                                                                  0     1       2       3       4          5      6




  Capacitance change (%)
                                                                                                                           Ripple current (Arms)
                            -5
                                                       F char.                                           Figure 7. Example of self-heating of high-dielectric series
                           -10                                                                                                   MLCC

                           -15

                           -20

                           -25

                           -30
                                 10   100     1000       10000   100000
                                            Time (h)

 Figure 6. Example of Chronological change in High-dielectric
                        series MLCC




© 2013, 2020 ROHM Co., Ltd.                                                                                                                  No. 62AN089E Rev.002
                                                                          4/4
                                                                                                                                                   JANUARY 2020
                                                                                                                                Notice




                                                                 Notes
                     1) The information contained herein is subject to change without notice.

                     2) Before you use our Products, please contact our sales representative and verify the latest specifica-
                        tions :

                     3) Although ROHM is continuously working to improve product reliability and quality, semicon-
                        ductors can break down and malfunction due to various factors.
                        Therefore, in order to prevent personal injury or fire arising from failure, please take safety
                        measures such as complying with the derating characteristics, implementing redundant and
                        fire prevention designs, and utilizing backups and fail-safe procedures. ROHM shall have no
                        responsibility for any damages arising out of the use of our Poducts beyond the rating specified by
                        ROHM.

                     4) Examples of application circuits, circuit constants and any other information contained herein are
                        provided only to illustrate the standard usage and operations of the Products. The peripheral
                        conditions must be taken into account when designing circuits for mass production.

                     5) The technical information specified herein is intended only to show the typical functions of and
                        examples of application circuits for the Products. ROHM does not grant you, explicitly or implicitly,
                        any license to use or exercise intellectual property or other rights held by ROHM or any other
                        parties. ROHM shall have no responsibility whatsoever for any dispute arising out of the use of
                        such technical information.

                     6) The Products specified in this document are not designed to be radiation tolerant.

                     7) For use of our Products in applications requiring a high degree of reliability (as exemplified
                        below), please contact and consult with a ROHM representative : transportation equipment (i.e.
                        cars, ships, trains), primary communication equipment, traffic lights, fire/crime prevention, safety
                        equipment, medical systems, servers, solar cells, and power transmission systems.

                     8) Do not use our Products in applications requiring extremely high reliability, such as aerospace
                        equipment, nuclear power control systems, and submarine repeaters.

                     9) ROHM shall have no responsibility for any damages or injury arising from non-compliance with
                        the recommended usage conditions and specifications contained herein.

                    10) ROHM has used reasonable care to ensurH the accuracy of the information contained in this
                        document. However, ROHM does not warrants that such information is error-free, and ROHM
                        shall have no responsibility for any damages arising from any inaccuracy or misprint of such
                        information.

                    11) Please use the Products in accordance with any applicable environmental laws and regulations,
                        such as the RoHS Directive. For more details, including RoHS compatibility, please contact a
                        ROHM sales office. ROHM shall have no responsibility for any damages or losses resulting
                        non-compliance with any applicable laws or regulations.

                    12) When providing our Products and technologies contained in this document to other countries,
                        you must abide by the procedures and provisions stipulated in all applicable export laws and
                        regulations, including without limitation the US Export Administration Regulations and the Foreign
                        Exchange and Foreign Trade Act.

                    13) This document, in part or in whole, may not be reprinted or reproduced without prior consent of
                        ROHM.




                                         Thank you for your accessing to ROHM product informations.
                                         More detail product informations and catalogs are available, please contact us.

                                         ROHM Customer Support System
                                                                                          http://www.rohm.com/contact/




ZZZURKPFRP
652+0&R/WG$OOULJKWVUHVHUYHG
                                                                                                                                5%
