#!/usr/bin/env python
# -*- coding: utf-8 -*-
from decimal import *


class Cart:
    @property
    def total(self):
        return float(Decimal('0.00').quantize(Decimal('0.01')))
