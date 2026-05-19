            NASA Electronic Parts and Packaging (NEPP)
                             Program




   NEPP Task: Guidelines for Selection of Ceramic Capacitors for Space
                              Applications




Cracking Problems in Low-Voltage Chip Ceramic
                 Capacitors




                              Alexander Teverovsky
                          ASRC Federal Space and Defense
                          Alexander.A.Teverovsky@nasa.gov

         Worked performed at NASA Goddard Space Flight Center


                                      2018


To be published on nepp.nasa.gov.                                        1
 Cracking Problems in Low-Voltage Chip Ceramic Capacitors

Abstract
   Cracking remains the major reason of failures in multilayer ceramic capacitors (MLCCs) used in space
   electronics. Due to a tight quality control of space-grade components, the probability that as manufactured
   capacitors have cracks is relatively low, and cracking is often occurs during assembly, handling and the
   following testing of the systems. Majority of capacitors with cracks are revealed during the integration and
   testing period, but although extremely rarely, defective parts remain undetected and result in failures during
   the mission. Manual soldering and rework that are often used during low volume production of circuit boards
   for space aggravate this situation. Although failures of MLCCs are often attributed to the post-manufacturing
   stresses, in many cases they are due to a combination of certain deviations in the manufacturing processes
   that result in hidden defects in the parts and excessive stresses during assembly and use. This report gives
   an overview of design, manufacturing and testing processes of MLCCs focusing on elements related to
   cracking problems. The existing and new screening and qualification procedures and techniques are briefly
   described and assessed by their effectiveness in revealing cracks. The capability of different test methods to
   simulate stresses resulting in cracking, mechanisms of failures in capacitors with cracks, and possible
   methods of selecting capacitors the most robust to manual soldering stresses are discussed.




To be published on nepp.nasa.gov.                                                                                   2
Contents
1.     INTRODUCTION ............................................................................................................................................. 5
2.     MANUFACTURING PROCESSES AND TYPES OF MLCCS ................................................................................... 8
     2.1.     DIELECTRIC MATERIALS .....................................................................................................................................10
     2.2.     ELECTRODE MATERIALS.....................................................................................................................................11
     2.3.     TERMINATION MATERIALS .................................................................................................................................12
       •      Flexible terminations ..................................................................................................................................14
     2.4.     DESIGN .........................................................................................................................................................15
       •      Laser marking .............................................................................................................................................18
3.     TESTING AND QUALITY ASSURANCE ............................................................................................................ 19
     3.1.     COMPARATIVE ANALYSIS OF SPECIFICATIONS .........................................................................................................19
       •      Military specifications ................................................................................................................................20
       •      NASA/GSFC specifications ..........................................................................................................................22
       •      ESA and JAXA specifications .......................................................................................................................24
       •      Automotive industry specifications ............................................................................................................25
     3.2.     QUALIFICATION PROCEDURES AND CRACKING PROBLEMS IN MLCCS..........................................................................25
       •      Thermal shock ............................................................................................................................................26
       •      Life testing ..................................................................................................................................................27
       •      Humidity testing .........................................................................................................................................27
       •      Resistance to soldering heat ......................................................................................................................28
       •      Flex testing .................................................................................................................................................30
       •      Sample size .................................................................................................................................................31
4.     CHARACTERISTICS OF MLCCS ....................................................................................................................... 32
       •      Rated voltage .............................................................................................................................................32
     4.1.     CAPACITANCE AND DISSIPATION FACTOR ..............................................................................................................32
     4.2.     INSULATION RESISTANCE AND LEAKAGE CURRENTS .................................................................................................34
       •      Specified IR values ......................................................................................................................................35
       •      Absorption and intrinsic leakage currents..................................................................................................36
       •      Effect of cracking on IR...............................................................................................................................38
     4.3.     BREAKDOWN VOLTAGE .....................................................................................................................................39
     4.4.     MECHANICAL CHARACTERISTICS .........................................................................................................................40
       •      Flexural strength ........................................................................................................................................41
       •      Vickers hardness .........................................................................................................................................43
       •      Indentation fracture toughness..................................................................................................................43
5.     FAILURE MECHANISMS IN MLCCS WITH CRACKS ......................................................................................... 44
     5.1.     DEGRADATION OF PME AND BME CAPACITORS IN THE PRESENCE OF MOISTURE .........................................................45
     5.2.     DEGRADATION IN DRY ENVIRONMENTS ................................................................................................................51
6.     SPECIAL CASES OF MLCC CRACKING DURING MANUFACTURING, ASSEMBLY, AND TESTING ....................... 52
     6.1.     HYDROGEN-RELATED CRACKING .........................................................................................................................53
     6.2.     EFFECT OF PICK AND PLACE MACHINE ..................................................................................................................55
     6.3.     ELECTRO-MECHANICAL RESONANCE ....................................................................................................................55
7.     REVEALING CRACKS ..................................................................................................................................... 57


To be published on nepp.nasa.gov.                                                                                                                                             3
     7.1.      OPTICAL EXAMINATIONS ...................................................................................................................................57
       •       Vicinal illumination.....................................................................................................................................57
       •       Revealing delamination by discoloration of ceramic layers. ......................................................................58
     7.2.      ELECTRICAL MEASUREMENTS .............................................................................................................................58
       •       Methanol test .............................................................................................................................................59
       •       Temperature dependence of capacitance ..................................................................................................59
       •       Time Domain Reflectometry (TDR) .............................................................................................................59
       •       Absorption voltage .....................................................................................................................................59
     7.3.      ELECTRO-MECHANICAL EFFECTS .........................................................................................................................60
       •       Variations of the electro-mechanical resonance spectrum ........................................................................60
       •       Resonant ultrasound spectroscopy (RUS)...................................................................................................60
       •       Tone-burst excitation .................................................................................................................................61
       •       Acoustic emission .......................................................................................................................................61
       •       Laser interferometry...................................................................................................................................61
8.     CRACKING CAUSED BY MANUAL SOLDERING .............................................................................................. 62
     8.1.      WORKMANSHIP RECOMMENDATIONS FOR MANUAL SOLDERING ...............................................................................63
       •       Effect of touch-up .......................................................................................................................................64
     8.2.      SELECTING CAPACITORS ROBUST TO MANUAL SOLDERING ........................................................................................65
       •       Terminal solder dip testing .........................................................................................................................65
       •       Assessment of the susceptibility to cracking ..............................................................................................66
9.     CONCLUSION ............................................................................................................................................... 67
10.         REFERENCES ............................................................................................................................................ 68




To be published on nepp.nasa.gov.                                                                                                                                         4
1. Introduction
Multilayer ceramic capacitors (MLCCs) constitute the majority of components used in electronic assemblies, mostly
as filtering, bypass or decoupling devices. Since 2010 more than a trillion of MLCCs is manufactured every year in
the world and consumed mostly by smart phones, PCs, TVs, and automotive industry [1, 2]. This makes MLCCs the
most widely used passive component. Early generations of mobile phones used several dozens of MLCCs but modern
smartphones have more than 600. A significant growth in consumption of electronics occurs within the automotive
sector. Many vehicles today use more than 300 MLCCs in both ‘under the hood’ (engine management) applications
and in the ‘passenger compartment‘. However, the latest Tesla models of electric cars have over 10,000 MLCCs per
vehicle. Most commercial applications require cheaper and smaller size MLCCs. In 2018 almost 50% of the market
share were size 0402 devices, but their production is declining and size 0201 capacitors are growing much faster. It
is expected that in the near future the predominance of the 0201 case size will decline in favor of the size 01005, which
already has 10% market share. Further, the designers should consider the 008004, a device that is taking off rapidly
and is already outselling the 1206 size capacitors. Advancement of small size, high CV value, low-voltage MLCCs
in commercial systems raised concerns regarding insulation resistance, IR, degradation and parametric failures in
capacitors related to migration of oxygen vacancies [3, 4].
Compared to commercial, hi-rel and especially space systems are using a more conservative approach for selection of
components and a substantial proportion of MLCCs used in high-level space projects has size 1206 and larger.
However, the trend for using smaller size, high volumetric efficiency capacitors exists, and the use of advanced
technology capacitors in newly design space instruments and systems is increasing.
Considering the amount of MLCCs used, the overall probability of their failures is extremely low. Still, because they
are failing typically in a short circuit mode, failures might cause catastrophic consequences to the whole system, cease
some system functions, or result in intermittent failures that can be misgauged as a software problem. Capacitors are
typically responsible for up to 30% of the field failures in commercial systems, and until recently, approximately half
of these failures were due to cracking in the parts [5].
The proportion of MLCCs in space instruments is similar to commercial assemblies and varies from 10 to 20% of all
electronic components. According to Paumanok Publications [6] the cost of capacitors procured by aerospace industry
is 73% of the whole cost of passive components. The major vendors that produce 57% of all capacitors procured by
aerospace companies are AVX Corporation, Vishay Intertechnology, and Kemet Electronics (see Fig.1.1). Japanese
vendors who dominate commercial market (TDK Corporation, Murata Manufacturing, Matsushita, Rubycon) do not
sell directly to the global defense markets; however, capacitors produced in Japan find their way into defense
electronics through distribution.




           Figure 1.1. Top manufacturers of capacitors for defense and aerospace electronics in 2017 [6]

To be published on nepp.nasa.gov.                                                                                      5
Cracks and delamination in MLCCs might originate from manufacturing processes or be introduced during assembly
or the following handling and testing of the boards (flex cracks or thermal shock cracks). Examples of different types
of cracks are shown in Fig. 1.2.




  a) Manufacturing defect: CDR 0.1 µF 100 V capacitor        b) Manufacturing defect: voids and delaminations (knit
   that failed due to delamination at ~1.5 kohm during                           line cracks).
                     board-level testing




          c) Assembly-related defect: flex crack.             d) Assembly-related defect: thermal shock cracking.




         e) Cracking caused by manual soldering.             f) Cracking caused by touch-up after reflow soldering.
                                  Figure 1.2. Different types of cracks in MLCCs.
A brief description of different causes of cracking is given below.
1. Manufacturing defects.
Note that some defects might not result in formation of visual cracks, but rather weaken the part and make them more
susceptible to cracking during assembly and applications. For example, thermal cracks caused by soldering might
initiate at the internal flaws such as voids and delaminations.
    1.1. Rapid cooling of the laminates can cause so-called firing cracks that typically propagate perpendicular to the
        plane at the terminals.
    1.2. Insufficient binding strength and/or the presence of foreign materials might result in knit-line cracks that
        typically extend parallel to the electrodes.
    1.3. Delaminations and knit line defects were a rather common defects in early ceramic capacitors, but are rare in
        contemporary MLCCs, especially those manufactured to military specification. Formation of the electrode-
        ceramic delaminations during manufacturing can be attributed to variety of reasons. C. Hodgkins [7] identified
        nine principal causes for interlayer ceramic-metal separation that include outgassing of the solvent binder

To be published on nepp.nasa.gov.                                                                                     6
       (removal of the vaporized binder during pre-sintering processes that occurs along the ceramic/metal electrode
       interfaces), trapped air during lamination, and surface contamination. Another possible reason for
       delaminations of PME capacitors is oxidation of palladium electrodes in air that is accompanied with volume
       expansion.
2. Assembly.
   2.1. Pick-and-place machines can damage parts by excessive stresses created by centering jaws or vacuum picks.
   2.2. Thermal shock cracks are due to a sharp temperature increase during soldering. These stresses might form
      large, visible U-shaped cracks on the surface of capacitors.
   2.3. Thermal shock cracks might also occur when liquid cleaners are applied to a board that has not sufficiently
      cooled after soldering reflow. The effect is due to a much higher sensitivity of MLCCs to the cold (from hot
      to cold) compared to hot (from hot to cold) thermal shocks [8]. To prevent this type of cracking the boards
      should be cooled slowly, preferably by natural cooling, or at a rate not exceeding 2 ºC to 3 ºC/sec., to
      temperatures below 60 ºC.
   2.4. Tensile stresses and cracking might develop in MLCCs after soldering them onto alumina boards, which is
      due to the differences in CTEs between the ceramic material and substrate, with the latter having lower CTEs.
      These stresses were responsible for many observed failures in the first ceramic chip capacitors mounted on
      alumina substrates in hybrids [9].
3. Board-level handling.
      Due to the lack of stress relief in mounted chip capacitors, deformation and flexing of the PWB might create
      significant tensile stresses resulting in so-called flex cracking. These cracks mostly originate at the bottom
      surface near the edge of the termination margin and propagate inside at angles close to 45º [10]. Typical sources
      of the flex cracking are de-paneling, test probing, handling during visual examinations, attachment of standoff
      elements and connectors, etc.
4 Application.
   4.1. Deformation of the board caused by temperature cycling, vibration or mechanical shocks that occur during the
      ground phase testing and integration or launch of the spacecraft might cause flexing of the board sufficient for
      cracking of MLCCs. Multiple guidelines for design and board layout have been developed to reduce the
      probability of this type of failures [11].
   4.2. Due to electrostriction in ceramic materials, voltage cycling might create mechanical stresses that would
      further develop preexisting microcracks, resulting in failures. This mechanism might be especially important
      for high-voltage ceramic capacitors [12, 13].
   4.3. Electro-mechanical resonances in class II dielectric capacitors due to the reverse piezoelectric effect in
      ceramics (see section 6.3).
Although soldering-induced damage might not lead to immediate failures and damaged capacitors may endure weeks
or months of service use, it can cause degradation of characteristics with time resulting eventually in field failures. In
this regard, microcracks in capacitors generated during assembly can be considered as a “time bomb” [14] that causes
increased leakage currents, shorts, opens, or intermittent contacts as degradation develops or cracks propagate with
time during application.
Cracking in ceramic capacitors is an old problem. It appeared in the 1970s when first surface mount technology
(SMT) chip capacitors were introduced to the market and their employment in NASA applications begun [9, 15].
According to J. Maxwell [11] this problem will continue to be with us in the foreseeable future. Two main factors
contribute to the problem: brittleness of ceramic materials and thermal and mechanical stresses associated with the
assembly process and/or post assembly handling and testing. Both factors are intrinsic to chip ceramic capacitors and
explain the persistence of the problem.
Due to a relatively large size of military and space-grade capacitors used in space systems and use of manual soldering,
a substantial proportion of MLCC cracking failures is attributed to the assembly process. Experience shows that the
propensity to cracking is lot-related, which means that cracking is often due to a combination of the weakness in the
part caused by flaws introduced during manufacturing and assembly-related stresses. A proper screening or
qualification testing could have revealed lots with defects and reduced the probability of failures.



To be published on nepp.nasa.gov.                                                                                       7
Historically, majority of defects in MLCCs were due to the manufacturing processes, and the screening and
qualification (S&Q) system used in military specifications was focused on revealing and removing this type of defects.
Currently, the proportion of manufacturing defects have been reduced substantially, and most problems with MLCCs
are due to the post-manufacturing stresses. However, the requirements in military specifications remain mostly
unchanged and do not address sufficiently post-manufacturing stresses.
One of the most powerful means used by hi-rel OEMs to improve reliability of components is derating that limits the
level of stress (typically, voltage and temperature) compared to the operating conditions specified for the part.
However, due to the low-voltage failure phenomena in MLCCs (see section 5.1) derating might be not effective in
reducing risks associated with cracking in the parts.
In this report, we will first give an overview of manufacturing processes and types of MLCCs and consider to what
degree the existing S&Q system assures safe assembly and reliable operation of the part. Techniques used to reveal
capacitors with cracks, failure modes and mechanisms related to cracking will be reviewed and possible risk mitigating
measures to reduce failures associated with manual soldering discussed.

2. Manufacturing processes and types of MLCCs
All MLCCs are manufactured using a ceramic slurry (a mixture of ceramic powder, dispersant, solvent, and organic
binder) and a paste for metal electrodes (see Fig.2.1). The dielectric layers are formed by the casting process and then
electrodes are formed by applying the paste by screen printing. Dry or wet stacking processes are used depending on
conditions of the layers used for lamination. During the wet process, the next layer of the ceramic slurry and electrode
paste are laid down on the top of the previous layer and then the stack is dried out to remove the binder (at ~ 400 ºC).
During the dry process the layers are casted on a Mylar or stainless steel belt, then dried out, removed from the belt,
stacked, and laminated at elevated temperature under pressure. It is considered that the wet process that is typically
used to manufacture precious metal electrode (PME) capacitors allows for a better interlayer bonding that results in
less delamination.

The dry process that is mostly used for the base metal electrode (BME) technology allows for thinner dielectric layers
and larger number of electrodes. Maximum number of layers for dry technology is ~1000 layers with the thickness
of the dielectric down to submicrometers, whereas for the wet technology the number of layers typically is less than
200 and the thickness is more than ~5 µm. However, experience shows that the type of the process is not a significant
factor affecting the probability of cracking in MLCCs and both methods, when optimized, are capable of producing
high-quality, defect free microstructure of MLCCs.

After cutting and presintering, the parts go through the tumbling process (not shown in Fig.2.1) to smooth and round
the corners and help to obtain good coverage of the termination ink and subsequent barrier layer plating. The tumbling
occurs in rotating barrels filled with water and zirconium balls. Tumbling also minimizes mechanical stresses at the
corners of the part and reduces breakages during pick and place operations [16].

After tumbling and drying, the parts are sintered/fired in kilns at high (typically above 1000 ºC) and tightly controlled
temperatures. The following processes include application of the base termination to make contacts to the internal
electrodes, electroplating and finishing.




To be published on nepp.nasa.gov.                                                                                      8
                          Figure 2.1. Schematic of the processes of MLCCs manufacturing [17].

Fig.2.2 shows a typical construction of a low-voltage (below 200 V) MLCC. The major elements of the part are
ceramic dielectric, metal electrodes, and terminations. Respectively, the type of capacitors depends on materials used
in these elements (see Table 2.1). Different types of ceramic materials can be used with different types of metal
electrodes and terminations resulting in a large variety of types of MLCCs. This variety further increases considering
different sizes and outlines of the parts. Standard design low-voltage MLCCs have two terminals, but for some
applications, in particular, for decoupling in microcircuits (e.g. FPGA), a design is changed to reduce inductance of
the parts.




                                         Figure 2.2. Schematic of a low-voltage MLCC.

                                         Table 2.1. Classification of low-voltage MLCCs

                                                                                                 Design (size
      Ceramic dielectric                        Electrode               Termination
                                                                                                 and olutline)
                                                               •  Base termination:
  •   Class I (C0G, NP0, BP, BG)                                 o silver glass frit (for PME)
      High stability, low loss                                   o copper glass frit (for BME)
                                                               • Barrier layer:
  •   Class II (e.g. X7R, BX) High                               o Ni
      volumetric efficiency with            •   Ag/Pd (PME)                                      •   Standard, two
                                                                 o Cu (non-magnetic)
                                                                                                     terminals.
      variations of cap. ±15% in temp.                         • Polymer (flex term. only)
      range from -55ºC to +125ºC.           •   Ni (BME)         o Silver epoxy                  •   Low inductance.
                                                               • Finish plating
  •   Class III (e.g. Y5V) Higher                                o Sn/Pb
      volumetric efficiency than class                           o Ag-Pd (non-magnetic)
      II, but less stable.                                       o Au (wire bond attachment)
                                                                 o Sn (ROHS compliant)




To be published on nepp.nasa.gov.                                                                                      9
    2.1. Dielectric materials
Materials used in MLCCs have polycrystalline structure that is based on barium titanate (BaTiO3) ceramics with
different doping for different areas of application and a few percent of glass to interconnect crystal grains. Based on
temperature stability of the dielectric constant, K, capacitors are divided into three classes of materials (see Table 2.2).
Per EIA-198 [18] classification, the level of temperature stability is characterized by a three-character alphanumeric
code (see Table 2.3) indicating the minimal low temperature, maximum high temperature, and maximum capacitance
change over the temperature range.
                       Table 2.2. Characteristics of dielectric materials in MLCCs per EIA 198
                                                                                                     Maximum
          EIA class         Dielectric       Low Temp.         High Temp          Maximum          loss of C, %
          dielectric*         class           rating, ºC        rating, ºC        Temp shift        per decade
                                                                                                      hour **
              C0G                 I               -55               125           ± 30 ppm/ºC             0
              X7R                II               -55               125              ± 15%               2.5
              Y5V                III              -30                85           +22% -82%               7

Characteristics of class III ceramic capacitors vary substantially with temperature, voltage and time under bias or
duration of storage. Due to a limited temperature range of class III capacitors, they cannot be tested and stressed to
the level that is typically used for high-reliability parts and are not recommended for space applications.
Class I ceramic capacitors are the most temperature stable, have minimal dielectric losses and are typically used in RF
systems. Thermal stability codes for this type of dielectrics are described in EIA-198, but the most commonly used
is C0G type that is also known as NP0-type or BP/BG in MIL specifications. These materials are paraelectrics and
have a relatively low dielectric constant (K < 100) that does not vary with voltage. Class I ceramic capacitors have a
relatively small concentration of barium titanate, below 50%, and are composed of a mixture of finely ground materials
such as Titanium dioxide (rutile, TiO2) or CaTiO3 modified by different additives (Zn, Zr, Nb, Mg, Ta, at al.).
KEMET is using calcium zirconate (CaZrO3) ceramics with K ~ 32 for class I dielectrics that allows for expanding
capacitance values in U2J type BME capacitors into the range previously available only in Class II dielectric materials
such as X5R and X7R.
                      Table 2.3. Temperature characteristic codes for class II and III dielectrics
      Low Temp.,                        High Temp.,                       Max. capacitance change
                         Symbol                             Symbol                                             Symbol
          ºC                                ºC                              over temp range, %
           +10               Z               +45                2                       ±1                       A
           -30               Y               +65                4                     ±1.5                       B
           -55               X               +85                5                     ±2.2                       C
                                             +105               6                     ±3.3                       D
                                             +125               7                     ±4.7                       E
                                             +150               8                     ±7.5                       F
                                             +200               9                      ±10                       P
                                                                                       ±15                       R
                                                                                       ±22                       S
                                                                                    +22 to -33                   T
                                                                                    +22 to -56                   U
                                                                                    +22 to -82                   V
Examples. X7R: X=> -55C, 7=> +125C, R=> ±15%.
          Z5U: Z=> +10C, 5=> +85C, U=> +22% to -56%
Class II and III dielectrics are based on ceramics with barium titanate concentration exceeding 90% that is doped with
different elements (e.g. rare earth elements La, Nd, Sm, Gd, Dy, Ho, Er, Yt, Mg, Va) and behave as ferroelectrics at
temperatures below ~ 125 ºC (Curie point) and as paraelectrics at higher temperatures. Their dielectric constant is
high, in the range from 200 to more than 10,000 for class II and more than 10,000 for class III capacitors, but the value



To be published on nepp.nasa.gov.                                                                                       10
of K is temperature dependent and varies substantially with applied voltage. Comparative temperature dependencies
of dielectric constant for different types of dielectrics are shown in Fig. 2.3.
Polycrystals in barium titanate ceramics are comprised of micrometer size grains that have glassy grain boundaries
and a crystalline core-shell structure that determines performance and reliability of capacitors [19]. A high-resistive
shell doped with rare elements is formed around the grain of the barium titanate ceramic during sintering. At
temperatures below the Curie point, the grains are divided into randomly oriented domains that have the same
spontaneous polarization (see Fig. 2.4). AC electric field changes the direction of polarization resulting in high values
of the dielectric constants. Under DC bias the reversal of polarization caused by AC signal is limited that is reflected
in a reduction of the dielectric constant with DC voltage in class II and III dielectrics.


                                                                                                       Grain



                                                                                  Core

                                                                                  Shell          Domain


  Figure 2.3. Comparative temperature dependencies of
                                                              Figure 2.4. TEM image of a BaTiO3 ceramic showing
    dielectric constant in different types of materials J.
                                                                         core-sell structure of a grain [21].
               Prymak, KEMET tutorial [20].
Low-voltage PME MLCCs manufactured to military specifications have typically a relatively thick dielectric layers,
in the range from 20 to 30 µm, and the number of layers below 100. Stacking of large size MLCCs is used to produce
large, microfarad range capacitors. Similar values of capacitance in BME MLCCs are reached in a smaller size parts
by reducing the thickness of the dielectric layers and increasing their number. Contemporary BME capacitors can
have dielectric thickness as low as 0.5 - 0.7 μm and have up to 400 layers in case size 0402. Production of this type
of capacitors require a very small grain size that is getting closer to the dimensional limit [22]. Reduction of the grain
size below a certain optimum (~1 µm) decreases room temperature dielectric constant and temperature stability of
capacitors. Until recently, maximum operation temperature of capacitors was 150 ºC (X8R, X8S, and X8T types),
which is likely a limit for barium titanate ceramics. Development of new types of materials, e.g. tungsten-bronze type
ferroelectrics, allows increasing further operating temperatures and development of X9R BME capacitors that can
operate in the range from -55 ºC to +200 ºC.

    2.2. Electrode materials
Historically, MLCCs used in space application had electrodes made of precious metals, typically silver/palladium
alloys (PME capacitors), but starting 2017 capacitors with nickel electrodes, or base metal electrode (BME) capacitors
manufactured per MIL-PRF-32535 are qualified for space applications. BME capacitors have been widely employed
in commercial and automotive industry applications since mid-90th mostly due to a lower price of materials. Table
2.4 shows characteristics of different types of metals used to form electrodes in MLCCs including the atmosphere for
the metal paste firing.
                       Table 2.4. Physical properties and price ratio of electrode materials [21]
                                    Melting           Resistivity,         Firing
                    Metal                                                                   Price ratio
                                    point, ºC           mohm            atmosphere
                     Ag                961               1.62                Air                  3
                     Cu               1080               1.72             Reducing                1
                     Ni               1453                6.9             Reducing                1
                     Pd               1552               10.4                Air                 80


To be published on nepp.nasa.gov.                                                                                      11
The paste that is typically used for PME capacitors has relatively large particle sizes, from 900 to 1000 nm, whereas
BME technology uses pasts with smaller particles, from 300 to 500 nm. This allows formation of relatively thin nickel
electrode layers. Typically, a composition of 70% Ag and 30% Pd is used for PME capacitors; however, depending
on design, manufacturing process, and type of ceramic, the Ag/Pd ratio can vary substantially.
Silver/palladium alloys do not react with ceramic and do not oxidize significantly, which allows for sintering in air
atmosphere. Although PME technology has been used for decades, some challenges during firing of capacitors with
Ag/Pd electrodes still exist [2]. These challenges include catalyzation of the binder burn-out that might accelerate gas
generation and cause delaminations and volumetric changes in the electrodes that can also facilitate delaminations.
Volumetric changes are due to increasing Pd volume up to 68% when it is oxidized at ~500 °C and reduces back at
~800 °C. A low melting temperature glassy components should be used to limit the firing temperature for 70Ag/30Pd
alloy to ~1,100°C, which results in reduction of the dielectric constant of ceramics. Silver evaporation during firing
requires using special measures to increase Ag vapor pressure during sintering. Diffusion of silver into ceramic
(mostly along the grain boundaries) limits the minimal thickness of the dielectric layers resulting in decreasing of
volumetric efficiency of capacitors.
The major challenge for the BME technology is nickel oxidation in air during sintering that results in a substantial
increase of resistance of electrodes. To reduce oxidation, high temperature operations (at ~1200 °C) are carried out
in reduced atmospheres. This results in generation of positively charged oxygen vacancies in the ceramic, increases
conductivity of the dielectric and causes IR degradation in capacitors with time of operation. To avoid the effects of
reducing environments and stabilize ceramic, a special dopants e.g. rare earth oxides Y2O3, Dy2O3, Ho2O3, and
Er2O3, are used. The dopans reduce concentration of oxygen vacancies and improve stability of capacitors during
life testing [2]. In addition, stability of BME MLCCs is improved by re-oxidation at temperatures below sintering
(~1000 °C) after firing of the parts. It is assumed that reoxidation of BME MLCCs is controlled by oxygen diffusion
along the Ni inner electrodes [23].
Diffusion and migration of Ag into dielectric layers from inner Ag or Ag/Pd electrodes might pose a problem for long-
term reliability. Silver is a material that is most susceptible to electromigration in the presence of moisture, and for
this reason, cracking of PME capacitors creates a higher risk of electrical failures compared to BME capacitors (see
section 5 of this report).

    2.3. Termination materials
After sintering, the end of a capacitor with exposed electrodes is dipped in a metal glass frit (thick film ink) consisting
of metal particles or flakes and doped borosilicate glass. This ink is then dried and sintered/fired to the ceramic body
allowing glass particles to fuse along contacts creating a sponge like structure and diffusing into ceramic to assure
adhesion between ceramic body and terminal metallization [24]. If manufacturing process is not optimized, the
interface boundary amorphous layer might crack during capacitors’ manufacturing or assembly thus increasing the
risk of failure. If termination firing temperature is below the optimal, not all internal electrodes form good
metallurgical contacts with terminations. Under environmental stresses during application, this might cause
intermittent electrical contacts resulting in sporadic changes in the value of capacitance and malfunctions of the
electronic system. The type and optimal amount of glass frit used in termination depends on the type of ceramic and
design of the capacitor.
The thickness and material of the glass frit affect the probability of cracking caused by thermal stresses associated
with soldering and/or temperature cycling [25]. Insufficient thickness of the base termination might increase the
proportion of MLCCs’ failures during wave soldering by several times. Experience shows that optimization of the
base terminal materials and processes improves substantially the robustness of capacitors and reduces risks of failures
during high humidity operations. The type of paste used might also affect the probability of IR failures in COG BME
capacitors after storage at normal conditions [26].
A silver-based frit is used for PME and a copper-based (sometimes nickel-based) frit is used for BME technology.
The copper-based frit is fired in oxygen-free atmosphere to avoid oxidation. Fig. 2.5 shows typical cross-sections of
terminations in PME and BME capacitors.




To be published on nepp.nasa.gov.                                                                                       12
After the termination has been sintered it is electroplated with a nickel layer to form a barrier and minimize dissolution
of electrodes and base metallization during soldering. A final step in forming terminations is plating with a tin/lead
solder for military or tin layer for commercial capacitors to assure solderability of the part.




                                                      a)                                                    b)
                         Figure 2.5. Terminations in BME (a) and PME (b) 50 V capacitors.
