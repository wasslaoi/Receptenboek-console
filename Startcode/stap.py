# Startcode/stap.py
class Stap:
    def __init__(self, beschrijving: str):
        self.beschrijving = beschrijving

    def __str__(self) -> str:
        return self.beschrijving