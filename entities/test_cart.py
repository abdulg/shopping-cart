#!/usr/bin/env python
# -*- coding: utf-8 -*-
from entities.cart import Cart
from entities.item import Item


class TestCart:
    def test_cart__total_of_empty_cart_should_be_0_00(self):
        cart = Cart()
        assert cart.total == 0.00

    def test_cart__ac0__total_for_single_item_should_be_that_items_value(self):
        item = Item('Dove Soap', 39.99)
        cart= Cart()
        cart.add(item, 1)
        assert cart.line_items == 1
        assert cart.total == 39.99