The porosity of the base termination and the presence of pinholes allow penetration of moisture through the terminals
of the part [24]. This can cause corrosion of copper or degradation of insulation resistance of the capacitor in the
presence of cracks that might create a path for moisture to short opposite electrodes. This degradation process might
accelerate in the presence of defects in the termination such as terminal-ceramic delamination or pinholes shown in
Fig. 2.6. Note, that MIL-PRF-123 considers acceptable pinholes of less than 130 µm and MIL-PRF-32535 reduces
these requirements to 80 µm for capacitors with sizes smaller than 0805. These pinholes not only transparent for
moisture, but can also trap contaminations and moisture for a long time thus enhancing the risk of corrosion.
Calculations have shown that the size of terminations affects the maximum principal stress in MLCCs [27].
Mechanical stresses in capacitors also depend on the thickness of nickel plating and process conditions [28].
Considering that CTE of nickel (13.4 ppm/K) is greater than that of ceramics (~9.6 ppm/K) and for both materials the
Young’s modulus is rather large, from ~ 100 GPa to 200 GPa, substantial tensile stresses might develop during
soldering conditions, thus enhancing metal/ceramic separation close to terminals. In some cases, failures of MLCCs
during temperature cycling have been attributed to increased stresses caused by nickel plating. The optimal thickness
of Ni barrier layers at the terminations is considered to be in the range from 2 to 6 µm. Thicker layers might increase
risks of cracking and delaminations and seal moisture and contaminations that could have penetrated inside the part
during initial stages of the plating process. Termination materials and geometry are important elements of capacitors’
design that affects the probability of cracking and failures [29]. The susceptibility to thermal shock failures is greater
for terminations with Ni barrier compared to Pd/Ag terminated chips.




                                                          a)                                                          b)




To be published on nepp.nasa.gov.                                                                                      13
                                                                               c)
Figure 2.6. Example of termination defects. a) delamination in a PME capacitor and pinholes in BME (b) and PME
                                                  (c) capacitors.
For non-magnetic capacitors that are often required by medical or special RF applications, nickel cannot be used as
the barrier layer and terminations are manufactured using Ag/Pd finishing. Capacitors with this type of terminations
are not recommended for soldering due to the leaching of silver into molten solder and should be attached by silver
epoxy. Also, a Cu barrier can be used instead of Ni on the top of Ag or Ag/Pd glass for the non-magnetic devices.
MLCCs with gold finishing are assembled using wire bonding at terminals. Gold electroplating might result in
excessive hydrogen generation, and reactions of hydrogen with palladium in PME MLCCs might cause delaminations
and cracking. The risk of hydrogen related delaminations is greater for PME compared to BME capacitors. A detailed
description of different types of terminations and acceptable methods of assembly can be found in manufacturers’
recommendations, e.g. [30, 31].

Commercial capacitors are typically compliant with the Restriction of Hazardous Substances (ROHS) regulations and
their terminations are manufactured using lead-free metals (typically pure tin) that are susceptible to growing whiskers.
For military and space applications, termination finishing with a Sn/Pb alloy having 3% lead minimum is required.
Replacement of pure tin with Sn/Pb finishing in commercial MLCCs can be achieved either by solder dipping into Pb
containing solder or by plating Sn/Pb layer on the top of the existing finishing and the following fusion (e.g., AEM
Inc. refinishing process). The latter process is less risky because avoids thermal shock stresses to the parts.

             •    Flexible terminations
Flexible terminations that are formed by addition of a conductive polymer layer between the base and Ni barrier (see
Fig.2.2) have been used for electronic boards’ assembly for more than a decade. What started as a commercial
technology to reduce failures related to flex cracking of MLCCs, is currently used for the advanced military and space
grade capacitors manufactured per MIL-PRF-55681 and MIL-PRF-32535. The major reason for popularity of this
technology is that flexible terminations reduce the stress that is transferred from the board to the ceramic body, and
possible cracks instead of propagating to the active area of capacitors are contained within the polymer [32].
Experience and testing show that introduction of flex terminations decreases substantially cracking of MLCCs during
soldering, handling, and field operations. Manufacturing experience shows that introduction of flexible terminations
practically eliminated field returns caused by flex cracking.
Temperature cycling tests of capacitors with flex terminations in comparison with regular termination parts soldered
onto PWBs showed a substantial improvement in reliability. Regular termination MLCCs started failing after 1000
cycles, whereas there was no failures detected in the flexterm capacitors after 3000 cycles.
Using conductive polymers in terminations improves substantially results of the drop testing. TDK data [33] show
that capacitors with soft terminations had no cracking failures after 10,000 drops (dropping from 1 m at a frequency
of 16 times per min), whereas a regular product had 30% failures after 2000 drops. In addition, after the drop testing
the parts passed humidity load test (1000 hours at 85 ℃ and 85% RH under rated voltage) thus indicating absence of
hidden cracks.
In BME capacitors with flex terminations operating in humid environments silver dendrites can grow along the surface
of ceramics (see Fig. 2.7). Although the risk of increased metal migration along the cracks and failures caused by the
growth of dendrites associated with silver-epoxy terminations exists, the benefits of reducing the probability of


To be published on nepp.nasa.gov.                                                                                     14
cracking apparently prevail. As a result, the overall quality and reliability of BME capacitors with soft terminations
is increased and field failures reduced.




 Figure 2.7. Silver dendrites on the surface of a cross-sectioned BME flex-termination capacitor after low-voltage
                                         humidity testing at 1.5 V (HSSLV).

    2.4. Design
Most cracks in MLCCs caused by deformation of PWBs during assembly, handling or testing are initiated at the
surface close to the terminal areas of capacitors (see Fig.2.8). These cracks might affect reliability of the parts if they
are reaching active area of capacitors and cross opposite electrodes. For these reasons, parts with thicker cover plates
and larger end margins are more resilient to cracking-related failures [34].

Existing requirements for margins in military specifications are similar to EIA-469 DPA standard [35] that has
different margin and cover plate thickness limits for different groups of capacitors. The EIA-469 requirements for the
margins are designed to provide sufficient electrical insulation, address mostly quality of the as-manufactured parts
and do not consider cracking-related issues.

Thin dielectric MIL-PRF-32535 follows EIA-469 and specifies different limits for parts with VR above 50 V, below
6.3 V, 16 V and 25 V. For example, the thickness of cover plates should exceed 0.003” (75 µm) for capacitors rated
to more than 50 V and can be as low as 0.001” (25 µm) for capacitors with VR ≤ 6.3 V. However, for capacitors
intended for automotive industry, manufacturers have stricter requirements for the margins. A minimal size for
margins and cover plates for commercial MLCCs manufactured by AVX is 75 µm, it is 100 to 125 µm for automotive
grade capacitors and 110 to170 µm for space application [36, 37].

To mitigate risks of cracking-related failures, special designs of MLCCs have been developed. For low capacitance
values, KEMET, similar to other manufacturers, offers the Floating Electrode (FE-CAP) capacitors (see Fig. 2.8.d).
This design is also known as a Serial Cap design [38]. For mid capacitance values, the Open Mode solution that has
enlarged end margins that create safe zones on both ends of the capacitor (see Fig.2.8.e). Other manufacturers, e.g.
TDK [33], are using similar design approaches to reduce failures caused by cracking (see Fig. 2.9).

Various designs of MLCCs that have been suggested by manufacturers to decrease the probability of flex cracking
can be summarize as following:
• Flexible termination.
     Application of relatively soft and/or tear-away termination layers made of conductive polymers (see Fig. 2.2)
     reduces the stress in ceramic and restricts flex cracks within a safe zone away from the body of the MLCC.
• Fail open design (Fig.2.8.e).
     End margins are widened, so if a crack occurs, it does not cross electrodes with opposite polarity, and thus
     prevents short-circuit failures.
• Floating electrodes (Fig. 2.8.d).
     Two capacitors connected in series within an individual case size, so the probability of shorting cracks is reduced
     substantially.
• Clip-on lead frame.
     Attachment of J-shaped leads see Fig. 2.9) mechanically decouples the MLCC from the PWB and allows for some
     stress relief.

To be published on nepp.nasa.gov.                                                                                       15
                                                                                                                       c)



                                                                                                                       d)

                                     a)                                      b)
                                                                                                                       e)
 Figure 2.8. Soldering related cracks in MLCCs and schematics of a standard part (c), floating electrode capacitor
 (d), and Open Mode design (e) [38]. Yellow and blue lines in (c-e) represent electrodes with different polarity.




                   Figure 2.9. MLCC designs with flex crack countermeasures used by TDK [33].
A combination of floating electrode and flex termination design (e.g. a TDK Dual-Fail-Safe, Mega Cap design [39])
allows to reduce the risk of failures even further. This design has been proven highly reliable, and no cracks developed
in the parts after 3000 thermal shock cycles.
Obviously, the cost of improved reliability of MLCCs with increased margins or floating electrodes is a lesser
volumetric efficiency. For this reason, flex termination is likely the most efficient cracking mitigating measure.
Typically, capacitors having maximum capacitance values for a given case size and rated voltage have smaller margins
and hence, pose a higher risk of failures. For this reason, for a given rated voltage and case size, the use of parts with
maximum available value of capacitance is not recommended.
Since operating frequencies of contemporary microcircuits have increased substantially, new designs of MLCCs that
are used in a close proximity to the microcircuits to improve their performance, suppress noise, and stabilize operation,
have been developed. Fig. 2.10. shows an example of low-inductance capacitors used in a package of XILINX FPGA.




To be published on nepp.nasa.gov.                                                                                      16
                                    a)                             b)                                        c)
 Figure 2.10. Overall external (a) and internal, after lid removal, (b) views of a XILINX VIRTEX-4 FPCA showing
IDC-type ceramic capacitors mounted inside the package. Figure c) shows a cross-section of the termination area of
                                 IDC capacitors with dielectric thickness of ~2 µm.
The equivalent series inductance, ESL, is an important parameter of capacitors that determines their efficiency during
operation at high frequencies. Fig.2.11.a shows an equivalent circuit of MLCCs operating in the RF range. The idea
of low ESL designs of MLCCs is in reduction of the length of the effective AC current flow path (see. Fig. 2.11.b).
ESL values can be decreased several times simply by reversing the width and length of capacitors. This change in the
design might potentially increase the susceptibility of the parts to cracking, first, by creating of a more rigid solder
connections, and second, because ceramic areas close to terminals have a higher level of internal mechanical stresses
and the larger this area is, the greater the probability of having a crack.
A more drastic reduction of ESL, to the picohenry levels is achieved by IDC and ball grid array vertical electrode
designs. Figure 2.11.c shows examples of designs of low-ESL MLCCs. The effect of design changes on the
susceptibility to cracking requires additional analysis; however, some part types, and in particular, IDC capacitors,
have passed extensive testing by XILINX and has been successfully used for more than a decade in FPGAs.




                                         a)                                                                       b)




                                                                                                 c)
Figure 2.11. Equivalent circuit of a capacitor at high frequency(a) a schematic of the AC current flow in capacitors
                  (b), J.Marshall [37], and types of low inductance MLCCs, R.Demko (c), [20].
Stacked capacitors are manufactured by attaching leads to several MLCCs connected in parallel and arranged
vertically one on the top of other (see for example Fig. 2.12a). This design allows for a substantial increase of
capacitance at the same footprint and reduces the size of the circuit board. The lead-frame decouples mechanically
capacitors from the board thus reducing microphonic noise and destructive effects of board flexing. Although the

To be published on nepp.nasa.gov.                                                                                      17
lead-frame is attached using a high-temperature solder, the process is thoroughly controlled by the manufacturers that
reduces the risk of cracking. However, shallow cracks under the terminations that are typical for most MLCCs occur
also in stacked capacitors (Fig. 2.12b and c) and when the thickness of the cover plate is not sufficient, these cracks
can cause life test failures as shown in Fig. 2.12d. When moisture and contaminations penetrate inside the crack, the
electric field between the tip of the crack and top electrode is increased, and with time, this might cause failures
according to the time dependent dielectric breakdown (TDDB) mechanism (see Fig. 12.2e).




                         a)                                        b)                                               c)




                                                              d)                                                  e)
   Figure 2.12. An overall view of a stacked capacitor (a), cross-sectioning showing a thin cover plate (b) and a
 shallow crack under the termination (c). Fig. d shows cross-sectioning of a capacitor that failed during life testing
                             and (e) is a schematic of the TDDB mechanism of failure.

             •     Laser marking
Due to a small size, MLCCs are usually unmarked. However, some customers, prefer marked capacitors, so that they
can have assurance that the correct component has been used [40]. A laser marking that is often used for plastic parts
might cause damage to a ceramic capacitor in case the laser power level is above optimal (see Fig. 2.13.). Different
types of capacitors use different materials and have different thickness of the cover layers and require different levels
of the power setting to avoid cracking.




                 Figure 2.13. A capacitor damaged due to excessive power of laser marking machine.




To be published on nepp.nasa.gov.                                                                                      18
3. Testing and quality assurance
All MLCCs are manufactured using similar technological processes and materials and the difference between
commercial and military or space grade capacitors is mostly in the design rules, the level of consistency of used
materials and processes, and in the approach to quality assurance (QA) or amount of testing. For example, the
thickness of the dielectric layers is typically much greater for military capacitors, and types of materials that are fixed
for military can be changed for commercial capacitors. Stability of design and materials is important to assure
consistency of characteristics and reliability of the parts, but retards innovations and improvements of performance.
Approaches for quality assurance of commercial and military capacitors are substantially different. Quality assurance
of mass production commercial capacitors is based on the build-in-design approach and extensive use of the Statistical
Process Control (SPC) system [41, 42]. SPC is a data-driven methodology for quality analysis and improvement that
is essentially a preventive activity performed in real-time during the manufacturing process. Military specifications
also require SPC system to be used, but it is not considered a major element of QA, and inability to make in-process
improvements reduces substantially its efficiency. Instead, QA for military capacitors is based on extensive
inspections and testing of the parts. As stated by Dan Friedlander [42] “SPC targets failures prevention, burn-in
(testing) targets failures detection”.
The first military specifications had been developed before the mass production era that was driven by commercial
electronics market, and historically played an important role in improving quality of electronic components.
Obviously, statistics was not effective without automotive process control and for low production volumes, so QA in
military specifications relied heavily on testing and inspection.
Historically, majority of MLCCs used in space applications by NASA have been manufactured and tested according
to MIL-PRF-123 (CKS-style) and MIL-PRF-55681 (CDR-style). In 2017 a specification for thin dielectric ceramic
capacitors that includes BME-type capacitors, MIL-PRF-32535 (M32535-style) has been developed. In addition,
USA, EU, and Japan space agencies have developed their own specifications (source control drawing, SCD) that
extended the range of capacitors suitable for space applications: S-311-P-828, S-311-P-838 by NASA/GSFC [43, 44],
ESCC-3009 by ESA [45], and QTS-2040 by JAXA [46, 47].
Capacitors developed for automotive industry are used sometimes in low-level space projects because these parts are
manufactured to a higher quality standards compared to a general use commercial capacitors. Quality of these parts
should be in compliance with AEC-Q200 requirements [48]. However, this document describes only general
specifications for passive components, and the parts that are actually used by car manufacturers might have additional
requirements detailed in non-disclosed documents.
All mentioned above documents use a variety of tests and inspection procedures that generally can be divided into
three groups: (i) screening gr.A, (ii) screening gr.B and (iii) qualification. Screening gr.A inspections and testing is
carried out for 100% of samples in each lot and have a purpose of removing parts with manufacturing defects from
the population. Burning-in is considered a major element of the screening because it supposed to prevent early, defect
related (infant mortality) failures.
Screening gr.B is carried out using samples from each lot (sometimes called lot acceptance testing, LAT), and its
purpose is to ensure that the manufacturer continue production of parts that conform to the specification. Qualification
testing is carried out periodically using samples from some lots to confirm the required quality level for a given type
of production. Obviously, gr.A screening can reveal manufacturing defects only, and the robustness of the parts
towards assembly, and post-assembly stresses should be addressed by gr.B screening and qualification tests.
Note that the notion of the lot of parts for commercial components is not defined as strictly as for military components.
However, considering that MLCCs are produced by huge batches and the amount of a certain type of capacitors used
in a space project is relatively small, the probability of having parts from different batches is low.

    3.1. Comparative analysis of specifications
Tables 3.1 and 3.2 give a comparison of screening and qualification tests used in different specifications. In all
documents, except for MIL-PRF-55681, there is a ban on use of pure tin for terminals’ finishing. MIL-PRF-55681
has an option with pure tin, but warns against the possibility of whiskers growth. Some specifications limit the


To be published on nepp.nasa.gov.                                                                                       19
thickness and dielectric constant of the ceramic layers and types of electrodes. For example, MIL-PRF-123 does not
allow nickel electrodes and flexible terminations, limits dielectric thickness (d) to 0.8 mil, and the dielectric constant
to 3000. In NASA/GSFC requirements, the values of d depend on the type of capacitors and can be as low as 0.28
mil (~7 µm), whereas JAXA specification QTS-2040 limits d to 3 µm. The latest military specification, MIL-PRF-
32535, does not have limits for the dielectric thickness at all. Destructive physical analysis (DPA) is required by all
specifications except for MIL-PRF-55681.

              •   Military specifications
Ultrasonic inspection when used for fully manufactured capacitors is limited to areas not covered by terminations, and
likely for this reason, MIL-PRF-123 requires this inspection before the terminations are formed. However, formation
of terminations might create a substantial stress to the capacitors and result in cracking, so the latest specification,
MIL-PRF-32535, requires acoustic examinations before and after formation of terminations. Note that MIL-PRF-
55681 (CDR-style capacitors) does not require ultrasonic inspection that might be the reason of several recent failures
in space projects that were attributed to the presence of delaminations and cracks.
Every lot manufactured per MIL-PRF-123 and MIL-PRF-32535 specifications requires voltage conditioning or
burning-in (BI) at two times rated voltage and 125 ºC for 168 hours minimum. BI requirements in MIL-PRF-55681
are somewhat relaxed: (i) the duration of testing is 100 hr, and (ii) the temperature might be less than 125 ºC and
depends on the maximum operation temperature specified for the part. MIL-PRF-55681 also does not require DPA
and thermal shock prior to BI. Considering high temperature processes during formation of terminations, the
efficiency of temperature cycling before BI for unmounted capacitors is not clear.
Reliability of military grade capacitors is determined during accelerated life testing, typically at 2VR and 125 ºC. The
failure rate (FR) for MLCCs is usually expressed as percent failures per thousand hours of test and indicates a
maximum failure rate at operating conditions that is determined in the assumption of random failures (exponential
distribution) [49]. To verify reliability level of 0.001%/1000hr with 60% confidence 91.6×106 unit-hours of testing
at operating conditions (125 ºC and rated voltage) should be accumulated without failures (e.g. 91,600 samples during
1000 hours). The same FR level at 90% confidence would require testing of 230×106 unit-hours. To accelerate the
testing, MIL-PRF-123 and MIL-PRF-55681 allow increasing test voltage two times that assumes 8X acceleration.
However, even with this acceleration the testing might last more than half a year.
Capacitors manufactured to M32535 specification are not established reliability parts. Instead, two product quality
levels are defined: standard reliability (M level) and high reliability (T level) that is intended for space applications.
Both types are manufactured and tested similarly and the quality level is determined by (i) duration of life testing, and
(ii) most importantly, by carrying out life testing on each lot of capacitors. Test duration for the T-level products is
4,000 hours for qualification and 1000 hours during gr. B screening testing, whereas qualification test for M-level
capacitors requires 1,000 hours.
A sample size that is used for life testing varies from123 for MIL-PRF-123 and MIL-PRF-32535 to 25 for MIL-PRF-
5681. Also, some lots might not be tested at all (e.g. CDR capacitors manufactured to MIL-PRF-55681 specification)
and they are qualified by similarity with samples from other lots representing manufacturing process over a certain
period. Considering that only a small proportion of capacitors might have defects that pose reliability risks, the
efficiency of life testing to reveal lots with defects, and cracks in particular is limited. This efficiency is even lower
when parts are tested in fixtures or soldered onto boards at conditions that are different compared to the actual
assembly of flight cards.




To be published on nepp.nasa.gov.                                                                                      20
                                       Table 3.1. Requirements for screening of low-voltage MLCCs
 Type                                 MIL-          MIL-        MIL-                                        ESA             JAXA
                                                                            S-311-P-      S-311-P-
  of                    Test         PRF-          PRF-        PRF-                                        ESCC             QTS-
                                                                              829           838
 test                                123, T        55681      32535, T                                     #3009           2040/M
                                                                             PME, no
                                                                                          BME, X7R,                        Sn/Pb by
                                       PME,                                  pure tin,
                                                                                           d ≥ 0.28                       solder dip,
                                    d ≤ 0.8 mil,                            d(PN), Kmax                   Type I and
            Scope/limit                                       No pure tin                  mil, N ≤                        d ≥ 3um
                                    no pure tin,                              =4000,                     II dielectrics
                                                                                          300, Sn/Pb                      2000 < K <
                                    Kmax= 3000                               X7R; 100
                                                                                            plated                           4000
                                                                             for NPO
                         C, DF        100%          100%        100%           100%         100%            100%             100%
                       IR @25C        100%          100%        100%           100%         100%            100%             100%
                      IR@125C         100%         Sample       100%           100%         100%           sample            100%
                     DWV/voltag       2.5 to                    2.5 to
                                                   2.5×VR                    2.5×VR        2.5×VR          2.5×VR           2.5×VR
                        e proof       4×VR                      4×VR
                                                                                                                          4hr/2VR/85




   Screening, gr.A
                                    20c -55 to                20c -55 to    20c -55 to    20c -55 to
                      TS and                                                                                              (in-process)
                                     +125C,         100hr      +125C,        +125C,        +125C,
                      Voltage                                                                              96hr at         20c -55 to
                                    168-264hr      2×VR, at   168-264hr     168-264hr     168-264hr
                     conditionin                                                                         2×VR, Tmax          +125C,
                                      2×VR,          Tmax       2×VR,         2×VR,         2×VR,
                         g                                                                                                21hr@ 3VR,
                                      125C                      125C          125C          125C
                                                                                                                              125C
                        PDA*            3%           8%          5%            5%             5%              5%               -
                                                              Before and       100%          100%
                                       100%
                     Ultrasonic                                  after       before or     before or
                     inspection
                                       before         -       termin. for      after         after             -             100%
                                    termination
                                                              size ≥0805    termination   termination
                       Visual
                                      100%         sample       100%          100%          100%            100%            20 pcs
                       exam.
                        DPA                           -
                                                                 100c,         100c,
                                    100c.,1000                                            20c, 1000hr                     25(0) pcs,
                     TS and Life                                1000hr        1000hr
                        test
                                     hr, 2×VR,        -         2×VR,         2×VR,
                                                                                            2×VR,              -          per JAXA-
                                       125C                                                  125C                         QTS-2040
                                                                 125C          125C
                                     20c per                  12(0) pcs.,
                     THB/moistu                                              20c per      85C, 85%                        12 pcs, 20c
                                      M202                    85C, 85%
                          re                          -                       M202        RH, 96hr,            -           per M202




   Screening, gr.B
                                    TM106, 10c                RH, 96hr,
                      resistance                                             TM106           VR                             TM106
                                      at 50V                      VR
                                                                VBR ≥                      30(0) pcs,
                     Breakdown                                                                                            As a part of
                                         -            -        6×VR or          -            VBR ≥             -
                       voltage                                                                                            evaluation
                                                                1200V                        6×VR
                                                                                            6(0) pcs,
                                                                                              M202                          4 pcs.
                     Resistance                                                            TM210, J,                      Solder dip:
                     to soldering        -            -           -             -         Infared/con          -           +260°C,
                         heat                                                             vection but                     10s. M202
                                                                                            1 cycle,                      TM210, B.
                                                                                           within gr.B
                      HSSLV**                         -           -                            -
                      PRVT***            -            -           -             -                              -               -
*PDA = percent defectives allowable
**HSSLV = humidity steady state low voltage test that is carried out at 1.3V for 240h at +85°C and 85%RH,
typically using 12 samples.
***PRVT = Process Reliability Verification Test.




To be published on nepp.nasa.gov.                                                                                                       21
                                     Table 3.2. Requirements for qualification testing
                     MIL-PRF-
                      123, T           MIL-PRF-           MIL-PRF-          ESA ESCC          JAXA QTS-
       Test                                                                                                   AEC-Q200
                                        55681             32535, T            #3009             2040/M

                                                                                                 18 pcs on
                                                         -55C to +125C
                       -55C to           -55C to                                                alumina or
                                                          mounted, 100      10 cycles Tmin                    77(0) 1000c -
        TS          +125C, 100 c,     +125C, 5 c, 18
                                                          c (T) and 5c         to Tmax
                                                                                                FR4, -30 to
                                                                                                              55 to +125C
                      186 pcs              pcs                                                   +100°C x
                                                          (M), 123 pcs
                                                                                                  1,000cy
                                                                                                  123pcs.
                                                                              (20 or 40)
                    123(1) 1000hr      25(1), 2000hr     123(1) 4000hr                            1.5VR,      77(0), 1000hr
   Life testing      2×VR, 125C        at Tmax, 2×VR      2×VR, 125C
                                                                            2000hr 2×VR,
                                                                                              4,000h@+125°      125C, VR
                                                                                125C
                                                                                                     C
                                                                            Within gr.B (10
                                                                              TS cucles                           (for PME
     HSSLV                                                      -            before the
                                                                                               Within gr.B
                                                                                                                  only)
                                                                               testing)
   THB/moistu                                             22(0), 85C,                                         77(0), ), 85C,
                    20c per M202       20c per M202
        re             TM106              TM106
                                                           85% RH,                -                 -           85% RH,
    resistance                                            1000hr, VR                                           1000hr, VR
                                                             22(0) pcs,
                     12(1) pcs,       9(1) pcs, M202                                            4(0), M202    30(0), M202,
   Resistance                                             M202 TM210,
                    M202 TM210,           TM210, J,                                               TM210,       TM210, D.
                                                                 J,
   to soldering     B, solder dip,    Infared/convec
                                                         Infared/convec           -           cond.B Solder   Wave solder,
       heat         230C, 10sec,       tion reflow but                                         dip: +260°C,     260C, no
                                                          tion reflow but
                        gr.C            1 cycle, gr.C                                               10s.         preheat
                                                           1 cycle, gr.C
                                          12 pcs.
                                                         12 pcs, 2mm                              1 mm           2mm
   Flex testing           -                2mm
                                                          deflection              -             deflection     deflection
                                         deflection
         *The combination of the mounting process and 1 heat cycle is considered to be equivalent to 2 heat cycles.
Life testing of small size thin dielectric IDC style X7S BME capacitors manufactured to MIL-PRF-32535 showed that
these parts couldn’t pass testing and fail after 4000 hr at 125 ºC, 2VR. This was attributed to a higher acceleration
factors compared to X7R capacitors with thicker dielectrics. For these parts, the exponent n in the Prokopowicz and
Vaskas equation is in the range from 4.4 to 4.9 and Ea is between 1.2 and 1.6 eV, which is greater than what is usually
assumed for PME capacitors (n ~ 3). For this reason, life testing for IDC capacitors is carried out at 1.5VR [37],
which is consistent with conditions used for thin dielectric capacitors by JAXA [47].
Some X7S thin dielectric small size capacitors had failures when tested at 85 ºC 85% RH for 1000hr at rated voltages.
This might be due to cracks formed during manufacturing or developed during assembly or testing. For these parts,
requirements in MIL-PRF-32535 were also reduced, and instead of THB conditions (85 ºC and 85% RH), capacitors
are tested at 40 ºC and 95% RH that are apparently less stressful. This relaxation of requirements would be reasonable
if failures occur when test conditions exceed a certain threshold. In this case, no failures would be expected at normal
operating conditions. Unfortunately, there is no proven predictive models for electrical failures of MLCCs with cracks
in humid environments, and additional analysis is necessary to understand the reason of parts failures at 85 ºC and
85% RH.

              •   NASA/GSFC specifications
NASA/GSFC S-311-P-829 and -838 specifications (see Table 3.3.) describe requirements for extended range
capacitors for space applications. Specification P-829 is related to precious metal and rigid terminal capacitors,
whereas P-839 to the BME MLCCs manufactured with flex terminations only.
For some reasons, in both specifications DPA is required before terminations are formed. Considering that most
cracks are associated with terminations, this excludes an important, reliability related area of MLCCs and allows
inspections to be carried out by manufacturers only.
In spite of different materials and technologies used for PME and BME capacitors and differences in their
performance, both specifications have the same requirements for AC and DC characteristics. Requirements for gr.A
are also similar, but requirements for gr.B screening differ substantially. In particular, HSSLV testing in P-829 is


To be published on nepp.nasa.gov.                                                                                              22
replaced by TBH as in MIL-PRF-32535. In addition, similar to MIL-PRF-32535, P-838 has requirements for flex
testing and resistance to soldering heat that are absent in P-829.
                                         Table 3.3. NASA/GSFC specification
 Requirement                        S-311-P-829 rev.J (2017)                        S-311-P-838 rev A (2017)
 Electrode                          PME only                                        BME only
 Voltage range                      5V to 100V                                      16 to 100
 Dielectric type                    NPO and X7R                                     X7R
                                    100% prior to termination (as in M123) or
 Ultrasonic examination             after, at the Mfr. option
                                                                                    Same as P-829
                                     a) Ag/Pd alloy ( type M in M123)
 Termination                         b) Ni barrier with Sn/Pb plating (type Z)      Flexible, Ni barrier and Sn/Pb plating
                                     c) Ni barrier with Au plating (type G)
 Size                                0402 to 2225                                   0402 to 1812
                                    1 mil for 100V, 0.8 mil for 50V, down to 0.25
 Dielectric thickness               mil at lower voltages
                                                                                     0.28 mil minimum for VR<50V

 Max. dielectric constant           4000 for X7R and 100 for NPO                                          -
                                                                                    A special procedure that evaluates
 Process Reliability                                                                acceptance (reliability) of the parts based
                                    Not required
 Verification Test (PRVT)                                                           on the number of grains in a dielectric
                                                                                    layer
                                                                                    SEM examinations and average grain size
 Dielectric microstructure          Not required
                                                                                    measurements (as a part of PRVT)
                                    1010 ohm or 100 ohm_F at 125C
 Insulation resistance              1011 ohm or 1000 ohm_F at 25C
                                                                                    Same as P-829
 Dielectric Withstanding
                                    2.5xVR per MIL-STD-202, TM 301                  Same as P-829
 Voltage (DWV).
                                    X7R: ≤7.5% for VR ≤ 10V; ≤ 5% at VR=16V,
                                    ≤ 4% at 25V, ≤ 3.5% at 50V, and ≤ 2.5% at       ≤ 5% at VR=16V and 25V, ≤ 2.5% at 50V
 Dissipation factor                 100V                                            and 100V
                                    NPO: ≤ 0.15% for all VR
 Percent Defective                                                                  < 5% after voltage conditioning and IR
                                    < 5% after voltage conditioning
 Allowable (PDA).                                                                   measurements at 125C
                                    DPA (pre-termination)
                                    Gr.A inspection includes:                       DPA (pre-termination)
                                    -Thermal shock (20 c -55C to +125C)             Gr. A is similar to P-829
                                    -Voltage conditioning (≥ 168hr at 125C, 2VR;    Gr.B. 45 pcs for d ≥ 0.8 mil and 125 pcs
                                    the number of failures detected during the      for d < 0.8 mil.
                                    last 48 hours of test < 0.1%, or one piece.)       B1: – same as P-829
 In-process inspection              Gr.B inspection includes:                          B2: HSSLV testing is replaced with TBH
                                      B1: TS (100c -55C to +125C) and Life test        (96hr at VR, 85C, 85% RH)
                                      B2: HSSLV per M123                               B4: Resistance to soldering heat
                                      B3: Voltage Temperature Limits and               B5: Shear stress
                                      Moisture resistance test per M123 (for           B6: Breakdown voltage test
                                      parts larger 0805)                               B7: Board flex test
                                    No resistance to soldering heat!

