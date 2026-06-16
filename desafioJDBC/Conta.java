public class Conta {

    // Encapsulamento
    // Getters e Setters
    public int idConta;
    public String numeroConta;
    public String tipoConta;
    public double saldo;
    public int idCliente;

    // Construtor vazio
    public Conta() {
    }

    public Conta(String numeroConta, String tipoConta, int idCliente) {
        this.numeroConta = numeroConta;
        this.tipoConta = tipoConta;
        this.saldo = 0.0;
        this.idCliente = idCliente;
    }
}