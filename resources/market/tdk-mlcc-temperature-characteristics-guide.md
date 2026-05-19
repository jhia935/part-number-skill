Frequently asked questions regarding:




Temperature Characteristics of Multilayer
Ceramic Capacitors




Trevor Crow,
TDK Components USA, Inc.



Abstract

All capacitors use a dielectric in their construction. This
material could be a film, ceramic, or even air. With the modern
trend for miniaturization, multilayer ceramic capacitors (MLCCs)
continue to be a vital type of capacitor used today because of
their volumetric efficiency. The material properties of the
ceramics used to manufacture MLCC dielectrics can create very
different DC-bias, permittivity, and temperature characteristics.
These differences can drastically affect the design engineer’s
circuit performance.

This document will describe some common ways in which these
temperature characteristics are categorized, graphically
demonstrate temperature characteristic performance, and
explain the physical reasons for the difference in temperature
characteristic behavior between different ceramics.




                                          January, 2014
             TDK Guide to MLCC Temperature Characteristics
                                    Trevor Crow, Applications Engineer

Q1. Why do some MLCC’s capacitances                       Class 1 ceramics have many EIA codes,
change with temperature?                                  however C0G is the most commonly used.
                                                          C0G is the EIA equivalent to the MIL NP0
This characteristic of the MLCC is based on the           (Negative, Positive, 0) specification. NP0 and
class of the ceramic with which the dielectric is         C0G are specified to have capacitance
made. There are two main classes of ceramics              tolerances of ±30ppm/ oC over the temperature
used today: class 1 and class 2.                          range of -55oC to +125oC. However, TDK
                                                          uses both NP0 and C0G to differentiate
Class 1 ceramics are non-ferroelectric ceramics           operating temperature ranges for class 1
based on titanium dioxide, also known as titania,         capacitors. TDK extends the operating
(TiO2), and frequently contain strontium titanate         temperature range of NP0 to +150oC.
(SrTiO3) and calcium titanate (CaTiO3) as
additives. Because they are paraelectric (non-                           TDK Class 1 Ratings
ferroelectric), these ceramics are very
temperature stable. Additionally, class 1                 C0G             -55 oC to +125 oC ±30ppm/ oC
ceramics do not change in capacitance when                NP0             -55 oC to +150 oC ±30ppm/oC
under a DC-bias, and show almost no loss in                  Table 1. TDK Class 1 Temperature Characteristics
capacitance over time.
                                                          Unlike class 1, class 2 has many commonly
Class 2 ceramics are ferroelectric and are usually        used codes. In the class 2 set of codes, the
based on barium titanate (BaTiO3). Class 2                first letter determines the lowest operating
ceramics have significantly higher dielectric             temperature, the number determines the upper
constants than class 1 ceramics. However, class           operating temperature, and the final letter
2 dielectric constants will fluctuate significantly       determines the maximum change in
with temperature, applied voltage, and over time.         capacitance at any temperature within that
Their dielectric constants can vary significantly         temperature range. Common class 2 EIA
with temperature because the crystal structure of         codes include X8R, X7R, X5R, Y5V, and Z5U.
the ceramic will undergo phase changes within
the operating temperature range of the MLCC.                             EIA Class 2 TC Codes
Class 2 ceramics also show a loss of capacitance         Lower Temp       Upper Temp             Tolerance
when exposed to a DC electric field (DC-bias),            X = -55oC         5 = 85oC             F = ±7.5%
and will exhibit a loss of capacitance over time
                                                          Y = -30 oC       6 = 105oC             P = ±10%
(aging).
                                                          Z = +10 oC       7 = 125oC             R = ±15%
Q2. Who creates the standards for                                          8 = 150oC             S = ±22%
temperature characteristics?                                                                 T = +22% / -33%
                                                                                            U = +22% / -56%
The Electronic Industries Alliance (EIA) and the                                            V = +22% / -82%
Japanese Industrial Standards (JIS) represent the
                                                            Table 2. EIA Class 2 Temperature Coefficient Codes
