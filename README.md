# C214 - Teste Unitário _Mock_

## Instruções

- Utilize os slides, livros e aulas como referência para resolver o exercício.
- Códigos realizados durante a aula podem ser encontrados [aqui](https://github.com/chrislima-inatel/C214).

## Objetivos

- Aprimorar os conhecimentos em teste unitário e teste mock.
- Ao final, o link do repositório com a solução deve ser enviada.
- Não deixe de contactar o professor/monitor(a) caso tenha _**QUALQUER**_ dúvida.

Bons Estudos!

## Questão 1

Teste uma classe responsável por popular uma página _WEB_ com informações referentes ao horário de atendimento dos professores do Inatel. O horário de atendimento é retornado por um **servidor remoto** em um JSON em formato String. Não é necessário demonstrar o funcionamento da página _WEB_, somente o teste.

### Observações

- Crie pelo menos 3 testes para cenários de sucesso e 3 para falha.
- Considere que o JSON retornado pelo servidor remoto possui, no mínimo, aseguinte estrutura:

  ```json
  {
    "nomeDoProfessor": "<nome_do_professor",
    "horarioDeAtendimento": "<horario_de_atendimento",
    "periodo": "<integral_ou_noturno>"
  }
  ```

- Utilize a linguagem da sua escolha para realizar os testes.
- Caso seja necessário, os objetos _mock_ devem ser criados manualmente.
- O último código feito em aula pode ser encontrado [aqui](https://github.com/chrislima-inatel/C214/tree/main/aula-07-mock-novo).
- O uso correto de versionamento e gerência de dependências será avaliado.

## Resolução

Com o Python instalado, execute os seguintes comandos no `cmd`:

```
python -m venv env
env\Scripts\activate
pip install -r requirements.txt
python -m unittest -v src.tests.inatel.__main__
```
