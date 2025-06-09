# sekcja importowania niezbędnych bibliotek
import random
import multiprocessing
import math
import time


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
                 minimalna_predkosc=None, maksymalna_predkosc=None, maksymalne_przeszpisenie=None,
                 powirchnia_projekcyjna=None, odpornosc_na_bron=None, obecnosc_broni=None):
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

class BP:
    def __init__(self, predkosc_puli, ilosc_strszaluw_na_sekunde, ilosc_pul_w_magazynie, czas_naladowania_magazynu, kierunek_X, kierunek_Y, kierunek_Z, predkosc_porusznia):
        #bazując na najbardziej rozpowszechnionym modelu BP instalowanym na okrętcie wójskowym "phalanx CIWS (Block 1b)" z niego wżęto patanetry BP
        self.predkosc_puli = 1100 #m/s
        self.ilosc_strszaluw_na_sekunde = 4000 #strsz/s
        self.ilosc_pul_w_magazynie = 2000
        self.czas_naladowania_magazynu = 5 #sekund
        #początkowy kierunek lufy działa będzie pionowo w góre
        self.kierunek_X = 0
        self.kierunek_Y = 0
        self.kierunek_Z = 0
        #maksymalna prędkość z którą może obracać BP woków siebie
        self.predkosc_porusznia = 100 #stopień/s       czyli za 3.6 sekundy BP zrobi pełny obrót woków śiebie w pożiomie. Zakładam że prędkość obrotowa w poziomie rówma pędkości w pionie.
# fukcja do tworzenia zbiorów NOL

def funkcja_wyszukiwania_najblizszego_objektu_odnosnie_polozenia_BP(lista_NOL_po_sortowaniu_na_osobne_procesy,number_of_thread : int):
    robocza_lista = lista_NOL_po_sortowaniu_na_osobne_procesy[number_of_thread]
    closest_object = None
    min_distance = float('inf')  # Начинаем с бесконечно большого расстояния

    for obj in robocza_lista:
        # Вычисляем расстояние до точки (0, 0, 0)
        distance = math.sqrt(obj.X ** 2 + obj.Y ** 2 + obj.Z ** 2)

        # Если нашли объект ближе — обновляем
        if distance < min_distance:
            min_distance = distance
            closest_object = obj
    # print(f"Najbliższy objekt do punktu X=0 Y=0 Z=0 to {closest_object} który ma parametry: X={closest_object.X} Y={closest_object.Y} Z={closest_object.Z}")
    return closest_object

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

# wspomagającja funkcja do tworzenia unikalnych osobnych zmiennych w wyznaczonym zakresie:

def generate_unikal_wartosc_od_minus_10000_do_plus_10000(amount: int):
    used_values = []
    for i in range(0, amount):
        value = random.uniform(-10000, 10000)
        if value not in used_values:
            used_values.append(value)
    return used_values


