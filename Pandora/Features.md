# Features

| Option | CLI Option | Description |
|---|---|---|
| **CLI Options** | | 
| Version | `--version` / `-v` | Pandora version |
| Help | `--help` / `-h` | Pandora help message |
| Metadata | `-m metadata_name` | Print the value of a metadata field (e.g., `-m jet_id`) |
| Parameters | `--parameters` / `-p` | Print the parameters presented in the flight record file(s) |
| Number of records | `--number` / `-n` | Print the number of records in the flight record file(s) |
| unit | `--unit metric\|imperial` / `-u metric\|imperial` | Choose the output unit system (metric or imperial) |
| metric | `--metric` / `-M` | Similar to `--unit metric` |
| imperial | `--imperial` / `-I` | Similar to `--unit imperial` |
| batch mode | `--batch` / `-b` | Process all flight record files in a folder and print the results in a single output file |
| Debug mode | `--debug` / `-d` | Use to print debug information during the execution of the program |

| Feature | CLI option | Input | Description | Output | Unit | Version |
|---|---|---|---|---|---|---|
| **Single Flight Computations** | | | | | | |
| Starting time | `-o start_time` | | | | | |
| Filenames | `-o filenames` | | | | | |
| Average Altitude | `-o avgAlt` | a flight record file | the average altitude during the flight | altitude | m | |
| Max Altitude | `-o maxAlt` | a flight record file | the maximum altitude during the flight | altitude | m | |
| Average Air Speed | `-o avgAirSpeed` | a flight record file | the average air speed during the flight | speed | m/s | |
| Max Air Speed | `-o maxAirSpeed` | a flight record file | the maximum air speed during the flight | speed | m/s | |
| Average Engine Power | `-o avgEnginePower` | a flight record file | the average total engine power during the flight | power | W | |
| Max Engine Power | `-o maxEnginePower` | a flight record file | the maximum total engine power during the flight | power | W | |
| Average Temperature | `-o avgTemp` | a flight record file | the average temperature in the cockpit during the flight | temperature | ℃ | |
| Min Temperature | `-o minTemp` | a flight record file | the minimum temperature in the cockpit during the flight | temperature | ℃ | |
| Max Temperature | `-o maxTemp` | a flight record file | the maximum temperature in the cockpit during the flight | temperature | ℃ | |
| Average Pressure | `-o avgPressure` | a flight record file | the average pressure in the cockpit during the flight | pressure | Pa | |
| Max Pressure | `-o maxPressure` | a flight record file | the maximum pressure in the cockpit during the flight | pressure | Pa | |
| Minimum Pressure | `-o minPressure` | a flight record file | the minimum pressure in the cockpit during the flight | pressure | Pa | |
| Average Relative Humidity | `-o avgHumidity` | a flight record file | the average relative humidity in the cockpit during the flight | humidity | % | |
| Max Relative Humidity | `-o maxHumidity` | a flight record file | the maximum relative humidity in the cockpit during the flight | humidity | % | |
| Min Relative Humidity | `-o minHumidity` | a flight record file | the minimum relative humidity in the cockpit during the flight | humidity | % | |
| Average Heart Rate | `-o avgHeartRate` | a flight record file | the average pilot's heart rate during the flight | heart rate | bpm | |
| Max Heart Rate | `-o maxHeartRate` | a flight record file | the maximum pilot's heart rate during the flight | heart rate | bpm | |
| Min Heart Rate | `-o minHeartRate` | a flight record file | the minimum pilot's heart rate during the flight | heart rate | bpm | |
| Average Oxygen Concentration | `-o avgOxygen` | a flight record file | the average oxygen concentration delivered by the pilot's mask during the flight | concentration | % | |
| Min Oxygen Concentration | `-o minOxygen` | a flight record file | the minimum oxygen concentration delivered by the pilot's mask during the flight | concentration | % | |
| Max Oxygen Concentration | `-o maxOxygen` | a flight record file | the maximum oxygen concentration delivered by the pilot's mask during the flight | concentration | % | |
| Flight Duration | `-o flightDuration` | a flight record file | the total flight duration | HH:mm:ss | | |
| Flight Distance | `-o flightDistance` | a flight record file | the total flight distance | distance | m | |
| Average Acceleration | `-o avgAcceleration` | a flight record file | the average acceleration during the flight | acceleration | m/s² | |
| Max Acceleration | `-o maxAcceleration` | a flight record file | the maximum acceleration during the flight | acceleration | m/s² | |
| Wind Speed | `-o windSpeed` | a flight record file | the average wind speed during the flight | speed | m/s | |
| Average Mach Speed | `-o avgMachSpeed` | a flight record file | the average speed in Mach during the flight | Mach | | |
| Max Mach Speed | `-o maxMachSpeed` | a flight record file | the maximum speed in Mach during the flight | Mach | | |
| Max Acceleration in G | `-o maxAccelG` | a flight record file | the maximum acceleration during the flight | acceleration | G | |
| Reaching 80% Max Altitude | `-o reachAlt` | a flight record file | the time to reach 80% of maximum altitude during the flight | time / max_altitude | min / m | |
| Reaching 80% Total Distance | `-o reachDist` | a flight record file | the time to arrive at 80% of total flight distance | time / total_distance | min / km | |
| Altitude with Fastest Wind | `-o fastWindAlt` | a flight record file | the altitude with the fastest wind outside the aircraft over a 5 min window | altitude: avg_5min_wind_speed | m: m/s | |
| Altitude with Highest Aircraft Speed | `-o fastJetAlt` | a flight record file | the altitude at which the jet had its fastest speed over a 5 min window | altitude: avg_5min_jet_speed | m: m/s | |
| Noise of Temperature Sensors | `-o noiseTemp` | a flight record file | the average noise in the temperature data assuming a reference temperature of 25℃ | noise_value | ℃ | |
| Stressed Pilot | `-o stressedPilot` | a flight record file | whether the pilot had a stress attack | y/n | | |
| 50% Oxygen Phase | `-o oxygenPhase` | a flight record file | which phase required more than 50% oxygen concentration in the mask | phase_name | | |
| **Flight Phases** | | | | | | |
| Take Off Phase Detection | `-o takeOff` | a flight record file | the start and end time of the take off phase | start=HH:mm:ss / end=HH:mm:ss | | |
| Cruise Phase Detection | `-o cruise` | a flight record file | the start and end time of the cruise phase | start=HH:mm:ss / end=HH:mm:ss | | |
| Landing Phase Detection | `-o landing` | a flight record file | the start and end time of the landing phase | start=HH:mm:ss / end=HH:mm:ss | | |
| Ratio Distance | `-o ratioDistance` | a flight record file | the ratio between the distance actually flown and the point-to-point distance between take off and landing | ratio | | |
| Average Air Speed (Take Off) | `-o avgAirSpeedTakeOff` | a flight record file | the average air speed during the take off phase | speed | m/s | Deprecated in v2 — use `--phase takeOff` with `-o avgAirSpeed` |
| Max Air Speed (Take Off) | `-o maxAirSpeedTakeOff` | a flight record file | the maximum air speed during the take off phase | speed | m/s | Deprecated in v2 — use `--phase takeOff` with `-o maxAirSpeed` |
| Average Engine Power (Take Off) | `-o avgEnginePowerTakeOff` | a flight record file | the average total engine power during the take off phase | power | W | Deprecated in v2 — use `--phase takeOff` with `-o avgEnginePower` |
| Max Engine Power (Take Off) | `-o maxEnginePowerTakeOff` | a flight record file | the maximum total engine power during the take off phase | power | W | Deprecated in v2 — use `--phase takeOff` with `-o maxEnginePower` |
| Average Air Speed (Cruise) | `-o avgAirSpeedCruise` | a flight record file | the average air speed during the cruise phase | speed | m/s | Deprecated in v2 — use `--phase Cruise` with `-o avgAirSpeed` |
| Max Air Speed (Cruise) | `-o maxAirSpeedCruise` | a flight record file | the maximum air speed during the cruise phase | speed | m/s | Deprecated in v2 — use `--phase Cruise` with `-o maxAirSpeed` |
| Average Engine Power (Cruise) | `-o avgEnginePowerCruise` | a flight record file | the average total engine power during the cruise phase | power | W | Deprecated in v2 — use `--phase Cruise` with `-o avgEnginePower` |
| Max Engine Power (Cruise) | `-o maxEnginePowerCruise` | a flight record file | the maximum total engine power during the cruise phase | power | W | Deprecated in v2 — use `--phase Cruise` with `-o maxEnginePower` |
| Average Air Speed (Landing) | `-o avgAirSpeedLanding` | a flight record file | the average air speed during the landing phase | speed | m/s | Deprecated in v2 — use `--phase Landing` with `-o avgAirSpeed` |
| Max Air Speed (Landing) | `-o maxAirSpeedLanding` | a flight record file | the maximum air speed during the landing phase | speed | m/s | Deprecated in v2 — use `--phase Landing` with `-o maxAirSpeed` |
| Average Engine Power (Landing) | `-o avgEnginePowerLanding` | a flight record file | the average total engine power during the landing phase | power | W | Deprecated in v2 — use `--phase Landing` with `-o avgEnginePower` |
| Max Engine Power (Landing) | `-o maxEnginePowerLanding` | a flight record file | the maximum total engine power during the landing phase | power | W | Deprecated in v2 — use `--phase Landing` with `-o maxEnginePower` |
| Flight Distance (Take Off) | `-o flightDistanceTakeOff` | a flight record file | the total flight distance during the take off phase | distance | km | Deprecated in v2 — use `--phase takeOff` with `-o flightDistance` |
| Average Acceleration (Take Off) | `-o avgAccelerationTakeOff` | a flight record file | the average acceleration during the take off phase | acceleration | m/s² | Deprecated in v2 — use `--phase takeOff` with `-o avgAcceleration` |
| Max Acceleration (Take Off) | `-o maxAccelerationTakeOff` | a flight record file | the maximum acceleration during the take off phase | acceleration | m/s² | Deprecated in v2 — use `--phase takeOff` with `-o maxAcceleration` |
| Wind Speed (Take Off) | `-o windSpeedTakeOff` | a flight record file | the average wind speed during the take off phase | speed | m/s | Deprecated in v2 — use `--phase takeOff` with `-o windSpeed` |
| Flight Distance (Cruise) | `-o flightDistanceCruise` | a flight record file | the total flight distance during the cruise phase | distance | km | |
| Average Acceleration (Cruise) | `-o avgAccelerationCruise` | a flight record file | the average acceleration during the cruise phase | acceleration | m/s² | Deprecated in v2 — use `--phase Cruise` with `-o avgAcceleration` |
| Max Acceleration (Cruise) | `-o maxAccelerationCruise` | a flight record file | the maximum acceleration during the cruise phase | acceleration | m/s² | Deprecated in v2 — use `--phase Cruise` with `-o maxAcceleration` |
| Wind Speed (Cruise) | `-o windSpeedCruise` | a flight record file | the average wind speed during the cruise phase | speed | m/s | Deprecated in v2 — use `--phase Cruise` with `-o windSpeed` |
| Flight Distance (Landing) | `-o flightDistanceLanding` | a flight record file | the total flight distance during the landing phase | distance | km | Deprecated in v2 — use `--phase Landing` with `-o flightDistance` |
| Average Acceleration (Landing) | `-o avgAccelerationLanding` | a flight record file | the average acceleration during the landing phase | acceleration | m/s² | Deprecated in v2 — use `--phase Landing` with `-o avgAcceleration` |
| Max Acceleration (Landing) | `-o maxAccelerationLanding` | a flight record file | the maximum acceleration during the landing phase | acceleration | m/s² | Deprecated in v2 — use `--phase Landing` with `-o maxAcceleration` |
| Wind Speed (Landing) | `-o windSpeedLanding` | a flight record file | the average wind speed during the landing phase | speed | m/s | Deprecated in v2 — use `--phase Landing` with `-o windSpeed` |
| Most Demanding Phase — Engine Power | `-o mostPowerPhase` | a flight record file | the phase which required the most average engine power | phase_name:power | W | |
| Most Demanding Phase — Stress | `-o mostStressPhase` | a flight record file | the phase which provoked the highest average heart rate | phase_name:heart_beat | bpm | |
| Most Demanding Phase — Horizontal Acceleration | `-o mostAccelPhase` | a flight record file | the phase with the highest average horizontal acceleration | phase_name:acceleration | m/s² | |
| **Cross Flights Computations** | | | | | | |
| Total Cumulative Flight Duration | `-o cumulDuration` | a folder containing flight record file(s) | the cumulative flight duration across all files | HH:mm:ss | | |
| Total Cumulative Flight Distance | `-o cumulDistance` | a folder containing flight record file(s) | the cumulative flight distance across all files | distance | km | |
| Most Used Airport (Take Off) | `-o airportTakeOff` | a folder containing flight record file(s) | the airport most often used for take off | airport_name | | |
| Most Used Airport (Landing) | `-o airportLanding` | a folder containing flight record file(s) | the airport most often used for landing | airport_name | | |
| Highest Drag Coef | `-o highestDrag` | a folder containing flight record file(s) | the fighter jet with the highest drag coefficient | jet_id:drag_coef | | |
| Smallest Drag Coef | `-o smallestDrag` | a folder containing flight record file(s) | the fighter jet with the smallest drag coefficient | jet_id:drag_coef | | |
| Highest Lift Coef | `-o highestLift` | a folder containing flight record file(s) | the fighter jet with the highest lift coefficient | jet_id:lift_coef | | |
| Smallest Lift Coef | `-o smallestLift` | a folder containing flight record file(s) | the fighter jet with the smallest lift coefficient | jet_id:lift_coef | | |
| Highest Average Speed | `-o highestSpeed` | a folder containing flight record file(s) | the fighter jet with the fastest average speed during its flight | jet_id:speed | km/h | |
| Slowest Average Speed | `-o slowestSpeed` | a folder containing flight record file(s) | the fighter jet with the slowest average speed during its flight | jet_id:speed | km/h | |
| Highest Altitude | `-o highestAltitude` | a folder containing flight record file(s) | the fighter jet which flew the highest | jet_id:max_altitude | m | |
| Longest Flight Duration | `-o longestDuration` | a folder containing flight record file(s) | the fighter jet which flew the longest | jet_id:duration | HH:mm:ss | |
| First Landing | `-o firstLanding` | a folder containing flight record file(s) | the fighter jet which landed first | jet_id:airport_name:landing_time | HH:mm:ss | |
| Last Landing | `-o lastLanding` | a folder containing flight record file(s) | the fighter jet which landed last | jet_id:airport_name:landing_time | HH:mm:ss | |
| Highest Average Engine Power | `-o highestPower` | a folder containing flight record file(s) | the fighter jet which used the highest average engine power | jet_id:power | W | |
| Highest Average Oxygen | `-o highestOxygen` | a folder containing flight record file(s) | the fighter jet which used the highest average oxygen concentration | jet_id:oxygen | % | |
| Highest Average Heart Beat | `-o highestHeartBeat` | a folder containing flight record file(s) | the fighter jet whose pilot had the highest average heart beat | jet_id:beat | bpm | |
| Lowest Average Heart Beat | `-o lowestHeartBeat` | a folder containing flight record file(s) | the fighter jet whose pilot had the lowest average heart beat | jet_id:beat | bpm | |
| Flight Closeness | `-o closeFlight` | a folder containing flight record file(s) | jets that flew less than 50 km from each other | [jet_id1, jet_id2]:min_distance (alphabetical order) | km | |
| Flight Closeness (Same origin) | `-o closeFlightSameOri` | a folder containing flight record file(s) | jets that flew less than 50 km from each other and share the same origin (US/RU) | [jet_id1, jet_id2]:min_distance (alphabetical order) | km | |
| Flight Closeness (Different origin) | `-o closeFlightDiffOri` | a folder containing flight record file(s) | jets that flew less than 50 km from each other and are from different origins (US/RU) | [jet_id1, jet_id2]:min_distance (alphabetical order) | km | |
