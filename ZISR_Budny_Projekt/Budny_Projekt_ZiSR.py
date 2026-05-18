import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

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
        ctrl.Rule(waga_ubr['lekka'] & poz_zabru['normalny'], (czas_pran['sredni'], ilosc_deter['srednia'], moc_wirow['srednia'])),
        ctrl.Rule(waga_ubr['lekka'] & poz_zabru['mocny'], (czas_pran['dlugi'], ilosc_deter['duza'], moc_wirow['srednia'])),
        
        ctrl.Rule(waga_ubr['srednia'] & poz_zabru['lekki'], (czas_pran['krotki'], ilosc_deter['srednia'], moc_wirow['srednia'])),
        ctrl.Rule(waga_ubr['srednia'] & poz_zabru['normalny'], (czas_pran['sredni'], ilosc_deter['srednia'], moc_wirow['srednia'])),
        ctrl.Rule(waga_ubr['srednia'] & poz_zabru['mocny'], (czas_pran['dlugi'], ilosc_deter['duza'], moc_wirow['szybka'])),
        
        ctrl.Rule(waga_ubr['ciezka'] & poz_zabru['lekki'], (czas_pran['sredni'], ilosc_deter['srednia'], moc_wirow['srednia'])),
        ctrl.Rule(waga_ubr['ciezka'] & poz_zabru['normalny'], (czas_pran['dlugi'], ilosc_deter['duza'], moc_wirow['szybka'])),
        ctrl.Rule(waga_ubr['ciezka'] & poz_zabru['mocny'], (czas_pran['dlugi'], ilosc_deter['duza'], moc_wirow['szybka']))
    ]

    system = ctrl.ControlSystem(reguly)
    return ctrl.ControlSystemSimulation(system)

if __name__ == "__main__":
    symulator = sterownik_pralki()

    zm_waga_ubr = 4.5
    zm_poz_zabru = 60.0
    
    symulator.input['waga_ubr'] = zm_waga_ubr
    symulator.input['poz_zabru'] = zm_poz_zabru
    
    symulator.compute()

    print("Dane wejściowe:")
    print(f"Waga ubrań: {zm_waga_ubr:.1f} kg")
    print(f"Poziom zabrudzenia: {zm_poz_zabru:.1f} %")
    print("")
    print("Dane wyjściowe:")
    print(f"Czas prania: {symulator.output['czas_pran']:.1f} min")
    print(f"Ilość detergentu: {symulator.output['ilosc_deter']:.1f} ml")
    print(f"Moc wirowania: {symulator.output['moc_wirow']:.0f} RPM")