import java.sql.*;

public class ConexaoDB {
    private static final String URL = "jdbc:sqlite:ETBPay.db";
    private static Connection conexao;

    // Conectar ao banco de dados
    public static Connection conectar() {
        try {
            Class.forName("org.sqlite.JDBC");
            conexao = DriverManager.getConnection(URL);
            System.out.println("✓ Conexão com o banco de dados estabelecida com sucesso!");
            return conexao;
        } catch (ClassNotFoundException e) {
            System.err.println("✗ Driver SQLite não encontrado: " + e.getMessage());
            return null;
        } catch (SQLException e) {
            System.err.println("✗ Erro ao conectar ao banco de dados: " + e.getMessage());
            return null;
        }
    }

    // Obter conexão ativa
    public static Connection getConexao() {
        if (conexao == null) {
            conectar();
        }
        return conexao;
    }

    // Verificar se a conexão está ok
    public static boolean isConectado() {
        try {
            return conexao != null && !conexao.isClosed();
        } catch (SQLException e) {
            return false;
        }
    }

    // Desconectar
    public static void desconectar() {
        try {
            if (conexao != null && !conexao.isClosed()) {
                conexao.close();
                System.out.println("Conexão fechada.");
            }
        } catch (SQLException e) {
            System.err.println("Erro ao fechar conexão: " + e.getMessage());
        }
    }

    // Testar conexão
    public static void testarConexao() {
        try {
            if (conectar() != null) {
                String query = "SELECT 1";
                Statement stmt = conexao.createStatement();
                ResultSet rs = stmt.executeQuery(query);
                if (rs.next()) {
                    System.out.println("✓ Teste de comunicação com banco: OK");
                }
                rs.close();
                stmt.close();
            }
        } catch (SQLException e) {
            System.err.println("✗ Erro no teste de comunicação: " + e.getMessage());
        }
    }
}
