# TestSuite & Autograder

The autograder is a Python script provided in the starter pack that runs a test suite against any `pandora.jar`. It is the primary tool used by both students and the teacher team to evaluate implementations.

## The Autograder

```bash
python test/autograder.py \
  -t <path_test_suite> \
  -m <path_manifest> \
  -f <json|md> \
  -o <output_path> \
  -j <jacoco_agent_path> \
  <pathToPandora>
```

### Arguments

| Argument | Required | Description |
|---|---|---|
| `<pathToPandora>` | yes | Path to the jar to test (e.g. `target/pandora.jar`) |
| `-t <path_test_suite>` | yes | Path to `testSuite.json` |
| `-m <path_manifest>` | yes | Path to `manifest.json` |
| `-f <json\|md>` | no | Output format: `json` (machine-readable) or `md` (Markdown report). Defaults to terminal output |
| `-o <output_path>` | no | Write results to this file instead of stdout |
| `-j <jacoco_agent_path>` | no | Path to the JaCoCo agent jar — enables [code coverage](Code-Coverage.md) measurement during the run |

### Typical Usage

Run your test suite against your own jar:

```bash
python test/autograder.py -t test/testSuite.json -m manifest.json target/pandora.jar
```

Run your test suite against another team's jar:

```bash
python test/autograder.py -t test/testSuite.json -m path/to/their/manifest.json path/to/their/pandora.jar
```

Save a Markdown report:

```bash
python test/autograder.py -t test/testSuite.json -m manifest.json -f md -o results.md target/pandora.jar
```

Run with code coverage:

```bash
python test/autograder.py -t test/testSuite.json -m manifest.json -j ~/.m2/repository/org/jacoco/org.jacoco.agent/0.8.11/org.jacoco.agent-0.8.11-runtime.jar target/pandora.jar
```

The script prints a summary grouped by milestone. A passing test is shown in green; a failing test shows the expected vs. actual diff.

---

## Building Your TestSuite

**You are required to produce Black Box Integration Tests for every feature you implement** by filling `test/testSuite.json` and placing the corresponding flight record files in `test/resources/`.

### File Format

`test/testSuite.json` is a JSON array of test descriptions:

```json
[
  {
    "id": 1,
    "feature": "maxAlt",
    "milestone": 1,
    "mode": "feature",
    "file": "test/resources/0_201_MiG-23MLD.frd",
    "result": "14321.00"
  },
  {
    "id": 2,
    "feature": "fullReport",
    "milestone": 1,
    "mode": "full",
    "file": "test/resources/0_201_MiG-23MLD.frd",
    "result": "14321.00"
  }
]
```

### Fields

| Field | Type | Description |
|---|---|---|
| `id` | number | Unique integer within the suite |
| `feature` | string | Exact value passed to `-o` (e.g. `maxAlt`, `flightDuration`) — must match the [Features](../../Pandora/Features.md) table |
| `milestone` | number | Milestone number, used for grouping output |
| `mode` | `"feature"` \| `"full"` | `feature`: run with `-o <feature>`; `full`: generate the full report and parse it for the expected value |
| `file` | string | Path to the flight record, **relative to the project root** (e.g. `test/resources/my_flight.frd`) |
| `result` | string | Expected output — the autograder does a **strict string comparison** |

> Follow the [output format rules](../../Pandora/Constants.md) precisely — decimal separator, number of digits, and units must all match exactly.

### What Makes a Good TestSuite

- **At least one test per feature and per CLI option** you have implemented
- **Feature mode tests**: use a hand-crafted flight record where the correct answer is easy to verify by hand (e.g., 10 records all at 1000 m → `avgAlt` must be `1000.00`)
- **Varied inputs**: different aircraft, different flight profiles, edge cases (short flight, single record, missing optional columns)
- **Discriminating tests**: your suite should catch bugs in other teams' implementations — if a team doesn't handle negative temperatures, your suite should fail them

Place hand-crafted flight records in `test/resources/` alongside the provided files. See [Integration-Test](Integration-Test.md) for guidance on designing test records.

## See Also

- [Integration-Test](Integration-Test.md) — concept and design of integration tests
- [Code-Coverage](Code-Coverage.md) — measuring coverage during autograder runs
- [manifest.json](../manifest.json.md) — declares which features are implemented
- [Features](../../Pandora/Features.md) — list of all feature names and their CLI options
