  
Semantic versioning, often abbreviated as SemVer, is a versioning scheme designed to bring clarity and consistency to software version numbers. It provides a systematic way of conveying changes and updates in a software project through a three-part version number, consisting of \<Major\>.\<Minor\>.\<Patch> components (e.g., 1.2.3). 

The key principle behind semantic versioning is to communicate the nature of changes succinctly: a change in the major version indicates incompatible API alterations, a minor version signals backward-compatible feature additions, and a patch version denotes backward-compatible bug fixes. 

 **Major Version (X.0.0):**   
 - Increased when incompatible API changes are introduced.
- Signifies that existing code relying on your CLI may break. (e.g. you change the option ```-o``` to ```-f```)
You should not have a major version update in the project unless the teachers decide to change something in the API of Pandora.

**Minor Version (X.Y.0):**
- Existing functionality remains intact, but new features are introduced. (e.g. you implement the feature -o minHumidity)
- Incremented for backward-compatible additions of features or enhancements. (e.g. you handle American fighters in addition to Russian ones)

Every time you fully introduce one or more feature you should release a new minor version. Update the [Changelog](Changelog) file explaining what change you have introduced since 

**Patch Version (X.Y.Z):**
- Raised for backward-compatible bug fixes. 
- Indicates that the code remains compatible, but specific issues have been addressed.

# See also

Learn everything about [semver](https://semver.org/)