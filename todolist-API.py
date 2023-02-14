from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from datetime import date

app = FastAPI()

class Task(BaseModel):
    tarefa: str
    realizada: bool
    prazo: Optional[date]

task_list = [
    Task(tarefa='teste', realizada=False),
]

@app.post('/newtask')
def newTask(todo_task: Task):
    try:
        task_list.append(todo_task)
        return {'status': 'task adicionada'}
    except:
        return {'status': 'erro'}

@app.post('/listtask')
def listTaskFilter(opcao: int = 0):
    if opcao == 0:
        return task_list
    elif opcao == 1:
        return list(filter(lambda x: x.realizada == False, task_list))
    elif opcao == 2:
        return list(filter(lambda x: x.realizada == True, task_list))


@app.get('/infotask/{id}')
def getTaskByID(id: int):
    try:
        return task_list[id]
    except:
        return {'status':'erro'}

@app.get('/alltasks')
def listAllTasks():
        return task_list


@app.post('/updatetask')
def updateTask(id: int):
    try:
        task_list[id].realizada = not task_list[id].realizada
    except:
        return {'status':'erro'}

@app.delete('/deletetask')
def deleteTask(id: int):
    try:
        del task_list[id]
        return 'task deletada '
    except:
        return {'status':'erro'}
