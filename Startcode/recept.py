from Startcode.ingredient import Ingredient
from Startcode.stap import Stap

class Recept:
    def __init__(self, naam: str, omschrijving: str):
        self.__naam = naam
        self.__omschrijving = omschrijving
        self.__ingredient_list: list[Ingredient] = []
        self.__stappen: list[Stap] = []
        self.__aantal_personen: int = 1

    def get_naam(self) -> str:
        return self.__naam

    def get_omschrijving(self) -> str:
        return self.__omschrijving

    def get_stappen(self) -> list[Stap]:
        return self.__stappen

    def get_ingredienten(self, plantaardig: bool = False) -> list[Ingredient]:
        return [ing.variant(plantaardig) for ing in self.__ingredient_list]

    def voeg_ingredient_toe(self, ingredient: Ingredient) -> None:
        ingredient.schaal_voor_personen(self.__aantal_personen)
        self.__ingredient_list.append(ingredient)

    def voeg_stap_toe(self, stap: Stap) -> None:
        self.__stappen.append(stap)

    def voeg_stap_met_tip_toe(self, beschrijving: str, tip: str) -> None:
        self.voeg_stap_toe(Stap(beschrijving, tip))

    def set_aantal_personen(self, aantal: int) -> None:
        if aantal < 1:
            raise ValueError("Aantal personen moet minimaal 1 zijn.")
        self.__aantal_personen = aantal
        for ing in self.__ingredient_list:
            ing.schaal_voor_personen(aantal)

    def totaal_kcal(self, plantaardig: bool = False) -> float:
        return sum(ing.variant(plantaardig).kcal_totaal() for ing in self.__ingredient_list)

    def toon_recept(self, plantaardig: bool = False) -> None:
        print(f"\n{self.get_naam()}")
        print(self.get_omschrijving())
        print("\nIngrediënten:")
        for ing in self.get_ingredienten(plantaardig):
            print(f"- {ing}")
        print("\nBereidingsstappen:")
        for i, stap in enumerate(self.get_stappen(), start=1):
            print(f"{i}. {stap}")
