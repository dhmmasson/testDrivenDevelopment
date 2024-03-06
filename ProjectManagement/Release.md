# Release

Releasing is the _act_ of publishing a new [version](Semantic-Versioning) (major, minor, patch) publicly. In the context of the project, releasing a new version allows you to be graded by the automatic grade evaluation. While you could release each new feature as a minor and each bug fix as a patch, aim for quality rather than quantity. For example, release 1.7.0 could be the altitude release (feature maxAlt and avgAlt), release 1.12.0 the outside conditions (all the temperature, pressure and humidity functions)

## Release process

- Update in your code the version number so that ```java -jar pandora.jar --version``` output the correct version
- Update the [Changelog](Changelog) file explaining what change you have introduced since the last version.
	- The features you have implemented
	- The bug you have 
Every time you fully introduce one or more features you should release a new minor version. 