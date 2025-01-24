# User ID Validation Tests

This project contains a set of automated tests for validating user IDs against the JSONPlaceholder API. These tests
check different scenarios of user ID inputs, including valid, invalid, empty, special characters, and non-integer user
IDs.

## Test Cases

The following test cases are included:

### 1. Valid User ID Test

This test checks the response for a valid user ID. It verifies that the user data is returned correctly and matches the
expected values.

- **Test User ID:** `1`
- **Expected Status Code:** `200 OK`
- **Expected Name:** `Leanne Graham`
- **Expected Email:** `Sincere@april.biz`

**Test Procedure:**

- Send a GET request to `https://jsonplaceholder.typicode.com/users/1`.
- Validate that the response status code is `200 OK`.
- Assert that the returned user name and email match the expected values.

---

### 2. Invalid User ID Test

This test checks the response for a non-existent user ID.

- **Test User ID:** `9999`
- **Expected Status Code:** `404 Not Found`

**Test Procedure:**

- Send a GET request to `https://jsonplaceholder.typicode.com/users/9999`.
- Validate that the response status code is `404 Not Found`.

---

### 3. Empty User ID Test

This test checks the response when the user ID is empty.

- **Test User ID:** `" "`
- **Expected Status Code:** `404 Not Found`

**Test Procedure:**

- Send a GET request to `https://jsonplaceholder.typicode.com/users/` (empty space).
- Validate that the response status code is `404 Not Found`.

---

### 4. Special Characters in User ID Test

This test checks the response when the user ID contains special characters.

- **Test User ID:** `@!#$$%`
- **Expected Status Code:** `404 Not Found`

**Test Procedure:**

- Send a GET request to `https://jsonplaceholder.typicode.com/users/@!#$$%`.
- Validate that the response status code is `404 Not Found`.

---

### 5. Non-integer User ID Test

This test checks the response when the user ID is a non-integer string.

- **Test User ID:** `abc`
- **Expected Status Code:** `404 Not Found`

**Test Procedure:**

- Send a GET request to `https://jsonplaceholder.typicode.com/users/abc`.
- Validate that the response status code is `404 Not Found`.

---

## Tech Stack / Tools Used

The following technologies and tools were used to develop and run the tests:

- **Programming Language:** Python
- **Testing Framework:** Pytest
- **API Testing:** Requests
- **Logging:** Python logging module
- **API:** JSONPlaceholder (for testing user ID validation)

## Running the API Tests

Once you’ve installed the dependencies, you can run the automated tests with Pytest:

```bash
cd ..
pytest api_testing.py -s -v
