import json
import re

with open(r"c:\workspace\etb-pay\web\etb_arena_de_questoes_3G.html", "r", encoding="utf-8") as f:
    content = f.read()

# UI Replacements
content = content.replace("Identificação do Engenheiro(a)", "Identificação do Engenheiro(a) de Dados")
content = content.replace("LTP II - Java", "Banco de Dados")
content = content.replace(">3G<", ">2G<")
content = content.replace("Carregar Missão Java", "Carregar Missão Banco de Dados")
content = content.replace("loadExam('java')", "loadExam('banco')")
content = content.replace("btn-load-java", "btn-load-banco")
content = content.replace("border-l-purple-500", "border-l-cyan-500") 
content = content.replace("text-purple-400", "text-cyan-400")

# The 15 DB questions
questions = [
    {
        "id": 1,
        "disciplina": "Banco de Dados",
        "assunto": "Arquitetura e Níveis de Abstração",
        "enunciado": "Sistemas de Gerenciamento de Banco de Dados (SGBD) como o SQLite operam sob uma arquitetura cliente-servidor tradicional, exigindo que um processo de background rodando em uma porta específica seja responsável por escutar e processar as requisições do sistema operacional.",
        "gabarito": "Errado",
        "comentario": "O SQLite possui uma arquitetura <strong>embutida (embedded) e sem servidor (serverless)</strong>. Ele não opera como um serviço de rede em porta específica (diferente do PostgreSQL ou Oracle), mas acessa e manipula diretamente os arquivos do banco de dados no disco onde a aplicação está rodando."
    },
    {
        "id": 2,
        "disciplina": "Banco de Dados",
        "assunto": "Arquitetura e Níveis de Abstração",
        "enunciado": "No estudo da arquitetura de Três Esquemas (Three-Schema Architecture), o <strong>Nível Físico (ou Interno)</strong> é responsável por descrever exatamente como os dados estão armazenados fisicamente no disco, englobando estruturas de dados, métodos de acesso e indexação, ocultando essas complexidades do programador que consome a base.",
        "gabarito": "Certo",
        "comentario": "Perfeito. O Nível Físico lida com o armazenamento real em baixo nível (cilindros, trilhas, blocos, arquivos). O programador interage geralmente com o Nível Lógico (tabelas e chaves), enquanto o SGBD abstrai os detalhes físicos de I/O."
    },
    {
        "id": 3,
        "disciplina": "Banco de Dados",
        "assunto": "Arquitetura e Níveis de Abstração",
        "enunciado": "O Nível Conceitual foca no diagrama entidade-relacionamento de forma técnica, sendo a etapa onde o desenvolvedor já deve obrigatoriamente definir os tipos de dados precisos (como VARCHAR ou INT) e as chaves estrangeiras específicas do SGBD escolhido para a aplicação.",
        "gabarito": "Errado",
        "comentario": "O <strong>Nível Conceitual</strong> é de alto nível, voltado para o negócio e para o entendimento do usuário. A definição de tipos de dados técnicos (como VARCHAR) e chaves estrangeiras rigorosas ocorre no <strong>Nível Lógico</strong> (e suas otimizações no Nível Físico)."
    },
    {
        "id": 4,
        "disciplina": "Banco de Dados",
        "assunto": "Normalização de Dados",
        "enunciado": "Uma tabela de produtos em que uma única coluna chamada <code>cores_disponiveis</code> armazena o valor \"Azul, Vermelho, Verde\" fere diretamente as regras da Primeira Forma Normal (1FN), pois contém atributos não atômicos (multivalorados).",
        "gabarito": "Certo",
        "comentario": "A <strong>1FN</strong> exige que todos os domínios de uma tabela sejam <strong>atômicos</strong> (indivisíveis). Armazenar uma lista separada por vírgulas em uma única célula viola essa regra, exigindo a criação de uma nova tabela para representar esse relacionamento 1:N."
    },
    {
        "id": 5,
        "disciplina": "Banco de Dados",
        "assunto": "Normalização de Dados",
        "enunciado": "A Segunda Forma Normal (2FN) prevê a eliminação de dependências transitivas. Ou seja, ela atua quando um atributo não-chave depende de outro atributo não-chave, garantindo que toda coluna dependa apenas da chave primária.",
        "gabarito": "Errado",
        "comentario": "A banca trocou os conceitos! A eliminação de dependências <strong>transitivas</strong> (o famoso atributo caroneiro) é o alvo da <strong>Terceira Forma Normal (3FN)</strong>. A 2FN atua exclusivamente na eliminação de dependências <strong>parciais</strong> (quando um atributo depende apenas de um pedaço de uma chave primária composta)."
    },
    {
        "id": 6,
        "disciplina": "Banco de Dados",
        "assunto": "Normalização de Dados",
        "enunciado": "Considere uma tabela de Itens de Pedido com a chave primária composta por (ID_Pedido, ID_Produto). Se a tabela contiver o campo <code>Nome_do_Produto</code>, que depende exclusivamente do ID_Produto e não do ID_Pedido, essa tabela viola a Segunda Forma Normal (2FN).",
        "gabarito": "Certo",
        "comentario": "Exatamente. O <code>Nome_do_Produto</code> depende apenas do Produto, mas a chave da tabela é composta (Pedido + Produto). Isso cria uma <strong>dependência parcial</strong>. Para atingir a 2FN, os dados do produto devem ser movidos para uma tabela independente."
    },
    {
        "id": 7,
        "disciplina": "Banco de Dados",
        "assunto": "Normalização de Dados",
        "enunciado": "Ao normalizar um banco de dados até a Terceira Forma Normal (3FN), o número total de tabelas geradas sempre diminuirá, tornando as consultas <code>SELECT</code> do sistema mais rápidas, devido à menor necessidade de realizar junções estruturais.",
        "gabarito": "Errado",
        "comentario": "A normalização visa <strong>reduzir anomalias de atualização e redundâncias</strong>, não necessariamente o número de tabelas (que geralmente <strong>aumenta</strong> após criar tabelas filhas). Além disso, o excesso de tabelas aumenta a necessidade de operações custosas de JOIN, o que pode tornar os comandos <code>SELECT</code> mais lentos (motivo pelo qual usamos a desnormalização em DWs)."
    },
    {
        "id": 8,
        "disciplina": "Banco de Dados",
        "assunto": "Comandos DDL vs DML",
        "enunciado": "A instrução <code>DELETE FROM Funcionarios;</code> pertence ao grupo DML (Linguagem de Manipulação de Dados) e irá esvaziar os registros, contudo, a estrutura da tabela (suas colunas e configuração) continuará existindo intacta no banco de dados.",
        "gabarito": "Certo",
        "comentario": "Correto. O comando <strong>DELETE (DML)</strong> opera nos dados armazenados (linhas), apagando os registros, mas preservando o \"molde\" da tabela. Se quiséssemos destruir a tabela inteira (dados e estrutura), usaríamos o <strong>DROP TABLE (DDL)</strong>."
    },
    {
        "id": 9,
        "disciplina": "Banco de Dados",
        "assunto": "Comandos DDL vs DML",
        "enunciado": "A exclusão de uma tabela inteira através do comando DDL <code>DROP TABLE Clientes;</code> é um processo reversível caso o desenvolvedor utilize imediatamente a instrução <code>ROLLBACK</code> em bancos de dados transacionais, por se tratar de uma operação DML.",
        "gabarito": "Errado",
        "comentario": "O comando <strong>DROP TABLE</strong> é um comando <strong>DDL (Data Definition Language)</strong>. Comandos DDL provocam commit automático em muitos SGBDs modernos (como MySQL e Oracle) e destroem irreversivelmente a estrutura do dicionário de dados, não podendo ser revertidos com um simples <code>ROLLBACK</code> como as operações DML (INSERT/UPDATE/DELETE)."
    },
    {
        "id": 10,
        "disciplina": "Banco de Dados",
        "assunto": "Comandos SQL",
        "enunciado": "O comando SQL DML conhecido como <code>INSERT INTO ... SELECT</code> é uma técnica avançada que permite consultar dados de uma tabela e inseri-los automaticamente em outra, sendo extremamente útil na criação de históricos e limpeza de tabelas sem necessidade de um script em linguagem de programação intermediária.",
        "gabarito": "Certo",
        "comentario": "Exato. A sintaxe <code>INSERT INTO Tabela_A SELECT * FROM Tabela_B</code> une DQL (busca) e DML (inserção) numa operação de alto desempenho no próprio motor do SGBD, ideal para migração ou consolidação de dados massivos."
    },
    {
        "id": 11,
        "disciplina": "Banco de Dados",
        "assunto": "Comandos SQL",
        "enunciado": "As linguagens SQL são categorizadas em subconjuntos baseados na sua função. Criar uma restrição de Chave Estrangeira com <code>ALTER TABLE</code> é uma ação DQL, enquanto atualizar salários usando <code>UPDATE</code> é uma ação DDL.",
        "gabarito": "Errado",
        "comentario": "A categorização está invertida/errada. O comando <code>ALTER TABLE</code> mexe na estrutura, logo é <strong>DDL (Data Definition Language)</strong>. O comando <code>UPDATE</code> manipula o conteúdo dos dados, logo é <strong>DML (Data Manipulation Language)</strong>. A <strong>DQL</strong> é reservada exclusivamente ao <code>SELECT</code>."
    },
    {
        "id": 12,
        "disciplina": "Banco de Dados",
        "assunto": "Álgebra Relacional",
        "enunciado": "Em operações baseadas na álgebra relacional, ao executarmos um comando <code>INNER JOIN</code> entre a tabela de Clientes e a tabela de Vendas usando o ID do Cliente, o resultado retornará apenas as linhas em que houver total correspondência do ID em ambas as tabelas envolvidas.",
        "gabarito": "Certo",
        "comentario": "Correto! O <strong>INNER JOIN</strong> atua como a operação de intersecção, retornando exclusivamente as tuplas (linhas) que possuam uma ligação (match) válida simultaneamente nas duas tabelas."
    },
    {
        "id": 13,
        "disciplina": "Banco de Dados",
        "assunto": "Integridade Referencial",
        "enunciado": "Em um cenário corporativo, a restrição de Chave Estrangeira (Foreign Key) configurada com o gatilho <code>ON DELETE CASCADE</code> protegerá a tabela filha. Se tentarem apagar o cliente \"José\" da tabela mãe, a operação será instantaneamente bloqueada se ele possuir pedidos vinculados na tabela filha.",
        "gabarito": "Errado",
        "comentario": "Pelo contrário! O <code>ON DELETE CASCADE</code> causa o efeito dominó: ao apagar o José, o SGBD <strong>apagará automaticamente</strong> todos os pedidos dele na tabela filha sem bloqueios. Para bloquear e proteger contra remoções indesejadas, a configuração correta seria o <code>ON DELETE RESTRICT</code> (que é o comportamento padrão)."
    },
    {
        "id": 14,
        "disciplina": "Banco de Dados",
        "assunto": "Integridade Referencial",
        "enunciado": "Registros órfãos ocorrem em bancos de dados relacionais quando uma linha da tabela filha faz referência a um identificador que não existe mais na tabela mãe, falha que pode ser prevenida com a correta implementação de Constraints de Integridade Referencial (Chaves Estrangeiras).",
        "gabarito": "Certo",
        "comentario": "Perfeito. Uma Chave Estrangeira existe justamente para impor a <strong>Integridade Referencial</strong> e evitar <strong>órfãos</strong> (ex: um pedido registrado no banco que aponta para um ID de Cliente inexistente)."
    },
    {
        "id": 15,
        "disciplina": "Banco de Dados",
        "assunto": "Álgebra Relacional",
        "enunciado": "A operação clássica de <strong>Projeção</strong> (símbolo Pi) na álgebra relacional equivale à cláusula <code>WHERE</code> no SQL moderno, cuja função primária é escolher um subconjunto de linhas que satisfaçam determinada condição.",
        "gabarito": "Errado",
        "comentario": "Os conceitos foram trocados. A operação que filtra as <strong>linhas</strong> (cláusula WHERE) é a <strong>Seleção (Sigma)</strong>. Já a operação de <strong>Projeção (Pi)</strong> equivale à cláusula <code>SELECT col1, col2</code>, cuja função é filtrar as <strong>colunas (atributos)</strong> desejadas da relação."
    }
]

questions_json = json.dumps(questions, indent=16, ensure_ascii=False)
# format nicely
lines = questions_json.splitlines()
formatted_json = "\n".join(lines[1:-1])

replacement = f"const bancoQuestoes = [\n{formatted_json}\n        ];"

content = re.sub(r'const bancoQuestoes = \[.*?\];', replacement, content, flags=re.DOTALL)

with open(r"c:\workspace\etb-pay\web\etb_arena_de_questoes_2G.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Migration to 2G complete.")
