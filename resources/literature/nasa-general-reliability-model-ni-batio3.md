             A General Reliability Model for Ni-BaTiO3-Based Multilayer
                                 Ceramic Capacitors
                                             Donhang (David) Liu
                                               AS and D, Inc.
                             7515 Mission Drive, Suite 200, Seabrook, MD 20706
                            Work performed for NASA Goddard Space Flight Center
                            8800 Greenbelt Road, Greenbelt, Maryland 20771, USA
                                          Donhang.liu-1@nasa.gov


Abstract

The evaluation for potential space project applications of multilayer ceramic capacitors (MLCCs) with Ni electrode
and BaTiO3 dielectric material requires an in-depth understanding of the MLCCs’ reliability. A general reliability
model for Ni-BaTiO3 MLCCs is developed and discussed in this paper. The model consists of three parts: a statistical
distribution; an acceleration function that describes how a capacitor’s reliability life responds to external stresses; and
an empirical function that defines the contribution of the structural and constructional characteristics of a multilayer
capacitor device, such as the number of dielectric layers N, dielectric thickness d, average grain size , and capacitor
chip size A. Application examples are also discussed based on the proposed reliability model for Ni-BaTiO3 MLCCs.

Introduction

Multilayer ceramic capacitors (MLCCs) are key building blocks in modern electronics [1]. MLCCs constitute ~30%
of the total components in a typical hybrid circuit module such as a DC-DC converter. The numbers of ceramic
capacitors used in integrated circuit (IC) power supply decoupling applications are even greater. Due to the increasing
demand for decoupling capacitors and to the limited space available, the use of Ni-BaTiO3 capacitors with a higher
capacitance and a smaller chip size is more attractive for current large-scale IC chip packages.

Indeed, a typical central processing unit (CPU) package today requires more than 100 ceramic capacitors performing
a variety of functions related to power delivery and signal integrity. These capacitors all need to work reliably for the
CPU to function. Due to cost pressures, the degree of redundancy in CPU systems has been reduced, and so the failure
of even one capacitor can cause the whole system to fail.

In its simplest form, capacitor system reliability can be expressed as:

              Capacitor system reliability = component reliability Number of capacitors                                (1)
If a CPU system with 100 capacitors needs to maintain a system reliability of 99.9%, each capacitor must have an
individual component reliability of 99.999% [2]. As a result, in order to improve system reliability, it is vital to better
understand and improve the reliability of MLCCs.

Reliability of Ni-BaTiO3 MLCCs

1. Reliability of MLCCs
The reliability of a MLCC is the ability of the dielectric material to retain its insulating properties under stated
environmental and operational conditions for a specified period of time t. Reliability defects are the failures that might
occur in the future inside a capacitor product that has been working well so far. Therefore, reliability must be regarded
as a function of time and of external stresses. In addition, the construction and structural parameters of a MLCC
device will also have an impact on its reliability.




To be presented by David (Donhang) Liu at the Capacitors and Resistors Technology Symposium
(CARTS) conference, Santa Clara, California, April 1-3, 2014.                                                            1
As a result, a general expression of MLCC reliability shall consist of three parts and can be expressed as [3]:

                                   () = (, , , ) ×         ( , ) × ()                                           (2)

where: () is a statistical distribution that describes the individual variation of properties in a testing group of samples
(Weibull, log normal, normal, etc.); ( , ) is an acceleration function that describes how a capacitor’s reliability
responds to external stresses such as applied voltage V and temperature T. All units in the testing group should follow
the same acceleration function if they share the same failure mode (independent of individual units); and

(, , , ) describes the effects on reliability from the structural and constructional characteristics of a capacitor
device, such as the number of dielectric layers N, the dielectric thickness d, average grain size , and capacitor chip
size A.

In general, a 2-parameter Weibull statistical distribution model is often used in the description of a Ni-BaTiO3
capacitor’s reliability as a function of time:
                                                            
                                                          ( )
                                                () =                                                                 (3)

where e is the base for natural logarithms,  is the dimensionless slope parameter whose value is often characteristic
of the particular failure mode under study, and  is the scale parameter that represents a characteristic time at which
63.2% of the population has failed and that is related to all other characteristic times, such as mean time to failure
(MTTF):

                                                   = (1 + 1 ),                                                     (4)

where  is the gamma function of x (Note:               >3.0).

Equation (3) provides a simple and clear understanding of the meaning of reliability:

    •    Reliability is a monotonic function of time and always decreases with time, which indicates that the loss of
         reliability is a common behavior for all devices.
    •    Since  and  always exceed zero, the value of R(t) is always between 0 and 1, indicating that reliability can
         also be viewed as the probability of a failure occurring.
    •    Reliability typically defines the durability of a device that can function normally. When  > 3 and  , R(t)
         ~1, suggesting a reliable lifespan before . When t > , R(t) decreases rapidly to 0. The lifetime of a device
         to sustain its function can be characterized by , as shown in Eq. (4).

2. Acceleration Functions of Ni-BaTiO3 MLCCs
    ( , ) in the general reliability form of Eq. (2), represents the impacts of external stresses (applied voltage and
temperature are commonly used) on the reliability of a Ni-BaTiO3 capacitor. It is widely known that the time to failure
(TTF) for a MLCC that is caused by a single failure mode when both V and T are changed from V1 to V2 and T1 to T2
is the product of the separate acceleration factors:

                                                  $% '    '
                                     =  =   !" # &  *  -                                                     (5)
                                                                         

