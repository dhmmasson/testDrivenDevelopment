# Organisation of the Features: Milestones and Issues



> **Outline**
> 
> - [Milestones](#milestones)
> - [Input](#input-features-flight-data-records)
>       - [Input](#input)
>       - [Data Validation](#data-validation)
>       - [Origin](#fighter-jet-origin)
> - [Output](#output-features-list)
>       - [Simple Flight Report](#simple-flight-report)
>       - [Cabin Report](#cabin-report)
>       - [Multiple Flights Analysis](#multiple-flights-analysis)



The project is organized according to 8 main milestones. Each of these [milestones](#milestones) has some [features](#output-features-list) and functionalities to implement in order to be completed.

# Milestones
* **Pandora-initial** :
    * Description : Initial version of the Pandora software : load one Russian flight record and output the
    * Number of issues: 3

* **Milestone 0: Initiation to Git**
    * Description: Learn about Git and the Pandora project
    * Number of features: 3
    * List:
        * Exercice 1: Project set up >> CLI option:  
        * Exercice 2: Update team member information >> CLI option:  
        * Exercice 3: Branch >> CLI option:  

* **Milestone 1: Mono RU Flight Description**
    * Description: Provide basic descriptive summary data of a Russian fighter jet flight
    * Number of features: 7
    * List:
        * Average Altitude >> CLI option: -o avgAlt 
        * Max Altitude >> CLI option: -o maxAlt 
        * Average Air Speed >> CLI option: -o avgAirSpeed 
        * Max Air Speed >> CLI option: -o maxAirSpeed 
        * Average Engine Power >> CLI option: -o avgEnginePower 
        * Max Engine Power >> CLI option: -o maxEnginePower 
        * Milestone 0 Full Report >> CLI option:  

* **Milestone 2: Mono RU Cockpit Description**
    * Description: Provide basic descriptive summary data of a Russian cockpit during a flight
    * Number of features: 16
    * List:
        * Average Temperature >> CLI option: -o avgTemp 
        * Min Temperature >> CLI option: -o minTemp 
        * Max Temperature >> CLI option: -o maxTemp 
        * Average Pressure >> CLI option: -o avgPressure 
        * Max Pressure >> CLI option: -o maxPressure 
        * Minimum Pressure >> CLI option: -o minPressure 
        * Average Relative Humidity >> CLI option: -o avgHumidity 
        * Max Relative Humidity >> CLI option: -o maxHumidity 
        * Min Relative Humidity >> CLI option: -o minHumidity 
        * Average Heart Rate >> CLI option: -o avgHeartRate 
        * Max Heart Rate >> CLI option: -o maxHeartRate 
        * Min Heart Rate >> CLI option: -o minHeartRate 
        * Average Oxygen Concentration >> CLI option: -o avgOxygen 
        * Min Oxygen Concentration >> CLI option: -o minOxygen 
        * Max Oxygen Concentration >> CLI option: -o maxOxygen 
        * Milestone 1 Full Report >> CLI option:  

* **Milestone 3: Mono RU Flight Computation**
    * Description: Provide simple computed data about a Russian jet flight
    * Number of features: 9
    * List:
        * Flight Duration >> CLI option: -o flightDuration 
        * Flight Distance >> CLI option: -o flightDistance 
        * Average Acceleration >> CLI option: -o avgAcceleration 
        * Max Acceleration >> CLI option: -o maxAcceleration 
        * Wind Speed >> CLI option: -o windSpeed 
        * Average Mach Speed >> CLI option: -o avgMachSpeed 
        * Max Mach Speed >> CLI option: -o maxMachSpeed 
        * Max Acceleration in G >> CLI option: -o maxAccelG 
        * Milestone 2 Full Report >> CLI option:  

* **Milestone 4: Mono RU Flight Analysis**
    * Description: Extract high-level information from data
    * Number of features: 39
    * List:
        * Take Off Phase Detection >> CLI option: -o takeOff 
        * Cruise Phase Detection >> CLI option: -o cruise 
        * Landing Phase Detection >> CLI option: -o landing 
        * Ratio Distance >> CLI option: -o ratioDistance 
        * Average Air Speed (Take Off) >> CLI option: -o avgAirSpeedTakeOff 
        * Max Air Speed (Take Off) >> CLI option: -o maxAirSpeedTakeOff 
        * Average Engine Power (Take Off) >> CLI option: -o avgEnginePowerTakeOff 
        * Max Engine Power (Take Off) >> CLI option: -o maxEnginePowerTakeOff 
        * Average Air Speed (Cruise) >> CLI option: -o avgAirSpeedCruise 
        * Max Air Speed (Cruise) >> CLI option: -o maxAirSpeedCruise 
        * Average Engine Power (Cruise) >> CLI option: -o avgEnginePowerCruise 
        * Max Engine Power (Cruise) >> CLI option: -o maxEnginePowerCruise 
        * Average Air Speed (Landing) >> CLI option: -o avgAirSpeedLanding 
        * Max Air Speed (Landing) >> CLI option: -o maxAirSpeedLanding 
        * Average Engine Power (Landing) >> CLI option: -o avgEnginePowerLanding 
        * Max Engine Power (Landing) >> CLI option: -o maxEnginePowerLanding 
        * Flight Distance (Take Off) >> CLI option: -o flightDistanceTakeOff 
        * Average Acceleration (Take Off) >> CLI option: -o avgAccelerationTakeOff 
        * Max Acceleration (Take Off) >> CLI option: -o maxAccelerationTakeOff 
        * Wind Speed (Take Off) >> CLI option: -o windSpeedTakeOff 
        * Flight Distance (Cruise) >> CLI option: -o flightDistanceCruise 
        * Average Acceleration (Cruise) >> CLI option: -o avgAccelerationCruise 
        * Max Acceleration (Cruise) >> CLI option: -o maxAccelerationCruise 
        * Wind Speed (Cruise) >> CLI option: -o windSpeedCruise 
        * Flight Distance (Landing) >> CLI option: -o flightDistanceLanding 
        * Average Acceleration (Landing) >> CLI option: -o avgAccelerationLanding 
        * Max Acceleration (Landing) >> CLI option: -o maxAccelerationLanding 
        * Wind Speed (Landing) >> CLI option: -o windSpeedLanding 
        * Most Demanding Phase - Engine Power >> CLI option: -o mostPowerPhase 
        * Most Demanding Phase - Stress >> CLI option: -o mostStressPhase 
        * Most Demanding Phase - Horizontal Acceleration >> CLI option: -o mostAccelPhase 
        * Reaching 80% Max Altitude >> CLI option: -o reachAlt 
        * Reaching 80% Total Distance >> CLI option: -o reachDist 
        * Altitude with Fastest Wind >> CLI option: -o fastWindAlt 
        * Altitude with Highest Aircraft Speed >> CLI option: -o fastJetAlt 
        * Noise of Temperature Sensors >> CLI option: -o noiseTemp 
        * Stressed Pilot >> CLI option: -o stressedPilot 
        * 50% Oxygen Phase >> CLI option: -o oxygenPhase 
        * Milestone 3 Full Report >> CLI option:  

* **Milestone 5: File Handling**
    * Description: Handle batch option and US fighter jet files
    * Number of features: 6
    * List:
        * US files Parser >> CLI option:  
        * Mono US Flight Description >> CLI option:  
        * Mono US Cockpit Description >> CLI option:  
        * Mono US Flight Computation >> CLI option:  
        * Mono US Flight Analysis >> CLI option:  
        * Batch  Option >> CLI option:  

* **Milestone 6: Error Management**
    * Description: Handle Errors
    * Number of features: 13
    * List:
        * Invalid Command Line Options >> CLI option:  
        * Missing Command Line Parameters >> CLI option:  
        * Not Implemented Handling >> CLI option:  
        * Missing Files >> CLI option:  
        * Encoding Problems >> CLI option:  
        * Corrupted Files >> CLI option:  
        * Missing Header >> CLI option:  
        * Incomplete Header >> CLI option:  
        * Missing Columns >> CLI option:  
        * Missing Column Names >> CLI option:  
        * Incorrect Timestamp Ordering >> CLI option:  
        * Incorrect Input >> CLI option:  
        * Milestone 5 Full Report >> CLI option:  

* **Milestone 7: Multiple Flights Computations**
    * Description: Perform computations using multiple flights data
    * Number of features: 19
    * List:
        * Total Cumulative Flight Duration >> CLI option: -o cumulDuration 
        * Total Cumulative Flight Distance >> CLI option: -o cumulDistance 
        * Most Used Airport (Take Off) >> CLI option: -o airportTakeOff 
        * Most Used Airport (Landing) >> CLI option: -o airportLanding 
        * Highest Drag Coef >> CLI option: -o highestDrag 
        * Smallest Drag Coef >> CLI option: -o smallestDrag 
        * Highest Lift Coef >> CLI option: -o highestLift 
        * Smallest Lift Coef >> CLI option: -o smallestLift 
        * Highest Average Speed >> CLI option: -o highestSpeed 
        * Slowest Average Speed >> CLI option: -o slowestSpeed 
        * Highest Altitude >> CLI option: -o highestAltitude 
        * Longest Flight Duration >> CLI option: -o longestDuration 
        * First Landing >> CLI option: -o firstLanding 
        * Last Landing >> CLI option: -o lastLanding 
        * Highest Average Engine Power >> CLI option: -o highestPower 
        * Highest Average Oxygen >> CLI option: -o highestOxygen 
        * Highest Average Heart Beat >> CLI option: -o highestHeartBeat 
        * Lowest Average Heart Beat >> CLI option: -o lowestHeartBeat 
        * Milestone 6 Full Report >> CLI option:  

* **Milestone 8: Multiple Flights Analysis**
    * Description: Extract high-level information about multiple flights
    * Number of features: 4
    * List:
        * Flight Closeness  >> CLI option: -o closeFlight 
        * Flight Closeness (Same origin) >> CLI option: -o closeFlightSameOri 
        * Flight Closeness (Different origin) >> CLI option: -o closeFlightDiffOri 
        * Milestone 7 Full Report >> CLI option:  





# Input features - Flight Data Records

## Input
* Mono: The program takes one file name as an argument on its command line
* Batch management: The program can take several file names on its command line
* Multi records management: The program needs multiple files to process the requested feature (e.g., find the fastest fighter jet)

## Data validation
* Command line
    * Missing argument (done)
* Files
    * Missing
    * Encoding problem
    * Corrupted
* Header
    * Missing
    * Incomplete
* Columns
    * Missing
    * Missing names
* Content
    * Wrong ordering

Refer to the [error handling](#error-handling) section for more details.

## Fighter jet origin
* Russian fighter jets
* American fighter jets

Make sure to distinguish both origin as they do not use the same units when logging data (see [details](./Pandora-»-Flight-Records#parameters-list))

# Output features - List

This is a list of option the program should have in the end. Some of them are explicit options (-o optionName in the command line) and will output a desired result. Some options are functionalities (e.g., possibility to parse both Russian and American files). All these features are on your git repository - created as issues and organized in milestones. The main themes are:

* Reporting (flight and cabin data) 
* Computing
* Analysis
* Error handling
* File management


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

### Anomaly Analysis
* None... yet!



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
* Which flight phase(s) required more than 50% of oxygen concentration in the mask?


### Anomaly Analysis
* None... yet!


## Multiple flights analysis

### Compute
* Total flight duration
* Total distance
* Airport the most used: 
    * For take off
    * For landing
* Which fighter jet:
    * Has the highest drag coefficient? The smallest?
    * Has the highest lift coefficient? The smallest?
    * Goes the fastest?
    * Flies the highest?
    * Flies the longest?
    * Lands first? Last? At what time?
    * Uses the most engine power?
* Which pilot:
    * Uses the most oxygen
        * During the full flight?
        * Per hour?
    * Is the most stressed? Less stressed?

### Analysis
* Which flights flew less than 50km away from each others? 100km away?
    * With the same origin
    * With different origins
* Which fighter jet flew the highest during its cruise phase? The lowest?



# Error Handling
Each errors should be reported according to a standard.
An error should start with: "ERROR", followed by the name of the error, a minus symbol "-", and finally its details. For example, if the test file 'file1.xyz' is missing 'origin' and 'date' from its header, and 'file2.xyz' is missing 'flight id', the program output will be:


**<p style="text-align: center;">ERROR: INCOMPLETE_HEADER - file1.xyz=[date,origin] file2.xyz=[flight id]</p>**

**<ins>Important</ins>** : In case of multiple files and multiple parameters, the output is organized `alphabetically`.


### List of potential errors:

| Error | Description | Error Name | Error Detail(s) | Example|
|-------------|-------------|------------|-----------------|----------------------------------------|
| Invalid options | Unrecognized options given to the program | -- | (already implemented) | ERROR: Invalid Options -x (or --xxxx) is not recognized |
| Missing command line parameters | Required parameter(s) given options are missing | -- | (already implemented) | ERROR: Invalid Options -x (or --xxxx) is missing a parameter|
| Not implemented | An option is not (yet) implemented | -- | (already implemented) | ERROR: Invalid Options -x (or --xxxx) has not been implemented yet |
| Missing file | A file given as an input is not found | MISSING_FILE | the file name(s) | ERROR: MISSING_FILE - file1 file2 file3|
| Encoding problem | The content of a file has encoding problems (ascii, utf-8, etc) | ENCODING | the file name(s) | ERROR: ENCODING - file1 file2 file3|
| Corrupted file | The file cannot be open because of incorrect binary data | CORRUPTED | the file name(s) |ERROR: CORRUPTED - file1 file2 file3|
|Missing header | The header section is not in the file | MISSING_HEADER | The file name(s) | ERROR: MISSING_HEADER - file1 file2|
|Incomplete header | The header is missing some information | INCOMPLETE_HEADER | file_name=[info1, info2...] | ERROR: INCOMPLETE_HEADER - file1=[origin,flight id] file2=[date] |
| Missing columns | Some required columns are not in the file | MISSING_COLUMN | file_name=[col1,col2] | ERROR: MISSING_COLUMN - file1=[timestamp] file2=[longitude,latitude] |
| Missing column names | The log file does not contain the column names | MISSING_COLNAMES | the file name(s) | ERROR: MISSING_COLNAMES - file1 file2 file3 |
| Incorrect timestamp ordering | The log file is not presenting data lines in a timely ordered way | ORDERING | The fle name(s) | ERROR: ORDERING - file1 file2 file3 



