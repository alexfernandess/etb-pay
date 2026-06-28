import re

with open(r"c:\workspace\etb-pay\web\etb_arena_de_questoes_2G.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Replace the bancoQuestoes array entirely with database
new_db = """        const database = {
            bd: {
                disciplina: "Banco de Dados",
                cargo: "Engenheiro de Dados",
                questions: [
                    {
                        id: "bd_q1",
                        assunto: "Abstração e Modelagem",
                        enunciado: "Na modelagem de banco de dados, o projeto é dividido em três níveis de abstração: o nível conceitual (independente de tecnologia, focado na regra de negócio), o nível lógico (estruturas de tabelas) e o nível físico (detalhes de armazenamento no SGBD).",
                        gabarito: "C",
                        comentario: "Exato. O Conceitual é o diagrama desenhado para o cliente (MER), o Lógico é a tradução para tabelas e chaves, e o Físico é o script SQL (DDL) rodando diretamente no motor do banco."
                    },
                    {
                        id: "bd_q2",
                        assunto: "Normalização Relacional",
                        enunciado: "Uma tabela atende à 1ª Forma Normal (1FN) mesmo quando um campo de contato armazena três números de celular separados por vírgula em uma mesma célula de coluna.",
                        gabarito: "E",
                        comentario: "A Regra Áurea da 1ª Forma Normal (1FN) é a Atomicidade. O dado deve ser indivisível. Valores multivalorados ferem a 1FN e devem ser extraídos para novas estruturas."
                    },
                    {
                        id: "bd_q3",
                        assunto: "Normalização Relacional",
                        enunciado: "Se a tabela possuir uma Chave Primária Composta (ID_Produto, ID_Loja), e a coluna \\"Nome do Produto\\" depender apenas da metade da chave (ID_Produto), a tabela ainda atende à 2ª Forma Normal (2FN).",
                        gabarito: "E",
                        comentario: "A 2ª Forma Normal (2FN) estipula que todos os atributos não-chave devem depender da CHAVE PRIMÁRIA COMPLETA. Dependência parcial de chave composta viola a 2FN."
                    },
                    {
                        id: "bd_q4",
                        assunto: "Integridade Referencial",
                        enunciado: "A exclusão de um registro na tabela principal, mesmo que efetuada sem a configuração de cláusulas como CASCADE ou RESTRICT, é garantida em compliance (conformidade) porque a tabela dependente não reterá o Foreign Key.",
                        gabarito: "E",
                        comentario: "Sem o ON DELETE CASCADE ou RESTRICT ativado, deletar um registro-pai cria um 'Registro Órfão' na tabela filha. Isso viola a Integridade Referencial e a conformidade (compliance) dos dados."
                    },
                    {
                        id: "bd_q9",
                        assunto: "Linguagem de Definição",
                        enunciado: "Os comandos CREATE, ALTER e DROP são utilizados primariamente para a manipulação dos registros e consultas de dados dentro das tabelas, atuando diretamente no nível das linhas.",
                        gabarito: "E",
                        comentario: "Esses comandos não manipulam dados (linhas), eles manipulam a ESTRUTURA. Eles pertencem à Linguagem de Definição de Dados (DDL) e servem para criar, alterar ou destruir as tabelas em si."
                    },
                    {
                        id: "bd_q10",
                        assunto: "Comandos SQL (DML)",
                        enunciado: "É possível popular uma tabela utilizando dados provenientes de outra tabela por meio do comando estruturado: <code>INSERT INTO tabela_destino SELECT * FROM tabela_origem;</code>, desde que as estruturas das tabelas sejam compatíveis.",
                        gabarito: "C",
                        comentario: "Correto. Essa é uma técnica avançada e muito útil de DML conhecida como 'Insert com Select', que permite migrar ou duplicar grandes volumes de dados de uma tabela para outra de forma rápida."
                    },
                    {
                        id: "bd_q12",
                        assunto: "Chaves Relacionais",
                        enunciado: "A Chave Primária (Primary Key) de uma tabela tem como principal função garantir a unicidade de cada registro, não permitindo valores nulos ou valores repetidos em sua respectiva coluna.",
                        gabarito: "C",
                        comentario: "Perfeito. A Primary Key (PK) é a identidade (o CPF) do registro. Por definição arquitetural, ela aplica automaticamente as restrições UNIQUE (não repete) e NOT NULL (não fica vazia)."
                    },
                    {
                        id: "bd_q14",
                        assunto: "Chaves Relacionais",
                        enunciado: "A Chave Estrangeira (Foreign Key) é o mecanismo relacional utilizado para criar vínculos entre tabelas diferentes, garantindo que o valor inserido na tabela filha exista obrigatoriamente na tabela mãe.",
                        gabarito: "C",
                        comentario: "Exato. A Foreign Key (FK) é o pilar dos bancos relacionais. Ela garante a amarração dos dados, impedindo que você cadastre uma venda para um 'ID de Cliente' que não existe no sistema."
                    },
                    {
                        id: "bd_q15",
                        assunto: "Tipos de Dados",
                        enunciado: "No momento da criação de uma tabela, a escolha do tipo de dado (como VARCHAR, INT ou DATE) é opcional, pois os bancos de dados relacionais modernos deduzem o tipo automaticamente com base no primeiro dado inserido.",
                        gabarito: "E",
                        comentario: "Bancos de dados relacionais (SQL) possuem tipagem forte e esquema rígido. A definição do tipo de dado para cada coluna no comando <code>CREATE TABLE</code> é obrigatória e inegociável."
                    }
                ]
            }
        };"""

content = re.sub(r'const bancoQuestoes = \[.*?\];', new_db, content, flags=re.DOTALL)

# 2. Update loadExam to use the database constant
load_exam_old = r"""            let examDisciplina = examKey === 'java' \? "Java Back-End" : "Banco de Dados";
            let filteredQuestions = bancoQuestoes\.filter\(q => q\.disciplina === examDisciplina\);

            currentExam = \{
                disciplina: examKey === 'java' \? "Banco de Dados" : "Banco de Dados",
                turma: examKey === 'java' \? "3G" : "2G",
                cargo: examKey === 'java' \? "Engenheiro de Software" : "Engenheiro de Dados",
                questions: filteredQuestions
            \};"""

load_exam_new = """            const examData = database.bd;
            
            currentExam = {
                disciplina: examData.disciplina,
                turma: "2G",
                cargo: examData.cargo,
                questions: examData.questions
            };"""

content = re.sub(load_exam_old, load_exam_new, content)

# 3. Update HTML generation for radio values (Certo -> C, Errado -> E)
html_certo_old = r'<input type="radio" name="opt_\$\{q\.id\}" value="Certo"'
html_certo_new = '<input type="radio" name="opt_${q.id}" value="C"'
content = re.sub(html_certo_old, html_certo_new, content)

html_errado_old = r'<input type="radio" name="opt_\$\{q\.id\}" value="Errado"'
html_errado_new = '<input type="radio" name="opt_${q.id}" value="E"'
content = re.sub(html_errado_old, html_errado_new, content)

# 4. Update responder gabaritoText
gabarito_old = r"const gabaritoText = gabaritoCorreto\.toUpperCase\(\);"
gabarito_new = "const gabaritoText = gabaritoCorreto.toUpperCase() === 'C' ? 'CERTO' : 'ERRADO';"
content = re.sub(gabarito_old, gabarito_new, content)

with open(r"c:\workspace\etb-pay\web\etb_arena_de_questoes_2G.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Refactoring complete.")
