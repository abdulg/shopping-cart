#!/usr/bin/env python
# -*- coding: utf-8 -*-
from decimal import *


class Item:
    def __init__(self, name, value, multi_discount=False):
        self._name = name
        self._value = Decimal(str(value))
        self._multi_discount = multi_discount

    @property
    def name(self):
        return self._name

    @property
    def value(self):
        return float(self._value.quantize(Decimal('1.00')))

    @property
    def value_in_decimal(self):
        return self._value

    @property
    def multi_discount(self):
        return self._multi_discount