def insert_value_to_objekts_in_list_of_NOL(lista_z_objektami_NOL: list):
    if len(lista_z_objektami_NOL) == 0:
        print("Error in function insert_value_to_objekts_in_list_of_NOL")
    else:
        lista_zkiennych_X = generate_unikal_wartosc_od_minus_10000_do_plus_10000(len(lista_z_objektami_NOL))
        lista_zmiennych_Y = generate_unikal_wartosc_od_minus_10000_do_plus_10000(len(lista_z_objektami_NOL))
        lista_zmiennych_Z = generate_unikal_wartosc_od_minus_10000_do_plus_10000(len(lista_z_objektami_NOL))
        for objekt in lista_z_objektami_NOL:
            objekt.set_X(lista_zkiennych_X[-1])  # dlugość w metrach. Wartości nie mogą się powtarazać
            lista_zkiennych_X.pop(-1)
            # print(len(lista_zkiennych_X)) #debag string print
            objekt.set_Y(lista_zmiennych_Y[-1])  # dlugość w metrach. Wartości nie mogą się powtarazać
            lista_zmiennych_Y.pop(-1)
            objekt.set_Z(lista_zmiennych_Z[-1])  # dlugość w metrach. Wartości nie mogą się powtarazać
            lista_zmiennych_Z.pop(-1)
            objekt.set_szerokosc(random.uniform(0.1, 100))
            objekt.set_dludosc(random.uniform(0.1, 100))
            objekt.set_waga(random.uniform(0.01, 100000))  # waga w kg
            objekt.set_minimalna_predkosc(random.uniform(0, 10))  # w m/s
            objekt.set_maksymalna_predkosc(1)
            while objekt.get_maksymalna_predkosc() < objekt.get_minimalna_predkosc():
                objekt.set_maksymalna_predkosc(random.uniform(0, 10000))
            objekt.set_odpornosc_na_bron(random.randint(1, 100))
            objekt.set_obecnosc_broni(random.choice([True, False]))
            objekt.set_maksymalne_przeszpisenie(random.uniform(1, 50))  # m/s^2
            objekt.set_powirchnia_projekcyjna(
                (objekt.get_dludosc() * objekt.get_szerokosc()) * random.uniform(0.2, 1))  # m^2


# funkcja do opracowania i symulacji przemieszczenia objektów w przesztrzeni powietrznej dokoła położenia BP które domyszlnie jest ustawione jako położenie X;Y;Z = 0;0;0;

def fukcja_ruchu_NOL(
        lista_NOL: list):  # funkcja jest obliczona tak że liczy zmiane położenia o co 0.1s w zależności od parametrów NOL
    # validacja podanej listy
    if len(lista_NOL) > 0:
        for valid_index in range(0, len(lista_NOL)):
            if lista_NOL[valid_index].get_X() == None:
                print("objekt w lista nie ma podanej wartośći X")
            if lista_NOL[valid_index].get_Y() == None:
                print("objekt w lista nie ma podanej wartośći Y")
            if lista_NOL[valid_index].get_Z() == None:
                print("objekt w lista nie ma podanej wartośći Z")
                # debug print
                # print(lista_NOL[valid_index].get_all_parameters())
    else:
        print("Error in function fukcja_ruchu_NOL")

    def Zmiana_poolozenia():
        # funkcja zmiany położenia NOL w przedziale 0.1s
        for objekt in lista_NOL:
            differense_X = objekt.get_X()
            objekt.set_X(objekt.get_X() + (objekt.get_minimalna_predkosc() + (
                    (objekt.get_maksymalne_przeszpisenie() * random.uniform(0, 1)) / 10)))
            print(f"Parametr X dla objektu: {objekt} zmieniono z {differense_X} na {objekt.get_X()} ")
            # differense_Y = objekt.get_Y()
            objekt.set_Y(objekt.get_Y() + (objekt.get_minimalna_predkosc() + (
                    (objekt.get_maksymalne_przeszpisenie() * random.uniform(0, 1)) / 10)))
            # print(f"Parametr Y dla objektu: {objekt} zmieniono z {differense_Y} na {objekt.get_Y()} ")
            # differense_Z = objekt.get_Z()
            objekt.set_Z(objekt.get_Z() + (objekt.get_minimalna_predkosc() + (
                    (objekt.get_maksymalne_przeszpisenie() * random.uniform(0, 1)) / 10)))
            # print(f"Parametr Z dla objektu: {objekt} zmieniono z {differense_Z} na {objekt.get_Z()} ")

    interval = 0.1  # 100 ms Dyskretny odztęp czasowy w celu unikęcia chazardu i niezawidnośći sprszętu fizycznego. Wiem że ten przedział przeba zrobić jaknajmniejszy w celu uliepszenia działania systemu i zbliżenia go do systemu analogowego.
    next_time = time.time()

    while True:
        Zmiana_poolozenia()
        next_time += interval
        sleep_time = next_time - time.time()
        if sleep_time > 0:
            time.sleep(sleep_time)
        else:
            # technizny print w celu wyłapywania niezdołności systemu z powodu nieoptymalizcji lub nizkiej częstotliwości taktowania procesora.
            print("Timer stracono")
            next_time = time.time()


