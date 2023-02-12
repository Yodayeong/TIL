public class Operators {

    public static void main(String[] args) {

        //산술 연산자
        int a = 10;
        int b = 20;
        String c = "abc";

        double d = 10;
        double e = 20;

        System.out.println(d / e);

        System.out.println(a + b);
        System.out.println(a - b);
        System.out.println(a * b);
        System.out.println(a / b);
        System.out.println(a % b);

        System.out.println(a + c); //모두 string으로 취급


        //비교 연산자
        int x = 5;
        int y = 8;

        System.out.println(x > y);
        System.out.println(x < y);

        System.out.println(x >= y);
        System.out.println(x <= y);

        //= : 대입연산자, == : 비교연산자
        System.out.println(x == y);
        System.out.println(x != y);

        //이때! string은 주소값을 참조하기 때문에 비교연산자 사용 불가


        //논리 연산자
        int variable_1 = 3;
        int variable_2 = 3;
        int variable_3 = 5;

        //AND(&&) - 교집합
        System.out.println(variable_3 > variable_1 && variable_3 > variable_2); //true && true
        System.out.println(variable_3 > variable_1 && variable_3 < variable_2); //true && false

        //OR(||) - 합집합
        System.out.println(variable_3 > variable_1 || variable_3 < variable_2); //true || false

        //NOT(!) - 여집합
        System.out.println(!true);
        System.out.println(!false);


        //대입 연산자
        int temp = 1;
        double price = 12.5;


        //증감 연산자
        System.out.println(temp++); //temp 값을 먼저 인자로 넘겨줘 출력한 후, 증감
        System.out.println(temp);

        System.out.println(++temp); //증감 연산을 먼저 수행하고 값을 인자로 넘겨줌

    }
}