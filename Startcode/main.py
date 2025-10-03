from Startcode.recept import Recept
from Startcode.ingredient import Ingredient
from Startcode.stap import Stap

def main():
    recepten: list[Recept] = []

    # Recept 1 - Kip Kerrie
    recept1 = Recept("Kip Kerrie", "Kip kerrie zonder pakjes en zakjes")
    recept1.voeg_ingredient_toe(Ingredient("Kipfilet", 200, "gram"))
    recept1.voeg_ingredient_toe(Ingredient("Sperziebonen", 150, "gram"))
    recept1.voeg_ingredient_toe(Ingredient("Rijst", 75, "gram"))
    recept1.voeg_ingredient_toe(Ingredient("Kerriepoeder", 1, "eetlepel"))
    recept1.voeg_ingredient_toe(Ingredient("Ui", 1, "stuk"))

    recept1.voeg_stap_toe(Stap("Kook de rijst volgens de aanwijzingen op de verpakking."))
    recept1.voeg_stap_toe(Stap("Snijd de kipfilet in blokjes en de ui fijn."))
    recept1.voeg_stap_toe(Stap("Bak de kip en ui in een pan en voeg kerriepoeder toe."))
    recept1.voeg_stap_toe(Stap("Voeg de sperziebonen toe en laat even mee garen."))
    recepten.append(recept1)

    # Recept 2 - Pannenkoeken
    recept2 = Recept("Pannenkoeken", "Luchtige pannenkoeken voor 1 persoon.")
    recept2.voeg_ingredient_toe(Ingredient("Bloem", 100, "gram"))
    recept2.voeg_ingredient_toe(Ingredient("Melk", 200, "ml"))
    recept2.voeg_ingredient_toe(Ingredient("Ei", 1, "stuk"))
    recept2.voeg_ingredient_toe(Ingredient("Boter", 10, "gram"))
    recept2.voeg_ingredient_toe(Ingredient("Zout", 1, "snufje"))

    recept2.voeg_stap_toe(Stap("Meng bloem, melk, ei en zout tot een glad beslag."))
    recept2.voeg_stap_toe(Stap("Verhit boter in een koekenpan."))
    recept2.voeg_stap_toe(Stap("Bak het beslag tot een dunne pannenkoek."))
    recepten.append(recept2)

    # Recept 3 - Omelet
    recept3 = Recept("Omelet", "Snelle omelet met groenten.")
    recept3.voeg_ingredient_toe(Ingredient("Ei", 2, "stuks"))
    recept3.voeg_ingredient_toe(Ingredient("Paprika", 50, "gram"))
    recept3.voeg_ingredient_toe(Ingredient("Ui", 0.5, "stuk"))
    recept3.voeg_ingredient_toe(Ingredient("Boter", 10, "gram"))
    recept3.voeg_ingredient_toe(Ingredient("Peper en zout", 1, "snufje"))

    recept3.voeg_stap_toe(Stap("Snijd de paprika en ui in kleine stukjes."))
    recept3.voeg_stap_toe(Stap("Klop de eieren los met peper en zout."))
    recept3.voeg_stap_toe(Stap("Bak de groenten kort in boter."))
    recept3.voeg_stap_toe(Stap("Voeg het eimengsel toe en bak de omelet gaar."))
    recepten.append(recept3)

    # Overzicht tonen
    print("\nReceptenboek — kies een recept:\n")
    for i, recept in enumerate(recepten, start=1):
        print(f"{i}. {recept.get_naam()}")

    keuze = int(input("\nVoer het nummer van een recept in: ")) - 1
    gekozen = recepten[keuze]
    gekozen.toon_recept()


if __name__ == "__main__":
    main()
