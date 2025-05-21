# Digikala Test Automation

This directory contains the automated test suite for Digikala website using Python, Selenium, and Behave framework.

## Directory Structure
```
automation/
├── features/              # Feature files
│   ├── login.feature     # Login scenarios
│   └── cart.feature      # Shopping cart scenarios
├── steps/                # Step implementations
│   ├── login_steps.py    # Login step implementations
│   └── cart_steps.py     # Cart step implementations
├── selectors/            # Page object selectors
│   └── digikala_selectors.py  # All Digikala selectors
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
pip install -r requirements.txt
```

## Running Tests
To run all tests:
```bash
behave
```

To run specific feature:
```bash
behave features/login.feature
```

## Test Structure
- Features are written in Gherkin syntax
- Step implementations use Selenium WebDriver
- Selectors are centralized in digikala_selectors.py
- Environment.py handles test setup and teardown

## Notes
- Update test credentials in login_steps.py before running tests
- Update product URLs in cart_steps.py with real Digikala product URLs
- Selectors are based on Digikala's current website structure 