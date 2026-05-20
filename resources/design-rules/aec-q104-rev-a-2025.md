                                                  AEC - Q104 - Rev-A
                                                   November 28, 2025




FAILURE MECHANISM BASED
STRESS TEST QUALIFICATION
           FOR
 MULTICHIP MODULES (MCM)
      IN AUTOMOTIVE
       APPLICATIONS




A u to m o tiv e E le c tro n ic s C o u n c il
         Component Technical Committee
                                                                   AEC - Q104 - REV-A
                                                                    November 28, 2025
A u t o m o tiv e E le c tr o n ic s C o u n c il
         Component Technical Committee


                              TABLE OF CONTENTS
AEC-Q104 Failure Mechanism Based Stress Test Qualification for Multichip Modules

1     SCOPE………………………………………………………………………………………………...1
      1.0  Purpose……………………………………………………………………………………….1
      1.1  Reference Documents………………………………………………………………………2
      1.2  Definitions…………………………………………………………………………………….3

2     GENERAL REQUIREMENTS………………………………………………………………………5
      2.1  AEC-Q104 Applicability……………………………………………………………………..5
      2.2  AEC-Q104 Objective………………………………………………………………………..8
      2.3  Precedence of Requirements………………………………………………………………8
      2.4  Use of Generic Data to Satisfy Qualification and Requalification Requirements……..8
      2.5  Test Samples……………………………………………………………………………….10
      2.6  Definition of Test Failure after Stressing………………………………………………...10

3     QUALIFICATION TESTS…………………….…………………………………………………….11
      3.1  Qualification of a New MCM……………………………………………………………....11
      3.2  Requalification of a Changed MCM11

4     QUALIFICATION AND REQUALIFICATION…………………………………………………….12
      4.1  General Tests………………………………………………………………………………12
      4.2  MCM Specific Tests………………………………………………………………………..13
      4.3  Wearout Reliability Tests………………………………………………………………….13

Figure 4: Qualification Test Flow………………………………………………………………..14

Table 1: Qualification Test Methods…………………………………………………………….15

Table 2: Process Change Qualification Guidelines for the Selection of Tests……………………….30

Appendix 1:   MCM Early Life Failure Rate (ELFR)…………………………………………………….33

Appendix 2:   Power Cycling Test (A5B)…………………………………………………………………35

Revision History……………………………………………………………………………………………..37
                                                                                AEC - Q104 - REV-A
                                                                                 November 28, 2025
A u t o m o tiv e E le c tr o n ic s C o u n c il
           Component Technical Committee


                                              Acknowledgment

Any document involving a complex technology brings together experience and skills from many sources. The
Automotive Electronics Council would especially like to recognize the following significant contributors to the
revision of this document:




             Maurice Brodeur                               Analog Devices Incorporated
             Jay Walters                                   BorgWarner
             Keith Edwards                                 Diodes Incorporated
             Gary Fisher                                   Gentex
             Steven Sibrel – [Q104 Team Lead
                                                           Harman
             and Sponsor]
             Ulrich Abelein                                Infineon Technologies
             Ife Hsu                                       Intel
             Banjie Bautista                               ISSI
             Robert Kinyanjui                              John Deere
             Tom Lawler [Q104 Team Leader]                 Consultant
             Mike Buzinski                                 Microchip Technologies
             Sumit Tayal                                   Micron Technology, Inc.
             Melissa Uribe                                 Micron Technology, Inc.
             Rene Rongen                                   NXP Semiconductors
             Zhongning Liang                               NXP Semiconductors
             Peter Turlo                                   onsemi
             Jeffrey Lockledge                             SiriusXM
             Allan Webber                                  Texas Instruments
             Thomas Koschmieder                            Veoneer
                                                                                AEC - Q104 - REV-A
                                                                                 November 28, 2025
A u t o m o tiv e E le c tr o n ic s C o u n c il
           Component Technical Committee


                                                   NOTICE


AEC documents contain material that has been prepared, reviewed, and approved through the AEC Technical
Committee.

AEC documents are designed to serve the automotive electronics industry through eliminating
misunderstandings between manufacturers and purchasers, facilitating interchangeability and improvement of
products, and assisting the purchaser in selecting and obtaining with minimum delay the proper product for use
by those other than AEC members, whether the standard is to be used either domestically or internationally.

AEC documents are adopted without regard to whether or not their adoption may involve patents or articles,
materials, or processes. By such action AEC does not assume any liability to any patent owner, nor does it
assume any obligation whatever to parties adopting the AEC documents. The information included in AEC
documents represents a sound approach to product specification and application, principally from the
automotive electronics system manufacturer viewpoint. No claims to be in Conformance with this document
shall be made unless all requirements stated in the document are met.

Inquiries, comments, and suggestions relative to the content of this AEC document should be addressed to the
AEC Technical Committee on the link http://www.aecouncil.com.

Published by the Automotive Electronics Council.

This document may be downloaded free of charge, however AEC retains the copyright on this material. By
downloading this file, the individual agrees not to charge for or resell the resulting material.

Printed in the U.S.A.
All rights reserved

Copyright © 2025 by the Automotive Electronics Council. This document may be freely reprinted with this
copyright notice. This document cannot be changed without approval from the AEC Component Technical
Committee.
                                                                                AEC - Q104 - REV-A
                                                                                 November 28, 2025
A u t o m o tiv e E le c tr o n ic s C o u n c il
         Component Technical Committee


      FAILURE MECHANISM BASED STRESS TEST QUALIFICATION
                 FOR MULTI-CHIP MODULES (MCM)

Text enhancements and differences made since the last revision of this document
are shown as underlined areas. Several figures and tables have also been revised,
but changes to these areas have not been underlined.

Unless otherwise stated herein, the date of implementation of this standard for new
qualifications and re-qualifications is as of the publish date above.
1.   SCOPE

      This document contains a set of failure mechanism based stress tests and defines the minimum stress
      test driven qualification requirements and references test conditions for qualification of multichip
      modules (MCM). A single MCM consists of multiple electronic components enclosed in a single
      package (refer to Section 1.3.5) that perform an electronic function.

      This document applies only to MCMs which are designed to be soldered directly to a printed circuit
      board assembly.

      MCM types not included in the scope of this document include the following:
       • Two assembly components or MCMs that a Tier 1 / original equipment manufacturers (OEM)
         assembles onto a system.
       • Light Emitting Diodes (LEDs) which are covered completely by the AEC-Q102 Light Emitting
         Diodes (LEDs), Discrete Optoelectronic Devices qualification document are not part of the scope
         of this document. However Discrete Optoelectronic devices which are also considered as MCMs
         are included in the scope of this document (See AEC-Q102-003 for clarification of what is
         considered MCM qualification test plan). In addition, Optoelectronic Devices which are included
         as part of a larger MCM are included in the scope of this document.
       • Micro Electro-Mechanical System (MEMS) which are covered completely by AEC-Q103-00X
         Qualification documents are not part of the scope of this document. However, MEMS devices
         which are also considered as MCMs are included in the scope of this document. In addition, MEMS
         Devices which are included as part of a larger MCM are included in the scope of this document.
       • Power MCMs may require specific considerations and qualification test procedures that are outside
         the scope of this document. A power MCM consists of multiple active power devices (i.e., IGBTs,
         power MOSFETs, diodes) and, if necessary, additional passive devices (e.g. temperature sensors,
         capacitors), which are integrated on a substrate.
       • MCMs with exterior connectors that are not soldered to a board or other assembly.

      For MCM with embedded firmware, the firmware is considered an integral part of the MCM. As such,
      it is qualified as part of the overall system methodology, which is dependent on the type of MCM.
      Standalone qualification of the firmware itself is not in the scope of this document.

      With customer agreement, other pertinent qualification data such as, but not limited to, other automotive
      qualification data, verified reliability numerical modeling or high-volume manufacturing reliability data
      can be utilized to understand and quantify the MCM qualification test plan.

      Use of this document does not relieve the MCM supplier of their responsibility to meet their own
      company's internal qualification program. In this document, "user" is defined as all customers using a
      device qualified per this specification. The user is responsible to confirm and validate all qualification
      data that substantiates conformance to this document. MCM supplier specifies the MCM device
      temperature operation range in their part information.


                                               Page 1 of 38
                                                                                AEC - Q104 - REV-A
                                                                                 November 28, 2025
A u t o m o tiv e E le c tr o n ic s C o u n c il
           Component Technical Committee



1.1     Purpose

        The purpose of this specification is to determine that a MCM is capable of passing the specified stress
        tests and thus can be expected to give a certain level of quality/reliability in the application. A MCM
        design may contain multiple components that are connected within and attached to the MCM.
        Multiple connections are additional sources for quality and reliability failures in MCMs.

1.2     Reference Documents

        Current revision of the referenced documents will be in effect at the date of agreement to the
        qualification plan. Subsequent qualification plans will automatically use updated revisions of these
        referenced documents.

1.2.1   Automotive

        AEC-Q100                        Failure Mechanism Based Stress Test Qualification for Integrated
                                        Circuits
        AEC-Q100-001                    Wire Bond Shear Test
        AEC-Q100-002                    Human Body Model Electrostatic Discharge Test
        AEC-Q100-004                    IC Latch-up Test
        AEC-Q100-005                    Non-Volatile Memory Program/Erase Endurance, Data Retention
                                        and Operational Life Test
        AEC-Q100-007                    Fault Simulation and Fault Grading
        AEC-Q100-009                    Electrical Distribution Assessment
        AEC-Q100-010                    Solder Ball Shear Test
        AEC-Q100-011                    Charged Device Model (CDM) Electrostatic Discharge (ESD) Test
        AEC-Q101                        Failure Mechanism Based Stress Test Qualification for Discrete
                                        Semiconductors
        AEC-Q102                        Failure Mechanism Based Stress Test Qualification for
                                        Optoelectronic Devices in Automotive Applications
        AEC-Q102-003                    Optoelectronic Multichip Modules (OE-MCM)
        AEC-Q103-002                    Failure Mechanism Based Stress Test Qualification for Micro Electro-
                                        Mechanical System (MEMS) Pressure Sensitive Switches
        AEC-Q103-003                    Failure Mechanism Based Stress Test Qualification for MEMS
                                        Microphone Devices
        AEC-Q104-CDC                    Certificate of Design and Construction (CDC Template)
        AEC-Q104-QTP                    Qualification Test Plan (QTP template)
        AEC-Q200                        Stress Test AEC-Q200 Stress Test Qualification for Passive
                                        Components
        AEC-Q001                        Guidelines for Part Average Testing
        AEC-Q002                        Guidelines for Statistical Yield Analysis
        AEC-Q003                        Guidelines for Characterizing the Electrical Performance
        AEC-Q005                        Pb-Free Requirements
        AEC-Q007                        Failure Mechanism Based Testing Guidelines for Components
                                        Mounted to a Printed Board

1.2.2   Military
        MIL-STD-883                     Test Methods Standard Microelectronics
        MIL-STD-1580                    Destructive Physical Analysis for Electronic. Electromagnetic and
                                        Electromechanical Parts

1.2.3   Industrial

        ANSI/ESDA/JEDEC JS-001          ANSI/ESDA/JEDEC Joint Standard for Electrostatic Discharge
                                        Sensitivity Testing, Human Body Model (HBM) Component Level
                                                Page 2 of 38
                                                                                  AEC - Q104 - REV-A
                                                                                   November 28, 2025
