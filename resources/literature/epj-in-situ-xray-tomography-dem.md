EPJ Web of Conferences 140 , 13006 (2017 )                                                                      DOI: 10.1051/epjconf/201714013006
Powders & Grains 2017




      Coupling in-situ X-ray micro- and nano-tomography and discrete element
      method for investigating high temperature sintering of metal and ceramic
      powders

      Zilin Yan1 , Christophe L. Martin1 , , Didier Bouvard1 , David Jauffrès1 , Pierre Lhuissier1 , Luc Salvo1 , Luis Olmos2 ,
      Julie Villanova3 , and Olivier Guillon4
      1
        Univ. Grenoble Alpes, CNRS, SIMAP, 38000 Grenoble, France
      2
        Universidad Michoacana de San Nicolás de Hidalgo, IIMM and INICIT, Fco. J. Mujica S/N, Ed. C-2 C.U., Morelia, Michoacán,
      C.P. 58060, Mexico
      3
        ESRF The European Synchrotron, CS 40220, 38043 Grenoble Cedex 9, France
      4
        Forschungszentrum Jülich Institute of Energy and Climate Research, D-52425 Jülich, Germany


                     Abstract. The behaviour of various powder systems during high temperature sintering has been investigated by
                     coupling X-ray microtomography and discrete element method (DEM). Both methods are particularly relevant
                     to analyse particle interactions and porosity changes occurring during sintering. Two examples are presented.
                     The ﬁrst one deals with a copper powder including artiﬁcially created pores which sintering has been observed
                     in situ at the European synchrotron and simulated by DEM. 3D images with a resolution of 1.5 μm have been
                     taken at various times of the sintering cycle. The comparison of the real displacement of particle centers with
                     the displacement derived from the mean ﬁeld assumption demonstrates signiﬁcant particle rearrangement in
                     some regions of the sample. Although DEM simulation showed less rearrangement, it has been able to accu-
                     rately predict the densiﬁcation kinetics. The second example concerns multilayer ceramic capacitors (MLCCs)
                     composed of hundreds of alternated metal electrode and ceramic dielectric layers. The observation of Ni-based
                     MLCCs by synchrotron nanotomography at Argon National Laboratory with a spatial resolution between 10
                     and 50 nm allowed understanding the origin of heterogeneities formed in Ni layers during sintering. DEM
                     simulations conﬁrmed this analysis and provided clues for reducing these defects.



      1 Introduction                                                           these contact force includes surface energy and diﬀusion
                                                                               coeﬃcients. The overall problem must be treated as the
      X-ray microtomography is a non-destructive method used                   minimization of the total surface energy of the packing. A
      to observe the microstructure of materials in 3D [1]. This               diﬃculty of DEM modelling is the availability of appro-
      technique is particularly powerful for particulate materials             priate data for both feeding and validating simulations. In
      where the pore phase is transparent to X-rays. Although                  situ X-ray tomography is clearly appropriate for this pur-
      technologically challenging, in situ observation of a ma-                pose as it can provide quantitative data on particle assem-
      terial during a high temperature thermal treatment, as for               bly dynamics during sintering. Here, we report on two ex-
      example powder sintering, is particularly attractive. With               amples of coupling synchrotron tomography experiments
      third generation synchrotrons, typical resolution is 1 μm                and discrete element simulations.
      and typical scanning time is a few tens of seconds, which
      is convenient for analysing the dynamics of the sintering
      of metal powders. More recently, novel nano-tomography                   2 DEM model
      conﬁgurations allow the antagonism between high resolu-
      tion (sub-micronic) and rapid scan times (tens of seconds)               The details of the DEM model may be found in [2]. The
      to be resolved. This opens new avenues for the observa-                  main ingredients, speciﬁc to the high temperature sinter-
      tion of micronic ceramic particles during sintering. Dis-                ing problem are recalled here. Particles are modeled as
      crete Element Methods (DEM) are relevant for modelling                   spheres that may indent each other due to surface energy
      powder sintering since they explicitly take into account the             minimization. Parhami and McMeeking’ model, which as-
      particulate nature of the material. DEM models for sinter-               sumes that grain boundary and surface diﬀusions are the
      ing should include the speciﬁc contact forces that mimic                 major mechanisms of mass transport, is used [3]. The nor-
      interparticle bonding at high temperature. The writing of                mal contact force between two sintering particles writes:

            e-mail: christophe.martin@grenoble-inp.fr                                    πa4s dδ                  ψ           ψ
           e-mail: didier.bouvard@grenoble-inp.fr                                Ns =           − πγ s 8R∗ 1 − cos    + a s sin        (1)
                                                                                          8Δb dt                     2            2

     © The Authors, published by EDP Sciences. This is an open access article distributed under the terms of the Creative Commons Attribution
     License 4.0 (http://creativecommons.org/licenses/by/4.0/).
EPJ Web of Conferences 140 , 13006 (2017 )                                                                                                        DOI: 10.1051/epjconf/201714013006
Powders & Grains 2017


                                                                                                      

                                                                                                      
                                                                                                                                                                       a)
                                                                                                      

                                                                                                      

                                                                                                      


                                                                                             
                                                                                                         

                                                                                                      

             a)                          b)                                                           

                                                                                                      

      Figure 1. 3D rendering (a) and virtual slice (b) of the image of a                              

      1 mm diameter copper sample with artiﬁcially created pores.                                     
                                                                                                                                            
                                                                                                                                            
                                                                                                      

                                                                                                      
                                                                                                                                                                       b)
      where a s is the contact radius, δ is the indentation, Δb is a
      temperature dependent diﬀusion coeﬃcient, γ s is the sur-                                       


      face energy, R∗ is the eﬀective radius of the two particles                                     

      and ψ is the dihedral angle that deﬁnes the equilibrium                                         


                                                                                           
      shape of the contact. The ﬁrst term on the rhs of eqn (1) is                                      

      the normal viscous term while the second term, which is                                       
      tensile, is the sintering term. A tangential force,
                                                        opposes                                   
      the tangential relative velocity at the contact du
                                                       du :                                         

                                                                                                    
                                       πa2s R∗2 du
                            T s = −η                                (2)                             
                                                                                                                                            
                                        2Δb dt                                                                                              

      where η is a is a viscous parameter with no dimension.
      Because of material transport, the contact radius a s writes:            Figure 2. Particle centre trajectories during sintering (in blue)
                                                                               compared with estimated mean ﬁeld trajectories (in red). a) from
                                 a s = 4R∗ δ                        (3)        microtomography images, b) from DEM simulation.

      which diﬀers by a factor 4 from its equivalent in elasticity.
           No external load is applied on the particle packing and
      particles motion is only dictated by surface minimization                by a watershed procedure. Fig. 2a compares the displace-
      (γ s term in eqn (1)).                                                   ment of each particle center projected in a horizontal plane
                                                                               with the one predicted by the mean ﬁeld hypothesis which
                                                                               assumes uniform isotropic shrinkage. The real displace-
      3 Copper based powders
                                                                               ment roughly follows the mean ﬁeld assumption with sig-
      Experiments were carried out at the European Synchrotron                 niﬁcant deviations in a few regions that evidence particle
      in Grenoble with copper based powder systems sintered up                 rearrangement.
      to 1060◦ C in a furnace located between the X-ray source                      In parallel, DEM simulations of the sintering have
      and the detector. 3D images with a resolution of 1.5 μm                  been performed. Building a realistic DEM packing di-
      and a scanning time of 1 min were recorded at various                    rectly from a 3D image was not satisfactory because of
      stages of the thermal cycle [4]. Among the various in-                   the non-regular particle shape. A customary fabrication
      vestigated systems, we focus on the one with artiﬁcially                 method, involving the real particle size distribution of par-
      created pores (so-called porous), which mimics materials                 ticles and pore formers as well as the initial density of
      with large, controlled porosity as ﬁlters, SOFC electrodes,              the material to be modeled, which have been deduced
      bone implants [5]. Copper powder with 0-63 μm size was                   from microtomography data, was thus worked out [6]. As
      ﬁrst mixed with 10 vol.% of NaCl salt particles with a di-               shown in Fig 2, the results of porous sample simulation
      ameter between 40 and 63 μm as pore formers. This mix-                   are more consistent with the mean ﬁeld assumption than
      ture was then poured in a 1 mm diameter quartz capillary                 the microtomography results. Fig. 3 shows experimen-
      and pre-sintered at 500◦ C during 30 minutes. The capil-                 tal and numerical densiﬁcation kinetics of both a regular
      lary was removed after cooling and the salt was dissolved                copper sample and the porous sample. The diﬀusion co-
      by keeping the sample in distilled water for 5 hours. Fig. 1             eﬃcient has been ﬁtted to get the best agreement between
      shows a 3D rendering and a virtual slice of an image of the              experimental and simulation curves for the regular mate-
      sample. Sintering was achieved at 1050◦ C under reducing                 rial. Then, with the same coeﬃcient the sintering of the
      atmosphere (He - 5 at.% H2) to prevent particle oxidation.               porous sample was also nicely predicted, which suggests
          The raw 3D images were converted to binary images                    that local rearrangement does not play a signiﬁcant role in
      by thresholding and particle segmentation was achieved                   the densiﬁcation process.


                                                                           2
