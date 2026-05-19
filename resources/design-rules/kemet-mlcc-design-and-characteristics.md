    Multilayer Ceramic Capacitors (MLCCs)



    Design and Characteristics

1
Form Factor




              © 2019 KEMET Corporation
 Design




© 2019 KEMET Corporation
MLCCs

                           Detailed Cross Section
                                               Dielectric Material
                                                                                  C = Design Capacitance
                                                                                  K = Dielectric Constant
                                                                                  A = Overlap Area
                                                                                  d = Ceramic Thickness
                                                                                  n = Number of Electrodes

         Inner Electrode

                                        End Termination

+                                                 Barrier Layer
 -                                                        Termination Finish
     Capacitances in parallel are additive
       CT=C1+C2+C3+….Cn                                    © 2019 KEMET Corporation
  Common Failure Modes




© 2019 KEMET Corporation
Ceramic Materials are Inherently Brittle


                                                          Ceramic Properties
                                                          •   High chemical bond strength
                                                          •   High Elastic Modulus
                                                          •   Low Ductility
                                                          •   Very Hard




                               © 2019 KEMET Corporation
Typical Crack Signatures


The major sources of MLCC cracks are:
  • Mechanical damage (impact)
    ‒ Aggressive pick and place                                                             Mechanical
    ‒ Physical mishandling                                                                   Damage


  • Thermal shock (parallel plate crack)
    ‒ Extreme temperature cycling
    ‒ Hand soldering
       •   Do not touch electrodes while hand soldering!                          Thermal Shock Crack


  • Flex or Bend stress
    ‒ Occurs after mounted to board
    ‒ Common for larger chips (>0805)
                                                                                            Flex Crack


                                               Failure is not always immediate!
                                                   © 2019 KEMET Corporation
External Forces on Ceramic Material


           Compression                                                      Tension


                             Force                              Force                        Force
   Force




       Strong under compression                                         Weak under tension




                                     © 2019 KEMET Corporation
Flex Cracking
Excessive Bending

                      MLCC Under Tension




                       High Stress Region




                    Finite Element Analysis

                         © 2019 KEMET Corporation
Flex Cracking
Excessive Bending


                               MLCC Active Area




    Flex crack signature
                                                      Starts here




                           © 2019 KEMET Corporation
Capacitor Mitigation Solutions
Level 1 Protection – Basic Level of Crack Protection

            Floating Electrode                 MLCC Active Area           Open Mode




    Pros                                                      Pros
    • Serial design                                           • Crack doesn’t go through active area
    • Fails open                                              • Fails open
    Cons                                                      Cons
    • Reduced capacitance in the same volume                  • Reduced capacitance in the same volume




                                           © 2019 KEMET Corporation
 Capacitor Mitigation Solutions
 Level 2 Protection – Intermediate Level of Crack Protection

                                         Flexible Termination (FT-CAP)
                                                                                      Pros
                                                                                      • Increased flex capability
                                                                                      • High volumetric efficiency
                                                                                      Cons
                                                                                      • Fail short

                                        End Termination/                                        Conductive-Epoxy
                                        External
                                        Electrode (Cu)                                                Crack

Termination Finish
                                  Flexible
(100% Matte
                                  Termination
Sn/SnPb–5% Pb min)
                                  Epoxy Layer (Ag)

                                                                                         Conductive-Epoxy
                 Barrier Layer (Ni)



                                                           © 2019 KEMET Corporation
Capacitor Mitigation Solutions
Level 3 Protection – High Level of Crack Protection (Hybrid Technology)


                     Flexible Termination (FT-CAP) +                      Flexible Termination (FT-CAP) +
                            Floating Electrode                                       Open Mode




   Pros
   • Increased flex capability
   • Floating Electrode design
   • Fail Open

   Cons
   • Reduced capacitance in the same volume

                                             © 2019 KEMET Corporation
Thermal Shock
Why is it an issue?

                                                       Dielectric Material




                          Inner Electrode   Circuit Board


                                             End Termination
  CTE – Coefficient of Thermal Expansion
                                                            Barrier Layer
                                                                 Termination Finish

                      Thermal Shock Cracks  CTE Mismatch
                                            © 2019 KEMET Corporation
Thermal Shock
Causes – Hand Soldering




                                                                Hand Solder Tips
             COLD                         HOT                   •   Don’t touch capacitor termination
                                                                •   Pre-heat assembly
                                                                •   Larger case sizes are more sensitive




                          Internal Temperature Gradients
                             Uneven Expansion and Contraction
                                 © 2019 KEMET Corporation
Thermal Shock
Causes – Solder Wave




                                               PCB Travel



                                         Solder Wave


                       Molten Solder

                               © 2019 KEMET Corporation
What is MLCC Surface Arcing?




                                                                              Influences
                                                                              • Humidity
                                                                              • Surface Contamination
                                                                              • Creepage Distance




                  Electrical breakdown between the two MLCC terminations or
                 between one of the terminations and the internal electrodes of
                               the capacitor within the ceramic body.



                                    © 2019 KEMET Corporation
The Phenomenon of Surface Arcing

          First Counter                               Electric Field
                                Ionization of Air
            Electrode




                                    Opposing
                                    Electrodes

                                   Opposing
                                  Terminations


                           © 2019 KEMET Corporation
