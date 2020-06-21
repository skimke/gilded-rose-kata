# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose

class GildedRoseStandardItemTest(unittest.TestCase):
    def setUp(self):
        self.item = Item(
            name="standard",
            sell_in=1,
            quality=1,
        )

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

    def test_update_quality_decreases_quality_by_2_if_sell_in_is_below_0(self):
        self.item.sell_in = -1
        self.item.quality = 4
        gilded_rose = GildedRose([self.item])

        gilded_rose.update_quality()

        self.assertEqual(2, self.item.quality)

        gilded_rose.update_quality()

        self.assertEqual(0, self.item.quality)


class GildedRoseAgedBrieTest(unittest.TestCase):
    def setUp(self):
        self.aged_brie = Item(
            name="Aged Brie",
            sell_in=1,
            quality=1,
        )

    def test_update_quality_increases_quality_for_aged_brie(self):
        gilded_rose = GildedRose([self.aged_brie])

        gilded_rose.update_quality()

        self.assertEqual(2, self.aged_brie.quality)

    def test_update_quality_never_increases_quality_over_50(self):
        self.aged_brie.quality = 50
        gilded_rose = GildedRose([self.aged_brie])

        gilded_rose.update_quality()

        self.assertEqual(50, self.aged_brie.quality)

    def test_update_quality_increases_quality_by_2_for_aged_brie_if_sell_in_is_below_0(self):
        self.aged_brie.sell_in = -1
        self.aged_brie.quality = 2
        gilded_rose = GildedRose([self.aged_brie])

        gilded_rose.update_quality()

        self.assertEqual(4, self.aged_brie.quality)

        gilded_rose.update_quality()

        self.assertEqual(6, self.aged_brie.quality)


class GildedRoseSulfurasTest(unittest.TestCase):
    def setUp(self):
        self.sulfuras = Item(
            name="Sulfuras, Hand of Ragnaros",
            sell_in=1,
            quality=1,
        )

    def test_update_quality_never_decreases_sell_in_or_quality_for_sulfuras(self):
        gilded_rose = GildedRose([self.sulfuras])

        gilded_rose.update_quality()

        self.assertEqual(1, self.sulfuras.sell_in)
        self.assertEqual(1, self.sulfuras.quality)

        self.sulfuras.sell_in = -1

        self.assertEqual(-1, self.sulfuras.sell_in)
        self.assertEqual(1, self.sulfuras.quality)


class GildedRoseBackstagePassesTest(unittest.TestCase):
    def setUp(self):
        self.backstage_passes = Item(
            name="Backstage passes to a TAFKAL80ETC concert",
            sell_in=11,
            quality=1,
        )

    def test_update_quality_increases_quality_for_backstage_passes(self):
        gilded_rose = GildedRose([self.backstage_passes])

        gilded_rose.update_quality()

        self.assertEqual(2, self.backstage_passes.quality)

    def test_update_quality_never_increases_quality_over_50_for_backstage_passes(self):
        self.backstage_passes.quality = 50
        gilded_rose = GildedRose([self.backstage_passes])

        gilded_rose.update_quality()

        self.assertEqual(50, self.backstage_passes.quality)

    def test_update_quality_sets_quality_to_0_for_backstage_passes_if_sell_in_is_below_0(self):
        self.backstage_passes.sell_in = -1
        self.backstage_passes.quality = 2
        gilded_rose = GildedRose([self.backstage_passes])

        gilded_rose.update_quality()

        self.assertEqual(0, self.backstage_passes.quality)

    def test_update_quality_increases_quality_by_2_for_backstage_passes_if_sell_in_is_below_11(self):
        self.backstage_passes.sell_in = 10
        self.backstage_passes.quality = 2
        gilded_rose = GildedRose([self.backstage_passes])

        gilded_rose.update_quality()

        self.assertEqual(4, self.backstage_passes.quality)

        gilded_rose.update_quality()

        self.assertEqual(6, self.backstage_passes.quality)

    def test_update_quality_increases_quality_by_3_for_backstage_passes_if_sell_in_is_below_6(self):
        self.backstage_passes.sell_in = 5
        self.backstage_passes.quality = 2
        gilded_rose = GildedRose([self.backstage_passes])

        gilded_rose.update_quality()

        self.assertEqual(5, self.backstage_passes.quality)

        gilded_rose.update_quality()

        self.assertEqual(8, self.backstage_passes.quality)


if __name__ == '__main__':
    unittest.main()
