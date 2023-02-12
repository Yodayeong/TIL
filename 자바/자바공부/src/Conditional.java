public class Conditional {

    public static void main(String[] args) {

        //if를 활용한 조건문
        int a = 1;
        int b = 100;

        if (a != b) {
            System.out.println("a != b");
        }

        if (a == b) {
            System.out.println("a == b");
        } else {
            System.out.println("else block");
        }

        //다중 조건의 경우, 조건을 만족하는 최초의 분기만 실행
        if (a == b) {
            System.out.println("a == b");
        } else if (a < b) {
            System.out.println("a < b");
        } else if (a <= b) {
            System.out.println("a <= b");
        } else {
            System.out.println("a > b");
        }

        //switch를 활용한 조건문
        int x = 10;

        switch(x + 1) {
            case 11:
                System.out.println("x + 1 == 11");
                break; //조건을 만족한다고 멈추지 않음 => 멈추도록 해줘야함
            case 10:
                System.out.println("x + 1 == 10");
                break;
            case 9:
                System.out.println("x + 1 == 9");
                break;
            default: //아무 조건도 만족하지 않는 경우
                System.out.println("default");
        }
    }
}
