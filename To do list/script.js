const form = document.getElementById('taskForm');
const taskList = document.getElementById('taskList');
let tasks = [];

form.addEventListener('submit', function (e) {
  e.preventDefault();
  const taskText = document.getElementById('taskInput').value;
  const taskDateTime = document.getElementById('taskDateTime').value;

  const task = {
    id: Date.now(),
    text: taskText,
    dateTime: taskDateTime,
    completed: false
  };

  tasks.push(task);
  displayTasks();
  form.reset();
});

function displayTasks() {
  taskList.innerHTML = '';

  tasks.forEach(task => {
    const li = document.createElement('li');
    li.className = task.completed ? 'completed' : '';

    li.innerHTML = `
      <div><strong>${task.text}</strong></div>
      <div class="time">${new Date(task.dateTime).toLocaleString()}</div>
      <div class="actions">
        <button onclick="toggleComplete(${task.id})">✔</button>
        <button onclick="editTask(${task.id})">✏</button>
        <button onclick="deleteTask(${task.id})">🗑</button>
      </div>
    `;

    taskList.appendChild(li);
  });
}

function toggleComplete(id) {
  tasks = tasks.map(task =>
    task.id === id ? { ...task, completed: !task.completed } : task
  );
  displayTasks();
}

function deleteTask(id) {
  tasks = tasks.filter(task => task.id !== id);
  displayTasks();
}

function editTask(id) {
  const task = tasks.find(t => t.id === id);
  const newText = prompt('Edit your task:', task.text);
  if (newText) {
    task.text = newText;
    displayTasks();
  }
}