# Startcode/stap.py
class Stap:
    def __init__(self, beschrijving: str, tip: str | None = None):
        self.beschrijving = beschrijving
        self.tip = tip

    def __str__(self) -> str:
        return f"{self.beschrijving}" + (f" (Tip: {self.tip})" if self.tip else "")
