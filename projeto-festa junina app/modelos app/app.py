from modelos.jurados import Jurado
from modelos.aluno import Aluno
    
mateus = Aluno('mateus', 'TI', 'Mister')
jurado = Jurado('Carléia', 'Educacional')

jurado.atribuir_nota(mateus, 5, 5, 5, 5)
jurado.atribuir_nota(mateus, 6, 6, 6, 6)

print(mateus)

if __name__ == "__main__":
 
def main():