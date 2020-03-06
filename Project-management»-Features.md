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
* Which phase:
  * Demands the most engine power?
  * Is the most stressful for the pilot?
  * Has the highest horizontal acceleration?
* How long did it take for the jet to:
  * Reach 80% of its max altitude?
  * Travel 80% of its planned distance?
* With an average over a time window of 5min, at what altitude level is:
  * The fastest wind outside the aircraft?
  * The highest speed of the aircraft?

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
* None

### Analysis
* None

### Questions
* Assuming a heating system set to 25 ℃ during the whole flight, what is the average noise in the data?
* Did the pilot suffered from stress?
* Which phase(s) required more than 50% of oxygen concentration in the mask?


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

* Which flights flew less than 50km away from each others? 100km away?
* Which flew the highest during its cruise phase? The lowest?
* Which pilot stressed more than the others? Less than the others?
* 


# Error Handling
Each errors should be reported according to a standard.
An error should start with: "error detected", followed by the name of the error and its details. For example, if the test file 'the_example_test_file.xyz' is missing, the program output will be "error detected: MISSING_FILE - the_example_test_file.xyz"

| Error | Description | Error Name | Error Detail(s) | Example|
| Missing file | A file given as an input is not found | MISSING_FILE | the file name(s) | error detected: MISSING_FILE - file1 file2 file3|
*
