from inventory_report.product import Product


def test_create_product() -> None:
    product_data = {
        "id": "1",
        "product_name": "Test Product",
        "company_name": "Test Company",
        "manufacturing_date": "2023-07-17",
        "expiration_date": "2023-12-31",
        "serial_number": "1793ZTM",
        "storage_instructions": "Lorem ipsum dolor sit amet.",
    }
    product = Product(**product_data)
    assert product.id == product_data["id"]
    assert product.product_name == product_data["product_name"]
    assert product.company_name == product_data["company_name"]
    assert product.manufacturing_date == product_data["manufacturing_date"]
    assert product.expiration_date == product_data["expiration_date"]
    assert product.serial_number == product_data["serial_number"]
    assert product.storage_instructions == product_data["storage_instructions"]


def test_product_report() -> None:
    product_data = {
        "id": "1",
        "product_name": "Test Product",
        "company_name": "Test Company",
        "manufacturing_date": "2023-07-17",
        "expiration_date": "2023-12-31",
        "serial_number": "1793ZTM",
        "storage_instructions": "Lorem ipsum dolor sit amet",
    }
    product = Product(**product_data)

    expected_report = (
        f"The product {product_data['id']} - {product_data['product_name']} "
        f"with serial number {product_data['serial_number']} manufactured on "
        f"{product_data['manufacturing_date']} by the company "
        f"{product_data['company_name']} valid until "
        f"{product_data['expiration_date']} must be stored according to "
        f"the following instructions: {product_data['storage_instructions']}."
    )

    product_str = str(product)

    assert product_str == expected_report
