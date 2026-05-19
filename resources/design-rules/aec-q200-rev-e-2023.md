                                     AEC - Q200 - Rev E
                                        March 20, 2023




             STRESS TEST
          QUALIFICATION FOR
         PASSIVE COMPONENTS




Automotive Electronics Council
     Component Technical Committee
                                                                                                                        AEC - Q200 - Rev E
                                                                                                                           March 20, 2023

 Automotive Electronics Council
                  Component Technical Committee

                                                            TABLE OF CONTENTS
 1.      SCOPE .................................................................................................................................................. 1
      1.1. Description ...................................................................................................................................... 1
      1.2. Purpose ........................................................................................................................................... 1
      1.3. Reference Documents ..................................................................................................................... 1
      1.4. Abbreviations .................................................................................................................................. 2
      1.5. Definitions ....................................................................................................................................... 2
            1.5.1. AEC-Q200 Qualification ......................................................................................................... 2
            1.5.2. AEC Certification .................................................................................................................... 2
            1.5.3. Temperature Ranges .............................................................................................................. 2
            1.5.4. Approval for Use in an Application........................................................................................ 3
            1.5.5. Most Sensitive Component .................................................................................................... 3
            1.5.6. Generic Data ........................................................................................................................... 3
 2.      GENERAL REQUIREMENTS ................................................................................................................ 3
       2.1. Objective.......................................................................................................................................... 3
       2.2. Precedence of Requirements .......................................................................................................... 3
       2.3. Use of Generic Data......................................................................................................................... 3
       2.4. Test Samples ................................................................................................................................... 4
            2.4.1. Lot Requirements ................................................................................................................... 4
            2.4.2. Production Requirements ...................................................................................................... 4
            2.4.3. Reusability of Test Samples .................................................................................................. 4
            2.4.4. Sample Size Requirements .................................................................................................... 4
            2.4.5. Pre-stress and Post-stress Test Requirements..................................................................... 4
 Figure 1: Pre and Post Stress Test Block Diagram ............................................................................................................... 5
            2.4.6. Test Failure After Stressing ................................................................................................... 5
            2.4.7. Criteria for Passing Qualification........................................................................................... 5
            2.4.8. Alternative Requirements ...................................................................................................... 5
3.    QUALIFICATION AND REQUALIFICATION ............................................................................................. 6
      3.1. Qualification of a New Component ................................................................................................. 6
      3.2. Qualification of Surface Mounted Device (SMD) Components ........................................................................ 6
 Table A: Temperature Grades...................................................................................................................... 6
 Table B: Stress Tests Requiring Reflow Passes..........................................................................................7
 Figure 2: Overall Process for SMD Lead-free Components ................................................................................................. 7
      3.3. Requalification of a Component ..................................................................................................... 7
            3.3.1. Process Change Notification (PCN) ...................................................................................... 7
            3.3.2. Changes Requiring Requalification ....................................................................................... 8
            3.3.3. Changes Requiring Requalification ....................................................................................... 8
            3.3.4. Criteria for Passing Requalification....................................................................................... 8
            3.3.5. User Approval ........................................................................................................................ 8
                                                                                                                                                              AEC - Q200 - Rev E
                                                                                                                                                                 March 20, 2023

 Automotive Electronics Council
                     Component Technical Committee

                                                               TABLE OF CONTENTS (continued)
4.   QUALIFICATION TESTS .......................................................................................................................... 9
     4.1. General Tests................................................................................................................................... 9
     4.2. Data Submission Format................................................................................................................. 9
 Table C: Reflow Passes for High Volume Components............................................................................. 10
 Table D: Qualification Sample Size............................................................................................................. 12
 Table 1: Stress Qualifications for Tantalum (MnO2 and Polymer) and Niobium Capacitors.................... 14
     Table 1A: Tantalum (MnO2 and Polymer) and Niobium Capacitors Process Change Qualification
     Guidelines for the Selection of Tests .................................................................................................... 17
     Table 1B: Tantalum (MnO2 and Polymer) and Niobium Capacitors Acceptance Criteria .................... 18
 Table 2: Stress Qualifications for Ceramic Capacitors............................................................................. 19
     Table 2A: Ceramic Capacitors Process Change Qualification Guidelines for the Selection of Tests 22
     Table 2B-1: Ceramic Capacitors - Class I SMD Acceptance Criteria ................................................... 23
     Table 2B-2: Ceramic Capacitors - Class II/III SMD Acceptance Criteria .............................................. 24
 Table 3: Stress Qualifications for Aluminum Electrolytic (Hybrid, Polymer and Standard) Capacitors . 25
     Table 3A: Aluminum Electrolytic (Hybrid, Polymer and Standard) Capacitors Process Change
     Qualification Guidelines for the Selection of Tests.............................................................................. 29
 Table 4: Stress Qualifications for Film Capacitors ................................................................................... 30
     Table 4A: Film Capacitors Process Change Qualification Guidelines for the Selection of Tests...... 34
 Table 5: Stress Qualifications for Magnetics (Inductors/Transformers) .................................................. 35
     Table 5A: Magnetics (Inductors/Transformers) Process Change Qualification Guidelines for the
     Selection of Tests.................................................................................................................................. 38
 Table 6: Stress Qualifications for Networks (R-C/C/R) ............................................................................. 39
     Table 6A: Networks (R-C/C/R) Process Change Qualification Guidelines for the Selection of Tests 43
 Table 7: Stress Qualifications for Resistors ............................................................................................. 44
     Table 7A: Resistors Process Change Qualification Guidelines for the Selection of Tests................ 48
     Table 7B-1: Acceptance Criteria for Carbon Film THT Fixed Resistors .............................................. 49
     Table 7B-2: Acceptance Criteria for Metal Film THT Fixed Resistors (Includes molded flat lead SMD)
     ............................................................................................................................................................... 50
     Table 7B-3: Acceptance Criteria for Metal Oxide THT Fixed Resistors ............................................... 51
     Table 7B-4: Acceptance Criteria for Wire Wound THT Fixed Resistors (Includes molded flat lead
     SMD) ...................................................................................................................................................... 52
     Table 7B-5: Acceptance Criteria for SMD chip resistors (Does not include molded flat lead SMD, but
     does include coated metal strip) .......................................................................................................... 53
 Table 8: Stress Qualifications for Thermistors (NTC, Platinum, Ceramic PTC) ...................................... 54
     Table 8A: Thermistors (NTC, Platinum, Ceramic PTC) Process Change Qualification Guidelines for
     the Selection of Tests ......................................................................................................................................................................................... 58
                                                                                                                          AEC - Q200 - Rev E
                                                                                                                             March 20, 2023

Automotive Electronics Council
                 Component Technical Committee


                                                 TABLE OF CONTENTS (continued)
Table 9: Stress Qualifications for Trimmer Capacitors/Resistors ............................................................ 59
    Table 9A: Trimmer Capacitors/Resistors Process Change Qualification Guidelines for the Selection
    of Tests ................................................................................................................................................. 63
Table 10: Stress Qualifications for Varistors ............................................................................................ 64
    Table 10A: Varistors Process Change Qualification Guidelines for the Selection of Tests ............... 68
Table 11: Stress Qualifications for Quartz Crystals .................................................................................. 69
    Table 11A: Quartz Crystals Process Change Qualification Guidelines for the Selection of Tests .... 73
Table 12: Stress Qualifications for Ceramic Resonators.......................................................................... 74
    Table 12A: Ceramic Resonators Process Change Qualification Guidelines for the Selection of Tests
    ............................................................................................................................................................... 77
Table 13: Stress Qualifications for Ferrite EMI Suppressors/Filters ........................................................ 78
    Table 13A: Ferrite EMI Suppressors/Filters Process Change Qualification Guidelines for the
    Selection of Tests.................................................................................................................................. 82
Table 14: Stress Qualifications for Polymeric Resettable Fuses ............................................................. 83
    Table 14A: Polymeric Resettable Fuses Process Change Qualification Guidelines for the Selection
    of Tests ................................................................................................................................................. 87
Table 15: Stress Qualifications for Fuses ................................................................................................. 88
    Table 15A: Fuses Process Change Qualification Guidelines for the Selection of Tests .................... 93
Table 16: Stress Qualifications for Super Capacitors ............................................................................... 94
    Table 16A: Super Capacitors Process Change Qualification Guidelines for the Selection of Tests.. 98
APPENDIX 1: Qualification Family ............................................................................................................ 99
APPENDIX 2: Certificate of Design and Construction (CDC).................................................................. 100
APPENDIX 3: Qualification Test Plan Format ......................................................................................... 101
Figure 3: Example of Passive Component Qualification Plan .........................................................................................102
APPENDIX 4: Data Presentation Format and Content ............................................................................ 103
Figure 4: Environmental Test Summary .............................................................................................................................103
Figure 5: Parametric Verification Summary........................................................................................................................104
Revision History....................................................................................................................................... 105
                                                                                 AEC - Q200 - Rev E
                                                                                    March 20, 2023

Automotive Electronics Council
           Component Technical Committee

                                              Acknowledgement


Any Document involving a complex technology brings together experience and skills from many sources. The
Automotive Electronics Council would especially like to recognize the following significant contributors to the
revision of this document:


 AEC Q200 Sub-Committee Members:

 Jenny Du                                        BorgWarner
 Dominick DeMartino                              Bose Corporation
 Joseph Petitti                                  Coilcraft Inc.
 Henning Zander                                  Continental Automotive Technologies GmbH
 Keith Edwards                                   Diodes Inc.
 Steven Sibrel                                   Harman International Group
 Robert Kinyanjui                                John Deere
 Saad Lambaz [Sub-Committee Chair]               Littelfuse Inc.
 Andrea Cantalupi                                Marelli
 Christian Merkel                                Murata Manufacturing Co. Ltd.
 Alex Yanez                                      Murata Manufacturing Co. Ltd.
 Peter Turlo                                     onsemi
 Andrea Wolf                                     Robert Bosch GmbH
 Rolf Nussbaumer                                 Schurter AG
 Michael Cannon                                  TDK Corporation
 Christoph Raible                                TDK Electronics AG
 Ralf Schiffel                                   TDK Electronics AG
 Heinz Strallhofer                               TDK Electronics GmbH & Co OG
 Ildikó Száraz                                   TDK Hungary Components Kft.
 Darin Glenn                                     Vishay Intertechnology, Inc.
 Breno Albuquerque                               Vishay Intertechnology, Inc.
 Andreas Seemayer                                Vishay Electronic GmbH
 LeAnna Weakley                                  Yageo Group
 Alfred Chen                                     Yageo Group
 Larry Dudley                                    ZF




            This document is dedicated in memoriam to:
                     Bob Knoell (1957-2018)
                                                                                 AEC - Q200 - Rev E
                                                                                    March 20, 2023

Automotive Electronics Council
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

Printed in the U.S.A. All rights reserved

Copyright © 2023 by the Sustaining Members of the Automotive Electronics Council. This document may be
freely reprinted with this copyright notice. This document cannot be changed without approval from the AEC
Component Technical Committee.
                                                                                  AEC - Q200 - Rev E
                                                                                     March 20, 2023

Automotive Electronics Council
          Component Technical Committee


                         STRESS TEST QUALIFICATION
                    FOR PASSIVE ELECTRICAL COMPONENTS
Text enhancements and differences made since the last revision of this document are
shown as underlined areas. Several figures and tables have also been revised, but
changes to these areas have not been underlined.

Unless otherwise stated herein, the date of implementation of this standard for new
qualifications and re-qualifications is as of the publish date above.


1.0   SCOPE

1.1   Description

      This specification defines the minimum stress test driven qualification requirements and references test
      conditions for qualification of passive electrical components. This document does not relieve the
      component Supplier of their responsibility to meet their own company's internal qualification program
      or meeting any additional requirements needed by their customers. In this document, "User" is defined
      as all customers using a component qualified per this specification. The User is responsible to confirm
      and validate all qualification and assessment data that substantiates conformance to this document.

      In using this document, the following shall apply:

      •       New qualifications, including additions to a qualified family (as stated in Section 2.3), shall use
              Revision E.
      •       On-going qualifications to Revision D, at the time of release of Revision E, may continue under
              Revision D.
      •       Any changes to an already qualified component (to Revisions A through D) must meet the
              applicable tests (found in Change Tables) of Revision E.
      •       Components qualified to previous Revisions A through D remain qualified.
      •       In all cases, the Supplier must clearly indicate which revision of this document a qualification
              was performed against in all relevant AEC-Q200 data and reports.

1.2   Purpose

      The purpose of this specification is to determine that the component is capable of passing the specified
      tests and thus can be expected to give a certain level of quality/reliability in the application.

1.3   Reference Documents

      The current revision of the referenced documents (shown below) will be in effect at the date of
      agreement to the qualification plan. Subsequent qualification plans will automatically use the latest
      revisions of these referenced documents.

      AEC-Q005                 Pb-Free Test Requirements
      AEC-Q200-001             Flame Retardance Test
      AEC-Q200-002             Human Body Model (HBM) Electrostatic Discharge (ESD) Test
      AEC-Q200-004             Measurement Procedures for Resettable Fuses
      AEC-Q200-005             Board Flex Test
      AEC-Q200-006             Terminal Strength (SMD) / Shear Stress Test
      AEC-Q200-007             Voltage Surge Test
      EIA-469                  Standard Test Method for Destructive Physical Analysis (DPA) for Ceramic
                               Monolithic Capacitors

                                             Page 1 of 107
                                                                                 AEC - Q200 - Rev E
                                                                                    March 20, 2023

Automotive Electronics Council
           Component Technical Committee

        IATF                    Quality Management System for Organizations in the Automotive Industry
        IEC 60695-11-5          Fire Hazard Testing – Part 11-5: Test Flames – Needle Flame Test Method,
                                Apparatus, Confirmatory Test Arrangement and Guidance
        IEC 60127 Series        Miniature Fuses
        IEC 60068-2-21          Robustness of terminations and integral mounting devices
        ISO-7637-1              Road Vehicles – Electrical Disturbances from Conduction and Coupling –
                                Part 1: Definitions and General Considerations
        J-STD-002               Solderability Tests for Component Leads, Terminations, Lugs, Terminals and
                                Wires
        J-STD-020               Moisture/Reflow Sensitivity Classification for Nonhermetic Surface Mount
                                Devices
        JESD22-A104             Temperature Cycling
        JESD22-B100             Physical Dimension
        JESD22-B106             Resistance to Solder Shock for Through-Hole Mounted Devices
        JIS-C-5101-1            Fixed Capacitors for use in Electronic Equipment – Part 1: Generic
                                Specification
        MIL-STD-202             Test Method Standard Electronic and Electrical Component Parts
        MIL-STD-883             Test Method Standard Microcircuits
        UL 94                   Tests for Flammability of Plastic Materials for Parts in Devices and Appliances


1.4     Abbreviations

        The following abbreviations are used within the document

        AEC     Automotive Electronic Council
        CDC     Certificate of Design and Construction
        ESD     Electrostatic Discharge
        PCB     Printed Circuit Board
        PCN     Product/Process Change Notification
        SMD     Surface Mount Device
        THT     Through-Hole Technology (Axial and Radial THT)


1.5     Definitions

1.5.1   AEC-Q200 Qualification

        Successful completion and documentation of the test results to the requirements outlined in this
        document allows the Supplier to claim that the component is “AEC-Q200 Qualified”.

        The Supplier, in agreement with the User, can perform qualification at sample sizes and conditions less
        stringent than what this document requires. However, that component cannot be considered “AEC-
        Q200 Qualified” until such time that the unfulfilled requirements have been successfully completed.

1.5.2   AEC Certification

        There are no "certifications" for AEC-Q200 qualification and there is no certification board run by AEC
        to qualify components.      Each Supplier performs their qualification to AEC documents, considers
        customer requirements and submits the data to the customer to verify compliance to AEC-Q200.

1.5.3   Temperature Ranges

        The minimum ambient temperature range for a component to be qualified to this document is -40°C to
        85°C. The manufacturer shall qualify their components to their specified ambient temperature range and
        in accordance with the applicable tables (Tables 1 through 16).

                                              Page 2 of 107
                                                                                    AEC - Q200 - Rev E
                                                                                       March 20, 2023

Automotive Electronics Council
             Component Technical Committee


        Note: Up to Revision D of this document, two different temperature cycling tests were specified:
        Temperature Cycling (Test No. 4) and Thermal Shock (Test No. 16). The Thermal Shock test was
        removed in Rev. D as it was considered that the Temperature Cycling test resulted in adequate thermal
        stresses since (1) the test requires a relatively fast transition time of 1 minute maximum between Low
        Temperature to Upper Temperature and (2) more cycles when compared to the Thermal Shock test.

1.5.4   Approval for Use in an Application

        “Approval” is defined as user approval for use of the part being qualified in the intended application
        along with any applicable supplements and compliance to any applicable user packaging specification.
        The user’s method of approval is beyond the scope of this document.

1.5.5   Generic Data

        Generic data is relevant data, from a qualification family, that the Supplier can use as a substitute for
        component-specific data for qualification and requalification. See Section 2.3.

1.5.6   Most Sensitive Component

        The most sensitive component within a family is the family member that is most affected by a given test.


2.0     GENERAL REQUIREMENTS

2.1     Objective

        The objective of this document is to ensure the component to be qualified meets the qualification
        requirements detailed in Tables 1 through 16.

2.2     Precedence of Requirements

        In the event of conflict in the requirements of this specification and those of any other documents, the
        following order of precedence applies:

        a.       The purchase order
        b.       The User’s individual component specification
        c.       This document
        d.       The reference documents in Section 1.3 of this document
        e.       The Supplier's data sheet

        For the component to be considered a qualified component, the purchase order and/or individual
        component specification cannot waive or detract from the requirements of this document.

2.3     The Use of Generic Data

        As stated in Section 1.5.5, generic data is relevant data from a qualification family that the Supplier can
        use as a substitute for component-specific data for qualification and requalification. Generic data
        reduces the number of samples to qualify as testing of certain components can cover others.

        Selection of which component to use in generic qualification testing is based on either:

        a.       Most sensitive family member (see Section 1.5.6) on a test-by-test basis, or
        b.       Minimum, middle and maximum value of the primary electrical characteristic of the family
                 members in accordance with Appendix 1 (i.e., for a Capacitor family, capacitor value, voltage,
                 etc.).

                                               Page 3 of 107
                                                                                      AEC - Q200 - Rev E
                                                                                         March 20, 2023

Automotive Electronics Council
           Component Technical Committee


        The Supplier shall provide reasoning as to the selection of the most sensitive members of the family,
        on a test-by-test basis. Where the most sensitive member(s) of the family for each test/inspection are
        not clear then the Supplier shall perform testing using the minimum, middle and maximum values of
        the given family.

        Appendix 1 defines the criteria by which components are grouped into a “qualification family”.

        Sources of generic data can come from certified test labs, internal Supplier's qualifications, User-
        specific qualifications, and/or Supplier's in-process monitors. The generic data to be submitted must
        meet or exceed the test conditions specified in Tables 1 through 16. The User(s) will be the final
        authority on the acceptance of generic data in lieu of component-specific test data.

2.4     Test Samples

2.4.1   Lot Requirements

        Lot requirements are in Table C.

2.4.2   Production Requirements

        All qualification components shall be produced on tooling and processes at the manufacturing site that
        will be used to support component deliveries at projected production volumes.

2.4.3   Reusability of Test Samples

        Components used for nondestructive qualification tests may be used to populate other qualification
        tests. Components that have been used for destructive qualification tests may not be used any further
        except for engineering analysis.

2.4.4   Sample Size Requirements

        Sample sizes used for qualification testing and/or generic data submission must be consistent with the
        specified minimum sample sizes in Table C. Additionally, the number of samples to be tested per lot
        may vary depending on the physical size of the component as per Table C. Where generic (family)
        data is provided instead of component-specific data, three (3) lots are required for all the tests that refer
        to Note B of Table C. If the qualification is performed on a specific component, only one (1) lot of that
        data is required, except for ESD (see Note E of Table C).

        If the Supplier elects to submit generic data for qualification, the specific test conditions and results
        must be reported. Existing applicable generic data shall first be used to satisfy these requirements and
        those of Section 2.3 for each test required in Table C. Component-specific qualification testing shall
        be performed if the generic data does not satisfy these requirements.

        For qualifications with a modified sample size (i.e., different than sample size required in Table C)
        based on the component type being considered, the Supplier and User can come to an agreement to
        modify the required number of samples per lot for qualification. Such an agreement may not allow for
        the Supplier to claim that the part is “AEC Qualified”.

2.4.5   Pre-stress and Post-stress Test Requirements

        To verify that the component to be qualified meets the components’ specification, the pre and post
        stress tests along with External Visual test are conducted. In general, Electrical Tests, Test Number 1
        in Table C, and External Visual, Test Number 9, are conducted before the stress test (pre-stress) and
        after the stress test (post-stress) as shown in Figure 1.


                                                Page 4 of 107
                                                                                      AEC - Q200 - Rev E
                                                                                         March 20, 2023

Automotive Electronics Council
             Component Technical Committee




                       Figure 1:      Pre and Post Stress Test Block Diagram
        Pre-stress and post-stress electrical tests are performed at nominal (room) temperature only unless
        otherwise stated in the “Additional Requirements” column of the applicable test of Tables 1 through 16.
        Any extreme endpoint test temperatures (e.g., minimum and maximum designed operational per
        Section 1.5.3 or the component datasheet) are specified in the "Additional Requirements" column of
        Tables 1 through 16 for each test.

2.4.6   Test Failure

        Test failures are those components not meeting (in order of significance as defined in Section 2.2):.

        a.       The User’s individual component specification,
        b.       Post-test criteria specific to the test, or
        c.       The manufacturer's data sheet

        Any component that shows external physical damage attributable to an environmental test is also
        considered a failed component. If the cause of failure is agreed (by the Supplier and the User) to be
        due to mishandling or ESD, the failure shall be discounted, but reported as part of the data submission.
        Suppliers must describe their parametric fail criteria for each stress test as part of the qualification data
        submission to the User for approval. A listing of suggested parameters for some component types are
        included after some component type test tables. The complete listing of failure criteria for each
        component type and parameter in this document is beyond its scope.

2.4.7   Criteria for Passing Qualification

        Passing all appropriate qualification tests specified in Tables 1 through 16, either by performing the test
        (acceptance of zero failures using the specified minimum sample size) on the specific component or
        demonstrating acceptable family generic data (using the family definition guidelines defined in Appendix
        1 and the total required lot and sample sizes), qualifies the component per this document.

        Passing the acceptance criteria (if Table xB is available) of all the tests in Tables 1 through 16 qualifies
        the component per this document. When the number of failures for any given test in Table C exceeds
        the acceptance criteria using the procedure herein, the component shall not be qualified until the root
        cause of the failure(s) is (are) determined and the corrective and preventive actions are implemented
        and confirmed to be effective in an 8D or other acceptable User format. New samples or data may be
        requested to verify the corrective and prevented action.

        Any unique reliability test or conditions requested by the User and not specified in this document shall
        be agreed upon between the Supplier and User requesting the test, and will not preclude a component
        from passing stress-test qualification as defined by this document.

2.4.8   Alternative Requirements

        Deviation from the requirements herein does not result in AEC Qualification and components cannot
        claim “AEC Qualified”, unless these deviations exceed the test conditions defined within the document.

        Any deviation from what is outlined in this document must be approved by the Users through supporting
        data presented by the Supplier demonstrating equivalency. These deviations will be clearly reported
        when the results of the qualification are submitted to the User for approval.
                                                Page 5 of 107
                                                                                 AEC - Q200 - Rev E
                                                                                    March 20, 2023

Automotive Electronics Council
           Component Technical Committee


3.0   QUALIFICATION AND REQUALIFICATION

3.1   Qualification of a New Component

      Requirements for qualification of a new component are listed in Table C, with the corresponding test
      conditions listed in Tables 1 through 16. Table E summarizes the stress tests for each passive
      component covered by this document. For each qualification, the Supplier must present data for ALL
      of these tests, whether it is stress test results on the component to be qualified or acceptable generic
      family data. A review is to be made of other components in the same generic family to ensure that
      there are no common failure mechanisms in that family. Upon request, justification for the use of generic
      data, whenever it is used, must be demonstrated by the Supplier and approved by the User.

      For each component qualification, the Supplier must present:

      a.       Certificate of Design and Construction (CDC) data (see Appendix 2) for the component to be
               qualified, and
      b.       The component(s) used for generic data testing.

      Test methodology, requirements and results shall be per the specifications and standards detailed
      under the “Reference” column of Tables 1 through 16. For example, if the referenced specification
      requires test samples to be PCB mounted (instead of loose component), the testing shall be conducted
      as such.

3.2   Qualification of Surface Mounted Device (SMD) Components

      For SMD lead-free components, added requirements needed to address the special quality and
      reliability issues that arise when lead-free (Pb-free) processing is utilized are specified in AEC-Q005:
      Pb-Free Test Requirements. Materials used in lead-free processing include the termination plating
      and the board attach (solder). These materials usually require higher board attach temperatures to
      yield acceptable solder joint quality and reliability. These higher temperatures may adversely affect
      the moisture sensitivity level of plastic packaged components.

      If a change is required to provide adequate robustness for Pb-free processing of the component, then
      the Supplier should refer to the process change qualification requirements (Tables 1A through 16A) in
      this specification.

      For SMD lead-free components, all components which are to be tested to stresses of the below Table
      A shall be preconditioned with three (3) reflow passes (reference J-STD-020) unless noted otherwise
      in Table B. The three (3) passes represent top side, bottom side and one (1) rework. When mounting
      of the components is required (per the stress test), the initial passes may be done with loose
      components and the final pass can be used to mount the components on the PCB. If agreed upon
      between User and Supplier, the number of reflows may be reduced and the Supplier shall make note
      of this in the qualification report and component datasheet. The Peak Temperature (Tpeak) during
      reflow shall be measured in accordance with Table B. Figure 2 shows the overall process.

      Moisture pre-conditioning (Moisture Soak) per J-STD-020 is not required.

                      Table A: Stress Tests Requiring Reflow Passes
                               Test No. Stress Test
                                  4     Temperature Cycling
                                  7     Humidity Bias
                                  8     High Temperature Operating Life



                                             Page 6 of 107
                                                                                      AEC - Q200 - Rev E
                                                                                         March 20, 2023

Automotive Electronics Council
              Component Technical Committee



                   Reflow                Pre-stress                                     Post-stress
                   passes                Electrical             Stress Test              Electrical
                                           Tests                                           Tests


                    Figure 2: Overall Process for SMD Lead-free Components

        High volume components that are > 1cm3 (e.g. film capacitors, aluminum electrolytic capacitors, super
        capacitors, or inductors etc.) may be preconditioned according to Table B. The Supplier shall make
        note of this in the qualification report and component datasheet.

                      Table B: Reflow Passes for High Volume Components
             Volume (cm³)             Number of Reflow Pre-                   Temperature Measurement
                                       Conditioning Passes                           Location
                  ≤1                           3*                                       Top
              >1 to < 2.5                       2                                       Top
                ≥ 2.5                           1                                 Solder Terminal

        * For aluminum electrolytic capacitors, including hybrids and polymers (Table 3) and film capacitors
        (Table 4) less than 1cm3 shall be preconditioned with two (2) passes as a minimum.


3.3     Requalification of a Component

        Requalification of a component or family shall be required when the supplier makes a change to the
        component or family and/or process that impact the form, fit, function, quality and reliability of the
        component or family.

3.3.1   Process Change Notification (PCN)

        The Supplier shall submit a projection to the Users of all component or process changes influencing the
        specified data or affecting the processing characteristics, negatively affecting reliability or quality data,
        changes of materials, manufacturing processes or test methods or each production relocation to
        another plant. The Supplier shall meet the mutually agreed upon requirements for product/process
        changes. Information required for submission to the User shall include the following as a minimum or
        as otherwise agreed upon between Supplier and User:

        a.        Benefit to the User (value, time and quality).
        b.        For each User component numbers involved in the change, the following information is
                  required:
                  i.       Supplier component number
                  ii.      An estimated date of the last production lot of unchanged components.
                  iii.     An estimated final order date and final ship date of unchanged components.
                  iv.      The first projected shipment date and date code of changed components.
        c.        A detailed description of the change in terms of the materials, processes,
                  visual/electrical/mechanical characteristics, rating, circuit design, internal element layout and
                  size, as applicable.
        d.        Technical data and rationale to support the proposed changes.




                                                Page 7 of 107
                                                                                      AEC - Q200 - Rev E
                                                                                         March 20, 2023

Automotive Electronics Council
             Component Technical Committee

        e.       If applicable, an electrical characterization comparison (between the new and original
                 component) of all significant electrical parameters over temperature extremes which could be
                 affected by the change. Changes in median and dispersion performances shall be noted even
                 though conformance to specification limits is still guaranteed. This is needed to evaluate any
                 adverse impact on specific end customer applications.
        f.       The Supplier shall submit an updated Certificate of Design, Construction and Qualification
                 along with information required by this section plus any changes impacting Appendix 2
                 information as originally submitted.
        g.       If applicable, the results of completed Supplier requalification tests of the changed
                 component(s).

        Items a through e are background information needed up front to evaluate the impact of the change on
        supply and reliability and to come to agreement on a qualification plan acceptable to the Supplier and
        User. Items e, f and g must be submitted prior to any final approval to implement any change on the
        User's product.

3.3.2   Component/Family Changes Requiring Requalification

        As a minimum, changes to a component or family shall use Tables 1A through 16A (Process Change
        Qualification Guidelines) as a guide for determining which tests need to be performed or whether
        equivalent generic data can be used. These tables are a superset of tests that the Supplier and User
        should use as a baseline for discussion of tests that are required for the requalification in question. It is
        the Supplier's responsibility to present rationale for why any of these tests need not be performed or
        whether any of the tests can be supplemented with generic data. Original test data from the old process
        (if it exists and is applicable) can be used as a baseline for comparative data analysis. If applicable,
        Electrical Characterization (Test Number 19) should be performed on a comparative basis.                 An
        agreement between the Supplier and the User(s) with justification for performing or not performing any
        recommended test shall occur before the implementation of a Requalification plan.

3.3.3   Lot/Sample Requirements for Requalification

        In case of a single component or family requalification, see Section 2.4.4 “Sample Size Requirements”.

3.3.4   Criteria for Passing Requalification

        It is the responsibility of each User to review the data, change notices, and supporting documentation to
        either approve or reject the change based on the results of the tests performed. All criteria requirements
        described in Section 2.4.6 apply.

3.3.5   User Approval

        A change may not affect a component's qualification status, but may affect its performance in an
        application. Individual User authorization of a process change will be required for that User's particular
        application(s), and this method of authorization is outside the scope of this document.




                                                Page 8 of 107
                                                                            AEC - Q200 - Rev E
                                                                               March 20, 2023

Automotive Electronics Council
           Component Technical Committee


4.0   QUALIFICATION TESTS

4.1   General Tests

      Qualification to this specification may be conducted either on a:

      a.       Family, or
      b.       Specific (individual) component.

      Test details are given in Tables 1 through 16. Not all tests apply to all components. For example,
      certain tests apply only to hermetically packaged components, while others apply only to SMD large
      can-components, and so on. The "Additional Requirements" column of Tables 1 through 16 also
      serves to highlight test requirements that supersede those described in the referenced test.

4.2   Data Submission Format

      Data summary shall be submitted similar to the examples given in Appendix 4.          Raw data and
      histograms shall be submitted upon request by the individual User. All data and documents (e.g.,
      justification for non- performed test, etc.) shall be maintained by the Supplier in accordance with
      a quality system such as ISO 9001 or IATF 16949.




                                             Page 9 of 107
                                                                                                               AEC - Q200 - Rev E
                                                                                                                  March 20, 2023

Automotive Electronics Council
          Component Technical Committee



                                              Table C: Qualification Sample Size
                                                                   Minimum Sample Size Per Lot                 Number of
                                                                 Depending on Component Size (cm3)               Lots
                                                                                                                                      Accept on
Test


                                                                                                                Individual
       Stress/Test                           Notes                                                                                     Number

                                                                                                                             Family
No.
                                                                < 10          10 ≤ x ≤ 330        > 330                                 Failed



