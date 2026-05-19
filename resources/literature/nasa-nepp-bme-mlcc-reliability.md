                              April/May 2013 • Volume 5 • Issue 2 (Published since 2009)


                                                  Special Issue
    Reliability of Multilayer Ceramic Capacitors with Base-Metal Electrodes

Base metal electrode (BME) multilayer ceramic capacitors have drawn a great deal of recent attention. This special issue
of the EEE Parts Bulletin was written by David (Donhang) Liu, a capacitor specialist of NASA Goddard Spaceflight Center.

1. Capacitor Reliability and System Reliability
Multilayer ceramic capacitors (MLCCs) are key building blocks in modern electronics. MLCCs comprise ~30% of the total
components in a typical hybrid circuit module such as a DC-DC converter. The numbers of ceramic capacitors used in
integrated circuit (IC) power supply decoupling applications are even greater. Figure 1 shows an example of today’s
large-scale IC chip package with many decoupling base-metal electrode (BME) MLCCs around it. Due to the demand for
increasing numbers of decoupling capacitors and the limited space available, the use of BME capacitors with higher ca-
pacitance and a smaller chip size is more attractive for current large-scale IC chip packages.




Figure 1. MLCC application in a large-scale integrated circuit showing MLCCs around the periphery of a large-
scale integration (LSI) package.

                                                           1
Indeed, a typical Intel central processing unit (CPU) package today requires more than 100 ceramic capacitors performing
a variety of functions related to power delivery and signal integrity. These capacitors all need to work reliably for the CPU
to function. Due to cost pressures, the degree of redundancy in CPU systems has been reduced, and so the failure of
even one capacitor can cause the whole system to fail.
Capacitor reliability is vital for all electronic systems, which may help to explain why the NASA Electronic Parts and Pack-
aging (NEPP) program has continuously funded studies on the reliability issues of various capacitor technologies.
In its simplest form, the capacitor system reliability can be expressed as:
                           Capacitor system reliability = component reliability Number of capacitors


If a CPU system with 100 capacitors needs to maintain a system reliability of 99.9%; each capacitor must have an individ-
ual component reliability of 99.999%.


2. Characteristics of Multilayer Ceramic Capacitors
An MLCC is a high-temperature (1350°C typical) co-fired ceramic monolithic that is composed of many layers of alternate-
ly stacked oxide-based dielectrics and internal metal electrodes. The internal electrodes are connected in parallel to form
end terminations for the electrical contacts (Figure 2).
The capacitance 𝐶𝑡 of an MLCC can be represented by:
                                                                     S
                                                 C = εr ∙ ε0 ∙ N ∙ ,                                                          (1)
                                                                     d


where S is the overlap area of internal electrodes, N is the number of individual dielectric layers, εr is the relative dielectric
constant of the ceramic dielectric, d is the thickness of the dielectric layer, and ε0 is the dielectric constant of free space.
Another important parameter for measuring the degree of miniaturization of a capacitor is volumetric efficiency, which is
the capacitance per volume and which can be expressed as:
                                                𝐶𝑡      𝜀                     𝜀     µ𝐹
                                                   ≈ 𝜀0 𝑑𝑟2   ≈ 8.854 × 10−8 𝑑𝑟2 �     �                                      (2)
                                                𝑉                                  𝑐𝑚3




                                        Figure 2. Typical structure of an MLCC device.

where 𝜀𝑟 is the dielectric constant and d is the dielectric thickness. MLCCs with high volumetric efficiency can be
achieved by increasing the dielectric constant and reducing the dielectric thickness.


3. Precious-Metal Electrodes vs. Base-Metal Electrodes
During the manufacturing of MLCC products, in order to make the dielectric layers insulating and the metal electrode lay-
ers conducting, only highly oxidation-resistant precious metals such as platinum, palladium, and silver can be used for the
co-firing in a regular air atmosphere. MLCCs made with precious metals as internal electrodes and terminations are
called PME capacitors. To date, MIL-PRF-123 requires all MLCCs for high-reliability and space projects to be PME ca-
pacitors.
                                                                 2
