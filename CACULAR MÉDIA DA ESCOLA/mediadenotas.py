n1 = float(input('Coloque a sua nota do primeiro bimestre: '))
n2 = float(input('Coloque sua nota do segundo bimestre: '))
n3 = float(input('Coloque sua nota do terceiro bimestre: '))
n4 = float(input('Coloque sua nota do quarto bimestre: '))
soma_das_notas = n1+n2+n3+n4
média = soma_das_notas/4
print(f'Sua média anual foi: {média:.2f}\nE sua soma de todas as notas foi: {soma_das_notas}')
if média >= 6 : {
  print('Você foi aprovado!')
} 
else : {
  print('Você foi reprovado!')
}
