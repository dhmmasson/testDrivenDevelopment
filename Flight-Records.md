# Flight records

> **Outline**
- [File Structure](#file-structure)
    + [List of metadata fields](#list-of-metadata-fields)
  * [Data Section](#data-section)
      - [Data record](#data-record)


A flight records is a text file describing a flight. It contains global information about the flight ( plane, operating company, flight number, ... [see for the complete list](#metadata-fields) ) as well as parameters values recorded along the flight ( GPS coordinates, air speed, fuel level, ... [see here for the complete list](#data-fields) )

# File Structure

A record is a file is composed of two sections, [metadata](#Metadata-structure) and [flight data](#Data-structure) separated by an empty line.
> ```
Metadata
[Empty Line]
Data
```
_Fig.1 The flight record is composed of two  sections_

## Metadata Section
The metadata section of the flight record file contains information
relative to the plane and the flight. Header fields are colon-separated key-value pairs in clear-text string format, terminated by a carriage return (CR) and line feed (LF) character sequence. The end of the metadata section is indicated by an empty field(line), resulting in the transmission of two consecutive CR-LF pairs.
> ```
field:value
....
field:value
```
_Fig.2 The metadata section is a list of colon-separated key-value pairs_

### List of metadata fields

Constructor
: [Airbus](./Constructors:-Airbus), [Boeing](./Constructors:-Boeing)

Plane Model
: Name of the plane, depends on the constructor, _e.g._ A300, B737

Operator
: Company that operates the flight. _e.g._ Air France, KLM...

Flight Number
: Unique identifier for the flight, _e.g._ AF8080, KL3021...

## Data Section
The Data structure contains the information recorded during the flights. X-Y parameters are recorded in a [CSV](https://en.wikipedia.org/wiki/Comma-separated_values) format. The first line is the header indicating the content of the data lines.
> ```
Header
Data record
...
Data record
```
_Fig.3 Data section is a csv table of  parameters values describing a flight_

#### Header
The header line is located at the top of the data section. It indicates which parameters were recorded for this flight. The complete list of possible parameters can be found [there](#Parameters-list). Some parameters are mandatory and will always be in the same position (_e.g._ timestamp is always first). Some parameters are optional and depends mostly on the plane (_e.g._ there will be as many engine thrust columns as there are engine on the plane).  
> ```
Timestamp,Parameter,...,Parameter
```
_fig.4_ The header line

#### Data record
A data line represents one point in time (denoted by the timestamp) during the flight. It is a record of all the parameters at this moment.   
> ```
Value,Value,...,Value
```
_fig.5_ the record structure

### Parameters list

Specifics about the parameters list vary among [constructors](./Constructors). See each one for specific information about them.