A u t o m o tiv e E le c tr o n ic s C o u n c il
           Component Technical Committee


        ANSI/ESDA/JEDEC JS-002           ANSI/ESDA/JEDEC Joint Standard for Electrostatic Discharge
                                         Sensitivity Testing -Charged Device Model (CDM) - Device Level
        JEDEC JEP001-1A                  Foundry Process Qualification Guidelines - Backend of Life (wafer
                                         fab manufacturing sites)
        JEDEC JEP001-2A                  Foundry Process Qualification Guidelines - Front End Transistor
                                         Level (wafer fab manufacturing sites)
        JEDEC JEP001-3A                  Foundry Process Qualification Guidelines - Product Level (wafer
                                         fabrication manufacturing sites)
        JEDEC JEP178                     Electrostatic Discharge (ESD) Sensitivity Testing – Reporting ESD
                                         Withstand Levels on Datasheets
        JEDEC JESD22 series              Reliability Test Methods for Packaged Devices Test methods details
                                         are included in Table 1.
        JEDEC JESD78                     Latch-up
        JEDEC JESD89                     Measurement and Reporting of Alpha Particle and Terrestrial Cosmic
                                         Ray Induced Soft Errors in Semiconductor Devices
        JEDEC JESD89-1                   Test Method for Real-time Soft Error Rate
        JEDEC JESD89-2                   Test Method for Alpha Source Accelerated Soft Error Rate
        JEDEC JESD89-3                   Test Method for Beam Accelerated Soft Error Rate
        IPC/JEDEC J-STD-002              Solderability Test for Component Leads, Terminations, Lugs,
                                         Terminals and Wires
        IPC/JEDEC J-STD-020              Moisture/Reflow Sensitivity Classification for Non-hermetic Surface
                                         Mount Devices (SMDs)
        IPC/JEDEC J-STD-046              Customer Notification Standard for Product/Process Changes by
                                         Electronic Product Suppliers
        IPC/JEDEC-9702                   Monotonic Bend Characterization of Board-Level Interconnects
        IPC-9701                         Performance Test Methods and Qualification Requirements for
                                         Surface Mount Solder Attachments
        ISO 16750-4                      Road Vehicles – Environmental Conditions and Testing for Electrical
                                         and Electronic Equipment – Part 4: Climatic Loads
        SAE J1752/3                      Integrated Circuits Radiated Emissions Measurement Procedure


1.3     Definitions

1.3.1   AEC Q104 Qualification

        Successful completion and documentation of the test results from requirements outlined in this
        document allows the supplier to claim that the MCM is “AEC-Q104 qualified”. For ESD, it is highly
        recommended that the passing voltage be specified in the supplier datasheet with a footnote on any
        pin exceptions. This will allow suppliers to state, e.g., "AEC-Q104 qualified to ESD Classification 2".

        This document focuses only on qualification of the completed MCM component. It does not address
        the qualification of each subcomponent used to create the MCM. However, MCM manufacturers are
        encouraged to leverage AEC qualified sub-components, when available, to promote best MCM quality.


1.3.2   AEC Certification

        Note that there are no "certifications" for AEC-Q104 qualification and there is no certification board run
        by AEC to qualify MCM. Each supplier performs their qualification to AEC standards, considers
        customer requirements, and submits the data to the customer to verify compliance to AEC-Q104.

1.3.3   Approval for Use in an Application

        "Approval" is defined as customer approval for use of a MCM in their application. The customer's
        method of approval is beyond the scope of this document.
                                                 Page 3 of 38
                                                                                  AEC - Q104 - REV-A
                                                                                   November 28, 2025
A u t o m o tiv e E le c tr o n ic s C o u n c il
           Component Technical Committee




1.3.4   Assembly Lot

        An assembly lot as used in this document is a batch of MCMs that are grouped together through the
        same process steps (i.e., through the same machines with same material set through completion of the
        MCM). The assembly lot includes all process and test steps. The same material set includes a
        traceable combination of multiple sub-component lots. A representative flow is shown in Figure 1
        below.




                           Figure 1: General MCM Manufacturing Process Flow


1.3.5   Multichip Module (MCM)

        Multiple active and/or passive sub-components interconnected to create a single complex circuit within
        a single MCM package that is intended for reflow solder attachment to a printed circuit board. Sub-
        components may be molded and/or unmolded (die) combined into a single hermetic or non-hermetic
        package. Bare die (unmounted) is outside the scope of this document.

        Note: Multi-chip and Multichip are both accepted in the industry literature.
                                                 Page 4 of 38
                                                                                 AEC - Q104 - REV-A
                                                                                  November 28, 2025
A u t o m o tiv e E le c tr o n ic s C o u n c il
           Component Technical Committee



1.3.6   MCM Operating Temperature Range

        Typical ambient operating temperature ranges for sub-components are defined in AEC-Q100, AEC-
        Q101, AEC-Q102, AEC-Q103X and AEC-Q200. Supplier shall document the specific operating
        temperature range for the MCM in their datasheet and qualification report.

1.3.7   Process Capability Index Measurement (Cpk)

        Refer to AEC-Q003 Characterization to understand how the Cpk measures will be used in this
        standard.

1.3.8   Subcomponent

        A subcomponent is any element – integrated circuit, discrete, passive, printed circuit board or
        interconnect – included in the MCM construction.

1.3.9   System in a Package (SiP)

        A System in Package (SiP) is an assembly of electronic components and associated interconnection
        in a package configuration that is also intended to be used as a single die package assembly.
        Therefore, it can be qualified within the scope of AEC-Q100 per Section 2.1. An example of a SiP is
        multiple die in a BGA package, where the die are assembled in a stacked or side-by-side configuration.

1.3.10 The Use of Non-Automotive Subcomponents

        The use of automotive qualified stand-alone subcomponents, which can be soldered, glued or
        mounted elsewise on a substrate, is recommended. The use of non-automotive subcomponents is to
        be declared in the CDC document.


2.      GENERAL REQUIREMENTS

2.1     AEC-Q104 Applicability

        The ratings of each subcomponent used in the MCM construction should meet or exceed the MCM
        ratings, including the operating temperatures used by the end user application. The selected
        subcomponent should be capable to withstand the temperature, voltage, current, etc. of the MCM, and
        operate after final testing without degradation.

        Use this document for MCMs that cannot be qualified completely using one of the following:
        • AEC-Q100 Failure Mechanism Based Stress Test Qualification for Integrated Circuits
        • AEC-Q101 Failure Mechanism Based Stress Test Qualification for Discrete Semiconductors
        • AEC-Q102 Failure Mechanism Based Stress Test Qualification for Optoelectronic Devices in
           Automotive Applications
        • AEC-Q102-003 Optoelectronic Multichip Modules (OE-MCM)
        • AEC-Q103-002 Failure Mechanism Based Stress Test Qualification for MEMS Pressure Sensitive
           Switches
        • AEC-Q103-003 Failure Mechanism Based Stress Test Qualification for MEMS Microphone Devices
        • AEC-Q200 Stress Test Qualification for Passive Components

        When feasible, the reliability test methods and qualification plans for MCM can leverage the existing
        guidelines established in AEC-Q100, AEC-Q101, or AEC-Q200. However, additional testing per AEC-
        Q104 Group H must be performed, see Figure 2 below. In addition, if the MCM is tested per AEC-Q102,
        AEC-Q103-002 or AEC-Q103-003 (or additional AEC specifications that are issued in the future) the
                                                Page 5 of 38
                                                                               AEC - Q104 - REV-A
                                                                                November 28, 2025
A u t o m o tiv e E le c tr o n ic s C o u n c il
          Component Technical Committee


       qualification tests that are done at the MCM level can also be used to provide surrogate data for
       qualification, as applicable, per Figure 2. Feasibility is based mainly on MCM complexity, technology,
       and/or package type, but consideration with respect to cost can be applicable with customer agreement.
       This document focuses only on qualification of the completed MCM component. It does not address
       the qualification of each sub-component used to create the MCM. However, MCM manufacturers are
       encouraged to leverage AEC qualified sub-components, when available, to promote best MCM quality.


       The MCM qualification plan is based on .the AEC-Q104 test flow and methods described in this
       document . Note the decisions in Figure 2 below are at the MCM level not subcomponent level.




                       Figure 2: Qualification test method options for the MCM
  The AEC-Q104 tests including Test Group H are the starting point for MCM Qualification planning.
    Note: This Qualification testing is at the completed MCM level not at the subcomponent level.


                                              Page 6 of 38
                                                                                  AEC - Q104 - REV-A
                                                                                   November 28, 2025
A u t o m o tiv e E le c tr o n ic s C o u n c il
             Component Technical Committee


2.2     AEC-Q104 Objective

        These tests are capable of stimulating and precipitating semiconductor device and package failures.
        The objective is to stimulate / precipitate failures in an accelerated manner compared to application
        conditions. This set of tests should not be used indiscriminately. Each qualification project should be
        examined for:

        a. Any potential new and unique failure mechanisms as determined through a Failure Mode Effects
           Analysis (FMEA).
        b. Any situation where these tests/conditions may induce failures that would not be seen in the
           application.
        c. Any extreme use condition and/or application that could adversely reduce the acceleration and,
           therefore, lifetime coverage of the stress test.

        Use of this document does not relieve the supplier of their responsibility to meet their own company's
        internal qualification program.

        In this document, "user" is defined as all customers using a MCM qualified per this specification. The
        user is responsible to confirm and validate all qualification data that substantiates conformance to this
        document.

        Supplier should document ambient operating temperature range for the MCM per Section 1.3.6.

2.3     Precedence of Requirements

        In the event of conflict in the requirements of this standard and those of any other documents, the
        following order of precedence applies:

        a.   The purchase order (or master purchase agreement terms and conditions)
        b.   The (mutually agreed) individual device specification
        c.   This document
        d.   The reference documents in Section 1.2 of this document
        e.   The supplier's data sheet

        For the MCM to be considered a qualified part per this specification, the purchase order and/or the
        individual MCM specification cannot waive or detract from the requirements of this document.

2.4     Use of Generic Data to Satisfy Qualification and Requalification Requirements

2.4.1   Definition of Generic Data

        For simple MCMs (i.e., an encapsulated plastic MCM) that can be qualified by AEC-Q100, AEC-
        Q101, or AEC-Q200, use those documents for the definition of generic data.

        The use of generic data to simplify the qualification process is strongly encouraged. Generic data can
        be submitted to the user as soon as it becomes available to determine the need for any additional
        testing. To be considered, the generic data must be based on a matrix of specific requirements
        associated with each characteristic of the MCM and manufacturing process. If the generic data
        contains any failures, the data is not usable as generic data unless the supplier has documented
        and implemented corrective action or containment for the failure condition that is acceptable to
        the user.

        As defined by other AEC documents, parametric drift measurements may be required for some tests.
        If the product specification or AEC specification has more stringent tests or additional tests than as
        defined in Table 1 they should be added to or substituted into the Module Qualification tests, as
        applicable.
                                                Page 7 of 38
                                                                                    AEC - Q104 - REV-A
                                                                                     November 28, 2025
