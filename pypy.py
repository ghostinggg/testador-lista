casellato = ['Emocionado','Burro','Mongoloide','Simp']
respostaSim = ['Sim', 'sim']
respostaNao = ['Não', 'não', 'Nao', 'nao']
print('Lista de coisas que o Casellato é: ')
for i in casellato:
    if (i <= casellato[2]):
        print(i + ', ', end='')
    if (i == casellato[3]):
        print(i + '.')

resposta = input('\nCasellato, vc vai parar de ser gadinho de mulher?: ')
if (resposta in respostaSim):
    casellato.pop(3)
    casellato.pop(1)
    print('\nFinalmente')
    print("\nLista de coisas que o Casellato é: " + str(casellato[0]) +" ," + str(casellato[1]) + ", Menos Burro.")

else:
   if (resposta in respostaNao):          
      print('\nEu te odeio muito')
      casellato.pop(1)
      casellato.append('Muito Burro')
      print('\nLista de coisas que o Casellato é: ' + str(casellato[0]) + ', '
       + str(casellato[1]) + ', ' + str(casellato[2]) + ', ' + str(casellato[3]), end='.')
    