where n is an empirical parameter that represents the voltage acceleration factors, ./ is an activation energy that
represents the temperature acceleration factor, and 0 is the Boltzmann constant.

This well-known Prokopowicz and Vaskas equation has proven to be useful in the capacitor industry for testing
MLCCs with precious metal electrodes (PMEs) at various highly accelerated testing conditions. An average of n23
has been found for the voltage acceleration factor, and an average value of 1 < ./ < 2 eV is typical for the
temperature acceleration factor [4].




To be presented by David (Donhang) Liu at the Capacitors and Resistors Technology Symposium
(CARTS) conference, Santa Clara, California, April 1-3, 2014.                                                             2
Since only a single failure mode is assumed, the value of E in Eq. (3) is usually assumed not to change with applied
stresses. Only the Weibull distribution scale parameter K will change with external stresses. This can be expressed,
according to Eq. (5), as
                                                                    7
                                                           4
                                           ( , ) =  5 6  (8) ,                                                     (6)

where C and B = ./ /0 are constants.

Due to the impact of oxygen vacancy electromigration on the reliability of Ni-BaTiO3 capacitors, the acceleration
function ( , ) of Ni-BaTiO3 capacitors has been found to not always follow the power law with respect to applied
voltage as specified in Eq. (5). Mixed failure modes have often been reported for Ni-BaTiO3 capacitors [5-9].

A recent NASA-funded study that combines the measurement of both TTF and capacitor leakage current as a function
of stress has been developed and used to describe the reliability of Ni-BaTiO3 capacitors. A two-stage dielectric wear-
out process that initiates with a slow dielectric degradation, followed by a thermally dominated catastrophic
breakdown, has been revealed (Figure 1). When the failure criterion is set with respect to a leakage current level,
some Ni-BaTiO3 capacitors will reach the failure level with a catastrophic failure, and some will fail prior to the
occurrence of a catastrophic dielectric breakdown [3, 8-9].




 Figure 1. A two-stage dielectric wear-out failure mode is proposed to describe the dielectric breakdown behaviors
                                                in BME capacitors.

Further investigation also revealed that the two identified failure modes follow different acceleration functions. Slow
degradation fits well to an exponential law against the applied field. Catastrophic failures fit the power-law better [3].
Table I summarizes the two failure modes and corresponding voltage acceleration functions that may be used to model
the Ni-BaTiO3 capacitors’ reliability life.

                  Table I. Summary of Acceleration Functions for Ni-BaTiO3 MLCCs
                  Acceleration      Expression to scale
  Failure mode                                                   Expression to time to failure (TTF)
                   function            parameter :
  Slow                                                $      '                           ./ 1     1
               Exponential model (., ) = ; >$ 6  &%      = !"[*@(.' * .? )]!" A B * CD
  Degradation                                                ?                            0 '      ?
                                                                                  
                    Power-law (P-V                     ;       $%        '     ?      ./ 1 1
  Catastrophic                             ( , ) =       6  (&)          = B C !" A B * CD
                    equation)                                           ?     '      0 '   ?




The Impact of Capacitor Structure on the Reliability of BME Capacitors




To be presented by David (Donhang) Liu at the Capacitors and Resistors Technology Symposium
(CARTS) conference, Santa Clara, California, April 1-3, 2014.                                                           3
Ni-BaTiO3 ceramic capacitors cannot be qualified for high reliability; they must be made for it. In other words, how
a MLCC was designed, constructed, and processed will have a significant impact on the reliability of the final capacitor
product. These parameters include the number of dielectric layers in a monolithic capacitor; the grain size, the
dielectric layer thickness, or the combination of two; the number of grains per dielectric layer; and the chip size of a
Ni-BaTiO3 MLCC.

1. The Impact of the Number of Dielectric Layers
As shown in Figure 2, a monolithic MLCC can be converted both constructively and electrically to a number of single-
layer ceramic capacitors connected in parallel. Assuming ;E is the i-th layer capacitor, the MLCC can be viewed as a
parallel connection among ;' , ;? , ;F ,… ;E ,…, and ;G , where N the number of dielectric layers inside a MLCC device.
Since every single-layer capacitor ;E shares the same electrode area S, the same dielectric thickness d, and the same
processing history, it is reasonable to assume that ;' = ;? = ;F = H = ;E … = ;G .

So the sum of the capacitance ; of a MLCC can be expressed as:

                         ; = ;' + ;? + ;F … + ;E … + ;G =  6 ;E .                                                   (7)
Similarly, the reliability of a MLCC with N dielectric layers that are connected in parallel can be expressed as:

                          = ' × ? × F … × E … × G = EG ,                                                      (8)
where E is the reliability of an i-th single-layer capacitor, and  is the overall reliability of a MLCC.




 Figure 2. A cross-sectional view of a monolithic MLCC shows a stack of N layers of single-layer capacitors (a);
this construction can be equivalently converted to the same number of single-layer capacitors connected in parallel.

The reliability relationship shown in Eq. (8) indicates that the overall reliability  of a MLCC device is highly
dependent on the reliability E of a single-layer capacitor inside a monolithic MLCC body.

From the structure of a MLCC unit shown in Figure 2, capacitor reliability can be expressed as:

                                                      () = E ()G                                                 (9)
where N is the number of individual dielectric layers and E () is the reliability of a dielectric layer. The capacitor
reliability  () as a function of E () and N is shown in Figure 3.

