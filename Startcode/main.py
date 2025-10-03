from Startcode.recept import Recept
from Startcode.ingredient import Ingredient
from Startcode.stap import Stap

# ==== invoerhelpers ====
def _yn(prompt: str) -> bool:
    while True:
        ans = input(prompt + " (j/n): ").strip().lower()
        if ans in ("j", "ja", "y", "yes"):
            return True
        if ans in ("n", "nee", "no"):
            return False
        print("Antwoord met j of n.")

def _int(prompt: str, min_value: int | None = None) -> int:
    while True:
        try:
            v = int(input(prompt))
            if min_value is not None and v < min_value:
                print(f"Minimaal {min_value}."); continue
            return v
        except ValueError:
            print("Geef een geheel getal op.")

def _float(prompt: str, min_value: float | None = None) -> float:
    while True:
        try:
            v = float(input(prompt))
            if min_value is not None and v < min_value:
                print(f"Geef een waarde ≥ {min_value}."); continue
            return v
        except ValueError:
            print("Geef een getal op.")

def _text(prompt: str) -> str:
    while True:
        t = input(prompt).strip()
        if t:
            return t
        print("Leeg is niet toegestaan.")

# ==== recept toevoegen (FR-6) ====
def voeg_recept_toe_interactief() -> Recept:
    print("\n=== Nieuw recept toevoegen ===")
    naam = _text("Naam: ")
    omschrijving = _text("Korte omschrijving: ")
    recept = Recept(naam, omschrijving)

    while _yn("Ingrediënt toevoegen?"):
        in_naam = _text("Ingrediëntnaam: ")
        hoeveelheid = _float("Hoeveelheid (voor 1 persoon): ", 0.0)
        eenheid = _text("Eenheid (bijv. gram, ml, stuk): ")
        kcal_per_eenheid = _float("kcal per eenheid: ", 0.0)
        ing = Ingredient(in_naam, hoeveelheid, eenheid, kcal_per_eenheid)

        if _yn("Plantaardig alternatief opgeven?"):
            alt_naam = _text("Alternatief naam: ")
            alt_kcal = _float("kcal per eenheid (alternatief): ", 0.0)
            alt = Ingredient(alt_naam, hoeveelheid, eenheid, alt_kcal)
            ing.set_plantaardig_alternatief(alt)

        recept.voeg_ingredient_toe(ing)

    while _yn("Bereidingsstap toevoegen?"):
        beschrijving = _text("Stap: ")
        tip = _text("Tip: ") if _yn("Tip toevoegen bij deze stap?") else None
        recept.voeg_stap_toe(Stap(beschrijving, tip))

    print(f"\nRecept '{naam}' toegevoegd.\n")
    return recept

# ==== recept tonen (FR-2,3,4 + FR-7) ====
def toon_recept_interactief(recepten: list[Recept], idx: int) -> None:
    if idx < 0 or idx >= len(recepten):
        print("Ongeldige keuze.")
        return
    gekozen = recepten[idx]

    aantal = _int("Voor hoeveel personen? ", 1)
    plantaardig = _yn("Plantaardige variant gebruiken?")
    gekozen.set_aantal_personen(aantal)
    gekozen.toon_recept(plantaardig=plantaardig)

    totaal = gekozen.totaal_kcal(plantaardig=plantaardig)
    print(f"\nTotaal kcal: {round(totaal, 1)}\n")

    if _yn("Dit recept verwijderen?"):
        verwijderd = recepten.pop(idx)
        print(f"Recept '{verwijderd.get_naam()}' is verwijderd.\n")

# ==== overzicht ====
def toon_overzicht(recepten: list[Recept]) -> None:
    if not recepten:
        print("\nGeen recepten beschikbaar.\n")
        return
    print("\nRecepten:")
    for i, r in enumerate(recepten, start=1):
        print(f"{i}. {r.get_naam()}")
    print()

def kies_recept_index(recepten: list[Recept]) -> int | None:
    if not recepten:
        return None
    keuze = _int("Kies een receptnummer: ", 1)
    if keuze > len(recepten):
        print("Ongeldige keuze.")
        return None
    return keuze - 1