A u t o m o tiv e E le c tr o n ic s C o u n c il
           Component Technical Committee


        It is the supplier's responsibility to present rationale for why any of the recommended tests
        need not be performed.


        The data on silicon with known fab process identification (i.e., internal fab site) is valid. For third party
        silicon where the fab process is not known, the supplier must rely on the subcomponent manufacturer
        to provide “fab” data. There are no hard and fast rules but a set of general guidelines can be generated.

        Recommended guidelines for grouping of similar MCMs for the purpose of generic reliability data are
        as follows:

        MCMs may leverage generic reliability data from:
        • MCMs with the same substrate base material (laminate) type, trace metal & trace plating. A
          significant change to the substrate, such as a change to the schematic, is considered a fundamental
          change to the MCM and requires extensive re-evaluation.
        • MCMs with the same or greater number of printed circuit board layers.
        • MCMs with the same or smaller feature size of substrate or printed circuit board.
        • MCMs with the same outer configuration package/lid/housing.
        • MCMs with the same series or types of subcomponents – including integrated circuits, discrete and
          passive elements.
        • MCMs with silicon from known same fab processes.
        • MCMs with the same assembly process materials such as solder, adhesives, epoxies, under-fill
          and encapsulant.
        • MCMs assembled at the same assembly subcontractor qualified for the given technology to be
          qualified.

2.4.2   Acceptance of Generic Data

        Use the diagram below for appropriate sources of reliability data that can be used. This data must
        come from the specific part or a MCM in the same qualification family. Potential sources of data could
        include any customer specific data (withhold customer name), process change qualification, and
        periodic reliability monitor data (see Figure 3).




                                                  Page 8 of 38
                                                                                                                              AEC - Q104 - REV-A
                                                                                                                               November 28, 2025
A u t o m o tiv e E le c tr o n ic s C o u n c il
         Component Technical Committee


                                                                                                 History                          Present



                                    Customer #1                         Process Change       Customer #2     Process Change
                                                                                                                                    Qualification data + Process
                                    Specific                                                 Specific
                                                                        Qualification                        Qualification
                                    Qualification                                            Qualification                          change qualification data +


                                                                                                                                    Reliability monitor data =


                                                                                                                                    acceptable generic data
                                                                                           Periodic Reliability

               Internal Device     Supplier Internal
                                                                                             Monitor Tests
                                                       Supplier Start


               Characterization    Qualification       of Production

                                  Note: Some process changes (e.g., die shrink) will affect the use of
                                        generic data such that data obtained before these types of
                                        changes will not be acceptable for use as generic data.

                                           Figure 3: Generic Data Acceptance Considerations




                                                                                         Page 9 of 38
                                                                                   AEC - Q104 - REV-A
                                                                                    November 28, 2025
A u t o m o tiv e E le c tr o n ic s C o u n c il
           Component Technical Committee


2.5     Test Samples

2.5.1   Lot Requirements

        Test samples shall consist of a representative MCM from the qualification family. Where multiple lot
        testing is required due to a lack of generic data, test samples as indicated in Table 1 should be
        composed of approximately equal numbers from non-consecutive sub-component lots, assembled in
        non-consecutive molding lots. That is, they should be separated in the fab or assembly process line
        by at least one non-qualification lot. Any deviation from the above requires technical explanation from
        the supplier. It is recommended that lots are separated by at least one calendar week.

2.5.2   Production Requirements

        All qualification MCMs shall be produced on tooling and processes at the manufacturing site that will
        be used to support MCM deliveries at production volumes. Other electrical test sites may be used for
        electrical measurements after having met the same qualification requirements.

2.5.3   Reusability of Test Samples

        MCMs that have been used for nondestructive qualification tests may be used to populate other
        qualification tests. MCMs that have been used for destructive qualification tests may not be used any
        further except for engineering analysis.

2.5.4   Sample Size Requirements

        Sample sizes used for qualification testing and/or generic data submission must be consistent with the
        specified minimum sample sizes and acceptance criteria in Table 1.

        If the supplier elects to use generic data for qualification, the specific test conditions and results must
        be recorded and available to the user. Existing applicable generic data should first be used to satisfy
        these requirements and those of Section 2.3 for each test requirement in Table 1. MCM specific
        qualification testing should be performed if the generic data does not satisfy these requirements.

2.5.5   Pre- and Post-stress Test Requirements

        End-point test temperatures (e.g., room, hot and/or cold) are specified in the "Additional Requirements"
        column of Table 1 for each test.

2.6     Definition of Test Failure after Stressing

        Test failures are defined as those MCMs not meeting the individual MCM specification, criteria specific
        to the test, or the supplier's data sheet, in the order of significance as defined in Section 2.3. Any MCM
        that shows external physical damage affecting form, fit and function of the final product shipped or
        attributable to the environmental test is also considered a failure. If the cause of failure is due to
        mishandling during stressing or testing such as EOS or ESD, or some other cause unrelated to the
        component reliability, the failure shall be discounted, but reported as part of the data submission.




                                                Page 10 of 38
                                                                                     AEC - Q104 - REV-A
                                                                                      November 28, 2025
A u t o m o tiv e E le c tr o n ic s C o u n c il
            Component Technical Committee


3.      QUALIFICATION AND REQUALIFICATION

3.1     Qualification of a New MCM

        The stress test requirements for qualification of a new MCM is shown in Figure 4 with the corresponding
        test conditions defined in Table 1. For each qualification, the supplier must have data available for all
        of these tests, whether it is stress test results on the MCM to be qualified or acceptable generic data.
        A review shall also be made of other MCMs in the same generic family to ensure that there are no
        common failure mechanisms in that family. Justification for the use of generic data, whenever it is
        used, must be demonstrated by the supplier and approved by the customer.

        For each MCM qualification, the supplier must have available the following:

        •   Certificate of Design and Construction. The AEC-Q104 CDC Template is available from the AEC
            website at http://www.aecouncil.com.
        •   Stress Test Qualification data (see Table 1)
        •   Data indicating the level of fault grading of the software / firmware used for qualification (when
            applicable to the MCM type) per AEC-Q100-007 that will be made available to the customer upon
            request.

        An AEC-Q104 Qualification Test Plan (QTP) template, to aid in qualification planning, is available from
        the AEC website at http://www.aecouncil.com.

3.2     Requalification of a Changed MCM

        Requalification of a MCM is required when the supplier makes a change to the product and/or process
        that impacts (or could potentially impact) the form, fit, function, quality and/or reliability of the MCM (see
        Table 2 for guidelines).

        There are a variety of different changes to a MCM:

        •   The least impact would be a qualified subcomponent change with no change in the critical
            characteristics of the subcomponent. For a simple non-risk change, a simple confirmation of the
            operating characteristics of the MCM is sufficient.
        •   If critical characteristics change (e.g., the device creates more heat, its resistance changes, etc.),
            then a more thorough evaluation is necessary.
        •   If it is a significant change to the substrate, such as a change to the schematic, it is a fundamental
            change to the MCM and requires extensive re-evaluation.
        •   If the change to the substrate is a minor change in manufacturing, less evaluation is possible.

3.2.1   Process Change Notification

        The supplier will meet IPC/JEDEC J-STD-046 or agreed user requirements for product/process
        changes.

3.2.2   Changes Requiring Requalification

        As a minimum, any change that is within customer change requirements or any major change to the
        MCM affecting form, fit and function requires performing the applicable tests listed in Table 1, using
        Table 2 to determine the requalification test plan. Table 2 should be used as a guide for determining
        which tests are applicable to the qualification of a particular change or whether equivalent generic data
        can be submitted for that test(s).




                                                  Page 11 of 38
                                                                                  AEC - Q104 - REV-A
                                                                                   November 28, 2025
A u t o m o tiv e E le c tr o n ic s C o u n c il
           Component Technical Committee


3.2.3   Criteria for Passing Requalification

        All requalification failures shall be analyzed for root cause. Only when corrective and preventative
        actions are in place, the MCM may then be considered AEC-Q104 qualified again.

3.2.4   User Approval

        A change may not affect a MCM's operating temperature range, but may affect its performance in an
        application. Individual user authorization of a process change will be required for that user’s particular
        application(s), and this method of authorization is outside the scope of this document.

3.2.5   Qualification of a MCM Requiring Pb-Free Board Attach

        Added requirements needed to address the special quality and reliability issues that arise when Lead
        (Pb)-Free processing is utilized is specified in AEC-Q005 Pb-Free Requirements. Materials used in
        Pb-Free processing include the termination plating and the board attach (solder). These materials
        usually require higher board attach temperatures to yield acceptable solder joint quality and reliability.
        These higher temperatures may affect the moisture sensitivity level of plastic packaged
        semiconductors. As a result, new, more robust mold compounds may be required. If an encapsulation
        material change is required to provide adequate robustness for Pb-Free processing of the MCM, the
        supplier should refer to the process change qualification requirements in this specification.
        Preconditioning should be performed at the Pb-Free reflow classification temperatures described in
        IPC/JEDEC J-STD-020 Moisture/Reflow Sensitivity Classification for Non-Hermetic Solid State Surface
        Mount Devices before environmental stress tests.


4.      QUALIFICATION TESTS

4.1     General Tests

        Test flows are shown in Figure 4 and test details are given in Table 1. Not all tests apply to all MCMs.
        For example, certain tests apply only to ceramic packaged MCMs, others apply only to MCMs with
        NVM, and so on. The applicable tests for the particular MCM type are indicated in the “Note” column
        of Table 1. The “Additional Requirements” column of Table 1 also serves to highlight test requirements
        that supersede those described in the referenced test method. Any unique qualification tests or
        conditions requested by the user and not specified in this document shall be negotiated between the
        supplier and user requesting the test.

        Note: Sequential Testing

        The general tests listed in Figure 4 and Table 1 are a single stress test methodology or industry
        recognized sequential tests such preconditioning before temperature cycling. Sequential testing, where
        (usually) two different stress methods are executed in a sequence are a common requirement to the
        Tier 1 from the OEM customer. However, sequential testing as a requirement by the component user
        (Tier 1) to the component supplier (Tier 2) has not found broad use. Sequential testing in addition to
        the AEC listed stress tests is permissible as required by a customer or internal supplier qualification
        processes.




                                                Page 12 of 38
                                                                              AEC - Q104 - REV-A
                                                                               November 28, 2025
A u t o m o tiv e E le c tr o n ic s C o u n c il
           Component Technical Committee


4.2   MCM Specific Tests

      The following tests must be performed on the specific MCM. Generic data is not allowed for these
      tests.

      1.       Electrostatic Discharge (ESD) - All product MCMs.

      2.       Latch-up (LU) - All MCMs that include active sub-components. See JESD78 appendix for
               details.

      3.       Electrical Distribution - The supplier must demonstrate, over the operating temperature range,
               voltage, and frequency, that the MCM is capable of meeting the parametric limits of the MCM
               specification. This data must be taken from at least three lots, or one matrixed (or skewed)
               process lot, and must represent enough samples to be statistically valid, see AEC-Q100-009.
               It is strongly recommended that the final test limits be established using AEC-Q001 Guidelines
               for Part Average Testing.


4.3   Wearout Reliability Tests

      Testing for the failure mechanisms listed below must be available to the user whenever a new
      technology or material relevant to the appropriate wearout failure mechanism is to be qualified. The
      data, test method, calculations, and internal criteria need not be demonstrated or performed on the
      qualification of every new MCM, but should be available to the user upon request.

      •    Electromigration
      •    Time-Dependent Dielectric Breakdown (or Gate Oxide Integrity Test) - for all MOS technologies
      •    Hot Carrier Injection - for all MOS technologies below 1 micron
      •    Bias Temperature Instability
      •    Stress Migration




                                             Page 13 of 38
                                                    AEC - Q104 - REV-A
                                                     November 28, 2025
