from aluno import Aluno
from disciplina import Disciplina
# classe geralmente começa co letramaiúscula

# CRIAR / INSTANCIAR 1 Aluno
aluno1 = Aluno('João', '123456','Ciência da Computação')

# CRIAR / INSTANCIAR 2 DICIPLINAS
prompt_ia = Disciplina('Prompt IA', 'Jorge')
sers = Disciplina('Soluções Renováveis', 'André')

# MATRICULAR O ALUNO NAS DISCIPLINAS
aluno1.matricular(prompt_ia)
aluno1.matricular(sers)

print(aluno1.disciplinas[0].nome)
print(aluno1.disciplinas[1].professor)

# ADICIONAR NOTAS DO ALUNO REFERENTE ÀS DISCIPLINAS
aluno1.adicionar_nota(prompt_ia, 10)
aluno1.adicionar_nota(prompt_ia, 8)
aluno1.adicionar_nota(sers, 5)
aluno1.adicionar_nota(sers, 3)

print("----------------------------- \n")
print(aluno1.notas_por_disciplina)

print("----------------------------- \n")
print(aluno1.calcular_media_d(sers))