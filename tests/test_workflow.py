# Automated Tests

This directory contains automated tests for the Pyragogy co-authoring workflow.

## Files

* `test_workflow.py` – Main test suite for the n8n workflow
* `test_report.json` – Automatically generated test report

## Running the Tests

### Prerequisites

1. Python 3.7+ installed
2. n8n running at `http://localhost:5678`
3. `pyragogy_master_workflow.json` imported and active in n8n

### Install Dependencies

```bash
pip install requests
```

### Execution

```bash
# Test with default configuration (localhost:5678)
python test_workflow.py

# Test with custom URL
python test_workflow.py http://your-n8n-instance:5678
```

## Types of Tests

### 1. Connectivity Test

* Checks that n8n is reachable
* Verifies the health status of the service

### 2. Webhook Endpoint Test

* Verifies that the `/webhook/pyragogy/process` endpoint responds
* Tests reception of JSON payloads

### 3. Payload Validation Test

* **Full Payload**: All fields present
* **Minimum Payload**: Only essential fields
* **Empty Payload**: Should fail
* **Incomplete Payload**: Missing fields

### 4. Agent Orchestration Test

* **Simple Input**: Tests basic orchestration
* **Complex Input**: Tests advanced orchestration with multiple agents

### 5. Error Handling Test

* Malformed JSON
* Incorrect Content-Type
* Invalid payloads

## Test Output

Tests produce colored output in the console:

* ✅ **PASS**: Test passed
* ❌ **FAIL**: Test failed

### JSON Report

A `test_report.json` file is generated with:

```json
{
  "total_tests": 10,
  "passed_tests": 8,
  "failed_tests": 2,
  "success_rate": 80.0,
  "results": [...]
}
```

## CI/CD Integration

Tests are integrated with GitHub Actions (see `.github/workflows/test.yml`):

* Automatically run on push/PR
* Sets up PostgreSQL and Redis for testing
* Launches n8n in headless mode
* Automatically imports the workflow
* Uploads results as artifacts

## Example Test Payloads

### Full Payload

```json
{
  "title": "Full Test",
  "input": "Complete test content",
  "tags": ["test", "validation"],
  "phase": "draft",
  "rhythm": "on-demand",
  "requireHitl": false
}
```

### Minimum Payload

```json
{
  "title": "Minimum Test",
  "input": "Minimum content"
}
```

## Troubleshooting

### n8n Not Reachable

* Verify that n8n is running
* Check the URL and port
* Ensure no firewall is blocking the connection

### Workflow Not Found

* Ensure the workflow is imported in n8n
* Verify the workflow is active
* Check the webhook endpoint configuration

### Failed Tests

* Check n8n logs for errors
* Verify credentials (OpenAI, PostgreSQL, etc.)
* Ensure all dependent services are running

## Extending the Tests

To add new tests:

1. Add a new `test_*` method to the `PyragogyWorkflowTester` class
2. Call the method from `run_all_tests()`
3. Use `self.log_test()` to log results

Example:

```python
def test_custom_feature(self) -> bool:
    """Tests a custom feature"""
    try:
        # Your test code here
        result = some_test_operation()
        self.log_test("Custom Feature", True, "Test passed")
        return True
    except Exception as e:
        self.log_test("Custom Feature", False, f"Error: {str(e)}")
        return False
```

## Python Script: `test_workflow.py`

This script automates testing of the Pyragogy n8n co-authoring workflow, including integration and payload validation.

```python
#!/usr/bin/env python3
"""
Test Suite for the Pyragogy n8n Co-Authoring Workflow

This script provides automated tests to verify the functioning
of the n8n workflow, including integration and payload validation.
"""

# (The rest of the script remains unchanged; see uploaded code)
```

You can include the full script inline or reference the file in your repository for execution and documentation purposes.