# funkcja analizy NOL i przypisanie typu do NOL. Klasyfikator będzie bardzo prosty i będzie klasyfikował tylko na 2 typy "dobry" "NIE dobry". Nie będzie
def funkcja_analizy_i_przypisywanie_typu_do_ekzemplarow_objektow_w_zbiorze_NOL(objekt):
    if objekt.get_powirchnia_projekcyjna() <= 15 or objekt.get_obecnosc_broni() == False:
        objekt.set_typ("dobry")
        # print(objekt.get_typ())
    else:
        objekt.set_typ("NIE dobry")
        # print(objekt.get_typ())


# funkcja do wypisywania przedziałów dla podania jako parametry w nastempnych funkcjach
def seperate_list_of_NOL(my_list: list, threads: int):
    k, m = divmod(len(my_list), threads)
    return [my_list[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in range(threads)]


# funkcja do testowania z dużym obczążeniem


def cpu_stress_task(i):
    print(f"Process {i} started")
    while True:
        math.sqrt(i ** 2 + time.time() % 1000)


def run_stress_test_V2(delay_between_processes=0.1):
    multiprocessing.set_start_method("spawn", force=True)
    max_processes = 0
    processes = []

    try:
        while True:
            p = multiprocessing.Process(target=cpu_stress_task, args=(max_processes,))
            p.start()
            processes.append(p)
            max_processes += 1
            time.sleep(delay_between_processes)
    except Exception as e:
        print(f"\n❌ Error was on proces number: #{max_processes}: {e}")

    print(f"\n✅ Max amount of awailable proceses in the same time is: {max_processes}")

    for p in processes:
        p.terminate()
    return max_processes


# punkt wejśćiowy do programu
if __name__ == "__main__":

    # sektor wstępnego testowania systemu i ustawienie odpowiednich ustawień wieluwątkowości oraz parametrów skomlikowaności zbiorów
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


    # funkcja do badania ilości możliwych jednocześnie pracezdatnych wątków w systemie
    # Użycie wieluwątkowego programowania (P_U02 , P_U04)
    def test_max_thread_in_system_V1():  # funcja dla sprawdzenia bardzo łatwych procesów potrzebujączych niestotną ilość fizycznych zasobów
        import threading
        import time

        def test_task(i):
            print(f"Thread {i} started")
            time.sleep(1)
            print(f"Thread {i} finished")

        max_threads = 0
        threads = []

        try:
            while True:
                t = threading.Thread(target=test_task, args=(max_threads,))
                t.start()
                threads.append(t)
                max_threads += 1
        except Exception as e:
            print(f"Ошибка при запуске потока #{max_threads}: {e}")

        # Подождём завершения всех потоков
        for t in threads:
            t.join()

        print(f"Максимальное количество потоков перед сбоем: {max_threads}")
        return max_threads


    # sektor badania systemu
    # MAX_list_lenhgt_is = test_max_list_size()  # Tęn wiersz jest czenścą programu ale polecam go zakomentowac jeżeli nie ma na to beżpośredniego zapotrzebowania ponieważ na niewydajnych kompóterach może potrwać od kilku minut do kilku dni. Kod został dostosowany do braku tego parametru i domuszlnie podejrzewano że maksymalna długość listy to 10**4 składającej z ekzemplarów klasów. Podany program został przetestowany na komputerze z procesorem "Ryzen Threadripper 7980X" + 512Gbt RAM ddr5 RDIMM z ECC sk hyniX OC Windows Server i maksymalnie uzyskana wartość to MAX_list_lenhgt_is == 2 012 936 090 biórác pod uwagé że taka metoda nie optymalna ale ma większą precyzyjność i prostsza w walidacji. Oczywiście można by było używać bazy dannuch takiej jak SQLite i wtedy zależność od pamięcia operacyjnej nie będzie taka istotna
    # MAX_threads_in_sysytem_V1 = test_max_thread_in_system_V1()
    # MAX_threads_in_sysytem_V2 = run_stress_test_V2() # Tęn wiersz jest czenścą programu ale polecam go zakomentowac jeżeli nie ma na to beżpośredniego zapotrzebowania ponieważ na niewydajnych kompóterach może potrwać od kilku minut do kilku dni. Kod został dostosowany do braku tego parametru i domuszlnie podejrzewano że maksymalna ilość procesów może być od 15 do 20. Podany program został przetestowany na komputerze z procesorem "Ryzen Threadripper 7980X" + 512Gbt RAM ddr5 RDIMM z ECC sk hyniX OC Windows Server i maksymalnie uzyskana wartość to MMAX_threads_in_sysytem_V2 == 45 407 biórác pod uwagé że taka metoda nie optymalna i wydajność zmiejsza po uzyskaniu 128 procesów ponieważ processor ma 128 osobnych wątków pozostałe procesy są wykonywane przez przerywanie z użyciem "infinity fabrik" AMD(r).
    MAX_threads_in_sysytem_V2 = 20
    MAX_threads_in_sysytem_V1 = 20
    MAX_list_lenhgt_is = 2000
    print(f"Maksymalna dugość listy NOL: {MAX_list_lenhgt_is}")
    MAX_threads_in_sysytem = min(MAX_threads_in_sysytem_V1, MAX_threads_in_sysytem_V2)
    print(f"Maksymalna ilość osobnych wątków dostempnych w obecnie używanym systemie: {MAX_threads_in_sysytem}")

    # początek programu
    LIST_OF_NOL = create_list_of_NOL(
        MAX_list_lenhgt_is)  # DUŻY NAPIS ZMIENNEJ ZBIORU EKZEMPLARÓW KLASY NOL OZANCZA ŻE TO GŁÓWNA KLASA NAD KTÓRĄ BĘDĄ PRZEPROWADZANA OPERACJE
    insert_value_to_objekts_in_list_of_NOL(
        LIST_OF_NOL)  # losowe podanie parametrów w pewnych przedziałach wyznaczonych wychodząc z założeń logichnych i ogrwaniczeń szwiata rzeczywistego.
    print(LIST_OF_NOL)
    for objekt in LIST_OF_NOL:  # pętla do przypisywania typu do objektów
        funkcja_analizy_i_przypisywanie_typu_do_ekzemplarow_objektow_w_zbiorze_NOL(objekt)
    print(f"ilość objektów przed sortowaniem = {len(LIST_OF_NOL)}")
    for objekt in LIST_OF_NOL:  # pętla do usuwania "dobrych" NOL żeby zostały tylko NOLSZ
        if objekt.get_typ() == "dobry":
            LIST_OF_NOL.remove(objekt)
    print(f"ilość objektów po usunięciu \"dobrych\" objektów = {len(LIST_OF_NOL)}")

    SEPARATED_LIST_OF_NOL = seperate_list_of_NOL(LIST_OF_NOL, MAX_threads_in_sysytem)

    print(
        f"LISTA_OF_NOL została podzielona na {MAX_threads_in_sysytem} przedziałów w każdym jest +-{len(SEPARATED_LIST_OF_NOL[0])} objektów ")

    # Lista_aktywnych_procesow = []
    # for number_of_thread in range(0, MAX_threads_in_sysytem):
    #     proces = multiprocessing.Process(target=fukcja_ruchu_NOL, args=(SEPARATED_LIST_OF_NOL[number_of_thread],))
    #     Lista_aktywnych_procesow.append(proces)
    #     proces.start()
    #     print(f"proces number {number_of_thread}, z PID = {proces.pid} was started now")
    #
    # time.sleep(60)
    # for p in Lista_aktywnych_procesow:
    #     print(f"Proces zakonczono PID={p.pid}")
    #     p.terminate()
    #     p.join()
