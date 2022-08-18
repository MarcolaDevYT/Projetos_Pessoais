#imc=peso/altura**2
peso = float(input('Qual seu peso em KG? '))
altura = float(input('Qual é sua altura em metros? '))
imc = peso/(altura**2)
print(f'O seu IMC é {imc:.2f}')
if imc <= 18.5:
    print('Magreza')
if imc >= 18.5 and imc <= 24.9:
    print("Normal")
if imc >= 25 and imc <= 29.9:
    print('Sobrepeso')
if imc >= 30:
    print('Obesidade')
