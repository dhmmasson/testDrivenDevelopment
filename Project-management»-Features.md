# Organisation of the features

The project is organized according to 8 main milestones. Each of these [milestones](#milestones) has some [features](#output-features-list) and functionalities to implement in order to be completed.

# Milestones
* **Pandora-initial** :
    * Description : Initial version of the pandora software : load one Russian flight record and output the
* **Milestone 0** : Mono RU Flight Description
    * Description: Provide basic descriptive summary data of a Russian fighter jet flight
* **Milestone 1** : Mono RU Cockpit Description
    * Description: Provide basic descriptive summary data of a Russian cockpit during a flight
* **Milestone 2** : Mono RU Flight Computation
    * Description: Provide simple computed data about a Russian jet flight
* **Milestone 3** : Mono RU Flight Analysis
    * Description: Extract high-level information from data
* **Milestone 4** : File Handling
    * Description: Handle batch option and US fighter jet files
* **Milestone 5** : Error Management
    * Description: Handle Errors
* **Milestone 6** : Multiple Flights Computations
    * Description: Perform computations using multiple flights data
* **Milestone 7** : Multiple Flights Analysis
    * Description: Extract high-level information about multiple flights






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

## Plane Constructor Integration
* Russian fighter jets
* American fighter jets

# Output features - List
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
An error should start with: "error detected", followed by the name of the error, a minus symbol "-", and finally its details. For example, if the test file 'file1.xyz' is missing 'origin' and 'date' from its header, and 'file2.xyz' is missing 'flight id', the program output will be:


**<p style="text-align: center;">error detected: INCOMPLETE_HEADER - the_example_test_file.xyz</p>**

**<ins>Important</ins>** : In case of multiple files and multiple parameters, the output is organized `alphabetically`.


### List of potential errors:

| Error | Description | Error Name | Error Detail(s) | Example|
|-------------|-------------|------------|-----------------|----------------------------------------|
| Invalid options | Unrecognized options given to the program | INCORRECT_CLI_OPT | ... | ...|
| Missing command line parameters | Required parameter(s) given options are missing | MISSING_OPT_PARAM | ... |...|
| Not implemented | An option is not (yet) implemented | NOT_IMPLEMENTED | ... | ...|
| Missing file | A file given as an input is not found | MISSING_FILE | the file name(s) | error detected: MISSING_FILE - file1 file2 file3|
| Encoding problem | The content of a file has encoding problems (ascii, utf-8, etc) | ENCODING | the file name(s) | error detected: ENCODING - file1 file2 file3|
| Corrupted file | The file cannot be open because of incorrect binary data | CORRUPTED | the file name(s) |error detected: CORRUPTED - file1 file2 file3|
|Missing header | The header section is not in the file | MISSING_HEADER | The file name(s) | error detected: MISSING_HEADER - file1 file2|
|Incomplete header | The header is missing some information | INCOMPLETE_HEADER | file_name=[info1, info2...] | error detected: INCOMPLETE_HEADER - file1=[origin,flight id] file2=[date] |
| Missing columns | Some required columns are not in the file | MISSING_COLUMN | file_name=[col1,col2] | error detected: MISSING_COLUMN - file1=[timestamp] file2=[longitude,latitude] |
| Missing column names | The log file does not contain the column names | MISSING_COLNAMES | the file name(s) | error detected: MISSING_COLNAMES - file1 file2 file3 |
| Incorrect timestamp ordering | The log file is not presenting data lines in a timely ordered way | ORDERING | The fle name(s) | error detected: ORDERING - file1 file2 file3 



