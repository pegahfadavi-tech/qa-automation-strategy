import pytest
import requests
from jsonschema import validate

# API endpoint
BASE_URL = "https://api.digikala.com/v2"

# JSON Schema for product search response
product_search_schema = {
    "type": "object",
    "properties": {
        "status": {"type": "integer"},
        "data": {
            "type": "object",
            "properties": {
                "products": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "id": {"type": "integer"},
                            "title": {"type": "string"},
                            "price": {
                                "type": "object",
                                "properties": {
                                    "rrp_price": {"type": "integer"},
                                    "selling_price": {"type": "integer"}
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}

def test_product_search():
    """Test product search API endpoint"""
    # Test data
    search_query = "laptop"
    
    # Make API request
    response = requests.get(f"{BASE_URL}/search/?q={search_query}")
    
    # Assert response status code
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    # Parse response
    data = response.json()
    
    # Validate response schema
    validate(instance=data, schema=product_search_schema)
    
    # Assert response contains products
    assert len(data["data"]["products"]) > 0, "No products found in response"
    
    # Assert product data structure
    product = data["data"]["products"][0]
    assert "id" in product, "Product ID missing"
    assert "title" in product, "Product title missing"
    assert "price" in product, "Product price missing" 