EPJ Web of Conferences 140 , 13006 (2017 )                                                                  DOI: 10.1051/epjconf/201714013006
Powders & Grains 2017



                                                                                a                            b



                                                                                                              scanned volume
                                                                                                200 μm                    100 μm

                                                                                                        c                           d




      Figure 3. Comparison of experimental and numerical densiﬁca-
      tion kinetics of porous copper sample during sintering.

                                                                                                        e                            f
      4 Multilayer ceramic capacitors
      Multilayer ceramic capacitors (MLCCs) are composed of
      hundreds of alternated metal electrode and ceramic dielec-
      tric layers. Several trillions of them are fabricated each
      year for electronic parts. Up-to-date MLLCs comprise
      typically 1 μm thick layers made of nano-sized powders.
      Using the synchrotron radiation provided at Argon Na-               Figure 4. (a-b) MLCC sample preparation for x-ray tomogra-
                                                                          phy; 2D projection images (c) before and (d) after sintering, (d),
      tional Laboratory, non-sintered (green) and sintered ML-
                                                                          reconstructed 3D microstructure (e) before and (f) after sintering.
      CCs composed of Ni electrode and BaTiO3 (BT) dielec-
      tric layers have been observed with a spatial resolution
      between 10 and 50 nm [8]. The green parts were ﬁrst
      machined into 60 μm cone shape with a special drilling
                                                                                    Au                                              BT
      machine (Fig. 4a). The tip was then milled by dual-beam
      FIB-SEM into a 20 μm-diameter cylinder of 20 μm height                                                                        Ni
      (Fig. 4b). Fig. 4c-f show ex-situ 2D projections and 3D
      images before and after sintering. The bright areas corre-
      spond to the Ni phase while dark ones correspond to the
      BT phase. Reverse colour code is used in Fig. 5, which
      shows the in-situ evolution of an MLCC during sintering.                      5 μm                              800 oC
                                                                                           400 oC
      Temperature calibrating was carried out by using nano-
      gold particles, which melting was monitored in-situ.
          Both post-mortem and in-situ observations indicate
      that the particulate nature of the layers dictates the mi-
      crostructural evolution [7]. This is particularly true of the
      Ni layer, which only contains a few submicronic particles
      along its thickness. The discontinuities observed in the Ni
      layers were found to originate from initial heterogeneities
      of nickel powders (Fig. 6). The heterogeneity grows into                             1000 oC                      1050 oC
      a full defect because of the constraint imposed by the two
      layers that sandwich the Ni layer. These ceramic layers do          Figure 5. In-situ observation of MLCC sintering at increasing
      not sinter since their sintering temperature is higher. DEM         temperature. Au particles are used both for image alignment and
      simulations were carried out to reﬁne this scenario.                for calibrating the furnace temperature.
          Particle size and size distribution measured by tomog-
      raphy were used as inputs for simulations. We have ob-
      served that the free sintering of a Ni monolayer leads to
      a ﬁnal homogeneous microstructure. When the metal Ni                duces some initially contacting particles to detach from
      layer is sandwiched between two non-sintering BT layers             each other. In particular, inspection of eqn (1) shows that
      (Fig. 7), discontinuities appear, thus demonstrating that a         small particles sinter faster than large ones. Indeed, we
      constraint is necessary for their nucleation.                       have observed that contacts between large particles were
          Fig. 7 indicates that particles that form clusters in           more prone to ’de-sintering’ than contacts between small
      the ﬁnal microstructure were initially closely packed. As           ones. Regions with initially low coordination number and
      sintering proceeds, local sintering shrinkage mismatch in-          with some large particles at their boundaries detach, re-


                                                                      3
