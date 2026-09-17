def sistema_de_senha():
    password = input("password you want to create: ")
    n = 3
    
    while n > 0:
        try:
            try_ = input("Write the password: ")

            if not isinstance(try_, str):
                raise TypeError("the value is not a string, try again")

            if try_ == password:
                print("🔓 access allowed")
                return 0

            n -= 1
            raise ValueError(f"The password is incorrect! Attempts remaining: {n}")

        except TypeError as not_string:
            print(f"❌ Erro de Sistema: {not_string}")

        except ValueError as not_the_password:
            print(f"⚠️ Erro de Autenticação: {not_the_password}")

    print("Account blocked due to too many attempts!")
    return 1

resultado = sistema_de_senha()
print(f"Código de retorno do sistema: {resultado}")