A major element of gr.B inspection in P-838 that makes it different from all other military and space specifications is
the Process Reliability Verification Test (PRVT). A theory behind this test is that the ratio of dielectric thickness to
the grain size is the most important parameter of BME capacitors that defines their reliability [50]. High reliability
capacitors are recommended to be selected based on an empirical criterion:
                                                                      𝑁𝑁
                                                        𝑟𝑟̅ 𝛼𝛼
                                       𝐹𝐹𝑡𝑡 = 1 − �1 − � � � < 0.00001
                                                        𝑑𝑑
where Ft is the probability of failure, 𝑟𝑟̅ is the measured average grain size, d is the average dielectric thickness, N is
the total number of dielectric layers, α is a constant that is assumed to be 5 for capacitors with rated voltage exceeding
100 V and 6 for capacitors with rated voltage below or equal 100 V.
Multiple studies have shown that the grain size of ceramic materials affects characteristics and reliability of MLCCs.
However, other factors, e.g. type and level of doping, the thickness of the shell, homogeneity of grain distribution,
and built-in mechanical stresses are a few other factors that have a strong effect on quality and performance of


To be published on nepp.nasa.gov.                                                                                            23
capacitors. For this reason, selecting MLCCs, and especially calculating their reliability based on the grain size might
be misleading. In any case, this criterion is not relevant to the cracking related failures in MLCCs that constitute the
majority of the observed failures.

              •   ESA and JAXA specifications
ESA Generic Specification ESCC-3009 (2017) [45] defines general requirements for qualification, procurement, and
delivery of types I and II MLCCs for space applications. Specific requirements for the parts are in the detailed
specifications available at the ESC web site: https://escies.org/specfamily/view. In general, these requirements are
close to those used by NASA, but a substantial deviation exists in the use of ultrasonic inspection and burn-in
conditions. ESCC-3009 does not require ultrasonic inspection and requirements for burning-in are limited to 96 hours
at 2VR and maximum operation temperature (similar to MIL-PRF-55681) that is determined in the detailed
specifications. Somewhat more flexibility compared to the military specifications exists for the operating life test
temperature and the range of temperatures during thermal shock testing. Both tests are carried out at temperatures
defined in detailed specifications instead of the standard conditions per military specifications: 125 ºC for life testing
and from-55 ºC to +125 ºC for thermal shock.

ESA employs different quality assurance systems for ESCC qualified and non-qualified parts. Periodic testing (every
2 years, that is similar to gr.C or qualification testing) is required for qualified components only. The lot validation
testing (corresponds to screening gr.B) for these components is not required, but can be requested in the purchase
order.

The Japanese system for selection and QA of MLCCs for space applications benefits substantially from the extensive
market for automotive components. Giants of MLCC manufacturing (Murata, TDK, et al.) have produced billions of
capacitors for automotive industry for more than two decades and have great reputation for high quality and reliability
of their products. Automotive grade BME capacitors are used as the base for MLCCs selected for space systems [51].
The selected capacitors are processed by solder dipping to replace pure tin finishing with Sn/Pb solder, ultrasonic
inspection, and are up-screened by burn-in within gr.A inspections [52]. Periodically, the parts are verified by the
quality conformance inspection (QCI) that in some aspects is more stringent than NASA requirements. Considering
that capacitors per QTS-2040 can have dielectric thickness down to 3 µm, life testing is carried out at 1.5VR instead
of 2VR that is typical for military standards.

Additional information necessary for better understanding of the test requirements, parts selection, equipment design,
assembly and handling is detailed in JAXA-ADS-2040/M105 [47]. Life testing of 123 samples at 125 ºC and 1.5VR
for 4000 hours can assure S-level FR (0.001%/1000HR) at room temperature. Voltage acceleration of this testing is
assumed to follow 4.5 power law (n = 4.5), and temperature accelerates testing by the 10°C rule. To further reduce
the risk of degradation and failures during applications, the parts are deratad to 50% of the rated voltage specified by
manufacturers, and maximum operation temperature for some part types is limited to the range from -55 °C to +75
°C.

Additional testing to assure reliability of capacitors includes a combination of the thermal shock with the Pressure
Cooker Bias Testing (PCBT) [47]. The parts (23 pcs) are mounted onto an FR-4 printed wiring board (PWB) with
the thickness of 1.6 mm and subjected to 2000 TS cycles from -55 °C to +125 °C (temperature transition time is less
than 5 min.). Following TS, the parts are tested by PCBT at +125 °C, 95%RH, 2 atm pressure, and rated voltage for
144 hours. This test is sensitive to the presence of cracks, but in the presented example, small cracks that were found
during visual inspection in one capacitor after TS did not reach internal electrodes and the insulation resistance during
PCBT stabilized at more than 1MΩ. This confirms that the reliability of the capacitor was not affected by small
cracks.

In addition to a regular TS and humidity testing, an immersion cycling is carried out for special cases. During this
testing 18 pcs are subjected to a combination of TS and immersion cycling. Capacitors soldered onto an alumina
substrate are stressed by 250 cycles between -55 °C and +125 °C, and then tested per MIL-STD-202 TM104, cond.
B: two immersion cycles between a hot (65 °C) and cold (25 °C) baths with salty water (saturated with NaCl). Passing
this test gives assurance that the parts soldered onto ceramic substrates will not form cracks and can operated reliably
even under severe environmental stresses.

To be published on nepp.nasa.gov.                                                                                      24
             •    Automotive industry specifications
Automotive Industry Council, AEC-Q200, specification defines qualification requirements for passive components
including MLCCs. It does not call for ultrasonic inspection and HSSLV testing and does not require burning-in and
life testing for each lot of capacitors. AEC-Q200 does not describe screening procedures at all, but does not relieve
the supplier of any additional requirements needed by the customers. In many cases, parts used in cars are built and
tested to SCDs that have detailed specifications for S&Q. For some applications, IR measurements are required at
180 ºC and life testing for the under the hood parts is carried out at 2VR and 150 °C for 2000 hours.
AEC-Q200 describes only the minimum required stress tests and additional testing and analysis working in
cooperation with capacitors manufacturers is often used to assure adequate quality parts for cars by using an
appropriate mixture of qualification methodologies including step-stress testing, application-specific tests, physics-
of-failure approaches, sequential stress tests, etc.
An example showing the difference of Murata requirements for auto (GCM series) and standard (GRM series) MLCCs
is shown in Table 3.4 (https://www.murata.com/en-us/support/faqs/products/capacitor/mlcc/char/0004). Note, that
MLCCs manufacturers are often trying to demonstrate that their product can exceed the AEC-Q200 requirements (e.g.
thermal shock is not required per AEC-Q200), and different manufacturers might demonstrate their compliance to
AEC-Q200 in different ways. In addition, AEC-Q200 does not specify acceptable variations of characteristics of the
parts after environmental stresses and these requirements are presented in the SCDs.
            Table 3.4. Quality requirements for automotive industry and general purpose Murata MLCCs

   Test                                          GCM (AEC-Q200)                          GRM (standard)
   Temperature cycle                                 1000 cycles                             5 cycles
   Thermal shock cycle                                300 cycles                                 -
   THB                                        85 C, 85% RH, VR, 1000hr               40 C, 90% RH, VR, 500 hr
   HSSLV                                               1000 hr                                   -
   High temperature load (life)                        1000 hr                               1000 hr
   Retention at high
                                                        1000 hr                                   -
   temperature (storage)
Automotive parts are built using more aggressive design rules compared to military MLCCs. Also, automotive
industry requirements are more flexible in selecting test conditions compared to the military specifications and allow
for some process and materials’ changes. For example, IR can be measured at voltages much greater than VR, and
the test voltage during the dielectric withstanding voltage (DWV) test can be increased to (6-10)×VR compared to
2.5×VR in military specifications. In some cases, humidity testing is carried out on mounted onto PCBs parts at 85
°C and 85% RH and voltages greater than VR (up to 2 times).

    3.2. Qualification procedures and cracking problems in MLCCs
Soldering and post-soldering stresses might generate cracks in MLCCs, and for this reason, reliability of capacitors
soldered onto PWBs and loose parts might differ substantially. Majority of MLCCs are used after soldering, so
simulation of the assembly conditions should precede any environmental tests, and it is imperative that the QA system
for MLCCs would address properly issues related to soldering.
The probability of cracking after soldering depends on the substrate material. For example, due to the differences in
CTEs between the ceramic material and substrate, tensile stresses develop in MLCCs (CTE ~ 10 ppm/ºC) after
soldering onto alumina boards (CTE ~ 7 ppm/ºC). These stresses were responsible for many observed failures in
ceramic chip capacitors mounted on alumina substrates back in 80th [9]. Temperature cycling testing between -55 ºC
and +125 ºC showed that proportion of failures is substantially greater for capacitors mounted onto alumina compared
to FR4 boards [25]. Contrary to alumina substrates, FR4 or polyimide PWBs have a greater CTE (~17 ppm/ ºC) that
should result in increasing compressive stresses in the parts. Considering that the compressive strength of ceramics
is more than ten times greater than the tensile strength, the probability of cracking after soldering onto polymer boards
should be substantially less compared to ceramic boards.



To be published on nepp.nasa.gov.                                                                                     25
Although soldering related stresses cannot be ignored in the quality assurance of MLCCs, most military specifications
do not address mounting conditions properly. For example, MIL-PRF-123 does not specify mounting before
qualification testing and MIL-PRF-55681 allows mounting the parts on a suitable substrate (e.g., 96 percent alumina
or FR4 glass epoxy) when specified in the test procedures, but does not have mounting requirements for life or HSSLV
testing. MIL-PRF-32535 requires mounting onto an FR4 board before TS and life testing, whereas mounting for
humidity testing is optional. GSFC specifications S-311-P-829 and P-838 do not have mounting requirements at all.
Even when mounting conditions are specified, there is typically a warning that “the substrate and mounting process
shall be such that it will not be the cause of, nor contribute to, failure of any test for which it may be used.” The
interpretation of this warning might be that only tests that did not result in failures are valid. Otherwise, the parts
might have been abused during soldering. However, it is reasonable to assume that high quality MLCCs should sustain
possible deviations from an ideal soldering process and some variations in materials and design of PWBs from those
used by MLCCs’ manufacturers should not pose reliability risks.

             •    Thermal shock
Most specifications require TS cycling between -55 ºC and +125 ºC, and some between max and min temperatures
specified for the part. However, the number of cycles and sample size varies substantially, from 1000 cycles and 77
samples in AEC-Q200 to 5 cycles and 18 pcs in MIL-PRF-55681. This variation might be partially due to the
uncertainty in the efficiency of TS testing to reveal lots with excessive proportion of defects.

Although maximum temperature for MLCCs is typically limited to 125 ºC (apparently, to the Curie point), some
applications involve higher temperatures. For example, qualification of military hybrid microcircuits require
temperature cycling (100 cycles) between -65 ºC and +150 ºC. This means that military grade MLCCs cannot be used
in military grade hybrid microcircuits without additional testing.

Changes in environmental temperature cause thermo-mechanical stresses in MLCCs for two reasons. The first is
related to the presence of materials with different CTE within the capacitor and between the capacitor and PWB in
case of mounted parts. In this case, the effect of temperature cycling depends mostly on the difference between
minimal and maximal temperatures (temperature swing). The second reason comes to play when the temperature of
the part changes drastically, so there is a substantial temperature gradient across the body of a capacitor. These
conditions are defined as thermal shock that per ASTM C-1525 [53] is “a large and rapid temperature change, resulting
in large temperature differences within or across a body”. If temperature on the surface is greater than in the bulk,
expansion of the surface areas of the part will be contained by the colder bulk areas thus resulting in compressive
stresses at the surface and tensile stresses in the bulk. These stresses can develop even in homogeneous materials and
depend strongly on both, the temperature swing and the rate of temperature variations.

Comparison of three different test conditions that create thermal shock in MLCCs: (i) terminal solder dip test, (ii) ice
water test, and (iii) liquid nitrogen drop test showed that the heat conduction and direction of temperature changes
(heating or cooling) are critical factors of thermal shock testing of MLCCs [8]. The probability of fracturing depends
also on the level of residual mechanical stresses, mostly in terminal areas of ceramic capacitors.

The ice water test (IWT) when preheated to a certain temperature MLCCs are immersed into icy water is a reproducible
and effective technique for evaluation of the susceptibility of MLCCs to fracturing during cold thermal shock
conditions. Majority of the parts can withstand IWT at 150 °C and the average critical temperature varied from 170
°C to 222°C. In spite of a significant temperature difference that capacitors experienced during the liquid nitrogen
drop test (capacitors at room temperature are dropped into liquid nitrogen that has temperature -196 °C), this testing
resulted in much less severe cracking compared to the ice-water testing performed at conditions with similar
temperature difference. The result is due to a rapid formation of a gaseous N2 film that shields the surface of the
capacitors and significantly reduces the heat transfer from the part. This confirms that the heat transfer conditions are
of critical importance for TS testing and for the assessment of the thermo-mechanical reliability of ceramic capacitors.
Due to compressive stresses developed by the hot thermal shock conditions during manual soldering or terminal solder
dip testing, the probability of cracking is much less compared to cold TS. For this reason, normal quality lots of large-
size MLCCs (2220) can sustain terminal solder-dip testing at 350 ºC (see section 8.2).



To be published on nepp.nasa.gov.                                                                                     26
Thermal shock testing that is required per military and space specifications for MLCCs is carried out according to
MIL-STD-202, TM107. During this testing the parts are transferred between cold and hot air chambers during up to
5 minutes. Apparently this testing cannot create thermal shock conditions, and a better name for the test would be
temperature cycling.

Built-in or residual stresses in MLCCs might affect their reliability [54, 55]. However, these stresses are mostly
developed during cooling from high-temperature processes such as sintering (>1000 ºC) or termination firing (~400
ºC), and the range of temperatures during temperature cycling of unmounted parts has a relatively minor effect on the
level of these stresses. However, temperature cycling might cause fractures and failures in MLCCs if they are mounted
on the board. The probability of these failures depends on the size of capacitors. For example, some types of large
size capacitors (size 2220) can pass up to 1000 cycles, but fail after 3000 cycles, whereas smaller size parts have a
better stability under this testing. To assure adequate reliability of MLCCs, temperature cycling during qualification
tests should be carried out after soldering, the number of cycles should be increased substantially (at least to 300
cycles), and electrical characteristics (at least DWV and IR) should be verified after the testing.

              •    Life testing
No electrical measurements are currently required after TS testing, and the effect of TS is assumed to be revealed by
the life testing that follows TS and is carried out on the same parts. However, the sequential testing does not allow
for revealing the origin of defects because they might have been preexisted even before TS. A similar sequence of
test is required during screening when TS precedes voltage conditioning. The difference in the screening and
qualification procedures is in the number of cycles, duration of biased testing, and most importantly, in the conditions
of mounting. Obviously, testing during screening cannot reveal cracks that could have been caused by soldering and
temperature cycling of the parts in the mounted conditions.
Requirements to combine TS and life test or voltage conditioning exists in most specifications except MIL-PRF-55681
and ESCC-3009 (however, ESA specification requires also mounting of the parts and 10 TS cycles before HSSLV
testing). This, as well as neglecting mounting before qualification testing might be one of the drawbacks in
manufacturing of the popular CDR- style capacitors.
As will be discussed in section 5.2, life testing of PME capacitors might reveal capacitors with cracks. However,
because only short circuit failures are determined during life testing and BME capacitors with cracks can increase
leakage currents but not fail short circuit, the effectiveness of this test to reveal BME MLCCs with cracks is relatively
low. In the latter case, variations of leakage currents or IR after life testing might be better indicators of quality of the
parts.

              •    Humidity testing
Moisture sorption in the cracks that cross opposite electrodes in ceramic capacitors reduces insulation resistance and
facilitates dendrite growth that might cause short circuit failures. For this reason, humidity testing might be more
sensitive to the presence of cracks compared to life test that occurs in dry conditions. Humidity testing in combination
with soldering and TS stresses would be more efficient compared to life test. However, not all specifications require
mounting, and none, except for ESCC-3009 requires temperature cycling.
Three types of humidity testing are used in different specifications:
   o Moisture resistance test per MIL-STD-202, TM106 with exceptions described in MIL-PRF-123. The purpose
      of this test is evaluation of the resistance of components to the deteriorative effects of high humidity and heat
      conditions typical of tropical environments. During this test, mounted parts are subjected to 20 cycles between
      25 ºC and 65 ºC at 80% to 100% RH (120 hr total at 65 ºC and 100% RH). A 50 V bias is applied during the
      first 10 cycles only.
   o Temperature humidity bias (THB) testing per MIL-PRF-32535 (or AEC-Q200). The parts are tested for 1000
      hours at rated voltages, 85 ºC and 85% RH.
   o Humidity steady state low voltage (HSSLV) testing. Per MIL-PRF-123 this test is carried out using 12 samples
      at 85 ºC, 85% RH for 240 hours at a voltage 1.3 ±0.25 V applied through 100 kohm resistors. The post stress
      measurements of IR should be carried out also at 1.3 ±0.25 V.
Studies of moisture-related failures of first MLCCs (back in late 70th) have shown that the conductive paths that are
formed in cracks can be destroyed by application of rated voltages, and for this reason, HSSLV testing had been

To be published on nepp.nasa.gov.                                                                                         27
developed and even now is often considered as the most effective testing to reveal cracks in capacitors. However,
NASA Engineering and Safety Center (NESC) studies in 2009 [56] have demonstrated that this test is not effective
for the contemporary MLCCs for the following reasons:
    o Historically, low voltage failures (LVF) were attributed to lots with a large proportion of manufacturing defects;
       however, currently, these failures are more likely to be caused by cracking caused by soldering, handling, and
       post-soldering environmental stresses. Technological advances in manufacturing processes and controls have
       produced much more uniform dielectric structure, thickness, and low porosity MLCCs that reduced
       substantially the probability of cracking during manufacturing.
    o No LVFs were identified using HSSLV testing in NASA flight systems for at least the past 15 years and per
       manufacturers’ information the HSSLV testing on military grade MLCCs has generated zero failures during
       last eight years. The hybrid manufacturers were unaware of any MLCC LVF problems in their products.
    o Statistical analysis shows that at the confidence level of 60%, zero failures out of 12 samples that are currently
       required for testing can assure that the proportion of defective parts in the lot is less than ~ 10% only.
Comparative analysis of cracking related failures in PME and BME capacitors has shown that HSSLV testing can
reveal PME capacitors with introduced cracks, but is not effective for BME technology [34]. For this reason, HSSLV
testing has been replaced in MIL-PRF-32535 with THB that had been shown to be more effective for BME capacitors.
It is important to note, that reduced IR or short circuit failures during humidity testing of mounted capacitors might
be caused by external conductive paths (e.g., metal dendrite formation) resulting from surface contaminations and
formed either on the surface of capacitors [57] or on the surface of PWB as shown in Fig.3.1. A thorough failure
analysis is required to confirm that the observed failures are actually caused by cracking in capacitors.




     Figure 3.1. External Metal Dendrite on PWB beneath the MLCC that resulted in false short circuit failure.

             •    Resistance to soldering heat
A qualification test that supposed to verify the robustness of MLCCs against soldering stresses and simulate the worst
case soldering thermal shock conditions is the Resistance to Soldering Heat (RSH) testing that in all specifications is
carried out per MIL-STD-202, TM210. Recommended test conditions per this method are displayed in Table 3.4 and
show that for most conditions the test temperatures are relatively benign and close to soldering temperatures that are
described in manufacturers’ and users’ guidelines for soldering of MLCCs. Note also that extensive experience of
using lead-free solder by commercial industry showed that chip ceramic capacitors are capable to withstand high-
temperature solder reflow processes up to 260 ºC, that exceeds test conditions that are currently used in military
specifications.
It is generally acknowledged [58, 59] that wave soldering causes the most severe thermal shock stress for ceramic
capacitors. The effect is due to a high heat transfer rate when liquid metal comes into contact with MLCCs. These
stresses might create visible cracks on the surface and sides of capacitors that start at or near the termination. Vapor
phase reflow soldering uses the latent heat of vaporization of the condensing vapor as the heat transfer method and
have a lesser effect compare to wave soldering. Infrared reflow soldering is also less stressful because of a low heat
transfer by air convection and radiation, and normally does not result in thermal shock failures.
Manufacturers are often using wave soldering test without preheating to assess quality of their production. The
maximum temperature during this test is 280° C for automotive industry capacitors and 235° C for military capacitors.
However, the wave soldering test is not required in military specifications for MLCCs.



To be published on nepp.nasa.gov.                                                                                    28
          Table 3.4. Test conditions for the “Resistance to soldering heat” test per MIL-STD-202, TM210.
    Solder          Test                                              Heat        Typical
                                          Time
  technique         con       T (°C)                Temp. ramp        cycle      soldering             Comments
                                           (s)
  simulation         d.                                                 s       conditions

  Solder iron         A       350 ±10      4-5             -            1      270C - 300C/ 5s      Not used for MLCCs

                                                                                Resoldering or
                                                                                                    Used for leaded parts
                                                                                   finishing
  Solder Dip          B       260 ±5       10 ±1      25 ±6 mm/s        1
                                                                                replacement at
                                                                                                   and for caps per M123
                                                                                                   (at T=230C) and JAXA
                                                                                   T = 260C
     Wave:                                                                                             Not used in the
                      C       260 ±5       20 ±1                        1           260C
                                                                                                        specifications
    Topside
                                                      Preheat 1-
                                                    4°C/s to within
    Wave:                                                                                          Used by AEC-Q200 w/o
                      D       260 ±5       10 ±1    100°C of solder     1           260C
                                                                                                        preheating.
  Bottomside                                        temp. 25 mm/s
                                                       ± 6 mm/s
                              215 ±5
 Vapor phase                                                                                           Not used in the
                      H       (vapor       60 ±5                        1           215C
                                                                                                       specifications.
    reflow                    temp)
                               215 ±5                 1-4°C/s; 90-
                                                                                                       Not used in the
                      I      (compone      30 ±5      120s above        3
                                                                                                        specifications
                              nt temp)                   183°C
                                                                                 220-230C/10s
                               235 ±5                 1-4°C/s; 90-
 IR/convectio                                                                  for Sn/Pb solder.   Relaxed cond. J is used
                      J      (compone      30 ±5      120s above        3
                                                                                 250-260C/10s      for chip cap per M55681
   n reflow                   nt temp)                   183°C
                                                                                  for Pb-free.
                               250 ±5                 1-4°C/s; 90-
                                                                                                       Not used in the
                      K      (compone      30 ±5      120s above        3
                                                                                                        specifications
                              nt temp)                   183°C

Solder dip test for the same reason as soldering wave test creates severe TS conditions for chip capacitors and is the
test that simulates manual soldering conditions more closely. According to Rawal and co-authors [60] different lots
of MLCCs manufactured in 1980th had different resistance to this type of thermal shock testing (solder dip at 260 ºC)
resulting in up to 74% of failures in some lots and no failures in others. However, the test temperature is reduced
substantially in MIL-PRF-123 (to 230 ºC). Also, the test have a risk of damaging parts by tweezers that create
unknown pressure and additional temperature gradients across the capacitor.
During solder dip, a ceramic capacitor experiences a hot thermal shock with an instant temperature increase that results
in large transient compressive stresses at the surface and relatively small tensile stresses in the bulk of the specimen.
Although this test provides good heat transfer conditions and results in formation of significant thermo-mechanical
stresses, the probability of fracture and crack formation is relatively low. This is mostly due to a high compressive
strength of ceramic materials that is typically in the range from 1 GPa to 4 GPa and is approximately an order of
magnitude greater than the tensile strength [19]. This explains a substantial increase of the critical temperature during
TSD testing over the data reported in literature [61, 62]. In the referred studies the critical temperatures were measured
during cold thermal shock testing that creates tensile stresses at the surface, and hence requires much smaller
temperature gradients to cause fracture. The critical temperature for the hot TS (∆T ~350 °C) is approximately two
times greater than for the cold TS (~150 °C) and is not proportional to the difference in compressive and tensile
strength of ceramics. This can be explained considering that the probability of fracturing depends not only on the
level of the temperature gradient and TS stresses, but also on the level of the built-in mechanical stresses that can vary
from lot to lot due to variations in manufacturing processes.
Resistance to soldering heat test using soldering iron is described in MIL-STD-202 TM 210, condition A. The testing
should be performed at a temperature of the soldering iron of 350 °C ±10 °C by contacting a solder pad with installed
component for 4 to 5 seconds. Although this test simulated rather closely actual manual soldering conditions, for
some reasons it is not used in specifications for space level MLCCs or by manufacturers of the parts.



To be published on nepp.nasa.gov.                                                                                        29
Analysis of requirements to RSH testing described in military and space specifications allows for the following
conclusions.
   o In all specifications except AEC-Q200 the requirements for RSH testing are relaxed even compared to the
      conditions described in MIL-STD-202 TM210. For example, MIL-PRF-55681 and 32535 require only one
      reflow simulation cycle instead of 3 cycles per MIL-STD-202; solder temperature for dip testing in MIL-PRF-
      123 is reduced from 260 ºC to 230 ºC, whereas majority of commercial components are reflow soldered at
      temperatures exceeding 245 ºC. Considering that the requirements of MIL-STD-202 are close to the conditions
      recommended for soldering, the level of stress provided by RSH testing is not sufficient to reveal potentially
      weak lots.
   o NASA/GSFC specification P-829 does not require RSH, but P-838 calls for 6(0) samples to be tested using
     solder dip testing (similar to MIL-PRF-32535) as a part of gr.B screening. Considering that PME capacitors
     might be more susceptible to cracking failures compared to BME parts, RSH testing should be included in the
     S-311-P-829 specification.
   o From 9 to 22 samples are used for RSH testing (AEC-Q200 requires 30 samples). In some cases, one sample
     can fail and the lot will be still considered acceptable for high-reliability applications. Considering that the
     parts are tested at typical soldering conditions, the reason for allowing from 5% to 15% of capacitors fail the
     test is difficult to comprehend.
   o None of the specifications requires the soldering iron test (cond. A per MIL-STD-202, TM210). Taking into
     account a wide use of manual soldering during assembly of space units and boards, this is a substantial
     drawback of the existing qualification system. Large size chip capacitors that are to be manually soldered
     should be first tested for the robustness against soldering stress conditions. A modified solder dip test that can
     be used for this purpose is described in section 8.2.

             •    Flex testing
One of the major causes of MLCCs’ cracking is deformations of the board that transmits stress to the chip through
soldered terminals. This deformation can be caused by variety of reasons including:
    o Thermo-mechanical stresses in the populated board during post-soldering cooling.
    o Depenalization of the individual cards from the master panel.
    o Attachment of components (e.g. insertion or removal of connectors, outlets, pins, etc.)
    o Attachment of the board to the case.
    o Vibration or mechanical shock. Note that vibration induced deformations and the risk of cracking increase
         substantially at the resonance frequencies.
    o CTE mismatch between board material and soldered components during temperature cycling.
KEMET studies [63] have shown that increasing deflection of the board almost exponentially increases the probability
of cracking. For example, bending of 1206 size capacitors on an FR4 board with 1.6 mm thickness at a span of 90
mm to 1.84 mm deflection has generated ~ 0.01% of failures, but increasing deflection raised the probability of failures
to 0.1%, 1%, and 10% respectively at 2.2 mm, 2.25 mm and 2.56 mm of deflection.
Typically, flex cracks originate from the terminal ends at the bottom of the capacitor and have a diagonal direction
inside the part usually at an angle of approximately 45º (see Fig. 2.8.b). In case of excessive amount of solder, the K-
shaped cracks can also develop due to formation of tensile stresses at the top of capacitors [64].
The flex testing first had been developed to reduce cracking during de-panelization in commercial applications.
Currently, this test is required for MLCCs by military and space specifications except for MIL-PRF-123, ESCC-3009,
and S-311-P-829. Note, that NASA/GSFC P-838 specification requires flex testing within gr.B of the screening tests.
According to AEC-Q200-005 and MIL-PRF-32535, this test is carried out using a specified size FR4 board with a
capacitor soldered in the middle of the board. The board is bent as shown in Fig. 3.2a to a certain deflection (typically
2 mm). AEC-Q200-005 defines failure as a condition when a part cracks that can be determined, for example, by
acoustic emission, or by changes in the parameters being monitored. The MIL-PRF-32535 requirement is more
specific and determines failure as capacitance change by more than 10% at a deflection ≥ 2 mm. However, KEMET
studies have shown that 2% of capacitance variations might provide a better resolution for revealing the initiation of
the cracks [10].



To be published on nepp.nasa.gov.                                                                                     30
Figures 3.2.c, d show capacitance variations during flex testing of small size (0603) PME and BME MLCCs. Note,
that variations of capacitance developing cracks during loading are reversible and electrodes separated during the
bending rejoin when the strain is removed. This means that capacitance in parts with cracks can remain within the
specified limits, and in general, capacitance measurements are not effective for revealing cracks. Degradation of
capacitance by steps (Fig. 3.2c and d) indicates partial separation of electrodes during bending that is consistent with
the results of cross-sectioning (Fig.3.2b).




                                                                                                             a)                                                b)

                    0.012       PME 0603 X7R 0.01uF 25V SN2              6
                                                                                                            0.11         BME 0603 X7R 0.1uF 50V SN1            7

                                                                                                             0.1                                               6
                     0.01                                                5




                                                                             deformation, mm
                                                                                                                                                               5




                                                                                                                                                                   deformation, mm
                    0.008                                                4                                  0.09
                                                                                                                                                               4
            C, uF   0.006                                                3                          C, uF   0.08
                                                                                                                                                               3
                    0.004                                                2                                  0.07
                                                        C, uF                                                                                                  2
                                Failure
                    0.002                               bend, mm         1                                  0.06       Failure       C, uF
                                condition                                                                                                                      1
                                                                                                                       condition     bend, mm
                       0                                                 0                                  0.05                                               0
                            0        60        120      180        240                                             0        50     100       150   200   250
                                            time, sec                                                                                time, sec
                                                                                               c)                                                                                d)
