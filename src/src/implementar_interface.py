import interface


def exemplo(**kwargs):
    """função de exemplo para ser usada em um botão"""
    print("a")


def setarbots(janela: interface.Janela):
    """função para criar e adicionar botões na janela"""
    bot1 = interface.Botao(10, 10, 0, 0, "exemplo", "1", 30,
                           [120, 120, 120], exemplo)
    janela.addBotões([bot1])


def setartextos(janela: interface.Janela):
    """função para criar e adicionar textos na janela"""
    text1 = interface.Texto(10, 50, 30, "aaa111aa\naaa", "1")
    janela.addTextos([text1])


def setarinputs(janela: interface.Janela):
    """função para criar e adicionar inputs na janela"""
    inpu1 = interface.Inp(10, 130, 10, 30, "", "1")
    janela.addInputs([inpu1])


def setarquads(janela: interface.Janela):
    """função para criar e adicionar quadrados na janela"""
    quad1 = interface.Quadrado(150, 50, 10, [10, 10, 10])
    janela.addQuads([quad1])


def main():
    """inicia um objeto Janela, seta suas caracteristicas iniciais, 
    assim como seu botões, textos inputs e imagens. retorna o objeto"""
    janela = interface.Janela(300, 200, "menu")
    setarbots(janela)
    setartextos(janela)
    setarinputs(janela)
    setarquads(janela)
    janela.iniciar()
    return janela


if __name__ == "__main__":
    janela = main()
    janela.main_loop()