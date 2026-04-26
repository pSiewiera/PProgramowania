class BazowyPomocnik:
    def __init__(self):
        self.nastepny = None

    def ustaw_nastepny(self, pomocnik):
        self.nastepny = pomocnik
        return pomocnik

    def pokaz_pomoc(self):
        if self.nastepny:
            return self.nastepny.pokaz_pomoc()
        return "Brak pomocy"

class Tooltip(BazowyPomocnik):
    def __init__(self, tekst=None):
        super().__init__()
        self.tooltiptext = tekst

    def pokaz_pomoc(self):
        if self.tooltiptext:
            return "Pomoc z dymka: " + self.tooltiptext
        return super().pokaz_pomoc()

class ModalHelp(BazowyPomocnik):
    def __init__(self, tekst=None):
        super().__init__()
        self.modalhelptext = tekst

    def pokaz_pomoc(self):
        if self.modalhelptext:
            return "Pomoc z okna modalnego: " + self.modalhelptext
        return super().pokaz_pomoc()

class PageHelp(BazowyPomocnik):
    def __init__(self, url=None):
        super().__init__()
        self.pageurl = url

    def pokaz_pomoc(self):
        if self.pageurl:
            return "Przekierowanie do strony: " + self.pageurl
        return super().pokaz_pomoc()

podpowiedz = Tooltip()
okno = ModalHelp()
strona = PageHelp("https://www.youtube.com/watch?v=TGaWLLBTnvs")

podpowiedz.ustaw_nastepny(okno).ustaw_nastepny(strona)

print(podpowiedz.pokaz_pomoc())



okno.modalhelptext = "Instrukcja wypełniania formularza"
print(podpowiedz.pokaz_pomoc())