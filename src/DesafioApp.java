public class DesafioApp {
    public static void main(String[] args) {
        System.out.println("========================================");
        System.out.println("     INICIALIZANDO MOTOR ETB-PAY       ");
        System.out.println("========================================");

        // 1. Conectar e testar conexão com o banco de dados SQLite
        ConexaoDB.testarConexao();

        // 2. Instanciar ClienteDAO
        ClienteDAO clienteDAO = new ClienteDAO();

        // 3. Criar um novo cliente para homologação (CPF deve ter exatamente 11 dígitos numéricos)
        Cliente cliente = new Cliente("Alex Fernandes", "12345678901", "alex.fernandes@etb.com");

        // 4. Inserir o cliente no banco de dados via DAO
        System.out.println("\nCadastrando cliente no banco de dados...");
        boolean sucesso = clienteDAO.inserir(cliente);

        if (sucesso) {
            System.out.println("✓ Cliente cadastrado com sucesso!");
        } else {
            System.out.println("✗ Falha ao cadastrar cliente (verifique se o CPF já existe ou as restrições da tabela).");
        }

        // 5. Criar conta para o cliente cadastrado
        Conta conta = new Conta(2026, cliente);

        // 6. Exibir relatório do sistema
        System.out.println("\n========================================");
        System.out.println("        RELATÓRIO DE INICIALIZAÇÃO      ");
        System.out.println("========================================");
        System.out.println("Titular da Conta: " + conta.getCliente().getNome());
        System.out.println("CPF: " + conta.getCliente().getCpf());
        System.out.println("E-mail: " + conta.getCliente().getEmail());
        System.out.println("Número da Conta: " + conta.getNumero());
        System.out.println("Saldo Inicial: R$ " + conta.getSaldo());
        System.out.println("========================================");

        // 7. Desconectar do banco de dados
        ConexaoDB.desconectar();
    }
}
