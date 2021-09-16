""""
Crie um programa que leia uma expressão qualquer que use parênteses. Seu programa deve analisar a expressão passada e falar se ela é válida ou inválida.
  Ex: expressão lida:  ((a + b) * c ) : expressão válida
    expressão lida:      (a + b) * c ) : expressão inválida
"""

def validarExpressao(exp: str):
  res = {
    'res': 'expressão inválida!',
    'msg': 'erro!'
  }
  if (( '(' not in exp ) and ( ')' not in exp )):
    res['msg'] = 'Expressão não utilizou parênteses!'
  else:
    abrir = []
    fechar = []

    for i in range(len(exp)):
      if (exp[i] == '('):
        abrir.append(i)
      elif (exp[i] == ')'):
        fechar.append(i)

    if (len(abrir) != len(fechar)):
      res['msg'] = 'Expressão não tem pares de parênteses correspondentes'
    else:
      for i in range(len(abrir)):
        if (abrir[i] > fechar[i]):
          res['msg'] = 'Primeiro é necessário abrir o parênteses!'
        else:
          res['res'] = 'Expressão Válida!'
          res['msg'] = 'Expressão correta!'
  return res        

expressao = input('Digite uma expressão que use parênteses: ')
res = validarExpressao(expressao)
print(f'Resultado: {res["res"]}\nMensagem: {res["msg"]}')