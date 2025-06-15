# main.py

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
import pandas as pd
from datetime import datetime


class OsobaNiepelnosprawna:
    def __init__(self):
        self.data = []

    def create(self, imie, nazwisko, data, czas_start, czas_stop, tekst, szablon):
        osoba = {
            "imie": imie,
            "nazwisko": nazwisko,
            "data": data,
            "czas_start": czas_start,
            "czas_stop": czas_stop,
            "tekst": tekst,
            "szablon": szablon
        }
        self.data.append(osoba)

    def read_all(self):
        return self.data

    def update(self, index, field, value):
        if index < len(self.data) and field in self.data[index]:
            self.data[index][field] = value

    def delete(self, index):
        if index < len(self.data):
            del self.data[index]

    def export_to_xls(self, filename="raport.xls"):
        df = pd.DataFrame(self.data)
        df.to_excel(filename, index=False)
        return filename


class MainLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.osoba = OsobaNiepelnosprawna()

        self.inputs = {}
        fields = ["imie", "nazwisko", "data", "czas_start", "czas_stop", "tekst", "szablon"]
        for field in fields:
            self.add_widget(Label(text=field.capitalize()))
            inp = TextInput(multiline=False)
            self.inputs[field] = inp
            self.add_widget(inp)

        self.time_button = Button(text="Rejestruj czas (Start/Stop)")
        self.time_button.bind(on_press=self.open_time_popup)
        self.add_widget(self.time_button)

        self.submit_button = Button(text="Dodaj wpis")
        self.submit_button.bind(on_press=self.save_entry)
        self.add_widget(self.submit_button)

        self.export_button = Button(text="Eksportuj do XLS")
        self.export_button.bind(on_press=self.export_data)
        self.add_widget(self.export_button)

        self.output = Label(text="")
        self.add_widget(self.output)

        # Вызов Popup'а сразу при запуске
        self.show_person_selection_popup()

    def save_entry(self, instance):
        entry = {key: self.inputs[key].text for key in self.inputs}
        self.osoba.create(**entry)
        self.output.text = "Zapisano wpis."
        for inp in self.inputs.values():
            inp.text = ""

    def export_data(self, instance):
        filename = self.osoba.export_to_xls()
        self.output.text = f"Wyeksportowano do pliku: {filename}"

    def open_time_popup(self, instance):
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        info_label = Label(text="Kliknij Start lub Stop aby ustawić czas")
        layout.add_widget(info_label)

        start_button = Button(text="Start")
        stop_button = Button(text="Stop")

        layout.add_widget(start_button)
        layout.add_widget(stop_button)

        popup = Popup(title="Rejestracja czasu", content=layout,
                      size_hint=(0.8, 0.5), auto_dismiss=True)

        def set_start_time(btn):
            now = datetime.now()
            self.inputs["czas_start"].text = now.strftime("%H:%M:%S")
            self.inputs["data"].text = now.strftime("%Y-%m-%d")
            popup.dismiss()

        def set_stop_time(btn):
            now = datetime.now()
            self.inputs["czas_stop"].text = now.strftime("%H:%M:%S")
            self.inputs["data"].text = now.strftime("%Y-%m-%d")
            popup.dismiss()

        start_button.bind(on_press=set_start_time)
        stop_button.bind(on_press=set_stop_time)

        popup.open()

    def show_person_selection_popup(self):
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        imie_input = TextInput(hint_text="Imię", multiline=False)
        nazwisko_input = TextInput(hint_text="Nazwisko", multiline=False)
        confirm_button = Button(text="Zatwierdź")

        layout.add_widget(Label(text="Wybierz osobę"))
        layout.add_widget(imie_input)
        layout.add_widget(nazwisko_input)
        layout.add_widget(confirm_button)

        popup = Popup(title="Wybór osoby", content=layout,
                      size_hint=(0.8, 0.5), auto_dismiss=False)

        def confirm_selection(instance):
            imie = imie_input.text.strip()
            nazwisko = nazwisko_input.text.strip()
            if imie and nazwisko:
                self.inputs["imie"].text = imie
                self.inputs["nazwisko"].text = nazwisko
                popup.dismiss()

        confirm_button.bind(on_press=confirm_selection)
        popup.open()


class CaritasApp(App):
    def build(self):
        return MainLayout()


if __name__ == "__main__":
    CaritasApp().run()
