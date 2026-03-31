def funcao_generica(arg_fixo, *args, **kwargs):
    print(f"Argumento Fixo: {arg_fixo}")
    print(f"Argumentos Posicionais (*args): {args}")
    print(f"Argumentos Nomeados (**kwargs): {kwargs}")
funcao_generica(10, 20, 30, nome="Maria", idade=30)
# Saída:
# Argumento Fixo: 10
# Argumentos Posicionais (*args): (20, 30)
# Argumentos Nomeados (**kwargs): {"nome": "Maria", "idade": 30}