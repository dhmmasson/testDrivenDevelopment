# Command Line Interface (CLI)

## Definition

A Command Line Interface (CLI) is a text-based interface that allows users to interact with a computer by typing commands. Unlike Graphical User Interfaces (GUI), which rely on visual elements, a CLI requires users to enter text commands to perform tasks. This enables the use of the CLI in scripts for system administration, programming, and software development.

Each line of a command line can be decomposed in several parts
```
Prompt Command Parameters1 ... ParametersN
```

- The prompt is given by the shell or terminal you are using, for example in the terminal in vscode it is something like this: 
	```bash
username:path$
	```

- The command is the program you are executing, for example to compile the project we use maven whose command is ```mvn```, to launch a java program we use ```java``` .
- The parameters or arguments are values that are transmitted to the program to parametrize its execution. The parameters depend on the command used (e.g. the parameter for ```mvn``` are not the same as the parameter for the ```java``` command). Parameters can either be options or arguments.  
	-  Options modify the behavior of a command. They are preceded by a hyphen (-) and can be single-letter or full words. Some options take a parameters.
	- Arguments are the inputs provided to a command. They can be filenames, directories, or other data needed for the command to operate on.

Example to compile and execute the pandora project from the command line: 
```bash
$ mvn -B --file pom.xml package
```

the first line call the program ```mvn``` which is the CLI for maven ([Maven](https://maven.apache.org/what-is-maven.html) is a software project management tool by Apache that manage a project's build, reporting and documentation from a single project object model (POM)). We gave to ```mvn``` two options ```-B``` (batch) and ```--file pom.xml``` and one argument ```package```. 

the [man](https://linuxcommandlibrary.com/man/mvn) for the ```mvn``` command explain what each of this options does, it also tell us that the last argument is the ```goal``` (here: package - **Compile and package the compiled code in its distributable format, such as a jar**)

Example to call your pandora program: 
```bash
$ java -jar target/pandora.jar
$ java -jar target/pandora.jar --version
```
the java command launches a java program, the -jar instruct the command that the main class is in the given .jar file (here target/pandora.jar) all the remaining arguments are given to the target java program (--version is an argument to your pandora program and not to the java command)

to make it clearer we can use an alias to rename ```java -jar target/pandora.jar``` to ```pandora```

```bash
$ alias pandora='java -jar target/pandora.jar'
$ pandora --version
```

## Options in CLI

Options in the command line are flags or switches that modify the behavior of a command. They can be categorized into short options (single-character) and long options (multi-character). Options can sometimes take parameters to provide additional information to the command.

### Short Options

Short options consist of a single character preceded by a hyphen (-). They are often used for quick, one-character modifications.

Example:
```bash
$ ls -l
```

In this example, the `-l` option is used with the `ls` command to display detailed information about files and directories.

short options that don't take a parameters can be combined 

Example:
```bash
$ ls -al
$ ls -a -l
```

### Long Options

Long options are more descriptive and consist of multiple characters preceded by two hyphens (--). They provide a clearer understanding of their purpose.

Example:
```bash
$ git commit --message "Fix bug in feature X"
```

Here, the `--message` option is used with the `git commit` command to include a specific commit message.

### Options with Parameters

Some options require additional parameters to provide more specific information. These parameters are specified immediately after the option.

Example:
```bash
$ curl -o output.txt https://example.com/file.txt
```

In this command, the `-o` option is used to specify the output file (`output.txt`) for the data retrieved by the `curl` command.

for pandora 

## Arguments in CLI

Arguments in the command line are inputs provided to a command to perform a specific operation. They follow the command and options.

Example:
```bash
$ cp file1.txt directory/
```

In this example, `file1.txt` and `directory/` are arguments for the `cp` (copy) command. The command copies `file1.txt` to the specified directory.

for pandora the arguments are either the [Flight-Records](Flight-Records) to parse or one folder that contain the [Flight-Records](Flight-Records)

```bash
$ pandora test/resources/0_201_MiG-23MLD.frd
$ pandora test/resources/0_201_MiG-23MLD.frd test/resources/0_301_Su-25T.frd
$ pandora test/resources
```