# QA Automation Strategy for Online Store

This project implements automated testing strategy for an online store (inspired by Digikala) using Python, Selenium, and Behave framework.

## Project Structure
```
qa-automation-strategy/
├── docs/
│   ├── Test_Cases_Manual.md    # Manual test cases
│   └── Test_Cases_Gherkin.md   # Gherkin test cases
├── features/
│   ├── login.feature           # Login scenarios
│   ├── cart.feature            # Shopping cart scenarios
│   ├── steps/
│   │   ├── login_steps.py      # Login step implementations
│   │   └── cart_steps.py       # Cart step implementations
│   └── environment.py          # Behave environment configuration
├── api_tests/                  # API test implementations
├── bug_reports/               # Bug reports documentation
└── requirements.txt           # Project dependencies
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
behave
```

To run specific feature:
```bash
behave features/login.feature
```

### API Tests
To run API tests:
```bash
python -m pytest api_tests/
```

## Test Cases
- Manual test cases are documented in `docs/Test_Cases_Manual.md`
- Gherkin test cases are in `docs/Test_Cases_Gherkin.md`

## Bug Reports
Bug reports are documented in the `bug_reports/` directory with detailed information about:
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
