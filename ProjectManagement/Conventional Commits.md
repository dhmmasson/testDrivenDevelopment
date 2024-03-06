# Conventional Commits

Conventional Commits represent a standardized convention for writing version control commit messages, providing a structured and semantic approach to tracking changes in a software project. Adopting a clear and consistent commit message format aids in automated release notes generation, versioning, and facilitates better communication within development teams. The convention defines a set of conventional keywords like "feat" for new features, "fix" for bug fixes, and "chore" for routine tasks, enabling developers to convey the nature of changes concisely.

## Structure

The commit message should be structured as follows:

```
<type>[optional scope]: <description>

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

# See Also

https://www.conventionalcommits.org/en/v1.0.0/
