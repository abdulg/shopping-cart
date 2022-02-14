#!/usr/bin/env python
# -*- coding: utf-8 -*-
from decimal import *

from entities.line_item import LineItem


class Cart:
    def __init__(self, tax_rate):
        self._tax_rate = int(tax_rate * 100)
        self._line_items = {}

    @property
    def total(self):
        total = sum([line_item.total_in_cents for line_item in self._line_items.values()])
        tax = self.tax
        return float(Decimal(total/100.0 + tax).quantize(Decimal('0.01')))

    @property
    def line_items(self):
        return len(self._line_items)

    @property
    def tax(self):
        subtotal = sum([line_item.total_in_cents for line_item in self._line_items.values()])
        str_tax = str(subtotal*self._tax_rate)
        tax = '{}.{}'.format(str_tax[:-6], str_tax[-6:])
        return float(Decimal(tax).quantize(Decimal('0.01')))

    def add(self, item, quantity):
        line_item = self._line_items.setdefault(item.name, LineItem(item, 0))
        line_item.add(quantity)
