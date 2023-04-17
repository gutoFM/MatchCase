estudo = int(input("Digite a opção para visualizar os estudos (1 ao 4): "))

match estudo:

    case 1:
        opcao = int(input("Escolha a opção desejada de 1 a 5: "))
        match opcao:
            case 1:
                print("Você escolheu a opção 1")
            case 2:
                print("Você escolheu a opção 2")
            case 3:
                print("Você escolheu a opção 3")
            case 4:
                print("Você escolheu a opção 4")
            case 5:
                print("Você escolheu a opção 5")
            case _:
                print("Opção errada!")

    case 2:
        print("""Digite o número da opção do destino desejado: \n
              (1) São Paulo \n
              (2) Rio de Janeiro \n
              (3) Curitiba \n
              (4) Brasilia \n
              (5) Florianópolis \n""")

        opcao = int(input("Digite o número do destino (1 ao 5): "))

        match opcao:
            case 1:
                print("O destino do trem para São Paulo partirá na PLATAFORMA 1!")
                print("Obrigado por comprar conosco")
            case 2:
                print("O destino do trem para Rio de Janeiro partirá na PLATAFORMA 2!")
                print("Obrigado por comprar conosco")
            case 3:
                print("O destino do trem para Curitiba partirá na PLATAFORMA 3!")
                print("Obrigado por comprar conosco")
            case 4:
                print("O destino do trem para Brasilia partirá na PLATAFORMA 4!")
                print("Obrigado por comprar conosco")
            case 5:
                print("O destino do trem para Florianópolis partirá na PLATAFORMA 5!")
                print("Obrigado por comprar conosco")
            case _:
                print("Digite uma oção válida!")
                
    case 3:
        print("""O cardápio de vinho estará disponivel abaixo: \n
              (1) Casa Valduga Gran \n
              (2) Casa Silva Gran Terrois los Carménère \n
              (3) Chocalan Origen Viognier \n
              (4) Miolo Demi-sec Reserva especial 2005 \n
              (5) Casa Silva Terrois Cabernet Savignon \n""")
              
        vinho = int(input("Digite o número do vinho desejado no catálogo: ")) 

        match vinho:
            case 1:
                print("O vinho escolhido foi o Casa Valduga Gran. O preço dele é de R$160,00")
            case 2:
                print("O vinho escolhido foi o Casa Silva Gran Terrois los Carménère. O preço dele é de R$130,00")
            case 3:
                print("O vinho escolhido foi o Chocalan Origen Viognier. O preço dele é de R$180,00")
            case 4:
                print("O vinho escolhido foi o Miolo Demi-sec Reserva especial 2005. O preço dele é de R$90,00")
            case 5:
                print("O vinho escolhido foi o Casa Silva Terrois Cabernet Savignon. O preço dele é de R$100,00")
            case _:
                print("Escolha uma opção válida!")
                
                
    case 4:
        print("Escolha 2 número para depois escolher uma operação matemática!")
        num1 = float(input("Primeiro número: "))
        num2 = float(input("Segundo número: "))
        
        
        
        
        
        escolha = int(input("""Digite o número da sua escolha da operação desejada: \n
                            (1) Adição \n
                            (2) Subtração \n
                            (3) Multiplicação \n
                            (4) Divisão: \n"""))
                            
        match escolha:
            case 1:
                adic = num1 + num2
                print("A adição entre os numeros %f e %f é de %f" % (num1, num2, adic))
            case 2:
                sub = num1 - num2
                print("A subtração entre os numeros %f e %f é de %f" % (num1, num2, sub))
            case 3:
                multi = num1*num2
                print("A subtração entre os numeros %f e %f é de %f" % (num1, num2, multi))
            case 4:
                div = num1/num2
                