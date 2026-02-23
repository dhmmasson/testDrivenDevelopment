# Code Coverage

Code coverage is a metric that measures how much of your source code is executed when your test suite runs. It helps identify untested paths and dead code.

## What Is Measured

Coverage tools instrument your bytecode and track which lines, branches, and methods are exercised during a test run. The most common metrics are:

| Metric | Description |
|---|---|
| **Line coverage** | Percentage of source lines executed at least once |
| **Branch coverage** | Percentage of decision branches taken (e.g., both sides of an `if`) |
| **Method coverage** | Percentage of methods called at least once |

For Pandora, aim for **high line and branch coverage** — every feature you implement should be reachable by your test suite.

## Why It Matters for Pandora

- **Grading**: your code is evaluated on test coverage. Dead code and untested paths lower your score.
- **Confidence**: high coverage reduces the risk of shipping a feature that only works in the happy path.
- **Discriminating other teams**: if your test suite cannot reach a code path, it cannot reveal whether another team's implementation is correct or not.

## Setting Up Coverage in VS Code (Maven + JaCoCo)

JaCoCo is the standard Java coverage tool. It is already configured in the Pandora starter pack.

### Run Coverage

```bash
mvn test jacoco:report
```

The HTML report is generated at:

```
target/site/jacoco/index.html
```

Open it in a browser to see line-by-line coverage for each class.

### Read the Report

- **Green** lines were executed by at least one test.
- **Yellow** lines were partially covered (some branches not taken).
- **Red** lines were never executed — write a test or remove the dead code.

## Setting Up Coverage in Eclipse

1. Right-click your project → **Coverage As** → **JUnit Test**
2. Eclipse highlights covered (green) and uncovered (red) lines directly in the editor.
3. The **Coverage** view at the bottom shows percentages per class and package.

> If the **Coverage As** option is missing, install **EclEmma**: Help → Eclipse Marketplace → search for *EclEmma*.

## Setting Up Coverage in IntelliJ / VS Code

- **IntelliJ IDEA**: Run → **Run with Coverage**. Coverage results are shown inline in the gutter.
- **VS Code**: use the [Coverage Gutters](https://marketplace.visualstudio.com/items?itemName=ryanluker.vscode-coverage-gutters) extension together with `mvn test jacoco:report`. Point the extension at `target/site/jacoco/jacoco.xml`.

## What to Do With the Report

1. **Delete dead code** — if a method or branch is never reached by any test and is not reachable by the program logic, remove it.
2. **Write missing tests** — for every red block that corresponds to real logic, write a test that exercises it.
3. **Check branches** — yellow coverage often means you only tested the `true` branch of a condition. Add a test for the `false` branch.

## Coverage Is Not a Goal in Itself

100% coverage does not mean your code is correct — it only means every line was executed at least once. A test that calls a method but asserts nothing will push coverage to 100% without providing any value.

Coverage is a **lower bound on test quality**, not an upper bound. Use it to find gaps, not to declare victory.

## See Also

- [Unit-Test](Unit-Test) — where to write your unit tests
- [Integration-Test](Integration-Test) — black-box tests that also contribute to coverage
- [Test-Driven-Development](../Test-Driven-Development) — the overall TDD workflow
