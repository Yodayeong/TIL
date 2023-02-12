import java.util.HashMap;

public class MapsExample {

    public static void main(String[] args) {

        //Map
        //키-값 쌍을 요소로 가지는 데이터의 모음, 순서 구분 없음
        //키는 중복 불가, 값은 중복 허용
        //HashMap

        HashMap<String, String> map = new HashMap();
        //HashMap도 <>를 통해 데이터 타입 지정 가능
        map.put("age", "23");
        map.put("mbti", "ENTP");
        map.put("name", "여다영");

        System.out.println(map.get("age"));
        System.out.println(map.get("mbti"));
        System.out.println(map.get("name"));
    }
}
