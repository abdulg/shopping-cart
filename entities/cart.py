#!/usr/bin/env python
# -*- coding: utf-8 -*-
from decimal import *

from entities.line_item import LineItem


class Cart:
    def __init__(self, tax_rate):
        self._tax_rate = Decimal(str(tax_rate))
        self._line_items = {}

    @property
    def total(self):
        total = sum([line_item.total_in_decimal for line_item in self._line_items.values()])
        tax = self._tax_in_decimal
        return float(Decimal(total + tax).quantize(Decimal('0.01')))

    @property
    def line_items(self):
        return len(self._line_items)

    def num_items(self, name):
        if name in self._line_items:
            return self._line_items[name].quantity
        return 0

    def item_value(self, name):
        if name in self._line_items:
            return self._line_items[name].value
        return None

    @property
    def tax(self):
        return float(self._tax_in_decimal.quantize(Decimal('1.00')))

    @property
    def discount(self):
        discount = sum([line_item.discount_in_decimal for line_item in self._line_items.values()])
        return float(discount.quantize(Decimal('0.01')))

    @property
    def _tax_in_decimal(self):
        subtotal = sum([line_item.total_in_decimal for line_item in self._line_items.values()])
        return subtotal * self._tax_rate / Decimal('100.0')

    def add(self, item, quantity):
        line_item = self._line_items.setdefault(item.name, LineItem(item, 0))
        line_item.add(quantity)

    def remove(self, item, quantity):
        if item.name in self._line_items:
            line_item = self._line_items[item.name]
            line_item.remove(quantity)
