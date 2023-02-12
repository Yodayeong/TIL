import java.util.ArrayList;

public class ListsExample {

    public static void main(String[] args) {

        //Lists
        //순서 구분, 중복 허용
        //Vector, ArrayList, LinkedList

        ArrayList<Integer> list = new ArrayList(10);
        //<>를 통해 데이터 타입을 지정할 수도 있음
        list.add(100);
        //list.add("ENFP");

        for (int i = 0; i < list.size(); i++) {
            System.out.println(list.get(i));
        }
    }
}