EPJ Web of Conferences 140 , 13006 (2017 )                                                                DOI: 10.1051/epjconf/201714013006
Powders & Grains 2017


                                                                           this analysis and provided clues for reducing this damage.
                                                                           The versatility of the experimental conﬁguration described
                                                                           here is of great interest for investigations of powders where
                                                                           visualization of thermally activated phenomena is neces-
                                                                           sary at a ﬁne scale. Current progresses to improve further
                                                                           the acquisition parameters toward even smaller resolution
                                                                           (< 100 nm) together with smaller scan times (< 1 s) will
                                                                           certainly qualify in-situ tomography as a method of choice
                                                                           for small powders at room and high temperature.

      Figure 6. Nickel layer evolution with sintering. Low packing
      density regions lead to large discontinuities after sintering.       References
                                                                           [1] L. Salvo, P. Cloetens, E. Maire, S. Zabler, J.J.
                                                                               Blandin, J.Y. Buﬃère, W. Ludwig, E. Boller, D. Bel-
      sulting in pore growth. Conversely, regions with high co-                let, C. Josserond, Nuclear Instruments and Methods in
      ordination number sinter rapidly leading locally to pore                 Physics Research, Section B: Beam Interactions with
      shrinkage. Although particle coarsening is not included in               Materials and Atoms 200, 273 (2003)
      the model (the mechanism that makes large particles grow             [2] Z. Yan, C.L. Martin, O. Guillon, D. Bouvard, Scripta
      by eating away smaller ones), it provides a sound scenario               Mater. 69, 327 (2013)
      for explaining the evolution of the real microstructure pic-         [3] F. Parhami, R.M. McMeeking, Mech. Mater. 27, 111
      tured in Fig. 6a to the one in Fig. 6b.                                  (1998)
          The DEM simulations presented here may also be used              [4] A. Vagnon, J.P. Riviere, J.M. Missiaen, D. Bellet,
      to propose potential improvements by varying some of the                 M.D. Michiel, C. Josserond, D. Bouvard, Acta Mater.
      process parameters [8]. We observed that increasing the Ni               56, 1084 (2008)
      layer thickness had a beneﬁcial eﬀect on the discontinuity           [5] L. Olmos, T. Takahashi, D. Bouvard, C.L. Martin,
      level because it decreases the constraint that non-sintering             L. Salvo, D. Bellet, M.D. Michiel, Philosophical Mag-
      layers. However, this is not a option for the MLCC in-                   azine 89, 2949 (2009)
      dustry, which wants to pack more dielectric layers per unit          [6] L. Olmos, C.L. Martin, D. Bouvard, D. Bellet, M.D.
      volume, not less. A more viable route is to decrease the                 Michielz, J. Am. Ceram. Soc. 92, 1492 (2009)
      sintering driving force for Ni particles until both the ce-
                                                                           [7] Z. Yan, O. Guillon, C.L. Martin, S. Wang, C.S. Lee,
      ramic (BT) and the metal (Ni) layers are at a suﬃciently
                                                                               D. Bouvard, Appl. Phys. Lett. 102, 223107 (2013)
      high temperature to sinter at similar rates. In that case,
                                                                           [8] Z. Yan, C.L. Martin, O. Guillon, D. Bouvard, C. Lee,
      the Ni layer has formed only a small amount of disconti-
                                                                               Journal of the European Ceramic Society 34, 3167
      nuities when the constraint imposed by the non-sintering
                                                                               (2014)
      BT layer is relieved. In that regard, increasing the heating
      rate to reach the sintering temperature (1150◦ C) should be
      eﬀective since it reduces the constrained sintering time of
      the Ni layer. DEM simulations indeed show that increas-
      ing the heating rate from 5 K/min to 50 K/min decreased                       2 μm
      discontinuity from 6 to 1 %. Another option is to use BT
      as additives in the Ni layer. This has the desired eﬀect of
                                                                                       Ni
      retarding the sintering of the metal layer in the temperature                                                      1 μm
      range where the BT layer does not sinter. The addition of
      10 vol. % of BTO nano-particles in the Ni layer decreases                        BT
      the amount of discontinuity from 6 to 4 % at 5 K/min.


      5 Conclusion
      Both study cases show the interest of coupling microto-
      mography and discrete element modelling to better under-
      stand and describe the sintering behaviour of metal and
      ceramic powders. The occurrence of particle arrangement
      during sintering copper material with artiﬁcially created
      pores has been assessed. DEM simulation proved that this
      rearrangement does not play a key role in densiﬁcation.              Figure 7. Nickel layer evolution with sintering. Low packing
      Concerning multilayer ceramic capacitors, nanotomogra-               density regions lead to large discontinuities after sintering.
      phy observation allowed understanding the origin of de-
      fects created during sintering. DEM simulation conﬁrmed



                                                                       4