1      Pre-and Post-Stress Electrical Test   G                 All qualification components unless otherwise specified                   0
3      High Temperature Exposure (Storage)   B, D, G, M           77                  26               10       1            3           0
4      Temperature Cycling                   B, D, G, M           77                  26               10       1            3           0
5      Destructive Physical Analysis         B, D, G              10                   5               3        1            3           0
7      Humidity Bias                         B, D, G, M           77                  26               10       1            3           0
8      Operating Life                        B, D, G, M           77                  26               10       1            3           0
9      External Visual                       G, N                              All qualification components                              0
10     Physical Dimensions                   G, N                 30                  10               4        1            3           0
11     Terminal Strength (THT)               D, G, L              30                  10               4        1            3           0
12     Resistance to Solvents                D, G                  5                   4               3        1            3           0
13     Mechanical Shock                      B, D, G              30                  10               4        1            3           0
14     Vibration                             B, D, G              30                  10               4        1            3           0
15     Resistance to Soldering Heat          D, G                 30                  10               4        1            3           0
17     ESD                                   D, E                 15                   6               3        1            3           0
                                                              15 each
18     Solderability                         D, G                                      6               3        1            3           0
                                                              condition
19     Electrical Characterization           G, M, N              30                  10               4             3                   0
20     Flammability                          D                        In accordance with Referenced Standards                            0
21     Board Flex (SMD)                      D, S                 30                  10               4        1            3           0
22     Terminal Strength (SMD)               D, S                 30                  10               4        1            3           0
24     Flame Retardance                      D, G                 30                  10               4        1            3           0
25     Rotational Life                       D, G                 30                  10               4        1            3           0
27     Surge Voltage                         D, G                 30                  10               4        1            3           0
30     Electrical Transient Conduction       D, G                 30                  10               4        1            3           0




                                                          Page 10 of 107
                                                                                                                                AEC - Q200 - Rev E
                                                                                                                                   March 20, 2023

Automotive Electronics Council
             Component Technical Committee



                                                  Table C: Qualification Sample Size (continued)

                                                                             Minimum Sample Size Per Lot                       Number of
                                                                           Depending on Component Size (cm3)                     Lots
                                                                                                                                                      Accept on
Test
         Stress/Test                                  Notes

                                                                                                                                Individual
                                                                                                                                                       Number
No.
                                                                                                                                                        Failed

                                                                                                                                             Family
                                                                             < 10         10 ≤ x ≤ 330           > 330


 32      Short Circuit Fault Current Durability       D, G                    30                   10               4            1           3             0
 33      Fault Current Durability                     D, G                    30                   10               4            1           3             0
 34      End-of-Life Mode Verification                D, G                    30                   10               4            1           3             0
 35      Jump Start Endurance                         D, G                    30                   10               4            1           3             0
 36      Load Dump Endurance                          D, G                    30                   10               4            1           3             0

Notes:

         B       Where generic data is provided instead of component specific data, 3 lots are required for all the tests. Number of allowed failures
                 remains 0 when 3 lots are tested. If the qualification is carried out on the component to be qualified (e.g., expanding an existing
                 product range) only 1 lot of that data is required, which are identified with a specific note.
         D       Destructive test. Devices are not to be reused for qualification or production.

         E       For a family qualification, if ESD classification or values are specified by the Supplier, all components within the family ( with this ESD
                 value) shall be tested. If no ESD classification or values are specified, generic data may be used.
         G       Generic data allowed.     See Section 2.3.

         L       Required for through-hole (THT) components only.

         M       Temperatures specified under “Additional Requirements” shall be understood as ambient chamber temperature rather than
                 component temperature.

         N       Nondestructive test. Components can be used to populate other tests or they can be used for
                 production.
         S       Required for surface mount components only.



                                                                     Page 11 of 107
                                                                                                                                                                                                       AEC - Q200 - Rev E
                                                                                                                                                                                                          March 20, 2023

Automotive Electronics Council
         Component Technical Committee



                                                  Table D: Applicable Stress Qualifications
                                                                                                                            Component


                                                                                                                                                                                                           EMI Suppressors /   Polymeric


                                                                               Film Capacitors                                                                              Quartz Crystals                                                               Super Capacitors
                                   Tantalum and


                                                                                                                                    Thermistors
                                                                                                                                                                                              Ceramic
                                                                Aluminum                                                                          Trimmer
                                                   Ceramic

                                                                                                 Magnetics
  Test


                                                                                                             Networks   Resistors                               Varistors
               Stress/Test
                                   Niobium
                                                                                                                                                                                                           Filters
  No.

                                                                                                                                                                                                                               Resettable Fuses
                                                                Electrolytic                                                                      Capacitors/
                                   Capacitors      Capacitors   Capacitors                                                                        Resistors                                   Resonators                                          Fuses

                                                                                                                        Table Number
                                       1             2              3              4             5             6        7    8    9                             10          11                 12             13                14                15      16
         Pre-and Post-Stress
   1                                   X             X             X              X              X            X         X           X                X          X           X                   X               X                 X               X       X
         Electrical Test
         High Temperature
   3                                   X                           X              X              X            X         X           X                X          X           X                   X               X                                 X       X
         Exposure (Storage)
   4     Temperature Cycling           X             X             X              X              X            X         X           X                X          X           X                   X               X                 X               X       X
         Destructive Physical
   5                                                 X                                                                                                                                                          X
         Analysis
   7     Humidity Bias                 X             X             X              X              X            X         X           X                X          X           X                   X               X                 X               X       X
         High Temperature
   8                                   X             X             X              X              X            X         X           X                X          X           X                   X               X                 X               X       X
         Operating Life
  9      External Visual               X             X             X              X              X            X         X           X                X          X           X                   X               X                 X               X       X
  10     Physical Dimensions           X             X             X              X              X            X         X           X                X          X           X                   X               X                 X               X       X
         Terminal Strength
  11                                   X             X             X              X              X            X         X           X                X          X           X                   X               X                 X               X       X
         (THT)
  12     Resistance to Solvent         X             X             X              X              X            X         X           X                X          X           X                   X               X                 X               X       X
  13     Mechanical Shock              X             X             X              X              X            X         X           X                X          X           X                   X               X                 X               X       X
  14     Vibration                     X             X             X              X              X            X         X           X                X          X           X                   X               X                 X               X       X
         Resistance to Soldering
  15                                   X             X             X              X              X            X         X           X                X          X           X                   X               X                                 X       X
         Heat
  17     ESD                                         X                            X              X            X         X           X                X          X                               X               X
  18     Solderability                 X             X             X              X              X            X         X           X                X          X           X                   X               X                 X               X       X


                                                                          Page 12 of 107
                                                                                                                                                                                                        AEC - Q200 - Rev E
                                                                                                                                                                                                           March 20, 2023

Automotive Electronics Council
         Component Technical Committee



                                 Table D: Applicable Stress Qualifications (continued)
                                                                                                                         Component


                                                                                                                                                                                                         EMI Suppressors /   Polymeric


                                                                            Film Capacitors                                                                              Quartz Crystals                                                                Super Capacitors
                                 Tantalum and


                                                                                                                                 Thermistors
                                                                                                                                                                                           Ceramic
                                                             Aluminum                                                                          Trimmer
                                                Ceramic

                                                                                              Magnetics
  Test


                                                                                                          Networks   Resistors                               Varistors
               Stress/Test
                                 Niobium
                                                                                                                                                                                                         Filters             Resettable Fuses
  No.
                                                             Electrolytic                                                                      Capacitors/
                                 Capacitors     Capacitors   Capacitors                                                                        Resistor                                    Resonators                                           Fuses

                                                                                                                     Table Number
                                     1            2              3              4             5             6        7    8    9                             10          11                 12              13                14                15      16
          Electrical
  19      Characterization           X            X             X              X              X            X         X           X                X          X           X                   X                X                 X               X       X
  20      Flammability                                          X              X              X            X         X           X                X          X           X                                    X                 X               X       X
  21      Board Flex (SMD)                        X             X              X              X            X         X           X                X          X           X                   X                X                 X               X       X
          Terminal Strength
  22      (SMD)                      X            X             X              X              X            X         X           X                X          X           X                   X                X                 X               X       X
  24      Flame Retardance                                                                                           X
  25      Rotational Life                                                                                                                         X
  27      Surge Voltage                                         X
          Electrical Transient
  30      Conduction                                                                                                                                         X                                                X
          Short Circuit Fault
  32      Current Durability                                                                                                                                                                                                    X
          Fault Current
  33      Durability                                                                                                                                                                                                            X
          End-of-Life Mode
  34      Verification                                                                                                                                                                                                          X
  35      Jump Start Endurance                                                                                                                                                                                                  X
          Load Dump
  36      Endurance                                                                                                                                                                                                             X




                                                                        Page 13 of 107
                                                                             AEC - Q200 - Rev E
                                                                                March 20, 2023

Automotive Electronics Council
         Component Technical Committee




  Table 1: Stress Qualifications for Tantalum (MnO2 and Polymer) and Niobium
                                    Capacitors
 Stress              No.   Reference            Additional Requirements
 Pre-and Post-                                  ▪ Test is performed at room temperature except as
 Stress Electrical   1     User Specification      specified in the applicable stress reference and
 Test                                              the additional requirements in this Table.
                                                ▪   Unpowered
                                                ▪   Tested at maximum specified operating
 High
                                                    temperature or maximum specified storage
 Temperature               MIL-STD-202
                     3                              temperature (whichever is higher). Minimum
 Exposure                  Method 108
                                                    test temperature shall be 85°C.
 (Storage)
                                                ▪   1,000 hours
                                                ▪   Measurement at 24±4 hours after test conclusion.
                                                ▪   Unpowered
                                                ▪   1,000 Cycles
                                                ▪   Lower Temp of the Chamber: -55°C
                                                ▪   Upper Temperature of the Chamber: maximum
                                                    specified operating temperature and shall not
                                                    exceed 125°C.
 Temperature
                     4     JESD22-A104          ▪   Dwell Time (Soak Time):
 Cycling
                                                         o 15 minutes minimum,
                                                         o 30 minutes minimum if component weighs
                                                             above 28g
                                                ▪   Transition Time: 1 minute maximum
                                                ▪   Measurement at least 24 hours after test
                                                    conclusion.
                                                ▪   1,000 hours
                           MIL-STD-202          ▪   85°C/85% RH
 Humidity Bias       7
                           Method 103           ▪   Measurement at 24±4 hours after test conclusion.
                                                ▪   Rated Voltage Only
                                                ▪   1,000 hours
 High                                           ▪   2/3 rated voltage
                           MIL-STD-202
 Temperature         8                          ▪   Temperature of the Chamber: maximum specified
                           Method 108
 Operating Life                                     operating temperature up to 150°C.
                                                ▪   Measurement at 24±4 hours after test conclusion.

                           MIL-STD-883          ▪   Inspect component construction, marking and
 External Visual     9                              workmanship.
                           Method 2009
                                                ▪   Pre and Post Electrical Test not required.

                                                ▪   Verify physical dimensions to the applicable
 Physical
                     10    JESD22-B100              component specification.
 Dimensions
                                                ▪   Pre and Post Electrical Test not required.




                                          Page 14 of 107
                                                                              AEC - Q200 - Rev E
                                                                                 March 20, 2023

Automotive Electronics Council
          Component Technical Committee




  Table 1: Stress Qualifications for Tantalum (MnO2 and Polymer) and Niobium
                              Capacitors (continued)
 Stress              No.   Reference         Additional Requirements
                                             ▪ Test THT component lead integrity only
                                             ▪ Test Condition A (pull test):
                                                     Nominal cross-sectional       Force (N)
                                                          area (mm2)
                                                             ≤ 0.05                    1
                                                          0.06 to 0.10                2.5
                                                          0.11 to 0.20                 5
                                                          0.21 to 0.50                10
                                                          0.51 to 1.20                20
                                                             > 1.20                   40
                                             ▪   Test Condition C (wire-lead bend test):
                                                      Section Modulus (ZX)         Force (N)
 Terminal Strength
                                                              (mm3)
 (for axial and            MIL-STD-202                      ≤ 1.5x10-3                0.5
                     11
 radial THT                Method 211                  1.6x10-3 to 4.2x10-3          1.25
 components)                                           4.3x10-3 to 1.2x10-2           2.5
                                                       1.3x10-2 to 0.5x10-1            5
                                                       0.6x10-1 to 1.9x10-1           10
                                                            > 1.9x10-1                20
                                                 For round terminations: ZX = (πd3)/32 where d is
                                                 the lead diameter.
                                                 For strip terminations: ZX = (ba2)/6 where a is the
                                                 thickness of the rectangular strip perpendicular to
                                                 the bending axis, b is the other dimension of the
                                                 rectangular strip.
                                             Note: the values and formulas are per IEC 60068-2-
                                             21, 6th Edition.
                                             ▪   In addition to the Method 215 solvents, add an
                                                 Aqueous wash chemical and follow chemical
 Resistance to             MIL-STD-202           manufacturers recommended parameters (i.e.,
                     12
 Solvents                  Method 215            solution temperature and immersion time).
                                             ▪   Applicable to ink marked components and not
                                                 laser marked components.
                                             ▪   Figure 1 of Method 213
 Mechanical                MIL-STD-202       ▪   THT: Condition C
                     13                      ▪   SMD: Condition C
 Shock                     Method 213
                                             ▪   Tested per the Supplier’s recommended mounting
                                                 method.




                                         Page 15 of 107
                                                                                 AEC - Q200 - Rev E
                                                                                    March 20, 2023

Automotive Electronics Council
          Component Technical Committee



  Table 1: Stress Qualifications for Tantalum (MnO2 and Polymer) and Niobium
                              Capacitors (continued)
 Stress              No.   Reference              Additional Requirements
                                                  ▪ 5g's for 20 minutes
                                                  ▪ 12 cycles each of 3 orientations.
                                                  ▪ Tested per the Suppliers’ recommended
                                                     mounting method.
                                                  ▪ Verification of transfer load: during setup, verify
                                                     that with the selected PCB design (size, thickness
                           MIL-STD-202               and secure points), or an alternative mount as
 Vibration           14
                           Method 204                appropriate to the use-case of the component,
                                                     that the transferred load onto the component
                                                     corresponds to the requested load. This
                                                     verification can be achieved using a laser
                                                     vibrometer or other adequate measuring device.
                                                  ▪ Test from 10 Hz -2000 Hz
                                                  ▪ THT: Conditions B or C
 Resistance to             MIL-STD-202            ▪ SMD: Condition K, time above 217°C, 60s – 150s
                      15                          ▪ Non-soldered type mounting/attach are not
 Soldering Heat            Method 210
                                                     applicable.
                                                  ▪ THT:
                                                          o Method A1, Coating Durability Category 2
                                                  ▪ SMD:
                                                          o Method B1, Coating Durability Category 2
                                                          o Method D, Coating Durability Category 2.
                                                  ▪ Note: in particular circumstances when SnPb
 Solderability        18   J-STD-002                 reverse compatibility is requested by the User,
                                                     Method A shall be used for THT and Method B
                                                     shall be used for SMD.
                                                  ▪ Pre and Post Electrical Test not required
                                                  ▪ Magnification 50x
                                                  ▪ Non-soldered type mounting/attach are not
                                                     applicable.
                                                  ▪    Parametrically test per lot and sample size
                                                       requirements.
 Electrical                                       ▪    Summary to show minimum, maximum, mean and
                      19   User Specification          standard deviation at room, minimum and
 Characterization
                                                       maximum operating temperatures.
                                                  ▪    Pre and Post Electrical Test not required.
 Terminal
 Strength             22   AEC-Q200-006
 (SMD)

      Note: For any deviation from the above stresses, refer to Section 2.4.8.

      Back to Table C: Qualification Sample Size
      Back to Table D: Applicable Stress Qualifications


                                            Page 16 of 107
                                                                                                    AEC - Q200 - Rev E
                                                                                                       March 20, 2023

Automotive Electronics Council
              Component Technical Committee



  Table 1A: Tantalum (MnO2 and Polymer) and Niobium Capacitors Process Change
                 Qualification Guidelines for the Selection of Tests

For a given change listed below, the Supplier should justify why a suggested test does not apply for the given
component(s) under consideration. Collaboration with their customer base is highly recommended.

             3.      High Temperature Exposure (Storage)     12.    Resistance to Solvents               22.   Terminal Strength (SMD)
             4.      Temperature Cycling                     13.    Mechanical Shock
             7.      Biased Humidity                         14.    Vibration
             8.      Operational Life                        15.    Resistance to Soldering Heat
             9.      External Visual                         18.    Solderability
            10.      Physical Dimension                      19.    Electrical Characterization


Note: A letter or "⚫" indicates that performance of that stress test should be considered (not necessarily
required) for the appropriate process change.

Test # From Table 1                                                    3    4    7    8   9    10   12   13    14   15   18   19   22
MATERIAL
New / Change Binder Material (anode pressing)                          ●    ●        ●                         ●              B
New / Change in Anode Powder Category (CV (uC/g))                      ●    ●    ●   ●                                        B
1st usage of Anode powder category (CV (uC/g)) in a voltage range      ●    ●    ●   ●                                        B
New / Change Cathodic Layer Materials                                  ●    ●    ●   ●                                        B
New/ / Change Silver Adhesive                                          ●    ●    ●   ●                                        B
New Lead Frame Material                                                ●    ●    ●   ● ●       ●         ●     ●    ●    ●    B    ●
Existing Lead frame - Change External Termination Material/Layers           ●    ●   ● ●       ●         ●     ●    ●    ●    B    ●
PROCESS
New / Change Anode Pressing technique                                  ● ●           ●                         ●              B
New Marking                                                                                         ●
New Assembly Process                                                   ● ● ● ● ●               ●         ●     ●    ●    ●    B    ●
DESIGN
Encapsulation                                                          ● ● ● ● ●               ●    ●                    ●    B
Dielectric Thickness                                                   ● ●   ●                                      ●         B
Anode Wire Diameter                                                      ●   ●                           ●     ●
Existing Lead frame - Change Dimensional / Geometry                                                      ●     ●    ●    ●    B    ●
MISCELLANEOUS
Mfg. Site Transfer                                                     ● ● ● ● ●               ●    ●    ●     ●    ●    ●    B    ●
Material Suppliers                                                     ● ● ● ●                      ●    ●     ●    ●    ●    B    ●
New/Modified Mfg. Equipment                                            ● ● ● ●                                                B


                                   B = comparative data (unchanged vs. Changed) required




                                                           Page 17 of 107
                                                                                                          AEC - Q200 - Rev E
                                                                                                             March 20, 2023

     Automotive Electronics Council
                     Component Technical Committee


            Table 1B: Tantalum (MnO2 and Polymer) and Niobium Capacitors Acceptance
                                            Criteria
     Note: The contents in this table are meant to serve as examples of wording or limits for each test and relative
     parameter to be measured and NOT actual requirements. Variables are denoted by lower-case letters (e.g.,
     x, y). The measured parameters, values and wording of each acceptance criteria for each test should be
     agreed to between the User and Supplier.

                                                                                     Acceptance Criteria
                                        General requirements:
Measured Parameter =>                   1. Acceptance criteria below apply unless otherwise specified.
AEC-Q200 Test                           2. Supplier spec limits apply, if required parameter is unspecified by the User.

                                            Capacitance           Dissipation factor                ESR                     Leakage current
                                        Within specified        Below specified          Below specified
1a. Initial limits                                                                                                Below specified upper limit
                                        tolerance               upper limit              upper limit
                                                                                                                  p% rated DC voltage, q C,
                                        X Hz, y Vrms max.       a Hz, b Vrms max.
                                                                                                                  1kohm series resistor,
1b. Test Conditions                     AC, u V max. DC, v      AC, c V max. DC, d       m Hz, n C
                                                                                                                  measurement taken after cap is
                                        C                       C
                                                                                                                  fully charged (typically r minutes)
3. High temp exposure                   Change <=x%           Initial limit              Initial limit            Initial limit
4. Temperature cycling                  Change <=x%           Initial limit              Initial limit            Initial limit
7. Biased Humidity                      Change <=x%           <=a% initial limit         <=m% initial limit       <=p% initial limit
8. Operational Life                     Change <=x%           Initial limit              Initial limit            <=p% initial limit
9. External Visual                      Per AEC-Q200 – Electrical test not required.
10. Physical Dimensions                 Per AEC-Q200 – Electrical test not required.
11. Terminal Strength (THT)             Per AEC-Q200 – Electrical test not required.
12. Resistance to Solvents              Change <=x%            Initial limit              No spec                  Initial limit
13. Mechanical Shock                    Change <=x%            Initial limit              No spec                  Initial limit
14. Vibration                           Change <=x%            Initial limit              No spec                  Initial limit
15. Resistance to Soldering Heat        Change <=x%            Initial limit              No spec                  Initial limit
18. Solderability                       Per AEC-Q200 – Electrical test not required.
19a. Elec. Char. @ 25C                  Initial limit          Initial limit              Initial limit            Initial limit
19b. Elec. Char. @ -55C (or specified
                                        Change <=x%              <=a% Initial limit       No spec                  No spec
lower operating temperature limit)
19c. Elec. Char. @ 85C (or specified
                                        Change <=x%              Initial limit            No spec                  <=p% initial limit
upper operating temperature limit)
19d. Elec. Char. @ 125C (or specified
                                        Change <=x%              Initial limit            No spec                  <=p% initial limit
upper operating temperature limit)
20. Flammability                        Per AEC-Q200 – Electrical test not required. Present certificate of compliance.
22. Terminal Strength (SMD)             Per AEC-Q200 – Electrical test not required.




                                                           Page 18 of 107
                                                                              AEC - Q200 - Rev E
                                                                                 March 20, 2023

Automotive Electronics Council
          Component Technical Committee




                     Table 2: Stress Qualifications for Ceramic Capacitors

 Stress               No.   Reference            Additional Requirements
 Pre- and Post-                                  ▪ Test is performed at room temperature except
 Stress Electrical     1    User Specification      as specified in the applicable stress reference
 Test                                               and the additional requirements in this Table.
                                                 ▪ Unpowered
                                                 ▪ 1,000 Cycles
                                                 ▪ Lower Temperature of the Chamber: -55C
                                                 ▪ Upper Temperature of the Chamber: maximum
                                                    specified operating temperature and shall not
 Temperature                                        exceed 125C.
 Cycling
                       4    JESD22-A104          ▪ Dwell Time (Soak Time):
                                                         o 15 minutes minimum,
                                                         o 30 minutes minimum if component weighs
                                                             above 28g
                                                 ▪ Transition Time: 1 minute maximum
                                                 ▪ Measurement at least 24 hours after test
                                                    conclusion.
 Destructive
                       5    EIA-469              ▪   Pre and Post Electrical Test not required.
 Physical Analysis
                                                 ▪   1,000 hours
                                                 ▪   85C/85% RH
                                                 ▪   Measurement at 244 hours after test conclusion.
                            MIL-STD-202          ▪   Rated Voltage and 1.3 to 1.5 volts. Add 100Kohm
 Humidity Bias         7                             resistor.
                            Method 103
                                                 ▪   For ceramic capacitors that have internal
                                                     electrodes with no silver content the low voltage
                                                     portion of this test may be excluded.
                                                 ▪   1,000 hours
                                                 ▪   Rated voltage
 High                                            ▪   The maximum rated temperature and voltage rating
                            MIL-STD-202
 Temperature           8                             for the dielectric employed in the component shall be
                            Method 108
 Operating Life                                      used.
                                                 ▪   Measurement at 244 hours after test conclusion.
                                                 ▪   Inspect component construction, marking and
                            MIL-STD-883
 External Visual       9                             workmanship.
                            Method 2009          ▪   Pre and Post Electrical Test not required.
                                                 ▪   Verify physical dimensions to the applicable
 Physical                                            component specification.
                      10    JESD22-B100          ▪   Pre and Post Electrical Test not required.
 Dimensions




                                            Page 19 of 107
                                                                           AEC - Q200 - Rev E
                                                                              March 20, 2023

Automotive Electronics Council
          Component Technical Committee




              Table 2: Stress Qualifications for Ceramic Capacitors (continued)

 Stress             No.   Reference         Additional Requirements
                                            ▪ Test THT component lead integrity only.
                                            ▪ Test Condition A (pull test):
                                                          Nominal cross-            Force (N)
                                                        sectional area (mm2)
                                                                ≤ 0.05                     1
                                                             0.06 to 0.10                 2.5
                                                             0.11 to 0.20                  5
                                                             0.21 to 0.50                 10
                                                             0.51 to 1.20                 20
                                                                > 1.20                    40
                                            ▪   Test Condition C (wire-lead bend test):
 Terminal                                               Section Modulus (ZX)        Force (N)
 Strength (for                                                  (mm3)
                          MIL-STD-202                        ≤ 1.5x10-3                0.5
 axial and radial   11
                          Method 211                     1.6x10-3 to 4.2x10-3         1.25
 THT
 components)                                             4.3x10-3 to 1.2x10-2          2.5
                                                         1.3x10-2 to 0.5x10-1           5
                                                         0.6x10-1 to 1.9x10-1          10
                                                             > 1.9x10-1                20
                                                 For round terminations: ZX = (πd3)/32 where d is
                                                 the lead diameter.
                                                 For strip terminations: ZX = (ba2)/6 where a is the
                                                 thickness of the rectangular strip perpendicular to
                                                 the bending axis, b is the other dimension of the
                                                 rectangular strip.
                                            Note: the values and formulas are per IEC 60068-2-21,
                                            6th Edition.
                                            ▪ In addition to the Method 215 solvents, add an
                                                 Aqueous wash chemical and follow chemical
 Resistance to            MIL-STD-202            manufacturer’s recommended parameters (i.e.,
                    12
 Solvents                 Method 215             solution temperature and immersion time).
                                            ▪ Applicable to ink marked components and not laser
                                                 marked components.
                                            ▪ Figure 1 of Method 213
 Mechanical               MIL-STD-202       ▪ THT: Condition C
                    13                      ▪ SMD: Condition C
 Shock                    Method 213
                                            ▪ Tested per the Supplier’s recommended mounting
                                                 method.




                                        Page 20 of 107
                                                                                  AEC - Q200 - Rev E
                                                                                     March 20, 2023

Automotive Electronics Council
             Component Technical Committee




              Table 2: Stress Qualifications for Ceramic Capacitors (continued)

 Stress               No.   Reference              Additional Requirements
                                                   ▪ 5g's for 20 minutes
                                                   ▪ 12 cycles each of 3 orientations.
                                                   ▪ Tested per the Supplier’s recommended mounting
                                                      method.
                                                   ▪ Verification of transfer load: during setup, verify that
                            MIL-STD-202               with the selected PCB design (size, thickness and
 Vibration            14
                            Method 204                secure points), or an alternative mount, that the
                                                      transferred load onto the component corresponds to
                                                      the requested load. This verification can be
                                                      achieved using a laser vibrometer or other adequate
                                                      measuring device.
                                                   ▪ Test from 10 Hz - 2000 Hz.
                                                   ▪ THT: Conditions B or C
 Resistance to              MIL-STD-202            ▪ SMD: Condition K, time above 217°C, 60s – 150s
                      15
 Soldering Heat             Method 210             ▪ Non-soldered type mounting/attach are not
                                                      applicable.

 ESD                  17    AEC-Q200-002

                                                   ▪   THT:
                                                          o Method A1, Coating Durability Category 2
                                                   ▪   SMD:
                                                          o Method B1, Coating Durability Category 2
                                                          o Method D, Coating Durability Category 2
                                                   ▪   Note: in particular circumstances when SnPb
 Solderability        18    J-STD-002                  reverse compatibility is requested by the User,
                                                       Method A shall be used for THT and Method B
                                                       shall be used for SMD.
                                                   ▪   Pre and Post Electrical Test not required.
                                                   ▪   Magnification 50x
                                                   ▪   Non-soldered type mounting/attach are not
                                                       applicable.
                                                   ▪   Parametrically test per lot and sample size
                                                       requirements.
 Electrical                                        ▪   Summary to show minimum, maximum, mean and
                      19    User Specification.        standard deviation at room, minimum and
 Characterization
                                                       maximum operating temperatures.
                                                   ▪   Pre and Post Electrical Test not required.
 Board Flex
                      21    AEC-Q200-005
 (SMD)
 Terminal Strength
                      22    AEC-Q200-006
 (SMD)

       Note: For any deviation from the above stresses, refer to Section 2.4.8.

       Back to Table C: Qualification Sample Size
       Back to Table D: Applicable Stress Qualifications



                                             Page 21 of 107
                                                                                                    AEC - Q200 - Rev E
                                                                                                       March 20, 2023

Automotive Electronics Council
            Component Technical Committee



    Table 2A: Ceramic Capacitors Process Change Qualification Guidelines for the
                                 Selection of Tests
For a given change listed below, the Supplier should justify why a suggested test does not apply for the given
component(s) under consideration. Collaboration with their customer base is highly recommended.

      4.    Temperature Cycling                          13.   Mechanical Shock
      5.    Destructive Physical Analysis                14.   Vibration
      7.    Biased Humidity                              15.   Resistance to Soldering Heat
      8.    Operational Life                             17.   Electrostatic Discharge (ESD)
      9.    External Visual                              18.   Solderability
      10.   Physical Dimension                           19.   Electrical Characterization
      11.   Terminal Strength (THT)                      21.   Board Flex
      12.   Resistance to Solvents                       22.   Terminal Strength (SMD)


Note: A letter or "⚫" indicates that performance of that stress test should be considered (not necessarily
required) for the appropriate process change

            Test # From Table 2             4   5   7     8    9   10   11   12   13   14      15   17   18   19   21   22
            MATERIAL
            Binder Material                 ⚫   ⚫                                       ⚫
            Dielectric Change               ⚫   ⚫   ⚫     ⚫             ⚫    ⚫     ⚫    ⚫           ⚫         B    ⚫
            Electrode Attach                ⚫             ⚫                                    ⚫              B    ⚫    ⚫
            Electrode Material              ⚫   ⚫   ⚫     ⚫             ⚫    ⚫          ⚫           ⚫         B
            Encapsulation                   ⚫       ⚫          ⚫   ⚫         ⚫
            Lead Material                   ⚫   ⚫         ⚫    ⚫        ⚫               ⚫      ⚫         ⚫    B
            PROCESS
            Dicing                          ⚫       ⚫          ⚫   ⚫         ⚫     ⚫                          B
            Electrode Apply                         ⚫                                                         B    ⚫
            Firing Profile                  ⚫   ⚫         ⚫                                         ⚫         B
            Lamination/Press Technique          ⚫   ⚫                                          ⚫              B    ⚫
            Powder Particle Size            ⚫       ⚫                                          ⚫    ⚫         B    ⚫
            Screening/Printing                            ⚫                        ⚫                ⚫         B
            Termination Process             ⚫   ⚫   ⚫     ⚫    ⚫   ⚫    ⚫    ⚫     ⚫    ⚫      ⚫         ⚫    B    ⚫    ⚫
            DESIGN
            Electrode Thickness             ⚫   ⚫         ⚫        ⚫               ⚫    ⚫           ⚫         B
            Layer Thickness                 ⚫   ⚫   ⚫     ⚫        ⚫    ⚫          ⚫                ⚫         B
            Lead Diameter                   ⚫       ⚫     ⚫    ⚫   ⚫    ⚫               ⚫
            Number of Layers                ⚫   ⚫   ⚫     ⚫        ⚫               ⚫                ⚫         B
            Termination Area                                   ⚫   ⚫                    ⚫                          ⚫    ⚫
            Terminal Interface              ⚫   ⚫   ⚫     ⚫             ⚫          ⚫    ⚫      ⚫              B    ⚫    ⚫
            MISCELLANEOUS
            Mfg. Site Transfer              ⚫   ⚫   ⚫     ⚫    ⚫   ⚫    ⚫    ⚫     ⚫    ⚫      ⚫    ⚫    ⚫    B    ⚫    ⚫
            Material Suppliers              ⚫   ⚫   ⚫     ⚫             ⚫    ⚫     ⚫    ⚫      ⚫    ⚫    ⚫    B    ⚫    ⚫
            New/Modified Mfg. Equipment     ⚫       ⚫     ⚫        ⚫    a               ⚫           ⚫    ⚫    B


      a = termination equipment only                    B = comparative data (unchanged vs. Changed) required




                                                    Page 22 of 107
                                                                                           AEC - Q200 - Rev E
                                                                                              March 20, 2023

Automotive Electronics Council
            Component Technical Committee


             Table 2B-1: Ceramic Capacitors – Class I SMD Acceptance Criteria
