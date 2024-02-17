'''
Projeto - medidor de velocidade

1. - Valor da velocidade
2. - Se valor da velocidade for abaixo de 80 km/h exibir "Não houve multa"
   - Caso esteja até 10 km acima,ou seja, entre 80 a 90 km/h exibir "Levou multa leve"
   - Caso esteja entre 11 a 20 km acima da velocidade máxima,ou seja, entre 91 a 100 km/h exibir "Levou multa grave"
   - Caso esteja acima de 20 km acima da velocidade máxima,ou seja, acima de 100 km/h exibir "Levou multa gravíssima"
3. tever ser números
4.
Se for até 80 km/h exibir "Não houve multa"
Entre 80 a 90 km/h exibir "Levou multa leve"
Entre 91 a 100 km/h exibir "Levou multa grave"
Acima de 100 km/h exibir "Levou multa gravíssima"
5.
input print digite o valor da velocidade
if velocidade <= 80
   print Não houve multa
elif velocidade >= 81 or velocidade = 90
   print Levou multa leve
elif velocidade >= 91 or velocidade = 100
   print Levou multa grave
elif velocidade >= 100
   print Levou multa gravíssima
'''
velocidade = int(input("digite o valor da velocidade: "))
velocidade_maxima = 80
if velocidade <= velocidade_maxima:
   print('Não houve multa')
elif velocidade > velocidade_maxima and velocidade <= velocidade_maxima + 10:
   print("Levou multa leve")
elif velocidade >= velocidade_maxima + 11 and velocidade <= velocidade_maxima + 20:
   print ("Levou multa grave")
elif velocidade > velocidade_maxima + 20:
   print("Levou multa gravíssima")