In the early 1990s, the high cost of precious metal materials, coupled with uncertainty about their continued availability,
forced an industry shift from PME to BME (Ni, Cu) technology for most commercial MLCCs. The switch from PMEs to
BMEs required a change in the manner in which the ceramic is fired from a regular-air atmosphere to a reducing atmos-
phere (low oxygen) to prevent the oxidation of internal nickel electrodes. This creates a significant amount of oxygen va-
cancies in the dielectric that will migrate under DC bias and degrade the dielectric’s insulating resistance. After more than
two decades of development, the insulating resistance degradation in BME MLCCs has been significantly reduced by two
primary approaches: (1) a subsequent low-temperature firing in an oxygen-rich environment to re-oxidize the dielectric by
occupying the oxygen vacancies, and (2) rare-earth element doping to pin or slow down the migration of still-existing oxy-
gen vacancies.
Although issues and concerns remain with respect to the lifetime reliability of MLCCs manufactured using BME technolo-
gy, substantial progress has been made. Due to its improved voltage robustness and its capability for making more layers
of internal electrodes, some of BME capacitors can achieve lifetime reliability equal to or better than that of space-level
PME capacitors, with higher capacitance per volume (volumetric efficiency) and much lower cost. This is another ad-
vantage to using BME capacitors for high-reliability, space-level applications.
An investigation into the possible use of BME capacitors for high-reliability NASA space-level applications has become
urgent and inevitable.


4. Reliability of BME Capacitors
The evaluation of BME capacitors for potential NASA space project applications requires an in-depth understanding of the
reliability of BME capacitors. BME capacitors cannot be qualified for high reliability; they must be made for it.

4.1 Reliability of MLCCs
The reliability of an MLCC is the ability of the dielectric material to retain its insulating properties under stated environmen-
tal and operational conditions for a specified period of time t. A general expression of reliability consists of three parts and
can be expressed as:
                                                𝑅(𝑡) = 𝜑(𝑁, 𝑑, 𝑟̅ , 𝑆) × 𝐴𝐹(𝑉, 𝑇) × 𝛾(𝑡)                                     (3)
Where 𝛾(𝑡) is a statistical distribution that describes the individual variation of properties in a testing group of samples
(Weibull, log normal, normal, etc.).
𝐴𝐹(𝑉, 𝑇) is an acceleration function that describes how a capacitor’s reliability responds to external stresses such as ap-
plied voltage V and temperature T. All units in the testing group should follow the same acceleration function if they share
the same failure mode (independent of individual units).
𝜑(𝑁, 𝑑, 𝑟̅ , 𝑆) describes the effect on reliability of the structural and constructional characteristics of a capacitor device,
such as the number of dielectric layers N, the dielectric thickness d, average grain size 𝑟̅ , and capacitor chip size S.
In general, a two-parameter Weibull statistical distribution model is often used in the description of a BME capacitor’s reli-
ability as a function of time:
                                                             𝑡
                                                           −( )𝛽
                                                𝛾(𝑡) = 𝑒     𝜂                                                               (4)
where e is the base for natural logarithms, β is the dimensionless slope parameter whose value is often characteristic of
the particular failure mode under study, and η is the scale parameter that represents a characteristic time at which 63.2%
of the population has failed and that is related to all other characteristic times, such as mean time to failure (MTTF):
                                              𝑀𝑇𝑇𝐹 = 𝜂𝛤(1 + 1⁄ 𝛽),                                                           (5)
where Γ(x) is the gamma function of x (Note: Γ (1+1/ β) ≈ 0.9 when β >3.0).
Equation (4) provides a simple and clear understanding of the meaning of reliability:
Reliability is a monotonic function of time and always decreases with time, which indicates that the loss of reliability is a
common behavior for all devices.
Since η and β always exceed zero, the value of R(t) is always between 0 and 1, indicating that reliability can also be
viewed as the probability of a failure to occur.




                                                                   3
Reliability typically defines the durability of a system that can function normally. When β > 3 and t < η, R(t) ~1, suggest-
ing a reliable life span before η. When t > η, R(t) decreases rapidly to 0. The lifetime of a device to sustain its function
can be characterized by η, as shown in Eq. (5).

4.2 Acceleration Functions of BME Capacitors
𝐴𝐹(𝑉, 𝑇)in Eq. (3) represents the impacts of external stresses (applied voltage and temperature are commonly used) on
the reliability of a BME capacitor. It is widely known that the time-to-failure (TTF) for MLCCs that is caused by a single
failure mode when both V and T are changed from V1 to V2 and T1 to T2 is the product of the separate acceleration fac-
tors:
                                               𝑡      𝑉 𝑛         𝐸     1    1
                                       𝐴𝑉𝑇 = 1 = � 2 � 𝑒𝑥𝑝 � 𝑎 � − ��                                                        (6)
                                               𝑡2     𝑉1          𝑘     𝑇1   𝑇2

