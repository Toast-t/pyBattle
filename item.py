from __future__ import annotations
from abc import ABC, abstractmethod


class Item(ABC):

    @abstractmethod
    def __init__(self, name, description, item_id):
        self._name = name
        self._description = description
        self._item_id = item_id

    @property
    @abstractmethod
    def name(self) -> str:
        return self._name

    @property
    @abstractmethod
    def description(self) -> str:
        return self._description

    @property
    @abstractmethod
    def item_id(self) -> str:
        return self._item_id

    def item_type(self) -> str:
        return self._item_id[0]


class KeyItem(Item):
    def __init__(self, name, description, item_id):
        Item.__init__(self, name, description, item_id)

    def name(self) -> str:
        return self._name

    def description(self) -> str:
        return self._description

    def item_id(self) -> str:
        return self._item_id


class Weapon(Item):
    def __init__(self, name, description, attack, strength, stamina, magic, item_id):
        Item.__init__(self, name, description, item_id)
        self._attack = attack
        self._strength = strength
        self._stamina = stamina
        self._magic = magic

    def name(self) -> str:
        return self._name

    def description(self) -> str:
        return self._description

    def item_id(self) -> str:
        return self._item_id

    def attack(self) -> int:
        return self._attack

    def strength(self) -> int:
        return self._strength

    def stamina(self) -> int:
        return self._stamina

    def magic(self) -> int:
        return self._magic


items = {
    "K00001": KeyItem("Starter Kit Voucher",
                      "A Voucher for a starter kit. You can redeem this at the store",
                      "K00001"),
    "W00001": Weapon("Wooden Sword",
                     "A really terrible sword",
                     2, 2, 1, 0, "W00001"),
    "W00002": Weapon("Bow",
                     "The most basic bow",
                     2, 1, 2, 0, "W00002"),
    "W00003": Weapon("Weak Spell Book",
                     "A shabby spell book filled with only one spell",
                     2, 1, 0, 2, "W00003")
}


def get_item_by_id(item_id) -> Item:
    if item_id in items:
        return items[item_id]


def get_item_by_name(item_name) -> Item:
    items_list = items.items()
    for item in items_list:
        if item[1].name() == item_name:
            return item[1]


def add_item_to_pool(item_id, name, description, attack="NOTCOOLJIM", strength="NOTCOOLJIM", stamina="NOTCOOLJIM",
                     magic="NOTCOOLJIM") -> bool:
    if item_id in items.keys():
        return False

    if item_id[0] == 'C':
        items[item_id] = KeyItem(name, description, item_id)
        return True

    if item_id[0] == 'W':
        if attack == "NOTCOOLJIM" or strength == "NOTCOOLJIM" or stamina == "NOTCOOLJIM" or magic == "NOTCOOLJIM":
            raise ValueError("Item_id indicated a weapon was needed but stats for the weapon were missing")
        else:
            items[item_id] = Weapon(name, description, attack, strength, stamina, magic, item_id)
            return True
