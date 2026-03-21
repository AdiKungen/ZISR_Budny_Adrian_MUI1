package fuzzyset;

public class Main {
	
    public static void main(String[] args) {
    	double x = 6.7;
    	double y = 3.1;
    	double z = 4.7;
    	double v = 1.5;
    	
        FuzzySet gauss1 = new GaussianFuzzySet(5, 0.35);
        FuzzySet gauss2 = new GaussianFuzzySet(3.4, 0.38);
        FuzzySet gauss3 = new GaussianFuzzySet(1.5, 0.17);
        FuzzySet gauss4 = new GaussianFuzzySet(0.2, 0.1);
        
        FuzzySet gauss5 = new GaussianFuzzySet(5.9, 0.51);
        FuzzySet gauss6 = new GaussianFuzzySet(2.8, 0.31);
        FuzzySet gauss7 = new GaussianFuzzySet(4.35, 0.47);
        FuzzySet gauss8 = new GaussianFuzzySet(1.3, 0.20);
        
        FuzzySet gauss9 = new GaussianFuzzySet(6.5, 0.63);
        FuzzySet gauss10 = new GaussianFuzzySet(3, 0.32);
        FuzzySet gauss11 = new GaussianFuzzySet(5.55, 0.55);
        FuzzySet gauss12 = new GaussianFuzzySet(2, 0.27);
        
        double pset = gauss1.getMembership(x) + gauss2.getMembership(y) + gauss3.getMembership(z) + gauss4.getMembership(v);
        double pver = gauss5.getMembership(x) + gauss6.getMembership(y) + gauss7.getMembership(z) + gauss8.getMembership(v);
        double pvir = gauss9.getMembership(x) + gauss10.getMembership(y) + gauss11.getMembership(z) + gauss12.getMembership(v);
        
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