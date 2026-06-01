O Script de "Limpeza e Resgate" (A Solução)
DDL: Criando a estrutura blindada

CREATE TABLE tb_clientes (
    id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
    cpf TEXT UNIQUE NOT NULL CHECK (cpf GLOB '[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]'),
    nome TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
);

INSERT INTO tb_clientes (cpf, nome, email)
SELECT cpf, nome, email
FROM clientes_old
WHERE length(cpf) = 11
  AND cpf GLOB '*[a-zA-Z]*' = 0;

 DQL: O resultado do resgate
SELECT * FROM tb_clientes;

Passo 1: Identificar e remover os registros "Bons" (os Válidos)
1. Auditoria: Visualizar o que será removido (os válidos)
SELECT * FROM clientes_old 
WHERE cpf GLOB '[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]';

2. DML: Remover apenas os registros válidos
Após este comando, sobrarão apenas os "sujos" na tabela
DELETE FROM clientes_old 
WHERE cpf GLOB '[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]';

SELECT * FROM clientes_old; -- Visualizar os registros "sujos" restantes

-- 1. Criar a nova tabela com a estrutura desejada (incluindo o CHECK)
CREATE TABLE tb_clientes_nova (
    id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    cpf TEXT UNIQUE NOT NULL CHECK (length(cpf) = 11)
);

-- 2. Copiar os dados válidos da tabela antiga para a nova
-- (Isso evita erros na inserção caso existam CPFs com tamanho incorreto)
INSERT INTO tb_clientes_nova (id_cliente, nome, email, cpf)
SELECT id_cliente, nome, email, cpf
FROM tb_clientes
WHERE length(cpf) = 11;

3. Remover a tabela antiga e renomear a nova
DROP TABLE tb_clientes;
ALTER TABLE tb_clientes_nova RENAME TO tb_clientes;