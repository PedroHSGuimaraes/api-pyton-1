


lista_alunos = [ 
  {
    'id':1,
    'nome': 'Pedro'
    
  },
  { 
  'id':2,
  'nome': 'Giuliana'
  }
  
]







def criar_aluno(aluno:str):
  
  novo_aluno = aluno
  lista_alunos.append(novo_aluno)
  return aluno

criar_aluno({'id':3, 'nome': 'Pedro Henrique ',})



def ler_aluno(id):
  for aluno in lista_alunos:
    if aluno['id'] == id:
      return print(aluno.get('nome'))
    
    
ler_aluno(2)

    
def ler_todos_alunos():
  for aluno in lista_alunos:
    print(aluno['nome'])


ler_todos_alunos()


def atualizar_aluno(id, nome):
  for aluno in lista_alunos:
    if aluno['id'] == id:
      aluno['nome'] = nome
      return aluno
    
atualizar_aluno(1, 'pedro henrique')    

print (lista_alunos)







def deletar_aluno(id):
  for aluno in lista_alunos:
    if aluno['id'] == id:
      lista_alunos.remove(aluno)       
      return lista_alunos 
    

    
deletar_aluno(2)
print(lista_alunos)









