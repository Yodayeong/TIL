import java.util.ArrayList;

public class ExceptionExample {

    public static void main(String[] args) {

        //예외(Exceptions)
        //자바에서 예측할 수 있었던 에러

        //example 1.
        //계산 할 수 없는 것을 줌
        int a = 10;
        int b = 0;

        int c = a / b;

        //example 2.
        //범위가 벗어난 것을 참조
        ArrayList arrayList = new ArrayList(3);
        arrayList.get(10);

        //try-catch 구문을 통해 예상되는 에러를 처리함
        ArrayList arrayList1 = new ArrayList(3);
        try {
            arrayList1.get(10);
//            int a = 10;
//            int b = 0;
//            int c = a / b;
        } catch (IndexOutOfBoundsException ioe) {
            //예상되는 에러가 특정할 수도
            System.out.println("IndexOutOfBoundsException 발생");

        } catch (IllegalArgumentException iae) {
            System.out.println("IllegalArgumentException 발생");

        } catch (Exception e) {
            //에러가 발생하면 catch 부분이 동작
            e.printStackTrace(); //에러 관련된 내용이 뜸
            System.out.println("Exception 발생");
        } finally {
            //무조건 실행됨
            System.out.println("finally");
        }

    }
}
