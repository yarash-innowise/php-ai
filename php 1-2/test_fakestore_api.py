import requests
import pytest

API_URL = "https://fakestoreapi.com/products"

def get_products():
    """Fetch products from the API"""
    response = requests.get(API_URL)
    return response

class TestFakeStoreAPI:
    @pytest.fixture(scope="class")
    def api_response(self):
        """Fixture to get API response once for all tests"""
        response = get_products()
        return response

    @pytest.fixture(scope="class")
    def products_data(self, api_response):
        """Fixture to get products data once for all tests"""
        return api_response.json()

    def test_server_response(self, api_response):
        """Test if server responds with status code 200"""
        assert api_response.status_code == 200, f"Expected status code 200, but got {api_response.status_code}"

    def test_product_titles(self, products_data):
        """Test if all products have non-empty titles"""
        products_with_empty_titles = [
            product for product in products_data
            if not product.get('title') or not isinstance(product.get('title'), str)
        ]
        
        assert len(products_with_empty_titles) == 0, (
            f"Found {len(products_with_empty_titles)} products with empty or invalid titles: "
            f"{[product.get('id') for product in products_with_empty_titles]}"
        )

    def test_product_prices(self, products_data):
        """Test if all products have valid prices (non-negative)"""
        products_with_invalid_prices = [
            product for product in products_data
            if not isinstance(product.get('price'), (int, float)) or product.get('price') < 0
        ]
        
        assert len(products_with_invalid_prices) == 0, (
            f"Found {len(products_with_invalid_prices)} products with invalid prices: "
            f"{[(product.get('id'), product.get('price')) for product in products_with_invalid_prices]}"
        )

    def test_product_ratings(self, products_data):
        """Test if all product ratings are within valid range (0-5)"""
        products_with_invalid_ratings = [
            product for product in products_data
            if not isinstance(product.get('rating', {}).get('rate'), (int, float)) or 
            product.get('rating', {}).get('rate') < 0 or 
            product.get('rating', {}).get('rate') > 5
        ]
        
        assert len(products_with_invalid_ratings) == 0, (
            f"Found {len(products_with_invalid_ratings)} products with invalid ratings: "
            f"{[(product.get('id'), product.get('rating', {}).get('rate')) for product in products_with_invalid_ratings]}"
        )

    def test_generate_defect_report(self, products_data):
        """Generate a report of all products with defects"""
        defective_products = []
        
        for product in products_data:
            defects = []
            
            # Check title
            if not product.get('title') or not isinstance(product.get('title'), str):
                defects.append("Empty or invalid title")
            
            # Check price
            if not isinstance(product.get('price'), (int, float)) or product.get('price') < 0:
                defects.append(f"Invalid price: {product.get('price')}")
            
            # Check rating
            rating = product.get('rating', {}).get('rate')
            if not isinstance(rating, (int, float)) or rating < 0 or rating > 5:
                defects.append(f"Invalid rating: {rating}")
            
            if defects:
                defective_products.append({
                    'id': product.get('id'),
                    'defects': defects
                })
        
        # This test will always pass, but prints the defect report
        if defective_products:
            print("\nDefect Report:")
            print("-------------")
            for product in defective_products:
                print(f"Product ID: {product['id']}")
                print(f"Defects: {', '.join(product['defects'])}")
                print("-------------")
        
        assert True  # This test always passes as it's for reporting purposes 