### QUESTÃO DISCURSIVA - ANSIBLE

**Afirmação-Chave:** O Ansible consolida as práticas de DevOps ao atuar como uma ferramenta de Infraestrutura como Código (IaC) e gerenciamento de configuração, viabilizando a automação de pipelines de entrega por meio de uma arquitetura *agentless* e assegurando a idempotência dos ambientes através de arquivos declarativos em formato YAML (*Playbooks*).

---

#### 📌 Pilares de Sustentação

Para detalhar essa afirmação e atingir a pontuação máxima em todos os quesitos da folha de correção, é necessário desenvolver os seguintes conceitos táticos:

* **O Princípio da Idempotência (O pilar estrutural):** É a propriedade pela qual a execução repetida de um mesmo *Playbook* produz exatamente o mesmo resultado no ambiente, sem gerar efeitos colaterais ou duplicar configurações. Se o servidor já estiver no estado desejado, o Ansible não realiza nenhuma alteração física, garantindo a consistência contínua entre os ambientes de desenvolvimento e produção.

* **Arquitetura *Agentless* e Inventário (Vantagem de Infraestrutura):** Diferente de outras ferramentas de gerência de configuração, o Ansible não requer a instalação de um software cliente ou *daemon* nos nós gerenciados. A comunicação é feita de forma direta via *push mode* usando protocolos nativos de comunicação, como SSH para sistemas Linux e WinRM para sistemas Windows, reduzindo o *overhead* de segurança e a sobrecarga da rede. A orquestração desses nós é gerenciada de forma centralizada através de um arquivo de **Inventário** (estático ou dinâmico), que mapeia os *hosts* que receberão as instruções.

* **Versionamento e Rastreabilidade (A intersecção com o Git):** Como os *Playbooks* são escritos em linguagem humana legível (YAML), a infraestrutura passa a se comportar exatamente como um software tradicional. Ela pode ser versionada em repositórios Git, passar por revisões de código (*pull requests*) e ser integrada diretamente a fluxos de Integração e Entrega Contínuas (CI/CD) para provisionamento automatizado de recursos em nuvem ou servidores locais.

### Q90 - Arquitetura de Software (RESTful)
* **O que a banca disse:** Caso seja utilizada a arquitetura RESTful, a API será stateless, ou seja, o servidor completará cada solicitação do cliente independentemente de todas as solicitações anteriores, e todas as solicitações serão separadas e desconectadas entre si. (CERTO)
* **O Erro (O Quê):** A questão está correta. O erro na hora da prova foi achar que o servidor mantém contexto ou conexão ativa contínua entre os pedidos do cliente.
* **A Regra (Por Quê):** O princípio *Stateless* (sem estado) obriga que cada requisição HTTP seja autossuficiente e contenha *todas* as informações e credenciais necessárias para ser processada. O servidor REST não guarda "memória" de sessões anteriores.

### Q91 - Engenharia de Software (Padrões GoF)
* **O que a banca disse:** O abstract factory é de criação e facade é estrutural; o facade separa a construção de um objeto complexo da sua representação. (ERRADO)
* **O Erro (O Quê):** A banca acertou a classificação das famílias (criação/estrutural), mas injetou o conceito de outro padrão na definição do Facade.
* **A Regra (Por Quê):** Quem "separa a construção de um objeto complexo da sua representação" é o padrão criacional **Builder**. O **Facade** (estrutural) tem como objetivo fornecer uma interface unificada, de alto nível e simplificada para um subsistema complexo.

### Q92 - Engenharia de Software (Padrões GoF)
* **O que a banca disse:** O padrão composite atribui responsabilidades adicionais a um objeto dinamicamente, e o memento captura e externaliza o estado interno de um objeto para restauração futura. (ERRADO)
* **O Erro (O Quê):** A definição do Memento (no final da questão) estava correta e serviu de isca, mas a definição do primeiro padrão estava invertida.
* **A Regra (Por Quê):** Quem "atribui responsabilidades adicionais dinamicamente" é o **Decorator**. O padrão **Composite** serve para compor objetos em estruturas de árvore, representando hierarquias do tipo parte-todo (ex: diretórios e arquivos).

### Q96 - Infraestrutura e Cloud (Kubernetes)
* **O que a banca disse:** Ao executar o arquivo YAML descrito, será criado um deployment com uma imagem do NGINX. (ERRADO)
* **O Erro (O Quê):** Ignorar a linha de declaração de tipo do recurso dentro do código e assumir o padrão por causa da imagem do NGINX.
* **A Regra (Por Quê):** O arquivo YAML da prova contém explicitamente a linha `kind: Service`. Logo, ele aciona a criação de um serviço de rede (neste caso, um `LoadBalancer`), e não um recurso do tipo `Deployment`. 

### Q98 - Infraestrutura e Cloud (Kubernetes)
* **O que a banca disse:** O kube-scheduler é o escalonador do Kubernetes e sua função consiste em controlar o aumento e a diminuição da quantidade de pods de acordo com as configurações de consumo. (ERRADO)
* **O Erro (O Quê):** Confundir "agendamento" (scheduling/kube-scheduler) com "autoescalonamento" (autoscaling/HPA).
* **A Regra (Por Quê):** O **kube-scheduler** é o componente responsável apenas por decidir em qual *Node* (nó/máquina) um Pod recém-criado irá rodar. Quem monitora o consumo e controla o aumento e diminuição da quantidade de Pods é o **HPA** (Horizontal Pod Autoscaler).

### Q101 - Observabilidade (Prometheus)
* **O que a banca disse:** A métrica do tipo gauge, suportada pelo Prometheus, representa um contador único para representar a quantidade de chamadas para um endpoint HTTP. (ERRADO)
* **O Erro (O Quê):** Inversão dos conceitos básicos de métricas de observabilidade.
* **A Regra (Por Quê):** Uma métrica **Gauge** é um medidor flexível que pode subir e descer (ex: uso de CPU, uso de memória, temperatura). Para contabilizar a quantidade de chamadas a um endpoint HTTP (um número que apenas incrementa, nunca diminui), utiliza-se o tipo **Counter**.