#!/usr/bin/env python
# -*- coding: utf-8 -*-
from entities.item import Item
from entities.line_item import LineItem


class TestLineItem:
    def test_line_item__total_with_no_items_should_be_0_00(self):
        line_item = LineItem()
        assert line_item.total == 0.00

    def test_line_item__quantity_with_no_items_should_be_zero(self):
        line_item = LineItem()
        assert line_item.quantity == 0

    def test_line_item__add_a_single_item_should_total_value_of_that_item(self):
        line_item = LineItem()
        item = Item('Dove Soap', 39.99)
        line_item.add(item)
        assert line_item.quantity == 1
        assert line_item.total == item.value

