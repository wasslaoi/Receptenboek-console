class Ingredient:
    def __init__(self, naam: str, basis_hoeveelheid: float, eenheid: str, kcal_per_eenheid: float):
        # basis_hoeveelheid is voor 1 persoon
        self.naam = naam
        self.basis_hoeveelheid = basis_hoeveelheid
        self.eenheid = eenheid
        self.kcal_per_eenheid = kcal_per_eenheid

        # actuele hoeveelheid past mee met aantal personen
        self.hoeveelheid = basis_hoeveelheid

        # optioneel plantaardig alternatief
        self.plantaardig_alternatief: "Ingredient | None" = None

    def set_plantaardig_alternatief(self, alternatief: "Ingredient") -> None:
        self.plantaardig_alternatief = alternatief

    def schaal_voor_personen(self, aantal_personen: int) -> None:
        self.hoeveelheid = self.basis_hoeveelheid * aantal_personen

    def variant(self, plantaardig: bool) -> "Ingredient":
        # geef de gekozen variant terug en neem de huidige hoeveelheid over
        if plantaardig and self.plantaardig_alternatief is not None:
            alt = self.plantaardig_alternatief
            alt.hoeveelheid = self.hoeveelheid
            return alt
        return self

    def kcal_totaal(self) -> float:
        return float(self.hoeveelheid) * float(self.kcal_per_eenheid)

    def __str__(self) -> str:
        return f"{self.hoeveelheid} {self.eenheid} {self.naam} ({round(self.kcal_totaal(), 1)} kcal)"

