Microstructure evolution during sintering of multilayer ceramic capacitors: nanotomography and

                                      discrete simulations



                       Vom Fachbereich Material- und Geowissenschaften

                            der Technischen Universität Darmstadt

                            zur Erlangung des akademischen Grades

                                 Doktor-Ingenieurs (Dr.-Ing.)

                                    genehmigte Dissertation

                                              von

                                      M.Eng. Zilin YAN

                                     aus Hubei, P.R.China



           Referent:     Prof. Dr.-Ing. Olivier Guillon

           Korreferent: Prof. Dr. rer. nat. Hans-Joachim Kleebe

           Tag der Einreichung: 7. September. 2013

           Tag der mündlichen Prüfung: 17. Oktober. 2013




                                             D 17


                                        Darmstadt, 2014
                                                                                   Acknowledgements


Acknowledgements

This thesis is conducted between Technische Universität Darmstadt and Université de Grenoble
(France) in the framework of International Doctoral Programme in Functional Materials funded by the
ERASMUS MUNDUS Programme of the European Commission in the duration of 10/2010-10/2013.


I gratefully thank my supervisors Profs. Christophe L. Martin, Olivier Guillon and Didier Bouvard for
introducing me into the community of constrained sintering, and their seasoned guidance, continuous
supports and patience throughout my PhD study. I highly appreciate their insightful discussions and
comments on my monthly project reviews such that I am in a precise and correct track to the end of
this dissertation. They not only guide me, a tourist in sciences, to some altitudes, but also cultivate my
scientific attitudes. Also, I appreciate very much their offering me a plenty of academic exchanges and
professional travels that benefit the development of my career.


I sincerely express my gratitude to the European Commission for the ERASMAS MUNDUS PhD
fellowship to cover my three-year stay in France and Germany. I also thank the administrative board
of the IDS-FUNMAT program for their well organised training program as well as my PhD colleagues‟
teamwork that enhance my transferrable skills.


Thanks to the Laboratoire SIMaP/GPM2, Université de Grenoble - CNRS providing a pleasant
atmosphere to work in. Thanks to Dr. Luc Salvo and Dr. Pierre Lhuissier for their helpful discussions
when I performed the 3D imaging processing. Thank Claire, Claude for taking good care of my
employment case, professional trips and other administrative stuff such that I can concentrate on my
scientific topic. Thanks to postdocs in the lab: Dr. Xiaoxing Liu, Dr. Patrick Pizette, Dr. David
Jauffres, Dr. Hao Wang and senior PhD students Magali, lottifi, Jean-Marie, Thiboult, Audrey,
Mathilde for their assistances in helping me get integrated with my PhD study while enjoying my life
in France. Thanks to the birthday croissant and cakes, and joyful chatting which help me to appreciate
the French culture little by little. Thanks to Pawel, Edouard, Achraf, Benjamin, Denis, Loinel, Natalia,
Mateo, Jérémy for their sharing their stories, point views and exotic natures which make my daily life
pleasant.


I would like to thank Prof. Jürgen Rödel, the leader of Ceramics Group, Department of Materials
Science, Technischen Universität Darmstadt, for his kind hosting me in his group to carry out the
material characterizations. In this dynamic, international group, I have been exposed to various topics
in ceramics at the group seminars which enlighten me in a subtle way. Thanks to technical specialists
Emil, Michael, Gundel and Daniel Isaia for their supports when I carried out my experiments. Thanks

                                                                                                         i
Acknowledgements


to my colleagues: Irene, Christine, Raschid, Jiadong, Silke, Eva Anton, Eva Sapper, Yohan, Suyan,
visiting scientists Prof. Hailong Zhang, Dr. Ke Wang for their instructions to the uses of some key
instruments. Thanks to Roswita and Gila for taking care of my administrative case with patience.
Thanks to all the Ceramics Group members for their companion at the work lunch, and for the
birthday cakes and BBQs which made my sweetest memories of Darmstadt.


Thanks to Prof. Olivier Guillon for hosting me in the Mechanics of Functional Materials Group,
Institute of Materials Science & Technology (IMT), Friedrich Schiller University of Jena. Thank Mrs.
Anke Partschefeld for her administrative support. Thanks to Mr. Volker Helmig, Susanne for technical
assistances. Thanks to Mr. Ralf Wagner (IMT), Mrs. Carmen Voigt (Institute for Solid State Physics,
ISSP) for their expertise in sample preparation using FIB milling. Thanks for the companion of Jesus,
André, Benjamin, Kaira, Christophe at daily lunch at the Campus Mensa.


Thanks to Dr. Chulseung Lee, senior scientist at the LCR Division of Samsung Electro-Mechanics for
his invitation to an on-site visit to the Samsung‟s Suwon MLCC factory that made me have a good and
clear understanding of the procedures for industrial MLCCs production. Thanks for his successive
provide of materials and for his professional advices on technical questions.


Thanks go to Beam-line scientist Dr. Steve Wang and beam-line staff, Alex Deriy, Dr. Joan Vila-
Comamala at the Sector 32 ID-C (APS synchrotron, Argonne National Laboratory, USA) for their
support to set up the in-situ X-ray imaging experiment unit and help with conducting the Transmission
X-ray Microscope data acquisition. Without their assistances, the X-ray tomography could not have
gone smoothly.


I am indebted to Frederic Charlot at the CMTC, Grenoble for his helpful discussions on the FIB
tomography experiments, also for his expertise and efforts in the FIB stack acquisitions.


Thanks to Prof. Gerhard Brey of Frankfurt University for the access to the micro drill to machine the
MLCC samples.


Specially, I would like to thank Profs. Clive A. Randall, Jürgen Rödel, Hans-Joachim Kleebe and
Dominique Bernard for their time spent reviewing my manuscript. I highly appreciate their perceptive
comments and enlightening suggestions.


Last, thanks to my beloved parents, my sisters, my brothers-in-law. Thanks for their persistent love,
understanding and support during my pursuit of my academic careers.



ii
                                                                                                 Abstract


Abstract

Multi-Layer Ceramic Capacitors (MLCCs) are key passive components in modern electronics.
MLCCs consist of alternating metal electrode and ceramic dielectrics layers. In ultrathin MLCC chips,
the micrometric layers are composed of submicrometric metal and ceramic powders and nano sized
ceramic additives (to retard the sintering of electrode and minimize the sintering mismatch). A
number of defects such as cracks, delamination of layers and electrode discontinuity and homogeneity,
may arise in the processing of these ultrathin MLCCs. The cracks and delamination result in product
rejection. Electrode discontinuities (uncovered areas) and thickness homogeneity generate a number
of problems including capacitance loss, electrical short, leakage current and decreased reliability.

It is generally recognized that these defects are linked to the sintering kinetics mismatch between
electrode and dielectric materials, during the co-firing (co-sintering) process of MLCCs. However,
when it comes to the origin of these defects and to their evolution during the sintering process, little
knowledge is available. Conventional post-sintering and 2-dimensional (2D) imaging methods suffer
limitations.

In this context, in-situ synchrotron X-ray imaging and Discrete Element Method (DEM) have been
carried out to explore the origin and the evolution of defects during the co-sintering process. X-ray
imaging including 2D radiography and 3-dimensional (3D) nano computed tomography (X-ray nCT)
enable non-destructive in-situ observation of the microstructure change in 2D and 3D. In parallel,
DEM can simulate the sintering of MLCCs by taking into account the powders‟ particulate nature
(particle size, packing, etc.)

Synchrotron (Advanced Photon Source, Argonne National Laboratory, IL, USA) X-ray based
Transmission X-ray Microscope (TXM) with spatial resolution of 30 nm was used to characterize a
representative cylindrical volume of Ø 20 µm × 20 µm extracted from a 0603 (1.6 mm×0.8 mm) case
size Nickel (Ni)-electrode Barium Titanate (BaTiO3, or BT)-based MLCC before and after sintering
under 2H2%+Ar atmosphere. 3D tomographic microstructure imaging shows that the final electrode
discontinuity is linked to the initial heterogeneity in the electrode layers. In situ X-ray radiography of
sintering (heating ramp of 10 oC, holding at 1200 oC for 1 hour, cooling ramp -15 oC) of a Palladium
(Pd) electrode BNT (Barium-neodymium-titanate) based MLCC representative volume was also
carried out. It confirmed that discontinuities in the electrode originate from the initial heterogeneities,
which are linked to the very particulate nature of the powder material. The discontinuity occurs at the
early stage of the sintering cycle. At this stage, the electrode starts to sinter while the dielectric
material may be considered as a constraining substrate.

Correlative studies using Focused Ion Beam - Scanning Electron Microscope (FIB - SEM)
tomography were conducted on green and sintered MLCC samples at high resolution (5 × 5 × 5 nm3).

                                                                                                        iii
Abstract

FIB images confirmed that the resolution of the X-ray nCT is sufficient to deal with these
heterogeneity evolutions. Still, FIB tomography allows the X-ray nCT to be re-interpreted more
accurately. Also, it provides detailed particulate parameters for the DEM simulations.

The DEM was used to simulate the microstructure of a multilayer system during sintering. These
simulations operate at the particle length scale and thus recognize the particulate nature of the
multilayers at the early stage of sintering. First, the sintering of Ni matrix with BT inclusions was
simulated using the dp3D codes (developed at SIMaP/GPM2, Universitéde Grenoble, France). The
retarding effect of BT inclusions on the sintering of Nickel matrix was predicted by varying the size,
the amount and the homogeneity of inclusions. It is found that the densification rate of the matrix
decreases with increasing volume fraction of inclusions and with decreasing size of inclusions. For a
given volume fraction and size of inclusions, a better dispersion of the inclusions results in a stronger
retardation of the densification kinetics of the nickel matrix.

Co-sintering of BT/Ni/BT multilayers was simulated with DEM by taking into account the particulate
nature collected from the high resolution FIB nanotomography (FIB-nT) data, such as particle size,
size distribution, heterogeneities, pores, and geometry. The temperature profile was also reproduced
in these simulations. It is found that the electrode discontinuities originate from the initial
heterogeneities in the green compact and form at the early stage of sintering under constraint, in good
correspondence to the experimental observations. Parametric studies suggest that electrode
discontinuities can be minimized by homogenizing the packing density and thickness of the electrodes
and using a fast heating rate.

Based on both experimental and DEM simulation results, a general conclusion is reached: the final
discontinuity originates from the initial heterogeneity in the electrode layers and occurs at the early
stage of sintering when the dielectric layers constrain the electrode layers.

A defect evolution mechanism is proposed: after the lamination of BT sheets, there exist inevitably
heterogeneous regions in the electrodes. Below 950-1000 oC, the nickel powder densifies except in
heterogeneous zones for which desintering has been observed. At this stage, the Ni layers are under
tensile stress. Tensile stresses in the thinner sections induce matter flow towards the thicker sections
until the thinner sections are disrupted and discontinuities form. Once nickel is fully dense, electrodes
are subjected to compressive stress at high temperature (1100 oC) due to BT densification. The
compressive stress causes contraction of the viscous nickel, resulting in swelling of electrodes and
hence a further increase in electrode discontinuity. Meanwhile, the nano-sized BT additives are
expelled due to their unwettability with Ni at high temperature. The aggregated BT additives sinter,
possibly forming percolation between two adjacent BT layers and enhancing the mechanical adhesion
between Ni and BT layers in the MLCCs.




iv
                                                                           Abstract

Key Words: Sintering; Multilayer Ceramic Capacitor (MLCC); Discrete Element Method;
Nanotomography




                                                                                 v
Abstract




vi
                                                                                          Abstrakt


Abstrakt

Keramische     Vielschichtkondensatoren       (Multilayer   Ceramic    Capacitor,   MLCC)      sind
Schlüsselkomponenten in der modernen Elektronik. MLCCs bestehen aus alternierenden metallischen
Schichten (Elektroden) und keramischen Schichten (Dielektrika). In ultradünnen MLCC-Chips
bestehen die einzelnen Mikroschichten aus submikrometrischen Metall -und Keramikpartikeln.
Zudem werden nanometrische keramische Additive zugefügt, die das Sintern der Elektrode verzögern
und den Sinterverzug zwischen den verschiedenen Schichtmaterialien minimieren. Eine Reihe von
Mängeln wie Rissbildung, Delamination der Schichten sowie Inhomogenität und Diskontinuität der
Elektrodenschichten können in ultradünnen MLCCs beobachtet werden. Rissbildung und
Delamination führen zur Verwerfung des Produkts. Diskontinuitäten in den Elektroden (unbedeckte
Bereiche) und mangelnde Dickenhomogenität erzeugen eine Reihe von Problemen wie zum Beispiel
Kapazitätsverlust, Kurzschlüsse, Leckstrom und verringerte Zuverlässigkeit.

Es ist allgemein anerkannt, dass diese Defekte auf die unterschiedliche Sinterkinetik von Elektrode
und Dielektrikum während des Kosinterns der MLCCs zurückzuführen sind. Informationen über die
Entstehung dieser Mängel sind jedoch nur in geringem Maß verfügbar, da herkömmliche
Nachbearbeitungsmethoden und zweidimensionale (2D) Bildgebungsverfahren mit Einschränkungen
verbunden sind.

In diesem Zusammenhang wurden In-Situ-Synchrotronröntgentomographie sowie Simulationen mit
der Diskrete Elemente Methode (DEM) durchgeführt, um den Ursprung und die Entwicklung der
Mängel während des Kosinterverfahrens zu erforschen. Bildgebende Röntgenverfahren, wie z. B. 2D
Radiographie und dreidimensionale (3D) Nanocomputertomographie (Röntgen-nCT) ermöglichen
zerstörungsfreie In-Situ-Beobachtung der Gefügeentwicklung in 2D und 3D. Begleitend kann mittels
DEM Methode das Sintern von MLCCs unter Berücksichtigung der Partikeleigenschaften des Pulvers
(Partikelgröße , Packung, etc..) simuliert werden.

Ein mittels Synchrotronstrahlung betriebenes Transmissionsröntgenmikroskop (TXM, Advanced
Photon Source , Argonne National Laboratory , IL, USA) mit räumlichen Auflösungsvermögen von
30nm wurde verwendet, um ein repräsentatives zylindrische Volumen von Ø 20µm x 20µm aus einer
0603 (1,6 mm × 0,8 mm) Gehäusegröße eines MLCC bestehend aus Nickel (Ni) – Elektrode und
Bariumtitanat (BaTiO3 oder BT) zu extrahieren und vor und nach dem Sintern unter 2H 2 % + Ar-
Atmosphäre zu charakterisieren. 3D-Computertomographie des Gefüges zeigt dass die Inhomogenität
der gesinterten Elektrode auf die anfängliche Heterogenität in den Elektrodenschichten
zurückzuführen ist. In-Situ-Röntgenradiographie während des Sinterns (Heizrampe von 10 °C und 1h
Haltezeit bei 1200 °C gefolgt von einer Kühlrampe von -15 °C) eines repräsentativen Volumens eines
MLCCs bestehend aus Palladium- (Pd) Elektrode und BNT (Barium – Neodym - Titanat) wurde


                                                                                                vii
Abstrakt

ebenfalls durchgeführt. Diese Studie bestätigt, dass Diskontinuitäten in der Elektrode auf deren
anfänglichen Heterogenität zurückzuführen sind, welche mit den Partikeleigenschaften des Pulvers
zusammenhängen. Die Diskontinuität tritt im frühen Stadium des Sinterzyklus auf. In diesem Stadium
beginnt die Elektrode zu sintern, während das dielektrische Material als nichtsinterndes Substrat agiert,
welches eine geometrische Einschränkung zur Folge hat.

Korrelative Studien mit Focused Ion Beam - Rasterelektronenmikroskop (FIB - SEM) - Tomographie
wurden auf grünen und gesinterten MLCC Proben bei hoher Auflösung (5 × 5 × 5 nm3 ) durchgeführt.
FIB Bilder bestätigen, dass die Auflösung der Röntgen-nCT ausreicht, um die Entwicklung dieser
Heterogenität zu beschreiben. Dennoch erlaubt die FIB –Tomographie eine genauere Interpretation
der Röntgen-nCT neu. Darüber hinaus stellt diese Technik detaillierte Parameter für die DEM –
Simulationen bereit.

DEM wurde verwendet, um das Gefüge eines Mehrschichtsystems während des Systems zu
simulieren.   Diese    Simulationen   arbeiten   auf   Partikelskala   und    beschreiben   somit    die
Partikeleigenschaften der Schichtsysteme im frühen Sinterstadien. Zuerst wurde das Sintern der Ni-
Matrix mit BT-Einschlüssen unter Verwendung des dp3D Codes (entwickelt bei SIMaP/GPM2,
Université de Grenoble, Frankreich) simuliert. Die verzögernde Wirkung von BT-Einschlüssen auf
das Sintern der Nickelmatrix wurde durch Variation der Größe, der Menge und der Homogenität der
Einschlüsse vorhergesagt. Eine sinkende Verdichtungsrate der Matrix bei zunehmendem
Volumenanteil von Einschlüssen und abnehmender Größe der Einschlüsse wird festgestellt. Bei
konstantem Volumenanteil und Größe der Einschlüsse führt eine bessere Verteilung der Einschlüsse
zu einer stärkeren Verzögerung der Sinterkinetik der Nickelmatrix .

Das Kosintern von BT / Ni / BT -Mehrfachschichten wurde mit DEM unter Berücksichtigung der
mittels hochauflösender FIB-Nanotomographie (FIB-nT) ermittelten Partikeldaten, wie zum Beispiel
der Partikelgröße sowie deren Verteilung, Heterogenität und Porengeometrie, simuliert. Das
Temperaturprofil wurde auch in diesen Simulationen wiedergegeben. Es zeigt sich, dass sich die
Diskontinuitäten in den Elektroden aus der anfänglichen Heterogenität im Grünling sowie der
geometrischen Einschränkung während des frühen Sinterstadiums ergeben. Dies ist in guter
Übereinstimmung mit den experimentellen Beobachtungen. Parameterstudien legen nahe, dass
Diskontinuitäten durch die Homogenisierung der Packungsdichte und der Dicke der Elektroden sowie
mit einer schnelleren Aufheizrate minimiert werden können.

Die experimentellen Ergebnisse und DEM-Simulationen erlauben eine allgemeine Schlussfolgerung:
die Diskontinuitäten in den Elektroden nach dem Sintern stammen aus der anfänglichen Heterogenität
in den Elektrodenschichten und treten im frühen Stadium des Sinterns auf, während welchem die
dielektrischen Schichten die Schrumpfung der Elektrodenschichten behindern.




viii
                                                                                         Abstrakt

Ein Mechanismus für die Defektentwicklung wird vorgeschlagen: Nach der Lamination der BT-
Blätter gibt es zwangsläufig heterogene Regionen in den Elektroden. Unterhalb von 950-1000 oC
verdichtet das Nickelpulver überall außer in den heterogenen Zonen. In letzteren wird Entsinterung
beobachtet. In diesem Stadium sind die Ni-Schichten unter Zugspannung. Zugspannungen in den
dünneren Abschnitten erzeugen Materialfluss in die dickeren Regionen, bis die dünneren Abschnitte
unterbrochen werden und sich Diskontinuitäten bilden. Sobald die Nickelelektrode komplett
verdichtet ist, stehen die Elektroden unter Druckspannung bei hohen Temperaturen (1100 °C)
aufgrund der Verdichtung der BT-Blätter. Die Druckspannung resultiert in Schrumpfung des viskosen
Nickels, was wiederum zu Schwellungen der Elektroden und damit zu einer weiteren Erhöhung der
Diskontinuität in den Elektroden führt. Währenddessen werden die Nano-Zusatzstoffe durch ihre
mangelnde Benetzbarkeit mit Ni bei hohen Temperaturen ausgetrieben. Die aggregierten Zusatzstoffe
im BT sintern und erzeugen somit möglicherweise Perkolation zwischen benachbarten BT-Schichten,
wodurch die mechanische Haftung zwischen Ni und BT- Schichten in den MLCCs verbessert wird.

Schlüsselwörter: Sintern , Keramische Mehrschichtkondensatoren (MLCC),         Diskrete-Elemente-
Methode , Nanotomographie




                                                                                                ix
Abstrakt




x
                                                                                                                                    Content


Content

Acknowledgements ..................................................................................................................... i
Abstract .................................................................................................................................... iii
Abstrakt....................................................................................................................................vii
Content ...................................................................................................................................... xi
Table of figures ........................................................................................................................ xv
List of abbreviations ............................................................................................................... xxi
List of symbols ..................................................................................................................... xxiii
1. Introduction ....................................................................................................................... - 1 -
   1.1 Basics of Multi-Layer Ceramic Capacitors (MLCCs) ................................................ - 3 -
       1.1.1 Structure ............................................................................................................... - 3 -
       1.1.2 Materials .............................................................................................................. - 4 -
       1.1.3 Manufacturing of MLLCs .................................................................................... - 8 -
       1.1.4 Challenges for miniaturization of MLCCs ........................................................ - 10 -
   1.2 Motivation ................................................................................................................. - 12 -
   1.3 Objectives and organization of the dissertation ........................................................ - 13 -
2. Co-firing of Multilayer Ceramic Capacitors ................................................................... - 15 -
   2.1 Sintering .................................................................................................................... - 15 -
       2.1.1 Mechanisms of sintering .................................................................................... - 16 -
       2.1.2 Sintering stages .................................................................................................. - 17 -
   2.2 Constrained sintering ................................................................................................ - 18 -
       2.2.1 Sintering with inclusions (agglomerates)........................................................... - 20 -
       2.2.2 Constrained sintering of film and multilayers ................................................... - 23 -
   2.3 Co-firing of MLCCs ................................................................................................. - 25 -
   2.4 Conclusion ................................................................................................................ - 27 -
3. Material characterization and sintering behaviour study ................................................ - 29 -
   3.1 Materials ................................................................................................................... - 29 -
   3.2 Experiment procedure ............................................................................................... - 29 -
   3.3 Results and discussions ............................................................................................. - 32 -
   3.4 Conclusions ............................................................................................................... - 42 -
4. Synchrotron X-ray imaging of the sintering of MLCCs ................................................. - 43 -
   4.1 Introduction ............................................................................................................... - 43 -
       4.1.1 X-ray computed tomography ............................................................................. - 43 -

                                                                                                                                              xi
Content


      4.1.2 Application to sintering ...................................................................................... - 46 -
  4.2 Experiment procedure ............................................................................................... - 47 -
      4.2.1 Set-up: Transmission X-ray Microscope ........................................................... - 47 -
      4.2.2 Sample preparation using FIB milling ............................................................... - 48 -
      4.2.3 Image acquisition and 3D reconstruction .......................................................... - 50 -
  4.3 Results and discussion .............................................................................................. - 51 -
      4.3.1 Ex-situ X-ray CT on Ni-MLCC sample............................................................. - 51 -
      4.3.2 In situ X-ray imaging of Pd-MLCC ................................................................... - 56 -
  4.4 Conclusion ................................................................................................................ - 61 -
5. Correlative studies using FIB-SEM nanotomography .................................................... - 63 -
  5.1 Introduction ............................................................................................................... - 63 -
  5.2 Experiments .............................................................................................................. - 69 -
      5.2.1 Experiment setup ............................................................................................... - 69 -
      5.2.2 Materials and procedures ................................................................................... - 69 -
      5.2.3 Image processing ............................................................................................... - 71 -
  5.3 Comparison of FIB-nT with X-ray nCT ................................................................... - 75 -
      5.3.1 Characterization of green microstructures ......................................................... - 75 -
      5.3.2 Characterization of sintered microstructures ..................................................... - 76 -
      5.3.3 Evaluation of pore size....................................................................................... - 76 -
  5.4 Particle size distribution (PSD)................................................................................. - 79 -
      5.4.1 Segmentation...................................................................................................... - 79 -
      5.4.2 3D watershed segmentation ............................................................................... - 80 -
      5.4.3 Particle size distribution..................................................................................... - 81 -
      5.4.4 Particle size distribution in 2D and 3D .............................................................. - 84 -
  5.5 Heterogeneities in the green electrode ...................................................................... - 86 -
  5.6 Porosity ..................................................................................................................... - 88 -
  5.7 Anisotropy ................................................................................................................. - 89 -
      5.7.1 Pore orientation in BT layer ............................................................................... - 89 -
      5.7.2 Density gradient ................................................................................................. - 92 -
  5.8 Microstructure evolution of the electrode ................................................................. - 94 -
      5.8.1 Discontinuity of electrode .................................................................................. - 94 -
      5.8.2 Correlation between discontinuity and capacitance ........................................... - 96 -
  5.9 Conclusion ................................................................................................................ - 98 -



xii
                                                                                                                                Content


6. Discrete element simulations of the sintering of electrode material ............................... - 99 -
   6.1 Introduction ............................................................................................................... - 99 -
       6.1.1 DEM simulation of sintering ............................................................................. - 99 -
       6.1.2 Principle of DEM ............................................................................................. - 100 -
   6.2 Model description ................................................................................................... - 103 -
   6.3 Simulation procedure .............................................................................................. - 106 -
   6.4 Result and Discussion ............................................................................................. - 108 -
   6.5 Conclusions ............................................................................................................. - 111 -
7. DEM simulation of Ni/BaTiO3 multilayers .................................................................. - 113 -
   7.1 Model description ................................................................................................... - 113 -
   7.2 Simulation procedures ............................................................................................ - 113 -
       7.2.1 Sample preparation .......................................................................................... - 113 -
       7.2.2 Sintering conditions ......................................................................................... - 115 -
       7.2.3 Post processing................................................................................................. - 116 -
   7.3 Free sintering and constrained sintering ................................................................. - 117 -
   7.4 Effect of heating ramp ............................................................................................ - 119 -
   7.5 Effect of green density ............................................................................................ - 121 -
   7.6 Effect of contact viscosity ....................................................................................... - 123 -
   7.7 Effect of electrode thickness ................................................................................... - 126 -
   7.8 Retarding effect of the inclusions ........................................................................... - 128 -
   7.9 Co-sintering induced anisotropy ............................................................................. - 129 -
   7.10 Towards more realistic microstructure: coupling with experiments ..................... - 132 -
   7.11 Conclusions ........................................................................................................... - 135 -
8. Conclusions and perspectives ....................................................................................... - 137 -
   8.1 General conclusions ................................................................................................ - 137 -
   8.2 Recommendations ................................................................................................... - 139 -
   8.3 Research perspectives ............................................................................................. - 140 -
Appendix A ....................................................................................................................... - 143 -
Appendix B ....................................................................................................................... - 145 -
Appendix C ....................................................................................................................... - 147 -
Erklärung........................................................................................................................... - 149 -
Curriculum Vitae .............................................................................................................. - 151 -
   Education ...................................................................................................................... - 151 -
   Publications ................................................................................................................... - 151 -

                                                                                                                                       xiii
Content


References ......................................................................................................................... - 153 -




xiv
                                                                                                          Table of figure


Table of figures

Figure 1. 1 MLCCs mounted on a graphic card circuit [4] ................................................................ - 1 -
Figure 1. 2 Case size trend over the year (Murata‟s road map [8]).................................................... - 2 -
Figure 1. 3 Cut-away view of a MLCC chip (adapted from Kishi [4]).............................................. - 4 -
Figure 1. 4 Perovskite crystal structure of BaTiO3 (from Perditax [10]) ........................................... - 6 -
Figure 1. 5 Phase transformation of BaTiO3 (after Pan [5]) .............................................................. - 7 -
Figure 1. 6 A schematic of the MLCC fabrication process (adapted from Pan [5]) .......................... - 8 -
Figure 1. 7 The electrode and dielectric thickness evolution [25] ................................................... - 11 -
Figure 1. 8 SEM image of the cross-section of a sintered 0603 type 22 µF MLCC (provided by
      Samsung Electro-mechanics). Surface was treated with focused ion beam. ........................... - 12 -
Figure 2. 1 Six mechanisms for the sintering of crystalline particles([43])                                             - 17 -
Figure 2. 2 Shrinkage during a typical sintering (after Kang [44])                                                      - 17 -
Figure 2. 3 The three stages of sintering and microstructure (after Tanaka [45])                                        - 18 -
Figure 2. 4 Schematic illustrations of structures that will undergo differential densification (after
      Green [47])                                                                                                       - 20 -
Figure 2. 5 Two types of interface flaws produced by the tensile stress when one region (shaded)
      sinters slower than the other (reproduced after Raj [48])                                                         - 21 -
Figure 2. 6 (a) the composite sphere model; (b) the stress components in a volume element at a
      distance r in the sintering matrix. The sphere has vi (volume fraction) of inclusions with radius
      value a and outer radius b (adapted from [55, 57])                                                                - 22 -
Figure 2. 7 A schematic of defects induced by constrained sintering of layers [75]                                      - 24 -
Figure 2. 8 An equilibrium configuration diagram for the sintering of a thin film with thickness of a
      and grain size of G (dihedral angle φ = 120 o) ( after Miller [77])                                               - 25 -
Figure 2. 9 A typical firing cycle for the Ni-MLCCs                                                                     - 26 -
Figure 2. 10 FIB treated cross-sections of 0603 size 22 µF Ni-MLCC                                                      - 27 -
Figure 3. 1 A schematic for the Bragg‟s scattering [80]                                                                 - 31 -
Figure 3. 2 TOM-AC optical dilatometer                                                                                  - 31 -
Figure 3. 3 Particle size distributions                                                                                 - 33 -
Figure 3. 4 XRD pattern of the starting powder                                                                          - 34 -
Figure 3. 5 Linear shrinkage of nickel paste and dielectrics                                                            - 35 -
Figure 3. 6 Linear shrinkage of 1206 type MLCCs                                                                         - 35 -
Figure 3. 7 Starting powders: (a) X5R type BT powder; (b) debinded nickel paste                                         - 36 -
Figure 3. 8 Green chips with binders at three different magnifications                                                  - 37 -
Figure 3. 9 SEM images of cross-section of debinded sample                                                              - 37 -
Figure 3. 10 SEM images of the fracture cross-sections                                                                  - 38 -
Figure 3. 11 Microstructural evolution of chips sintered with different temperature profiles                            - 39 -

                                                                                                                           xv
Table of figure

Figure 3. 12 Roughness on the surface of an electrode                                                 - 40 -
Figure 3. 13 A schematic of discontinuous electrode                                                   - 43 -
Figure 3. 14 Discontinuity and thickness, roughness of electrodes as a function of time               - 41 -
Figure 4. 1 A schematic diagram of the X-ray image acquisitions [96]                                  - 43 -
Figure 4. 2 A schematic diagram of tomographic reconstruction using the back-projection method
      [85].                                                                                           - 45 -
Figure 4. 3 Spatial resolutions achievable with different lenses: calculated resolutions (open symbols),
      measured resolutions (filled symbols); synchrotron source (circle symbol) and lab sources
      (square symbol) (reproduced after withers [94])                                                 - 46 -
Figure 4. 4 A schematic illustration of a TXM imaging system consisting of a condenser lens,
      objective lens, and detector system. Beamstop and pinhole block out the unfocused X-rays (after
      Nelson [128])                                                                                   - 47 -
Figure 4. 5 A schematic for the setup of the TXM at Sector 32-IDC of APS Synchrotron                  - 48 -
Figure 4. 6 Photograph of a microscope adapted drill                                                  - 49 -
Figure 4. 7 Two-step preparation of sample for X-ray nCT                                              - 49 -
Figure 4. 8 (a) MLCC sample for X-ray tomography; (b), (c) 2D projection images before and after
      sintering, respectively; and (d), (e) reconstructed 3D microstructure before and after sintering,
      respectively.                                                                                   - 51 -
Figure 4. 9 BT and Ni absorption edge                                                                 - 52 -
Figure 4. 10 Microstructural changes of MLCC samples                                                  - 53 -
Figure 4.11 Schematic for the mass correlation before and after sintering in the electrode (the read
      areas represent the pores in the electrode)                                                     - 53 -
Figure 4. 12 Morphology of inner electrode #2                                                         - 54 -
Figure 4. 13 (a) Discontinuity of electrodes; (b) Axial and radial strains in different BT layers,
      irregular top BT layer (#1) was not considered and (c) relative densities of BT layers (the layers
      are indexed as in Fig. 4.8(c)).                                                                 - 56 -
Figure 4. 14 Microstructural evolutions during sintering. Note that Au particles were used both for
      image alignment in the reconstruction and for calibrating the temperature in the furnace.       - 57 -
Figure 4. 15 3D reconstruction and rendering (top view) of the electrodes in the Pd-MLCC samples
                                                                                                     -- 57 -
Figure 4. 16 Radial and axial strains in dielectric layers, radial strains in electrodes as function of time
                                                                                                      - 59 -
Figure 4. 17 A schematic of the defect evolution mechanism during sintering                           - 60 -
Figure 5. 1 Resolution of different tomography techniques (after Holzer [135])                        - 64 -
Figure 5. 2 Dual beam FIB-SEM system (after Volkert [151])                                            - 65 -
Figure 5. 3 Schematic for the FIB serial sectioning (after Holzer [135] )                             - 66 -




xvi
                                                                                          Table of figure

Figure 5. 4 Electron material (SiO2) interaction diagram (adapted from Salh [152])                    - 66 -
Figure 5. 5 The schematic of drift correction                                                         - 68 -
Figure 5. 6 Configuration of the nVison 40 FIB/SEM [153]                                              - 69 -
Figure 5. 7 Serial sectioning on the sample #2                                                        - 70 -
Figure 5. 8 Serial sectioning on the sample # 1-s-ct                                                  - 71 -
Figure 5. 9 Serial sectioning on the sample # 3                                                       - 71 -
Figure 5. 10 Imaging pretreatment flow chat                                                           - 72 -
Figure 5. 11 Removal of noise using 3D median filter                                                  - 73 -
Figure 5. 12 (a) an original slice (b) the gray gradient of the slice, (c) resulting image after subtraction
     of from the gradient image, (d) histogram of the original image a, (e) histogram of the filtered
     image c, (f) the pore phase separated from the original image, and (g) the pores in the image after
     the filtering                                                                                    - 74 -
Figure 5. 13 3D reconstructed volume for (a) #2, (b) #1-s-ct and (c) #3                               - 74 -
Figure 5. 14 Microstructures of the green MLCC with X-ray nCT (column a: sample #1-s) and FIB-
     nT (column b: sample #2)                                                                         - 75 -
Figure 5. 15 X-ray nCT (column a) and FIB tomography (SE mode: column b), (BSE mode: column
     c) on the final microstructure                                                                   - 76 -
Figure 5. 16 Percolation of pores and skeletons: (a) before sintering; (b) after sintering            - 77 -
Figure 5. 17 Pore size distribution in the BT (a) and Ni (b) layer obtained with X-ray -nCT and FIB-
     nT                                                                                               - 78 -
Figure 5. 18 (a) an original slice, (b) a zoomed in area of the original image, (c) histogram of the slice,
     (d) identification of Ni phase, (e) removal of noises from image (d), (f) manual removal of the
     artifacts, (g) imposition of the electrode on the original image, (h) identification of the BT phase,
     and (i) the remaining pore phase                                                                 - 80 -
Figure 5. 19 Definition of watershed in a watershed segmentation algorithm from [157]                 - 81 -
Figure 5. 20 Separation of Ni particles using 3D watershed segmentation (Avizo Fire)                  - 81 -
Figure 5. 21 Result of the 3D watershed segmentation of Ni particles in the electrode: (a) 3D view of
     separated Ni partilces, colors are assigned randomly (BT inclusions not considered); (b) PSD
     measured with FIB-nT and laser scattering.                                                       - 82 -
Figure 5. 22 3D watershed segmentation for the BT particles in a representative dielectric layer - 83 -
Figure 5. 23 Result of the 3D watershed segmentation of BT particles in the BT layer                  - 84 -
Figure 5.24 Sectioning a sphere randomly produce a distribution of circle sizes, which can be
     calculated from analytical geometry (after [155])                                                - 85 -
Figure 5. 25 Correlation between PSDs in 2D and in 3D using the unfolding scheme                      - 85 -
Figure 5. 26 (a) 3D rendering of the electrode (the electrode plane is xz); (b) xy middle plane cross-
     section; (c) zy middle plane cross-section; (d) xz middle plane cross-section                    - 86 -
Figure 5. 27 Density profile in x, y, z direction (1 pixel represents 5 nm)                           - 87 -

                                                                                                       xvii
Table of figure

Figure 5. 28 Coordination number map for the xz plane cross-sections                                   - 88 -
Figure 5. 29 Pore orientations in the 2D cross-section                                                 - 89 -
Figure 5. 30 Pore orientation in the xz plane before and after sintering                               - 90 -
Figure 5. 31 Pore orientation in the x’y’ plane before and after sintering                             - 91 -
Figure 5. 32 Pore orientation in the y’z’ plane before and after sintering                             - 92 -
Figure 5. 33 Density profile in the thickness (from the surface to the bottom of the cylinder sample)
                                                                                                       - 93 -
Figure 5. 34 Anisotropy in thin film on substrate                                                      - 93 -
Figure 5. 35 A model for the co-sintering of multilayers                                               - 94 -
Figure 5. 36 An electrode (#2) from the sample #1-s-ct                                                 - 95 -
Figure 5. 37 EDX mapping of the cross-section of the sintered chips (sample #3)                        - 95 -
Figure 5. 38 The PSD evolutions of BT inclusion particles entrapped in the electrode (#2) in sample
     #1-s-ct                                                                                           - 96 -
Figure 5. 39 Two reconstructed electrodes and a unit capacitor                                         - 97 -
Figure 6. 1 Two-particle contact model                                                               - 101 -
Figure 6. 2 Schematics of (a) wall conditions and (b) periodic conditions                            - 103 -
Figure 6. 3 Contact models: (a) matrix-matrix contact (matrix can be metal or ceramic); and (b)
     inclusion-matrix contact                                                                        - 106 -
Figure 6. 4 Generating of the numerical samples                                                      - 107 -
Figure 6. 5 Numerical microstructure of composites with: 20% of randomly dispersed 300 nm (a), 100
     nm (b), and 60 nm (c) inclusions;10% of randomly dispersed 60 nm inclusions (d); and 10% of
     agglomerated 60 nm inclusions (agglomerate sizes are ~ 120 nm (e) and ~300 nm (f)).             - 108 -
Figure 6. 6 (mm) and (im) contact numbers in the green packing for various amounts and size of
     inclusions.                                                                                     - 109 -
Figure 6. 7 Evolution of (mm) contacts upon densification: (a) effect of inclusion amount, (b) of
     inclusion size, and (c) of the inclusions as agglomerates (agg.) or well dispersed (no agg.) - 109 -
Figure 6. 8 Contact size evolution of three types of contacts.                                       - 110 -
Figure 6. 9 Densification rate evolution with relative density: (a) effect of inclusion amount, (b) effect
     of inclusion size, and (c) of inclusions as agglomerates (agg.) or well dispersed (no agg.). - 110 -
Figure 7. 1 Numerical samples: (a) BT dielectric layer (b) Ni electrode layer without BT additives (c)
     Ni electrode with 10 vol% BT additives (d) BT/Ni/BT multilayers                                 - 115 -
Figure 7. 2 (a) definition of coble contact radius ac; (b) visualization of two sintered particles after the
     voxelization procedure.                                                                         - 117 -
Figure 7. 3 Microstructure evolution of electrode: (a) green microstructure; (b) definition of the
     inter/intra- agglomerate pores; (c) freely sintered electrode; and (d) constrained sintered electrode
                                                                                                     - 118 -




xviii
                                                                                         Table of figure

Figure 7. 4 The microstructure evolution in the magnified area                                     - 119 -
Figure 7. 5 Electrode discontinuity against the temperature                                        - 120 -
Figure 7. 6 Microstructure of electrode sintered at different heating rates, with the calculated
     discontinuity.                                                                                - 121 -
Figure 7. 7 Discontinuity of electrode as functions of heating time                                - 122 -
Figure 7. 8 Microstructure of electrode with different green density (at 15 oC/min)                - 123 -
Figure 7. 9 Discontinuity of electrode as functions of heating time for different values of the viscous
     parameter.                                                                                    - 124 -
Figure 7. 10 Microstructure of electrode with different viscosities (at 15 oC/min)                 - 125 -
Figure 7. 11 Green microstructures of different samples with (a) 0.2 µm, (b) 0.4 µm (c), 0.6 µm, and
     (d) 0.8 µm thick electrode (pure Ni )                                                         - 126 -
Figure 7. 12 Electrode discontinuity as functions of heating time                                  - 127 -
Figure 7. 13 Microstructure of electrode with different electrode thickness (at 15 oC/min)         - 127 -
Figure 7. 14 Green microstructures of pure Ni electrode                                            - 128 -
Figure 7. 15 Microstructures of the sintered pure Ni electrode (a) and the composite electrode
     excluding the BT inclusions                                                                   - 129 -
Figure 7. 16 Discontinuity as function of sintering time                                           - 129 -
Figure 7. 17 Crystalline-like packed BT/Ni/BT multilayers                                          - 130 -
Figure 7. 18 Microstructure and density profile: (a) before sintering; (b) after sintering         - 130 -
Figure 7. 19 Contact size evolution during sintering                                               - 131 -
Figure 7. 20 Contact size evolution during sintering                                               - 132 -
Figure 7. 21 (a) cylinder sample extracted from FIB nano tomography; (b) equivalent numerical
     model; (c) initial microstructures of the nickel electrode; (d) equivalent numerical model - 133 -
Figure 7. 22 Rearrangement of particles after relaxation process                                   - 134 -
Figure 7. 23 Microstructures of electrode before and after sintering (nano additives of BT have been
     removed for clarity)                                                                          - 135 -




                                                                                                      xix
Table of figure




xx
                                                           List of abbreviations


List of abbreviations

     2D                 2 Dimension/Dimensional

     3D                 3 Dimension/Dimensional

     BBO                Binder Burn-Out/Binder Bake-Out

     BME                Base Metal Electrode

     BNT                Barium Neodymium Titanate

     BSE                Backscattered Electrons

     BT                 Barium Titanate

     CCD                Charge-Coupled Device

     CMOS               Complementary Metal-Oxide-Semiconductor

     CT                 Computed Tomography

     DEM                Discrete/Distinct Element Method/Modeling

     EBSD               Electron Backscatter Selective Diffraction

     EDX(S)             Energy-dispersive X-ray spectroscopy

     FIB                Focused Ion Beam

     FOV                Field of View

     HTCC               High Temperature Co-fired Ceramics

     LSA                Laser Scattering Analyzer

     LTCC               Low Temperature Co-fired Ceramics

     MEMS               Microelectromechanical Systems

     MLCC               Multilayer Ceramic Capacitors

     NDT                Non-destructive Test

     NME                Noble Metal Electrode

     OM                 Optical Microscope

     PC                 Personal Computer

     PCB                Printed Circuit Board

     PSD                Particle/Pore Size Distribution

     PVB                Polyvinylbutyral


                                                                            xxi
List of abbreviations

       PVD              Physical Vapor Deposition

       ROI              Region of Interest

       RVE              Representative Volume Element

       SE               Secondary Electrons

       SEM              Scanning Electron Microscope

       SOFC             Solid Oxide Fuel Cells

       TEM              Transmission Electron Microscope

       TXM              Transmission X-ray Microscope

       XRD              X-ray Diffraction




xxii
                                                                                List of symbols


List of symbols

Symbol   Unit          Description

amm      m             Matrix-matrix contact radius

aii      m             Inclusion-inclusion contact radius

aim      m             Inclusion-matrix contact radius

A        m2            Effective electrode overlapping area

C        F             Capacitance

d0       Å             Length of the lattice

de       m             The distance between adjacent electrodes

D        -             Relative density

D0b      m2·s-1        Diffusion coefficients for grain boundary

D10      m             The size below which lies10% of the population of particles

D50      m             The median diameter of the particle size

D90      m             The size below which lies 90% of the population of particles

E        eV            Beam energy

h        m             Indentation

I0       photons·s-1   Intensity of the incidence X-ray

I        photons·s-1   Intensity of the transmitted X-ray

Km       Pa·s          Bulk viscosities

l1       m             The length of the first segment of the electrode

l2       m             The length of the second segment of the electrode

ln       m             The length of n-th segment of the electrode

L        m             Sampling length of the electrode

M        Kg            Mass

Mm       Kg mol-1      Molar mass

Ne       N             Number of electrode in a multilayer ceramic capacitor

Nii      N             Normal force at the inclusion-inclusion contact




                                                                                          xxiii
List of symbols

Nij        N           Normal force at contact between particle i and particle j

Nmm        J·m-2       Normal force at the matrix-matrix contact

Qb         KJ·mol-1    Sintering activation energy

Ra         m           Roughness

R          m           Radius of particles

Rm         m           Radius of the matrix particle

Rg         JK-1mol-1   Gas constant

R*         m           Reduced radius
           o
T              C       Temperature

Tmm        N           Tangential force at matrix-matrix contact

Te         m           Mean Thickness of electrode

Tij        N           Tangential force at contact between particle i and particle j

u          m·s-1       Tangential velocity at the contact

V          m3          Volume

Vsolid     m3          Volume of the solid phase

Venvelop   m3          Volume that envelops the material

Vm         m3·mol-1    Molar volume

w          J·mol-1     Work of adhesion

Zmm        -           Average matrix-matrix contact number

Zim        -           Average inclusion-matrix contact number
           o
α              C-1     Thermal expansion coefficients

γs         J·m-2       Surface energy

δb         m           Thickness of grain boundary

t         s           Time step

ε0         F·m−1       Vacuum permittivity

εr         -           Relative permittivity

εr         -           Radial strain

εa         -           Axial strain




xxiv
                                                                          List of symbols

ɛij          -        Strain between particle i and j

 ij         s-1      Strain rate between particle i and particle j

c           s-1      Sintering strain rate of the composites

 mfree      s-1      Sintering strain rate of the matrix of composites

x           s-1      x component strain rate

y           s-1      y component strain rate

z           s-1      z component strain rate

 porosity   -        Porosity

Ø            m        Diameter of the unit cell

λ            Å        Wave length of the incidence X-ray

ν            -        Poisson‟s ratio

νp           -        Viscous Poisson‟s ratio

i           -        Volume fraction of the inclusion phase

appar .     Kg·m-3   Apparent density

theor .     Kg·m-3   Theoretical density

 BT
  theor .    Kg·m-3   Theoretical density of BaTiO3

 rm         Pa       Radial component stress in the matrix

 m         Pa       Polar component stress in the matrix

 m         Pa       Angular component stress in the matrix

m           Pa       Mean stress in the matrix

i           Pa       Stress in the inclusion

x           Pa       x component stress

y           Pa       y component stress

z           Pa       z component stress

            Pa       Sintering stress in the matrix

η           -        Viscosity coefficients

µ            m-1      The material's linear attenuation coefficient

μf           -        Friction coefficient


                                                                                     xxv
List of symbols

Ω         m3      Atomic volume




xxvi
                                                                                         Introduction


1. Introduction

Capacitors, resistors and inductors are passive components often considered as minor but crucial parts
in modern electronics. Capacitors can accomplish in electrical circuits numerous functions including
blocking, coupling and decoupling, alternating-direct current separation, filtering and energy storage
[1]. In particular, ceramic capacitors are crucial to leading-edge semiconductor devices, which cannot
operate properly without them. In 2012 the global capacitor market reached $17.933 billion USD,
including $8.8 billion USD in ceramic capacitors. Unit shipments of capacitors totalled an estimated
1.594 trillion pieces worldwide [2]. Multi-Layer Ceramic Capacitors (MLCCs), characterized by their
high volumetric efficiency, high reliability, and excellent high-frequency features, dominate in the
ceramic capacitor market. In 2008, it accounted for ~90% of the capacitor market in part volume [1].
The global MLCC market is forecast to grow at a compound-annual-growth rate of 22.2 % over the
period 2010-2014 [3]. One of the key factors contributing to this market growth is the increasing
demand for MLCCs in consumer electronics such as cellular phones, digital players and personal
computers (PCs). Figure 1.1 shows typical MLCCs mounted on a graphic card circuit.




                         Figure 1. 1 MLCCs mounted on a graphic card circuit [4]


Recently, trends towards miniaturization, higher performance, and lower energy-consumption have
driven research and development efforts [4]. Miniaturizations of passive components used in these
pieces of equipment have also been accelerated. With hundreds of MLCCs used in typical electronic
devices (Table 1.1), trillions of pieces of MLCC are demanded by market each year [5].




                                                                                                 -1-
Introduction

                        Table 1. 1 Number of MLCCs used in electronic devices [6]
                       Electronic equipment               Typical number of MLCCs
                            Laptop PC                                 730
                          Cellular Phone                              230
                           Smart Phone                                500
                        Digital Camcorder                             400
                      Car Navigation System                          1000
                            Digital TV                               1000




Since the first MLCCs were introduced in the early years of World War II there have been two major
development trends. One is towards smaller size and higher capacitance, that is towards maximizing
volumetric efficiency (capacitance per volume) at a rate that exceeds Moore‟s Law [7] (Figure 1.2).




                      Figure 1. 2 Case size trend over the year (Murata‟s road map [8])

To keep pace with the miniaturization of modern electronics, the thicknesses of the electrode and
dielectric layers are increasingly being downsized to meet the shrinking surface mounting space in the
PCBs (Printed Circuit Boards). Presently, EIA 1 case sizes 0603 and 0402 are most common as
shown in Figure 1.2. The state-of-the-art case size is EIA01005 (0.4 mm × 0.2 mm). In a EIA 0402
case size 22 µF MLCC, thickness of dielectric layers is approximately 0.3 µm [6]. The smallest




1
 Metric codes define the dimensions of MLCC chips: 0402 stands for (0.4 mm × 0.2 mm) for example, (0402 is
01005 in inch code), see Table 1.2. The EIA code is used for the MLCCs in this thesis.


-2-
                                                                                           Introduction

available size (0.2 mm × 0.1 mm) of commercial MLCCs by Murata still does not have an EIA
definition.

The other important trend is to reduce the production cost. Over the last two decades, the noble metal
electrode (NME, mainly, palladium/silver) has been gradually replaced by the base metal electrode
(BME, mainly, copper/nickel) due to the high price of Pd and Ag. Nowadays, the BME-MLCCs
account for more than 95% of the MLCC market [9].

                                        Table 1. 2 EIA code table
                                    EIA             Dimensions        IEC/EN           Dimensions
              Drawing
                                    inch code       L × W(inch)       metric code      L × W(mm)
                                    01005           0.016 × 0.0079    0402             0.4 × 0.2
                                    015015          0.016 × 0.016     0404             0.4 × 0.4
                                    0201            0.024 × 0.012     0603             0.6 × 0.3
                                    0202            0.02 × 0.02       0505             0.5 × 0.5
                                    0302            0.03 × 0.02       0805             0.8× 0.5
                                    0303            0.3 × 0.03        0808             0.8 × 0.8
                                    0504            0.05 × 0.04       1310             1.3 × 1.0
                                    0402            0.039 × 0.020     1005             1.0 × 0.5
                                    0603            0.063 × 0.031     1608             1.6 × 0.8
                                    0805            0.079 × 0.049     2012             2.0 × 1.25
                                    1008            0.098 × 0.079     2520             2.5 × 2.0
                                    1111            0.11 × 0.11       2828             2.8 × 2.8
                                    1206            0.126 × 0.063     3216             6.2 × 1.6
   Dimensions L×W×H of the          1210            0.126 × 0.10      3225             6.2 × 2.5
    multi-layer ceramic chip        1410            0.14 × 0.10       3625             3.6 × 2.5
           capacitors               1515            0.15× 0.15        3838             3.81 × 3.81
                                    1806            0.18 × 0.063      4516             6.5 × 1.6
                                    1808            0.18 × 0.079      4520             6.5 × 2.0
                                    1812            0.18 × 0.13       4532             6.5 × 6.2
                                    1825            0.18 × 0.25       4564             6.5 × 6.4
                                    2010            0.20 × 0.098      5025             5.0 × 2.5
                                    2020            0.20 × 0.20       5050             5.08 × 5.08


1.1 Basics of Multi-Layer Ceramic Capacitors (MLCCs)

1.1.1 Structure

A MLCC is a monolithic block of ceramic consisting of two sets of offset, interweaved
(“interdigitated”) planar electrodes that extend to two opposite surfaces of the ceramic dielectric (Fig.
1.3). The capacitance C (unit, farad, F) of a MLCC is given by:

                                                    A( Ne  1)
                                       C   r o                                                    (1.3)
                                                       de
Where ε0 is the vacuum permittivity (unit F·m-1), εr the relative permittivity of the dielectrics
(dimensionless), N e the number of inner electrodes, A the capacitive area of the electrodes, and d e

the thickness of the dielectrics.

                                                                                                     -3-
Introduction

The area A is increased by stacking many electrodes in parallel. This construction allows for very thin
inter-planar space d e between opposing electrodes. For a given case size, d e is equal to the chip

thickness H divided by N e . Thus the capacitance C is proportional, for a given chip thickness, to N e 2 .




                    Figure 1.3 Cut-away view of a MLCC chip (adapted from Kishi [4])



1.1.2 Materials

a) Ceramic Dielectric Materials [1]

Ceramic dielectrics cover a broad range of properties, from steatite with an εr value of 6 to complex
ferroelectric compositions with εr higher than 20,000. Commercial ceramic dielectrics can be
categorized into three classes:


Class I dielectrics usually include low- and medium- permittivity ceramics with dissipation factors
(loss tangent2) < 0.003. Relative permittivity εr covers a range of 15-500 with stable temperature
coefficients of permittivity that lies between +100 and -2,000 ppm/°C.


For example, a P3K capacitor has a -1,500 ppm/°C change in capacitance and a tolerance of ±250
ppm/°C, and a C0G capacitor has zero temperature coefficient and a ±30 ppm/°C tolerance.




2
  The loss tangent is a parameter of a dielectric material that quantifies its inherent dissipation of
electromagnetic energy


-4-
                                                                                                Introduction

                       Table 1. 3 Class I EIA specification codes for Class I dielectrics
  Significant        Symbol           Multiplier        Symbol            Tolerance of         Symbol
  figure of                           applied to                          temperature.
  temperature                         significant                         coefficient (ppm)
  coefficient of                       figure
  permittivity
  (ppm/C)
          0                C                 -1                0                 30                 G
         0.3               B                -10                1                 60                 H
         0.8               L               -100                2                 120                J
         0.9               A              -1,000               3                 250                K
         1.0               M             -10,000               4                 500                L
         1.5               P                  1                5                                     M
                                                                                1,000
         2.2               R                 10                6                                     N
                                                                                2,500
         6.3               S                100                7
         4.7               T               1,000               8
         5.6               V              10,000               9
         7.5               U


Class II//III dielectrics consist of high-permittivity ceramics based on ferroelectrics. They have εr
values between 2,000 and 20,000 and properties that depend more on temperature, field strength and
frequency than Class I dielectrics. Their dissipation factors are generally less than 0.03 but may
exceed this level in some temperature ranges and in many cases become much higher when high AC
fields are applied. Their main importance lies in their high volumetric efficiency (Table 1.4).

Table 1. 4 Coding for temperature range and capacitance variation for Class II/III Capacitors (codes D-R: Class
                                          II; Codes S-V: Class III)
       EIA Code            Temperature range/oC             EIA Code             Capacitance change/%
           X5                   -55 to +125                      D                        ±6.3
           X7                   -55 to +150                      E                        ±4.7
           X8                    -30 to +85                      F                        ±7.5
           Y5                    +10 to +85                      P                        ±10
           Z5                                                    R                        ±15
                                                                 S                        ±22
                                                                 T                    +22 to -33
                                                                 U                    +22 to -56
                                                                 V                    +22 to -82


For instance, a Z5U capacitor will operate from +10 °C to +85 °C with a capacitance change of at
most +22% to -56%. An X7R capacitor will operate from -55 °C to +125 °C with a capacitance
change of at most ±15%.


Class IV dielectrics have a conductive phase that effectively decreases the thickness of dielectric
layers in capacitors by at least an order of magnitude. Very simple structures such as small discs and
tubes having two parallel electrodes can achieve capacitances of over 1 mF. Their disadvantages are


                                                                                                          -5-
Introduction

low working voltages in range of 2-25V and high losses. They mainly apply in “barrier layer”
capacitors that are now very little used and considered as outdated.

   Barium Titanate [5]

Emblematic for class II/III dielectrics, barium titanate (BaTiO3, or BT) was discovered simultaneously
in several countries during World War II. Due to the presence of ferroelectricity, BT features high
permittivity (maximum εr >10,000) that was orders of magnitude greater than other existing
dielectrics at that time. The technological importance of BT was recognized immediately, and
extensive efforts were devoted to tune its dielectric properties. Nowadays, BT is still the base material
for ceramic dielectrics. BT has a perovskite crystal structure as shown in Figure 1.4.




                   Figure 1. 4 Perovskite crystal structure of BaTiO3 (from Perditax [10])


Three phase transitions take place in BT when cooled from high temperature (Fig. 1.5): cubic to
tetragonal at ~120 °C, tetragonal to orthorhombic at 0 °C, and orthorhombic to rhombohedral at -
90 °C. The temperature induced phase transitions cause dramatic drifts in dielectric constants. Thus,
pure BT cannot be used directly since the dielectric in the capacitors should have little temperature
dependency. Manufacturers typically use solid solutions of BT. with dopants based on Sr, Ca, Zr, Sn
and rare earths. Dopants broaden the dielectric constant peaks of the doped BT.




-6-
                                                                                         Introduction




                         Figure 1. 5 Phase transformation of BaTiO3 (after Pan [5])



b) Electrode metals

The electrode material is supposed to lead to a conductive and continuous film that does not diffuse
into, or react with the ceramic dielectric during sintering. This requires the use of non-oxidizing
metals or alloys with high melting points. There are two material systems used today to make ceramic
capacitors: Noble Metal Electrode (NME) and Base Metal Electrode (BME).

   NME

The NME is the older technology and uses Pd/Pd-Ag electrodes, Ag termination, and Ni and Sn
plating. Palladium reduces during heating to allow film formation, and its surface oxidizes during
cooling (below 870 °C). This causes it to bond to the ceramic. For cost reduction, increasing amounts
of silver are added to the electrode alloys to replace palladium. This also allows the melting point of
the alloy to be lowered. The development of lower firing formulations allows the use of more silver,
which results in electrode cost savings.

   BME

The BME is of a newer technology and uses Ni electrode, Ni or Cu termination, and Ni and Sn plating.
The use of Ni electrodes reduces further the cost of electrode, but the requirement for a low oxygen
partial pressure (to keep the metal from oxidizing) during firing causes significant changes in ceramic
composition and processing. Base-metal-electrode MLCCs have accounted for >95% of global
MLCC market for their high volumetric efficiency and low cost [9].



                                                                                                  -7-
Introduction

                    Table 1. 5 Physical properties and price ratio of various electrodes [4]
        Metals         Melting point(°C)         Resistivity(mΩ)         Firing atmosphere      Price ratio
         Ag                    961                     1.62                      Air                 3
         Cu                    1080                    1.72                   Reducing               1
         Ni                    1453                     6.9                   Reducing               1
         Pd                    1552                    10.4                      Air                80




1.1.3 Manufacturing of MLLCs

The processes used in the manufacture of MLCCs require a high degree of sophistication to insure
high-yield, large-scale and low-cost production. The typical procedure of MLCCs fabrication is
shown in Figure 1.6.




               Figure 1. 6 A schematic of the MLCC fabrication process (adapted from Pan [5])



   Ceramic slurry making [11]

The ceramic slurry is made by mixing predetermined proportions of powder in a solvent, dispersing
agent, binder (polyvinylbutyral, PVB), plasticizer and other additives using dispersing apparatus such
as a bead mill, ball mill, attriter, paint shaker or sand mill to yield a homogeneous ceramic slurry.

   Tape casting

The slurry is cast on a film carrier by tape casting (doctor blading). The slip is carried by a
conveyor belt into a drying oven to produce the dry ceramic tape. This tape is then cut into

-8-
                                                                                           Introduction


pieces, so called sheets. A proper dispersion of the powder in the slip is necessary to secure a
maximum packing in the dried slip.

   Screen printing

The electrode ink is made by mixing a submicron metal powder, solvents and ceramic additives. The
ink is deposited on the green ceramic sheets according to the electrode patterns using a screen printing
process. Poor printing quality may cause significant yield loss. Proper dispersion of metal particles
helps to provide a homogeneous film. This is required to minimize the amount of metal that gives a
continuous fired film.

   Stacking and lamination

The patterned sheets are stacked and laminated to form a solid bar. The pressure, temperature and
dwelling time are important parameters and have to be optimized in accordance with to the material
system.

   Dicing

The bar is cut into separate parts (capacitors). The parts are now in a “green” state. In general, the
yield decreases with increasing volume of capacitor and depends on the aspect ratio of the component.

   Binder burn out

The binder burn-out or bake-out (BBO) process is to remove the organics from the chips before firing.
This process usually requires the longest time and often causes a large amount of product rejection.
Voids or pores arise when the generation of gaseous products exceeds some critical pressure within
the body. The heating profiles need to be adjusted according to specific capacitor geometry and size.
This step must be performed gradually since excessive initial heating rates result in rapid gas
generation. Therefore, it is necessary to control the heating rates and the atmosphere.

   Firing

The firing (sintering) of green parts is conducted in kilns with slowly moving conveyor belts. The
temperature profile is crucial to the characteristics of the capacitors. Time dependent changes in firing
conditions and variations due to location of the parts in the kiln must be minimized.

   Wet tumbling

During this process, sharp corners of MLCCs are rounded to minimize potential breakage during
handling. Also, this rounding of corners is helpful to obtain good coverage of termination ink.

   Termination and curing

Fired chips are terminated in the electrode pick-up regions with a conductive ink. Then the ink cures
in the range of 650-800 oC. The termination provides the external layer with electrical and mechanical

                                                                                                    -9-
Introduction

connection to the capacitor. The conductive ink is made of metal powder, solvents and glass frit in a
mixer.

   Plating

The termination is coated with a nickel layer and a tin layer using an electroplating process. The
nickel serves as a barrier layer between the tin plating and the termination. The tin is to protect the
nickel from oxidizing.

   Testing

The parts are tested and sorted according to their correct capacitance tolerances. The parts can be
packaged on tape and reel after this process.


1.1.4 Challenges for miniaturization of MLCCs

As Eq. (1.1) indicates, increase in volumetric efficiency of MLCC can be achieved by increasing the
number of dielectric layers and decreasing the layer thickness. Today, a Class II capacitor could have
up to 1000 submicrometric layers. The innovative efforts in MLCC technology has resulted in an
exponential increase of capacitance in recent years (see Fig. 1.7). With the thinning of dielectric
layers, tape-casting technology becomes problematic for the development of next generation MLCCs.
Conventional processing of tape casting/screen printing has reached its technological limit at 0.8-1.0
μm. MLCC manufacturers tend to reduce the BT grain size in order to pack more grains across the
thickness of the dielectric layer. However, due to size effects, smaller grains lead to lower permittivity
and thus to lower capacitance [12-15]. Many efforts have gone to the development of novel core-shell
ceramic dielectrics with higher dielectric constant and smaller grain size [16-21]. The core-shell grain
features a core region, pure tetragonal structure BT surrounded by a pseudocubic shell which contains
other additive elements [22-24].




- 10 -
                                                                                          Introduction




                      Figure 1. 7.The electrode and dielectric thickness evolution [25]


In the meanwhile, thinning of electrode also goes with the thinning of dielectrics to reduce the case
size of the chips and the consumption of electrode materials. However, when the thickness of
electrodes approaches 1.0 μm or less, significant discontinuities of electrode build up after the firing
process (see Fig. 1.8). The electrode coverage loss results in a direct decrease in the overlapping area
(A) in Eq.(1.1). An average discontinuity of 15% causes around 20% capacitance loss. Inversely, this
means that, for a given capacitance, the volume of MLCC could have further downsized by 20% if
one was able to get rid of this discontinuity. Furthermore, the effects of microstructural
heterogeneities are much more significant when thinning electrodes. In particular, the local electric
field is disturbed at electrode discontinuities and roughness [26-29]. Thus, controlling of the
connectivity and smoothness of the electrode in ultrathin MLCC is of much interest to enhance the
capacitance, the performance and the reliability of MLCCs.




                                                                                                  - 11 -
Introduction




   Figure 1. 8 SEM image of the cross-section of a sintered 0603 type 22 µF MLCC (provided by Samsung
                      Electro-Mechanics). Surface was treated with Focused Ion Beam.


1.2 Motivation

It has been reported that defects in electrode layers are related to different processing phases. Gas
release from inappropriately controlled BBO [30] results in residual pores which act as initial defects.
To achieve thinner electrode layers, it is necessary to reduce the electrode paste attachment during the
printing process. However, a reduction in the paste attachment results in a decreased coverage rate of
the metal electrode following the firing process [31]. Moreover, the sintering shrinkage mismatch [32]
between the electrode and dielectric layers also leads to other defects, such as delamination, cracks,
and warpage [30, 31, 33-35].


Takahashi [36] and Sugimura [31] et al. found that the addition of BT particles into the Ni paste
results in a higher coverage ratio of nickel film on BT sheets due to reduced sintering mismatch.
Accordingly, Kang et al. [37] have shown that an additional amount BT particle into the nickel paste
decreases the shrinkage of the composite electrode.


Weil et al. [38] studied the sintering of nickel film on BT sheets and found that instabilities of Ni film
were formed as a series of interconnected or discrete nickel islands separated by patches of exposed
BT substrate surfaces. This is due to a dewetting effect and becomes significant when the nickel layer
thickness is sub-micrometric.




- 12 -
                                                                                             Introduction

Polotai et al. [28, 29, 39] proposed that thin (~10 nm) liquid (Ni, Ba, Ti) alloy layer formed at Ni/BT
interfaces during sintering of ultrathin MLCCs. The presence of the high-temperature interfacial
liquid film modifies the interfacial free energy and provides a fast kinetic pathway for mass transport,
which leads to the enhanced Ni grain growth and degradation of the electrode layers. By using a fast
heating scheme this liquid alloy could be suppressed and Yoon et al. [26] observed higher linear
connectivity (93%) of electrode by using high heating rates of 3600 oC/h. Addition of refractory
elements (Cr, Pt) into the nickel paste further limits the formation of interfacial liquid alloy layer and
improves the Ni electrode continuity [40]. These authors also suggest that the residual carbon [41] due
to incomplete removal of the binder plays a role in the formation of this liquid phase.


To date, the investigations were mainly based on 2-dimensional (2D) information from sectioned
surfaces using optical microscopy (OM) or Scanning Electron Microscopy (SEM) [26, 42]. First, the
final microstructures cannot reveal correctly the origin and historic evolution of the defects. Second,
2D evaluation such as the linear electrode coverage is sometimes not sufficient to quantify defects and
layer thickness shrinkage. Furthermore, inappropriate handling during sample preparation can be
problematic and add some artifacts. Samantaray et al. [27] demonstrated Focused Ion Beam -
Scanning Electron Microscope (FIB-SEM) based 3-dimensional (3D) tomography characterization on
the 3D morphology of electrode in sintered MLCC sample for the first time. To refine the
understanding of mechanisms that are responsible for the defects initiation and evolution during the
co-firing of the MLCCs, we need some superior, non-destructive, 3D and quantifiable characterization
techniques.


In parallel to 3D observations, simulation of the sintering process at the pertinent length scale (particle
length scale) should provide information that can relate the defect origin and evolution to structural
parameters (particle size, particle packing, layer thickness, temperature profile, etc.)


1.3 Objectives and Organization of the Dissertation

In this thesis, the aim is to better understand the origin of the electrode defects and the defect
evolution mechanism during the co-firing process. This understanding will be built on the sintering
phenomena at the particle length scale in 3D by using state-of-the-art nano-tomography techniques
and discrete element simulations. The dissertation is organized as follows:


Chapter 2: This chapter presents a background study. The co-firing process of the MLCCs is revisited
and the possible scenarios that might result in defects development are considered. Co-sintering or
constrained sintering of composites and multilayers is reviewed.


                                                                                                    - 13 -
Introduction

Chapter 3: This chapter describes the characteristics of the starting electrode and dielectric powders
(Ni and BT, respectively) including their compositions, particle size distribution and sintering kinetics
using X-ray diffraction (XRD), SEM and dilatometry.


Chapter 4: In this chapter, the application of the state-of-the-art synchrotron based X-ray nano-
computed tomography (nCT) is introduced. The microstructure of a Ni-MLCC sample is
characterized using X-ray nCT and quantifications of microstructure evolution have been carried out
before and after sintering. An in-situ x-ray radiographic observation on sintering of a Pd-MLCC
sample is also presented and discussed.


Chapter 5: In this chapter, correlative studies on the sintering of Ni-MLCCs have been carried out
using high-resolution Focused Ion Beam (FIB)-SEM nanotomography. FIB-SEM reconstructions of
Ni-MLCC samples have been conducted to enhance the resolution available in X-ray
nanotomography.


Chapter 6: In this chapter, the applications of discrete elements method to the sintering is introduced
and reviewed. The effect of the ceramic additives on the sintering kinetics of the electrode paste
materials is investigated using DEM simulation. Simulation parameters include the size, and the
volume fraction and the dispersion degree of the additives.


Chapter 7: Free sintering of single electrode and co-sintering sandwiched BT/Ni/BT layers are
simulated using DEM. The defects origin and evolution of the electrode are investigated. Comparison
between the experiments and simulation limitations are commented. The effect of microstructure and
process parameters, such as the thickness of the electrode layers, the green packing density, the
arrangement of the particles, and the heating ramp have been investigated.


Chapter 8: This chapter summarizes the findings from the experiments and DEM simulations. A
defect evolution mechanism is put forward. Finally, recommendations are proposed to improve the
manufacturing of MLCCs with less electrode discontinuity.




- 14 -
                                                            Co-firing of Multilayer Ceramic Capacitors


2. Co-firing of Multilayer Ceramic Capacitors

Microstructural control in ultrathin MLCCs is nowadays one of the main challenges for maintaining
an increase in volumetric efficiency of capacitance. To help solve this problem, understanding the
impact of the firing process on the microstructure of materials (compact of metallic and dielectrics
powder) is of the greatest importance. During the firing process of MLCC parts, complex phenomena
take place, including chemical reaction, and microstructural evolution. In this chapter, we attempt to
understand this firing process by considering the fundamentals of the sintering mechanisms in the
firing process. Starting from an introduction to the sintering, the literature on co-sintering of
composite and layered systems is revisited to find potential solutions.


2.1 Sintering

Generally, the term firing has been used when the processes occurring during the heating stage are
very complex, as in many traditional ceramics produced from clay-based materials. In less complex
cases, the term sintering has been used [43]. Sintering is a processing technique used to produce dense
or density-controlled materials and products from metal and/or ceramic powders by applying thermal
energy [44]. This sintering process is associated with a reduction of the free energy of the system. The
sources that cause this reduction of the free energy are usually referred to as the driving forces for
sintering. There are three possible driving forces: (i) the curvature of the particle surfaces; (ii) an
external pressure, and (iii) a chemical reaction.


When an external stress and a chemical reaction are not involved, surface curvature provides the
driving force for sintering. Considering one mole of powder consisting of N spherical particles of
radius R.
                                             3M m   3Vm
                                       N         =      (2.1)
                                            4 R  4 R3
                                                3


Where ρ is the density of the particles, M the molecular mass, and Vm the molar volume. The surface
area of the powder is
                                                          3Vm
                                       SA =4 R 2 N             (2.2)
                                                           R
If γsv is the specific surface energy of the particles, then the surface free energy associated with the
system of particles is
                                                        3 sVm
                                       Es   s S A             (2.3)
                                                          R
Es represents the reduction in surface free energy of the system if a fully dense body were to be
achieved finally. It implies powder with high surface energy (as for metals) or fine particle size is


                                                                                                  - 15 -
Co-firing of Multilayer Ceramic Capacitors

prone to sintering more rapidly. External pressure and chemical reaction are not in the scope of
current study of sintering of MLCCs and not detailed here (see Ref. [44]).


Sintering of crystalline materials is usually categorized into two types: solid state sintering and liquid
phase sintering. Solid state sintering occurs when the powder compact is densified fully in the solid
state at the sintering temperature. Liquid phase sintering occurs when the powder compact is densified
during sintering in the presence of a liquid phase. Normally, this liquid phase is formed due to the
sintering temperature exceeding melting point of one material. If it is not specified, sintering in this
thesis refers to solid state sintering.


2. 1.1 Mechanisms of sintering

Sintering of polycrystalline materials occurs by transport of matter along definite paths (bulk, lattice,
grain boundary, and surface) that define the mechanisms of sintering. Matter is transported from
higher chemical potential regions (the source) to lower chemical potential regions (the sink). As
schematized in Figure 2.1, there are six typical mechanisms of sintering in polycrystalline materials.
They all lead to bonding and neck growth (a) between particles (with radius of R). They can also be
generally categorized as densifying and nondensifying mechanisms.

    a) Nondensifying mechanisms include surface diffusion, volume (lattice) diffusion from the
         particle surfaces to the neck, and vapor transport (mechanisms 1, 2, and 3) which lead to neck
         coarsening without densification. The nondensifying mechanisms cannot simply be ignored
         because they reduce the curvature of the neck surface (i.e., sintering potential, activation
         energy).

    b) Densifying mechanisms include grain boundary diffusion and lattice diffusion from the grain
         boundary to the pore (mechanisms 4 and 5) which permits neck growth as well as
         densification (common in polycrystalline ceramics) and plastic flow by dislocation motion
         (mechanism 6, common in the sintering of metal powders).




- 16 -
                                                                         Co-firing of Multilayer Ceramic Capacitors


                                                                                  R
                                                                            a




Figure 2. 1 Six mechanisms for the sintering of crystalline particles: (1) surface diffusion, (2) volume diffusion
from the surface, (3) evaporation/condensation transport, (4) grain boundary diffusion from the grain boundary,
(5) volume diffusion from the grain boundary, and (6) plastic flow by dislocation motion (after Rahaman [43]).



2.1.2 Sintering stages

The curve in the Figure 2.2 shows the relative density against the sintering time in a typical sintering.
Sintering is usually subdivided into three sequential stages referred to as: (1) the initial stage, (2) the
intermediate stage, and (3) the final stage.




                 Relative density



                                    O
                                                                  Sintering time
                                    Figure 2. 2 Shrinkage during a typical sintering (after Kang [44].)




                                                                                                             - 17 -
Co-firing of Multilayer Ceramic Capacitors

       1) The initial stage: this stage features a rapid inter-particle neck growth (Fig. 2.3) by diffusion,
           vapor transport, plastic flow, or viscous flow. Large initial differences in surface curvature
           characterize this stage, and densification accompanies neck growth for the densifying
           mechanisms. It is assumed to last until the normalized neck radius3 has reached a value of 0.4-
           0.5. This corresponds to a linear shrinkage of around 3% when the densifying mechanisms
           dominate, for a packing with an initial green density of 0.5-0.6.

       2) The intermediate stage: this stage begins when pores have reached their equilibrium shapes as
           governed by the surface and interfacial tensions. Densification is assumed to result from pores
           simply shrinking to reduce their cross section. Finally, the pores become unstable and pinch
           off, resulting in isolated pores. The intermediate stage normally covers the major part of the
           sintering process, and it comes to an end when the density is ~0.9.

       3) The final stage: the final stage begins when the pores pinch off and become isolated at the
           grain corners. With continuous shrinking of pores, relative density of 0.90-0.95 is achievable.
           Fully dense final state has been achieved in the sintering of several real powder systems when
           all the pores vanish (Fig. 2.3).




                    Figure 2. 3 The three stages of sintering and microstructure (after Tanaka [45])


2.2 Constrained sintering

The term constrained sintering is commonly used to refer to sintering in which a geometrical
constraint is present, as shown in Figure 2.4. Conversely, a system in which the constraint is absent is
referred to as free or unconstrained system. The constraint may be inherent to the sintering system: for
example, a second rigid phase (particles, platelets or whiskers) is incorporated intentionally into the
matrix to obtained tunable functionality and improve the mechanical properties. A common feature of
such inhomogeneities is that they often lead to different local densification, referred to as differential
densification. Due to sintering shrinkage mismatch, some regions will be constrained by others. Even
in a single-phase material system, the presence of agglomerates or inhomogeneous powder packing in



3
    Defined as the ratio of neck to particle radius


- 18 -
                                                         Co-firing of Multilayer Ceramic Capacitors

the green bodies also provides constraining conditions (Fig. 2.4(a)). The inhomogeneities can also be
density variations (green-density gradients) through a single-phase porous media (Fig. 2.4(b)).


Adherent films/coatings on a rigid substrate are required in some important applications, such as
corrosion resistance coating, thermal barrier coating, insulating and optical coatings. Coatings made
by deposition of particles, sol-gel or consolidated agglomerates need further densification. When a
thin ceramic film is sintered on a rigid substrate, it is placed under biaxial tension and the
densification can only occur in vertical direction (thickness direction) (Fig. 2.4(c)).

Multilayered ceramics are widely used and being developed in electronics, information, medical and
energy. Excellent examples include Low/High Temperature Co-fired Ceramics, Solid Oxide Fuel
Cells, and piezoelectric multilayer actuators. When these multilayered structures are co-fired, the
different layers intend to shrink at different rates and constrain each other, giving rise to internal
compatibility stresses (Fig. 2.4(d)).

In the four types of co-sintering, two or more materials with different inherent densification behaviors
are in physical contact. The difference in the densification behavior originates from the chemical
nature or physical characteristics (e.g., particle size, green density) that control the densification
behavior. The internal stresses induced have the potential to hinder densification and lead to defects
and/or distortion in the fired bodies.

In this section, focus will be concentrated on sintering with inclusions and co-sintering of multilayers.
An example of density-induced constrained sintering can be found in Ref. [46].




                                                                                                  - 19 -
Co-firing of Multilayer Ceramic Capacitors




   Figure 2. 4 Schematic illustrations of structures that will undergo differential densification (a) Sintering of
composite materials in which a porous matrix densifies around rigid inclusions; (b) a porous material that has a
gradient in density; (c) a thin film densifying on a rigid (nondensifying) substrate; (d) Layered structures of two
                   or more types of materials that densify at different rates (after Green [47])


2.2.1 Sintering with inclusions (agglomerates)

The presence of inert and rigid inclusions results in drastic reduction in the densification rates of both
polycrystalline ceramic matrix composites [48-51] and metal matrix composites [31, 37, 52, 53].
Hence, due to inhomogeneous or random distribution of the inclusions, differential densification takes
place during sintering. This sintering shrinkage mismatch results in stresses concentration at the
interfaces. Theoretically, when stresses exceed the strength of the materials, crack, delamination will
develop, resulting in detrimental failure or loss of functionality (Fig. 2.5).




- 20 -
                                                                     Co-firing of Multilayer Ceramic Capacitors




                                                              Fast

                                                              Slow
                                (a)                                                         (b)
Figure 2. 5 Two types of interface flaws produced by the tensile stress when one region (shaded) sinters slower
                 than the other: (a) radial cracks; (b) circumferential cracks (reproduced after Raj [48])


Different models have been proposed to describe the sintering behavior of such mixtures and have
been reviewed by Bordia and Scherer [54-56]. These theoretical models and simulations operate
under the following conditions: (i) the matrix is homogeneous and isotropic [57], and may be treated
as a continuous linear viscoelastic body [48], (ii) the inclusions are inert rigid spherical particles that
are homogeneously distributed in the matrix [58].

    The Rule of Mixtures

The rule of mixtures assumes the densification of the composite to be a weighted average of the
independent densification rates of the matrix and of the inclusions; that is, it assumes that in the
composite, each phase densifies in the same way as it would independently by itself. If, for example,
we consider the linear densification rate  , defined as one-third the volumetric densification rate
1/ρ(dρ/dt), then according to the rule of mixtures:
                                     c   mfree (1  i )   i i   mfree (1  i ) (2.4)
Where  c is the composite densification rate,  mfree is the densification rate of the free matrix, and  i

(=0) is the densification rate of the inclusions. According to Eq.(2.4), the ratio  c /  mfree varies linearly

as (1  i ) .


This model is considered limited and inadequate to describe the sintering behavior of the composites
because the assumptions are too simplistic.

    Scherer‟s Model [55, 57]

Scherer proposed the Composite Sphere (CS) model to deal with sintering with well-dispersed
inclusions. In the CS model, a core/cladding structure is used to represent the porous matrix in which
the core represents the inclusion and the cladding represents the matrix (Fig. 2.6(a)). When the
inclusion is much larger than the matrix particle size, justified in most practical composites, the matrix

                                                                                                             - 21 -
Co-firing of Multilayer Ceramic Capacitors

can be considered as a continuum. In doing this, phenomenological constitutive equations can be used
for matrix.

                                                                                      Volume element in
                                                                                      the sintering matrix
    Composite Sphere Model




                                                                         Spherical rigid inclusion


               (a)                                                       (b)
Figure 2. 6 (a) the composite sphere model; (b) the stress components in a volume element at a distance r in the
   sintering matrix. The sphere has vi (volume fraction) of inclusions with radius value a and outer radius b
                                            (adapted from [55, 57])


A shrinking cladding (matrix) around a core (inclusion) gives rise to compressive stresses within the
core and compressive radial stresses and tensile tangential stresses within the cladding (Fig. 2.6(b)).
The mean hydrostatic stress in the matrix is:
                                    1                                vi
                              m  ( rm    m    m )   i (       ) (2.5)
                                    3                              1  vi

According to Eq.(2.5), the mean hydrostatic stress  m is uniform in the matrix and it is independent

of the radius and shape of the inclusions. Since  i is compressive,  m is tensile, opposing to the

compressive sintering stress.  m is often called a backstress.


The linear densification rate in the matrix is given by:
                                         m   1              v
                               m                [   i ( i )] (2.6)
                                          Km    Km           1  vi
Where  is the sintering potential. It is also the compressive hydrostatic stress that causes
densification of an unconstrained sintering material [54]. K m is the densification or bulk viscosity.

The backstress  m opposes  so it reduces the densification rate of the matrix. The tensile hoop

stress  m may influence the growth of radial cracks in the matrix.




- 22 -
                                                               Co-firing of Multilayer Ceramic Capacitors


2.2.2 Constrained sintering of film and multilayers

A common feature in sintering of these coatings and multilayers is that different components densify
at different rates. Different stress states develop in the layers in analogy to the thermal expansion
mismatch. The stresses in turn interact and modify the densification behavior of different layers. For
instance, in-plane tensile stresses develop in the coating due to the constraint imposed from the
substrate. This stress lowers the densification rate of the constrained film relative to that of a freely
sintered one [59].

   Sintering of thin films

Bordia and Raj [60] studied the sintering of thin ceramic films on rigid substrates and presented a
model using phenomenological descriptions of the densification and shear properties. Scherer and
Garino [61] and Hsueh [62] performed similar analyses. Assuming the densifying film is linear
viscous, by analogy with Hooke‟s law, the sintering rate along the orthogonal x, y, and z directions
can be written as:
                                             1
                                x   f       ( x   p [ y   z ])
                                             Ep
                                             1
                                y   f       ( y   p [ x   z ]) (2.7)
                                             Ep
                                             1
                                z   f       ( z   p [ x   y ])
                                             Ep

If the film is totally constrained in the xy plane, then  x   y  0 and the film stress,  f , is easily

derived from Eq.(2.7) as:
                                                      E p f
                                          f                  (2.8)
                                                      1  p

The strain rate in the non-constrained direction,  z , also follows and it depends only on υp and the

unconstrained strain rate:
                                                    1p 
                                         z   f 
                                                    1   
                                                              (2.9)
                                                         p 



    Sintering of laminates

In absence of external forces, the integrals of forces and bending moments along the thickness
direction z should be equal to zero for a multilayer in mechanical equilibrium. Cai et. al. [63]
considered a symmetric laminate consisting of alternating layers of two sintering materials. Applying
the infinite plate solution to materials that densify by linear viscous sintering, it was shown that the
equi-biaxial stresses that arise in the layers are given by:


                                                                                                    - 23 -
Co-firing of Multilayer Ceramic Capacitors


                                                  1
                                        1           E p' 1      (2.8)
                                               1  mn
                                          t                E p' 1
                                       m 1,          n             (2.9)
                                         t2                E p' 2

Where t is the layer thickness,   1   2 the strain rate difference between the layers,

E p'  E p / (1  v p ) for plates and E p'  E p for beams and the subscripts refer to layer 1 or 2. The
above solution is obtained by setting the strain rates in the two layers equal to each other and
maintaining a force balance for the compensating tensile and compressive stresses in the two layers.

When the stress is higher than the strength of materials, a variety of defects and shape distortions can
be generated, including warpages [64-70], cracks [71] and delamination [72] as shown in Figure 2.7.
Besides, anisotropic pore orientation develops during constrained sintering of layers [73, 74].




               Figure 2. 7 A schematic of defects induced by constrained sintering of layers [75]



In addition, when the thickness of polycrystalline film or thin layer is less than the critical value (in
which case, the single grains cross the layer), they may become unstable under an interfacial energy
equilibrium disturbance [76] and break up into discontinuous islands [38], thereby uncovering the
substrate [31]. This instability is driven by capillarity (surface tension) due to the thermodynamic
requirement of minimization of the interfacial energy. A necessary condition is that the film/substrate
interface has a higher specific energy than the substrate surface. Miller et al. [77] analyzed the
breakup phenomena of an Y2O3-stabilized ZrO2 film (8 mol% Y2O3) that was prepared by spin
coating. By evaluating the total energy of the surfaces and interfaces to determine its minimum value
as a function of the configuration of the film, an equilibrium configuration diagram was calculated
(Fig. 2.8). The diagram can be divided into three regions, showing the conditions for the completely
covered substrate, the uncovered substrate and the partially connected film (with the grain boundary
just intercepting the substrate).




- 24 -
                                                            Co-firing of Multilayer Ceramic Capacitors




 Figure 2. 8 An equilibrium configuration diagram for the sintering of a thin film with thickness of a and grain
                             size of G (dihedral angle φ= 120 o) (after Miller [77])


2.3 Co-firing of MLCCs

Firing is a key and complex stage in the manufacture of MLCCs. In this stage of the fabrication route,
the green chips are loaded into continuous kilns and fired on zirconia slabs. The multilayer capacitors
with noble metal electrodes (NME), such as pure Pd, Ag-Pd and pure Ag inner electrodes are fired in
air since they exhibit excellent oxidation resistance. Conversely, firing of MLCCs with Ni, Cu
electrode is conducted in moist reducing atmosphere (0.1-0.01%H2/Ar-H2O) to control the oxygen
partial pressure pO2 during the firing process. Time dependent changes in firing conditions, as well as
variations caused by location of the parts in the kiln, must be minimized. A second binder burn-out
(bake-out) (BBO) is applied to completely deplete the organics. After the sintering step the products
are re-oxidized at a lower temperature of 1000 °C in a higher pO2 atmosphere consisting of moist Ar
to recover resistivity. Figure 2.9 shows a typical firing profile for Ni-MLCCs.




                                                                                                           - 25 -
Co-firing of Multilayer Ceramic Capacitors


                                                   nd
                              1200              2 BBO         sintering        annealing
                                                                                         o
                                                                             (900-1100 C)
                              1000




               Temperature ( C)
               o
                                  800

                                  600

                                  400                   Reducing              Re-oxidizing
                                              (0.1-0.01%)H2/Ar-H2O               Ar-H2O
                                  200

                                    0
                                        0     50        100   150      200   250       300        350   400
                                                                    Time(min)
                                            Figure 2. 9 A typical firing cycle for the Ni-MLCCs


Nano-sized BT particles are added to the nickel paste (see Fig. 2.10) to reduce the sintering shrinkage
mismatch between nickel and BT layers during the firing process. The onset sintering temperature for
Ni electrode material is 400-600 oC, and the onset sintering temperature for BT is 900-1000 oC [29].
Thus, we are expecting the following sintering scenarios:

  I.     During the heating ramp and the second BBO, the Ni particles in the electrode sinter while the
         sintering of BT has not started yet. In presence of BT additive nanoparticles, the sintering
         kinetics of Ni particles is expected to be modified.

 II.     During the early stage of sintering of Ni particles, the particles at the interfaces interact with
         the BT particles through viscous friction. This interaction should hinder the rearrangement of
         the Ni particles.

III.     At high temperature (>1000 oC), sintering of Ni and BT co-exists. This has been referred to as
         co-sintering due to the different sintering strain rates encountered in the different layers. In
         addition, different stress states develop in the layers. This in-plane stress state plays an
         important role in the anisotropy development.




- 26 -
                                                              Co-firing of Multilayer Ceramic Capacitors


                                                  (a)                       Ni electrode
                                                                                                       (b)


                                                                    discontinuity
       BaTiO3 particles
                               Ni particles




                          Nano BatiO3 additives                                  BaTiO3 dielectrics




    Figure 2. 10 FIB treated cross-sections of 0603 size 22 µF Ni-MLCC (Samsung Electro-Mechanics, Inc.) (a)
                                          before firing; (b) after firing



2.4 Conclusion

We have attempted in this chapter to relate the sintering sciences and the practical firing processes
employed in the MLCC industry. Based on this review, we conclude that in order to understand defect
evolution during the co-firing process of MLCCs, the sintering behavior and the microstructure
evolution must be better analyzed. This may be undertaken by studying in more details the co-
sintering of Ni/BT composite material and of Ni/BT multilayers.

The general aim of this thesis is to describe the use of novel tools (tomography and numerical
simulations) that may help in attaining this goal.
.




                                                                                                       - 27 -
Co-firing of Multilayer Ceramic Capacitors




- 28 -
                                           Material characterization and sintering behaviour study


3. Material characterization and sintering behaviour study

The aim of this chapter is to characterize the materials involved in this work, including the starting
Nickel (Ni) powder and the BaTiO3 (BT) dielectrics powder. The Ni-electrode BT based MLCC chips
were also characterized. The microstructures of these materials were characterized using Scanning
Electron Microscope (SEM) and their sintering behavior was characterized by dilatometry.


3.1 Materials

   Starting powders

Ni powder and X5R BT powder were provided by Samsung Electro-mechanics (Suwon, South Korea).
Ni powder (Shoei Chemical, Tokyo, Japan) is made using a PVD (Physical vapor deposition) method.
X5R type characteristic 99.9% BT powder (NanoAmor, Inc., NM, USA) is made using solid state
synthesis as the dielectric material. Nickel paste is made by mixing 55 vol. % of Ni and nano-sized
BT powder at a ratio of 100 : 7 by weight with 41 vol. % terpineol (C10H18O) and 4 vol. % resin.

   MLCC manufacture

For Ni-electrodes MLCC chips, EIA 1206 series (3.2 × 1.6 × 1.6 mm3), and EIA 0603 series (1.6 ×
0.8 × 0.8 mm3), were fabricated at Samsung Electro-mechanics (Suwon, South Korea). Dielectric
sheets (2.5-μm-thick) were fabricated by tape casting with X5R type BT powder. Electrodes (1.2-μm-
thick) were made with deposition of nickel paste on those sheets using screen-printing. Patterned
sheets were laminated, isostatically pressed, and finally diced into green chips.

   Preparation of BT and electrode pellets

Nickel paste was dried first in an oven at 100 oC for 2 hrs, and then the organic binder was removed in
a muffle furnace with a temperature profile: heating 25-120oC at 3oC/min and 120-230 oC at 0.3 oC
/min, holding for 2 hrs at 230 oC, and cooling 230-25 oC at 3 oC/min. The debinded bulk Ni paste was
ground into powder in a corundum mortar.

Ni and BT powders were compacted in a closed cylindrical die (inner Ø 8mm) under uniaxial pressure
of 30 MPa using a P/O/Weber (PW100, Remshalden, Germany) laboratory press.


3.2 Experiment procedure

   Particle size measurement

A LA-950 high performance Laser diffraction Analyzer (Horiba, Kyoto, Japan) was used to
characterize Ni and BT particle size distribution. The LA-950 uses Mie Scattering (laser diffraction)
to measure particle size of suspensions or dry powders with a measuring range of 0.01-3000 µm. In

                                                                                                   - 29 -
Material characterization and sintering behaviour study

practice, a small amount of powder is dropped into water or alcohol, and the reflective index is
specified, and then the size distribution data is gathered [78].

   Green density

Green density measurement was conducted by weighting the mass and measuring the volume of
cylindrical samples. Some parameters are defined as follows:
                                                        M
                          Density definition:                (3.1)
                                                        V
                                                                        Mm
                          Theoretical or true density: theor .                 (3.2)
                                                                        Vm
                                                               M
                          Apparent density: appar .                    (3.3)
                                                            Venvelop

                                                       Vsolid   appar .
                          Relative density: D                                (3.4)
                                                      Venvelop theor .

                          Percent porosity:  porosity  100(1  D)            (3.5)

Where M is the mass (Kg), M m the molar mass (Kg·mol-1), V is the volume (m3), Vm the molar

volume (m3·mol-1), Vsolid the volume of the solid phase in the porous media, and Venvelop the overall

volume including the volume of the solid phase and pore phase in the porous media.


For BT pellet sample, relative density is given as:

                                                   M BT /  BT
                                                            theor .
                                           DBT                        (3.6)
                                                    2 H / 4
For composite Ni paste sample, relative density is given as:
                                     VNi  VBT M Ni /  Ni
                                                        theor .
                                                                 M BT /  BT
                                                                           theor .
                      Delectrode                                                       (3.7)
                                      Venvelop            2 H / 4

Where  BT
        theor .
                ,  Ni
                    theor .
                            are the theoretical density of the BT and Ni; M Ni , M BT are the mass of the Ni

matrix and the BT additives in the electrode, and  , H are the diameter and height of the samples.

   Phase determination

Room temperature X-ray powder diffraction (XRD) was applied to determine the phases of starting
powders. X-ray diffraction is based on Bragg's law. The general relationship between the wavelength
of the incident X-rays, angle of incidence and spacing between the crystal lattice planes of atoms is
known as Bragg's Law, expressed as [79]:
                                                nλ = 2dsinθ (3.8)



- 30 -
                                            Material characterization and sintering behaviour study

Where n (an integer) is the order of reflection, λ is the wavelength of the incident X-rays, d is the
inter-planar space distance of the crystal and θ is the angle of incidence (Fig. 3.1).




                           Figure 3. 1 A schematic for the Bragg‟s scattering [80]


Dry BT and Ni paste samples are analyzed using a Bruker D8 X-ray diffractometer (Billerica, MA,
USA) with Cu Kα1 X-Ray radiation.

   Sintering kinetics

After the removal of binders between 120-230 oC for 30 hrs in air, the samples were sintered in a DIL-
402E dilatometer (NETZSCH, Germany) in 2%H2/Ar atmosphere at 800, 900 and 1150 oC for 1 hr, at
heating rate of 15 oC/min and cooling rate of 50 oC/min. To investigate the effects of dwelling time on
the electrode evolution, dwelling time was varied (t = 0, 5, 10, 15, 20, 25, 30, 45 and 60 min). The
linear shrinkages were measured in real time. Sintering behaviors of pure bulk electrode material and
X5R dielectrics were also measured with a TOM-AC optical dilatometer (Fraunhofer ISC, Würzburg,
Germany) as reference. The images were taken every 60 s and an average image calculated within the
period of the 60 s was saved. Figure 3.2 shows the structure of the TOM-AC optical dilatometer. This
optical dilatometry enables measurement with resolution of 0.4 µm [81]




            Figure 3. 2 TOM-AC optical dilatometer (adapted from user manual of the TOM-AC)


   Scanning Electron Microscopy




                                                                                                 - 31 -
Material characterization and sintering behaviour study

The starting powder of Ni paste and BT dielectrics, the green MLCC chips, the debinded MLCC chips
were characterized suing a FEI/Philips XL30 FEG High-resolution scanning electron microscope
(HR-SEM) (Hillsboro, Oregon, USA). The cross-sections of green and the other sintered chips were
characterized with an AURIGA 60 Focused Ion Beam-Scanning Electron Microscope (FIB-SEM)
(Carl Zeiss, Germany). The chips were embedded in cold resin (EpoFix, Struers) then ground using
SiC sand papers (#240, #600, #800, and #1200) and polished with diamond aqueous suspension
abrasives (diamond particles size from 6 µm, 3 µm, 1 µm, and 0.25 µm). The polished cross-sections
of the samples were cleaned with flowing alcohol and dried quickly with compressed air. The powder
samples were prepared by dropping a small amount of powder on a conductive tape. Prior to the SEM
measurements, the BT power sample, cross-section sample were coated with thin gold thin film in an
argon atmosphere using a sputtering coater (SCD 050, BAL-TEC) at a current of 40 mA for 20 s.


3.3 Results and discussions

   Particle size distribution (PSD)

Table 3.1 shows particle size characteristics of both powders. BT powder has a narrower span,
defined as (D90-D10)/D50, than Ni powder.
                              Table 3.1 particle size of the BT and Ni powder
           Powder      Dmean       D10           D50          D90        Span = (D90-D10)/D50
             BT         0.260     0.16          0.23         0.34               0.783
             Ni         0.181     0.088         0.164        0294               1.257

Figure 3.3 shows the PSDs of the starting powders (Ni powder and BT powder). Both
powders follow a lognormal size distribution function. In MLCC industry, nano sized BT
additives are added into the Ni powders to make the electrode paste. Ueyama et al. [31] reported that
the largest particle size ratio of ceramic (BT) particles/metallic (Ni) particles is 0.155, because it is
required that the smaller ceramic particles enter triple bond spots (three spots) among the Ni particles.
In this work, the mean size of the BT additive nanoparticles for the Ni-MLCC chip is 50 nm.




- 32 -
                                                         Material characterization and sintering behaviour study


                        20                                                                              100
                        18
                        16                                                      frequency               80




        frequency (%)                                                                                           cumulative(%)
                        14                                                      cumulative
                        12                                                                              60
                        10
                         8                                                    Ni powder                 40
                         6
                         4                                                                              20
                         2
                         0                                                                            0
                             0         100         200         300         400         500         600
                                                    particle size (nm)
                        20                                                                              100
                        18
                        16                                                         frequecny            80




                                                                                                             cumulative(%)
                        14




      frequency (%)
                                                                                   cumulative
                        12                                                                              60
                        10
                         8                                                    BT powder                 40
                         6
                         4                                                                              20
                         2
                         0                                                                            0
                             0         100         200         300         400         500         600
                                                 particle size (nm)
                                 Figure 3. 3 Particle size distributions: (a) Ni powder (b) BT powder



   Phase determination

Figure 3.4 shows the XRD patterns of the starting powders. In Figure 3.4(a), only single phase,
tetragonal BT (PDF # 05-0626), is detected from BT powder. As shown in Figure 3.4(b), Ni (PDF #
04-0850) as a major phase and additive BT (PDF #05-0626) as a secondary phase are confirmed in the
Ni paste.




                                                                                                                                - 33 -
Material characterization and sintering behaviour study


                                                                       (110)
                               250                                (101)                                                                       (a)

                               200         tetragonal BaTiO3




            Intensity/counts
                               150
                                                                                                            (211)
                                                                                (111)
                               100                                                        (200)
                                                                                                        (112)
                                                                                                                        (220)
                                50                        (110)
                                                       (001)                            (002)
                                                                                                    (210)
                                                                                                  (201)
                                                                                                                     (202)           (310)
                                                                                                                              (300) (301) (311)
                                                                                                (102)                       (212) (103) (113)
                                 0
                                                                                         (111)
                               7000                                                                                                           (b)
                                              Nickel




           Intensity/counts
                               6000
                               5000          tetragonal BaTiO3

                               4000
                                                                                                   (200)
                               3000
                                                                                            (200)
                               2000                                 (110)
                                                                                            (002)
                                                                                               (210)
                                                                                                                                      (220)
                                                         (110)                                              (211)      (220)
                                                                                               (201)
                               1000                      (001)
                                                                    (101)
                                                                                (111)           (102)       (112)      (202)

                                  0
                                      0     10         20          30            40               50            60              70        80
                                                                                                    o
                                                                               2*theta /
                         Figure 3. 4 XRD pattern of the starting powders: (a) BT powder; (b) Ni paste (debinded)



      Green density

Table 3.2 shows the green density of the compacted pellets of BT sample and Ni paste samples for the
sintering curve measurements.
                                 Table 3.2 Density of BT and Ni pellets for the sintering curve measurements

Materials                                 M (g)    theor . (g/cm3)             (cm)             H (cm)            Venvelop         Vsolid          D
Dielectric BT                             0.5285         6.020                  7.77               6.14             148.889          87.791         0.590
Electrode                        Ni       0.6550         8.908                                                                       73.529
                                                                                7.89               6.22             157.434                         0.536
(Ni:BT=10:1)                     BT       0.0655         6.020                                                                       10.880



      Sintering behavior

Figure 3.5 shows the shrinkage and densification rate of Ni electrode paste and X5R type dielectrics
powders as a function of time. The densification onset temperature of electrode paste was around 450
o
    C, much sooner than that of the dielectrics, 900-950 oC (Fig. 3.5(a)). It can be seen in Figure 3.5(b)
that the maximum densification rate of Ni electrode corresponds to 900 oC. The densification rate
decreases as the temperature increases further. The reason for this decrease in densification rate is the
coarsening of Ni grains. The densification rate of Ni is almost zero when maximum temperature



- 34 -
                                                                                     Material characterization and sintering behaviour study

(1150 oC) is reached. In contrast, the densification rate of BT peaks at 1150 oC and densification
ceases after about 25-30 min dwelling time at this maximum temperature.
                                  0   50                      100     150     200     250                                                                0          50       100         150     200    250
                                                                                            1200                                                                                                          1200
                                                                               Ni     (a)                                                          0.004                                          Ni   (b)
                           0.00
                                                                               BaTiO3     1000                                                                                                    BaTiO3   1000




                                                                                                                      Densification rate (%/min)
                                                                                                                                                   0.000




    Linear shrinkage (%)                                                                           Temperature ( C)                                                                                             Temperature (oC)
                      -0.05
                                                                                            800   o
                                                                                                                                                   -0.004                                                 800

                      -0.10                                                                 600                                                    -0.008                                                 600

                                                                                            400                                                    -0.012                                                 400
                      -0.15
                                                                                                                                                   -0.016
                                                                                            200                                                                                                           200
                      -0.20                                                                                                                        -0.020
                                                                                            0                                                                                                             0
                                  0   50                      100     150     200     250                                                                0          50       100         150     200    250
                                                         Sinter time (min)                                                                                                Sintering time (min)

                                                                    Figure 3. 5 Linear shrinkage of Ni paste and dielectrics


Figure 3.6 shows the densification behaviors of Ni-MLCC chips sintered with different temperature
profiles. The densification of all the Ni-MLCC chips starts around 900 oC that is the same as the
sintering onset temperature of the dielectrics. The densification of the electrode (450-950 oC) does not
contribute to the macroscopic densification of the chips until the dielectrics begin to sinter. All the
densification curves are identical until the temperature reaches 1150 oC. Sintering in the range of 950-
1150 oC accounts for 6-7% shrinkage, that is about half of the final shrinkage. The densification leads
to a ~12% linear shrinkage after holding time of 30 min at 1150 oC. Sintering curves for dwelling time
t = 30-60 min are identical and longer dwelling times do not contribute to further densification.

                                                              0.02                                                     1200

                                                              0.00                                                     1000




                                                                                                Temperature oC)
                                                                                                                                   800
                                                                                    0
                                                                                                       (


                                                              -0.02                                                                600




                                           Linear shrinakge
                                                                                    5
                                                              -0.04                 15
                                                                                                                                   400

                                                                                                                                   200
                                                              -0.06                 20                                                             0
                                                                                    25                                                              0        50     100     150    200
                                                                                                                                                                  sintering time (min)
                                                                                                                                                                                           250
                                                              -0.08
                                                                                    30
                                                              -0.10                 45
                                                              -0.12                 60

                                                              -0.14
                                                                      0        40           80                                                     120            160       200          240
                                                                                         sintering time (min)
                                                                      Figure 3. 6 Linear shrinkage of 1206 type MLCCs



                 Microstructures


                                                                                                                                                                                                           - 35 -
Material characterization and sintering behaviour study

Figure 3.7 shows the morphology of the starting BT and Ni powders. The BT particles (Fig. 3.7(a))
made using solid synthesis are irregular, while Ni powders made using PVD are almost spherical. As
could be seen in the Ni paste, nano scaled BT additives aggregate together.

                                                  (a)                                             (b)

                                                                Ni


                                                                              Nano BT additives




                Figure 3. 7 Starting powders: (a) X5R type BT powder; (b) debinded Nickel paste


Figure 3.8 shows the microstructures of the cross-sections of the green chips before the binder
burnout (BBO). In the ~1 µm-thick electrode, there are about 4-5 layers of Ni particle packing on the
top of each other (Fig. 3.8(a)). Heterogeneities in Ni packing can be observed in the form of pores that
are larger than the particles. Particles arrange into well packed regions (or agglomerates) surrounded
by low density regions. In this work, we refer to pores inside these well-packed agglomerates as intra-
agglomerate pores and to pores in between agglomerates as inter-agglomerate pores. Some authors
use a different wording. Bordia, for example, defines intra and inter- pores as intra and inter- granular
pores [82]. Figure 3.8(b) and (c) show the zoomed Ni packing in the electrode and the BT packing in
the dielectric layer, respectively. The electrode layer is more porous than the dielectric layer The
heterogeneities and high porosity in the electrode might be due to the addition of a significant amount
of organics (40-50 vol.%) which are mixed with powder to enhance the ink rheological property such
that it is suitable for the screen printing process. Note that the nano sized BT additive particles in the
electrode are aggregated. This agglomeration appears probably during the making and/or the drying of
the Ni paste.




- 36 -
                                              Material characterization and sintering behaviour study




Figure 3. 8 Green chips with binders at three different magnifications: (a) 20000 ×; (b)12000 × dielectric layer;
                                              (c) 12000 × Ni layer


Figure 3.9 shows the microstructures of the sample after the first BBO process. The cross-section was
prepared using traditional sectioning and polishing. It is observed that a substantial fraction of inter-
agglomerate pores remain. This may be due to the pulling out of the particles during the polishing
process. After the removal of the polymeric binders, adhesion between nickel particles is degraded.
This means that a conventional sectioning method can be problematic in studying the defect formation
in the electrode.




                Figure 3. 9 SEM images of cross-section of debinded sample: (a) SE; (b) BSE



                                                                                                           - 37 -
Material characterization and sintering behaviour study

Figure 3.10(a) shows the fracture surfaces of the green chips after the first BBO process (230 oC, 34
hrs). Nanocrystalline BT particles dispersed in the nickel matrix can be noticed. They are used to
increase the onset temperature for sintering and reduce the densification rate of electrode layers. After
the second BBO (800 oC, 1 hr), which is required to burn-out the organics binders completely, nickel
powder sintered already, as shown in Figure 3.10(b). No significant modification can be observed in
the BT powder in the dielectrics layers.

                         BaTiO3
                                                                           BaTiO3



          Ni                                                                 Ni
                                     BaTiO3 additives




   Figure 3. 10 SEM images of the fracture cross-sections of (a) green chip and; b) after bake-out at (800 oC)


Figure 3.11 shows the microstructural evolution at different sintering stages. Figure 3.11(a) and (b)
show polished cross-sections of the green chips after the first (230 oC) and second BBO (800 oC). It is
very clear that the electrode already densified during the second BBO. Clustering of Ni particles
occurred and pores were enlarged. When the temperature reaches 900 oC, as shown in Figure 3.11(c),
some discontinuities of electrode form while the particulate nature of BT layers is still recognizable.
When the temperature increases to 1150 oC, the densification of BT layers is obvious. By increasing
dwelling time at 1150 oC (Fig. 3.11(d-h)), the densification of both layers continues. It seems that
electrodes are fully densified after only 10 min while the densification of BT layer is not completed
even after 30 min. Hardly any microstructure changes occur for longer dwelling time as shown in
Figure 3.11(i-l), which correlates well with the absence of further shrinkage at the macroscopic scale
(Fig. 3.6).




- 38 -
                                             Material characterization and sintering behaviour study




          Figure 3. 11 Microstructural evolution of chips sintered with different temperature profiles



   Roughness of electrodes

Roughness is usually measured as a summation of negative and positive deviations from a “mean
plane” fit over the surface of interest referencing to the standard DIN EN ISO 4287:1998. Figure 3.12
shows an example of a roughness profile where variations in the y-direction are depicted as a function
of x.




                                                                                                         - 39 -
Material characterization and sintering behaviour study




                                Figure 3. 12 Roughness on the surface of an electrode


Roughness of the electrode is defined as below in the following relations:
                                                     L

                                                     | f ( x)  z |
                                                Ra  1                  (3.9)
                                                          L x
Where Ra is the arithmetic average surface roughness, or average deviation, Y, of all points from a
plane fit to the test surface over sampling length, L.


Thickness is measured as the arithmetic average thickness of the (L/∆x) segments of electrode, each of
which could be treated as a flat electrode when the ∆x →0.
                            L

                            | f ( x)  f ( x) |
                                   1            2
                                                         1 L                             A
                    Te     0

                                       L / x
                                                     
                                                         L 0
                                                              | f1 ( x)  f 2 ( x) |dx 
                                                                                         L
                                                                                           (3.10)


The linear, or 1-dimensional (1D) electrode discontinuity is defined as the ratio of summation of the
lengths of discontinuous segments (l1, l2,…, ln ) to the entire length (L) considered(See Fig. 3.13).


                   l1                                        l2                               ln

                                                         L

                                Figure 3. 13 A schematic of discontinuous electrode


                                                      l l             ln
                                    Discontinuity1D  1 2                       (3.11)
                                                          l0
Figure 3.14 shows the thicknesses and the linear electrode discontinuity change as a function of
holding time. It turned out that the thickness of electrode layer decreases with sintering of chips at


- 40 -
                                                                   Material characterization and sintering behaviour study

first (densifying phase), but this trend reversed after the holding temperature last for ~15 min
(densification fulfilled). That means swelling of electrodes was observed from this moment.

                                                                                                         0.075                       8
                                  0.90
                                                                                                         0.070

                                  0.88                                                                   0.065
                                                                                                                                     6




       Electrode thickness (m)                                                                                                          Linear discontinuity (%)
                                  0.86                                                                   0.060




                                                                                                                 Roughness Ra (m)
                                                                                                         0.055
                                  0.84
                                                                                                         0.050
                                                                                                                                     4
                                  0.82
                                                                                                         0.045

                                  0.80                                                                   0.040

                                                                                                         0.035                       2
                                  0.78
                                                                                                         0.030
                                  0.76
                                         0       10        20      30       40             50         60
                                                           Dwelling time (min)
                                  Figure 3. 14 Discontinuity and thickness, roughness of electrodes as a function of time


The thicknesses of electrodes changes as a function of holding time. We observed that the thickness of
the electrode layer decreases with sintering of chips at first (densifying phase), but this trend reverses
after a holding temperature of ~15 min (densification fulfilled). This corresponds also to a swelling of
electrodes. This phenomenon was also found in the work of Polotai et al [29]. However, the swelling
of electrodes was not discussed in this paper. The evolution of discontinuities with dwelling time
follows, like the electrode thickness, a non monotonous behavior. A local maximum is observed
around 15 min dwelling time. The reason for this non-intuitive behavior may be linked to the
compressive stresses in the electrode at high temperature that temporarily facilitate the recovery of the
discontinuity of electrode [29]. However, when the densification of BT layers is completed, the
compressive stresses are released and this recovery disappears. The further decrease in the coverage
of electrode is considered to be due to the creep of nickel at elevated temperature and this is
accompanied by swelling and flattening of electrodes. After around 30 min dwelling time,
densification of BT ceases (although not fully densified). While the wavy electrode deforms to fit the
dielectric layers, which is comparatively flatter. This makes the electrode swell in the thickness
direction and the lateral discontinuities become much more severe.




                                                                                                                                                                    - 41 -
Material characterization and sintering behaviour study


3.4 Conclusions

    (1) It is observed that some initial extrinsic pores exist in the green MLCC chips, especially in the
         composite electrode layers. However, the presence of these extrinsic pores needs confirmation
         as they may originate from the sample preparation.

    (2) These artifacts could be problematic in the characterization of the initial defect in the green
         chips.

    (3) It is found that after the second bake out procedure, some nickel particles have already
         sintered, and discontinuities form. However, this slight modification does not cause the
         macroscopic shrinkage, since the BT skeleton does not start to sinter yet.

    (4) Measurement of the thickness of the electrode layers is not accurate, because the cross-section
         of the MLCCs is not necessarily perpendicular to the layers. This is a motivation to use
         focused ion beam machining and utilize non-destructive X-ray tomography.




- 42 -
                                           Synchrotron X-ray imaging of the sintering of MLCCs


4. Synchrotron X-ray imaging of the sintering of MLCCs

Since the discovery of X-rays by W. C. Roentgen in 1895, a wide range of applications have been
developed in X-ray imaging techniques. As a non-destructive detective technique (NDT), X-ray
imaging, including 2D radiography and 3D tomography, is applied to medicine, geosciences [83, 84],
life sciences, mineralogy, archeology, and materials sciences [85-93]. It was commented on
Hounsfield‟s first system for computed X-ray tomography of 1968 that led to a Nobel Prize in
Physiology or Medicine in 1979, “It can be no exaggeration to maintain that no other method within
X-ray diagnostics has, during such a short period of time, led to such remarkable advances, with
regard to research and number of applications, as computer-assisted tomography.” This continues to
be true today [94]. Thanks to the advances in optics and computer sciences, in-situ and real-time X-
ray tomography with nanometric spatial resolution is mature as a NDT routine to image an object.


4.1 Introduction

4.1.1 X-ray computed tomography

The technique of X-ray Computed Tomography (CT) invented by Godfrey Hounsfield in 1972, is
based on X -ray radiography used by doctors when they image tissues in a patient‟s body. However,
rather than taking just one 2D X-ray radiograph, a large number of radiographs are taken at serial
spatial angles. The series of 2D radiographs can then be mathematically reconstructed into a 3D
image. This 3D image can be resliced into stacks at arbitrary orientation. For interested readers, a
history of the X-ray CT can be found in Ref. [95].




                   Figure 4. 1 A schematic diagram of the X-ray image acquisitions [96]




                                                                                              - 43 -
Synchrotron X-ray imaging of the sintering of MLCCs

The acquisition of a 2D radiograph is based on the Beer's Law. The intensity of a monochromatic X-
ray beam travelling through a homogeneous material is:
                                      I  I 0 exp[ x]          (4.1)

Where I0 and I are the incident and transmitted X-ray intensities, µ is the material's linear attenuation
coefficient (unit m-1) and x is the length of the X-ray path. A high value of the constant μ corresponds
to an efficient absorption of X-rays by the considered material, with only a small amount of photons
reaching the detector. If there are multiple materials, the equation becomes:

                                    I  I 0 exp[  i xi ]           (4.2)
                                                     i

Where µi is the attenuation coefficient of the ith material. In a well-calibrated system using a
monochromatic X-ray source (i.e. synchrotron), this equation can be solved directly. If a
polychromatic X-ray source is used and as the attenuation coefficient strongly depends on X-ray
energy, the complete solution would require solving the equation over the range of the X-ray energy
(E) spectrum utilized:

                             I   I 0 ( E ) exp[ i ( E ) xi ]dE           (4.3)
                                                 i

There are a number of methods by which the X-ray attenuation data can be converted into an image
[97]. The classical approach is called "filtered back projection", in which the linear data acquired at
each angular orientation are convolved with a specially designed filter and then back-projected across
a pixel field at the same angle. As demonstrated in Figure 4.2, a series of images are recorded at
successive tilts (Fig. 4.2(a)), and then these images are back projected in along their original tilt
directions into a three-dimensional object space. The overlap of all of the back-projections will define
the reconstructed object (Fig.4.2 (b)). However, the mathematics behind is out of scope in this thesis,
and can be found in Ref. [97].




- 44 -
                                            Synchrotron X-ray imaging of the sintering of MLCCs




    Figure 4. 2 A schematic diagram of tomographic reconstruction using the back-projection method [85].


Owing to advances in optics, spatial resolution of 10-50 nm has been achieved recently [98-101].
Withers [94] shows resolution of X-ray tomography techniques as a function of X-ray energy (see Fig.
4.3). Advances in Nano scale X-ray tomography techniques and related applications were recently
reviewed by Sakdinawat [102].




                                                                                                      - 45 -
Synchrotron X-ray imaging of the sintering of MLCCs




Figure 4. 3 Spatial resolutions achievable with different lenses: calculated resolutions (open symbols), measured
 resolutions (filled symbols); synchrotron source (circle symbol) and lab sources (square symbol) (reproduced
                                               after Withers [94])



4.1.2 Application to sintering

As a non-destructive 3D characterization technique, X-ray CT has superior capabilities over
traditional optical microscopy, SEM, and other tomography techniques. It has been applied in
different domains of material sciences recently [103, 104]. With advanced detectors and optics at the
synchrotron, high-resolution, in-situ, high temperature real-time observation of microstructure
evolutions becomes available and routine. In-situ X-ray µCT has been utilized in the studies on the
solidification of alloys [105-108]. In the domain of particulate materials, It covers packing and
rearrangement of particles in granular materials [109, 110] (also coupled with DEM) and porous
media [111].

X-ray CT was first used for the study on the sintering of glass beads by Bernard and coworkers in
2001 [112]. The technique was then used by Lame [113, 114], Vagnon [115, 116], and Olmos [117,
118] to study the sintering of metallic powder under atmosphere. Xu [119] and Niu [120] studied the
sintering of ceramic particles with in-situ X-ray CT. Bernard and Guillon investigated the constrained
sintering of glass films on rigid substrates [121]. Co-sintering of multilayered systems, i.e., SOFCs,
was extensively studied using X-ray CT [122-127].




- 46 -
                                             Synchrotron X-ray imaging of the sintering of MLCCs


4.2 Experiment procedure

4.2.1 Set-up: Transmission X-ray Microscope

As a direct analog to the visible light microscope or transmission electron microscope (TEM), a
Transmission X-ray Microscope (TXM) consists of a capillary condenser lens, an objective lens
(Fresnel zone plate) and detector system (Fig. 4.4).




 Figure 4. 4 A schematic illustration of a TXM imaging system consisting of a condenser lens, objective lens,
       and detector system. Beamstop and pinhole block out the unfocused x-rays (After Nelson [128])


The capillary condenser lens is to focus the X-ray beam generated by the X-ray source onto the
sample and the objective lens is to magnify the X-ray image passing through the sample to form an
image on the detector plane. The detector is typically a scintillated camera consisting of scintillator
screen that converts X-ray beam into visible light, and a fiber-optics taper or visible light microscope
objective to relay the visible light to a high-resolution Charge-Coupled Device (CCD) sensor or a
Complementary Metal-Oxide-Semiconductor (CMOS) detector. The unique properties of synchrotron
radiation lie in its continuous spectrum, high flux and brightness, as well as high coherence, which
make it an indispensable tool in the exploration of matter. Figure 4.4 shows the TXM system setup at
the Sector 32-IDC at the APS synchrotron (Advanced Photon Source, Argonne National Lab, USA),
which was used in this work. The X-ray lens typically provides 10-50 times magnification while the
visible light system in the detector assembly provides an additional factor of 2-20 times magnification.
That gives a typical total magnification of between 200-1000 times. For example, the TXM at the
APS [129, 130] has an X-ray magnification of 80 times while the visible light magnification is 10,
resulting in an overall 800 times magnification. Thus, to a typical detector pixel size of 10 μm
corresponds an effective pixel size of 12.5 nm in the sample.




                                                                                                        - 47 -
Synchrotron X-ray imaging of the sintering of MLCCs

Figure 4.5 shows the experimental set up for the X-ray CT data acquisition. The heating unit is
designed for the in-situ real time X-ray imaging.
                                             thermocouple


                       cooling water                                      x-ray port
                                       copper housing
                                                                         x-ray beam

                      CCD sensor
                                    furnace unit

                                       zone plate
                                                                             pin hole
                                                               sample holder
                                            sample stage


           Figure 4. 5 A schematic for the setup of the TXM at Sector 32-IDC of APS Synchrotron



4.2.2 Sample preparation using FIB milling

In order to maximize the quality of the reconstruction, the sample should be contained within the field
of view (FOV = 26 µm) of the TXM at the required magnification during rotation. If the region of
interest (ROI) is not maintained within the FOV for the full rotation, the algorithm must essentially
reconstruct an incomplete data set. Ultimately, this increases the noise observed in the reconstruction.
Furthermore, in tomographic studies of composite materials (including porous ones) phase
identification is typically achieved by observation of the spatial distribution of X-ray absorption.
However, if the sample is not maintained within the X-ray FOV throughout the rotation, the
attenuation due to sample geometry and that due to material composition cannot be separated, leading
to challenges in reconstructing the difference phases within large specimens. Banhart [131] provides
further discussion of this limitation due to “missing data”.

Commercial 0603 size (1.6 × 0.8 × 0.8 mm3) Ni-MLCC chips and 01005 size (0.4 × 0.2 × 0.2 mm3)
Pd-MLCC chips (Samsung Electro-Mechanics, Suwon, South Korea) were used in our study. These
green chips were first roughly machined into 60 μm cone shape with a special micro drill (see Fig.
4.6). The tip was then milled by a Quanta 3D FEG FIB-SEM (FEI, USA) into a 20 μm-diameter
cylinder of 20 μm height (Fig. 4.7).




- 48 -
                                                Synchrotron X-ray imaging of the sintering of MLCCs




                               Figure 4. 6 Photograph of a microscope adapted drill


After organics were burnt out between 120 and 230 oC for 30 hrs in air, the Ni-MLCC sample was
imaged with TXM operating at 8.9 KeV before and after sintering (in 5% H2+Ar atmosphere at 1100
o
    C for 2 hrs, heating/cooling at 15 °C/min).

                                 machining
                                      ω         micro drill
                          electrode         v


     Step 1:

                          dielectric
                                    MLCC chip




                             FIB milling
                                             Ga+
                        Φ60×100µm


     Step 2:

                       ceramic glue



                                      alumina base

                            Figure 4. 7 Two-step preparation of sample for X-ray nCT




                                                                                             - 49 -
Synchrotron X-ray imaging of the sintering of MLCCs


4.2.3 Image acquisition and 3D reconstruction

An attempt was made to image in-situ the sintering of a cylindrical Ni-MLCC sample on beam-lime.
To simulate the reducing sintering atmosphere, 2%H2-N2 gas was introduced from the top opening,
before the heating up of the furnace. The sample was heated from room temperature at a heating rate
of 15 oC/min until 1150 oC and was sintered for 1 hr at 1150 oC. During the sintering, 2D X-ray
radiographs were taken every 20 oC increment and every 5 min during the dwelling time. However, no
shrinkage was noticed during this standard sintering cycle. This is because with the current facility,
the furnace is open for the insertion of the sample, which means that the reducing atmosphere (pO2 =
10-11-10-9 atom) normally required for the successful sintering of nickel electrodes cannot be
guaranteed. It showed that the sintering of Ni electrode was significantly modified due to the
oxidation of the metal particles and no obvious densification was observed during the thermal cycle.
A compromise is to characterize the sintered Ni-MLCC sample ex-situ. To explore the missing gap
during the thermal cycle, the sintering of Pd-MLCC chip in air was used to simulate the sintering of
Ni-MLCC in a reducing atmosphere. Pd exhibits excellent oxidation resistance. Hence, the sintering
behavior of the Ni electrode in reducing atmosphere is assumed similar to the sintering of Pd
electrode in the air. Note that the nano-sized ceramic inclusions were not used in the Pd electrode.

For the Ni-MLCC sample, an ex-situ experiment was carried out. A cylindrical Ni-MLCC sample was
imaged before and after sintering. When the X-ray imaging was being conducted, the sample was
rotated every 0.25o, each 2D projection image was collected in 2 s from a CCD camera with 2048 ×
2048 pixels, which corresponds to the FOV of 26 μm. The sintering was conducted in a tube furnace
in 2%H2-N2 reducing atmosphere with heating/cooling rates of 15 oC/min and dwelling time of 1 hr.

For Pd-MLCCs, no specific atmosphere was used during the sintering. In-situ observation of sintering
of Pd-MLCC was carried out as a reference. The sample was mounted onto a movable stage. A
FibHeat200-XRD furnace (MHI, OH, USA) with an Ø 6 mm heating chamber was driven by a 1693-
model DC power supply (BK Precision, CA, USA). The input current of the furnace was controlled to
obtain the required temperature ramps. A type S thermocouple was introduced from the top port. Its
tip was located approximately 1 mm away from the sample (position controlled by microscopy). The
temperature measurement was calibrated with Au particles located upon the sample. The melting of
Au particles (indicated by the flowing of the material) was observed between the recorded
temperatures of 1050 °C and 1070 °C (melting point of Au is 1064 °C). The heating unit was water-
cooled so that it could operate for a long period of time at high temperature (1200 oC) without
disturbing the alignment of the pin hole and zone plate. The sample was inserted through the opening
at the bottom of the chamber and the region of interest was positioned in the center of the X-ray
microscope window. The sample was heated up to 1200 oC at 10 oC/min, held for 60 min at this
temperature and cooled down to room temperature at 15 oC/min. The sample was aligned in rotation

- 50 -
                                               Synchrotron X-ray imaging of the sintering of MLCCs

and its position was kept all along the experiment to ensure 2D projections quality. 2D projections
were recorded every 50 oC during the heating ramp below 900 oC, and every 20 oC between 900 and
1200 oC.


3D data acquisition was not possible during sintering because such a measurement takes 20-30 min
(360-720 projections). During that period of time, the microstructure changes rapidly, which does not
allow any reliable reconstruction with the filtered back projection algorithm. Thus, 3D data
acquisition was only conducted on the green sample at room temperature. Additionally, 3D X-ray data
acquisitions were carried out on additional samples that were partially sintered at 900 oC and 1100 oC,
respectively. These acquisitions allow 2D projection data to be re-interpreted more accurately.


3D microstructures were reconstructed using the classical filtered back-projection algorithm from the
series of 2D projection images with TXMReconstructor software package (Xradia, Inc., Pleasanton,
CA, USA).

4.3 Results and discussion

4.3.1 Ex-situ X-ray CT on Ni-MLCC sample

Figure 4.8(b) and (c) are typical 2D projection images collected directly from the CCD camera before
and after sintering, respectively. Figure 4.8(d) and (e) show the reconstructed microstructure from 2D
images.




 Figure 4. 8 (a) MLCC sample for X-ray tomography; (b), (c) 2D projection images before and after sintering,
respectively (the layers are indexed for later use); and (d), (e) Reconstructed 3D microstructure before and after
                                             sintering, respectively.



                                                                                                            - 51 -
Synchrotron X-ray imaging of the sintering of MLCCs

The bright areas correspond to the Ni phase and the dark areas correspond to the BT phase (as the
photon energy was 8.9 KeV, above the Ni absorption edge [128]), please see the attenuation length 4
of Ni and BT as a function of beam energy (Fig. 4.9).




                   Attenuation length (micron)
                                                 30
                                                              Nickel
                                                 25
                                                              BaTiO3
                                                 20
                                                 15
                                                 10
                                                 5
                                                 0
                                                      0   2000 4000 6000 8000                     10000
                                                              Photon energy (eV)
                                                          Figure 4. 9 BT and Ni absorption edge


3D raw data was filtered using the Edge-Preserving Smoothing Filter, segmented and rendered using
Avizo software (VGS, France). Figure 4.10 shows 3D rendering of a representative volume extracted
from reconstructed microstructures. Note that the volumes are from the same spot of the same sample
before (Fig. 4.10 (a) and (b)) and after (Fig. 4.10 (c) and (d)) sintering.


In Figure 4.10(a), BT particles in the dielectrics and Ni particles in the electrodes are distinguishable.
Nano-sized BT additives dispersed in Ni matrix cannot be discriminated into individual particles as
the size of the contact areas is below the spatial resolution. Heterogeneous zones are found in the
electrodes, with Ni particles having lower contact number and with smaller local density. Figure
4.10(b) shows the pore network in the green MLCC chip. Clear discontinuities are found in Ni layers
after sintering (Fig. 4.10(c)). These discontinuities correspond to very large pores (Fig. 4.10(d)) that
reduce the effective electrode overlapping area and hence the total capacitance of the capacitor.
Isolated pores are present within the partially densified BT layer.




4
 The depth into the material measured along the surface normal where the intensity of x-rays falls to 1/e of its
value at the surface.


- 52 -
                                               Synchrotron X-ray imaging of the sintering of MLCCs




  Figure 4. 10 Microstructural changes of MLCC sample (Ni in purple, BT in green and pores in yellow): (a)
      before sintering, (b) pore network before sintering, (c) after sintering, and (d) pores after sintering


With benefit of the X-ray nanotomography technique, we have been able to observe the 3D
morphology of discontinuities in electrodes in an ex-situ test. The exact orientation of layers can be
tracked and we can correlate the displacement of matter within the sample induced by sintering.




                                                                                    Sintered

                        Green
 Fig 4.11 Schematic for the mass correlation before and after sintering in the electrode (the red areas represent
                                           the pores in the electrode)


                                                                                                                - 53 -
Synchrotron X-ray imaging of the sintering of MLCCs

Fig 4.11 shows the mass correlation in the electrode before and after sintering process. The electrode
is subdivided by a n × n grid. The pores (in red) in the sintered electrode can be approximately
represented by connected mosaics. It is assumed that the strain in the electrode plane is isotropic. The
area in the green electrode mapped from this mosaic defined pore is considered to be the original area
that evolves into the final discontinuous area.


Figure 4.12 shows the morphology of the inner electrode #2 before and after sintering from the top
view. The disconnected areas (#1ʹ-8ʹ) correspond well to the initial heterogeneities (#1-8). The
relative densities of these areas are much lower than the average relative density (D = 0.51) of the
green electrode (Fig. 4.12(a)). Ni particles in these low density regions have lower coordination
number. However, the larger porosity in Ni layers near the edge does not result in any discontinuity
probably due to the proximity of the free boundary.

                                                       (a)                                                 (b)
                                                                                     4’
                             4
                                                0.48
                             0.45           5                                               5’
                                                                           3’
               3                                6
                     0.44
                                                    0.44
                                                                                                    6’
                                 7    0.44                                           7’
                                                                      2’
             2     0.42
                                       8
                                     0.45                                                  8’
                      0.40
                                                                                1’
                     1

                                                    2μm                                                  2μm

  Figure 4. 12 Morphology of inner electrode #2: (a) initial microstructure and (b) final microstructures after
   sintering, respectively. Microstructures of electrodes #3-4 (not present) are similar to that of electrode #2.


Thanks to the 3D tomographic data that is saved as a stack with voxel size of 26 × 26 × 26 nm3,
quantifications of the microstructure and its changes can be implemented using ImageJ (NIH, USA)
together with specific plugins. For example, the discontinuity rate of the electrodes, strains and the
density in the BT layers are of great interest for understanding the co-sintering of the multilayer
system.

Take the electrode #2 for example; its areal (2D) discontinuity is defined as the ratio of the
discontinuous areas (a1, a2, ·
                             ·,
                              ·an) to the entire area (A0):



- 54 -
                                              Synchrotron X-ray imaging of the sintering of MLCCs


                                                            a1  a2    an
                                Discontinuity2D                                                    (4.4)
                                                                    A0

The radial and axial strains in the BT layers are calculated as
                                      r  ln(l r / l0r )
                                                                       (4.5)
                                      a  ln(l a / l0a )
         r       a
Where l and l denotes the radial and the axial dimensions of the BT layers images and l0r and l0a

the reference dimension of the layer measured from the 3D microstructure.


The relative density of the sintered BT layers is defined as the solid volume ( Vsolid ) fraction over the

total volume ( Vtotal ):

                                                  Vsolid
                                        DBT                         (4.6)
                                                  Vtotal
Figure 4.13(a) shows that the top electrode layer has smaller discontinuity (6%) than inner layers (14-
16%). Figure 4.13(b) shows the true axial and radial strains of dielectric layers after co-sintering.
Axial strains (11-14%) are larger than radial strains (5-7%), as it is expected from geometrically
constrained systems [75]. A smaller anisotropy is observed for BT layer #2, which is closer to the top
free surface of the specimen. Under free sintering conditions shrinkage is expected to be almost
isotropic, although structural anisotropy may be brought by tape casting and lamination. It is also
interesting to observe that the swelling of electrodes is about 16% on average along the thickness
direction. Figure 4.13(c) presents the relative density of the different BT layers, showing a decrease in
achieved density as function of layer position in the multilayer.

In view of these microstructures and considering the relatively small thermal expansion mismatch
between Ni and BT (αNi=16.3×10-6 /oC, αBT=11×10-6 /oC [132]), we propose that the electrode
discontinuities originate predominantly from the sintering strain mismatch. Ni powders sinter at a
lower temperature (400-450 oC) than BT powders (950-1000 oC) [29]. Due to their larger
densification rate at low temperature (<1050-1100 oC), the Ni layers are under tensile stresses while
the BT layers are almost rigid. The more constraint imposed on the Ni layer, the larger the
discontinuities. This explains the presence of a smaller discontinuity for the top electrode layer, which
can almost sinter freely, as compared to the inner ones which are under more constraint from adjacent
layers. At higher temperature (1100 oC) already densified Ni layers are under compressive stress, and
they may deform by creep [133]. Due to poor wettability between Ni and BT layer [134], the viscous
Ni layer tends to contract laterally, finally resulting in swelling of the electrodes. Contrasting with Ni
layers, dielectric BT layers are under tensile stress, which explains that the shrinkage along the
thickness direction is larger than in-plane. The top BT layer is only constrained by the bottom Ni layer,



                                                                                                   - 55 -
Synchrotron X-ray imaging of the sintering of MLCCs

i.e., to a less degree than other inner BT layers during sintering. This explains the higher relative
density of the top BT layer in comparison with inner ones.

                                                    16                                    (a)



                                Discontiniuty (%)
                                                    14
                                                    12
                                                    10
                                                     8
                                                     6
                                                               1        2        3       4
                                                                   Electrode layer No.
                                             -0.02                      axial strain      (b)
                                                                        radial strain
                                             -0.04
                                             -0.06

                              Strain
                                             -0.08
                                             -0.10
                                             -0.12
                                             -0.14
                                                               1        2        3      4
                                                                   Dielectric layer No.
                                                    1.00
                                                                                          (c)
                                                    0.95




                               Relative density
                                                    0.90
                                                    0.85
                                                    0.80
                                                    0.75
                                                    0.70
                                                           1           2          3          4
                                                                   Dielectric layer No.
Figure 4. 13 (a) Discontinuity of electrodes; (b) Axial and radial strains in different BT layers, irregular top BT
 layer (#1) was not considered and (c) Relative densities of BT layers (The layers are indexed as in Fig. 4.8(c)).


4.3.2 In situ X-ray imaging of Pd-MLCC

Figure 4.14 shows the selected images of the region of interest obtained during the sintering cycle.
The light grey phase corresponds to the BNT dielectrics while stronger X-ray absorption of Pd
electrode leads to a dark grey phase. It should be noted that the elliptical shape of the projected
electrode is due to the incident angle between the X-ray beam and the electrode plane. The initial
microstructure of the electrodes exhibits some heterogeneities as implied by the grey level distribution
in the electrode layers shown in Figure 4.14(a). The darker grey regions are the high density regions,
while the lighter grey regions are the low density regions where particles have smaller coordination


- 56 -
                                               Synchrotron X-ray imaging of the sintering of MLCCs

numbers. Such heterogeneities are common in green thin layers, especially when layers are composed
of only a few particles piled on top of each other.




  Figure 4. 14 Microstructural evolutions during sintering of a Pd-MLCC sample. Note that Au particles were
     used both for image alignment in the reconstruction and for calibrating the temperature in the furnace.


Neither clear microstructural evolution nor densification could be observed below 800 oC. At 900 oC
(Fig. 4.14(b)), the Pd electrode layers appear more inhomogeneous. As Pd particles densify, the
contrast with neighboring pores is getting stronger due to increased X-ray attenuation differences. The
darkened regions indicating densified Pd suggest that sintering of Pd particles has started already at
900 °C. As sintering proceeds (Fig. 4.14(c-g)), the pores evolve into a number of discontinuities in the
electrode layer. Fig. 4.14(h-i) indicate that no obvious microstructure change occur during the cooling
ramp.




                                                                                                          - 57 -
Synchrotron X-ray imaging of the sintering of MLCCs

Figure 4.15 illustrates the morphology evolution of the electrodes at the different stages by 3D X-ray
nCT.




 Figure 4. 15 3D reconstruction and rendering of the electrodes in the Pd-MLCC sample (top view): (a) green
state; (b) partially sintered at 900 oC; (c) partially sintered at 1100 oC (E1); and (d) partially sintered at 1100 oC
                                                        (E2)


Figure 4.15(a) shows the morphology of an electrode from the sample tested in situ. Circled areas
point to the low-density regions. Differential densification takes place in powder compacts of
heterogeneous nature [43]. Particles in high-density regions sinter faster than those in low-density
regions and form clusters. Some particles in the low-density regions de-sinter and large pores appear
(Fig. 4.15(b)). Finally, pores enlarge and lead to discontinuous areas in electrode layers (Figs. 4.15(c)
and 4.15(d)). These discontinuities result in capacitance loss.


Continuous recording of the 2D radiographs allows radial and axial strains of the electrode and
dielectrics layers to be calculated directly from dimensional changes. However, the axial strain in the
electrode is not measured due to the uncertainty in thickness correlated to the elliptical projection (due
to the incident angle between the X-ray beam and the electrode plane). Anisotropic sintering behavior
of different layers is shown in Figure 4.16.


- 58 -
                                                Synchrotron X-ray imaging of the sintering of MLCCs


                         0.2                                                     a , E1
                                                                                           1200
                                                                                 a , E2
                         0.1
                                                                                 r , D1
                                                                                           1000
                                                                                 r , D2
                         0.0




                                                                                                  Temperature( C)
                                                                                 a , D1 800     o

                         -0.1                                                    a , D2
                Strain                                                                     600
                         -0.2
                                                                                           400
                         -0.3
                                                                                           200
                         -0.4

                         -0.50                                                           0
                                   50       100 150 200                      250       300
                                              Time (min)
  Figure 4. 16 Radial and axial strains in dielectrics layers, radial strains in electrodes as function of time (E1
          stands for 1st electrode, E2 for 2nd electrode, D1 for 1st dielectric, and D2 for 2nd dielectric).


It is found that the radial shrinkage of the top electrode layer (E1, c.f. Fig. 4.14(b)) is smaller than that
of the second layer (E2). This difference cannot be attributed to the initial conditions since the two
layers should be very much similar. It must be related to differences in constraint levels during
sintering as already observed on Ni-MLCCs. The top electrode layer has only one adjacent dielectric
layer on the bottom. This layer acts as a rigid substrate and imposes a geometrical constraint. In
contrast, the second electrode is constrained by both adjacent layers. This difference has consequences
on the radial shrinkage but also more significantly on the degree of discontinuity. The discontinuity,
defined as percentage of uncovered areas over the total electrode area, is smaller in the top electrode
layer (~56.1%) than in the second electrode layer (~60.4%) as shown in Figure. 4.15(c) and (d). These
electrode discontinuities are much larger than those in commercial Pd-MLCCs. The reason is that in
our experiment design the electrodes are not encapsulated in ceramics, thus easily swell and expand
during sintering (Fig. 4.15). This swelling of electrodes (creep deformation without any volume
change) leads to a further increase in electrode discontinuity.

In a single dielectric layer, the strain anisotropy is initially negligible. However, as the temperature
reaches approximately 1000 °C, the axial strain exceeds the radial strain. As temperature increases, it
is also observed that the dielectric layers sinter faster than the electrode layers. This sintering strain-
rate mismatch results in in-plane tensile stresses in the dielectrics layers. These stresses accelerate the
axial shrinkage of the dielectric materials through Poisson‟s coupling. A difference of ~0.1 between

                                                                                                                    - 59 -
Synchrotron X-ray imaging of the sintering of MLCCs

axial and radial strains is measured after the sintering cycle. Both radial and axial strains are nearly
equal in the first and second dielectric layers, which are sintered under the same constraining
conditions.

From the strain measurement and microstructure evolution in the 2D projections, it can be concluded
that the cooling process does not affect much MLCCs. The thermal contraction during cooling has
thus a negligible effect on microstructure compared to the sintering shrinkage and rules out a possible
creep deformation of Pd induced by differential thermal contraction. This indicates that discontinuities
in the electrodes are primarily linked to the sintering strain mismatch during the heating ramp.

We finally propose a possible mechanism for electrode microstructure changes during sintering of Ni-
MLCCs as schematized in Figure 4.17. After lamination of BT sheets, there are heterogeneous regions
in the electrodes. Below 950-1000 oC the Ni powder densifies except in heterogeneous zones (Fig.
4.17(a)) where de-sintering is observed [71] (Fig. 4.17(b)). As discussed earlier, at this stage the Ni
layers are under tensile stress. The tensile stress in the thinner sections induces matter flow towards
the thicker sections [76] (Fig. 4.17(c)) until the thinner sections are disrupted and discontinuities form.
Once nickel is fully dense, electrodes are subjected to compressive stress at high temperature (1100 oC)
due to BT densification (Fig. 4.17(d)). The compressive stress causes contraction of the viscous Ni,
resulting in swelling of electrodes and hence a further increase in electrode discontinuity (Fig.
4.17(e)). Meanwhile, the nano-sized BT additives are discarded by Ni due to their unwettability with
Ni at high temperature. They aggregate and sinter, possibly forming percolation between two adjacent
BT layers and enhancing the mechanical adhesion between Ni and BT layers in the MLCCs.




                 Figure 4. 17 A schematic of the defect evolution mechanism during sintering




- 60 -
                                          Synchrotron X-ray imaging of the sintering of MLCCs


4.4 Conclusion

   (1) Synchrotron X-ray nano-tomography was for the first time used to study the microstructural
      changes during sintering of single MLCCs. As shown here, this unique technique enables 3D
      visualization of the internal microstructure as well as the quantification of features such as
      strains in three directions for each layer, defect size and morphology.

   (2) In-situ X-ray imaging of sintering of Pd-MLCC chips confirmed that the final electrode
      discontinuities originate from the initial heterogeneities through a differential densification
      process. The formation of discontinuity occurs at the early stage of sintering of MLCC when
      the dielectric layers serve as constraining substrates.

   (3) However, we show that care must be taken in interpreting results. The sintering behavior of
      the extracted small sample may deviate from that of a real several-hundred-layer chip. In a
      sample with very few layers, as used in these nano-tomographic experiments, external and
      internal layers are not submitted to the same constraints, thus resulting in different
      discontinuity levels.




                                                                                               - 61 -
Synchrotron X-ray imaging of the sintering of MLCCs




- 62 -
                                             Correlative studies using FIB-SEM nanotomography


5. Correlative studies using FIB-SEM nanotomography

It has been demonstrated in Chapter 4 that the X-ray nano computed tomography (nCT) enables the
comparison of the microstructure change before and after sintering. However, its resolution is not
sufficient to resolve the submicrometric particle packing or identify the nano BT additives.
Characterization of this green microstructure at the particle length scale is however necessary,
because: (i) the initial contact configuration between particles determines their sintering behavior and
final microstructure; (ii) it provides us with realistic input for the DEM numerical simulations. We
make use here of the excellent resolution of Focused Ion Beam (FIB)/SEM nanotomography (FIB-nT),
which is rapidly emerging as a powerful tool to characterize the 3D microstructure, grain orientations,
and chemical compositions in micrometric devices or materials. FIB-nT is utilized here to image
green and sintered MLCCs, including the very MLCC sample characterized using X-ray nCT.
Comparison between the two techniques is the scope of the present chapter.


5.1 Introduction

Compared with other tomography techniques (see Fig. 5.1), FIB tomography is currently of great
technological importance because of its high resolution and capability of analyzing a comparatively
large volume of the material. The typical resolutions (lateral pixels and slicing steps) which can be
reached by the FIB tomography are from tens of nm down to a few nm, depending on the quality of
the equipment available. The FIB tomography technique can reach better resolution than X-ray
tomography and mechanical serial sectioning. Although TEM tomography and 3D Atomic Probe have
achieved higher resolutions, but the volume that these two techniques can probe is limited to 0.1-1
µm3. Hence, the small volume investigated may not be representative of the whole sample.




                                                                                                  - 63 -
Correlative studies using FIB-SEM nanotomography




               Figure 5. 1 Resolution of different tomography techniques (after Holzer [135])


Nowadays, the automated acquisition of large image stacks of fine resolutions (below 10 nm) using
FIB serial sectioning can be accomplished by following standard routines. The latest FIB/SEM system
is capable of performing multi-channel acquisitions of microstructural (BSE, SE), chemical (EDX)
[136-138] and crystallographic (EBSD) [139] information with different detectors from the same
sample. FIB tomography is becoming a versatile method and widely applied in materials [137, 138,
140, 141], life [142-144], and geosciences [145, 146]. A good example of application of FIB
tomography is 3D characterization of particulate media [140, 147, 148]. This unique technique is still
young but developing rapidly. The advances in FIB tomography and its applications have recently
been review by Kubis [149], Munroe [141] and Holzer [135].

   Working principle

Modern FIB/SEM machines are equipped with ion and electron optical columns. These dual-beam
systems are integrated with high precision MEMS (Microelectromechanical Systems) which make
them perfect tools for high precision serial sectioning and/or high-resolution imaging. As Figure 5.2
shows in a dual-beam FIB-SEM, separated ion gun and electron gun integrated in one chamber
typically by an angle of 52o (FEI series) or 54o (Carl Zeiss series). They can work both independently


- 64 -
                                             Correlative studies using FIB-SEM nanotomography

and synergistically. The ion gun can be utilized in nano-machining and nano-fabrication. An example
of this application is the TEM lamella preparation with a lift-out technique [150]. It also may serve as
a SEM with the electron beam working solely.




                       Figure 5. 2 Dual beam FIB-SEM system (after Volkert [151])


Anyhow, definite advantages of dual-beam FIB-SEM lie in in-situ sectioning and imaging. This
allows users to conduct fine milling with the ion beam normal to the specimen surface and
simultaneously image using the electron beam.


As depicted in Figure 5.3, in a dual-beam FIB-SEM system, the ion beam (y-direction) can etch (mill)
away material with close to nanometric (within the range of 10 nm) precision and the sample can be
rotated with a numerically controlled stage; the electron beam interact with the ion beam treated
surface (x- and y-directions), and signals are collected by different detectors. Alternating performance
of sectioning and imaging is secured without disturbing the sample. The sample is placed at the
eucentric point, so that the electron beam that interacts with the surface can be scanned with a
constant angle without changing sample position. During the acquisition of the image stack, the
imaging plane is moving in the z-direction at a prescribed interval that is either equal or non-equal to
the lateral pixels, resulting in a stack with isotropic or anisotropic voxels. This sequential sectioning
process can be automated.




                                                                                                   - 65 -
Correlative studies using FIB-SEM nanotomography




                  Figure 5. 3 A schematic for the FIB serial sectioning (after Holzer [135])


The entire serial sectioning procedure includes three phases that are described below: (1) cube
preparation and optimization of parameters, (2) serial sectioning, and (3) data processing.

(1) Sample preparation

Before starting the FIB serial sectioning routine, several sectioning and imaging parameters that are
dependent on each other have to be optimized such as, beam energy, magnification, slicing step.
Resolution is determined by the scale that should be sufficient for evaluating microstructural,
chemical, or crystallographic features in the sample. The magnification and volume relate to the
resolution. Definition of an optimum magnification, the relationship between depth penetration of the
electron beam and excitation volume of BSE and X-rays also must be taken into account. This
relationship is illustrated in Figure 5.4 with SiO2 as reference materials.




              Figure 5. 4 Electron material (SiO2) interaction diagram (adapted from Salh [152])


- 66 -
                                                Correlative studies using FIB-SEM nanotomography

Depending on the beam energy, the size of the BSE interaction volume can influence the effective
resolution of FIB tomography. For instance, the depth of the BSE excitation at 5 kV is larger than 100
nm, which is too large for nano scale investigations. In contrast, at 1 kV the BSE excitation depth is in
the range of a few nm which makes it a suitable parameter for nano scale analysis. By the same
reasoning, slicing step size should be in line with this scale. For example, serial sectioning at ≥ 5 kV
(SEM) with a step size in the 10 nm range will lead to a strong oversampling.


In addition, for non-conductive samples a thick conductive coating (carbon, platinum) should be
deposited beforehand to secure images of good quality by avoiding charging effects. Trenches are
created to prepare a cube as the volume of interest.

(2) Data acquisition

In this step, the major concern is the drifting correction in z- direction and xy plane. In order to
produce a regular stack of images which can directly be transformed into a voxel-based data volume,
z-step size of milling should have similar scales to the xy pixels (i.e., approximately 10 nm). Because
the acquisition of hundreds of images can lasts for 20 hours or even longer, drifting can become
significant. Without correction, the drifting in z- direction causes z- distortions (nonevent z- step size)
in the reconstructed 3D microstructure. The drifting can be compensated by pattern recognition by
tracking fiduciary markers [140]. However, in modern FIB/SEM systems have become much more
stable, and usually after a period of stabilization and thermal equilibration drifting becomes very small
or even negligible. In contrast, drift components in x- and y- directions can be compensated during the
post processing with image alignment and registration.


In practice, the z-drift correction can be verified by measuring the distance between two lines which
form a certain angle (Fig. 5.5(a) and (b)). According to geometry, the average z-step size is:
                                               z0 d n  d 0
                                        z                        (5.1)
                                               d0     n
Where n is the number of slices, dn is the distance between the two crossing lines, d0 is the initial
distance, z0 is the distance from the intersect to the edge.


The x- and y- direction drift causes the images to move out of the field of view. For those images
within the field of view, due to slight xy- drift, structure in z- direction is not continuous. This type of
drift can be corrected offline. As shown in Fig. 5.5(a), before slicing, two fine paralleled lines that are
perpendicular to the surface were made with FIB milling, these two points at a constant distance can
be used as alignment references. After the alignment, two straight lines should be reconstructed.




                                                                                                     - 67 -
Correlative studies using FIB-SEM nanotomography


                                  ion beam
                                                            e- beam
                                                                                 (b)
          fiduciary marker                                                                  l3        l4
                                                      54o
                                  l2
                                                                                                                   Z0
                                                                                   z             dn
                         l1       l3    l4                                              x                      nΔz
                                                                                                 d0
                              Z                  x                                                         Z step size= Δz
                                             y
                                                                                  (c)
                                                                                                      l1      l2
                                                                                   z

    (a)
                                                                                        x
                                                                             y



                                       Figure 5. 5 The schematic of drift correction


In addition to the drift compensation, further corrections are needed because of the tilting angle (52 ◦
for FEI system, 54◦ for Zeiss system) in dual beam systems.

Focus correction:      during the serial sectioning, the imaging plane is shifted in z-direction and
therefore focus tracking is required in order to correct for the increasing working distances. When
shifting the working distance and imaging under oblique angle, the region of interest is shifted out of
the field of view. This has to be compensated with automated region tracking.

Fore-shortening correction: When imaging is conducted at an angle incident to the surface, the
images are not taken from front view. A tilt-correction must be applied to remove the fore-shortening
effects of imaging.

In modern dual beam FIB/SEM systems, all these phenomena are compensated with the automated
sectioning procedure. In this way, image stacks of high quality can be acquired.

(3) Data processing

Care should be taken to obtain usable and valuable data from the 3D stacks. Usually, depending on
the material system to be dealt with, specific treatments should be employed correspondingly.
Nevertheless, some general procedures of image processing can be described as follows:
    -     Image alignment registration for 3D-reconstruction
    -     Removal of noises and spikes using filters (e.g., median filter)
    -     Segmentation of different phases (different materials, pores, etc.)
    -     Separation of individual objects for subsequent statistical analysis
    -     Visualization of volume, surface or orthotic sections based in 3D grey-scale data

- 68 -
                                                  Correlative studies using FIB-SEM nanotomography

      -   Quantitative analysis and statistical measurement of features (i.e., particle/pore size
          distributions, surface area, shape factors)


For       interested   reader,    a    standard     FIB    tomography      wizard    is   available   at
(http://www.vsg3d.com/webinar-3d-fib-tomography-and-reconstruction-materials).


5.2 Experiments

5.2.1 Experiment setup

In this work, a nVision 40 (Figure 5.6) and a AURIGA 60 FIB-SEM (Carl Zeiss, Germany) were used
to conduct the serial sectional data acquisitions. SE, BSE detectors were used to obtain the
microstructure features and EDX detector was used to determine the composition.




                          Figure 5. 6 Configuration of the Nvison 40 FIB/SEM [153]


5.2.2 Materials and procedures

     Materials

Commercial 0603 case size Ni-MLCC chips fabricated at Samsung (See section 3.1) were used in this
work. The cylindrical Ni-MLCC sample (#1), in the green (g) state (#1-g) and after sintering (#1-s)
are detailed in Chapter 4. Cross-sections of a green (#2-g) Ni-MLCC chip (binder removed) and a
sintered (#3) MLCC chip were prepared by traditional metallography procedures. Sample #1-s-ct that



                                                                                                  - 69 -
Correlative studies using FIB-SEM nanotomography

was saved from the non-destructive X-ray nCT characterization was mounted onto conductive paste
glued on the sample holder. Details of the samples examined are listed in Table 5.1.


The thickness step (z pixel) for ion beam milling was adjusted to be equal to the xy pixels to obtain an
isotropic voxel. Sample #1-g and sample #2 are for comparison of microstructures in the green state
between with X-ray nCT and FIB-nT. Sample #1-s and sample #1-s-ct are for comparison in the
sintered state. Sample #3 is extracted from an entire 0603 MLCC chip sintered under the same
conditions as the cylindrical sample (#1-g, #1-s-ct) to investigate the representativity of the cylindrical
sample and possible size effect. The data acquisition on sample #3 was conducted with a larger voxel
size (30 × 30 × 30 nm3) so that a larger volume can be obtained.
                             Table 5.1 The details of the samples that were analyzed
                                                                Slice       Voxel size       Analyzed
                    Heat treatments             Methods
                                                               number       (x,y,z nm)     volume(µm3)
    # 1-g      @230 oC, 2 hours, air           X-ray nCT          -        26×26 × 26       Ø 20 × 20
             Heating/cooling:15 oC/min,
    # 1-s                                      X-ray nCT          -        26×26 × 26       Ø 20 × 20
              1150 oC, 1hr, N2+2%H2
                                                FIB-SEM
    #2            @230 oC, 2 hours, air                          473         5 × 5× 5     9.8 × 6.6 × 2.3
                                                (SE,BSE)
                                                FIB-SEM
# 1-s-ct                                                         578         5× 5× 5       6.5 × 5.1× 3.4
             Heating/cooling:15 oC/min,         (SE,BSE)
             @1150 oC, 1hr, N2+2%H2             FIB-SEM
    #3                                                           400       30 × 30 × 30   15.3×12.0 ×7.6
                                                (SE,BSE)


     Procedure

Data acquisition on a green 0603 Ni-MLCC (sample #2) was conducted using the nVision 40 FIB-
SEM at the CMTC, Grenoble INP (Fig. 5.7).




                                  Figure 5. 7 Serial sectioning on the sample #2


Figure 5.8 shows the serial sectioning of the sample #1-s-ct. Note that the fiduciary marker was not
used because the pattern recognition feature has not been integrated into this system at this moment.




- 70 -
                                              Correlative studies using FIB-SEM nanotomography




                            Figure 5. 8 Serial sectioning on the sample # 1-s-ct


Data acquisition on sample #3 (Fig. 5.9) was conducted using AURIGA 60 FIB-SEM at IMT,
University of Jena. The etched cross served as the fiduciary mark for the pattern tacking. Two
correctional lines were made to verify the final reconstructed microstructure.




                              Figure 5. 9 Serial sectioning on the sample # 3


5.2.3 Image processing

The goal of image processing is: (1) to separate the pores, Ni and BT particles in the green and
sintered samples and extract the microstructural parameters such as pore size, orientations, particle
size distribution of Ni and BT particles; (2) to quantify the discontinuity and roundness of the
electrode.

For this, the following steps have to be followed:

   Slice alignment

This pretreatment can be done manually or automated. It consists of image registration and shearing
correction.




                                                                                               - 71 -
Correlative studies using FIB-SEM nanotomography

Image registration: each slice is used as the template with respect to which the next slice is aligned, so
that the alignment proceeds by propagation [154]. In this work, the mapping of coordinates takes into
consideration of translation and rotation. The new coordinate u is given by:
                                       cos     sin  
                                                         u  u (5.2)
                                       sin    cos  
Registration can be done using an ImageJ plugin called StackReg [154] or using registration module
in Avizo. After registration, the stack is as shown in Figure 5.10(d).

Shearing correction: a shearing by θ in -y direction would be found, this could be corrected by a pre-
alignment with the two correlational lines Figure 5.10(c) before the registration, or shearing a certain
angle -θ using the shearing module under Avizo.

Finally, the stack was cropped into a cube as shown in Figure 5.10(f). It is noted that the pre-designed
straight lines on the surface are kept straight as they should. This means that the reconstructed 3D
microstructure is quite reliable.




                                    Figure 5. 10 Image pretreatment flow chart


   Filtering

(1) Removal of noise


- 72 -
                                                 Correlative studies using FIB-SEM nanotomography

A 3D median filter was used to remove the noise [155]. Figure 5.11(a) shows the principle of the
median filter. Pixel with high value (which is assumed as a noise) is replaced by the median value in
its local neighborhood. In doing this, it preserves edges while removing noise. Figure 5.11(b) and (c)
show the one slice of the FIB-BSE stack before and after the application of the 3D median filter.




 Figure 5. 11 Removal of noise using 3D median filter: (a) principle of the median filter,(b) a slice of FIB BSE
                stack of green MLCC (sample #2), and (c)after filtering using 3D median filter.


(2) Removal of shadowing

Due to the incident angle between the electron beam and the sample surface, the bottom part of the
images appears darker. This shadow can be problematic when segmenting images. However it can be
removed by subtracting the gray gradient. This procedure can be done by using an ImageJ filter plugin
“fit polynomial”. As shown in Figure 5.12 after this correction, there are two sharp peaks in the gray
value histogram. The first peak corresponds to the dark-gray phase BT, while the second one the
light-gray phase Ni.




                                                                                                          - 73 -
Correlative studies using FIB-SEM nanotomography




  Figure 5. 12 (a) an original slice (b) the gray gradient of the slice, (c) resulting image after subtraction of the
 gradient image, (d) histogram of the original image a, (e) histogram of the filtered image c, (f) the pore phase
               separated from the original image, and (g) the pores in the image after the filtering


Figure 5.13 shows the pretreated and corrected processed stacks for samples #2, #1-s-ct and #3.




                      Figure 5. 13 3D reconstructed volume for (a) #2, (b) #1-s-ct and (c) #3


- 74 -
                                             Correlative studies using FIB-SEM nanotomography


5.3 Comparison of FIB-nT with X-ray nCT

5.3.1 Characterization of green microstructures

Figure 5.14 shows the microstructure of representative volume of 0603 MLCC obtained by X-ray
nCT (#1-g) (Figure 5.14(a)) and FIB-nT (#2) (Fig. 5.14(b)). As for the microstructure obtained with
the FIB-nT, the Ni and all BT particles, even the nano scale BT additives in the electrode, are
discernible. Hence, the FIB-nT is an ideal tool to finely characterize the microstructure of the present
MLCCs. Conversely, when using X-ray nCT, pore structure is distinguishable, but particles cannot be
decomposed as the size of their contacting area is under resolution. We have demonstrated in Chapter
4 that the porous regions or the heterogeneities are associated with the final discontinuities of
electrode. In this sense, the quality offered by X-ray nCT is sufficient to study the formation of
discontinuities.




Figure 5. 14 Microstructures of the green MLCC with X-ray nCT (column a: sample #1-g) and FIB-nT (column
                                             b: sample #2)




                                                                                                  - 75 -
Correlative studies using FIB-SEM nanotomography


5.3.2 Characterization of sintered microstructures

Figure 5.15 shows the comparison of the microstructures of the final microstructure (sintered) with X-
ray nCT and FIB-nT. Note that the microstructures originate from the same location of the same
sample. It can be noticed that the morphology of the discontinuities and of the pores are quite
consistent with each other. Although X-ray nCT image has good Ni/BT phase contrast, pores are still
blurry. This X-ray nCT image is preferable for evaluation of the electrode morphology. The FIB-SE
image exhibits good solid/pore phase contrast. Thus it is preferable for pore quantification. The FIB-
BSE image has good Ni/BT phase contrast, and the Ni grains, entrapped BT additives are discernible.




 Figure 5. 15 X-ray nCT (column a) and FIB tomography (SE mode: column b), (BSE mode: column c) on the
                                            final microstructure


Through these qualitative comparisons, we conclude that X-ray nCT is efficient to characterize
defects in the MLCCs, while the better resolution of FIB-nT provides more information on pore
characteristic, grains, and additives. Combining the strengths of the non-destructive X-ray nCT and
the high resolution FIB-nT, correlative studies can be carried out. In the following section, the
quantitative correlative studies are presented.


5.3.3 Evaluation of pore size

Figure 5.16 shows the pore percolation in the BT layers before and after sintering. In both the green
and sintered microstructures, the 3D pores are highly percolated, making it inappropriate to separate
the pores.


- 76 -
                                                 Correlative studies using FIB-SEM nanotomography




            Figure 5. 16 Percolation of pores and skeletons: (a) before sintering; (b) after sintering


In 2D, individual pores in sections are generally easy to isolate before characterization. Separating the
continuous 3D pore space into individual pores is technically feasible; however, this depends on the
definition of a pore. As Bernard et al. [121] argued, there is no intrinsic partition of the 3D pore space
and the definition of pore must be related to a physical phenomenon.

In this work, the pore size distribution is statistically analyzed from the 2D sections using line
intercepts (in practice, 1-pixel thick). The segmentation of the pore phases is very decisive to the
accuracy of the pore size measurement. With the high resolution FIB-nT, the pore/solid phase contrast
is excellent. We use the porosity measured with FIB tomographic data as a benchmark (refer to Table
5.2). When we segment the pores in the microstructure obtained by X-ray nCT, first we need to
ensure that the porosity is the same as that obtained from the FIB tomographic data. Figure 5.17
compares the pore size distributions in the Ni layers and BT layers in both green and sintered MLCC
chips.

The pore size distribution measurements with X-ray CT and FIB-nT are reasonably in agreement with
each other in terms of the mode, median, mean and frequency (i.e., they are in the same size bin).
However, distribution curve for the X-ray nCT is not as smooth as that for the FIB-nT. This is
probably due to the differences in dataset quality. The voxel size for the CT microstructure is indeed
26 nm, while for FIB tomography microstructure, it is 5 nm.




                                                                                                         - 77 -
Correlative studies using FIB-SEM nanotomography


                                        20
                                        18           (a)
                                                                         FIB tomography
                                        16                               X-ray nCT
                                        14
                                        12

                       frequency
                                        10
                                         8                               pores in BT layer
                                         6                                (green MLCC)
                                         4
                                         2
                                         0
                                                 0     100 200 300 400 500 600 700
                                                                 pore size (nm)
                                        18           (b)
                                        16                            FIB tomography
                                        14                            X-ray nCT


                       freqency (%)
                                        12
                                        10
                                         8
                                         6                                pores in Ni layer
                                         4                                 (green MLCC)
                                         2
                                         0
                                                 0         200     400     600     800    1000
                                                                 pore size (nm)
                                        20
                                                     (c)                   FIB tomography
                                        15
                                                                           X-ray CT




                              frequency(%)
                                        10
                                                                          Pores in BT layer
                                             5                            (sintered MLCC)


                                             0
                                                 0         200     400     600     800    1000
                                                                 pore size (nm)
    Figure 5. 17 Pore size distribution in the BT (a) and Ni (b) layer obtained with X-ray nCT and FIB-nT


Given the same volume in voxels, the size of the dataset for X-ray nCT is 1/5 of that for the FIB-nT.
Nevertheless, we can conclude that the X-ray nCT, as a pore scale analysis tool, is sufficient to study
pore evolution.

In addition, note that the average pore size (160 nm, Ni layer Figure 5.17(b)) is close to the average
particle size (180 nm, see Figure 3.3(b) in Chapter 3). Most of the pores can be referred to as intrinsic
pores, which have the same scale of the particles. The fraction of larger pores (~800 nm, that is 4-5

- 78 -
                                              Correlative studies using FIB-SEM nanotomography

times large the particles) remains small. These large pores are extrinsic pores, which are considered at
the origin of electrode discontinuity (Chapter 4). The pores (extrinsic and intrinsic pores) in the
sintered BT layers (Fig. 5.17(c)) do not contribute to the formation of discontinuities in the BT layer,
because the BT layer is thicker. During sintering, both types of pores disappear.


5.4 Particle size distribution (PSD)

The geometry and packing of the particles are key factors for the final microstructures; hence, the
evaluation of the particle size distribution (PSD) is of much interest to this study. The initial
particulate characteristics will be used both to identify possible initial defects and to provide input
parameters for the DEM simulations. We take the advantage of the high-resolution FIB tomography to
implement this task. Segmentation and separation are required to quantify the microstructure.


5.4.1 Segmentation

Ni and BT particles (including the nano sized BT additives) as well as pores have sharp contrast as
shown in Figure 5.18(a-b). Following the de-shadowing processing, thresholding process was applied
to the stack to separate different phases by choosing corresponding threshold value (Fig. 5.18(c)).
However, due to edge effect, some sharp corners of the BT particles were recognized as Ni particles
(Fig. 5.18(d)). The median filter is capable of eliminating these errors, but as a consequence of this
filter some pixels in the real Ni particles disappear. In this work, the noise with volume under 150
voxels (an approximate size of 30 nm) is firstly labeled and eliminated (Fig. 5.18(e)). Some artifacts
that were recognized as Ni (above 150 voxels) can be removed manually by filling the selected
volume with background color (Fig. 5.18(f)). The original image is then superimposed with Ni phase
(Fig. 5.18(g)) to obtain sharper contrast. The BT particles in the dielectric layers and the BT additives
in the electrode are identified (Fig. 5.18(h)). The remaining phase corresponds to pores (Fig. 5.18(i)).




                                                                                                   - 79 -
Correlative studies using FIB-SEM nanotomography


                                    (a)           Ni                      (b)
                 Ni                                                                                 BT               (c)
                                                                                     pore
                                                                                                               Ni
                                                         nano BT additives
         BT
                                          BT
                                                                                              111        160


                                    (d)                                   (e)                                         (f)




                                    (g)                                    (h)                                        (i)




   Figure 5. 18 (a) an original slice, (b) a zoomed in area of the original image, (c) histogram of the slice, (d)
       identification of Ni phase, (e) removal of noises from image d, (f) manual removal of the artifacts, (g)
imposition of the electrode on the original image, (h) identification of the BT phase, and (i) the remaining pore
                                                        phase


5.4.2 3D watershed segmentation

Watershed segmentation [156] is usually preferred for separating touching features in an image that
are mostly convex.

This algorithm simulates the flooding from a set of labeled regions in a 2D or 3D image. It expands
the regions according to a priority map, until the regions reach the watershed lines. The process can be
understood as progressive immersion in a landscape (Fig. 5.19). This algorithm depends on two inputs:

  I.      Definition of the ultimate points (or, maxima): these maxima are labeled as different marker
          regions that are used as seeds for the flooding. It is like the water trying to retrieve the
          catchment areas. In doing this, there will be as many separated objects as markers.
 II.      Definition of Euclidean distance map: a grey image representing the landscape height field
          that controls the flood progression and finally the location of watershed separations. These
          separations are located on the crest lines between valleys of landscape, so called watershed
          (Fig. 5.19).



- 80 -
                                              Correlative studies using FIB-SEM nanotomography




The curve represents three minima, A,    A is flooded at the levels 1 and 2,   A and C are flooded until reaching
B and C and two maxima D and E. The      but not B. Then it reaches point C.       point D. D belongs to the
 set of markers contains only A and C          C: From the next level                watershed. But not E
           Figure 5. 19 Definition of watershed in a watershed segmentation algorithm from [157]



5.4.3 Particle size distribution

Figure 5.20 shows the separation of the Ni particle using the 3D watershed segmentation routine in
the Avizo Fire packages.




                                                                                                      - 81 -
Correlative studies using FIB-SEM nanotomography

    Figure 5. 20 Separation of Ni particles using 3D watershed segmentation (Avizo Fire): (a) binary stack
 consisting of connected nickel particles; (b) the Euclidean distance map of the binary stack; (c) binary image
  and watershed lines; (d) separation by subtracting the watershed lines from the binary image; (e) deletion of
               sectioned particles on the borders; (f) rendering of the randomly colored particles


Once the particles are separated, particulate characteristics, such as volume, surface area, equivalent
diameter, sphericity and centroid can be calculated.
An equivalent diameter is used to describe the particle size. It is defined as:
                                                     d  (6V /  )1/3   (5.3)
Figure 5.21 shows the 3D visualization of the separated Ni packing of the electrode (Fig. 5.21(a)) and
the corresponding PSD for the Ni particles measured by FIB-nT and laser scattering (LS) (Fig.
5.21(b)). Figure 5.21(b) demonstrates that the PSDs with laser scattering (based on 2D projection) and
the FIB-nT are consistent with each other. Because the Ni particles are almost spherical, the 2D
projection size (LS) is identical to the 3D size (FIB). The slight variation may be attributed to the
sampling size. For the laser scattering data collection, the sample size is approximately 1000 particles,
while for the FIB tomography volume, there were about 1500 particles segmented in total.



                                         (a)




                                         (b)
                                    18
                                    16                                    Laser scattering
                                    14                                    FIB tomography



                    frequency (%)
                                    12
                                    10
                                     8
                                     6
                                     4
                                     2
                                     0
                                         0     100      200      300    400     500   600
                                                         particle size (nm)
   Figure 5. 21 3D watershed segmentation of Ni particles: (a) 3D view of separated Ni particles, colors are
    randomly assigned (BT inclusions not considered); (b) PSD measured with FIB-nT and laser scattering.


- 82 -
                                                 Correlative studies using FIB-SEM nanotomography

The same 3D watershed algorithm was applied to separate the BT particles in the dielectrics layer as
shown in Figure 5.22.




 Figure 5. 22 3D watershed segmentation for the BT particles in a representative dielectric layer: (a) gray level
 image, (b) binary image, (c) Euclidean distance map, (d) result at maxima size= 1 pixel, (e) result at maxima
                               size = 2 pixels, (f) result at maxima size =3 pixels


We have shown here that care should be taken when applying the 3D watershed segmentation to the
irregular particle systems. As detailed in the principles of the watershed, the maximum (ultimate point,
calculated from a binary image) acts as a seed that will be used to retrieve the catchments. Thus, the
number of maxima dictates the final number of separated objects. An overestimation of the number of
maxima leads to an over segmented image (as shown by the arrows in Figure 5.22(d)). This happens
when the object exhibits a concave feature. In that case, more than one maxima will be found in the
volume of object (3D watershed). In another extreme case, if the maxima size is too large, contacting
particles will be treated as one (under segmentation shown in Figure 5.22(f)). So the option of the


                                                                                                           - 83 -
Correlative studies using FIB-SEM nanotomography

maxima size should be examined for each segmentation until an acceptable error is found. The
ultimate decision for minimizing this error is made visually. In this work, the maximum size for the
BT particle segmentation has been set to 2 pixels. Figure 5.23 shows the separated BT particles and
the PSD with different maxima size.



                                         (a)




                                         (b)
                                    18
                                                                             Laser scattering
                                    16
                                                                             maxima 1 pixel
                                    14                                       maxima 2 pixels




                    frequency (%)
                                    12                                       maxima 3 pixels
                                    10
                                     8
                                     6
                                     4
                                     2
                                     0
                                         0     100   200     300       400     500     600
                                                      particle size (nm)
Figure 5. 23 Result of the 3D watershed segmentation of BT particles in the BT layer: (a) 3D view of separated
BT particles, colors are assigned randomly;(b) PSD measured with laser scattering and FIB-nT (maxima size =
                                                     1, 2, 3 pixels)


Figure 5.23 indicates that the 2D projection based on LSA method predicts smaller particles size than
the FIB-nT method. This is consistent with Kelly et al‟s [158] argument which states that, for
nonspherical particles, image analysis leads to much larger particle sizes compared to laser diffraction.
This is because laser diffraction undercounts events generated by larger dimensions (major chord) or
rather overestimates the contribution of minor chord data.


5.4.4 Particle size distribution in 2D and 3D

Characterization of particles using FIB-nT is not simple. It cannot be accessed as easily as optical
microscopy or SEM. In this section, an attempt is to establish the correlation between a traditional 2D

- 84 -
                                                      Correlative studies using FIB-SEM nanotomography

sectioning measurements (SEM, OM) and 3D measurements (FIB tomography). By virtue of the 3D
data, cross-sections can be attained by re-slicing the volume at an arbitrary angle. So the 2D
measurement can be performed very easily by following a similar routine.


In this work, the model for unfolding cross-sections of spherical particle as described by classical
stereology (see Russ‟ book [155]) is employed. The scheme dates back to Wicksell‟s work in 1925
[159] and has been refined by Schwartz [160] and Saltykov [161]. The simple idea is to use a thin
plane to section the mono-size particles to obtain a mapping relation between 2D and 3D statistics as
depicted in Figure 5.24.




 Figure 5. 24 Sectioning a sphere randomly produce a distribution of circle sizes, which can be calculated from
                                             analytical geometry (after [155])


The particles are distributed in a certain fashion (e.g., log-normal). We assume that each class of
particles is mono-sized and can be unfolded using the classical stereology. For a 3D measurement, Fi
stands for the frequency of the particle falling in the i-th bin. By multiplying the unfolding matrix, a fi
is obtained for the corresponding frequency of the sectioned size that falls in the same bin. In this
work, a 24 × 24 (n=24) system matrix is used.

            1           1
                               2
                                          1
                                                 2
                                                             1
                                                                    2
                                                                                      1
                                                                                            2
                                                                                                  F
   f1                                                                                           1
                    1 1          1 1            1 1                  1 1 
                         2               3                4                     n

   f  0              1
                      1 
                              2
                                     1
                                          2
                                             2
                                   1   1 
                                                 2
                                                        1
                                                            2
                                                                2
                                                      1   1 
                                                                    2
                                                                             1   1  
                                                                               1
                                                                                   2
                                                                                           2
                                                                                               2
                                                                                                     F 
   2                 2           3    3        4     4            n         n
                                                                                                     2
   f3  0            0                 2
                                       1 
                                               2
                                                        2
                                                            2
                                                                3
                                                      1   1 
                                                                    2
                                                                               2
                                                                                   2
                                                                             1   1 
                                                                                           3
                                                                                               2

                                                                                           n 
                                                                                                      F3 
                                                                                                 
                                         3            4     4            n
                                                                                                              (5.3)
                                                                                           4 
   f 4  0                                                                                       
                                                                                                       F4
                                                                2                  2           2
                       0                 0                  3
                                                          1 
                                                            4
                                                                               3
                                                                             1   1 
                                                                               n         n
                                                                                                
                                                                                                F 
   f n  0
                                                                                                   n 
                                                                                           2
                     0                 0                  0                   1
                                                                                    n1 
                                                                                    n 
                                                                                         




                                                                                                                 - 85 -
Correlative studies using FIB-SEM nanotomography

Figure 5.25 shows the correlations between the PSD of nickel particles in 2D and 3D. The 2D
sectioning method underestimates the true size. After being corrected with the 24 × 24 system matrix,
the results are shown as the blue curve in Figure 5.25.
                                   18
                                   16                                  FIB tomography 3D
                                                                       FIB tomography 2D



                   frequency (%)
                                   14
                                   12                                  unfolding from 2D to 3D
                                   10
                                    8
                                    6
                                    4
                                    2
                                    0
                                        0      100       200       300       400       500       600
                                                        particle size (nm)
               Figure 5. 25 Correlation between PSDs in 2D and 3D using the unfolding scheme



5.5 Heterogeneities in the green electrode

Figure 5.26(a) shows the 3D microstructures rendered with Avizo. Figure 5.26(b-d) shows the cross-
sections of the Ni green electrode in three orthogonal planes. The average relative density is D = 0.50.
However, local densities deviate from this average volume very much. This is because the Ni particles
are not homogeneously arranged. As can be seen from the cross sections (Fig. 5.26(b-d)), they are
either separated by pores or BT additives (not displayed in the image). In addition to these
heterogeneities, the thickness of the electrode is not constant (Fig. 5.26(b)).




 Figure 5. 26 (a) 3D rendering of the electrode (the electrode plane is xz); (b) xy middle plane cross-section; (c)
                                   zy middle plane cross-section; (d) xz middle plane cross-section

- 86 -
                                                                     Correlative studies using FIB-SEM nanotomography

Figure 5.27 plots the density (areal density in the serial slices) profile probed in x (Fig. 5.27(a)), y (Fig.
5.27(b)), z (Fig. 5.27(c)) direction. The peaks and valleys imply respectively the high density regions
and low density regions, which can be referred to as heterogeneities. The heterogeneities can be
located easily by the peaks and valleys‟ coordinates (in pixel). The discrepancy in the local relative
density reaches up to 0.25 as shown in Figure 5.27(a).




                relative density (%)
                                       70
                                       65
                                                (a)
                                       60
                                       55
                                       50
                                       45
                                       40
                                       35
                                            0          200      400        600       800       1000       1200
                                                           distance in x direction (pixel)




               relative density (%)
                                       54       (b)
                                       52

                                       50

                                       48

                                       46
                                            0     10 20 30 40 50 60 70 80 90 100 110
                                                 distance in y (thickness) direction (pixel)




               relative density (%)
                                       56       (c)
                                       52

                                       48

                                       44

                                       40
                                            0         50     100 150 200 250 300 350 400 450
                                                           distance in z direction (pixel)
                                       Figure 5. 27 Density profile in x, y, z direction (1 pixel represents 5 nm)


Figure 5.28 shows the particle coordination number map at two reprehensive heterogeneities. Slice
#40 (xy slice in z direction) has the lowest density while the slice #60 has the highest density. The
average coordination number in the high density regions is larger than that in the low density regions.
Consider now the thickness of the electrode that sometimes consists only of a few particles. The
coordination numbers are computed from 2D cross-sections. Since the step size is only 5 nm (1 pixel),
we think the 2D coordination map is sufficient to signify the spatial heterogeneity.



                                                                                                                     - 87 -
Correlative studies using FIB-SEM nanotomography




                    Figure 5. 28 Coordination number map for the xz plane cross-sections



5.6 Porosity

As reviewed in Chapter 2, size and morphology of pores evolve as sintering proceeds. The pores can
further play a role in physical and mechanical properties of the functional materials. Anisotropic pore
development can also give valuable information on the sintering conditions (e.g., pressure-assisted,
constrained sintering).

In the binary image, solid and pore phase are represented by 1 (black) and 0 (white). By counting the
white pixels or voxels, pore area (2D) or pore volume (3D) is obtained. The ratio of the pore area
(volume) to the envelope area (volume) represents the 2D and 3D porosity. Table 5.2 presents the 2D
and 3D relative density in the three BT layers.

Green density in the BT layers is ~61%; while it is 56% for the electrode (including the 5.4% of BT
additives). For porous media, in absence of heterogeneities, the 2D density (porosity) should be equal
to the 3D measurement [162]. Density discrepancy in 2D and 3D for the Ni layers is larger than that
for the BT layers. This echoes the significant heterogeneities in the electrode layers as previously
shown in Figure 5.26.




- 88 -
                                              Correlative studies using FIB-SEM nanotomography

                          Table 5.2 Average 2D and 3D density in different layers
                                               Layer Density(2D) Density(3D) Porosity(3D)
                                                E1      52.9        51.9         43.6
                                                E2      54.8        52.7         41.5
                                   Electrode
                                                E3      53.7        50.9         43.2
                                               Avg.     53.8        51.8         42.8
                                                E1       6.2         4.5           -
                                                E2       6.2         5.8           -
                                   Additives
                                                E3       4.5         5.9           -
                                               Avg.      5.6         5.4           -
                                                D1      62.4        63.5         36.5
                                                D2      61.1        59.7         40.3
                                   Dielectrics
                                                D3      59.9        60.8         39.2
                                               Avg.     61.1        61.3         38.7



5.7 Anisotropy

5.7.1 Pore orientation in BT layer

Understanding the effect of geometrical constraint during the co-sintering of multilayers should help
to manage the control of the microstructure. Anisotropy development has been reported both in
experiments and in numerical simulations on constrained sintering thin films on rigid substrates [121,
163]. For the same reason, we evaluate pore orientation based on 2D cross-sections. As Figure 5.29(a)
and (b) show, pores in the cross-section of the sintered sample are well isolated. These pores can be
fitted as ellipses that have the same area and moments (first and the secondary moment) as the
original pores (Fig. 5.29(c)). The major and minor axes define the shape of the ellipse. The orientation
of pores is defined as the anti-clockwise angle between the major axis and the x axis. (Fig. 5.29(d)).




                           Figure 5.29 Pore orientations in the 2D cross-section

                                                                                                  - 89 -
Correlative studies using FIB-SEM nanotomography

By using the particle analyzer in ImageJ, a best-fitting algorithm [164] is performed to generate
equivalent ellipses and to obtain the orientation angle information.

The circularity C is defined as the ratio of A the area of a circle having a perimeter equal to P:
                                                                         4 A
                                                                  C          (5.3)
                                                                          P2
In practice, particles whose circularity is 1 and aspect ratio is less than 1.05 are not taken into account
when the statistics is carried out.

Figure 5.30(a) shows the polar plot of the angular frequency as a function of the angle (0-180o). Note
that, the curves for the other half (180-360o) is duplicated symmetrically for demonstration.

In the green state (black curve), most of the pores are elongated along θ = 140-160o. In tape casting, it
has been observed that textured pores elongate along the tape casting direction [165] due to the fact
that the particles are preferentially orientated along the tape casting direction during the die-slot tape
casting procedure. It indicates that the tape casting direction is along θ = 150o in the selected
coordinate system (Fig. 5.30(b)). After sintering, the fraction of pores that are oriented along the
original tape casting direction increases (red curve). This means that pores further elongate along their
original orientation during sintering. During sintering, smaller intra-agglomerate pores may pinch off
and disappear while larger inter-agglomerate pores, which are elongated in the tape casting direction,
remain.

                      (a)                             90                                       (b)
                  8                     120                         60
                  7
                  6                                                                                             z‟
                  5         150                                                  30
                  4
                  3                                                                        z


  frequency (%)
                  2
                  1                                                                                             x‟
                      180                                                              0
                  1                                                                                              x
                  2
                                                                                                   (c)                z‟
                  3
                  4                                                                                z
                  5         210                                                  330
                  6
                  7
                                                                                                       x             x‟
                  8                     240                         300                                    y‟
                                                     270
                                                                                               y
                                  xz plane (green)         xz plane (sintered)

                                      Figure 5. 30 Pore orientation in the xz- plane before and after sintering




- 90 -
                                                        Correlative studies using FIB-SEM nanotomography

To examine the role of initial anisotropy induced by tape casting during sintering, new planes were
created as shown in Figure 5.30(b). x’y’ plane is considered parallel to the tape casting direction; y’z’
plane is perpendicular to the tape casting direction.

Figure 5.31 shows pore orientation statistics in the vertical plane x’y’ before (black curve) and after
(red curve) sintering. The frequency of the pores that orient along the tape casting is initially about
3%. After sintering, the frequency of the pores that orient in the tape casting direction increased to
11%. The change is probably caused by the in-plane (x’z’) compressive stresses developed during co-
sintering of multilayers, on top of the contribution due to the disappearance of the intra-agglomerate
pores. Before the BT starts to sinter (1000-1050 oC), the rapid sintering of Ni layers imposes
compressive stresses, which facilitate the rearrangement and further sintering of the BT particles.
Pores preferentially elongate along the direction of the compressive load. This stress induced
anisotropy can be analogous to that produced during sinter forging, that is, pores preferentially orient
along the direction of the external load [166]. However, once the dielectric layer really starts to
densify, an in-plane tensile stress develops, which should lead to pores oriented along the thickness
direction as observed in alumina films [167]. But co-sintering of YSZ layers [168] revealed that
possible large pores may evolve as the macroscopic shrinkage of the sintering body (which means
perpendicular to the compressive loading direction) as evidenced by additional sinter-forging
experiments on porous bodies containing artificial large pores [82].

                                                                90
                                  14
                                                  120                         60
                                  12
                                  10
                                   8     150                                             30
                                   6




                  frequency (%)
                                   4
                                   2
                                       180                                                     0
                                  2
                                  4
                                  6
                                  8      210                                             330
                                  10
                                  12
                                                  240                         300
                                  14
                                                                 270
                                               x'y' plane (green)      x'y' plane (sintered)

                    Figure 5. 31 Pore orientation in the x’y’ plane before and after sintering




                                                                                                   - 91 -
Correlative studies using FIB-SEM nanotomography

Figure 5. 32 shows the orientation statistics of the pore 2D sections in the y’z’ plane, which is also
through the thickness but perpendicular to the casting direction. The initial 2D sections of the pores
are randomly orientated. It is interesting to observe that after sintering this initial random distribution
tends to orientate along the horizontal direction (parallel to the in-plane stresses). The frequency of
the 2D pore sections that orient at θ = 0 in y’z’ plane does not increase as significantly as that in x’y’
plane (Fig. 5.31). This is supportive evidence that the disappearance of the intra-agglomerate pores
also contribute to the increase in the pores that orient in the stress loading direction.

                                                                 90
                                  6
                                                  120                           60
                                  5
                                  4
                                      150                                                   30
                                  3




                  frequency (%)
                                  2
                                  1
                                  0 180                                                          0
                                  1
                                  2
                                  3
                                      210                                                   330
                                  4
                                  5
                                                  240                           300
                                  6
                                                                 270
                                            y'z' plane (green)      y'z' plane (sintered)
                        Figure 5. 32 pore orientation in the y’z‟ plane before and after sintering



5.7.2 Density gradient

Figure 5.33 shows the relative density in the thickness direction. The density is calculated as the solid
area fraction in the cross section plane. Two obvious findings are presented:

(1) In each single BT layer (D1, D2, and D3), the surface region (interface) is much denser than the
middle region. It has been observed experimentally by Guillon [73] and Bernard [121] and in discrete
simulations by Martin and Bordia [163] that in a sintered thin film on a rigid substrate, the density at
the interface is lower than the inner region of the film. These studies also show that pores near the
interface are elongated perpendicular to the thickness direction.




- 92 -
                                                                   Correlative studies using FIB-SEM nanotomography



                                                   D1                    D2                       D3




                                                                                                     1 µm

                                            100




                     relative density (%)
                                             95
                                             90 94.3%
                                             85                        91.4%
                                                                                              86.6%
                                             80
                                             75
                                             70
                                               0     100 200 300 400 500 600 700 800
                                                             distance (pixel)
 Figure 5. 33 Density profile in the thickness direction (from the surface to the bottom #1-s-ct). The density is
                                                   measured from the 2D slices along the thickness


The mechanism for the anisotropy development is depicted in Figure 5.34(a). Due to the restraining
effect of the substrate, tensile stresses develop in the thin film, especially near the interface. These
tensile stresses hinder the sintering of the film near the interface, thus resulting in a lower final density
close to the interface. In the meanwhile, due to the restraint of the substrate, grain grows preferentially
in the thickness direction, resulting in vertical oriented pores at the interface.
           L                                               L

      +         +                           Δz
                                                     +         +     densifying layer


      +                                              +
                                                                      nondensifying
                                                                       (substrate)

                                            (a)                                                        (b)
 Figure 5. 34 Anisotropy in thin film on substrate: (a) Bordia‟s model for the constrained sintering of thin film
                                            ([169]); (b) numerical simulations by Martin and Bordia [163]




                                                                                                              - 93 -
Correlative studies using FIB-SEM nanotomography

In the current study on the co-sintering of BT/Ni/BT multilayers, both Ni and BT layers densify but at
different densification rates as shown in Figure 5.35. At the early stage of the sintering of Ni/BT
multilayers (400-1050 oC), the BT layer is placed under compression, as the nickel sinters earlier and
faster than the BT layers. Thus, compressive stresses may facilitate particle rearrangement at the
interface. The interface regions sinter faster than the inner regions in the BT layers, resulting in a
higher density near the interface. Meanwhile, these compressive stresses facilitate the necks grow in
the load direction, that is, in parallel to the BT planes, resulting in horizontally elongated pores. Note
that when the temperature reaches 1050 oC, the stress state reverses in both layers. However, the
anisotropy that initially developed at the early stage (before the temperature reaches 1050 oC) plays a
decisive role in the entire sintering.
                                               L                             L


                                         +          +                 + L +
                 densifying layer 1      +          +                 +   +
                                         +                             +

                 densifying layer 2




                           Figure 5. 35 A model for the co-sintering of multilayers


(2) Average relative density in the BT layers decreases from the top layer (D1) to the bottom layer
(D3), as explained in Chapter 4; this is due to different constraint levels in different layers.

We are aware that the obtained density in dielectric layers (86-94%) is lower than that obtained in
commercial ones (almost fully densified). However, this does not alter the qualitative statements in
this work.


5.8 Microstructure evolution of the electrode

5.8.1 Discontinuity of electrode

Figure 5.36 shows the FIB reconstructed electrode of the sintered MLCC sample (#1-s-ct) that was
imaged by X-ray nCT (Chapter 4). In this discontinuous electrode, only the solid area can contribute
to the capacitance of MLCC. With FIB tomography (BSE), plenty of BT particles are observed in the
electrode.



- 94 -
                                              Correlative studies using FIB-SEM nanotomography




                          Figure 5. 36 An electrode (#2) from the sample #1-s-ct


A further EDX chemical analysis was carried out to confirm the phase of these entrapped particles.
Figure 5.37 shows the EDX mapping of the cross-section of sample #3. The darker spots, entrapped
particles (spots 1 and 2) are analyzed with EDX quantitative spot analyses.




              Figure 5. 37 EDX mapping of the cross-section of the sintered chips (sample #3)


From the EDX mapping, the darker particles are rich in Ba, Ti and O elements, the same as
compositions of BT. Qualitative EDX analysis (Table 5.4) indicates that these darker phases are
actually entrapped BT additives in the initial Ni matrix. Most of the BT additives are excluded by the
nickel matrix due to their incompatibility with Ni. These excluded BT particles sinter with adjacent
BT layers to form percolating bridges. The percolation of BT (bridges between electrode layers) can
improve the union of the neighboring dielectrics layers and the overall mechanical properties of the
chips. From the O map, oxygen elements could be found in the electrodes. It indicates that the nickel
particles absorbed the residual oxygen in the Ar+2%H2 mixture. In industry, (0.1-0.01%) H2-Ar-H2O

                                                                                                - 95 -
Correlative studies using FIB-SEM nanotomography

wet gas is utilized so that the content of the partial oxygen pressure is controlled within 10 -9-10-11 atm.
This residual oxygen modifies the sintering kinetics of the electrodes and dielectrics. That may also
explain why the dielectrics are not fully densified. This may alter the final dielectric properties, which
are, however, not considered in our study.
                                  Table 5.4 EDX spot analysis on sample #3
         Element                     spot 1                                     spot 2
                      Ba        Ti            O    Ni        Ba          Ti              O         Ni
         Atom%      31.12     33.6       36.28     0        38.09       36.93        24.98          0


Figure 5.38 shows the BT inclusion particle size change before and after sintering in the electrode #2
in sample (#1-2-ct). The PSD distribution usually shifts towards larger particle size due to grain
coarsening which consumes smaller particles. In our case, while a portion of coarsened particles have
been found, the portion of small particles increases and the average particle size does not change
significantly. This is because the nano BT additive inclusions are dispersed in the electrode. Isolated
single BT particles are not modified. Only aggregated BT particles sinter and form a single larger
particle finally.




  Figure 5. 38 The PSD evolutions of BT inclusion particles entrapped in the electrode (#2) in sample #1-s-ct



5.8.2 Correlation between discontinuity and capacitance

Figure 5.39 shows two neighboring electrodes, which comprises a unit capacitor. The capacitance of a
multilayer capacitor as given by Eq.(1.1) is directly proportional to the total effective electrode area.




- 96 -
                                                Correlative studies using FIB-SEM nanotomography




                        Figure 5. 39 Two reconstructed electrodes and a unit capacitor


The discontinuous areas (black areas) in the electrodes lead to a decrease in the effective overlapping
area, and thus in the capacitance. The effective overlapping area A (white area) in the Eq.(1.1) can be
calculated by a Boolean ORing operation of the areas of the two electrodes. The relative capacitance
C is

                                                C C0  A A0                                                (5.6)

Table 5.5 presents the areal (2D) discontinuities of the six electrodes and the relative capacitances of
the five unit capacitors in the FIB-SEM reconstructed representative volume extracted from the
sintered MLCC sample (#3).



                                             No.        discontinuity2D (%)        Relative capacitance (%)
                                              1                 16.3
                                              2                 22.3                         63.6
                                              3                 16.4                         66.3
                                              4                 12.3                         75.0
                                              5                  9.4                         79.8
                                              6                 10.9                         81.1
                                           average              16.3                         73.4

   Table 5.5 Discontinuity of electrodes (#1-6) measured in 2D and the relative capacitances of the five unit
                        capacitors, which are comprised of the neighboring electrodes


Average discontinuity is 16.3%. Notice that the average discontinuity for the electrodes that sintered
with a smaller cylindrical sample is 12.5%. This size and geometry effect on the final electrode
discontinuity is detailed in Chapter 4. The average relative capacitance is 26.6% compared to a
capacitor with continuous electrodes. That means that theoretically, by getting rid of these electrode

                                                                                                          - 97 -
Correlative studies using FIB-SEM nanotomography

discontinuities, the chips could be downsized by a quarter of their size and still have the same
capacitance.



5.9 Conclusion

High resolution FIB-nT has been utilized to characterize the green MLCC chips (#2-g) and sintered
MLCC samples. The analysis also included the sample imaged with X-ray nCT (#1-s-ct) and a
sintered MLCC with a real size (#3). It is concluded that:

(1) Qualitative and quantitative correlative studies on the microstructures of both the green and
sintered Ni-MLCC sample have proved that the X-ray nCT spatial resolution is sufficient for the
current work dealing with heterogeneity evolutions.

(2) FIB-nT enables 3D evaluation of the particulate characteristic including the particle and pore size
and their distribution. This provides accurate particulate parameters for the discrete element
simulations.

(3) Heterogeneities in the electrodes have been quantified. Because particles are not homogeneously
arranged, there are density variations through the electrode layers. In the high density regions, the
average particle coordination numbers are larger than in the low density regions.

(4) Anisotropy has been observed for both pore orientation and density in the BT layers. These
anisotropic effects are considered to be caused by the compressive stress that develops during the
heating stage when the Ni electrode sinters faster than the BT layers. The compressive stresses near
the interface facilitate the sintering of the BT particles, leading to a denser region at the interface than
in the inner regions. Under this in-plane compressive stresses, the BT particles grow preferentially in
the loading direction leading to pores that orient preferentially parallel to the layers.




- 98 -
                              Discrete element simulations of the sintering of electrode material


6. Discrete element simulations of the sintering of electrode material

This chapter presents a numerical approach to simulate the sintering of powders. The Discrete
Element Method (DEM) is used here specifically to simulate the sintering of a powder in the presence
of inclusions as this represents well the actual process in MLCCs where Ni powders are sintered with
BT particles. We take advantage of the fact that DEM simulations work explicitly at the particle
length scale, which continuum techniques such as Finite Element Method cannot. This allows the
retarding effect of inclusions to be taken into account, together with important effects such as
inclusion size and inclusion dispersion. We first review the modeling efforts concerning sintering with
rigid inclusions. Literature on DEM of sintering is reviewed. The general principles of DEM are then
briefly described. Finally, the modeling of the sintering of composite materials with dp3D code is
described.


6.1 Introduction

The discrete (or distinct) element method element method (DEM), was first proposed by Cundall and
Strack [170] in 1979 to study the micromechanics of geomaterials. The DEM simulates the behavior
of granular materials at the particle-length scale. Over the last decades, with advances in computing
power and numerical algorithms for nearest neighbor sorting, it has become possible to numerically
simulate hundreds of thousands of particles with a single processor. Today DEM is becoming widely
accepted as an effective method for addressing engineering problems in granular materials, especially
in granular flows [171-174], micromechanics [175-177], environmental sciences [178], rock
mechanics [179-181], pharmaceuticals [182, 183], and powder metallurgy [52, 163, 184-194].


6.1.1 DEM simulation of sintering

Jagota and Scherer [195, 196] were the first researchers to study sintering with DEM. Sintering of
mono-sized composites was modeled with DEM simulations by assuming that all contacts follow a
linear viscous law. Vergina [197] proposed a 3D DEM model that is based on two-particle
interactions. This model considered the grain-boundary and lattice diffusion. It predicted rationally
the structural reorganization effects which occur during the early stage of sintering of random and of
some crystalline-type packings in which various initial defects have been created. Parhami and Mc
Meeking [198] used a discrete element model to predict the densification of initial stage of sintering
through computer simulations, in which every particle center is represented by a node and every
contact between neighboring particles by a discrete element. The velocity of each node is related to
external and sintering forces governed by grain boundary and surface diffusion, derived from Bouvard




                                                                                                 - 99 -
Discrete element simulations of the sintering of electrode material

and Mc Meeking‟s work [199]. Then the motion of each discrete element was determined and was
assembled to present the behavior of a powder system with 266 particles.

The Parhami-McMeeking model has been taken and practiced by many authors [163, 189, 200, 201]
to consider macroscopic behavior and/or microstructural evolutions aided with computer power and
numerical schemes. Among these authors, Martin and his co-workers investigated the sintering
kinetics of metal powder [187], the effect of local heterogeneities arising from non-sintering
inclusions [52, 117], defects development in film/layers with complex geometry [163, 189].

Riedel and Kraft [202, 203] considered the pore evolution‟s influence on the sintering force. The
sintering force, taking into account the pores characteristics (i.e., coordination number, volume
fraction), enables prediction of the immediate and final stage of sintering. By incorporating Riedel
and Kraft model, DEM simulations have been implemented to study the rearrangement of particles
[188], anisotropy [204] during the sinter-forging by Wonisch et al. Wonisch et al.‟s DEM study
confirmed that intergranular pores are preferentially orientated along the compressive loading axis in
accordance with their experimental observations. Taps et al. predicted [205] distortion of film due to
constrained sintering by a rigid substrate using DEM simulations.


6.1.2 Principle of DEM

The general principle of DEM is based on the writing of the mechanical equilibrium of a set of
discrete objects that interact with each other through their contacts. A large majority of the
simulations based on DEM uses disc-shaped and spherical elements in 2D and 3D simulations,
respectively. This simplification allows including as few geometrical parameters as possible, i.e., only
the relative position of particle centers are tracked to determine particle contacts. The greatest
advantage of this assumption is computational simplicity. As a result, the computer storage and
processing time are significantly reduced and a large-scale simulation within a reasonable time
becomes possible. However, it should be noted that disks and spheres tend to roll or rotate easily,
which does not reflect the behavior of real materials in case of large shear processes. In the remaining,
we will only consider spherical particles. Also, we specialize the description of DEM by referring
essentially to the dp3D code, which has been developed at SIMaP, Universitéde Grenoble and which
be used to simulate sintering.


Particles are described by their number i (i = 1, N), their position Xi , velocity Vi , angular velocity ω i ,

radius R i , mass mi and moment of inertia Ii.




- 100 -
                                  Discrete element simulations of the sintering of electrode material

In each simulation time step Δt, first the neighbors of every particle are determined. This
neighborhood is defined by a previously specified interaction radius Rc. Then forces between
neighboring particles are calculated, depending on a given force law, as described later in Section 6.2.
The time evolution of the particle positions is governed by Newton‟s equations of motion:
                           d              d
                              Xi  Vi , mi Vi  Fitot   Fij  mi g                (6.1)
                           dt             dt            j i

                               d
                           I      ωi  M itot   M ij                             (6.2)
                               dt               j i


Here, Fij and M ij denote the inter-particle force and moment from the j-th particle on the i-th one (see
Fig. 6.1). The first term Fij includes the contributions of normal force N, tangential force T and
gravitational force mig. Fitot denotes the total force acting on the i-th particle and M itot the total torque
acting on the i-th particle, calculated from the particle-particle torques:
                                       1
                                Tij   ( Xi  X j )  Fij                      (6.3)
                                       2
                                            vi          hij
                          X1

                                             ωi
                                                        dij                   ωj
                                       oi                               oj
                                                   Xj                                       vi

                                Xi
                                                                   X3

                         O



                                                              X2
                                     Figure 6. 1 Two-particle contact model


The most widely used method for integrating the equations of motion is the algorithm initially
adopted by Verlet [206]. Swope et al. [207] proposed a Verlet-equivalent algorithm, which stores
positions, velocities and accelerations all at the same time t. This velocity- Verlet-algorithm uses a
group of equations:
                                                                    1
                           Xi (t  t )  Xi (t )  tVi (t )         (t ) 2 Fitot (6.4)
                                                                   2mi

                                                    1
                        Vi (t  t )  Vi (t )        t (Fitot (t )  Fitot (t  t )) (6.5)
                                                   2mi


                                                                                                      - 101 -
Discrete element simulations of the sintering of electrode material


                                                         1
                             ωi (t  t )  ωi (t )        t ( M itot (t )  M itot (t  t )) (6.6)
                                                        2Ii
This method, which is the standard integrating method in dp3D, has the advantages of numerical
stability, convenience and simplicity [208].

To obtain a proper integration of the particle movement, the time step must be chosen carefully. The
time step is determined using the method proposed by Cundall and Strack [170] as:

                                                         m0
                                          t  2 ft                              (6.7)
                                                         K0
In analogy with a contact with stiffness K0 and an oscillating mass m0. The safety factor ft is less than
unity to ensure stability of the calculation, m0 is the smallest particle mass and K0 is the maximum
contact stiffness, defined by contact equations. The simulation for quasi-static deformation can be
carried out either using a so-called non viscous damping method [170] or by scaling the density of the
particles by a factor of β with a typical value of β = 1012 [209].

         Boundary conditions

Three types of boundary conditions are typically available in DEM. Note that they can be mixed
together depending on the application.
     I.      Rigid Walls
Rigid walls can be constructed using objects such as planes, spheres, or cylinders. These objects have
an infinite mass, so their motion is not dictated by the second law of Newton (6.1) but only by the
imposed conditions set by the user. Walls may represent real process conditions such as a die wall in
uniaxial close-die compaction.
    II.       Free surface
Particles on surface of the sample only interact with other particles.
 III.        Periodic boundary
Periodic conditions are imposed by stating that when a particle protrudes outside the periodic cell
through a given face, a mirror particle is generated on the opposite face of the periodic cell. The
mirror particle interacts with other particles on that face (Fig. 6.2). Similarly, when the center of a
particle lies outside the periodic cell, the particle is translated to the opposite face of the cell by a
distance equal to the length between the two opposite faces. The relative density of the sample is
defined as the ratio between the particles volume and the volume of the cell. Periodic conditions are
well adapted for simulating a Representative Volume Element (RVE) far away from any rigid walls.
Typically, it may represent a volume of powder inside a matrix far from the perturbation of the rigid
die wall.




- 102 -
                                Discrete element simulations of the sintering of electrode material


                                                           periodic cell face




                                                      i                                   mirror particle

                                                                                    j




                        (a)                                           (b)
                     Figure 6. 2 Schematics of (a) wall conditions; (b) periodic conditions


In a typical DEM simulation, macroscopic strains are imposed. Depending on the boundary conditions
that have been chosen, strains are imposed by moving the objects or by moving the boundaries of the
periodic cell by the following equation:
                                  x j   ij xi t                     (6.8)

Where xi is the location of the object centroid or of the periodic cell, and  ij is the imposed strain rate.

The centers may also be moved according to the same equation (as if they are points in a continuum)
at the beginning of each time step. This, in general, facilitates the convergence toward force
equilibrium.

The imposed strains in the simulation result in contacting particles generating contact forces. These
contact forces produce stresses at the macroscopic scale. The macroscopic stress tensor  ij may be

computed from contact forces by considering a set of particles inside a volume V:
                                             1
                                     ij         (Ti  Ni )l j    (6.9)
                                             V contacts
Where lj is the branch vector between particles i and j centers.

In DEM of sintering, stress is imposed, instead of strain. This is done by calculating the strain rate of
the simulation box which needs to be imposed to minimize the error between the calculated stress and
the required stress. To simulate free sintering a zero (or very small compressive stress) should be
imposed.


6.2 Model description

In this section, we describe the contact forces, which model particle interactions in an electrode layer
(Ni and nano BT). In Chapter 3, experiments have shown that electrode powders containing both


                                                                                                            - 103 -
Discrete element simulations of the sintering of electrode material

nickel and nano BT particles sinter earlier (400-800 oC) than BT powders (950-1050 oC). Using X-ray
tomography, we have demonstrated that the discontinuities of electrode form at the early stage of
sintering while the BT has not started to sinter yet. To simulate the sintering process of Ni/BT
composite powders below 950°C, we make the following simplifying assumptions:
    -     All particles are spherical.
    -     Particles cannot rotate (we assume that sufficiently large contacts grow fast enough to
          counteract rotations).
    -     BT-BT contacts are elastic.
    -     Ni-Ni contacts are sintering contacts.
    -     Ni-BT contacts are viscous contacts.
    -     Coarsening is neglected.
    -     Sintering is isothermal.
    -     Gravitation is neglected.

To keep some generality to the model description, we define Ni as the matrix particle, and BT as the
inclusion. Spherical matrix and inclusions particles interact through specific contact laws. In such a
case, three types of contacts coexist: inclusion-inclusion (ii), matrix-matrix (mm), and inclusion-
matrix (im) contacts. We define an equivalent radius R*=R1R2/(R1+R2), for two particles of radius R1
and R2.

For (ii) contacts between particles with Young‟s modulus E and Poisson‟s ratio ν, the normal contact
force is elastic with an additional adhesive term given by the Derjaguin-Muller-Toporov model [210]:

                                                  8 E aii3
                                            Nii            2 wR*                             (6.10)
                                                  3 1  R
                                                        2


Where aii is the elastic contact radius and w is the work of adhesion (twice the surface energy). The
second term denotes the driving force for agglomeration between small particles. Frictional forces Tii
= µNii between inclusion particles are also included using Coulomb law (with a friction coefficient set
to µ = 0.1). For inclusions, we set E = 130 GPa, ν= 0.25 and w = 0.05 J m-2, typical values for BT
polycrystalline ceramics [211].

We use the model of Parhami and McMeeking for sintering (mm) contacts [198]. It assumes that grain
boundary and surface diffusion are the major mechanisms of mass transport [163, 187]. Particles
approach each other due to the flux of vacancies from the inner of the grain boundary to the triple
point (pore). The normal contact force is given by:

                                 amm
                                   4
                                      dh                                
                       N mm                  s 8R* 1  cos   amm sin                   (6.11)
                                8b      dt                   2          2



- 104 -
                               Discrete element simulations of the sintering of electrode material


Where amm (Fig. 6.3(a)) is the sintering contact radius, h the indentation,  the dihedral angle,  s the

surface energy and  b a diffusion parameter related to the grain boundary diffusion coefficient:

                                            
                                     b        b D0b exp(Qb / RT )                               (6.12)
                                            kT
with δb the grain boundary thickness, D0b a material constant, Qb the activation energy, Ω the atomic
volume, R the gas constant and T the temperature. The first term on the right-hand side of Eq (6.11)
may be considered as a normal viscosity, whereas the second term relates to surface tension effects.
The same viscosity term was used by Kraft et al. [202] in the normal force expression but their tensile
term was slightly different. The tangential force Tmm at a (mm) contact opposes the tangential
component of the relative velocity at the contact, du/dt, and is given by:

                                                 amm
                                                   2
                                                      R*2 du
                                     Tmm                                                         (6.13)
                                                  2 b     dt
where η is a dimensionless viscous parameter [212]. A value of η = 0.1 was used in this study. Note
that Eq. (6.13) also applies to (im) contacts. The contact radius amm which appears in Eq. (6.11) and
(6.13) is given by a generalization of Coble‟s law [213] for contacts between non-monomodal
particles, as proposed by Parhami and McMeeking [198] and confirmed numerically by Pan [214]:
                                             2
                                            amm  4R*h                                              (6.14)
For (im) contacts, we assume that a nearly flat surface, instead of a sintering neck, forms on the matrix
side at the (im) contact (Fig. 6.3(b)). In support of this assumption, clear interfaces between matrix
and inclusions are observed in some sintered polycrystalline ceramic or metal matrix composites [31,
215]. The normal force is given solely by the viscosity term of Eq. (6.11) and the contact radius aim is
derived by conservation of matter (the derivation is available in the supplementary material online):
                                              2
                                             aim  4Rm h                                            (6.15)
Where Rm is the radius of the matrix particles.



                                  matrix                           inclusion




                                 matrix                          matrix



                               (a)                                (b)



                                                                                                    - 105 -
Discrete element simulations of the sintering of electrode material

Figure 6. 3 Contact models: (a) matrix-matrix contact (matrix can be metal or ceramic); and (b) inclusion-matrix
                                                    contact


Note that the inclusion/matrix contact model we propose here is comparable to the case of particles
sintering on a rigid substrate. In accordance with Ref. [163], Eq.(6.15) is equivalent to Eq.(6.14) if the
inclusion particle is treated as a flat constraining substrate (when the radius of inclusion Ri = ∞). This
would indicate that Eq.(6.15) may also apply to polyhedron inclusions. Inclusion shape may affect the
sintering behavior of the composite, as shown by Sudre and Lange et al. [216] although Nakada et al.
[217] experimentally found that the shape of the inclusions had little effect on the macroscopic
densification behavior of ZnO matrix with 10 vol% of ZrO2 inclusions.


6.3 Simulation procedure

   Generation of packing

The preparation method consists of several steps:
    (1) Making of a gas of randomly distributed non-overlapping spheres in a periodic simulation box.
          Before a new particle is generated, a potential position will be checked. If this particle is not
          intersecting with any other existing particles, it is accepted, otherwise, a new attempt is
          performed. This routine is repeated until all particles are accommodated. This process takes
          tolerable time to result in a low packing fraction of approximately 0.32, with no contact
          between particles.

    (2) Jamming under isostatic equilibrium. In this stage, the loose gas is submitted to a slow stress-
          controlled hydrostatic densification to ensure force equilibration. During this preparation
          stage, friction is not introduced and only elastic contacts appear between particles [190]. This
          preparation stage is stopped when the relative density in the simulation box is equal to 0.55. A
          large external pressure can also be imposed to simulate close-die compaction and attain larger
          green density.

    (3) Sintering. In this stage, normal and tangential forces are activated depending on the contact
          (Eqs. (6.10) to (6.13)). Densification is stopped when the macroscopic density is 0.85 to
          ensure that interactions between neighboring contacts remain negligible.

   Generating of composites with inclusions

Generation of composites with inclusions can be realized in a similar way; however, matrix and
inclusion particles will be labeled as different materials. In presence of aggregated inclusions,
adhesion between inclusions is treated with specific bonding forces, thus ensuring the aggregate
survival during jamming (Fig. 6.4).

- 106 -
                                Discrete element simulations of the sintering of electrode material


                                                   jamming
                         gas of particles                         packing of particles




           (a)




          (b)




      Figure 6. 4 Generating of the numerical samples: (a) randomly dispersed; (b) aggregated inclusions

A series of composite samples consisting of 1000 spherical monosized matrix particles of 180 nm and
various volume fractions of inclusions (5%, 10%, 15% and 20%) were generated. For 20% volume
fraction, the inclusion size was varied (60, 100, 180 and 300 nm, see Fig. 6.5 (a, b and c)). Periodic
conditions are kept all along the sintering stage.




                                                                                                      - 107 -
Discrete element simulations of the sintering of electrode material

 Figure 6. 5 Numerical microstructure of composites with: 20% of randomly dispersed 300 nm (a), 100 nm (b),
    60 nm (c) inclusions;10% of randomly dispersed 60 nm inclusions (d); and 10% of agglomerated 60 nm
                         inclusions (agglomerate sizes are ~ 120 nm (e) and ~300 nm (f)).


In standard homogeneous samples (Fig. 6.5 (a, b, c and d)), inclusions are randomly dispersed in the
matrix. In contrast, two other types of samples, with 10% and 20% of 60 nm inclusions were also
generated to test the effect of an heterogeneous packing of inclusions. These samples are initially
made of matrix particles randomly mixed with inclusions that are clustered together as agglomerates
with average diameters of ~120 nm (Fig. 6.5(e)) and ~300 nm (Fig. 6.5(f)), respectively. All these
samples were sintered isothermally at 800 oC. The material parameters needed for the Nickel material
of the matrix are listed in Table 6.1. According to the work by Polotai et al [29], the diffusivity in Ni
is increased due to the formation of liquid Ni-Ba-Ti alloy. However, this influence on the grain
boundary diffusion coefficient is ignored in this work.
   Table 6.1 Material constants of Ni used in Eqs. (6.11), (6.12), and (6.13) [218]. Activation energy of Ni is
                                         regarded as a fitting parameter.

           b D0b (m3 s-1)              Qb (kJ mol-1)             Ω (m3)           s (J m-2)        (°)
            3.5×10-15                       232                 1.09×10-29           2.0             146



6.4 Result and Discussion

The most obvious effect of introducing inclusions into the matrix is to substitute (mm) contacts, which
are bound to sinter, by (im) contacts. This effect is stronger as the number of inclusions increases.
Also, since the inclusion number scales inversely with the cube of particle size, smaller inclusions will
lead to a larger number of substitutions between (mm) and (im) contacts. This effect is demonstrated
in Figure 6.6, which shows that starting from an average contact number between matrix particles Zmm
= 4.4, the green powder loses on average one to two (mm) contacts when the inclusion volume
fraction increases to 20%. The size effect is also clear: while the gain of (im) contacts is only
moderate for 180 nm inclusions, it is much larger for 60 nm inclusions. This is because smaller
inclusion particles are much more efficient in decorating the surface of large matrix particles.




- 108 -
                                    Discrete element simulations of the sintering of electrode material


                              4.5                                                 12

                                                                                  10
                              4.0
                                         60nm                                     8
                              3.5       100nm
                        Zmm             180nm                                     6    Zim

                              3.0                                                 4

                              2.5                                                 2

                                                                                  0
                              2.0 0          5         10         15        20
                                           inclusion volume fraction(%)

  Figure 6. 6 (mm) and (im) contact numbers in the green packing for various amounts and size of inclusions.


Although all packings exhibit a net gain in contacts due to densification and rearrangement, the initial
loss of (mm) contacts due to the presence of inclusions is not recovered during sintering. The (mm)
contact number depends almost linearly on the relative density, once the rearrangement stage is
completed (Fig. 6.7(a, b and c)). Figure 6.7(c) demonstrates that when inclusions are introduced as
larger agglomerates, their 8
                           effect on the decrease in (mm) contact number is less pronounced.
                                                          8
       8                    7
         60 nm inclusions                 20% inclusions              10% 60 nm inclusions
                               matrix                     7 matrix
       7                    6
                              5%                          6
       6                    5                               300nm
   Zmm 5
                           10%
                            4
                                                          5
                                                         180nm
                     15%                                                              300 nm agg.
       4                                           100nm4
                            3                                                         120 nm agg.
                20%                          60nm         3                               no agg.
       3                    2
                                    (a)                           (b)                           (c)
                                                          2
       2    0.6        0.7        0.8       0.6       0.7      0.8      0.6        0.7       0.8
                relative density                  relative density                    relative density
Figure 6. 7 Evolution of (mm) contacts upon densification: (a) effect of inclusion amount, (b) of inclusion size,
                  and (c) of the inclusions as agglomerates (agg.) or well dispersed (no agg.)


Figure 6.8 shows the typical evolutions of the relative indentation for the three types of contact in the
composite. In accordance with Eqs.(6.(10-15)), the (ii) elastic contact growth is negligible, while the
(mm) contacts grow faster than the (im) contacts due to the surface energy term (Eq. (6.11)) which
drives densification.




                                                                                                         - 109 -
Discrete element simulations of the sintering of electrode material


                                                                                         0.36




                                                        normalized indentation (h/2R*)
                                                                                         0.32            ii
                                                                                         0.28            im
                                                                                         0.24            mm
                                                                                         0.20
                                                                                         0.16
                                                                                         0.12
                                                                                         0.08
                                                                                         0.04
                                                                                         0.00
                                                                                                   0.6                 0.7             0.8
                                                                                                                relative density
                                                      Figure 6. 8 Contact indentation evolution of three types of contacts.


The reduction in (mm) contact number due to the substitution by (im) contacts results in a retardation
effect on the macroscopic shrinkage of the composites. This is demonstrated by Figure 6.9(a) which

shows the densification rate ( 1 dD ) against relative density for the various packings. As expected,
                                                                                            D dt
the sintering of the pure matrix is the fastest. The densification rate of composites is decreasing with
increasing amount of inclusions for a given size. We define the retarding factor as the ratio of the
matrix and composite densification rates for a given relative density D. This factor is approximately 7
at D = 0.70 when 20% of 60 nm inclusions are introduced. It also shows that a small amount (5%) of
(small) inclusions is sufficient to have a noticeable retarding effect. Figure 6.9(b) demonstrates that
densification rates decrease as inclusion size decreases for a given volume fraction. For instance,
when the particle size ratio of the inclusion to matrix decreases from 5/3 (Ri = 300 nm) to 1/3 (Ri = 60
nm), the retarding factor increases from 2 to 7 at D = 0.70.

                                                                 -2
                                       -2
                                                      10




  densification rate (dD/dt)/D (s )
        -1
                                      10    (b)
                                            (a)                                                     (b)                 10
                                                                                                                             -2
                                                                                                                                         (c)            10% 300nm agg.
                                                            matrix                                                      matrix                          10% 120nm agg.
                                                            5% 60nm                                                     20% 300 nm                      10% no agg.
                                                        -3
                                       -3
                                      10              10 10% 60nm                                                       20%
                                                                                                                        10
                                                                                                                           -3 180 nm
                                                                                                                                                        20% 300nm agg.
                                                           15% 60nm                                                     20% 100 nm                      20% 120nm agg.
                                                                                                                        20% 60 nm
                                                        -4 20% 60nm                                                                                     20% no agg.
                                       -4
                                      10              10                                                                10
                                                                                                                             -4
                                                                                                                                                               10%

                                                                 -5
                                       -5
                                      10              10                                                                10
                                                                                                                             -5
                                                                                                                                                                    20%
                                                                                                                                             60 nm inclusions

                                             0.6          0.7       0.8                                  0.6          0.7       0.8          0.6          0.7       0.8
                                                   relative density                                            relative density                    relative density
                        Figure 6. 9 Densification rate evolution with relative density: (a) effect of inclusion amount, (b) effect of
                                            inclusion size, and (c) of inclusions as agglomerates (agg.) or well dispersed (no agg.).


- 110 -
                               Discrete element simulations of the sintering of electrode material

Figure 6.9(c) shows that, for a given volume amount and size of inclusions, the spatial distribution
homogeneity of the inclusions can also influence the magnitude of the retardation. It indicates that the
more the inclusions agglomerate, the weaker the retarding effect. This may be understood by
considering these agglomerates of fine inclusions as larger (and more deformable) particles of
equivalent size (the same reasoning applies for Fig. 6.9(c)). Note that the effect of agglomerates is
only discernible when the volume fraction is large (20%). Still, the effect of homogeneity is of second
order as compared to the effect of volume fraction and size in our simulations for which aggregates
are very large.

Experimental data on the retarding effect of inclusions deals essentially with large inclusions [50, 215,
217, 219]. For example, Weiser et al. [50] studied the sintering of ZnO/SiC composites containing 0-
20% inclusions with size ratio (inclusion to matrix) value of 1-150 and found a retarding factor of
~2.5 for 20% inclusions. This number compares satisfactorily with our simulations, which predict a
factor of 2 for 20% of 300 nm inclusions. Still, one should be careful when comparing these
experimental data for which the inclusion to matrix size ratio is much larger than in our simulations.
For composites with small inclusions, there is a lack of experimental data to quantitatively compare
with our simulations. However, literature on Ni/BT composites indicates some interesting general
trends. Ueyama et al. [220] found possible to suppress sintering of the Ni electrode paste film by
adding 10 mass % of BT particles of 30 nm size while 50 nm particles had a less retarding effect. This
result was obtained only when the 30 nm particles were well dispersed. On the opposite, Sugimara et
al.[31], while demonstrating the retarding effect of BT (30-100 nm) on the sintering of Ni powder
(200 nm), found that agglomerated 30 nm inclusions had a smaller retarding effect than well dispersed
larger inclusions. These results are in broad agreement with our simulations which point to the
following general rule: smaller inclusions have a greater retarding effect if they are well dispersed.



6.5 Conclusions

    (1) A matrix/rigid inclusion contact model has been proposed which take size effect into account
                                                                                                         .

    (2) The effects of volume fraction, size and homogeneity of rigid non-sintering inclusions on the
        densification behavior of the matrix have been investigated using discrete element simulations
        at the particle length scale. It is found that the densification rate of the matrix decreases with
        increasing amount of inclusions and with decreasing size of inclusions. For a given amount
        and size of inclusions, a better dispersion of the inclusions results in a stronger retardation of
        densification.




                                                                                                  - 111 -
Discrete element simulations of the sintering of electrode material

   (3) By controlling the size, volume fraction and dispersion degree of the BT additives in the
          nickel paste, the sintering kinetics can be tailored to reduce the sintering mismatch between
          nickel and BT




- 112 -
                                                            DEM simulation of Ni/BaTiO3 multilayers


7. DEM simulation of Ni/BaTiO3 multilayers

The previous chapter dealt with the simulation, using the DEM codes dp3D, of the sintering of a
composite electrode material. The sintering of the representative volume element of the mixture was
conducted under idealistic boundary conditions (periodic conditions), which do not reflect the firing
conditions of a real MLCC. In this chapter, we seek to implement conditions that take into account
more realistically the geometry of an MLCC, the constraining conditions that characterize MLCC
sintering, and the particle size distribution obtained from experimental observations. The aim of these
simulations is to provide information on the evolution of the microstructure in the electrode. In
particular, we study the initiation and the evolution of discontinuities at the length scale of particles.


7.1 Model description

As detailed in Chapter 3, significant discontinuities of electrode (Ni or Pd) have formed already at the
early stage of co-sintering, before the onset of densification of the dielectric layers. When the
dielectric material starts to sinter, the electrode layers are almost dense (Fig. 3.7(f)). At this final stage,
it is not possible anymore to consider the Ni (or Pd) layer as a collection of individual particles with
the characteristics of a particulate system. The DEM model is inappropriate to simulate the final stage
of electrode sintering. Thus, this chapter mainly focuses on the early stage of the co-sintering of
Ni/BT multilayers (i.e. temperature range of 700-1050 oC). We note that only a small amount (~3%)
of shrinkage is observed in the BT material at this stage. The BT-BT contacts in the dielectric layers
are modeled as sintering contacts. That is to say, like Ni-Ni contacts, BT particles also sinter but at a
negligible rate. This allows to model two different materials which co-sinter at significantly different
rates. To implement these simulations for Ni-Ni and Ni-BT contacts, the normal forces and tangential
forces are calculated using the same contact models as in Chapter 6.2. For both Ni-Ni contacts and the
BT-BT contacts, Eq.(6.11) is used to calculate the normal force and Eq.(6.13) for the tangential force.
In the presence of nano-sized BT inclusions in the electrodes, BT-BT contacts between these nano BT
particles are modeled as elastic.

7.2 Simulation procedures

7.2.1 Sample preparation

   Particle size distributions (PSDs)

As in the preceding chapter, BT and Ni particles are ideally treated as spheres. The PSDs of the BT
particles in the dielectric layers and of the Ni particles in the electrode layers are fitted as log-normal
functions directly from the FIB nano-tomography data (see Chapter 5.3.2). The log-normalized
particle size lnd is distributed according to a log-normal function:

                                                                                                      - 113 -
DEM simulation of Ni/BaTiO3 multilayers

                                                                     2
                                                           d
                                                         ln 
                                                     exp 
                                                A             dc 
                            f (d )  f 0                                  (7.1)
                                            ln 2 d       2 ln 2

Where f 0 is the offset, A is the area, ln and  2 ln are the expected (or mean) value and variance for
the log-normal distribution, respectively. The real mean value of particles  can be calculated as
  exp(ln   ln 2 / 2) and the variance is calculated as  2  (exp(ln )2  1)  exp(2ln  ( ln )2 )
[221].

Representing all particle sizes given by Eq.(7.1) would result in a very large number of particles. This
would be CPU prohibitive. Instead, we cut off the PSD for small particles by simulating only particles
larger than dmin.

For the Ni powder in the electrode and BT powder in the dielectrics, the parameters for the fitted PSD
functions are listed in Table 7.1.
                              Table 7.1 Fitted parameters of the PSD functions

          Powder             f0              A               ln          d c (nm)     d min (nm)
            Ni             0.276        2836.645           0.473          182.96          27
            BT            -0.074         3086.47           0.325          274.38          60


For the nano scale BT additives, the exact PSD is not known but the mean additive particle size is 50
nm. This value is used in the simulations.

   Cylindrical samples

To reduce the CPU simulation time to a tolerable duration, a representative BT/Ni/BT sandwich
multilayered cylinder with a diameter of Ø = 10 µm was created (Fig.7.1). This geometry is close to
that of the sample used for the synchrotron nanotomography. BT and Ni particles with lognormal
distribution (Eq.(7.2) and Eq.(7.3) respectively) were randomly generated using Box-Muller
transform [222] and using the parameter given in Table 7.1. Green packings with density range of 0.3-
0.5 (depending on the green density to be achieved) were first generated (see Chapter 6.3 for the
routine description). In that initial packing stage, interactions between particles are solely elastic.
Figure 7.1(a) shows a BT layer. Figure 7.1(b) shows a nickel electrode without any BT inclusions.
Figure 7.1(c) shows a Ni electrode with 10 vol. % mono-sized BT inclusions (d = 50 nm) which are
homogeneously dispersed (no agglomeration). The cylindrical BT and Ni discs were aligned and
stacked (Fig. 7.1(d)). These stacked multilayers were then hydrostatically jammed together to achieve
a green density equal to that observed in real MLCC samples.




- 114 -
                                                             DEM simulation of Ni/BaTiO3 multilayers




    Figure 7. 1 Numerical samples: (a) BT dielectric layer (b) Ni electrode layer without BT additives (c)Ni
                         electrode with 10 vol.% BT additives (d) BT/Ni/BT multilayers


Table 7.2 lists the initial conditions of the BT dielectric layers and electrode layers including the pure
Ni electrode and the Ni/BT composite electrode. Except mentioned otherwise, these are the standard
parameters used in the simulations.
                         Table 7.2 Standard sample properties for the numerical samples
                 Layer          Thickness (µm)          Particle number           Green density
                  BT                 2.4                      9375                    0.61
                  Ni                 1.0                      6500                    0.50
                 Ni/BT               1.0              6500 (Ni):1300(BT)              0.55


7.2.2 Sintering conditions

All surfaces (top, bottom and lateral) of the cylindrical sample are considered as free surfaces. The
physical properties of Ni are detailed in Chapter 6.2. In the absence of diffusion data specific to
Barium Titanate (BT), the sintering properties in the dielectric layer were assumed to be the same as
those of Alumina (Al2O3) except for the sintering activation energy Qb. Specific surface energy  s is

known to vary moderately from one oxide to the other, and remains close to 1.0 J/m 2. The volume of
the diffusing particles is 8.47 × 10-30. The properties used are listed in Table 7.2. Note that, for a given
microstructure, it can be shown that time in dp3D may be advantageously normalized to
  kBTR4 /  s  Db [187]. Thus, sintering kinetics obtained from one DEM simulation for a given

                                                                                                        - 115 -
DEM simulation of Ni/BaTiO3 multilayers

set of material (δbD0b, Qb, γs, Ω, R) and process (T) parameters can be used to retrieve the sintering
kinetics of another set. By correlating sintering kinetics of a BT disc sample (Chapter 3) with DEM
simulations of the sintering of BT under the same conditions (i.e., PSD, green density and heating
ramp and temperature), we may fit a suitable activation energy (Qb = 480 KJ/mol). By using the
material properties of α-Al2O3 in Table 7.2 for all material parameters except the activation energy, no
physical meaning can be ascribed to the activation energy. It only represents a practical manner to
model the slow BT sintering kinetics at low temperature.
                     Table 7.2 Material properties of BT (adopted from α-Al2O3 [204])
    δbD0b (m /s)
             3
                              γs (J/m2)                Ω(m3)                 ηNi-BT       ηBT-BT
             -8                                                 -30
      1.3 × 10                  1.1                 8.47 × 10                 0.1            1



Table 7.3 lists the values of the viscous parameter used in the simulations. Except mentioned
otherwise (see Chapter 7.6 on the effect of ), these are the values used in all simulations. A BT-BT
contact viscosity value of ηBT-BT = 1 is believed acceptable, since the irregular shape of BT particles
resist significantly the rotations and slides of the BT particles, hence the rearrangement of the BT
particles can be neglected.

7.2.3 Post processing

   Voxelisation

The output of a dp3D simulation is a set of spheres defined simply by their coordinates and radii.
These spheres are truncated due to the densification process which has taken place during sintering
(Fig. 7.2(a)). To visualize in a more realistic manner the simulated microstructures of the sintered
samples, necks and grain boundaries need to be taken into account. In accordance with Eq. (6.14), the
neck size is estimated using Coble‟s law as Figure 7.2(b) shows.
                                           ac 2  4R* (h1  h2 ) (7.2)

Where ac is the contact radius, R* is the reduced radius, defined as R* =R1R2/(R1+R2), h ( = h1+h2 ) is

the indentation. The volume redistributed in the triangular torus is equal to the overlapped volume.
The out surface of the neck is tangential to the two particles with curvatures of ρ1 and ρ2. The
geometry lengths are given by Eqs. (7.(3-6)). The derivation of these values is detailed in Appendix B.

                                               a 2  2 R1h2  h22
                                          1                     (7.3)
                                                   2 R1  2a

                                                 a 2  2 R2 h1  h12
                                          2                        (7.4)
                                                     2 R2  2a




- 116 -
                                                                    DEM simulation of Ni/BaTiO3 multilayers


                                                   ( R1  h2 ) 1
                                            y1                       (7.5)
                                                      R1  1
                                                   ( R2  h1 ) 2
                                           y2                        (7.6)
                                                      R2  2
To voxelise the sample, the entire sample including the solid volume and porous volume was
subdivided in voxels with values 1 (solid) and 0 (porosity). The routine is detailed in Ref. [193]. This
routine assumes that contacts do not interfere with their neighbors. Hence, when the sample reaches a
high density (>0.85-0.90), many triple contacts (or higher coordination contacts) exist and the validity
of this post-processing process is not any more ensured.

   Visualization

The voxelised microstructures can be resliced and visualised using ImageJ or Avizo software
packages as shown in Figure 7.2(b). Quantification of the real microstructures can be made from the
3D microstructures. In this study, we focus on the discontinuity of the electrode, defined as the
percentage of uncovered area over the enveloping area.




    Figure 7. 2 (a) Definition of Coble Contact radius ac; (b) visualization of two sintered particles after the
                                             voxelisation procedures


7.3 Free sintering and constrained sintering

The simulation results of the sintering of a single Ni layer were compared with those of BT/Ni/BT
layers under the same conditions to understand the main consequences of constrained sintering. The
DEM simulations started at an initial temperature of 700 oC with a heating rate of 1 oC/min. The Ni
layer has a 0.50 green density. The sintering was terminated at 1050 oC (total time = 21 000 s,
approximately 6 hrs). The viscous parameterNi-Ni was set to 0.1.

                                                                                                            - 117 -
DEM simulation of Ni/BaTiO3 multilayers

Figure 7.3 shows the microstructure (Fig. 7.3(a)) of the green electrode together with the
microstructures of the electrodes that have been freely sintered (Fig. 7.3(c)) and constrained sintered
(Fig. 7.3(d)) in the presence of BT layers. For clarity, in that last case the BT layers are not shown.
Close inspection of Figure 7.3(a) indicates that there are numerous heterogeneous zones which exhibit
rather large pores. These zones, previously mentioned as inter-agglomerate pores (Chapter 3.3), are
shown in circled areas in Figure 7.3(a). These porous zones are typically larger than the average size
of the particles. The packing can be subdivided into well packed agglomerates separated by these
extrinsic pores. The particles in these well packed agglomerates have higher coordination numbers
than the average value. Pores between particles within these agglomerates are defined as intra-
agglomerate pores.

After sintering, the Ni electrode sintered freely has densified homogeneously with nearly no
discernable discontinuity. Conversely, the Ni electrode which has been sintered under constraints
imposed by the BT layers clearly breaks into discontinuous areas (discontinuity content is about
14.5%). Constraints play an important role in the formation of discontinuous electrode, and we shall
examine in more details in the following sections the mechanisms that lead to these discontinuities.




  Figure 7. 3 Microstructure evolution of electrode: (a) green microstructure; (b) definition of the inter/intra-
            agglomerate pores; (c) freely sintered electrode; and (d) constrained sintered electrode



- 118 -
                                                                DEM simulation of Ni/BaTiO3 multilayers

      Defect evolution mechanisms

To understand how these defects initiate and evolve, a representative area was selected and followed
in detail. Particles in the final continuous area were colored differently to easily trace them at different
phases of the sintering. As Figure 7.4 demonstrates, particles that pertain to these continuous areas
were initially closely packed (see the agglomerates in Figure 7.4(a)). The pores that bound these
agglomerates are mostly inter-agglomerate pores and may be considered as initial heterogeneities, as
shown in the circled areas. In the close packed agglomerates (colored areas) which are mainly formed
of intra-agglomerate pores, particles sinter faster while the initial inter-agglomerate pores enlarge due
to the shrinkage of agglomerates.

As sintering proceeds, the contacting particles at the boundaries are detached due to local sintering
shrinkage mismatch. This contact loss is referred to as de-sintering. The de-sintering indicated by the
arrows in the Figure 7.4(c) results in the growth of pores (discontinuities). On the other hand, intra-
agglomerate pores shrink and gradually pinch off and finally disappear as shown in the Figure 7.4(d-f).




    Figure 7. 4 The microstructure evolution in the magnified area as function of sintering time during the heating
                                                        ramp


7.4 Effect of heating ramp

A standard sample (BT layer and Ni layer see Table 7.2) was sintered at different heating rates: 1, 5,
10, 15, 30 and 50 oC/min, starting from 700 oC until 1050 oC.

                                                                                                            - 119 -
DEM simulation of Ni/BaTiO3 multilayers

Figure 7.5 plots the electrode discontinuity as a function of temperature with different heating rates.
As sintering proceeds during the heating ramp, the discontinuity increases as sintering temperature
increases. It is concluded that a fast heating rate results in lower discontinuity. For instance, with
heating rate increasing from 1 oC/min to 50 oC/min the discontinuity decreases from 15.44% to 1.73%.
However, it should be clear that according to the simulation, the density reached at a given
temperature is also lower for a faster heating ramp. This is because the value of the heating rate
impacts the duration of the ramp during which the Ni layer may be considered to sinter under
constraint.

                                  16            o
                                            50 C/min
                                              o
                                  14        30 C/min
                                              o
                                  12        15 C/min




              discontinuity (%)
                                              o
                                            10 C/min
                                  10          o
                                             5 C/min
                                              o
                                   8         1 C/min
                                   6
                                   4
                                   2
                                   0
                                   700    750        800        850       900        950       1000    1050
                                                                             o
                                                          temperature ( C)
                                         Figure 7. 5 Electrode discontinuity against the temperature


As Figure 3.5 shows, the Ni electrode (with 10 vol. % BT inclusions) sinters sooner and faster than
the BT dielectric layer during the heating stage. The sintering shrinkage mismatch between electrode
and dielectrics, which is built up in this stage, directly contributes to the electrode discontinuity.
Experimental observations indicate that below the critical temperature (1050 oC, at 15 oC/min), the
electrode is always under tensile stresses. Above this critical temperature, BT layers sinter faster than
electrode layers and compressive stresses are generated. Using fast heating rate allows the Ni to be
only slightly sintered when reaching the high temperature domain (above the critical temperature and
the dwelling temperature 1150 oC). In that case, the compressive stresses experienced at higher
temperature should facilitate the final densification of Ni, resulting in slower growth of discontinuities,
or even some recovery of the discontinuities. When the Ni approaches completion of sintering, it is
still viscous and highly deformable. In this stage, compressive stresses will cause lateral contraction
and a further increase in the discontinuity through a swelling mechanism already discussed in Chapter
5. It is not possible to simulate with DEM this last stage. This is because DEM operates with
interacting particles, which are not suited to simulate a continuum. In any case, the discontinuity

- 120 -
                                                              DEM simulation of Ni/BaTiO3 multilayers

initiation and development, which is well predicted by DEM during the heating stage, will contribute
to the final discontinuity.

Figure 7.6 shows the microstructures (z- axis view.) at the end of the different heating ramps running
from 700 to 1050 oC.

                          Discon=14.6%                      Discon=6.4%                      Discon=4.3%




             1 oC/min                         5 oC/min                         10 oC/min

                         Discon=2.3%                        Discon=1.7%                      Discon=1.1%




            15 oC/min                         30 oC/min                        50 oC/min

     Figure 7.6 Microstructure and the discontinuity of the electrode sintered at different heating rates. The
discontinuities of the electrode are 14.55% (at 1 oC/min), 6.44% (at 5 oC/min), 4.33% (at 10 oC/min), 2.27% (at
                           15 oC/min), 1.7% (30 oC/min), and 1.13 %( at 50 oC/min).


The results of these simulations indicate that the shorter the sample is exposed to sintering during the
heating stage, the less discontinuity is built up. In the industrial firing process, there is a second binder
bake-out (BBO) step. For example, the Ni-MLCC chips are held at 800 oC for 1 hr to remove the
organic completely. During this BBO process, the electrode has already sintered to some extent (Fig.
3.7). This seems to be detrimental according to the simulations. To solve this problem, one possibility
would be to apply a fast heating schedule. An alternative solution is to adapt the organic system such
that it can be burnt out at a lower temperature (< 400 oC for example) before nickel starts to sinter.

7.5 Effect of green density

DEM simulations allow particulate microstructures to be generated at various green densities. We
take advantage of this feature to study the effect of green density on the evolution of discontinuity.
The sintering of BT/Ni/BT multilayers consisting of the same two BT layers (D = 0.60) and constant

                                                                                                           - 121 -
DEM simulation of Ni/BaTiO3 multilayers

thickness electrode with different packing density (D = 0.40, 0.45, 0.50, 0.55, and 0.60, pure nickel)
was simulated at a heating rate of 15 oC/min from 700 to 1050 oC.

Figure 7.7 plots the electrode discontinuity as a function of heating time for samples with different
green densities.

                               7

                               6




           discontinuity (%)
                               5                    D=0.40              D=0.45
                               4                    D=0.50              D=0.55
                                                    D=0.60
                               3

                               2

                               1

                               0
                                   0        300           600     900       1200                 1500       1800
                                                           heating time (s)
                                       Figure 7.7 Discontinuity of electrode as functions of heating time


Owing to our definition of discontinuity (see Eq.(4.4)), it is found that the initial discontinuity is
related to the initial green density. Lower green density results in more initial pores or heterogeneities.
For all green densities, the effect of constrained sintering is to increase discontinuity.

Figure 7.8 shows the sintered microstructure of these samples after the heating ramp. It is found that
within the range of D = 0.40-0.55, the lower the green density, the higher the final discontinuity. This
is supportive of our early argument: the final discontinuity of electrode originates from initial
heterogeneity (pores).




- 122 -
                                                               DEM simulation of Ni/BaTiO3 multilayers


                             Discon=7.0%                    Discon=3.5%                      Discon=3.4%




                 D = 0.40                        D = 0.45                        D = 0.50

                                Discon=2.3%                                                   Discon=3.1%




                  D = 0.55                                                       D = 0.60
                 Figure 7. 8 Microstructure of electrode with different green density (at 15 oC/min)


We also note that when the green density of the Ni layer is large (D0 = 0.60), the discontinuity growth
rate is somewhat larger than that of more porous green layers although they have fewer initial pores
(heterogeneities). This is because a denser green body sinters faster, owing to the larger number of
contacts between particles that increase the total driving force for sintering. For the same given
heating time, the faster the sintering, the larger the shrinkage mismatch, thus leading to a larger
discontinuity.


7.6 Effect of contact viscosity

We have seen that the BT layer constrains the sintering of the Ni layer. It is thus important to
understand the consequence of the interactions at the interfaces between Ni and BT particles. The
tangential force partly dictates the amplitude of particle rearrangement at the interface between Ni and
BT. However, we shall see that particle rearrangement in the Ni layers is also critical. The following
simulations attempt to decouple the effect of rearrangements by varying the values of ηNi-Ni and ηNi-BT
that dictate the amplitude of viscous tangential forces at the contact in Eq. (6.13). The exact value of
is very difficult to ascertain. Parhami and McMeeking [198] and Henrich et al. [188] using the same
tangential law, used 0.003 and 0.3 values, respectively. In any case, the value ofshould be less than
unity. The rationale for this is that the normal viscosity term in Eq. (6.11) should be of the same order




                                                                                                       - 123 -
DEM simulation of Ni/BaTiO3 multilayers

or larger than the tangential viscosity term (Eq. (6.13) when the normal and tangential relative
velocities are of the same order.

In order to mimic the behavior of the real irregular shaped BT particles, a large viscosity coefficient
ηBT-BT = 1 is used in all simulations [163]. For Ni-Ni and Ni-BT contacts, extreme values (0 and 1) are
used to decouple clearly the effect. A 0.01 value has also been tested for ηNi-Ni to approach more
realistic values given in the literature [198].
           Table 7.3 Contact viscosity between Ni-Ni, Ni-BT, and BT-BT contacts (dimensionless)

                                                ηNi-Ni           ηNi-BT        ηBT-BT
                                                  0                0             1
                                                  1                0             1
                                                  1                1             1
                                                0.01               1             1
                                                  0                1             1


Figure 7.9 plots electrode discontinuity evolution against the sintering time during the heating ramps
for multilayers with various material viscosities. Both the viscosity between Ni-Ni and that between
Ni-BT (interface) influence the electrode discontinuity. For a given Ni-BT viscosity value (ηNi-BT = 1),
the larger the Ni-Ni viscosity, the larger the electrode discontinuity. It is because the viscosity
between sintering particles plays an important role in the rearrangement of the sintering particles.
When particle rearrangement is limited, it is not possible for particles to compensate for the BT layer
constraint, leading to local tensile stresses. Thus, at the location of a local heterogeneity, contacts are
broken and the heterogeneity is able to grow.


                                4.0
                                3.5             
                                                
                                3.0
                                                



            discontinuity (%)
                                2.5
                                                
                                2.0             
                                1.5
                                1.0
                                0.5
                                0.0
                                      0   200     400     600      800    1000 1200 1400 1600 1800
                                                                    time(s)
Figure 7. 9 Discontinuity of electrode as functions of heating time for different values of the viscous parameter.



- 124 -
                                                             DEM simulation of Ni/BaTiO3 multilayers

More generally, viscosity hinders the rearrangement of sintering particles, while the rearrangement of
particles has been proved in experiments by Kieback et al. [223] and DEM simulations [188, 189] to
be able to facilitate the homogeneous sintering of powder. Additionally, the viscosity between Ni and
BT hinders the interface rearrangement, such that a relative rigid interface is maintained during
sintering, thus allowing the in-built stresses near the interface to be transmitted. This is in accordance
with previous DEM simulations on the development of cracks in constrained sintering systems [189].

The variation of ηNi-BT does not seem to have as much impact on discontinuity as the variation of ηNi-Ni.
This is not intuitive since section 7.3, which compared free sintering and constrained sintering
conditions, demonstrated the importance of the existence of the Ni-BT interface. In fact, the
interaction that affects mostly the rearrangement of Ni particles at the Ni-BT interface is the normal
contact force (Eq.(6.11)) that exists between Ni and BT particles. Since the interface is not smooth
(BT particles are spherical), any tangential or normal motion of Ni particles result in a counteracting
viscous force opposite to dh/dt.


From Figure 7.10 showing the microstructures at the end of the heating stage, it is observed that on
top of the difference in discontinuity in percentage, the pores form at different locations in the
electrode. This difference is due to the rearrangement of the particles.

                                         Discon.= 0.8%                           Discon.= 1.9%




                   ηNi-Ni=0 ηNi-BT=1                      ηNi-Ni=0.01 ηNi-BT=1

                                         Discon.=4.0%                             Discon.= 3.0%




                    ηNi-Ni=1 ηNi-BT=1                      ηNi-Ni=1 ηNi-BT=0

               Figure 7. 10 Microstructure of electrode with different viscosities (at 15 oC/min)




                                                                                                    - 125 -
DEM simulation of Ni/BaTiO3 multilayers

It has been observed that rearrangement of particles should accelerate the sintering kinetics [188].
Thus, the shrinkage mismatch between the electrode and dielectrics should increase and a larger
discontinuity of electrode could be expected. However, in these simulations, we observed the reverse.
This is because a constraint is a more crucial requirement for the formation of discontinuities and easy
rearrangement of the particles at the interface lowers the constraint at the interface.

7.7 Effect of electrode thickness

The electrode thickness is an important functional parameter. It has decreased over the years in the
MLCC industry. Here we investigate its effect on the sintering process. To investigate the effect of the
electrode thickness on the electrode discontinuity, BT/Ni/BT multilayers with electrode having
different average thickness were sintered at 15 oC/min from 700 to 1050 oC. The samples are shown in
Figure 7.11. The BT layers have a constant thickness (2.4 µm) while the thickness of electrode varies:
H = 0.2 µm, 0.4 µm, 0.6 µm, 1.0 µm. These serial thicknesses correspond to on average 1, 2, 3 and 5
layers of particles packed in the electrode layer.




Figure 7. 11 Green microstructures of different samples with (a) 0.2 µm (b) 0.4 µm (c) 0.6 µm (d) 0.8 µm thick
                                           electrode (pure nickel)


Figure 7.12 shows the effect of the initial thickness of the electrode on its final discontinuity after
sintering. It is observed that the thinner the electrode thickness, the larger the electrode discontinuity.
However, the layer thickness has mostly an effect on the initial heterogeneity value. For example,
when the electrode consists of a monolayer of particles (H = 0.2 µm), a large initial discontinuity
content (22.8%) is calculated.




- 126 -
                                                                     DEM simulation of Ni/BaTiO3 multilayers


                               25


                               20             H=0.2 m (1d)
                                              H=0.4 m (2d)




           discontinuity (%)
                                              H=0.6 m (3d)
                               15             H=1.0 m (5d)

                               10


                               5


                               0
                                    0   200   400     600     800    1000 1200 1400      1600 1800
                                                            heating time (s)
       Figure 7. 12 Electrode discontinuity as functions of heating time for various electrode thickness


Figure 7.13 shows the sintered microstructures at the end of the heating ramps. As sintering proceeds,
the discontinuity content only increases slightly. It is found that the continuous areas are formed by
the bonding and sintering of several particles (Fig. 7.13(a)). They do not connect with the neighboring
continuous areas. In a thin electrode, almost each single particle is constrained by the top and bottom
layers simultaneously. Hence, the rearrangement of particles is almost impossible.


                                                     Discon.=24.3%                  Discon.= 8.0%




                                        H = 0.2 µm                     H = 0.4 µm

                                                     Discon.= 4.6%                  Discon.= 2.3%




                                        H = 0.6 µm                     H = 1.0 µm

          Figure 7. 13 Microstructure of electrode with different electrode thickness (at 15 oC/min)

                                                                                                           - 127 -
DEM simulation of Ni/BaTiO3 multilayers

It is concluded that by increasing the electrode thickness the connectivity of the electrode can be
enhanced. However, increase in electrode thickness leads to an increase in the overall size of the
MLCC chips and consumption of electrode materials. This is clearly not an option that the MLCC
industry can adopt. Still, the electrode thickness should be carefully designed to obtain acceptable
level of electrode discontinuities.

7.8 Retarding effect of the inclusions

To investigate the effect of the inclusions on the electrode discontinuity, sintering of the multilayers
with pure Ni electrode and Ni/BT composite electrode were compared. Figure 7.14(b) shows the
composite electrode (D = 0.55) containing 10 vol. % 50 nm mono sized BT inclusions. Figure 7.3(a)
shows the pure electrode obtained by taking out the BT inclusions (D = 0.50). Thus, the two
electrodes have the same packing of Ni particles. The sintering was conducted from 700 to 1050 oC at
a heating rate of 15 oC/min.




Figure 7. 14 Green microstructures of pure Ni electrode (a) and Ni/BT composite electrode with 10 vol. % of 50
                                            nm BT inclusions (b)


Figure 7.15 compares microstructures of electrodes after 10 000 s of isothermal sintering at 1150 oC.
Figure 7.15(a) shows the microstructures of the sintered pure Ni electrode with 4.37% of discontinuity.
Figure 7.15(b) shows the microstructures of the composite electrode with a discontinuity of 2.75%.
Note that the BT inclusions in composite electrode are not represented as part of the electrode,
because the inclusions are equivalent to the discontinuities which cannot accommodate charges when
a MLCC is operating.




- 128 -
                                                                              DEM simulation of Ni/BaTiO3 multilayers


                                                     Discon.=4.4%                                     Discon.= 2.8%




                                      (a)                                                (b)

Figure 7. 15 Microstructures of the sintered pure Ni electrode (a) and the composite electrode excluding the BT
                                                                 inclusions


Figure 7.16 plots the discontinuities in the pure Ni and composite electrodes increasing as sintering
proceeds. The two electrodes start from the same initial discontinuity percentage but then the
discontinuity growth in the composite electrode is slower than that in the pure nickel electrode. The
discontinuity is attributed to the shrinkage mismatch. The presence of inclusions leads to a decrease of
the sintering mismatch between electrode and dielectrics, by retarding the sintering of Ni particles
(while the sintering kinetics of BT layer is not changed).
                                     4.5
                                     4.0             with BT additives (10 vol. %)
                                     3.5             without BT additives




                 discontinuity (%)
                                     3.0
                                     2.5
                                     2.0
                                     1.5
                                     1.0
                                     0.5
                                     0.0
                                           0        2000       4000        6000        8000       10000
                                                                  heating time(s)
                                           Figure 7. 16 Discontinuity as function of sintering time



7.9 Co-sintering induced anisotropy

As detailed in Chapter 5, anisotropic shrinkage behavior was observed in the co-sintering of
multilayers. In this section, a simplified and perfectly packed multilayer system was sintered using
DEM to validate the basics of microstructure evolution before considering complex multilayers with

                                                                                                                      - 129 -
DEM simulation of Ni/BaTiO3 multilayers

heterogeneous microstructures. As Figure 7.17 shows BT/Ni/BT multilayers consist of symmetrically
and crystalline-like packed mono size BT and Ni particles.


                                             (a)                                               (b)
                                                                              z
                z             r
                                                                                   r




                                                    Nickel                    Barium Titan ate

                         Figure 7. 17 Crystalline-like packed BT/Ni/BT multilayers

The initial contact size is 0.1 (normalized by 2R). Initial average green density is D = 0.55 (Fig.
7.18(a)). Contact laws developed previously for sintering are further used without modifications.
Several significant results can be highlighted (see Fig. 7.18(b)):




            Figure 7. 18 Microstructure and density profile: (a) before sintering (b) after sintering



- 130 -
                                                                                   DEM simulation of Ni/BaTiO3 multilayers

First, the electrode is continuous and seems to be able to achieve a full densification. This is due to the
homogenous initial microstructures. This again indicates that initial heterogeneity is one of the
conditions that lead to electrode discontinuity.

Second, an obvious anisotropy is found in different layers. The pores in BT layers are orientated in
parallel to the layer plane while the pores in the Ni layers are orientated perpendicular to the layer
plane. In the BT layers, the interface regions are denser than the inner regions; conversely, in the Ni
layers, the interface regions are less dense than the inner regions (in Fig. 7.18(b)). Note that density
was measured in the middle of the sample as indicated by the selected volume in the dashed lined
rectangular volume. This anisotropy is in qualitative agreement with experimental data (see Chapter
5.3.2) and the same arguments can be used to explain this anisotropy. That is, the compressive
stresses facilitate the growth of vertical BT-BT contacts; while the tensile stresses hinder the growth
of the vertical Ni-Ni contacts. Figure 7.19(a) shows the evolution of typical horizontal and vertical Ni-
Ni and BT-BT contacts evolve as a function of time.

                                       1.0                                                               Ni-Ni
                                                Ni-Ni




      normalized contact size (a/2R)
                                       0.9
                                                Ni-Ni                                                    ˔
                                       0.8                                                          //
                                                BT-BT
                                       0.7      BT-BT//
                                       0.6
                                       0.5
                                                                                                            ˔
                                       0.4                                                          //

                                       0.3
                                       0.2
                                       0.1
                                         0.55     0.60        0.65        0.70          0.75             BT-BT
                                                          relative density

  Figure 7. 19 The normalized vertical and horizontal contact sizes of the Ni-Ni contacts and BT-BT contacts
                                                                evolve as function of density

It is found that the anisotropy is more pronounced for the Ni-Ni contacts than for BT-BT contacts
because the Ni sinters earlier and faster.

Figure 7.20 shows contact size distributions (regardless of the orientation of the contacts) of the Ni-Ni
contacts and the BT-BT contacts after having achieved different densities. Generally, all the
distributions are bimodal. The two modes indicate the horizontal and vertical (z- direction) contacts.
As sintering proceeds, both the vertical and the horizontal contacts grow, resulting in the two peaks‟
shift to the right. By referring to the average contact size with Figure 7.19(a), the major peak for the


                                                                                                                   - 131 -
DEM simulation of Ni/BaTiO3 multilayers

Ni-Ni contact distribution indicates the horizontal contacts. Also, it is interesting to notice that the
population of the horizontal contacts increases compared with the population of the vertical contacts.
this might be because some vertical contacts size decrease at some point (D = 0.73-0.74), due to the
de-sintering of the Ni-Ni under tensile stresses (refer to the blue curve in Fig.7.19(a)). For the BT-BT
contacts, the major peak represents the horizontal contacts while the minor peak represents the
vertical contacts. The population of vertical contacts is comparatively smaller than that of the
horizontal contacts. This is because only a small population of particles, which are near the interface
(1-2 layers of particles) might be influenced. Note that the absolute number of vertical and horizontal
contacts is almost unchanged in Ni and BT layers.


                                         2800
                                                   (a)
                                                                                                                       D=0.60




                  counts of occurances
                                         2400
                                                                                                                       D=0.75
                                         2000
                                         1600
                                         1200
                                                                                                                   Ni-Ni contacts

                                          800
                                          400
                                            0
                                             0.4         0.5      0.6       0.7        0.8       0.9       1.0        1.1         1.2
                                                                         nornalized contact size (a/2R)
                                         16000     (b)
                                                                                                                       D=0.60
                                         14000                                                                         D=0.75




          counts of occurances
                                         12000
                                         10000
                                         8000                                                                    BT-BT contacts
                                         6000
                                         4000
                                         2000
                                            0
                                             0.4         0.5      0.6       0.7        0.8       0.9       1.0        1.1         1.2
                                                                             normalized size (a/2R)


                                                          Figure 7. 20 Contact size evolution during sintering


7.10 Towards more realistic microstructure: coupling with experiments

In the aforementioned simulations, the PSDs of BT and Ni simulated particles were those of
experimental data. The packings were randomly generated and then were isostatically compacted to
obtain the same green density as measured from experiments. However, we have demonstrated that
some inter-agglomerate pores which size are several times the average particle size, exist before
sintering. These inter-agglomerate pores are considered to form from the inhomogeneous dispersion
of nickel particles and/or the release of the gas due to the burning of the binders at the binder burn out
process. It may thus be interesting to be able to generate numerical microstructures from even more
realistic conditions.


- 132 -
                                                            DEM simulation of Ni/BaTiO3 multilayers

Thanks to the high-resolution FIB-nT, all single particles, even the nano sized BT additives, can be
separated using marker controlled 3D watershed segmentation (see Chapter 5). Assuming that
particles can be approximated to spheres, a corresponding numerical sample can be reproduced by
locating particles of equivalent radius (see Eq.(5.3)) at the same positions of their centroid.


Figure 7.21 shows how the representative cylindrical BT/Ni/BT sandwiched sample (Fig. 7.21(b)) is
duplicated from its real microstructure (Fig. 7.21(a)).




      Figure 7. 21 (a) Cylinder sample extracted from FIB-nT; (b) equivalent numerical model; (c) initial
                     microstructures of the Ni electrode; (d) equivalent numerical model


Note that the direct processing of nanotomography images into numerical microstructures causes
abnormal initial inter-particle contacts as shown in the ellipses in Figure 7.22(a). This is because real
particles have irregular shape. Simple intersecting spheres overestimate the size of these contacts.
Conversely, some contacts that existed in the real sample disappear from the numerical sample.




                                                                                                       - 133 -
DEM simulation of Ni/BaTiO3 multilayers




                      Figure 7. 22 Rearrangement of particles after relaxation process


The sintering behavior of these direct fitted green microstructures with abnormal initial contacts can
be quite different from the real situation. Thus, an unloading process was simulated to release the
stresses originating from the abnormal overlapping of particles. After a relaxation, reasonable initial
relative contact size (0.1) was obtained (Fig. 7.22(b)). Ni packing was not rearranged so much due to
the almost spherical nature of the Ni particles. In that case, the numerical Ni packing replicates
correctly the real packing and initial inter-agglomerate pores. On the other hand, in the BT layers,
significant rearrangement of BT particles was observed in the BT layers during the relaxation
treatment. Since the BT particles act primarily as a constraining substrate and do not densify much,
we consider that the proposed method leads to a realistic microstructure.


Figure 7.23 shows microstructures before and after sintering during the standard heating stage.
Discontinuous areas in the sintered electrode clearly originate from the initial inter-agglomerate pores,
which can be considered as initial defects. It may also be observed that large initial defects lead to
significant discontinuities (Fig. 7.23(d)). In any case, the findings from these simulations that use
numerical microstructures originating from experimental data confirm those from the fully numerical
processed microstructures.




- 134 -
                                                            DEM simulation of Ni/BaTiO3 multilayers




 Figure 7. 23 Microstructures of electrode before and after sintering (nano additives of BT have been removed
                                                 for clarity)


7.11 Conclusions

We have described in this chapter DEM simulations of co-sintering of BT/Ni/BT multilayers during
the heating stage. This stage is believed to be critical for the initiation of discontinuities. The effects
of inclusions, heating rate, green density, electrode thickness and of the rearrangement of particles
have been investigated. The following conclusions can be made:

(1) Intrinsic heterogeneities (inter-agglomerate pores) are the origins of discontinuities in the
electrode. It was shown that a theoretically perfectly homogenous electrode can develop a continuous
and dense microstructure, even in the presence of the adjacent constraining BT layers. However, a
heterogeneous electrode can also achieve full densification in the absence of external constraints.
Therefore, the existence of heterogeneities and the presence of constraining conditions are the
necessary conditions for the formation of large electrode discontinuities.

(2) Electrode discontinuities can be lessened by the introduction of inclusions, which retard the
densification of electrode materials.


                                                                                                      - 135 -
DEM simulation of Ni/BaTiO3 multilayers



(3) A fast heating can reduce the formation of the discontinuities as the sintering mismatch between
electrode and dielectric is reduced.

(4) The electrode thickness should be carefully designed to obtain continuous, homogenous layer. A
maximal particle size of 1/10 of the average layer thickness seems to be a good compromise.

(5) The green density of electrode should be optimized. In general, it is always disadvantageous to
start with a too porous electrode, since more pores lead to more heterogeneities. The electrode should
not be too dense so that a fast densification of electrode materials is avoided. It is likely that the
condition of a too dense green electrode is hardly met in real industrial settings.

(6) Particle rearrangement of electrode powders should improve the connectivity of the electrode.




- 136 -
                                                                         Conclusions and perspectives


8. Conclusions and perspectives

8.1 General conclusions

Multilayer ceramic capacitors (MLCCs), as the most widely used passive components in the
electronics devices, face the problem of electrode discontinuity (uncovered ratio of sintered electrode)
which forms during the co-firing process. This challenge becomes more important as the size of the
MLCCs steadily decrease due to miniaturization. Ni-electrode BT based MLCCs, which account for
95% of the MLCC market, have been considered in this work.

In comparison with conventional post-sintering 2D sectioning methods, nondestructive X-ray nano
computed tomography (X-ray nCT) was utilized to comprehend the evolution mechanism of the
electrode discontinuity. Synchrotron X-ray nCT characterization was conducted at the Beamline 32-
IDC of the Synchrotron Advanced Photon Source (Argonne National Laboratory, USA). X-ray nCT
characterizations of initial and sintered microstructures of a representative cylindrical volume (Ø20
µm × 20 µm) extracted from a Ni-MLCC chip using FIB machining indicate that the final
discontinuities are linked to the initial heterogeneities already present in the green state. In-situ X-ray
imaging of the sintering of a cylindrical Pd-MLCC sample prepared by the same routine, was carried
out to refine the missing data taken during in the ex-situ observation of the sintering of the Ni-MLCC
sample. It is confirmed that the discontinuities of the electrode originate from the initial existing
heterogeneities, represented by the inter-agglomerate porous and low density regions. These
discontinuities form during the heating ramp due to the sintering shrinkage mismatch between
electrodes and dielectrics.

Correlative studies on green and sintered MLCCs (including the one imaged by X-ray nCT) were
carried out using high resolution (5 × 5 × 5 nm3) FIB-nT.
These comparisons are very informative and show that:

    (1) The current spatial resolution (30 nm) of the X-ray nCT is sufficient to study pore evolution
        and the formation of electrode discontinuities.

    (2) Particulate characteristics, such as particle (pore) size, particle (pore) size distribution can be
        quantitatively analyzed, providing realistic input for the DEM simulations.

These multi-scale characterizations using X-ray nCT and FIB-nT have shed light on comprehension
of the anisotropic sintering behavior and microstructure evolutions during the co-sintering of
multilayered systems. This knowledge is not limited to the MLCCs, and can be extended to SOFCs,
H/LTTCs, and gas separation membranes, etc. General conclusions are:




                                                                                                   - 137 -
Conclusions and perspectives

    (1) Due to the sintering kinetics mismatch, compressive stresses developed near the interfacial
          region on the slowly densifying layer side and facilitate the sintering of particles
          preferentially in the layer plane, resulting in preferential growth of the vertical contacts.

    (2) Conversely, on the fast-densifying side, the tensile stresses can hinder the sintering in the
          layer plane, resulting in preferential growth of the horizontal contacts.

    (3) Density gradient was observed due to this anisotropic sintering behavior. In the slowly
          densifying layer, the interface is denser than the inner regions; in the fast-densifying layer, the
          interface is less dense than the inner regions.

The achieved density of BT layers in the sintered Ni/BT MLCC is lower than that in the commercial
MLCC chips due to the sintering atmosphere. However, this should not alter the qualitative statements
in this work but the quantitative aspects. As it has been revealed in experiments (Chapter 3 and 4),
discontinuities have formed already during the heating stage. The Discrete Element Method (DEM) is
a powerful tool to study the microstructure evolution during this stage. We consider that in the early
stage of sintering of Ni/BT MLCCs, Ni sinters earlier and faster than BT, and that BT shows
negligible shrinkage by the end of the heating ramp. The Ba-Ni-Ti alloy which forms a liquid phase
at the Ni/BT interface was not considered in this study for the moment.

The proposed model was first tested on the Ni/BT composite material. The effects of the size, the
volume fraction and the dispersion degree (aggregates) of BT additives were investigated. The
retardation effect of the inclusions on the sintering of a nickel matrix has been documented:

    (1) The retardation effect increases as the inclusion size decreases;

    (2) The retardation effect increases as the inclusion volume fraction increases;

    (3) For a given size and a given volume fraction of inclusions, a good dispersion of the inclusions
          can enhance the retardation effect.

Sintering kinetics is tuned by controlling the size, the volume fraction (which fits to micromechanical
previously established) and dispersion degree of the inclusions.

The DEM simulations were also applied to the sintering of BT/Ni/BT multilayers. Particle size and
size distribution measured from the experiments were used as inputs for the particle properties. The
comparison of the free sintering of a mono electrode layer with the constrained sintering of a
sandwiched Ni electrode shows that the presence of constraints is a necessary condition for the
appearance of discontinuities. However, a second necessary condition is the existence of an initial
heterogeneity. In a real particulate system, this second condition is always met.




- 138 -
                                                                       Conclusions and perspectives

The qualitative conclusions that are found from experimental observations and from detailed
simulations at the particle length scale agree with each other.

It has been demonstrated that the introduction of 10 vol.% BT inclusions into the Ni electrode leads to
a reduction of electrode discontinuity. A series of DEM simulations on different samples and
conditions have been carried out to suggest possible ways to optimize parameters for producing
MLCC chips with lower electrode discontinuity. The following conclusions have been achieved:

    (1) Fast heating rates are beneficial to obtain lower electrode discontinuity. During the heating
        stage, the electrodes sinter significantly while the dielectrics hardly densify. The shorter the
        heating ramp, the less sintering mismatch is accumulated and hence less discontinuity.

    (2) An optimum green density should be targeted in the electrode. Loose green packing of the
      electrode must be avoided since it can lead to high discontinuity due to higher probability of
      having initial heterogeneity. A too high green density may also lead to a larger sintering
      mismatch, as the coordination number and sintering potential are increased.

    (3) The electrode thickness should be carefully designed to obtain electrode with acceptable
      discontinuity level. The constraints are transmitted via the interfaces through a few layers of
      particles. So the thinner the electrode layers are in comparison with the particle size, the
      stronger the effect of the constraint is.

    (4) The presence of initial heterogeneity contributes significantly on the final discontinuity in the
      electrode.


8.2 Recommendations

Based on our findings from both experiments and numerical simulations, we may propose some
suggestions to manufacturers to improve the MLCC fabrication process.

   To produce MLCC green chips with homogenous packing in electrode.

    (1) Use of electrode metal powders with narrow particle size distributions should help to achieve
        a homogenous packing in electrode.

    (2) Good dispersion of metal powders and ceramic inclusions should reduce the amount of initial
      heterogeneities.

    (3) Green density of electrode should be optimized. Balance between sintering kinetics and initial
      heterogeneity should be achieved.

    (4) Electrode thickness should be optimized to balance electrode discontinuity and the MLCC
      chip‟s size and consumption of metal.


                                                                                                 - 139 -
Conclusions and perspectives

    (5) Smoothness of the dielectric sheets is important for printing smooth electrodes.

    (6) Binder burn out process should be carefully conducted to release the gas slowly and avoid
      residual pores.

   To optimize the firing temperature profile

    (1) Reducing the temperature and dwelling time at the second BBO process should reduce the
          discontinuity formation. Binders with lower decomposition temperature need to be developed.

    (2) Fast heating rates can be utilized but may lead to potential thermal cracks.

    (3) Dwelling time should be minimized to let the material obtain sufficient mechanical and
          physical properties but not allow the electrode to deform and swell.


8.3 Research perspectives

   2D X-ray imaging and 3D tomography

X-ray imaging as a non-destructive method is an excellent technique to study the microstructure
evolutions during sintering. Currently, time-resolved 2D X-ray imaging (radiography) is available at
most synchrotron beam lines equipped with CCD (scanning time few seconds) or CMOS (scanning
time ms) detectors. However, the projected images are insufficient for accurate quantification in space.
Fast X-ray micro Computed Tomography (µCT) with CMOS detectors allows for fast 3D data
acquisition with 512 × 512 pixels (ESRF) within 10 s. This ultrafast X-ray µCT should be qualified as
a time resolved tool to study sintering at micro-scale. In the current study, nanotomography is
required to investigate submicron and nano scale powders. However, to date, the only available
synchrotron X-ray nCT (Sector 32-IDC) with high-temperature measurement capability is located at
APS and takes 20-30 min for each 3D data acquisition scanning with a CCD detector.

Thus, combination of in-situ 2D imaging and ex-situ X-ray nCT is a compromise. In addition, high
resolution FIB-nT can be used as a correlative method.

   Coupling of tomography and DEM simulations

In the case of a direct coupling, MLCC samples should consist of micro-scale particles, which are
decomposable with current ultrafast X-ray µCT. The initial microstructure is fitted for DEM
simulation input. DEM simulations are performed using the same experimental conditions and the
same materials properties. Finally, the in-situ reconstructed 3D microstructure and DEM simulated
microstructure can be directly compared and correlated.




- 140 -
                                                                       Conclusions and perspectives

In the case of an indirect coupling, in the presence of nano scale particles, the destructive FIB-nT is
used to obtain the 3D green microstructure and then is transformed to the DEM model. The simulation
results can be compared with additional sintered MLCC sample.

In both case, the DEM simulations face transformation issue. That is the fitted packing has different
contact statistics. One ultimate solution is to use irregular shape elements that are duplicated from the
tomographic data. Another compromise is to introduce an unloading and arrangement process. In this
sense, the direct comparison is in fact an indirect one.

One possible use of DEM simulation, which does not require extensive experimental input, is the
optimization of the particle size distribution in the Ni layer (both for Ni and BT additives).
Simulations may provide an optimum for green density and initial heterogeneity content.

   Multi-scale modeling

The sintering kinetics of Ni is modified by the formation of liquid Ni-Ba-Ti alloy; this modification is
ignored for the moment. An atomic scale simulation is being considered to predict the sintering
kinetics of Ni in the future work. In this DEM simulation study, only sintering during the heating
stage is modeled. As experiment shows, once the sintering temperature of dielectric is reached, the
ceramic particles start to sinter while the metal electrodes are almost fully dense. At this point, it is
inappropriate to simulate the continuum electrode materials using DEM simulation. Thus, simulations
using coupling between FEM (for the Ni layer) and DEM (for the BT layer) may lead to new insight
in the MLCC process.




                                                                                                 - 141 -
Conclusions and perspectives




- 142 -
                                                                                            Appendix A


Appendix A

Based on clear interfaces at inclusion-matrix contacts observed in sintered metal or ceramic matrix
composites [52, 215], we assume that unlike the sintering neck formed at the matrix-matrix contact, a
nearly flat surface is formed at the inclusion-matrix contact on the matrix particle side (Fig. A1). The
outer surface of this plateau is of axial length ρ, which is also assumed to be the radius of curvature in
the axial direction. The axial length ρ is assumed to approximate to indentation h [213].




                              Figure A.1 Inclusion-matrix contact model


The cylindrical plateau V1 and spherical cap V2with height of 2h ( = h+ρ) are calculated as:
V1   aim 2 h               (A.1)

                   1
V2   (2h)2 ( Rm   2h) (A.2)
                   3
Using mass conservation, the volumes V1 and V2 are equal, which leads to:
                8
aim 2  4 Rm h  h 2 ,   (A.3)
                3
Neglecting the h2 term (h<<aim) leads to Eq. (6.14).




                                                                                                  - 143 -
Appendix A




- 144 -
                                                                                          Appendix B


Appendix B

For sintering contacts, the contact radius a can be estimated using Coble‟s law [213] (see Figure B.1).
The outer surface of the neck is tangent to the two spheres with radius of ρ1 and ρ2. The contact radius
is given by:
                                             R1R2
                                  a2  4             h1  h2          (B.1)
                                            R1  R2




                                Figure B.1 Contact model by Coble‟s Law


Using simple geometric relations in triangles ΔO1MO1’ and ΔO2MO2’:
                             ( R1  h2 )2  (a  1 )2  ( R1  1 )2       (B.2)

                             ( R2  h1 )2  (a  2 )2  ( R2  2 )2       (B.3)

Solving Eq. (B.2) and Eq. (B.3) leads to;

                                           a 2  2 R1h2  h22
                                      1                     (B.4)
                                               2 R1  2a

                                              a 2  2 R2 h1  h12
                                      2                         (B.5)
                                                  2 R2  2a
Using the Similar Triangles Theorem, we obtain:
                                                 ( R1  h2 ) 1
                                          y1                   (B.6)
                                                    R1  1



                                                                                                - 145 -
Appendix B


                                               ( R2  h1 ) 2
                                        y2                   (B.7)
                                                  R2  2
Which is used to obtain the final expression of the neck radius.




- 146 -
                                                                                                                                                                            Appendix C


Appendix C

According to the Wicksell‟s classic work in 1925 [159], the frequency of particle size from the 2D
section of mono-sized partilce sample (Fig. C.1) follows:
                                                                                 r r
                                                              f (r )                                                               (C.1)
                                                                             R (R2  r 2 )
Hence, the accumulative frequency is given by:
                                                          r              r        rdr              r
                                        G (r )   f (r )dr                            1  1  ( )2                                                              (C.2)
                                                         0           0
                                                                             R (R  r )
                                                                                      2            R              2




 Figure C.1 Sectioning a sphere randomly produce a distribution of circle sizes, which can be calculated from
                                                                         analytical geometry


For the actual size (3D) distribution of spheres (Fig. C.2(a)), we can assume that spheres which are in
the same bin size (i.e., Class Ni) are mono sized. The corresponding cross-sectioned 2D circle size of
these spheres belonging to Class Ni will distribute according to Eq. (C.1). And the frequency is
distributed as Figure C.2(b).
                             (a)                    Nk                                                                (b)




     Number of occurrences                                                                Number of occurrences
                                                                                                                                                  Class Nk


                                            Ni-1                                                                                                         f i k Nk


                                   N2
                                                                                                                                               fi-1kNk

                             N1                                                                                                 f2 k N k
                                                                                                                      f1 kN k
                                        …                                        Nn                                                        …
                                                                                 R                                                                                            R

                                                   size                                                                                             size
                                            Figure C.2 Practice of the sectioning of each class of the spheres


                                                                                                                                                                                  - 147 -
                                                                                                                       Appendix C

 k

 f  f  f    f  f  1
i 1
        i
            k
                1
                 k
                       2
                        k                 k
                                        i 1        i
                                                        k
                                                                   (C.3)


                     i 1            i 1 2
fi k  1  G (            R)  1  (     )                      (C.4)
                       k               i

                i 1          i2            i2 2       i 1 2
fi k1  G(          R)  G (     R)  1  (    )  1 (     ) (C.5)
                  k            k              i            i

         1              1
f1k  G ( R)  1  1  ( ) 2                            (C.6)
         k              k
This scheme applies to all other classes of particles. Finally, for the 2D sphere size distribution that
has the same size range and bin size:
Nk'  fi k Nk  fi k 1 Nk 1    fi n1 Nn1  fi n Nn (C.7)
For the final frequency distribution of the 2D sectioned size is the sum of N sets of the classic
distributions:

 N  1                                                                                                 N
                                    2                       2                   2                2
                              1                   1                  1               1

                                                                                                           1
        '                1- 1-               1- 1-              1- 1-           1- 1- 
                              2                    3                 4               n
       1
  0 '                      1
                                    2
                                            1
                                                 2
                                                     2
                                                         2
                                                                    1
                                                                         2
                                                                             2
                                                                  1-   1- 
                                                                                 2
                                                                                     1-   1-  
                                                                                       1
                                                                                           2
                                                                                                   2
                                                                                                       2
                                                                                                             N 
N  
                            1-          1-  - 1- 
       2                      2            3     3             4     4       n         n
                                                                                                             2
 N  0
       '
                             0                     2
                                                 1- 
                                                            2
                                                                     2
                                                                         2
                                                                            3
                                                                  1-   1- 
                                                                                2
                                                                                       2
                                                                                           2
                                                                                     1-   1- 
                                                                                                   3
                                                                                                       2

                                                                                                   n 
                                                                                                              N3 
                                                                                                       
                                                                                                           N 4  (C.8)
       3                                           3               4    4        n
       '
 N  0                                                                                                   
                                                                                2                  2
       4                     0                     0                      3
                                                                        1- 
                                                                          4
                                                                                            n-1 
                                                                                         1-
                                                                                            n 
                                                                                                 

                                                                                                        
 '                                                                                                      N 
 N n  0                 0                     0                     0                   n-1 
                                                                                                           n 
                                                                                         1-
                                                                                             n 
                                                                                                  




- 148 -
                                                                                          Erklärung


Erklärung


Ich versichere, dass ich die vorliegende Dissertation selbständig und nur mit den angegebenen
Quellen und Hilfsmitteln angefertigt habe. Die Arbeit hat in gleicher oder ähnlicher Form noch keiner
Prüfungsbehörde vorgelegen.



                                                                     Darmstadt, 13. September 2013

                                                                                           Zilin Yan




                                                                                                 149
Erklärung




150
                                                                                     Curriculum Vita


Curriculum Vitae

Education

10/2010-10/2013            Universitéde Grenoble, Grenoble, France

10/2010-10/2013            Technische Universität Darmstadt, Darmstadt, Germany

                           Double-degree PhD in Material Sciences

09/2007-06/2010            Chinese Academy of Sciences, Hefei, China

                           M. E. in Nuclear Energy Sci. & Eng., Inst. of Plasma Physics

09/2007-06/2008            University of Science and Technology China, Hefei, China,

                           Master courses study

09/2003-06/2007            Huazhong University of Science and Technology, Wuhan, China

                           B.E. in Materials Sci. & Eng., College of Materials Sci. & Eng.



Publications

Peer-reviewed articles

 [1]. Z. Yan, O. Guillon, S. Wang, C.L. Martin, C.-S. Lee D. Bouvard, Synchrotron x-ray nano-
       tomography characterization of the sintering of multilayered systems. Appl. Phys. Lett.
       100(2012)263107.

 [2]. Z. Yan, C.L. Martin, O. Guillon, D. Bouvard, Effect of size and homogeneity of rigid
       inclusions on the sintering of composites, Scripta Mater. 69 (2013) 327-330

 [3]. Z. Yan, O. Guillon, C.L. Martin, S. Wang, C.-S. Lee D. Bouvard, In-situ synchrotron x-ray
       microscopy of sintering of multilayers. Appl. Phys. Lett. 102(2013)223107

Conferences

[1].   Z. Yan, C.L. Martin, O. Guillon, R.K. Bordia, Discrete element simulation: a tool to model
       sintering at the particle length scale, 12th International Conference on Ceramic Processing
       Science. 4-7 Aug, 2013, Portland, USA (Invited plenary talk, presented by C.L. Martin)

[2].   Z. Yan, O. Guillon, S. Wang, C.L. Martin, C-S. Lee, D. Bouvard. Sintering of Ni-based
       electrode in multilayer ceramic capacitors: numerical simulations and experiments, 2012
       Powder Metallurgy World Congress & Exhibition. 14-18 Oct, 2012, Yokohama, Japan (Oral)

[3].   Z. Yan, O. Guillon, S. Wang, C.L. Martin, C. Lee, D. Bouvard. Microstructural evolution


                                                                                                - 151 -
Curriculum Vita

       during co-sintering of multi-layer ceramic capacitors: coupling of simulation and experiment.
       International Conference on Sintering, 28 Aug-1 Sept, 2011, Jeju, South Korea (Poster)

[4].   X. Liu, Z. Yan, C.L. Martin. Discrete Element Simulation of sintering: Towards more realistic
       microstructures, International Conference Sintering 2011, 28 Aug-1 Sept, 2011, Jeju, South




- 152 -
                                                                                            References


References

[1] A Moulson, J. M. Herbert, Electroceramics: Materials, properties, applications, John Wiley &
Sons, Chichester, 2003.
[2] D. M. Zogbi, Capacitors: World Markets, Technologies & Opportunities: 2012-2017(2012),
Paumanok Publications
[3] Technavio, Global Multilayer Ceramic Capacitor Market 2010-2014, 2011
[4] H. Kishi, Y. Mizuno, H. Chazono, Base-Metal Electrode-Multilayer Ceramic Capacitors: Past,
Present and Future Perspectives, Jpn. J. Appl. Phys., 42 (2003) 1-15.
[5] M.-J. Pan, C. A. Randall, A brief introduction to ceramic capacitors. Electrical Insulation
Magazine, IEEE 26 (2010) 44-50.
[6] H. Takagi, History and Future Prospect of Electro-ceramics in Japan and Asia, in: IMAPS/ACerS
8th International CICMT Conference and Exhibition, Erfurt, Germany, 2012.
[7] M. Randall, D. Skamser, T. Kinard, J. Qazi, A. Tajuddin, S. Trolier-McKinstry, C. Randall, S. W.
Ko, T. Decbakupt, Thin Film MLCC, CARTS 2007 Symposium Proceedings, Albuquerque, NM,
2007
[8] http://www.murata.com, accessed 13.05.2013
[9] D. D. Liu, M. J. Sampson, Reliability evaluation of base-metal-electrode multilayer ceramic
capacitors for potential space applications, CARTS proceed., (2011) 45-63.
[10]http://commons.wikimedia.org/wiki/File:BaTiO3_oxygen_coordination.png,accessed 24.05.2013
[11] http://www.avx.com/docs/techinfo/mlcmat.pdf, acessed 01.05.2013
[12] K. Kinoshita, A. Yamaji, Grain-size effects on dielectric properties in barium titanate ceramics, J.
Appl. Phys., 47 (1976) 371-373.
[13] G. Arlt, D. Hennings, G. De With, Dielectric properties of fine-grained barium titanate ceramics,
J. Appl. Phys., 58 (1985) 1619-1626.
[14] M. H. Frey, D. A. Payne, Grain-size effect on structure and phase transformations for barium
titanate, Phys. Rev. B, 54 (1996) 3158-3168
[15] D. McCauley, R. E. Newnham, C. A. Randall, Intrinsic Size Effects in a Barium Titanate Glass-
Ceramic, J. Am. Ceram. Soc., 81 (1998) 979-987.
[16] Y. Mizuno, T. Hagiwara, H. Kishi, Microstructral Design of Dielectrics for Ni-MLCC with
Ultra-thin Active Layers, J. Ceram. Soc. Jpn., 115 (2007) 360-364.
[17] C.-H. Kim, K.-J. Park, Y.-J. Yoon, M.-H. Hong, J.-O. Hong, K.-H. Hur, Role of yttrium and
magnesium in the formation of core-shell structure of BaTiO3 grains in MLCC, J. Eu. Ceram. Soc., 28
(2008) 1213-1219.
[18] H. Kishi, Y. Okino, M. Honda, Y. Iguchi, M. Imaeda, Y. Takahashi, H. Ohsato, T. Okuda, The
effect of MgO and rare-earth oxide on formation behavior of core-shell structure in BaTiO3, Jpn. J.
Appl. Phys., 36 (1997) 5954-5957.

                                                                                                    153
References

[19] H. Chazono, M. Fujimoto, Sintering characteristics and formation mechanisms of core-shell
structure in BaTiO3-Nb2O5-Co3O5 ternary system, Jpn. J. Appl. Phys., 34 (1995) 5354-5359.
[20] Y. Fujikawa, Y. Umeda, F. Yamane, Analysis on the sintering process of X7R MLCC materials,
J. Jpn. Soc. Powder Powder Metall., 51 (2004) 839-844.
[21] C. S. Chen, C. C. Chou, I. N. Lin, Microstructure of X7R type basemetal-electroded BaTiO3
capacitor materials co-doped with MgO/Y2O3 additives, J. Electroceram., 13 (2004) 567-571.
[22] D. Hennings, G. Rosenstein, Temperature-stable dielectrics based on chemically inhomogeneous
BaTiO3, J. Am. Ceram. Soc., 67 (1984) 249-254.
[23] C. A. Randall, S. F. Wang, D. Laubscher, J. P. Dougherty, W. Huebner, Structure property
relationships in core-shell BaTiO3-LiF ceramics, J. Mater. Res., 8 (1993) 871-879.
[24] S. H. Yoon, J. H. Lee, D. Y. Kim, N. M. Hwang, Core-shell structure of acceptor-rich, coarse
barium titanate grains, J. Am. Ceram. Soc., 85 (2002) 3111-3113.
[25] M. Cannon, Focus on Power: Advancements in Ceramic Capacitors, APEC 2011: Applied
Energy and Conversion Conference, 2011
[26] J. R. Yoon, D. S. Shin, D. Y. Jeong, H. Y. Lee, Control of Connectivity of Ni Electrode with
Heating Rates During Sintering and Electrical Properties in BaTiO3 Based Multilayer Ceramic
Capacitors, Trans. Electr. Electron. Mater., 13 (2012) 181-184.
[27] M. M. Samantaray, A. Gurav, E. C. Dickey, C. A. Randall, Electrode Defects in Multilayer
Capacitors Part I: Modeling the Effect of Electrode Roughness and Porosity on Electric Field
Enhancement and Leakage Current, J. Am. Ceram. Soc., 95 (2012) 257-263
[28] A. V. Polotai, I. Fujii, D. P. Shay, G.-Y. Yang, E. C. Dickey, C. A. Randall, Effect of Heating
Rates during Sintering on the Electrical Properties of Ultra-Thin Ni-BaTiO3 Multilayer Ceramic
Capacitors, J. Am. Ceram. Soc., 91 (2008) 2540-2544.
[29] A. V. Polotai, G.-Y. Yang, E. C. Dickey, C. A. Randall, Utilization of Multiple-Stage Sintering
to Control Ni Electrode Continuity in Ultrathin Ni-BaTiO3 Multilayer Capacitors, J. Am. Ceram. Soc.,
90 (2007) 3811-3817
[30] J. G. Pepin, W. Borland, P. O'Callaghan, R. J. S. Young, Electrode-Based Causes of
Delaminations in Multilayer Ceramic Capacitors, J. Am. Ceram. Soc., 72 (1989) 2287-2291.
[31] K. Sugimura, K. Hirao, Effect of a BaTiO3 nanoparticle additive on the quality of thin-film Ni
electrodes in MLCC, J. Ceram. Soc. Jpn., 117 (2009) 1039-1043.
[32] Y. Kinemuchi, S. Uchimura, K. Watari, Centrifugal sintering of BaTiO3/Ni layered ceramics, J.
Eu. Ceram. Soc., 25 (2005) 2223-2226.
[33] Y.-I. Shin, K.-M. Kang, Y.-G. Jung, J.-G. Yeo, S.-G. Lee, U. Paik, Internal stresses in BaTiO3/Ni
MLCCs, J. Eu. Ceram. Soc., 23 (2003) 1427-1434.
[34] S.-H. Wang, Y.-L. Chai, W.-H. Lee, A novel approach to sintering (Ba,Ca)(Ti,Zr)O3 multilayer
ceramiccapacitors with Ni electrodes, J. Eu. Ceram. Soc., 32 (2012) 1711-1723


154
                                                                                           References

[35] J. G. Pepin, High fire multilayer ceramic capacitor electrode technology, Electronic Components
and Technology Conference, 1991, Atlanta, GA, USA,
[36] T. Takahashi, Y. Nakano, H. Shoji, H. Matsushita, H. Ogawa, A. Onoe, H. Kanai, Y.
Yamashita,Effects of additives on the sintering behavior of the Ni internal electrode of BaTiO 3-based
multilayer ceramic capacitors Applications of Ferroelectrics: Proceedings of the 11th IEEE
International Symposium, 1998
[37] Ji-Hun Kang, Dongwon Joo, Hyun-Min Cha, Yeon-Gil Jung, Ungyu Paik, Shrinkage behavior
and interfacial diffusion in Ni-based internal electrodes with BaTiO3 additive, Ceram. Int., 34 (2008)
1487-1494.
[38] K.S. Weil, E.S. Mast, V.L. Sprenkle, Agglomeration behavior of solid nickel on polycrystalline
barium titanate, Mater. Lett., 61 (2007) 4993-4996.
[39] A. V. Polotai, T.-H. Jeong, G.-Y. Yang, E. C. Dickey, C. A. Randall, Pascal Pinceloup, Abhijit S.
Gurav, Effect of Cr additions on the microstructural stability of Ni electrodes in ultra-thin BaTiO3
multilayer capacitors, J. Electroceram. 18 (2007).
[40] A.V. Polotai, D. P. Shay, G.-Y. Yang, E. C. Dickey, C. A. Randall, in. Applications of
Ferroelectrics, 17th IEEE International Symposium on the. IEEE, 1 (2008)1-2.
[41] J.-H. Jean, C.-R. Chang, Effect of Densification Mismatch on Camber Development during
Cofiring of Nickel-Based Multilayer Ceramic Capacitors, J. Am. Ceram. Soc., 80 (1997) 2401-2406.
[42] B.-Y. Yu, W.-C. J. Wei, Defects of Base Metal Electrode Layers in Multi-Layer Ceramic
Capacitor, J. Am. Ceram. Soc., 88 (2005) 2328-2331.
[43] M. N. Rahaman, Ceramic Processing and Sintering, 2nd ed, New York, 2003.
[44] S.-J. L. Kang, Sintering Densification Grain Growth and Microstructure, 1st ed, Elsevier
Butterworth-Heinemann, Burlington, 2005.
[45] H. Tanaka, A. Yamamoto, J. Shimoyama, H. Ogino, K. Kishio, Strongly connected ex situ MgB2
polycrystalline bulks fabricated by solid-state self-sintering, Supercond. Sci. Technol., 25 (2012)
115022.
[46] D. Ravi, D. J. Green, Sintering stresses and distortion produced by density differences in bi-layer
structures, J. Eu. Ceram. Soc., 26 (2006) 17-25.
[47] D. J. Green, O. Guillon, J. Rödel, Constrained sintering: A delicate balance of scales, J. Eu.
Ceram. Soc., 28 (2008) 1451-1466.
[48] R. Raj, R. K. Bordia, Sintering behavior of bi-modal powder compacts, Acta Metall., 32 (1984)
1003-1019.
[49] L. C. De Jonghe, M. N. Rahaman, C. H. Hsueh, Transient stresses in bimodal compacts during
sintering, Acta Metall., 34 (1986) 1467-1471.
[50] M. W. Weiser, L. C. D. Jonghe, Inclusion Size and Sintering of Composite Powders, J. Am.
Ceram. Soc., 71 (1988) C125-C127.



                                                                                                   155
References

[51] W. H. Tuan, E. Gilbart, R. J. Brook, Sintering of heterogeneous ceramic compacts, J. Mater. Sci.,
24 (1989) 1062-1068.
[52] L. Olmos, C. L. Martin, D. Bouvard, Sintering of mixtures of powders: Experiments and
modelling, Powder Technol., 190 (2009) 134-140.
[53] K. Shinagawa, Sintering Stress and Viscosity of Ni/Al2O3Powder Mixtures, AIP Conf. Proceed.,
973 (2008) 22-27.
[54] R. K. Bordia, G. W. Scherer, On constrained sintering I: Constitutive model for a sintering body,
Acta Metall., 36 (1988) 2393-2397.
[55] R. K. Bordia, G. W. Scherer, On constrained sintering III: Rigid inclusions, Acta Metall., 36
(1988) 2411-2416.
[56] R. K. Bordia, G. W. Scherer, On constrained sintering II: Comparison of constitutive models,
Acta Metall., 36 (1988) 2399-2409.
[57] G. W. Scherera, Sintering with Rigid Inclusions, J. Am. Ceram. Soc., 70 (1987) 719-725.
[58] W. Hong, L. R. Dharani, Pressureless Sintering of a Ceramic Matrix with Multiple Rigid
Inclusions: Finite Element Model, J. Am. Ceram. Soc., 78 (1995) 1593-1600.
[59] J. W. Choe, J. N. Calata, G.-Q. Lu, Constrained-film sintering of a gold circuit paste, J. Mater.
Res., 10 (1995) 986-995.
[60] R. K. Bordia, R. Raj, Sintering behavior of ceramic films constrained by a rigid substrate, J. Am.
Ceram. Soc., 68 (1985) 287-292.
[61] G. W. Scherer, T. Garino, Viscous sintering on a rigid substrate, J. Am.Ceram. Soc., 68 (1985)
216-220.
[62] C. H. Hsueh, Sintering of a ceramic film on a rigid substrate, Scripta Metall., 19 (1985) 1213-
1217.
[63] P. Z Cai, D. J Green, G. L Messing, Constrained densification of alumina/zirconia hybrid
laminates, II: viscoelastic stress computation, J. Am. Ceram. Soc., 80 (1997) 1940-1948.
[64] S.-H. Lee, G. L. Messing, D. J. Green, Warpage Evolution of Screen Printed Multilayer
Ceramics During Co-firing, Key Eng. Mater., 264-268 (2004) 321-330.
[65] J.-C. Chang, J.-H. Jeanw, Camber Development During the Cofiring of Bi-Layer Glass-Based
Dielectric Laminate, J. Am. Ceram. Soc., 88 (2005) 1165-1170.
[66] C. S. Kim, S. J. Lombardow, R. A. Winholtz, Strain-Induced Deformation in Magnesia-Alumina
Layered Composites, J. Am. Ceram. Soc., 88 (2005) 2064-2070.
[67] C. S. Kim, S. J. Lombardow, Effect of Processing on the Microstructure and Induced-Strain
Mismatch in Magnesia-Alumina-Layered Composites, J. Am. Ceram. Soc., 89 (2006) 2718-2725.
[68] O. Guillon, Partial Constrained Sintering of Ceramic Layers on Metallic Substrates: A
Comparison Between Modeling and Experiments, J. Am. Ceram. Soc., 94 (2011) 1040-1045.




156
                                                                                            References

[69] J. Chang, O. Guillon, J. Rödel, S.-J. L. Kang, Characterization of warpage behaviour of Gd-
doped ceria/NiO-yttria stabilized zirconia bi-layer samples for solid oxide fuel cell application, J.
Power Sources, 185 (2008) 759-764.
[70] C. S. Kim, S. J. Lombardo, Curvature and bifurcation of MgO-Al2O3 bilayer ceramic structures, J.
Ceram. Process. Res., 9 (2008) 93-96.
[71] J. M. Heintz, O. Sudre, F. F. Lange, Instability of Polycrystalline Bridges that Span Cracks in
Powder Films Densified on a Substrate, J. Am. Ceram. Soc., 77 (1994) 787-791.
[72] L. E. Khoong, Y. M. Tan, Y. C. Lam, Study of deformation and porosity evolution of low
temperature co-fired ceramic for embedded structures fabrication, J. Eu. Ceram. Soc., 29 (2009) 2737-
2745.
[73] O. Guillon, S. Krauß, .J Rödel, Influence of thickness on the constrained sintering of alumina
films, J. Eu. Ceram. Soc., 27 (2007) 2623-2627.
[74] O. Guillon, Microstructural Characterization of Alumina Films During Constrained Sintering, J.
Am. Ceram. Soc., 93 (2010) 627-629.
[75] O. Guillon, R. K. Bordia, C. L. Martin, Constrained Sintering of Ceramic Films and Coatings, in:
Z.Z. Fang (Ed.) Sintering of Advanced Materials, Woodhead Publishing Ltd., 2011.
[76] A. C. Lewis, D. Josell, T. P. Weihs, Stability in thin film multilayers and microlaminates: the role
of free energy, structure, and orientation at interfaces and grain boundaries, Scripta Mater., 48 (2003)
1079-1085.
[77] K.T. Miller, F. F. Lange, D. B. Marshall, The instability of polycrystalline thin films: Experiment
and theory, J. Mater. Res., 5 (1990) 151-160.
[78] http://www.horiba.com, accessed 4.5.2013
[79] H. P. MyersIntroduct, Introductory Solid State Physics, Taylor & Francis, 2002.
[80] http://www.microscopy.ethz.ch/bragg.htm, accessed 11.09.2013
[81] http://www.isc.fraunhofer.de/uploads/media/TOM-AC_english_01.pdf,accessed 8.25.2013
[82] D. M. Frame, Microstructural development and the evolution of defects in constrained and sinter-
forged ceramics, University of Washington, PhD, 2006
[83] F. Mees, Applications of X-ray computed tomography in the geosciences, Geological Society of
London, London, 2003.
[84] S. Bugani, M. Camaiti, L. Morselli, E. V. Casteele, P. Cloetens, K. Janssens, x-ray computed
tomography as a non-destructive tool for stone conservation, in: 9th International Conference on NDT
of Art, Jerusalem Israel, 2008.
[85] P. A. Midgley, E. P. W. Ward, A. B. Hungria, J. M. Thomas, Nanotomography in the chemical,
biological and materials sciences, Chem. Soc. Rev., 36 (2007) 1477-1494.
[86] S. Vasic, B. Grobéty, J. Kueblera, T. Graule, L. Baumgartner, X-ray computed micro
tomography as complementary method for the characterization of activated porous ceramic preforms,
J. Mater. Res., 22 (2007) 1414-1424.

                                                                                                    157
References

[87] J. Chen, C. Wu, J. Tian, W. Li, S Yu, Three-dimensional imaging of a complex concaved
cuboctahedron copper sulfide crystal by x-ray nanotomography, Appl. Phys. Lett., 92 (2008) 233104
[88] A. Kaestner, E. Lehmann, M. Stampanoni, Imaging and image processing in porous media
research, Adv. Water Resourc., 31 (2008) 1174-1187.
[89] W. Li, N. Wang, J. Chen, G. Liu, Z. Pan, Y. Guan, Y. Yang, W. Wu, J. Tian, S. Wei, Z. Wu, Y.
Tian, L. Guo, Quantitative study of interior nanostructure in hollow zinc oxide particles on the basis
of nondestructive x-ray nanotomography, Appl. Phys. Lett., 95 (2009) 053108
[90] J.-Y. Buffiere, E. Maire, J. Adrien, J.-P. Masse, E. Boller, In-situ Experiments with X ray
Tomography: An Attractive Tool for Experimental Mechanics, Exp. Mechan., 50 (2010) 289-305.
[91] Y. K. Chen, Y. S. Chu, J. Yi, I. McNulty, Q. Shen, P. W. Voorhees, D. C. Dunand,
Morphological and topological analysis of coarsened nanoporous gold by X-ray nanotomography,
Appl. Phys. Lett., 96 (2010) 043122.
[92] A. Schropp, P. Boye, A. Goldschmidt, S. Hönig, R. Hoppe, J. Patommel, C. Rakete, D. Samberg,
S. Stephan, S. Schöder, M. Burghammer, C. G. Schroer, Non-destructive and quantitative imaging of
a nano-structured microchip by ptychographic hard X-ray scanning microscopy, J. Microscopy, 241
(2010) 9-12.
[93] A. Diaz, P. Trtik, M. Guizar-Sicairos, A. Menzel, P. Thibault, O. Bunk, Quantitative x-ray phase
nanotomography, Phys. Rev. B, 85 (2012) 020104.
[94] P. J. Withers, X-ray nanotomography, Material today, 10 (2007) 26-34.
[95] W. A. Kalender, Review: X-ray computed tomography, Phys. Med. Biol., 51 (2006) R29-R43.
[96]http://www.ndt-ed.org/EducationResources/HighSchool/Radiography/hs_rad_index.htm, accessed
06.07.2013
[97] A. C. Kak, M. Slaney, Principles of Computerized Tomographic Imaging, The Institute of
Electrical and Electronics Engineers, Inc., New York, 1987.
[98] A. Tkachuk, F. Duewer, H. Cui, M. Feser, S. Wang, W. Yun, X-ray computed tomography in
Zernike phase contrast mode at 8 keV with 50-nm resolution using Cu rotating anode X-ray source,
Zeitschrift für Kristallographie 222 (2007) 650-655.
[99] Y. S. Chu, M. Yi, F. De Carlo, Q. Shen, W.-K. Lee, H. J. Wu, C. L. Wang, J. Y. Wang, C. J. Liu,
C. H. Wang, S. R. Wu, C. C. Chien, Y. Hwu, A. Tkachuk, W. Yun, M. Feser, K. S. Liang, C. S. Yang,
J. H. Je, G. Margaritondo, Hard-x-ray microscopy with Fresnel zone plates reaches 40 nm Rayleigh
resolution, Appl. Phys. Lett., 92 (2008) 103119.
[100] W. Chao, J. Kim, S. Rekawa, P. Fischer, E. H. Anderson, Demonstration of 12 nm resolution
Fresnel zone plate lens based soft X-ray microscopy, Opt. Express, 17 (2009) 17669-17677.
[101] J. Vila-Comamala , K. Jefimovs, J. Raabe, T. Pilvi, R. H. Fink, M. Senoner, A. Maaßdorf, M.
Ritala, C. David, Advanced thin film technology for ultrahigh resolution X-ray microscopy,
Ultramicroscopy, 109 (2009) 1360-1364.
[102] A. Sakdinawat, D. Attwood, Nanoscale X-ray imaging, Nature Photonics, 14 (2010) 799-882

158
                                                                                            References

[103] L. Salvo, P. Cloetens, E. Maire, S. Zabler, J. J. Blandin, J.-Y. Buffière, W. Ludwig, E. Boller, D.
Bellet, C. Josserond, X-ray micro-tomography an attractive characterisation technique in materials
science, Nuclear instruments and methods in physics research section B: Beam interactions with
materials and atoms, 200 (2003) 273-286.
[104] L. Salvo, M. Suéry, A. Marmottant, N. Limodin, D. Bernard, 3D imaging in material science:
Application of X-ray tomography, Comptes Rendus Physique, 11 (2010) 641-649.
[105] H. N. Thi, H. Jamgotchian, J. Gastaldi, J. Härtwig, T. Schenk, H. Klein, B. Billi, J. Baruchel, Y.
Dabo, Preliminary in situ and real-time study of directional solidification of metallic alloys by X-ray
imaging techniques, J. Phys. D: Appl. Phys., 36 (2003) A83-A86.
[106] N. Limodin, L. Salvo, E. Boller, M. Suéry, M. Felberbaum, S. Gailliègue, K. Madi, In situ and
real-time 3-D microtomography investigation of dendritic solidification in an Al-10 wt.% Cu alloy,
Acta Mater., 57 (2009) 2300-2310.
[107] A. Bareggiw, E. Maire, A. Lasalle, S. Deville, Dynamics of the Freezing Front During the
Solidification of a Colloidal Alumina Aqueous Suspension: In Situ X-Ray Radiography Tomography,
and Modeling, J. Am. Ceram. Soc., 94(2011) 3570-3578
[108] D. Tolnai, P. Townsend, G. Requen, L. Salvo, J. Lendvai, H.P. Degischer, In situ synchrotron
tomographic investigation of the solidification of an AlMg4.7Si8 alloy, Acta Mater., 60 (2012) 2568-
2577.
[109] A. Marmottant, L. Salvo, C.L. Martin, A. Mortensen, Coordination measurements in compacted
NaCl irregular powders using X-ray microtomography, J. Eu. Ceram. Soc., 28 (2008) 2441-2449.
[110] M. Tsukahara, S. Mitrovic, V. Gajdosik, G. Margaritondo, L. Pournin, M. Ramaioli, D. Sage, Y.
Hwu, M. Unser, Th. M. Liebling, Coupled tomography and distinct-element-method approach to
exploring the granular media microstructure in a jamming hourglass, Phys. Rev. E, 77 (2008) 061306.
[111] R. Moreno-Atanasio, R. A. Williams, X. Jia, Combining X-ray microtomography with
computer simulation for analysis of granular and porous materials, Particuology, 8 (2010) 81-99.
[112] D. Bernard, D. Gendron, S. Bordere,Proceedings of the 4th Pacific RIM International Conf.
Adv. Mater. Process., PRICM4, 2001
[113] O. Lame, D. Bellet, M. D. Michiel, D. Bouvard, In situ microtomography investigation of metal
powder compacts during sintering, Nucl. Instrum. Method. Phys. Res. B, 200 (2003) 287-294.
[114] O. Lame, D. Bellet, M. D. Michiel, D. Bouvard, Bulk observation of metal powder sintering by
X-ray synchrotron microtomography, Acta Mater., 52 (2004) 977-984.
[115] A. Vagnon, O. Lame, D. Bouvard, M. D. Michiel, D. Bellet, G. Kapelski, Deformation of steel
powder compacts during sintering: Correlation between macroscopic measurement and in situ
microtomography analysis, Acta Mater., 54 (2006) 513-522.
[116] A. Vagnon, J. P. Rivière, J. M. Missiaen, D. Bellet, M. D. Michiel, C. Josserond, D. Bouvard,
3D statistical analysis of a copper powder sintering observed in situ by synchrotron microtomography,
Acta Mater., 56 (2008) 1084-1093.

                                                                                                    159
References

[117] L. Olmos, C. L. Martin, D. Bouvard, D. Bellet, M. D. Michiel, Investigation of the Sintering of
Heterogeneous Powder Systems by Synchrotron Microtomography and Discrete Element Simulation,
J. Am. Ceram. Soc., 92 (2009) 1492-1499.
[118] L. Olmos, T. Takahashi, D. Bouvard, C. L. Martin, L. Salvo, D. Bellet, M. D. Michiel,
Analysing the sintering of heterogeneous powder structures by in situ microtomography,
Philosophical Magazine, 89 (2009):2949-2965.
[119] F. Xu, X.-F. Hu, H. Miao, J.-Hua Zhao, In situ investigation of ceramic sintering by synchrotron
radiation X-ray computed tomography, Opt. Lasers Eng., 48 (2010) 1082-1088.
[120] Y. Niu, F. Xu, X. Hu, J. Zhao, H. Miao, X. Wu, Z. Zhang, In situ investigation of the silicon
carbide particles sintering, J. Nanomater., 2011 (2011) 26.
[121] D. Bernard, O. Guillon, N. Combaret, E. Plougonven, Constrained sintering of glass films:
Microstructure evolution assessed through synchrotron computed microtomography, Acta Mater., 59
(2011) 6228-6238.
[122] P. R. Shearing, Characterisation of Solid Oxide Fuel Cell Electrode Microstructures in Three
Dimensions, Imperial College London, PhD, 2009
[123] P. R. Shearing, J. Gelb, N. P. Brandon, X-ray nano computerised tomography of SOFC
electrodes using a focused ion beam sample-preparation technique, J. Eu. Ceram. Soc., 30 (2010)
1809-1814.
[124] Y. Guan, W. Li, Y. Gong, G. Liu, X. Zhang, J. Chen, J. Gelb, W. Yun, Y. Xiong, Y. Tian, H.
Wang, Analysis of the three-dimensional microstructure of a solid-oxide fuel cell anode using nano
X-ray tomography, J. Power Sources, 196 (2011) 1915-1919.
[125] G. J. Nelson, W. M. Harris, J. J. Lombardo, J. R. I. Jr., W. K. S. Chiu, P. Tanasini, M. Cantoni,
J. V. herle, C. Comninellis, J. C. Andrews, Y. Liu, P. Pianetta, Y. S. Chu, Comparison of SOFC
cathode microstructure quantified using X-ray nanotomography and focused ion beam-scanning
electron microscopy, Electrochem. Commun., 13 (2011) 586-589.
[126] P. R. Shearing, R. S. Bradley, J. Gelb, S. N. Lee, A. Atkinson, P. J. Withers, N. P. Brandon,
Using Synchrotron X-Ray Nano-CT to Characterize SOFC Electrode Microstructures in Three-
Dimensions at Operating Temperature, Electrochem. Solid-State Lett., 14 (2011) B117-B120
[127] G. J. Nelson, K. N. Grew, J. R. I. Jeffrey J. Lombardo, W. M. Harris, A. Faes, .A Hessler-
Wyser, J. V. Herle, S. Wang, Y. S. Chu, A. V. Virkar, W. K. S. Chiu, Three-dimensional
microstructural changes in the Ni-YSZ solid oxide fuel cell anode during operation, Acta Mater., 60
(2012) 3491-3500.
[128] G. J. Nelson, W. M. Harris, J. R. I., K. N. Grew, W. K. S. Chiu, Y. S. Chu, J. Yi, J. C. Andrews,
Y. Liu, P. Pianetta, Three-dimensional mapping of nickel oxidation states using full field x-ray
absorption near edge structure nanotomography, Appl. Phys. Lett., 98 (2011) 173109.




160
                                                                                            References

[129] Q. Shen, W.-K. Lee, K. Fezza, Y. S. Chu, F. D. Carlo, P. Jemian, J. Ilavsky, M. Erdmann, G. G.
Long, Dedicated full-field X-ray imaging beamline at Advanced Photon Source, Nuclear Instruments
and Methods in Physics Research A, 582 (2007) 77-79.
[130] Y. Wang, Y. K. Chen, W. K. S. Chiu, In Situ 3D Imaging and Characterization of Nano-
Structures with X-ray Nano-CT Technique, ECS Trans., (2011) 21-29.
[131] B. John, Advanced tomographic methods in materials research and engineering, Oxford
University Press, New York, 2008.
[132] J.-S. Park, H. Shin, K. S. Hong, H. S. Jung, J.-K. Lee, K.-Y. Rhee, Effect of margin widths on
the residual stress in a multi-layer ceramic capacitor, Microelectr. Eng., 83 (2006) 2558-2563.
[133] M. F. Ashby, A first report on sintering diagrams, Acta Metall., 22 (1974) 275-289.
[134] A. Masuda, Y. Mizuno, S. Ueda, H. Chazono, H. kishi, Development of Multilayer Ceramics
Capacitors exhibiting high Q value, Microelectronics, 13 (1994) 37-42.
[135] L. Holzer, M. Cantoni, Review of FIB-tomography, Nanofabrication Using Focused Ion and
Electron Beams: Principles and Applications, Oxford University Press, 2012
[136] P. G. Kotula, M. R. Keenan, J. R. Michael, Tomographic Spectral Imaging with Multivariate
Statistical Analysis: Comprehensive 3D Microanalysis, Microsc Microanal, 12 (2006) 36-48.
[137] F. Lasagni, A. Lasagni, E. Marks, C. Holzapfel, F. Mücklich, H. P. Degischer, Three-
dimensional characterization of „as-cast‟ and solution-treated AlSi12(Sr) alloys by high-resolution
FIB tomography, Acta Mater., 55 (2007) 3875-3882.
[138] F. Lasagni, A. Lasagni, M. Engstler, H. P. Degischer, F. Mücklich, Nano-characterization of
Cast Structures by FIB-Tomography, Adv. Eng. Mater., 10 (2008) 62-66.
[139] S. Zaefferer, S. I. Wright, D. Raabe, Three-dimensional orientation microscopy in a focused ion
beam-scanning electron microscope: A new dimension of microstructure characterization, Metall.
Mater. Trans. A, 39 (2008) 374-389.
[140] L. Holzer, F. Indutnyi, P. H. Gasser, B. Münch, M. Wegmann, Three-dimensional analysis of
porous BaTiO3 ceramics using FIB nanotomography, J. Microscopy, 216 (2004) 84-95.
[141] P. R. Munroe, The application of focused ion beam microscopy in the material sciences, Mater.
Charact., 60 (2009) 2-13.
[142] J. AW. Heymann, M. Hayles, I. Gestmann, L. A Giannuzzi, B. Lich, S. Subramaniam, Site-
specific 3D imaging of cells and tissues with a dual beam microscope, J. Struct. Biol., 155 (2006) 63-
73.
[143] J. AW Heymann, D. Shi, S. Kim, D. Bliss, J. LS Milne, S. Subramaniam, 3D imaging of
mammalian cells with ion-abrasion scanning electron microscopy, J. Struct. Biol., 166 (2009) 1-7.
[144] E. Schroeder-Reiter, F. Pérez-Willard, U. Zeile, G. Wanner, Focused ion beam (FIB) combined
with high resolution scanning electron microscopy: A promising tool for 3D analysis of chromosome
architecture, J. Struct. Biol., 165 (2009) 97-106.



                                                                                                    161
References

[145] S. Zhang, R. E. Klimentidis, P. Barthelemy, Porosity and permeability analysis on nanoscale
FIB-SEM 3D imaging of shale rock, in: SCA Symposium, 2011.
[146] R. Wirth, Focused Ion Beam (FIB) combined with SEM and TEM: Advanced analytical tools
for studies of chemical composition, microstructure and crystal structure in geomaterials on a
nanometre scale, Chem. Geol., 261 (2009) 217-229.
[147] L. Holzer, B. Muench, M. Wegmann, P. Gasser, R. J. Flatt, FIB-Nanotomography of Particulate
Systems-Part I: Particle Shape and Topology of Interfaces, J. Am. Ceram. Soc., 89 (2006) 2577-2585.
[148] B. Münch, P. Gasser, L. Holzer, R. Flatt, FIB-Nanotomography of Particulate Systems-Part II:
Particle Recognition and Effect of Boundary Truncation, J. Am. Ceram. Soc., 89 (2006) 2586-2595.
[149] A. J. Kubis, G. J. Shiflet, R. Hull, D. N. Dunn, Focused ion-beam tomography, Metall. Mater.
Trans. A, 35 (2004) 1935-1943.
[150] L. A. Giannuzzi, B. W. Kempshall, S. M. Schwarz, J. K. Lomness, B. I. Prenitzer, F. A. Stevie,
FIB lift-out specimen preparation techniques, in: Introduction to Focused Ion Beam, Springer US,
(2005) 201-228[151]
[151] C. A. Volkert, A. M. Minor, Focused ion beam microscopy and micromachining, MRS Bull., 32
(2007) 389-395.
[152] R. Salh, Silicon Nanocluster in Silicon Dioxide: Cathodoluminescence, Energy Dispersive X-
Ray Analysis, Infrared Spectroscopy Studies, 2011.
[153] H. Stegmann, R. Hübner, Y. Ritz, D. Uteß, B. Volkmann, H.-J. Engelmann, In-situ Low Energy
Noble Gas Ion Milling in a Three BeamInstrument,FIB-Workshop: Focused Ion Beams in Research,
Science and Technology, Halle, Germany, 2009
[154] P. Thevenaz, U. E. Ruttimann, M. Unser, A pyramid approach to subpixel registration based on
intensity, IEEE Transactions on Image Processing, 7 (1998) 27-41.
[155] J. C. Russ, The image processing handbook, CRC press, 2006.
[156] L. Vincent, P. Soille, Watersheds in digital spaces: an efficient algorithm based on immersion
simulations, IEEE transactions on pattern analysis and machine intelligence, 13 (1991) 583-598.
[157] www.vsg.com, accessed 2013
[158] http://www.donner-tech.com/whats_wrong_with_ld.pdf, accessed 23.05.2013
[159] S. D. Wicksell, The corpuscle problem: a mathematical study of a biometric problem,
Biometrika, 17 (1925) 84-99.
[160] H. A. Schwartz., The metallographic determination of size distribution of temper carbon
nodules, Metals and Alloys, 5 (1934) 139-141.
[161] S. A. Saltykov, Stereometric Metallography, 2nd ed., Metallurgizdat, Moscow, 1958.
[162] F. A. L. Dullien, Porous Media. Fluid Transport and Pore Structure, Academic Press, 1992.
[163] C. L. Martin, R. K. Bordia, The effect of a substrate on the sintering of constrained films, Acta
Mater., 57 (2009) 549-558.
[164] H. Cremér, Mathematical Methods of Statistics (PMS-9), Princeton University press, 1999.

162
                                                                                          References

[165] Y. Shigegaki, M. E. Brito, K. Hirao, M. Toriyama, S. Kanzaki, Strain tolerant porous silicon
nitride, J. Am. Ceram. Soc., 80 (1997) 495-498.
[166] R. Zuo, E. Aulbach, R. K. Bordia, J. Rödel, Critical evaluation of hot forging experiments: Case
study in alumina, J. Am. Ceram. Soc., 86 (2003) 1009-1105.
[167] O. Guillon, E. Aulbach, R. Bordia, J. Rödel, Constrained sintering of alumina thin films:
Comparison between experiment and modeling, J. Am. Ceram. Soc., 90 (2007) 1733-1737.
[168] R. Mücke, N. H. Menzler, H. P. Buchkremer, D. Stöver, Cofiring of Thin Zirconia Films
During SOFC Manufacturing, J. Am. Ceram. Soc., 92 (2009) S95-S102.
[169] R. K. Bordia, G. W. Scherer, Ceram. Trans. 1 (1988) 872-886.
[170] P. A. Cundall, O. DL Strack, A discrete numerical model for granular assemblies, Geotechnique,
29 (1979) 47-65.
[171] Y. Tsuji, T. Kawaguchi, T. Tanaka, Discrete particle simulation of two-dimensional fluidized
bed, Powder Technol., 77 (1993) 79-87.
[172] P. A. Langston, U. Tüzün, D. M. Heyes, Discrete element simulation of granular flow in 2D and
3D hoppers: dependence of discharge rate and wall stress on particle interactions, Chem. Eng. Sci., 50
(1995) 967-987.
[173] B. H. Xu, A. B. Yu, Numerical simulation of the gas-solid flow in a fluidized bed by combining
discrete particle method with computational fluid dynamics, Chem. Eng. Sci., 52 (1997) 2785-2809.
[174] L. Vu-Quoc, X. Zhang, O. R. Walton, A 3-D discrete-element method for dry granular flows of
ellipsoidal particles, Comput. Meth. Appl. Mech. Eng., 187 (2000) 483-528.
[175] C. O'Sullivan, L. Cui, Micromechanics of granular material response during load reversals:
Combined DEM and experimental study, Powder Technol., 193 (2009) 289-302.
[176] R. Garcıa-Rojo, S. McNamara, H. J. Herrmann, in: European Congress on Computational
Methods in Applied Sciences and Engineering: ECCOMAS 2004, Jyväskylä, 2004.
[177] G. Jeffson, G. K. Haritos, R. M. McMeeking, The elastic response of a cohesive aggregate-a
discrete element model with coupled particle interaction, J. Mech. Phys. Solid., 50 (2002) 2539-2575.
[178] K. Richards, M. Bithell, M. Dove, R. Hodge, Discrete-element modelling: methods and
applications in the environmental sciences, Phil. Trans. R. Soc. Lond. A, 362 (2004) 1797-1816
[179] G. A. D‟addetta, F. Kun, E. Ramm, H. J. Herrmann, From solids to granulates-discrete element
simulations of fracture and fragmentation processes in geomaterials, in: Continuous and discontinuous
modelling of cohesive-frictional materials, Springer US, (2001) 231-258.
[180] S. Hentz, F. V. Donzé, L. Daudeville, Discrete element modelling of concrete submitted to
dynamic loading at high strain rates, Comput. Struct., 82 (2004) 2509-2524.
[181] M. Jiang, S. Leroueil, J.-M. Konrad, Yielding of microstructured geomaterial by distinct
element method analysis, J. Eng. Mech., 131 (2005) 1209-1213.




                                                                                                  163
References

[182] X. Fu, M. Dutt, A. C. Bentham, B. C. Hancock, R. E. Cameron, J. A. Elliott, Investigation of
particle packing in model pharmaceutical powders using X-ray microtomography and discrete
element method, Powder Technol., 167 (2006) 134-140.
[183] W. R. Ketterhagen, M. T am Ende, B. C. Hancock, Process modeling in the pharmaceutical
industry using the discrete element method, J. Pharma. Sci., 98 (2009) 442-470.
[184] C. L. Martin, D. Bouvard, Study of the cold compaction of composite powders by the discrete
element method, Acta Mater., 51 (2003) 373-386.
[185] C. L. Martin, D. Bouvard, S. Shima, Study of particle rearrangement during powder compaction
by the Discrete Element Method, J. Mech. Phys. Solid., 51 (2003) 667-693.
[186] S. Luding, K. Manetsberger, J. Müllers, A discrete model for long time sintering, J. Mech. Phys.
Solid., 53 (2005) 455-491.
[187] C. L. Martin, L. C.R. Schneider, L. Olmos, D. Bouvard, Discrete element modeling of metallic
powder sintering, Scripta Mater., 55 (2006) 425-428.
[188] B. Henrich, A. Wonisch, T. Kraft, M. Moseler, H. Riedel, Simulations of the influence of
rearrangement during sintering, Acta Mater., 55 (2007) 753-762.
[189] C. L. Martin, H. Camacho-Montes, L. Olmos, D. Bouvard, R. K. Bordia, Evolution of Defects
During Sintering: Discrete Element Simulations, J. Am. Ceram. Soc., 92 (2009) 1435-1441.
[190] C. L. Martin, R. K. Bordia, Influence of adhesion and friction on the geometry of packings of
spherical particles, Phys. Rev. E, 77 (2008) 031307.
[191] C. L. Martin, Unloading of powder compacts and their resulting tensile strength, Acta Mater.,
51 (2003) 4589-4602.
[192] C. L. Martin, D. Bouvard, Discrete Element Simulations of the Compaction of Aggregated
Ceramic Powders, J. Am. Ceram. Soc., 89 (2006) 3379-3387.
[193] S. M. Sweeney, C. L. Martin, Pore size distributions calculated from 3-D images of DEM-
simulated powder compacts, Acta Mater., 51 (2003) 3635-3649.
[194] P. Pizette, C. L. Martin, G. Delette, P. Sornay, F. Sans, Compaction of aggregated ceramic
powders: From contact laws to fracture and yield surfaces, Powder Technol., 198 (2010) 240-250.
[195] A. Jagota, G. W. Scherer, Viscosities and Sintering Rates of Composite Packings of Spheres, J.
Am. Ceram. Soc., 78 (1995) 521-528.
[196] A. Jagota, G. W. Scherer, Viscosities and Sintering Rates of a Two-Dimensional Granular
Composite, J. Am. Ceram. Soc., 76 (1993) 3123-3135.
[197] W. J. Soppe, G. J. M. Janssen, B. C. Bonekamp, L. A. C. Veringa, H. J. Veringa, A computer-
simulation method for sintering in 3-dimensional powder compacts, J. Mater. Sci., 29 (1994) 754-761.
[198] F. Parhami, R. M. McMeeking, A network model for initial stage sintering, Mech. Mater., 27
(1998) 111-124.
[199] D. Bouvard, R. M. McMeeking, Deformation of interparticle necks by diffusion-controled creep,
J. Am. Ceram. Soc., 79 (1996) 666-672.

164
                                                                                           References

[200] C. Wang, S. Chen, Application of the complex network method in solid-state sintering, Comput.
Mater. Sci., 69 (2013) 14-21.
[201] J. Rojek, K. Pietrzak, M. Chmielewski, D. Kaliński, S. Nosewicz, Discrete element simulation
of powder sintering, Comput. Meth. Mater. Sci., 11 (2011) 68-73.
[202] T. Kraft, H. Riedel, Numerical simulation of solid state sintering, model and application, J. Eu.
Ceram. Soc., 24 (2004) 345-361.
[203] H. Riedel, H. Zipse, J. Svoboda, Equilibrium pore surfaces sintering stresses and constitutive
equations for the intermediate and late stages of sintering-II diffusional densification and creep, Acta
Metall. Mater., 42 (1994) 445-452.
[204] A. Wonisch, O. Guillon, T. Kraft, M. Moseler, H. Riedel, J. Rödel, Stress-induced anisotropy of
sintering alumina: Discrete element modelling and experiments, Acta Mater., 55 (2007) 5187-5199.
[205] T. Rasp, C. Jamin, A. Wonisch, T. Kraft, O. Guillon, Shape Distortion and Delamination
During Constrained Sintering of Ceramic Stripes: Discrete Element Simulations and Experiments, J.
Am. Ceram. Soc., 95 (2012) 586-592.
[206] L. Verlet, Computer experiment on classical fluids. I. Thermodynamical properties of Lennard-
Jones molecules, Phys. Rev., 159 (1967) 98.
[207] W. C Swope, H. C Andersen, P. H Berens, K. R Wilson, A computer simulation method for the
calculation of equilibrium constants for the formation of physical clusters of molecules: Application
to small water clusters, J. Chem. Phys., 76 (1982) 637.
[208] M. P. Allen, D. J. Tildesley, Computer simulation of liquids, Oxford Science Press, Oxford,
1987.
[209] C. Thornton, S. J. Antony, Quasi-static deformation of particulate media, Phil Trans Roy. Soc.
Lond. Math. Phys. Sci., (1998) 2763-2782.
[210] B.V. Derjaguin, V. M. Muller, Y. P. Toporov, Effect of contact deformations on the adhesion of
particles, J. Colloid. Interface Sci., 53 (1975) 314-326.
[211] S. D. Mesarovic, K. L. Johnson, Adhesive contact of elastic-plastic spheres, J. Mech. Phys.
Solid., 48 (2000) 2009-2033.
[212] R. Raj, M. F. Ashby, On grain boundary sliding and diffusional creep, J. Am. Ceram. Soc., 2
(1971) 1113-1127.
[213] R. L. Coble, Initial Sintering of Alumina and Hematite, J. Am. Ceram. Soc., 41 (1958) 55-62.
[214] J. Pan, H. Le, S. Kucherenko, J. A. Yeomans, A model for the sintering of spherical particles of
different sizes by solid state diffusion, Acta Mater., 46 (1998) 4671-4690.
[215] W. H. Tuan, R. J. Brook, Sintering of heterogeneous ceramic compacts, J. Mater. Sci., 24 (1989)
1953-1958.
[216] O. Sudre, G. Bao, B. Fan, F. F. Lange, Anthony G. Evans, Effect of Inclusions on Densification:
II, Numerical Model, J. Am. Ceram. Soc., 75 (1992) 525-531.



                                                                                                   165
References

[217] Y. Nakada, T. Kimura, Effects of Shape and Size of Inclusions on the Sintering of ZnO-ZrO2
Composites, J. Am. Ceram. Soc., 80 (1997) 401-406.
[218] F. B. Swinkels, M. F. Ashby, A second report on sintering diagrams, Acta Mettal., 29 (1980)
259-281.
[219] R. K. Bordia, R. Raj, Sintering of TiO2-Al2O3 Composites: A Model Experimental Investigation,
J. Am. Ceram. Soc., 71 (1988) 302-310.
[220] R. Ueyama, K. Koumoto, K. Yubuta, T. Fujii, Influence of BaTiO3 nano particle on paste and
sintering properties of Ni internal electrode films by MLCC, J. Ceram. Soc. Jpn., 111 (2003) 282-284.
[221] N. L. Johnson, S. Kotz, N. Balakrishnan, Continuous Multivariate Distributions, Volume 1,
Models and Applications, New York: John Wiley & Sons, 2002.
[222] G. E. P. Box, M. E. Muller, A Note on the Generation of Random Normal Deviates, Ann. Math.
Statist. 29(1958) 610-611.
[223] B. Kieback, M. Noethe, R. Grupp, J. Banhart, T. Rasp, T. Kraft, Analysis of particle rolling and
intrinsic rotations in copper powder during sintering, J. Mater. Sci., 47 (2012) 7047-7055.




166
