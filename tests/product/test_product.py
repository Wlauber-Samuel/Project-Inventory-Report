from inventory_report.product import Product


def test_create_product() -> None:
    # Arrange
    product_data = {
        "id": "1",
        "product_name": "Test Product",
        "company_name": "Test Company",
        "manufacturing_date": "2023-07-17",
        "expiration_date": "2023-12-31",
        "serial_number": "1793ZTM",
        "storage_instructions": "Lorem ipsum dolor sit amet.",
    }

    # Act
    product = Product(**product_data)

    # Assert
    for key, value in product_data.items():
        assert getattr(product, key) == value
