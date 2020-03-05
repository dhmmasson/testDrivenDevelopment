# Organisation of the features

The projet

# Milestone
* **Pandora-initial** :
  - Description : Initial version of the pandora software : load one airbus flight record and output the
  - Features: 1,2,3  

# Input features - Flight Data Records
## Input
* Mono
* Batch management
* Multi records management
## Data validation
* Files
    * Ascii problem
    * Corrupted
* Header
    * Missing
    * Incomplete
* Columns
    * Missing
    * Missing names
 
* Content
    * Wrong ordering

## Plane Constructor Integration
* Russian fighter jets
* American fighter jets

# Output features - Analysis
## Simple flight report  

### Get
* Altitude
  * Average
  * Max
* Air speed
  * Average
  * Max
* Total engine power
  * Average
  * Max

### Compute
* Flight Duration
* Flight distance
* Acceleration
  * Average
  * Max
* Wind speed
* Max Speed in mach
* Max Acceleration in g

### Analysis
* Phase detection 
  * Take off
  * Cruise
  * Landing
* Ratio 
  * distance done / line distance between take off and landing
  * "Get" + "Computed" features according to flight phases
* Other?

### Questions
* Which phase demands the most engine power?
* How long did it take for the jet to:
  * reach 80% of its max altitude?
  * travel 80% of its planned distance?

## Cabin report

### Get
* Internal temperature
  * Average
  * Min
  * Max
* Internal pressure
  * Average
  * Min
  * Max
* Internal humidity
  * Average
  * Min
  * Max
* Heart rate
  * Average
  * Min
  * Max
* Oxygen Mask
  * Average
  * Min
  * Max

### Compute
* ?

### Analysis
* 

## Simple flight analysis ?
* Comparison to some objective ( mission time, expected consumption)
* Rapport de grandeur  ...
* Best Engine

## Anomaly Analysis

* Turbulence
* Décrochage
* Panne moteur
* dépréssurisation cabine
* Leak

## Multiple flights analysis
### Same flight
* Best fuel efficiency (ratio consumption / h, min, etc)
* more secure (fewer anomalies)
* Fastest
*

### different flights


# Error Handling

* Missing file
*
