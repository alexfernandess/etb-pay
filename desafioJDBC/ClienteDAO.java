import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;

public class ClienteDAO {

    public void cadastrarCliente(Cliente cliente) {
        String sql = "INSERT INTO clientes (cpf, nome, email, telefone) VALUES (?, ?, ?, ?)";

        try (Connection conn = ConexaoDB.conectar();
                PreparedStatement stmt = conn.prepareStatement(sql)) {

            stmt.setString(1, cliente.getCpf());
            stmt.setString(2, cliente.getNome());
            stmt.setString(3, cliente.getEmail());
            stmt.setString(4, cliente.getTelefone());

            // Métodos do objeto Statement

            System.out.println("Processando cadastro de cliente no sistema...");

        } catch (SQLException e) {
            System.out.println("Falha na persistência: " + e.getMessage());
        }
    }
}