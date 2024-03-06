# Release

Releasing is the _act_ of publishing a new [version](Semantic-Versioning) (major, minor, patch) publicly. In the context of the project, releasing a new version allows you to be graded by the automatic grade evaluation. While you could release each new feature as a minor and each bug fix as a patch, aim for quality rather than quantity. For example:

- release 1.7.0 could be the altitude release (feature maxAlt and avgAlt)
- release 1.12.0 the outside conditions (all the temperature, pressure and humidity functions)
- release 1.12.1 the outside conditions with the correction for the negative temperatures.

Each release you publish on github will be evaluated by the teacher testSuite. Each Evaluation will contribute to your final grade:

- a successful release will count positively
	- all the features declared in the manifest.json pass
	- minor version bump and at least one more feature in the manifest.json
- an unsuccessful release will count slightly negatively
	- One of the newly declared features failed
- A successful patch will offset an unsuccessful release
	- patch bump and fix the previous unsuccessful release
- a regression release will count negatively
	- already validated features are now broken

## Release Process

- Update in your code the version number so that ```java -jar pandora.jar --version``` outputs the correct version
- Update the manifest.json with the new version number and the implemented features
- Update the [Changelog](ProjectManagement/Changelog) file explaining what change you have introduced since the last version.
	- The features you have implemented
	- The bugs you have fixed  
- Commits the updated source code, manifest.json and Changelog under ```chore(release): release vX.Y.Z```
- **Tag the commit** vX.Y.Y
- Push the commit and the tag to Github
