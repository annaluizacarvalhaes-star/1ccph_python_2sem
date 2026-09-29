from disciplina import Disciplina


class Aluno:
    def __init__(self,nome, rm, curso):
        self.nome = nome
        self.rm = rm
        self.curso = curso
        self.disciplinas = [] # Lista de objetos disciplina
        self.notas_por_disciplina = {}

    def matricular(self, disciplina: Disciplina):
        self.disciplinas.append(disciplina)
        self.notas_por_disciplina.setdefault(disciplina.nome, [])

    def adicionar_nota(self, disciplina: Disciplina, nota: float):
        self.notas_por_disciplina[disciplina.nome].append(nota)

    def calcular_media_d(self, d: Disciplina) -> float:
        notas = self.notas_por_disciplina.get(d.nome, [])
        if not notas:
            return 0
        return sum(notas) / len(notas) # sum = soma todos os valores dentro do array, e divide pela quantidade de atributos (len)

    def calcular_media_geral(self) -> float:
        medias = []
        for d in self>disciplinas:
            media_d = self>calcular_media_d(d)
            medias.append(media_d)

        return sum(medias)/len(medias)