# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def __decrease_quality(self, item, amount):
        for i in range(amount):
            if item.quality > 0:
                item.quality = item.quality - 1

    def update_quality(self):
        for item in self.items:
            if item.name == "Sulfuras, Hand of Ragnaros":
                item.quality = 80
                continue

            if "Conjured" in item.name:
                self.__decrease_quality(item, 2)
            elif item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
                self.__decrease_quality(item, 1)
            else:
                if item.quality < 50:
                    item.quality = item.quality + 1
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        if item.sell_in < 11:
                            if item.quality < 50:
                                item.quality = item.quality + 1
                        if item.sell_in < 6:
                            if item.quality < 50:
                                item.quality = item.quality + 1

            item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if item.name == "Aged Brie":
                    if item.quality < 50:
                        item.quality = item.quality + 1
                        continue

                if item.name == "Backstage passes to a TAFKAL80ETC concert":
                    item.quality = 0
                    continue

                if "Conjured" in item.name:
                    self.__decrease_quality(item, 2)
                    continue

                self.__decrease_quality(item, 1)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
