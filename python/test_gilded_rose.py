# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    def setUp(self):
        self.item = Item("standard", 1, 1)

    def test_update_quality_decreases_standard_item_sell_in_and_quality_by_1(self):
        gilded_rose = GildedRose([self.item])

        gilded_rose.update_quality()

        self.assertEqual(0, self.item.sell_in)
        self.assertEqual(0, self.item.quality)

    def test_update_quality_decreases_standard_item_sell_in_by_1_below_0(self):
        self.item.sell_in = 0
        gilded_rose = GildedRose([self.item])

        gilded_rose.update_quality()

        self.assertEqual(-1, self.item.sell_in)

    def test_update_quality_does_not_decrease_quality_below_0(self):
        self.item.quality = 0
        gilded_rose = GildedRose([self.item])

        gilded_rose.update_quality()

        self.assertEqual(0, self.item.quality)

    def test_update_quality_doubles_quality_decrease_if_sell_in_is_below_0(self):
        self.item.sell_in = -1
        self.item.quality = 2
        gilded_rose = GildedRose([self.item])

        gilded_rose.update_quality()

        self.assertEqual(0, self.item.quality)

if __name__ == '__main__':
    unittest.main()
