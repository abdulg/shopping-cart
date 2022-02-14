#!/usr/bin/env python
# -*- coding: utf-8 -*-
from entities.line_item import LineItem


class TestLineItem:
    def test_line_item__total_with_no_items_should_be_0_00(self):
        line_item = LineItem()
        assert line_item.total == 0.00