The Phenomenon of Surface Arcing

                                 Electric Arc




                           © 2019 KEMET Corporation
Surface Arcing Between MLCC Termination and the
Internal Electrode Structure




                            © 2019 KEMET Corporation
Surface Arcing Failure Modes


        Terminal-to-Terminal Arcing                              Terminal-to-Active Arcing




               Carbon Traces



                                                                  Voltage Breakdown Failures
                                      © 2019 KEMET Corporation
Solutions for MLCC Surface Arcing


      Surface Coatings                             Serial Electrode Designs                        ArcShield Designs




• MLCC Coating                              • Reduce electric field strength                     • Reduce electric field strength
  –   Added by MLCC supplier                   –   Available capacitance in a MLCC package
  –   Additional process step
                                                                                                 • Reduce ionization of air at MLCC
                                                   size is lowered
                                                                                                   surface
  –   Critical that there is no damage to      –   Allows for higher voltage capability
      or air gap under the coating             –   Reduces the probability of MLCC failure due
                                                                                                 • Maximizes available capacitance
• PCB Coating                                      to flex crack                                   in a MLCC package size
  –   Added after PCB assembly
  –   Additional process step
  –   Added cost
  –   Cannot rework



                                                         © 2019 KEMET Corporation
The Benefits of Coating Technology

                                Creepage Distance
           Low K Coating

                                   Ionization of Air




                             © 2019 KEMET Corporation
Issues With Coating Technologies

                      Electric Arc                              Damaged Coating




                                     © 2019 KEMET Corporation
Serial Electrode Design
Reduction of Electric Field

                              1000V


    Single MLCC                                       1uF 1000V


                                                                                                      1          1
                              1000V           1000V         1000V           1000V          1000V            = �
                                                                                                   𝐶𝐶𝐶𝐶𝐶𝐶𝐶𝐶     𝐶𝐶𝑁𝑁

   Five Series MLCCs                                                                               0.22uF 5000V

                                      Electric Field Distributed Across Individual MLCCs


                              1000V           1000V         1000V           1000V          1000V


Single Monolithic Structure                                                                        0.22uF 5000V
      (Serial Design)
                                 Electric Field Distributed Across Each Serial Design


                                                 © 2019 KEMET Corporation
Serial Electrode Design

                               High-Voltage Ceramic
               Also known as “Floating Electrode” or “Cascade Electrode” designs
                               Capacitive                  Capacitive
                                 Area                        Area




                                        Separation Between
                                         Series Elements

                                     © 2019 KEMET Corporation
“Serial” to “Shield” Design Comparison

                    V/2            V/2




                   “Serial” Design                                   “Shield” Design
        • With capacitors (N) in series, the            • Larger electrode area overlap A so
            acting voltage on each capacitor is           higher capacitance while retaining
            reduced by the reciprocal of the              high voltage breakdown.
            number of capacitors (1/N).                 • Thickness d between opposing
        •   Effective Capacitance is reduced:             electrodes increased:
                     1          1                                       ϵo KNA
                           = �                                       C=
                  𝐶𝐶𝐶𝐶𝐶𝐶𝐶𝐶     𝐶𝐶𝑁𝑁                                        d
                                          © 2019 KEMET Corporation
KEMET ArcShield Technology




         Shield                                           Shield
       Electrodes                                       Electrodes




                             © 2019 KEMET Corporation
Explanation of Shield Design
Reduction of Electric Field


  Terminal-to-Terminal Arcing                            Terminal-to-Terminal Arcing
  Standard Design                                        ArcShield Design
  • Opposite Field extends close to terminal of          • Opposite Field is longer distance from
    opposed polarity so low energy barrier                 terminal of opposed polarity increasing size
                                                           of energy barrier
            -                                  +        -                                  +




            E                                            E



                                           © 2019 KEMET Corporation
Explanation of Shield Design
Designed for Higher Voltage


 Consider a Standard Design                                                         2.
 • In a standard overlap X7R MLCC there are                               1.
   3 ways of failing high voltage:                          -                            +
    1.   Arcing between terminal and 1st electrode
         of opposite polarity
    2.   Arcing between terminals                                    3.
    3.   Internal breakdown
 Shield designs solve these voltage
 breakdown issues by:                                       -        a.        b.        +
    a. Adding a shield to prevent 1.
    b. The shield also creates a barrier to 2.
    c. Thicker actives for higher breakdown 3.                       c.


                                          © 2019 KEMET Corporation
KEMET ArcShield Technology
Summary



 • Permanent Protection

 • No protective coating necessary

 • Higher breakdown voltage capability than similarly rated devices using coating

   technology.

 • Downsizing and board space saving opportunities.




                                     © 2019 KEMET Corporation
ArcShield Key Features and Benefits

                          Patented Electrode Design
    • Suppresses an arc-over event while increasing available capacitance



                          Permanent protection!
• Competitive versions often use a non-permanent surface coating




                          BME X7R Dielectric


                   500, 630 and 1,000Vdc                                                    Shield Electrode Technology
                                                                                               Built Inside the MLCC

                    0603 - 2225 Case Sizes


                                        1.0nF – 560nF                                        “The World’s Smallest
                                                                                             High Voltage MLCC’s”
                    Flexible Termination Available

                                                                            © 2019 KEMET Corporation
 Thank You




© 2019 KEMET Corporation
