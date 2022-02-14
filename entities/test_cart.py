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
        cart= Cart(0)
        cart.add(item, 1)
        assert cart.line_items == 1
        assert cart.num_items('Dove Soap') == 1
        assert cart.item_value('Dove Soap') == 39.99
        assert cart.total == 39.99

    def test_cart__ac1__total_for_multiple_items_should_be_that_items_value_multiplied_by_quantity(self):
        item = Item('Dove Soap', 39.99)
        cart= Cart(0)
        cart.add(item, 5)
        cart.add(item, 3)
        assert cart.line_items == 1
        assert cart.num_items('Dove Soap') == 8
        assert cart.item_value('Dove Soap') == 39.99
        assert cart.total == 319.92

    def test_cart__ac2__total_for_multiple_items_should_be_that_items_value_multiplied_by_quantity_plus_tax(self):
        soap = Item('Dove Soap', 39.99)
        deo = Item('Axe Deo', 99.99)
        cart= Cart(12.5)
        cart.add(soap, 2)
        cart.add(deo, 2)
        assert cart.line_items == 2
        assert cart.num_items('Dove Soap') == 2
        assert cart.item_value('Dove Soap') == 39.99
        assert cart.num_items('Axe Deo') == 2
        assert cart.item_value('Axe Deo') == 99.99
        assert cart.tax == 35.00
        assert cart.total == 314.96