In general, when dielectric reliability E () is very close to unity, N does not have a significant impact on MLCC
reliability  (). If E () is reduced slightly, the overall reliability  () of a MLCC can degrade rapidly due to the
amplifying effect of the number of dielectric layers N. Since most commercial Ni-BaTiO3 capacitors are made with
a large number of dielectric layers (typically N >250), the impact of N on Ni-BaTiO3 capacitor reliability is critical.




To be presented by David (Donhang) Liu at the Capacitors and Resistors Technology Symposium
(CARTS) conference, Santa Clara, California, April 1-3, 2014.                                                              4
  Figure 3. MLCC reliability  () as a function of dielectric reliability E () and number of dielectric layers N.

2. The Impact of Number of Grains per Dielectric Layer
As shown in Figure 4, if a single-layer capacitor Ci has an average grain size  and an average dielectric thickness d,
                                                                      J
the number of grains per dielectric layer can be calculated as  .
                                                                      K




 Figure 4. Estimate of the number of grains in a dielectric layer. With average dielectric thickness d and average
                                                                                                  J
                   grain size  , the number of grains per dielectric layer can be calculated as  .
                                                                                                  K

                                                                           J
The MTTF of Ni-BaTiO3 MLCCs as a function of parameter   was measured and reported recently at high
                                                                           K
temperature (150°C) and high DC field (10kV/mm) by a Ni-BaTiO3 capacitor manufacturer [10]. The measured MTTF
                                                                 J
data were found to be proportional to the number of grains  . But if the voltage-per-grain-boundary is adjusted to
                                                                 K
                                                       J
the same value, all MLCCs under test with different   values give rise to almost identical MTTF values. According
                                                       K
to Eqs. (5) and (6), the MTTF of a Ni-BaTiO3 capacitor at a given temperature can be directly written as:

                                     '             '               '        J 
                             =            =              5 =           5 ×  .                                  (10)
                                  LM%N5 5     P%QQRNST        %QQRNST     K
                                             O    T     V
                                                 U
                                                  M


This indicates that the MTTF of Ni-BaTiO3 capacitors follow a power-law relationship for the dielectric thickness d
when applied voltage and average grain size are both given.
                                                            J
In order to implement the microstructure parameter   into the reliability of a single-layer capacitor, a structural
                                                            K
model based on the dielectric thickness and the feature size of a defect can be developed.




To be presented by David (Donhang) Liu at the Capacitors and Resistors Technology Symposium
(CARTS) conference, Santa Clara, California, April 1-3, 2014.                                                           5
As shown in Figure 5, assuming that the feature size of a defect that causes a catastrophic failure is r, d is the dielectric
thickness, and the reliability of the defect is 0, then the reliability of a single dielectric layer E () with thickness d
will be determined by the value of d with respect to r. When d is far greater than the defect feature size r, the defect
is non-harmful and may not cause any failures for many years, or even during a capacitor’s lifetime.




   Figure 5. An illustration of dielectric thickness d with respect to feature size r of an extrinsic defect inside the
                    dielectric layer. The dielectric layer reliability is dependent on the ratio r/d:

                                                     (a): d >> r; (b): .

However, as d approaches the feature size of the defect r, the defect will cause dielectric failure instantly. In other
words, the survival probability of the dielectric layer E can be written as E () W 1 when d >> r and as E () W
0 when . According to Eq. (10), the Weibull reliability of a dielectric layer with respect to its thickness d and
defect feature size r can thus be expressed as:

                                                               
                                                                         K Y
                                             E () =              6 A1 *   D.
                                                                            J

For simplicity, the defect size r can be directly related to the average grain size  as:  2 Z × , where Z is a constant.
The equation above can be further expressed with respect to average grain size  as:

                                              K Y                    K ^
                                \ = A1 *   D = #1 * J -, (_ ` 5)                                                    (11)
                                              J

where P is a geometric factor that determines the dielectric layer reliability E () with respect to the microstructure of
a MLCC. _ is an experimental constant that was determined by the formulation, processing conditions, and
microstructure of a BME capacitor. _ was experimentally determined in this study such that _ 2 6  and
_ 2 5 for V > 50 V.

The Weibull reliability of a Ni-BaTiO3 capacitor is equal to unity when  , so the reliability of a single dielectric
layer inside of a MLCC can be expressed as:

                                                h j
                                              -             kl n                kl n      kl n
                            R d (t < e) = e i         6 #1- m - = 1 6 #1- m - = #1- m -.

Combining Eqs. (9) and (11) yields the time-independent, simplified reliability of a BME MLCC:
                                                                                     G
                                                                                K ^
                                  ( < ) = E ( < )G = #1 * J - , (_ ` 5).                                       (12)

Eq. (12) shows that a reliability defect may function in two different ways when it exists in a single-layer capacitor.
Such a defect can be benign for the rest of the product life without causing a failure if the feature size of the reliability
defect is much less than that of the dielectric thickness. On the other hand, the defect may cause catastrophic failures
if the feature size approaches that of the dielectric thickness and if the level of external stress is extremely high.




To be presented by David (Donhang) Liu at the Capacitors and Resistors Technology Symposium
(CARTS) conference, Santa Clara, California, April 1-3, 2014.                                                              6
3. The Impact of Capacitor Chip Size A
In order to reveal the impact of chip size on the reliability of BME MLCCs, the effective areas of MLCC devices with
different chip sizes were measured and normalized with respect to the Electronic Industries Alliance (EIA) chip size
of 0402, the smallest chip size used in this comparison study. Corresponding measured results are summarized in
Table II. The chip size scaling factor S represents how many times larger the effective area of a given EIA chip size
is than that of 0402 for a single dielectric layer. For example, the effective chip size of a 0805 MLCC is equal to 6.76
times that of a 0402 MLCC connected in parallel.

