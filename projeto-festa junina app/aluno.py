#Metodo construtor _init_
#Metodo especial _str_ 


class Alunos:

    alunos =[]
    def ___init__(self, nome, turmas,  elegancia, desenvoltura, simpatia,  item_reciclavel ):
        self._nome = nome
        self._turmas = turmas
        self._elegancia = elegancia
        self._desenvoltura = desenvoltura
        self._simpatia = simpatia
        self._item_reciclavel = item_reciclavel
        self._notas = []


    def ___str__(self):
        return f'{self._nome} | {self._turma} | {self.nota} | {self.categoria}
    
    
    def __init__(self, Aluno, Mister, TI):