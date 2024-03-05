# Flight records

> **Outline**
> 
> - [Test files](#test-files)
> - [File Structure](#file-structure)
> - [Metadata Section](#list-of-metadata-fields)
> - [Data Section](#data-section)
>       - [RU](#russian-fighter-jets-ru)
>       - [US](#american-fighter-jets-us)



A flight records is a text file describing a flight. It contains global information about the flight (flight id, origin, ... [complete list](#metadata-section)), as well as parameters values recorded during the flight (GPS coordinates, air speed, ... [complete list](#parameters-list) )

# Test files

[Folder full of test files](https://github.com/Estia-advanced-programming/pandora-public/tree/master/flightRecords)

# File Structure

A record is a file composed of two sections, [metadata](#metadata-section) and [flight data](#data-section) separated by an empty line.
> ```
> Metadata
> [Empty Line]
> Data
> ```
> _Fig.1 The flight record is composed of two  sections_

## Metadata Section
The metadata section of the flight record file contains information relative to the plane and the flight. Header fields are colon-separated key-value pairs in clear-text string format, terminated by a carriage return (CR) and line feed (LF) character sequence. The end of the metadata section is indicated by an empty  line, resulting in the transmission of two consecutive CR-LF pairs.
> ```
> field:value
> ....
> field:value
> ```
> _Fig.2 The metadata section is a list of colon-separated key-value pairs_

### List of metadata fields

> ```
> flight id:601
> flight code:F-14A
> origin:US
> date:2011-06-01
> from:krasnodar pashkovsky
> to:tbilissi-lochini
> motor(s):2
> mass aircraft:41780
> mass fuel:41780
> lift coef:1.9650056483374456
> drag coef:0.010121101720646569
> ```
> _Fig.3 Example of a metadata section_

* **flight id**: A unique identifier
* **flight code**: The code name of the fighter jet
* **origin**: The origin of the fighter jet (US or RU)
* **date**: The date of the flight (yyyy-mm-dd)
* **from**: The take off airport name  
* **to**: The landing airport name
* **motor(s)**: The number of engines the jet has
* **mass aircraft**: The mass of the fighter jet
* **mass fuel**: The mass of fuel at take off in the fighter jet
* **lift coef**: The (overall) lift coefficient of the fighter jet 
* **drag coef**: The (overall) drag coefficient of the fighter jet 

**<ins>Important</ins>**: Weights are in `kg` in RU files, `lbs` in US files. 

## Data Section
The Data structure contains the information recorded during the flights. Parameters are recorded in a [CSV](https://en.wikipedia.org/wiki/Comma-separated_values) format. The first line is the header indicating the content of the data lines (_column names_).
> ```
> Header
> Data record
> ...
> Data record
> ```
> _Fig.4 Data section is a csv table of  parameters values describing a flight_

#### Column Names
The line with column names is located at the top of the data section. It indicates which parameters were recorded for this flight. The complete list of possible parameters can be found [there](#parameters-list). Some parameters are mandatory and will always be in the same position (_e.g._ timestamp is always first). Some parameters are optional and depends mostly on the plane (_e.g._ there will be as many engine thrust columns as there are engine on the plane).  
> ```
> Timestamp,Parameter,...,Parameter
> ```
> _fig.5_ The header line

#### Data Record
A data line represents one point in time (denoted by the timestamp) during the flight. It is a record of all the parameters at this moment.   
> ```
> Value,Value,...,Value
> ```
> _fig.6_ the record structure

### Parameters List

RU and US fighter jets do not use the same units when logging their data.

#### Russian Fighter Jets (RU)

| Parameter name | Presence | Data Type | Unit | Description | Example |
|----------------|----------------|----------|-----------------|-----------------------------------------|---------------|
| timestamp | Required First | Decimal | s | Elapsed time in second since 01/01/1970 | 1583010425910.56 |
| longitude | Required  | Decimal | Decimal Degrees (°)  | Location longitude. Positive values are toward the north and east directions. | 2.9382915 |
| latitude | Required | Decimal | Decimal Degrees (°) | Location latitude. Positive values are toward the north and east directions. | 79.982 |
| altitude | Required | Decimal | Meter (m) | Height above sea level | 2985.9909092 |
| roll | Optional | Decimal | Decimal Degrees (°) | Roll is positive when rolling the aircraft to the right | 0.8 |
| pitch | Optional | Decimal | Decimal Degrees (°) | Pitch is positive when taking-off | 1.5 |
| yaw | Optional | Decimal | Decimal Degrees (°) | Yaw is clockwise relative to the true north | 224.8 |
| heading | Optional | Decimal | Decimal Degrees (°) | Heading is the yaw relative to the true north of the flat world. It is required because the native world north usually does not match spherical world north because of projection errors. | 224.8 |
| air_speed | Required | Decimal | Meter per second (m/s) | Wind speed reported by external sensors  | 516.6514247099457 |
| engine_X | Required | Decimal | Watt (W) | Power of engine number X  | 30565986.61627765 |
| temperature_in | Required | Decimal | Celsius Degree (℃) | Cockpit temperature  | 27.156045641442 |
| humidity_in | Required | Decimal | Percentage (%) | Relative humidity  | 45.971654984 |
| pressure_in | Required | Decimal | Pascal (Pa) | Cockpit pressure  | 27.156045641442 |
| heart_rate | Required | Decimal | Beats per Minute (bpm) | Pilot's heart beats  | 80.00 |
| oxygen_mask | Required | Decimal | Percentage (%) | Oxygen concentration sent to the pilot  | 78.3458795665 |



#### American Fighter Jets (US)

| Parameter name | Presence | Data Type | Unit | Description | Example |
|----------------|----------------|----------|-----------------|-----------------------------------------|---------------|
| timestamp | Required First | Decimal | s | Elapsed time in second since 01/01/1970 | 1583010425910.56 |
| longitude | Required  | Decimal | Decimal Degrees (°)  | Location longitude. Positive values are toward the north and east directions. | 2.9382915 |
| latitude | Required | Decimal | Decimal Degrees (°) | Location latitude. Positive values are toward the north and east directions. | 79.982 |
| altitude | Required | Decimal | Feet (ft) | Height above sea level | 2985.9909092 |
| roll | Optional | Decimal | Decimal Degrees (°) | Roll is positive when rolling the aircraft to the right | 0.8 |
| pitch | Optional | Decimal | Decimal Degrees (°) | Pitch is positive when taking-off | 1.5 |
| yaw | Optional | Decimal | Decimal Degrees (°) | Yaw is clockwise relative to the true north | 224.8 |
| heading | Optional | Decimal | Decimal Degrees (°) | Heading is the yaw relative to the true north of the flat world. It is required because the native world north usually does not match spherical world north because of projection errors. | 224.8 |
| air_speed | Required | Decimal | Miles per Hour (mph) | Wind speed reported by external sensors  | 516.6514247099457 |
| engine_X | Required | Decimal | HorsePower (hp) | Power of engine number X  | 30565986.61627765 |
| temperature_in | Required | Decimal | Kelvin Degree (K) | Cockpit temperature  | 27.156045641442 |
| humidity_in | Required | Decimal | Percentage (/100) | Relative humidity  | 0.45971654984 |
| pressure_in | Required | Decimal | Pound-Force per Square Inch (psi) | Cockpit pressure  | 27.156045641442 |
| heart_rate | Required | Number | Beats per Minute (bpm) | Pilot's heart beats  | 80 |
| oxygen_mask | Required | Decimal | Percentage (/100) | Oxygen concentration sent to the pilot  | 0.783458795665 |

