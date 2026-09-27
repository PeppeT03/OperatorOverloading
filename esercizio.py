class Frazione():
    def __init__(self,numeratore,denominatore):
        self.numeratore=numeratore
        self.denominatore=denominatore
    def __add__(self, altro):
        nuovo_numeratore=self.numeratore+altro.numeratore
        nuovo_denominatore=self.denominatore+altro.denominatore
        return Frazione(nuovo_numeratore,nuovo_denominatore)
    def __eq__(self, altro):
        return self.numeratore==altro.numeratore and self.denominatore==altro.denominatore
    def __str__(self):
        return f"{self.numeratore}/{self.denominatore}"

F1=Frazione(10,20)
F2=Frazione(20,10)
F3=Frazione(10,20)

F4=F1+F2
print(F1==F3)
print(F1)
print(F2)
print(F3)
print(F4)                
