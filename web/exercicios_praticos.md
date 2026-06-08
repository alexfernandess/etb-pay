# ETB-PAY | Laboratório Prático: Integração e Saneamento

## Bloco 1: Engenharia de Software e POO (Java)

**Desafio 1: Polimorfismo e Extensão**
* **Contexto**: O sistema ETB-PAY precisa de um novo método de pagamento (Pix).
* **Exercício**: Crie uma interface `Pagamento` com o método `processar()`. Em seguida, implemente a classe `Pix` que estende essa interface. 
* **Alvo no Concurso**: Por que a criação de novas classes para `Pix` não exige modificação nas classes de pagamento existentes[cite: 1]?

**Desafio 2: Encapsulamento em Ação**
* **Contexto**: Segurança de saldo na classe `Conta`.
* **Exercício**: Implemente um atributo `private double saldo`. Crie métodos `getSaldo()` e `setSaldo()` (com verificação para impedir valores negativos).
* **Alvo no Concurso**: Explique por que o modificador `private` protege o atributo de acessos externos não autorizados[cite: 1].

---

## Bloco 2: Banco de Dados e Governança

**Desafio 3: DDL vs DML (Cirurgia de Estrutura)**
* **Cenário**: Você tem a tabela `clientes_old` com dados corrompidos.
* **Exercício**: 
    1. Utilize `DROP TABLE` para eliminar a estrutura legada[cite: 2].
    2. Utilize `CREATE TABLE` para definir a nova tabela `tb_clientes` com as restrições `PRIMARY KEY` e `NOT NULL`[cite: 2].
* **Alvo no Concurso**: Por que o `DROP` atua na DDL enquanto o `DELETE` atua na DML[cite: 2]?

**Desafio 4: Máscaras e Validação (GLOB vs LIKE)**
* **Contexto**: Garantir que o CPF tenha apenas números e tamanho 11.
* **Exercício**: Escreva um `CHECK` utilizando o operador `GLOB` para validar que o campo `cpf` contenha estritamente dígitos[cite: 2].
* **Alvo no Concurso**: Por que o `GLOB` é mais rigoroso que o `LIKE` para validações de máscaras[cite: 2]?

**Desafio 5: Transações ACID (O Caso da Atomicidade)**
* **Contexto**: Migração de dados da `clientes_old` para `tb_clientes`.
* **Exercício**: Execute um bloco de inserção de 10 registros. Simule uma falha no 5º registro e verifique se o banco reverteu as inserções anteriores[cite: 2].
* **Alvo no Concurso**: O que o conceito de "Tudo ou Nada" (Atomicidade) garante em caso de falhas durante o lote[cite: 2]?

**Desafio 6: DCL e Segurança (Menor Privilégio)**
* **Contexto**: O sistema precisa separar o analista de suporte do administrador.
* **Exercício**: Utilize `GRANT` para dar privilégios de `INSERT` ao usuário `suporte` e verifique se ele consegue executar `SELECT`[cite: 2].
* **Alvo no Concurso**: Por que, sob o princípio do menor privilégio, o acesso de escrita não herda automaticamente a leitura[cite: 2]?