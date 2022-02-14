#!/usr/bin/env python
# -*- coding: utf-8 -*-
from entities.item import Item


class TestItem:
    def test_item__correctly_constructed_item(self):
        item = Item('Dove Soap', 29.99)
        assert item.name == 'Dove Soap'
        assert item.value == 29.99
