# Name

pandora - a [CLI](CLI) tool to analyze [Flight-records](Flight-Records) data to provide summary and high-level information based on low-level sensor data (e.g., fighter jet position).

# Synopsis

```
java -jar pandora.jar [-v|-h]
java -jar pandora.jar [OPTIONS] ...sources

...source - path to flightRecord files or folder containing flightRecord files

OPTIONS o:m:bhvd
-b, --batch,            Batch Mode - process all files in the source folder one by one
-d, --debug,            Debug - print additional debug information on Unhandled 
-h, --help,             Help - print this help message
-m <metadata>, --metadata <metadata>  Metadata - Print the value of the specified metadata
-o <feature>, --output <feature>,   output - Print only the specified feature at the end
-p, --parameters        Parameters - List in alphabetical order the parameters presents in the source
-v, --version,          Version - print the version of the application 

Implemented Features

<Feature List>
```

## Usage

the main usage of pandora is to parse one or several flight records and to output on the command line some computed values. The default mode is to output a **full report** of all the [Features](#Features) (see example). The other mode is the **single feature output mode** triggered by the ```-o or --output``` option, in that mode only the value of the requested feature is printed (with no prefix, nor units)

# EXAMPLES

Print the [Semantic-Versioning](Semantic-Versioning) of the pandora project:

```bash
$ java -jar pandora.jar --version 
pandora@1.0.1
```

print the filenames

```bash
$ java -jar pandora.jar -o filenames d.frd b.frd a
a
b.frd
d.frd
```

Print the maximum altitude reached during a given flight:

```bash
$ java -jar pandora.jar -o maxAlt test/resources/0_201_MiG-23MLD.frd
14321
```

With no option pandora produce a **Full report**,

```bash 
$ java -jar pandora.jar test/resources/0_201_MiG-23MLD.frd 
Flight Report for flight:201
avgAcceleration: -0.36
avgAccelerationCruise: -0.41
avgAccelerationLanding: 4.30
avgAccelerationTakeOff: -1.02
avgAirSpeed: 273.38
avgAirSpeedCruise: 275.11
avgAirSpeedLanding: 89.91
avgAirSpeedTakeOff: 74.84
avgAlt: 4874.94
avgEnginePower: 323097967.62
avgEnginePowerCruise: 325944892.58
avgEnginePowerLanding: 20038604.28
avgEnginePowerTakeOff: 7425623.46
avgHeartRate: 88.80
avgHumidity: 7.53
avgMachSpeed: 0.87
avgOxygen: 68.45
avgPressure: 25133.12
avgTemp: 25.30
cruise: start=04:00:32 / end=04:13:03
fastJetAlt: 7878.79: 762.91
fastWindAlt: 7801.41: 122.69
flightDistance: 246.63
flightDistanceCruise: 246.04
flightDistanceLanding: 0.56
flightDistanceTakeOff: 0.03
flightDuration: 00:12:36
filename: test/resources/0_201_MiG-23MLD.frd 
landing: start=04:13:03 / end=04:13:08
maxAccelG: 27.66
maxAcceleration: 271.20
maxAccelerationCruise: 271.20
maxAccelerationLanding: 35.85
maxAccelerationTakeOff: 0.00
maxAirSpeed: 641.15
maxAirSpeedCruise: 641.15
maxAirSpeedLanding: 98.90
maxAirSpeedTakeOff: 74.84
maxAlt: 11095.51
maxEnginePower: 2092177462.68
maxEnginePowerCruise: 2092177462.68
maxEnginePowerLanding: 36671730.55
maxEnginePowerTakeOff: 7830065.57
maxHeartRate: 100.00
maxHumidity: 8.89
maxMachSpeed: 2.22
maxOxygen: 99.93
maxPressure: 27661.17
maxTemp: 33.21
minHeartRate: 78.60
minHumidity: 6.43
minOxygen: 35.66
minPressure: 22706.67
minTemp: 17.45
mostAccelPhase: Landing:6.82
mostPowerPhase: Cruise:325944892.58
mostStressPhase: Cruise:88.81
noiseTemp: -0.30
oxygenPhase: Cruise,Landing
ratioDistance: 1.55
reachAlt: 9.40 / 11095.51
reachDist: 8.95 / 246629.25
stressedPilot: n
takeOff: start=04:00:31 / end=04:00:32
windSpeed: 24.05
windSpeedCruise: 24.05
windSpeedLanding: 25.96
windSpeedTakeOff: 3.44
```

# Options

- -b, --batch,  
  **Batch Mode** - process all files in the source folder one by one
- -d, --debug  
   **Debug** - print additional debug information on Unhandled error. By default pandora should be as silent as possible, only outputting what is expected by the -o option or the full report. For debug purposes you can print additional debug information when the option -d is used.
- -h, --help  
  **Help** - Print an help message and quit
- -m arg, --metadata arg  
  **Metadata** - Print the value of the specified metadata
- -o \<feature\>, --output \<feature\>  
  **Output** - Print only the result of the specified [Feature](Features) on the command line
- -p, --parameters  
  **Parameters** - List in alphabetical order the parameters presents in the source
- -v, --version,  
  **Version** - print the version of the application

## Features

- avgAlt  
  Average Altitude
- maxAlt  
  Max Altitude
- avgAirSpeed  
  Average Air Speed
- maxAirSpeed  
  Max Air Speed
- avgEnginePower  
  Average Engine Power
- maxEnginePower  
  Max Engine Power
- avgTemp  
  Average Temperature
- minTemp  
  Min Temperature
- maxTemp  
  Max Temperature
- avgPressure  
  Average Pressure
- maxPressure  
  Max Pressure
- minPressure  
  Minimum Pressure
- avgHumidity  
  Average Relative Humidity
- maxHumidity  
  Max Relative Humidity
- minHumidity  
  Min Relative Humidity
- avgHeartRate  
  Average Heart Rate
- maxHeartRate  
  Max Heart Rate
- minHeartRate  
  Min Heart Rate
- avgOxygen  
  Average Oxygen Concentration
- minOxygen  
  Min Oxygen Concentration
- maxOxygen  
  Max Oxygen Concentration
- flightDuration  
  Flight Duration
- flightDistance  
  Flight Distance
- avgAcceleration  
  Average Acceleration
- maxAcceleration  
  Max Acceleration
- windSpeed  
  Wind Speed
- avgMachSpeed  
  Average Mach Speed
- maxMachSpeed  
  Max Mach Speed
- maxAccelG  
  Max Acceleration in G
- reachAlt  
  Reaching 80% Max Altitude
- reachDist  
  Reaching 80% Total Distance
- fastWindAlt  
  Altitude with Fastest Wind
- fastJetAlt  
  Altitude with Highest Aircraft Speed
- noiseTemp  
  Noise of Temperature Sensors
- stressedPilot  
  Stressed Pilot
- cumulDuration  
  Total Cumulative Flight Duration
- cumulDistance  
  Total Cumulative Flight Distance
- airportTakeOff  
  Most Used Airport (Take Off)
- airportLanding  
  Most Used Airport (Landing)
- highestDrag  
  Highest Drag Coef
- smallestDrag  
  Smallest Drag Coef
- highestLift  
  Highest Lift Coef
- smallestLift  
  Smallest Lift Coef
- highestSpeed  
  Highest Average Speed
- slowestSpeed  
  Slowest Average Speed
- highestAltitude  
  Highest Altitude
- longestDuration  
  Longest Flight Duration
- firstLanding  
  First Landing
- lastLanding  
  Last Landing
- highestPower  
  Highest Average Engine Power
- highestOxygen  
  Highest Average Oxygen
- highestHeartBeat  
  Highest Average Heart Beat
- lowestHeartBeat  
  Lowest Average Heart Beat
- closeFlight  
  Flight Closeness
- closeFlightSameOri  
  Flight Closeness (Same origin)
- closeFlightDiffOri  
  Flight Closeness (Different origin)
- takeOff  
  Take Off Phase Detection
- cruise  
  Cruise Phase Detection
- landing  
  Landing Phase Detection
- ratioDistance  
  Ratio Distance
- avgAirSpeedTakeOff  
  Average Air Speed (Take Off)
- maxAirSpeedTakeOff  
  Max Air Speed (Take Off)
- avgEnginePowerTakeOff  
  Average Engine Power (Take Off)
- maxEnginePowerTakeOff  
  Max Engine Power (Take Off)
- avgAirSpeedCruise  
  Average Air Speed (Cruise)
- maxAirSpeedCruise  
  Max Air Speed (Cruise)
- avgEnginePowerCruise  
  Average Engine Power (Cruise)
- maxEnginePowerCruise  
  Max Engine Power (Cruise)
- avgAirSpeedLanding  
  Average Air Speed (Landing)
- maxAirSpeedLanding  
  Max Air Speed (Landing)
- avgEnginePowerLanding  
  Average Engine Power (Landing)
- maxEnginePowerLanding  
  Max Engine Power (Landing)
- flightDistanceTakeOff  
  Flight Distance (Take Off)
- avgAccelerationTakeOff  
  Average Acceleration (Take Off)
- maxAccelerationTakeOff  
  Max Acceleration (Take Off)
- windSpeedTakeOff  
  Wind Speed (Take Off)
- flightDistanceCruise  
  Flight Distance (Cruise)
- avgAccelerationCruise  
  Average Acceleration (Cruise)
- maxAccelerationCruise  
  Max Acceleration (Cruise)
- windSpeedCruise  
  Wind Speed (Cruise)
- flightDistanceLanding  
  Flight Distance (Landing)
- avgAccelerationLanding  
  Average Acceleration (Landing)
- maxAccelerationLanding  
  Max Acceleration (Landing)
- windSpeedLanding  
  Wind Speed (Landing)
- mostPowerPhase  
  Most Demanding Phase - Engine Power
- mostStressPhase  
  Most Demanding Phase - Stress
- mostAccelPhase  
  Most Demanding Phase - Horizontal Acceleration
- oxygenPhase  
  50% Oxygen Phase