A u t o m o tiv e E le c tr o n ic s C o u n c il
         Component Technical Committee




           Figure 4: Qualification Test Flow




                    Page 14 of 38
                                                                                                                                 AEC - Q104 - REV-A
                                                                                                                                  November 28, 2025
                                                 A u t o m o tiv e E le c tr o n ic s C o u n c il
                                                              Component Technical Committee


                                                           Table 1: Qualification Test Methods
   Table 1 is applicable to all MCMs in the scope of this document but unique technologies such as LED and MEMS may require additional tests. See the test
   requirements for details in Figure 2.

                                               TEST GROUP A – ACCELERATED ENVIRONMENT STRESS TESTS

                                   LEVEL TO               SAMPLE SIZE      NUMBER OF   ACCEPT
     STRESS          ABV      #                NOTES                                              TEST METHOD                  ADDITIONAL REQUIREMENTS
                                     TEST                    / LOT           LOTS      CRITERIA

                                                                                                                   Performed on surface mount MCMs only. PC performed
                                                                                                                   before THB/HAST, AC/UHST/TH, TC, and PTC stresses.
                                                                                                                   It is recommended that J-STD-020 be performed to
                                                                                                                   determine what preconditioning level to perform in the
                                                            Per AEC-
                                                                                                    IPC/JEDEC      actual PC stress per JESD22-A113. The minimum
                                                          Q100/Q101/Q200
                                                                                                     J-STD-020     acceptable level for qualification is level 3 per JESD22-
                                    Apply to   P, B, S,
Preconditioning       PC     A1                                                3        0 Fails                    A113. Where applicable, preconditioning level and peak
                                     MCM        N, G      minimum 30/lot
                                                                                                      JEDEC        reflow temperature must be reported when preconditioning
                                                           or negotiated
                                                          with Customer                            JESD22-A113     and / or MSL is performed. Delamination from the die
                                                                                                                   surface in JESD22-A113/J-STD-020 is acceptable if the
                                                                                                                   MCM passes the subsequent qualification tests. Any
                                                                                                                   replacement of MCM must be reported. TEST before and
                                                                                                                   after PC at room temperature.



                                                            Per AEC-
                                                          Q100/Q101/Q200                                           For surface mount MCMs, PC before THB (85oC/85%RH
Temperature-                                                                                         JEDEC
                    THB or          Apply to                                                                       for 1000 hours) or HAST (130oC/85%RH for 96 hours, or
Humidity-Bias or             A2                P, D, G    minimum 30/lot       3        0 Fails   JESD22-A101 or
                     HAST            MCM                                                                           110oC/85%RH for 264 hours). TEST before and after THB
Biased HAST                                                                                           A110
                                                           or negotiated                                           or HAST at room and hot temperature.
                                                          with Customer




                                                                                                                   For surface mount MCMs, PC before AC (121oC/15psig for
Autoclave or                                                Per AEC-
                                                                                                                   96 hours) or unbiased HAST (130C/85%RH for 96 hours,
                                                          Q100/101/Q200
Unbiased HAST or     AC or                                                                            JEDEC        or 110oC/85%RH for 264 hours). For MCMs sensitive to
                                    Apply to   P, B, D,
Temperature-         UHST    A3                           minimum 30/lot       3        0 Fails    JESD22-A102,    high temperatures and pressure (e.g., BGA and complex
                                     MCM          G
Humidity (without    or TH                                                                         A118, or A101   MCMs), PC followed by TH (85oC/85%RH) for 1000 hours
                                                           or negotiated
Bias)                                                     with Customer                                            may be substituted. TEST before and after AC, UHAST or
                                                                                                                   TH at room temperature.




                                                                           Page 15 of 38
                                                                                                                            AEC - Q104 - REV-A
                                                                                                                             November 28, 2025
                                                A u t o m o tiv e E le c tr o n ic s C o u n c il
                                                            Component Technical Committee


                                                 Table 1: Qualification Test Methods (continued)
                                     TEST GROUP A – ACCELERATED ENVIRONMENT STRESS TESTS (CONTINUED)

                                  LEVEL TO              SAMPLE SIZE      NUMBER OF   ACCEPT
     STRESS           ABV    #                NOTES                                             TEST METHOD               ADDITIONAL REQUIREMENTS
                                    TEST                   / LOT           LOTS      CRITERIA

                                                                                                              For surface mount MCMs, PC before TC.

                                                                                                              1000 cycles across ambient operating temperature range.

                                                                                                              TEST before and after TC at hot temperature. For
                                                                                                              encapsulated packages, include pre- and post-Acoustic
                                                                                                              Microscopy (see AM).
                                                          Per AEC-
                                                        Q100/Q101/Q200                                        Note: At the MCM level, “fast TC” that is quick transition
                                   Apply to                                                        JEDEC      between hot maximum to cold minimum cycling can be
Temperature Cycling   TC     A4                D, G     minimum 30/lot       3        0 Fails
                                    MCM                                                         JESD22-A104   referred to as a “Thermal Shock” (similar to MIL-STD-883,
                                                         or negotiated                                        test method 1010).
                                                        with Customer
                                                                                                              After completion of TC, decap five MCMs from one lot and
                                                                                                              perform WBP and WBS tests on corner bonds (2 bonds
                                                                                                              per corner) and one mid-bond per side on each device.
                                                                                                              See AEC-Q100 Appendix 3 for preferred decap procedure
                                                                                                              to minimize damage and false data. The WBP and WBS
                                                                                                              failure modes observed must be reviewed with the failure
                                                                                                              modes observed before TC stress.


                                                          Per AEC-                                            1000 hours at max ambient storage temperature.
                                                        Q100/Q101/Q200
High Temperature                   Apply to                                                        JEDEC      Note: Not an operation use.
                      HTSL   A6               D, G, K   minimum 30/lot       1        0 Fails
Storage Life                        MCM                                                         JESD22-A103
                                                         or negotiated                                        TEST before and after HTSL at room and hot
                                                        with Customer                                         temperature.




                                                                         Page 16 of 38
                                                                                                                                AEC - Q104 - REV-A
                                                                                                                                 November 28, 2025
                                              A u t o m o tiv e E le c tr o n ic s C o u n c il
                                                         Component Technical Committee


                                               Table 1: Qualification Test Methods (continued)

                                    TEST GROUP A – ACCELERATED ENVIRONMENT STRESS TESTS (CONTINUED)

                                 LEVEL TO            SAMPLE SIZE      NUMBER OF   ACCEPT
     STRESS          ABV    #                NOTES                                               TEST METHOD                  ADDITIONAL REQUIREMENTS
                                   TEST                 / LOT           LOTS      CRITERIA
                                                                                                                PC before PTC for surface mount devices.
                                                                                                                Test required on MCM only if
                                                                                                               -      thermal management structure/materials are used for
                                                                                                                      deliberate heat transfer from a subcomponent within the MCM
                                                                                                                      to the housing of the MCM or the MCM datasheet
                                                       Per AEC-                                                       requires/recommends heat transfer management;
                                                     Q100/Q101/Q200                                            -      the MCM is a MCM meant to regulate (not only sense)
                                                                                                                      voltage/current, directly drive load, or purposefully control
                                  Apply to                                                          JEDEC
                     PTC   A5A               D, G                         1         0 Fails                           current;
                                   MCM               minimum 30/lot                              JESD22-A105          or
                                                      or negotiated                                            -      maximum power dissipation results in internal heating (ΔTJ)
                                                     with Customer                                                    of a subcomponent or MCM ≥ 40 °C (determined from
                                                                                                                      thermal model or empirically)

                                                                                                               1000 cycles across ambient operating temperature range.
                                                                                                               Thermal shut-down shall not occur during this test.
Power Temperature                                                                                              TEST before and after PTC at room and hot temperature.
                                                                                                                PC before PCT for surface mount devices.
Cycling
                                                                                                               Test required on MCM only if
                                                                                                               -     thermal management structure/materials are used for
Or                                                                                                                   deliberate heat transfer from a subcomponent within the
                                                                                                                     MCM to the housing of the MCM or the MCM datasheet
Power Cycling Test                                                                                                   requires/recommends heat transfer management;
                                                                                                               -     the MCM is meant to regulate (not only sense)
(PCT)
                                                                                                                     voltage/current, directly drive load, or purposefully control
                                                                                                                     current;
                                                        Per AEC-                                                        or
                                                     Q100/Q101/Q200                                            -     maximum power dissipation results in internal heating (ΔTJ)
                                                                                    Report                           of a subcomponent or MCM ≥ 40 °C (determined from
                                  Apply to                                                          JEDEC
                     PCT   A5B               D, G    minimum 30/lot       1       Failures and                       thermal model or empirically)
                                   MCM                                                           JESD22-A122
                                                      or negotiated                 Failure
                                                                                  Mechanisms                   Reference the test method with the following modifications.
                                                     with Customer                                             Power cycle between negligible self-heating state and maximum
                                                                                                               self-heating state
                                                                                                               1)    for 7500 cycles at minimum operating ambient temperature
                                                                                                               2)    followed by 7500 cycles at the highest ambient temperature
                                                                                                                     that demonstrates maximum ΔTJ without stressing beyond
                                                                                                                     the maximum datasheet specification of the MCM. Report
                                                                                                                     ambient temperature.
                                                                                                               Thermal shut-down shall not occur during this test.
                                                                                                               TEST before and after PCT at cold and hot temperature.
                                                                                                               See Appendix 2 for more information.




                                                                      Page 17 of 38
                                                                                                                                     AEC - Q104 - REV-A
                                                                                                                                      November 28, 2025
                                                  A u t o m o tiv e E le c tr o n ic s C o u n c il
                                                               Component Technical Committee



                                                   Table 1: Qualification Test Methods (continued)
                                                TEST GROUP B – ACCELERATED LIFETIME SIMULATION TESTS

                                  LEVEL TO                 SAMPLE SIZE      NUMBER OF   ACCEPT
      STRESS          ABV    #                  NOTES                                              TEST METHOD                     ADDITIONAL REQUIREMENTS
                                    TEST                      / LOT           LOTS      CRITERIA



                                                             Per AEC-                                                  1000 hours at maximum ambient operating temperature.
                                                           Q100/Q101/Q200
High Temperature                   Apply to     D, G, K,                                               JEDEC           Voltage at Vcc maximum.
                      HTOL   B1                                                 3        0 Fails
Operating Life                      MCM            M       minimum 30/lot                           JESD22-A108
                                                            or negotiated                                              TEST before and after HTOL at room, cold, and hot
                                                           with Customer                                               temperature, in that order.


                                                                                                                       48 hours at maximum ambient operating temperature.

                                                                                                                       Voltage at Vcc maximum.

                                                                                                                       The electrical verification testing needs to be completed
Early Life Failure                 Apply to                                                        See appendix 1 in
Rate
                      ELFR   B2
                                    MCM
                                                 N, G           231             1        0 Fails
                                                                                                    this document
                                                                                                                       within 48 hours of the end of stress. MCM that pass this
                                                                                                                       stress can be used to populate other stress tests. Generic
                                                                                                                       data is applicable. TEST before and after ELFR at room
                                                                                                                       temperature.

                                                                                                                       See Appendix 1 for details.

                                                                                                                       TEST per AEC-Q100 requirements.

                                     MCM or                                                                            Note for memory cells that may be sensitive to X-rays, an
                                                           Per AEC-Q100
                                   Individual                                                                          X-ray stress may be applicable.
