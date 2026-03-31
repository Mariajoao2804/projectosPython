def exibir_info(**info):
    for chave, valor in info.items():
        print(f"{chave.replace("_", " ").title()}: {valor}")
exibir_info(nome="Carlos", idade=25, cidade="Luanda")