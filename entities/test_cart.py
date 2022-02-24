#!/usr/bin/env python
# -*- coding: utf-8 -*-
from entities.cart import Cart
from entities.item import Item


class TestCart:
    def test_cart__total_of_empty_cart_should_be_0_00(self):
        cart = Cart(0)
        assert cart.total == 0.00
        assert cart.num_items('Axe Deo') == 0

    def test_cart__ac0__total_for_single_item_should_be_that_items_value(self):
        item = Item('Dove Soap', 39.99)
        cart = Cart(0)
        cart.add(item, 1)
        assert cart.line_items == 1
        assert cart.num_items('Dove Soap') == 1
        assert cart.item_value('Dove Soap') == 39.99
        assert cart.total == 39.99

    def test_cart__ac1__total_for_multiple_items_should_be_that_items_value_multiplied_by_quantity(self):
        item = Item('Dove Soap', 39.99)
        cart = Cart(0)
        cart.add(item, 5)
        cart.add(item, 3)
        assert cart.line_items == 1
        assert cart.num_items('Dove Soap') == 8
        assert cart.item_value('Dove Soap') == 39.99
        assert cart.total == 319.92

    def test_cart__ac2__total_for_multiple_items_should_be_that_items_value_multiplied_by_quantity_plus_tax(self):
        soap = Item('Dove Soap', 39.99)
        deo = Item('Axe Deo', 99.99)
        cart = Cart(12.5)
        cart.add(soap, 2)
        cart.add(deo, 2)
        assert cart.line_items == 2
        assert cart.num_items('Dove Soap') == 2
        assert cart.item_value('Dove Soap') == 39.99
        assert cart.num_items('Axe Deo') == 2
        assert cart.item_value('Axe Deo') == 99.99
        assert cart.tax == 35.00
        assert cart.total == 314.96

    def test_cart__ac3__remove_soap_there_should_be_three_soaps_in_cart(self):
        soap = Item('Dove Soap', 39.99)
        deo = Item('Axe Deo', 99.99)
        cart = Cart(12.5)
        cart.add(soap, 4)
        cart.add(deo, 2)
        assert cart.line_items == 2
        assert cart.num_items('Dove Soap') == 4
        assert cart.item_value('Dove Soap') == 39.99
        assert cart.num_items('Axe Deo') == 2
        assert cart.item_value('Axe Deo') == 99.99
        cart.remove(soap, 1)
        assert cart.num_items('Dove Soap') == 3
        assert cart.tax == 39.99
        assert cart.total == 359.94

    def test_cart__ac3a__only_two_items_should_not_trigger_multi_discount(self):
        soap = Item('Dove Soap', 39.99, True)
        cart = Cart(12.5)
        cart.add(soap, 2)
        assert cart.line_items == 1
        assert cart.num_items('Dove Soap') == 2
        assert cart.item_value('Dove Soap') == 39.99
        assert cart.discount == 0.00
        assert cart.tax == 10.00
        assert cart.total == 89.98

    def test_cart__ac3b__three_items_should_trigger_multi_discount(self):
        soap = Item('Dove Soap', 39.99, True)
        deo = Item('Axe Deo', 99.99, False)
        cart = Cart(12.5)
        cart.add(soap, 3)
        cart.add(deo, 3)
        assert cart.line_items == 2
        assert cart.discount == 44.99
        assert cart.tax == 47.49
        assert cart.total == 427.44

    def test_cart__ac3c__six_multi_discount_items_should_triger_two_discounted_items(self):
        soap = Item('Dove Soap', 39.99, True)
        cart = Cart(12.5)
        cart.add(soap, 6)
        assert cart.line_items == 1
        assert cart.num_items('Dove Soap') == 6
        assert cart.item_value('Dove Soap') == 39.99
        assert cart.discount == 89.98
        assert cart.tax == 20.00
        assert cart.total == 179.95

    # prep
    # def test_cart__ac4a__total_price_discount_for_total_greater_than_1000_tax_inclusive_should_be_10_percent(self):
    #     deo = Item('Axe Deo', 99.99)
    #     cart = Cart(12.5)
    #     cart.add(deo, 10)
    #     assert cart.item_value('Axe Deo') == 99.99
    #     assert cart.tax == 124.99
    #     assert cart.discount == 1012.40
    #     assert cart.total == 1012.40  # 1124.89 - 112.49
    #
    # def test_cart__ac4a__total_price_discount_for_total_under_1000_tax_inclusive_should_be_zero(self):
    #     deo = Item('Axe Deo', 99.99)
    #     cart = Cart(12.5)
    #     cart.add(deo, 5)
    #     assert cart.item_value('Axe Deo') == 99.99
    #     assert cart.tax == 62.49
    #     assert cart.discount == 0.00
    #     assert cart.total == 562.44
    #
    # def test_cart__ac4b__total_price_discount_should_be_calculated_after_multi_buy(self):
    #     deo = Item('Axe Deo', 99.99)
    #     cart = Cart(12.5)
    #     cart.add(deo, 10)
    #     assert cart.item_value('Axe Deo') == 99.99
    #     assert cart.tax == 124.99
    #     assert cart.discount == 1012.40
    #     assert cart.total == 1012.40  # 1124.89 - 112.49
