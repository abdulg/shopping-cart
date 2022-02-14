#!/usr/bin/env python
# -*- coding: utf-8 -*-
from decimal import *


class Cart:
    @property
    def total(self):
        return Decimal(0.00)
