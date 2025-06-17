import os
import pytest
from main import OsobaNiepelnosprawna, MainLayout


def test_create_entry():
    osoba = OsobaNiepelnosprawna()
    osoba.create("Jan", "Kowalski", "2025-06-15", "08:00", "16:00", "Testowy tekst", "Szablon1")
    data = osoba.read_all()
    assert len(data) == 1
    assert data[0]["imie"] == "Jan"
    assert data[0]["nazwisko"] == "Kowalski"


def test_update_entry():
    osoba = OsobaNiepelnosprawna()
    osoba.create("Jan", "Kowalski", "2025-06-15", "08:00", "16:00", "Test", "Szablon1")
    osoba.update(0, "tekst", "Zmieniony tekst")
    assert osoba.read_all()[0]["tekst"] == "Zmieniony tekst"


def test_delete_entry():
    osoba = OsobaNiepelnosprawna()
    osoba.create("Jan", "Kowalski", "2025-06-15", "08:00", "16:00", "Test", "Szablon1")
    osoba.delete(0)
    assert len(osoba.read_all()) == 0


def test_export_to_xls(tmp_path):
    osoba = OsobaNiepelnosprawna()
    osoba.create("Jan", "Kowalski", "2025-06-15", "08:00", "16:00", "Test", "Szablon1")
    file_path = tmp_path / "raport_test.xls"
    filename = osoba.export_to_xls(filename=str(file_path))
    assert os.path.isfile(filename)
    assert filename == str(file_path)


def test_mainlayout_save_entry():
    layout = MainLayout()
    # заполняем поля вручную
    layout.inputs["imie"].text = "Anna"
    layout.inputs["nazwisko"].text = "Nowak"
    layout.inputs["data"].text = "2025-06-15"
    layout.inputs["czas_start"].text = "09:00"
    layout.inputs["czas_stop"].text = "17:00"
    layout.inputs["tekst"].text = "Testowy wpis"
    layout.inputs["szablon"].text = "Szablon2"

    # симулируем нажатие кнопки сохранить
    layout.save_entry(None)
    data = layout.osoba.read_all()
    assert len(data) == 1
    assert data[0]["imie"] == "Anna"
    assert data[0]["czas_start"] == "09:00"
