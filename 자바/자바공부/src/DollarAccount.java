public class DollarAccount extends BankAccount {

    //오버로딩 => 부모 클래스에서 상속받은 메서드에서 파라미터를 변경
    //새로운 메서드 정의!
    void inquiry(double currencyRate) {}

    //오버라이딩 => 부모 클래스에서 상속받은 메서드의 내용 변경
    //자식 클래스의 상황에 맞게
    void deposit() {
        //파라미터가 아니라 중괄호 부분을 변경하는 것임!
    }
}
