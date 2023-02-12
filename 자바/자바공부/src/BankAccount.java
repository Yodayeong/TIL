public class BankAccount {

    //멤버변수(정적)
    //BankAccount 클래스는 6가지 멤버변수를 가짐
    private int bankCode;
    private int accountNo;
    private String owner;
    private int balance;
    private boolean isDormant;
    private int password;

    //메서드(동적)
    public void inquiry() {}
    public void deposit() {}
    public void withdraw() {}
    public void heldInDormant() {}
    //private => 동일 클래스 안에서만 참조 및 수정 가능
    public void changePassword (int password) {
        this.password = password;
    }

    //생성자
    //클래스 내부에 정의, 생성자 메서드명은 클래스명과 일치!
    //new 연산자와 함께 사용

    //생성자를 직접 만들어주지 않으면, 이처럼 빈 생성자가 생성됨
    //빈 생성자가 필요한 경우에는 아래처럼 직접 만들어주면 됨
    BankAccount() {

    }
    BankAccount (
            int bankCode,
            int accountNo,
            String owner,
            int balance,
            int password,
            boolean isDormant
    ) {
        //this: 인스턴스 자기자신을 가리킴
        this.bankCode = bankCode;
        this.accountNo = accountNo;
        this.owner = owner;
        this.balance = balance;
        this.password = password;
        this.isDormant = isDormant;
    }
}
