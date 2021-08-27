import interface


def exemplo(**kwargs):
    print("a")


def setarbots(janela: interface.Janela):
    bot1 = interface.Botao(10, 10, 0, 0, "exemplo", "1", 30,
                           [120, 120, 120], exemplo)
    janela.addBotões([bot1])


def setartextos(janela: interface.Janela):
    text1 = interface.Texto(10, 50, 30, "aaa111aa\naaa", "1")
    janela.addTextos([text1])


def setarinputs(janela: interface.Janela):
    inpu1 = interface.Inp(10, 130, 10, 30, "", "1")
    janela.addInputs([inpu1])


def main():
    janela = interface.Janela(300, 200, "menu")
    setarbots(janela)
    setartextos(janela)
    setarinputs(janela)
    janela.iniciar()
    janela.main_loop()


if __name__ == "__main__":
    main()
