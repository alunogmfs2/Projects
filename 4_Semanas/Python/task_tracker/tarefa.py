"""
!Requisitos
*A aplicação deve ser executada a partir da linha de comando, aceitar ações e entradas do usuário como argumentos e armazenar as tarefas em um arquivo JSON. O usuário deve ser capaz de:

Adicionar, atualizar e excluir tarefas
Marcar uma tarefa como em progresso ou concluída
Listar todas as tarefas
Listar todas as tarefas concluídas
Listar todas as tarefas não concluídas
Listar todas as tarefas em progresso
*Aqui estão algumas restrições para guiar a implementação:

Você pode usar qualquer linguagem de programação para construir este projeto.
Use argumentos posicionais na linha de comando para aceitar entradas do usuário.
Use um arquivo JSON para armazenar as tarefas no diretório atual.
O arquivo JSON deve ser criado se não existir.
Use o módulo nativo do sistema de arquivos da sua linguagem de programação para interagir com o arquivo JSON.
Não use nenhuma biblioteca ou framework externo para construir este projeto.
Certifique-se de lidar com erros e casos extremos graciosamente.
!Exemplo
*A lista de comandos e seu uso é dada abaixo:

*# Adicionando uma nova tarefa
*task-cli add "Comprar mantimentos"
*# Saída: Tarefa adicionada com sucesso (ID: 1)

*# Atualizando e excluindo tarefas
*task-cli update 1 "Comprar mantimentos e cozinhar jantar"
*task-cli delete 1

*# Marcando uma tarefa como em progresso ou concluída
*task-cli mark-in-progress 1
*task-cli mark-done 1

*# Listando todas as tarefas
*task-cli list

*# Listando tarefas por status
*task-cli list done
*task-cli list todo
*task-cli list in-progress

!Propriedades da Tarefa
*Cada tarefa deve ter as seguintes propriedades:

*id: Um identificador único para a tarefa
*description: Uma breve descrição da tarefa
*status: O status da tarefa (todo, in-progress, done)
*createdAt: A data e hora em que a tarefa foi criada
*updatedAt: A data e hora em que a tarefa foi atualizada pela última vez
*Certifique-se de adicionar essas propriedades ao arquivo JSON ao adicionar uma nova tarefa e atualizá-las ao atualizar uma tarefa.
"""