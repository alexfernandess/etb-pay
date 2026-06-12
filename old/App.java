public class App {
    public static void main(String[] args) {

        // 0. Testar Conexão com Banco de Dados
        System.out.println("========================================");
        System.out.println("   VERIFICANDO CONEXÃO COM BANCO...    ");
        System.out.println("========================================");
        ConexaoDB.testarConexao();
        System.out.println();

        // 1. Instanciando um novo Cliente (O dono da conta)
        Cliente alunoETB = new Cliente("Alex Alves", "123.456.789-00", "alex@etb.com.br");

        // 2. Instanciando a Conta (Passando o objeto cliente como titular)
        // O construtor da Conta exige um número e um objeto do tipo Cliente
        Conta contaEstudo = new Conta(2026, alunoETB);

        // 3. Exibindo os dados no terminal
        System.out.println("========================================");
        System.out.println("        SISTEMA ETB-PAY: RELATÓRIO      ");
        System.out.println("========================================");

        // Note a Navegação de Objetos: conta -> titular -> nome
        System.out.println("Titular da Conta: " + contaEstudo.getCliente().getNome());
        System.out.println("Saldo Inicial: R$ " + contaEstudo.getSaldo());

        System.out.println("========================================");

        // 4. Fechar conexão
        ConexaoDB.desconectar();
    }
}