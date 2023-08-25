from fastapi import FastAPI
from data import lista_alunos


app= FastAPI()




@app.get('/get-alunos')
async def get():
    return lista_alunos 


@app.get('/get-aluno/{id}')
async def get_aluno(id: int):
    id_int = id - 1
    return lista_alunos[id_int]

@app.post('/add-aluno')
async def post (aluno: str):
    novo_aluno = {'id': len(lista_alunos) + 1, 'nome': aluno}
    lista_alunos.append(novo_aluno)
    return lista_alunos




@app.put('/update-aluno/{id}')
async def update (id: int, aluno: str):
    id_int = id - 1
    lista_alunos[id_int]['nome'] = aluno
    return lista_alunos[id_int]


@app.delete('/delete-aluno/{id}')
async def delete (id: int):
    id_int = id - 1
    lista_alunos.pop(id_int)

    return lista_alunos


    news_id= 0 
    for i in lista_alunos:
        if i['id'] > news_id:
            news_id = i['id']
    return news_id


