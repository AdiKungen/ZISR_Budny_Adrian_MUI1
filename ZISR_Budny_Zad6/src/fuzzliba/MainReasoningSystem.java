package fuzzliba;

import fuzzlib.DefuzMethod;
import fuzzlib.FuzzySet;
import fuzzlib.norms.*;
import fuzzlib.reasoning.ReasoningSystem;
import fuzzlib.reasoning.SystemConfig;

public class MainReasoningSystem {
	
	private static final long serialVersionUID = 1L;

    public static void main(String[] args) {

        FuzzySet tempNiska = new FuzzySet("t_niska", "");
        FuzzySet tempSrednia = new FuzzySet("t_srednia", "");
        FuzzySet tempWysoka = new FuzzySet("t_wysoka", "");
        
        tempNiska.addPoint(0.0,  1.0);
        tempNiska.addPoint(10.0, 1.0);
        tempNiska.addPoint(20.0, 0.0);

        tempSrednia.addPoint(10.0, 0.0);
        tempSrednia.addPoint(20.0, 1.0);
        tempSrednia.addPoint(30.0, 0.0);

        tempWysoka.addPoint(20.0, 0.0);
        tempWysoka.addPoint(30.0, 1.0);
        tempWysoka.addPoint(40.0, 1.0);
        
        FuzzySet wilgNiska = new FuzzySet("w_niska", "");
        FuzzySet wilgSrednia = new FuzzySet("w_srednia", "");
        FuzzySet wilgWysoka = new FuzzySet("w_wysoka", "");
        
        wilgNiska.addPoint(0.0,  1.0);
        wilgNiska.addPoint(30.0, 1.0);
        wilgNiska.addPoint(50.0, 0.0);

        wilgSrednia.addPoint(30.0, 0.0);
        wilgSrednia.addPoint(50.0, 1.0);
        wilgSrednia.addPoint(70.0, 0.0);

        wilgWysoka.addPoint(50.0, 0.0);
        wilgWysoka.addPoint(70.0, 1.0);
        wilgWysoka.addPoint(100.0, 1.0);
        
        FuzzySet chlNiskie = new FuzzySet("ch_niskie", "");
        FuzzySet chlSrednie = new FuzzySet("ch_srednie", "");
        FuzzySet chlWysokie = new FuzzySet("ch_wysokie", "");
        
        chlNiskie.addPoint(0.0,   1.0);
        chlNiskie.addPoint(30.0,  1.0);
        chlNiskie.addPoint(50.0,  0.0);
        
        chlSrednie.addPoint(30.0, 0.0);
        chlSrednie.addPoint(50.0, 1.0);
        chlSrednie.addPoint(70.0, 0.0);

        chlWysokie.addPoint(50.0,  0.0); 
        chlWysokie.addPoint(70.0,  1.0);
        chlWysokie.addPoint(100.0, 1.0);
        
        FuzzySet nawNiski = new FuzzySet("n_niski", "");
        FuzzySet nawSredni = new FuzzySet("n_sredni", "");
        FuzzySet nawWysoki = new FuzzySet("n_wysoki", "");
        
        nawNiski.addPoint(0.0,   1.0);
        nawNiski.addPoint(30.0,  1.0);
        nawNiski.addPoint(50.0,  0.0); 

        nawSredni.addPoint(30.0, 0.0);
        nawSredni.addPoint(50.0, 1.0);
        nawSredni.addPoint(70.0, 0.0);

        nawWysoki.addPoint(50.0,  0.0); 
        nawWysoki.addPoint(70.0,  1.0);
        nawWysoki.addPoint(100.0, 1.0);

        SystemConfig config = new SystemConfig();
        config.setInputWidth(2);
        config.setOutputWidth(2);
        config.setNumberOfPremiseSets(6);
        config.setNumberOfConclusionSets(6);

        config.setIsOperationType(TNorm.TN_PRODUCT);
        config.setAndOperationType(TNorm.TN_MINIMUM);
        config.setOrOperationType(SNorm.SN_PROBABSUM); 
        config.setImplicationType(TNorm.TN_MINIMUM);
        config.setConclusionAgregationType(SNorm.SN_PROBABSUM);
        config.setTruthCompositionType(TNorm.TN_MINIMUM);
        config.setAutoDefuzzyfication(false);
        config.setDefuzzyfication(DefuzMethod.DF_COG); 
        config.setAutoAlpha(true);
        config.setTruthPrecision(0.001, 0.0001);

        ReasoningSystem klim = new ReasoningSystem(config);

        klim.getInputVar(0).id = "temp";
        klim.getInputVar(1).id = "wilg";
        klim.getOutputVar(0).id = "chl";
        klim.getOutputVar(1).id = "naw";

        klim.addPremiseSet(tempNiska);
        klim.addPremiseSet(tempSrednia);
        klim.addPremiseSet(tempWysoka);
        
        klim.addPremiseSet(wilgNiska);
        klim.addPremiseSet(wilgSrednia);
        klim.addPremiseSet(wilgWysoka);

        klim.addConclusionSet(chlNiskie);
        klim.addConclusionSet(chlSrednie);
        klim.addConclusionSet(chlWysokie);
        
        klim.addConclusionSet(nawNiski);
        klim.addConclusionSet(nawSredni);
        klim.addConclusionSet(nawWysoki);

        try {
            klim.addRule(1, 1);
            klim.addRuleItem("temp", "t_niska", "AND", "wilg", "w_niska");
            klim.addRuleConclusion("chl", "ch_niskie");
            klim.addRule(1, 1);
            klim.addRuleItem("temp", "t_niska", "AND", "wilg", "w_niska");
            klim.addRuleConclusion("naw", "n_niski");

            klim.addRule(1, 1);
            klim.addRuleItem("temp", "t_niska", "AND", "wilg", "w_srednia");
            klim.addRuleConclusion("chl", "ch_niskie");
            klim.addRule(1, 1);
            klim.addRuleItem("temp", "t_niska", "AND", "wilg", "w_srednia");
            klim.addRuleConclusion("naw", "n_niski");

            klim.addRule(1, 1);
            klim.addRuleItem("temp", "t_niska", "AND", "wilg", "w_wysoka");
            klim.addRuleConclusion("chl", "ch_niskie");
            klim.addRule(1, 1);
            klim.addRuleItem("temp", "t_niska", "AND", "wilg", "w_wysoka");
            klim.addRuleConclusion("naw", "n_niski");

            klim.addRule(1, 1);
            klim.addRuleItem("temp", "t_srednia", "AND", "wilg", "w_niska");
            klim.addRuleConclusion("chl", "ch_srednie");
            klim.addRule(1, 1);
            klim.addRuleItem("temp", "t_srednia", "AND", "wilg", "w_niska");
            klim.addRuleConclusion("naw", "n_sredni");

            klim.addRule(1, 1);
            klim.addRuleItem("temp", "t_srednia", "AND", "wilg", "w_srednia");
            klim.addRuleConclusion("chl", "ch_srednie");
            klim.addRule(1, 1);
            klim.addRuleItem("temp", "t_srednia", "AND", "wilg", "w_srednia");
            klim.addRuleConclusion("naw", "n_sredni");

            klim.addRule(1, 1);
            klim.addRuleItem("temp", "t_srednia", "AND", "wilg", "w_wysoka");
            klim.addRuleConclusion("chl", "ch_srednie");
            klim.addRule(1, 1);
            klim.addRuleItem("temp", "t_srednia", "AND", "wilg", "w_wysoka");
            klim.addRuleConclusion("naw", "n_wysoki");

            klim.addRule(1, 1);
            klim.addRuleItem("temp", "t_wysoka", "AND", "wilg", "w_niska");
            klim.addRuleConclusion("chl", "ch_wysokie");
            klim.addRule(1, 1);
            klim.addRuleItem("temp", "t_wysoka", "AND", "wilg", "w_niska");
            klim.addRuleConclusion("naw", "n_sredni");

            klim.addRule(1, 1);
            klim.addRuleItem("temp", "t_wysoka", "AND", "wilg", "w_srednia");
            klim.addRuleConclusion("chl", "ch_wysokie");
            klim.addRule(1, 1);
            klim.addRuleItem("temp", "t_wysoka", "AND", "wilg", "w_srednia");
            klim.addRuleConclusion("naw", "n_sredni");

            klim.addRule(1, 1);
            klim.addRuleItem("temp", "t_wysoka", "AND", "wilg", "w_wysoka");
            klim.addRuleConclusion("chl", "ch_wysokie");
            klim.addRule(1, 1);
            klim.addRuleItem("temp", "t_wysoka", "AND", "wilg", "w_wysoka");
            klim.addRuleConclusion("naw", "n_wysoki");

        } catch (Exception e) {
            e.printStackTrace();
        }
        
        double aktTemp = 25.0;
        double aktWilg = 65.0;
        
        klim.setInput(0, aktTemp); 
        klim.setInput(1, aktWilg); 
        
        klim.Process();

        double mocChl = klim.getOutputVar(0).outset.DeFuzzyfy();
        double mocNaw = klim.getOutputVar(1).outset.DeFuzzyfy();

        System.out.println("Temperatura: " + aktTemp + "C | Wilgotność: " + aktWilg + "%");
        System.out.println("Moc chłodzenia: " + mocChl + "% | Prędkość nawiewu: " + mocNaw + "%");
    }
}