Per Figure 2, Table II, and Eq. (9), the single dielectric layer reliability of a 0805 MLCC E (0805) can be expressed
with respect to that of a 0402 MLCC E (0402) as:

                                            E (0805) = E (0402)q.rq.

                  Table II. EIA Chip Size and Calculated Scaling Factors for BME Capacitors
                                                                            Effective area of a
 Chip                             Terminal-t      Side     End margin                                Chip size
         Length (Pm) Width (Pm)                                           single dielectric layer
 size                                (Pm)     margin (Pm)      (Pm)                               scaling factor s
                                                                                  (mm2)
 0402    1000 ± 100 500 ± 100 250 ± 150           125           100               0.225                 1.00
 0603    1600 ± 150 810 ± 150 350 ± 150           175           100               0.763                 3.39
 0805    2010 ± 200 1250 ± 200 500 ± 200          250           150               1.520                 6.76
 1206    3200 ± 200 1600 ± 200 500 ± 200          250           150               3.510                15.60
 1210    3200 ± 200 2500 ± 200 500 ± 200          250           150               5.940                26.40
 1812    4500 ± 300 3200 ± 200 610 ± 300          300           200               10.920               48.53
 2220    5700 ± 400 5000 ± 400 640 ± 390          320           220               23.074              102.55
 1825    4500 ± 300 6400 ± 400 610 ± 360          300           220               23.244              103.31

In general, when the chip size scaling factor S is used, the single dielectric layer reliability of a MLCC with an EIA
chip size of xy can be expressed with respect to the single dielectric layer reliability of a 0402 MLCC as:

                                E (!s) = E (0402)u .                                                              (13)
When the chip size scaling factor increases by a hundredfold, the single dielectric layer reliability declines: 45% when
E (0402)= 99%; 10% when E (0402)= 99.9%; and 1% when E (0402)= 99.99%. The single dielectric layer
reliability of MLCCs decreases with increasing chip size, but not significantly in comparison to the reliability decrease
that accompanies an increase in the number of dielectric layers. Results are shown in Figure 6.

