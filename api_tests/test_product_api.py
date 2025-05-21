import pytest
import requests
from typing import Dict, Any
from datetime import datetime

BASE_URL = "https://api.digikala.com/v2"
PRODUCT_ID = "13078758"

@pytest.fixture
def product_response():
    """Fixture to get product API response"""
    response = requests.get(f"{BASE_URL}/product/{PRODUCT_ID}/")
    return response

@pytest.fixture
def product_data(product_response):
    """Fixture to get product data from response"""
    return product_response.json()["data"]["product"]

def test_product_api_status_code(product_response):
    """Test that the product API returns 200 status code"""
    assert product_response.status_code == 200
    assert product_response.headers["content-type"] == "application/json"

def test_product_api_response_structure(product_response):
    """Test the basic structure of the product API response"""
    data = product_response.json()
    
    assert "status" in data
    assert data["status"] == 200
    assert "data" in data
    assert "product" in data["data"]
    assert isinstance(data["data"]["product"], dict)

def test_product_basic_info(product_data):
    """Test the basic product information fields"""
    assert product_data["id"] == 13078758
    assert "title_fa" in product_data
    assert "title_en" in product_data
    assert "status" in product_data
    assert product_data["status"] == "marketable"
    assert "url" in product_data
    assert "uri" in product_data["url"]
    assert isinstance(product_data["title_fa"], str)
    assert isinstance(product_data["title_en"], str)

def test_product_images(product_data):
    """Test the product images structure"""
    assert "images" in product_data
    assert "main" in product_data["images"]
    assert "list" in product_data["images"]
    
    main_image = product_data["images"]["main"]
    assert "url" in main_image
    assert "webp_url" in main_image
    assert isinstance(main_image["url"], list)
    assert isinstance(main_image["webp_url"], list)
    assert len(main_image["url"]) > 0
    assert len(main_image["webp_url"]) > 0
    
    image_list = product_data["images"]["list"]
    assert isinstance(image_list, list)
    if image_list:
        first_image = image_list[0]
        assert "url" in first_image
        assert "webp_url" in first_image
        assert isinstance(first_image["url"], list)
        assert isinstance(first_image["webp_url"], list)

def test_product_variants(product_data):
    """Test the product variants structure"""
    assert "variants" in product_data
    assert isinstance(product_data["variants"], list)
    
    if product_data["variants"]:
        variant = product_data["variants"][0]
        assert "id" in variant
        assert "price" in variant
        assert "status" in variant
        assert "color" in variant
        assert "seller" in variant
        assert "warranty" in variant
        assert "digiplus" in variant
        
        # Test color structure
        color = variant["color"]
        assert "id" in color
        assert "title" in color
        assert "hex_code" in color
        assert isinstance(color["hex_code"], str)
        assert color["hex_code"].startswith("#")

def test_product_price(product_data):
    """Test the product price structure"""
    assert "default_variant" in product_data
    assert "price" in product_data["default_variant"]
    price = product_data["default_variant"]["price"]
    
    assert "selling_price" in price
    assert "rrp_price" in price
    assert "order_limit" in price
    assert "is_incredible" in price
    assert "is_promotion" in price
    assert "discount_percent" in price
    
    assert isinstance(price["selling_price"], (int, float))
    assert isinstance(price["rrp_price"], (int, float))
    assert isinstance(price["order_limit"], int)
    assert isinstance(price["is_incredible"], bool)
    assert isinstance(price["is_promotion"], bool)
    assert isinstance(price["discount_percent"], (int, float))
    
    # Validate price logic
    assert price["selling_price"] >= 0
    assert price["rrp_price"] >= 0
    assert price["order_limit"] > 0
    assert 0 <= price["discount_percent"] <= 100

def test_product_seller_info(product_data):
    """Test the seller information structure"""
    assert "default_variant" in product_data
    assert "seller" in product_data["default_variant"]
    seller = product_data["default_variant"]["seller"]
    
    assert "id" in seller
    assert "title" in seller
    assert "code" in seller
    assert "url" in seller
    assert "rating" in seller
    assert "properties" in seller
    assert "stars" in seller
    assert "grade" in seller
    
    rating = seller["rating"]
    assert "total_rate" in rating
    assert "total_count" in rating
    assert "commitment" in rating
    assert "no_return" in rating
    assert "on_time_shipping" in rating
    
    assert isinstance(rating["total_rate"], (int, float))
    assert isinstance(rating["total_count"], int)
    assert 0 <= rating["total_rate"] <= 100
    assert rating["total_count"] >= 0

def test_product_specifications(product_data):
    """Test the product specifications structure"""
    assert "specifications" in product_data
    assert isinstance(product_data["specifications"], list)
    
    if product_data["specifications"]:
        spec = product_data["specifications"][0]
        assert "title" in spec
        assert "attributes" in spec
        assert isinstance(spec["attributes"], list)
        
        if spec["attributes"]:
            attr = spec["attributes"][0]
            assert "title" in attr
            assert "values" in attr
            assert isinstance(attr["values"], list)
            assert len(attr["values"]) > 0

def test_product_comments(product_data):
    """Test the product comments structure"""
    assert "comments_count" in product_data
    assert "last_comments" in product_data
    assert isinstance(product_data["last_comments"], list)
    
    if product_data["last_comments"]:
        comment = product_data["last_comments"][0]
        assert "id" in comment
        assert "body" in comment
        assert "rate" in comment
        assert "created_at" in comment
        assert "reactions" in comment
        assert "is_buyer" in comment
        assert "user_name" in comment
        
        reactions = comment["reactions"]
        assert "likes" in reactions
        assert "dislikes" in reactions
        assert isinstance(reactions["likes"], int)
        assert isinstance(reactions["dislikes"], int)
        
        # Validate rating
        assert 1 <= comment["rate"] <= 5

def test_product_questions(product_data):
    """Test the product questions structure"""
    assert "questions_count" in product_data
    assert "last_questions" in product_data
    assert isinstance(product_data["last_questions"], list)
    
    if product_data["last_questions"]:
        question = product_data["last_questions"][0]
        assert "id" in question
        assert "text" in question
        assert "status" in question
        assert "answer_count" in question
        assert "sender" in question
        assert "created_at" in question
        
        # Validate status
        assert question["status"] in ["accepted", "pending", "rejected"]
        assert isinstance(question["answer_count"], int)
        assert question["answer_count"] >= 0

def test_product_breadcrumb(product_data):
    """Test the product breadcrumb structure"""
    assert "breadcrumb" in product_data
    assert isinstance(product_data["breadcrumb"], list)
    
    if product_data["breadcrumb"]:
        for item in product_data["breadcrumb"]:
            assert "title" in item
            assert "url" in item
            assert "uri" in item["url"]
            assert isinstance(item["title"], str)
            assert isinstance(item["url"]["uri"], str)
            assert item["url"]["uri"].startswith("/") 