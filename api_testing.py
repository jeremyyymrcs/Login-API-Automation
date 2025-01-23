import pytest
import requests
import logging

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger()

BASE_URL = "https://jsonplaceholder.typicode.com/users"


# Test case for a valid user ID
@pytest.mark.run(order=1)
def test_valid_user_id():
    user_id = "1"
    logger.info(f"Testing with valid user ID: {user_id}")
    response = requests.get(f"{BASE_URL}/{user_id}")

    # Log and print response status code
    logger.debug(f"Response status code: {response.status_code}")
    print(f"Status Code for valid user ID: {response.status_code}")

    assert response.status_code == 200

    user_data = response.json()
    logger.debug(f"User data: {user_data}")

    # Validate user data
    assert user_data['id'] == 1
    assert user_data['name'] == "Leanne Graham"
    assert user_data['email'] == "Sincere@april.biz"

    # Output the user data
    print(f"Valid user ID test passed for user ID: {user_id}")
    print(f"User Name: {user_data['name']}")
    print(f"User Email: {user_data['email']}")


# Test case for an invalid user ID
@pytest.mark.run(order=2)
def test_invalid_user_id():
    user_id = "9999"
    logger.info(f"Testing with invalid user ID: {user_id}")
    response = requests.get(f"{BASE_URL}/{user_id}")

    # Log and print response status code
    logger.debug(f"Response status code: {response.status_code}")
    print(f"Status Code for invalid user ID: {response.status_code}")

    assert response.status_code == 404

    print(f"Invalid user ID test passed for user ID: {user_id}")


# Test case for an empty user ID
@pytest.mark.run(order=3)
def test_empty_user_id():
    user_id = " "
    logger.info(f"Testing with empty user ID: {user_id}")
    response = requests.get(f"{BASE_URL}/{user_id}")

    # Log and print response status code
    logger.debug(f"Response status code: {response.status_code}")
    print(f"Status Code for empty user ID: {response.status_code}")

    assert response.status_code == 404

    print(f"Empty user ID test passed for user ID: {user_id}")


# Test case for special characters in user ID
@pytest.mark.run(order=4)
def test_special_characters_in_user_id():
    user_id = "@!#$$%"
    logger.info(f"Testing with special characters in user ID: {user_id}")
    response = requests.get(f"{BASE_URL}/{user_id}")

    # Log and print response status code
    logger.debug(f"Response status code: {response.status_code}")
    print(f"Status Code for special characters in user ID: {response.status_code}")

    assert response.status_code == 404

    print(f"Special characters test passed for user ID: {user_id}")


# Test case for a non-integer user ID
@pytest.mark.run(order=5)
def test_non_integer_user_id():
    user_id = "abc"
    logger.info(f"Testing with non-integer user ID: {user_id}")
    response = requests.get(f"{BASE_URL}/{user_id}")

    # Log and print response status code
    logger.debug(f"Response status code: {response.status_code}")
    print(f"Status Code for non-integer user ID: {response.status_code}")

    assert response.status_code == 404

    print(f"Non-integer user ID test passed for user ID: {user_id}")
