  SimSurfing
  Multilayer Ceramic Capacitors
  Characteristics Viewer
  Measurement Conditions




                                            September, 2022
                                 Murata Manufacturing Co., Ltd

                                                                       13 September 2022
Copyright © Murata Manufacturing Co., Ltd. All rights reserved. 2019
目次

                                                                  Page
     1. Outline of this document                                      3

     2. S-parameter                                                   4

     3. DC Bias Characteristics                                       7

     4. Temperature Characteristics                                   9

     5. Temperature Rise Characteristics                            11

     6. AC Voltage Characteristics                                  13




                                                                                                                  2
                                           Copyright © Murata Manufacturing Co., Ltd. All rights reserved. 2019
 1. Outline of this document

Simsurfing provides DC bias characteristics, Temperature characteristics, Temperature rise (Ripple
current), AC voltage characteristics and S-parameter in addition to basic characteristics.
This document explains how this data was prepared.




                                                                                                                                         3
                                                                  Copyright © Murata Manufacturing Co., Ltd. All rights reserved. 2019
 2. S-parameter (1/3)

S-parameter library provides the S-parameter data which could be used in circuit designs.
Below are the details of the procedure for measuring S-parameter data, the applied land pattern, the
measurement equipment, and the measurement conditions for capacitors.

1. Measurement Procedure
   The measurement procedure is indicated below. The S-parameter data is measured with two ports
   using a network analyzer and measurement jig, as shown mainly in Fig. 1.
                                                                                                    Network Analyzer
  (1) Correction
      Two kinds of correction, SOLT (partly SOL) and TRL, are used.
      SOLT applies Murata’s original land pattern (Short, Open, Load, and
      Thru).
      Meanwhile, TRL uses Murata’s original land pattern (Thru, Reflect,
      Line, Match).
                                                                                                        Measurement
  (2) Measurement                                                                                        Equipment
      After soldering the capacitor to the land pattern, we fix it to a
      measurement jig connected to a network analyzer, impedance analyzer,
      and measure it.

  (3) Extraction of S-parameter data for the capacitor alone                             Fig.1 Measurement of
                                                                                            S-parameter data
      In the S-parameter data, although the characteristics of the land pattern
      and measurement equipment are eliminated by correction and electrical delay, the characteristics of
      the via holes and the land pattern are still included in the measurement . Therefore, the data of the
      capacitor itself is extracted by eliminating the characteristics of the via holes and the land pattern.
                                                                                                                                            4
                                                                     Copyright © Murata Manufacturing Co., Ltd. All rights reserved. 2019
 2. S-parameter (2/3)

                                                                 LW Dimension       Land Pattern[mm]
2. Land pattern                                                 JIS[mm] EIA[inch]    a      b      C
                                                                 0201M   008004     0.11   0.12 0.145
                                                                 0402M    01005     0.2    0.18   0.23
                                                                 0603M    0201      0.3    0.35   0.40
                                                                 1005M    0402      0.5    0.45   0.60
                                                                 1608M    0603      0.8    0.7    0.8
                                                                 2012M    0805      1.2    0.7    1.1
                                                                 2828M    1111      2.1    0.9    2.6          c
                                                                 3216M    1206      2.4    0.9    1.4
                                                                 3225M    1210      2.4    0.9    2.3
                                                                 4532M    1812      3.5    1.4    3.0                       b
                                                                 4520M    1808      3.5    1.4    1.8
                                                                 5750M    2220      4.6    1.6    4.8                       a
                                                                 0510M    0204      0.2    0.3    1.0
                                                                 0816M    0306      0.3    0.4    1.6
                                                                 1220M    0508      0.6    0.5    1.8
                                                                                                                            b
                                                                 1632M    0612      0.8    0.7    2.8
                                                                 2040M    0816      0.9    0.8    4.0


                                                                              Fig.2 Structure of Land Pattern
3. Measurement Equipment
   Listed below is the equipment used in the measurements.

  [Temperature compensating type capacitor] (For a capacitor of 1000 pF or more, the same conditions as those
                                                        used for a high dielectric constant type capacitor are used.)
  (1) Impedance analyzer : E4991A/B (Keysight Technologies)
  (2) Network Analyzer : E5071C/N5225A (Keysight Technologies)
  (3) Measurement jig    : PC-SMA/PC-V (YOKOWO)

  [High dielectric constant type capacitor]
  (1) Impedance analyzer : E4990A/4294A (Keysight Technologies)
  (2) Network Analyzer : E5061B/E5071C (Keysight Technologies)
  (3) Measurement jig       : PC-SMA (YOKOWO)                 Copyright © Murata Manufacturing Co., Ltd. All rights reserved. 2019
                                                                                                                                   5
 2. S-parameter (3/3)

4. Measurement Condition
   In the measurements, the frequency is classified into a higher range and a lower range.
   The proper conditions are applied to each frequency. Table 1 shows the measurement conditions for
   a temperature compensating type capacitor, and Table 2 shows the measurement conditions for a
   high dielectric constant type capacitor.


   Types of freq.              Lower Freq.                Higher Freq. 1              Higher Freq. 2                       Higher Freq. 2
 Network Analyzer/             E4991A/B                   E5071C                         N5225A                            N5225A