where n is an empirical parameter that represents the voltage acceleration factors, 𝐸𝑎 is an activation energy that repre-
sents the temperature acceleration factor, and 𝑘 is the Boltzmann constant.
This well-known Prokopowicz and Vaskas equation (P-V equation) has proven to be useful in the capacitor industry for
testing PME MLCCs at various highly accelerated testing conditions. An average of n≈3 has been found for the voltage
acceleration factor, and an average value of 1 < 𝐸𝑎 < 2 eV is typical for the temperature acceleration factor.
Since only a single failure mode is assumed, the value of β in Eq. (4) should not change over applied stresses. Only the
Weibull distribution scale parameter η will change with external stresses. This can be expressed, according to Eq. (6), as
                                                                     𝐵
                                                             𝐶
                                                𝜂(𝑉, 𝑇) =     𝑛 ∙ 𝑒 (𝑇) ,                                                    (7)
                                                            𝑉

where C and B = 𝐸𝑎 /𝑘 are constants.
Due to the relatively high concentration of oxygen vacancies in BME capacitors and to the impact of oxygen vacancy
electromigration on the reliability of BME capacitors, the acceleration function 𝐴𝐹(𝑉, 𝑇) of BME capacitors has been
found to not always follow the power law with respect to applied voltage as specified in Eq. (6). Mixed failures have often
been reported for BME capacitors.
A recent NASA NEPP-funded study that combines the measurement of both TTF and the capacitor leakage current as a
function of stress has been developed and practiced to describe the reliability of BME capacitors. A two-stage dielectric
wear-out process that initiates with a slow dielectric degradation, followed by a thermally dominated catastrophic break-
down, has been revealed (Figure 3). When the failure criterion is set with respect to a leakage current level, some BME
capacitors will reach the failure level with a catastrophic failure, and some will fail prior to the occurrence of a catastrophic
dielectric breakdown.




Figure 3. A two-stage dielectric wear-out failure mode is proposed to describe the dielectric breakdown behaviors
in BME capacitors.

Further investigation also revealed that the two identified failure modes follow different acceleration functions. Slow deg-
radation fits well to an exponential law against the applied field. The catastrophic failures fit the power-law better. Table I
summarizes the two failure modes and corresponding voltage acceleration functions that may be used to model the BME
capacitors’ reliability life.




                                                                 4
Table I. Summary of Acceleration Functions for BME MLCCs

                               Acceleration             Expression to scale
      Failure mode                                                                     Expression to time-to-failure (TTF)
                                 function                  parameter 𝜼
                                                                              𝐸𝑎    𝑡1                         𝐸𝑎 1 1
     Slow Degradation       Exponential model      𝜂(𝐸, 𝑇) = 𝐶𝑒 −𝑏𝐸 ∙ 𝑒 �𝑘𝑇�           = 𝑒𝑥𝑝[−𝑏(𝐸1 − 𝐸2 )]𝑒𝑥𝑝 � � − ��
                                                                                    𝑡2                         𝑘 𝑇1 𝑇2

                           Power-law (P-V equa-                𝐶        𝐸𝑎          𝑡1    𝑉2 𝑛    𝐸𝑎 1 1
       Catastrophic                                𝜂(𝑉, 𝑇) =       ∙ 𝑒 (𝑘𝑇)            = � � 𝑒𝑥𝑝 � � − ��
                                   tion)                       𝑉 𝑛
                                                                                    𝑡2    𝑉1      𝑘 𝑇1 𝑇2



4.3 The Impact of Capacitor Structure on the Reliability of BME Capacitors

4.3.1 The Impact of the Number of Dielectric Layers
As shown in Figure 4, a monolithic MLCC can be converted both constructively and electrically to a number of single-layer
ceramic capacitors connected in parallel. Assuming 𝐶𝑖 is the i-th layer capacitor, the MLCC can be viewed as a parallel
connection among 𝐶1 , 𝐶2 , 𝐶3 ,… 𝐶𝑖 ,…, and 𝐶𝑁 , where N the number of dielectric layers inside an MLCC device. Since
every single-layer capacitor 𝐶𝑖 shares the same electrode area S, the same dielectric thickness d, and the same pro-
cessing history, it is reasonable to assume that 𝐶1 = 𝐶2 = 𝐶3 = ⋯ = 𝐶𝑖 … = 𝐶𝑁 .
So the sum of the capacitance 𝐶𝑡 of an MLCC can be expressed as:
                                𝐶𝑡 = 𝐶1 + 𝐶2 + 𝐶3 … + 𝐶𝑖 … + 𝐶𝑁 = 𝑁 ∙ 𝐶𝑖 .                                                    (8)
