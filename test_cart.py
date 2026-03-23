import pytest

@pytest.fixture
def cart():
    return []

@pytest.mark.smoke
def test_cart_is_empty_initially(cart):
    assert len(cart) == 0

@pytest.mark.regression
def test_add_item_to_cart(cart):
    cart.append("Laptop")
    assert "Laptop" in cart

@pytest.mark.skip
def test_payment():
    assert True