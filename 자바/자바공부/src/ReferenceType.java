public class ReferenceType {

    public static void main(String[] args) {

        //참조형
        //참조형 데이터의 값 => 힙 메모리 영역
        //변수에 대입되는 값 => 힙 메모리 영역의 주소값

        String a = new String("Hello!");
        System.out.println(a);

        String b = "Hello!";
        String c = "Hello!";

        if (a == b) {
            System.out.println("a == b");
            //출력되지 않음 => a와 b의 주소값이 다름
            //힙 메모리에 동일한 데이터가 있건 없건 생성함
        }

        if (b==c) {
            System.out.println("b == c");
            //출력됨 => b와 c의 주소값이 같음
            //힙 메모리 내의 동일한 데이터를 활용하기 위해 주소를 동일하게 가져감
        }

    }
}
