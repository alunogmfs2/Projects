function addTodo() {
    const todoInput = document.getElementById('newTodo');
    const todoList = document.getElementById('todoList');

    if (todoInput.value) {
        const newTodo = document.createElement('li');
        newTodo.textContent = todoInput.value;
        todoList.appendChild(newTodo);
        todoInput.value = '';
    }

    // Adicionando um botão de deletar ao novo item
    const deleteButton = document.createElement('button');
    deleteButton.textContent = 'X';
    deleteButton.addEventListener('click', () => {
        todoList.removeChild(newTodo);   

    });
    newTodo.appendChild(deleteButton);
}