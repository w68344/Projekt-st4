# # # # # # #lab 1
# # # # # # #zad 1
# # # # # #. Sprawdź typ bazowy dla danych str, int, list, range, dict, bool, bytes, NoneType#
# # # # # # print(type(str))        # <class 'type'>
# # # # # # print(type(int))        # <class 'type'>
# # # # # # print(type(list))       # <class 'type'>
# # # # # # print(type(range))      # <class 'type'>
# # # # # # print(type(dict))       # <class 'type'>
# # # # # # print(type(bool))       # <class 'type'>
# # # # # # print(type(bytes))      # <class 'type'>
# # # # # # print(type(type(None))) # <class 'type'> (NoneType)
# # # # # # #zad 2
# # # # # #. Zdefiniuj klasycznie za pomocą słowa kluczowego class jedną klasę i utwórz jej obiekty.
# # # # # # class Samochod:
# # # # # #     def __init__(self, marka, model):
# # # # # #         self.marka = marka
# # # # # #         self.model = model
# # # # # #
# # # # # # auto1 = Samochod("Toyota", "Corolla")
# # # # # # auto2 = Samochod("Ford", "Focus")
# # # # # #zad 3Zdefiniuj dynamicznie jedną klasę, w tym klasy z atrybutami i metodami. Stwórz jej obiekty.
# # # # # # def przedstaw(self):
# # # # # #     return f"Nazywam się {self.imie}"
# # # # # #
# # # # # # Osoba = type("Osoba", (object,), {"imie": "Jan", "przedstaw": przedstaw})
# # # # # # o1 = Osoba()
# # # # # # print(o1.przedstaw())
# # # # # #zad 4. Stwórz własną metaklasę. Utwórz własną metodę __new__ dla tej klasy, żeby nie dziedziczyła jej od metaklasy `type`
# # # # # # class MojaMeta:
# # # # # #     def __new__(cls, name, bases, dct):
# # # # # #         print(f"Tworzenie klasy: {name}")
# # # # # #         return type.__new__(type, name, bases, dct)
# # # # # # Zad. 5. Za pomocą swojej metaklasy utwórz kilka nowych klas potomnych.
# # # # # class MojaMeta(type):
# # # # #     def __new__(cls, name, bases, dct):
# # # # #         print(f"Tworzę klasę: {name}")
# # # # #         return super().__new__(cls, name, bases, dct)
# # # # #
# # # # # class A(metaclass=MojaMeta): pass
# # # # # class B(metaclass=MojaMeta): pass
# # # # #
# # # # # # Zad. 6. Stwórz dynamicznie klasy jako zmienne globalne, na bazie danych zapisanych w strukturze:
# # # # # # {‘Osoba’: [‘imię’, ‘nazwisko’, ‘wiek’], ‘Pojazd’: [‘marka’, ‘model’, ‘rocznik’]}.
# # # # # dane = {'Osoba': ['imię', 'nazwisko', 'wiek'], 'Pojazd': ['marka', 'model', 'rocznik']}
# # # # #
# # # # # for nazwa_klasy, atrybuty in dane.items():
# # # # #     def init(self, *args):
# # # # #         for attr, val in zip(atrybuty, args):
# # # # #             setattr(self, attr, val)
# # # # #     globals()[nazwa_klasy] = type(nazwa_klasy, (object,), {"__init__": init})
# # # # #
# # # # # # Zad. 7. Stwórz metaklasę , która przy próbie tworzenia klas na jej bazie o nazwach [Student, Wykladowca, Dziecko] stworzy klasy o nazwie Osoba.
# # # # # class MetaZamianaNazwy(type):
# # # # #     def __new__(cls, name, bases, dct):
# # # # #         if name in ['Student', 'Wykladowca', 'Dziecko']:
# # # # #             name = 'Osoba'
# # # # #         return super().__new__(cls, name, bases, dct)
# # # # #
# # # # # class Student(metaclass=MetaZamianaNazwy): pass
# # # # # print(Student.__name__)  # Osoba
# # # # #
# # # # # # Zad. 8. Stwórz metaklasę, która będzie powodować, że klasa stworzona na jej bazie i podająca
# # # # # # jako klasa bazowa klasę Osoba doda drugą klasę bazową Niewolnik.
# # # # # class Osoba: pass
# # # # # class Niewolnik: pass
# # # # #
# # # # # class MetaDodajNiewolnik(type):
# # # # #     def __new__(cls, name, bases, dct):
# # # # #         if Osoba in bases and Niewolnik not in bases:
# # # # #             bases = (Osoba, Niewolnik)
# # # # #         return super().__new__(cls, name, bases, dct)
# # # # #
# # # # # class Pracownik(Osoba, metaclass=MetaDodajNiewolnik): pass
# # # # # print(issubclass(Pracownik, Niewolnik))  # True
# # # # #
# # # # # # Zad. 9. Stwórz metaklasę Roślina do weryfikowania poprawności atrybutów/metod nowo tworzonych klas. Niech nowa klasa będzie miała możliwość posiadania naraz tylko jednego z listy
# # # # # # atrybutów [energetyczna, pastewna , rekultywacyjna, ozdobna].
# # # # # class Roslina(type):
# # # # #     dozwolone = ['energetyczna', 'pastewna', 'rekultywacyjna', 'ozdobna']
# # # # #
# # # # #     def __new__(cls, name, bases, dct):
# # # # #         count = sum(1 for a in cls.dozwolone if a in dct)
# # # # #         if count > 1:
# # # # #             raise TypeError("Tylko jeden atrybut z listy dozwolony!")
# # # # #         return super().__new__(cls, name, bases, dct)
# # # # #
# # # # #
# # # # # # Przykład poprawnej klasy:
# # # # # class Trawa(metaclass=Roslina):
# # # # #     energetyczna = True
# # # # #
# # # # # # Zad. 10. Stwórz metaklasę Podatnik, która do klas potomnych doda składnik numer_nip.
# # # # # class Podatnik(type):
# # # # #     def __new__(cls, name, bases, dct):
# # # # #         dct['numer_nip'] = '000-000-00-00'
# # # # #         return super().__new__(cls, name, bases, dct)
# # # # #
# # # # # class Firma(metaclass=Podatnik): pass
# # # # # print(Firma.numer_nip)
# # # # #
# # # # # # Zad. 11. Stwórz metaklasę Roślina, która z klas potomnych będzie usuwać atrybuty [mięśnie, nerwy, oczy, skóra].
# # # # # class Roslina(type):
# # # # #     niechciane = ['mięśnie', 'nerwy', 'oczy', 'skóra']
# # # # #
# # # # #     def __new__(cls, name, bases, dct):
# # # # #         for a in cls.niechciane:
# # # # #             dct.pop(a, None)
# # # # #         return super().__new__(cls, name, bases, dct)
# # # # #
# # # # #
# # # # # class Kaktus(metaclass=Roslina):
# # # # #     kolce = True
# # # # #     mięśnie = True  # zostanie usunięte
# # # # #
# # # # # # Zad. 12. Stwórz metaklasę Nazewnik do sprawdzania czy: nazwy klas zaczynają się od dużej litery;
# # # # # # zmienne klas zaczynają się od małej litery; zaś metody klas od dużej litery. Gdy nie zastosowano się do tych reguł należy poprawić nazwy w nowo tworzonej klasie.
# # # # # class Nazewnik(type):
# # # # #     def __new__(cls, name, bases, dct):
# # # # #         # popraw nazwę klasy
# # # # #         if not name[0].isupper():
# # # # #             name = name.capitalize()
# # # # #
# # # # #         # popraw zmienne klasowe
# # # # #         nowe_dct = {}
# # # # #         for k, v in dct.items():
# # # # #             if callable(v):
# # # # #                 if not k[0].isupper():
# # # # #                     k = k.capitalize()
# # # # #             else:
# # # # #                 if not k[0].islower():
# # # # #                     k = k.lower()
# # # # #             nowe_dct[k] = v
# # # # #
# # # # #         return super().__new__(cls, name, bases, nowe_dct)
# # # # #
# # # # #
# # # # # class test(nazewnik := Nazewnik):  # dynamiczne przypisanie metaklasy
# # # # #     Imie = "Jan"
# # # # #
# # # # #     def przedstaw(self):
# # # # #         pass
# # # # #
# # # # #
# # # # # print(hasattr(test, 'imie'))  # True
# # # # # print(hasattr(test, 'Przedstaw'))  # True
# # # # #
# # # # # # Zad. 13. Stwórz metaklasę Plikownik, który dla nowo tworzonych klas na jej bazie będzie tworzył
# # # # # # ich obiekty z atrybutami w formie plików tekstowych na dysku. W przypadku usuwania
# # # # # # obiektów, niech również zostanie usunięty ten plik z dysku.
# # # # #
# # # # # import os
# # # # #
# # # # # class Plikownik(type):
# # # # #     def __call__(cls, *args, **kwargs):
# # # # #         obj = super().__call__(*args, **kwargs)
# # # # #         filename = f"{cls.__name__}_{id(obj)}.txt"
# # # # #         obj._plik = filename
# # # # #         with open(filename, 'w') as f:
# # # # #             f.write(str(obj.__dict__))
# # # # #         return obj
# # # # #
# # # # #     def __del__(cls):
# # # # #         try:
# # # # #             os.remove(cls._plik)
# # # # #         except Exception:
# # # # #             pass
# # # # #
# # # # # class Dane(metaclass=Plikownik):
# # # # #     def __init__(self, a, b):
# # # # #         self.a = a
# # # # #         self.b = b
# # # # #
# # # # # d = Dane(1, 2)
# # # #
# # # #
# # # #
# # # # ##########################
# # # # ############################
# # # # ############################
# # # # # Zad. 1. Stwórz dekorator do dowolnej funkcji, który będzie wypisywał informację przed i po wywołaniu funkcji.
# # # # def info_decorator(func):
# # # #     def wrapper(*args, **kwargs):
# # # #         print("-> Przed wywołaniem funkcji.")
# # # #         result = func(*args, **kwargs)
# # # #         print("-> Po wywołaniu funkcji.")
# # # #         return result
# # # #     return wrapper
# # # #
# # # # @info_decorator
# # # # def przyklad():
# # # #     print("Wewnątrz funkcji.")
# # # #
# # # # przyklad()
# # # #
# # # # # Zad. 2. Stwórz funkcję do obliczania np. średniej dwóch liczb. Utwórz i dodaj do niej dekorator,
# # # # # który wypisze jakie argumenty zostały dostarczone do funkcji, celem weryfikacji wyniku.
# # # # def pokaz_argumenty(func):
# # # #     def wrapper(*args, **kwargs):
# # # #         print(f"Argumenty: {args}, {kwargs}")
# # # #         return func(*args, **kwargs)
# # # #     return wrapper
# # # #
# # # # @pokaz_argumenty
# # # # def srednia(a, b):
# # # #     return (a + b) / 2
# # # #
# # # # print(srednia(4, 8))
# # # #
# # # # # Zad. 3. Stwórz kolejny dekorator, który zmierzy czas wykonania funkcji (można użyć moduł `time`).
# # # # import time
# # # #
# # # # def mierzenie_czasu(func):
# # # #     def wrapper(*args, **kwargs):
# # # #         start = time.time()
# # # #         wynik = func(*args, **kwargs)
# # # #         end = time.time()
# # # #         print(f"Czas wykonania: {end - start:.6f} s")
# # # #         return wynik
# # # #     return wrapper
# # # #
# # # # @mierzenie_czasu
# # # # def obliczenia():
# # # #     time.sleep(0.5)
# # # #     return "Gotowe"
# # # #
# # # # obliczenia()
# # # #
# # # # # Zad. 4. Dla dowolnej klasy z metoda dodaj dekorator metody, który wypisze informacje o danej
# # # # # klasie.
# # # # def dekorator_klasy_metoda(func):
# # # #     def wrapper(self, *args, **kwargs):
# # # #         print(f"Wywołano metodę z klasy: {self.__class__.__name__}")
# # # #         return func(self, *args, **kwargs)
# # # #     return wrapper
# # # #
# # # # class Test:
# # # #     @dekorator_klasy_metoda
# # # #     def pokaz(self):
# # # #         print("Metoda klasy")
# # # #
# # # # t = Test()
# # # # t.pokaz()
# # # #
# # # # # Zad. 5. Stwórz dekorator klasy, który doda do niej zmienną `licznik_obiektów`.
# # # # def licznik_obiektow_dekorator(cls):
# # # #     cls.licznik_obiektow = 0
# # # #     orig_init = cls.__init__
# # # #
# # # #     def nowy_init(self, *args, **kwargs):
# # # #         cls.licznik_obiektow += 1
# # # #         orig_init(self, *args, **kwargs)
# # # #
# # # #     cls.__init__ = nowy_init
# # # #     return cls
# # # #
# # # #
# # # # @licznik_obiektow_dekorator
# # # # class Osoba:
# # # #     def __init__(self, imie):
# # # #         self.imie = imie
# # # #
# # # #
# # # # a = Osoba("Jan")
# # # # b = Osoba("Ala")
# # # # print(Osoba.licznik_obiektow)  # 2
# # # #
# # # # # Zad. 6. Stwórz dekorator klasy, który doda do niej metodę `info()` wypisującą składniki klasy.
# # # # def dodaj_info(cls):
# # # #     def info(self):
# # # #         print("Składniki klasy:", self.__dict__)
# # # #     cls.info = info
# # # #     return cls
# # # #
# # # # @dodaj_info
# # # # class Zwierze:
# # # #     def __init__(self, gatunek):
# # # #         self.gatunek = gatunek
# # # #
# # # # z = Zwierze("pies")
# # # # z.info()
# # # #
# # # # # Zad. 7. Stwórz klasę i wykorzystaj wbudowane dekoratory: staticmethod, classmethod, property.
# # # # # Przetestuj składniki na obiektach.
# # # # class Pracownik:
# # # #     podatek = 0.2
# # # #
# # # #     def __init__(self, imie, zarobki):
# # # #         self._imie = imie
# # # #         self._zarobki = zarobki
# # # #
# # # #     @property
# # # #     def zarobki_netto(self):
# # # #         return self._zarobki * (1 - self.podatek)
# # # #
# # # #     @classmethod
# # # #     def zmien_podatek(cls, nowy):
# # # #         cls.podatek = nowy
# # # #
# # # #     @staticmethod
# # # #     def powitanie():
# # # #         return "Witaj w firmie!"
# # # #
# # # #
# # # # p = Pracownik("Adam", 5000)
# # # # print(p.zarobki_netto)
# # # # print(Pracownik.powitanie())
# # # # Pracownik.zmien_podatek(0.1)
# # # # print(p.zarobki_netto)
# # # #
# # # # # Zad. 8. Zastosuj na swoich funkcjach dekoratory z pakietu HandyDecorators: trycatch, timer, singleton.
# # # # # pip install HandyDecorator
# # # # from HandyDecorators import trycatch, timer, singleton
# # # #
# # # # @trycatch
# # # # def dzielenie(a, b):
# # # #     return a / b
# # # #
# # # # @timer
# # # # def sleep_func():
# # # #     import time; time.sleep(0.3)
# # # #     return "done"
# # # #
# # # # @singleton
# # # # class Singleton:
# # # #     def __init__(self, x):
# # # #         self.x = x
# # # #
# # # # print(dzielenie(4, 0))  # bez wyjątku
# # # # print(sleep_func())
# # # # s1 = Singleton(10)
# # # # s2 = Singleton(20)
# # # # print(s1 is s2)  # True
# # # #
# # # # # Zad. 9. Z pakietu log_calls wykorzystaj dekoratory dla logowania funkcji, metod, klas, pakietów zewnętrznych.
# # # # # pip install log_calls
# # # #
# # # # from log_calls import log_calls, log_class
# # # #
# # # # @log_calls()
# # # # def suma(a, b):
# # # #     return a + b
# # # #
# # # # @log_class()
# # # # class Kalkulator:
# # # #     def __init__(self, model):
# # # #         self.model = model
# # # #
# # # #     def dodaj(self, x, y):
# # # #         return x + y
# # # #
# # # # suma(2, 3)
# # # #
# # # # k = Kalkulator("Casio")
# # # # print(k.dodaj(10, 5))
# # # ##########################
# # # ##########################
# # # ##########################
# # from multiprocessing import Process
# #
# #
# # def funkcja():
# #     print("Działa w osobnym procesie.")
# #
# # if __name__ == "__main__":
# #     # Zad. 1. Uruchom dowolną funkcję w procesie.
# #
# #
# #     p = Process(target=funkcja)
# #     p.start()
# #     p.join()
# #     p1 = Process(target=funkcja)
# #     p1.start()
# #     p1.join()
# #
# #
# #
# #     # Zad. 2. Uruchom funkcję z argumentami w procesie.
# #
# #
# #     def powitanie(imie, wiek):
# #         print(f"Cześć {imie}, masz {wiek} lat.")
# #
# #     p = Process(target=powitanie, args=("Ala", 25))
# #     p.start()
# #     p.join()
# #
# #     # Zad. 3. Utwórz klasę bazującą na klasie Process definiując działanie procesu w metodzie run.
# #     from multiprocessing import Process
# #
# #     class MojProces(Process):
# #         def run(self):
# #             print("Proces działa w metodzie run.")
# #
# #     p = MojProces()
# #     p.start()
# #     p.join()
# #
# #     # Zad. 4. Utwórz klasę bazującą na klasie Process definiując działanie procesu w metodzie run. Dodatkowo niech ten proces zwraca wartość.
# #     from multiprocessing import Process, Queue
# #
# #     class ProcesZWartoscia(Process):
# #         def __init__(self, a, b, kolejka):
# #             super().__init__()
# #             self.a = a
# #             self.b = b
# #             self.kolejka = kolejka
# #
# #         def run(self):
# #             wynik = self.a + self.b
# #             self.kolejka.put(wynik)
# #
# #     q = Queue()
# #     p = ProcesZWartoscia(5, 7, q)
# #     p.start()
# #     p.join()
# #     print("Wynik:", q.get())  # 12
# #
# ###################################
# ###################################
# ###################################
#
# # Zad. 2. Utwórz przykład wieloprocesowy wykorzystujący blokadę Lock.from multiprocessing import Process, Lock
# # import time
# #
# # def drukuj_z_lockiem(lock, komunikat):
# #     with lock:
# #         for _ in range(3):
# #             print(komunikat)
# #             time.sleep(0.1)
# #
# # if __name__ == "__main__":
# #     lock = Lock()
# #     p1 = Process(target=drukuj_z_lockiem, args=(lock, "Proces 1"))
# #     p2 = Process(target=drukuj_z_lockiem, args=(lock, "Proces 2"))
# #     p1.start()
# #     p2.start()
# #     p1.join()
# #     p2.join()
# # Zad. 3. Utwórz przykład wieloprocesowy wykorzystujący blokadę RLock.from multiprocessing import Process, RLock
# # import time
# #
# # def drukuj_z_rlockiem(rlock, n):
# #     with rlock:
# #         print(f"[{n}] Pierwsza blokada")
# #         with rlock:
# #             print(f"[{n}] Druga blokada")
# #             time.sleep(0.1)
# #
# # if __name__ == "__main__":
# #     rlock = RLock()
# #     p1 = Process(target=drukuj_z_rlockiem, args=(rlock, "Proces 1"))
# #     p2 = Process(target=drukuj_z_rlockiem, args=(rlock, "Proces 2"))
# #     p1.start()
# #     p2.start()
# #     p1.join()
# #     p2.join()
# # Zad. 4. Utwórz przykład wieloprocesowy wykorzystujący zmienną Condition.from multiprocessing import Process, Condition
# # import time
# #
# # def czekaj_na_sygnal(condition):
# #     with condition:
# #         print("Proces czeka na sygnał...")
# #         condition.wait()
# #         print("Proces otrzymał sygnał i kontynuuje.")
# #
# # def wyslij_sygnal(condition):
# #     time.sleep(1)
# #     with condition:
# #         print("Wysyłanie sygnału...")
# #         condition.notify()
# #
# # if __name__ == "__main__":
# #     condition = Condition()
# #     p1 = Process(target=czekaj_na_sygnal, args=(condition,))
# #     p2 = Process(target=wyslij_sygnal, args=(condition,))
# #     p1.start()
# #     p2.start()
# #     p1.join()
# #     p2.join()
# # Zad. 5. Utwórz przykład wieloprocesowy wykorzystujący blokadę Semafor.from multiprocessing import Process, Semaphore
# # import time
# # import random
# #
# # def zadanie(semafor, id):
# #     with semafor:
# #         print(f"{id} - wchodzi")
# #         time.sleep(random.uniform(0.5, 1.5))
# #         print(f"{id} - wychodzi")
# #
# # if __name__ == "__main__":
# #     semafor = Semaphore(2)  # tylko 2 procesy mogą jednocześnie działać
# #     procesy = [Process(target=zadanie, args=(semafor, f"Proces {i}")) for i in range(5)]
# #
# #     for p in procesy: p.start()
# #     for p in procesy: p.join()
# # Zad. 6. Utwórz przykład wieloprocesowy wykorzystujący blokadę Event.from multiprocessing import Process, Event
# # import time
# #
# # def czekaj_na_start(event):
# #     print("Czekam na sygnał startu...")
# #     event.wait()
# #     print("Startuję!")
# #
# # if __name__ == "__main__":
# #     event = Event()
# #     p1 = Process(target=czekaj_na_start, args=(event,))
# #     p2 = Process(target=czekaj_na_start, args=(event,))
# #
# #     p1.start()
# #     p2.start()
# #     time.sleep(2)
# #     print("Wysyłam sygnał START")
# #     event.set()
# #
# #     p1.join()
# #     p2.join()
# # Zad. 7. Utwórz przykład wieloprocesowy wykorzystujący blokadę Barrier.from multiprocessing import Process, Barrier
# # import time
# # import random
# #
# # def zadanie(bariera, id):
# #     print(f"{id} - przygotowuję się...")
# #     time.sleep(random.uniform(0.5, 1.5))
# #     print(f"{id} - czeka na innych")
# #     bariera.wait()
# #     print(f"{id} - wszyscy gotowi, zaczynam!")
# #
# # if __name__ == "__main__":
# #     bariera = Barrier(3)
# #     procesy = [Process(target=zadanie, args=(bariera, f"Proces {i}")) for i in range(3)]
# #
# #     for p in procesy: p.start()
# #     for p in procesy: p.join()
#
# #########################
# ########################
# #########################
#
# import os
# from multiprocessing import Pool, cpu_count
#
# # ---- Szukana fraza ----
# SZUKANA_FRAZA = "python"
#
#
# # ---- Funkcja do przeszukiwania pojedynczego pliku ----
# def przeszukaj_plik(ścieżka):
#     try:
#         with open(ścieżka, 'r', encoding='utf-8', errors='ignore') as f:
#             for nr_linii, linia in enumerate(f, 1):
#                 if SZUKANA_FRAZA in linia:
#                     return f"Znaleziono w {ścieżka}, linia {nr_linii}: {linia.strip()}"
#     except Exception as e:
#         return f"Nie można odczytać {ścieżka}: {e}"
#     return None
#
#
# # ---- Pobieranie listy plików z katalogu i podkatalogów ----
# def pobierz_pliki(katalog):
#     pliki = []
#     for root, _, files in os.walk(katalog):
#         for f in files:
#             pełna_ścieżka = os.path.join(root, f)
#             pliki.append(pełna_ścieżka)
#     return pliki
#
#
# # ---- Główna funkcja z użyciem multiprocessing.Pool ----
# def main():
#     katalog = input("Podaj ścieżkę do katalogu: ").strip()
#     pliki = pobierz_pliki(katalog)
#
#     print(f"Przeszukuję {len(pliki)} plików...")
#
#     with Pool(processes=cpu_count()) as pool:
#         wyniki = pool.map(przeszukaj_plik, pliki)
#
#     # Filtruj tylko te, gdzie znaleziono frazę
#     znalezione = list(filter(None, wyniki))
#
#     if znalezione:
#         print("\n--- Wyniki ---")
#         for linia in znalezione:
#             print(linia)
#     else:
#         print("Nie znaleziono frazy w żadnym pliku.")
#
#
# if __name__ == "__main__":
#     main()
#
