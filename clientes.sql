-- Garante um estado limpo antes da carga
DROP TABLE IF EXISTS clientes;
DROP TABLE IF EXISTS tb_clientes;

-- Criação da estrutura da tabela 'clientes' (utilizada no pacote desafioJDBC)
CREATE TABLE clientes (
    id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    cpf TEXT UNIQUE NOT NULL CHECK (length(cpf) = 11 AND NOT cpf GLOB '*[^0-9]*'),
    telefone TEXT CHECK (
        length(telefone) <= 11 
        AND NOT telefone GLOB '*[^0-9]*'
    )
);

-- Criação da estrutura da tabela 'tb_clientes' (utilizada no pacote src)
CREATE TABLE tb_clientes (
    id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    cpf TEXT UNIQUE NOT NULL CHECK (length(cpf) = 11 AND NOT cpf GLOB '*[^0-9]*'),
    telefone TEXT CHECK (
        length(telefone) <= 11 
        AND NOT telefone GLOB '*[^0-9]*'
    )
);

-- Carga Atômica de 10 Registros na tabela 'clientes'
INSERT INTO clientes (cpf, nome, email, telefone) VALUES 
    ('11122233344', 'Ana Silva', 'ana.silva@etb.com', '61991223344'),
    ('22233344455', 'Bruno Costa', 'bruno.costa@etb.com', '61992334455'),
    ('33344455566', 'Carla Dias', 'carla.dias@etb.com', '61993445566'),
    ('44455566677', 'Diego Souza', 'diego.souza@etb.com', '61994556677'),
    ('55566677788', 'Elena Rocha', 'elena.rocha@etb.com', '61995667788'),
    ('66677788899', 'Felipe Lima', 'felipe.lima@etb.com', '61996778899'),
    ('77788899900', 'Gabriela Alves', 'gabriela.alves@etb.com', '61997889900'),
    ('88899900011', 'Hugo Santos', 'hugo.santos@etb.com', '61998990011'),
    ('99900011122', 'Isabela Reis', 'isabela.reis@etb.com', '61999001122'),
    ('00011122233', 'Joao Ferreira', 'joao.ferreia@etb.com', '61990112233');

-- Carga Atômica de 10 Registros na tabela 'tb_clientes'
INSERT INTO tb_clientes (cpf, nome, email, telefone) VALUES 
    ('11122233344', 'Ana Silva', 'ana.silva@etb.com', '61991223344'),
    ('22233344455', 'Bruno Costa', 'bruno.costa@etb.com', '61992334455'),
    ('33344455566', 'Carla Dias', 'carla.dias@etb.com', '61993445566'),
    ('44455566677', 'Diego Souza', 'diego.souza@etb.com', '61994556677'),
    ('55566677788', 'Elena Rocha', 'elena.rocha@etb.com', '61995667788'),
    ('66677788899', 'Felipe Lima', 'felipe.lima@etb.com', '61996778899'),
    ('77788899900', 'Gabriela Alves', 'gabriela.alves@etb.com', '61997889900'),
    ('88899900011', 'Hugo Santos', 'hugo.santos@etb.com', '61998990011'),
    ('99900011122', 'Isabela Reis', 'isabela.reis@etb.com', '61999001122'),
    ('00011122233', 'Joao Ferreira', 'joao.ferreia@etb.com', '61990112233');

-- Validação de sucesso para a Squad
SELECT * FROM clientes;