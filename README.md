# QA Automation Strategy for Online Store

This project implements automated testing strategy for an online store (inspired by Digikala) using Python, Selenium, and Behave framework.

## 📎 Downloadable Test Artifacts
- [Manual Test Cases (Excel)](automation/docs/Test_Cases_Manual.xlsx)
- [Sample API Test Output](automation/api_tests/outputs/api_test_output.txt)
- [Edge Case Feature File](automation/features/edge_cases.feature)
- [Edge Case Step Implementation](automation/steps/edge_cases_steps.py)

## Project Structure
```
qa-automation-strategy/
├── automation/
│   ├── api_tests/                # API test implementations
│   │   ├── outputs/              # API test outputs
│   │   └── test_product_api.py
│   ├── bug_reports/              # Bug reports documentation
│   │   ├── bug_report_1.md
│   │   └── bug_report_2.md
│   ├── docs/                     # Manual test cases (Excel)
│   │   └── Test_Cases_Manual.xlsx
│   ├── features/                 # Feature files (UI tests)
│   │   ├── login.feature
│   │   ├── cart.feature
│   │   └── edge_cases.feature
│   ├── steps/                    # Step implementations
│   │   ├── login_steps.py
│   │   ├── cart_steps.py
│   │   └── edge_cases_steps.py
│   ├── selectors/                # Page object selectors
│   │   └── digikala_selectors.py
│   └── environment.py            # Behave environment configuration
├── docs/
│   ├── Test_Cases_Manual.md      # Manual test cases (Markdown)
│   └── Test_Cases_Gherkin.md     # Gherkin test cases
├── README.md
└── requirements.txt
```

## Prerequisites
- Python 3.8 or higher
- Chrome browser
- Git

## Installation
1. Clone the repository:
```bash
git clone https://github.com/pegahfadavi-tech/qa-automation-strategy.git
cd qa-automation-strategy
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running Tests

### UI Tests
To run all UI tests:
```bash
cd automation
behave
```

To run a specific feature:
```bash
behave features/login.feature
```

### API Tests
To run API tests:
```bash
cd automation
python -m pytest api_tests/
```

## Test Cases
- Manual test cases are documented in `docs/Test_Cases_Manual.md` and `automation/docs/Test_Cases_Manual.xlsx`
- Gherkin test cases are in `docs/Test_Cases_Gherkin.md` and as `.feature` files in `automation/features/`

## Bug Reports
Bug reports are documented in the `automation/bug_reports/` directory with detailed information about:
- Bug title
- Steps to reproduce
- Expected vs actual results
- Severity level

## Contributing
1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request
