#!/usr/bin/env python
# -*- coding: utf-8 -*-
from decimal import *

from entities.line_item import LineItem


class Cart:
    def __init__(self):
        self._line_items = {}

    @property
    def total(self):
        total = sum([line_item.total for line_item in self._line_items.values()])
        return float(Decimal(total).quantize(Decimal('0.01')))

    @property
    def line_items(self):
        return len(self._line_items)

    def add(self, item, quantity):
        line_item = self._line_items.setdefault(item.name, LineItem(item, 0))
        line_item.add(quantity)
