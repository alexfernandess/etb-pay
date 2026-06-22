public class Conta {

    // CORREÇÃO: Campos alterados para private para respeitar as regras de encapsulamento
    private int idConta;
    private String numeroConta;
    private String tipoConta;
    private double saldo;
    private int idCliente;

    // Construtor vazio
    public Conta() {
    }

    public Conta(String numeroConta, String tipoConta, int idCliente) {
        this.numeroConta = numeroConta;
        this.tipoConta = tipoConta;
        this.saldo = 0.0;
        this.idCliente = idCliente;
    }

    // CORREÇÃO: Métodos Getters e Setters adicionados para acesso seguro
    public int getIdConta() {
        return idConta;
    }

    public void setIdConta(int idConta) {
        this.idConta = idConta;
    }

    public String getNumeroConta() {
        return numeroConta;
    }

    public void setNumeroConta(String numeroConta) {
        this.numeroConta = numeroConta;
    }

    public String getTipoConta() {
        return tipoConta;
    }

    public void setTipoConta(String tipoConta) {
        this.tipoConta = tipoConta;
    }

    public double getSaldo() {
        return saldo;
    }

    public void setSaldo(double saldo) {
        this.saldo = saldo;
    }

    public int getIdCliente() {
        return idCliente;
    }

    public void setIdCliente(int idCliente) {
        this.idCliente = idCliente;
    }
}