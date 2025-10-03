# Startcode/ingredient.py
class Ingredient:
    def __init__(self, naam: str, basis_hoeveelheid: float, eenheid: str, kcal_per_eenheid: float):
        # basis_hoeveelheid is voor 1 persoon (week 1-eis)
        self.naam = naam
        self.basis_hoeveelheid = basis_hoeveelheid
        self.eenheid = eenheid
        self.kcal_per_eenheid = kcal_per_eenheid
        self.plantaardig_alternatief: "Ingredient | None" = None

        # actuele hoeveelheid = basis * aantal_personen (initieel 1)
        self.hoeveelheid = basis_hoeveelheid

    def set_plantaardig_alternatief(self, alternatief: "Ingredient"):
        self.plantaardig_alternatief = alternatief

    def schaal_voor_personen(self, aantal_personen: int) -> None:
        """Stel de actuele hoeveelheid in op basis van het aantal personen."""
        self.hoeveelheid = self.basis_hoeveelheid * aantal_personen

    def variant(self, plantaardig: bool) -> "Ingredient":
        """Geef de gekozen variant terug (plantaardig of origineel)."""
        if plantaardig and self.plantaardig_alternatief is not None:
            # Zorg dat alternatief ook dezelfde hoeveelheid krijgt
            alt = self.plantaardig_alternatief
            alt.hoeveelheid = self.hoeveelheid
            return alt
        return self

    def kcal_totaal(self) -> float:
        return float(self.hoeveelheid) * float(self.kcal_per_eenheid)

    def __str__(self) -> str:
        return f"{self.hoeveelheid} {self.eenheid} {self.naam}"