Similarly, the reliability of an MLCC with N dielectric layers that are connected in parallel can be expressed as:
                                𝑅𝑡 = 𝑅1 × 𝑅2 × 𝑅3 … × 𝑅𝑖 … × 𝑅𝑁 = 𝑅𝑖𝑁 ,                                                       (9)
where 𝑅𝑖 is the reliability of an i-th single-layer capacitor, and 𝑅𝑡 is the overall reliability of an MLCC.




Figure 4. A cross-sectional view of a monolithic MLCC shows a stack of N layers of single-layer capacitors (a); this construc-
tion can be equivalently converted to the same number of single-layer capacitors connected in parallel.

The reliability relationship shown in Eq. (9) indicates that the overall reliability 𝑅𝑡 of an MLCC device is highly dependent
on the reliability 𝑅𝑖 of a single-layer capacitor inside a monolithic MLCC body.
From the structure of an MLCC unit shown in Figure 4, capacitor reliability can be expressed as:
                                                𝑅𝑡 (𝑡) = 𝑅𝑖 (𝑡)𝑁                                                             (10)
where N is the number of individual dielectric layers and 𝑅𝑖 (𝑡) is the reliability of a dielectric layer. The capacitor
reliability 𝑅𝑡 (𝑡) as a function of 𝑅𝑖 (𝑡), and N is shown in Figure 5.




                                                                   5
        Figure 5. MLCC reliability 𝑹𝒕 (𝒕) as a function of dielectric reliability 𝑹𝒊 (𝒕) and number of dielectric layers N.

In general, when dielectric reliability 𝑅𝑖 (𝑡) is very close to unity, N does not have a significant impact on MLCC
reliability 𝑅𝑡 (𝑡). If 𝑅𝑖 (𝑡) is reduced slightly, the overall reliability 𝑅𝑡 (𝑡) of an MLCC can degrade rapidly due to the
amplifying effect of the number of dielectric layers N. Since most commercial BME capacitors are made with a large
number of dielectric layers (typically N >250), the impact of N on BME capacitor reliability is critical.

4.3.2 The Impact of Number of Grains per Dielectric Layer
As shown in Figure 6, if a single-layer capacitor Ci has an average grain size 𝑟̅ and an average dielectric thickness d, the
                                                                              𝑑
number of grains per dielectric layer can be calculated as � �.
                                                                              𝑟̅




Figure 6. Estimate of the number of grains in a dielectric layer; with average dielectric thickness d and average grain
                                                                                                𝒅
size �
     𝒓, the number of grains per dielectric layer can be calculated as � �.
                                                                                                𝒓�

                                                                                           𝑑
The MTTF of BME capacitors as a function of parameter � � was measured and reported recently by Murata
                                                                                           𝑟̅
(http://iopscience.iop.org/1757-899X/18/9/092007/pdf/1757-899X_18_9_092007.pdf). Figure 7 shows MTTF data (as
                                                                                  o
presented by time dependence of insulating resistance) under high temperature (150 C) and high DC field (10kV/mm)
                                                                                                                         𝑑
using highly accelerated life test (HALT). The measured MTTF data are proportional to the number of grains � �. But if
                                                                                                                         𝑟̅
                                                                                                               𝑑
the voltage per grain boundary is adjusted to a same value, all four MLCCs with different � � values have almost identical
                                                                                                               𝑟̅
MTTF values. According to Eqs. (5) and (7), the MTTF of a BME capacitor at a given temperature can be written as:
                                           1                     1                         1            𝑑 𝑛
                             𝑀𝑇𝑇𝐹 =              𝑛   =                    𝑛   =                   𝑛   ×� � .                  (11)
                                        𝑉𝑔𝑟𝑎𝑖𝑛               𝑉𝑎𝑝𝑝𝑙𝑖𝑒𝑑                  𝑉𝑎𝑝𝑝𝑙𝑖𝑒𝑑         𝑟̅
                                                         �      𝑑     �
                                                               ���
                                                                𝑟




                                                                                   6
This indicates that the MTTF of BME capacitors follows a power-law relationship to the dielectric thickness d when applied
voltage and average grain size are both given.




                                                                                                 𝒅