Note: The contents in this table are meant to serve as examples of wording or limits for each test and relative
parameter to be measured and NOT actual requirements. Variables are denoted by lower-case letters (e.g.,
x, y). The measured parameters, values and wording of each acceptance criteria for each test should be
agreed to between the User and Supplier.

                                                                  Acceptance Criteria
 Measured Parameter =>
                                       Capacitance                           Q                 Insulation Resistance
 AEC-Q200 Test:
 1a. Initial limits            Within specified limits       Within specified limits           Within specified limits
                               Change <= greater of
 4. Temperature cycling                                      Initial limit                     Initial limit
                               +/-x% or +/-y pF
 5. Destructive physical
                               Per AEC-Q200 – Electrical test not required.
 analysis
                               Change <= greater of       <a pF: Q >= b + (c /pf * C)
 7. Biased Humidity                                                                            >= m% Initial limit
                               +/-x% or +/-y pF           >=a pF: Q >= d% initial
                                                          <a pF: Q >= b + (c /pf * C)
                               Change <= greater of
 8. Operational Life                                      d pF to e pF: Q>= f + (g /pf * C)    >= m% Initial limit
                               +/-x% or +/-y pF
                                                          >= h pF: Q >= i
 9. External Visual            Per AEC-Q200 – Electrical test not required.
 10. Physical Dimensions       Per AEC-Q200 – Electrical test not required.
 12. Resistance to Solvents    Initial limit              Initial limit                        Initial limit
 13. Mechanical Shock          Initial limit              Initial limit                        Initial limit
 14. Vibration                 Initial limit              Initial limit                        Initial limit
 15. Resistance to Soldering   Change <= greater of
                                                          Initial limit                        Initial limit
 Heat                          +/-x% or +/-y pF
 17. ESD                       Initial limit              Initial limit                        Initial limit
 18. Solderability             Per AEC-Q200 – Electrical test not required.
 19a. Elec. Char.
                               Initial limit                 Initial limit                     Initial limit
 @ 25ºC
                               Dielectric Withstanding Voltage: 250% rated voltage
 19b. Elec. Char. @ -55ºC      Change <= +/-x%              No spec                            No spec
 19c. Elec. Char. @ 125ºC      Change <= +/-x%              No spec                            >= m% Initial limit
 21. Board Flex                Initial limit                Initial limit                      Initial limit
                               >=x mm (record deflection at point of electrical failure)
 22. Terminal Strength (SMD)   Initial limit                Initial limit                      Initial limit
                               0603 and greater: x N
                               0402 and less: y N




                                                Page 23 of 107
                                                                                             AEC - Q200 - Rev E
                                                                                                March 20, 2023

Automotive Electronics Council
            Component Technical Committee


          Table 2B-2: Ceramic Capacitors – Class II/III SMD Acceptance Criteria
Note: The contents in this table are meant to serve as examples of wording or limits for each test and relative
parameter to be measured and NOT actual requirements. Variables are denoted by lower-case letters (e.g.,
x, y). The measured parameters, values and wording of each acceptance criteria for each test should be
agreed to between the user and supplier.

                                                                  Acceptance Criteria
  Measured Parameter =>
                                          Capacitance                Dissipation Factor         Insulation Resistance
  AEC-Q200 Test
  1a. Initial limits            Within specified limits           Within specified limits     Within specified limits
  4. Temperature cycling        Change <= +/-x %                  Initial limit               Initial limit
  5. Destructive physical
                                Per AEC-Q200 – Electrical test not required.
  analysis
  7. Biased Humidity            Change <= +/-x%                < a% initial                   >= m% Initial limit
  8. Operational Life           Change <= +/-x%                < a% initial                   >= m% Initial limit
  9. External Visual            Per AEC-Q200 – Electrical test not required.
  10. Physical Dimensions       Per AEC-Q200 – Electrical test not required.
  12. Resistance to Solvents    Initial limit                  Initial limit                  Initial limit
  13. Mechanical Shock          Initial limit                  Initial limit                  Initial limit
  14. Vibration                 Initial limit                  Initial limit                  Initial limit
  15. Resistance to Soldering
                                Change <= +/-x%                   Initial limit               Initial limit
  Heat
  17. ESD                       Initial limit                  Initial limit                  Initial limit
  18. Solderability             Per AEC-Q200 – Electrical test not required.
  19a. Elec. Char.
                                Initial limit                     Initial limit               Initial limit
  @ 25ºC
                                Dielectric Withstanding Voltage: 250% rated voltage
  19b. Elec. Char.
                                Change <= +/-x%                   No spec                     No spec
  @ -55ºC
  19c. Elec. Char.
                                Change <= +/-x%                   No spec                     >= m% Initial limit
  @ 125ºC
  21. Board Flex                Initial limit                   Initial limit                 Initial limit
                                >= x mm (record deflection at point of electrical failure)
  22. Terminal Strength
                                Initial limit                     Initial limit               Initial limit
  (SMD)
                                0603 and greater: x N
                                0402 and less: y N




                                                 Page 24 of 107
                                                                             AEC - Q200 - Rev E
                                                                                March 20, 2023

Automotive Electronics Council
          Component Technical Committee



    Table 3: Stress Qualifications for Aluminum Electrolytic (Hybrid, Polymer and
                                 Standard) Capacitors
 Stress              No.   Reference            Additional Requirements
 Pre- and Post-                                 ▪ Test is performed at room temperature except as
 Stress Electrical   1     User Specification      specified in the applicable stress reference and the
 Test                                              additional requirements in this Table.
                                                ▪ Unpowered
 High                                           ▪ 1,000 hours
 Temperature               MIL-STD-202          ▪ Upper category temperature or maximum specified
                     3                             storage temperature (whichever is higher).
 Exposure                  Method 108
 (Storage)                                         Minimum test temperature shall be at least 85C.
                                                ▪ Measurement at 244 hours after test conclusion.
                                                ▪ Unpowered
                                                ▪ 1,000 Cycles
                                                ▪ Lower Temperature of the Chamber: -40C
                                                ▪ Upper Temperature of the Chamber: maximum
                                                   specified operating temperature and shall not
                                                   exceed 125C.
                                                ▪ Dwell Time (Soak Time):
 Temperature
                     4     JESD22-A104                  o 15 minutes minimum,
 Cycling
                                                        o 30 minutes minimum if component weighs
                                                            above 28g
                                                ▪ Transition Time: 1 minute maximum
                                                ▪ Measurement at least 24 hours after test
                                                   conclusion.
                                                ▪ Peeling, flaking, chipping, bubbling or shrinking of
                                                   insulation sleeve is acceptable.
                                                ▪ Rated Voltage
                                                ▪ 1,000 hours
                                                ▪ 85C/85%RH for hybrid and standard.
                           MIL-STD-202
 Humidity Bias       7                          ▪ 60C/90%RH for solid polymers
                           Method 103
                                                ▪ Measurement at 244 hours after test conclusion.
                                                ▪ Peeling, flaking, chipping, bubbling or shrinking of
                                                   insulation sleeve is acceptable.
                                                ▪ 1,000 hours
                                                ▪ Rated Voltage
 High                                           ▪ Temperature of the Chamber: the maximum
                           MIL-STD-202             permissible ambient temperature at which the
 Temperature         8
                           Method 108              capacitor may be continuously operated at rated
 Operating Life
                                                   conditions.
                                                ▪ Measurement at 244 hours after test conclusion.
                                                ▪ Inspect component construction, marking and
                           MIL-STD-883
 External Visual     9                             workmanship.
                           Method 2009          ▪ Pre and Post Electrical Test not required.
                                                ▪ Verify physical dimensions to the applicable
 Physical                                          component detail specification. Note:
                     10    JESD22-B100             User(s) and Suppliers spec.
 Dimensions
                                                ▪ Pre and Post Electrical Test not required.




                                          Page 25 of 107
                                                                              AEC - Q200 - Rev E
                                                                                 March 20, 2023

Automotive Electronics Council
          Component Technical Committee



    Table 3: Stress Qualifications for Aluminum Electrolytic (Hybrid, Polymer and
                           Standard) Capacitors (continued)
 Stress             No.   Reference         Additional Requirements
                                            ▪ Test THT component lead integrity only.
                                            ▪ Test Condition A (pull test):
                                                     Nominal cross- sectional
                                                                                   Force (N)
                                                          area (mm2)
                                                             ≤ 0.05                    1
                                                          0.06 to 0.10                2.5
                                                          0.11 to 0.20                 5
                                                          0.21 to 0.50                10
                                                          0.51 to 1.20                20
                                                             > 1.20                   40
                                            ▪   Test Condition C (wire-lead bend test):
 Terminal                                          Section Modulus (ZX) (mm3)     Force (N)
 Strength (for
                          MIL-STD-202                      ≤ 1.5x10 -3
                                                                                      0.5
 axial and radial   11
                          Method 211                   1.6x10-3 to 4.2x10-3          1.25
 THT
 components)                                           4.3x10-3 to 1.2x10-2           2.5
                                                       1.3x10-2 to 0.5x10-1            5
                                                       0.6x10-1 to 1.9x10-1           10
                                                           > 1.9x10-1                 20
                                                 For round terminations: ZX = (πd3)/32 where d is
                                                 the lead diameter.
                                                 For strip terminations: ZX = (ba2)/6 where a is the
                                                 thickness of the rectangular strip perpendicular to
                                                 the bending axis, b is the other dimension of the
                                                 rectangular strip.
                                            Note: the values and formulas are per IEC 60068-2-21,
                                            6th Edition.
                                            ▪   Capacitors with sleeve in addition to the Method
                                                215 solvents, add an Aqueous wash chemical and
                                                follow chemical manufacturer’s recommended
 Resistance to            MIL-STD-202           parameters (i.e., solution temperature and
                    12                          immersion time).
 Solvents                 Method 215
                                            ▪   All others: follow MIL-STD-202, Method 215
                                            ▪   Applicable to ink marked components and not laser
                                                marked components.
                                            ▪   Figure 1 of Method 213.
 Mechanical               MIL-STD-202       ▪   THT: Condition C
                    13                      ▪   SMD: Condition C
 Shock                    Method 213
                                            ▪   Tested per the Supplier’s recommended mounting
                                                method.




                                        Page 26 of 107
                                                                             AEC - Q200 - Rev E
                                                                                March 20, 2023

Automotive Electronics Council
             Component Technical Committee



    Table 3: Stress Qualifications for Aluminum Electrolytic (Hybrid, Polymer and
                           Standard) Capacitors (continued)
 Stress               No.   Reference            Additional Requirements
                                                 ▪ 5g's for 20 minutes
                                                 ▪ 12 cycles each of 3 orientations.
                                                 ▪ Tested per the Supplier’s recommended mounting
                                                    method.
                                                 ▪ Verification of transfer load: during setup, verify
                            MIL-STD-202             that with the selected PCB design (size, thickness
 Vibration            14                            and secure points), or an alternative mount, that
                            Method 204
                                                    the transferred load onto the component
                                                    corresponds to the requested load. This
                                                    verification can be achieved using a laser
                                                    vibrometer or other adequate measuring device.
                                                 ▪ Test from 10 Hz - 2000 Hz
                                                 ▪   THT: Conditions B or C
                                                 ▪   SMD: Condition J or K, time above 217°C, 60s –
 Resistance to              MIL-STD-202
                      15                             150s
 Soldering Heat             Method 210
                                                 ▪   Non-soldered type mounting/attach are not
                                                     applicable.
                                                 ▪   THT:
                                                        o Method A1, Coating Durability Category 2
                                                 ▪   SMD:
                                                        o Method B1, Coating Durability Category 2
                                                        o Method D, Coating Durability Category 2
                                                 ▪   Note: in particular circumstances when SnPb
                                                     reverse compatibility is requested by the User,
                                                     Method A shall be used for THT and Method B
 Solderability        18    J-STD-002
                                                     shall be used for SMD.
                                                 ▪   Pre and Post Electrical Test not required.
                                                 ▪   Magnification 50x
                                                 ▪   Applicable to axial/radial THT, SMD and snap-in.
                                                 ▪   Does not apply to press-fit or screw-in terminal
                                                     types.
                                                 ▪   Non-soldered type mounting/attach are not
                                                     applicable.
                                                 ▪   Parametrically test per lot and sample size
                                                     requirements
 Electrical                                      ▪   Summary to show minimum, maximum, mean
                      19    User Specification
 Characterization                                    and standard deviation at room, minimum and
                                                     maximum operating temperatures.
                                                 ▪   Pre and Post Electrical Test not required.




                                           Page 27 of 107
                                                                                 AEC - Q200 - Rev E
                                                                                    March 20, 2023

Automotive Electronics Council
          Component Technical Committee



   Table 3: Stress Qualifications for Aluminum Electrolytic (Hybrid, Polymer and
                          Standard) Capacitors (continued)
 Stress             No.    Reference              Additional Requirements
                                                  ▪ Applicable to components with exposed cured
                                                     resins or plastic materials.
                                                  ▪ If exposed resins or plastic materials are V-1, V-0
                                                     or 5VA testing is not required.
                                                  ▪ If exposed resins or plastic materials are not V-1,
                           UL-94 or                  V-0 or 5VA, components or applicable parts of the
 Flammability        20
                           IEC 60695-11-5            component (e.g., sleeve or encapsulant), material
                                                     shall be tested to the Needle Flame Test per IEC
                                                     60695-11-5. Data from previously qualified
                                                     materials can be supplied in place of conducting
                                                     test.
                                                  ▪ Pre and Post Electrical Test not required.
 Board Flex
                     21    AEC-Q200-005
 (SMD)
 Terminal
                     22    AEC-Q200-006
 Strength (SMD)
 Surge Voltage       27    JIS-C-5101-1

      Note: For any deviation from the above stresses, refer to Section 2.4.8.

      Back to Table C: Qualification Sample Size
      Back to Table D: Applicable Stress Qualifications




                                            Page 28 of 107
                                                                                                     AEC - Q200 - Rev E
                                                                                                        March 20, 2023

Automotive Electronics Council
            Component Technical Committee


Table 3A: Aluminum Electrolytic (Hybrid, Polymer and Standard) Capacitors Process
             Change Qualification Guidelines for the Selection of Tests
For a given change listed below, the supplier should justify why a suggested test does not apply for the given
component(s) under consideration. Collaboration with their customer base is highly recommended.

 3.    High Temperature Exposure (Storage)   13.       Mechanical Shock                         27     Surge Voltage
 4.    Temperature Cycling                   14.       Vibration
 7.    Biased Humidity                       15.       Resistance to Soldering Heat
 8.    Operational Life                18.   18.       Solderability
 9.    External Visual                       19.       Electrical Characterization
 10.   Physical Dimension              19.   20.       Flammability
 11.   Terminal Strength (THT)         21.   21.       Board Flex
 12.   Resistance to Solvents          22.   22.       Terminal Strength (SMD)


Note: A letter or "⚫" indicates that performance of that stress test should be considered (not necessarily
required) for the appropriate process change

       Test # From Table 3           3   4   7     8     9    10   11   12   13       14   15   18    19   20   21     22   27
       MATERIAL
       End Seal                          ⚫   ⚫     ⚫     ⚫    ⚫         ⚫                                  ⚫
       Housing                           ⚫                    ⚫               ⚫                            ⚫
       Sleeving                          ⚫         ⚫     ⚫    ⚫         ⚫                                  ⚫
       Lead/Termination                                            ⚫                  ⚫    ⚫    ⚫     B         ⚫      ⚫
       PROCESS
       Curing                            ⚫   ⚫     ⚫          ⚫                                       B                     ⚫
       Impregnation method           ⚫   ⚫         ⚫                                                  B                     ⚫
       Terminal Attach                   ⚫                         ⚫          ⚫            ⚫          B         ⚫      ⚫
       Winding                           ⚫         ⚫                                  ⚫               B
       DESIGN
       Electrolyte Change            ⚫   ⚫         ⚫                                                  B                     ⚫
       Foil Design                       ⚫         ⚫                                                  B                     ⚫
       Insulation Change                 ⚫         ⚫                                                  B                     ⚫
       MISCELLANEOUS
       Mfg. Site Transfer            ⚫   ⚫   ⚫     ⚫     ⚫    ⚫    ⚫    ⚫     ⚫       ⚫    ⚫    ⚫     B    ⚫    ⚫      ⚫    ⚫
       Material Suppliers            ⚫   ⚫   ⚫                     ⚫    ⚫     ⚫       ⚫    ⚫    ⚫     B    ⚫    ⚫      ⚫
       New/Modified Mfg. Equipment       ⚫         ⚫          ⚫    ⚫          ⚫       ⚫               B                     ⚫


                             B = comparative data (unchanged vs. Changed) required




                                                   Page 29 of 107
                                                                              AEC - Q200 - Rev E
                                                                                 March 20, 2023

Automotive Electronics Council
          Component Technical Committee



                     Table 4: Stress Qualifications for Film Capacitors
 Stress              No.   Reference             Additional Requirements
 Pre- and Post-                                  ▪ Test is performed at room temperature except as
 Stress Electrical   1     User Specification.      specified in the applicable stress reference and the
 Test                                               additional requirements in this Table.
                                                 ▪ Unpowered
                                                 ▪ 1,000 hours.
 High                                            ▪ Upper Temperature: maximum specified operating
 Temperature               MIL-STD-202              temperature or maximum specified storage
                     3
 Exposure                  Method 108               temperature (whichever is higher). Minimum test
 (Storage)                                          temperature shall be 85C.
                                                 ▪ Measurement at 244 hours after test conclusion.
                                                 ▪   Unpowered
                                                 ▪   1,000 Cycles
                                                 ▪   Lower Temperature of the Chamber: -55C
                                                 ▪   Upper Temperature of the Chamber: maximum
                                                     permissible ambient temperature at which the
                                                     capacitor may be continuously operated at rated
 Temperature                                         conditions.
                     4     JESD22-A104           ▪   Dwell Time (Soak Time):
 Cycling
                                                         o 15 minutes minimum,
                                                         o 30 minutes minimum if component weighs
                                                              above 28g
                                                 ▪   Transition Time: 1 minute maximum
                                                 ▪   Measurement at least 24 hours after test
                                                     conclusion.
                                                 ▪   Rated Voltage
                           MIL-STD-202           ▪   1,000 hours
 Humidity Bias       7
                           Method 103            ▪   40C/93%RH
                                                 ▪   Measurement at 244 hours after test conclusion.
                                                 ▪   1,000 hours
                                                 ▪   Temperature of the Chamber: the maximum
                                                     permissible ambient temperature at which the
 High                                                capacitor may be continuously operated at rated
                           MIL-STD-202
 Temperature         8                               conditions.
                           Method 108
 Operating Life                                  ▪   125% of rated voltage at 85C.
                                                 ▪   100% of rated voltage above 85C.
                                                 ▪   Measurement at 244 hours after test conclusion.
                                                 ▪   Inspect device construction, marking and
                           MIL-STD-883
 External Visual     9                               workmanship.
                           Method 2009           ▪   Pre and Post Electrical Test not required.
                                                 ▪   Verify physical dimensions to the applicable
 Physical                                            component specification.
                     10    JESD22-B100
 Dimensions                                      ▪   Pre and Post Electrical Test not required.




                                           Page 30 of 107
                                                                              AEC - Q200 - Rev E
                                                                                 March 20, 2023

Automotive Electronics Council
          Component Technical Committee



              Table 4: Stress Qualifications for Film Capacitors (continued)
 Stress             No.   Reference         Additional Requirements
                                            ▪ Test THT component lead integrity only.
                                            ▪ Test Condition A (pull test)
                                                     Nominal cross- sectional
                                                                                   Force (N)
                                                          area (mm2)
                                                             ≤ 0.05                    1
                                                          0.06 to 0.10                2.5
                                                          0.11 to 0.20                 5
                                                          0.21 to 0.50                10
                                                          0.51 to 1.20                20
                                                             > 1.20                   40
                                            ▪   Test Condition C (wire-lead bend test):
 Terminal                                          Section Modulus (ZX) (mm3)      Force (N)
 Strength (for
                          MIL-STD-202                      ≤ 1.5x10 -3
                                                                                      0.5
 axial and radial   11
                          Method 211                   1.6x10-3 to 4.2x10-3          1.25
 THT
 components)                                           4.3x10-3 to 1.2x10-2           2.5
                                                       1.3x10-2 to 0.5x10-1            5
                                                       0.6x10-1 to 1.9x10-1           10
                                                           > 1.9x10-1                 20
                                                 For round terminations: ZX = (πd3)/32 where d is
                                                 the lead diameter.
                                                 For strip terminations: ZX = (ba2)/6 where a is the
                                                 thickness of the rectangular strip perpendicular to
                                                 the bending axis, b is the other dimension of the
                                                 rectangular strip.
                                            Note: the values and formulas are per IEC 60068-2-21,
                                            6th Edition
                                            ▪   In addition to the Method 215 solvents, add an
                                                Aqueous wash chemical and follow chemical
 Resistance to            MIL-STD-202           manufacturer’s recommended parameters (i.e.,
                    12                          solution temperature and immersion time).
 Solvents                 Method 215
                                            ▪   Applicable to ink marked components and not laser
                                                marked components.
                                            ▪   Figure 1 of Method 213
                                            ▪   THT: Condition C
 Mechanical               MIL-STD-202       ▪   SMD: Condition C
                    13
 Shock                    Method 213        ▪   Tested per the Supplier’s recommended mounting
                                                method.




                                        Page 31 of 107
                                                                                AEC - Q200 - Rev E
                                                                                   March 20, 2023

Automotive Electronics Council
            Component Technical Committee



                 Table 4: Stress Qualifications for Film Capacitors (continued)
 Stress               No.   Reference             Additional Requirements
                                                  ▪ 5g's for 20 minutes
                                                  ▪ 12 cycles each of 3 orientations.
                                                  ▪ Tested per the Supplier’s recommended mounting
                                                     method.
                                                  ▪ Verification of transfer load: during setup, verify that
                             MIL-STD-202             with the selected PCB design (size, thickness and
Vibration             14                             secure points), or an alternative mount, that the
                            Method 204
                                                     transferred load onto the component corresponds
                                                     to the requested load. This verification can be
                                                     achieved using a laser vibrometer or other
                                                     adequate measuring device.
                                                  ▪ Test from 10 Hz - 2000 Hz
                                                  ▪   THT: Conditions B or C
                                                  ▪   SMD: Condition J or K, time above 217°C, 60s –
 Resistance to              MIL-STD-202               150s
                      15
 Soldering Heat             Method 210            ▪   Non-soldered type mounting/attach are not
                                                      applicable.
                                                  ▪   Not applicable for charges V x C (nF) ≥ 100
 ESD                  17    AEC-Q200-002
                                                  ▪   THT:
                                                         o Method A1, Coating Durability Category 2
                                                  ▪   SMD:
                                                         o Method B1, Coating Durability Category 2
                                                         o Method D, Coating Durability Category 2
                                                  ▪   Note: in particular circumstances when SnPb
 Solderability        18    J-STD-002                 reverse compatibility is requested by the User,
                                                      Method A shall be used for THT and Method B
                                                      shall be used for SMD.
                                                  ▪   Magnification 50x
                                                  ▪   Pre and Post Electrical Test not required.
                                                  ▪   Non-soldered type mounting/attach are not
                                                      applicable.
                                                  ▪   Parametrically test per lot and sample size
                                                      requirements.
 Electrical                                       ▪   Summary to show minimum, maximum, mean
                      19    User Specification.
 Characterization                                     and standard deviation at room, minimum and
                                                      maximum operating temperatures.
                                                  ▪   Pre and Post Electrical Test not required.




                                            Page 32 of 107
                                                                                 AEC - Q200 - Rev E
                                                                                    March 20, 2023

Automotive Electronics Council
          Component Technical Committee



               Table 4: Stress Qualifications for Film Capacitors (continued)
 Stress             No.    Reference              Additional Requirements
                                                  ▪ Applicable to components with exposed cured
                                                     resins or plastic materials.
                                                  ▪ If exposed resins or plastic materials are V-1, V-0
                                                     or 5VA testing is not required.
                                                  ▪ If exposed resins or plastic materials are not V-1,
                           UL-94 or                  V-0 or 5VA, components or applicable parts of the
Flammability         20                              component (e.g., sleeve or encapsulant), material
                          IEC 60695-11-5
                                                     shall be tested to the Needle Flame Test per IEC
                                                     60695-11-5. Data from previously qualified
                                                     materials can be supplied in place of conducting
                                                     test.
                                                  ▪ Pre and Post Electrical Test not required.
 Board Flex
                     21    AEC-Q200-005
 (SMD)
 Terminal
                     22    AEC-Q200-006
 Strength (SMD)

      Note: For any deviation from the above stresses, refer to Section 2.4.8.

      Back to Table C: Qualification Sample Size
      Back to Table D: Applicable Stress Qualifications




                                            Page 33 of 107
                                                                                                            AEC - Q200 - Rev E
                                                                                                               March 20, 2023

Automotive Electronics Council
             Component Technical Committee


Table 4A: Film Capacitors Process Change Qualification Guidelines for the Selection
                                    of Tests
For a given change listed below, the Supplier should justify why a suggested test does not apply for the given
component(s) under consideration. Collaboration with their customer base is highly recommended.

 3.     High Temperature Exposure (Storage)       13.       Mechanical Shock                          22.     Terminal Strength (SMD)
 4.     Temperature Cycling                       14.       Vibration
 7.     Biased Humidity                           15.       Resistance to Soldering Heat
 8.     Operational Life                          17.       Electrostatic Discharge (ESD)
 9.     External Visual                           18.       Solderability
 10.    Physical Dimension                        19.       Electrical Characterization
 11.    Terminal Strength (THT)                   20.       Flammability
 12.    Resistance to Solvents                    21.       Board Flex


Note: A letter or "⚫" indicates that performance of that stress test should be considered (not necessarily
required) for the appropriate process change

       Test # From Table 4            3       4   7     8      9   10   11    12   13       14   15    17    18   19   20   21   22
       MATERIAL
       Epoxy                          ⚫       ⚫   ⚫     ⚫      ⚫    ⚫         ⚫     ⚫       ⚫                          ⚫
       Housing                                ⚫   ⚫     ⚫      ⚫    ⚫    ⚫          ⚫       ⚫                ⚫
       Lead/Termination                                             ⚫    ⚫          ⚫            ⚫           ⚫    B         ⚫    ⚫
       PROCESS
       Epoxy Fill                     ⚫       ⚫   ⚫     ⚫      ⚫              ⚫
       Terminal attach                        ⚫         ⚫                ⚫    ⚫                                   B         ⚫    ⚫
       Winding                        ⚫                 ⚫                                               ⚫         B
       DESIGN
       Foil Design                            ⚫         ⚫                                               ⚫         B
       Insulation Change                      ⚫         ⚫                                               ⚫         B
       MISCELLANEOUS
       Mfg. Site Transfer             ⚫       ⚫   ⚫     ⚫      ⚫    ⚫    ⚫    ⚫     ⚫       ⚫    ⚫      ⚫    ⚫    B    ⚫    ⚫    ⚫
       Material Suppliers             ⚫       ⚫         ⚫                ⚫    ⚫             ⚫    ⚫           ⚫         ⚫         ⚫
       New/Modified Mfg. Equipment            ⚫         ⚫                ⚫                              ⚫         B              ⚫


                              B = comparative data (unchanged vs. Changed) required




                                                        Page 34 of 107
                                                                              AEC - Q200 - Rev E
                                                                                 March 20, 2023

Automotive Electronics Council
          Component Technical Committee




         Table 5: Stress Qualifications for Magnetics (Inductors/Transformers)
 Stress              No.   Reference             Additional Requirements
 Pre- and Post-                                  ▪ Test is performed at room temperature except as
 Stress Electrical   1     User Specification.      specified in the applicable stress reference and the
 Test                                               additional requirements in this Table.
                                                 ▪ Unpowered
 High                                            ▪ 1,000 hours
 Temperature               MIL-STD-202           ▪ Upper Temperature: maximum specified operating
                     3                              temperature or maximum specified storage
 Exposure                  Method 108
 (Storage)                                          temperature (whichever is higher).
                                                 ▪ Measurement at 244 hours after test conclusion.
                                                 ▪   Unpowered
                                                 ▪   1,000 Cycles
                                                 ▪   Lower Temperature of the Chamber: -40C
                                                 ▪   Upper Temperature of the Chamber: maximum
                                                     specified operating temperature and shall not
                                                     exceed 125C.
 Temperature
                     4     JESD22-A104           ▪   Dwell Time (Soak Time):
 Cycling
                                                         o 15 minutes minimum,
                                                         o 30 minutes minimum if component weighs
                                                              above 28g
                                                 ▪   Transition Time: 1 minute maximum
                                                 ▪   Measurement at least 24 hours after test
                                                     conclusion.
                                                 ▪   Unpowered
                           MIL-STD-202           ▪   1,000 hours
 Humidity Bias       7
                           Method 103            ▪   85C/85%RH
                                                 ▪   Measurement at 244 hours after test conclusion.
                                                 ▪   1,000 hours
                                                 ▪   Upper Temperature of the Chamber: maximum
 High                                                specified operating temperature (not including
                           MIL-STD-202
 Temperature         8                               heat rise) at maximum rated power and shall not
                           Method 108
 Operating Life
                                                     exceed 125C.
                                                 ▪   Measurement at 244 hours after test conclusion.
                                                 ▪   Inspect device construction, marking and
                           MIL-STD-883               workmanship.
 External Visual     9
                           Method 2009           ▪   Pre and Post Electrical Test not required.
                                                 ▪   Verify physical dimensions to the applicable
 Physical                                            component detail specification.
                     10    JESD22-B100
 Dimensions                                      ▪   Pre and Post Electrical Test not required.




                                           Page 35 of 107
                                                                                AEC - Q200 - Rev E
                                                                                   March 20, 2023

Automotive Electronics Council
             Component Technical Committee




 Table 5: Stress Qualifications for Magnetics (Inductors/Transformers) (continued)
 Stress               No.   Reference          Additional Requirements
                                               ▪ Test THT component lead integrity only.
                                               ▪ Test Condition A (pull test)
                                                       Nominal cross- sectional
                                                                                     Force (N)
                                                            area (mm2)
                                                               ≤ 0.05                    1
                                                            0.06 to 0.10                2.5
                                                            0.11 to 0.20                 5
                                                            0.21 to 0.50                10
                                                            0.51 to 1.20                20
                                                               > 1.20                   40
                                               ▪   Test Condition C (wire-lead bend test):
 Terminal                                             Section Modulus (ZX) (mm3)     Force (N)
 Strength (for
                            MIL-STD-202                      ≤ 1.5x10 -3
                                                                                        0.5
 axial and radial     11
                            Method 211                   1.6x10-3 to 4.2x10-3          1.25
 THT
 components)                                             4.3x10-3 to 1.2x10-2           2.5
                                                         1.3x10-2 to 0.5x10-1            5
                                                         0.6x10-1 to 1.9x10-1           10
                                                             > 1.9x10-1                 20
                                                   For round terminations: ZX = (πd3)/32 where d is
                                                   the lead diameter.
                                                   For strip terminations: ZX = (ba2)/6 where a is the
                                                   thickness of the rectangular strip perpendicular to
                                                   the bending axis, b is the other dimension of the
                                                   rectangular strip.
                                               ▪   Note: the values and formulas are per IEC 60068-
                                                   2-21, 6th Edition
                                               ▪   In addition to the Method 215 solvents, add an
                                                   Aqueous wash chemical and follow chemical
 Resistance to              MIL-STD-202            manufacturer’s recommended parameters (i.e.,
                      12                           solution temperature and immersion time).
 Solvents                   Method 215
                                               ▪   Applicable to ink marked components and not laser
                                                   marked components
                                               ▪   Figure 1 of Method 213.
                                               ▪   THT: Condition C
 Mechanical                 MIL-STD-202        ▪   SMD: Condition C
                      13
 Shock                      Method 213         ▪   Tested per the Supplier’s recommended mounting
                                                   method
 Vibration            14    MIL-STD-202        ▪   5g's for 20 minutes
                            Method 204         ▪   12 cycles each of 3 orientations.
                                               ▪   Tested per the Supplier’s recommended
                                                   mounting method
                                               ▪   Verification of transfer load: during setup, verify
                                                   that with the selected PCB design (size, thickness
                                                   and secure points), or an alternative mount, that
                                                   the transferred load onto the component
                                                   corresponds to the requested load. This
                                                   verification can be achieved using a laser
                                                   vibrometer or other adequate measuring device.
                                               ▪   Test from 10 Hz - 2000 Hz.

                                          Page 36 of 107
                                                                                  AEC - Q200 - Rev E
                                                                                     March 20, 2023

