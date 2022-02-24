#!/usr/bin/env python
# -*- coding: utf-8 -*-
from decimal import *


class LineItem:
    def __init__(self, item, quantity):
        self._item = item
        self._quantity = int(quantity)

    @property
    def total(self):
        return float(self._quantity * self._item.value_in_decimal)

    @property
    def total_in_decimal(self):
        return self._quantity * self._item.value_in_decimal

    @property
    def quantity(self):
        return self._quantity

    @property
    def value(self):
        return self._item.value

    def add(self, quantity):
        self._quantity += quantity
