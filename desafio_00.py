nome = input("Digite o seu nome: ")
salario = int(input("Digite a sua remuneração: "))
porcentagem_bonus = float(input("Digite o seu % de bonus: "))

def calcula_bonus(remun, porc):
    bonus= 1000+(remun*porc)
    
    return bonus

print("Saudações meu querido "+nome+ ", o seu bônus foi de "+str(calcula_bonus(salario, porcentagem_bonus)))