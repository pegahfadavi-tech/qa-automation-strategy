# Bug Report: Login Page Error Message Not Displayed

## Bug Description
When attempting to log in with invalid credentials, the error message is not displayed to the user, making it unclear why the login failed.

## Severity
High - Affects user authentication flow

## Steps to Reproduce
1. Navigate to the login page
2. Enter a valid email address
3. Enter an invalid password
4. Click the login button

## Expected Result
- An error message should be displayed indicating that the credentials are invalid
- The error message should be clearly visible below the login form

## Actual Result
- No error message is displayed
- User is left on the login page without any feedback
- Console shows 401 Unauthorized response

## Environment
- Browser: Chrome 120.0.6099.130
- OS: macOS Sonoma 14.2
- Device: Desktop

## Screenshots
[Attach relevant screenshots here]

## Additional Notes
- This issue affects both the main login page and the popup login form
- The API returns the correct error response, but the frontend is not handling it properly 