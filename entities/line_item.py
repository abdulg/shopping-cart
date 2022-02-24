#!/usr/bin/env python
# -*- coding: utf-8 -*-
from decimal import *


class LineItem:
    def __init__(self, item, quantity):
        self._item = item
        self._quantity = int(quantity)
        self._multi_discount = item.multi_discount
        self._discount = Decimal('0.00')

    @property
    def total(self):
        return float((self._quantity - self._num_discounted_items) * self._item.value_in_decimal)

    @property
    def total_in_decimal(self):
        return (self._quantity - self._num_discounted_items) * self._item.value_in_decimal

    @property
    def discount(self):
        return float(self._num_discounted_items * self._item.value_in_decimal)

    @property
    def discount_in_decimal(self):
        return self._num_discounted_items * self._item.value_in_decimal

    @property
    def quantity(self):
        return self._quantity

    @property
    def value(self):
        return self._item.value

    @property
    def _num_discounted_items(self):
        if self._multi_discount is True:
            return self._quantity // 3
        return 0

    def add(self, quantity):
        self._quantity += quantity

    def remove(self, quantity):
        if quantity > self._quantity:
            self._quantity = 0
        else:
            self._quantity -= quantity