Figure 7. MTTF of BME capacitors as a function of grain boundaries per dielectric layer � �. Longer MTTF will be obtained
                                                                                                 𝒓�
                          𝒅
for MLCCs with higher � � values (left); when the applied voltage is adjusted to a constant voltage per grain boundary, MTTF
                          𝒓�
values become identical (test results courtesy of Murata).

                                                           𝑑
In order to implement the microstructure parameter � � into the reliability of a single-layer capacitor, a structural model
                                                           𝑟̅
based on the dielectric thickness and the feature size of a defect can be developed. This model is briefly described be-
low.
As shown in Figure 8, assuming that the feature size of a defect that causes a catastrophic failure is r, d is the dielectric
thickness, and the reliability of the defect is 0, then the reliability of a single dielectric layer 𝑅𝑖 (𝑡) with thickness d will be
determined by the value of d with respect to r. When d is far greater than the defect feature size r, the defect is non-
harmful and may not cause any failures for many years, or even during a capacitor’s lifetime.




Figure 8. An illustration of dielectric thickness d with respect to feature size r of an extrinsic defect inside the dielectric layer.
The dielectric layer reliability is dependent on the ratio r/d: (a), d >> r (b), d ≈ r.

However, as d approaches the feature size of the defect r, the defect will cause dielectric failure instantly. In other words,
the survival probability of the dielectric layer 𝑅𝑖 can be written as 𝑅𝑖 (𝑡) → 1 when d >> r and as 𝑅𝑖 (𝑡) → 0 when d ≈ r .
According to Eq. (11), the Weibull reliability of a dielectric layer with respect to its thickness d and defect feature size r can
thus be expressed as:
                                                                  𝑡 𝛽
                                                                −� �           𝑟 𝜉
                                                  𝑅𝑖 (𝑡) = 𝑒      𝜂     ∙ �1 − � � �.
                                                                               𝑑

For simplicity, the defect size r can be directly related to the average grain size 𝑟̅ as: 𝑟 ≈ 𝑐 × 𝑟̅ , where 𝑐 is a constant.
The equation above can be further expressed with respect to average grain size 𝑟̅ as:
                                                   𝑟 𝜉                 𝑟̅ 𝛼
                                       𝑃 = �1 − � � � = �1 − �𝑑� �, (𝛼 ≥ 5)                                                      (12)
                                                   𝑑


                                                                   7
where P is a geometric factor that determines the dielectric layer reliability 𝑅𝑖 (𝑡) with respect to the microstructure of an
MLCC. 𝛼 is an experimental constant that was determined by the formulation, processing conditions, and microstructure
of a BME capacitor. 𝛼 was determined in this study such that 𝛼 ≈ 6 for V ≤ 50 V and 𝛼 ≈ 5 for V > 50 V.
The Weibull reliability of a BME capacitor is equal to unity when t < η, so the reliability of a single dielectric layer inside of
an MLCC can be expressed as:
                                                   t β
                                                 −� �                r� α                   r� α             r� α
                               R i (t < 𝜂) = e     η     ∙ �1 − �d� � = 1 ∙ �1 − �d� � = �1 − �d� � .                                               (13)

Combining Eqs. (10) and (13) yields the time-independent, simplified reliability of a BME MLCC:
                                                                                      𝑁
                                                                                 𝑟̅ 𝛼
                               𝑅𝑡 (𝑡 < 𝜂) = 𝑅𝑖 (𝑡 < 𝜂)𝑁 = �1 − �𝑑� � , (𝛼 ≥ 5).                                                                     (14)

