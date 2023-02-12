public class Variables {

    //변수 => 데이터가 저장되는 공간

    //1. 1개의 변수 => 1개의 값만 할당 가능
    //2. 변수에 저장된 값 => 재할당을 통해 변경 가능
    //3. 값의 형태에 맞는 자료형을 사용
    //4. 변수명은 소문자로 시작
    //5. 대소문자 구분, 공백 포함 불가능
    //6. 자바 예약어 사용 불가

    public static void main(String[] args) {
        int num = 1;
        double width = 12.34;
        String content = "Programming";

        num = 10;
        System.out.println(num);

    }
}