Furthermore, according to Eq. (9), the reliability of a MLCC with chip size xy  (!s) can be expressed as:
                                                                                 yvw     u
                                 (!s) = [E (0402)Gvw ]u = x (0402)yz{z | ,                                    (14)

where  (!s) is the reliability of a BME MLCC with a chip size of xy and Nxy of dielectric layers, and  (0402) =
E (0402)Gz{z is that with a 0402 chip size and N0402 of dielectric layers. Construction analysis of Ni-BaTiO3
                                                                        Gvw
capacitors has revealed that N0402 –80 and Nxy –300, so that           –4.
                                                                        Gz{z




To be presented by David (Donhang) Liu at the Capacitors and Resistors Technology Symposium
(CARTS) conference, Santa Clara, California, April 1-3, 2014.                                                          7
Figure 6. The single dielectric layer reliability Ri (xy) as a function of EIA chip size, and the single layer reliability
                                             of a 0402 MLCC Ri (0402).

Conversely, the dielectric thickness of Ni-BaTiO3 capacitors is also found to gradually increase with MLCC chip size
A. Figure 7 shows construction analysis results of average Ni-BaTiO3 dielectric thickness as a function of chip size.
According to Eq. (10), the MTTF of a MLCC follows a power-law increase with increasing dielectric thickness.
Therefore, the reliability decreases due to increasing chip size have been greatly compensated for by increasing the
dielectric thickness.

As a result of that, the overall reliability of a Ni-BaTiO3 MLCC will not change significantly with increasing capacitor
chip size.




              Figure 7. Measured average dielectric thickness as function of BME MLCC chip size A.




To be presented by David (Donhang) Liu at the Capacitors and Resistors Technology Symposium
(CARTS) conference, Santa Clara, California, April 1-3, 2014.                                                            8
Application Examples

The general expression of a BME capacitor’s reliability as given in Eq. (2) can be specifically rewritten for Ni-BaTiO3
capacitors based on this study. A two-parameter Weibull distribution is applicable to (). Two identified failure
modes will follow different acceleration functions      ( , ), as summarized in Table I. Function (, , , ) can be
expressed using Eq. (12). The impact of chip size S on the reliability of BME capacitors is negligible. Therefore, the
reliability of a Ni-BaTiO3 capacitor is finally obtained:

                   () = (, ,  , ) ×        ( , ) × ()


                                                                j
                                                                                                   j
                                                           h                            h
                                                   -                         -               
                                        }
                                   kl n                                                 
                                                         6                                  B  C
                         = #1- m - × { p × e        
                                                                     + (1-p) × e  - 6     
                                                                                                        },          (15)

where E1 and E2 are the Weibull slope parameters for catastrophic and slow degradation failures, respectively; Ea1 and
Ea2 are the activation energies for the two failure modes, respectively; p is the percentage of catastrophic failures; a,
b, C are constants; _ is a constant that can be determined experimentally; and N, d, and  are the number of dielectric
layers, average dielectric thickness, and average grain size, respectively.

1. Reliability Model at t=0
From Eq. (15), when t=0, the general reliability model is simplified to a constant that is only dependent on the
structural and construction parameters of a MLCC device.
                                                                         G
                                                                    K ^
                                               (0) = #1 * J - .

Table III summarizes the calculated R(0) data for a number of commercial Ni-BaTiO3 MLCCs based on the
construction analysis results. It has been found that when Eq. (16) is satisfied, most Ni-BaTiO3 MLCCs pass 1000-
hour life testing at 125°C and twice the rated voltage specified in MIL-PRF-55681.

              Table III. Calculated Reliability Data per Eq. (16) and Corresponding Life Test Results
                                          Dielectric  No. of Dielectric                 1000-hours Life Test
        CAP ID       Grain Size (Pm)                                    Calculated R(0)
                                        Thickness(Pm)    Layers N                         at 125°C, 2 x Vr
      A08X22525            0.305             3.89           211             0.99995             Fail
      B08X33425            0.420             5.80            74             0.99999             Pass
      A08X15425            0.460             9.80            43             1.00000             Pass
      C06X10525            0.440             3.20           150             0.99899             Fail
      A06X10425            0.470             7.89            62             1.00000             Pass
      A12X47425            0.492            10.40            58             1.00000             Pass
      C04X47325            0.386             4.40            60             0.99997             Fail
      B12X47525            0.376             4.34           260             0.99989             Fail
      P08X10425            0.790            20.20            23             1.00000             Pass
      B06X10516            0.273             2.29           179             0.99948             Fail
      A08X47416            0.319             3.75           208             0.99992             Fail
      B12X68416            0.375             6.21            64             1.00000             Pass
      C08X22516            0.224             3.81           212             0.99999             Pass
      B08X22516            0.340             3.23           230             0.99969             Fail
      B08X56416            0.373             4.21            80             0.99996             Pass
      C08X47516            0.230             2.49           260             0.99984             Pass




To be presented by David (Donhang) Liu at the Capacitors and Resistors Technology Symposium
(CARTS) conference, Santa Clara, California, April 1-3, 2014.                                                          9
      B12X10516             0.475              7.82              99                1.00000                 Pass
      B04X10416             0.342              3.05               67               0.99987                 Fail
      B12X10606             0.365              3.11              348               0.99908                 Fail
      B04X10406             0.323              2.50               70               0.99967                 Fail
      B08X22506             0.419              3.42              230               0.99922                 Fail
      A08X10406             0.490             12.50              34                1.00000                 Pass
      B06X22406             0.373              4.01               67               0.99996                 Pass
      P06X10405             0.770             12.60              24                1.00000                 Pass
  *: Capacitor ID: C (manufacturer ID); 08 (EIA chip size, 08=0805); X (dielectric type, X=X7R); 475 (cap
     values, 475=4,700,000 pF); 16 (rated voltage). For example: A08X10406 = 100,000pF, 6V, 0805, from
     manufacturer A.
In addition, all of the commercially available automotive-grade Ni-BaTiO3 MLCCs (that meet the requirements of
AEC-Q200) that have been processed for construction and microstructure investigations have been found to meet the
conditions of Eq. (16).
                                                        G
                                                   K ^
                                 (0) = #1 * J - = 1.00000.                                                           (16)

One may wonder why there must be 5 zeroes in Eq. (16). As discussed previously, BX% is a better term over MTTF
to describe the reliability life of Ni-BaTiO3 MLCCs [3]. When predicting reliability life, it is important to know the
rate at which a population will fail. To better predict the reliability life of Ni-BaTiO3 capacitors, it is preferable that
BX% life be used.
BX% refers to the time by which X% of the units in a population will have failed. BX% life of a 2-parameter Weibull
can be calculated using Eq. (17). The BX% life is not only related to the model parameters but is also directly related
to the reliability () that is a function of time.

                                            = {*[( )]}'/                                                      (17)
where ( ) = 1-X%, which corresponds to the probability that 1-X% units in the population have not failed at  .

According to MIL-PRF-55681, the reliability level of a MLCC is defined by 1000 hours at a given failure rate level.
Table IV summarizes the reliability levels per MIL-PRF-55681 and the corresponding calculated BX% life at different
failure rates. It is clear that the number of zeroes in Eq. (16) corresponds to the reliability life of a level S, or a 1000-
hour lifetime with a failure rate of 100 ppm (parts per million).


             Table IV. Product Level in MIL-PRF-55681 and Corresponding Calculated BX% Life
                                     with Respect to the Failure Rate for MLCCs
       Product level per MIL-PRF-55681                       BX% life and reliability level per Eq. (17)
                      Failure rate level (%)
      Symbol                                      BX% life (hours) to failure rate       BX% life to reliability
                    (percent per 1000 hours)
        M                       1.0                        BX1.0%=1000                       R(1.0%)=0.99
        P                       0.1                        BX0.1%=1000                      R(0.1%)=0.999
        R                      0.01                       BX0.01%=1000                     R(0.01%)=0.9999
        S                     0.001                      BX0.001% =1000                   R(0.001%)=0.99999

Although a significant amount of Ni-BaTiO3 MLCCs that meet Eq. (16) have passed the life test at 125°C and twice
the rated voltage for 1000 hours, Eq. (16) is not sufficient to be used to predict the reliability life of Ni-BaTiO3 MLCCs.
Indeed, for users of Ni-BaTiO3 MLCCs, Eq. (16) can be used as a selection criterion for Ni-BaTiO3 MLCCs that can
be considered for high-reliability applications because most of the Ni-BaTiO3 MLCCs that meet Eq. (16) can pass the
life test per MIL-PRF-55681. Those that do not meet this requirement can be rejected prior to tedious life testing,
thus saving time and effort.




To be presented by David (Donhang) Liu at the Capacitors and Resistors Technology Symposium
(CARTS) conference, Santa Clara, California, April 1-3, 2014.                                                             10
For manufacturers, Eq. (16) can be used as a simple rule of thumb when designing Ni-BaTiO3 MLCCs for high-
reliability applications. However, it should be pointed out that since some dopants used in formulating Ni-BaTiO3
MLCCs, such as Ca and Mg, may function as grain growth prohibiters, tone must be very careful when using Eq. (16)
to compare Ni-BaTiO3 MLCCs. It is recommended that only Ni-BaTiO3 MLCCs with similar formulations and
processing conditions should be compared using Eq. (16). It is also worth mentioning that per Eq. (16), at a given
dielectric thickness and number of dielectric layers, the smaller grain size would give rise to a better reliability.

2. Reliability Model at t>0
When t > 0, Eq. (15) suggests two different failure modes in Ni-BaTiO3 MLCCs that follow different acceleration
functions with external applied stress. Figure 8 shows a number of TTF data sets obtained for a Ni-BaTiO3 MLCC of
C08X47516 at various stress conditions during highly accelerated life stress testing (HALST), in which a data set
obtained at 135°C and 72V is used for model verification purposes only. This data set will not be used in statistical
modeling to determine the acceleration factors; it will only be used to compare the calculated MTTF results from
Weibull modeling.

All TTF data sets appear to fit to single Weibull plots, indicating a single failure mode. When the Prokopowicz and
Vaskas equation (Eq. (5)) is used to process the Weibull modeling data shown in Figure 8, the acceleration factors Ea
and n can be determined. The Weibull reliability life as characterized by MTTF can then be calculated for various
stress conditions.

                                                                                 Weibull Plot of C08X47516
                                                              99.0

                                                                        165C
                                                                                             155C            165C
                                                              90.0
                                                                        80V     165C         72V             48V
                                                                                72V




                          Cumulative Failure Percentile (%)
                                                              50.0                 165C
                                                                                   64V                              135C
                                                                                                                    72V
                                                                                                                    For Verification




                                                              10.0



                                                               5.0




                                                               1.0
                                                                100.0          1000.0                     10000.0                100000.0
                                                                                   Stress Time(minutes)




 Figure 8. Weibull plots of a number of TTF data under various stress conditions. The MTTF, E, and Kvalues are
also included for information. The TTF data that were obtained at 135°C, 72V are for verification of the model only
                                  and were not used for the reliability modeling.

Table V summarizes the calculated MTTF and compares it to experimentally determined MTTF data at 135°C, 72V.
It is clear that the calculated lifetime of 2111.17 hours is much longer than the 318.28 hours actually measured. Indeed,
the inconsistency between calculated MTTF using a single Weibull model and Eq. (5) and that of actual measured
MTTF has been observed for quite a while for many Ni-BaTiO3 MLCCs. Calculated lifetimes often have been found
to be longer than measured ones [1].




To be presented by David (Donhang) Liu at the Capacitors and Resistors Technology Symposium
(CARTS) conference, Santa Clara, California, April 1-3, 2014.                                                                               11
                    Table V. Calculated Statistical Parameters and Acceleration Factors for a Ni-BaTiO3 Capacitor C08X47516
                                                  Acceleration Factors from P-V Equation and MTTF Calculated for 135°C, 72V
                     Weibull Model Parameters      E          K         Ea (eV)        n       MTTF (min)     MTTF (Hours)
          Calculated Data                                                          2.755      3.587E+07         2.60   4.524   126670.20   2111.17
  Verification Data at 135°C, 72V                                                  3.822        21124           N/A     N/A    19097.00    318.28

As has been suggested before [3, 8-9], this inconsistency is likely due to the existence of mixed failure modes. Since
the traditional highly accelerated life test is a method that is based on a single failure mode, it is necessary to introduce
another independent test parameter, in addition to TTF, to reveal the complexity of failure modes in Ni-BaTiO3
MLCCs. In this study, leakage current as a function of applied stress time was measured together with TTF data.
Figure 9 shows corresponding leakage current data at a stress condition of 165°C and 72V, together with the TTF data
shown in Figure 8. It is clear that the measured leakage current data reveal two distinct failure modes: (a) a
catastrophic failure, characterized by a gradual leakage increase followed by a time-accelerating increase in leakage,
and (b) a slow degradation, characterized by a near-linear leakage increase until the failure criterion is reached.

Figure 10 shows a re-plot of the Weibull probability plots of the TTF data shown in Figure 9 with respect to the failure
modes. Arrows are used to indicate the data points that failed catastrophically. Corresponding failure modes
for each TTF data points in the plot are listed in the chart on the right-hand side of Figure 10.

Weibull modeling of the data shown in Figure 10 was performed as follows: When all of the catastrophic data points
were processed as failures, the others in the group were treated as suspensions. The process was switched, with all
slow degradation failures processed as failures and all catastrophic ones treated as suspensions. As a result, the
original mixed TTF data set could be separated into “catastrophic” and “slow degradation” subsets that were modeled
separately. Figure 11(a) shows the Weibull plots from two subsets as distinguished in Figure 10.

                                                 Weibull ProbabilityPlot of C08X47516 at 165C72V
                                       99.0



                                       90.0




   Cumulative Failure Percentile (%)
                                       50.0




                                       10.0



                                        5.0




                                        1.0
                                         100.0                            1000.0                      10000.0
                                                                Stress Time (Minutes)


                                                                    (a)                                                              (b)
Figure 9. The Weibull plot of TTF data and corresponding leakage current measurement results are shown together.
 The leakage current data are characterized by mixed failure modes that are not revealed in the corresponding TTF
                                                  measurement.




To be presented by David (Donhang) Liu at the Capacitors and Resistors Technology Symposium
(CARTS) conference, Santa Clara, California, April 1-3, 2014.                                                                                        12
                                                                                                            TTF (minutes) Failure Mode symbol
                                                Weibull ProbabilityPlot of C08X47516 at 165C72V
                                      99.0                                                                      377.26      Catastrophic    C
                                                                                                                614.70      Catastrophic    C
                                      90.0                                                                      712.00      Catastrophic    C
                                                                                                                723.40      Catastrophic    C
                                                                                                                749.30      Catastrophic    C




  Cumulative Failure Percentile (%)
                                                                                                                766.34      Catastrophic    C
                                      50.0
                                                                                                                793.25   Slow Degradation   S
                                                                                                                805.29      Catastrophic    C
                                                                                                                866.30      Catastrophic    C
                                                                                                                908.27      Catastrophic    C
                                                                                                                953.18      Catastrophic    C
                                      10.0
                                                                                                               1112.39   Slow Degradation   S
                                                                                                               1124.51   Slow Degradation   S
                                       5.0
                                                                                                               1163.47   Slow Degradation   S
                                                                                                               1203.19   Slow Degradation   S
                                                                                                               1235.54      Catastrophic    C
                                                                                                               1302.47   Slow Degradation   S
                                                                                                               1425.38   Slow Degradation   S
                                       1.0
                                        100.0                           1000.0                    10000.0      1515.23   Slow Degradation   S
                                                               Stress Time (Minutes)
                                                                                                               1583.30   Slow Degradation   S



     Figure 10. A re-plot of Weibull modeling as shown in Figure 9, with arrows indicating the catastrophic failures
           when the leakage current data were applied to distinguish between the two different failure modes.

Corresponding contour plots of the two subsets are shown in Figure 11(b). A contour plot gives rise to a visual picture
of confidence bounds on E and  for a 2-parameter Weibull distribution at a certain confidence level (typically 95%).
The plot defines the boundary of a data set with respect to the possible values of E and , and it is often applied to
compare different data sets for different failure modes and to determine whether two sets have statistically different
failure modes.

It is important to note that in the contour plots shown in Figure 11(b), the two data sets do not show any overlap with
respect to the E values (Y-axis). This is a clear indication that the two data sets statistically represent two different
failure modes, as characterized by two different E values.

What makes this example even more interesting is the fact that the TTF data shown in Figure 9(a) would appear to fit
a single Weibull model well (a linear-like curve) if the leakage current data shown in Figure 9(b) were not used.
However, when the leakage current data are used to distinguish the failure modes, the TTF data that seem to fit a
single failure mode can clearly be separated into two subsets with two different E values, indicating that the two
subsets have different failure modes.




To be presented by David (Donhang) Liu at the Capacitors and Resistors Technology Symposium
(CARTS) conference, Santa Clara, California, April 1-3, 2014.                                                                                   13
                                                        C08X47516at 165°C, 72V
                             99.00
                                                                                                                                        Contour Plot of C08X47516 at 165Cand72V
                                                                                                                          12.0


                             90.00




     Normalized Failure Percentile (%)
                                                                                                                               9.6

                                                     Catastrophic




                                                                                                        Slope Parameter Beta
                             50.00



                                                                                                                               7.2
                                                                                                                                                              SlowDegradation

                                                                           SlowDegradation
                             10.00                                                                                             4.8



                                         5.00

                                                                                                                               2.4
                                                                                                                                                    Catastrophic



                                         1.00                                                                                  0.0
                                            100.00               1000.00                     10000.00                           800.0   1120.0       1440.0         1760.0        2080.0   2400.0
                                                      Stress Time (minutes)                                                                         Scale Parameter Eta


                                                       (a)                                                                                                         (b)
 Figure 11. Weibull modeling plots using the TTF data and failure modes information revealed in Table II from the
    corresponding leakage current measurement (a). Contour plot reveals the two slope parameters E for the two
                different failure modes, but the two subgroups share a similar scale parameter  (b).
To repeat the process shown in Figures 9 and 10 for all data sets shown in Figure 8, the data sets can be split into two
separate subsets with two different failure modes. The normalized Weibull probability plots at 125°C and 32V (twice
the rated voltage) are shown in Figure 12(b) for three different failure scenarios, in which each data point is
extrapolated from Figure 12(a) using a most likelihood estimation (MLE) method and a power-law acceleration
function for catastrophic failures and an exponential-law acceleration function for slow degradation failures (Table I).
This is done for each failure and for any suspensions that are entered, and then the median ranks of the failures are
determined. Additional details on this approach for characterizing HALST results have been described previously [8,
9].

A total of three normalized Weibull plots were generated to represent the two distinct failure modes that were revealed
in leakage current measurements, as well as a mixture of both. The plot labeled “complete set” is the normalized
Weibull plot that all TTF data points shown in Figure 12(a) were used for modeling, except the data set of 135°C, 72V.
This plot also represents a conventional Weibull plot when all of the units are assumed to fail with only a single failure
mode. The “catastrophic” plot is created using all of the data points that failed with a catastrophic characteristic and
with all remaining data points (that failed with slow degradation) set as suspensions. The “slow degradation” plot is
one in which only slow degradation failed samples were used for Weibull modeling and those that failed
catastrophically remain suspensions.

It is noticeable that the three Weibull modeling plots give rise to different scale parameters , indicating that each
model predicts a different reliability life. The calculated MTTF for the catastrophic failure mode with power-law
acceleration function (Eq. (5)) at 135°C, 72V is 318.7 hours, which is almost identical to the MTTF value of 318.3
hours estimated from the data set of 135°C, 72V shown in Figure 12(a). In addition, the leakage current measurement
also showed that all data points for 135°C, 72V revealed a catastrophic failure mode [3].




To be presented by David (Donhang) Liu at the Capacitors and Resistors Technology Symposium
(CARTS) conference, Santa Clara, California, April 1-3, 2014.                                                                                                                                       14
                                                               Weibull Plot of C08X47516                                                                                  NormalizedWeibull Plot of C08X47516at 125C, 32V
                                            99.0                                                                                                              99.9

                                                      165C
                                                                           155C            165C                                                               90.0            Catastrophic
                                            90.0
                                                      80V     165C         72V             48V
                                                              72V                                                                                             50.0
                                                                                                                                                                                                                 SlowDegradation




        Cumulative Failure Percentile (%)                                                                                 Cumulative Failure Percentile(%)
                                            50.0                 165C                                                                                         10.0
                                                                 64V                              135C
                                                                                                                                                                5.0
                                                                                                  72V
                                                                                                  For Verification

                                                                                                                                                                1.0
                                                                                                                                                                0.5
                                                                                                                                                                                                            Complete Set
                                            10.0
                                                                                                                                                                0.1
                                                                                                                                                             5.0E-2
                                             5.0


                                                                                                                                                             1.0E-2
                                                                                                                                                             5.0E-3



                                             1.0                                                                                                             1.0E-3
                                              100.0          1000.0                     10000.0                100000.0                                               1    100           10000         1000000         1.E+8       1.E+10
                                                                 Stress Time(minutes)                                                                                                   Stress Time (minutes)



                                                             (a)                                                                                                                                      (b)
    Figure 12. Weibull plots for BME capacitor C08X47516 under various stress conditions (a); corresponding
             normalized probability plots at 125°C and 32V, with a power-law acceleration factor (b).
Summary

A general reliability model for Ni-BaTiO3 MLCCs has been proposed and verified. The model consists of three parts:
(1) a 2-parameter Weibull distribution; (2) two acceleration functions that describe two statistically distinct failure
modes: a power-law form for catastrophic failures, and an exponential-law form for slow degradation failures; (3) an
empirical function that defines contribution of the structural and constructional characteristics of a multilayer capacitor
device, such as the number of dielectric layers N, dielectric thickness d, and average grain size . The capacitor chip
size A is found not to play a role in the reliability of a Ni-BaTiO3 MLCC.

Two examples are discussed for the application of this reliability model. At t=0, the reliability model can be used as
a selection criterion for Ni-BaTiO3 MLCCs that may be applicable to high-reliability applications. When t>0, the
proposed reliability model defines two distinct failure modes in Ni-BaTiO3 MLCCs. The calculated reliability life
using the proposed model gives rise to a good agreement with measured MTTF results.

Acknowledgements

The author appreciates the NASA Electronic Parts and Packaging (NEPP) program’s support for this study The author
also expresses his gratitude to Michael Sampson and Bruce Meinhold for reviewing the manuscript. The author would
also like to thank the GSFC Code 562 Parts Analysis Laboratory for assistance with electrical testing.
References

[1] H. Kishi, Y. Mizono, H. Chazuno, H. Chazono , Jpn. J. Appl. Phys. Vol. 42, p. 1, 2003
[2] C. Hendricks, Y. Min, T. Lane, and V. Magadala, CARTS Proceedings, New Orleans, LA,p. 3, 2010
[3] D. Liu, CARTS Proceedings, Houston, TX, p. 235, March 2013
[4] T. I. Prokopowicz and A. R. Vaskas, Final Report ECOM-90705-F, NTIS AD-864068, October 1969
[5] B. Rawal and N. Chan, Proceedings of Electronic Components Conference, New Orleans, p. 184, 1984
[6] J. L. Paulsen and E. K. Reed, Microelectronics Reliability, Vol. 42, p. 815, 2002
[7] M. Randall, A. Gurav, D. Skamser, and J. Beeson, CARTS Proceedings, p. 134, 2003
[8] D. Liu and M. Sampson, CARTS Proceedings, Jacksonville, FL, p. 45, 2011
[9] D. Liu and M. Sampson, CARTS Proceedings, Las Vegas, NV, p. 59, 2012
[10] T. Nakamura, T. Yao, J. Ikeda, N. Kubodera, H. Takagi, IOP Conf. Series: Materials Science and Engineering
     Vol. 18, p. 1, 2011




To be presented by David (Donhang) Liu at the Capacitors and Resistors Technology Symposium
(CARTS) conference, Santa Clara, California, April 1-3, 2014.                                                                                                                                                                               15
