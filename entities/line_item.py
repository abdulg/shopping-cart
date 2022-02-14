#!/usr/bin/env python
# -*- coding: utf-8 -*-
from decimal import *


class LineItem:
    def __init__(self, item, quantity):
        self._item = item
        self._quantity = quantity

    @property
    def total(self):
        return float(self._quantity * self._item.value_in_cents / 100.0)

    @property
    def total_in_cents(self):
        return self._quantity * self._item.value_in_cents

    @property
    def quantity(self):
        return self._quantity

    def add(self, quantity):
        self._quantity += quantity
