import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import tkinter as tk
from tkinter import ttk

def sterownik_pralki():
    waga_ubr = ctrl.Antecedent(np.arange(1, 11, 1), 'waga_ubr')
    poz_zabru = ctrl.Antecedent(np.arange(10, 101, 1), 'poz_zabru')

    czas_pran = ctrl.Consequent(np.arange(30, 121, 1), 'czas_pran')
    ilosc_deter = ctrl.Consequent(np.arange(20, 151, 1), 'ilosc_deter')
    moc_wirow = ctrl.Consequent(np.arange(400, 1201, 1), 'moc_wirow')

    waga_ubr['lekka'] = fuzz.trimf(waga_ubr.universe, [1, 1, 5])
    waga_ubr['srednia'] = fuzz.trimf(waga_ubr.universe, [2, 5, 8])
    waga_ubr['ciezka'] = fuzz.trimf(waga_ubr.universe, [5, 10, 10])

    poz_zabru['lekki'] = fuzz.trimf(poz_zabru.universe, [10, 10, 50])
    poz_zabru['normalny'] = fuzz.trimf(poz_zabru.universe, [25, 50, 75])
    poz_zabru['mocny'] = fuzz.trimf(poz_zabru.universe, [50, 100, 100])

    czas_pran['krotki'] = fuzz.trimf(czas_pran.universe, [30, 30, 60])
    czas_pran['sredni'] = fuzz.trimf(czas_pran.universe, [40, 60, 90])
    czas_pran['dlugi'] = fuzz.trimf(czas_pran.universe, [70, 120, 120])

    ilosc_deter['mala'] = fuzz.trimf(ilosc_deter.universe, [20, 20, 60])
    ilosc_deter['srednia'] = fuzz.trimf(ilosc_deter.universe, [40, 75, 110])
    ilosc_deter['duza'] = fuzz.trimf(ilosc_deter.universe, [90, 150, 150])

    moc_wirow['wolna'] = fuzz.trimf(moc_wirow.universe, [400, 400, 800])
    moc_wirow['srednia'] = fuzz.trimf(moc_wirow.universe, [600, 800, 1000])
    moc_wirow['szybka'] = fuzz.trimf(moc_wirow.universe, [800, 1200, 1200])

    reguly = [
        ctrl.Rule(waga_ubr['lekka'] & poz_zabru['lekki'], (czas_pran['krotki'], ilosc_deter['mala'], moc_wirow['wolna'])),
        ctrl.Rule(waga_ubr['lekka'] & poz_zabru['normalny'], (czas_pran['krotki'], ilosc_deter['srednia'], moc_wirow['wolna'])),
        ctrl.Rule(waga_ubr['lekka'] & poz_zabru['mocny'], (czas_pran['sredni'], ilosc_deter['srednia'], moc_wirow['srednia'])),
        
        ctrl.Rule(waga_ubr['srednia'] & poz_zabru['lekki'], (czas_pran['krotki'], ilosc_deter['mala'], moc_wirow['srednia'])),
        ctrl.Rule(waga_ubr['srednia'] & poz_zabru['normalny'], (czas_pran['sredni'], ilosc_deter['srednia'], moc_wirow['srednia'])),
        ctrl.Rule(waga_ubr['srednia'] & poz_zabru['mocny'], (czas_pran['sredni'], ilosc_deter['duza'], moc_wirow['szybka'])),
        
        ctrl.Rule(waga_ubr['ciezka'] & poz_zabru['lekki'], (czas_pran['sredni'], ilosc_deter['srednia'], moc_wirow['srednia'])),
        ctrl.Rule(waga_ubr['ciezka'] & poz_zabru['normalny'], (czas_pran['sredni'], ilosc_deter['duza'], moc_wirow['szybka'])),
        ctrl.Rule(waga_ubr['ciezka'] & poz_zabru['mocny'], (czas_pran['dlugi'], ilosc_deter['duza'], moc_wirow['szybka']))
    ]

    system = ctrl.ControlSystem(reguly)
    return ctrl.ControlSystemSimulation(system)

symulator = sterownik_pralki()

def oblicz_rozmycie(event=None):
    zm_waga_ubr = slider_waga_ubr.get()
    zm_poz_zabru = slider_poz_zabru.get()
    
    symulator.input['waga_ubr'] = zm_waga_ubr
    symulator.input['poz_zabru'] = zm_poz_zabru
    symulator.compute()
    
    lbl_wynik_czas_pran.config(text=f"{symulator.output['czas_pran']:.1f} min")
    lbl_wynik_ilosc_deter.config(text=f"{symulator.output['ilosc_deter']:.1f} ml")
    lbl_wynik_moc_wirow.config(text=f"{symulator.output['moc_wirow']:.0f} RPM")

root = tk.Tk()
root.title("Sterownik rozmyty - Inteligenta pralka")
root.geometry("400x350")
root.configure(padx=20, pady=20)

style = ttk.Style()
style.configure("TLabel", font=("Arial", 12))

ttk.Label(root, text="Waga ubrań (kg):", font=("Arial", 10, "bold")).pack(anchor="w")
slider_waga_ubr = tk.Scale(root, from_=0.5, to=10, resolution=0.5, orient="horizontal", length=350, command=oblicz_rozmycie)
slider_waga_ubr.set(5.0)
slider_waga_ubr.pack()

ttk.Label(root, text="Poziom zabrudzenia (%):", font=("Arial", 10, "bold")).pack(anchor="w", pady=(10, 0))
slider_poz_zabru = tk.Scale(root, from_=1, to=100, resolution=1, orient="horizontal", length=350, command=oblicz_rozmycie)
slider_poz_zabru.set(50.0)
slider_poz_zabru.pack()

ttk.Separator(root, orient="horizontal").pack(fill="x", pady=20)

frame_wyniki = ttk.Frame(root)
frame_wyniki.pack(fill="x")

ttk.Label(frame_wyniki, text="Czas prania:").grid(row=0, column=0, sticky="w", pady=5)
lbl_wynik_czas_pran = ttk.Label(frame_wyniki, text="0.0 min", font=("Arial", 12, "bold"), foreground="blue")
lbl_wynik_czas_pran.grid(row=0, column=1, sticky="e")

ttk.Label(frame_wyniki, text="Ilość detergentu:").grid(row=1, column=0, sticky="w", pady=5)
lbl_wynik_ilosc_deter = ttk.Label(frame_wyniki, text="0.0 ml", font=("Arial", 12, "bold"), foreground="blue")
lbl_wynik_ilosc_deter.grid(row=1, column=1, sticky="e")

ttk.Label(frame_wyniki, text="Moc wirowania:").grid(row=2, column=0, sticky="w", pady=5)
lbl_wynik_moc_wirow = ttk.Label(frame_wyniki, text="0 RPM", font=("Arial", 12, "bold"), foreground="blue")
lbl_wynik_moc_wirow.grid(row=2, column=1, sticky="e")

frame_wyniki.columnconfigure(1, weight=1)

oblicz_rozmycie()
root.mainloop()