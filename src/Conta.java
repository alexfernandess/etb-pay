public class Conta {
    private int numero;
    private double saldo;
    private Cliente cliente; // Composição: A conta "tem" uma pessoa

    // Construtor
    public Conta(int numero, Cliente cliente) {
        this.numero = numero;
        this.cliente = cliente;
        this.saldo = 0.0; // Toda conta nasce zerada
    }

    // Getters e Setters
    public int getNumero() {
        return numero;
    }

    public void setNumero(int numero) {
        this.numero = numero;
    }

    public double getSaldo() {
        return saldo;
    }
    // Note: Não criamos setSaldo por segurança, o saldo mudará via métodos de
    // negócio

    public Cliente getCliente() {
        return cliente;
    }

    public void setCliente(Cliente cliente) {
        this.cliente = cliente;
    }
}