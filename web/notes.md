Precisamos atualizar a estrutura de protótipo de forma a manter os títulos em uma barra recolhível do lado esquerdo. A imagem de controle de apresentação ou recolhimento da barra deverá ser o símbolo da base de dados apresentada no topo do título.

Será importantíssimo termos botões para aumentar e reduzirmos os tamanhos da fonte utilizada em cada página.

No slide 3, é importantíssimo termos a descrição completa das ações a serem executadas em classe, como:
1. Deixar bem claro a necessidade de criação de uma tabela tb_clientes;
2. Identificação dos campos da tabela, seus tipos e restrições (id_cliente, cpf, nome, email e telefone);
3. Bem como as constraints e limitações aplicados a cada campo;
4. Utilizar a constraint BLOB simplificada para o CPF aceitar somente numeros (AND GLOB('*[0-9]*', cpf);)