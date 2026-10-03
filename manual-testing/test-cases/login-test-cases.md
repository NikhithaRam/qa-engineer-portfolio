# Login Test Cases

## TC_LOGIN_001 — Login with Valid Credentials

**Test Type:** Functional Testing  
**Priority:** High

### Preconditions
- User has a registered account.
- Application is accessible.
- User is on the Login screen.

### Test Steps
1. Enter a valid username/email.
2. Enter a valid password.
3. Click the Login button.

### Expected Result
User should be successfully authenticated and redirected to the Home screen.

---

## TC_LOGIN_002 — Login with Invalid Password

**Test Type:** Negative Testing  
**Priority:** High

### Preconditions
- User has a registered account.
- User is on the Login screen.

### Test Steps
1. Enter a valid username/email.
2. Enter an incorrect password.
3. Click the Login button.

### Expected Result
The application should display an appropriate error message and should not authenticate the user.

---

## TC_LOGIN_003 — Login with Empty Credentials

**Test Type:** Negative Testing  
**Priority:** Medium

### Test Steps
1. Leave the username/email field empty.
2. Leave the password field empty.
3. Click the Login button.

### Expected Result
The application should display appropriate validation messages for the required fields.

---

## TC_LOGIN_004 — Password Masking

**Test Type:** UI / Functional Testing  
**Priority:** Medium

### Test Steps
1. Navigate to the Login screen.
2. Enter a password in the password field.

### Expected Result
The password should be masked and should not be displayed as plain text.
