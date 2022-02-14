#!/usr/bin/env python
# -*- coding: utf-8 -*-
from decimal import *


class LineItem:
    def __init__(self):
        self._item = None
        self._quantity = 0

    @property
    def total(self):
        if self._item is None:
            return Decimal('0.00')
        return float((Decimal(self._quantity) * Decimal(self._item.value)).quantize(Decimal('0.01')))

    @property
    def quantity(self):
        return self._quantity

    def add(self, item):
        self._item = item
        self._quantity += 1