4.3.3 The Impact of Chip Sizes
In order to reveal the impact of chip size on the reliability of BME MLCCs, the effective areas of MLCC devices with differ-
ent chip sizes have been measured and normalized with respect to the Electronic Industries Alliance (EIA) chip size of
0402, the smallest chip size used in this comparison study. Corresponding measured results are summarized in
Table II. The chip size scaling factor S represents how many times larger the effective area of a given EIA chip size is
than that of 0402 for a single dielectric layer. For example, the effective chip size of a 0805 MLCC is equal to 6.76 times
that of an 0402 MLCC connected in parallel.
Per Figure 2, Table II, and Eq. (9), the single dielectric layer reliability of a 0805 MLCC 𝑅𝑖 (0805) can thus be expressed
with respect to that of a 0402 MLCC 𝑅𝑖 (0402) as:
                                                  𝑅𝑖 (0805) = 𝑅𝑖 (0402)6.76

                          Table II. EIA Chip Size and Calculated Scaling Factors for BME Capacitors
                                                                                 Side                      Effective area of a
        Chip        Length           Width              Terminal-t                           End                                    Chip size
                                                                                margin                   single dielectric layer
        size         (µm)            (µm)                 (µm)                            margin (µm)                 2          scaling factor S
                                                                                 (µm)                            (mm )
       0402       1000 ± 100       500 ± 100        250 ± 150                    125         100                0.225                 1.00
       0603       1600 ± 150       810 ± 150        350 ± 150                    175         100                0.763                 3.39
       0805       2010 ± 200      1250 ± 200        500 ± 200                    250         150                1.520                 6.76
       1206       3200 ± 200      1600 ± 200        500 ± 200                    250         150                3.510                 15.60
       1210       3200 ± 200      2500 ± 200        500 ± 200                    250         150                5.940                 26.40
       1812       4500 ± 300      3200 ± 200        610 ± 300                    300         200                10.920                48.53
       2220       5700 ± 400      5000 ± 400        640 ± 390                    320         220                23.074               102.55
       1825       4500 ± 300      6400 ± 400        610 ± 360                    300         220                23.244               103.31


In general, when the chip size scaling factor S is used, the single dielectric layer reliability of an MLCC with an EIA chip
size of xy can be expressed with respect to the single dielectric layer reliability of a 0402 MLCC as:
                                                  𝑅𝑖 (𝑥𝑦) = 𝑅𝑖 (0402)𝑆                                                                              (15)

When the chip size scaling factor increases by a hundredfold, the single dielectric layer reliability declines: 45% when
𝑅𝑖 (0402)= 99%; 10% when 𝑅𝑖 (0402)= 99.9%; and 1% when 𝑅𝑖 (0402)= 99.99%. The single dielectric layer reliability of
MLCCs decreases with increasing chip size, but not significantly in comparison to the reliability decrease that accompa-
nies an increase in the number of dielectric layers. Results are shown in Figure 9.
Furthermore, according to Eq. (10), the reliability of a MLCC with chip size xy 𝑅𝑡 (𝑥𝑦) can be expressed as:
                                                                                                   𝑁𝑥𝑦   𝑆
                                       𝑅𝑡 (𝑥𝑦) = [𝑅𝑖 (0402)𝑁𝑥𝑦 ]𝑆 = �𝑅𝑡 (0402)𝑁0402 � ,                                                             (16)


                                                                            8
where 𝑅𝑡 (𝑥𝑦) is the reliability of an BME MLCC with a chip size of xy and Nxy of dielectric layers; and
𝑅𝑡 (0402) = 𝑅𝑖 (0402)𝑁0402 is that with an 0402 chip size and N0402 of dielectric layers. The construction analysis of BME
                                                                                𝑁𝑥𝑦
capacitors has revealed that N0402 ≈ 70–80 and Nxy ≈ 250–300, so that                   ≈ 3–4.
                                                                                𝑁0402




 Figure 9. The single dielectric layer reliability Ri (xy) as a function of EIA chip size, and the single layer reliability of a 0402
                                                           MLCC Ri (0402).


Conversely, the dielectric thickness of BME capacitors is also found to gradually increase with MLCC chip size. Figure 10
shows the construction analysis results of average BME dielectric thickness as a function of chip size. According to
Eq. (11), the MTTF of an MLCC follows a power-law increase with increasing dielectric thickness. Therefore, the reliability
decreases due to increasing chip size have been fully compensated for by increasing the dielectric thickness.
As a result of that, the overall reliability of a BME MLCC will not change significantly with increasing capacitor chip size.




                    Figure 10. Measured average dielectric thickness as function of BME MLCC chip size.

5. Summary
The general expression of a BME capacitor’s reliability given in Eq. (3) can be specifically rewritten for BME capacitors
based on this study. A two-parameter Weibull distribution is applicable to 𝛾(𝑡). Two identified failure modes will follow
different acceleration functions 𝐴𝐹(𝑉, 𝑇), as summarized in Table I. Function 𝜑(𝑁, 𝑑, 𝑟̅ , 𝑆) can be expressed using
Eq. (14). The impact of chip size S on the reliability of BME capacitors is negligible. Therefore, the reliability of a BME
capacitor is finally obtained:

                     𝑅(𝑡) = 𝜑(𝑁, 𝑑, 𝑟̅ , 𝑆) × 𝐴𝐹(𝑉, 𝑇) × 𝛾(𝑡)
                                                                  9
                                                                       β1
                                                                                                                      β2
                                                              t                                        t
                                                   −�          Ea1 �                        −�                    �
                                       𝑁                                                                  E
                                  𝑟� 𝛼                  A � kT
                                                           ∙e
                                                                  �                                      � a2 �
                        = �1 − �𝑑� � × { p × e          Vn                  + (1 − p) × e        Ce−bE ∙e kT               }
