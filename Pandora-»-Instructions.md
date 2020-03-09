# Instructions

Since we want to compare computed values between your program and ours for every tests, we need to set up some ground rules. You will need constants. We list here some constant values you might need. 

**<ins style="color:red;">Important</ins>**: If you need another constant, let us know. Call us, or even better, use the git repository to [open an issue](https://github.com/Estia-advanced-programming/pandora-public/issues). We will then update this page so that everyone can use the same values.


<!-- * **Decimal**: Round your decimal values to 2 digits (e.g., `1234.5678` becomes `1234.57`) -->

## Constant Values

* Distances:
	* 1 m = `3.281` ft

* Weights:
	* 1 kg = `2.205` lbs

* Speed:
	* 1 kts = `1.852` km/h
	* 1 mph = `1.609` km/h

* Earth radius: `6,371` km

## Computations

* Distance between 2 longitude/latitude coordinates: see this [link](http://www.movable-type.co.uk/scripts/latlong.html) (uses the `haversine` formula)

* Approximation for speed and acceleration data for the first point (respectively the first two points): `repeat` the first value

* ℃ to radian conversion: Use the Java built-in method `Math.toRadians(...)`



