# sekcja importowania niezbędnych bibliotek
import random


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
# versja 0.0.1
class NOL:
    def __init__(self, X=None, Y=None, Z=None, szerokosc=None, dludosc=None, waga=None, typ=None,
                 minimalna_predkosc=None, maksymalna_predkosc=None,
                 maksymalne_przeszpisenie=None, powirchnia_projekcyjna=None,
                 odpornosc_na_bron=None,
                 obecnosc_broni=None):
        # domyślnie jednostki miary traktowane są jako jednostki miary układu SI (o podstawie 10^0*JEDNOSTKA jeżeli nie będzie to specjalnie podano inaczej)
        self.X = X  # Położenie odnośnie położenia BP w Prawo
        self.Y = Y  # Położenie odnośnie położenia BP W Lewo
        self.Z = Z  # Położenie odnośnie położenia BP w Góre
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
    def get_all_parameters(self):  # Master geter
        print(f"X: {self.X}")
        print(f"Y: {self.Y}")
        print(f"Z: {self.Z}")
        print(f"Szerokosc: {self.szerokosc}")
        print(f"Dludosc: {self.dludosc}")
        print(f"Waga: {self.waga}")
        print(f"Typ: {self.typ}")
        print(f"Minimalna predkosc: {self.minimalna_predkosc}")
        print(f"Maksymalna predkosc: {self.maksymalna_predkosc}")
        print(f"Maksymalne przeszpisenie: {self.maksymalne_przeszpisenie}")
        print(f"Powirchnia projekcyjna: {self.powirchnia_projekcyjna}")
        print(f"Odpornosc na bron: {self.odpornosc_na_bron}")
        print(f"Obecnosc broni: {self.obecnosc_broni}")

    def get_X(self):
        return self.X

    def get_Y(self):
        return self.Y

    def get_Z(self):
        return self.Z

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
    def set_X(self, value):
        if is_value_integer(value) == True or is_value_float(value) == True:
            self.X = value

    def set_Y(self, value):
        if is_value_integer(value) == True or is_value_float(value) == True:
            self.Y = value

    def set_Z(self, value):
        if is_value_integer(value) == True or is_value_float(value) == True:
            self.Z = value

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


# fukcja do tworzenia zbiorów NOL

def create_list_of_NOL(amount_NOL: int):
    List_of_NOL = []
    if is_value_integer(amount_NOL) and is_value_biger_than_0(amount_NOL) and (
            amount_NOL <= MAX_list_lenhgt_is):  # walidacja typu podawanej zmiennej oraz sprawdzenie czy liczba jest większa od zera        for i in range(0, amount_NOL):
        for a in range(0, amount_NOL):
            List_of_NOL.append(NOL())
        else:
            print("Error in function create_list_of_NOL")
    return List_of_NOL


# funkcja uzupełnienia dannych w objektach klasy NOL w zależności od podanych atrybutów

#wspomagającja funkcja do tworzenia unikalnych osobnych zmiennych:

def generate_unikal_wartosc_od_minus_10000_do_plus_10000():
    used_values = []
    for i in range(0,2):
        value = random.uniform(-10000,10000)
        if value not in used_values:
            used_values.append(value)



def insert_value_to_objekts_in_list_of_NOL(lista_z_objektami_NOL: list):
    if len(lista_z_objektami_NOL) == 0:
        print("Error in function insert_value_to_objekts_in_list_of_NOL")
    else:
        for objekt in lista_z_objektami_NOL:
            objekt.set_X(random.uniform(-100000, 100000))  # dlugość w metrach Wartości nie mogą się powtarazać
            objekt.set_Y(random.uniform(-100000, 100000))
            objekt.set_Z(random.uniform(-100000, 100000))
            objekt.set_szerokosc(random.uniform(0.1, 100))
            objekt.set_dludosc(random.uniform(0.1, 100))
            objekt.set_waga(random.uniform(0.01, 100000))  # waga w kg
            objekt.set_minimalna_predkosc(random.uniform(0, 10000))  # w m/s
            objekt.set_maksymalna_predkosc(1)
            while objekt.get_maksymalna_predkosc() < objekt.get_minimalna_predkosc():
                objekt.set_maksymalna_predkosc(random.uniform(0, 10000))
            objekt.set_odpornosc_na_bron(random.randint(1, 100))
            objekt.set_obecnosc_broni(random.choice([True, False]))
            objekt.set_maksymalne_przeszpisenie(random.uniform(1, 50))  # m/s^2
            objekt.set_powirchnia_projekcyjna(
                (objekt.get_dludosc() * objekt.get_szerokosc()) * random.uniform(0.2, 1))  # m^2


# funkcja do opracowania i symulacji przemieszczenia objektów w przesztrzeni powietrznej dokoła położenia BP które domyszlnie jest ustawione jako położenie X;Y;Z = 0;0;0;

def fukcja_ruchu_NOL(lista_NOL: list):
    # validacja podanej listy
    if len(lista_NOL) > 0:
        if lista_NOL[0].get_X != None:
            print("вяшфф")


# punkt wejśćiowy do programu
if __name__ == "__main__":
    # wstępne testowanie systemu
    # funcja do sprawdzenia maksymalnych możliwośći kompótera w przetwarżaniu dużych zbiorów dannych złaszcia zmiennych typu List z wartościami typu Class
    def test_max_list_size():
        size = 10 ** 6  # начнём с миллиона
        step = 10 ** 2  # шаг увеличения
        while True:
            try:
                test_list = [NOL()] * size
                print(f"Успешно создан список длиной {size}")
                print(test_list)
                size += step
            except MemoryError:
                print(f"ОШИБКА ПАМЯТИ при попытке создать список длиной {size}")
                return size


    MAX_list_lenhgt_is = 10 ** 5
    # MAX_list_lenhgt_is = test_max_list_size()  # Tęn wiersz jest czenścą programu ale polecam go zakomentowac jeżeli nie ma na to beżpośredniego zapotrzebowania ponieważ na niewydajnych kompóterach może potrwać od kilku minut do kilku dni. Kod został dostosowany do braku tego parametru i domuszlnie podejrzewano że maksymalna długość listy to 10**4 składającej z ekzemplarów klasów. Podany program został przetestowany na komputerze z procesorem "Ryzen Threadripper 7980X" + 512Gbt RAM ddr5 RDIMM z ECC sk hyniX i maksymalnie uzyskana wartość to MAX_list_lenhgt_is == 2 012 936 090 biórác pod uwagé że taka metoda nie optymalna ale ma większą precyzyjność i prosta w walidacji. Oczywiście można by było używać bazy dannuch takiej jak SQLite i wtedy zależność od pamięcia operacyjnej nie będzie taka istotna
    list_of_NOL = create_list_of_NOL(MAX_list_lenhgt_is)
    print(list_of_NOL[0].get_all_parameters())
    insert_value_to_objekts_in_list_of_NOL(list_of_NOL)
    for a in list_of_NOL:
        print(a.get_X())
