-- 1. Resetando o ambiente destino
DROP TABLE IF EXISTS tb_clientes;

-- 2. DDL: Criação da tabela destino blindada
CREATE TABLE tb_clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cpf TEXT UNIQUE NOT NULL,
    nome TEXT NOT NULL,
    email TEXT,
    telefone TEXT CHECK (
        telefone IS NULL OR
        (LENGTH(telefone) = 11 AND GLOB('[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]', telefone))
    )
);

BEGIN TRANSACTION;

-- 3. Executando a carga com saneamento de dados preliminar
INSERT INTO tb_clientes (cpf, nome, email, telefone)
SELECT
    cpf,
    nome,
    email,
    NULL -- O campo telefone inicia vazio na migração
FROM clientes_old
WHERE
    -- Filtro para capturar apenas CPFs estruturalmente viáveis (tamanho 11 ou 12)
    LENGTH(cpf) IN (11, 12)
    -- Evita que strings de lixo do mesmo tamanho passem (como '---.--.--')
    AND GLOB('*[0-9]*', cpf);

COMMIT;

SELECT * FROM tb_clientes;
SELECT count(*) AS 'TOTAL DE CLIENTES MIGRADOS' FROM tb_clientes; -- número de registros migrados

-- 4. Recuperando o registro que estava trocado no legado
INSERT INTO tb_clientes (cpf, nome, email, telefone)
VALUES (777788899900, 'João da Silva', 'joao.silva@etb.com', NULL);

-- 5. Higienizando o CPF do cliente Alex
UPDATE tb_clientes
SET cpf = '07762634177'
WHERE nome = 'Alex%';

-- 5.1 Higienização dinâmica usando REPLACE
UPDATE tb_clientes
SET cpf = REPLACE(cpf, '-', '')
WHERE cpf LIKE '%-%';

-- 5.2Saneamento Avançado: Removendo Pontos E Hifens de uma só vez
UPDATE tb_clientes 
SET cpf = REPLACE(REPLACE(cpf, '.', ''), '-', '')
WHERE cpf LIKE '%.%' OR cpf LIKE '%-%'; 