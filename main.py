# sekcja importowania niezbędnych bibliotek

# sekcja ręcznie stwożonych funcij do walidacji
def is_value_integer(wartosc_do_sprawdzenia):
    if isinstance(wartosc_do_sprawdzenia, int):
        return True
    else:
        return False


def is_value_string(wartosc_do_sprawdzenia):
    if isinstance(wartosc_do_sprawdzenia, str):
        return True
    else:
        return False


def is_value_boolean(wartosc_do_sprawdzenia):
    if isinstance(wartosc_do_sprawdzenia, bool):
        return True
    else:
        return False


def is_value_float(wartosc_do_sprawdzenia):
    if isinstance(wartosc_do_sprawdzenia, float):
        return True
    else:
        return False


def is_value_biger_than_0(wartosc_do_sprawdzenia):
    if is_value_float(wartosc_do_sprawdzenia) == True or is_value_integer(wartosc_do_sprawdzenia) == True:
        if wartosc_do_sprawdzenia > 0:
            return True
    else:
        return False


def is_value_str_and_lengh_of_value_more_than_1_character(wartosc_do_sprawdzenia):
    if is_value_string(wartosc_do_sprawdzenia):
        if any(c.isalpha() for c in wartosc_do_sprawdzenia):
            return True
    else:
        return False


# tworzenie klasa NOL z konstruktorem, walidacją, geterami i setereami
#versja 0.0.1
class NOL:
    def __init__(self, szerokosc=None, dludosc=None, waga=None, typ=None,
                 minimalna_predkosc=None, maksymalna_predkosc=None,
                 maksymalne_przeszpisenie=None, powirchnia_projekcyjna=None,
                 odpornosc_na_bron=None,
                 obecnosc_broni=None):
        # domyślnie jednostki miary traktowane są jako jednostki miary układu SI (o podstawie 10^0*JEDNOSTKA jeżeli nie będzie to specjalnie podano inaczej)
        self.szerokosc = szerokosc  # szerokość OL
        self.dludosc = dludosc  # dludosc OL
        self.waga = waga  # waga OL
        self.typ = typ  # typ
        self.minimalna_predkosc = minimalna_predkosc  # minimalna_predkosc
        self.maksymalna_predkosc = maksymalna_predkosc  # maksymalna_predkosc
        self.maksymalne_przeszpisenie = maksymalne_przeszpisenie  # maksymalne_prztszpisenie
        self.powirchnia_projekcyjna = powirchnia_projekcyjna  # powirchnia_projekcyjna obliczana w odniesziniu do pozycji BP
        self.odpornosc_na_bron = odpornosc_na_bron  # odpornosc_na_bron to liczba całkowita wskazująca na ilość sztrałoł którą może wytrzymać przed uszkodzeniem krytycznym czyli zniszczeniem. Analog miary życia NOL
        self.obecnosc_broni = obecnosc_broni  # obecnosc_broni na NOL

    # getery z funkcjonalnością (opcjonalnie)
    def get_szerokosc(self):
        return self.szerokosc

    def get_dludosc(self):
        return self.dludosc

    def get_waga(self):
        return self.waga

    def get_typ(self):
        return self.typ

    def get_minimalna_predkosc(self):
        return self.minimalna_predkosc

    def get_maksymalna_predkosc(self):
        return self.maksymalna_predkosc

    def get_maksymalne_przeszpisenie(self):
        return self.maksymalne_przeszpisenie

    def get_powirchnia_projekcyjna(self):
        return self.powirchnia_projekcyjna

    def get_odpornosc_na_bron(self):
        return self.odpornosc_na_bron

    def get_obecnosc_broni(self):
        return self.obecnosc_broni

    # setery z walidacją(opcjonalnie)
    def set_szerokosc(self, value):  # wymiary długośći będą podawane w 10^1*mm czyli w cantymetrach
        if (is_value_integer(value) == True or is_value_float(value) == True) and is_value_biger_than_0(value) == True:
            self.szerokosc = value
        else:
            print("Error in function set_szerokosc")

    def set_dludosc(self, value):  # wymiary długośći będą podawane w 10^1*mm czyli w cantymetrach
        if (is_value_integer(value) == True or is_value_float(value) == True) and is_value_biger_than_0(value) == True:
            self.dludosc = value
        else:
            print("Error in function set_dludosc")

    def set_waga(self, value):  # waga będzie podawana w 10^3*gr czyli w kilogramach
        if (is_value_integer(value) == True or is_value_float(value) == True) and is_value_biger_than_0(value) == True:
            self.waga = value
        else:
            print("Error in function set_waga")

    def set_typ(self,
                value):  # typy NOL będą tworzone dynamicznie i będą przedstawione jako wartość string w której będzie zapisano krótki opis NOL z minimum 1j litery
        if is_value_str_and_lengh_of_value_more_than_1_character(value):
            self.typ = value
        else:
            print("Error in function set_typ")

    def set_minimalna_predkosc(self, value):
        if (is_value_integer(value) == True or is_value_float(value) == True) and is_value_biger_than_0(value) == True:
            self.minimalna_predkosc = value
        else:
            print("Error in function set_minimalna_predkosc")

    def set_maksymalna_predkosc(self, value):
        if (is_value_integer(value) == True or is_value_float(value) == True) and is_value_biger_than_0(value) == True:
            self.maksymalna_predkosc = value
        else:
            print("Error in function set_maksymalna_predkosc")

    def set_maksymalne_przeszpisenie(self, value):
        if (is_value_integer(value) == True or is_value_float(value) == True) and is_value_biger_than_0(value) == True:
            self.maksymalne_przeszpisenie = value
        else:
            print("Error in function set_maksymalne_przeszpisenie")

    def set_powirchnia_projekcyjna(self, value):
        if (is_value_integer(value) == True or is_value_float(value) == True) and is_value_biger_than_0(value) == True:
            self.powirchnia_projekcyjna = value
        else:
            print("Error in function set_powirchnia_projekcyjna")

    def set_odpornosc_na_bron(self, value):
        if is_value_integer(value) == True and (value <= 100):
            self.odpornosc_na_bron = value
        else:
            print("Error in function set_odpornosc_na_bron")

    def set_obecnosc_broni(self, value):
        if is_value_boolean(value):
            self.obecnosc_broni = value
        else:
            print("Error in function set_obecnosc_broni")


# punkt wejśćiowy do programu
if __name__ == "__main__":
    NOL1 = NOL(
        szerokosc=5,
        dludosc=5,
    )
    #test
    #test2
