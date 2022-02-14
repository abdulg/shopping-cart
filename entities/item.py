#!/usr/bin/env python
# -*- coding: utf-8 -*-
from decimal import *


class Item:
    def __init__(self, name, value):
        self._name = name
        self._value = value

    @property
    def name(self):
        return self._name

    @property
    def value(self):
        return float(Decimal(self._value).quantize(Decimal('0.01')))
