#!/usr/bin/env python
# -*- coding: utf-8 -*-
from decimal import *


class LineItem:
    def __init__(self, item, quantity):
        self._item = item
        self._quantity = quantity

    @property
    def total(self):
        return float((Decimal(self._quantity) * Decimal(self._item.value)).quantize(Decimal('0.01')))

    @property
    def quantity(self):
        return self._quantity

    def add(self, item):
        self._quantity += 1