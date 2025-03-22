# Github-Forkinator

> **Nota:**  
> Atualmente, o repositório contém apenas um script simples que funciona como **prova de conceito**.  
> Ele realiza exclusivamente o embaralhamento de colaboradores entre repositórios GitHub, sem interface gráfica ou funcionalidades adicionais.  
> O aplicativo completo ainda está em desenvolvimento e será construído aos poucos, sempre que houver tempo disponível.  
> Mesmo assim, decidi disponibilizar o script agora, já que ele resolve a parte mais trabalhosa do processo proposto e pode ser útil por si só.


Uma aplicação em Python para facilitar a integração do Git e GitHub em ambientes educacionais, promovendo a colaboração, revisões de código e boas práticas entre alunos.

## Visão Geral

Esse projeto nasceu de uma conversa descontraída com um professor que buscava uma maneira prática de aplicar Git e GitHub com alunos iniciantes. A ideia era incentivar a colaboração e boas práticas, mas também evitar que os alunos apenas "clicassem para aprovar" os pull requests dos amigos sem ler de verdade. Pra isso, ele queria rotacionar os colaboradores entre diferentes repositórios durante as atividades.

Apesar de ser algo que daria pra fazer manualmente, resolvi automatizar por diversão e criar uma ferramenta que facilitasse esse processo. Assim surgiu o **Github-Forkinator**, que ajuda a:

- **Forçar a colaboração:** Com revisões de código obrigatórias.
- **Rotacionar colaboradores:** Pra manter a atenção e promover análise crítica entre diferentes colegas.
- **Diversificar experiências:** Colocando os alunos em contato com diferentes bases de código ao longo do curso.

## Tecnologias Utilizadas

- **Python 3.12.9**

## Objetivo

Desenvolver uma aplicação com interface gráfica simples para auxiliar na configuração de repositórios e na rotação de colaboradores entre forks, tornando o aprendizado mais dinâmico e colaborativo.

## Fluxo de Trabalho Proposto

1. **Criação do Repositório Base:**  
   - Estruturação de um repositório com regras (ruleset) que enforce revisões e outras boas práticas.
   
2. **Fork dos Repositórios:**  
   - Cada fork herda o ruleset do repositório pai.
   - Convite aos alunos para colaborarem nos respectivos forks.
   
3. **Embaralhamento dos Colaboradores:**  
   - A funcionalidade principal da aplicação é “embaralhar” os colaboradores entre os repositórios, garantindo a rotação e a diversificação na revisão dos códigos.

## Funcionalidades

- **Randomização de Colaboradores:**  
  - Distribuição aleatória dos colaboradores entre os repositórios fornecidos.
  
- **Configuração Flexível:**  
  - Permite definir opcionalmente a quantidade de colaboradores por repositório. Se não informado ou se o valor for menor que zero, utiliza-se a média dos colaboradores entre os repositórios.

- **Integração com GitHub:**  
  - Opera via API do GitHub, exigindo que o usuário possua as credenciais apropriadas e permissões para os repositórios.

## Instalação e Configuração

1. **Pré-requisitos:**
   - Instalar o Python 3.12.9 ou versão mais recente.
   - Possuir uma conta GitHub com token de acesso que possua as permissões necessárias.

2. **Clonagem do Repositório:**
   
```bash  
git clone https://github.com/seu-usuario/github-forkinator.git  
cd github-forkinator  
```

3. **Instalação das Dependências:**
   
```bash  
pip install -r requirements.txt  
```

4. **Configuração das Credenciais:**
   - Insira suas credenciais no arquivo `.env`.

## Uso

Dentro da pasta `scripts`, execute o script principal:

```bash  
python collaborator_randomizer.py --repos nome-do-meu-projeto1 meu-projeto2 outro-repo [--qtd 5]  
```

### Parâmetros

- `--repos`:  
  Lista os repositórios (separados por espaço).  
  *Exemplo:*  
  `--repos projeto1 projeto2 projeto3`

- `--qtd`:  
  (Opcional) Define o número de colaboradores por repositório.  
  Se não informado ou se o valor for menor que zero, o script utilizará a média de colaboradores entre todos os repositórios.

## Considerações Finais

- **Permissões:** Certifique-se de que você é o proprietário dos repositórios e que seu token do GitHub possui as permissões necessárias.
- **Ambiente Educacional:** Ideal para professores que desejam incentivar práticas colaborativas e revisões de código entre alunos.
- **Evolução do Projeto:** A ideia começou com um script simples só por diversão, mas pode crescer com o tempo, ganhando novas funcionalidades conforme a necessidade.

## Contribuição

Contribuições são bem-vindas!  
- Abra uma issue para sugerir melhorias ou reportar problemas.
- Envie pull requests com suas alterações para avaliação.

## Licença

Este projeto está licenciado sob a Licença MIT — veja o arquivo [LICENSE](LICENSE) para detalhes.

