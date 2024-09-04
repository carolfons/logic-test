def verifica (a):
    texto_min = a.lower() #converte o texto para minúsculo
    count = texto_min.count('a') #conta quantas vezes 'a' aparece no texto
    if count > 0:
        return f"A letra 'a' aparece {count} vez(es) na string."
    else:
        return f"A letra 'a' não aparece na string."


#exemplo de uso com entrada do usuário ------

text_user = input("Informe uma string: ")
result = verifica(text_user)
print(result)