import pytest
from cart import ShoppingCart

def test_add_item_and_total_without_discount():
    cart = ShoppingCart()     
    cart.add_item('Apple', 2.50, 2)    
    cart.add_item('Banana', 1.25, 4)     
    assert cart.get_total() == 10.0


def test_add_same_item_twice_accumulates_quantity_instead_of_overwriting():
    cart = ShoppingCart()     
    cart.add_item('Apple', 2.00, 2)     
    cart.add_item('Apple', 2.00, 3)     
    assert cart.get_item_count() == 5     
    assert cart.get_total() == 10.0

def test_add_item_with_zero_quantity_raises_value_error():
    cart = ShoppingCart()
    with pytest.raises(ValueError):
        cart.add_item('Apple', 2.00, 0)

def test_add_item_with_negative_quantity_raises_value_error():
    cart = ShoppingCart()     
    with pytest.raises(ValueError):         
        cart.add_item('Apple', 2.00, -1)


def test_add_item_with_negative_price_raises_value_error():
    cart = ShoppingCart()     
    with pytest.raises(ValueError):         
        cart.add_item('Apple', -2.00, 1)

def test_remove_existing_item_updates_total():
    cart = ShoppingCart()     
    cart.add_item('Apple', 3.00, 2)     
    cart.remove_item('Apple')     
    assert cart.get_total() == 0.0     
    assert cart.get_item_count() == 0
def test_remove_missing_item_raises_key_error():
    cart = ShoppingCart()     
    with pytest.raises(KeyError):         
        cart.remove_item('Ghost')

def test_apply_valid_percent_discount_reduces_total():
    cart = ShoppingCart()     
    cart.add_item('Book', 20.00, 1)     
    cart.apply_discount('SAVE10')     
    assert cart.get_total() == 18.0
def test_apply_fixed_discount_reduces_total_at_exact_threshold():
    cart = ShoppingCart()
    cart.add_item('Game', 15.00, 2)   # subtotal exactly 30     cart.apply_discount('FLAT5')     assert cart.get_total() == 25.0
def test_apply_discount_fails_below_minimum_threshold():     
    cart = ShoppingCart()
    cart.add_item('Game', 10.00, 2)   # subtotal 20 < 30     with pytest.raises(ValueError):         cart.apply_discount('FLAT5')

def test_discount_boundary_exactly_at_threshold_is_allowed_for_save20():
    cart = ShoppingCart()
    cart.add_item('Shoes', 25.00, 2)  # subtotal exactly 50     cart.apply_discount('SAVE20')     assert cart.get_total() == 40.0
def test_invalid_discount_code_raises_value_error():
    cart = ShoppingCart()     
    cart.add_item('Book', 10.00, 1)     
    with pytest.raises(ValueError):         
        cart.apply_discount('NOTREAL')

def test_clear_empties_cart_and_resets_discount_state():
    cart = ShoppingCart()     
    cart.add_item('Shoes', 30.00, 2)    
    cart.apply_discount('SAVE20')     
    cart.clear()
    assert cart.get_total() == 0.0     
    assert cart.get_item_count() == 0

def test_get_item_count_returns_sum_of_quantities():
    cart = ShoppingCart()     
    cart.add_item('Apple', 1.00, 2)     
    cart.add_item('Orange', 1.50, 3)     
    assert cart.get_item_count() == 5


