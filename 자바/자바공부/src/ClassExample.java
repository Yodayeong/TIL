public class ClassExample {

    public static void main(String[] args) {

        BankAccount account = new BankAccount();
        System.out.println(account);
//        System.out.println(account.bankCode);
//        System.out.println(account.isDormant);

//        BankAccount bankAccount = new BankAccount();
//        bankAccount.password = 123456;
//        System.out.println(bankAccount.password);

        BankAccount bankAccount = new BankAccount();
        bankAccount.changePassword(123456);
        System.out.println(bankAccount.password);
    }
}
