# Fake Store API Test Suite

This test suite validates the data provided by the Fake Store API (https://fakestoreapi.com/products).

## Test Objectives

1. Verify server response code (expected 200)
2. Confirm the presence and validity of the following attributes for each product:
   - `title` (must not be empty)
   - `price` (must not be negative)
   - `rating.rate` (must not exceed 5)
3. Generate a list of products containing defects

## Setup

1. Install Python 3.7 or higher
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Tests

To run the tests with a detailed report:
```bash
pytest test_fakestore_api.py -v
```

To generate an HTML report:
```bash
pytest test_fakestore_api.py --html=report.html
```

## Test Cases

1. `test_server_response`: Verifies that the API endpoint returns a 200 status code
2. `test_product_titles`: Checks if all products have non-empty titles
3. `test_product_prices`: Validates that all product prices are non-negative
4. `test_product_ratings`: Ensures all product ratings are within the valid range (0-5)
5. `test_generate_defect_report`: Generates a comprehensive report of all products with defects 