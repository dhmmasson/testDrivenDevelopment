# Vscode

Vscode can run maven goals from the interface, you can also use the terminal to run maven commands as explained in the [maven documentation](maven.md). You can also use the maven extension for vscode to run maven goals from the interface. You can also install the Java Extension Pack for better Java support in vscode. You can also add the coverage extension to vscode to be able to see the code coverage report directly in vscode with [Coverage Gutters](https://marketplace.visualstudio.com/items?itemName=ryanluker.vscode-coverage-gutters) for example.

# Extensions
 Install the extensions from the Extensions tab in vscode (Ctrl + Shift + X) and search for the following extensions:
- **Maven for Java**: to run maven goals from the interface
- **Extension Pack for Java**: for better Java support in vscode
- **Coverage Gutters**: to see the code coverage report directly in vscode
# Build

* ```ctrl + shift + p``` >type: maven execute command > package
* ```ctrl + shift + B``` Build

# Tests

* ```ctrl + shift + p``` >type: maven execute command > verify

This will run the `verify` maven goal which will run the tests from the autograder python script []. You can also run the `test` goal to only run the tests without packaging the project.

* if python is not found, try changing "python3" to "python" in the pom.xml file

# Coverage

* ```ctrl + shift + p``` >type: maven execute command > custom > type `jacoco:report`

## Favorite

Create a favorite in the maven extension for the `verify` goal to run the tests and generate the coverage report in one click. You can also create a favorite for the `package` goal to build the project in one click.

* ```ctrl + shift + p``` >type: maven extension > Favorites > Add Favorite > type `clean verify jacoco:report` for the goals

run it with 

* ```ctrl + shift + p``` >type: maven execute command > favorites > select your favorite