NVM Endurance,
                                      sub-
Data Retention, and   EDR    B3                 D, G, K    minimum 30/lot       3        0 Fails    AEC Q100-005
                                  component                                                                            For controller-firmware-managed MCMs, the endurance
Operational Life                                            or negotiated
                                    level per                                                                          and operating life portions can be performed in MCM
                                                           with Customer
                                  AEC-Q100                                                                             qualification according to AEC Q100-005. Data retention
                                                                                                                       can be performed on the individual components in
                                                                                                                       accordance with AEC-Q100.




                                                                            Page 18 of 38
                                                                                                                                       AEC - Q104 - REV-A
                                                                                                                                        November 28, 2025
                                             A u t o m o tiv e E le c tr o n ic s C o u n c il
                                                        Component Technical Committee


                                              Table 1: Qualification Test Methods (continued)
                                             TEST GROUP C – PACKAGE ASSEMBLY INTEGRITY TESTS

                                LEVEL TO            SAMPLE SIZE       NUMBER OF        ACCEPT
      STRESS         ABV   #                NOTES                                                      TEST METHOD                  ADDITIONAL REQUIREMENTS
                                  TEST                 / LOT            LOTS           CRITERIA

                                                                                      CPK >1.67 as                      At appropriate time interval for each bonder to be used.
                                                    30 bonds from a minimum of 5           built
                                 Apply to
                                                               devices.                [Note: after        AEC
                                  Wires                                                                                 Note: Wire Bond Shear is not required for wire bonds that
Wire Bond Shear      WBS   C1               D, G                                      TC no failure      Q100-001
                                  Within                                                                                have been previously qualified inside a package. The
                                                       Samples from each wire to          modes          AEC Q003
                                  MCM                                                                                   intent is to evaluate additional wire bonds produced during
                                                    subcomponent bond type in the        change]
                                                                                                                        the manufacture of the MCM.
                                                        MCM construction is to be
                                                        sampled. Each bond wire
                                                                                      CPK >1.67 as                      Condition C or D.
                                                    composition, wire diameter and
                                 Apply to                                                  built
                                                        silicon metal interface can                     MIL-STD-883
                                  Wires                                                [Note: after                     Note: Wire Bond Pull/Wire Shear is not required for wire
Wire Bond Pull       WBP   C2               D, G         generate a unique bond                         Method 2011
                                  within                                              TC no failure                     bonds that have been previously qualified inside a
                                                     structure. Duplicate wire bond                      AEC Q003
                                  MCM                                                     modes                         package. The intent is to evaluate additional wire bonds
                                                    structures need not be sampled.
                                                                                         change]                        produced during the manufacture of the MCM.

                                                                                                                        SD test needs to be performed on MCMs samples in final
                                                                                                                        shipment state with ALL normal processing steps included.

                                 Apply to                                                                               If burn-in screening is normally performed on the MCM
                                 External                                                                               before shipment, samples for the SD test must undergo
Solderability                                                                         Per JEDEC            JEDEC
                     SD    C3    Leads /    D, G         15                 1                                           burn in or receive equivalent high temperate bake.
MCM External Leads                                                                    J-STD-002          J-STD-002
                                 Balls of
                                  MCM                                                                                   Note there are circumstances that the Board Level
                                                                                                                        Reliability testing per IPC-9701 or AEC-Q007 can replace
                                                                                                                        this test.

                                                                                                          JEDEC
Physical                         Apply to                                                             JESD22-B100 and   See applicable JEDEC standard outline and/or individual
                     PD    C4               D, G         10                 3          CPK >1.67
Dimensions                        MCM                                                                      B108         MCM spec for significant dimensions and tolerances.
                                                                                                         AEC Q003
                                 Apply to
                                 External            5 balls each
                                                                                                          JEDEC
Solder Ball Shear    SBS   C5     MCM         B     from a min. of          3          CPK >1.67                        Precondition per JESD22-A113.
                                                                                                       JESD22-B117
                                  Solder               10 MCM
                                   Balls
                                 Apply to
                                  MCM               10 leads from                       No lead
                                                                                                          JEDEC         Not required for surface mount MCMs. Only required for
Lead Integrity       LI    C6    Leads /    D, G      each of 5             1         breakage or
                                                                                                       JESD22-B105      through-hole MCM.
                                   Pins                 MCMs                             cracks




                                                                       Page 19 of 38
                                                                                                                   AEC - Q104 - REV-A
                                                                                                                    November 28, 2025
                                          A u t o m o tiv e E le c tr o n ic s C o u n c il
                                                    Component Technical Committee




                                            Table 1: Qualification Test Methods (continued)
                                          TEST GROUP C – PACKAGE ASSEMBLY INTEGRITY TESTS

                             LEVEL TO            SAMPLE SIZE   NUMBER OF   ACCEPT
        STRESS   ABV    #                NOTES                                        TEST METHOD                ADDITIONAL REQUIREMENTS
                               TEST                 / LOT        LOTS      CRITERIA

                                                                                                    Required to document MCM construction.               Not a
                              Apply to            5 MCM for
X-Ray            XRAY   C7                ---                      1           ---        ---       qualification test.
                               MCM                 each lot

                                                                                                    Only required for surface mount MCMs that have
                                                                                                    monolithic construction as included in IPC/JEDEC J-STD-
                                                                                                    020. Perform delamination check after TC. AM with 10
Acoustic                      Apply to            10 MCM for
                 AM     C8                 P                       3           ---        ---       samples per lot. Delamination is not allowed, if it occurs in
Microscopy                     MCM                  each lot
                                                                                                    the area of wire bond interconnects or if it changes the
                                                                                                    thermal behavior of the MCM in a way, that it is out of
                                                                                                    specification.




                                                               Page 20 of 38
                                                                                                                          AEC - Q104 - REV-A
                                                                                                                           November 28, 2025
                                                 A u t o m o tiv e E le c tr o n ic s C o u n c il
                                                           Component Technical Committee


                                                  Table 1: Qualification Test Methods (continued)
                                                   TEST GROUP D – DIE FABRICATION RELIABILITY TESTS

                                    LEVEL TO            SAMPLE SIZE   NUMBER OF   ACCEPT
      STRESS            ABV    #                NOTES                                        TEST METHOD                ADDITIONAL REQUIREMENTS
                                      TEST                 / LOT        LOTS      CRITERIA

                                                                                                           Consult with supplier on its wafer level process
                                     Apply to                                                  JEDEC
Electromigration        EM     D1                ---        ---          ---          ---                  characterization and/or die-level qualification data (test
                                       Die                                                     JEP001
                                                                                                           method, sampling, criteria).
Time Dependent                                                                                             Consult with supplier on its wafer level process
                                     Apply to                                                  JEDEC
Dielectric              TDDB   D2                ---        ---          ---          ---                  characterization and/or die-level qualification data (test
                                       Die                                                     JEP001
Breakdown                                                                                                  method, sampling, criteria).

                                                                                                           Consult with supplier on its wafer level process
                                     Apply to                                                  JEDEC
Hot Carrier Injection   HCI    D3                ---        ---          ---          ---                  characterization and/or die-level qualification data (test
                                       Die                                                     JEP001
                                                                                                           method, sampling, criteria).
                                                                                                           Consult with supplier on its wafer level process
Bias Temperature                     Apply to                                                  JEDEC       characterization and/or die-level qualification data (test
                        BTI    D4                ---        ---          ---          ---
Instability                            Die                                                     JEP001      method, sampling, criteria). Note: Positive bias may be
                                                                                                           applicable as well.
                                                                                                           Consult with supplier on its wafer level process
                                     Apply to                                                  JEDEC
Stress Migration        SM     D5                ---        ---          ---          ---                  characterization and/or die-level qualification data (test
                                       Die                                                     JEP001
                                                                                                           method, sampling, criteria).




                                                                      Page 21 of 38
                                                                                                                                          AEC - Q104 - REV-A
                                                                                                                                           November 28, 2025
                                                A u t o m o tiv e E le c tr o n ic s C o u n c il
                                                            Component Technical Committee


                                                 Table 1: Qualification Test Methods (continued)
                                                      TEST GROUP E – ELECTRICAL VERIFICATION TESTS

                                   LEVEL TO             SAMPLE SIZE   NUMBER OF    ACCEPT
      STRESS           ABV    #                NOTES                                                 TEST METHOD                       ADDITIONAL REQUIREMENTS
                                     TEST                  / LOT        LOTS       CRITERIA

                                                                                                                          Test is performed as specified in the applicable stress
                                                                                                     Test program to      reference and the additional requirements.
Pre- and Post-Stress                Apply to                                                        supplier data sheet
                       TEST   E1               N, G         All          All            0 Fails
Function/Parameter                   MCM                                                                  or user         All electrical tests before and after the qualification
                                                                                                       specification      stresses are performed within the MCM specification and
                                                                                                                          temperature range values.
                                                                                                                          TEST before and after ESD at room and hot temperature.
                                                                                                                          MCM shall be classified according to the maximum
                                                                                     Target:                              withstand voltage level.
                                                                                                         AEC
Electrostatic                                                                       0    Fails
                                    Apply to              See Test                                    Q100-002 or
Discharge Human        HBM    E2                D                         1           1000V                               HBM < 1000V require customer notification.
                                     MCM                   Method                                     ANSI/ ESDA/
Body Model                                                                        (Classification
                                                                                                     JEDEC JS-001
                                                                                   1C or better)
                                                                                                                          Report results per JEP178 in product data sheet or
                                                                                                                          qualification report.
                                                                                                                          TEST before and after ESD at room and hot temperature.
                                                                                                                          MCM shall be classified according to the maximum
                                                                                                                          withstand Test Condition voltage level.
                                                                                     Target:
                                                                                                                          CDM < Test Condition 250 requires customer notification.
                                                                                      0 Fails            AEC
Electrostatic
                                    Apply to              See Test                Test Condition      Q100-011 or
Discharge Charged      CDM    E3                D                         1                                               Report results per JEP178 in product data sheet or
                                     MCM                   Method                      250            ANSI/ESDA/
Device Model                                                                                                              qualification report.
                                                                                  (Classification    JEDEC JS-002
                                                                                   C1 or better)
                                                                                                                          * Note: Test condition refers to the tester plate voltage that
                                                                                                                          meets the waveform parameter requirements per AEC
                                                                                                                          Q100-011D and ANSI/ESDA/JEDEC JS-002 to make
                                                                                                                          different CDM tester hardware comparable.




                                                                      Page 22 of 38
                                                                                                                                AEC - Q104 - REV-A
                                                                                                                                 November 28, 2025
                                                A u t o m o tiv e E le c tr o n ic s C o u n c il
                                                          Component Technical Committee


                                                 Table 1: Qualification Test Methods (continued)
                                            TEST GROUP E – ELECTRICAL VERIFICATION TESTS (CONTINUED)

                                LEVEL TO               SAMPLE SIZE   NUMBER OF   ACCEPT
      STRESS       ABV     #                   NOTES                                           TEST METHOD                   ADDITIONAL REQUIREMENTS
                                  TEST                    / LOT        LOTS      CRITERIA

                                 Apply to                                                          AEC           TEST before and after LU at room and hot temperature.
                                                         See Test
