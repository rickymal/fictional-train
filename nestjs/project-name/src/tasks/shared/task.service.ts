import { Injectable } from '@nestjs/common';
import { Task } from './task';

@Injectable()
export class TaskService {
  tasks: Task[] = [
    { id: 1, description: 'Tarefa 1', completed: false },
    { id: 2, description: 'Tarefa 1', completed: false },
    { id: 3, description: 'Tarefa 1', completed: true },
    { id: 4, description: 'Tarefa 1', completed: false },
    { id: 5, description: 'Tarefa 1', completed: false },
    { id: 6, description: 'Tarefa 1', completed: false },
    { id: 7, description: 'Tarefa 1', completed: false },
    { id: 8, description: 'Tarefa 1', completed: false },
    { id: 9, description: 'Tarefa 1', completed: false },
    { id: 10, description: 'Tarefa 1', completed: true },
  ];

  getAll() {
    return this.tasks;
  }

  getById(id: number) {
    const task = this.tasks.find((e) => e.id == id);
    return task;
  }

  create(task: Task) {
    let lastId = 0;
    if (this.tasks.length > 0) {
      lastId = this.tasks[this.tasks.length - 1].id;
    }

    task.id = lastId + 1;
    return task;
  }

  update(task: Task) {
    const taskArray = this.getById(task.id);
    if (taskArray) {
      taskArray.description = task.description;
      taskArray.completed = task.completed;
    }

    return taskArray;
  }

  delete(id: number) {
    const index = this.tasks.findIndex((v) => v.id == id);
    this.tasks.splice(index, 1);
  }

  
}