Figure 3.2. Schematic of the flex testing (a), cross-sectioning of a capacitor failed flex testing (b), and variations of
                  capacitance and deflection with time for a PME (c) and BME (d) capacitors.
Multiple studies of the flex cracking showed that in addition to the quality of MLCC itself, variety of other factors
might affect test results [32, 63, 65-68]. These factors include:
    o Orientation of the component on the board.
    o Type of attachment, e.g. mounting with Ag-epoxy or soft terminations in the parts absorbs stress and reduces
         cracking.
    o The height and thickness of the solder fillet, and presence of solder under the chip.
    o The type of solder. According to some research [66] less cracking was observed when Pb-free alloys are
         used because high-temperature soldering process creates a higher compressive stresses in MLCCs after
         cooling. However, Adam [69] reported that because Pb-free solders are quite rigid, cracks are generally more
         likely during bending of the boards when Pb-free solders are used.
    o Ceramic material (X7R capacitors are weaker compared to COG capacitors).
   o The size of the chip (larger chips experience greater stress and have greater susceptibility to cracking).
All researches indicate the effect of the chip size on results of flex cracking, so some application engineers utilize a
rule of thumb that prohibits using MLCCs with a size of 1210 or larger. A strong size dependence of the probability
of cracking failures means that commercial BME capacitors that have a smaller size compared to similar value military
grade PME parts are less vulnerable to flex cracking. Application of parts with flex terminations manufactured by
BME technology might reduce failures related to flex cracking substantially.

                •           Sample size
Qualification tests in military and space specifications are carried out using a relatively small sample size, typically
from 6 to 22 pcs, and often require zero failures for the test to pass. However, statistical analysis (e.g. using a Fisher
exact test) shows that when such a small number of samples is used, there is no significant difference between groups
with zero and a few failed samples.




To be published on nepp.nasa.gov.                                                                                                                                                     31
If we want to assure that the proportion of defective samples in a lot (e.g. samples with cracks that can be revealed by
humidity testing) is below a certain value, Pf, the number of samples that has to be tested with a zero failure result (N)
can be calculated as:
            ln(1−𝑐𝑐.𝑙𝑙.)    ln(1−𝑐𝑐.𝑙𝑙.)
𝑁𝑁�𝑃𝑃𝑓𝑓 � = ln(1−𝑃𝑃 ) ≈ −       𝑃𝑃𝑓𝑓
                                           ,
                     𝑓𝑓
where c.l. is the confidence level.

At Pf = 0.1% and c.l. = 60% calculations yield N ≈ 1000, which exceeds substantially a typical sample size for
qualification testing. However, when multiple lots of components manufactured to military specifications passed the
testing, then, considering consistency in manufacturing conditions and materials used, the significance of the testing
is different. For example, if a dozen of lots passed HSSLV testing with 12(0) results, but one lot had one failure,
12(1), the latter can be considered as different at the confidence level of 90%.
This means that using a relatively small sample size for qualification testing might be sufficient for mature
technologies with known consistent and successful results of testing. However, positive results of qualification testing
per military specifications for a new technology or a commercial device does not give the required confidence and
might be misleading.

4. Characteristics of MLCCs
Specifications for low-voltage MLCCs have only three electrical characteristics: capacitance (C), dissipation factor
(DF) and insulation resistance (IR). Measurements of breakdown voltages (VBR) and mechanical characteristics are
not required. However, VBR might be sensitive to the presence of cracks and mechanical characteristics might be
used to assess the robustness of the parts to cracking. For these reasons, these tests are also described below.

              •     Rated voltage
The rated voltage (VR) is an important parameter of MLCCs that determines conditions of measurements and affects
AC and DC characteristics of the parts and their reliability. It is often assumed that VR is limited by breakdown
voltages in capacitors. However, it is not true for low-voltage ceramic capacitors because VBR exceeds rated voltages
by dozens and hundreds times. Contrary to tantalum capacitors, this allows for highly accelerated testing of MLCCs
at voltages exceeding VR many times and allowing for a substantial reduction of times to failure (orders of magnitude)
compared to application conditions. However, high acceleration might increase risks of introducing new failure
mechanisms and cause errors in the reliability prediction.
The rated voltage is selected from a set of standardized values that are changing with increasing increments. This is
one of the reasons why VR is not directly related to physical properties of low-voltage MLCCs, cannot be measured,
and might be skewed by the marketing trends.
Class II dielectrics have a strong dependence of the dielectric constant on the electric field that results in substantial
variations of capacitance with applied voltage. This dependence, rather than VBR, is one of the most important factors
limiting VR. Another important factor is that the probability of failures in MLCCs increases sharply with operating
voltage. This factor is more important for military or space grade parts that should withstand life testing at 2VR and
125 ºC for 4,000 and even 10,000 hours, whereas commercial parts are typically life tested for not more than 1000
hours.
The rated voltage is a technical parameter chosen by manufacturers based on their experience and internal rules so
that voltage dependent characteristics and reliability of the part remained within the specified limits.

    4.1. Capacitance and dissipation factor
According to specifications, measurements of dissipation factors and capacitance for majority of MLCCs (capacitors
in the range from 100 pF to 10 µF) should be made at room temperature, 1 kHz and 1Vrms of the AC signal. However,
the values of C and DF for class II dielectrics are changing substantially with temperature, DC voltage, frequency and
the amplitude of the AC signal. Note, that voltage and temperature stability of capacitance is required only for military
BR or BX type capacitors, whereas military X7R and X7S capacitors are tested to temperature stability only.


To be published on nepp.nasa.gov.                                                                                      32
The limit for DF might be several times greater than the actual values, whereas capacitance should remain within the
specified tolerance. Considering that application conditions might vary substantially from conditions used for AC
measurements, the specified parameters for MLCCs are rarely sufficient for electronic designers to make an informed
choice.
Typical variations of DF for 10 µF 10 V capacitors manufactured by Murata with the level of stress during
measurements are shown in Fig.4.1 [70]. Note that DF decreases with bias and temperature, but increases with
frequency and AC signal. Values of DF are also increasing for thin dielectric capacitors, for example, capacitors with
d ~ 2 to 4 µm typically have DF ~ 4%, whereas for d ~ 15 to 25 µm DF is in the range from 1 to 2%. AC characteristics
of class II dielectric MLCCs might be affected by the prehistory of the parts, e.g. duration of the shelf life or exposure
to high voltages (e.g., DWV testing). For this reason, deaging (e.g. 2 to 5 hours at 150 ºC) is recommended before
measurements.




                                                             a)                                                         b)




                                                             c)                                                         d)
 Figure 4.1. Variations of dissipation factor in 10 µF 10 V X7R and Y5V MLCCs with frequency (a), DC bias (b),
                                      temperature (c), and AC voltage (d) [70].
                                                                                         2
Dissipation factor determines the level of power dissipated in the part, 𝑃𝑃 = 2𝜋𝜋𝜋𝜋𝜋𝜋𝑉𝑉𝑟𝑟𝑟𝑟𝑟𝑟 𝐷𝐷𝐷𝐷, that results in self-heating.
In pulse application the self-heating can cause temperature cycling that might eventually result in cracking and failures.
For example, a 1 µF 0402 size capacitor operating at 1 MHz at DF ~ 5% and Vrms =0.1 V would dissipate ~0.0031 W
that might cause overheating by approximately 20 ºC.
Although military and space documents do not require limiting the maximum dissipated power, this factor might be
critical for signal filtering applications in contemporary low voltage microcircuits operating at high frequencies.
Typical values of the power rating determined by Johansen Dielectrics, JDI, [71] for various size commercial MLCCs
are shown in Table 4.1. The rating is based on 25 ºC temperature rise for standard mounting conditions. For military
and space specifications, it would be reasonable to set the maximum dissipated power and describe procedure for its
measurements. During applications, the power should be derated to 75% of the maximum specified value.




To be published on nepp.nasa.gov.                                                                                            33
                                                                                Table 4.1 Typical power ratings for MLCCs




To assess the effect of cracking on AC characteristics, several types of PME and BME capacitors have been damaged
either by cutting off corners of the parts (fractured capacitors) or by pressing the surface with a Vickers indenter
(damaged capacitors). Figure 4.2 displays correlation of characteristics measured before and after the cracking.
Results show that cracking does not affect capacitance, which is consistent with the results of flex testing when in
many cases capacitance recovers when the stress is removed. Dissipation factor shows some sensitivity and increases
after cracking by 10 to 50%, but remains within the specified limits. Apparently, capacitance is not a useful
characteristic to reveal the presence of cracks, and in some cases, increasing DF might be related to cracking.
However, DF variations might be not related to the crack formation, but rather to mechanical stresses or acoustic
waves associated with the cracking process [72]. Hitting the capacitors without introducing cracks increased DF by
20% to 30% initially, but DF gradually decreased with time and stabilized at the initial level after dozens and hundreds
hours of storage.
                                                           0.36             MLCC 0.33uF 50V                                                            2.25                 MLCC 2.2uF 50V
                                                           0.35
                                                                                                                                                        2.2
                                                           0.34




                                           C_damaged, uF                                                                               C_damaged, uF
                                                           0.33                                                                                        2.15
                                                           0.32                                              PME_C_1825
                                                           0.31                                              PME_V_1825                                 2.1
                                                                                                                                                                                                             BME_C_1206
                                                                                                             BME_A_1210
                                                                                                                                                                                                             BME_C_1210
                                                            0.3                                              BME_C_1210
                                                                                                                                                       2.05                                                  BME_A_1210
                                                                                                             BME_C_0805                                                                                      PME_stack
                                                           0.29
                                                                                                             BME_A_0805
                                                           0.28                                                                                          2
                                                               0.28       0.3       0.32                      0.34         0.36                               2      2.05         2.1       2.15                 2.2      2.25
                                                                                  C_init, uF                                      a)                                                C_init, uF                                   b)

                 2.2             MLCC 0.33uF 50V                                                      1.5                  MLCC 2.2uF 50V                                                         1.4                  MLCCs 1825, X7R

                  2                                                                                   1.4                                                                                         1.3

                                                                                                      1.3                                                                                         1.2
                 1.8




 DF_damaged, %                                                                        DF_damaged, %
                                                                                                                                                                                         DF_fract, %
                                                                                                      1.2                                                                                         1.1
                 1.6                                              PME_C_1825
                                                                  PME_V_1825                          1.1                                                                                              1
                 1.4                                              BME_A_1210                                                                                  BME_C_1206                                                              PME Mfr. C 0.47uF, 50V
                                                                                                       1                                                                                          0.9
                                                                  BME_C_1210                                                                                  BME_C_1210                                                              PME Mfr.C 0.1uF, 100V
                 1.2                                              BME_C_0805                                                                                  BME_A_1210                          0.8                                 BME Mfr.A 1uF 50V
                                                                                                      0.9
                                                                  BME_A_0805                                                                                  PME_stack                                                               BME Mfr.C 1uF 50V
                  1                                                                                   0.8                                                                                         0.7
                       1   1.2   1.4      1.6     1.8                 2     2.2                             0.8      0.9   1      1.1    1.2                  1.3   1.4     1.5                            0.7   0.8   0.9       1      1.1    1.2   1.3       1.4
                                                                                                                  DF_init, %
                                       DF_init, %   c)                                       d)                                   DF_init, %                                                                                                                         e)
                 Figure 4.2. Effect of cracking on capacitance (a, b) and dissipation factors (c-e) of different types of MLCCs.

                 4.2. Insulation resistance and leakage currents
Leakage currents in MLCCs similar to other types of capacitors depend on the applied voltage and are decreasing with
time under bias. For this reason, IR measurements are specified after 2 min of electrification at the rated voltage.
However, if IR meets the specified limit, and is steady or increasing with time, the test may be terminated before the
end of the specified period. Typically, manufacturers are testing IR within a few seconds using a go/no go test, so
actual values of IR are rarely measured.

To be published on nepp.nasa.gov.                                                                                                                                                                                                                          34
Manufacturers of commercial MLCCs or capacitors for automotive industry often use so-called flash IR measurements
instead of regular measurements that require testing at VR. Voltage during flash testing might be up to 10 times
greater than the rated voltage. Although these measurements formally deviate from the military specifications, it
might be an effective means for quality assurance because IR at high voltages should be less than at VR, and passing
the limit at higher voltages gives more confidence in quality of the parts.

Cracks in MLCCs increase leakage currents and might reduce IR, which makes it a characteristic potentially sensitive
to the presence of cracks. To understand factors that affect the sensitivity of IR measurements to cracking, we need
to understand the nature of leakage currents in MLCCs and their relation to the existing requirements for IR.

               •   Specified IR values
Although in many cases, and in particular when capacitors are used for filtering or decoupling in high frequency
applications, circuit designers would be satisfied with IR values in the megohm range, the specifications typically
require gigaohm values of IR (see Table 4.2). This means that the existing requirements for IR are driven by the
quality assurance reasons, rather than by the needs of applications, so the requirements for high IR during screening
are likely used to confirm that capacitors are defect-free.
IR requirements in all specifications except for JAXA QTS-2040M are similar to MIL-PRF-123: 100,000 megohms
or 1,000 megohm-microfarads, whichever is less at 25 ºC. In most applications, the same IR requirements are applied
to PME and BME capacitors. However, JAXA specifications for the thin dielectric BME MLCCs allows for 10 times
lesser IR values.
Experience shows that high volumetric efficiency BME capacitors might have relatively low IR at high temperatures
but excellent long-term reliability. Relatively high leakage currents in BME compared to PME capacitors reflect a
different nature of materials used and are not directly related to the quality and reliability of the parts. Due to a higher
intrinsic conductivity of BME compared to PME capacitors, IR requirements for commercial BME parts are typically
ten times less stringent than for PME capacitors. Requirements of MIL-PRF-55325 to have the same IR values for
BME and PME MLCCs, forces manufacturers of BME capacitors to have increased thickness of the dielectric and
produce capacitors of a larger size that are more vulnerable to cracking.
                               Table 4.2. Requirements for IR in different specifications
                               MIL-          MIL-        MIL-                                  ESA         JAXA
                                                                    S-311-       S-311-
       Temp         VR         PRF-         PRF-        PRF-                                  ESCC         QTS-
                                                                    P-829        P-838
                              123, T        55681       32535                                 #3009       2040/M
                             100 GΩ or    100 GΩ or   100 GΩ or
         25C       ≥25V                                                                                      NA
                             1000 Ω×F     1000 Ω×F    1000 Ω×F     100 GΩ or    100 GΩ or     Typical
                                          100 GΩ or   100 GΩ or    1000 Ω×F     1000 Ω×F     1000 Ω×F
         25C       <25V         NA                                                                         100 Ω×F
                                           500 Ω×F     500 Ω×F
                             10 GΩ or      10 GΩ or    10 GΩ or
        125C       ≥25V                                                                                      NA
                             100 Ω×F       100 Ω×F     100 Ω×F      10 GΩ or     10 GΩ or      Typical
                                           10 GΩ or    10 GΩ or     100 Ω×F      100 Ω×F      100 Ω×F
        125C       <25V         NA                                                                         10 Ω×F
                                            50 Ω×F      50 Ω×F

Increasing temperatures to 125 ºC reduces the specified IR values by 10 times, which corresponds to an effective
activation energy of 0.23 eV. This value is substantially less that the activation energy for intrinsic leakage currents
in MLCCs. The discrepancy is due to absorption currents that are typically prevailing in capacitors within minutes
after voltage application.
Unfortunately, users have a limited information about actual IR values and their distributions, so the margin between
the real values and the limit are rarely known. Without this information, it is difficult to assess the effectiveness of
IR limits for quality assurance, and selection of the criteria in military and space specifications are often based on the
“engineering practice”, “historic data”, and similar specifications rather than on statistical analysis of the test results.
For the same reason, the necessity of two times relaxation of IR requirements for capacitors with VR < 25 V in MIL-
PRF-55681 and MIL-PRF-32535 that might or might not have thinner dielectrics compared to 50 V capacitors is
difficult to assess.


To be published on nepp.nasa.gov.                                                                                        35
Experiments show that military requirements for IR at 125 ºC provide sufficient margin between actual values and the
limit for PME (1 to 2 orders of magnitude) but might be not adequate for BME capacitors. To meet IR requirements,
manufacturers have to increase the thickness of the dielectric for BME capacitors thus increasing the size of the parts
and increasing risks of cracking.

                          •     Absorption and intrinsic leakage currents
Dielectric absorption processes that result in transient leakage currents include dipole orientation, redistribution of
ionic charges, or charge injection from electrodes into the traps in the dielectric. Currents caused by absorption, Iabs,
decrease with time after a step voltage application and follow the empirical Curie - von Schweidler law, according to
which the currents decrease with time as a power function, Iabs(t) = I0×t-n, where I0 and n are constants, and n is close
to 1. Similar absolute values, but different polarity transient currents flow through capacitors under applied voltage
(polarization process) and under short circuit conditions (depolarization process). Intrinsic leakage currents, Iil, in
MLCCs are attributed to electron injection from metal electrodes ito conduction band of the dielectric and can be
described by the modified Schottky model [73].
In a general case, leakage currents in a capacitor can be presented as a sum of charging, absorption, intrinsic, and
defect-related leakage currents:

                       I (t , T ,V ) = I ch (t ,V ) + I abs (t , T ,V ) + I il (T ,V ) + I dl (T ,V , RH )
Charging currents, Ich, correspond to currents in an ideal capacitor without losses, depend on the applied voltage, are
limited mostly by the external circuit (power supply or limiting resistance), and might prevail at times below ~ 1 sec
(see Fig. 4.3). Absorption currents depend strongly on time under bias and applied voltage. Intrinsic currents, Iil(T,V),
do not vary with time, increase exponentially with temperature and super-linearly with voltage. Defect- or crack-
related leakage currents, Idl(T, V, RH), depend also on the relative humidity of the environment.
Figure 4.3 illustrates typical time variations of leakage currents in MLCCs at different voltages and temperatures.
Absorption currents prevail at room temperatures, have a poor temperature dependence, and vary mostly with the
value of capacitance. In high-capacitance MLCCs Iabs are large, and can mask the presence of cracks. Intrinsic leakage
currents prevail at high temperatures and/or high voltages that are typically exceed VR.

                                    Currents in ceramic capacitors                             1.E-07        PME 0805 1uF 10V
                      1.E-03                                   1uF 50V I_ch
                                                               1uF 50V I_abs
                                                               1uF 50V I_lk
                                                               100uF 6.3V I_ch
                      1.E-05                                   100uF 6.3V I_abs
                                                                                               1.E-08


                                                                                  current, A
                                                               100uF 6.3V I_lk



         current, A
                      1.E-07                                                                                10V
                                                                                               1.E-09       30V
                                                                                                            50V
                      1.E-09    charging     absorption        leakage                                      70V           n = 0.99
                                                                                                            90V
                                                                                               1.E-10
                      1.E-11                                                                        1.E+1         1.E+2              1.E+3
                            1.E-3   1.E-1   1.E+1    1.E+3   1.E+5      1.E+7
                                                                                                                      time, sec
                                                time, sec

                        a)   Currents in high-value MLCCs after voltage                         b) Absorption currents at RT and VR prevail
                         application. Gray area shows a typical range of                        during 1 hour of electrification, and increasing
                                        current variations.                                        voltages increase currents exponentially.




To be published on nepp.nasa.gov.                                                                                                                  36
                                     BME_C 2.2uF 50V 1210 at 50V                                          0603 BME 0.1uF 50V
                        1.E-04                                                             1.E-07


                        1.E-05                                                                                                        125C
                                                                                           1.E-08



                                                                              current, A
           current, A
                        1.E-06
                                                                                           1.E-09
                                                                       85C                                 22C                        n = 0.7
                        1.E-07
                                                                       105C
                                                                       125C
                                 n = 0.9                                                   1.E-10        Mf r.C
                        1.E-08                                         150C                                                 n = 0.9
                                                                       175C                              Mf r.M
                                                                                                         Mf r.A
                        1.E-09                                                             1.E-11
                             1.E+1         1.E+2           1.E+3     1.E+4                      1.E+1        1.E+2            1.E+3             1.E+4
                                                                                                                     time, sec
                                                   time, sec

                          c) Dashed lines indicate depolarization, solid                        d) Same value capacitors from different
                          lines - polarization currents. Increasing T rises                   vendors have similar absorption currents (at 22
                            intrinsic currents exponentially and does not                     ºC), but different intrinsic leakage currents (at
                                    affect depolarization currents.                                                125 ºC)
                                               Figure 4.3. Relaxation of leakage currents in MLCCs.
A linear increase of absorption currents with voltage at voltages close or below VR, allows for characterization of
capacitors by a resistance that does not change substantially with voltage. However, at increasing voltages, above 2
to 3 times VR, absorption currents are saturating but intrinsic currents are rising exponentially thus resulting in a
substantial decreasing of IR. Voltage dependence of leakage currents associated with cracks is likely less significant
compared to the intrinsic leakage currents, so increasing voltages might not increase the sensitivity of IR
measurements to the presence of cracks. Fig. 4.4.a presents an example of the current relaxation in a normal and in a
capacitor with cracks. The difference can be observed only after ~ 100 seconds of polarization. This makes the
presence of the defect undetectable by regular IR measurements.
An equivalent circuit of a capacitor that accounts for dielectric absorption, intrinsic, and defect-related leakage currents
is presented in Fig. 4.4.b. The capacitor has a nominal value, C0. Resistor Ril represents intrinsic leakage currents,
and Rd is related to cracking.
Dow [74] has proposed a model for absorption polarization processes that presents a capacitor by a circuit with five
r-Ct relaxators connected in parallel to C0. The relaxation process can be simulated by a proper selection of the
relaxation times, τi = ri×Cti, and absorption capacitances, Cti. In this model, variations of the absorption currents with
time after application of a step voltage, V0, can be described by a simple equation:

𝐼𝐼(𝑡𝑡, 𝑉𝑉)𝑎𝑎𝑎𝑎𝑎𝑎 = ∑𝑖𝑖 0 𝑒𝑒𝑒𝑒𝑒𝑒�−𝑡𝑡�𝜏𝜏𝑖𝑖 �
                      𝑉𝑉
                      𝑟𝑟𝑖𝑖

Calculations based on modeling of absorption processes show that the IR values measured after ~ 100 sec corresponds
to an effective absorption resistance that can be estimated as [73]:
                                 100 × 106 4 × 108 ,
               IR = r >                    =
                                 0.25 × C0   C0
where, C0 is in µF and r is in Ω. This corresponds to the absorption resistance: Rabs×C0 > 400 Ω×F, which is 4 times
greater than the typical requirements for IR (IR×C0 > 100 Ω×F) and provide ~ 40 times margin to the actual IR values.




To be published on nepp.nasa.gov.                                                                                                                       37
                            1.E-06


                            1.E-07             n = 0.7



               current, A
                            1.E-08


                            1.E-09        virgin

                                          crack

                            1.E-10
                                 1.E+0      1.E+1         1.E+2      1.E+3     1.E+4

                                                         time, sec


                             a)      Relaxation of currents in a normal and              b) Equivalent circuit of a capacitor C0
                                     fractured case size 0805, 3.3 µF, 6.3 V           having intrinsic leakage current (represented
                                            capacitors at RT and VR.                   by Ril) with absorption (elements ri, Cti) and
                                                                                                        defect (Rd).
  Figure 4.4. Effect of cracking on relaxation of leakage currents (a), and an equivalent circuit of a capacitor with
                                                      cracks (b).
The intrinsic current density through a dielectric layer is controlled by electron injection over a metal/dielectric barrier
and can be described using the Schottky/Simmons model:
                                                    −Φ                  𝛽𝛽 𝐸𝐸 0.5
𝐼𝐼(𝑇𝑇, 𝑉𝑉)𝑖𝑖𝑖𝑖 = 𝐴𝐴𝑇𝑇 1.5 𝜇𝜇 𝐸𝐸 𝑒𝑒𝑒𝑒𝑒𝑒 � kT𝐵𝐵 � 𝑒𝑒𝑒𝑒𝑒𝑒 � 𝑠𝑠𝑘𝑘𝑘𝑘 �
where A is a constant, µ is the mobility of electrons in the dielectric, E is the electric field in the dielectric, ΦB is the
barrier height at the metal/ceramic interface, βs = 2.7×10-24 C× (m×V)0.5 is the Schottky constant, k is the Boltzmann
constant, T is the absolute temperature.
Experiments show that activation energy of the intrinsic leakage currents, Ea =ΦB – bsE0.5, at rated voltages is 1.19
±0.14 eV for PME and somewhat less, 0.83 ±0.13 eV, for BME capacitors, which explains a higher leakage currents
in BME parts [75].
Manufacturers’ data on temperature dependence of IR, in the range from room temperature to 125°C and the
requirements in military specifications, indicate much lower values of the activation energies, from 0.23 eV to 0.32
eV. This is due to the different nature of currents measured at room temperature and 125 °C. Absorption currents
that have weak temperature dependence prevail at relatively low temperatures close to room temperature, whereas
intrinsic leakage currents that have high activation energy prevail in the high temperature range.

                 •            Effect of cracking on IR
Close correlation between IR values in 15 different types of virgin and fractured capacitors at room temperature (Fig.
4.5a) shows that that IR measurements during screening at room temperature might not detect fractured capacitors.
Apparently, absorption currents that control IR are much greater than currents associated with tiny cracks. It is often
assumed that IR measurements at high temperatures (125 °C) are more sensitive to the presence of defects, and thus
are more effective in evaluating quality of capacitors. However, results of high-temperature measurements for 9 types
of fractured and virgin MLCCs (Fig. 4.5b) also failed in revealing cracks. Obviously, this is due to a high level of
intrinsic leakage currents that apparently exceeds the currents associated with the presence of cracks.
Considering a relatively large margin between the specified and actual IR values, the sensitivity of IR testing for
revealing cracks is further reduced when actual IR values are not recorded and instead the compliance with the
specifications is verified by the go-no go method.




To be published on nepp.nasa.gov.                                                                                                       38
                          1.E+12                                                                                                  1.E+11




        IR_damaged, Ohm                                                                                         IR_damaged, Ohm
                          1.E+11                                                                                                  1.E+10

                          1.E+10                                                                                                  1.E+09

                          1.E+09                                                                                                  1.E+08

                          1.E+08                                                                                                  1.E+07

                          1.E+07                                                                                                  1.E+06

                          1.E+06                                                                                                  1.E+05
                               1.E+06 1.E+07 1.E+08 1.E+09 1.E+10 1.E+11 1.E+12                                                        1.E+05 1.E+06 1.E+07 1.E+08 1.E+09 1.E+10 1.E+11
                                                IR_virgin, Ohm                                                                                        IR_virgin, Ohm
                          2225 1uF 50V      1206 4.7uF 25V                            1210 0.1uF 50V                     M1206 22uF 6.3V           C1206 4.7uF 25V     M1206 10uF 16V
                          1812 1uF 100V     2220 1uF 50V                              0805 3.3uF 6.3V
                          2220 10uF 50V     1210 0.1uF 50V                            1825 0.1uF 100V                    A1206 0.47uF 25V          V1825 0.47uF 50V    A1825 0.47uF 50V
                          1206 82nF 50V     1825 1uF 50V                              2220 22uF 25V                      C1825 0.47uF 50V          A 1825 1uF 50V      P 1825 1uF 50V
                          2223 22nF 50V                   a)
                                            1206 0.47uF 16V                           2220 100uF 6.3V        b)
Fig. 4.5. Effect of cracking on insulation resistance in different types of ceramic capacitors. The IR measurements
   were carried out using a standard technique: 120 seconds of electrification at rated voltages. The dashed line
 corresponds to no-change values. (a) Room temperature measurements. (b) Measurements at 85 °C, 125 °C, and
                                                        165 °C.

    4.3. Breakdown voltage
Breakdown voltage (VBR) is an important characteristic of ceramic capacitors that is sensitive to the presence of
structural defects. Distributions of VBR can be used to assess the proportion of defective parts in a lot and evaluate
quality of the product [76]. In many cases, distributions of VBR values for BME capacitors are bimodal (see Fig.4.6).
For such distributions the intercept point indicates the proportion of parts with defects, and the spread of VBR towards
low voltages indicates the significance of defects (more significant defects result in a more substantial reduction of
VBR).
                                                                                      BME capacitors with bimodal distributions
                                                                                99



                                                                                           1812 1uF50V
                                                                                                  15 um
                                                                                                                0805 0.12uF50V




                                                    cumulative probability, %
                                                                                                                14 um



                                                                                50


                                                                                                                             1210 0.1uF50V
                                                                                                                   12 um, floating electrode

                                                                                10
                                                                                5         0805 0.1uF25V
                                                                                          13 um


                                                                                1
                                                                                200       600        1000             1400                 1800    2200

                                                                                                   breakdown voltage, V


      Figure 4.6. Examples of distributions of VBR for different types of BME MLCCs rated to 25 and 50 V.
Breakdown fields (EBR) in ceramic capacitors increase substantially with decreasing of the thickness of the dielectric
(Fig. 4.7a). Considering that the breakdown has a thermal nature, decreasing EBR with increasing d is likely related to
better thermal conditions for thinner dielectric layers. It is also possible that thin dielectrics have a reduced number
of flaws that are responsible for breakdown.
Breakdown voltages in low-voltage MLCCs are several to more than a hundred times greater than the rated voltage,
and there is a trend of decreasing the safety margin (defined as a ratio of VBR to VR) with the rated voltage (Fig.4.7b).
However, safety margins for capacitors with the same VR can vary up to two orders of magnitude, which is mostly
due to a wide spread of the dielectric thicknesses for capacitors rated to the same voltage (see Fig. 4.7c).




