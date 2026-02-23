# Vscode

# Extensions

You should install:

* [Maven](https://maven.apache.org/download.cgi). Unzip it somewhere safe. Then enter the path of the `mvn.cmd` file in vscode settings (under Maven path)

# Build

* ```ctrl + shift + p``` >type: maven execute command > package

* ```ctrl + shift + B``` Build

# Tests

* ```ctrl + shift + p``` >type: maven execute command > test  
If the test does not work, check the error messages

* if python is not found, try changing "python3" to "python" in the pom.xml file
