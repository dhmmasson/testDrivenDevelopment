# CHANGELOG

This Changelog tracks the change relative to the Advanced Programming Class. It does not follow the instructions from [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) nor does the version follow [Semantic-Versioning](Semantic-Versioning).

# 2024

- 2023-03-20 - Update the documentation about test-driven-developement, add a tester for milestone 0 in the starterpack
- 2023-03-07 - [Synchronize-Update-From-The-Starterpack](Synchronize-Update-From-The-Starterpack) to help you merge the modification from the teachers

# 2023

- 17/03/2023 - 14:22: For features `fastJetAlt` and `fastWindAlt`, forget about the 5min window. Just return the first altitude at which the maximum is encountered. You should hence simply have `altitude (m): max_wind_speed (m/s)` and `altitude (m): max_jet_speed (m/s)`.

# 2022

- 08/03/2022 - 12:23: Updated a mistake in the template / skeleton code where `flightDuration` was stored as an `int`. **Teams should merge immediately** the pull request `Correction for first pandora run` by williamDelamare.  

# 2021

- 24/03/2021 - 10:16: New algorithm for **phase detection** in [instructions](Constants.md#algorithm).
- 09/03/2021 - 10:16: Common Eclipse configuration issue. If `could not find or load Pandora main class` error, simply clean the project.

# 2020

- 20/03/2020 - 19:09: New detail: maxAcceleration should consider negative values as well (e.g., max([-3.2, -0.1, 0.5, 2.9]) = -3.2)
- 20/03/2020 - 12:34: Updated [tests][tests] up to milestone 3, reference version of [pandora.jar] updated
- 20/03/2020 - 00:02: Added required values for the metadata section in [instructions](Constants.md#metadata)
- 19/03/2020 - 15:27: Added conversion values for Temperature and Pressure in [instructions](Constants.md#constant-values)
- 19/03/2020 - 15:27: Added conversion values for power (1 hp = `754.7` W) in [instructions](Constants.md#constant-values)
- 19/03/2020 - 15:00: add new [tests][tests] for milestone 1 and 2 to check your code
- 19/03/2020 - 15:00: updated pandora.jar in the release folder v1.5
- 18/03/2020 - 23:56: We added more information in case of [special situations](Constants.md#special-situations)
- 18/03/2020 - 20:06: Issue #99. We consider a stress pilot if her/his heart rate jumps more than ±10 bpm.
- 18/03/2020 - 18:06: Issue #100. If multiple phases required an oxygen concentration > 50%, list them in alphabetical order, and separate the names with coma.
- 18/03/2020 - 17:40: Issues #96 and #97. Discard the `average` part. Just report the altitude at which the max (wind speed for #96 and aircraft speed for #97) occurs.
- 18/03/2020 - 15:42: Flights should be around 4:00 am with your local time zone [timestamp](Constants.md#clues)
- 17/03/2020 - 17:25: We added some more information about [using timestamp](Constants.md#timestamps) in your program
- 17/03/2020 - 15:26: We added a simple heuristic to find flight phases [in the instructions](Constants.md#flight-phases) along with a pseudo-code in python
- 17/03/2020 - 12:18: If you want us to look to a specific problem in your code follow [this procedure ](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/commenting-on-a-pull-request#adding-line-comments-to-a-pull-request)
- 16/03/2020 - 10:46: Regarding the precision of printed numbers ([issue](https://github.com/Estia-advanced-programming/pandora-public/issues/29)), use `String.format("%.2f", variableName);` instead of `String.valueOf(variableName);` to add your resuls into the `featureValues` dictionary
- 16/03/2020 - 10:15: I have opened chat on [moodle]( https://moodle2a.estia.fr/mod/chat/view.php?id=11608 )  
- 13/03/2020 - 15:00: you can find more about tests files [here](Flight-Records) (US jet files, files with various errors, files with several jet engines, etc)

[tests]:https://github.com/Estia-advanced-programming/pandora-public/tree/master/testGenerator/autogradingGenerator/autograder/testsFiles
[pandora.jar]:https://github.com/Estia-advanced-programming/pandora-public/blob/master/release/pandora.jar
