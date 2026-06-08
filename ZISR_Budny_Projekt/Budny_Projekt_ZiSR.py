import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import tkinter as tk
from tkinter import ttk

def sterownik_pralki():
    waga_ubr = ctrl.Antecedent(np.arange(1, 11, 1), 'waga_ubr')
    poz_zabru = ctrl.Antecedent(np.arange(10, 101, 1), 'poz_zabru')
    deli_tka = ctrl.Antecedent(np.arange(0, 101, 1), 'deli_tka')

    czas_pran = ctrl.Consequent(np.arange(30, 121, 1), 'czas_pran')
    ilosc_deter = ctrl.Consequent(np.arange(20, 151, 1), 'ilosc_deter')
    temp_pran = ctrl.Consequent(np.arange(20, 91, 1), 'temp_pran')

    waga_ubr['lekka'] = fuzz.trimf(waga_ubr.universe, [1, 1, 5])
    waga_ubr['srednia'] = fuzz.trimf(waga_ubr.universe, [2, 5, 8])
    waga_ubr['ciezka'] = fuzz.trimf(waga_ubr.universe, [5, 10, 10])

    poz_zabru['lekki'] = fuzz.trimf(poz_zabru.universe, [10, 10, 50])
    poz_zabru['normalny'] = fuzz.trimf(poz_zabru.universe, [25, 50, 75])
    poz_zabru['mocny'] = fuzz.trimf(poz_zabru.universe, [50, 100, 100])

    deli_tka['niska'] = fuzz.trimf(deli_tka.universe, [0, 0, 50])
    deli_tka['srednia'] = fuzz.trimf(deli_tka.universe, [25, 50, 75])
    deli_tka['wysoka'] = fuzz.trimf(deli_tka.universe, [50, 100, 100])

    czas_pran['krotki'] = fuzz.trimf(czas_pran.universe, [30, 30, 60])
    czas_pran['sredni'] = fuzz.trimf(czas_pran.universe, [40, 60, 90])
    czas_pran['dlugi'] = fuzz.trimf(czas_pran.universe, [70, 120, 120])

    ilosc_deter['mala'] = fuzz.trimf(ilosc_deter.universe, [20, 20, 60])
    ilosc_deter['srednia'] = fuzz.trimf(ilosc_deter.universe, [40, 75, 110])
    ilosc_deter['duza'] = fuzz.trimf(ilosc_deter.universe, [90, 150, 150])

    temp_pran['niska'] = fuzz.trimf(temp_pran.universe, [20, 20, 40])     
    temp_pran['srednia'] = fuzz.trimf(temp_pran.universe, [30, 40, 60])   
    temp_pran['wysoka'] = fuzz.trimf(temp_pran.universe, [50, 60, 90])    

    reguly = [
        ctrl.Rule(deli_tka['wysoka'], (czas_pran['krotki'], ilosc_deter['srednia'], temp_pran['niska'])),
        
        ctrl.Rule(waga_ubr['lekka'] & poz_zabru['lekki'] & deli_tka['srednia'], (czas_pran['krotki'], ilosc_deter['mala'], temp_pran['niska'])),
        ctrl.Rule(waga_ubr['lekka'] & poz_zabru['normalny'] & deli_tka['srednia'], (czas_pran['krotki'], ilosc_deter['srednia'], temp_pran['niska'])), 
        ctrl.Rule(waga_ubr['lekka'] & poz_zabru['mocny'] & deli_tka['srednia'], (czas_pran['sredni'], ilosc_deter['srednia'], temp_pran['srednia'])),  

        ctrl.Rule(waga_ubr['srednia'] & poz_zabru['lekki'] & deli_tka['srednia'], (czas_pran['krotki'], ilosc_deter['mala'], temp_pran['niska'])),     
        ctrl.Rule(waga_ubr['srednia'] & poz_zabru['normalny'] & deli_tka['srednia'], (czas_pran['sredni'], ilosc_deter['srednia'], temp_pran['srednia'])),
        ctrl.Rule(waga_ubr['srednia'] & poz_zabru['mocny'] & deli_tka['srednia'], (czas_pran['sredni'], ilosc_deter['duza'], temp_pran['srednia'])), 

        ctrl.Rule(waga_ubr['ciezka'] & poz_zabru['lekki'] & deli_tka['srednia'], (czas_pran['krotki'], ilosc_deter['srednia'], temp_pran['srednia'])),
        ctrl.Rule(waga_ubr['ciezka'] & poz_zabru['normalny'] & deli_tka['srednia'], (czas_pran['sredni'], ilosc_deter['duza'], temp_pran['srednia'])),
        ctrl.Rule(waga_ubr['ciezka'] & poz_zabru['mocny'] & deli_tka['srednia'], (czas_pran['dlugi'], ilosc_deter['duza'], temp_pran['srednia'])),

        ctrl.Rule(waga_ubr['lekka'] & poz_zabru['lekki'] & deli_tka['niska'], (czas_pran['krotki'], ilosc_deter['mala'], temp_pran['niska'])),
        ctrl.Rule(waga_ubr['lekka'] & poz_zabru['normalny'] & deli_tka['niska'], (czas_pran['krotki'], ilosc_deter['srednia'], temp_pran['srednia'])),
        ctrl.Rule(waga_ubr['lekka'] & poz_zabru['mocny'] & deli_tka['niska'], (czas_pran['sredni'], ilosc_deter['srednia'], temp_pran['wysoka'])),
        
        ctrl.Rule(waga_ubr['srednia'] & poz_zabru['lekki'] & deli_tka['niska'], (czas_pran['krotki'], ilosc_deter['mala'], temp_pran['srednia'])),
        ctrl.Rule(waga_ubr['srednia'] & poz_zabru['normalny'] & deli_tka['niska'], (czas_pran['sredni'], ilosc_deter['srednia'], temp_pran['srednia'])),
        ctrl.Rule(waga_ubr['srednia'] & poz_zabru['mocny'] & deli_tka['niska'], (czas_pran['dlugi'], ilosc_deter['duza'], temp_pran['wysoka'])),
        
        ctrl.Rule(waga_ubr['ciezka'] & poz_zabru['lekki'] & deli_tka['niska'], (czas_pran['sredni'], ilosc_deter['srednia'], temp_pran['srednia'])),
        ctrl.Rule(waga_ubr['ciezka'] & poz_zabru['normalny'] & deli_tka['niska'], (czas_pran['dlugi'], ilosc_deter['duza'], temp_pran['srednia'])),
        ctrl.Rule(waga_ubr['ciezka'] & poz_zabru['mocny'] & deli_tka['niska'], (czas_pran['dlugi'], ilosc_deter['duza'], temp_pran['wysoka'])) 
    ]

    system = ctrl.ControlSystem(reguly)
    return ctrl.ControlSystemSimulation(system)

