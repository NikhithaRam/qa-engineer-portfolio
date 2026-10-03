# API Test Cases

This document contains sample test cases for validating REST APIs using Postman.

---

## TC_API_001 — Validate Successful GET Request

**Test Type:** Functional Testing  
**Priority:** High

### Test Steps

1. Send a GET request to a valid API endpoint.
2. Observe the HTTP response.
3. Validate the response body.

### Expected Result

- API should return the expected HTTP status code.
- Response body should contain the expected data.
- Response should follow the expected JSON structure.

---

## TC_API_002 — Validate POST Request

**Test Type:** Functional Testing  
**Priority:** High

### Test Steps

1. Prepare a valid POST request.
2. Provide all mandatory request parameters.
3. Send the request.
4. Validate the response.

### Expected Result

The API should successfully process the request and return the expected response.

---

## TC_API_003 — Validate Invalid Request

**Test Type:** Negative Testing  
**Priority:** High

### Test Steps

1. Send a request with invalid or incorrect input data.
2. Observe the response.

### Expected Result

The API should reject the invalid request and return an appropriate HTTP status code and error response.

---

## TC_API_004 — Validate Missing Mandatory Parameter

**Test Type:** Negative Testing  
**Priority:** High

### Test Steps

1. Prepare a request without a required parameter.
2. Send the request.
3. Validate the response.

### Expected Result

The API should reject the request and return an appropriate validation error.

---

## TC_API_005 — Validate Invalid Authentication

**Test Type:** Security / Negative Testing  
**Priority:** High

### Test Steps

1. Prepare a request requiring authentication.
2. Provide an invalid or expired authentication token.
3. Send the request.

### Expected Result

The API should reject the request and return the appropriate authentication or authorization error.

---

## TC_API_006 — Validate Response Headers

**Test Type:** API Validation  
**Priority:** Medium

### Test Steps

1. Send a valid API request.
2. Inspect the response headers.
3. Validate the required headers.

### Expected Result

The response should contain the expected headers and appropriate values.

---

## TC_API_007 — Validate Response Schema

**Test Type:** API Validation  
**Priority:** Medium

### Test Steps

1. Send a valid API request.
2. Inspect the JSON response.
3. Verify required fields and data types.

### Expected Result

The response should follow the expected schema, including required fields and correct data types.

---

## TC_API_008 — Validate Invalid Resource ID

**Test Type:** Negative Testing  
**Priority:** Medium

### Test Steps

1. Send a request using an invalid or non-existing resource ID.
2. Observe the response.

### Expected Result

The API should return an appropriate error response indicating that the requested resource could not be found or processed.

---

## API Validation Checklist

| Validation | Status |
|------------|--------|
| HTTP Status Code | ☐ |
| Response Body | ☐ |
| JSON Structure | ☐ |
| Response Headers | ☐ |
| Authentication | ☐ |
| Mandatory Parameters | ☐ |
| Negative Scenarios | ☐ |
| Error Handling | ☐ |