# ==== startrecepten (FR-1 basis) ====
def init_startrecepten() -> list[Recept]:
    recepten: list[Recept] = []

    # Recept 1
    r1 = Recept("Kip Kerrie", "Kip kerrie zonder pakjes en zakjes")
    kip = Ingredient("Kipfilet", 200, "gram", 1.65)
    tofu = Ingredient("Tofu", 200, "gram", 0.76)
    kip.set_plantaardig_alternatief(tofu)
    r1.voeg_ingredient_toe(kip)
    r1.voeg_ingredient_toe(Ingredient("Sperziebonen", 150, "gram", 0.31))
    r1.voeg_ingredient_toe(Ingredient("Rijst (droog)", 75, "gram", 3.6))
    r1.voeg_ingredient_toe(Ingredient("Kerriepoeder", 1, "el", 20))
    r1.voeg_ingredient_toe(Ingredient("Ui", 1, "stuk", 40))
    r1.voeg_stap_toe(Stap("Kook de rijst volgens de aanwijzingen."))
    r1.voeg_stap_toe(Stap("Snijd de kip en de ui."))
    r1.voeg_stap_toe(Stap("Bak de kip en ui met kerriepoeder.", tip="Scheutje water tegen aanbakken."))
    r1.voeg_stap_toe(Stap("Voeg sperziebonen toe en laat garen."))
    recepten.append(r1)

    # Recept 2
    r2 = Recept("Pannenkoeken", "Luchtige pannenkoeken voor 1 persoon.")
    r2.voeg_ingredient_toe(Ingredient("Bloem", 100, "gram", 3.64))
    r2.voeg_ingredient_toe(Ingredient("Melk", 200, "ml", 0.65))
    ei = Ingredient("Ei", 1, "stuk", 78)
    aquafaba = Ingredient("Aquafaba (ei-vervanger)", 60, "ml", 0.02)
    ei.set_plantaardig_alternatief(aquafaba)
    r2.voeg_ingredient_toe(ei)
    r2.voeg_ingredient_toe(Ingredient("Boter", 10, "gram", 7.2))
    r2.voeg_ingredient_toe(Ingredient("Zout", 1, "snufje", 0))
    r2.voeg_stap_toe(Stap("Meng alles tot beslag.", tip="Laat 10 minuten rusten."))
    r2.voeg_stap_toe(Stap("Verhit boter in een pan."))
    r2.voeg_stap_toe(Stap("Bak het beslag tot een pannenkoek."))
    recepten.append(r2)

    # Recept 3
    r3 = Recept("Omelet", "Snelle omelet met groenten.")
    ei2 = Ingredient("Ei", 2, "stuks", 78)
    kikkererwtenmeel = Ingredient("Kikkererwtenmeel + water", 120, "gram/ml", 1.1)
    ei2.set_plantaardig_alternatief(kikkererwtenmeel)
    r3.voeg_ingredient_toe(ei2)
    r3.voeg_ingredient_toe(Ingredient("Paprika", 50, "gram", 0.26))
    r3.voeg_ingredient_toe(Ingredient("Ui", 0.5, "stuk", 20))
    r3.voeg_ingredient_toe(Ingredient("Boter/olie", 10, "gram", 9))
    r3.voeg_ingredient_toe(Ingredient("Peper en zout", 1, "snufje", 0))
    r3.voeg_stap_toe(Stap("Snijd paprika en ui."))
    r3.voeg_stap_toe(Stap("Klop de eieren los met peper en zout.", tip="Scheutje water maakt luchtiger."))
    r3.voeg_stap_toe(Stap("Bak groenten kort."))
    r3.voeg_stap_toe(Stap("Voeg eimengsel toe en bak gaar."))
    recepten.append(r3)

    return recepten

# ==== hoofdmenu (FR-8) ====
def hoofdmenu(recepten: list[Recept]) -> None:
    while True:
        print("\n=== Receptenboek ===")
        print("1) Recepten bekijken")
        print("2) Nieuw recept toevoegen")
        print("3) Stoppen")
        keuze = _int("Kies: ", 1)

        if keuze == 1:
            toon_overzicht(recepten)
            idx = kies_recept_index(recepten)
            if idx is not None:
                toon_recept_interactief(recepten, idx)
        elif keuze == 2:
            nieuw = voeg_recept_toe_interactief()
            recepten.append(nieuw)
        elif keuze == 3:
            print("Afgesloten.")
            break
        else:
            print("Ongeldige keuze.")

def main():
    recepten = init_startrecepten()
    hoofdmenu(recepten)

if __name__ == "__main__":
    main()
