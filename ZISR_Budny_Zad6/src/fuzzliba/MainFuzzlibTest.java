/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package fuzzliba;

import fuzzlib.FuzzySet;
import fuzzlib.creators.OperationCreator;
import fuzzlib.norms.Norm;
import fuzzlib.norms.SNorm;
import fuzzlib.norms.TNMin;
import fuzzlib.norms.TNorm;

/**
 *
 * @author Student
 */
public class MainFuzzlibTest {
    
     public static void main(String[] args) {
     	double x = 6.7;
     	double y = 3.1;
     	double z = 4.7;
     	double v = 1.5;
         
         FuzzySet fs1 = new FuzzySet();
         FuzzySet fs2 = new FuzzySet();
         FuzzySet fs3 = new FuzzySet();
         FuzzySet fs4 = new FuzzySet();
         
         fs1.newGaussian(5, 0.35);
         fs2.newGaussian(3.4, 0.38);
         fs3.newGaussian(1.5, 0.17);
         fs4.newGaussian(0.2, 0.1);
         
         Norm op = OperationCreator.newTNorm(TNorm.TN_MINIMUM);
         
         double pset1 = op.calc(fs1.getMembership(x), fs2.getMembership(y));
         double pset2 = op.calc(fs3.getMembership(z), fs4.getMembership(v));
         double pset = op.calc(pset1, pset2);
         
         FuzzySet fs5 = new FuzzySet();
         FuzzySet fs6 = new FuzzySet();
         FuzzySet fs7 = new FuzzySet();
         FuzzySet fs8 = new FuzzySet();
         
         fs5.newGaussian(5.9, 0.51);
         fs6.newGaussian(2.8, 0.31);
         fs7.newGaussian(4.35, 0.47);
         fs8.newGaussian(1.3, 0.20);
         
         double pver1 = op.calc(fs5.getMembership(x), fs6.getMembership(y));
         double pver2 = op.calc(fs7.getMembership(z), fs8.getMembership(v));
         double pver = op.calc(pver1, pver2);
         
         FuzzySet fs9 = new FuzzySet();
         FuzzySet fs10 = new FuzzySet();
         FuzzySet fs11 = new FuzzySet();
         FuzzySet fs12 = new FuzzySet();
         
         fs9.newGaussian(6.5, 0.63);
         fs10.newGaussian(3, 0.32);
         fs11.newGaussian(5.55, 0.55);
         fs12.newGaussian(2, 0.27);
         
         double pvir1 = op.calc(fs9.getMembership(x), fs10.getMembership(y));
         double pvir2 = op.calc(fs11.getMembership(z), fs12.getMembership(v));
         double pvir = op.calc(pvir1, pvir2);
         
         if(pset > pver && pset > pvir) {
         	System.out.println("Wybrany irys to Setosa");
         } else if(pver > pvir) {
         	System.out.println("Wybrany irys to Versicolor");
         } else {
         	System.out.println("Wybrany irys to Virginica");
         }
         
         System.out.println("Iris-setosa: " + pset + " | Iris-versicolor: " + pver + " | Iris-virginica: " + pvir);
     }
}
