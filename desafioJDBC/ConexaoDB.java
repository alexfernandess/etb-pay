import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class ConexaoDB {

    // CORREÇÃO: Alterada a string de conexão de MySQL para SQLite para pleno funcionamento da SPA local
    private static final String URL = "jdbc:sqlite:etbpay.db";

    public static Connection conectar() {
        try {
            return DriverManager.getConnection(URL);
        } catch (SQLException e) {
            System.out.println("Erro crítico ao conectar no banco: " + e.getMessage());
            return null;
        }
    }
}