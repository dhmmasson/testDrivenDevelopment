# Integration Test

An integration test validates the behaviour of `pandora.jar` as a whole, from the outside — exactly as the teacher's grading system does. Rather than testing an internal method in isolation, you run the compiled program against a flight record file and compare its output to an expected value.

This is the **primary testing strategy** for Pandora.

## Concept: Black Box Testing

You treat `pandora.jar` as a black box:

```
flight_record.frd  ──▶  java -jar pandora.jar -o <feature> file.frd  ──▶  "1234.56"
                                                                               │
                                                                          compare to
                                                                        expected value
```

You do not know or care how the value is computed internally. You only check that the output matches the specification. This mirrors exactly what the teacher autograder does, so passing your own test suite is a strong signal that you will pass the teacher's.

## Test Flight Records

You can use two kinds of input files:

| Kind | When to use |
|---|---|
| **Existing records** from `test/resources/` | Quick sanity checks on real data |
| **Hand-crafted records** | Precise control — design a file where the correct answer is obvious (e.g., 10 records at altitude 100 m → `avgAlt` must be `100.00`) |

Hand-crafted files are strongly recommended for edge cases: empty files, single-record flights, zero engine power, extreme values, files with optional columns missing, etc. Place them in `test/resources/` alongside the existing files.

## The `testSuite.json` Format

All integration tests must be described in `test/testSuite.json`. The file is a JSON array of test descriptions:

```json
[
  {
    "id": 1,
    "feature": "avgAlt",
    "milestone": 1,
    "mode": "feature",
    "file": "test/resources/0_201_MiG-23MLD.frd",
    "result": "1234.56"
  },
  {
    "id": 2,
    "feature": "maxAlt",
    "milestone": 1,
    "mode": "feature",
    "file": "test/resources/0_201_MiG-23MLD.frd",
    "result": "14321.00"
  }
]
```

### Fields

| Field | Type | Description |
|---|---|---|
| `id` | number | Unique identifier within the suite |
| `feature` | string | The exact value passed to `-o` (e.g. `avgAlt`, `flightDuration`) |
| `milestone` | number | Milestone number — used for grouping output |
| `mode` | `"feature"` \| `"full"` | `feature`: run with `-o <feature>`; `full`: parse the full report |
| `file` | string | Path to the flight record, relative to the project root |
| `result` | string \| number | Expected output, must match exactly |

> The autograder does a **strict string comparison** between the program output and `result`. Follow the [output format](../../Pandora/Constants) precisely (decimal separator, number of digits, units).

### One Test Per Feature Minimum

You must have at least one test for **every feature and CLI option** you claim to have implemented. The feature name in `testSuite.json` must match the `-o` option name from the [Features](../../Pandora/Features) table exactly.

## Running Your Test Suite

A Python script is provided in the starter pack to run the suite against any `pandora.jar`:

```bash
python test/autograder.py -t test/testSuite.json -m manifest.json target/pandora.jar
```

| Argument | Description |
|---|---|
| `-t` | Path to `testSuite.json` |
| `-m` | Path to `manifest.json` |
| last argument | Path to the jar to test |

The script prints a summary of passed and failed tests grouped by milestone. A green line means your output matched exactly; a red line shows the expected vs. actual diff.

## Running Against Another Group's Project

Because the format is standardised, you can run **your** test suite against **another team's** jar:

```bash
python test/autograder.py -t test/testSuite.json -m manifest.json path/to/other/pandora.jar
```

This is how your test suite contributes to the grade: it must agree with the teacher's results. If team B passes feature `avgAlt` according to the teacher, your suite should also pass it. If team B fails `maxAlt`, your suite should catch that failure too.

A good test suite:
- Has varied inputs (different files, different flight profiles)
- Tests boundary conditions (minimum values, maximum values, empty phases)
- Has at least one hand-crafted file per feature where the expected answer is trivially verifiable by hand

## Workflow in TDD

Integration tests slot into the Red–Green–Refactor cycle at the **Red** step:

1. **Red** — write a `testSuite.json` entry for the feature; run the autograder → it fails (feature not implemented yet)
2. **Green** — implement the feature; run the autograder → it passes
3. **Refactor** — clean up the code; run the autograder again to confirm nothing regressed

## See Also

- [Unit-Test](Unit-Test) — for testing individual methods in isolation
- [Code-Coverage](Code-Coverage) — measuring how much of your code is exercised
- [Test-Driven-Development](../Test-Driven-Development) — the overall TDD workflow
- [manifest.json](../manifest.json) — declares which features are implemented
- [Constants](../../Pandora/Constants) — output format rules the autograder enforces
