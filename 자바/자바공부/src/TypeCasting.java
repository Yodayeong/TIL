public class TypeCasting {

    public static void main(String[] args) {

        //형변환
        //byte < short < int < long <<< float < double

        //강제 형변환
        int a = 128;
        short b = (short) a;
        byte c = (byte) a;

        System.out.println(a);
        System.out.println(b);
        System.out.println(c); //-128 출력 => overflow 발생

        //자동 형변환
        short x = 10;
        int y = x;

        System.out.println(x);
        System.out.println(y);

        int m = 80;
        double n = m;

        System.out.println(m);
        System.out.println(n);

        double d = 10.33124546435;
        float e = (float) d;

        System.out.println(d);
        System.out.println(e);

        int f = 10;
        short g = 20;

        short h = (short) (f + g);
        System.out.println(h);
    }
}