To be published on nepp.nasa.gov.                                                                                                                                                         39
            200                                                                                                                                                                              60
                                                                                                    140
            180




                                                                                                                                                           thickness of the dielectric, um
                                                                                                                                                                                             50
            160                                                                                     120
            140
                                                                                                    100                                                                                      40



EBR, V/um
            120

                                                                                           VBR/VR
                                                                                                    80                                     BME
            100                                                 BME                                                                                                                          30
                               y = 217.42x-0.429                                                                                           PME
            80                                                  PME                                 60
                                                                                                                                                                                             20
            60
                                                                                                    40                                                                                                                    BME
            40
                                                                                                                                                                                             10                           PME
                                                                                                    20
            20
                      y = 155.66x-0.419
             0                                                                                       0                                                                                        0
                  0       20     40         60     80     100                        120                  0                 50              100                                                   0   20   40   60   80   100   120
                                          d, um                rated voltage, V                          rated voltage, V
                                             a)                                        b)                                   c)
       Figure 4.7. Relationship between breakdown field and thickness of the dielectric (a), normalized breakdown voltage
          vs. rated voltage (b), and variations of the thickness of the dielectric with VR (c) in different types of MLCCs.
Measurements and analysis of VBR distributions are not required by the military and space specifications. However,
per MIL-PRF-32535 capacitors during qualification testing should demonstrate VBR exceeding VR by 30 times.
Selection of this criterion for all types of capacitors is not justified, and based on results shown in Fig. 4.7b, a
substantial proportion of parts, including military PME capacitors, would fail this criterion. JAXA employs
measurements of VBR to demonstrate the level of the safety margin in MLCCs for space applications [47].
Most specifications require screening of the parts by the dielectric withstanding voltage (DWV) test that is typically
carried out by exposure of the parts to 2.5VR. However, experiments show that low-voltage capacitors with cracks
can pass this testing but cause failures during long-term operations at lower voltages. Note, that high-quality
commercial MLCCs are often screened by DWV at voltages up to 10 times greater than VR [77].
Figure 4.8 shows an example of VBR distributions for virgin capacitors and capacitors with cracks. The cracks were
introduced by mechanical fracture (MF) at the corner of the part, by cross-sectioning (X-sect), and by a thermal shock
(TS). Similar testing with different types of capacitors showed that on average only ~ 20% of the mechanically
fractured parts have VBR below 2.5VR. Cross-sectioned capacitors and capacitors with TS-introduced cracks had
VBR exceeding DWV by several times. A large percentage of capacitors with tiny cracks created by thermal shock
testing did not decrease substantially VBR compared to virgin parts.
                                                                                                              Gr.2 1812 Mfr.A 1uF 50V
                                                                                    99


                                                                                    90

                                                                                                               MF
                                                                                                                                                  virgin
                                                                                    50




                                                        cumulative probability, %
                                                                                                                                           TS

                                                                                                                           X-sect


                                                                                    10


                                                                                    5




                                                                                    1
                                                                                     60    100                                                    1000     2000
                                                                                                                    breakdown voltage, V

              Figure 4.8. Distributions of VBR for case size 1812 1 uF 50V capacitors in a virgin condition (virg), and with
              cracks introduced by mechanical fracture (MF), cross-sectioning (X-sect), and thermal shock (TS). The insert
                             shows fractured capacitor, and the error indicates voltage during DWV testing.
Results show that the probability of failure during DWV testing per the existing requirements is low even for
capacitors with rough mechanical fractures. Increasing voltage during DWV test up to 50% VBR as suggested in [78]
would increase the efficiency of the testing substantially.

                  4.4. Mechanical characteristics
Cracking of MLCCs occurs when the sum of external and internal mechanical stresses exceeds the strength of the
part. It is reasonable to assume that selection of the most mechanically robust capacitors can reduce the risk of

To be published on nepp.nasa.gov.                                                                                                                                                                                                40
cracking related failures. Mechanical characteristics that can be measured in-situ on MLCCs include flexural strength,
Vickers hardness, and indentation fracture toughness. Below is the summary of mechanical tests that have been
reviewed and detailed in the previous NEPP reports [79, 80].

              •    Flexural strength
Ceramic is a brittle material and its mechanical strength is typically measured using the three point or four point
bending tests. AEC-Q200-003 describes a version of the test for the in-situ measurements of the break strength for
MLCCs. Figure 4.9 gives a schematic and an example of the test set-up. A sample in a special holder is pressed with
a metal rod in the middle until it breaks, thus indicating the fracture load. The specification requires that the minimum
acceptable force to be set by the detailed specifications for the part. However, no methodology for selecting the
minimal force is suggested, and no data for the acceptable limits were found in literature or in the manufacturers’
specifications for automotive industry MLCCs. One of the drawback of the test is that it is limited to relatively large
size (≥ 0805) capacitors. However, using a special fixture or parts soldered onto PWB, the tensile strength can be
measured even for case size 0402 capacitors [81].
Assuming that the test conditions correspond to a three-point bending of a rectangular sample with the thickness d and
width b, the flexural strength, or modulus of rupture, MOR, can be calculated as:
           3𝐹𝐹𝐹𝐹
𝑀𝑀𝑀𝑀𝑀𝑀 = 2𝑏𝑏𝑑𝑑2
where F is the load during fracture, and L is the span of the fixture.
Distributions of MOR values, rather than the fracture loads F are used in technical literature to normalize the strength
and compare results for different part types. Due to small sizes of MLCCs, the stress distribution in a capacitor under
stress deviates from pure bending conditions, and strictly speaking, the above equation is not applicable. However,
the purpose of the testing is mechanical characterization of capacitors rather than ceramic materials and the calculated
MOR values should be considered as an effective flexure strength that characterizes a specific size of capacitors. In
this case, the effective MOR values might allow for comparison of the mechanical robustness of different types of
MLCCs.




                                                         a)                                                         b)
Figure 4.9. An overall view of the set-up for the flexural strength testing (a) and a close -up view of the fixture (b).
                             Insert shows a schematic of the test per AEC-Q200-003
Samples of MLCCs made of the same materials but having different sizes might have a substantially different flexural
strength. For this reason, this technique does not allow an accurate comparison of MOR values for different EIA size
capacitors. However, for the same size capacitors, but with different thickness, normalization allows for a more
accurate comparative analysis. Still, two times difference in the thickness can cause ~ 12% MOR variations, and
thicker samples tend to have smaller strength.
Figure 4.10 shows the effect of surface treatment and the presence of cracks on distributions of MOR in CDR35 style
capacitors. Polishing, immersion into solder flux (Kester 1544 Rosin) and exposure to humid conditions did not affect
the distributions. The latter is somewhat surprising because it is known that cracks can propagate with time of moisture


To be published on nepp.nasa.gov.                                                                                     41
exposure. A thermal shock caused by a solder dip testing at 350 ºC (TSD350) also did not reduce mechanical strength
of the capacitors. No cracking was detected on the parts after TSD350, which is consistent with the measurements of
the flexural strength.
Results indicate that microcracks with a size of a few micrometers or less as well as the presence of water molecules
or contaminations on the surface do not affect significantly the strength of MLCCs. However, cracking caused by a
Vickers indenter applied in the center of the part at forces 2.5 N, 5 N, and 10 N reduced the strength substantially,
from 2 to 5 times. Considering that the size of the cracks increases with the applied force from ~20 µm to ~ 100 µm,
this means that only relatively large cracks, above a few micrometers, reduce the strength of MLCCs.

                                   CDR35BX104AKUS, 0.1uF, 50V, size 1825, Mfr.C                                                            CDR35 capacitors rated to 0.33uF, 50V
                            99                                                                                                   99
                                              10N
                            90                                                                                                   90
                                                    5N
                                                           2.5N

                            50                                                                                                   50




cumulative probability, %                                                                          cumulative probability, %
                            10                                                                                                   10                                          Mfr.V, DC1312
                                                                                                                                                                             Mfr.C, DC1251
                                                                    initial                                                                                                  Mfr.C, DC0140
                            5                                                                                                     5
                                                                    activated rosin flux                                                                                     Mfr.C, DC0135
                                                                    polished                                                                                                 Mfr.C, DC0045
                                                                    moisture: 160hr, 85%RH, 22C
                                                                    TSD350 &moisture

                            1                                                                                                     1
                             40                      100                                     400                                   40                    100                                 400

                                                         MOR, MPa
                                                                a)                       MOR, MPa                     b)
           Figure 4.10. Weibull distributions of MOR for CDR35 capacitors after different treatment before testing (a) and
                                               different lot date codes and vendors (b).
MOR distributions for five different lots of CDR35 capacitors (see Fig.4.10b) indicate that both factors, lot date code
and vendor are significant and the flexural strength technique is capable of revealing lots with reduced strength. The
results show that the mechanical strength is a lot-related characteristic of MLCCs and variations of MOR values from
lot to lot might exceed 50%. However, a substantial amount of statistical data should be obtained to develop
acceptance criteria and use the flexural strength testing for quality assurance.
Measurements of mechanical characteristics of MLCCs from a lot of CDR35 capacitors that had flight failures in
comparison with a reference lot of similar parts that did not have failures (see Fig. 4.11a) showed a statistically
significant difference in the MOR values [28]. Similar results indicating that that 1825 CDR-05 capacitors that were
susceptible to cracking and also caused flight failures had substantially lower MOR values compared to the reference
capacitors have been reported by the Indian Space Research Organization, ISRO, [82]. This confirms the effectiveness
of MOR testing for selecting capacitors resilient to soldering stresses.

                                             CDR35 0.47uF 50V capacitors                                                         600             Effect of case size on MOR
                            99

                            90                                                                                                   500




                                                                                                       characteristic MOR, MPa
                                                                                                                                                                                       PME
                                                         Mfr.A                                                                   400
                            50                  (113/8.6 MPa)                                                                                                                          BME




cumulative probability, %
                                                                             Mfr.C                                               300
                                                                             (148/17.7 MPa)
                                                                                                                                          4 5
                                                                                                                                 200
                            10                                                                                                                    7 8

                             5                                                                                                                                 4
                                                                                                                                 100                                 7   3   19    8    13

                                                                                                                                      0
                             1
                                                                                                                                          1206    1210     1808    1812       1825      2225
                              50                            100                              200
                                                                                                                                                             case size
                                                         MOR, MPa
                                                       a)                                                       b)
    Figure 4.11. Distributions of the flexural strength (MOR) for Mfr.A capacitors that caused flight failures and
reference, Mfr.C, capacitors (a) and characteristic MOR values of the relevant Weibull distributions for different lots
    of MLCCs (b). Red lines in (a) indicate 90% confidence bounds; error bars in (b) correspond to the standard
                             deviations and numbers indicate quantity of the tested lots.

To be published on nepp.nasa.gov.                                                                                                                                                                  42
Results of MOR measurements for different size capacitors are shown in Fig. 4.11.b and indicate a trend of increasing
the strength for the smaller size parts. Case size 1206 MLCCs have MOR values approximately twice the value for
2225 capacitors. This trend is similar to what is observed during the board flex testing and indicates that smaller size
MLCCs are more resilient to bending stresses. Considering that there is no substantial difference in the strength
between BME and PME capacitors, and the first have typically smaller size for the same CV values compared to PME
capacitors, a wider use of BME capacitors in space applications would likely reduce the probability of cracking related
failures.

             •    Vickers hardness
Hardness of materials can be defined as a resistance to indentation. A square-based diamond pyramid indenter is used
during the Vickers hardness testing that is specified in ASTM C1327-15 (2015). Vickers hardness is calculated as a
ratio of the applied force P to the surface area of the footprint:
       1.854 × P
VH =
          D2     ,
where D is the diagonal of the footprint, see Fig. 4.12.
If P is measured in kgf and D in mm, VH number is in kgf/mm2. If P is in newtons and D is in meters, then VH is
measured in GPa.
Analysis shows that in-situ measurements of Vickers hardness are possible for capacitors with relatively thick cover
plates. The effect of metal electrodes can be neglected if P is low enough so the depth of the indentation is more than
~2 times less that the thickness of the cover plate.
Vickers hardness testing of 30 lots of PME and 8 lots BME X7R capacitors (see Fig 4.12b) did not reveal any
substantial difference between PME and BME MLCCs. The observed average VH values varied from 8.5 GPa to
10.2 GPa at a typical standard deviations in the range from 0.5 to 0.6 GPa.

                                                                                            Vickers Hardness Test for PME and BME Capacitors
                                                                                       99




                                                                                                         BME

                                                           cumulative probability, %
                                                                                       50

                                                                                                                     PME
                                                                                       10
                                                                                       5


                                                                                       1
                                                                                        7            8          9         10         11        12

                                                  a)                          VH, GPa                      b)
Figure 4.12. An example of the footprint during Vickers hardness testing (a) and distributions of average VH values
         for different lots of PME and BME capacitors. Dashed lines in (b) indicate 90% confidence range.
Contrary to plastic materials, where the hardness is approximately three times greater than the strength, there is no
correlation between the hardness and strength for brittle ceramics. Although this testing is used sometimes to
characterize ceramic in MLCCs and during failure investigations, it is most likely not effective for prediction of the
susceptibility of capacitors to cracking.

             •    Indentation fracture toughness
Microcracks existing at the surface of a capacitor might not affect its performance if they do not cross opposite
electrodes. However, stresses created during or after soldering might result in enlargement and propagation of small
preexisting cracks resulting in electrical failures with time of operation. Obviously, capacitors using materials with
higher fracture toughness can better resist cracks’ extension and would be more reliable. The ability of a material to
resist fracture and withstand stresses in the presence of cracks is determined by its fracture toughness, Kc.


To be published on nepp.nasa.gov.                                                                                                                   43
Fracture toughness for ceramics in general is one of the controversial issues in materials testing, with more than 30
different tests and many variations for each test available [83]. In-situ measurements of Kc using indentation fracture
technique (IFT) is the most controversial, and has not been standardized so far. Nevertheless, this method has been
used by many researchers because of its simplicity and the applicability to small size samples. This technique is
considered an unrivalled quick, convenient and economical means for comparative, site-specific evaluations of the
toughness of ceramics [84].
This method consists of using a Vickers indenter in order to generate cracks at the corners of the indent (see Fig.
4.12a) and calculating Kc based on the length of cracks, c. A commonly used equation for the radial-median cracks
relates Kc with the load P, Vickers hardness H, and Young’s modulus E:
                          0.5
                        E  P 
K c ( R _ M ) = ξ R _ M    1.5 
                        H  c  ,
where ξR_M = 0.015 is constant.
Results of IFT measurements on samples from different lots of PME capacitors having the same part number are
shown in Fig. 4.13b. No significant difference between lots with different date codes was observed. However, it
appears that the fracture toughness for M123BX474 capacitors is ~ 30% less than for CDR35BX334 capacitors. It is
possible that in spite of the controversy, IFT in-situ measurements of the fracture toughness can provide useful
information regarding robustness of capacitors to the cracking failures. However, improvements in the accuracy of
measurement to better than ±20% are required.
                                                                             1.60          Different lots of capacitors
                                                                                       1.351.33
                                                                             1.40
                                                                             1.20                   1.07




                                                             Kc, Mpa_m^0.5
                                                                                    1.03                1.00
                                                                             1.00                                       0.89
                                                                                                                    0.83
                                                                             0.80
                                                                             0.60                                              L1
                                                                             0.40                                              L2
                                                                             0.20                                              L3
                                                                             0.00




                                                         a)                                            b)
 Figure 4.13. An example of the footprint during indentation fracture toughness testing (a) and Fracture toughness
                  for different lots (L1, l2, and L3) for three types of military grade capacitors.
Experiments show that Kc values for MLCCs are in the range from 0.8 to 1.4 MPa×m0.5 for PME BX, from 1.3 to 1.6
MPa×m0.5 for PME BP, and from 0.7 to 1.3 MPa×m0.5 for BME class II dielectric capacitors. Considering the accuracy
of measurements, there is no statistical difference between fracture toughness of PME and BME capacitors.

5. Failure mechanisms in MLCCs with cracks
Failures of MLCCs with cracks are commonly explained by moisture sorption that increases conductivity along the
surface of the crack or causes electrochemical migration (ECM) of electrode materials and formation of shorting metal
dendrites. Silver that is used in PME capacitors is a metal most susceptible to ECM. Migration of silver can be
observed at voltages as low as 0.4 V [85] and relative humidity down to ~ 40% RH [86], which is the reason of so-
called low-voltage failure phenomena in capacitors. Fig.5 shows an example of a capacitor failed due to silver
electromigration along an internal crack shorting opposite electrodes. Note, that this part passed screening testing per
MIL-PRF-55681.
Much less is known about ECM in BME capacitors with internal electrodes made of nickel, which is often considered
as a non-migrating metal. In the absence of moisture in environments, e.g. during life testing at 125 ºC or at low
temperatures in vacuum, degradation and failures in capacitors with cracks might also happen, but the mechanism of
the process is less obvious compared to humid environments.


To be published on nepp.nasa.gov.                                                                                                   44
                                                                                                                Ag




                                                          a)                                                        b)
  Figure 5. An overall (a) and close-up (b) views of a shorting crack in 0.1 µF 16 V PME capacitor. The part was
tested at 6 V and started showing increased and unstable leakage currents after 110 hr at room temperature and then
     failed eventually short circuit due to silver electromigration after 50 hr at 60 ºC. (Pictures courtesy of Ron
                                           Weachok, Jacobs Technology Inc.)

    5.1. Degradation of PME and BME capacitors in the presence of moisture
Capillary condensation can fill tiny cracks with water even at relatively low level of humidity in environments and
remain trapped in the crack even after several days in dry conditions [87]. To simulate electrochemical processes in
capacitors with cracks filled with condensed water, a water layer testing (WLT) at low voltages, from 0.5 V to 1.5 V,
was used in [88]. The parts were cross-sectioned perpendicular to the internal electrodes and a quarts slide pressed
against the surface with exposed electrodes formed a few micrometers’ gap filled with deionized water. Formation of
dendrites was observed using an inverted metallurgical microscope (Fig.5.1).




                                                           a)                                                         b)

Figure 5.1. Schematic of the water layer test set-up (a) and an example of dendrites formed between the termination
 and the tip of the negatively biased electrode on the surface of 1825 0.1 µF 100 V PME capacitor that was shorted
                                  after 3.6 min at 1.3 V and blown after shorting (b).

Results show that the presence of condensed water in relatively wide cracks can result in formation of shorting
dendrites within a few minutes even at voltages below 1.5 V. Formation of dendrites bridging electrodes and their
blowing after short circuit (Fig. 5.1b) might explain intermittent behavior of failures in MLCCs in humid
environments. When electrodes are bridged by a tiny dendrite, this blowing might clear the short, after which the
process repeats. However, when a relatively large dendrite is formed, the resistance of the short is less and the
dissipated power is larger. This might result in a micro explosion creating a more severe damage to the structure of
capacitors and cause melting of ceramic and catastrophic failures (see an example in Figure 5.2.). It is also possible
that during such an event the melted metal will be forced to fill out other areas of the crack that during cross-sectioning
might be misjudged as metal migration.




To be published on nepp.nasa.gov.                                                                                       45
Figure 5.2. An example of a catastrophic failure caused by copper dendrites growth on a surface of a BME, 1 µF 50
V, case size 1812, capacitor. These dendrites grew for 5 min at 3 V, 95% RH, but the short circuit failure occurred
when a rated voltage was applied after the testing. An overall SEM image is overlapped with EDS mapping and the
  top insert shows the area of a blown dendrite resulted in damage of ceramic, and the bottom shows a clos-up of a
                                                   copper dendrite.
Surprisingly, dendrites in PME capacitors in many cases were formed not by silver, that was expected initially, but by
lead (Fig. 5.1b) or tin (Fig. 5.3a). Similar tin dendrites were also observed on the surface of BME capacitors (Fig.
5.3b). Apparently, anodic dissolution, diffusion, and migration of Pb and Sn ions in water occurs faster than
dissolution of silver in the Ag/Pd alloy used in internal electrodes. This is likely due to the impeding role of palladium
oxide that is formed on the surface of electrodes in PME capacitors and is likely the major protection against
development of Ag dendrites [89, 90]. Alloying of silver with palladium reduces the probability of dendrite growth,
but it still might happen due to Ag diffusion along the grain boundaries of ceramics during sintering.




                                                         a)                                                  b)
Figure 5.3. Growth of tin dendrites at the edge cathode electrodes in a BME 1825 0.47uF 50V capacitor that failed
  at 0.8 V after 23 minutes of testing (a) and in a PME capacitor that failed short circuit after 18 min at 0.8V (b).
Errors indicate location of anodic dissolution of tin in the termination. Inserts show EDS mapping of the dendrites.

Figure 5.4.a shows silver dendrites formed on the surface of a PME capacitor at the tips of negatively biased electrodes
and along the portion of the electrodes near terminations. Location of the dendrites indicates that the silver base frit,
rather than the positively biased internal electrodes was the source of silver. Copper dendrites on the surface of BME
capacitors (Fig. 5.4b) were also formed at the tips of electrodes and pitting corrosion of the copper frit termination
indicates the source of the metal used to form dendrites. Results show that in both types of capacitors, BME and PME,
shorting dendrites can be formed by materials used in terminations and/or solder used for attachment to the board.

To be published on nepp.nasa.gov.                                                                                      46
                                                                a)                                                              b)
Figure 5.3. Dendrite growth during WLT at 1.3V in PME (a) and BME (b) 0.47 uF 50 V MLCCs. Silver dendrites
were formed after 2.5 min in PME (a) and copper dendrites were formed after 8 min in the BME capacitor (b). Note
   pitting corrosion in the Ag (a) and Cu (b) base metal terminations for PME and BME capacitors respectively.

Contrary to WLT, only a few (from 2 to 4) monolayers of water are absorbed during humidity testing at 85% RH and
85 ºC. This retards significantly processes of the anodic dissolution and ion migration. At these conditions, formation
of silver and/or Ag/Pd dendrites and failures due to short circuit or intermittent contacts in PME capacitors was
detected after hours of testing (Fig. 5.4.a). Also, silver precipitates between the electrodes were formed by a colloidal
silver oxide [85, 91]. Considering that silver oxides have relatively high conductivity [92], these deposits can cause
increased leakage currents and parametric failures even without development of shorting dendrites.
Testing of the damaged by cross-sectioning BME and PME 0.47 µF 50 V capacitors having the same thickness of the
dielectric (~1 mil) in humidity chamber at 1.3 V (HSSLV testing) showed that failures occurred in ~85% of PME
capacitors, whereas BME capacitors had no failures. Typical variations of leakage currents in the parts are displayed
in Fig. 5.4, and Fig.5.5 shows typical formations observed on the surface of the parts after the testing.
                            PME Mfr.C 1825 0.47uF 50V X-sect.                               BME Mfr.A 1825 0.47uF 50V X-Sect.
                                 at 85C/85% RH, 1.3V                                             at 85C/85% RH, 1.3V
                   1.E-04                                                      1.E-04
                                                                                                                        SN6
                                                                                                                        SN7
                   1.E-05                                                      1.E-05
                                                                                                                        SN8
                                           SN36                                                                         SN9


      current, A                                                  current, A
                   1.E-06                  SN37                                1.E-06
                                                                                                                        SN10
                                           SN38
                   1.E-07                  SN39                                1.E-07
                                           SN40
                   1.E-08                                                      1.E-08

                   1.E-09                                                      1.E-09
                         0.01    0.1      1         10   100                         0.01        0.1     1         10   100

                                         time, hr                                                       time, hr
                                                    a)                                                   b)
 Figure 5.4. Variations of leakage currents with time during HSSLV testing of PME (a) and BME (b) 0.47uF 50V
           cross-sectioned MLCCs. Note that the currents were limited to ~ 10-5 A by external resistors.

BME capacitors after HSSLV had IR typically exceeding 10 MOhm, whereas PME capacitors had IR in the kilo-ohm
range. Although BME capacitors did not fail electrically, SEM examinations revealed nickel carbonate compositions
formed around anode electrodes. These compositions had high resistivity and did not short the capacitors. Note that
similar formations were detected on the surface of fractured BME capacitors after humidity testing, whereas silver
deposits were present on the surface of PME capacitors (Fig. 5.5 c, d).




To be published on nepp.nasa.gov.                                                                                                    47
         Anode                        Cathode




        a) Ag/Pd dendrites on the surface of a PME
      capacitor failed after HSSLV testing. Note erosion           b) surface of a BME 1 µF 50 V capacitor after
        of the anode electrode indicating the source of            44 hr of HSSLV testing. Note copper formations
               metal ions used to form dendrites.                           at the tips of anode electrodes.




      c) PME, case size 1825, 0.1 µF, 100 V capacitor,
                                                                   d) BME, case size 1825, 1 µF, 50 V, capacitor,
      after testing at 22 °C, 85% RH, and 5 V. Although
                                                                   after testing at 22 °C, 85% RH, and 15 V for 300
          Ag dendrites were not found, EDS mapping
                                                                     hours. High-resistivity Ni/C/O formations at
       indicates the presence of silver deposits between
                                                                          anode electrodes are similar to Fig.b.
                           electrodes.
Figure 5.5. SEM and EDS images of formations on the surface of PME (a, c) and BME (b, d) cross-sectioned (a, b)
                           and fractured (c, d) capacitors after humidity testing.
In a simplified form, processes of ECM on the surface of BME and PME capacitors that result in dendrite growth at
cathode electrodes, formation of precipitations between the opposite electrodes, or formation of deposits at anode
electrodes are shown in Fig. 5.6. The process of dendrite growth (Fig.5.6a) occurs in three-steps: (i) anodic dissolution



To be published on nepp.nasa.gov.                                                                                     48
of metal ions, (ii) migration of ions along the surface, and (iii) deposition at the cathode. Anodic dissolution is an
essential part of all ECM processes.
Depending on the type of materials and test conditions, the precipitates might be conductive (typical for PME
capacitors) or isolative (typical for BME capacitors). Silver oxides are conductive and the resistivity of Ag2O/Ag2O3
varies from 10-5 to 10-3 Ω-cm. At this resistivity, even tiny areas of the crack can cause substantial IR degradation
and failures. For example, in a 100 μm wide crack with a 10 μm spacing between electrodes, a thin, 10 nm thick crack
filled with Ag-oxide would have resistance from 1 Ω to 100 Ω.


                                             Me           OH

+ A                            -+ A                 Me                -
                 M           C                                    C
                                                    Me

         Me
                                              precipitates
                a)                                b)                                    c)
 Figure 5.6. Simplified schematic of electrochemical processes in MLCCs: cathode dendrites growth (a), formation
                              of precipitations (b), formation of anode deposits (c).

ECM of silver in test structures consisting of conductive elastomer land grid array sockets did not result in formation
of dendrites. Instead, leakage current degradation and failures occurred when surface insulation resistance dropped
substantially due to silver ion accumulation prior to the dendritic formation [93]. In this case, the time necessary for
the ion accumulation to reach a certain critical concentration determines the time-to-failure.
Analysis of the surface of fractured BME capacitors after humidity testing revealed evidence of the electrochemical
migration of nickel at voltages as low as 1.3 V. However, similar to cross-sectioned samples, nickel formed
amorphous, bulbous deposits on the anode electrodes (Fig.5.5 b, d). These deposits covered large areas of capacitors
and were mostly comprised of nickel oxide, with the addition of carbon. Formation of these deposits can be explained
by the anodic dissolution of Ni+ ions from the internal electrodes that form complex cations through reactions with
water and CO2 in air. This subsequently leads to reduction of the complex cations at the anode (Fig.5.6c) and
formation of agglomerates of nickel oxides (NiO) and nickel carbonates (NiCO3) around anode electrodes of the
capacitor.
The following reactions might explain ECM processes in BME capacitors:
     Ni2+ + 2H2O  HNiO2- + 3H+
     or Ni-OH + CO2  NiOCO2- + H+ .
At the anode nickel carbonates and oxides are formed:
3HNiO2- + H+ Ni3O4 + 2H2O + 2e-
or NiOCO2- +4H2O –e NiCO3(H2O)4
Pure stoichiometric NiO crystals are perfect insulators (~1013 Ω-cm) [94], but even doped, non-stoichiometric oxides
still have high resistivity (10 to 106 Ω-cm). Formation of highly resistive composites does not degrade substantially
IR and does not cause electrical failures in BME capacitors.
Due to a high susceptibility of metals used in terminations (Cu, Sn, Pb, Ag) to electromigration, generation of ions by
the anodic dissolution and their diffusion from terminations along the moisture absorbed layer on the surface of
MLCCs (see Fig. 5.7) can cause failures in both types, PME and BME capacitors. This mechanism might prevail over
ECM of internal electrodes in BME capacitors, whereas silver migration originated either from terminations or internal
electrodes and formation of conductive oxides deposits is prevailing in PME capacitors.
An example of behavior of leakage currents with time of operation in capacitors with cracks is shown in Fig. 5.8.
Leakage currents at 22 ºC and 85% RH were monitored for 1000 hours in CDR35 capacitors after simulation of
stresses associated with manual soldering by the terminal solder dip (TSD350) testing (see section 8.2). Seven out 20

To be published on nepp.nasa.gov.                                                                                    49
samples after TSD350 failed the testing. In spite of the presence of cracks, electrical failures even at a relatively high
humidity were observed only after long periods of testing ranging from 100 to 860 hours (Fig. 5.8b). The failures
were intermittent and the parts exhibited unstable currents even before reaching the level of the formal failure.

                    diffusion
                                                                                             Mfr.A after TSD350 and CSAM at 22C
                                 dissolution
                                                                                                          85% RH, 50V
       water                            Sn/Pb                                    1.E-4

                                                                                 1.E-5
                                deposition
                                                                                 1.E-6
                migration          short

                                                                    current, A
                                                                                                  SN A1        SN A5
                                                                                                  SN A6        SN A9

                                                +                                1.E-7            SN A15
                                                                                                  SN A20
                                                                                                               SN A18
                                                                                                               1 G_uF

                                                                                 1.E-8

                                                                                 1.E-9

                                                                            1.E-10
                                                                                         0       200       400      600   800     1000
                                                                                                             time, hr
                                                              Figure 5.8. Leakage currents in CDR35 0.47 µF 50 V
    Figure 5.7. Schematic of failures in MLCCs with
                                                              capacitors during 1000 hour testing at 22 ºC, 85% RH,
  cracks caused by migration of ions that are anodically
                                                              and 50 V. An insert shows example of cracks formed
              dissolved from terminations.
                                                                                   by TSD350.