Latch-Up            LU    E4      Active        D                        1         0 Fails       Q100-004        See JESD78 applicability for pins to be Latch-up tested at
                                                          Method
                                 Devices                                                         JESD78          device level.

                                 Apply to                                          Where           AEC           Supplier and user to mutually agree upon electrical
Electrical
                    ED    E5      MCM           D          30            3       applicable,     Q100-009        parameters to be measured and accept criteria. TEST at
Distributions
                                 Function                                        CPK >1.67       AEC Q003        room, hot, and cold temperature.
                                                                                 AEC Q100-
                                 Apply to                                                                        For production testing, see Q100-007 for test
                                                                                 007 unless        AEC
Fault Grading       FG    E6      MCM           ---        ---          ---                                      requirements. In a controller-managed MCM, FG of the
                                                                                  otherwise      Q100-007
                                 Function                                                                        controller covers the MCM.
                                                                                  specified
                                 Apply to
                                                                                                                 Characterization over MCM data sheet voltage               /
Characterization   CHAR   E7      MCM           ---        ---          ---          ---         AEC Q003
                                                                                                                 temperatures for critical performance parameters.
                                 Function

                                 Apply to                                                      SAE J1752/3 –     This test and its accept criteria are per agreement between
Electromagnetic
                   EMC    E8      MCM           ---         1            1           ---         Radiated        user and supplier on a case-by-case basis. See AEC-
Compatibility
                                 Function                                                        Emissions       Q100 Appendix 5 for details.

                                                                                                                 Applicable to MCM with SRAM and or/ DRAM based
                                                                                                                 memory sizes  1 Mbits. Either test option (un-
                                  Apply to                                                         JEDEC         accelerated or accelerated) can be performed, in
                                MCM or can                                                     Un-accelerated:   accordance to the referenced specifications.            For
                                     be                                                          JESD89-1        controller-managed MCMs, the MCM fail rate can be
Soft Error Rate    SER    E9    extrapolated   D, G         3            1           ---             or          determined from sub-component data (un-accelerated or
                                 from sub-                                                      Accelerated:     accelerated) taking into account the ability of the
                                component                                                       JESD89-2 &       firmware/controller to mask failures. This test and accept
                                    data                                                         JESD89-3        criteria are per agreement between user and supplier on a
                                                                                                                 case-by-case basis. Final test report shall include detailed
                                                                                                                 test facility location and altitude data.

                                 Apply to                See Test     See Test    See Test
Lead (Pb) Free      LF    E10                    L                                               AEC-Q005        Applicable to ALL Pb-Free MCM.
                                  MCM                     Method       Method      Method




                                                                     Page 23 of 38
                                                                                                                              AEC - Q104 - REV-A
                                                                                                                               November 28, 2025
                                                    A u t o m o tiv e E le c tr o n ic s C o u n c il
                                                                Component Technical Committee


                                                     Table 1: Qualification Test Methods (continued)
                                                             TEST GROUP F – DEFECT SCREENING TESTS

                                    LEVEL TO                 SAMPLE SIZE   NUMBER OF   ACCEPT
      STRESS            ABV    #                  NOTES                                           TEST METHOD               ADDITIONAL REQUIREMENTS
                                      TEST                      / LOT        LOTS      CRITERIA

                                      Apply to
                                     Individual
Part Average                            Sub-
                        PAT    F1                   ---          ---          ---          ---     AEC Q001
Testing                             components
                                      or MCM                                                                    These tests are intended for MCMs in production.
                                      Function
                                      Apply to                                                                  The supplier must perform some variant of PAT and SBA
                                     Individual                                                                 that meets the intent of the guideline.
Statistical Bin/Yield                   Sub-
                        SBA    F2                   ---          ---          ---          ---     AEC Q002
Analysis                            components
                                      or MCM
                                      Function
                                                          TEST GROUP G – CAVITY MODULE INTEGRITY TESTS

                                    LEVEL TO                 SAMPLE SIZE   NUMBER OF   ACCEPT
      STRESS            ABV    #                  NOTES                                           TEST METHOD               ADDITIONAL REQUIREMENTS
                                      TEST                      / LOT        LOTS      CRITERIA

                                                                                                                Y1 plane only, 5 pulses, 0.5 msec duration, and 1500 g
                                     Apply to                                                        JEDEC
Mechanical Shock        MS     G1                 H, D, G        15            1        0 Fails                 peak acceleration. TEST before and after at room
                                      MCM                                                         JESD22-B110
                                                                                                                temperature.

                                                                                                                20 Hz to 2 KHz to 20 Hz (logarithmic variation) in >4
Variable Frequency                   Apply to                                                        JEDEC
                        VFV    G2                 H, D, G        15            1        0 Fails                 minutes, 4X in each orientation, 50 g peak acceleration.
Vibration                             MCM                                                         JESD22-B103
                                                                                                                TEST before and after at room temperature.

                                                                                                                Y1 plane only, 30 K g-force for <40 pin packages, 20 K g-
Constant                             Apply to                                                     MIL-STD-883
                         CA    G3                 H, D, G        15            1        0 Fails                 force for 40 pins and greater. TEST before and after at
Acceleration                          MCM                                                         Method 2001
                                                                                                                room temperature.
                                                                                                                Any single-specified fine test followed by any single-
                                     Apply to                                                     MIL-STD-883
Gross/Fine Leak         GFL    G4                 H, D, G        15            1        0 Fails                 specified gross test. For hermetic sealed packaged cavity
                                      MCM                                                         Method 1014
                                                                                                                MCMs only.
                                                                                                                A MCM shall be defined as a failure if hermeticity
                                                                                                                requirements cannot be demonstrated.          Mechanical
Mechanical Shock                                                                                                damage, such as cracking, chipping or breaking of the
                                     Apply to                                                        JEDEC
Cavity Device           DROP   G5                 H, D, G         5            1        0 Fails                 package will also be considered a failure provided such
                                      MCM                                                         JESD22-B110
Drop                                                                                                            damage was not caused by fixturing or handling and the
                                                                                                                damage is critical to MCM performance in the specific
                                                                                                                application.
                                     Apply to                                                     MIL-STD-883
Lid Torque               LT    G6                 H, D, G         5            1        0 Fails                 For ceramic packaged cavity MCMs.
                                      MCM                                                         Method 2024

                                                                           Page 24 of 38
                                                                                                                             AEC - Q104 - REV-A
                                                                                                                              November 28, 2025
                                                 A u t o m o tiv e E le c tr o n ic s C o u n c il
                                                             Component Technical Committee


                                                  Table 1: Qualification Test Methods (continued)
                                              TEST GROUP G – CAVITY MODULE INTEGRITY TESTS (CONTINUED)

                                  LEVEL TO                 SAMPLE SIZE   NUMBER OF   ACCEPT
      STRESS           ABV   #                   NOTES                                             TEST METHOD               ADDITIONAL REQUIREMENTS
                                    TEST                      / LOT        LOTS      CRITERIA

                                                                                                   MIL-STD-883
Die Shear              DS    G7   Apply to Die   H, D, G        5            1           0 Fails                 To be performed before cap/seal for all cavity MCMs.
                                                                                                   Method 2019
                                   Apply to                                                        MIL-STD-883
Internal Water Vapor   IWV   G8                  H, D, G        5            1           0 Fails                 For hermetically sealed packaged cavity MCMs only.
                                    MCM                                                            Method 1018




                                                                         Page 25 of 38
                                                                                                                                   AEC - Q104 - REV-A
                                                                                                                                    November 28, 2025
                                          A u t o m o tiv e E le c tr o n ic s C o u n c il
                                                       Component Technical Committee


                                           Table 1: Qualification Test Methods (continued)

                                                     TEST GROUP H –MODULE SPECIFIC TESTS

                              LEVEL TO               SAMPLE SIZE      NUMBER OF    ACCEPT
     STRESS       ABV    #                NOTES                                                     TEST METHOD                    ADDITIONAL REQUIREMENTS
                                TEST                    / LOT           LOTS       CRITERIA

                                                                                                                       Temperature cycling test, state the used IPC-9701 test
                                                                                                       IPC-9701        condition. Note: the TC cycle condition used needs to
                                                                                                                       align with the MCM expected use condition (e.g., an
                                                     Per IPC-9701                                                      under the hood use may dictate a TC3 or TC4). Likewise
                                                       accepted                                      Chose the TC
                                                                                                     level and NTC     the number of thermal cycles (NTC) needs to align with
                                                                                  Report initial                       the intended use environment. The ramp rate, dwell time,
                                                          Or                       failure and        requirements
Board Level
                  BLR    H1
                               Apply to
                                           D, G                           1       50% failure      based on intended   and test duration defined per IPC-9701. The MCM may
Reliability                     MCM                                                                 use environment    be used in lieu of the IPC-9701 daisy chain requirement if
                                                     Per AEC-Q007                  cycles per
                                                     recommended                    IPC-9701                           the MCM corner solder attachments and a representable
                                                                                                          Or           sample outer rows and solder attachments under or near
                                                                                                                       major die locations can be electrically measured.

                                                                                                      AEC-Q007         AEC-Q007-001 defines test method criteria

                                                          Per
                                                     Q100/Q101/Q200                                                    1000 hours at minimum ambient storage temperature.
Low Temperature                Apply to   H, P, B,                                                     JEDEC
                  LTSL   H2                          minimum 30/lot       1           0 Fails
Storage Life                    MCM       D, G, K                                                   JESD22-A119        Test after LTSL at the MCM data sheet (low, high and room
                                                      or negotiated                                                    temperature) temperatures.
                                                     with Customer




                                                                      Page 26 of 38
                                                                                                                       AEC - Q104 - REV-A
                                                                                                                        November 28, 2025
                                            A u t o m o tiv e E le c tr o n ic s C o u n c il
                                                      Component Technical Committee


                                                    TEST GROUP H –MODULE SPECIFIC TESTS
                                LEVEL TO            SAMPLE SIZE   NUMBER OF   ACCEPT
STRESS              ABV    #                NOTES                                           TEST METHOD    ADDITIONAL REQUIREMENTS
                                  TEST                 / LOT        LOTS      CRITERIA
                                                                                                           Start up and Temperature Steps tests are combined in this
                                                                                                           test.

                                                                                                           Startup occurs first. The module is cooled down
                                                                                                           unpowered and stabilized at the lowest operating
                                                                                                           temperature and then turned on to check for any issue with
                                                                                                           functionality or performance. This process is repeated at
                                                                                                           the maximum rated operating temperature.
                                                                                                           The Temperature Steps portion of this test starts at room
                                                                                                           temperature and the device is then turned on. The
                                                                                                           temperature is decreased and the functionality is checked
                                                                                                           at 10°C increments until the minimum operating
                                                                                                           temperature is reached (Note: the final decrease may be
                                                                                                           less than 10°C such as 5°C). Then the temperature is
                                                                                                           increased in 10°C increments until the maximum operating
                                                                                                           temperature is reached. Confirm functionality at each step
                                                                                                           within the device specified operating range.
Start Up and                     Apply to
                    STEP   H3                ---      5 MCMs          1           0 Fails    ISO 16750-4
