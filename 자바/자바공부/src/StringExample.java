public class StringExample {

    public static void main(String[] args) {

        //String => 문자열 객체
        //객체 => 힙 메모리 영역
        //변수 => 힙 메모리 영역의 주소

        String str_1 = "안녕하세요!"; //문자열 리터럴
        String str_2 = new String("안녕하세요!"); //생성자
        String str_3 = "안녕하세요!";

        //주소값을 비교
        if (str_1 == str_2) {
            System.out.println("str1 == str2");
        }

        if (str_1 == str_3) {
            System.out.println("str1 == str3");
        }

        if (str_2 == str_3) {
            System.out.println("str2 == str3");
        }

        //내용 자체를 비교
        if (str_1.equals(str_2)) {
            System.out.println("str_1.equals(str_2)");
        }

        if (str_1.equals(str_3)) {
            System.out.println("str_1.equals(str_3)");
        }

        if (str_2.equals(str_3)) {
            System.out.println("str_2.equals(str_3)");
        }

        //문자열 병합

        //1. '+' 연산자
        String str1 = "Hello,";
        String str2 = "World!";

        System.out.println(str1 + " " + str2);

        //2. StringBuilder
        StringBuilder strBdr_1 = new StringBuilder("Hello,");

        strBdr_1.append(" ");
        strBdr_1.append("World!");

        String str_new = strBdr_1.toString();

        System.out.println(str_new);

        //문자열 슬라이스
        String string_1 = "이름: 김자바";
        System.out.println(string_1.indexOf("이"));
        System.out.println(string_1.indexOf("름"));

        String str_name = string_1.substring(4, 7);
        System.out.println(str_name);

        //문자열 대소문자 반환
        String string_2 = "abc";
        String string_3 = "ABC";

        string_2 = string_2.toUpperCase();
        string_3 = string_3.toLowerCase();

        System.out.println(string_2);
        System.out.println(string_3);

        if (string_2.equals(string_3)) {
            System.out.println("string_2.equals(string_3)");
        }

        if (string_2.equalsIgnoreCase(string_3)) {
            //대소문자를 무시하고 값을 비교
            System.out.println("(string_2.equalsIgnoreCase(string_3))");
        }

        //공백 제거

        //1. 양쪽 끝 공백
        String str_ex1 = "  Hello   ";
        str_ex1 = str_ex1.trim();
        System.out.println(str_ex1);

        //2. 문자열 중간 공백
        String str_ex2 = "  Hel lo  ";
        str_ex2 = str_ex2.replace(" ", "");
        System.out.println(str_ex2);
    }
}