Automotive Electronics Council
          Component Technical Committee




 Table 5: Stress Qualifications for Magnetics (Inductors/Transformers) (continued)
 Stress              No.    Reference              Additional Requirements
                                                   ▪ THT: Conditions B or C
Resistance to               MIL-STD-202            ▪ SMD: Condition K, time above 217°C, 60s – 150s
                      15                           ▪ Non-soldered type mounting/attach are not
Soldering Heat             Method 210
                                                      applicable

 ESD                  17    AEC-Q200-002
                                                   ▪   Through-hole Technology (THT:
                                                          o Method A1, Coating Durability Category 2
                                                   ▪   SMD:
                                                          o Method B1, Coating Durability Category 2
                                                          o Method D, Coating Durability Category 2
                                                   ▪   Note: in particular circumstances when SnPb
 Solderability        18    J-STD-002                  reverse compatibility is requested by the User,
                                                       Method A shall be used for THT and Method B
                                                       shall be used for SMD.
                                                   ▪   Magnification 50x
                                                   ▪   Pre and Post Electrical Test not required.
                                                   ▪   Non-soldered type mounting/attach are not
                                                       applicable.
                                                   ▪   Parametrically test per lot and sample size
                                                       requirements,(inductance only unless otherwise
                                                       agreed upon)
 Electrical                                        ▪   Summary to show minimum, maximum, mean
                      19    User Specification.
 Characterization                                      and standard deviation at room, minimum and
                                                       maximum operating temperatures.
                                                   ▪   Pre and Post Electrical Test not required
                                                   ▪   Applicable to components with exposed cured
                                                       resins or plastic materials.
                                                   ▪   If exposed resins or plastic materials are V-1, V-0
                                                       or 5VA, testing is not required.
                                                   ▪   If exposed resins or plastic materials are not V-1,
                            UL-94 or                   V-0 or 5VA, components or applicable parts of the
 Flammability         20                               component (e.g., sleeve or encapsulant), material
                            IEC 60695-11-5
                                                       shall be tested to the Needle Flame Test per IEC
                                                       60695-11-5. Data from previously qualified
                                                       materials can be supplied in place of conducting
                                                       test.
                                                   ▪   Pre and Post Electrical Test not required.
 Board Flex
                      21    AEC-Q200-005
 (SMD)
 Terminal
                      22    AEC-Q200-006
 Strength (SMD)


       Note: For any deviation from the above stresses, refer to Section 2.4.8.

       Back to Table C: Qualification Sample Size
       Back to Table D: Applicable Stress Qualifications


                                             Page 37 of 107
                                                                                                  AEC - Q200 - Rev E
                                                                                                     March 20, 2023

Automotive Electronics Council
            Component Technical Committee


       Table 5A: Magnetics (Inductors/Transformers) Process Change Qualification
                          Guidelines for the Selection of Tests
For a given change listed below, the Supplier should justify why a suggested test does not apply for the given
components under consideration. Collaboration with their customer base is highly recommended.

 3.     High Temperature Exposure (Storage)       13.   Mechanical Shock                          22.       Terminal Strength (SMD)
 4.     Temperature Cycling                       14.   Vibration
 7.     Biased Humidity                           15.   Resistance to Soldering Heat
 8.     Operational Life                          17.   Electrostatic Discharge (ESD)
 9.     External Visual                           18.   Solderability
 10.    Physical Dimension                        19.   Electrical Characterization
 11.    Terminal Strength (THT)                   20.   Flammability
 12.    Resistance to Solvents                    21.   Board Flex



Note: A letter or "⚫" indicates that performance of that stress test should be considered (not necessarily
required) for the appropriate process change

         Test # From Table 5        3    4    7     8   9   10   11   12    13   14     15   17   18    19     20   21   22
         MATERIAL
         Bobbin material            ⚫    ⚫    ⚫     ⚫   ⚫                   ⚫                                  ⚫
         Core material                   ⚫          ⚫   ⚫                   ⚫                           B      ⚫
         Insulation material        ⚫    ⚫    ⚫     ⚫   ⚫              ⚫                ⚫    a          B      ⚫
         Lead material                              ⚫   ⚫        ⚫               ⚫      ⚫         ⚫                 ⚫    ⚫
         Mold material              ⚫    ⚫    ⚫     ⚫   ⚫              ⚫    ⚫                           B      ⚫
         Solder material                 ⚫              ⚫        ⚫          ⚫    ⚫                ⚫                 ⚫    ⚫
         Wire/foil material                   ⚫     ⚫   ⚫                                    ⚫          B           ⚫    ⚫
         PROCESS
         Insulation strip                               ⚫              ⚫                ⚫
         Lead prep/plating               ⚫              ⚫        ⚫               ⚫      ⚫         ⚫                 ⚫    ⚫
         Terminal Attach                 ⚫              ⚫        ⚫          ⚫    ⚫      a         ⚫
         Marking                                        ⚫              ⚫
         Molding                    ⚫    ⚫    ⚫     ⚫   ⚫   ⚫          ⚫    ⚫                           B      ⚫
         Soldering                       ⚫              ⚫        ⚫               ⚫                ⚫                 ⚫    ⚫
         Winding - Insulation                 ⚫     ⚫                  ⚫                ⚫    a          B
         Winding - Wire                             ⚫   ⚫                                               B
         DESIGN
         Bobbin                          ⚫              ⚫   ⚫               ⚫                ⚫          B
         Core                            ⚫              ⚫   ⚫               ⚫    ⚫                      B
         Insulation system                    ⚫     ⚫   ⚫   ⚫          ⚫                ⚫    a          B      ⚫
         Lead                                           ⚫   ⚫    ⚫               ⚫      ⚫    ⚫    ⚫                 ⚫    ⚫
         Mold                            ⚫              ⚫   ⚫          ⚫    ⚫                           B
         Wire/foil                       ⚫              ⚫   ⚫                                           B           ⚫    ⚫
         MISCELLANEOUS
         Mfg. Site Transfer         ⚫    ⚫          ⚫            ⚫                      ⚫               B                ⚫
         Material Suppliers              ⚫              ⚫   ⚫    ⚫                                      B
         Process Control Change                         ⚫   ⚫


             a = Multilayer only                  B = comparative data (unchanged vs. Changed) required




                                                    Page 38 of 107
                                                                               AEC - Q200 - Rev E
                                                                                  March 20, 2023

Automotive Electronics Council
          Component Technical Committee



                     Table 6: Stress Qualifications for Networks (R-C/C/R)
 Stress               No.   Reference             Additional Requirements
 Pre- and Post-                                   ▪ Test is performed at room temperature except as
 Stress Electrical     1    User Specification.      specified in the applicable stress reference and the
 Test                                                additional requirements in this Table.
                                                  ▪ Tested at maximum specified operating
                                                     temperature or maximum specified storage
 High                                                temperature (whichever is higher). Minimum
 Temperature                MIL-STD-202              test temperature shall be 85C.
                       3
 Exposure                   Method 108            ▪ 1,000 hours.
 (Storage)                                        ▪ Unpowered
                                                  ▪ Measurement at 244 hours after test conclusion.
                                                  ▪   Unpowered
                                                  ▪   1,000 Cycles
                                                  ▪   Lower Temperature of the Chamber: -55C
                                                  ▪   Upper Temperature of the Chamber: maximum
                                                      specified operating temperature.
 Temperature                                      ▪   Dwell Time (Soak Time):
                       4    JESD22-A104
 Cycling                                                  o 15 minutes minimum,
                                                          o 30 minutes minimum if component weighs
                                                               above 28g
                                                  ▪   Transition Time: 1 minute maximum
                                                  ▪   Measurement at least 24 hours after test
                                                      conclusion.
                                                  ▪   1,000 hours
                                                  ▪   85C/85%RH
                                                  ▪   Capacitor Networks: Rated Voltage
                            MIL-STD-202
 Humidity Bias         7                          ▪   Resistor Networks: 10% Rated Power (for
                            Method 103
                                                      components with specified operating voltages
                                                      higher or equal to 500V, 10% of operating voltage).
                                                  ▪   Measurement at 244 hours after test conclusion.
                                                  ▪   1,000 hours
                                                  ▪   Temperature of the Chamber: maximum specified
                                                      operating temperature at maximum rated voltage
 High                                             ▪
                            MIL-STD-202               Capacitor Networks: rated voltage
 Temperature           8
                            Method 108            ▪   Resistor Networks: Power shall be applied to the
 Operating Life
                                                      component intermittently: 90 minutes ON and 30
                                                      minutes OFF.
                                                  ▪   Measurement at 244 hours after test conclusion.
                                                  ▪   Inspect device construction, marking and
                            MIL-STD-883
 External Visual       9                              workmanship.
                            Method 2009           ▪   Pre and Post Electrical Test not required.
                                                  ▪   Verify physical dimensions to the applicable
 Physical                                             component specification.
                      10    JESD22-B100
 Dimensions                                       ▪   Pre and Post Electrical Test not required.




                                            Page 39 of 107
                                                                              AEC - Q200 - Rev E
                                                                                 March 20, 2023

Automotive Electronics Council
          Component Technical Committee



            Table 6: Stress Qualifications for Networks (R-C/C/R) (continued)



 Stress             No.   Reference         Additional Requirements
                                            ▪ Test THT component lead integrity only.
                                            ▪ Test Condition A (pull test):
                                                  Nominal cross- sectional area
                                                                                   Force (N)
                                                             (mm2)
                                                             ≤ 0.05                    1
                                                          0.06 to 0.10                2.5
                                                          0.11 to 0.20                 5
                                                          0.21 to 0.50                10
                                                          0.51 to 1.20                20
                                                             > 1.20                   40
                                            ▪   Test Condition C (wire-lead bend test):
 Terminal                                          Section Modulus (ZX) (mm3)     Force (N)
 Strength (for
                          MIL-STD-202                      ≤ 1.5x10 -3
                                                                                      0.5
 axial and radial   11
                          Method 211                   1.6x10-3 to 4.2x10-3          1.25
 THT
                                                       4.3x10-3 to 1.2x10-2           2.5
 components)
                                                       1.3x10-2 to 0.5x10-1            5
                                                       0.6x10-1 to 1.9x10-1           10
                                                           > 1.9x10-1                 20
                                                 For round terminations: ZX = (πd3)/32 where d is
                                                 the lead diameter.
                                                 For strip terminations: ZX = (ba2)/6 where a is the
                                                 thickness of the rectangular strip perpendicular to
                                                 the bending axis, b is the other dimension of the
                                                 rectangular strip.
                                            Note: the values and formulas are per IEC 60068-2-21,
                                            6th Edition
                                            ▪   In addition to the Method 215 solvents, add an
                                                Aqueous wash chemical and follow chemical
 Resistance to            MIL-STD-202           manufacturer’s recommended parameters (i.e.,
                    12                          solution temperature and immersion time).
 Solvents                 Method 215
                                            ▪   Applicable to ink marked components and not laser
                                                marked components.
                                            ▪   Figure 1 of Method 213
                                            ▪   THT: Condition C
 Mechanical               MIL-STD-202       ▪   SMD: Condition C
                    13
 Shock                    Method 213        ▪   Tested per the Supplier’s recommended mounting
                                                method.




                                        Page 40 of 107
                                                                               AEC - Q200 - Rev E
                                                                                  March 20, 2023

Automotive Electronics Council
             Component Technical Committee



              Table 6: Stress Qualifications for Networks (R-C/C/R) (continued)
 Stress               No.   Reference            Additional Requirements
                                                 ▪ 5g's for 20 minutes
                                                 ▪ 12 cycles each of 3 orientations.
                                                 ▪ Tested per the Supplier’s recommended mounting
                                                    method.
                                                 ▪ Verification of transfer load: during setup, verify that
                            MIL-STD-202             with the selected PCB design (size, thickness and
 Vibration            14                            secure points), or an alternative mount, that the
                            Method 204
                                                    transferred load onto the component corresponds
                                                    to the requested load. This verification can be
                                                    achieved using a laser vibrometer or other
                                                    adequate measuring device.
                                                 ▪ Test from 10 Hz - 2000 Hz
                                                 ▪   THT: within 1.5mm of component body Condition B
                                                     C, or D
 Resistance to              MIL-STD-202          ▪   SMD: Condition K, time above 217°C, 60s – 150s
                      15
 Soldering Heat             Method 210           ▪   Non-soldered type mounting/attach are not
                                                     applicable.

 ESD                  17    AEC-Q200-002
                                                 ▪   Through-hole Technology (THT:
                                                        o Method A1, Coating Durability Category 2
                                                 ▪   SMD:
                                                        o Method B1, Coating Durability Category 2
                                                        o Method D, Coating Durability Category 2
                                                 ▪   Note: in particular circumstances when SnPb
 Solderability        18    J-STD-002                reverse compatibility is requested by the User,
                                                     Method A shall be used for THT and Method B
                                                     shall be used for SMD.
                                                 ▪   Magnification 50x
                                                 ▪   Pre and Post Electrical Test not required.
                                                 ▪   Non-soldered type mounting/attach are not
                                                     applicable.
                                                 ▪   Parametrically test per lot and sample size
                                                     requirements
 Electrical                                      ▪   Summary to show minimum, maximum, mean
                      19    User Specification       and standard deviation at room, minimum and
 Characterization
                                                     maximum operating temperatures.
                                                 ▪   Pre and Post Electrical Test not required.




                                           Page 41 of 107
                                                                                 AEC - Q200 - Rev E
                                                                                    March 20, 2023

Automotive Electronics Council
          Component Technical Committee



              Table 6: Stress Qualifications for Networks (R-C/C/R) (continued)
 Stress              No.   Reference              Additional Requirements
                                                  ▪ Applicable to components with exposed cured
                                                     resins or plastic materials.
                                                  ▪ If exposed resins or plastic materials are V-1, V-0
                                                     or 5VA, testing is not required.
                                                  ▪ If exposed resins or plastic materials are not V-1,
                           UL-94 or                  V-0 or 5VA, components or applicable parts of the
 Flammability        20                              component (e.g., sleeve or encapsulant), material
                           IEC 60695-11-5
                                                     shall be tested to the Needle Flame Test per IEC
                                                     60695-11-5. Data from previously qualified
                                                     materials can be supplied in place of conducting
                                                     test.
                                                  ▪ Pre and Post Electrical Test not required.

 Board Flex
                     21    AEC-Q200-005
 (SMD)

 Terminal
                     22    AEC-Q200-006
 Strength (SMD)
 Flame
                     24    AEC-Q200-001
 Retardance

      Note: For any deviation from the above stresses, refer to Section 2.4.8.

      Back to Table C: Qualification Sample Size
      Back to Table D: Applicable Stress Qualifications




                                            Page 42 of 107
                                                                                                     AEC - Q200 - Rev E
                                                                                                        March 20, 2023

Automotive Electronics Council
                  Component Technical Committee


       Table 6A: Networks (R-C/C/R) Process Change Qualification Guidelines for the
                                    Selection of Tests
For a given change listed below, the Supplier should justify why a suggested test does not apply for the given
component(s) under consideration. Collaboration with their customer base is highly recommended.

 3.       High Temperature Exposure (Storage)       13.   Mechanical Shock                     22.       Terminal Strength (SMD)
 4.       Temperature Cycling                       14.   Vibration                            24        Flame Retardance
 7.       Biased Humidity                           15.   Resistance to Soldering Heat
 8.       Operational Life                          17.   Electrostatic Discharge (ESD)
 9.       External Visual                           18.   Solderability
 10.      Physical Dimension                        19.   Electrical Characterization
 11.      Terminal Strength (THT)                   20.   Flammability
 12.      Resistance to Solvents                    21.   Board Flex


Note: A letter or "⚫" indicates that performance of that stress test should be considered (not necessarily
required) for the appropriate process change

       Test # From Table 6            3    4    7    8    9   10   11   12 13    14       15   17    18 19     20 21     22   24
       MATERIAL
       Ink/Wire Material              ⚫    ⚫         ⚫             W                           F           B        ⚫    ⚫    R
       Package                        ⚫    ⚫    ⚫         ⚫   ⚫    ⚫    ⚫         ⚫            ⚫                ⚫   ⚫    ⚫    R
       Passivation                    ⚫    ⚫    ⚫    ⚫                  ⚫                                       ⚫             R
       Substrate Material                  ⚫    ⚫    ⚫             ⚫                      ⚫          ⚫     B        ⚫    ⚫
       PROCESS
       Ink Fire                            ⚫         ⚫             R                                       B
       Ink Print                      ⚫    ⚫         ⚫             R                                       B        R    R    R
       Laser Trim                               ⚫    ⚫                                                     B
       Lead Form                                ⚫         ⚫   ⚫    ⚫                                 ⚫     B
       Termination Attach                       ⚫                  ⚫        ⚫             ⚫                B
       Marking                                            ⚫             ⚫
       Molding                        ⚫    ⚫    ⚫         ⚫   ⚫    ⚫    ⚫         ⚫            ⚫                ⚫   ⚫    ⚫    R
       DESIGN
       Package                        ⚫    ⚫    ⚫         ⚫   ⚫    ⚫    ⚫         ⚫       ⚫    ⚫     ⚫          ⚫   ⚫    ⚫    R
       Passivation                    ⚫    ⚫    ⚫    ⚫                  ⚫                                       ⚫             R
       Res/Cap Tolerance              ⚫    ⚫         ⚫                                    ⚫    ⚫           B
       Res/Cap Value                  ⚫    ⚫         ⚫                                    ⚫    ⚫           B                  R
       MISCELLANEOUS
       Mfg. Site Transfer             ⚫    ⚫    ⚫    ⚫    ⚫   ⚫    ⚫    ⚫                 ⚫    ⚫           B        ⚫    ⚫    R
       Material Suppliers                  ⚫                  ⚫    ⚫    ⚫                 ⚫    ⚫           B    ⚫             R
       New/Modified Mfg. Equipment         ⚫         ⚫                                         ⚫           B


              B = comparative data (unchanged vs. Changed) required     F = Film products only
                             R = Resistors Only    W = Wirewound products only




                                                      Page 43 of 107
                                                                              AEC - Q200 - Rev E
                                                                                 March 20, 2023

Automotive Electronics Council
          Component Technical Committee




                           Table 7: Stress Qualifications for Resistors
 Stress              No.   Reference             Additional Requirements
 Pre- and Post-                                  ▪ Test is performed at room temperature except as
 Stress Electrical   1     User Specification.      specified in the applicable stress reference and the
 Test                                               additional requirements in this Table.
                                                 ▪ Upper Temperature: maximum specified operating
                                                    temperature or maximum specified storage
 High                                               temperature (whichever is higher). Minimum test
 Temperature               MIL-STD-202
                     3                              temperature shall be 85C.
 Exposure                  Method 108
                                                 ▪ 1,000 hours
 (Storage)
                                                 ▪ Unpowered
                                                 ▪ Measurement at 244 hours after test conclusion.
                                                 ▪ Unpowered
                                                 ▪ 1,000 Cycles
                                                 ▪ Lower Temperature of the Chamber: -55C
                                                 ▪ Upper Temperature of the Chamber: maximum
                                                    specified operating temperature but shall not
                                                    exceed 155C
 Temperature
                     4     JESD22-A104           ▪ Dwell Time (Soak Time):
 Cycling
                                                         o 15 minutes minimum,
                                                         o 30 minutes minimum if component weighs
                                                             above 28g
                                                 ▪ Transition Time: 1 minute maximum
                                                 ▪ Measurement at least 24 hours after test
                                                    conclusion.
                                                 ▪ 1,000 hours
                                                 ▪ 85C/85%RH
                           MIL-STD-202           ▪ 10% of operating power (for components with
 Humidity Bias       7
                           Method 103               specified operating voltages higher or equal to
                                                    500V, 10% of operating voltage)
                                                 ▪ Measurement at 244 hours after test conclusion.
                                                 ▪ 1,000 hours
                                                 ▪ Power shall be applied to the component
 High                                               intermittently: 90 minutes ON and 30 minutes OFF
                           MIL-STD-202           ▪ Temperature of the Chamber: maximum specified
 Temperature         8
                           Method 108               operating temperature at 100% rated power without
 Operating Life
                                                    derating
                                                 ▪ Measurement at 244 hours after test conclusion.
                                                 ▪   Inspect device construction, marking and
                           MIL-STD-883
 External Visual     9                               workmanship.
                           Method 2009
                                                 ▪   Pre and Post Electrical Test not required.
                                                 ▪   Verify physical dimensions to the applicable
 Physical                                            component specification.
                     10    JESD22-B100
 Dimensions                                      ▪   Pre and Post Electrical Test not required.




                                           Page 44 of 107
                                                                              AEC - Q200 - Rev E
                                                                                 March 20, 2023

Automotive Electronics Council
          Component Technical Committee




                    Table 7: Stress Qualifications for Resistors (continued)
 Stress             No.   Reference         Additional Requirements
                                            ▪ Test THT component lead integrity only.
                                            ▪ Test Condition A (pull test):
                                                  Nominal cross- sectional area
                                                                                   Force (N)
                                                             (mm2)
                                                             ≤ 0.05                    1
                                                          0.06 to 0.10                2.5
                                                          0.11 to 0.20                 5
                                                          0.21 to 0.50                10
                                                          0.51 to 1.20                20
                                                             > 1.20                   40
                                            ▪   Test Condition C (wire-lead bend test):
 Terminal                                          Section Modulus (ZX) (mm3)     Force (N)
 Strength (for
                          MIL-STD-202                      ≤ 1.5x10 -3
                                                                                      0.5
 axial and radial   11
                          Method 211                   1.6x10-3 to 4.2x10-3          1.25
 THT
                                                       4.3x10-3 to 1.2x10-2           2.5
 components)
                                                       1.3x10-2 to 0.5x10-1            5
                                                       0.6x10-1 to 1.9x10-1           10
                                                           > 1.9x10-1                 20
                                                 For round terminations: ZX = (πd3)/32 where d is
                                                 the lead diameter.
                                                 For strip terminations: ZX = (ba2)/6 where a is the
                                                 thickness of the rectangular strip perpendicular to
                                                 the bending axis, b is the other dimension of the
                                                 rectangular strip.
                                            Note: the values and formulas are per IEC 60068-2-21,
                                            6th Edition.
                                            ▪   In addition to the Method 215 solvents, add an
                                                Aqueous wash chemical and follow chemical
 Resistance to            MIL-STD-202           manufacturer’s recommended parameters (i.e.,
                    12                          solution temperature and immersion time).
 Solvents                 Method 215
                                            ▪   Applicable to ink marked components and not laser
                                                marked components.
                                            ▪   Figure 1 of Method 213
                                            ▪   THT: Condition C
 Mechanical               MIL-STD-202       ▪   SMD: Condition C
                    13
 Shock                    Method 213        ▪   Tested per the Supplier’s recommended mounting
                                                method




                                        Page 45 of 107
                                                                                AEC - Q200 - Rev E
                                                                                   March 20, 2023

Automotive Electronics Council
             Component Technical Committee




                     Table 7: Stress Qualifications for Resistors (continued)
 Stress               No.   Reference             Additional Requirements
                                                  ▪ 5g's for 20 minutes
                                                  ▪ 12 cycles each of 3 orientations.
                                                  ▪ Tested per the Supplier’s recommended mounting
                                                     method
                                                  ▪ Verification of transfer load: during setup, verify that
                            MIL-STD-202              with the selected PCB design (size, thickness and
 Vibration            14                             secure points), or an alternative mount, that the
                            Method 204
                                                     transferred load onto the component corresponds
                                                     to the requested load. This verification can be
                                                     achieved using a laser vibrometer or other
                                                     adequate measuring device.
                                                  ▪ Test from 10 Hz - 2000 Hz
                                                  ▪   THT: within 1.5mm of device body, Condition B, C
                                                      or D
 Resistance to              MIL-STD-202           ▪   SMD: Condition K, time above 217°C, 60s – 150s
                      15
 Soldering Heat             Method 210            ▪   Non-soldered type mounting/attach are not
                                                      applicable.

 ESD                  17    AEC-Q200-002
                                                  ▪   Through-hole Technology (THT:
                                                         o Method A1, Coating Durability Category 2
                                                  ▪   SMD:
                                                         o Method B1, Coating Durability Category 2
                                                         o Method D, Coating Durability Category 2
                                                  ▪   Note: in particular circumstances when SnPb
 Solderability        18    J-STD-002                 reverse compatibility is requested by the User,
                                                      Method A shall be used for THT and Method B
                                                      shall be used for SMD.
                                                  ▪   Magnification 50x
                                                  ▪   Pre and Post Electrical Test not required.
                                                  ▪   Non-soldered type mounting/attach are not
                                                      applicable.
                                                  ▪   Parametrically test per lot and sample size
                                                      requirements.
 Electrical                                       ▪   Summary to show minimum, maximum, mean
                      19    User Specification.
 Characterization                                     and standard deviation at room, minimum and
                                                      maximum operating temperatures.
                                                  ▪   Pre and Post Electrical Test not required.




                                            Page 46 of 107
                                                                                 AEC - Q200 - Rev E
                                                                                    March 20, 2023

Automotive Electronics Council
          Component Technical Committee


                     Table 7: Stress Qualifications for Resistors (continued)
 Stress              No.   Reference              Additional Requirements
                                                  ▪ Applicable to components with exposed cured
                                                     resins or plastic materials.
                                                  ▪ If exposed resins or plastic materials are V-1, V-0
                                                     or 5VA, testing is not required.
                                                  ▪ If exposed resins or plastic materials are not V-1,
                           UL-94 or                  V-0 or 5VA, components or applicable parts of the
 Flammability        20                              component (e.g., sleeve or encapsulant), material
                           IEC 60695-11-5
                                                     shall be tested to the Needle Flame Test per IEC
                                                     60695-11-5. Data from previously qualified
                                                     materials can be supplied in place of conducting
                                                     test.
                                                  ▪ Pre and Post Electrical Test not required.

 Board Flex (SMD)    21    AEC-Q200-005
 Terminal Strength
                     22    AEC-Q200-006
 (SMD)
 Flame
                     24    AEC-Q200-001           Pre and Post Electrical Test not required.
 Retardance

      Note: For any deviation from the above stresses, refer to Section 2.4.8.

      Back to Table C: Qualification Sample Size
      Back to Table D: Applicable Stress Qualifications




                                            Page 47 of 107
                                                                                                     AEC - Q200 - Rev E
                                                                                                        March 20, 2023

Automotive Electronics Council
                  Component Technical Committee


  Table 7A: Resistors Process Change Qualification Guidelines for the Selection of
                                     Tests
For a given change listed below, the Supplier should justify why a suggested test does not apply for the given
component(s) under consideration. Collaboration with their customer base is highly recommended.

 3.       High Temperature Exposure (Storage)       13.   Mechanical Shock                     22.       Terminal Strength (SMD)
 4.       Temperature Cycling                       14.   Vibration                            24        Flame Retardance
 7.       Biased Humidity                           15.   Resistance to Soldering Heat
 8.       Operational Life                          17.   Electrostatic Discharge (ESD)
 9.       External Visual                           18.   Solderability
 10.      Physical Dimension                        19.   Electrical Characterization
 11.      Terminal Strength (THT)                   20.   Flammability
 12.        Resistance to Solvents                  21.   Board Flex


Note: A letter or "⚫" indicates that performance of that stress test should be considered (not necessarily
required) for the appropriate process change

       Test # From Table 7            3    4    7    8    9   10   11   12 13    14       15   17    18 19     20 21     22   24
       MATERIAL
       Ink/Wire Material              ⚫    ⚫         ⚫             W                           F           B        ⚫    ⚫    R
       Package                        ⚫    ⚫    ⚫         ⚫   ⚫    ⚫    ⚫         ⚫            ⚫                ⚫   ⚫    ⚫    R
       Passivation                    ⚫    ⚫    ⚫    ⚫                  ⚫                                       ⚫             R
       Substrate Material                  ⚫    ⚫    ⚫             ⚫                      ⚫          ⚫     B        ⚫    ⚫
       PROCESS
       Ink Fire                            ⚫         ⚫             R                                       B
       Ink Print                      ⚫    ⚫         ⚫             R                                       B        R    R    R
       Laser Trim                               ⚫    ⚫                                                     B
       Lead Form                                ⚫         ⚫   ⚫    ⚫                                 ⚫     B
       Termination Attach                       ⚫                  ⚫        ⚫             ⚫                B
       Marking                                            ⚫             ⚫
       Molding                        ⚫    ⚫    ⚫         ⚫   ⚫    ⚫    ⚫         ⚫            ⚫                ⚫   ⚫    ⚫    R
       DESIGN
       Package                        ⚫    ⚫    ⚫         ⚫   ⚫    ⚫    ⚫         ⚫       ⚫    ⚫     ⚫          ⚫   ⚫    ⚫    R
       Passivation                    ⚫    ⚫    ⚫    ⚫                  ⚫                                       ⚫             R
       Res/Cap Tolerance              ⚫    ⚫         ⚫                                    ⚫    ⚫           B
       Res/Cap Value                  ⚫    ⚫         ⚫                                    ⚫    ⚫           B                  R
       MISCELLANEOUS
       Mfg. Site Transfer             ⚫    ⚫    ⚫    ⚫    ⚫   ⚫    ⚫    ⚫                 ⚫    ⚫           B        ⚫    ⚫    R
       Material Suppliers                  ⚫                  ⚫    ⚫    ⚫                 ⚫    ⚫           B    ⚫             R
       New/Modified Mfg. Equipment         ⚫         ⚫                                         ⚫           B


              B = comparative data (unchanged vs. Changed) required     F = Film products only
                             R = Resistors Only    W = Wirewound products only




                                                      Page 48 of 107
                                                                                     AEC - Q200 - Rev E
                                                                                        March 20, 2023

Automotive Electronics Council
           Component Technical Committee


          Table 7B-1: Acceptance Criteria for Carbon Film THT Fixed Resistors
Note: The contents in this table are meant to serve as examples of wording or limits for each test and relative
parameter to be measured and NOT actual requirements. Variables are denoted by lower-case letters (e.g.,
x, y). The measured parameters, values and wording of each acceptance criteria for each test should be
agreed to between the User and Supplier.

                                                      Acceptance Criteria
  AEC-Q200 Test
                                                      Resistance
  1. Initial Limits                                   Within specified tolerance
  3. High Temperature Exposure (storage)              x% +y
  4. Temperature Cycling                              x% +y
  7. Biased Humidity                                  x% +y
  8. Operational Life                                 x% +y
  9. External Visual                                  Per AEC-Q200 - Electrical test not required
  10. Physical Dimensions                             Per AEC-Q200 - Electrical test not required
  11. Terminal Strength (leaded)                      x%
  12. Resistance to Solvents                          Marking must remain legible
  13. Mechanical Shock                                x% +y
  14. Vibration                                       x% +y
  15.Resistance to Soldering Heat                     x% +y
  17. ESD                                             Per AEC-Q200-002
  18. Solderability                                   Per AEC-Q200 - Electrical test not required
  19a. Elec. Char. @25ºC                              Initial limit
  19b. Elec. Char. @Min. operating temp.              Initial limit Ω change allowed over temp. range
  19c. Elec. Char. @Max operating temp.               Initial limit Ω change allowed over temp. range
  20. Flammability                                    Per AEC-Q200 - Electrical test not required
  24. Flame Retardance                                See AEC-Q200-001

        Significant characteristics:
           1. D.C. Resistance
           2. Temperature Coefficient of Resistance




                                              Page 49 of 107
                                                                                      AEC - Q200 - Rev E
                                                                                         March 20, 2023

Automotive Electronics Council
           Component Technical Committee


Table 7B-2: Acceptance Criteria for Metal Film THT Fixed Resistors (Includes molded
                                    flat lead SMD)
Note: The contents in this table are meant to serve as examples of wording or limits for each test and relative
parameter to be measured and NOT actual requirements. Variables are denoted by lower-case letters (e.g.,
x, y). The measured parameters, values and wording of each acceptance criteria for each test should be
agreed to between the User and Supplier.

                                                  Acceptance Criteria
  AEC-Q200 Test
                                                  Resistance
  1. Initial Limits                               Within specified tolerance
  3. High Temperature Exposure (storage)          x% +y
  4. Temperature Cycling                          x% +y
  7. Biased Humidity                              x% +y
  8. Operational Life                             x% +y
  9. External Visual                              Per AEC-Q200 - Electrical test not required
  10. Physical Dimensions                         Per AEC-Q200 - Electrical test not required
  11. Terminal Strength (leaded)                  x% +y
  12. Resistance to Solvents                      Marking must remain legible
  13. Mechanical Shock                            x% +y
  14. Vibration                                   x% +y
  15.Resistance to Soldering Heat                 x% +y
  17. ESD                                         Per AEC-Q200-002
  18. Solderability                               Per AEC-Q200 - Electrical test not required
  19a. Elec. Char. @25ºC                          Initial limit
  19b. Elec. Char. @Min. operating temp.          Initial limit  change allowed over temp. range
  19c. Elec. Char. @Max operating temp.           Initial limit  change allowed over temp. range
  20. Flammability                                Per AEC-Q200 - Electrical test not required
  21. Board Flex (SMD)                            N/A
  22. Terminal Strength (SMD)                     N/A
  24. Flame Retardance                            See AEC-Q200-001

        Significant characteristics:
           1. D.C. Resistance
           2. Temperature Coefficient of Resistance




                                              Page 50 of 107
                                                                                     AEC - Q200 - Rev E
                                                                                        March 20, 2023

Automotive Electronics Council
           Component Technical Committee


           Table 7B-3: Acceptance Criteria for Metal Oxide THT Fixed Resistors
Note: The contents in this table are meant to serve as examples of wording or limits for each test and relative
parameter to be measured and NOT actual requirements. Variables are denoted by lower-case letters (e.g.,
x, y). The measured parameters, values and wording of each acceptance criteria for each test should be
agreed to between the User and Supplier.

                                                      Acceptance Criteria
  AEC-Q200 Test
                                                      Resistance
  1. Initial Limits                                   Within specified tolerance
  3. High Temperature Exposure (storage)              x% +y
  4. Temperature Cycling                              x% +y
  7. Biased Humidity                                  x% +y
  8. Operational Life                                 x% +y
  9. External Visual                                  Per AEC-Q200 - Electrical test not required
  10. Physical Dimensions                             Per AEC-Q200 - Electrical test not required
  11. Terminal Strength (leaded)                      x% +y
  12. Resistance to Solvents                          Marking must remain legible
  13. Mechanical Shock                                x% +y
  14. Vibration                                       x% +y
  15.Resistance to Soldering Heat                     x% +y
  17. ESD                                             Per AEC-Q200-002
  18. Solderability                                   Per AEC-Q200 - Electrical test not required
  19a. Elec. Char. @25ºC                              Initial limit
  19b. Elec. Char. @Min. operating temp.              Initial limit  change allowed over temp. range
  19c. Elec. Char. @Max operating temp.               Initial limit  change allowed over temp. range
  20. Flammability                                    Per AEC-Q200 - Electrical test not required
  24. Flame Retardance                                See AEC-Q200-001

        Significant characteristics:
           1. D.C. Resistance
           2. Temperature Coefficient of Resistance




                                              Page 51 of 107
                                                                                      AEC - Q200 - Rev E
                                                                                         March 20, 2023

Automotive Electronics Council
            Component Technical Committee


    Table 7B-4: Acceptance Criteria for Wire Wound THT Fixed Resistors (Includes
                               molded flat lead SMD)
Note: The contents in this table are meant to serve as examples of wording or limits for each test and relative
parameter to be measured and NOT actual requirements. Variables are denoted by lower-case letters (e.g.,
x, y). The measured parameters, values and wording of each acceptance criteria for each test should be
agreed to between the User and Supplier.

                                               Acceptance Criteria
   AEC-Q200 Test
                                               Resistance
   1. Initial Limits                           Within specified tolerance
                                               Technologies J and K (Crimped): x% +y
   3. High Temperature Exposure (storage)
                                               Technology H (Welded): a% +b
   4. Temperature Cycling                      x% +y
                                               Technologies J and K (Crimped ): x% +y
   7. Biased Humidity
                                               Technology H (Welded): x% +y
                                               Technologies J and K (Crimped): x% +y
   8. Operational Life
                                               Technology H (Welded): x% +y
   9. External Visual                          Per AEC-Q200 - Electrical test not required
   10. Physical Dimensions                     Per AEC-Q200 - Electrical test not required
                                               Technologies J and K (Crimped ): x% +y
   11. Terminal Strength (leaded)
                                               Technology H (Welded): x% +y
   12. Resistance to Solvents                  Marking must remain legible
                                               Technologies J and K (Crimped ): x% +y
   13. Mechanical Shock
                                               Technology H (Welded): x% +y
                                               Technologies J and K (Crimped ): x% +y
   14. Vibration
                                               Technology H (Welded): x% +y
                                               Technologies J and K (Crimped ): x% +y
   15.Resistance to Soldering Heat
                                               Technology H (Welded): x% +y
   17. ESD                                     Per AEC-Q200-002
   18. Solderability                           Per AEC-Q200 - Electrical test not required
   19a. Elec. Char. @25ºC                      Initial limit
   19b. Elec. Char. @Min. operating temp.      Initial limit  change allowed over temp. range
   19c. Elec. Char. @Max operating temp.       Initial limit  change allowed over temp. range
   20. Flammability                            Per AEC-Q200 - Electrical test not required
   24. Flame Retardance                        See AEC-Q200-001

        Significant characteristics:
           1. D.C. Resistance
           2. Temperature Coefficient of Resistance




                                              Page 52 of 107
                                                                                       AEC - Q200 - Rev E
                                                                                          March 20, 2023

Automotive Electronics Council
           Component Technical Committee


               Table 7B-5: Acceptance Criteria for SMD Chip Resistors
     (Does not include molded flat lead SMD, but does include coated metal strip)
Note: The contents in this table are meant to serve as examples of wording or limits for each test and relative
parameter to be measured and NOT actual requirements. Variables are denoted by lower-case letters (e.g.,
x, y). The measured parameters, values and wording of each acceptance criteria for each test should be
agreed to between the User and Supplier.

                                             Acceptance Criteria
    AEC-Q200 Test
                                             Resistance
    1. Initial Limits                        Within specified tolerance
    3. High Temperature Exposure (storage)   x% +y
    4. Temperature Cycling                   x% +y
                                             Technologies L, M, and U: x% +y
    7. Biased Humidity
                                             Technologies N, P, R and T : x% +y
                                             Technologies L, M, N and U: x% +y
    8. Operational Life
                                             Technologies P, R and T : x% +y
    9. External Visual                       Per AEC-Q200 - Electrical test not required
    10. Physical Dimensions                  Per AEC-Q200 - Electrical test not required
    12. Resistance to Solvents               Marking must remain legible
    13. Mechanical Shock                     x% +y
    14. Vibration                            x% +y
                                             Technologies L, M, and U: x% +y
    15.Resistance to Soldering Heat          Technology N: x% +y
                                             Technologies P, R, and T : x% +y
    17. ESD                                  Per AEC-Q200-002
    18. Solderability                        Per AEC-Q200 - Electrical test not required
    19a. Elec. Char. @25ºC                   Initial limit
    19b. Elec. Char. @Min. operating temp.   Initial limit  change allowed over temp. range

    19c. Elec. Char. @Max operating temp.    Initial limit  change allowed over temp. range
    20. Flammability                         Per AEC-Q200 - Electrical test not required
    21. Board Flex (SMD)                     x% +y
                                             0603 and greater: x N
    22. Terminal Strength (SMD)
                                             0402 and less: y N
    24. Flame Retardance                     See AEC-Q200-001

        Significant characteristics:
           1. D.C. Resistance
           2. Temperature Coefficient of Resistance




                                              Page 53 of 107
                                                                             AEC - Q200 - Rev E
                                                                                March 20, 2023

Automotive Electronics Council
          Component Technical Committee




    Table 8: Stress Qualifications for Thermistors (NTC, Platinum, Ceramic PTC)
 Stress              No.   Reference            Additional Requirements
 Pre- and Post-                                 ▪ Test is performed at room temperature except as
 Stress Electrical   1     User Specification      specified in the applicable stress reference and the
 Test                                              additional requirements in this Table.
                                                ▪   Unpowered
                                                ▪   Tested at maximum specified operating
 High                                               temperature or maximum specified storage
 Temperature               MIL-STD-202              temperature (whichever is higher). Minimum test
                     3
 Exposure                  Method 108               temperature shall be 85C.
 (Storage)                                      ▪   1,000 hours
                                                ▪   Measurement at 244 hours after test conclusion.
                                                ▪   Unpowered
                                                ▪   1,000 Cycles
                                                ▪   Lower Temperature of the Chamber: -55C
                                                ▪   Upper Temperature of the Chamber: maximum
                                                    specified operating temperature and shall not
                                                    exceed 125C.
 Temperature
                     4     JESD22-A104          ▪   Dwell Time (Soak Time):
 Cycling
                                                         o 15 minutes minimum,
                                                         o 30 minutes minimum if component weighs
                                                             above 28g
                                                ▪   Transition Time: 1 minute maximum
                                                ▪   Measurement at least 24 hours after test
                                                    conclusion.
                                                ▪   1,000 hours
                                                ▪   85C/85%RH
                                                ▪   Ceramic PTC: Biased at 20% of rated hold current
                                                    or 10% of rated power or voltage.
                           MIL-STD-202          ▪   All other: 10% rated power, unless the thermistor
 Humidity Bias       7
                           Method 103               resistance during the test violates its specified
                                                    value for the applied test temperature +0.2 K due to
                                                    self-heating. In this case, the applied power shall
                                                    be reduced to ensure the resistance limit.
                                                ▪   Measurement at 244 hours after test conclusion.
                                                ▪   1,000 hours
                                                ▪   Heater-type Ceramic PTC: Rated voltage
                                                ▪   Non heater-type Ceramic PTC: Rated hold current
                                                    or 50% of rated voltage.
                                                ▪   All other: 10% rated power, unless the thermistor
 High
                           MIL-STD-202              resistance during the test violates its specified
 Temperature         8
                           Method 108               value for the applied test temperature +0.2 K due to
 Operating Life
                                                    self-heating. In this case, the applied power shall
                                                    be reduced to ensure the resistance limit.
                                                ▪   Temperature of the Chamber: maximum specified
                                                    operating temperature up to 150C
                                                ▪   Measurement at 244 hours after test conclusion.




                                          Page 54 of 107
                                                                              AEC - Q200 - Rev E
                                                                                 March 20, 2023

Automotive Electronics Council
          Component Technical Committee



    Table 8: Stress Qualifications for Thermistors (NTC, Platinum, Ceramic PTC)
                                      (continued)
 Stress             No.   Reference         Additional Requirements
                                            ▪ Inspect device construction, marking and
                          MIL-STD-883
 External Visual    9                          workmanship.
                          Method 2009       ▪ Pre and Post Electrical Test not required.
                                            ▪ Verify physical dimensions to the applicable
 Physical                                      component specification.
                    10    JESD22-B100
 Dimensions                                 ▪ Pre and Post Electrical Test not required.
                                            ▪   Test THT component lead integrity only.
                                            ▪   Test Condition A (pull test):
                                                  Nominal cross- sectional area
                                                                                   Force (N)
                                                             (mm2)
                                                             ≤ 0.05                    1
                                                          0.06 to 0.10                2.5
                                                          0.11 to 0.20                 5
                                                          0.21 to 0.50                10
                                                          0.51 to 1.20                20
                                                             > 1.20                   40
                                            ▪   Test Condition C (wire-lead bend test):
 Terminal                                          Section Modulus (ZX) (mm3)     Force (N)
 Strength (for
                          MIL-STD-202                      ≤ 1.5x10 -3
                                                                                      0.5
 axial and radial   11
                          Method 211                   1.6x10-3 to 4.2x10-3          1.25
 THT
                                                       4.3x10-3 to 1.2x10-2           2.5
 components)
                                                       1.3x10-2 to 0.5x10-1            5
                                                       0.6x10-1 to 1.9x10-1           10
                                                           > 1.9x10-1                 20
                                                 For round terminations: ZX = (πd3)/32 where d is
                                                 the lead diameter.
                                                 For strip terminations: ZX = (ba2)/6 where a is the
                                                 thickness of the rectangular strip perpendicular to
                                                 the bending axis, b is the other dimension of the
                                                 rectangular strip.
                                            Note: the values and formulas are per IEC 60068-2-21,
                                            6th Edition.
                                            ▪   In addition to the Method 215 solvents, add an
                                                Aqueous wash chemical and follow chemical
 Resistance to            MIL-STD-202           manufacturer’s recommended parameters (i.e.,
                    12                          solution temperature and immersion time).
 Solvents                 Method 215
                                            ▪   Applicable to ink marked components and not laser
                                                marked components.
                                            ▪   Figure 1 of Method 213
                                            ▪   THT: Condition C
 Mechanical               MIL-STD-202       ▪   SMD: Condition C
                    13
 Shock                    Method 213        ▪   Tested per the Supplier’s recommended mounting
                                                method.




                                        Page 55 of 107
                                                                               AEC - Q200 - Rev E
                                                                                  March 20, 2023

Automotive Electronics Council
            Component Technical Committee



    Table 8: Stress Qualifications for Thermistors (NTC, Platinum, Ceramic PTC)
                                      (continued)
 Stress              No.   Reference             Additional Requirements
                                                 ▪ 5g's for 20 minutes
                                                 ▪ 12 cycles each of 3 orientations.
                                                 ▪ Tested per the Supplier’s recommended mounting
                                                    method.
                                                 ▪ Verification of transfer load: during setup, verify that
                            MIL-STD-202             with the selected PCB design (size, thickness and
Vibration            14
                           Method 204               secure points), or an alternative mount, that the
                                                    transferred load onto the component corresponds
                                                    to the requested load. This verification can be
                                                    achieved using a laser vibrometer or other
                                                    adequate measuring device.
                                                 ▪ Test from 10 Hz - 2000 Hz.
                                                 ▪   THT: within 1.5mm of device body, Condition B, C
                                                     or D
 Resistance to             MIL-STD-202           ▪   SMD: Condition K, time above 217°C, 60s – 150s,
                     15                              remove carrier
 Soldering Heat            Method 210
                                                 ▪   Non-soldered type mounting/attach are not
                                                     applicable.

 ESD                 17    AEC-Q200-002
                                                 ▪   Through-hole Technology (THT:
                                                        o Method A, Coating Durability Category 2
                                                 ▪   SMD:
                                                        o Method B1, Coating Durability Category 2
                                                        o Method D, Coating Durability Category 2
                                                 ▪   Note: in particular circumstances when SnPb
 Solderability       18    J-STD-002                 reverse compatibility is requested by the User,
                                                     Method A shall be used for THT and Method B
                                                     shall be used for SMD.
                                                 ▪   Magnification 50x
                                                 ▪   Pre and Post Electrical Test not required.
                                                 ▪   Non-soldered type mounting/attach are not
                                                     applicable.
                                                 ▪   Parametrically test per lot and sample size
                                                     requirements.
                                                 ▪   Summary to show minimum, maximum, mean and
 Electrical
                     19    User Specification.       standard deviation at room or 0°C, minimum and
 Characterization
                                                     maximum operating temperatures (or other
                                                     temperatures as defined by Supplier).
                                                 ▪   Pre and Post Electrical Test not required.




                                           Page 56 of 107
                                                                                 AEC - Q200 - Rev E
                                                                                    March 20, 2023

Automotive Electronics Council
          Component Technical Committee



    Table 8: Stress Qualifications for Thermistors (NTC, Platinum, Ceramic PTC)
                                      (continued)
 Stress             No.    Reference              Additional Requirements
                                                  ▪ Applicable to components with exposed cured
                                                     resins or plastic materials.
                                                  ▪ If exposed resins or plastic materials are V-1, V-0
                                                     or 5VA, testing is not required.
                                                  ▪ If exposed resins or plastic materials are not V-1,
                           UL-94 or                  V-0 or 5VA, components or applicable parts of the
 Flammability        20
                          IEC 60695-11-5             component (e.g., sleeve or encapsulant), material
                                                     shall be tested to the Needle Flame Test per IEC
                                                     60695-11-5. Data from previously qualified
                                                     materials can be supplied in place of conducting
                                                     test.
                                                  ▪ Pre and Post Electrical Test not required.
 Board Flex
                     21    AEC-Q200-005
 (SMD)
 Terminal
                     22    AEC-Q200-006
 Strength (SMD)

      Note: For any deviation from the above stresses, refer to Section 2.4.8.

      Back to Table C: Qualification Sample Size
      Back to Table D: Applicable Stress Qualifications




                                            Page 57 of 107
                                                                                                   AEC - Q200 - Rev E
                                                                                                      March 20, 2023

Automotive Electronics Council
            Component Technical Committee


TABLE 8A: Thermistors (NTC, Platinum, Ceramic PTC) Process Change Qualification
                      Guidelines for the Selection of Tests
For a given change listed below, the Supplier should justify why a suggested test does not apply for the given
component(s) under consideration. Collaboration with their customer base is highly recommended.

      3.     High Temperature Exposure (Storage)       13.    Mechanical Shock                          22.    Terminal Strength (SMD)
      4.     Temperature Cycling                       14.    Vibration
      7.     Biased Humidity                           15.    Resistance to Soldering Heat
      8.     Operational Life                          17.    Electrostatic Discharge (ESD)
      9.     External Visual                           18.    Solderability
      10.    Physical Dimension                        19.    Electrical Characterization
      11.    Terminal Strength (THT)                   20.    Flammability
      12.      Resistance to Solvents                  21.    Board Flex


Note: A letter or "⚫" indicates that performance of that stress test should be considered (not necessarily
required) for the appropriate process change.

            Test # From Table 8     3   4   7      8    9    10   11   12   13   14   15      17   18     19   20   21   22
            MATERIAL
            Ink Material            ⚫   ⚫   ⚫      ⚫                                          ⚫           B
            Protective Coat         ⚫   ⚫
            Substrate Material                                              ⚫          ⚫           ⚫            ⚫
            PROCESS
            Lead Form                                   ⚫    ⚫    ⚫                                       B          ⚫   ⚫
            Marking                                     ⚫              ⚫
            Molding                 ⚫   ⚫               ⚫    ⚫         ⚫         ⚫     ⚫           ⚫            ⚫
            Termination Attach              ⚫      ⚫              ⚫         ⚫                 ⚫    ⚫      B          ⚫   ⚫
            DESIGN
            Package                 ⚫   ⚫   ⚫      ⚫    ⚫    ⚫    ⚫    ⚫    ⚫    ⚫     ⚫           ⚫            ⚫
            Thermistor Value        ⚫   ⚫          ⚫                                          ⚫           B
            Thermistor Tolerance    ⚫   ⚫          ⚫                                   ⚫      ⚫           B
            MISCELLANEOUS
            Mfg. Site Transfer      ⚫   ⚫          ⚫    ⚫    ⚫    ⚫         ⚫    ⚫     ⚫      ⚫    ⚫      B     ⚫    ⚫   ⚫
            Material Suppliers          ⚫          ⚫              ⚫    ⚫               ⚫           ⚫      B     ⚫    ⚫   ⚫


                                 B = comparative data (unchanged vs. Changed) required




                                                       Page 58 of 107
                                                                              AEC - Q200 - Rev E
                                                                                 March 20, 2023

Automotive Electronics Council
          Component Technical Committee



              Table 9: Stress Qualifications for Trimmer Capacitors/Resistors
 Stress              No.   Reference             Additional Requirements
 Pre- and Post-                                  ▪ Test is performed at room temperature except as
 Stress Electrical   1     User Specification.      specified in the applicable stress reference and the
 Test                                               additional requirements in this Table.
                                                 ▪   Tested at maximum specified operating
                                                     temperature or maximum specified storage
 High
                                                     temperature (whichever is higher). Minimum test
 Temperature               MIL-STD-202
                     3                               temperature shall be 85C
 Exposure                  Method 108
                                                 ▪   1,000 hours
 (Storage)
                                                 ▪   Unpowered
                                                 ▪   Measurement at 244 hours after test conclusion.
                                                 ▪   Unpowered
                                                 ▪   1,000 Cycles
                                                 ▪   Lower Temperature of the Chamber: -55C
                                                 ▪   Upper Temperature of the Chamber: maximum
                                                     specified operating temperature and shall not
                                                     exceed 125C.
 Temperature
                     4     JESD22-A104           ▪   Dwell Time (Soak Time):
 Cycling
                                                         o 15 minutes minimum,
                                                         o 30 minutes minimum if component weighs
                                                              above 28g
                                                 ▪   Transition Time: 1 minute maximum
                                                 ▪   Measurement at least 24 hours after test
                                                     conclusion.
                                                 ▪   1,000 hours
                                                 ▪   85C/85%RH.
                           MIL-STD-202
 Humidity Bias       7                           ▪   Capacitor Networks: Rated Voltage
                           Method 103
                                                 ▪   Resistor Networks: 10% Rated Power
                                                 ▪   Measurement at 244 hours after test conclusion.
                                                 ▪   1,000 hours
                                                 ▪   Temperature of the Chamber: maximum specified
 High
                           MIL-STD-202               operating temperature up to 150C
 Temperature         8
                           Method 108            ▪   Trimmer Resistor: de-rated power at temperature
 Operating Life
                                                 ▪   Trimmer Capacitor: Rated Voltage
                                                 ▪   Measurement at 244 hours after test conclusion.
                                                 ▪   Inspect device construction, marking and
                           MIL-STD-883
 External Visual     9                               workmanship.
                           Method 2009
                                                 ▪   Pre and Post Electrical Test not required.
                                                 ▪   Verify physical dimensions to the applicable
 Physical
                     10    JESD22-B100               component specification.
 Dimensions
                                                 ▪   Pre and Post Electrical Test not required.




                                           Page 59 of 107
                                                                              AEC - Q200 - Rev E
                                                                                 March 20, 2023

Automotive Electronics Council
          Component Technical Committee



     Table 9: Stress Qualifications for Trimmer Capacitors/Resistors (continued)
 Stress             No.   Reference         Additional Requirements
                                            ▪ Test THT component lead integrity only.
                                            ▪ Test Condition A (pull test):
                                                  Nominal cross- sectional area
                                                                                   Force (N)
                                                             (mm2)
                                                             ≤ 0.05                    1
                                                          0.06 to 0.10                2.5
                                                          0.11 to 0.20                 5
                                                          0.21 to 0.50                10
                                                          0.51 to 1.20                20
                                                             > 1.20                   40
                                            ▪   Test Condition C (wire-lead bend test):
 Terminal                                          Section Modulus (ZX) (mm3)     Force (N)
 Strength (for
                          MIL-STD-202                      ≤ 1.5x10 -3
                                                                                      0.5
 axial and radial   11
                          Method 211                   1.6x10-3 to 4.2x10-3          1.25
 THT
 components)                                           4.3x10-3 to 1.2x10-2           2.5
                                                       1.3x10-2 to 0.5x10-1            5
                                                       0.6x10-1 to 1.9x10-1           10
                                                           > 1.9x10-1                 20
                                                 For round terminations: ZX = (πd3)/32 where d is
                                                 the lead diameter.
                                                 For strip terminations: ZX = (ba2)/6 where a is the
                                                 thickness of the rectangular strip perpendicular to
                                                 the bending axis, b is the other dimension of the
                                                 rectangular strip.
                                            Note: the values and formulas are per IEC 60068-2-21,
                                            6th Edition.
                                            ▪   In addition to the Method 215 solvents, add an
                                                Aqueous wash chemical and follow chemical
 Resistance to            MIL-STD-202           manufacturer’s recommended parameters (i.e.,
                    12
 Solvents                 Method 215            solution temperature and immersion time).
                                            ▪   Applicable to ink marked components and not laser
                                                marked components.
                                            ▪   Figure 1 of Method 213
 Mechanical               MIL-STD-202       ▪   THT: Condition C
                    13                      ▪   SMD: Condition C
 Shock                    Method 213
                                            ▪   Tested per the Supplier’s recommended mounting
                                                method.




                                        Page 60 of 107
                                                                                AEC - Q200 - Rev E
                                                                                   March 20, 2023

Automotive Electronics Council
             Component Technical Committee




     Table 9: Stress Qualifications for Trimmer Capacitors/Resistors (continued)
 Stress               No.   Reference             Additional Requirements
                                                  ▪ 5g's for 20 minutes
                                                  ▪ 12 cycles each of 3 orientations.
                                                  ▪ Tested per the Supplier’s recommended mounting
                                                     method
                                                  ▪ Verification of transfer load: during setup, verify that
                            MIL-STD-202              with the selected PCB design (size, thickness and
 Vibration            14
                            Method 204               secure points), or an alternative mount, that the
                                                     transferred load onto the component corresponds
                                                     to the requested load. This verification can be
                                                     achieved using a laser vibrometer or other
                                                     adequate measuring device.
                                                  ▪ Test from 10 Hz - 2000 Hz
                                                  ▪   THT: within 1.5mm of device body, Condition B, C
                                                      or D
 Resistance to              MIL-STD-202
                      15                          ▪   SMD: Condition K, time above 217°C, 60s – 150s
 Soldering Heat             Method 210
                                                  ▪   Non-soldered type mounting/attach are not
                                                      applicable.

 ESD                  17    AEC-Q200-002

                                                  ▪   Through-hole Technology (THT:
                                                         o Method A1, Coating Durability Category 2
                                                  ▪   SMD:
                                                         o Method B1, Coating Durability Category 2
                                                         o Method D, Coating Durability Category 2
                                                  ▪   Note: in particular circumstances when SnPb
 Solderability        18    J-STD-002                 reverse compatibility is requested by the User,
                                                      Method A shall be used for THT and Method B
                                                      shall be used for SMD
                                                  ▪   Magnification 50x
                                                  ▪   Pre and Post Electrical Test not required.
                                                  ▪   Non-soldered type mounting/attach are not
                                                      applicable.
                                                  ▪   Parametrically test per lot and sample size
                                                      requirements.
 Electrical                                       ▪   Summary to show minimum, maximum, mean
                      19    User Specification.
 Characterization                                     and standard deviation at room, minimum and
                                                      maximum operating temperatures.
                                                  ▪   Pre and Post Electrical Test not required.




                                            Page 61 of 107
                                                                                  AEC - Q200 - Rev E
                                                                                     March 20, 2023

Automotive Electronics Council
          Component Technical Committee



     Table 9: Stress Qualifications for Trimmer Capacitors/Resistors (continued)
 Stress              No.    Reference              Additional Requirements
                                                   ▪ Applicable to components with exposed cured
                                                      resins or plastic materials.
                                                   ▪ If exposed resins or plastic materials are V-1, V-0
                                                      or 5VA, testing is not required.
                                                   ▪ If exposed resins or plastic materials are not V-1,
                            UL-94 or                  V-0 or 5VA, components or applicable parts of the
 Flammability         20
                            IEC 60695-11-5            component (e.g., sleeve or encapsulant), material
                                                      shall be tested to the Needle Flame Test per IEC
                                                      60695-11-5. Data from previously qualified
                                                      materials can be supplied in place of conducting
                                                      test.
                                                   ▪ Pre and Post Electrical Test not required.
 Board Flex
                      21    AEC-Q200-005
 (SMD)

 Terminal
                      22    AEC-Q200-006
 Strength (SMD)

                            MIL-STD-202
 Rotational Life      25                           ▪   Condition A
                            Method 206

       Note: For any deviation from the above stresses, refer to Section 2.4.8.

       Back to Table C: Qualification Sample Size
       Back to Table D: Applicable Stress Qualifications




                                             Page 62 of 107
                                                                                                     AEC - Q200 - Rev E
                                                                                                        March 20, 2023

Automotive Electronics Council
              Component Technical Committee


 TABLE 9A: Trimmer Capacitors/Resistors Process Change Qualification Guidelines
                           for the Selection of Tests
For a given change listed below, the Supplier should justify why a suggested test does not apply for the given
component(s) under consideration. Collaboration with their customer base is highly recommended.

      3.       High Temperature Exposure (Storage)   13.        Mechanical Shock                     22.        Terminal Strength (SMD)
      4.       Temperature Cycling                   14.        Vibration                            25         Rotational Life
      7.       Biased Humidity                       15.        Resistance to Soldering Heat
      8.       Operational Life                      17.        Electrostatic Discharge (ESD)
      9.       External Visual                       18.        Solderability
      10.      Physical Dimension                    19.        Electrical Characterization
      11.      Terminal Strength (THT)               20.        Flammability
      12.      Resistance to Solvents                21.        Board Flex


Note: A letter or "⚫" indicates that performance of that stress test should be considered (not necessarily
required) for the appropriate process change

            Test # From Table 9    3   4    7    8   9     10    11   12   13   14   15   17    18   19    20    21   22   25
            MATERIAL
            Element Material           ⚫                                                   ⚫         B                     ⚫
            Housing Material           ⚫        ⚫    ⚫     ⚫
            Substrate                  ⚫    ⚫                               ⚫
            Termination Material       ⚫        ⚫          ⚫     ⚫    ⚫     C    ⚫    ⚫         ⚫                ⚫    ⚫
            Washer                 ⚫   ⚫                              ⚫                         ⚫                          ⚫
            PROCESS
            Brush Attach               ⚫    ⚫                                    ⚫                   B                     ⚫
            Termination Attach         ⚫        ⚫                ⚫                    ⚫                          ⚫    ⚫
            DESIGN
            Element                    ⚫                                                   ⚫         B                     ⚫
            Housing                ⚫   ⚫        ⚫    ⚫     ⚫          ⚫                                    ⚫
            MISCELLANEOUS
            Mfg. Site Transfer     ⚫   ⚫    ⚫   ⚫    ⚫     ⚫     ⚫    ⚫     ⚫    ⚫    ⚫    ⚫    ⚫    B     ⚫     ⚫    ⚫    ⚫
            Material Suppliers         ⚫                   ⚫                C                   ⚫


      C = Capacitive Trimmers only                       B = comparative data (unchanged vs. Changed) required




                                                     Page 63 of 107
                                                                               AEC - Q200 - Rev E
                                                                                  March 20, 2023

Automotive Electronics Council
          Component Technical Committee



                           Table 10: Stress Qualifications for Varistors
 Stress              No.    Reference             Additional Requirements
 Pre- and Post-                                   ▪ Test is performed at room temperature except as
 Stress Electrical   1      User Specification.      specified in the applicable stress reference and the
 Test                                                additional requirements in this Table.
                                                  ▪ Unpowered
                                                  ▪ 1,000 hours
 High
                                                  ▪ Tested at maximum specified operating
 Temperature                MIL-STD-202
                     3                               temperature or maximum specified storage
 Exposure                   Method 108
                                                     temperature (whichever is higher). Minimum test
 (Storage)
                                                     temperature shall be 85C
                                                  ▪ Measurement at 244 hours after test conclusion.
                                                  ▪ Unpowered
                                                  ▪ 1,000 Cycles
                                                  ▪ Lower Temperature of the Chamber: -40C
                                                  ▪ Upper Temperature of the Chamber: maximum
                                                     specified operating temperature and shall not
 Temperature                                         exceed 125C.
 Cycling
                     4      JESD22-A104           ▪ Dwell Time (Soak Time):
                                                          o 15 minutes minimum,
                                                          o 30 minutes minimum if component weighs
                                                              above 28g
                                                  ▪ Transition Time: 1 minute maximum
                                                  ▪ Measurement at least 24 hours after test
                                                     conclusion.
                                                  ▪ 1,000 hours
                            MIL-STD-202           ▪ 85C/85%RH.
 Humidity Bias       7
                            Method 103            ▪ Bias at 85% (+5%/-0%) of rated Varistor voltage
                                                  ▪ Measurement at 244 hours after test conclusion.
                                                  ▪ 1,000 hours
 High                                             ▪ Temperature of the Chamber: maximum specified
                            MIL-STD-202
 Temperature         8                               operating temperature up to 150C.
                            Method 108
 Operating Life                                   ▪ Bias at 85% (+5%/-0%) of rated Varistor voltage
                                                  ▪ Measurement at 244 hours after test conclusion.
                            MIL-STD-883           ▪ Inspect device construction, marking and
 External Visual     9                               workmanship.
                            Method 2009
                                                  ▪ Pre and Post Electrical Test not required.
                                                  ▪ Verify physical dimensions to the applicable
 Physical
                     10     JESD22-B100              component specification.
 Dimensions
                                                  ▪ Pre and Post Electrical Test not required.




                                            Page 64 of 107
                                                                                AEC - Q200 - Rev E
                                                                                   March 20, 2023

Automotive Electronics Council
          Component Technical Committee



                    Table 10: Stress Qualifications for Varistors (continued)
 Stress               No.   Reference         Additional Requirements
                                              ▪ Test THT component lead integrity only.
                                              ▪ Test Condition A (pull test):
                                                    Nominal cross- sectional area
                                                                                     Force (N)
                                                               (mm2)
                                                               ≤ 0.05                    1
                                                            0.06 to 0.10                2.5
                                                            0.11 to 0.20                 5
                                                            0.21 to 0.50                10
                                                            0.51 to 1.20                20
                                                               > 1.20                   40
                                              ▪   Test Condition C (wire-lead bend test):
 Terminal                                            Section Modulus (ZX) (mm3)     Force (N)
 Strength (for
                            MIL-STD-202                      ≤ 1.5x10 -3
                                                                                        0.5
 axial and radial     11
                            Method 211                   1.6x10-3 to 4.2x10-3          1.25
 THT
 components)                                             4.3x10-3 to 1.2x10-2           2.5
                                                         1.3x10-2 to 0.5x10-1            5
                                                         0.6x10-1 to 1.9x10-1           10
                                                             > 1.9x10-1                 20
                                                  For round terminations: ZX = (πd3)/32 where d is
                                                  the lead diameter.
                                                  For strip terminations: ZX = (ba2)/6 where a is the
                                                  thickness of the rectangular strip perpendicular to
                                                  the bending axis, b is the other dimension of the
                                                  rectangular strip.
                                              ▪   Note: the values and formulas are per IEC 60068-2-
                                                  21, 6th Edition.
                                              ▪   In addition to the Method 215 solvents, add an
                                                  Aqueous wash chemical and follow chemical
 Resistance to              MIL-STD-202           manufacturer’s recommended parameters (i.e.,
                      12
 Solvents                   Method 215            solution temperature and immersion time).
                                              ▪   Applicable to ink marked components and not laser
                                                  marked components.
                                              ▪   Figure 1 of Method 213
 Mechanical                 MIL-STD-202       ▪   THT: Condition C
                      13                      ▪   SMD: Condition C
 Shock                      Method 213
                                              ▪   Tested per the Supplier’s recommended mounting
                                                  method.




                                          Page 65 of 107
                                                                                AEC - Q200 - Rev E
                                                                                   March 20, 2023

Automotive Electronics Council
             Component Technical Committee



                    Table 10: Stress Qualifications for Varistors (continued)
 Stress               No.   Reference             Additional Requirements
                                                  ▪ 5g's for 20 minutes,
                                                  ▪ 12 cycles each of 3 orientations.
                                                  ▪ Tested per the Supplier’s recommended mounting
                                                     method
                                                  ▪ Verification of transfer load: during setup, verify that
                            MIL-STD-202              with the selected PCB design (size, thickness and
 Vibration            14
                            Method 204               secure points), or an alternative mount, that the
                                                     transferred load onto the component corresponds
                                                     to the requested load. This verification can be
                                                     achieved using a laser vibrometer or other
                                                     adequate measuring device.
                                                  Test from 10 Hz - 2000 Hz
                                                  ▪  THT: within 1.5mm of device body, Condition B, C
                                                     or D
 Resistance to              MIL-STD-202
                      15                          ▪ SMD: Condition K, time above 217°C, 60s – 150s,
 Soldering Heat             Method 210
                                                     remove carrier
                                                  Non-soldered type mounting/attach are not applicable

 ESD                  17    AEC-Q200-002

                                                  ▪   Through-hole Technology (THT:
                                                         o Method A1, Coating Durability Category 2
                                                  ▪   SMD:
                                                         o Method B1, Coating Durability Category 2
                                                         o Method D, Coating Durability Category 2
                                                  ▪   Note: in particular circumstances when SnPb
 Solderability        18    J-STD-002                 reverse compatibility is requested by the User,
                                                      Method A shall be used for THT and Method B
                                                      shall be used for SMD.
                                                  ▪   Magnification 50x
                                                  ▪   Pre and Post Electrical Test not required.
                                                  ▪   Non-soldered type mounting/attach are not
                                                      applicable.
                                                  ▪   Parametrically test per lot and sample size
                                                      requirements.
 Electrical                                       ▪   Summary to show minimum, maximum, mean
                      19    User Specification.
 Characterization                                     and standard deviation at room, minimum and
                                                      maximum operating temperatures.
                                                  ▪   Pre and Post Electrical Test not required.
                                                  ▪   Parametrically test per lot and sample size
                                                      requirements.
 Electrical                                       ▪   Summary to show minimum, maximum, mean
 Characterization     19    User Specification.
                                                      and standard deviation at room, minimum and
                                                      maximum operating temperatures.
                                                  ▪   Pre and Post Electrical Test not required.




                                            Page 66 of 107
                                                                                 AEC - Q200 - Rev E
                                                                                    March 20, 2023

Automotive Electronics Council
          Component Technical Committee



                  Table 10: Stress Qualifications for Varistors (continued)
 Stress             No.    Reference              Additional Requirements
                                                  ▪ Applicable to components with exposed cured
                                                     resins or plastic materials.
                                                  ▪ If exposed resins or plastic materials are V-1, V-0
                                                     or 5VA, testing is not required.
                                                  ▪ If exposed resins or plastic materials are not V-1,
                           UL-94 or                  V-0 or 5VA, components or applicable parts of the
 Flammability        20
                           IEC 60695-11-5            component (e.g., sleeve or encapsulant), material
                                                     shall be tested to the Needle Flame Test per IEC
                                                     60695-11-5. Data from previously qualified
                                                     materials can be supplied in place of conducting
                                                     test.
                                                  ▪ Pre and Post Electrical Test not required.
 Board Flex
                     21    AEC-Q200-005
 (SMD)

 Terminal
                     22    AEC-Q200-006
 Strength (SMD)

 Electrical
 Transient           30    ISO7637-2              ▪   Test pulses 1 to 3
 Conduction


      Note: For any deviation from the above stresses, refer to Section 2.4.8.

      Back to Table C: Qualification Sample Size
      Back to Table D: Applicable Stress Qualifications




                                            Page 67 of 107
                                                                                                       AEC - Q200 - Rev E
                                                                                                          March 20, 2023

Automotive Electronics Council
               Component Technical Committee


  TABLE 10A: Varistors Process Change Qualification Guidelines for the Selection of
                                     Tests
For a given change listed below, the Supplier should justify why a suggested test does not apply for the given
component(s) under consideration. Collaboration with their customer base is highly recommended.

3.    High Temperature Exposure (Storage)       13.   Mechanical Shock                          22.    Terminal Strength (SMD)
4.    Temperature Cycling                       14.   Vibration                                 30     Electrical Transient Conduction
7.    Biased Humidity                           15.   Resistance to Soldering Heat
8.    Operational Life                          17.   Electrostatic Discharge (ESD)
9.    External Visual                           18.   Solderability
10.   Physical Dimension                        19.   Electrical Characterization
11.   Terminal Strength (THT)                   20.   Flammability
12.   Resistance to Solvents                    21.   Board Flex


Note: A letter or "⚫" indicates that performance of that stress test should be considered (not necessarily
required) for the appropriate process change

      Test # From Table 10            3     4     7   8    9   10   11    12   13     14   15     17    18   19   20   21   22   30
      MATERIAL
      Coating Material               ⚫      ⚫              ⚫              ⚫    ⚫      ⚫                           ⚫
      Electrode Attach               ⚫      ⚫         ⚫              ⚫                     ⚫                 B         ⚫    ⚫     ⚫
      Element Material               ⚫      ⚫         ⚫                        ⚫                  ⚫          B                    ⚫
      Passivation                           ⚫                                                                          ⚫
      Termination                    ⚫      ⚫         ⚫              ⚫                     ⚫            ⚫    B         ⚫    ⚫     ⚫
      PROCESS
      Coating Dip/Cure               ⚫      ⚫              ⚫    ⚫         ⚫                                       ⚫
      Dicing                                ⚫     ⚫        ⚫    ⚫                                            B         ⚫    ⚫     ⚫
      Lead Forming                   ⚫            ⚫             ⚫    ⚫                ⚫    ⚫            ⚫    B
      Marking                        ⚫                     ⚫              ⚫
      Sintering                      ⚫      ⚫         ⚫                                           ⚫          B                    ⚫
      Termination Attach             ⚫      ⚫         ⚫         ⚫    ⚫                ⚫    ⚫                 B         ⚫    ⚫     ⚫
      Termination Plating            ⚫      ⚫         ⚫         ⚫    ⚫                     ⚫            ⚫    B         ⚫    ⚫
      DESIGN
      Element Size                          ⚫         ⚫                        ⚫      ⚫           ⚫          B                    ⚫
      Grain Boundary Size                             ⚫                                           ⚫          B                    ⚫
      Grain Size                                      ⚫                                                      B                    ⚫
      Layer - Number of                     ⚫         ⚫                               ⚫                                           ⚫
      Layer - Thickness                               ⚫                                                      B         ⚫    ⚫     ⚫
      Package Size                          ⚫         ⚫    ⚫    ⚫    ⚫         ⚫      ⚫           ⚫                    ⚫          ⚫
      Passivation Thickness                 ⚫         ⚫                        ⚫                             B
      MISCELLANEOUS
      Mfg. Site Transfer             ⚫      ⚫     ⚫   ⚫    ⚫    ⚫    ⚫         ⚫      ⚫    ⚫      ⚫     ⚫    B         ⚫    ⚫     ⚫
      Material Suppliers             ⚫      ⚫         ⚫              ⚫                ⚫    ⚫      ⚫     ⚫    B         ⚫    ⚫     ⚫
      New/Modified Mfg. Equipment           ⚫         ⚫              ⚫                ⚫           ⚫          B                    ⚫


                              B = comparative data (unchanged vs. Changed) required




                                                      Page 68 of 107
                                                                               AEC - Q200 - Rev E
                                                                                  March 20, 2023

Automotive Electronics Council
          Component Technical Committee




                     Table 11: Stress Qualifications for Quartz Crystals
 Stress              No.   Reference             Additional Requirements
 Pre- and Post-                                  ▪ Test is performed at room temperature except as
 Stress Electrical   1     User Specification.      specified in the applicable stress reference and the
 Test                                               additional requirements in this Table.
                                                 ▪   Tested at maximum specified operating
                                                     temperature or maximum specified storage
 High
                                                     temperature (whichever is higher). Minimum
 Temperature               MIL-STD-202
                     3                               test temperature shall be 85C.
 Exposure                  Method 108
                                                 ▪   1,000 hours
 (Storage)
                                                 ▪   Unpowered
                                                 ▪   Measurement at 244 hours after test conclusion.
                                                 ▪   Unpowered
                                                 ▪   1,000 Cycles
                                                 ▪   Lower Temperature of the Chamber: -55C
                                                 ▪   Upper Temperature of the Chamber: maximum
                                                     specified operating temperature and shall not
                                                     exceed 85C.
 Temperature
                     4     JESD22-A104           ▪   Dwell Time (Soak Time):
 Cycling
                                                         o 15 minutes minimum
                                                         o 30 minutes minimum if component weighs
                                                               above 28g
                                                 ▪   Transition Time: 1 minute maximum
                                                 ▪   Measurement at least 24 hours after test
                                                     conclusion.
                                                 ▪   1,000 hours
                                                 ▪   85C/85%RH
 Humidity Bias       7
                           MIL-STD-202           ▪   Rated VDD applied with 1M and inverter in
                           Method 103                parallel, 2X crystal CL capacitors between each
                                                     crystal leg and GND.
                                                 ▪   Measurement at 244 hours after test conclusion.
                                                 ▪   Note: 1,000 hours
                                                 ▪   Temperature of the Chamber: maximum specified
 High                                                operating temperature up to 150C
                           MIL-STD-202
 Temperature         8                           ▪   Rated VDD applied with 1M and inverter in
                           Method 108
 Operating Life                                      parallel, 2X crystal CL capacitors between each
                                                     crystal leg and GND.
                                                 ▪   Measurement at 244 hours after test conclusion.
                                                 ▪   Inspect device construction, marking and
                           MIL-STD-883
 External Visual     9                               workmanship.
                           Method 2009
                                                 ▪   Pre and Post Electrical Test not required.
                                                 ▪   Verify physical dimensions to the applicable
 Physical
                     10    JESD22-B100               component specification.
 Dimensions
                                                 ▪   Pre and Post Electrical Test not required.




                                           Page 69 of 107
                                                                              AEC - Q200 - Rev E
                                                                                 March 20, 2023

Automotive Electronics Council
          Component Technical Committee




              Table 11: Stress Qualifications for Quartz Crystals (continued)
 Stress             No.   Reference         Additional Requirements
                                            ▪   Test THT component lead integrity only.
                                            ▪   Test Condition A (pull test):
                                                  Nominal cross- sectional area
                                                                                   Force (N)
                                                             (mm2)
                                                             ≤ 0.05                    1
                                                          0.06 to 0.10                2.5
                                                          0.11 to 0.20                 5
                                                          0.21 to 0.50                10
                                                          0.51 to 1.20                20
                                                             > 1.20                   40
                                            ▪   Test Condition C (wire-lead bend test):
 Terminal                                          Section Modulus (ZX) (mm3)     Force (N)
 Strength (for
                          MIL-STD-202                      ≤ 1.5x10 -3
                                                                                      0.5
 axial and radial   11
                          Method 211                   1.6x10-3 to 4.2x10-3          1.25
 THT
 components)                                           4.3x10-3 to 1.2x10-2           2.5
                                                       1.3x10-2 to 0.5x10-1            5
                                                       0.6x10-1 to 1.9x10-1           10
                                                           > 1.9x10-1                 20
                                                 For round terminations: ZX = (πd3)/32 where d is
                                                 the lead diameter.
                                                 For strip terminations: ZX = (ba2)/6 where a is the
                                                 thickness of the rectangular strip perpendicular to
                                                 the bending axis, b is the other dimension of the
                                                 rectangular strip.
                                            Note: the values and formulas are per IEC 60068-2-21,
                                            6th Edition.
                                            ▪   In addition to the Method 215 solvents, add an
                                                Aqueous wash chemical and follow chemical
 Resistance to            MIL-STD-202           manufacturer’s recommended parameters (i.e.,
                    12
 Solvents                 Method 215            solution temperature and immersion time).
                                            ▪   Applicable to ink marked components and not laser
                                                marked components.
                                            ▪   Figure 1 of Method 213
 Mechanical               MIL-STD-202       ▪   THT: Condition C
 Shock
                    13                      ▪   SMD: Condition C
                          Method 213
                                            ▪   Tested per the Supplier’s recommended mounting
                                                method.




                                        Page 70 of 107
                                                                                  AEC - Q200 - Rev E
                                                                                     March 20, 2023

Automotive Electronics Council
             Component Technical Committee




                 Table 11: Stress Qualifications for Quartz Crystals (continued)
 Stress                No.   Reference             Additional Requirements
                                                   ▪   5g's for 20 minutes
                                                   ▪   12 cycles each of 3 orientations.
                                                   ▪   Tested per the Supplier’s recommended mounting
                                                       method.
                                                   ▪   Verification of transfer load: during setup, verify that
                             MIL-STD-202               with the selected PCB design (size, thickness and
 Vibration             14
                             Method 204                secure points), or an alternative mount, that the
                                                       transferred load onto the component corresponds
                                                       to the requested load. This verification can be
                                                       achieved using a laser vibrometer or other
                                                       adequate measuring device.
                                                   ▪   Test from 10 Hz - 2000 Hz
                                                   ▪   THT: Conditions B or C
 Resistance to               MIL-STD-202           ▪   SMD: Condition K, time above 217°C, 60s – 150s
                       15
 Soldering Heat              Method 210            ▪   Non-soldered type mounting/attach are not
                                                       applicable.

 ESD                   17    AEC-Q200-002

                                                   ▪   Through-hole Technology (THT:
                                                          o Method A1, Coating Durability Category 2
                                                   ▪   SMD:
                                                          o Method B1, Coating Durability Category 2
                                                          o Method D, Coating Durability Category 2
                                                   ▪   Note: in particular circumstances when SnPb
 Solderability         18    J-STD-002                 reverse compatibility is requested by the User,
                                                       Method A shall be used for THT and Method B
                                                       shall be used for SMD.
                                                   ▪   Magnification 50x
                                                   ▪   Pre and Post Electrical Test not required.
                                                   ▪   Non-soldered type mounting/attach are not
                                                       applicable.
                                                   ▪   Parametrically test per lot and sample size
                                                       requirements.
 Electrical                                        ▪   Summary to show minimum, maximum, mean
                      19     User Specification.
 Characterization                                      and standard deviation at room, minimum and
                                                       maximum operating temperatures.
                                                   ▪   Pre and Post Electrical Test not required.




                                             Page 71 of 107
                                                                                 AEC - Q200 - Rev E
                                                                                    March 20, 2023

Automotive Electronics Council
          Component Technical Committee




                Table 11: Stress Qualifications for Quartz Crystals (continued)
 Stress               No.   Reference             Additional Requirements
                                                  ▪   Applicable to components with exposed cured
                                                      resins or plastic materials.
                                                  ▪   If exposed resins or plastic materials are V-1, V-0
                                                      or 5VA, testing is not required.
                                                  ▪   If exposed resins or plastic materials are not V-1,
                            UL-94 or                  V-0 or 5VA, components or applicable parts of the
 Flammability         20
                            IEC 60695-11-5            component (e.g., sleeve or encapsulant), material
                                                      shall be tested to the Needle Flame Test per IEC
                                                      60695-11-5. Data from previously qualified
                                                      materials can be supplied in place of conducting
                                                      test.
                                                  ▪   Pre and Post Electrical Test not required.

 Board Flex
                      21    AEC-Q200-005
 (SMD)

 Terminal
                      22    AEC-Q200-006
 Strength (SMD)


      Note: For any deviation from the above stresses, refer to Section 2.4.8.

      Back to Table C: Qualification Sample Size
      Back to Table D: Applicable Stress Qualifications




                                            Page 72 of 107
                                                                                                      AEC - Q200 - Rev E
                                                                                                         March 20, 2023

Automotive Electronics Council
             Component Technical Committee

        TABLE 11A: Quartz Crystals Process Change Qualification Guidelines for the
                                    Selection of Tests
For a given change listed below, the Supplier should justify why a suggested test does not apply for the given
component(s) under consideration. Collaboration with their customer base is highly recommended.
  3.      High Temperature Exposure (Storage)       13.     Mechanical Shock
  4.      Temperature Cycling                       14.     Vibration
  7.      Biased Humidity                           15.     Resistance to Soldering Heat
  8.      Operational Life                          18.     Solderability
  9.      External Visual                           19.     Electrical Characterization
  10.     Physical Dimension                        20.     Flammability
  11.     Terminal Strength (THT)                   21.     Board Flex
  12.     Resistance to Solvents                    22.     Terminal Strength (SMD)

Note: A letter or "⚫" indicates that performance of that stress test should be considered (not necessarily
required) for the appropriate process change

             Test # From Table 11        3      4    7     8   9    10   11   12   13      14   15   18   19   20   21   22
             MATERIAL
             Quartz Blank                ⚫      ⚫          ⚫                       ⚫       ⚫              B         ⚫
             Base                               ⚫    ⚫         ⚫    ⚫         ⚫    ⚫       ⚫                        ⚫    ⚫
             Lead/Termination                   ⚫              ⚫    ⚫    ⚫    ⚫            ⚫    ⚫    ⚫    B         ⚫    ⚫
             Glass Seal                  ⚫      ⚫    ⚫     ⚫   ⚫         ⚫    ⚫    ⚫       ⚫    ⚫         B         ⚫    ⚫
             Can/Cap                            ⚫    ⚫         ⚫    ⚫         ⚫    ⚫       ⚫                        ⚫
             Blank Support                      ⚫          ⚫                       ⚫       ⚫              B         ⚫
             Overmold                    ⚫      ⚫              ⚫    ⚫         ⚫    ⚫       ⚫    ⚫              ⚫    ⚫    ⚫
             Case Sealing                ⚫      ⚫    ⚫         ⚫              ⚫    ⚫       ⚫    ⚫         B    ⚫    ⚫
             Electrode                   ⚫      ⚫          ⚫                               ⚫
             Insulator                   ⚫      ⚫              ⚫    ⚫         ⚫            ⚫    ⚫         B    ⚫    ⚫
             PROCESS
             Quartz Blank                       ⚫          ⚫                       ⚫       ⚫              B         ⚫
             Base Assembly               ⚫      ⚫    ⚫         ⚫    ⚫    ⚫         ⚫       ⚫    ⚫    ⚫              ⚫    ⚫
             Blank Etch/Clean                                                                             B
             Electrode Formation                ⚫          ⚫                               ⚫              B         ⚫
             Auto Trim                                                             ⚫       ⚫              B         ⚫
             Bond/Anneal Blank           ⚫      ⚫          ⚫                       ⚫       ⚫              B         ⚫
             Cap/Can Attach              ⚫      ⚫    ⚫     ⚫   ⚫    ⚫              ⚫       ⚫              B         ⚫
             Overmolding                        ⚫              ⚫    ⚫              ⚫       ⚫              B    ⚫    ⚫    ⚫
             Marking                                           ⚫              ⚫
             Aging                                                                 ⚫       ⚫              B         ⚫
             DESIGN
             Quartz Blank                       ⚫                                  ⚫       ⚫              B         ⚫
             Base                        ⚫      ⚫    ⚫         ⚫    ⚫    ⚫         ⚫       ⚫                        ⚫    ⚫
             Lead/Termination                   ⚫              ⚫    ⚫    ⚫         ⚫       ⚫    ⚫    ⚫    B         ⚫    ⚫
             Can/Cap                            ⚫    ⚫         ⚫    ⚫              ⚫       ⚫              B         ⚫
             Blank Support                      ⚫          ⚫                       ⚫       ⚫              B         ⚫
             Package (Molded)                   ⚫              ⚫    ⚫    ⚫    ⚫    ⚫       ⚫    ⚫         B    ⚫    ⚫    ⚫
             Insulator                                         ⚫    ⚫         ⚫
             MISCELLANEOUS
             Mfg. Site Transfer          ⚫      ⚫    ⚫     ⚫   ⚫    ⚫    ⚫    ⚫    ⚫       ⚫    ⚫    ⚫    B    ⚫    ⚫    ⚫
             Material Suppliers                 ⚫          ⚫   ⚫    ⚫    ⚫    ⚫    ⚫       ⚫         ⚫    B    ⚫    ⚫    ⚫
             Process Control Change                            ⚫    ⚫

                                  B = comparative data (unchanged vs. Changed) required

                                                          Page 73 of 107
                                                                                 AEC - Q200 - Rev E
                                                                                    March 20, 2023

Automotive Electronics Council
          Component Technical Committee




                     Table 12: Stress Qualifications for Ceramic Resonators
 Stress                No.   Reference             Additional Requirements
 Pre- and Post-                                    ▪ Test is performed at room temperature except as
 Stress Electrical      1    User Specification.      specified in the applicable stress reference and the
 Test                                                 additional requirements in this Table.
                                                   ▪   Unpowered
                                                   ▪   Tested at maximum specified operating
 High
                                                       temperature or maximum specified storage
 Temperature                 MIL-STD-202
                        3                              temperature (whichever is higher). Minimum test
 Exposure                    Method 108
                                                       temperature shall be 85C
 (Storage)
                                                   ▪   1,000 hours
                                                   ▪   Measurement at 244 hours after test conclusion.
                                                   ▪   Unpowered
                                                   ▪   1,000 Cycles
                                                   ▪   Lower Temperature of the Chamber: -55C
                                                   ▪   Upper Temperature of the Chamber: maximum
                                                       specified operating temperature and shall not
 Temperature                                           exceed 85C.
                        4    JESD22-A104           ▪   Dwell Time (Soak Time):
 Cycling
                                                           o 15 minutes minimum
                                                           o 30 minutes minimum if component weighs
                                                                above 28g
                                                   ▪   Transition Time: 1 minute maximum
                                                   ▪   Measurement at least 24 hours after test
                                                       conclusion.
                                                   ▪   1,000 hours
                                                   ▪   85C/85%RH.
                             MIL-STD-202           ▪   Measurement at 244 hours after test conclusion.
 Humidity Bias          7
                             Method 103            ▪   Rated VDD applied with 1M and inverter in parallel,
                                                       2X resonator CL capacitors between each resonator
                                                       leg and GND.
                                                   ▪   1,000 hours
                                                   ▪   Temperature of the Chamber: maximum specified
 High                                                  operating temperature up to 150C
                             MIL-STD-202
 Temperature            8
                             Method 108            ▪   Rated VDD applied with 1M and inverter in
 Operating Life                                        parallel, 2X resonator CL capacitors between each
                                                       resonator leg and GND.
                                                   ▪   Measurement at 244 hours after test conclusion.

                             MIL-STD-883           ▪   Inspect device construction, marking and
 External Visual        9                              workmanship.
                             Method 2009
                                                   ▪   Pre and Post Electrical Test not required.

 Physical                                          ▪   Verify physical dimensions to the applicable
                       10    JESD22-B100               component specification.
 Dimensions
                                                   ▪   Pre and Post Electrical Test not required.




                                             Page 74 of 107
                                                                              AEC - Q200 - Rev E
                                                                                 March 20, 2023

Automotive Electronics Council
          Component Technical Committee




           Table 12: Stress Qualifications for Ceramic Resonators (continued)
 Stress             No.   Reference         Additional Requirements
                                            ▪ Test THT component lead integrity only.
                                            ▪ Test Condition A (pull test):
                                                     Nominal cross- sectional
                                                                                   Force (N)
                                                          area (mm2)
                                                             ≤ 0.05                    1
                                                          0.06 to 0.10                2.5
                                                          0.11 to 0.20                 5
                                                          0.21 to 0.50                10
                                                          0.51 to 1.20                20
                                                             > 1.20                   40
                                            ▪   Test Condition C (wire-lead bend test):
 Terminal                                          Section Modulus (ZX) (mm3)     Force (N)
 Strength (for
                          MIL-STD-202                      ≤ 1.5x10 -3
                                                                                      0.5
 axial and radial   11
                          Method 211                   1.6x10-3 to 4.2x10-3          1.25
 THT
 components)                                           4.3x10-3 to 1.2x10-2           2.5
                                                       1.3x10-2 to 0.5x10-1            5
                                                       0.6x10-1 to 1.9x10-1           10
                                                           > 1.9x10-1                 20
                                                 For round terminations: ZX = (πd3)/32 where d is
                                                 the lead diameter.
                                                 For strip terminations: ZX = (ba2)/6 where a is the
                                                 thickness of the rectangular strip perpendicular to
                                                 the bending axis, b is the other dimension of the
                                                 rectangular strip.
                                            Note: the values and formulas are per IEC 60068-2-21,
                                            6th Edition.
                                            ▪ In addition to the Method 215 solvents, add an
                                                 Aqueous wash chemical and follow chemical
 Resistance to            MIL-STD-202            manufacturer’s recommended parameters (i.e.,
                    12
 Solvents                 Method 215             solution temperature and immersion time).
                                            ▪ Applicable to ink marked components and not laser
                                                 marked components.
                                            ▪ Figure 1 of Method 213.
 Mechanical               MIL-STD-202       ▪ THT: Condition C
 Shock
                    13
                          Method 213        ▪ SMD: Condition C
                                            ▪ Tested per the Supplier’s recommended mounting
                                                 method.




                                        Page 75 of 107
                                                                                  AEC - Q200 - Rev E
                                                                                     March 20, 2023

Automotive Electronics Council
             Component Technical Committee




             Table 12: Stress Qualifications for Ceramic Resonators (continued)
 Stress               No.   Reference              Additional Requirements
                                                   ▪ 5g's for 20 minutes
                                                   ▪ 12 cycles each of 3 orientations
                                                   ▪ Tested per the Supplier’s recommended mounting
                                                      method.
                                                   ▪ Verification of transfer load: during setup, verify that
                            MIL-STD-202               with the selected PCB design (size, thickness and
 Vibration            14
                            Method 204                secure points), or an alternative mount, that the
                                                      transferred load onto the component corresponds
                                                      to the requested load. This verification can be
                                                      achieved using a laser vibrometer or other
                                                      adequate measuring device.
                                                   ▪ Test from 10 Hz - 2000 Hz
                                                   ▪   THT: Condition B, C or D
 Resistance to              MIL-STD-202            ▪   SMD: Condition K, time above 217°C, 60s – 150s
                      15
 Soldering Heat             Method 210             ▪   Non-soldered type mounting/attach are not
                                                       applicable.

 ESD                  17    AEC-Q200-002

                                                   ▪   Through-hole Technology (THT:
                                                          o Method A1, Coating Durability Category 2
                                                   ▪   SMD:
                                                          o Method B1, Coating Durability Category 2
                                                          o Method D, Coating Durability Category 2
                                                   ▪   Note: in particular circumstances when SnPb
 Solderability        18    J-STD-002                  reverse compatibility is requested by the User,
                                                       Method A shall be used for THT and Method B
                                                       shall be used for SMD.
                                                   ▪   Magnification 50x
                                                   ▪   Pre and Post Electrical Test not required.
                                                   ▪   Non-soldered type mounting/attach are not
                                                       applicable.
                                                   ▪   Parametrically test per lot and sample size
                                                       requirements.
 Electrical                                        ▪   Summary to show minimum, maximum, mean
                      19    User Specification.
 Characterization                                      and standard deviation at room, minimum and
                                                       maximum operating temperatures.
                                                   ▪   Pre and Post Electrical Test not required.
 Board Flex
                      21    AEC-Q200-005
 (SMD)
 Terminal
                      22    AEC-Q200-006
 Strength (SMD)

       Note: For any deviation from the above stresses, refer to Section 2.4.8.

       Back to Table C: Qualification Sample Size
       Back to Table D: Applicable Stress Qualifications



                                             Page 76 of 107
                                                                                                AEC - Q200 - Rev E
                                                                                                   March 20, 2023

Automotive Electronics Council
           Component Technical Committee


  TABLE 12A: Ceramic Resonators Process Change Qualification Guidelines for the
                              Selection of Tests
For a given change listed below, the Supplier should justify why a suggested test does not apply for the given
component(s) under consideration. Collaboration with their customer base is highly recommended.
     3.    High Temperature Exposure (Storage)       13.   Mechanical Shock
     4.    Temperature Cycling                       14.   Vibration
     7.    Biased Humidity                           15.   Resistance to Soldering Heat
     8.    Operational Life                          18.   Solderability
     9.    External Visual                           19.   Electrical Characterization
     10.   Physical Dimension                        21.   Board Flex
     11.   Terminal Strength (THT)                   22.   Terminal Strength (SMD)
     12.   Resistance to Solvents

Note: A letter or "⚫" indicates that performance of that stress test should be considered (not necessarily
required) for the appropriate process change

           Test # From Table 12            3     4     7   8    9   10   11   12   13     14   15   18   19   21   22
           MATERIAL
           Ceramic Element                 ⚫     ⚫         ⚫              ⚫         ⚫     ⚫              B
           Inner Electrode                 ⚫     ⚫         ⚫              ⚫         ⚫     ⚫
           Epoxy Resin Overcoat            ⚫     ⚫    ⚫    ⚫    ⚫    ⚫    ⚫    ⚫
           Outer Electrode                       ⚫              ⚫    ⚫    ⚫    ⚫          ⚫    ⚫    ⚫         ⚫    ⚫
           Wax                                                  ⚫                                        B
           Terminal Solder                       ⚫              ⚫                                   ⚫         ⚫    ⚫
           Element/Lead Attach             ⚫     ⚫         ⚫              ⚫         ⚫     ⚫    ⚫         B
           Case                            ⚫     ⚫         ⚫    ⚫    ⚫         ⚫    ⚫     ⚫    ⚫              ⚫    ⚫
           Case Adhesive/Seal              ⚫     ⚫         ⚫    ⚫    ⚫    ⚫    ⚫    ⚫     ⚫    ⚫              ⚫    ⚫
           Capacitor                       ⚫     ⚫         ⚫              ⚫         ⚫     ⚫    ⚫         B    ⚫    ⚫
           PROCESS
           Ceramic Blank                         ⚫         ⚫              ⚫         ⚫     ⚫              B    ⚫    ⚫
           Lapping                               ⚫                        ⚫         ⚫     ⚫              B    ⚫    ⚫
           Electroding                           ⚫         ⚫              ⚫         ⚫     ⚫              B    ⚫    ⚫
           Cutting                                                        ⚫         ⚫     ⚫              B    ⚫    ⚫
           Annealing                                       ⚫              ⚫         ⚫     ⚫              B    ⚫    ⚫
           Polarize/Freq. Adjust                                                                         B
           Element/Lead Attach                   ⚫         ⚫              ⚫         ⚫     ⚫              B    ⚫    ⚫
           Adhesive/Epoxy Seal                   ⚫    ⚫    ⚫    ⚫                   ⚫     ⚫                   ⚫
           Epoxy Dip & Cure                                ⚫    ⚫    ⚫    ⚫    ⚫
           Wax Application                                      ⚫    ⚫
           Terminal Solder                 ⚫     ⚫         ⚫    ⚫    ⚫    ⚫                         ⚫         ⚫    ⚫
           Marking                                              ⚫              ⚫
           DESIGN
           Ceramic Element                       ⚫         ⚫         ⚫              ⚫     ⚫              B    ⚫
           Electrode/Capacitor                   ⚫         ⚫              ⚫         ⚫     ⚫              B    ⚫    ⚫
           Case                                  ⚫         ⚫    ⚫    ⚫              ⚫     ⚫                   ⚫    ⚫
           Termination                           ⚫         ⚫    ⚫         ⚫         ⚫     ⚫         ⚫         ⚫    ⚫
           MISCELLANEOUS
           Mfg. Site Transfer              ⚫     ⚫    ⚫    ⚫    ⚫    ⚫    ⚫    ⚫    ⚫     ⚫    ⚫    ⚫    B    ⚫    ⚫
           Material Suppliers                    ⚫         ⚫    ⚫    ⚫    ⚫    ⚫    ⚫     ⚫         ⚫    B    ⚫    ⚫
           New/Modified Mfg. Equipment                          ⚫    ⚫

                                B = comparative data (unchanged vs. Changed) required

                                                     Page 77 of 107
                                                                               AEC - Q200 - Rev E
                                                                                  March 20, 2023

Automotive Electronics Council
          Component Technical Committee



           Table 13: Stress Qualifications for Ferrite EMI Suppressors/Filters
 Stress              No.   Reference             Additional Requirements
 Pre- and Post-                                  ▪ Test is performed at room temperature except as
 Stress Electrical   1     User Specification.      specified in the applicable stress reference and the
 Test                                               additional requirements in this Table.
                                                 ▪   Unpowered
                                                 ▪   Tested at maximum specified operating
 High
                                                     temperature or maximum specified storage
 Temperature               MIL-STD-202
                     3                               temperature (whichever is higher). Minimum test
 Exposure                  Method 108
                                                     temperature shall be 85C
 (Storage)
                                                 ▪   1,000 hours
                                                 ▪   Measurement at 244 hours after test conclusion.
                                                 ▪   Unpowered
                                                 ▪   1,000 Cycles
                                                 ▪   Lower Temperature of the Chamber: -55C
                                                 ▪   Upper Temperature of the Chamber: maximum
                                                     specified operating temperature and shall not
                                                     exceed 125C.
 Temperature
                     4     JESD22-A104           ▪   Dwell Time (Soak Time):
 Cycling
                                                         o 15 minutes minimum
                                                         o 30 minutes minimum if component weighs
                                                              above 28g
                                                 ▪   Transition Time: 1 minute maximum
                                                 ▪   Measurement at least 24 hours after test
                                                     conclusion.
 Destructive
 Physical            5     EIA-469               ▪   Pre and Post Electrical Test not required.
 Analysis
                                                 ▪   1,000 hours
                     7
                           MIL-STD-202           ▪   85C/85%RH
 Humidity Bias
                           Method 103            ▪   Measurement at 244 hours after test conclusion.
                                                 ▪   Apply 10% of maximum rated power.
                                                 ▪   1,000 hours
 High                                            ▪   Temperature of the Chamber: maximum specified
                           MIL-STD-202
 Temperature         8                               operating temperature up to 150C.
                           Method 108
 Operating Life                                  ▪   Measurement at 244 hours after test conclusion.
                                                 ▪   Rated IL applied

                           MIL-STD-883           ▪   Inspect device construction, marking and
 External Visual     9                               workmanship.
                           Method 2009
                                                 ▪   Pre and Post Electrical Test not required.
                                                 ▪   Verify physical dimensions to the applicable
 Physical
                     10    JESD22-B100               component specification.
 Dimensions
                                                 ▪   Pre and Post Electrical Test not required.




                                           Page 78 of 107
                                                                              AEC - Q200 - Rev E
                                                                                 March 20, 2023

Automotive Electronics Council
          Component Technical Committee



   Table 13: Stress Qualifications for Ferrite EMI Suppressors/Filters (continued)
 Stress             No.   Reference         Additional Requirements
                                            ▪   Test THT component lead integrity only.
                                            ▪   Test Condition A (pull test):
                                                     Nominal cross- sectional
                                                                                   Force (N)
                                                          area (mm2)
                                                             ≤ 0.05                    1
                                                          0.06 to 0.10                2.5
                                                          0.11 to 0.20                 5
                                                          0.21 to 0.50                10
                                                          0.51 to 1.20                20
                                                             > 1.20                   40
                                            ▪   Test Condition C (wire-lead bend test):
 Terminal                                          Section Modulus (ZX) (mm3)     Force (N)
 Strength (for
                          MIL-STD-202                      ≤ 1.5x10 -3                0.5
 axial and radial   11
                          Method 211                   1.6x10-3 to 4.2x10-3          1.25
 THT
 components)                                           4.3x10-3 to 1.2x10-2           2.5
                                                       1.3x10-2 to 0.5x10-1            5
                                                       0.6x10-1 to 1.9x10-1           10
                                                           > 1.9x10-1                 20
                                                 For round terminations: ZX = (πd3)/32 where d is
                                                 the lead diameter.
                                                 For strip terminations: ZX = (ba2)/6 where a is the
                                                 thickness of the rectangular strip perpendicular to
                                                 the bending axis, b is the other dimension of the
                                                 rectangular strip.
                                            Note: the values and formulas are per IEC 60068-2-21,
                                            6th Edition.
                                            ▪   In addition to the Method 215 solvents, add an
                                                Aqueous wash chemical and follow chemical
 Resistance to            MIL-STD-202           manufacturer’s recommended parameters (i.e.,
                    12
 Solvents                 Method 215            solution temperature and immersion time).
                                            ▪   Applicable to ink marked components and not laser
                                                marked components.
                                            ▪   Figure 1 of Method 213
                                            ▪   THT: Test Condition C
 Mechanical               MIL-STD-202
                    13                      ▪   SMD: Test Condition C
 Shock                    Method 213
                                            ▪   Tested per the Supplier’s recommended mounting
                                                method.




                                        Page 79 of 107
                                                                               AEC - Q200 - Rev E
                                                                                  March 20, 2023

Automotive Electronics Council
            Component Technical Committee



   Table 13: Stress Qualifications for Ferrite EMI Suppressors/Filters (continued)
 Stress              No.   Reference             Additional Requirements
                                                 ▪ 5g's for 20 minutes
                                                 ▪ 12 cycles each of 3 orientations.
                                                 ▪ Tested per the Supplier’s recommended mounting
                                                    method.
                                                 ▪ Verification of transfer load: during setup, verify that
                           MIL-STD-202
Vibration            14                             with the selected PCB design (size, thickness and
                           Method 204
                                                    secure points), or an alternative mount, that the
                                                    transferred load onto the component corresponds to
                                                    the requested load. This verification can be
                                                    achieved using a laser vibrometer or other adequate
                                                    measuring device.
                                                 ▪   THT: Condition B, C or D
 Resistance to             MIL-STD-202           ▪   SMD: Condition K, time above 217°C, 60s – 150s
                     15
 Soldering Heat            Method 210            ▪   Non-soldered type mounting/attach are not
                                                     applicable.

 ESD                 17    AEC-Q200-002

                                                 ▪   Through-hole Technology (THT:
                                                        o Method A1, Coating Durability Category 2
                                                 ▪   SMD:
                                                        o Method B1, Coating Durability Category 2
                                                        o Method D, Coating Durability Category 2
                                                 ▪   Note: in particular circumstances when SnPb
 Solderability       18    J-STD-002                 reverse compatibility is requested by the User,
                                                     Method A shall be used for THT and Method B
                                                     shall be used for SMD.
                                                 ▪   Magnification 50x
                                                 ▪   Pre and Post Electrical Test not required.
                                                 ▪   Non-soldered type mounting/attach are not
                                                     applicable.
                                                 ▪   Parametrically test per lot and sample size
                                                     requirements.
 Electrical                                      ▪   Summary to show minimum, maximum, mean
                     19    User Specification.
 Characterization                                    and standard deviation at room, minimum and
                                                     maximum operating temperatures.
                                                 ▪   Pre and Post Electrical Test not required.




                                           Page 80 of 107
                                                                                 AEC - Q200 - Rev E
                                                                                    March 20, 2023

Automotive Electronics Council
          Component Technical Committee



   Table 13: Stress Qualifications for Ferrite EMI Suppressors/Filters (continued)
 Stress              No.   Reference              Additional Requirements
                                                  ▪   Applicable to components with exposed cured
                                                      resins or plastic materials.
                                                  ▪   If exposed resins or plastic materials are V-1, V-0
                                                      or 5VA, testing is not required.
                                                  ▪   If exposed resins or plastic materials are not V-1,
                           UL 94
                                                      V-0 or 5VA, components or applicable parts of the
 Flammability        20    or
                                                      component (ex: sleeve or encapsulant), material
                           IEC 60695-11-5
                                                      shall be tested to the Needle Flame Test per IEC
                                                      60695-11-5. Data from previously qualified
                                                      materials can be supplied in place of conducting
                                                      test.
                                                  ▪   Pre and Post Electrical Test not required.

 Board Flex
                     21    AEC-Q200-005
 (SMD)

 Terminal Strength
                     22    AEC-Q200-006
 (SMD)
 Electrical
 Transient           30    ISO7637-2              ▪   Test pulses 1 to 3
 Conduction

      Note: For any deviation from the above stresses, refer to Section 2.4.8.

      Back to Table C: Qualification Sample Size
      Back to Table D: Applicable Stress Qualifications




                                            Page 81 of 107
                                                                                                      AEC - Q200 - Rev E
                                                                                                         March 20, 2023

Automotive Electronics Council
                   Component Technical Committee


          TABLE 13A: Ferrite EMI Suppressors/Filters Process Change Qualification
                            Guidelines for the Selection of Tests
 For a given change listed below, the Supplier should justify why a suggested test does not apply for the given
     component(s) under consideration. Collaboration with their customer base is highly recommended.

3.     High Temperature Exposure (Storage) 12.   Resistance to Solvents                    21.        Board Flex
4.     Temperature Cycling                 13.   Mechanical Shock                          22.        Terminal Strength (SMD)
5.     Destructive Physical Analysis       14.   Vibration                                 30.        Electrical Transient Conduction
7.     Biased Humidity                     15.   Resistance to Soldering Heat
8.     Operational Life                    17.   Electrostatic Discharge (ESD)
9.     External Visual                     18.   Solderability
10.    Physical Dimension                  19.   Electrical Characterization
11.    Terminal Strength (THT)             20.   Flammability

Note: A letter or "⚫" indicates that performance of that stress test should be considered (not necessarily
required) for the appropriate process change

      Test # From Table 13          3    4   5   7    8   9    10   11   12      13   14   15    17    18   19    20   21   22   30
      MATERIAL
      Binder Material                   ⚫                                             ⚫                      B
      Dielectric                    ⚫   ⚫    ⚫   ⚫                  ⚫            ⚫    ⚫          ⚫           B         ⚫
      Terminal Interface            ⚫   ⚫    ⚫   ⚫                               ⚫    ⚫          ⚫           B         ⚫
      Conductor Material            ⚫   ⚫    ⚫   ⚫    ⚫             ⚫                 ⚫                      B         ⚫
      Encapsulation                          ⚫            ⚫    ⚫         ⚫                 ⚫
      Lead/Termination                  ⚫                 ⚫    ⚫    ⚫                 ⚫    ⚫            ⚫    B              ⚫
      PROCESS
      Dicing                        ⚫   ⚫        ⚫        ⚫    ⚫         ⚫       ⚫                           B    ⚫
      Conductor Apply               ⚫            ⚫    ⚫                                    ⚫     ⚫           B         ⚫
      Electrode Formation               ⚫    ⚫        ⚫                                          ⚫           B                   ⚫
      Firing Profile                    ⚫    ⚫                                                   ⚫           B         ⚫         ⚫
      Lamination Press                       ⚫   ⚫                                         ⚫                 B         ⚫
      Powder Particle Size              ⚫        ⚫                                         ⚫     ⚫           B         ⚫
      Screen Printing                   ⚫                                                        ⚫           B
      Termination Process           ⚫   ⚫    ⚫   ⚫        ⚫    ⚫    ⚫            ⚫    ⚫    ⚫            ⚫    B         ⚫    ⚫
      DESIGN
      Conductor Thickness           ⚫   ⚫    ⚫                                   ⚫               ⚫           B
      Lead/Term. Thickness              ⚫                 ⚫    ⚫    ⚫                 ⚫                                ⚫    ⚫
      Number of Layers                  ⚫    ⚫   ⚫             ⚫                                 ⚫           B         ⚫
      Termination Area                  ⚫                 ⚫    ⚫                      ⚫                                ⚫    ⚫
      Terminal Interface            ⚫   ⚫    ⚫   ⚫                       ⚫       ⚫    ⚫    ⚫     ⚫           B         ⚫    ⚫    ⚫
      MISCELLANEOUS
      Mfg. Site Transfer            ⚫   ⚫    ⚫   ⚫    ⚫   ⚫    ⚫    ⚫    ⚫       ⚫    ⚫    ⚫     ⚫      ⚫    B    ⚫    ⚫    ⚫
      Material Suppliers            ⚫   ⚫    ⚫   ⚫    ⚫   ⚫    ⚫    ⚫    ⚫       ⚫    ⚫    ⚫     ⚫      ⚫    B    ⚫    ⚫    ⚫
      New/Modified Mfg. Equipment       ⚫        ⚫             ⚫    a                 ⚫          ⚫      ⚫    B


         a = termination equipment only               B = comparative data (unchanged vs. Changed) required




                                                     Page 82 of 107
                                                                             AEC - Q200 - Rev E
                                                                                March 20, 2023

Automotive Electronics Council
          Component Technical Committee




              Table 14: Stress Qualifications for Polymeric Resettable Fuses

 Stress              No.   Reference            Additional Requirements
 Pre- and Post-                                 ▪ Test is performed at room temperature except as
 Stress Electrical   1     User Specification      specified in the applicable stress reference and the
 Test                                              additional requirements in this Table.
                                                ▪   Unpowered
                                                ▪   1,000 Cycles
                                                ▪   Lower Temperature of the Chamber: -40C
                                                ▪   Upper Temperature of the Chamber: maximum
                                                    specified operating temperature and shall not
                                                    exceed 125C.
 Temperature
                     4     JESD22-A104          ▪   Tri-temperature Pre and post stress required.
 Cycling                                        ▪   Dwell Time (Soak Time):
                                                         o 15 minutes minimum
                                                         o 30 minutes minimum if component weighs
                                                             above 28g
                                                ▪   Transition Time: 1 minute maximum
                                                ▪   Measurement at least 24 hours after test
                                                    conclusion.
                                                ▪   1,000 hours
                                                ▪   85C/85%RH
                           MIL-STD-202
 Humidity Bias       7
                           Method 103           ▪   Measurement at 244 hours after test
                                                    conclusion.
                                                ▪   Biased at 10% of hold current.
                                                ▪   1,000 hours
 High                                           ▪   Temperature of the Chamber: maximum specified
                           MIL-STD-202
 Temperature         8                              operating temperature up to 150C.
                           Method 108
 Operating Life                                 ▪   Measurement at 244 hours after test
                                                    conclusion.
                                                ▪   Inspect device construction, marking and
                           MIL-STD-883
 External Visual     9                              workmanship.
                           Method 2009
                                                ▪   Pre and Post Electrical Test not required.
                                                ▪   Verify the physical dimensions to the applicable
 Physical
                     10    JESD22-B100              component specification.
 Dimensions
                                                ▪   Pre and Post Electrical Test not required.




                                          Page 83 of 107
                                                                              AEC - Q200 - Rev E
                                                                                 March 20, 2023

Automotive Electronics Council
          Component Technical Committee




     Table 14: Stress Qualifications for Polymeric Resettable Fuses (continued)

 Stress             No.   Reference         Additional Requirements
                                            ▪ Test THT component lead integrity only.
                                            ▪ Test Condition A (pull test):
                                                     Nominal cross- sectional
                                                                                   Force (N)
                                                          area (mm2)
                                                             ≤ 0.05                    1
                                                          0.06 to 0.10                2.5
                                                          0.11 to 0.20                 5
                                                          0.21 to 0.50                10
                                                          0.51 to 1.20                20
                                                             > 1.20                   40
                                            ▪   Test Condition C (wire-lead bend test):
 Terminal                                          Section Modulus (ZX) (mm3)     Force (N)
 Strength (for
                          MIL-STD-202                      ≤ 1.5x10 -3                0.5
 axial and radial   11
                          Method 211                   1.6x10-3 to 4.2x10-3          1.25
 THT
 components)                                           4.3x10-3 to 1.2x10-2           2.5
                                                       1.3x10-2 to 0.5x10-1            5
                                                       0.6x10-1 to 1.9x10-1           10
                                                           > 1.9x10-1                 20
                                                For round terminations: ZX = (πd3)/32 where d is
                                                the lead diameter.
                                                For strip terminations: ZX = (ba2)/6 where a is the
                                                thickness of the rectangular strip perpendicular to
                                                the bending axis, b is the other dimension of the
                                                rectangular strip.
                                            ▪   Note: the values and formulas are per IEC 60068-2-
                                                21, 6th Edition.
                                            ▪   In addition to the Method 215 solvents, add an
                                                Aqueous wash chemical and follow chemical
                                                manufacturer’s recommended parameters (i.e.,
 Resistance to            MIL-STD-202
                    12                          solution temperature and immersion time).
 Solvents                 Method 215
                                            ▪   Verify marking permanency.
                                            ▪   Applicable to ink marked components and not laser
                                                marked components.
                                            ▪   Figure 1 of Method 213
                                            ▪   THT: Test Condition C
 Mechanical               MIL-STD-202
                    13                      ▪   SMD: Test Condition C
 Shock                    Method 213
                                            ▪   Tested per the Supplier’s recommended mounting
                                                method.




                                        Page 84 of 107
                                                                               AEC - Q200 - Rev E
                                                                                  March 20, 2023

Automotive Electronics Council
            Component Technical Committee




     Table 14: Stress Qualifications for Polymeric Resettable Fuses (continued)

 Stress              No.   Reference             Additional Requirements
                                                 ▪ 5g's for 20 minutes
                                                 ▪ 12 cycles each of 3 orientations.
                                                 ▪ Tested per the Supplier’s recommended mounting
                                                    method.
                                                 ▪ Verification of transfer load: during setup, verify that
                           MIL-STD-202              with the selected PCB design (size, thickness and
Vibration            14
                           Method 204               secure points), or an alternative mount, that the
                                                    transferred load onto the component corresponds to
                                                    the requested load. This verification can be
                                                    achieved using a laser vibrometer or other
                                                    adequate measuring device.
                                                 ▪ Test from 10 Hz - 2000 Hz
                                                 ▪   THT: Condition B, C or D
Resistance to               MIL-STD-202          ▪   SMD: Condition K, time above 217°C, 60s – 150s
                     15
Soldering Heat             Method 210            ▪   Non-soldered type mounting/attach are not
                                                     applicable.
                                                 ▪   Through-hole Technology THT:
                                                        o Method A1, Coating Durability Category 2
                                                 ▪   SMD:
                                                        o Method B1, Coating Durability Category 2
                                                        o Method D, Coating Durability Category 2
                                                 ▪   Note: in particular circumstances when SnPb
Solderability        18    J-STD-002                 reverse compatibility is requested by the User,
                                                     Method A shall be used for THT and Method B
                                                     shall be used for SMD.
                                                 ▪   Magnification 50x
                                                 ▪   Pre and Post Electrical Test not required.
                                                 ▪   Non-soldered type mounting/attach are not
                                                     applicable.
                                                 ▪   Parametrically test per lot and sample size
                                                     requirements.
 Electrical                                      ▪   Summary to show minimum, maximum, mean
                     19    User Specification.
 Characterization                                    and standard deviation at room, minimum and
                                                     maximum operating temperatures.
                                                 ▪   Pre and Post Electrical Test not required.
                                                 ▪   Applicable to components with exposed cured
                                                     resins or plastic materials.
                                                 ▪   If exposed resins or plastic materials are V-1, V-0
                                                     or 5VA, testing is not required.
                                                 ▪   If exposed resins or plastic materials are not V-1,
                           UL 94
                                                     V-0 or 5VA, components or applicable parts of the
 Flammability        20    or
                                                     component (ex: sleeve or encapsulant), material
                           IEC 60695-11-5
                                                     shall be tested to the Needle Flame Test per IEC
                                                     60695-11-5. Data from previously qualified
                                                     materials can be supplied in place of conducting
                                                     test.
                                                 ▪   Pre and Post Electrical Test not required.


                                           Page 85 of 107
                                                                                 AEC - Q200 - Rev E
                                                                                    March 20, 2023

Automotive Electronics Council
          Component Technical Committee




     Table 14: Stress Qualifications for Polymeric Resettable Fuses (continued)

 Stress              No.   Reference              Additional Requirements
 Board Flex
                     21    AEC-Q200-005
 (SMD)

 Terminal Strength
                     22    AEC-Q200-006
 (SMD)
 Short Circuit
 Fault Current       32    AEC-Q200-004
 Durability
 Fault Current
                     33    AEC-Q200-004
 Durability

 End-of-Life Mode
                     34    AEC-Q200-004
 Verification
 Jump Start
                     35    AEC-Q200-004
 Endurance

 Load Dump
                     36    AEC-Q200-004
 Endurance

      Note: For any deviation from the above stresses, refer to Section 2.4.8.

      Back to Table C: Qualification Sample Size
      Back to Table D: Applicable Stress Qualifications




                                            Page 86 of 107
                                                                                                           AEC - Q200 - Rev E
                                                                                                              March 20, 2023

Automotive Electronics Council
                Component Technical Committee


TABLE 14A: Polymeric Resetable Fuses Process Change Qualification Guidelines for
                            the Selection of Tests
For a given change listed below, the Supplier should justify why a suggested test does not apply for the given
component(s) under consideration. Collaboration with their customer base is highly recommended.

   4.     Temperature Cycling                   14.        Vibration                            32.        Short Circuit Current Durability
   7.     Biased Humidity                       15.        Resistance to Soldering Heat         33.        Fault Current Durability
   8.     Operational Life                      17.        Electrostatic Discharge (ESD)        34.        End-of-Life Mode Verification
   9.     External Visual                       18.        Solderability                        35.        Jump Start Endurance
   10.    Physical Dimension                    19.        Electrical Characterization          36.        Load Dump Endurance
   11.    Terminal Strength (THT)               20.        Flammability
   12.    Resistance to Solvents                21.        Board Flex
   13.    Mechanical Shock                      22.        Terminal Strength (SMD)

Note: A letter or “⚫ “ indicates that performance of that stress test should be considered (not necessarily
required) for the appropriate process change.

Test # From Table 14            4   7   8   9         10   11   12   13   14   15   17     18   19    20    21    22   32    33   34    35    36
MATERIAL
PTC Core Material                   ⚫   ⚫   ⚫                                  ⚫                B                            ⚫     ⚫
Marking                                     ⚫                   ⚫
Terminal/Lead                               ⚫         ⚫    ⚫         ⚫    ⚫                ⚫                 ⚫    ⚫
Terminal/Lead Attachment                    ⚫         ⚫              ⚫    ⚫                ⚫                 ⚫    ⚫
Protective Coating                  ⚫   ⚫   ⚫         ⚫                                               ⚫
PROCESS
PTC Forming                         ⚫   ⚫                                      ⚫                      ⚫      ⚫
Substrate Singulation                       ⚫         ⚫
Terminal/Lead Attachment            ⚫   ⚫   ⚫              ⚫                               ⚫                 ⚫    ⚫
Protective Coating                  ⚫   ⚫   ⚫         ⚫
Marking                                     ⚫                   1
DESIGN
Form Factor                                 ⚫         ⚫                                         B
Terminal Configuration (Kink)               ⚫         ⚫    ⚫         ⚫    ⚫
Characteristics Specification                                                                   B
MISCELLANEOUS
Mfg. Site Transfer              ⚫   ⚫   ⚫   ⚫         ⚫    ⚫    1    ⚫    ⚫    ⚫    ⚫      ⚫    B            ⚫    ⚫    ⚫     ⚫     ⚫    ⚫     ⚫


          1 = For components marked with ink only. Laser and stamped marked components shall be exempt
                  from this test.
          B = comparative data (unchanged vs. Changed) required




                                                           Page 87 of 107
                                                                             AEC - Q200 - Rev E
                                                                                March 20, 2023

Automotive Electronics Council
          Component Technical Committee




                           Table 15: Stress Qualifications for Fuses

 Stress              No.   Reference            Additional Requirements
                                                Pre-test:
                                                ▪ Resistance Measurement
                                                       o    Per AEC-Q200-004
                                                       o    Mount fuse as per specification.
                                                       o    Measure fuse on-board resistance @
                                                            10% nominal fuse current rating.
                                                Post-test:
                                                ▪ Resistance Measurement
                                                       o    Per AEC-Q200-004
                                                       o    Mount fuse as per specification.
                                                       o    Measure fuse on-board resistance @
 Pre- and Post-            UL 248,                          10% nominal fuse current rating.
 Stress Electrical   1     IEC 60127 or                o    All samples
 Test                      User Specification   ▪ Current Carrying Capacity
                                                       o Test methodology per UL 248 Series, IEC
                                                            60127 Series or per User spec.
                                                       o Half of samples
                                                       o Room Ambient
                                                ▪ Overload (Time/Current Characteristic) Test
                                                       o    Lowest specification (maximum fusing time)
                                                       o    Test methodology per UL 248 Series,
                                                            IEC 60127 Series or per User spec.
                                                       o    Overload specification per User Spec.
                                                       o    Half of samples
                                                       o    Room Ambient
 High
                                                ▪   Mount fuse as per specification.
 Temperature               MIL-STD-202
                     3                          ▪   1000 hrs @ max. temperature
 Exposure                  Method 108
                                                ▪   Fuses not energized
 (Storage)
                                                ▪    Unpowered
                                                ▪    1,000 Cycles
                                                ▪    Lower Temperature of the Chamber: Lower
                                                     operating temp as specified. Minimum -40°C.
                                                ▪    Upper Temperature of the Chamber: maximum
                                                     specified operating temperature and shall not
 Temperature                                         exceed 125°C.
                     4     JESD22-A104
 Cycling                                        ▪    Dwell Time (Soak Time):
                                                        o 15 minutes minimum
                                                        o 30 minutes minimum if component weighs
                                                             above 28g
                                                ▪    Transition Time: 1 minute maximum
                                                ▪    Measurement at least 24 hours after test
                                                     conclusion.
                                                    ▪ Biased at 10% of Nominal Fuse Current Rating.
                           MIL-STD-202              ▪ 1,000 hours
 Humidity Bias       7
                           Method 103               ▪ 85C, 85% relative humidity
                                                    ▪ Measurement at 244 hours after test conclusion.



                                          Page 88 of 107
                                                                               AEC - Q200 - Rev E
                                                                                  March 20, 2023

Automotive Electronics Council
          Component Technical Committee




                    Table 15: Stress Qualifications for Fuses (continued)

 Stress              No.   Reference         Additional Requirements
                                             ▪ 1,000 hours
                                             ▪ Temperature of the Chamber: maximum specified
 High Temperature          MIL-STD-202
                     8                           operating temperature up to 150°C.
 Operating Life            Method 108
                                             ▪ Biased at the derated nominal fuse current rating.
                                             ▪ Measurement at 244 hours after test conclusion.
                                             ▪   Inspect component construction, marking and
                           MIL-STD-883
 External Visual     9                           workmanship.
                           Method 2009
                                             ▪   Pre and Post Electrical Test not required.
                                             ▪   Verify physical dimensions to the applicable
 Physical
                     10    JESD22-B100           component specification.
 Dimensions
                                             ▪   Pre and Post Electrical Test not required.
                                             ▪   Test THT component lead integrity only
                                             ▪   Test Condition A (pull test):
                                                   Nominal cross-sectional area
                                                                                    Force (N)
                                                              (mm2)
                                                              ≤ 0.05                    1
                                                           0.06 to 0.10                2.5
                                                           0.11 to 0.20                 5
                                                           0.21 to 0.50                10
                                                           0.51 to 1.20                20
                                                              > 1.20                   40
                                             ▪   Test Condition C (wire-lead bend test):
 Terminal                                           Section Modulus (ZX) (mm3)     Force (N)
 Strength (for
                           MIL-STD-202                      ≤ 1.5x10 -3                0.5
 axial and radial    11
                           Method 211                   1.6x10-3 to 4.2x10-3          1.25
 THT
 components)                                            4.3x10-3 to 1.2x10-2           2.5
                                                        1.3x10-2 to 0.5x10-1            5
                                                        0.6x10-1 to 1.9x10-1           10
                                                            > 1.9x10-1                 20
                                                  For round terminations: ZX = (πd3)/32 where d is
                                                  the lead diameter.
                                                  For strip terminations: ZX = (ba2)/6 where a is the
                                                  thickness of the rectangular strip perpendicular to
                                                  the bending axis, b is the other dimension of the
                                                  rectangular strip.
                                             Note: the values and formulas are per IEC 60068-2-21,
                                             6th Edition
                                             ▪ In addition to the Method 215 solvents, add an
                                                  Aqueous wash chemical and follow chemical
 Resistance to             MIL-STD-202            manufacturers recommended parameters (i.e.,:
                     12
 Solvents                  Method 215             solution temperature and immersion time).
                                             ▪ Applicable to ink marked components and not laser
                                                  marked components.




                                         Page 89 of 107
                                                                             AEC - Q200 - Rev E
                                                                                March 20, 2023

Automotive Electronics Council
             Component Technical Committee




                     Table 15: Stress Qualifications for Fuses (continued)

 Stress               No.   Reference         Additional Requirements
                                              ▪   Figure 1 of Method 213
                                              ▪   THT: Test Condition C
 Mechanical                 MIL-STD-202
                      13                      ▪   SMD: Test Condition C
 Shock                      Method 213
                                              ▪   Tested per the Supplier’s recommended
                                                  mounting method.
                                              ▪   5g's for 20 minutes
                                              ▪   12 cycles each of 3 orientations
                                              ▪   Tested per the Suppliers’ s recommended
                                                  mounting method.
                                              ▪   Verification of transfer load: during setup, verify that
                            MIL-STD-202           with the selected PCB design (size, thickness and
 Vibration            14
                            Method 204            secure points), or an alternative mount, that the
                                                  transferred load onto the component corresponds
                                                  to the requested load. This verification can be
                                                  achieved using a laser vibrometer or other
                                                  adequate measuring device.
                                              ▪   Test from 10 Hz -2000 Hz
 Resistance to        15    MIL-STD-202       ▪   THT: Test Condition B, C or D
 Soldering Heat             Method 210        ▪   SMD: Condition K, time above 217°C, 60s – 150s
                                              ▪   Non-soldered type mounting/attach are not
                                                  applicable.
                                              ▪   Through-hole Technology (THT):
                                                     o Method A1, Coating Durability Category 2
                                              ▪   SMD:
                                                     o Method B1, Coating Durability Category 2
                                                     o Method D, Coating Durability Category 2
                                              ▪   Note: in particular circumstances when SnPb
 Solderability        18    J-STD-002              reverse compatibility is requested by the User,
                                                   Method A shall be used for THT and Method B
                                                   shall be used for SMD.
                                              ▪   Magnification 50x
                                              ▪   Pre and Post Electrical Test not required.
                                              ▪   Non-soldered type mounting/attach are not
                                                   applicable.




                                          Page 90 of 107
                                                                             AEC - Q200 - Rev E
                                                                                March 20, 2023

Automotive Electronics Council
          Component Technical Committee




                    Table 15: Stress Qualifications for Fuses (continued)

 Stress              No.   Reference            Additional Requirements
                                                ▪   Characteristics shall be measured for the following
                                                    operating temperature:
                                                      o minimum
                                                      o room
                                                      o maximum
                                                ▪   Resistance Measurement
                                                      o Mount fuse as per specification.
                                                      o Measure fuse on-board resistance @ 10%
                                                           nominal fuse current rating.
                                                      o Conduct at maximum, room, and minimum
                                                           temperature range.
                                                ▪   Current Carrying Capacity
                                                      o Per UL 248 Series or IEC 60127 Series
                                                      o Conduct at maximum, room, and minimum
                           UL 248,
 Electrical                                                temperature range. For minimum and
                     19    IEC 60127 or
 Characterization                                          maximum operating temperatures, rerate
                           User Specification
                                                           the fuse current based on Supplier’s
                                                           recommendation.
                                                ▪   Overload Test
                                                      o Test methodology per UL 248 Series or
                                                           IEC 60127 Series
                                                      o Overload gates per User Spec.
                                                      o Conduct at maximum, room, and minimum
                                                           temperature range.
                                                ▪   Short Circuit Tests
                                                      o Test methodology per UL 248 Series or
                                                           IEC 60127 Series
                                                      o Short circuit value per User Spec.
                                                      o Conduct at maximum, room, and minimum
                                                           temperature range.
                                                ▪   Applicable to components with exposed cured
                                                    resins or plastic materials.
                                                ▪   If exposed resins or plastic materials are V-1, V-0
                                                    or 5VA, testing is not required.
                                                ▪   If exposed resins or plastic materials are not V-1,
                           UL 94
                                                    V-0 or 5VA, components or applicable parts of the
 Flammability        20    or
                                                    component (ex: sleeve or encapsulant), material
                           IEC 60695-11-5
                                                    shall be tested to the Needle Flame Test per IEC
                                                    60695-11-5. Data from previously qualified
                                                    materials can be supplied in place of conducting
                                                    test.
                                                ▪   Pre and Post Electrical Test not required.




                                          Page 91 of 107
                                                                                 AEC - Q200 - Rev E
                                                                                    March 20, 2023

Automotive Electronics Council
          Component Technical Committee




                     Table 15: Stress Qualifications for Fuses (continued)

 Stress               No.   Reference             Additional Requirements
 Board Flex
                      21    AEC-Q200-005
 (SMD)

 Terminal Strength
                      22    AEC-Q200-006
 (SMD)


      Note: For any deviation from the above stresses, refer to Section 2.4.8.

      Back to Table C: Qualification Sample Size
      Back to Table D: Applicable Stress Qualifications




                                            Page 92 of 107
                                                                                                  AEC - Q200 - Rev E
                                                                                                     March 20, 2023

Automotive Electronics Council
           Component Technical Committee


   TABLE 15A: Fuses Process Change Qualification Guidelines for the Selection of
                                   Tests
For a given change listed below, the Supplier should justify why a suggested test does not apply for the given
component(s) under consideration. Collaboration with their customer base is highly recommended.

                     4.     Temperature Cycling                14.       Vibration
                     7.     Biased Humidity                    15.       Resistance to Soldering Heat
                     8.     Operational Life                   18.       Solderability
                     9.     External Visual                    19.       Electrical Characterization
                     10.    Physical Dimension                 20.       Flammability
                     11.    Terminal Strength (THT)            21.       Board Flex
                     12.    Resistance to Solvents             22.       Terminal Strength (SMD)
                     13.    Mechanical Shock

Note: A letter or "⚫" indicates that performance of that stress test should be considered (not necessarily
required) for the appropriate process change.

           Test # From Table 15             4    7     8   9   10    11 12    13 14     15   18    19   20   21   22
           MATERIAL
           Housing                          ⚫    ⚫    ⚫    ⚫   ⚫          ⚫    ⚫   ⚫               B    ⚫
           Marking                                         ⚫              ⚫
           Terminal/Lead                                   ⚫   ⚫     ⚫         ⚫   ⚫          ⚫         ⚫    ⚫
           Terminal/Lead Attachment                        ⚫   ⚫               ⚫   ⚫          ⚫         ⚫    ⚫
           Element                          ⚫         ⚫                        ⚫   ⚫               B
           Filler                           ⚫         ⚫                        ⚫   ⚫               B
           PROCESS
           Element Attach                             ⚫                        ⚫   ⚫
           Terminal/Lead Attachment              ⚫    ⚫    ⚫         ⚫                        ⚫              ⚫    ⚫
           Molding                          ⚫    ⚫    ⚫    ⚫   ⚫          ⚫    ⚫
           Marking                                         ⚫              ⚫
           DESIGN
           Element size                               ⚫        ⚫               ⚫   ⚫               B
           Characteristics Specification                                                           B
           MISCELLANEOUS
           Mfg. Site Transfer               ⚫    ⚫    ⚫    ⚫   ⚫     ⚫         ⚫   ⚫     ⚫    ⚫    B         ⚫    ⚫
           Materials Suppliers              ⚫         ⚫              ⚫             ⚫     ⚫    ⚫    B    ⚫    ⚫    ⚫
           New/Modified Mfg. Equipment      ⚫         ⚫              ⚫             ⚫               B


                                 B = comparative data (unchanged vs. Changed) required




                                                      Page 93 of 107
                                                                                AEC - Q200 - Rev E
                                                                                   March 20, 2023

Automotive Electronics Council
          Component Technical Committee




                     Table 16: Stress Qualifications for Super Capacitors

 Stress               No.   Reference             Additional Requirements
 Pre- and Post-                                   ▪ Test is performed at room temperature except as
 Stress Electrical    1     User Specification.      specified in the applicable stress reference and the
 Test                                                additional requirements in this Table.
                                                  ▪   Unpowered
                                                  ▪   1,000 hours
 High                                             ▪   Tested at maximum specified operating
 Temperature                MIL-STD-202
                      3                               temperature or maximum specified storage
 Exposure                   Method 108
                                                      temperature (whichever is higher). Minimum
 (Storage)
                                                      test temperature shall be 85C.
                                                  ▪   Measurement at 244 hours after test conclusion.
                                                  ▪   Unpowered
                                                  ▪   1,000 Cycles
                                                  ▪   Lower Temperature of the Chamber: -40C
                                                  ▪   Upper Temperature of the Chamber: maximum
                                                      specified operating temperature and shall not
 Temperature                                          exceed 125C.
 Cycling
                      4     JESD22-A104           ▪   Dwell Time (Soak Time):
                                                          o 15 minutes minimum
                                                          o 30 minutes minimum if component weighs
                                                               above 28g
                                                  ▪   Transition Time: 1 minute maximum
                                                  ▪   Measurement at least 24 hours after test
                                                      conclusion.
                                                  ▪   1,000 hours
                            MIL-STD-202           ▪   85C/85%RH
 Humidity Bias        7
                            Method 103            ▪   Measurement at 244 hours after test conclusion.
                                                  ▪   Rated Voltage
                                                  ▪   1,000 hours
                                                  ▪   Temperature of the Chamber: the maximum
 High                                                 permissible ambient temperature at which the
                            MIL-STD-202
 Temperature          8                               component may be continuously operated at rated
                            Method 108
 Operating Life                                       conditions.
                                                  ▪   Rated Voltage applied.
                                                  ▪   Measurement at 244 hours after test conclusion.
                                                  ▪   Inspect device construction, marking and
                            MIL-STD-883
 External Visual      9                               workmanship.
                            Method 2009
                                                  ▪   Pre and Post Electrical Test not required.

                                                  ▪   Verify physical dimensions to the applicable
 Physical
                      10    JESD22-B100               component specification.
 Dimensions
                                                  ▪   Pre and Post Electrical Test not required.




                                            Page 94 of 107
                                                                              AEC - Q200 - Rev E
                                                                                 March 20, 2023

Automotive Electronics Council
          Component Technical Committee




            Table 16: Stress Qualifications for Super Capacitors (continued)

 Stress             No.   Reference         Additional Requirements
                                            ▪   Test THT component lead integrity only
                                            ▪   Test Condition A (pull test):
                                                  Nominal cross-sectional area
                                                                                   Force (N)
                                                             (mm2)
                                                             ≤ 0.05                    1
                                                          0.06 to 0.10                2.5
                                                          0.11 to 0.20                 5
                                                          0.21 to 0.50                10
                                                          0.51 to 1.20                20
                                                             > 1.20                   40
                                            ▪   Test Condition C (wire-lead bend test):
 Terminal                                          Section Modulus (ZX) (mm3)     Force (N)
 Strength (for
                          MIL-STD-202                      ≤ 1.5x10 -3                0.5
 axial and radial   11
                          Method 211                   1.6x10-3 to 4.2x10-3          1.25
 THT
 components)                                           4.3x10-3 to 1.2x10-2           2.5
                                                       1.3x10-2 to 0.5x10-1            5
                                                       0.6x10-1 to 1.9x10-1           10
                                                           > 1.9x10-1                 20
                                                 For round terminations: ZX = (πd3)/32 where d is
                                                 the lead diameter.
                                                 For strip terminations: ZX = (ba2)/6 where a is the
                                                 thickness of the rectangular strip perpendicular to
                                                 the bending axis, b is the other dimension of the
                                                 rectangular strip.
                                            Note: the values and formulas are per IEC 60068-2-21,
                                            6th Edition

                                            ▪   In addition to the Method 215 solvents, add an
                                                Aqueous wash chemical and follow chemical
 Resistance to            MIL-STD-202           manufacturer’s recommended parameters (i.e.,
                    12
 Solvents                 Method 215            solution temperature and immersion time).
                                            ▪   Applicable to ink marked components and not laser
                                                marked components.
                                            ▪   Figure 1 of Method 213
                                            ▪   THT: Test Condition C
 Mechanical               MIL-STD-202
                    13                      ▪   SMD: Test Condition C
 Shock                    Method 213
                                            ▪   Tested per the Supplier’s recommended mounting
                                                method.




                                        Page 95 of 107
                                                                                AEC - Q200 - Rev E
                                                                                   March 20, 2023

Automotive Electronics Council
             Component Technical Committee




              Table 16: Stress Qualifications for Super Capacitors (continued)

 Stress               No.   Reference             Additional Requirements
                                                  ▪ 5g's for 20 minutes
                                                  ▪ 12 cycles each of 3 orientations.
                                                  ▪ Tested per the Supplier’s recommended mounting
                                                     method.
                                                  ▪ Verification of transfer load: during setup, verify that
                            MIL-STD-202              with the selected PCB design (size, thickness and
 Vibration            14
                            Method 204               secure points), or an alternative mount, that the
                                                     transferred load onto the component corresponds
                                                     to the requested load. This verification can be
                                                     achieved using a laser vibrometer or other
                                                     adequate measuring device.
                                                  ▪ Test from 10 Hz - 2000 Hz
                                                  ▪   THT: Conditions B or C
                                                  ▪   SMD: Condition J or K, time above 217°C, 60s -
 Resistance to              MIL-STD-202
                      15                              150s
 Soldering Heat             Method 210
                                                  ▪   Non-soldered type mounting/attach are not
                                                      applicable.
                                                  ▪   Through-hole Technology (THT):
                                                         o Method A1, Coating Durability Category 2
                                                  ▪   SMD:
                                                         o Method B1, Coating Durability Category 2
                                                         o Method D, Coating Durability Category 2
                                                  ▪   Note: in particular circumstances when SnPb
 Solderability        18    J-STD-002                 reverse compatibility is requested by the User,
                                                      Method A shall be used for THT and Method B
                                                      shall be used for SMD.
                                                  ▪   Magnification 50x
                                                  ▪   Pre and Post Electrical Test not required.
                                                  ▪   Non-soldered type mounting/attach are not
                                                      applicable.
                                                  ▪   Parametrically test per lot and sample size
                                                      requirements.
 Electrical                                       ▪   Summary to show minimum, maximum, mean and
                      19    User Specification.
 Characterization                                     standard deviation at room, minimum and
                                                      maximum operating temperatures.
                                                  ▪   Pre and Post Electrical Test not required.




                                            Page 96 of 107
                                                                                 AEC - Q200 - Rev E
                                                                                    March 20, 2023

Automotive Electronics Council
          Component Technical Committee


              Table 16: Stress Qualifications for Super Capacitors (continued)

 Stress             No.    Reference              Additional Requirements
                                                  ▪   Applicable to components with exposed cured
                                                      resins or plastic materials.
                                                  ▪   If exposed resins or plastic materials are V-1, V-0
                                                      or 5VA testing is not required.
                                                  ▪   If exposed resins or plastic materials are not V-1,
                           UL-94 or                   V-0 or 5VA, components or applicable parts of the
 Flammability        20
                           IEC 60695-11-5             component (e.g., sleeve or encapsulant), material
                                                      shall be tested to the Needle Flame Test per IEC
                                                      60695-11-5. Data from previously qualified
                                                      materials can be supplied in place of conducting
                                                      test.
                                                  ▪   Pre and Post Electrical Test not required.

 Board Flex
                     21    AEC-Q200-005
 (SMD)

 Terminal
                     22    AEC-Q200-006
 Strength (SMD)


      Note: For any deviation from the above stresses, refer to Section 2.4.8.

      Back to Table C: Qualification Sample Size
      Back to Table D: Applicable Stress Qualifications




                                            Page 97 of 107
                                                                                            AEC - Q200 - Rev E
                                                                                               March 20, 2023

Automotive Electronics Council
           Component Technical Committee


    TABLE 16A: Super Capacitor Process Change Qualification Guidelines for the
                               Selection of Tests
For a given change listed below, the Supplier should justify why a suggested test does not apply for the given
component(s) under consideration. Collaboration with their customer base is highly recommended.

                3.      High Temperature Exposure (Storage)       13.   Mechanical Shock
                4.      Temperature Cycling                       14.   Vibration
                7.      Biased Humidity                           15.   Resistance to Soldering Heat
                8.      Operational Life                          18.   Solderability
                9.      External Visual                           19.   Electrical Characterization
                10.     Physical Dimension                        22.   Terminal Strength (SMD)
                11.     Terminal Strength (THT)

Note: A letter or "⚫" indicates that performance of that stress test should be considered (not necessarily
required) for the appropriate process change.

                 Test # From Table 16       3   4    7   8    9    10   11   13   14   15    18   19   22
                 MATERIAL
                 Electrode                  ●   ●    ●   ●                                         B
                 Electrolyte                ●   ●    ●   ●                              ●          B
                 Separator                  ●   ●    ●   ●                   ●          ●          B
                 Lead terminal                  ●    ●   ●    ●         ●    ●    ●     ●    ●     B   ●
                 Package                        ●    ●   ●    ●     ●        ●    ●                B
                 Sleeve                         ●        ●    ●
                 PROCESS
                 Element                    ●   ●    ●   ●                                         B
                 Package                        ●    ●   ●    ●     ●                              B
                 DESIGN
                 Electrode                  ●   ●    ●   ●                                         B
                 Electrolyte                ●   ●    ●   ●                              ●          B
                 Separator                  ●   ●    ●   ●                   ●          ●          B
                 Lead terminal                  ●    ●   ●    ●         ●    ●    ●     ●    ●     B   ●
                 Package                        ●    ●   ●    ●     ●        ●    ●                B
                 MISCELLANEOUS
                 Mfg. Site Transfer         ●   ●    ●   ●    ●     ●   ●    ●    ●     ●    ●     B   ●
                 Material Suppliers         ●   ●    ●   ●              ●    ●    ●     ●    ●     B   ●

                               B = comparative data (unchanged vs. Changed) required




                                                 Page 98 of 107
                                                                                  AEC - Q200 - Rev E
                                                                                     March 20, 2023

Automotive Electronics Council
         Component Technical Committee



                               APPENDIX 1: Qualification Family
    1.        General

              The qualification of a particular process will be defined within, but not limited to, the
              categories listed below. The Supplier will provide a complete description of each
              process, case size and material of significance. There must be valid and obvious
              links between the data and the subject of qualification.

              For components to be categorized in a qualification family, they all must share the same:

             a.      Major process,
             b.      Material elements, and
             c.      Basic design

              Basic design qualification family members shall share the same design elements
              except for the constructional attribute (i.e., layer count for capacitors) that is varied
              to achieve the different performance values (i.e., Capacitance value) for the family.
              Examples of attributes are materials, and physical construction.

              All members of a qualification family are qualified by association when the most
              sensitive family members successfully complete qualification testing. Depending
              on the qualification test, a family’s most sensitive component is defined on a test-by-
              test basis. The most sensitive component might be different for each qualification
              test.

              Extensions to an existing qualified family, if the added components meet the most
              sensitive definition, these added components shall be subject to qualification. If
              these added components do not meet the most sensitive definition and therefore fall
              within the qualified family, testing is not required.




                                           Page 99 of 107
                                                                                   AEC - Q200 - Rev E
                                                                                      March 20, 2023

Automotive Electronics Council
            Component Technical Committee



                  APPENDIX 2: Certificate of Design and Construction (CDC)

The following information, as applicable, is required to identify a component which has met the requirements of
this specification. This page is available as a stand-alone document.


                                                        Lead/terminal attachment
   Supplier
                                                        method

   User P/N(s)                                          Package outline drawing
   Supplier P/N(s)                                      Flammability rating
   Data sheet                                           ESD characterization(s)
   Assembly Location                                    Lead/Termination material
   Process Identifier                                   Lead plating/coating
   Final QC Facility Location                           Construction cross section
   Family number                                        Package Subcontractor(s)
   Technology description                               Element composition
   All dimensions in
                                                        Solvent exposure restriction
   millimeters
   Metallization material                               Marking method
                                                        Exceptions taken to
   Number of active layers
                                                        AEC- Q200
   Electrode/Internal element
                                                        Subassembly location
   attachment method
   Thickness range                                      Insulation material
   Package material                                     Temperature Range


   Attachments:                                          Requirements
                                                         1) A separate CDC shall be submitted for each
       1)   Cross section photo
                                                            family as defined by Appendix 1 and
       2)   Package outline drawing
                                                            Appendix 2.
       3)   Special test circuits
                                                         2) Document shall be signed by a responsible
       4)   Letter stating exceptions taken to
                                                            individual at the Supplier who can verify that
            AEC-Q200
                                                            all of the above information is correct.


                                             Type name and sign.

   Completed by:      Date:           Certified By:          Title                           Date:




                                                 Page 100 of 107
                                                                                   AEC - Q200 - Rev E
                                                                                      March 20, 2023

Automotive Electronics Council
           Component Technical Committee



                           APPENDIX 3: Qualification Test Plan Format

The Supplier is requested to complete and submit the Passive Component Qualification Plan as part of the pre-
launch Control Plan whenever production approval submission is required. Acceptance and subsequent sign-
off of the plan will establish a qualification agreement between the User and the Supplier determining
requirements for both new components and process changes prior to commencement of testing. Where “family”
data is being proposed, the plan will document how the reliability testing previously completed fulfills the
requirements outlined in this specification. An approved copy of the qualification plan should be included with
each production approval submission.

The test plan section of the form should detail ONLY the testing that will be performed on the specific component
shown. Testing MUST include the additional requirements listed in the applicable Tables 1-16. For
process change qualifications, multiple components can be included on the same plan. Supporting generic or
family data reports should be noted in the comment section and attached. When requesting use of generic or
family data, attach a separate page detailing similarities or differences between components referencing the
criteria in Appendix1. There must be valid and obvious links between the data and the subject of qualification.

The example below is provided to demonstrate how the Qualification Plan Form should be used. In this case, a
ceramic multilayer capacitor was chosen as being representative of a typical new component qualification
requesting reduced component testing by including generic test data. The component comes from a Supplier
who previously qualified the package, assembly site, etc. This EXAMPLE is shown for illustration purposes
only and should not limit any requirements from Tables 1 through 16 herein.




                                             Page 101 of 107
                                                                                                                                                   AEC - Q200 - Rev E
                                                                                                                                                      March 20, 2023

       Automotive Electronics Council
                            Component Technical Committee



                                   Figure 3: Example of Passive Component Qualification Plan

       Page 1 of 1                                                           Passive Component Qualification Test Plan                                                              Rev: - 2/3/96


               User P/N : N611045BF DDAARA                                                                                                User Component Engineer : John Doe

               User Spec. # : ES-N610450FDAARA                                                                                            General Specification : AEC-Q200

               Supplier : Sam’s Disco
                                    unt Capacitor                                                                                         Supplier Manufacturing Site : Shanghai, Ch ina

               Supplier P/N: N611045 BFDDAARA                                                                                             Required production approval Submission Date 5/1/96


                                                                                                                              Family Type : X7R1206 Ceramic
               Reason for Qualification : New device Qualification

Item                    Test       Test conditions                               Exceptions                                  Est. Start   Est.          # Lots   S. S.    Additional Requirements
                                                                                                                                          Comp.
1                     Electrical   @ -55C, 25C, 125 C                                                                     4/1/09       4/5/09        all      all
                        Test
3                    High Temp     1000 Hours @ 150C                                                                        4/11/09      6/24/09       3        40
                     Exposure
4                    Temperatur    1000 cycles (-55C to +125C)                                                             4/15/09      6/24/09
                      e Cycling
5                    Destructive                                                                                             4/22/09      4/29/09
                      Physical
                      Analysis
6                     Moisture     Cycled 25C to 65C, 80-100% RH,                                                          4/29/09      5/27/09
                     Resistance    24 hours/cycle 10 Cycles
7                     Biased       1000 hours 85C/85RH                          Use attached generic data for this          4/28/09      6/24/09                          generic data uses
                      Humidity                                                   package related test. Comment #1                                                          +70C/85% (rather than
                                                                                                                                                                           85C)
                                                                                                                                                                           Rated and 1.3V. Add 100K
                                                                                                                                                                           Ohm resistor.
8                    Operating     1000 hours 125C with Full rated                                                          4/15/09      6/24/09
                       Life        Voltage
9                     External     Per Spec.                                                                                 4/22/09      4/29/09
                       Visual
10                    Physical     Per user(s) Spec.                                                                         4/22/09      4/28/09
                     Dimensions
12                   Resistance    MIL STD 215 and Aqueous Wash                                                              4/22/09      4/26/09
                     to Solvents   materials
13                   Mechanical    ½ Sine Pulse 1500g Peak                                                                   5/19/09      5/26/09
                       Shock
Test summaries are to include mean, std. Deviation, min. & max. Reading for all endpoint tests.
Comments:

1. Supplier requests 1 lot qualification of this device type in addition to attached reliability reports of similar parts.

Prepared by:
                                                                                                                              Approved by:
(supplier)
                                                                                                                              (User Engineer)




                                                                                      Page 102 of 107
                                                                             AEC - Q200 - Rev E
                                                                                March 20, 2023

Automotive Electronics Council
          Component Technical Committee



                    APPENDIX 4: Data Presentation Format and Content

The Supplier is required to complete and submit an Environmental Test Summary (Figure 4) and Parametric
Verification Summary (Figure 5) with each Passive Component production approval submittal. Figure 4 is an
EXAMPLE of a completed Environmental Test Summary. The content of the example shall be followed in a
similar format.

                              Figure 4: Environmental Test Summary

                          Production Part Approval - Environmental Test Summary

   SUPPLIER                          USER PART NUMBER
   Sam’s Discount Capacitors         N611045BFDAARA

   NAME OF LABORATORY                PART NAME

          SDS Qual Lab.                                       Ceramic Capacitor

   Test                                                                # Lots      Qty       Number
            Description              Test Conditions
    #                                                                  Tested      Tested    Failed

   3        High Temp. Exposure      Per Spec.                         3           120       0

            Destructive Physical
   5                                 Per Spec.                         3           15        0
            Analysis

   9        External Visual          Per Spec.                         3           260       0

   10       Physical Dimensions      Per Spec.                         3           30        0

   12       Resistance to Solvents   Per Spec.                         1           5         0

   13       Mechanical Shock         ½ Sine Pulse 1500g                3           90        0




                                          Page 103 of 107
                                                                               AEC - Q200 - Rev E
                                                                                  March 20, 2023

Automotive Electronics Council
          Component Technical Committee


Figure 5 is an EXAMPLE of a completed Parametric Verification Summary. The content of the example shall
be followed in a similar format.

                            Figure 5: Parametric Verification Summary
                        Production Part Approval - Parametric Verification Summary

Supplier                                    Part Number
SAM’s Discount Passive Components           N611045BFDAARA

Lot Number                                  Temperature
              394A                          -55C

               User Spec.      User Spec.
Test Name                                   Min.          Max.        Mean        Std. Dev.   Cpk
               LSL             USL

Capacitance    0.09 µF         0.11 µF      0.0971 µF     0.1086 µF   0.103 µF    0.0013 µF   1.79

DF             ------          ±2.5%        1.07%         1.98%       1.6%        .092%       3.79

IR             20G            ------       40G          100G       70G        30G        7.03

Temperature
               -15.0%          +15%         -14.83%       -5.97%      -11.4%      1.01%       1.19
Coefficient




                                            Page 104 of 107
                                                                         AEC - Q200 - Rev E
                                                                            March 20, 2023

Automotive Electronics Council
         Component Technical Committee


                                     Revision History

 Rev #     Date of change    Brief summary listing affected sections

   -        April 30, 1996   Initial Release.

  A         June 16, 1997    1.1.1   Add Crystals, Resonators, Ferrites
                             2.1     Changed “qualification program” to “document”; Added “user’s” to
                                     item #2.
                             2.3     Changed 2-10, 2A-10A to 2-13,2A-13A
                             2.4.5   Changed 2-10 to 2-13
                             2.6     Changed 2-10 to 2-13
                             2.7     Changed 2-10 to 2-13
                             3.1     Changed 2-10 to 2-13
                             3.2.2   Changed 2-10, 2A-10A to 2-13,2A-13A
                             4.1     Table 1 - Remove N on Test 12; Add S on Test 21-22
                                     Table 2 - Remove Test 24; Add 1.5mm to Test 15
                                     Table 2A - Remove Test 24
                                     Table 4 - Changed temperature on Test 16
                                     Table 9 - Added 230C, term. coverage Test 15; Changed minutes
                                              to seconds Test 16
                                     Tables 2-10 - Added 24 Hour meas. Tests3,4,6-8; Add 10-2000 Hz
                                              on Test 14
                                     Tables 11-13 - Added Tables 11-13, 11A-13A
                                     Appendix 2 - Added resp. Individual to requirement 2

  B        March 15, 2000    Removed CDF designation through document.
                             Removed Chrysler, Delco, and Ford logo from each heading.
                             Removed Automotive Grade through document.
                             Added Component Technical Committee to each heading.
                             1.2.3 Replaced Automotive with AEC
                                    Tables 14 –14A Added Tables for Polymetric Resettable Fuses.
                                    Changed all references to Tables 2– 13 to 2–14
                                    Changed all references to Tables 2A – 13A to 2A –14A
                             4.1    Changed reference to Table 1-13 to 1-14
                             2.4.1 Changed to Lot requirements are designated in Table1, herein
                                    Tables 2-13, item 18 – Reversed Method a and b for SMD
                                            solderability requirements
                                    Table 3, item 16 – Changed Dwell Time (Soak Time) to 15 minutes
                                    Table 5, item 16 – Changed Dwell Time (Soak Time) to 15 minutes
                                    Table 6, item 21 – Added 3mm board flex for COG devices
                                    Table 1, Added Note A and Note B
                                    Table 1, item 18 - Changed sample size from 10 to 15
                                    Table 1, item 18 – Added each condition
                                    Legend for Table 1- Added Note A and B




                                        Page 105 of 107
                                                                           AEC - Q200 - Rev E
                                                                              March 20, 2023

Automotive Electronics Council
         Component Technical Committee


                            Revision History (continued)

 Rev #     Date of change   Brief summary listing affected sections

  C         June 17, 2005   Acknowledgements – latest information on members
                            Table of Contents – page number corrections
                            1.1.1 Temperature Grades – definition of AEC qualified
                            1.2.1 MIL-PRF-27 reference correction
                            1.2.3 Addition of AEC subspec test method references
                            2.3     editorial
                            2.4.3 editorial
                            3.2     Added section: Qualification of a Lead (Pb) – Free Device
                            3.3.2 comparative testing of parts
                            4.3     Added section: Lead (Pb) – Free Specific Tests
                            4.4     Data maintenance per TS-16949
                            Table 1: Solderability note C and legend description
                            Test 21: AEC-Q200-005 reference in Table of Tests
                            Test 22: AEC-Q200-006 reference in Table of Tests
                            Test 19: B reference in Change tables and legend description
                            Test 27: AEC-Q200-007 reference in Table of Tests
                            Test 8: MIL-PRF-27 reference in Table of Tests #5
                            Appendix 1, family 7 & 8

  D         June 1, 2010    Acknowledgements – latest information on members
                            Notice Statement (page 3) Added
                            Table of Contents – page number corrections
                            (1.1.1): Temperature Grades – definition of AEC qualified
                            (1.1.2): Approval for Use in an Application - editorial
                            (1.2.1): JESD201 and JESD22-A121 addition
                            (1.2.2): IEC ISO/DIS10605 and iNEMI addition.
                            (1.2.3): AEC-Q200-005, -006, -007, Q005 clarification/addition.
                            (2.3): editorial
                            (2.4.4): Prohibit – Dip-Fixturing
                            (2.4.5): Pre- and post-stress electrical tests at room temperature.
                            (3.2): Describe new Qualification of Pb–Free Device requirement.
                            (3.3.1): adverse impact on specific end customer applications.
                            Items 1 through 5 are background information.
                            (3.3.2): baseline for comparative data analysis.
                            Table 1: Lot Size – Test Item 5. Added Items 31 – 36
                            Table 2: Test Items 3,4,7,8,12,15,17,19,21,&22 updated.
                            Table 2A: Collaboration statement added. D added for Tantalums
                            Table 2B: Acceptable Criteria table added.
                            Table 2C: Acceptable Criteria table added.
                            Table 2D: Acceptable Criteria table added.
                            Table 3: Test Items 3,4,7,8,17,20,21,22,&27 updated. Criteria reg
                            Table 3A: Collaboration statement added.
                            Table 3: Test Items 3,4,6,7,8,17,21,&22 updated. Criteria reg




                                      Page 106 of 107
                                                                              AEC - Q200 - Rev E
                                                                                 March 20, 2023

Automotive Electronics Council
            Component Technical Committee


                               Revision History (continued)

 Rev #        Date of change   Brief summary listing affected sections

D (cont.)      June 1, 2010    Table 3: Test Items 3,4,6,7,8,17,21,&22 updated. Criteria reg
                               Table 3A: Collaboration statement added.
                               Table 4: Test Items 3,4,6,7,8,17,21,&22 updated. Criteria reg
                               Table 4A: Collaboration statement added.
                               Table 5: Test Items 3,4,7,8,17,21,&22 updated. Criteria reg
                               Table 5A: Collaboration statement added.
                               Table 6: Test Items 3,4,7,8,17,21,&22 updated. Criteria reg
                               Table 6A/7A: Collaboration statement added.
                               Table 7: Test Items 3,4,7,8,17,21,&22 updated.
                               Table 7B: Acceptable Criteria table added.
                               Table 7C: Acceptable Criteria table added.
                               Table 7D: Acceptable Criteria table added.
                               Table 7E: Acceptable Criteria table added.
                               Table 7F: Acceptable Criteria table added.
                               Table 8: Test Items 4,17, 21, & 22 updated. Criteria reg
                               Table 8A: Collaboration statement added.
                               Table 9: Test Items 3,4,7,8,17, 21, & 22 updated. Criteria reg
                               Table 9A: Collaboration statement added.
                               Table 10: Test Items 4,7,8,17,21,&22 updated. Criteria reg
                               Table 10A: Collaboration statement added.
                               Table 11: Test Items 3,4,7,8,21,&22 updated.
                               Table 11A: Collaboration statement added.
                               Table 11B: Acceptable Criteria table added.
                               Table 12: Test Items 4,17,21,&22 updated.
                               Table 12A: Collaboration statement added.
                               Table 12B: Acceptable Criteria table added.
                               Table 13: Test Items 4,17,21,&22 updated. Criteria reg
                               Table 13A: Collaboration statement added.
                               Table 14: Test Items 4,17,21,&22 updated. Criteria reg
                               Table 14A: Collaboration statement added

   E          March 20, 2023   Revised Sections 1.1, 1.3, 2, 3, 4, Tables 1-14, All Tables xA, All Tables
                               xB, Appendix 1, Appendix 2, Appendix 3, and Appendix 4. Added Sections
                               1.2, 1.4, 1.5, Figure 1, Table A, Figure 2, Table B, Table C, Table D, Table
                               15, Table 16, Figure 3, Figure 4, and Figure 5. Deleted Table 1.




                                         Page 107 of 107