Temperature Steps                 MCM




                                                                  Page 27 of 38
                                                                                                                                   AEC - Q104 - REV-A
                                                                                                                                    November 28, 2025
                                                   A u t o m o tiv e E le c tr o n ic s C o u n c il
                                                             Component Technical Committee


                                                    TEST GROUP H –MODULE SPECIFIC TESTS (CONTINUED)

                                    LEVEL TO               SAMPLE SIZE   NUMBER OF    ACCEPT
        STRESS         ABV     #                   NOTES                                              TEST METHOD                 ADDITIONAL REQUIREMENTS
                                      TEST                    / LOT        LOTS       CRITERIA

                                                                                                                        Note: Select H4A or H4B based on construction of the
                                                                                                                         MCM. H4A applies to MCM assemblies which have
                                                                                                                       exposed subcomponents solder joints and/or wire bonds
                                     Apply to
                                     MCM –                                                            JEDEC JESD22-     Condition A (500G, 1.0 ms half-sine pulse) as listed in
                              H4A                  D, G      6 MCMs          1           0 Fails
                                    Component                                                             B110                            JESD22-B110B
                                    Level Test
                                                                                                                           Each MCM sample: 5 drops per ±X, ±Y & ±Z (30
                                                                                                                                        total/sample).
MCM Drop Test          MCM
                       DROP                                                                                           Note: Select H4A or H4B based on construction of the
                                                                                                                      MCM.H4B applies to encapsulated (over molded)
                                                                                                                      surface mounted electronic components without exposed
                                     Apply to
                                                                                                                      solder joints and/or wire bonds.
                                    MCM – Test
                                                                                     Report initial
                                    Vehicle with                                                      JEDEC JESD22-
                              H4B                  D, G     24 MCMs          1        and 62.3%                       Condition B (1500 G, 0.5 ms half-sine pulse) as listed in
                                      multiple                                                            B111
                                                                                     failure cycles                   JESD22-B110, in the -z direction
                                    Daisy-Chain
                                      MCM1
                                                                                                                      Minimum of 10 and up to 100 drops per test vehicle.
                                                                                                                      Characteristic life reported for MCM.

Destructive Physical                  Apply to                                                                        After MCM thermal cycling exposure, check key risks
                       DPA    H5                   D, G      5 MCMs          1             ---        MIL-STD-1580
Analysis                               MCM                                                                            based on the MCM DFMEA and PFMEA.
                                      Apply to              5 MCM for                                                 X-ray test not required if X-ray test is done in Test
X-ray                  XRAY   H6                    ---                      ---           ---             ---
                                       MCM                   each lot                                                 Group C. See Test Group C X-ray (XRAY) for details.
                                                                                                                      Acoustic Microscopy test not required if Acoustic
Acoustic                              Apply to              10 MCM for
                       AM     H7                    P, G                     ---           ---             ---        Microscopy test is done in Test Group C. See Test
Microscopy                             MCM                    each lot
                                                                                                                      Group C Acoustic Microscopy (AM) for details.




                                                                         Page 28 of 38
                                                                                                                                               AEC - Q104 - REV-A
                                                                                                                                                November 28, 2025

                           A u t o m o tiv e E le c tr o n ic s C o u n c il
                                         Component Technical Committee




                                                                          Legend for Table 1
Notes:   H   Required for hermetic packaged MCMs only.
         P   Required for plastic packaged MCMs only.
         B   Required Solder Ball Surface Mount Packaged (BGA) MCMs only.
         N   Nondestructive test, MCMs can be used to populate other tests or they can be used for production.
         D   Destructive test, MCMs are not to be reused for qualification or production.
         S   Required for surface mount plastic packaged MCMs only.
         G   Generic data allowed.
         K   Use method AEC-Q100-005 for preconditioning a stand-alone Non-Volatile Memory integrated circuit or an integrated circuit with a Non-Volatile Memory MCM.
         L   Required for Pb-Free MCMs only.
         M   Table 1 is applicable to MCMs that also have unique test requirements from a different AEC or product specification.
             An example is Photoelectric currents from LED Radiation and Reaction with outgassing materials.




                                                                               Page 29 of 38
                                                                                                                                                                                                                                    AEC - Q104 - REV-A
                                                                                                                                                                                                                                     November 28, 2025

                              A u t o m o tiv e E le c tr o n ic s C o u n c il
                                            Component Technical Committee


                                          Table 2: Process Change Qualification Guidelines for the Selection of Tests
 A2      Temperature Humidity Bias or HAST        C4           Physical Dimensions                                                    E8                Electromagnetic Compatibility                                           G8              Internal Water Vapor
 A3      Autoclave or Unbiased HAST               C5           Solder Ball Shear                                                      E9                Soft Error Rate                                                         H1              Board Level Reliability
 A4      Temperature Cycling                      C6           Lead Integrity                                                         E10               Lead (Pb) Free                                                          H2              Low Temperature Storage Life
 A5      Power Temperature Cycling                C7           X-ray / CSAM                                                           G1                Mechanical Shock                                                        H3              Start Up and Temperature Steps
 A6      High Temperature Storage Life            D1-5         Die Fabrication Reliability Tests                                      G2                Variable Frequency Vibration                                            H4              MCM Drop Test
 B1      High Temperature Operating Life          E2           Human Body Model ESD                                                   G3                Constant Acceleration                                                   H5              Destructive Physical Analysis
 B2      Early Life Failure Rate                  E3           Charged Device Model ESD                                               G4                Gross/Fine Leak                                                         H6              X-ray
 B3      NVM Endurance, Data Retention            E4           Latch-up                                                                                 Mechanical Shock Cavity Device                                          H7              Acoustic Microscopy
                                                                                                                                      G5
 C1      Wire Bond Shear                          E5           Electrical Distribution                                                                  Drop
 C2      Wire Bond Pull                           E6           Fault Grading                                                          G6                Lid Torque
 C3      Solderability                            E7           Characterization                                                       G7                Die Shear


Note: A letter or "⚫" indicates that performance of that stress test should be considered for the appropriate process change. Reason for not performing a considered test should be given
in the qualification plan or results.


                                         Test #                      A5A/B                                                                 C7-8        D1-5                                                 E10   G1-3                                                         H4A/B            H6/H7
                                                    A2    A3    A4             A6     B1     B2     B3    C1    C2    C3   C4   C5    C6                      E2    E3    E4   E5   E6   E7     E8    E9                      G4    G5     G6   G7   G8    H1    H2     H3                H5




                                                                     PTC/PCT                                                               XRAY/CSAM                                                              MS/VFV/GA                                                    MCM DROP         XRAY/AM
                           Test Abbreviation        THB   AC    TC             HTSL   HTOL   ELFR   EDR   WBS   WBP   SD   PD   SBS                    DFRT   HBM   CDM   LU   ED   FG   CHAR   EMC   SER                     GFL   DROP        DS   IWV   BLR   LTSL   STEP              DPA
                                                                                                                                      LI                                                                    LF                             LT



 Change Type                 Change Impact
                             Including critical
                             characteristics of
 Any                                             ⚫ ⚫ ⚫ ⚫ ⚫ ⚫ ⚫ ⚫ D D ⚫ ⚫ ⚫ ⚫ ⚫ F ⚫ ⚫ ⚫ H ⚫ H ⚫ K ⚫ ⚫ ⚫ ⚫ ⚫ L ⚫ ⚫ ⚫ ⚫ ⚫ ⚫ ⚫
                             subcomponent(s) are
                             affected (Note 1)
 Substrate materials
 change and/ or external
                             Any                    ⚫ ⚫ ⚫ ⚫ ⚫ ⚫ ⚫ ⚫ D D ⚫ ⚫ ⚫ ⚫ ⚫ F ⚫ ⚫ ⚫ H ⚫ H ⚫ K ⚫ ⚫ ⚫ ⚫ ⚫ L ⚫ ⚫ ⚫ ⚫ ⚫ ⚫ ⚫
 dimensions

 Substrate change
 affecting module
 schematic
                          Any                       ⚫ ⚫ ⚫ A                           ⚫ ⚫                 D D                                                 ⚫ ⚫ ⚫ H ⚫ H ⚫ K                                                                    L                                        ⚫
 (changes to the internal
 dimensions and/or
 schematics)
 Change that adds or
 subtracts sub-components Any                       ⚫ ⚫ ⚫ A ⚫ ⚫ ⚫                                                                                      G ⚫ ⚫ ⚫ H ⚫ H ⚫ K                                           ⚫                             L                      ⚫
 from the module BOM


                                                                                                            Page 30 of 38
                                                                                                                                                                                                                                           AEC - Q104 - REV-A
                                                                                                                                                                                                                                            November 28, 2025
                                                          A u t o m o tiv e E le c tr o n ic s C o u n c il
                                                                              Component Technical Committee



                                              Test #                       A5A/B                                                                 C7-8        D1-5                                                  E10   G1-3                                                         H4A/B            H6/H7
                                                           A2    A3   A4             A6     B1     B2     B3    C1    C2    C3   C4   C5    C6                      E2    E3    E4   E5    E6   E7     E8    E9                      G4    G5     G6   G7   G8    H1    H2     H3                H5




                                                                           PTC/PCT                                                               XRAY/CSAM                                                               MS/VFV/GA                                                    MCM DROP         XRAY/AM
                           Test Abbreviation               THB   AC   TC             HTSL   HTOL   ELFR   EDR   WBS   WBP   SD   PD   SBS                    DFRT   HBM   CDM   LU   ED    FG   CHAR   EMC   SER                     GFL   DROP        DS   IWV   BLR   LTSL   STEP              DPA
                                                                                                                                            LI                                                                     LF                             LT



 Change Type                     Change Impact
 Change to the processes
 used in during module
 assembly (pick & place,
                                 Influencing the
 reflow, encapsulation,
                                 integrity of the final    ⚫          ⚫ A                   B                   D D              ⚫ ⚫             ⚫                                   H,I        H                                                                                                ⚫
 singulation, etc.), including
                                 product
 new equipment/tool which
 uses a different basic
 technology
 Change to testing platform
                                 Any                                                                                                                                                 H H H
 and/or coverage
 Change to testing location      Any                                                                                                                                                 J
 Change to assembly
                                 Any                       ⚫ ⚫ ⚫ A                          ⚫ ⚫                 D D ⚫ ⚫ ⚫ ⚫                                                          H,J        J                  ⚫ ⚫ ⚫ ⚫ ⚫ L ⚫ M ⚫ ⚫ ⚫ ⚫ ⚫
 location
 Change to materials used
 in module assembly (e.g.,
 adhesive, underfill,            Any                       ⚫          ⚫ A ⚫ C C                                 D D ⚫ ⚫ ⚫ ⚫                                                          J                       K ⚫ ⚫ ⚫ ⚫ ⚫ L ⚫ ⚫ ⚫ ⚫ ⚫ ⚫ ⚫
 encapsulant, solder,
 epoxy)
 Change from a Non-AEC
 or an AEC Qualified sub-
                                 Any                       ⚫ ⚫ ⚫ ⚫ ⚫ ⚫ ⚫ ⚫                                                                                   ⚫ ⚫ ⚫ ⚫ H ⚫ H ⚫ K                                            ⚫ ⚫ ⚫                        D                                         N N
 component to a Non-AEC
 Qualified sub-component
 Change from a Non-AEC
 or an AEC Qualified sub-
 component to an(other)          Any                                                        ⚫             ⚫                                                         ⚫ ⚫ ⚫ H ⚫ H ⚫ K                                       ⚫ ⚫ ⚫                        D                                         N N
 AEC Qualified sub-
 component
 Change within an AEC
 Qualified sub-component         Any                                                        ⚫             ⚫                                                         ⚫ ⚫ ⚫ H ⚫ H ⚫ K                                       ⚫                            D
 that has been requalified
 Change of product
 marking process (ink                                                                                                       E
 marking only)

