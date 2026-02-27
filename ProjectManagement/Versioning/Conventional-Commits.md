# Conventional Commits

Conventional Commits represent a standardized convention for writing version control commit messages, providing a structured and semantic approach to tracking changes in a software project. Adopting a clear and consistent commit message format aids in automated release notes generation, versioning, and facilitates better communication within development teams. The convention defines a set of conventional keywords like "feat" for new features, "fix" for bug fixes, and "chore" for routine tasks, enabling developers to convey the nature of changes concisely.

## Structure

The commit message should be structured as follows:

```
<type>[optional scope]: <description that start with a verb in the present tense>

[optional body]

[optional footer(s)]
```

### Type

- **feat**: A new feature
- **fix**: A bug fix
- **docs**: Documentation only changes
- **style**: Changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons, etc)
- **refactor**: A code change that neither fixes a bug nor adds a feature
- perf: A code change that improves performance
- **test**: Adding missing tests or correcting existing tests
- **chore**: Other changes that don't modify src or test files (e.g. chore(release): release v1.0.1)  

less useful for you in the pandora project

- build: Changes that affect the build system or external dependencies (change to maven. **You should not do that**)
- ci: Changes to our CI configuration files and scripts (change in the.github repository. **You should not do that**)
- revert: Reverts a previous commit


### Short Description

The description is a short summary of the commit. It should be concise and to the point, ideally no more than 50 characters. It should start with a verb in the present tense (e.g. "add", "fix", "update", "remove", etc) and should not end with a period.

```fix: remove the version that is not used anymore in the pom.xml```
```

### Scope

The scope is optional and can be anything specifying the place of the commit change. For example, if you are fixing a bug in the parser you can write:

```fix(parser): correct the parsing of the option -o
```

```feat(records): add the feature to count the number of records in a flight record
```


### Footer

The footer is the place to reference any issues that this commit closes or affects. For example:

```
fix: correct minor typos in code
See the issue for details:
Closes #123
```
this commit message indicates that the commit fixes a bug and that the issue #123 is now closed. If you push that commit to github, the issue #123 will be automatically closed by github when merged onto the main branch.

# See Also

https://www.conventionalcommits.org/en/v1.0.0/
