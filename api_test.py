import requests

url = 'https://bc-staging.itdev.app/api/external/stepper/v1/completed-order'

headers = {
    'Content-Type': 'application/json',
    'User-Agent': 'insomnia/10.3.0',
    'x-client-id': '1737bfd6166866cbacf7625245b80332ef690511c23dd8824285510dccae3a71',
    'x-client-secret': '672b057ebd8155176a8a08d88e70f60232b8fbb7af58544e1544055c138682f1',
}

cookies = {
    'paraglide_lang': 'en'
}

payload = {
    "orderId": "000F78B2-2B17-459E-AC31-0B757E898772",
    "companyName": "Tech Solutions Ltd",
    "emailAddress": "contact@techsolutions.com",
    "sicCode": "62020",
    "supplierId": "SUP123456",
    "supplierName": "Supplier Corp",
    "siteId": "SITE98765",
    "primary": {
        "title": "Mr",
        "firstName": "John",
        "middleName": "Regala",
        "lastName": "Smith",
        "mobileNumber": "+447700900123",
        "mobileNumberCountry": "United Kingdom",
        "mobileNumberCode": "+44",
        "dateOfBirth": "1985-05-15",
        "countryOfResidence": 826,
        "nationalityCountry": 826,
        "townOfBirth": "London",
        "personalAddress": {
            "line1": "123 Tech Street",
            "line2": "Suite 5B",
            "city": "London",
            "postCode": "EC1A 1BB",
            "country": "United Kingdom"
        },
        "isPsc": True,
        "isShareholder": True,
        "sharesAllocated": 95
    },
    "additionalDirectors": [
        {
            "title": "Ms",
            "firstName": "Jane",
            "middleName": "Marie",
            "lastName": "Smith",
            "mobileNumber": None,
            "mobileNumberCountry": None,
            "mobileNumberCode": None,
            "dateOfBirth": "1990-09-10",
            "countryOfResidence": 840,
            "nationalityCountry": 840,
            "townOfBirth": "Manchester",
            "personalAddress": None,
            "isPsc": True,
            "isShareholder": False,
            "sharesAllocated": 25
        }
    ],
    "companyAddress": {
        "line1": "456 Corporate Avenue",
        "line2": None,
        "city": "Manchester",
        "postCode": "M1 4BT",
        "country": "United Kingdom"
    },
    "productPriceIds": [1001, 1002, 1003]
}

response = requests.post(url, headers=headers, cookies=cookies, json=payload)

# Print the response (status code and body)
print(f"Status Code: {response.status_code}")
print(f"Response Body: {response.text}")
