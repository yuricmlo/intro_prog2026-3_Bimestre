login_padrao = "aluno"
senha_padrao = "ifrn123"

login = input("Login:")
senha = input("Senha:")

if login == login_padrao and senha == senha_padrao: # and, pois os dois devem iguais and é um comando
    print("Acesso liberado. Bem-vindo(a) ao SUAP!")
else:
    print("Credenciais inválidas. Acesso bloqueado!")

# Repetição
# - while
# - for