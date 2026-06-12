import java.awt.*;
import javax.swing.*;
import javax.swing.border.EmptyBorder;

// Classe customizada para JTextField com cantos arredondados
class RoundedTextField extends JTextField {
    private int raio = 15;

    public RoundedTextField(int raio) {
        this.raio = raio;
        setOpaque(false);
        setBorder(new EmptyBorder(5, 10, 5, 10));
    }

    @Override
    protected void paintComponent(Graphics g) {
        Graphics2D g2 = (Graphics2D) g;
        g2.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);

        // Desenhar fundo com cantos arredondados
        g2.setColor(getBackground());
        g2.fillRoundRect(0, 0, getWidth(), getHeight(), raio, raio);

        // Desenhar borda com cantos arredondados
        g2.setColor(new Color(100, 100, 100));
        g2.setStroke(new BasicStroke(2));
        g2.drawRoundRect(0, 0, getWidth() - 1, getHeight() - 1, raio, raio);

        super.paintComponent(g);
    }
}

// Classe customizada para JPasswordField com cantos arredondados
class RoundedPasswordField extends JPasswordField {
    private int raio = 15;

    public RoundedPasswordField(int raio) {
        this.raio = raio;
        setOpaque(false);
        setBorder(new EmptyBorder(5, 10, 5, 10));
    }

    @Override
    protected void paintComponent(Graphics g) {
        Graphics2D g2 = (Graphics2D) g;
        g2.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);

        // Desenhar fundo com cantos arredondados
        g2.setColor(getBackground());
        g2.fillRoundRect(0, 0, getWidth(), getHeight(), raio, raio);

        // Desenhar borda com cantos arredondados
        g2.setColor(new Color(100, 100, 100));
        g2.setStroke(new BasicStroke(2));
        g2.drawRoundRect(0, 0, getWidth() - 1, getHeight() - 1, raio, raio);

        super.paintComponent(g);
    }
}

public class FormCadastro extends JFrame {

    String txtNome, txtCPF, txtEmail, txtTelefone;
    JPasswordField txtSenha, txtConfirmacao;
    JButton btnCadastrar;

    public FormCadastro() {
        // 1. Configurar Janela (Resolução, Não Redimensionável, Dark Mode)
        configurarJanela();

        // 2. Inicializar JPanel com Glassmorphism
        JPanel painel = criarPainel();

        // 3. Adicionar componentes
        adicionarComponentes(painel);

        // 4. Exibir
        this.add(painel);
        this.setVisible(true);
    }

    // Método para configurar tudo de uma vez
    private void configurarJanela() {
        // Dark Mode
        try {
            UIManager.setLookAndFeel(UIManager.getSystemLookAndFeelClassName());
            UIManager.put("Panel.background", new Color(30, 30, 30));
            UIManager.put("Label.foreground", new Color(255, 255, 255));
            UIManager.put("Button.background", new Color(50, 50, 50));
            UIManager.put("Button.foreground", new Color(255, 255, 255));
            UIManager.put("TextField.background", new Color(45, 45, 45));
            UIManager.put("TextField.foreground", new Color(255, 255, 255));
        } catch (Exception e) {
            e.printStackTrace();
        }

        // Resolução + Não Redimensionável
        this.setSize(400, 700);
        this.setResizable(false);
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.setLocationRelativeTo(null); // Centraliza na tela
        this.setTitle("Cadastro ETB Pay");
    }

    private JPanel criarPainel() {
        JPanel painel = new JPanel() {
            @Override
            protected void paintComponent(Graphics g) {
                // Dark Mode background
                g.setColor(new Color(30, 30, 30));
                g.fillRect(0, 0, getWidth(), getHeight());
                super.paintComponent(g);
            }
        };
        painel.setLayout(new BoxLayout(painel, BoxLayout.Y_AXIS));
        painel.setBackground(new Color(30, 30, 30));
        painel.setBorder(BorderFactory.createEmptyBorder(20, 20, 20, 20));
        return painel;
    }

    private void adicionarComponentes(JPanel painel) {
        // Estilo de Labels e Inputs
        Font fonteLabel = new Font("Arial", Font.BOLD, 12);

        // Nome
        adicionarCampo(painel, "Nome Completo", new RoundedTextField(15), fonteLabel);

        // CPF
        adicionarCampo(painel, "CPF (Apenas números)", new RoundedTextField(15), fonteLabel);

        // Email
        adicionarCampo(painel, "E-mail Corporativo", new RoundedTextField(15), fonteLabel);

        // Telefone
        adicionarCampo(painel, "Telefone / WhatsApp", new RoundedTextField(15), fonteLabel);

        // Senha
        txtSenha = new RoundedPasswordField(15);
        adicionarCampo(painel, "Senha de Acesso", txtSenha, fonteLabel);

        // Confirmar Senha
        txtConfirmacao = new RoundedPasswordField(15);
        adicionarCampo(painel, "Confirme a Senha", txtConfirmacao, fonteLabel);

        painel.add(Box.createVerticalStrut(20));

        // Botão Cadastrar (Verde Neon)
        btnCadastrar = new JButton("CADASTRAR");
        btnCadastrar.setBackground(new Color(0, 255, 100)); // Verde Neon
        btnCadastrar.setForeground(new Color(0, 0, 0));
        btnCadastrar.setFont(new Font("Urbanist", Font.BOLD, 14));
        btnCadastrar.setPreferredSize(new Dimension(200, 40));
        btnCadastrar.setMaximumSize(new Dimension(200, 40));
        btnCadastrar.setAlignmentX(Component.CENTER_ALIGNMENT);
        painel.add(btnCadastrar);
    }

    private void adicionarCampo(JPanel painel, String label, JComponent campo, Font fonte) {
        JLabel lbl = new JLabel(label);
        lbl.setForeground(new Color(200, 200, 200));
        lbl.setFont(fonte);

        if (campo instanceof RoundedTextField) {
            ((RoundedTextField) campo).setBackground(new Color(45, 45, 45));
            ((RoundedTextField) campo).setForeground(new Color(255, 255, 255));
            ((RoundedTextField) campo).setPreferredSize(new Dimension(350, 35));
            ((RoundedTextField) campo).setMaximumSize(new Dimension(Integer.MAX_VALUE, 35));
            ((RoundedTextField) campo).setFont(new Font("Arial", Font.PLAIN, 12));
        } else if (campo instanceof RoundedPasswordField) {
            ((RoundedPasswordField) campo).setBackground(new Color(45, 45, 45));
            ((RoundedPasswordField) campo).setForeground(new Color(255, 255, 255));
            ((RoundedPasswordField) campo).setPreferredSize(new Dimension(350, 35));
            ((RoundedPasswordField) campo).setMaximumSize(new Dimension(Integer.MAX_VALUE, 35));
            ((RoundedPasswordField) campo).setFont(new Font("Arial", Font.PLAIN, 12));
        }

        painel.add(lbl);
        painel.add(Box.createVerticalStrut(5));
        painel.add(campo);
        painel.add(Box.createVerticalStrut(15));
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> new FormCadastro());
    }
}