where β1 and β2 are the Weibull slope parameters for catastrophic and slow degradation failures, respectively; Ea1 and Ea2
are the activation energies for the two failure modes, respectively; p the percentage of catastrophic failures; A, b, C are
constants; 𝛼 is a constant that can be determined experimentally; and N, d, and 𝑟̅ are the number of dielectric layers, av-
erage dielectric thickness, and average grain size, respectively.


6. NASA NEPP-Funded Studies on BME Capacitors
The NASA NEPP program began funding the evaluation of BME capacitors as early as 2004. Following are selected pub-
lications on the evaluation of BME capacitors, including a recently released publication entitled “Selection, Qualification,
Inspection, and Derating of Multilayer Ceramic Capacitors with Base-Metal Electrodes.” These publications can be ac-
cessed via the web links provided. Detailed discussions on the reliability of BME capacitors and other related issues can
be found in these published technical papers.
  1.   J. Brusse and M. Sampson, “COTS Ceramic Chip Capacitors: An Evaluation of the Parts and Assurance Methodol-
       ogies,” CARTS Proceedings, San Antonio, TX, pp. 128-140, (2004). (http://nepp.nasa.gov/DocUploads/65B2E69A-
       658E-46EE-BF080EAB54B25EDC/2004%20Brusse-COTS%20Ceramic%20Caps%20-
       %20An%20Eval%20Report.pdf)
  2.   D. Liu, H. Leidecker, T. Perry, and F. Felt, “Accelerating Factors in Life Testing of High-Voltage Multilayer Ceramic
       Capacitors,” CARTS Proceedings, Palm Springs, pp. 151–156, (March 21–24, 2005).
       (ecadigitallibrary.com/pdf/CARTS50551_05ijt.pdf)
  3.   D. Liu and M. Sampson, “Reliability Evaluation of Base-Metal-Electrode Multilayer Ceramic Capacitors for Potential
       Space Applications,” CARTS Proceedings, pp. 45–63, (2011).
       (https://nepp.nasa.gov/files/21703/GSFC_Liu_Sampson_Reliability_Eval_BME_Multilayer_Ceramic.pdf)
  4.   D. Liu, “Failure Modes in Capacitors When Tested Under a Time-Varying Stress,” CARTS Proceedings, pp. 209-
       223, (2011). (https://nepp.nasa.gov/files/21705/11_005_gsfc_Liu_Failure_Modes_in_Capacitors.pdf)
  5.   D. Liu and M. J. Sampson, “Some Aspects of the Failure Mechanisms in BaTiO3-Based Multilayer Ceramic Capaci-
       tors,” CARTS Proceedings, Las Vegas, NV, pp. 59–71, (March 26–29, 2012). (CARTS Outstanding Paper Award)
       (https://nepp.nasa.gov/files/24291/CARTS2012_Liu_BaTiO3.pdf)
  6.   D. Liu, “Evaluation of Multilayer Ceramic Capacitors with C0G Dielectric and Base-Metal Electrodes,” NASA NEPP
       FY Report, Part II, NEPP Task 1051-005, GSFC, Greenbelt, MD (2012).
       (https://nepp.nasa.gov/files/24320/Liu_2013_Pt2Capacitors.pdf)
  7.   D. Liu, “Highly Accelerated Life Stress Testing (HALST) of Base-Metal Electrode Multilayer Ceramic Capacitors,”
       CARTS Proceedings, Houston, TX, pp. 235–248, (March 26–29, 2013).
       (https://nepp.nasa.gov/files/24300/CARTS2013_Liu_HALST.pdf)
  8.   R. Weachock and D. Liu, “Failure Analysis of Dielectric Breakdowns in Base-Metal Electrode Multilayer Ceramic
       Capacitors,” CARTS Proceedings, Houston, TX, pp. 151-165, (2013).
       (https://nepp.nasa.gov/files/24303/CARTS2013_Liu_FailureAnalysis.pdf)
  9.   D. Liu, “Selection, Qualification, Inspection, and Derating of Multilayer Ceramic Capacitors with Base-Metal Elec-
       trodes,” NASA NEPP FY Report, (2013). (https://nepp.nasa.gov/files/24351/Liu_2013_G11_BME_Guidelines.pdf)
For more information, contact
David (Donhang) Liu at 301-286-8573




                                                                  10
GIDEP Alerts/Advisories                                            Upcoming Meetings
Contact your GIDEP Representative for a copy of:                    •   JEDEC JC-13, Memphis, Tennessee, May 20–23,
                                                                        2013
                   CHZ-A-13-01 Disk Drive Unit, CHZ-A-
                   13-02 Disk Drive Unit, CHZ-A-13-03               •   Electronics Technology Workshop (ETW) at GSFC,
                   Disk Drive Unit, D8Y-A-13-06 4-Port                  Greenbelt, Maryland, June 11–12, 2013
                   Gigabit and 24-Port Ethernet                         http://nepp.nasa.gov/workshops/etw2013/
                   Switch/Router, D8Y-A-13-07A,
                   Unprogrammable parts, Highly Pro-                •   JEDEC JC-13, Columbus, Ohio, Sept. 16–19, 2013
   Suspect
                   grammable Voltage Supervisory Circuit,           •
                                                                                                                 st
    Coun-                                                               Space Passive Component Days, 1 International
                   D8Y-A-13-08A Suspect Counterfeit,                    Symposium, ESA/ESTEC, Noordwijk, the Nether-
    terfeit
                   Microcircuit, 32Kx8 Autostore nvSRAM,                lands, September 24–26, 2013
                   GR2-P-13-01 Transistor, Silicon PNP, 6               http://www.globaleventslist.elsevier.com/events/201
                   Watt, R4-A-13-06 Microcircuit, Op-Amp,               3/09/space-passive-component-days/
                   1000 uV Offset-Max, 725 MHz Band
                   Width

                   EK-S-13-01 Connector, Plug, Electrical,
                   EO-P-13-01 Samarium Cobalt (SmCo)                Contacts
                   Specialty Metal High Performance
                   Magnet, GB4-P-13-02A Microcircuit,              NEPAG
                   Digital, CMOS, Radiation Hardened, 32-          http://atpo.jpl.nasa.gov/nepag/index.html
                   BIT Fault-Tolerant Processor, Monolith-
                   ic Silicon, GB4-P-13-03 Microcircuit,           Shri Agarwal 818-354-5598
     Misc.         Memory, Digital, CMOS, Radiation                Shri.g.agarwal@jpl.nasa.gov
                   Hardened Dual Voltage SRAM, with                Lori Risse 818-354-5131
                   EDAC, NX4-P-13-01A Contact, Termini,            Lori.a.risse@jpl.nasa.gov
                   Fiber Optic, Connector, Removable En-
                   vironment Resisting, Pin/Socket Termi-
                   nus, SW3-P-13-01 Microcircuit, Digital
                   Driver, High Level                              ATPO http://atpo.jpl.nasa.gov
                                                                   Chuck Barnes 818-354-4467
                                                                   Charles.e.barnes@jpl.nasa.gov

Reduced Schedule of Meetings
                                                                   JPL Electronic Parts http://parts.jpl.nasa.gov
(Communication from DLA)
                                                                   Rob Menke 818-393-7780
Due to “sequestration” and other budgetary negotiations            Robert.j.menke@jpl.nasa.gov
in Congress and the associated contingency planning at
DLA due to these negotiations, all travel that can be de-
ferred will be deferred indefinitely. The publishing of the        Previous Issues:
audit schedule will also be suspended during this time.            JPL: http://atpo/nepag/index.html
For the rare exceptions to the travel deferment, you               Other NASA centers:
should hear from the responsible engineer/technician or            http://nepp.nasa.gov/index.cfm/12753
Branch Chief directly. If you have any questions, please           Public Link (best with Internet Explorer):
direct them to Joe Gemperline, (614) 692-0663, or Jo-              http://trs-new.jpl.nasa.gov/dspace/handle/2014/41402
seph.Gemperline@dla.mil.


NASA Parts Specialists Recent Support for
DLA Land and Maritime Audits:
Audit performed at Crane Electronics, Redmond,
Washington
____________________________________________________________________________
www.nasa.gov                                                                        © 2013 California Institute of Technology
National Aeronautics and Space Administration                                       Government sponsorship Acknowledged.
Jet Propulsion Laboratory
California Institute of Technology
Pasadena, California


                                                              11