two main governing bodies for MLCC standards,
including the standards defining temperature              The two main JIS codes for MLCC temperature
characteristics. The JIS is referenced primarily          characteristics are CH, and JB. CH is the
in Japan, and the EIA is referenced in most other         class 1 JIS code, rated for temperatures of -
regions.                                                  25oC to 85oC with a tolerance of ±60ppm/ oC.
                                                          JB is the class 2 code, corresponding to a
Q3. Which Temperature Characteristic are                  ±10% tolerance over the same temperature
commonly referenced?                                      range of -25oC to 85oC.
There are two different sets of code schemes
used in the EIA standards. One set of codes is
used to define temperature characteristics of
class 1 capacitors (table 1), and the other is used
to define temperature characteristics of class 2
capacitors (table 2).


                                                                                      January, 2014
Q4. Do TDK’s part numbers contain the                 structure of the ceramic changes from
temperature characteristics?                          tetragonal to cubic.

TDK includes the TC in both the internal “item        The EIA and JIS standards state that within the
description”, and the catalog number used in          operating temperature range, the change in
distribution channels. The section that is            capacitance will not exceed the specified
common to both is shown below.                        tolerance. The chemical composition of the
                                                      ceramic is not a part of the standard.
 (Commercial) C3216X7R1H105K*****                     Manufacturers of MLCCs use different
 (Automotive) CGA3LX7R1H105K*****                     additives to the dielectrics in order to change
                                                      the performance of the MLCCs. These
                                                      additives can shift the Curie point closer to
 (Commercial) C3216C0G2E223J*****                     room temperature (e.g. Z5U) or smooth the
 (Automotive) CGA3LC0G2E223J*****                     dielectric constant curve (e.g. X7R). The
                                                      former have the highest unbiased dielectric
Q5. If X7R and C0G cover the same                     constants, while the latter lower the maximum
temperature range, how do I pick the one I            dielectric constant in order to achieve greater
need?                                                 temperature stability.
Class 1 capacitors are good for RF matching, and      These formulations are proprietary, and ensure
resonant circuit applications, and are also used in   that not all MLCCs are created equal.
applications requiring precise operation over wide
temperature ranges and operating voltages.            Below is a graph of several MLCC’s
                                                      temperature characteristics.
Class 2 capacitors offer much higher dielectric
constants and therefore have significantly higher
capacitances than a class 1 of the same case
size. This makes them suited for by-pass, bulk
energy storage, and decoupling applications.

Q6. Which temperature characteristics can be
substituted for another?

Temperature characteristics that cover the same
range and offer tighter tolerances are drop-in
compatible. X5R is a good replacement for Y5V
and Z5U because of it’s significantly tighter
tolerances and superior DC bias performance
compared to Y5V and Z5U. Because of this, TDK
no longer offers MLCCs in Y5V or Z5U
temperature characteristics.

X7R (-55oC ~ +125oC) can replace X5R (-55oC ~
+85oC) because the operating temperature range
includes X5R’s completely.                                  Figure 1. A TC graph of three 10nF, 50V,
                                                                        EIA0603MLCCs
Q7. How much change in capacitance with
temperature can I expect?                             Performance Data, including Temperature
                                                      Characteristics curves, for TDK’s MLCCs can
C0G and NP0 Class 1 ceramic temperature               be found on TDK.com.
characteristics do not show significant changes in
capacitance vs temperature.

Generally, heat lowers Class 2 MLCCs’
capacitances, however around the Curie point
(approximately 120oC for BaTiO3), the
capacitance increases. This is due to an
increase in the dielectric constant as the crystal


                                                                                 January, 2014
                 End of Report



Contact TDK for further information or visit our website at www.tdk.com.




                   TDK CORPORATION OF AMERICA.
                        475 Half Day Road, Suite 300
                           Lincolnshire, IL 60069
                           Phone: 847-699-2299
                             Fax: 847-803-6296




                                                                           January, 2014
