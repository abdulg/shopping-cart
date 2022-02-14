#!/usr/bin/env python
# -*- coding: utf-8 -*-
from decimal import *


class Item:
    def __init__(self, name, value):
        self._name = name
        self._value = int(value * 100)

    @property
    def name(self):
        return self._name

    @property
    def value(self):
        return float(self._value) / 100.0

    @property
    def value_in_cents(self):
        return self._value