Moisture adsorption on the surface of cracks reduces the surface energy of ceramics, thereby decreasing the critical
stress needed for the crack growth [95]. Delayed cracking under operating electric fields is one of the major reliability
issues for ferroelectric devices [96] and the effect has a strong dependence on humidity and voltage. Results for
potassium sodium niobate ferroelectric ceramics show that crack growth occurs in humid air of 70% and 90% RH but
was not observed at RH ≤ 30%. It is assumed that the critical humidity for crack growth without an electric field is
~50% RH. Crack growth can also occur in dry air when the electric field is larger than a certain threshold value, and
the incubation time decreases for larger fields.
Considering that cracks might grow with time in the presence of moisture in environments, it might take months and
even years of operation at normal conditions to form a short. Incresed humidity, temperature and voltage would
accelerate the degradation process substantially. However, due to the difficulties in predicting behavior of cracks and
complexity of the ECM processes involved, there is no reliable models to assess acceleration facors for cracking
related failures.
Derating, that is one of the major means to increase reliability of components during operation, might be not effective
to mitigate cracking related failures. For example, decreasing temperature of operation might have an adverse effect
due to the associated increase of relative humidity. Because ECM can occur at very low voltages (below 1.5 V),
reduction of voltage does not eliminates the risk of electrical failures.
Operation in dry environments after the parts with cracks have been exposed to humid conditions might not eliminate
the risks of failures. For space electronic modules stored or operating at the ground, a gradual diffusion of water
molecules inside a capacitor is possible, and the presence of moisture on the surface of cracks and associated
degradation of IR can be observed with time of operation at normal conditions. It is also possible that a certain amount
of moisture remains trapped in the cracks in flight modules operating in space. Water molecules in cracks are bonded
to the surface by strong physical and chemical forces (in the form of –OH groups), which makes their removal without
high-temperature baking extremely difficult even in vacuum. This allows for ECM processes in cracks to continue
after launch, but it might take much more time for the failure to occur compared to the ground operations (unless the
crack developed further, for example due to vibration during the launch).
A specific trait of silver is that it can migrate even in dry conditions through the ceramic grain boundaries and
eventually cause shorts [97]. The activation energy of silver migration through the glass is relatively large, 1 to 1.3
eV [98], so the process at room temperatures might take thousands of hours. At a low rate of the ECM process,
formation of dendrites is unlikely due to the effect of poisoning by contaminations, and the failures are most likely
due to formation of silver oxide deposits.


To be published on nepp.nasa.gov.                                                                                                    50
Results of testing of BME and PME MLCCs with cracks in humid environments can be summarized as follows [34,
88]:
1.       In the presence of condensed water, dendrite growth on the surface of cracks in PME and BME ceramic
capacitors can occur at voltages in the range from 0.5 V to 1.3 V and metals the most susceptible to dendrite growth
are Pb > Sn > Ag for PME capacitors and Pb > Sn ≥ Cu for BME capacitors.
2.       The specific of ECM in fractured MLCCs is the presence of different metals forming galvanic cells in the
termination that enhance substantially anodic elution of metal ions such as Pb, Sn, and Cu at low voltages. PME
capacitors, due to the presence of Sn/Pb – Ag galvanic cells, are more susceptible to Pb and Sn dendrite growth
compared to BME capacitors that have Sn/Pb – (Ni or Cu) cells with more compatible anodic indexes.
3.        At a similar level of cracking, BME capacitors have lower probability of failures compared to PME
capacitors. Leakage currents in BME capacitors typically degrade relatively slowly, and require higher voltages than
in PME capacitors. This is due to different electro-chemical behavior of the nickel and silver/palladium electrodes.
In PME capacitors, formation of conductive silver dendrites or silver oxide deposits results in short-circuits between
the electrodes, whereas in BME capacitors, highly resistive nickel/carbon/oxygen compositions are formed.
4.       In humid environments, the rate of degradation of leakage currents in BME capacitors with cracks increases
with the applied voltage. For this reason, HSSLV testing that is used for PME capacitors, is not effective for BME
capacitors, and instead, THB testing at 85 °C, 85% RH, and rated voltages for 240 hours is recommended.

    5.2. Degradation in dry environments
Due to a reducing atmosphere during sintering of BME capacitors, the concentration of charged oxygen vacancies
(VO++ ) in the ceramic is increased, and the mechanism of degradation during life testing is attributed to migration and
accumulation of VO++ at the grain boundaries and metal/ceramic interfaces. This causes decreasing of the energy
barriers and increasing of leakage currents by enhanced electron injection according to the Schottky mechanism. For
this reason, BME capacitors are much more susceptible to wear-out failures compared to PME capacitors.
Improvements in materials and process control reduced degradation in BME MLCCs substantially, and currently, the
inception of the intrinsic wear-out failures became much greater than the mission duration in most high-reliability
applications. However, in capacitors with defects degradation processes might accelerate substantially and cause
infant mortality (IM) failures. Studies have shown that roughness and presence of voids in metal electrodes result in
local field enhancement causing reduction of insulation resistance [52, 99, 100]. This might affect performance of
capacitors with thin dielectrics.
A thermal runaway model that relates the presence of defects resulting in thinning of the dielectric to reduction of
breakdown voltages and decreasing times to failure has been suggested in [101]. According to this model, the same
degradation process that is responsible for the intrinsic wear-out failures might result in IM failures for capacitors
having defects. In this case, voltage and temperature reliability acceleration factors that are determined for wear-out
failures might be used to predict IM failures. The model can also explain degradation of leakage currents in BME
capacitors with cracks during operation at high temperatures in dry conditions by enhanced migration of oxygen
vacancies along the surface of cracks.
Compared to BME, PME capacitors have much lower leakage currents and lower probability of thermal breakdown.
Failures in these parts are likely due to the time dependent dielectric breakdown (TDDB) caused by generation of
traps in the dielectric. According to the percolation model, breakdown occurs when concentration of defects reaches
the critical level [102]. During breakdown, the energy stored in the part is released instantaneously resulting in
adiabatic overheating and melting of a local area of the dielectric and metal electrodes. Contrary to PME, degradation
in BME capacitors occurs gradually and the energy generated at the defect can be balanced by heat dissipation. This
explains why “leaky” BME capacitors often degrade, but do not fail catastrophically, whereas PME capacitors with
prevailing avalanche-like breakdown [103] might not degrade, but fail short circuit instantly (see Fig. 5.9.d).
Variations of leakage currents in BME and PME capacitors with introduced cracks (Fig.5.9) show that cracking did
not affect leakage currents in capacitors measured after a few minutes of testing. This confirms that IR measurements
at 125 °C might be not sensitive to the presence of cracks. However, currents started increasing after ~ 1 hour and



To be published on nepp.nasa.gov.                                                                                    51
raised more than two orders of magnitude after 10 to 100 hours (Fig. 5.9.a, b). After that, the currents stabilized or
decreased with time, so no catastrophic failures happen.
Degradation of leakage currents in BME capacitors can be explained assuming that migration of VO++ along the surface
of cracks occurs faster than in the bulk of the dielectric. This facilitates accumulation of VO++ at local areas of metal
electrodes near the crack, and accelerates degradation of leakage currents. After reaching the ceramic/electrode
interface, oxygen vacancies can diffuse along the interface thus charging areas close to the crack and reducing the
barrier height at metal/ceramic interface (see Fig. 5.9.c). According to this mechanism, relatively minor cracks with
a size of a few micrometers might increase leakage currents during HALT, but not cause catastrophic failures.
However, a short circuit failure due to a thermal runaway might happen in a case of extensive cracking.
                       1.E-4                                                             1.E-03
                                                                                                          virgin
                                                                                                          fractured
                                                                                         1.E-04
                       1.E-5


          current, A
                                                                            current, A
                                                                                         1.E-05

                       1.E-6
                                   Mfr.C                                                 1.E-06

                                     Mfr.A               reference
                       1.E-7                                                             1.E-07
                            0.01    0.1        1        10       100                              0.1       1            10       100   1000
                                             time, hr                                                                 time, hr
                                                                       a)                                                                       b)

                                                                                                        CDR 1825 with cracks at125C
                                                                                          1.E-04                  200V
                                                                                          1.E-05




                                                                            current, A
                                                                                          1.E-06


                                                                                          1.E-07         Mfr.C

                                                                                          1.E-08
                                                                                                                      Mfr.V
                                                                                          1.E-09
                                                                                               1.E+2             1.E+3         1.E+4    1.E+5
                                                                                                                         time, sec
                                                                       c)                                                                            d)

 Figure 5.9. Variations of currents through HALT testing in BME (a, b) and PME (d) capacitors with cracks. BME
 capacitors, 0.33 µF 50 V (a) and 1 µF 50 V (b) were tested at 125 ºC, 100 V and PME capacitors, 0.47 µF 50V, at
125 ºC and 200 V. Dashed lines correspond to virgin and solid lines to capacitors with cracks introduced by Vickers
             indenter. Fig.c shows a schematic of degradation processes in BME capacitors with cracks.
Due to the thermal nature of breakdown in BME capacitors, degradation caused by migration of VO++ after HALT not
only increases leakage currents, but also reduces breakdown voltages. Capacitors with defects reduce VBR after
HALT to a much greater degree compared to the defect-free capacitors. This makes high-voltage DWV testing after
burning-in or life test a useful instrument to reveal capacitors with cracks.
Analysis shows that low-voltage BME capacitors with defects during life testing in dry conditions are more likely to
fail parametrically, whereas catastrophic failures are more probable for PME capacitors, which is attributed to different
mechanisms of breakdown for PME (electronic) and BME (thermal) capacitors. This situation is reversed compared
to humid environments when PME capacitors with cracks are more likely to fail compared to BME capacitors.

6. Special cases of MLCC cracking during manufacturing, assembly, and
   testing
Common reasons for cracking are associated with:

To be published on nepp.nasa.gov.                                                                                                                         52
   o   stresses during manual soldering, rework, or touch-up to improve appearance of the fillets;
   o   flex bending of the boards during depanelization, handling, mounting, or vibration testing;
   o   temperature cycling of MLCCs soldered onto PWBs;
   o   Excessive power during ultrasonic cleaning of the assembled boards.
To reduce the risk of failures during ultrasonic cleaning some manufacturers [104] and JAXA [47] recommend using
cleaners with power not exceeding 20 Watts per liter at a frequency of 40 kHz for not more than 5 minutes. The
cleaning process might cause substantial damage to MLCCs in case of resonance of PWB, so Murata recommends
testing the cleaning equipment before starting the process to ensure it does not degrade capacitors [31].
Several less often discussed reasons of cracking are described below.

    6.1. Hydrogen-related cracking
Anomalies in a module operating in space have been detected after months of work and were attributed to excessive
leakage currents in CDR35 0.47 µF 50 V capacitors, These parts have been soldered manually and were suspected of
having cracks [28]. Testing of a spare unit on the ground also showed increasing leakage currents after several weeks
of operation. Failure analysis investigation confirmed that increased leakage currents were due to delaminations and
cracking in the part. No external cracks on the failed lot were observed; however, acoustic microscopy showed that a
substantial proportion of parts had delaminations at the termination areas.

Simulation of manual soldering stresses by TSD350 testing using virgin capacitors from the failed lot showed that
cracks initiated at the surface continued as metal/ceramic delamination and facilitated formation of internal cracks
crossing electrodes (see Fig. 6.1). Most likely, delaminations or weakening of the metal-ceramic adhesion occurred
during manufacturing and grew further due to manual soldering stresses. Delaminations facilitated formation of crack
crossing electrodes and resulted in electrical failures with time during biased testing. Corner location of delaminations
indicates that they developed during formation of terminals.




                                            a)                                                                 b)




                                                        c)                                                          d)

    Figure 6.1. Crack reveled in MLCCs after TSD350 cross-sectioning across (a, b) and along (c, d) terminals.

One of the reasons for corner delaminations is evolution of hydrogen during electroplating of nickel and solder
finishing. Several publications have discussed effect of hydrogen on ceramic materials and capacitors. Severe
degradation of physical properties of ceramics has been reported by H.Zhang et.al. [96]. Hydrogen generation and its
diffusion through ceramics during electroless nickel plating was attributed to failures of MLCCs by W. Chen and co-
workers [105].


To be published on nepp.nasa.gov.                                                                                        53
J. Piper [7] reported on failures of capacitors operating in the battery hydrogen atmosphere. The failures were
attributed to the splitting of the side margins caused by hydrogen absorbed by the palladium electrodes. H.Zhang
at.al. studied the effect of hydrogen on the fracture properties of the lead-free ferroelectric ceramics [96, 106].
Hydrogenation decreased the fracture toughness measured by IFT linearly with increasing concentration of hydrogen
and delayed propagation of unloaded indentation cracks.
Y.Saito at al., studied degradation and failures of BME capacitors during biased testing at 120 ºC and 85% RH [107].
Leakage currents during the testing started increasing after dozens to hundreds of hours of testing and were unstable.
Experiments with terminals having different thicknesses showed that moisture can penetrate to the active areas of
MLCCs by permeation through relatively thin terminals and produce hydrogen by electrolysis of water molecules.
The hydrogen reduced nickel oxide at the cathode electrodes and caused cracking due to release of internal stresses in
the capacitors.
Using impedance spectroscopy and diffusion analysis Heidary and Randall [108] have demonstrated that increased
leakage currents in MLCC after hydrogen diffusion are mostly due to decreasing Schottky barriers at the
electrode/ceramic interface. It has been shown that the fastest path for diffusion in BME X7R capacitors is along the
Ni/ceramic interface and somewhat slower along the grain boundaries. The pre-exponential factors D0, and activation
energies, Ea, for diffusion along electrodes, along the grain boundaries and through the grains respectively are 0.88,
0.28, and 0.002 cm2/sec and Ea = 0.73, 0.76, and 0.52 eV. At these conditions, the effective diffusion coefficient of
hydrogen is ~1.1×10-7 cm2/sec at 250 ºC and the diffusion length is ~ 0.2 mm after 1 hour of exposure to the forming
gas (5% H2 and 95% N2).
In PME capacitors, palladium in Ag/Pd electrodes forms a layer of PdO, which is considered the major protection
against silver migration and development of silver dendrites [89, 90, 97]. Reduction of PdO in the presence of
hydrogen removes the barrier and facilitates electrochemical migration of silver. This process occurs also with a
substantial volumetric changes because palladium volume increases during oxidation by 68% [97]. According to
R.Newnham [7], the lattice parameter of PdO decreases from 3.902 A to 3.891 Å during the reduction. Volume
expansion due to the oxidation of Pd and contraction during reduction of PdO can have a detrimental impact on the
microstructure of not only the metal, but also of surrounding ceramic [97].
Based on the effect of hydrogen, failures of MLCCs that have caused flight anomalies can be described as follows
(see Fig. 6.2). Initially, due to some anomalies in the Ni plating process, a relatively thick Ni layer was formed and
an excessive amount of hydrogen was generated at the terminals. The hydrogen diffused inside the ceramic and due
to a high solubility of hydrogen in palladium (up to several percent [7]) accumulated mostly in the first electrode
layers in areas close to terminals. Because the solubility of hydrogen in palladium decreases with temperature, heating
of the parts during manufacturing, e.g. burning-in, can release some hydrogen that caused volumetric changes by oxide
reduction, decreased adhesion and fracture toughness, and caused some relatively minor delaminations at the corner
areas of the capacitors. A more severe heating during manual soldering or TSD350 simulation increased further
delaminations by the same mechanism and also because of a relatively large tensile stresses created by expansion of
thick Ni layers. Increased delaminations might facilitate formation of corner cracks caused by thermo-mechanical
stresses during the soldering induced thermal shock. In the presence of moisture, electrochemical migration in cracks
crossing opposite electrodes resulted in increased and unstable leakage currents. Reduction of PdO by hydrogen also
facilitated electromigration of silver and electrical failures during biased testing.
Experience gained during MLCC manufacturing shows that cracking and delaminations caused by Ni plating occur
more often with PME than with BME capacitors, which is due to a much higher level of hydrogen absorption in Ag/Pd
electrodes compared to Ni electrodes. Absorbed hydrogen can also create a pop-corn-like effect during fast heating
of capacitors that occurs during manual soldering of the parts.




To be published on nepp.nasa.gov.                                                                                   54
                                                                           a)      Electroplating of Nickel results in
                                                                           hydrogen generation at the surface and its
                                                                           diffusion inside the capacitor at the
                                                                           terminals.



                                                                           b)       In the formed capacitors, hydrogen
                                                                           is mostly absorbed in electrodes close to
                                                                           the surface and terminations. Hydrogen
                                                                           absorption goes along with reduction of the
                                                                           protective PdO layer and decrease in
                                                                           metal-ceramic adhesion.




                                                                           c)       Manual soldering creates a thermal
                                                                           shock and together with mechanical
                                                                           stresses caused by the difference in CTE
                                                                           between Ni and ceramic, results in
                                                                           delaminations and cracking.
  Figure 6.2. Schematic of the delaminations and cracking in MLCCs caused by hydrogen evolved during nickel
                                                 electroplating.

    6.2. Effect of pick and place machine
During automatic assembly processes, MLCCs are picked up by a vacuum tool or tweezers and either placed on bond
pads with solder paste for reflow, or glued to the board in preparation for wave soldering. In either case, damage and
crack formation in the parts are possible. A trend of rising the probability of damaging by the pick-and-place machine
for small size (0402) ceramic components (capacitors and resistors) and possible techniques to assess the susceptibility
to this kind of damage was discussed by S.Meyer at al. [81]. Stresses created by the pick-and-place machines might
be not revealed by initial optical inspections and electrical testing, but cause failures during operations. In some cases,
partially cracked components had electrical parameters within the specification, but their mechanical stability was
compromised.
Testing techniques that can assess the tensile strength of SMD components have been suggested and used to
differentiate damaged and faultless components. One of the techniques used was measurements of the impact strength
to evaluate the critical energy of cracking for ceramic components. Another technique included measurements of the
tensile strength that is similar to the flexural strength method (section 3.2), but uses a special fixture for small-size
capacitors. A version of this test employs capacitors soldered onto PWB instead of loose parts in fixtures.
Results show that variations of the parameters of the pick-and-place tools (placement force and energy absorption in
the spring systems) affected the tensile strength of 0402 SMD components. It was found that adjustments in the spring
system of the pick-and-place equipment had the most significant effect on the probability of cracking and failures.

    6.3. Electro-mechanical resonance
Class II and III dielectrics in MLCCs are ferroelectric materials that exhibit piezoelectric (generation of charges under
stress) and reverse piezoelectric (formation of mechanical strain under applied electric field) effects. The reverse
piezoelectric effect results in small, but measurable deformations in the capacitors. For example, ~ 0.75 µm
displacement was detected in a 300 V, 9 µF capacitor at the rated voltage [109].

To be published on nepp.nasa.gov.                                                                                       55
Rapid deformation under bias results in generation of acoustic waives when an AC signal is applied to polarized
(biased) ceramic capacitors. At these conditions, a capacitor operates as a resonator and can be characterized by a
series of resonance frequencies (see Fig. 6.3). The electro-mechanical resonance (EMR) effect is observed in all types
of MLCC except for class I dielectrics and has a strong dependence on the DC bias.
The major resonance that corresponds to a maximum amplitude spike corresponds to the standing wave spread along
the width of the capacitor. Independent on the part type and/or manufacturer, the major resonance frequency is
determined by the width, W, of the capacitor and can be predicted using a simple relationship fres = v/(2W), where v is
the sound velocity (longitudinal waves) in the ceramics. Experimental data illustrating the relationship between fres
and W are shown for X7R capacitors in Fig. 6.3. The results correspond to v ~4.1×103 m/sec, which is close to typical
values for the sound velocity reported in literature [110].
Impedance spikes on the frequency dependence of biased MLCCs might not only result in excessive noise in the
system, but cause a mechanical damage to the part and catastrophic failures. Such a failure has happened with stacked
9 µF 300 V capacitors used in a beam power supply system in the NEXT PPU project [109]. The part operated
normally at ripple currents of 20 A p-p, frequency 200 kHz, and 80 to 160 V DC bias for many hours during multiple
air and vacuum testing, but failed short circuit eventually after 345 hours of operation. Fig. 6.3.f shows the failed
capacitor with a crack caused by the EMR effect in the part. Note, that the width of the capacitor corresponded to a
resonance frequency of approximately 200 kHz that coincided with the operational frequency of the system.
Electro-mechanical resonances might be especially detrimental when capacitors are used in power applications and
operate under large DC and ripple voltages. NASA/GSFC guidelines for selection of MLCCs [111] is warning about
the EMR effect and suggests using impedance spectroscopy to make sure that the major resonance frequency is outside
the range of operating conditions.
                                          BME, 1uF 50V, size 1812                                             BME, 22uF 6.3V, size 1206

                              1             0V                                                      1
                                                                                                             0V
                                            40V                                                              4V
                                                                                                             9V


        ESR, Ohm                                                                       ESR, Ohm
                         0.1                                                                       0.1



                                                                                                  0.01
                     0.01


                                                                                          0.001
              0.001                                                                           1.E+05                    1.E+06                 1.E+07
                  1.E+05                             1.E+06              1.E+07
                                                                                                                     freqiency, Hz
                                                  frequency, Hz
                                                                                  a)                                                                    b)
                              0.8       BME, 10uF 25V, size 1210 MLCC                             0.8         PME, 0.1uF 50V, size 1825
                              0.7                                                                 0.7

                              0.6                                   0V                            0.6
                                                                                                                                          0V
                                                                    25V
                                                                                                  0.5

                                                                                       ESR, Ohm
                              0.5


                   ESR, Ohm
                                                                                                                                          40V
                              0.4                                                                 0.4

                              0.3                                                                 0.3

                              0.2                                                                 0.2

                              0.1                                                                 0.1

                               0                                                                    0
                               3.E+05                                    3.E+06                     4.0E+5                                     4.0E+6
                                                  frequency, Hz                                                   frequency, Hz
                                                                                  c)                                                                    d)




To be published on nepp.nasa.gov.                                                                                                                            56
                                Resonance frequencies in X7R MLCCs
                                         with different size
                     5.E+06

                     4.E+06
                                      y = 4.09E+06x



     frequency, Hz
                     3.E+06

                     2.E+06

                     1.E+06

                     0.E+00
                              0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1 1.1
                                              1/2W, 1/mm
                                                                            e)                                   f)
  Figure 6.3. ESR spectrums for different types of X7R capacitor with and without DC bias (a-d), variation of the
  major resonance frequency with the width of capacitors (e), and a 9 µF 300 V stacked ceramic capacitor that has
                          been damaged when operating frequency was close to fres (f).

7. Revealing cracks
Commonly used techniques to detect cracks include external visual examination, ultrasonic inspection, electrical
measurements of capacitance, dissipation factors and IR. These techniques have been used for screening and
qualification in military and space specifications and have been discussed in previous sections. It has been shown that
they have a limited capability in detecting small cracks in MLCCs, are used mostly to reveal defects created during
manufacturing and cannot be relied on to reliably detect damage caused by soldering and post-soldering stresses.
The most common technique to reveal cracks and delaminations is by ultrasonic microscopy that can reveal gaps even
as small as ~ 0.1 µm. Until recently, this technique could be applied to horizontal cracks only, but Sonoscan has
developed a method that images cracks and delaminations in unmounted MLCCs, regardless of their direction [69].
Although the latest development in X-ray imaging, especially using computer tomography 3D or CT-scan imaging
system, have been used successfully in revealing flex cracking in assembled large size (1812) capacitors [112], more
work has to be done to assess its sensitivity for smaller size capacitors with cracks caused by soldering.
A brief description of new or less frequently used methods that have been suggested for detecting cracks in MLCCs
is given below. Although these methods have been successfully used in lab environments, none has been widely
adopted for inspection by manufacturers and require further work and improvements. Nevertheless, they might be
beneficial for end users during failure investigations or evaluation of new board designs, assembly processes or new
technology components.

    7.1. Optical examinations
                         •     Vicinal illumination
Fine cracks are difficult or impossible to detect using standard visual inspection even using high-power microscopes
due to the lack of contrast. Using dye penetrants and examinations under the black light illumination might be more
effective, but contaminates the part. The effectiveness of optical inspection can be increased substantially by
application of the vicinal illumination technique [113]. Examples of revealing cracks using vicinal illumination are
shown in Fig. 7.1. This technique employs a high power bright field microscope with a small aperture. Light from a
small bright spot on the ceramic is scattered by near-by cracks thus creating a sufficient contrast for easy detection.
This technique is widely used for failure analysis of ceramic components, but it is time consuming because requires
scanning of relatively large areas using small light spots (~200 µm) and high-power microscopes. For this reason, its
application for screening purposes is limited. A restricted access to the parts soldered onto PWBs for the close
proximity inspection using high-power microscopes limits application of this technique for soldered MLCCs.

To be published on nepp.nasa.gov.                                                                                     57
                                                         a)                                                          b)

Figure 7.1. Examples of cracks exposed in MLCCs by the vicinal illumination technique. Top images show regular
   dark field high-power (X200 magnification) images of the cracks indicated by errors, and bottom images were
                                      obtained using vicinal illumination.

              •   Revealing delamination by discoloration of ceramic layers.
Optical examination of cross-sectioned samples during DPA might sometimes reveal discoloration of ceramic layers
similar to those shown in Fig. 7.2. These discolorations were attributed to internal mechanical stresses formed during
sintering and caused by the CTE mismatch between ceramic and metal electrodes. Cracks and delamination are
formed with time when the stress is released. Formation of these defects might cause failures when terminal electrodes
are not compact enough and do not block electroplating solutions from penetrating inside the capacitor. This
phenomena affected mostly BME COG capacitors [26]. It was noted that the dielectric discoloration can be more
easy found after terminal firing than after tumbling.




                                                         a)                                             b)
    Figure 7.2. Discoloration in a dielectric layer of MLCCs revealed by a dark field inspection during DPA a)
                          attributed to stresses [26], b) attributed to delamination [114].

    7.2. Electrical measurements
Insulation resistance (IR) is a parameter sensitive to the presence of cracks, and in some cases up to 60% of damaged
parts exhibit a detectable change in IR [115]. However, only a minority of MLCCs can be actually identified as
potential failures before use. In addition, in-circuit tests can rarely apply sufficient voltage and/or time for realistic
IR measurement. For capacitors soldered onto circuit cards, leakage through the circuit might be greater than through
the capacitor, and the electrical problem may be intermittent [40]. Most functional tests of the assembled electronic
cards are not sensitive to IR values, and many decoupling or EMC suppression capacitors may be damaged and
defective without affecting circuit function in normal conditions initially.
The reason by which IR measurements might be not sensitive enough to the presence of fine cracks are discussed in
section 4.2. A procedures that might improve the sensitivity of IR measurements for the cracks’ detection and
techniques that do not require measurements of leakage currents are described below.

To be published on nepp.nasa.gov.                                                                                      58
              •   Methanol test
Methanol is a conductive, low-viscosity liquid with a perfect capillary action that allows penetration into tiny cracks
in ceramics. A methanol test was used to further increase the sensitivity of leakage current (or IR) measurements to
cracking [116]. During this test, the parts are preheated to 85 ºC for 15 minutes and then immersed into methanol at
room temperature for 3 minutes. DCL measurements were repeated after methanol removal and drying the part for
~1 minute. This test has been used successfully for revealing cracks in MLCCs; however, several factors may also
lower the insulation resistance, thus obscuring the effect of cracks. These factors include contaminated cleaning
solvents or large amounts of dissolved flux residue [115]. In several cases, application of methanol for parts with
excessive DCL values decreased leakage currents, thus casting doubt on the effectiveness of this test [79]. It is possible
that this was due to preheating at 85 ºC that was used before immersing capacitors into methanol. Overall, the success
of using methanol testing to reveal cracks was less than expected.

              •   Temperature dependence of capacitance
Exploiting thermal mismatch between the capacitor and the organic board to create tensile stresses and expand the
crack in the part was used in [117] to reveal cracks by monitoring variations in capacitance with temperature. The
idea of this technique is similar to flex testing, but instead of bending, the tensile force is created by the CTE mismatch
between the capacitor and the board. However, class II and III dielectrics have a strong temperature dependence of
capacitance that might obscure capacitance decay caused by damage.

              •   Time Domain Reflectometry (TDR)
Using TDR technique was suggested by M. Azarian to detect cracks in assembled MLCCs [118]. A short high-
frequency pulse is applied by probes close to a capacitor, and a reflection of the signal that is detected at the input
terminal can indicate the presence of cracks. A reliable detection of cracks was possible for large, case size 1812,
capacitors with severe cracking. However, the testing was much less successful for smaller size capacitors (0805).

              •   Absorption voltage
A relatively poor sensitivity of traditional IR measurements to the presence of cracks is due to high level of absorption
currents that prevail in MLCCs during first minutes after voltage application and mask currents related to cracks.
However, time dependence of absorption voltages, Vabs, can be used to assess IR values related to the intrinsic currents
in capacitors that are much lower than absorption currents.
The absorption voltage is due to releasing charges absorbed in the dielectric back to electrodes after a brief short
circuit of a pre-polarized capacitor. When polarized at VR and then short-circuited for a few seconds, absorption
voltages in X5R and X7R MLCCs typically increase within a few hours and can reach several volts. Subsequently,
Vabs decreases slowly and can remain above one volt even after hundreds of hours (Fig. 7.3). The time to Vabs roll-off
and the rate of voltage decrease are related to the leakage currents in the capacitor. A simple model that is based on
the Dow equivalent circuit for capacitors with absorption allows for estimations of the insulation resistances in MLCCs
that are not skewed by absorption currents [119]. The method is based on monitoring long-term variations of Vabs and
allows for estimations of the insulation resistances up to 1014 Ω.
In the presence of cracks, the roll-off occurs earlier and maximum values of Vabs are substantially less than for virgin
capacitors (see Fig.7.3a). Estimations of IR values for capacitors with cracks showed a substantial reduction compared
to the values for virgin capacitors (see Fig 7.3.b). Note, that all damaged capacitors, except one, had IR exceeding 1
GΩ, which is acceptable per the existing requirements. Measurements of insulation resistance in MLCCs using a
standard technique fail to reveal capacitors with cracks (see section 4.2), whereas the voltage absorption technique
was effective in more than 70% of cases. However, the technique is time consuming and cannot be used for assembled
capacitors.




