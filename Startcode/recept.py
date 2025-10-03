# Startcode/recept.py
from Startcode.ingredient import Ingredient
from Startcode.stap import Stap


class Recept:
    def __init__(self, naam: str, omschrijving: str):
        self.__naam = naam
        self.__omschrijving = omschrijving
        self.__ingredient_list: list[Ingredient] = []
        self.__stappen: list[Stap] = []

    # nodig voor het overzicht in main
    def get_naam(self) -> str:
        return self.__naam

    # FR-1: toevoegen
    def voeg_ingredient_toe(self, ingredient: Ingredient) -> None:
        self.__ingredient_list.append(ingredient)

    def voeg_stap_toe(self, stap: Stap) -> None:
        self.__stappen.append(stap)

    # FR-1: tonen in gevraagde volgorde/format
    def toon_recept(self) -> None:
        print(f"\n{self.__naam}")
        print(self.__omschrijving)

        print("\nIngrediënten:")
        for ing in self.__ingredient_list:
            print(f" - {ing}")

        print("\nStappen:")
        for i, stap in enumerate(self.__stappen, start=1):
            print(f"{i}. {stap}")
