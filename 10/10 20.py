class Kontakt():
    def __init__(self,nazwa,email,telefon):
        self.nazwa=nazwa
        self.email=email
        self.telefon=telefon
    def wyswietl_kontakt(self):
        print(f"{self.nazwa},{self.email},{self.telefon}")    
class ListaKontaktow():
    def __init__(self):
        self.kontakty=[]
    def dodaj(self,kontakt):
        self.kontakty.append(kontakt)
    def wyswietl_kontakty(self):
        for kontakt in self.kontakty:
            kontakt.wyswietl_kontakt()
p=Kontakt("John Brown","brown@onet.pl", 555234000)
lista=ListaKontaktow()
lista.dodaj(p)
lista.wyswietl_kontakty()