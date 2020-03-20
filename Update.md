# Updates 
- 20/03/2020 - 19:09 : New detail: maxAcceleration should consider negative values as well (e.g., max([-3.2, -0.1, 0.5, 2.9]) = -3.2)
- **20/03/2020 - 12:34 : Updated [tests][tests] up to milestone 3, reference version of [pandora.jar] updated**
- 20/03/2020 - 00:02 : Added required values for the metadata section in [instructions](./Pandora-»-Instructions#metadata)
- 19/03/2020 - 15:27 : Added conversion values for Temperature and Pressure in [instructions](./Pandora-»-Instructions#constant-values)
- 19/03/2020 - 15:27 : Added conversion values for power (1 hp = `754.7` W) in [instructions](./Pandora-»-Instructions#constant-values)
- 19/03/2020 - 15:00 : add new [tests][tests] for milestone 1 and 2 to check your code
- 19/03/2020 - 15:00 : updated pandora.jar in the release folder v1.5
- 18/03/2020 - 23:56 : We added more information in case of [special situations](./Pandora-»-Instructions#special-situations)
- 18/03/2020 - 20:06 : Issue #99. We consider a stress pilot if her/his heart rate jumps more than ±10 bpm.
- 18/03/2020 - 18:06 : Issue #100. If multiple phases required an oxygen concentration > 50%, list them in alphabetical order, and separate the names with coma.
- 18/03/2020 - 17:40 : Issues #96 and #97. Discard the `average` part. Just report the altitude at which the max (wind speed for #96 and aircraft speed for #97) occurs.
- 18/03/2020 - 15:42 : Flights should be around 4:00 am with your local time zone [timestamp](./Pandora-»-Instructions#clues)
- 17/03/2020 - 17:25 : We added some more information about [using timestamp](./Pandora-»-Instructions#timestamps) in your program
- 17/03/2020 - 15:26 : We added a simple heuristic to find flight phases [in the instructions](./Pandora-»-Instructions#flight-phases) along with a pseudo-code in python
- 17/03/2020 - 12:18 : If you want us to look to a specific problem in your code follow [this procedure ](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/commenting-on-a-pull-request#adding-line-comments-to-a-pull-request)
- 16/03/2020 - 10:46 : Regarding the precision of printed numbers ([issue](https://github.com/Estia-advanced-programming/pandora-public/issues/29)), use `String.format("%.2f", variableName);` instead of `String.valueOf(variableName);` to add your resuls into the `featureValues` dictionary
- 16/03/2020 - 10:15 : I have opened chat on [moodle]( https://moodle2a.estia.fr/mod/chat/view.php?id=11608 )  
- 13/03/2020 - 15:00 : you can find more about tests files [here](./Pandora-»-Flight-Records) (US jet files, files with various erros, files with several jet engines, etc)

[tests]:https://github.com/Estia-advanced-programming/pandora-public/tree/master/testGenerator/autogradingGenerator/autograder/testsFiles
[pandora.jar]:https://github.com/Estia-advanced-programming/pandora-public/blob/master/release/pandora.jar