public class ArraysExmample {

    public static void main(String[] args) {

        //배열(Arrays)

        int[] price = {10000, 9000, 4000, 7000};
        String[] mbti = {"INFP", "ENFP", "ISTJ", "ESTP"};

        System.out.println(price[0]);
        System.out.println(mbti[1]);

        price[1] = 8000;
        mbti[1] = "ENTP";
        System.out.println(price[1]);
        System.out.println(mbti[1]);

        System.out.println(price); //객체의 주소가 출력됨

        System.out.println(mbti.length);

        for (int i = 0; i < mbti.length; i++) {
            System.out.println(mbti[i]);
        }
    }
}
