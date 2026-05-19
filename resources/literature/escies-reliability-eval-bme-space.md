Reliability Evaluations of BME Capacitors for
              Space Applications



                  David (Donhang) Liu
                   MEI Technologies, Inc.
  Parts, Packaging, and Assembly Technology Office, Code 562
            NASA Goddard Space Flight Center
                  Greenbelt, MD 20771
                          Outline


 • NEPP Funded Deliverables for Fiscal Year 2013
 • Development of a Reliability Model for BME Capacitors
 • Key Issues in Evaluating BME Capacitors for Space
   Applications
 • Summary




6/11/2013             NEPP ETW Presentation by David Liu   2
       NEPP Funded Deliverables for This Fiscal Year

• Engineering guidelines and drawings to be used as specifications for
  NASA procurement of BME capacitors for high-reliability applications
      D. Liu, “Selection, Qualification, Inspection, and Derating of Multilayer Ceramic
       Capacitors with Base-Metal Electrodes,” NASA NEPP FY Report, (2013).
        (https://nepp.nasa.gov/files/24351/Liu_2013_G11_BME_Guidelines.pdf)
      Participating G11 BME Industrial Forum weekly meeting to establish a MIL
       standard for BME capacitors
• Possible reliability model that can become a practical standard for
  advanced MLCCs placed in demanding conditions
      D. Liu, “Reliability of Multilayer Ceramic Capacitors with Base-Metal Electrodes,”
       NASA EEE Parts Bulletin, Special Issue, Vol. 5[2], April/May, pp. 1-10, (2013).
        (https://nepp.nasa.gov/files/24396/EEE_Parts_Bulletin_Apr-May2013_final.pdf)
      D. Liu, “Highly Accelerated Life Stress Testing (HALST) of Base-Metal Electrode
       Multilayer Ceramic Capacitors,” CARTS Proceedings, Houston, TX, pp. 235–248,
       (March 26–29, 2013). (https://nepp.nasa.gov/files/24300/CARTS2013_Liu_HALST.pdf)
      R. Weachock and D. Liu, “Failure Analysis of Dielectric Breakdowns in Base-Metal
       Electrode Multilayer Ceramic Capacitors,” CARTS Proceedings, Houston, TX, pp.
       151–165, (2013). (https://nepp.nasa.gov/files/24303/CARTS2013_Liu_FailureAnalysis.pdf)


  6/11/2013                            NEPP ETW Presentation by David Liu                       3
              A General Expression of Reliability for MLCCs



                        Statistical distribution that describes the individual variation of
                        properties (Weibull, log normal, normal)
                        A function that describes lifetime of a device to respond to
                        the external stresses (independent of individual units)
                        Impacts due to the characteristics of a capacitor device
                        (structure, construction, etc.)

   • Statistical Distribution:
            – 2-parameter Weibull:
            – A function of time, always decreases with time
            – The probability of a failure occurring:
            – The durability of a MLCC that can function normally during wearout:
                • When β >3 and t < η, R(t) ~1, a reliable life span before η
                • When β >3 and t > η, R(t) ~0, part failed rapidly after η


6/11/2013                           NEPP ETW Presentation by David Liu                    4
                                                     Determination of Acceleration Functions

    • Determination of AF(V,T) requires the performance of highly
      accelerated life testing (HALT)
    • A typical HALT method involves the measurements of time-to-
      failure (TTF) data of a group of BME capacitors under certain
      stress conditions
                                                     Weibull ProbabilityPlot of C08X47516 at 165C72V                 TTF (minutes)
                                           99.0
                                                                                                                         81.50
                                                                                                                        601.63
                                           90.0
                                                                                                                        947.00
                                                                                                                       1019.27




       Cumulative Failure Percentile (%)
                                                                                                                       1497.37
                                           50.0                                                                        1565.63
                                                                                                                       1921.03
                                                                                                                       2187.37
                                                                                                                       2189.72
                                                                                                                       2525.67
                                           10.0                                                                        2527.30
                                                                                                                       2564.23
                                            5.0                                                                        2629.02
                                                                                                                       2827.58
                                                                                                                       3096.52
                                                                                                                       3141.35
                                                                                                                       3233.25
                                            1.0
                                             100.0                           1000.0                       10000.0
                                                                                                                       3290.27
                                                                    Stress Time (Minutes)                              3314.33
                                                                                                                       3404.85



6/11/2013                                                                       NEPP ETW Presentation by David Liu                   5
                                                Determination of Acceleration Functions (Cont’d)

                               • Repeat the testing procedure under different stress conditions
                                 (three voltages and three temperatures are normally required)
                                 and a group of TTF data under various stress conditions will be
                                 obtained.
                               • Data set at 135oC, 72V is for verification purposes only.

                                                            Weibull Plot of C08X47516
                                      99.0                                                                                  BME Info.       HALT Conditions     MTTF (min)   Beta (β)    Eta (η)
                                                   165C
                                                                        155C            165C
                                                   80V
                                      90.0                 165C         72V             48V                                                165oC 48V (3X Vr)     4787.46      3.32      5335.48
                                                           72V                                                             C08X47516
                                                                                                                          0805, 0.47uF,
                                                                                                                                          165oC 54V (3.4X Vr)    3087.29      2.95      3459.73




  Cumulative Failure Percentile (%)
                                      50.0                    165C                                                            16V
                                                                                                135C
                                                              64V
                                                                                                72V                        From Mfr. C     165oC 64V (4xVr)      1710.94      4.08      1885.37
                                                                                                 For Verification


                                                                                                                                          165oC 72V (4.5xVr )     998.04      3.53      1108.74
                                      10.0
                                                                                                                                           165oC 80V (5x Vr)      529.27      4.17       582.54
                                       5.0
                                                                                                                                          175oC 72V (4.5xVr )     111.84      2.21       126.28

                                                                                                                                          155oC 72V (4.5xVr )    3029.82      3.47      3368.76

                                       1.0
                                        100.0             1000.0                      10000.0                 100000.0   for verification 135oC 72V (4.5xVr )    19097.00     3.82      21124.00
                                                              Stress Time (minutes)




6/11/2013                                                                                NEPP ETW Presentation by David Liu                                                                6
            Determination of Acceleration Functions (Cont’d)
 • Up to this point the TTF data were processed with Weibull modeling
   only
 • The most widely known acceleration function, the Prokopowicz and
   Vaskas equation, is now applied to process the Weibull modeling
   data and determine the acceleration factors Ea and n, respectively
                      Prokopowicz and Vaskas Equation (P-V Equation):




                                         Acceleration Factors from P-V Equation and MTTF Calculated for 135oC, 72V
               Model Parameters            β             η         Ea (eV)     n        MTTF(min)     MTTF (Hours)
            Calculated Model Results     2.755      3.587E+07       2.60     4.524     126670.20       2111.17
       Verification data at 135oC, 72V   3.822        21124         N/A       N/A       19097.00       318.28

 • The calculated MTTF data using a single Weibull model and P-V
   equation has been widely found to always be longer than that of the
   measured MTTF for most BME capacitors

6/11/2013                                      NEPP ETW Presentation by David Liu                                    7
                                               Determination of Acceleration Functions (Cont’d)
 •                                          The gap between the calculated and the measured has been thought due
                                            to the introduction of some new failure modes that were not found, nor
                                            dominant in PME capacitors.
 •                                          The traditional HALT modeling, using only the TTF data and P-V equation,
                                            is not adequate to characterize the complexity of the failure mechanisms in
                                            BME capacitors.
 •                                          In this study the leakage current against stress time has been measured
                                            together with TTF data
                                               Weibull ProbabilityPlot of C08X47516 at 165C72V
                                     99.0



                                     90.0




 Cumulative Failure Percentile (%)
                                     50.0




                                     10.0



                                      5.0




                                      1.0
                                       100.0                           1000.0                        10000.0
                                                              Stress Time (Minutes)




6/11/2013                                                                                  NEPP ETW Presentation by David Liu   8
            Determination of Acceleration Functions (Cont’d)
                       C08X47516, 165oC, 72V                  Exponential Fitting Eq. (10)     Power-Law Fitting Eq. (11)
     Position on PCB
                       TTF (minutes)       Failure Mode      τ (Hrs)      I(0)       R2      Slope m       A0          R2
          Board
           C15            377.26           Catastrophic      27.778      25.68      0.979     7.528      3.0E-25     0.849
           C12            614.70           Catastrophic      27.778      33.80      0.992     4.832      2.0E-16     0.875
           C16            712.00           Catastrophic      27.778      35.08      0.995     5.197      1.0E-17     0.905
           C19            723.40           Catastrophic      33.333      37.88      0.996     4.375      6.0E-15     0.888
           C14            749.30           Catastrophic      33.333      37.56      0.996     4.679      7.0E-16     0.888
           C10            766.34           Catastrophic      33.333      37.48      0.993     3.953      2.0E-13     0.894
           C18            793.25         Slow Degradation    27.778      41.48      0.998     4.250      2.0E-14     0.887
            C4             805.29          Catastrophic      33.333      38.83      0.994     3.511      4.0E-12     0.898
           C17             866.30          Catastrophic      33.333      40.85      0.997     3.476      6.0E-12     0.896
            C3             908.27          Catastrophic      41.667      41.72      0.993     3.481      4.0E-12     0.902
            C9             953.18          Catastrophic      33.333      39.97      0.994     2.865      5.0E-10     0.908
            C2            1112.39        Slow Degradation    33.333      46.82      0.999     2.791      9.0E-10     0.915
            C8            1124.51        Slow Degradation    33.333      46.82      0.999     2.865      6.0E-10     0.920
            C6            1163.47        Slow Degradation    33.333      47.77      0.999     2.368      2.0E-08     0.924
            C0            1203.19        Slow Degradation    33.333      48.51      0.999     2.417      2.0E-08     0.931
            C7            1235.54          Catastrophic      41.667      45.56      0.992     1.919      6.0E-07     0.935
           C13            1302.47        Slow Degradation    41.667      48.71      0.999     2.138      1.0E-07     0.948
           C11            1425.38        Slow Degradation    41.667      51.88      0.999     1.884      8.0E-07     0.951
            C1            1515.23        Slow Degradation    41.667      53.51      0.999     1.576      8.0E-06     0.968
            C5            1583.30        Slow Degradation    41.667      52.95      0.999     1.293      6.0E-05     0.988

•   Although Slow Degradation (SD) appears linear, exponential form fits the
    data much better：

•   Neither exponential nor power-law fit well for catastrophic failures
6/11/2013                                      NEPP ETW Presentation by David Liu                                            9
    Determination of Acceleration Functions (Cont’d)
                                                        Two Stage Dielectric Wearout
                                 300

                                 250




          Leakage Current (µA)
                                 200
                                                                   Catastrophic   Slow Degradation
                                 150
                                       Failure Criterion: 100 µA
                                 100

                                  50

                                  0
                                       0           50         100          150       200        250   300
                                                               Stress Time (minutes)

• A two-stage dielectric wearout failure mode is better for describing
  the failure behavior in BME MLCCs with BaTiO3
  dielectrics(supported by Failure analysis results)
    – Slow degradation: leakage increases with time nearly linearly due to
      oxygen vacancy migration until the failure criterion (100 µA) is reached
      (parts failed prior to catastrophic failures)
    – Catastrophic failure: leakage current increases gradually, followed by
      time-accelerating catastrophic failures

                                                                                                            10
                                                        Determination of Acceleration Functions (Cont’d)
                                                         Weibull ProbabilityPlot of C08X47516 at 165C72V
                                            99.0                                                                                                              Single Set                      Slow
                                                                                                                         TTF (minutes)   Failure Mode                       Catastrophic
                                                                                                                                                                                           Degradation
                                            90.0                                                                                                            (Traditional)
                                                                                                                            377.26         Catastrophic           F              F             S




        Cumulative Failure Percentile (%)
                                            50.0
                                                                                                                            614.70         Catastrophic           F              F             S
                                                                                                                            712.00         Catastrophic           F              F             S
                                                                                                                            723.40         Catastrophic           F              F             S
                                            10.0
                                                                                                                            749.30         Catastrophic           F              F             S
                                             5.0
                                                                                                                            766.34         Catastrophic           F              F             S
                                                                                                                            793.25       Slow Degradation         F              S             F
                                             1.0
                                              100.0                               1000.0                      10000.0
                                                                                                                            805.29         Catastrophic           F              F             S
                                                                        Stress Time (Minutes)
                                                                                                                            866.30         Catastrophic           F              F             S
                                    99.00
                                                                         C08X47516at 165°C, 72V                             908.27         Catastrophic           F              F             S
                                    90.00
                                                                                                                            953.18         Catastrophic           F              F             S
                                                                                                                           1112.39       Slow Degradation         F              S             F




Normalized Failure Percentile (%)
                                    50.00
                                                                     Catastrophic                                          1124.51       Slow Degradation         F              S             F
                                                                                                                           1163.47       Slow Degradation         F              S             F
                                                                                                                           1203.19       Slow Degradation         F              S             F
                                                                                            SlowDegradation
                                    10.00                                                                                  1235.54         Catastrophic           F              F             S
                                            5.00                                                                           1302.47       Slow Degradation         F              S             F
                                                                                                                           1425.38       Slow Degradation         F              S             F
                                                                                                                           1515.23       Slow Degradation         F              S             F
                                            1.00
                                               100.00                             1000.00

                                                                       Stress Time (minutes)
                                                                                                              10000.00
                                                                                                                           1583.30       Slow Degradation         F              S             F

•                                             When two failure modes A and B are presented in a group of TTF data, Weibull modeling
                                              can be simply processed like this: When TTF data of failure mode A is used for modeling,
                                              the TTF data for mode B can be treated as “censored”, or “suspensions”, meaning that the
                                              capacitors may fail by a different failure mode but cannot be ignored even though the
                                              suspensions were never plotted.
      6/11/2013                                                                                               NEPP ETW Presentation by David Liu                                                         11
                                              Determination of Acceleration Functions (Cont’d)
                                              Weibull ProbabilityPlot of C08X47516 at 165C72V                                                  Contour Plot of C08X47516 at 165Cand72V
                                    99.0                                                                                         12.0



                                    90.0


                                                                                                                                      9.6




Cumulative Failure Percentile (%)
                                                                                                               Slope Parameter Beta
                                    50.0


                                                                                                                                      7.2
                                                                                                                                                                     SlowDegradation


                                                                                                                                      4.8
                                    10.0



                                     5.0

                                                                                                                                      2.4
                                                                                                                                                           Catastrophic



                                     1.0                                                                                              0.0
                                      100.0                           1000.0                         10000.0                           800.0   1120.0       1440.0        1760.0         2080.0   2400.0
                                                             Stress Time (Minutes)                                                                         Scale Parameter Eta


•                                      A interesting Fact: TTF data appears to be a SINGLE failure mode!
•                                      when the leakage current data are used to distinguish the failure modes, TTF
                                       data can clearly be separated into two subsets with two different β values,
                                       indicating the two subsets have different failure modes.
•                                      Most BME manufacturers did not report the mixed failure modes in their HALT
                                       evaluation because they do not measure leakage current!
•                                      Leakage current combined with TTF data measurement is essential for HALT
                                       analysis of BME capacitors
                                     6/11/2013                                              NEPP ETW Presentation by David Liu                                                                        12
          Determination of Acceleration Functions (Cont’d)




•   To repeat the modeling process, a number of MTTF data can be obtained for
    Catastrophic and slow degradation failure modes (curve-fitting coefficient of
    determination R2 is used to compare the fitting results):

      – Catastrophic failures fit power-law (P-V Equation) better:

      – Slow Degradation failures fit exponential-law better:
•   There are no exceptions!
    6/11/2013                       NEPP ETW Presentation by David Liu              13
                Determination of Acceleration Functions (Cont’d)
•       6 quite different Weibull modeling results with respect to three different
        failure scenarios and two different acceleration functions
             Failure Modes         Weibull Modeling Results using P-V Equation       Weibull Modeling Results Using E-Model
               C08X47516           beta         Eta          Ea (eV)      n       beta        Eta           Ea (eV)           -b
        Single Set (Traditional)   2.755    3.587E+07         2.60      4.524    2.7953    1.70E+07         2.612       -0.1813
        Slow Degradation           3.326    1.322E+10         3.78      7.477    3.3486    2.51E+09         3.862       -0.2621
        Catastrophic               3.288    8.055E+05         1.39      3.249    3.2621    4.88E+05         1.393       -0.1341

                   Calculated MTTF (hours) Data of C08X47516 at 135oC and 72V for Model Verification
                                                                          Acceleration Functions
                            Failure Modes                   E-Model (Exponential)         Power Law (P-V Equation)
               Single Set (traditional)                           427.10                          2111.17
               Slow Degradation                                  9438.50                         30835.00
               Catastrophic                                        79.86                          318.67
               Measured Verification Data                                                         318.28
    •     Single set scenario with P-V equation gives rise to a lifetime of 2111.17
          hours which is much longer to that of actually measured 318.28 hours
    •     The single set with exponential acceleration function gives rise to a lifetime
          of 427.10 hours, which is a significant improvement when compared to that
          of measured 318.28 hours (Murata has use this model to calculate MTTF data for a
          number of BME capacitors, all the calculated lifetime results are close but still longer than the
          measured results)
    •     The best MTTF result has been obtained in this study for catastrophic failure
          with a power-law acceleration function
    6/11/2013                                      NEPP ETW Presentation by David Liu                                              14
            Reliability Model of BNE Capacitors




6/11/2013               NEPP ETW Presentation by David Liu   15
     Ceramic Structure of BME Capacitors with BaTiO3

• Ceramic is a polycrystalline structure that
  contains great number of closed-packed
  single crystal grains
• In a ceramic BaTiO3 structure, although
  each grain is polarized, the ceramic posses
  a centrosymmetric structure and is neither
  polarized, nor piezoelectric
• Microstructures of each grain is
  inhomogeneous, a core-shell structure is
  often reported due to the inhomogeneity
  between a grain boundary and the interior
  of a grain
     Core: Ferroelectric BaTiO3 single crystal
     Shell: Non-Ferroelectric, different
      composition and structure


6/11/2013                      NEPP ETW Presentation by David Liu   16
 Ceramic Structure of BME Capacitors with BaTiO3 (Cont’d)

            35oC                   85oC                               125oC




   • Resistivity is also inhomogeneous
       Core is relative conductive; shell is highly resistive (holding the
        insulating resistance (IR) for a BaTiO3 grain)
       The applied voltage distribution is inhomogeneous
       Due to the formation of a high insulating layer at the grain boundary,
        most of the voltage will be applied on the grain boundary region



6/11/2013                       NEPP ETW Presentation by David Liu               17
     Ceramic Structure of BME Capacitors with BaTiO3 (Cont’d)




   • Impact of Grain Size
            When applied voltage and the dielectric thickness is identical for two capacitors,
             the one with a smaller grain size has a better dielectric strength
            This is why powders with smaller particle sizes are always preferred for making
             BME capacitors
            The voltage per grain is the key to characterize the voltage robustness in BaTiO3


                                                                           : average grain size (µm)
                                                                         d : dielectric thickness (µm)


            A key Structural parameter that determines the dielectric
            strength and reliability!
6/11/2013                           NEPP ETW Presentation by David Liu                               18
Microstructure Determines the Rated Voltage of BME Capacitors
    CAP ID
               Grain Size
                 (µm)
                              Dielectric
                            Thickness(µm)
                                            # of grains
                                             per layer
                                                          Voltage per
                                                            Grain
                                                                        • A number of BME capacitors from
   A08X22525     0.305           3.89          12.75          1.96        different manufacturers with
   B08X10525     0.400           4.60          11.50          2.17
   C08X22525     0.320           3.80          11.88          2.11        different chip size, capacitance,
   B08X33425     0.420           5.80          13.81          1.81
   A06X10425     0.470           7.89          16.79          1.49        and rated voltage have been
   B06X22425     0.340           4.20          12.35          2.02
   B04X47325     0.305           4.00          13.11          1.91
                                                                          processed for microstructure
   C04X47325
   B12X10525
                 0.386
                 0.421
                                 4.40
                                 6.15
                                               11.40
                                               14.61
                                                              2.19
                                                              1.71
                                                                          analysis
   B12X47525     0.376           4.34          11.54          2.17
   C08X56425     0.339           4.00          11.80          2.12
                                                                        • At a given rated voltage, the Vgrain
   P08X10425     0.790          20.20          25.57          0.98        is almost constant! It decreases
   A06X10516     0.296          3.01          10.17          1.57         with decreasing rated voltage
   A12X10616     0.344          3.51          10.20          1.57
   C04X10416
   A08X47416
                 0.332
                 0.319
                                3.40
                                3.75
                                              10.24
                                              11.76
                                                             1.56
                                                             1.36
                                                                        • Similarly, number of grains per
   B12X68416     0.375          6.21          16.56          0.97         dielectric layer also does not
   C08X22516     0.224          3.81          17.01          0.94
   C12X10616     0.264          2.80          10.61          1.51         change much when the rated
   B08X22516     0.340          3.23           9.50          1.68
   B08X56416     0.373          4.21          11.29          1.42         voltage is the given
   C08X47516     0.230          2.49          10.83          1.48
   B12X10516     0.475          7.82          16.45          0.97       • The rated voltage is determined
   B04X10416     0.342          3.05           8.91          1.80
                                                                          by the microstructure of BME
   B12X10606     0.365          3.11           8.51          0.74
   B04X10406     0.323          2.50           7.74          0.81
                                                                          capacitors
   B04X56306     0.407          3.00           7.37          0.85
   B06X10506     0.426          2.80           6.57          0.96
   C08X10606     0.330          2.23           6.76          0.93
   B08X22506     0.419          3.42           8.16          0.77
   A12X22606     0.309          1.82           5.90          1.07
   B06X22406     0.373          4.01          10.76          0.59
   P06X10405     0.770         12.60          16.36          0.39

   6/11/2013                                    NEPP ETW Presentation by David Liu                               19
             Reliability vs. Microstructure Parameter




• Mean-time-to-failure (MTTF) data as a function of number of grains per
  dielectric layer has been measured at 150oC and 10KV/mm
   •     More grains per dielectric layer, longer the MTTF
   •     When voltage per grain is normalized to a constant value, the MTTF data
         are identical to a single grain

 Prokopowicz and Vaskas Equation:

 At a given temperature:



 6/11/2013                      NEPP ETW Presentation by David Liu            20
            BME Capacitor Reliability: Reliability Defects
• Reliability failure is caused by reliability defects
• Quality Defects and Reliability Defects:
       Quality Defects: refer to deficient products or components at present,
        particularly deficient parts that are out of the standard specifications; quality is
        generally expressed in percentages.
       Reliability Defects: refer to failures that might occur in the future inside a
        product that has been working well so far. Therefore, reliability must be
        regarded as a ratio expressed in terms of units of time.
• Reliability defects may behave in two ways:
      • They can be benign for the rest of the product life without causing a
        failure
      • They can be catastrophic depending on the feature size and the level
        of external stress
• It is equivalent to increase external stress level:
      • To increase the applied voltage for a given dielectric thickness
      • To decrease the dielectric thickness at a constant voltage


6/11/2013                           NEPP ETW Presentation by David Liu                         21
  BME Capacitor Reliability: Reliability Defects (Cont’d)


                                                                        Reliability
                                 Reliability   Dielectric               Defect
Dielectric                                     Thickness d
                                 Defect                                 Feature
Thickness d
                                 Feature                                Size r
                                 Size r



 Dielectric layer reliability:


         For Weibull model:


                     Since:


                  We have:


        P is a geometric factor that determines the dielectric reliability
                with respect to the microstructure of an MLCC.
 6/11/2013                        NEPP ETW Presentation by David Liu             22
 BME Capacitor Reliability: Reliability Defects (Cont’d)

With External Stress:



       We have:



      In general:

   So finally, single layer dielectric reliability can be simplified as:




  α is an empirical constant that depends on the processing conditions
                  and microstructure of a ceramic capacitor.
                α ≈ 6 (V ≤ 50) and α ≈ 5 (V >50) For BME MLCCs
                           α ≈ 5 for most PME MLCCs
6/11/2013                   NEPP ETW Presentation by David Liu             23
                    BME Capacitor Reliability:
                  From Single Layer to Multilayer




     Total capacitance:



     Total reliability:


                          : Single dielectric layer reliability, as discussed earlier

6/11/2013                           NEPP ETW Presentation by David Liu                  24
                                       BME Capacitor Reliability:
                                     From Single Layer to Multilayer
                                                (Cont’d)
                                                                                             Ri=99.999%
                                    100%




              Reliability of MLCC
                                                                                      Ri=99.99%

                                    80%                                    Ri=99.9%

                                                           Ri=99.0%
                                    60%

                                    40%

                                    20%

                                     0%
                                           1          10                      100                    1000
                                                   Number of Dielectric Layers N



      •     The reliability of an MLCC Rt decreases with increasing N
      •     The value of N can be as high as 1000!




6/11/2013                                      NEPP ETW Presentation by David Liu                           25
            Reliability Model of BME Capacitors




6/11/2013               NEPP ETW Presentation by David Liu   29
                                       Key Issues

 • BME capacitors can’t be screened to be high-reliability, they
   have to be made for space-level applications
      – Practices by individual manufacturers are based on lessons
        learned
      – Need better understanding of failure mechanisms, and quality on
        high reliability (As has been discussed previously)
      – Design rules
             Dielectric thickness vs. rated voltage
             Number of dielectric layers
             Margins (JAXA guidelines)
             Chip sizes
     − Raw Materials Control
             How to control
             Requires lot specific verification
     − A Specification Controlled Drawing (SCD) in the format of GSFC
       S-311 document is in development




6/11/2013                            NEPP ETW Presentation by David Liu   30
                                    Key Issues (Cont'd)
 • Different manufacturers, different behaviors
       – Two BMEs with same cap, chip size, and rated voltage can reveal quite
         different reliability life
       – To team up with ONE manufacturer: like ESA and AVX
       – Need to find a supplier to team up and also find a way to balance the sole
         source supplier (for FY14)
 • Almost all BME capacitors are manufactured outside USA
       − In-Process Inspection would be performed for each production lot during the
         qualification. The inspection should be performed as per Table below
       − The raw material control and lot inspection shall follow MIL-PRF-123,
         paragraph 4.5.2.1.




    *: 0.65 AQL for J size for normal inspection per ANSI/ASQ Z 1.4. AQL for MIL-PRF-123 is 1.50 for the
    same lot size and inspection level.

6/11/2013                               NEPP ETW Presentation by David Liu                                 31
                          Key Issues (Cont'd)
• Screening of commercial BMEs for high-reliability has
  been practiced at NASA Goddard (Non-critical
  missions only)
      − All BME capacitors are commercial, made for high volume,
        high volumetric efficiency: i.e., highest capacitance/volume
      − Select units from various suppliers (typically 100% screened
        and meeting a certain level of reliability: e.g., automotive
        grade) with moderate cap values, and perform significant
        voltage derating
      − Evaluation is still in progress (to be completed in FY14)
      − The results will help to develop an independent section for
        IEEE-INST-002 for BME capacitors (for FY14)




6/11/2013                   NEPP ETW Presentation by David Liu         32
      Selection of BME Capacitors for High Reliability Applications

        Table 1. Selection criteria of BME capacitors for space-level applications
                                                                                                                                                              Part
                   Inspection/Test                                             Test Methods, Conditions, and Requirements                                  Type/Level
                                                                                                                                                           1    2    3
                                                       The voltage temperature characteristic shall be referenced to the +25oC value and shall be
   1. Dielectric Type                                  applicable over the entire temperature range of -55oC to +125oC. Dielectric type C0G ( N )          X    X    X
                                                       shall be 0±30 ppm/oC, and dielectric type X7R ( X ) shall be +15, -15%.
                                                       Destructive physical analysis shall be performed on each inspection lot of capacitors supplied
                                                       to this specification.
                                                           - DPA sample size shall follow MIL-PRF-123, Table XVII.
  2. Destructive Physical Analysis (DPA)                   - DPA shall be performed in accordance with the requirements of MIL-PRF-123,                    X    X    X
                                                       paragraph 4.6.1, except that paragraphs 3.4.1 and 3.4.2 shall be replaced with paragraph 2.3
                                                       herein.
                                                           - Margin defects shall be determined using EIA 469, paragraph 5.1.3.
                                                       BME capacitors shall not be used for high reliability space applications if the following
  3. Microstructure Analysis
                                                       construction and microstructure criteria are not satisfied
   3.1. Nickel Electrodes                              All BME capacitors shall use nickel for internal electrodes
                                                       The structure parameter of a BME ceramic capacitor P with respect to its microstructure and
                                                       construction details can be expressed as:


                                                       Where: d = Dielectric thickness that is the actual measured thickness of the fired ceramic
   3.2.Capacitor Structure Parameter                   dielectric layer. Voids, or the cumulative effect of voids, shall not reduce the total dielectric   X    X    X
                                                       thickness by more than 50%.
                                                          ā= Averaged ceramic grain size measured per the linear interception method.
                                                          N = Number of individual dielectric layers.
                                                          α= An empirical parameter that is applied voltage-dependent: α= 6 for V ≤ 50V, and α= 5
                                                       for V > 50V.
   3.3. Acceptance Criterion for X7R                   The calculated R shall be greater than 1.00000 for X7R dielectric
                                                       The minimum dielectric thickness shall be greater than 3.0 micrometers for the NPO dielectric
   3.4. Acceptance Criterion for C0G1/
                                                       at V ≤ 50V and greater than 5.0 micrometers at V > 50V; N should be less than 300.
                                                       The maximum dielectric constant shall be 4000 for the X7R dielectric and 100 for the C0G
  4. Maximum dielectric constant                                                                                                                           X    X    X
                                                       dielectric.
                                                       Devices supplied to this specification shall have a termination coating of copper, nickel, or
  5. Termination                                       their alloy, or shall be base-metal barrier tin-lead solder (MIL-PRF-123, type Z) plated. Tin-      X    X    X
                                                       lead solder plating shall contain a minimum of 4% lead, by mass.
   1/: BME capacitors with NPO dielectric of CaZrO3 are not ferroelectric and the MTTF is not controlled by the grain boundaries, therefore, NPO capacitors have a different
   selection criterion from those with X7R dielectric.

6/11/2013                                               NEPP ETW Presentation by David Liu                                                                                     33
            Selection Criterion and the Number of Zeros



                                    BX life to failure rate:   BX life to Reliability:


                                    M: B1% life                M: B1% life               where R(x1%) =0.99
                                    P: B0.1% life              P: B0.1% life             where R(x2%) =0.999
                                    R: B0.01% life             R: B0.01% life            where R(x3%) =0.9999
                                    S: B0.001% life            S: B0.001% life           where R(x4%) =0.99999


MIL-PRF-55681, paragraph, 1.2.1.7




  Number of zeros represents the level of failure rate!




6/11/2013                              NEPP ETW Presentation by David Liu                                        34
                                              Qualification Plan
   • Qualification Inspection shall be performed at a laboratory acceptable
     to the qualifying agency on sample units produced with equipment and
     procedures normally used in production
                                             BME Capacitors Qualifications
                                                                                                                Sample Size
                                             Test Methods, Conditions, and
       Inspection/Test                                                                               AEC-Q200   MIL-PRF-123
                                                                                                                                This
                                                    Requirements                                                              Document
              Group I
                                      MIL-STD-202, Method 107, Condition B, min. rated temp.
   1. Thermal Shock                   to max. rated temp. (when specified in the product               N/A          182         200
                                      specification/ data sheet, the min. and max. “storage” temp.
                                      shall be used in lieu of the specified operating temp.)
                                         4 x rated voltage,
   2. Voltage Conditioning (Burn-        125 °C, 160 hours (Level 1)
                                                                                                       N/A          182         200
      In)                                125 °C, 96 hours (Level 2)
                                         125 °C, 48 hours (Level 3)
   3. Electrical Measurements            As specified
      Capacitance                        MIL-STD-202, Method 305
      Dissipation Factor                 MIL-STD-202, Method 305(shall be 306)
                                                                                                       100%        100%        100%
      DWV                                MIL-STD-202, Method 301
      Insulation Resistance              MIL-STD-202, Method 302
               Group II
   1. Visual and Mechanical          Visual and sample-based mechanical inspection to be
      Examination, material, design, performed to requirements of applicable military                   30         15(1)        15(0)
      construction and workmanship specification
                                        Destructive physical analysis shall be performed on each
                                      inspection lot of capacitors supplied to this specification.
                                         - DPA shall be performed in accordance with the
   2. Destructive physical analysis   requirements of MIL-PRF-123, paragraph 4.6.1, except              10         15(1)        15(0)
                                      that paragraphs 3.4.1 and 3.4.2 shall be replaced with
                                      paragraph 2.3 herein.
                                         - Margin defects shall be determined using EIA 469,
                                      paragraph 5.1.3.
6/11/2013                                                    NEPP ETW Presentation by David Liu                                          35
                                         Qualification Plan (Cont'd)
                                        BME Capacitors Qualifications (Cont’d)
                                                                                                                 Sample Size
                                                 Test Methods, Conditions, and
            Inspection/Test                                                                           AEC-Q200   MIL-PRF-123
                                                                                                                                 This
                                                        Requirements                                                           Document
     Group IIIb - Nonleaded devices
  1. Terminal strength                         AEC-Q200-006; MIL-STD-202, Method 211                     30           12(1)     15(0)
  2. Solderability                             MIL-STD-202, Method 208                                   15           12(1)     15(0)
  3. Resistance to soldering heat              MIL-STD-202, Method 210; condition C                      30           12(1)     15(0)
                Group IV
                                             Capacitance change over the range of temperatures
                                             and voltages specified shall not exceed limits of
 1. Voltage-temperature limits                                                                          N/A           12(1)     15(0)
                                             specification. NPO Capacitors shall be tested in
                                             accordance with MIL-PRF-123 BP characteristics.
                                             MIL-STD-202, Method 106
                                             20 cycles (first 10 cycles with rated voltage applied)
  2. Moisture resistance                                                                                 77           12(1)     15(0)
                                             DWV, IR and DC to specification
                                             AEC-Q200-006 removed this test in version D
                Group V
 1. Humidity, steady state, low voltage 1/           Not required for BME capacitors                    N/A           12(0)
                                               MIL-STD-202, Method 103
 1. Biased Humidity                                                                                      77           N/A       125(0)
                                               AEC-Q200 Biased Humidity
 2. Beam Load Test                             AEC-Q200 -003                                             30           N/A       15(0)
 3. Resistance to solvents                     MIL-STD-202, Method 215                                   5            12(1)     15(0)
                Group VI
                                               MIL-STD-202, Method 108
                                               Ttest = maximum operating temperature
                                               Vtest = 2 X Vrated (1X Vrated perAEC-Q200-
  Life 2/                                    006)                                                        77          123(1)     125(0)
                                               Duration: 4,000 hours for level 1,
                                                         2,000 hours for levels 2 and 3
                                               IR, ∆C, and DF to specification
Note 1: Humidity, steady state, low voltage in group V is not required. (This test is required for PME capacitors with
potential micro cracks and silver electrode migration. However, the DPA of significant number of virgin BME
capacitors did not reveal any cracks and the nickel migration is insignificant when comparing to that of silver.)
Note 2: Life test, AQL=0.10 for K Size normal inspection per ANSI/ASQ Z 1.4
  6/11/2013                                         NEPP ETW Presentation by David Liu                                                    36
             Voltage Derating of BME capacitors
 •    Derating shall be performed by the designer in accordance with
      the requirements set in Table below for different dielectric types.
 •    Voltage derating is accomplished by multiplying the maximum
      operating voltage by the appropriate derating factor appearing in
      Table below.
 •    The derating factor applies to the sum of peak AC ripple and DC
      voltage applied.
 •    Voltage derating factor of 0.6 was determined in this study. A
      10V unit will be derated to 0.4X10V = 4V
 •    Ambient temperature was determined with ripple current
      simulation results

                      Voltage Derating Chart for BME Capacitors
        Dielectric Type     Voltage Derating Factors          Maximum Ambient Temperature
             X7R                      0.6                              110°C
             NPO                      0.2                              125oC


6/11/2013                    NEPP ETW Presentation by David Liu                             38
                        Summary
• A general reliability model for BME capacitors has
  been developed with respect to the acceleration
  function and BME capacitor’s structural parameters
• Improved reliability lifetime calculations can be
  achieved with the proposed reliability model for BME
  capacitors
• As part of this fiscal year’s deliverables, A guideline
  documentation on Selection, Qualification, Inspection,
  and Derating of BME capacitors has been completed
  and uploaded to NASA NEPP website




6/11/2013               NEPP ETW Presentation by David Liu   39