Note 1: Critical characteristics are those which have the greatest effect on form, fit, function, yield, and/or reliability. Use of SPC controls and 100% testing are common.

                                                                                                                  Page 31 of 37
                                                                                                                                       AEC - Q104 - REV-A
                                                                                                                                        November 28, 2025
                                                  A u t o m o tiv e E le c tr o n ic s C o u n c il
                                                                Component Technical Committee


Legend:
 A   For devices requiring PTC (requirement in Q100)
 B   Die preparation and/or die clean
 C Only applicable to materials that impact electrical reliability performance (e.g., Electromigration)
 D Only applies to a subcomponent which is wire bonded during MCM assembly
 E   For symbol rework, new cure time, temp
 F   Per AEC-Q100 change Table, if applicable to the subcomponent under consideration
 G In case of adding a non-AEC Qualified subcomponent
 H Delta analysis on key parameters
 I   Processes for material in direct contact with die surfaces
 J   Correlation between new and old
 K   Applicable for subcomponents with > 1M SRAM or DRAM per AEC-Q100
 L   Only applies to subcomponent which is die attached during MCM assembly (flip chips are exempted)
     For MCMs with exterior (outside surface) solder-joints, generic board-level reliability data comparing the existing an proposed
 M assembly sites must be available as an option
 N Applicable to a changed component only




                                                                                    Page 32 of 37
                                                                                    AEC - Q104 - REV-A
                                                                                     November 28, 2025


 A u t o m o tiv e E le c tr o n ic s C o u n c il
            Component Technical Committee


                     Appendix 1: MCM Early Life Failure Rate (ELFR)


A1.1   SCOPE

       This test method is applicable to Multichip Modules (MCM) qualifications. In the case of many MCMs,
       generic data (see AEC-Q104, Section 2.4 may fulfill the requirements of this test method. If the supplier is
       qualifying a MCM for which no generic data is available (unproven technology or design rules) for general
       use, then the requirements of this test method should be utilized to meet the requirements of AEC-Q104.
       If the supplier is qualifying a MCM for a single user, that user may optionally designate the implementation
       of AEC-Q001 as a substitute for ELFR. All parts used for such a qualification must have been evaluated
       to AEC-Q001 tests and limits approved by the user. If AEC-Q001 is utilized, the user shall review and
       approve of the particular tests and the method used to determine test limits. (Note: The failures from ELFR
       and AEC-Q001 do not always show a 1:1 correlation.)

A1.1.1 Description

       This MCM Early Life Failure Rate (ELFR) establishes the testing method for evaluation of early life failure
       characteristics on MCMs that are utilizing new or unproven processing technology or design rules where
       generic data is not available. This would include MCMs for which there is no prior usage information or
       generic data. Unsatisfactory results in this evaluation indicate that corrective action is required and the
       MCMs may require processing changes, design changes, burn-in, more aggressive burn-in, or application
       of statistical part test limits (see AEC-Q001).

A1.1.2 Reference Documents

       AEC-Q001 Guidelines for Part Average Testing
       JEDEC JESD22-A108 Temperature, Bias, and Operating Life

A1.2   PROCEDURE

A1.2.1 Sample Size

       The sample size shall be per Table 1 of AEC-Q104. In the case of MCMs that are deemed too expensive,
       the requirement for use of this test method and the sample size will be based upon agreement between the
       user and supplier.

A1.2.2 General ELFR Procedure

       The MCM shall be tested per the High-Temperature Operating Life (HTOL) requirements in JEDEC
       JESD22-A108 with the following special condition. The ambient test temperature shall be per the applicable
       operating temperature grade as defined in AEC-Q104 Section 1.3.6 for 48 hours.

A1.2.3 Acceptance Criteria

       The MCM shall be functionally tested within 48 hours after completion of high temperature exposure.
       Testing shall be at room temperature. Failures during this test are not acceptable and indicate that
       corrective action must be taken. The supplier shall notify all interested users of this non-conforming
       condition and the corrective action that has / will take place. The user(s) must approve of the corrective
       action for the MCM to be qualified.

A1.2.4 Sample Disposition

                                                Page 33 of 38
                                                                               AEC - Q104 - REV-A
                                                                                November 28, 2025
A u t o m o tiv e E le c tr o n ic s C o u n c il
         Component Technical Committee



   MCMs that pass electrical testing after this test can be used to populate other non-operating tests. These
   MCMs can also be supplied as production material if agreed to by the user.




                                           Page 34 of 37
                                                                                      AEC - Q104 - REV-A
                                                                                       November 28, 2025
   A u t o m o tiv e E le c tr o n ic s C o u n c il
              Component Technical Committee



                                  Appendix 2: Power Cycling Test (A5B)

A2.1   SCOPE

       This test method is applicable to Multichip Modules (MCM) qualifications. Due to the complexity of MCMs
       and the possibility for non-uniform temperatures across the MCM due to power states of the individual sub-
       components within the MCM, AEC-Q104 has the additional option of running Power Cycling Test (PCT)
       that component qualifications do not.

       This test can be performed as an alternative to Power Temperature Cycling (A5A). Power Cycling Test
       decouples the power cycling stress from temperature cycling. Although this test can be used for power
       devices, the benefit is in stressing non-power devices in power cycling from a minimum self-heating state,
       such as standby, to a maximum self-heating active state.

       Power Cycling Test is required if:

       1)      thermal management structure/materials are used for deliberate heat transfer from a
               subcomponent within the MCM to the housing of the MCM or the MCM datasheet
               requires/recommends heat transfer management;

       2)      the MCM is a “power MCM” - meant to regulate (not only sense) voltage/current, directly drive
               current (load), or purposefully control current;
                        or
       3)      maximum power dissipation results in internal heating (ΔTj) of subcomponent or module of >40 °C
               (determined from thermal model or empirically)

       4)      and Power Temperature Cycling was not performed.



A2.1.1 Description

       Power Cycling Test is the testing method to evaluate the stresses resulting from non-uniform temperature
       gradients within the MCM during power cycles. Possible failure mechanisms that can be observed from
       this test include, but are not limited to, internal interconnect faults, internal PCB faults, sub-component die
       or package crack, etc.

       The test method uses a powered device which is cycled between minimum and maximum power cycles
       intended to emulate the range of usage conditions of the device while maximizing thermal impact from the
       change in power state. Each power cycle starts at a low or negligible self-heating power state (such as off,
       low power mode, standby, etc) from which the MCM can quickly reach the maximum self-heating power
       state (such as on, active, maximum performance, etc) and then is powered to a maximum self-heating
       power state before returning to the low self-heating power state.

       Power Cycling Test is a new test introduced in AEC-Q104 and, as such, may be subject to future updates.

A2.1.2 Reference Documents

       JEDEC JESD22-A122 Power Cycling

       The reference document shall be used for the test method of Constant Heat Removal/Cooling with Variable
       Power with adjustments to the power cycling specifics as per AEC-Q104.

                                                 Page 35 of 37
                                                                                    AEC - Q104 - REV-A
                                                                                     November 28, 2025
   A u t o m o tiv e E le c tr o n ic s C o u n c il
              Component Technical Committee




A2.2   PROCEDURE

A2.2.1 Sample Size

       The sample size shall be per Table 1 of AEC-Q104. In the case of MCMs that are deemed too expensive,
       the requirement for use of this test method and the sample size will be based upon agreement between the
       user and supplier.

A2.2.2 General Procedure

       The test procedure uses constant temperature and variable power.

       The ambient test temperature(s) used shall be defined in AEC-Q104 Table 1 and is(are) to remain constant
       during testing. Thermal shut-down shall be avoided. If the ambient test temperature results in a
       Tcycle(max) beyond the maximum datasheet specification, the test temperature shall be lowered to the
       highest temperature that does not result in thermal shut-down and the test temperature shall be reported.
       Power cycle between the minimum self-heating state Tcycle(min) and maximum self-heating state
       Tcycle(max) for 7500 cycles at each specified ambient temperature. Cycle count is aligned with the highest
       AEC-Q101 power cycling count of 15,000 total cycles of quick and large temperature swings between on
       and off conditions.

       The dwell time at each power state can be determined empirically from the characterization of temperature
       saturation for the MCM after switching to the power state. Note that the dwell time may be different for the
       minimum/negligible self-heating power state and the maximum self-heating power state. Dwell time may
       also be dependent on ambient temperature. The dwell time shall be set to the time it takes for the MCM to
       reach –5 °C to +10 °C of Tcycle(max) for the upper end of the cycle and +5 °C to –10 °C of Tcycle(min)
       for the lower end of the cycle. Refer to figure A.1 in JESD22-A122.

       An example MCM cycle could be 1 minute at minimum self-heating state Tcycle(min) and 1 minute at
       maximum self-heating state for a total of 2 minutes per cycle. This equates to 500 hours to complete the
       stress.

       Tcycle(max) Interim read points or continuous monitoring are preferred but not required.

A2.2.3 Acceptance Criteria

       For Power Cycling Test (PCT), the MCM shall be functionally tested at cold and hot temperature, in order
       to observe failures related to CTE mismatch.

       Report all failures and their failure mechanisms.

       Note that the readout temperatures are different from the Power Temperature Cycling (PTC) readout
       temperatures. PTC evolved from AEC-Q101 where it started with room temperature readout only and then
       added hot temperature readout upon being incorporated into AEC-Q100.




                                                 Page 36 of 37
                                                                          AEC - Q104 - REV-A
                                                                           November 28, 2025
A u t o m o tiv e E le c tr o n ic s C o u n c il
          Component Technical Committee


                                  Revision History


  Rev #      Date of change   Brief summary listing affected sections

    -        Sept. 14, 2017   Initial Release.

   A         Nov. 28, 2025    Updates include the following:
                              Scope added AEC-Q102 in scope, cross references, applicability. Added
                              AEC-Q102, AEC-Q103-002, and AEC-Q103-003 references.

                              AEC-Q104 Applicability Updated and Figure 2

                              Updated Definition of Generic Data to include AEC-Q102 and AEC-Q103X
                              requirements

                              Updated Test Flow figure 4 consistent with Table 1 Test Methods

                              Test Methods Table 1 Updates
                                Added note M
                                High Temperature Storage (HTSL) stress at maximum storage
                                temperature
                                Power Cycling Test (PCT) PTC option for Power Temperature Cycling
                                (PTC)
                                TC – past TC stress test WBP and WBS criteria clarified
                                WBP and WBS post TC stress test criteria clarified
                                NBTI changes to BTI
                                Latch-up sample size defined by test method document
                                HBM ESD and CDM ESD criteria consistent with AEC-Q100
                                MCM Drop Test details clarified
                                STEP test pictorial added
                                Low Temperature Storage (LTSL) stress at minimum storage
                                temperature
                                Board Level Reliability(BLR) add AEC-Q007 test method alternative

                              Updated Table 2: Process Change Qualification Guidelines for the
                              Selection of Tests

                              Removed prior Appendix 1 CDCQ reference

                              Added Appendix 2 Power Cycling Test (A5B)




                                         Page 37 of 37
