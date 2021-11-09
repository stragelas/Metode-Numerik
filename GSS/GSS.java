public class GSS {
    public static void main(String[] args) {
        
        double x_lower = 0;
        double x_upper = 6;

        double x1 = 0;
        double x2 = 0;

        final double k = 0.61803;

        System.out.println();
        for (int i = 0; i < 5; i++) {
            double d = k * (x_upper - x_lower);
            x1 = x_lower + d;
            x2 = x_upper - d;

            double fx1 = 5 + 6 * (x1 - 3) * (x1 - 3);
            double fx2 = 5 + 6 * (x2 - 3) * (x2 - 3);

            if (fx1 <= fx2) {
                x_lower = x2;
            }else{
                x_upper = x1;
            }
            System.out.println("----- Iterasi ke - "+(i+1)+" -----\n");
            System.out.println("D       = "+d);
            System.out.println("X lower = "+x_lower);
            System.out.println("X upper = "+x_upper);
            System.out.println("X1      = "+x1);
            System.out.println("X2      = "+x2);
            System.out.println("Fx1     = "+fx1);
            System.out.println("Fx2     = "+fx2);
            System.out.println();
        }
    }
}