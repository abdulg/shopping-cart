#!/usr/bin/env python
# -*- coding: utf-8 -*-
from entities.cart import Cart


class TestCart:
    def test_total_of_empty_cart_should_be_0_00(self):
        cart = Cart()
        assert cart.total == 0.00