To be published on nepp.nasa.gov.                                                                                       59
                                 2                                                                          1.E+15
                                         init                                                               1.E+14
                               1.6
                                         fract. SN1
                                                                                                            1.E+13




                                                                                           R_damaged, Ohm
                                                                          5E14 Ω
                               1.2       fract. SN2
                                                                                                            1.E+12


                  voltage, V
                               0.8                                                                          1.E+11

                                                                       2.5E12 Ω                             1.E+10
                               0.4
                                                                                                            1.E+09
                                                                        7E10 Ω
                                 0                                                                          1.E+08
                                 1.E-3   1.E-2    1.E-1      1.E+0    1.E+1     1.E+2                            1E+08 1E+09 1E+10 1E+11 1E+12 1E+13 1E+14 1E+15
                                                          time, hr                                                               R_init, Ohm
                                                           a)                                             b)
  Figure 7.3. Absorption voltages in normal and damaged case size 1825, 0.1 µF 100 V capacitors (a) and effect of
fracturing on IR, calculated based on absorption voltage model for 20 different types of capacitors (b). Dashed lines
   in (a) are calculations at the indicated values of IR and in (b) the dashed line corresponds to no-change values.

    7.3. Electro-mechanical effects
Methods employing electro-mechanical effects are based on excitation and registration of mechanical waves in
MLCCs by different techniques. Changes in the spectrum of the observed signals or in deformation of the part in the
presence of cracks allow for revealing defective capacitors. These techniques include electromechanical resonance
spectroscopy, resonance ultrasound spectroscopy, acoustic emission, and scanning laser interferometry.

               •                     Variations of the electro-mechanical resonance spectrum
The spectrum of electro-mechanical resonances, similar to those shown in Fig. 6.3, is formed by the standing acoustic
waves reflected from different interfaces. Cracks and delamination are additional sources for reflection and dissipation
of acoustic energy and affect the spectrum. This effect was used by O. Boser at al. [110] to develop a non-destructive
testing to reveal delaminations and cracks in capacitors. An automatic equipment for testing that can test a capacitor
in 25 ms with 95% accept accuracy has been suggested.
Our experiments have confirmed that impedance spectroscopy might be sensitive to the presence of rough defects and
cracks in capacitors. An example of variations in the spectrum shown in Fig. 7.4.a indicates that cracks introduced
by the Vickers indenter on the surface of the part shift the resonance frequencies and substantially reduce the
amplitudes of spikes. However, the changes in the amplitude and position of the spikes were much less noticeable for
tiny cracks caused by thermal shock. Another problem with this method is that the spectrum depends on the prehistory
of the part. In particular, long-term polarization can shift resonance frequencies with time even in defect-free
capacitors (see Fig. 7.4.b).
                               0.4              BME 1812 1uF 50V                                             0.2            BME 1206 1uF 50V
                        0.35                                                                                0.18
                                                                                                                                                     init
                                                                                                            0.16
                               0.3                                                                                                                   10 min
                                                                                                            0.14                                     40 min



                                                                                           ESR, Ohm
                        0.25

             ESR, Ohm
                                                                                                            0.12                                     3.5 hr

                               0.2                                                                           0.1
                                                                                                            0.08
                        0.15
                                                                                                            0.06
                               0.1
                                                                                                            0.04
                        0.05                                  SN1 d           SN2 d                         0.02
                                                              SN3             SN4
                                0                                                                             0
                                1.5E+6                   2.0E+6                   2.5E+6                     2.7E+05       2.9E+05       3.1E+05            3.3E+05
                                                      frequency, Hz           frequency, Hz
                                                         a)                                            b)
 Figure 7.4. Electromechanical resonance spectrums. a) virgin (dashed lines) and capacitors with introduced cracks
               (solid lines). b) Spectrums in a virgin capacitor measured with time under 40 V bias.

               •                     Resonant ultrasound spectroscopy (RUS)
Generation and detection of vibrational resonances in solids by resonant ultrasound spectroscopy (RUS) technique
have been used to determine elastic properties of materials [120]. A version of the RUS method has been also


To be published on nepp.nasa.gov.                                                                                                                                     60
developped to detect cracks in MLCCs [121]. According to this technique, a driving transducer at a corner of a
capacitor generates a range of vibrational frequencies that are detected by another piezoelectric transducer/receiver at
the opposite corner of the part. To minimize damping effects due to transducer contacts, the two transducers hold the
specimen with small contact areas at the diagonal opposing corners. The receiving spectrum is similar to those shown
in Fig. 7.4 and indicate vibrational resonances in the capacitor that change their position and amplitude if cracks are
present.

The benefit of this technique is that it does not require biasing of the capacitor and can be used for the parts soldered
onto PWBs. RUS measurements made over the frequency range from 500 kHz to 3 MHz for virgin capacitors and
capacitors subjected to thermal shock by the IWT (from 150 ºC to ice water) showed some changes in the spectrum.
However, variations in the amplitude, contrary to the shift in frequency, might be also due to some changes in the
position of the transducers. No significant changes in spectrums was detected after the flaws have been introduced
by FIB milling and microindentation. It was assumed that the size of these flaws is too small to cause substantial
changes in the resonant frequency. Apparently, more studies are necessary to increase the reproducibility of test
results and sensitivity of this technique to tiny cracks.

             •    Tone-burst excitation
Phase analysis of electromechanical resonance with tone-burst excitation was used by Johnson at al. [122] to reveal
cracks in X7R MLCCs. A ferroelectric transducer that generated radio-frequency tone bursts with durations of 0.2
ms in a 50 V capacitors biased at ~ 30 V formed mechanical waves in the part. The nonlinearity was quantified by
shifts in resonant frequencies as a function of ferroelectric excitation level. Special algorithms of data analysis have
been developed to characterize the non-linear effects in MLCCs. Acoustic non-linear measurements can provide data
that are less sensitive to variations of frequencies but change significantly in the presence of defects. However, only
89 % of the MLCCs with visible cracks formed by the IWT (quenching preheated to189 ºC capacitors in ice water)
have been detected. It is recognized that although the observed correlations indicate that nonlinear acoustic
measurements offer a promising approach for nondestructive detection of cracks in MLCCs, further work to improve
the level of detection should be pursued.

The technique was later upgraded by analysis of the dependence of phases and resonant frequencies on vibrational
amplitude during ring down following the tone-burst excitation [123]. This improvement increased the proportion of
detected MLCCs with visible cracks to 93%.

             •    Acoustic emission
Acoustic emission is a well known effect during breakdown events in capacitors. Measurements of acoustic signal
caused by partial breakdown in capacitors with defects was used in [124] to screen out high voltage Z5U and X7R/BX
capacitors with voids and delaminations. An AC-voltage-induced acoustic emission testing showed that the severity
of delaminations correlates with the corresponding level of the acoustic signal.
Acoustic emission test for low-voltage MLCCs has been developed in [125]. Electrical pulses with amplitude of +-
10V and duty cycle 80% applied to the parts soldered onto a PWB created vibration and resonances in capacitors. The
pulses had frequency sweeps from 100 Hz to 2 MHz. The acoustic emission (in the megahertz range) induced by the
electrical signal was measured directly from the component using a piezoelectric point contact sensor. Mechanical
damage, such as flex cracks and delamination, changed acoustic behavior and was used to reveal MLCCs with defects.
Acoustic signals were characterized with a numerical algorithm, and analysis has demonstrated that defects caused by
the board bending affected the acoustic response. However, the precision and sensitivity of the acoustic measurements
leave some room for improvement and more work is necessary to reduce errors and develop a technique that would
detect capacitors with defects more reliably.

             •    Laser interferometry
A different technique to generate mechanical waives and detect the effect of cracks in MLCCs was suggested by
Erdahl and Ume [126, 127]. A structural vibration was stimulated by a short, ~6 nsec, pulse of an infrared laser and
the out-of-planer displacement of the surface was measured by a fiber-coupled laser interferometer (see Fig. 7.5a).
Comparison of the waveforms between a reference, defect-free capacitor and device under test (see Fig. 7.5b) allows
for revealing capacitors with defects. Because vibration of a capacitor depends on the attachment conditions, both,

To be published on nepp.nasa.gov.                                                                                     61
the reference and the tested device should be attached to the same board in the same soldering process. A special
signal processing technique improves the sensitivity of this method that had been successfully used for small size
(0805 and 0603) capacitors.
The method can be automated and used for online quality assurance of MLCCs after soldering in mass production
environments. The lack of reference capacitors on the board and insufficient statistics might limit application of this
test for low-volume production of circuit assemblies. Although this method was able to detect flex cracks intentionally
introduced in MLCCs, further testing and analysis are required to account for possible process-induced manufacturing
variations.




                                                       a)                                                         b)
  Figure 7.5. Set-up of the laser ultrasonic quality inspection system (a) and a time-domain vibration response (b).
                     The insert shows a capacitor with laser excitation and measurement spots.

8. Cracking caused by manual soldering
Due to the process variations and dependence on operator skills, possible formation of significant temperature
gradients, and deviations in the amount of solder, all manufacturers strongly discourage the use of hand soldering for
MLCCs. However, due to the low volume production manual soldering is a common process for space electronic
assemblies and hybrid microcircuits. In some cases, large size capacitors cannot be positioned using pick-and-place
tools, and have to be soldered manually. In addition, high cost of the boards makes rework necessary in case of
failures.
Experiments show that manual soldering have a detrimental effect on MLCCs with preexisting cracks [34]. A much
greater proportion of case size 1825 capacitors failed environmental stress testing after manual soldering compared to
the parts tested in fixtures. For different part types, the times to failure (TTF) during humidity testing of manually
soldered capacitors decreased by one to three orders of magnitude in comparison with similar capacitors that have
been tested in mechanical fixtures.
The risk of cracking during hand-soldering is increasing with the size of capacitors. J.Maxwell [11] suggested to
“never use soldering irons” for parts with a case size of more than 1210. However, even small size capacitors (0603)
might have a high probability of fracturing after hand soldering [128].
Volume of publications discuss the susceptibility of MLCCs to cracking caused by manual soldering. However, there
is a lack of technical literature that analyses stresses during the attachment with soldering iron and describes physical
mechanisms of cracking and failures.
In general terms, cracking in MLCCs occurs when the sum of internal stresses built during manufacturing and external
stresses caused by soldering exceeds the strength of the part. Assuring that the level of soldering stresses is at the
acceptable level is a workmanship issue and requires compliance with the existing guidelines. Assuring that MLCCs
can withstand soldering stresses (have low built-in stresses and a high strength) is a part’s issue and should be achieved
by adequate selection and qualification tests. Commonly used workmanship requirements and suggestions for


To be published on nepp.nasa.gov.                                                                                      62
qualification tests to assess the robustness of MLCCs are described below. The workmanship requirements are based
on decades of industry practice and studies, are well-developed and documented. However, procedures that would
allow selection of the most robust to manual soldering capacitors has not been sufficiently developed yet.

     8.1. Workmanship recommendations for manual soldering
The international standards for rework, modification and repair of electronic assemblies, IPC-7711C/7721C and IPC
J-STD-001G [129, 130] warn against touching components by the soldering iron and recommend preheating and
limiting temperature heating rate to below 2 - 4 °C/sec to avoid thermal shock conditions. However, it does not
provide any specifics related to the hand soldering procedures for MLCCs and refers to manufacturers’ data sheets for
additional information.
NASA and ESA guidelines for manual soldering [131-133] are mostly applicable to connectors and also lack
information related to MLCCs. JAXA [47] has a more specific guidelines for manual soldering that mostly follow
recommendations by Murata and TDK.
Most manufacturers of MLCCs (see for example, [5, 31, 134, 135]) have similar guidelines to reduce the risk of
cracking in case of rework or hand-soldering. These recommendations can be summarized as follows:
1.   Direct contact by a soldering iron tip often causes thermal cracks, so the tip should be applied to the contact
     pad only. Use a soldering tip no greater than 0.120" [3.0 mm] in diameter, and transmit the heat through the
     soldering material to prevent contact with MLCC. The power of the soldering iron should be limited to 30 W
     (some manufacturers allow up to 60 W), and the duration of the process should not exceed 5 sec (preferably,
     a few seconds).
2.   If lands are different, solder the smaller land first, and remove the tip quickly when the fillet is formed. The
     fillet should have a concave profile and be at least 25% of the chip height. Excess solder might cause
     mechanical stresses on components, increase the probability of flex cracking and thereby diminishing
     reliability. All thermal shock studies supported a moderate amount of solder, with excessive solder leading
     to a greater susceptibility to fault.
3.   Compared to local heating with a soldering iron, air heaters result in a more uniform temperature distribution
     and a lesser thermal shock, so the hot air approach provides a more benign hand solder technique compared
     to soldering iron. Murata suggests setting a hot air outlet at a temperature 400 °C, application of the tool at a
     distance more than 5 mm and at the angle of 45º for less than 10 sec. When removal of a chip capacitor is
     necessary, a hot air pencil is the preferred tool.
4.   After soldering, allow the chip to cool at room ambient conditions. Using forced cool air or refrigerated air
     for expediting the cooling process is not recommended and can create thermal shock cracks.
5.   Some manufacturers specify different tip temperatures for different size capacitors. For example, ESA limits
     the maximum tip temperature, Tmax, to 340 °C [133], Murata allows Tmax 350 °C for capacitors of size 1206
     and less and 280 °C for larger parts, whereas ATC limits tip temperature to 285 °C for all parts. Panasonic
     requires 270 °C for size 0805 capacitors and smaller and below 250 °C for size 1206 to 1812. It is unlikely
     that this difference is due to different thermal resistance and quality of the product from different
     manufacturers. Most probable, it reflects different experience with field failures and possibly different
     techniques used for testing. In any case, it would be reasonable to use the lowest tip temperature setting
     possible.
6.   Preheating of the board and capacitor is likely the most important condition for safe soldering. Most
     recommendations suggest preheating by a hot plate or hot air flow to 150 °C minimum. Some manufacturers
     call for different preheating temperatures for different size capacitors. Panasonic requires preheating to a
     temperature that is 150 °C below the soldering temperature (the delta temperature, ∆T = 150 °C) for case size
     1206 and smaller and 130°C for 1210 to 1812. Novocap suggests ∆T = 100 °C for case size 1812 and smaller
     and 50 °C for larger than 1812. According to Johanson Dielectrics ∆T should be approximately 100 °C. Some
     internal OEM guidelines suggest ∆T as low as 40 °C. Apparently, low ∆T values would improve safety of the
     process but might be harmful to other components on the board. During rework, the populated and tested
     boards cannot be exposed to high temperatures, so in practice the preheating temperature and possible level
     of ∆T should be determined in each case separately.

To be published on nepp.nasa.gov.                                                                                        63
To illustrate the effect of preheating, several groups of case size 0603 BME 0.01 µF, 25 V capacitors have been
soldered onto similar FR4 boards using manual and reflow soldering. Manual soldering was carried out with different
tip sizes (0.03” and 0.08”) and different preheating temperatures of the board: cold (22°C) and hot (150 °C). After
soldering, the parts were inspected visually and tested for breakdown voltages. Results of the inspection and
measurements are displayed on Fig. 8.1. Visual examinations and cross-sectioning confirmed formation of cracks in
capacitors manually soldered onto a cold PWB, whereas no defects were observed in MLCCs after solder reflow and
after manual soldering onto a board preheated to 150 °C. Soldering iron tips of larger size increased the probability
of failures during manual soldering from ~20% for 0.03” to ~70% for 0.08”.

                                          BME 0603 0.01uF 25V capacitors Mfr.M
                               99




                                     manual soldering, cold FR4 PWB
                                                                                                                              crack


   cumulative probability, %
                               50




                               10                                      initial
                                                                       FR4 PCBsoldered by paste reflow
                               5                                       FR4 PCBat 150C, manual sold., 0.08" tip at 350C
                                                                       FR4 PCBat 22C, manual sold., 0.03" tip at 350C
                                                                       FR4 PCBat 22C, manual sold., 0.08" tip at 350C
                               1
                               100            400            700       1000              1300               1600

                                                         breakdown voltage, V                                            a)           b)

Figure 8.1. Distributions of breakdown voltages in 25 V, size 0603 capacitors (a) and examples of failed parts (b).
  MLCCs have been soldered onto FR4 boards using four methods: (i) standard reflow, (ii) assembly onto a PWB
preheated to 150 °C using a soldering iron with 0.08” tip at 350 °C, (iii) manual soldering onto a cold PWB using a
           0.08” tip at 350 °C, and (iiii) manual soldering onto a cold PWB using a 0.03” tip at 350 °C.

                                      •      Effect of touch-up
A touch-up with a soldering iron is often used after reflow soldering to improve appearance of the solder fillets and
make them look nice and in compliance with the workmanship requirements. One of the reasons of cracking during
the touch-up is thermal shock. Similar to manual soldering, hot air pencil creates lesser temperature gradients and is
preferable for touch-up to soldering iron.
Another reason of cracking caused by the manual touch-up with a soldering iron is related to CTE mismatch between
the board and ceramic capacitor. During the touch-up on a cold board, the capacitor heats up instantly and slightly
expands (∆L in Fig. 8.2a). After solidification of the solder, the capacitor tries to shrink back, but its deformation is
limited by the board, so tensile stresses develop. An example of a touch-up induced cracking in a case size 0402
capacitor is shown in Fig. 8.2.b.
Because CTE of the board is greater than of a ceramic capacitor, compressive stresses in the part develop after reflow
soldering. Ceramic materials can tolerate compressive stresses that are approximately an order of magnitude greater
than tensile stresses and normally, no failures occurs after reflow soldering. However, formation of tensile stresses
after touch-up might increase the probability of cracking substantially. If improvements in soldering and touch-up are
necessary, preheating might be still useful because it expands the board and thus reduces the stress that can be relaxed
during the following slow cooling because of creeping and stress relaxation in solder.




To be published on nepp.nasa.gov.                                                                                                      64
                                                                   a)                                b)
 Figure 8.2. Formation of cracks caused by touch-up with a soldering iron (a) and an example of cracks formed by
                          touch-up in X7R case size 0402 1000 pF 50 V capacitors (b).

    8.2. Selecting capacitors robust to manual soldering
Data presented in this report show that no single inspection or testing provides reliable information regarding the
susceptibility of a lot of capacitors to cracking. However, some tests have been shown to have a greater sensitivity
than the others. These tests include monitoring of leakage currents during humidity testing after temperature cycling
for capacitors soldered onto PWBs, acoustic microscopy, analysis of distributions of MOR, DF and IR. Another
useful test that is described below is the terminal solder dip testing (TSD). A combination of these tests can be used
to select the most robust to manual soldering capacitors and mitigate risks of failure.

             •    Terminal solder dip testing
Solder dip testing that is used in military and space applications requires immersing into molten solder at a relatively
low temperature (230 °C) that is typically less than the temperature of the soldering iron and simulates wave soldering
conditions rather than thermal stresses specific to manual soldering.
The terminal solder dip test is a modification of the standard solder dip testing that can be used to simulate conditions
of manual soldering more adequately [136]. During this test, one terminal of a capacitor is clamped in a fixture while
the other is touching molten solder (see Fig.8.3). This eliminates local pressure to ceramic and unpredictable changes
in the temperature distribution caused by application of tweezers, stabilizes temperature at the clamped terminal, and
creates a significant temperature gradient at another terminal. Experiments with the solder pot temperatures varying
from 300 °C to 350 °C showed that practically no failures of large size capacitors occur at 300 °C, some cracks appear
at 325 °C, and a much better discrimination of the lots regarding their robustness to soldering stresses can be achieved
at 350 °C, TSD350 test. The latter condition also corresponds to the maximum soldering iron temperature
recommended by manufacturers and is still less than the temperatures used sometimes during assembly of hybrid
microcircuits (up to 400 °C).
During TSD350 testing, one terminal of each capacitor is dipped for 3-5 seconds into a pot of molten solder heated to
350 °C and then the parts are left to cool at room temperature for ~2-3 minutes. Typically, the dipping and cooling
procedures are repeated three times for each part, after which all capacitors are examined visually and electrically.
Experiments using different lots of X7R MLCCs from five vendors using large size, (from 1210 to 2220) with 10 to
20 samples in a group showed that approximately half of the 26 tested lots can pass TSD350 without cracking (Fig

To be published on nepp.nasa.gov.                                                                                     65
8.3.b). Approximately 60% of lots had less than 10% of cracks but ~ 20% had more than half of capacitors with
cracks. Note that post TSD350 environmental tests in humidity chamber showed that not all capacitors with cracks
have electrical failures. Obviously, shallow cracks that are not affecting active areas of capacitors do not cause
failures.

                                                                                              100       Results of TSD350 testing
                                                                                               90




                                                                    cumulative frequency, %
                                                                                               80
                                                                                               70
                                                                                               60
                                                                                               50
                                                                                               40
                                                                                               30
                                                                                               20
                                                                                               10
                                                                                                0
                                                                                                    0      20        40       60        80     100
                                                                                                         proportion of cracked capacitors, %
                                                               a)                                                                                    b)
Figure 8.3. A set-up for terminal solder dip testing with a simple fixture that can be used to test 5 samples at a time
(a) and distribution of the percentage of lots of capacitors having a certain proportion of cracks after TSD350 based
             on testing of 26 lots (b). The insert in (b) shows a typical crack caused by TSD350 testing.
A relatively high robustness of MLCCs toward solder dip testing is mostly due to a high compressive strength of
ceramic materials. Also, an increased thermal conductivity of capacitor along the metal plates mitigates the effect of
high temperature gradients developed when the heat from molten solder is transferred to MLCC.
Two groups of tested capacitors were from two case studies when a large proportion of capacitors that have been
soldered manually onto the flight cards had cracks. These cards had been reworked and MLCCs had been replaced
with similar CDR-style capacitors from other batches. No cracking was observed on the cards after rework. Twenty
virgin capacitors from the failed lots, as well as samples from the replacement lots have been tested by TSD350. In
the first case, capacitors from the failed lot had 55% of failures whereas reference parts had zero failures. In the
second case, all 20 samples from the failed lot had severe cracking, whereas only one shallow crack out of 20 samples
had been detected in parts from the replacement lot.
Results show that different lots of military grade MLCCs might have different susceptibility to fracturing during
manual soldering and TSD350 testing can reveal this difference.

              •   Assessment of the susceptibility to cracking
Tests and inspections that can be used for revealing MLCCs with cracks include temperature cycling after soldering
onto test boards followed by monitored humidity testing, TSD350, and ultrasonic inspections (C-SAM). A
combination of these tests is likely the most effective means to assess the robustness of MLCCs toward manual
soldering stresses. Several types of tests that might be used for different level projects are presented in Fig. 8.4. Here,
L1, L2, and L3 correspond to different levels of projects as they are defined in [137]. Note, that the criticality of
MLCCs’ applications should be also considered, and in cases when short circuit of a capacitor would result in a single
point failure and/or significant loss of the system’s functions, the level of scrupulosity during testing should be
increased. Also, large size PME capacitors are especially sensitive to cracking under manual soldering and require
extra precautions.
Groups of 20 samples minimum are suggested for test flows described below. For level 1 projects, a test flow in Fig.
8.4.a that includes manual soldering onto a test PWB that simulates actual soldering conditions is preferable.
However, when details of soldering conditions are not known, the parts might be stressed by TSD350 as described in
the flow in Fig. 8.4.b. One of the benefits of the second option is that it does not require soldering onto a board and
thus eliminates problems with faulty leakage currents along the board during humidity testing.
For level 2 projects (Fig. 8.4.c), TSD350 can be also optional, and can be replaced by actual manual soldering onto a
test board. A simple visual examination and electrical measurements after TSD350 are suggested to mitigate risks of
failures for level 3 projects (Fig. 8.4.d).

To be published on nepp.nasa.gov.                                                                                                                         66
                                                          a)                                                              b)




                                                          c)                                                              d)
 Figure 8.4. Test flows for the resistance to manual soldering testing for different level projects: L1 (a) –preferred,
                                       (b)-optional, L2 (c), and L3 (d) projects.

9. Conclusion
High-temperature manufacturing processes and materials with different CTEs that are used in MLCCs result in
significant built-in mechanical stresses. Deviations from the optimal conditions and some anomalies in the
manufacturing process might form hidden defects and reduce the strength of the parts. Additional thermo-mechanical
stresses associated with soldering and post-soldering handling of the assemblies can increase stresses to the level
sufficient for cracking. These cracks might not affect performance of the system initially, but result in failures with
time of operation.
The existing military and space specifications are focused mostly on the quality of as build capacitors and do not
address properly effects of soldering and post soldering stresses. Improvements in the existing qualification
procedures and using tests that would reflect adequately environmental stresses experienced by capacitors after
assembly is necessary to reduce risks of failures during applications.
In spite of substantial efforts that have been made to develop methods for revealing cracks in MLCCs after soldering,
none is universal and can detect defective parts reliably.
Replacement of large size PME capacitors with a smaller size, thin dielectric BME capacitors with flexible
terminations might reduce risks of cracking and failures in space systems.



To be published on nepp.nasa.gov.                                                                                    67
The probability of cracking caused by manual soldering depends on the level of external stresses that is controlled by
the workmanship and the robustness of MLCCs that depends on the level of built-in stresses, presence of defects and
mechanical strength, and is lot-related. To mitigate risks of manual soldering and reduce the probability of cracking-
related failures both, a tighter workmanship control and selection of parts robust against manual soldering stresses is
necessary. Procedures to select MLCCs most resilient to manual soldering are suggested.

