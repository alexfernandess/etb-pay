BEGIN TRANSACTION;

-- 1. Resetando o ambiente legado
DROP TABLE IF EXISTS clientes_old;

-- 2. DDL: Criação da tabela legada sem restrições
CREATE TABLE clientes_old (
    cpf TEXT,
    nome TEXT,
    email TEXT
);

-- 3. DML: Injeção de exatamente 10 registros
INSERT INTO clientes_old (cpf, nome, email) VALUES 
    -- [VÁLIDOS - 6 Registros]
    ('077626341-77', 'Alex F B Alves', 'alexalves@etb.df.gov.br'),
    ('11122233344', 'Bruno Lima', 'brunolima@email.com'),
    ('22233344455', 'Carla Dias', 'Carla Dias@exemplo.com'),
    ('33344455566', 'Ana Silva', 'ana@exemplo.com'),
    ('44455566677', 'Carlos Souza', 'carlos@exemplo.com'),
    ('55566677788', 'Mariana Lima', 'mariana@exemplo.com'),

    -- [INVÁLIDOS - 4 Registros (Dados Sujos para o Saneamento)]
    ('JOAO DA SILVA', 'Registro Invalido 1', 'erro1@etb.com'), -- Recuperável via UPDATE (Cirurgia)
    ('123-INVALIDO', 'Registro Invalido 2', 'erro2@etb.com'),  -- Lixo puro (Será barrado)
    ('---.--.--', 'Registro Invalido 3', 'erro3@etb.com'),     -- Lixo puro (Será barrado)
    ('99900011122A', 'Registro Invalido 4', 'erro4@etb.com');   -- Alfanumérico/Tamanho errado (Será barrado)

COMMIT;

-- 4. DQL: Conferência da Amostragem
SELECT * FROM clientes_old;

SELECT count(*) AS 'TOTAL DE CLIENTES' FROM clientes_old; -- número de registros inseridos