Impedance Analyzer       Keysight Technologies      Keysight Technologies          Keysight Technologies             Keysight Technologies
   Range of freq.          100MHz to 3GHz             100MHz to 8.5GHz              500MHz to 20GHz                     100MHz to 30GHz
                                  SOL                                                                                         SOLT
   Correction Kit                                                            TRL
                         (+ low-loss capacitor)                                                                          + de-embedding
 Connection Mode                  １port                                              2 port shunt mode

                    Table 1 Measurement conditions for a temperature compensating type capacitor




              Types of freq.              Lower Freq. 1             Lower Freq. 2                    Higher Freq.
           Network Analyzer/           E4990A/4294A                   E5061B                        E5071C
          Impedance Analyzer        Keysight Technologies       Keysight Technologies         Keysight Technologies
             Range of freq.           100Hz to 100kHz              100Hz to 100kHz                100kHz to 6GHz
              Correction Kit                  SOL                          SOLT                            TRL
            Connection Mode                                                       2 port shunt mode
                     Table 2 Measurement conditions for a high dielectric constant type capacitor
                                                                                                                                                              6
                                                                                       Copyright © Murata Manufacturing Co., Ltd. All rights reserved. 2019
 3. DC Bias Characteristics (1/2)

The capacitance of multilayer ceramic chip capacitors changes when DC bias voltage is applied.
There are two types of multilayer ceramic capacitors: capacitors for temperature compensation and
high dielectric constant capacitors. Capacitors for temperature compensation (C0G type etc.) hardly
change when DC bias voltage is applied. On the other hand, the high dielectric constant type (X5R
type etc.) changes when DC bias voltage is applied. Fig.3 shows an example of the DC bias
characteristics of the C0G type and X5R type.


                               20

                                0




              Cap.Change[%]
                               -20

                               -40                                                                             X5R

                               -60
                                                                                                               C0G
                               -80

                              -100
                                     0   2            4           6           8            10
                                                      DC Bias[Vdc]


                                             Fig.3 An example of DC bias characteristics


Simsurfing provides the capacitance value and capacitance change rate at any DC bias voltage.
Simsurfing will not show DC bias effects on capacitance for C0G/NP0 type capacitors because they
do not experience a remarkable change in capacitance.
                                                                                                                                                              7
                                                                                       Copyright © Murata Manufacturing Co., Ltd. All rights reserved. 2019
 3. DC Bias Characteristics (2/2)

1. Measurement Equipment
   Typical measurement equipment is shown below. (Fig.4 and Fig.5)




                                                               Fig.5 Measurement jig: Test fixture16034E/G
                                                                       （Keysight Technologies）
  Fig.4 Measurement equipment: LCRmeter E4980A
              （Keysight Technologies）




2. Measure Settings (C: nominal capacitance)
   (1) Measure frequency          : C≦10uF 1kHz, C＞10uF 120Hz
   (2) Measure voltage*: C≦10uF（6.3V以下） & C＞10uF 0.5Vrms
                                    C≦10uF（10V以上） 1Vrms
   (3) DC bias voltage : From 0Vdc to Rated voltage
   (4) DC bias apply duration     : 60 sec
   (5) Measure temperature        : 25℃±3℃

 * For some items, measure voltage is different from others.                                                                               8
                                                                    Copyright © Murata Manufacturing Co., Ltd. All rights reserved. 2019
 4. Temperature Characteristics (1/2)

The capacitance of multilayer ceramic chip capacitors changes with temperature. Therefore EIA
standards classify temperature characteristics. There are two types of chip multilayer ceramic
capacitors: capacitors for temperature compensation and high dielectric constant capacitors.
Capacitors for temperature compensation (C0G, NP0 type etc.) show little change in capacitance due
to temperature. On the other hand, the high dielectric constant type (X5R, X7R etc.) demonstrates a
typical change in temperature. Fig.6 shows an example of the temperature characteristics of the C0G
type and X5R type. Table.3 lists the operating temperature range and capacitance tolerance of the
C0G type and X5R type.

                          30
                          20
                                                  X5R      C0G


          Cap.Change[％]
                          10
                                                                          Code      Operating                 Capacitance Change
                           0                                                       Temperature                  or Temperature
                          -10                                                        Range                        Coefficient
                          -20
                                                                          C0G      -55 to 125℃                  0±30ppm/deg ℃
                          -30
                                -60 -40 -20   0     20 40 60 80 100 120
                                                                          X5R      -25 to 85℃                           ±15%
                                                  Temperature[℃]
                                  Fig.6 Temperature characteristics         Table.3 Temperature characteristics (EIA)



Simsurfing provides capacitance value and capacitance change rate at any temperature.
Additionally, Simsurfing provides temperature characteristics at 50% rated voltage (VDC).
Simsurfing will not show temperature effects on capacitance for C0G/NP0 type capacitors because
they do not experience a remarkable change in capacitance.
                                                                                                                                                         9
                                                                                  Copyright © Murata Manufacturing Co., Ltd. All rights reserved. 2019