10.      References
[1]    A.Fletcher. (2018). Restricted MLCC supply focuses on re-design activity. Available:
       https://www.electronicspecifier.com/around-the-industry/restricted-mlcc-supply-focuses-on-re-design-
       activity[7/1/2018
[2]    P. Ming-Jen and C. A. Randall, "A brief introduction to ceramic capacitors," Electrical Insulation Magazine, IEEE, vol. 26,
       pp. 44-50, 2010
[3]    D. Brown, "Oxygen vacancy migration in MLCCS," in 2018 Pan Pacific Microelectronics Symposium (Pan Pacific), 2018,
       pp. 1-6.
[4]    C.Hendricks, "Concerns with the long term reliability of MLCC for decoupling," presented at the Reliability and Energy
       Storage in Capacitors Workshop, Center for dielectric studies, PSU, 2011.
[5]    L. Lambert. (2014). Damage Prevention When Soldering Ceramic Chip Capacitors Available:
       http://www.eptac.com/webinars/presentations/eptac_09_17_14.pdf
[6]    D. M. Zogbi, "ELECTRONIC COMPONENTS FOR THE DEFENSE & AEROSPACE SECTOR: WORLD MARKETS, TECHNOLOGIES
       AND OPPORTUNITIES: 2017-2022," in Paumanok Publications, Inc., 2018,
[7]    "The Reliability of Multilayer Ceramic Capacitors, report NMAB-400," Washington DC 1983,
[8]    A. Teverovsky, "Thermal Shock Testing and Fracturing of MLCCs under Manual Soldering Conditions," IEEE Transactions
       on Device and Materials Reliability vol. 12, pp. 413-419, 2012
[9]    D. L. Kinser, S. M. Graff, and S. V. Caruso, "The relationship between reliability and bonding techniques in hybrid
       systems," IEEE Transactions on parts, hybrids, and packaging, vol. PHP-11, pp. 195-201, Sept. 1975 1975
[10]   B. Sloka, D.Skamser, A. Hill, M. Laps, R. Grace, J. Prymak, et al., "Flexure Robust Capacitors," in The 27th symposium for
       passive components, CARTS'07, Albuquerque, NM, 2007.
[11]   J. Maxwell. (2006). Capacitor Cracks: Still with Us after All These Years. Available:
       http://www.johansondielectrics.com/technicalnotes/cra/
[12]   S. Haishan and C. Shoutian, "Charge-discharge breakdown of dielectric ceramic," in 6th Intemational Conference on
       Properties and Applications of Dielectric Materials, Xi'an, China, 2000, pp. 1029-1032.
[13]   L. Bin, C. Wei, Z. Yajie, and C. Shoutian, "Distribution regularity of breakdown field strength of high voltage ceramic
       capacitor," in Proceedings of the 6th International Conference on Properties and Applications of Dielectric Materials,
       2000., 2000, pp. 1037 - 1040.
[14]   J. Maxwell, "Cracks: the hidden defect," in Proceedings of the 38th Electronics Components Conference, 1988, pp. 376-
       384.
[15]   T. Brennan, "Ceramic Capacitor Insulation Resistance Failures Accelerated by Low Voltage," IEEE transactions on electron
       devices, vol. ED-26, pp. 102-108, 1979
[16]   B. V. Hiremath, "Evaluation of tumbling processes of multilayer ceramic capacitors for surface mount device
       applications," IEEE Transactions on Components, Hybrids, and Manufacturing Technology, vol. 16, pp. 822-827, 1993
[17]   J. Maxwell. (2007). Basics of Ceramic Chip Capacitors. Available:
       https://www.johansondielectrics.com/downloads/jdi_mlcc-basics_2007-12.pdf
[18]   EIA-198-1, 2002, Ceramic Dielectric Capacitors Classes I, II, III and IV – Part I: Characteristics and Requirements,
       https://ewb.ihs.com/#/document/VYVRABAAAAAAAAAA?qid=636682241794939520&sr=re-1-
       10&kbid=4%7C20027&docid=941257214#h961943d3
[19]   R. C. Buchanan, Ceramic materials for electronics: Marcel Dekker, Inc, 2004.
[20]   Tutorial, "Passive Electronic Component Reliability and Selection Criteria," in CARTS, Las Vegas, NV, 2012.
[21]   H. Kishi, Y. Mizuno, and H. Chazono, "Base-metal electrode-multilayer ceramic capacitors: Past, present and future
       perspectives," Japanese Journal of Applied Physics Part 1, vol. 42, pp. 1-15, Jan 2003 <Go to
       ISI>://WOS:000181161300001
[22]   "Recent Topics in the Field of Ferroelectric Materials for BME-MLCCs," in Proceedings of the 12th Pacific Rim Conference
       on Ceramic and Glass Technology, ed, 2018.
[23]   M. R. Opitz, K. Albertsen, J. J. Beeson, D. F. Hennings, J. L. Routbort, and C. A. Randall, "Kinetic Process of Reoxidation of
       Base Metal Technology BaTiO3-Based Multilayer Capacitors," Journal of the American Ceramic Society, vol. 86, pp. 1879-
       1884, 2003 https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1151-2916.2003.tb03576.x
[24]   J. Maxwell, "Understanding Ceramic Capacitor Terminations," 2006, http://www.johansondielectrics.com/technical-
       notes/general/understanding-ceramic-capacitor-terminations.html.

To be published on nepp.nasa.gov.                                                                                                68
[25]   L. A. Mann, S. P. Gupta, and L. G. Jones, "The Influence of Termination Properties on the Thermal Shock and Thermal
       Cycle Performance of Surface Mount Multilayer Ceramic Capacitors," in Electronic Components and Technology
       Conference, 1991, pp. 437-441.
[26]   P. Xiao, Z. Tan, and Y. Deng, "Analysis on Discoloration of MLCC Dielectric in DPA," in CARTS USA, Jacksonville, Florida,
       USA, 2009, pp. 289-297.
[27]   J. W. Park, J. H. Chae, I. H. Park, H. J. Youn, and Y. H. Moon, "Thermo-mechanical stresses and mechanical reliability of
       multilayer ceramic capacitors (MLCC)," Journal of the American Ceramic Society, vol. 90, pp. 2151-2158, Jul 2007 <Go to
       ISI>://WOS:000247756500028
[28]   A. Teverovsky, "Susceptibility to Cracking of Different Lots of CDR35 Capacitors," NASA/GSFC, Greenbelt, MD, NEPP
       report 2017, https://nepp.nasa.gov/files/29210/NEPP-TR-2018-Teverovsky-CDR35-Capacitors-TN52049.pdf
[29]   B. S. Rawal, R. Ladew, and R. Garcia, "Factors responsible for thermal shock behavior of chip capacitors," AVX technical
       information, 1987 http://www.avx.com/docs/techinfo/factors.pdf
[30]   D. K. Eli Bershadsky. (2016). Vishay Vitramon MLCC End Termination. Available:
       https://www.vishay.com/docs/45063/tn0029.pdf
[31]   Murata, 2017, Chip Multilayer Ceramic Capacitors for Automotive,
       https://www.murata.com/~/media/webrenewal/support/library/catalog/products/capacitor/mlcc/c03e.ashx?la=en-us
[32]   C. A. J.Prymak, P.Blais, "Flexible termination - reliability in stringeent environments," presented at the 29'th Passive
       Components Symposium, CARTS USA, Jacksonville, FL, 2009.
       https://www.mouser.com/pdfdocs/FlexibleTerminationAbstract.pdf
[33]   TDK-Tech_Notes, Flex crack contermeasures in MLCCs,
       (https://product.tdk.com/info/en/products/capacitor/ceramic/mlcc/technote/solution/mlcc02/index.html
[34]   A. Teverovsky and J. Herzberger, "Humidity Testing of PME and BME Ceramic Capacitors with Cracks," in CARTS
       International, Santa Clara, CA, 2014, pp. 15-29.
[35]   EIA-469_D, 2006, STANDARD TEST METHOD FOR DESTRUCTIVE PHYSICAL ANALYSIS (DPA) OF CERAMIC MONOLITHIC
       CAPACITORS,
[36]   R. Demco, "Ni Electrode for Auto Grade and High Reliability Applications," in Components for Military and Space
       Electronics, CMSE'15, Los Angeles, CA, 2015, p. 3.1.
[37]   J. Marshall, "Ceramic Capacitor B.M.E. Technology and future developments for Space, Military Applications," in 21st
       Components for Military and Space Electronics, CMSE'17, Los Angeles, CA, 2017, p. 2.6.
[38]   KEMET, 2008, Flex Crack Mitigation, Tech Topic,
       https://www.mouser.com/pdfdocs/TechnicalOverviewofFlexMitigationSolutions.pdf
[39]   TDK, 2013, High Reliability Automotive Use MLCCs,
       https://product.tdk.com/en/techlibrary/archives/vol06_mlcc/TDK_TJ_CAR_E_0711.pdf
[40]   Tayloredge, Failure mechanisms in ceramic capacitors,
       https://www.tayloredge.com/reference/Electronics/Capacitors/MLC_FailureMechanisms.pdf
[41]   D. Friedlander, "The use of COTS components in space: debunking 10 myths," Intelligent aerospace, July, 5 2017
       https://www.intelligent-aerospace.com/articles/2017/10/electrical-electronic-and-electromechanical-cots-components-
       in-space-penalizing-policy.html
[42]   D. Friedlander, "COTS in space: the 100 percent testing risk," Intelligent aerospace, November, 13 2017
       https://www.intelligent-aerospace.com/articles/2017/10/electrical-electronic-and-electromechanical-cots-components-
       in-space-penalizing-policy.html
[43]   NASA_GSFC, 2015, SPECIFICATION CONTROL DRAWING Capacitor, Ceramic, Multilayer Chip, Space Applications, S-311-
       P-829, http://www.presidiocomponents.com/products/S-311-P-829-Rev-J.pdf
[44]   NASA_GSFC, 2016, SPECIFICATION CONTROL DRAWING Capacitor, Ceramic, Multilayer Chip, Space Applications, S-311-
       P-838, https://nepp.nasa.gov/files/27161/S-311-P-838A.pdf
[45]   ESCC-3009, 2017, CAPACITORS, FIXED, CHIPS, CERAMIC DIELECTRIC, TYPES I AND II, ESCC Generic Specification No. 3009,
       https://escies.org/download/specdraftapppub?id=3232
[46]   JAXA-QTS-2040/M, 2016, "CAPACITORS, MINIATURE, HIGH-CAPACITY, SURFACE MOUNT, FINE CERAMIC DIELECTRIC
       (J2040/M105), HIGH RELIABILITY, SPACE USE, DETAIL SPECIFICATION FOR",
       https://eeepitnl.tksc.jaxa.jp/en/qts/q_level_1/QAE2040_M105B.pdf
[47]   JAXA-ADS-2040/M105, 2012, "APPLICATION DATA SHEET FOR COMMON PARTS/MATERIALS, SPACE USE",
       https://eeepitnl.tksc.jaxa.jp/en/ads/a_level_1/AAE2040_M105.pdf
[48]   AEC-Q200, 2010, STRESS TEST QUALIFICATION FOR PASSIVE COMPONENTS, AEC-Q200 REV D,
       http://www.aecouncil.com/Documents/AEC_Q200_Rev_D_Base_Document.pdf
[49]   MIL-STD-690, 2013, FAILURE RATE SAMPLING PLANS AND PROCEDURES,
       https://landandmaritimeapps.dla.mil/Downloads/MilSpec/Docs/MIL-STD-690/std690.pdf
[50]   D. Liu, "How to Select/Screen/Quality Conformance Inspection (QCI) BME Capacitors for Space Applications," presented
       at the ETW, NASA/GSFC, 2013. https://nepp.nasa.gov/files/24681/Liu_2013_n217_NEPPETW_Pres_QCI.pdf


To be published on nepp.nasa.gov.                                                                                            69
[51]   "JAXA Report," in G-12 Meeting. San Antonio, TX, 2012,
[52]   Y. Yamada, "Introduction of Small Size MLCC to Aero-Space Application and its technology, Murata," presented at the
       ESA 1st International Symposium 'Space Passive Component Days', Noordwijk, The Netherlands, 2013.
       https://escies.org/webdocument/showArticle?id=984&groupid=6
[53]   ASTM, "C1525-04," in Standard Test Method for Determination of Thermal Shock Resistance for Advanced Ceramics by
       Water Quenching, 2009,
[54]   J. d. Toonder, C. Rademaker, and C. Hu, "Residual stresses in multilayer ceramic capacitors: measurement and
       computation," Journal of Electronic Packaging, vol. 125, pp. 506-511, 2003
[55]   G. Yang, Z. Yue, T. Sun, W. Jiang, X. Li, and L. Liz, "Evaluation of Residual Stress in a Multilayer Ceramic Capacitor and its
       Effect on Dielectric Behaviors Under Applied dc Bias Field," Journal of American Ceramic Society, vol. 91, pp. 887-892,
       2008
[56]   M. Sampson, J. Brusse, and A. Teverovsky, "Humidity Steady State Low Voltage Testing of MLCCs (Based on NESC
       Technical Assessment Report)," in CARTS USA, Jacksonville, Fl, 2011.
[57]   A. Raman, S. Sahasrabudhe, L. Dietz, and M. Hossain, "Phenomenological understanding of Sn migration in ceramic-chip
       capacitors," in Electronic Components and Technology Conference (ECTC), 2011 IEEE 61st, 2011, pp. 541-546.
[58]   J. Maxwell.) Surface mount soldering techniques and thermal shock in multilayer ceramic capacitors. AVX Technical
       information issue, pp., Available: http://www.avx.com/docs/techinfo/soldmlc.pdf
[59]   G. De With, "Structural integrity of ceramic multilayer capacitor materials and ceramic multilayer capacitors," Journal of
       the European Ceramic Society, vol. 12, pp. 323-336, 1993 <Go to ISI>://A1993MK16700001
[60]   B. Rawal, M. Childs, A. Cooper, and B. McLaughlin, "Reliability of multilayer ceramic capacitors after thermal shock,"
       Proceedings of the 38th Electronics Components Conference, pp. 371 - 375, 9-11 May 1988 1988
[61]   Y. C. Chan, Y. Wang, Z. Gui, and L. Li, "Thermal effects on the dielectric and electrical properties of relaxor ferroelectric
       ceramic-based MLCs," in Proceedings of 1995 Japan International, 18th IEEE/CPMT Electronic Manufacturing Technology
       Symposium, International Omiya, 1995, pp. 328-333.
[62]   C. Koripella, "Mechanical behavior of ceramic capacitors," IEEE Transactions on Components, Hybrids, and
       Manufacturing Technology, vol. 14, pp. 718 - 724, 1991
[63]   J. D. Prymak and J. Bergenthal, "Capacitance Monitoring while Flex Testing," IEEE transactions on components,
       packaging, and manufacturing technology, part A, vol. 18, pp. 180-186, 1995
[64]   J. A. Ahmar, E. Wiss, and S. Wiese, "Four-point-bending experiments on multilayer ceramic capacitors: Microstructural
       details on crack initiation and propagation," in 2018 19th International Conference on Thermal, Mechanical and Multi-
       Physics Simulation and Experiments in Microelectronics and Microsystems (EuroSimE), 2018, pp. 1-6.
[65]   K. Franken, H. R. Maier, K. Prume, and R. Waser, "Finite-Element Analysis of Ceramic Multilayer Capacitors: Failure
       Probability Caused by Wave Soldering and Bending Loads," Journal of the American Ceramic Society, vol. 83, pp. 1433-
       1440, 2000 http://dx.doi.org/10.1111/j.1151-2916.2000.tb01407.x
[66]   M. Keimasi, M. H. Azarian, and M. G. Pecht, "Flex Cracking of Multilayer Ceramic Capacitors Assembled With Pb-Free
       and Tin–Lead Solders," IEEE transactions on device and material reliability, vol. 8, pp. 182-192, 2008
[67]   J. Prymak, M. Prevallet, P. Blais, and B. Long, "New Improvements in Flex Capabilities for MLC Chip Capacitors," in The
       26th symposium for passive components, CARTS'06, Orlando, FL, 2006, pp. 63-76.
[68]   J. Al Ahmar, E. Wiss, S. Wiese, and Ieee, "Fracture Probability of MLCC in Dependence of Solder Fillet Height," 2017 18th
       International Conference on Thermal, Mechanical and Multi-Physics Simulation and Experiments in Microelectronics and
       Microsystems (Eurosime), 2017 <Go to ISI>://WOS:000403217700045
[69]   T. Adams, "Preventing MLCC Failures," Circuits assembly, August 2009 http://www.circuitsassembly.com/cms/sea-
       award/8686-preventing-mlcc-failures
[70]   Murata. (2007, Capacitance and Dissipation Factor Measurement of Chip Multilayer Ceramic Capacitors. (TD No.C10E).
       Available:
       https://www.murata.com/~/media/webrenewal/support/faqs/products/capacitor/mlcc/char/0007/07_capmeasureen.a
       shx?la=en
[71]   JohansenDielectrics. (2005, AC power computation for DC rated capacitors. Available:
       https://www.johansondielectrics.com/downloads/jdi-ac-power-2005-05.pdf
[72]   A. Teverovsky, "The Effectiveness of Screening Techniques for Revealing Cracks in High Volumetric Efficiency MLCCs," in
       46th International Symposium on Microelectronics, IMAPS, Orlando, FL, 2013.
       https://nepp.nasa.gov/files/24723/2013_n241_Teverovsky_IMAPS_Paper.pdf
[73]   A. Teverovsky, "Insulation Resistance and Leakage Currents in Low-Voltage Ceramic Capacitors With Cracks,"
       Components, Packaging and Manufacturing Technology, IEEE Transactions on, vol. 4, pp. 1169-1176, 2014
[74]   P. C. Dow, "An Analysis of Certain Errors in Electronic Differential Analyzers II-Capacitor Dielectric Absorption," Electronic
       Computers, IRE Transactions on, vol. EC-7, pp. 17-22, 1958




To be published on nepp.nasa.gov.                                                                                                70
[75]   A. Teverovsky, "Leakage Currents in Low-Voltage PME and BME Ceramic Capacitors," presented at the 7th International
       Conference on Electroceramics (ICE2015), Penn State Conference Center, State College PA, USA, 2015.
       https://nepp.nasa.gov/
[76]   A. Teverovsky, "Breakdown voltages in ceramic capacitors with cracks," IEEE Transactions on Dielectrics and Electrical
       Insulation, vol. 19, pp. 1448-1455, 2012
[77]   EPCOS. Multi Layer Serial Ceramic Capacitor, 2005. Available: http://www.epcos.fr/Produits/pdf/Presentation_MLSC.pdf
[78]   A. Teverovsky, "The Significance of Breakdown Voltages for Quality Assurance of Low-Voltage BME Ceramic Capacitors,"
       in CARTS International, Santa Clara, CA, 2014, pp. 129-144.
[79]   A. Teverovsky, "Effect of Manual-Soldering-Induced Stresses on Ceramic Capacitors," NASA Electronic Parts and
       Packaging (NEPP) Program, Part I 2008, https://nepp.nasa.gov/files/16346/08_002_01%20GSFC%20Teverovsky.pdf
[80]   A. Teverovsky, "Mechanical Testing of MLCCs," NASA/GSFC, Greenbelt, MD, NEPP report 2016,
       https://nepp.nasa.gov/files/27587/NEPP-TR-2016-Teverovsky-TGR-Paper-MLCCs-TN39992.pdf
[81]   S. Meyer, H. Wohlrabe, K. J. Wolter, H. Rcuter, and M. Keil, "Investigations on the mechanical stability and integrity of
       chip components after picking and placing in the surface mount technology process chain," in Electronics Packaging
       Technology Conference (EPTC 2013), 2013 IEEE 15th, 2013, pp. 873-877.
[82]   S. K. Dash, P. Kumar, M. P. James, S. Kamat, K.Venkatesh, V.Venkatesh, et al., "Study of Cracks in Ceramic Chip
       Capacitors (CDR-05) of Two Different Makes," International Journal of Emerging Technology and Advanced Engineering,
       vol. 3, pp. 85-90, 2013
[83]   M. Szutkowska, "Fracture toughness of advanced alumina ceramics and alumina matrix composites used for cutting tool
       edges," Journal of Acheivements in Materials and Manufacturing Engineering, vol. 54, 2012
[84]   D. B. Marshall, R. F. Cook, N. P. Padture, M. L. Oyen, A. Pajares, J. E. Bradby, et al., "The Compelling Case for Indentation
       as a Functional Exploratory and Characterization Tool," Journal of the American Ceramic Society, vol. 98, pp. 2671-2680,
       Sep 2015 <Go to ISI>://WOS:000362229400001
[85]   J. J. Steppan, J. A. Roth, L. C. Hall, D. A. Jeannotte, and S. P. Carbone, "A review of corrosion failure mechanisms during
       accelerated tests - electrolytic metal migration," Journal of the Electrochemical Society, vol. 134, pp. 175-190, Jan 1987
       <Go to ISI>://WOS:A1987F664400035
[86]   M. J. Ditz and I. N. T. Asm, Determination of the moisture threshold for silver migration, 1994.
[87]   M. Ciccotti, M. George, V. Ranieri, L. Wondraczek, and C. Marlière, "Dynamic condensation of water at crack tips in
       fused silica glass," Journal of Non-Crystalline Solids, vol. 354, pp. 564-568, 2008/01/15/ 2008
       http://www.sciencedirect.com/science/article/pii/S002230930701109X
[88]   J. Herzberger and A. Teverovsky, "Dendrite growth in PME and BME ceramic capacitors," in CARTS International,
       Houston, TX, 2013, pp. 3.3 1-25. https://nepp.nasa.gov/
[89]   J. C. Lin and J. Y. Chan, "On the resistance of silver migration in Ag-Pd conductive thick films under humid environment
       and applied d.c. field," Materials Chemistry and Physics, vol. 43, pp. 256-265, 1996
       http://www.sciencedirect.com/science/article/pii/0254058495016428
[90]   N. J. Donnelly and C. A. Randall, "Refined Model of Electromigration of Ag/Pd Electrodes in Multilayer PZT Ceramics
       Under Extreme Humidity," Journal of the American Ceramic Society, vol. 92, pp. 405-410, Feb 2009 <Go to
       ISI>://000263358000017
[91]   S. J. Krumbein, "METALLIC ELECTROMIGRATION PHENOMENA," Ieee Transactions on Components Hybrids and
       Manufacturing Technology, vol. 11, pp. 5-15, Mar 1988 <Go to ISI>://WOS:A1988M705300002
[92]   U. Kumar Barik, S. Srinivasan, C. L. Nagendra, and A. Subrahmanyam, "Electrical and optical properties of reactive DC
       magnetron sputtered silver oxide thin films: role of oxygen," Thin Solid Films, vol. 429, pp. 129-134, 2003
       http://www.sciencedirect.com/science/article/pii/S0040609003000646
[93]   S. A. Yang and A. Christou, "Failure model for silver electrochemical migration," Ieee Transactions on Device and
       Materials Reliability, vol. 7, pp. 188-196, Mar 2007 <Go to ISI>://WOS:000248067500023
[94]   P. S. Patil and L. D. Kadam, "Preparation and characterization of spray pyrolyzed nickel oxide (NiO) thin films," Applied
       Surface Science, vol. 199, pp. 211-221, 2002 http://www.sciencedirect.com/science/article/pii/S0169433202008395
[95]   B. Jiang, Y. Bai, J. L. Cao, Y. J. Su, S. Q. Shi, W. Y. Chu, et al., "Delayed crack propagation in barium titanate single crystals
       in humid air," Journal of Applied Physics, vol. 103, Jun 2008 <Go to ISI>://WOS:000256706200131
[96]   H. Zhang, J. X. Li, W. Y. Chu, Y. J. Su, and L. J. Qiao, "Effect of humidity and hydrogen on the promotion of indentation
       crack growth in lead-free ferroelectric ceramics," Materials Science and Engineering B-Advanced Functional Solid-State
       Materials, vol. 167, pp. 147-152, Mar 2010 <Go to ISI>://WOS:000277532400004
[97]   S. F. Wang, J. P. Dougherty, W. Huebner, and J. G. Pepin, "Silver-Palladium Thick-Film Conductors," Journal of the
       American Ceramic Society, vol. 77, pp. 3051-3072, 1994 http://dx.doi.org/10.1111/j.1151-2916.1994.tb04549.x
[98]   G. DiGiacomo, Reliability of Electronic Packages and Semiconductor Devices McGrow Hill, 1996.
[99]   M. M. Samantaray, A. Gurav, E. C. Dickey, and C. A. Randall, "Electrode Defects in Multilayer Capacitors Part I: Modeling
       the Effect of Electrode Roughness and Porosity on Electric Field Enhancement and Leakage Current," Journal of the
       American Ceramic Society, vol. 95, pp. 257-263, 2012 http://dx.doi.org/10.1111/j.1551-2916.2011.04769.x


To be published on nepp.nasa.gov.                                                                                                    71
[100] M. Nakano, A. Saito, and N. Wada, "E–J Characteristics in Multilayer Ceramic Capacitors with the Thin Dielectric Layers,"
      Key Engineering Materials vol. 421-422, pp. 277-280, 2009
[101] A. Teverovsky, "Failure models for low-voltage BME ceramic capacitors with defects," in 2017 IEEE International
      Reliability Physics Symposium (IRPS), 2017, pp. 6C-5.1-6C-5.8.
[102] I. Stolichnov, A. Tagantsev, N. Setter, S. Okhonin, P. Fazan, J. S. Cross, et al., "Constant-current study of dielectric
      breakdown of Pb(Zr,Ti)O-3 ferroelectric film capacitors," Integrated Ferroelectrics, vol. 32, pp. 737-746, 2001 <Go to
      ISI>://000167524400006
[103] B. Rawal and H. Chan, "Conduction and failure mechanisms in barium titanate based ceramics under highly accelerated
      conditions"," AVX Technical information,
[104] PSA-Walsin-Tech, 2017, MLCC APPLICATION GUIDE,
      http://www.passivecomponent.com/document/MLCC/MLCC_application_guide.pdf
[105] W. P. Chen, L. T. Li, J. Q. Qi, Y. Wang, and Z. L. Gui, "Influence of electroless nickel plating on multilayer ceramic
      capacitors and the implications for reliability in multilayer ceramic capacitors," Journal of the American Ceramic Society,
      vol. 81, pp. 2751-2752, Oct 1998 <Go to ISI>://WOS:000076450800039
[106] H. Zhang, Y. J. Su, L. J. Qiao, W. Y. Chu, D. Wang, and Y. X. Li, "The effect of hydrogen on the fracture properties of
      0.8(Na1/2Bi1/2)TiO3-0.2(K1/2Bi1/2)TiO3 ferroelectric ceramics," Journal of Electronic Materials, vol. 37, pp. 368-372,
      Mar 2008 <Go to ISI>://WOS:000252483100017
[107] Y. Saito, T. Oguni, K. Uchida, J. Ikeda, K. Kawasaki, T. Nakamura, et al., "Mechanisms of MLCCs Insulation Resistance
      Degradation Under Highly Accelerated Temperature and Humidity Stress," in CARTS, Santa Clara, CA, 2014, p. 4.7.
[108] D. Sohrabi Baba Heidary and C. A. Randall, "Analysis of the degradation of BaTiO3 resistivity due to hydrogen ion
      incorporation: Impedance spectroscopy and diffusion analysis," Acta Materialia, vol. 96, pp. 344-351, 2015/09/01/ 2015
      http://www.sciencedirect.com/science/article/pii/S135964541500347X
[109] L. P. James F. Soeder, Robert Scheidegger. (2012). Capacitor Failure Investigation Results for the NEXT Ion Thruster
      Power Processing Unit (PPU). Available: https://ntrs.nasa.gov/archive/nasa/casi.ntrs.nasa.gov/20150010352.pdf
[110] O. Boser, P. Kellawon, and R. Geyer, "Electromechanical resonances in ceramic capacitors and their use for rapid
      nondestructive testing," Journal of the American Ceramic Society, vol. 72, pp. 2282-2286, Dec 1989 <Go to
      ISI>://WOS:A1989CE83100011
[111] A. Teverovsky, "Guidelines for Selection, Screening and Qualification of Low-Voltage Commercial Multilayer Ceramic
      Capacitors for Space Programs," NASA/GSFC, Greenbelt, MD 2012, http://nepp.nasa.gov/
[112] J. I. C. Andersson, E. Varescon, and M. Kiviniemi.) Imaging Detects Cracks in Multilayer Ceramic Capacitors. Power
      Electronics Europe issue 5, pp. 24-27, 2017 Available: http://www.power-
      mag.com/pdf/feature_pdf/1506960397_ABB_Feature.pdf
[113] S. Hull, "Nondestructive detection of cracks in ceramics using vicinal illumination," in 25th International Symposium for
      Testing and Failure Analysis, ISTFA, Santa Clara, CA, 1999, pp. 217-223.
[114] K. O. Sridhar Canumalla, Pedro Ramirez. Acoustic Microscopy of Tightly Closed Delaminations in Multilayer Ceramic Chip
      Capacitors. Available:
      https://www.researchgate.net/profile/Sridhar_Canumalla/publication/253547181_Acoustic_Microscopy_of_Tightly_Clo
      sed_Delaminations_in_Multilayer_Ceramic_Chip_Capacitors/links/55ca51b708aebc967dfbe183/Acoustic-Microscopy-
      of-Tightly-Closed-Delaminations-in-Multilayer-Ceramic-Chip-Capacitors.pdf
[115] M. Tarr. (2007). Failure mechanisms in ceramic capacitors. Available:
      http://www.ami.ac.uk/courses/topics/0179_fmcc/index.html
[116] R. Chittick, E. Gray, J. Alexander, M. Drake, and E. Bush, "Non-destructive screening for low-voltage failure in multilayer
      ceramic capacitors," in The 3rd Capacitor and Resistor Technology Symposium, CARTS'83, Phoenix, AZ, 1983, pp. 61-69.
[117] B. Wunderle, T. Braun, D. May, and A. Mazloum, "Non-destructive failure analysis and modeling of encapsulated
      miniature SMD ceramic chip capacitors under thermal and mechanical loading," in 13th International Workshop on
      Thermal Investigation of ICs and Systems, THERMINIC 2007., 2007, pp. 104 - 109.
[118] M. H. Azarian, "Detection of Cracked Multi-Layer Ceramic Capacitors on Printed Circuit Board Assemblies," presented at
      the IMAPS Chesapeake Chapter Summer Technical Symposium, JHU APL, Laurel, 2014.
[119] A. Teverovsky, "Absorption Voltages and Insulation Resistance in Ceramic Capacitors with Cracks," IEEE Transactions on
      Dielectrics and Electrical Insulation, vol. 21, pp. 2020-2027, 2014
[120] R. G. Leisure and F. A. Willis, "Resonant ultrasound spectroscopy," Journal of Physics-Condensed Matter, vol. 9, pp. 6001-
      6029, Jul 1997 <Go to ISI>://WOS:A1997XL95400002
[121] S. A. Kim, W. L. Johnson, G. S. White, R. Roberts, and A. S. M. International, Ultrasonic Detection of Defects in Multi
      layered Ceramic Capacitors for Active Implantable Medical Devices, 2013.
[122] W. L. Johnson, S. A. Kim, G. S. White, J. Herzberger, and Ieee, "Nonlinear resonant acoustic detection of cracks in
      multilayer ceramic capacitors," in 2014 Ieee International Ultrasonics Symposium, New York, 2014, pp. 248-251. <Go to
      ISI>://WOS:000352792500063



To be published on nepp.nasa.gov.                                                                                            72
[123] W. L. Johnson, S. A. Kim, G. S. White, J. Herzberger, K. L. Peterson, and P. R. Heyliger, "Time-domain Analysis of Resonant
      Acoustic Nonlinearity Arising from Cracks in Multilayer Ceramic Capacitors," in 42nd Annual Review of Progress in
      Quantitative Nondestructive Evaluation: Incorporating the 6th European-American Workshop on Reliability of Nde, 2016.
      <Go to ISI>://WOS:000371907800065
[124] N. H. Chan and B. S. Rawal, "An electrically-excited acoustic emission test technique for screening multilayer ceramic
      capacitors," in Electronics Components Conference, 1988., Proceedings of the 38th, 1988, pp. 502-506.
[125] S. Levikari, T. J. Kärkkäinen, C. Andersson, J. Tamminen, and P. Silventoinen, "Acoustic Phenomena in Damaged Ceramic
      Capacitors," IEEE Transactions on Industrial Electronics, vol. 65, pp. 570-577, 2018
[126] D. S. Erdahl and I. C. Ume, "Online–Offline Laser Ultrasonic Quality Inspection Tool for Multilayer Ceramic Capacitors,"
      IEEE Transactions on advanced packaging, vol. 27, pp. 647-653, 2004
[127] D. S. Erdahl and I. C. Ume, "Online-offline laser ultrasonic quality inspection tool for multilayer ceramic capacitors - Part
      II," Ieee Transactions on Advanced Packaging, vol. 28, pp. 264-272, May 2005 <Go to ISI>://WOS:000229003700014
[128] A. Teverovsky, "Evaluation of case size 0603 BME ceramic capacitors," in Components for Military and Space Electronics,
      CMSE'15, Los Angeles, CA, 2015, p. 6.2. https://nepp.nasa.gov/files/26562/2015-562-Teverovsky-Final-NEPPweb-Pres-
      CMSE-BME-TN22758.pdf
[129] IPC-7711C/7721C, 2017, Rework, Modification and Repair of Electronic Assemblies,
      https://products.ihserc.com/tmp_stamp/607629926/VWHIUFAAAAAAAAAA.pdf?sess=607629926&prod=SPECS4
[130] IPC-J-STD-001G, 2017, Requirements for Soldered Electrical and Electronic Assemblies,
[131] NASA-STD-8739.2, 2011, WORKMANSHIP STANDARD FOR SURFACE MOUNT TECHNOLOGY,
[132] ECSS-Q-ST-70-38C, 2008, Space product assurance. High-reliability soldering for surface-mount and mixed technology.,
      http://esmat.esa.int/ecss-q-st-70-38c.pdf
[133] ECSS-Q-ST-70-38C, 2017, High-reliability soldering for surface-mount and mixed technology,
      https://escies.org/download/webDocumentFile?id=66008
[134] Johansen_Technology, "SOLDERING APPLICATION NOTE FOR CERAMIC CHIP COMPONENTS," 2011
[135] ATC-AT#001-119. (2007). Recommended attachment techniques for ATC multilayer chip capacitors. Available:
      www.atceramics.com
[136] A. Teverovsky, "Terminal Solder Dip Testing for Chip Ceramic and Tantalum Capacitors," in International Conference on
      Soldering & Reliability (ICSR) Ontario, Canada, 2012, pp. 163-173.
[137] NEPAG, 2016, NASA Parts Selection List, NASA Parts Levels, https://nepp.nasa.gov/npsl/npsl_UsePolicy.htm




To be published on nepp.nasa.gov.                                                                                               73
