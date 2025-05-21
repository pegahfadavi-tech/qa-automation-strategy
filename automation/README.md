# Digikala Test Automation

This directory contains the automated test suite for Digikala website using Python, Selenium, Behave, and API testing tools.

## Directory Structure
```
automation/
├── features/              # Feature files (UI tests)
│   ├── login.feature     # Login scenarios
│   └── cart.feature      # Shopping cart scenarios
├── steps/                # Step implementations
│   ├── login_steps.py    # Login step implementations
│   └── cart_steps.py     # Cart step implementations
├── selectors/            # Page object selectors
│   └── digikala_selectors.py  # All Digikala selectors
├── api_tests/            # API test implementations
│   └── test_product_api.py
├── bug_reports/          # Real bug reports for Digikala
│   ├── bug_report_1.md
│   └── bug_report_2.md
├── environment.py        # Behave environment configuration
└── README.md            # This file
```

## Prerequisites
- Python 3.8 or higher
- Chrome browser
- Git

## Installation
1. Install dependencies:
```bash
pip install -r ../requirements.txt
```

## Running UI Tests
To run all UI tests:
```bash
behave
```

To run a specific feature:
```bash
behave features/login.feature
```

## Running API Tests
To run all API tests:
```bash
python -m pytest api_tests/
```

## Bug Reports
- Real bug reports for Digikala are documented in the `bug_reports/` directory.
- Each report includes: title, steps to reproduce, expected/actual results, severity, and environment.

## Test Structure
- Features are written in Gherkin syntax
- Step implementations use Selenium WebDriver
- Selectors are centralized in digikala_selectors.py
- API tests use requests, pytest, and jsonschema
- Environment.py handles test setup and teardown

## Notes
- Update test credentials in login_steps.py before running tests
- Update product URLs in cart_steps.py with real Digikala product URLs
- Selectors are based on Digikala's current website structure
- API endpoints and schemas should be verified with Digikala's actual API 