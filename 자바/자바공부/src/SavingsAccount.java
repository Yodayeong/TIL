public class SavingsAccount extends BankAccount implements Withdrawable{
    //부모의 속성을 가지고 시작

    //해당 자식만 가지는 멤버변수와 메서드를 추가
    boolean isOverdraft;
    void transfer() {};
    public void withdraw() {
        //외부에서 가져올 때는 public 접근 제어자 꼭 붙여주기!
        System.out.println("Withdraw");
    };
}
