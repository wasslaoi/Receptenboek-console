from Startcode.recept import Recept
from Startcode.ingredient import Ingredient
from Startcode.stap import Stap


def main():
    recepten: list[Recept] = []

    # Recept 1: Kip Kerrie
    recept1 = Recept("Kip Kerrie", "Kip kerrie zonder pakjes en zakjes")
    kip = Ingredient("Kipfilet", 200, "gram", 1.65)          # ~165 kcal per 100g
    tofu = Ingredient("Tofu", 200, "gram", 0.76)
    kip.set_plantaardig_alternatief(tofu)
    recept1.voeg_ingredient_toe(kip)
    recept1.voeg_ingredient_toe(Ingredient("Sperziebonen", 150, "gram", 0.31))
    recept1.voeg_ingredient_toe(Ingredient("Rijst (droog)", 75, "gram", 3.6))
    recept1.voeg_ingredient_toe(Ingredient("Kerriepoeder", 1, "el", 20))
    recept1.voeg_ingredient_toe(Ingredient("Ui", 1, "stuk", 40))
    recept1.voeg_stap_toe(Stap("Kook de rijst volgens de aanwijzingen op de verpakking."))
    recept1.voeg_stap_toe(Stap("Snijd de kipfilet in blokjes en de ui fijn."))
    recept1.voeg_stap_toe(Stap("Bak de kip en ui in een pan en voeg kerriepoeder toe.", tip="Scheutje water tegen aanbakken."))
    recept1.voeg_stap_toe(Stap("Voeg de sperziebonen toe en laat even mee garen."))
    recepten.append(recept1)

    # Recept 2: Pannenkoeken
    recept2 = Recept("Pannenkoeken", "Luchtige pannenkoeken voor 1 persoon.")
    recept2.voeg_ingredient_toe(Ingredient("Bloem", 100, "gram", 3.64))
    recept2.voeg_ingredient_toe(Ingredient("Melk", 200, "ml", 0.65))
    ei = Ingredient("Ei", 1, "stuk", 78)
    aquafaba = Ingredient("Aquafaba (ei-vervanger)", 60, "ml", 0.02)
    ei.set_plantaardig_alternatief(aquafaba)
    recept2.voeg_ingredient_toe(ei)
    recept2.voeg_ingredient_toe(Ingredient("Boter", 10, "gram", 7.2))
    recept2.voeg_ingredient_toe(Ingredient("Zout", 1, "snufje", 0))
    recept2.voeg_stap_toe(Stap("Meng bloem, melk, ei en zout tot een glad beslag.", tip="Laat 10 minuten rusten."))
    recept2.voeg_stap_toe(Stap("Verhit boter in een koekenpan."))
    recept2.voeg_stap_toe(Stap("Bak het beslag tot een dunne pannenkoek."))
    recepten.append(recept2)

    # Recept 3: Omelet
    recept3 = Recept("Omelet", "Snelle omelet met groenten.")
    ei2 = Ingredient("Ei", 2, "stuks", 78)
    kikkererwtenmeel = Ingredient("Kikkererwtenmeel + water", 120, "gram/ml", 1.1)
    ei2.set_plantaardig_alternatief(kikkererwtenmeel)
    recept3.voeg_ingredient_toe(ei2)
    recept3.voeg_ingredient_toe(Ingredient("Paprika", 50, "gram", 0.26))
    recept3.voeg_ingredient_toe(Ingredient("Ui", 0.5, "stuk", 20))
    recept3.voeg_ingredient_toe(Ingredient("Boter/olie", 10, "gram", 9))
    recept3.voeg_ingredient_toe(Ingredient("Peper en zout", 1, "snufje", 0))
    recept3.voeg_stap_toe(Stap("Snijd de paprika en ui in kleine stukjes."))
    recept3.voeg_stap_toe(Stap("Klop de eieren los met peper en zout.", tip="Een scheutje water maakt het luchtiger."))
    recept3.voeg_stap_toe(Stap("Bak de groenten kort in boter/olie."))
    recept3.voeg_stap_toe(Stap("Voeg het eimengsel toe en bak de omelet gaar."))
    recepten.append(recept3)

    # Overzicht
    print("\nReceptenboek — kies een recept:\n")
    for i, r in enumerate(recepten, start=1):
        print(f"{i}. {r.get_naam()}")

    idx = int(input("\nVoer het nummer van een recept in: ")) - 1
    gekozen = recepten[idx]

    # Invoer voor personen en variant
    while True:
        try:
            aantal = int(input("Voor hoeveel personen? "))
            if aantal < 1:
                raise ValueError()
            break
        except ValueError:
            print("Voer een positief geheel getal in.")

    plantaardig = input("Plantaardige variant gebruiken? (j/n): ").strip().lower() == "j"

    gekozen.set_aantal_personen(aantal)
    gekozen.toon_recept(plantaardig=plantaardig)

    # Totaal kcal
    totaal = gekozen.totaal_kcal(plantaardig=plantaardig)
    print(f"\nTotaal kcal: {round(totaal, 1)}\n")


if __name__ == "__main__":
    main()
# ==== Helpers voor invoer ====
def _yn(prompt: str) -> bool:
    while True:
        ans = input(prompt + " (j/n): ").strip().lower()
        if ans in ("j", "ja", "y", "yes"): return True
        if ans in ("n", "nee", "no"): return False
        print("Foutieve invoer. Antwoord met j of n.")

def _int(prompt: str, min_value: int = None) -> int:
    while True:
        try:
            v = int(input(prompt))
            if min_value is not None and v < min_value:
                print(f"Geef minimaal {min_value} op."); continue
            return v
        except ValueError:
            print("Foutieve invoer. Geef een geheel getal op.")

def _float(prompt: str, min_value: float = None) -> float:
    while True:
        try:
            v = float(input(prompt))
            if min_value is not None and v < min_value:
                print(f"Geef een waarde ≥ {min_value} op."); continue
            return v
        except ValueError:
            print("Foutieve invoer. Geef een getal op.")

def _text(prompt: str) -> str:
    while True:
        t = input(prompt).strip()
        if t: return t
        print("Leeg is niet toegestaan.")

# ==== Nieuw recept toevoegen ====
from recept import Recept
from ingredient import Ingredient
from stap import Stap

def voeg_recept_toe_interactief() -> Recept:
    print("\n=== Nieuw recept toevoegen ===")
    naam = _text("Naam van het recept: ")
    omschrijving = _text("Korte omschrijving: ")
    recept = Recept(naam, omschrijving)

    # Ingrediënten
    while _yn("Ingrediënt toevoegen?"):
        in_naam = _text("Naam ingrediënt: ")
        hoeveelheid = _float("Hoeveelheid: ", 0.0)
        eenheid = _text("Eenheid (bijv. gram, stuks): ")
        kcal = _float("Aantal kcal: ", 0.0)
        alternatief = None
        if _yn("Plantaardig alternatief opgeven?"):
            alternatief = _text("Naam alternatief: ")
        recept.voeg_ingredient_toe(Ingredient(in_naam, hoeveelheid, eenheid, kcal, alternatief))

    # Stappen
    while _yn("Bereidingsstap toevoegen?"):
        beschrijving = _text("Stap: ")
        tip = None
        if _yn("Tip toevoegen bij deze stap?"):
            tip = _text("Tip: ")
        recept.voeg_stap_toe(Stap(beschrijving, tip))

    print(f"\nRecept '{naam}' toegevoegd!\n")
    return recept

