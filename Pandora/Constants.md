# Constants

Since we want to compare computed values between your program and ours for every tests, we need to set up some ground rules. You will need constants. We list here some constant values you might need.

**<ins style="color:red;">Important</ins>**: If you need another constant, let us know. Call us, or even better, use the git repository to [open an issue](https://github.com/Estia-advanced-programming/pandora-public/issues). We will then update this page so that everyone can use the same values.

## Number Precision

Make sure to use the `String.format("%.2f", variableName)` solution to display your results with a 0.01 precision.

<!-- * **Decimal**: Round your decimal values to 2 digits (e.g., `1234.5678` becomes `1234.57`) -->

## Constant Values

* Distances:

	* 1 m = `3.281` ft

* Weights:

	* 1 kg = `2.205` lbs

* Power:

	* 1 hp = `754.7` W

* Temperature:

	* 1 K = ℃ - `273.15`

* Pressure

	* 1 psi = `6894.76` Pa

* Speed:

	* 1 kts = `1.852` km/h

	* 1 mph = `1.609` km/h

	* `1225` km/h = 1 Mach

	* Classification:

		* Subsonic: Mach < 1.0

		* Transonic: Mach = 1.0

		* Supersomic: Mach > 1.0

		* Hypersonic: Mach > 5.0

	* 1 g = `9.80665` m/s2

* Earth radius: `6,371` km

## Computations

* Distance between 2 longitude/latitude coordinates: see this [link](http://www.movable-type.co.uk/scripts/latlong.html) (uses the `haversine` formula)

* Approximation for speed and acceleration data for the first point (respectively the first two points): `repeat` the first value

* ℃ to radian conversion: Use the Java built-in method `Math.toRadians(...)`

## Timestamp

You can convert double values to Instant Java objects.  
In this case, you can access quick display options (via `DateTimeFormatter`). For this, you need to define a zone. Use the `.withZone(ZoneId.systemDefault())`. (Check this [forum thread](https://stackoverflow.com/questions/25229124/format-instant-to-string) for more examples).

### Clue

All flights happened around 8:00am in a particular timezone. With your system timezone, these flights should be around 4:00am.

## Special Situations

* if a phase is not detected, report: `phase_name: not detected`

* if no phase has a O2 concentration > 50%, report `oxygenPhase: none`
