import java.sql.*;
import java.util.ArrayList;
import java.util.List;

public class ClienteDAO {
    private Connection conexao;

    public ClienteDAO() {
        this.conexao = ConexaoDB.getConexao();
    }

    // Inserir novo cliente
    public boolean inserir(Cliente cliente) {
        try {
            String sql = "INSERT INTO tb_clientes (cpf, nome, email) VALUES (?, ?, ?)";
            PreparedStatement pstmt = conexao.prepareStatement(sql);
            pstmt.setString(1, cliente.getCpf());
            pstmt.setString(2, cliente.getNome());
            pstmt.setString(3, cliente.getEmail());

            int linhasAfetadas = pstmt.executeUpdate();
            pstmt.close();

            if (linhasAfetadas > 0) {
                System.out.println("✓ Cliente inserido com sucesso!");
                return true;
            }
        } catch (SQLException e) {
            System.err.println("✗ Erro ao inserir cliente: " + e.getMessage());
        }
        return false;
    }

    // Buscar cliente por CPF
    public Cliente buscarPorCPF(String cpf) {
        try {
            String sql = "SELECT * FROM tb_clientes WHERE cpf = ?";
            PreparedStatement pstmt = conexao.prepareStatement(sql);
            pstmt.setString(1, cpf);

            ResultSet rs = pstmt.executeQuery();
            if (rs.next()) {
                Cliente cliente = new Cliente(
                    rs.getString("nome"),
                    rs.getString("cpf"),
                    rs.getString("email")
                );
                rs.close();
                pstmt.close();
                return cliente;
            }
            rs.close();
            pstmt.close();
        } catch (SQLException e) {
            System.err.println("✗ Erro ao buscar cliente: " + e.getMessage());
        }
        return null;
    }

    // Listar todos os clientes
    public List<Cliente> listarTodos() {
        List<Cliente> clientes = new ArrayList<>();
        try {
            String sql = "SELECT * FROM tb_clientes";
            Statement stmt = conexao.createStatement();
            ResultSet rs = stmt.executeQuery(sql);

            while (rs.next()) {
                Cliente cliente = new Cliente(
                    rs.getString("nome"),
                    rs.getString("cpf"),
                    rs.getString("email")
                );
                clientes.add(cliente);
            }
            rs.close();
            stmt.close();
        } catch (SQLException e) {
            System.err.println("✗ Erro ao listar clientes: " + e.getMessage());
        }
        return clientes;
    }

    // Atualizar cliente
    public boolean atualizar(Cliente cliente) {
        try {
            String sql = "UPDATE tb_clientes SET nome = ?, email = ? WHERE cpf = ?";
            PreparedStatement pstmt = conexao.prepareStatement(sql);
            pstmt.setString(1, cliente.getNome());
            pstmt.setString(2, cliente.getEmail());
            pstmt.setString(3, cliente.getCpf());

            int linhasAfetadas = pstmt.executeUpdate();
            pstmt.close();

            return linhasAfetadas > 0;
        } catch (SQLException e) {
            System.err.println("✗ Erro ao atualizar cliente: " + e.getMessage());
        }
        return false;
    }

    // Deletar cliente
    public boolean deletar(String cpf) {
        try {
            String sql = "DELETE FROM tb_clientes WHERE cpf = ?";
            PreparedStatement pstmt = conexao.prepareStatement(sql);
            pstmt.setString(1, cpf);

            int linhasAfetadas = pstmt.executeUpdate();
            pstmt.close();

            return linhasAfetadas > 0;
        } catch (SQLException e) {
            System.err.println("✗ Erro ao deletar cliente: " + e.getMessage());
        }
        return false;
    }
}
