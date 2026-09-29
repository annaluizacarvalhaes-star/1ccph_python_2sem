class Disciplina:
    def __init__(self, nome, professor):
        self.nome = nome
        self.professor = professor

    def exibir_infos(self):
        print(f"Disciplina: {self.nome} | Professor: {self.professor}")

# EXEMPLO - TEMPORÁRIO
# python = Disciplina('PCP', 'Russi')
# print(python.professor)
# python.exibir_infos()
