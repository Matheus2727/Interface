import interface


def exemplo(**kwargs):
    """exemplo de função para ser usada em um botão"""
    print("a")


def setarbots(grupo:interface.Grupo, janela: interface.Janela):
    """exemplo de função para criar e adicionar botões na janela"""
    bot1 = interface.Botao(10, 10, 0, 0, "exemplo", "1", 30,
                           [120, 120, 120], exemplo)
    bot_troca = interface.Botao(250, 10, 0, 0, "->", "1", 30,
                           [120, 120, 120], grupo.trocar_janela, {"alvo": "opt"})
    janela.addBotões([bot1, bot_troca])


def setarbots2(grupo: interface.Grupo, janela: interface.Janela):
    """exemplo de função para criar e adicionar botões na janela"""
    bot1 = interface.Botao(10, 10, 0, 0, "exemplo", "1", 30,
                           [120, 120, 120], exemplo)
    bot_troca = interface.Botao(150, 10, 0, 0, "<-", "1", 30,
                           [120, 120, 120], grupo.trocar_janela, {"alvo": "menu"})
    janela.addBotões([bot1, bot_troca])


def setartextos(janela: interface.Janela):
    """exemplo de função para criar e adicionar textos na janela"""
    text1 = interface.Texto(10, 50, 30, "aaa111aa\naaa", "1")
    janela.addTextos([text1])


def setarinputs(janela: interface.Janela):
    """ exemplo de função para criar e adicionar inputs na janela"""
    inpu1 = interface.Inp(10, 130, 10, 30, "", "1")
    janela.addInputs([inpu1])


def setarquads(janela: interface.Janela):
    """exemplo de função para criar e adicionar quadrados na janela"""
    quad1 = interface.Quadrado(150, 50, 10, [10, 10, 10])
    janela.addQuads([quad1])


def main():
    """inicia objetos Janela e um objeto Grupo, seta suas caracteristicas iniciais, 
    assim como seu botões, textos inputs e imagens. retorna o objeto Grupo com
    as janelas armazenadas"""
    grupo = interface.Grupo()
    janela = interface.Janela(300, 200, "menu")
    janela2 = interface.Janela(200, 200, "opt")
    grupo.adicionar_janelas([janela, janela2])
    grupo.trocar_janela("menu")
    setarbots(grupo, janela)
    setarbots2(grupo, janela2)
    setartextos(janela)
    setarinputs(janela)
    setarquads(janela)
    return grupo


if __name__ == "__main__":
    grupo = main()
    grupo.main_loop()