While git is a _version_ control system, and each commit is a new version of your software, these versions are too granular to be meaningful for end-users of your software. In particular because the commit number or hash is seemingly random it is difficult to know if commit ```abc34ef``` is more recent than commit ```32ff76a``` [^hash] and if an update is required. To address this, versioning schemes propose assigning meaningful numbers to incremental software versions.

Semantic versioning, often abbreviated as [semver](https://semver.org/), is one of the possible versioning schemes for a project. It provides a systematic way of conveying changes and updates in a software project through a three-part version number, consisting of \<Major\>.\<Minor\>.\<Patch> components (e.g., 1.2.3).

The key principle behind semantic versioning is to communicate the nature of changes succinctly: a change in the major version indicates incompatible API alterations, a minor version signals backward-compatible feature additions, and a patch version denotes backward-compatible bug fixes.

 - **Major Version (X.0.0):** Increased when incompatible API changes are introduced, meaning that [tests](Test-Driven-Development) that previously passed should now be red. It signifies that existing code relying on your CLI may break. (e.g. you change the option ```-o``` to ```-f```) A breaking change also means that the [test suite](Test-Driven-Development) should rewritten.  
   You should not have a major version update in the project unless the teachers decide to change something in the API of Pandora.
- **Minor Version (1.Y.0):** Increased when new features are introduced. (e.g. you implement the feature -o minHumidity) or for backward-compatible improvement. (e.g. you handle American fighters in addition to Russian ones). A minor version is the result of several [Commits](Conventional%20Commits) at least one of them should be a ```feat: implemented feature X``` but there should be some ```test: add some tests for feature X```, ```refactor: create a class to handle Y``` and ```docs: add the documentation for the method C::X```
- **Patch Version (1.0.Z):** Raised for backward-compatible bug fixes. It indicates that the code remains compatible, but specific issues have been addressed. (e.g. you have discovered that you have a bug in the [Feature](Features) ```avgTemp``` when the temperature are negative and you fix it.

# See also

Learn everything about [semver](https://semver.org/)

[^hash]: in reality a commit hash is 40 character long: ca82a6dff817ec66f44342007202690a93763949