4. Temperature Characteristics (2/2)

1. Measurement equipment
   Typical measurement equipment is listed below.
   (1) LCR Meter     : E4980A/4284A（Keysight Technologies）
   (2) Test chamber  : Thermostatic chamber


2. Measuring conditions (C: Nominal Capacitance)
   (1) Measuring Frequency       : C≦10uF 1kHz, C＞10uF 120Hz
   (2) AC voltage*               : C≦10uF（6.3V and less） and C＞10uF                   0.5Vrms
                                   C≦10uF（10V and over） 1Vrms
   (3) DC bias                   : 50% of the related voltage (VDC)
   (4) DC bias applied time      : 60 sec

 * For some items, measure voltage is different from others.




                                                                                                                                      10
                                                               Copyright © Murata Manufacturing Co., Ltd. All rights reserved. 2019
 5. Temperature Rise Characteristics (1/2)

When ripple current is applied to multilayer ceramic chip capacitors, the capacitor generates heat.
This internal temperature rise cannot be disregarded. While Murata does not guarantee a ripple
current rating, it is recommended that the temperature rise does not exceed 20℃. Fig.7 show a
temperature rise characteristics of high dielectric type of capacitors.

                                               40

                                               35




                    Temperature Rise [deg.C]
                                               30

                                               25

                                               20                                                                     1MHz
                                               15                                                                     500KHz

                                               10                                                                     100kHz

                                                5

                                                0
                                                    0   0.5    1      1.5     2     2.5    3     3.5

                                                                   Current[Arms]


                                                              Fig.7 Temperature Rise Characteristics


Simsurfing provides temperature rise characteristics at 50% of the rated voltage (VDC). Simsurfing
provides this data for high dielectric constant type capacitors that have a capacitance value of 1uF or
greater.
                                                                                                                                                                        11
                                                                                                 Copyright © Murata Manufacturing Co., Ltd. All rights reserved. 2019
 5. Temperature Rise Characteristics (2/2)

1. Measurement Equipment
   Fig.8(a) shows a circuit diagram of this measuring system. The test device is soldered onto a glass
  epoxy board and put into an acrylic box. An infrared thermometer is attached on the top surface of
  the acrylic box to measure chip’s surface temperature. Fig8(b) shows a model diagram of the acrylic
  box.

                                                                                 Infrared
                                                                               thermometer
               Choke coil

                               Voltmeter                     Test devise
                 High
                 frequency                  V
    DC
    power        source
    source
                                            A                 Current probe



                      (a) Circuit diagram                                            (b) Model diagram of terminal Box

                                                Fig.8 Temperature rise characteristics

2. Measurement Conditions
  (1) Ripple frequency                                   : Up to three conditions in the range from 20kHz
                                                           to 1MHz (Sine wave)
 (2) Measurement base temperature                        : 25℃±3℃
 (3) DC bias                                             : 50% of rated voltage (VDC)
                                                                                                                                                          12
                                                                                   Copyright © Murata Manufacturing Co., Ltd. All rights reserved. 2019
 6. AC Voltage Characteristics (1/2)

The capacitance of monolithic ceramic chip capacitors changes when AC voltage is applied.
Those capacitors are classified into temperature compensation type and high dielectric constant type.
The capacitance of the temperature compensation type (C0G, NP0 type, etc.) rarely changes when
AC voltage is applied. However, the capacitance of the high dielectric constant type (X5R) changes
when AC voltage is applied. Fig.9 shows the typical AC voltage data of both C0G and X5R types.

                              10

                               5




              Cap.Change[%]
                               0
                                                                                                                     X5R
                               -5
                                                                                                                     C0G
                              -10

                              -15

                              -20
                                    0.0   0.5              1.0             1.5                   2.0
                                                   AC Voltage[Vrms]


                                                Fig.9 AC Voltage Characteristics Data


Simsurfing provides the capacitance data and the change of capacitance value by an optional AC
voltage. However, Simsurfing does not include the data of capacitors that are of the temperature
compensating type as there is no influence by AC voltage.

                                                                                                                                                               13
                                                                                        Copyright © Murata Manufacturing Co., Ltd. All rights reserved. 2019
 6. AC Voltage Characteristics (2/2)

1. Measurement Equipment
  Typical measure equipment is shown below. (Fig.4 and Fig.5)




                                                      Fig.5 Measurement jig: Test fixture16034E/G
   Fig.4 Measurement Equipment: LCRmeter E4980A                     （Keysight Technologies）
                   （Keysight Technologies）




2. Measurement Conditions (C: nominal capacitance)
   (1) Frequency       ：C≦10uF 1kHz, C＞10uF 120Hz
   (2) AC bias voltage ：0.01 to 2.0Vrms
   (3) Time            ：30 sec
   (4) Temperature     ：25℃±3℃



                                                                                                                                  14
                                                           Copyright © Murata Manufacturing Co., Ltd. All rights reserved. 2019
