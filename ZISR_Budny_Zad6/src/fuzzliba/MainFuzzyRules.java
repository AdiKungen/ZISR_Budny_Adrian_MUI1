/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package fuzzliba;

import fuzzlib.FuzzySet;
import fuzzlib.creators.OperationCreator;
import fuzzlib.norms.SNorm;
import fuzzlib.norms.TNorm;

/**
 *
 * @author Student
 */
public class MainFuzzyRules {
    public static void main(String[] args) {
    	FuzzySet tempNiska = new FuzzySet();
        FuzzySet tempSrednia = new FuzzySet();
        FuzzySet tempWysoka = new FuzzySet();
        
        tempNiska.addPoint(0.0,  1.0);
        tempNiska.addPoint(10.0, 1.0);
        tempNiska.addPoint(20.0, 0.0);

        tempSrednia.addPoint(10.0, 0.0);
        tempSrednia.addPoint(20.0, 1.0);
        tempSrednia.addPoint(30.0, 0.0);

        tempWysoka.addPoint(20.0, 0.0);
        tempWysoka.addPoint(30.0, 1.0);
        tempWysoka.addPoint(40.0, 1.0);
        
        FuzzySet wilgNiska = new FuzzySet();
        FuzzySet wilgSrednia = new FuzzySet();
        FuzzySet wilgWysoka = new FuzzySet();
        
        wilgNiska.addPoint(0.0,  1.0);
        wilgNiska.addPoint(30.0, 1.0);
        wilgNiska.addPoint(50.0, 0.0);
        
        wilgSrednia.addPoint(30.0, 0.0);
        wilgSrednia.addPoint(50.0, 1.0);
        wilgSrednia.addPoint(70.0, 0.0);

        wilgWysoka.addPoint(50.0, 0.0);
        wilgWysoka.addPoint(70.0, 1.0);
        wilgWysoka.addPoint(100.0, 1.0);
        
        FuzzySet nawNiski = new FuzzySet();
        FuzzySet nawSredni = new FuzzySet();
        FuzzySet nawWysoki = new FuzzySet();
        
        nawNiski.addPoint(0.0,   1.0);
        nawNiski.addPoint(30.0,  1.0);
        nawNiski.addPoint(50.0,  0.0);
        
        nawSredni.addPoint(30.0, 0.0);
        nawSredni.addPoint(50.0, 1.0);
        nawSredni.addPoint(70.0, 0.0);

        nawWysoki.addPoint(50.0,  0.0);
        nawWysoki.addPoint(70.0,  1.0);
        nawWysoki.addPoint(100.0, 1.0);
        
        FuzzySet chlNiskie = new FuzzySet();
        FuzzySet chlSrednie = new FuzzySet();
        FuzzySet chlWysokie = new FuzzySet();
        
        chlNiskie.addPoint(0.0,   1.0);
        chlNiskie.addPoint(30.0,  1.0);
        chlNiskie.addPoint(50.0,  0.0);
        
        chlSrednie.addPoint(30.0, 0.0);
        chlSrednie.addPoint(50.0, 1.0);
        chlSrednie.addPoint(70.0, 0.0);

        chlWysokie.addPoint(50.0,  0.0);
        chlWysokie.addPoint(70.0,  1.0);
        chlWysokie.addPoint(100.0, 1.0);
        
        TNorm t = OperationCreator.newTNorm(TNorm.TN_PRODUCT);
        SNorm s = OperationCreator.newSNorm(SNorm.SN_MAXIMUM);
        
        Double aktTemp = 25.0;
        Double aktWilg = 65.0;
        
        double stopTempNiska = tempNiska.getMembership(aktTemp);
        double stopTempSrednia = tempSrednia.getMembership(aktTemp);
        double stopTempWysoka = tempWysoka.getMembership(aktTemp);
        
        double stopWilgNiska = wilgNiska.getMembership(aktWilg);
        double stopWilgSrednia = wilgSrednia.getMembership(aktWilg);
        double stopWilgWysoka = wilgWysoka.getMembership(aktWilg);
        
        //stopTempWysoka AND stopWilgWysoka => silaChlWysokie, silaNawWysoki
        double r1 = t.calc(stopTempWysoka, stopWilgWysoka);

        //(stopWilgNiska OR stopWilgSrednia) AND stopTempWysoka => silaChlWysokie, silaNawSredni
	    double r2_wilg = s.calc(stopWilgNiska, stopWilgSrednia);
	    double r2 = t.calc(stopTempWysoka, r2_wilg);
	
	    //stopTempSrednia AND stopWilgWysoka => silaChlSrednie, silaNawWysoki
	    double r3 = t.calc(stopTempSrednia, stopWilgWysoka);
	
	    //(stopWilgNiska OR stopWilgSrednia) AND stopTempSrednia => silaChlSrednie, silaNawSredni
	    double r4_wilg = s.calc(stopWilgNiska, stopWilgSrednia);
	    double r4 = t.calc(stopTempSrednia, r4_wilg);
	
	    //stopTempNiska => silaChlNiskie, silaNawNiski
	    double r5 = stopTempNiska;
	
	    double silaChlWysokie = s.calc(r1, r2);
	    double silaChlSrednie = s.calc(r3, r4);
	    double silaChlNiskie = r5;
	
	    double silaNawWysoki = s.calc(r1, r3);
	    double silaNawSredni = s.calc(r2, r4);
	    double silaNawNiski = r5;

        chlNiskie.processSetAndMembershipWithNorm(silaChlNiskie, t);
        chlSrednie.processSetAndMembershipWithNorm(silaChlSrednie, t);
        chlWysokie.processSetAndMembershipWithNorm(silaChlWysokie, t);
        
        FuzzySet wynikChlTemp = new FuzzySet();
        FuzzySet wynikChlFinal = new FuzzySet();
        FuzzySet.processSetsWithNorm(wynikChlTemp, chlNiskie, chlSrednie, s);
        FuzzySet.processSetsWithNorm(wynikChlFinal, wynikChlTemp, chlWysokie, s);

        nawNiski.processSetAndMembershipWithNorm(silaNawNiski, t);
        nawSredni.processSetAndMembershipWithNorm(silaNawSredni, t);
        nawWysoki.processSetAndMembershipWithNorm(silaNawWysoki, t);
        
        FuzzySet wynikNawTemp = new FuzzySet();
        FuzzySet wynikNawFinal = new FuzzySet();
        FuzzySet.processSetsWithNorm(wynikNawTemp, nawNiski, nawSredni, s);
        FuzzySet.processSetsWithNorm(wynikNawFinal, wynikNawTemp, nawWysoki, s);
        
        wynikChlFinal.PackFlatSections();
        wynikNawFinal.PackFlatSections();
        
        double finalChl = wynikChlFinal.DeFuzzyfy();
        double finalNaw = wynikNawFinal.DeFuzzyfy();
        
        System.out.println("Temperatura: " + aktTemp + "C | Wilgotność: " + aktWilg + "%");
        System.out.println("Moc chłodzenia: " + finalChl + "% | Prędkość nawiewu: " + finalNaw + "%");
    }
}