symulator = sterownik_pralki()

def oblicz_rozmycie(event=None):
    zm_waga_ubr = slider_waga_ubr.get()
    zm_poz_zabru = slider_poz_zabru.get()
    zm_deli_tka = slider_deli_tka.get()
    
    symulator.input['waga_ubr'] = zm_waga_ubr
    symulator.input['poz_zabru'] = zm_poz_zabru
    symulator.input['deli_tka'] = zm_deli_tka
    
    symulator.compute()
    
    lbl_wynik_czas_pran.config(text=f"{symulator.output['czas_pran']:.1f} min")
    lbl_wynik_ilosc_deter.config(text=f"{symulator.output['ilosc_deter']:.1f} ml")
    lbl_wynik_temp_pran.config(text=f"{symulator.output['temp_pran']:.1f} °C")

root = tk.Tk()
root.title("Sterownik rozmyty - Inteligentna pralka")
root.geometry("420x450")
root.configure(padx=20, pady=20)

style = ttk.Style()
style.configure("TLabel", font=("Arial", 12))

ttk.Label(root, text="Waga ubrań (kg):", font=("Arial", 10, "bold")).pack(anchor="w")
slider_waga_ubr = tk.Scale(root, from_=1, to=10, resolution=0.5, orient="horizontal", length=370, command=oblicz_rozmycie)
slider_waga_ubr.set(5.0)
slider_waga_ubr.pack()

ttk.Label(root, text="Poziom zabrudzenia (%):", font=("Arial", 10, "bold")).pack(anchor="w", pady=(10, 0))
slider_poz_zabru = tk.Scale(root, from_=10, to=100, resolution=1, orient="horizontal", length=370, command=oblicz_rozmycie)
slider_poz_zabru.set(50.0)
slider_poz_zabru.pack()

ttk.Label(root, text="Delikatność tkanin (%):", font=("Arial", 10, "bold")).pack(anchor="w", pady=(10, 0))
slider_deli_tka = tk.Scale(root, from_=0, to=100, resolution=1, orient="horizontal", length=370, command=oblicz_rozmycie)
slider_deli_tka.set(20.0)
slider_deli_tka.pack()

ttk.Separator(root, orient="horizontal").pack(fill="x", pady=20)

frame_wyniki = ttk.Frame(root)
frame_wyniki.pack(fill="x")

ttk.Label(frame_wyniki, text="Czas prania:").grid(row=0, column=0, sticky="w", pady=5)
lbl_wynik_czas_pran = ttk.Label(frame_wyniki, text="0.0 min", font=("Arial", 12, "bold"), foreground="blue")
lbl_wynik_czas_pran.grid(row=0, column=1, sticky="e")

ttk.Label(frame_wyniki, text="Ilość detergentu:").grid(row=1, column=0, sticky="w", pady=5)
lbl_wynik_ilosc_deter = ttk.Label(frame_wyniki, text="0.0 ml", font=("Arial", 12, "bold"), foreground="blue")
lbl_wynik_ilosc_deter.grid(row=1, column=1, sticky="e")

ttk.Label(frame_wyniki, text="Temperatura prania:").grid(row=2, column=0, sticky="w", pady=5)
lbl_wynik_temp_pran = ttk.Label(frame_wyniki, text="0.0 °C", font=("Arial", 12, "bold"), foreground="blue")
lbl_wynik_temp_pran.grid(row=2, column=1, sticky="e")

frame_wyniki.columnconfigure(1, weight=1)

oblicz_rozmycie()
root.mainloop()