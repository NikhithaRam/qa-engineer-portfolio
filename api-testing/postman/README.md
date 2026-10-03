# Postman API Testing

This section demonstrates API testing using Postman, including request creation, response validation, positive and negative testing.

## Postman Testing Activities

- Creating API requests
- Managing request parameters
- Validating HTTP status codes
- Validating response bodies
- Validating JSON fields
- Validating response headers
- Authentication validation
- Positive and negative testing
- Test data validation
- Collection-based execution
- Regression testing

## HTTP Methods

| Method | Purpose |
|--------|---------|
| GET | Retrieve data |
| POST | Create data |
| PUT | Update existing data |
| PATCH | Partially update data |
| DELETE | Delete data |

## Sample Postman Validation

For each API request, I validate:

### Request

- HTTP method
- Endpoint
- Query parameters
- Path parameters
- Headers
- Request body
- Authentication

### Response

- HTTP status code
- Response time
- Response body
- JSON structure
- Required fields
- Data types
- Error messages

## Positive Testing

Examples:

- Valid request parameters
- Valid authentication
- Valid resource IDs
- Expected request payload

## Negative Testing

Examples:

- Missing mandatory parameters
- Invalid parameters
- Invalid authentication
- Invalid resource IDs
- Empty request body
- Unsupported values

## Collection Execution

API requests can be organized into Postman collections for:

- Smoke testing
- Regression testing
- Functional testing
- End-to-end API validation
