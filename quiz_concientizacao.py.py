import tkinter #importando tKinter
from tkinter import * #importando tudo que está dentro da biblioteca
from tkinter import ttk #Importando a classe 
from functools import partial
#import funcoes 
#cores =========================================================
fundo_da_tela="#DCDCDC"#cor hexadecimal
cor_quadro = "#C0C0C0"
escrito = "black"
escrito2 = "#C852D8"
cor_menu="#C54FDE"
arm_respostas=[]
#janela mãe C0C0C0=============================================================
janela = Tk ()
janela.title("Quiz da concientização") 
janela.geometry("1000x600+100+100")
janela.configure(bg=fundo_da_tela)
#import funcoes=======================================================
def acao_menu(botao):
    if(botao==botao1):
        menu ["text"] = "certo"
        p1()
    else:
        encerramento= Label(janela, text="Programa encerrado, agradecemos a sua atenção ")
        encerramento.pack()


def p1():
    #limpando a tela
    botao1.destroy() #funciona 
    botao2.destroy()
    menu.destroy()
    menu_quadro.destroy()
    #menu_quadro.destroy() width=600, height=300
    quadro.pack(ipady= 50, ipadx=50)
    #pergunta 1 ================================================================================
    pergunta1 = LabelFrame(quadro, text="Primeira Pergunta: Como podemos agir para manter o banheiro mais organizado?", font="arial 20", background=cor_quadro, foreground=escrito, bd= 0 )
    pergunta1.pack(anchor=CENTER, expand=1)

    def resp(op):
            if(op==op1):
                a = Label(pergunta1,text="""Não é ético limpar os cabelos na pia
                antes de molhar todo o banheiro, devemos pensar nas próximas pessoas que usarão. 
                Molhar as mãos e não enxugar corretamente pode pingar no chão assim deixando o mesmo 
                sujo e bagunçado!""", font="arial 14", background=cor_quadro, foreground=escrito2)
                arm_respostas.append("1. A) Molhar os cabelos na pia e lavar as mãos sem enxugar corretamente!")
                a.pack()
            elif(op==op2):
                b = Label(pergunta1,text="""Parabéns, temos papéis-toalha disponíveis para uso geral, e também, 
                depois de nós outras pessoas vão utilizar o banheiro,
                logo, devemos pensar no próximo e em nós mesmos, mantendo a ordem do lugar público""", font="arial 14", background=cor_quadro, foreground=escrito2)
                arm_respostas.append("1. B)Enxugar as mãos corretamente tomando cuidado para não molhar todo o chão!")
                b.pack()
            else: 
                pergunta1.destroy()
                p2()
    #opção 1
    op1 = Button(pergunta1, text="A) Molhar os cabelos na pia e lavar as mãos sem enxugar corretamente!", font="arial 16", background=cor_quadro, foreground=escrito)
    op1 ["command"] = partial(resp, op1)
    op1.pack(padx=10, pady=10)
    #op 2
    op2 = Button(pergunta1, text="B) Enxugar as mãos corretamente tomando cuidado para não molhar todo o chão!", font="arial 16", background=cor_quadro, foreground=escrito)
    op2 ["command"] = partial(resp, op2)
    op2.pack(padx=10, pady=10)
    px = Button(pergunta1, text="Proxima pergunta", font="arial 13", background=cor_quadro, foreground=escrito)
    px ["command"] = partial(resp,px)
    px.pack(anchor=SE, expand=True, pady=20)
#pergunta 2===========================================
def p2():
    quadro.pack(ipady= 50, ipadx=50)
    pergunta2 = LabelFrame(quadro, text="Segunda Pergunta: Como podemos agir para conseguir conscientizar nossos colegas?", font="arial 20", background=cor_quadro, foreground=escrito, bd=0)
    pergunta2.pack(anchor=CENTER, expand=1)

    def resp(op):
            if(op==op1):
                a = Label(pergunta2,text="""Parabéns, todas mudanças começam por nós mesmos,
                 precisamos agir como inspiração para que todos à nossa volta melhorem conosco""", font="arial 14", background=cor_quadro, foreground=escrito2)
                arm_respostas.append("2. A) Aconselhar seus colegas através de exemplos e atitudes!")
                a.pack()
            elif(op==op2):
                b = Label(pergunta2,text="""Essa não é a melhor opção , não devemos repreender alguém sem ensinar o correto.
                é importante que as mudanças partam de nós mesmos, para que podemos colaborar 
                com a mudança dos outros à nossa volta!""", font="arial 14", background=cor_quadro, foreground=escrito2)
                arm_respostas.append("2. B) Repreender seus colegas e não fazer sua parte!")
                b.pack()
            else: 
                pergunta2.destroy()
                p3()
    #opção 1
    op1 = Button(pergunta2, text="A) Aconselhar seus colegas através de exemplos e atitudes!", font="arial 16", background=cor_quadro, foreground=escrito)
    op1 ["command"] = partial(resp, op1)
    op1.pack(padx=10, pady=10)
    #op 2
    op2 = Button(pergunta2, text="B) Repreender seus colegas e não fazer sua parte!", font="arial 16", background=cor_quadro, foreground=escrito)
    op2 ["command"] = partial(resp, op2)
    op2.pack(padx=10, pady=10)
    px = Button(pergunta2, text="Proxima pergunta", font="arial 16", background=cor_quadro, foreground=escrito)
    px ["command"] = partial(resp,px)
    px.pack(anchor=SE, expand=True, pady=20)
#pergunta 3 ======================================================
def p3():
    quadro.pack(ipady= 50, ipadx=50)
    pergunta3 = LabelFrame(quadro, text="Terceira Pergunta: Para promover um melhor clima entre os usuários do banheiro devemos:", font="arial 20", background=cor_quadro, foreground=escrito, bd=0)
    pergunta3.pack(anchor=CENTER, expand=1)

    def resp(op):
            if(op==op1):
                a = Label(pergunta3,text="""Isso aí, seguir regras comuns em um ambiente é fundamental para ter  um bom convívio, precisamos de empatia para orientar e 
                disciplina para sermos exemplos.""", font="arial 14", background=cor_quadro, foreground=escrito2)
                arm_respostas.append("3. A) Ter empatia e código de conduta!")
                a.pack()
            elif(op==op2):
                b = Label(pergunta3,text="""Seja o banheiro, ou outras áreas da escola
                são de uso coletivo, e ser egoísta não resolve os problemas de forma geral.
                o correto é conscientizar seus colegas!
                Ser organizado é de extrema importância para gerar um clima 
                melhor entre os bens comuns da escola!""", font="arial 14", background=cor_quadro, foreground=escrito2)
                arm_respostas.append("3. B) Ser egoísta e não ser organizado!")
                b.pack()
            else: 
                pergunta3.destroy()
                p4()
    #opção 1
    op1 = Button(pergunta3, text="A) Ter empatia e código de conduta!", font="arial 16", background=cor_quadro, foreground=escrito)
    op1 ["command"] = partial(resp, op1)
    op1.pack(pady=10, padx=10)
    #op 2
    op2 = Button(pergunta3, text="B) Ser egoísta e não ser organizado!", font="arial 16", background=cor_quadro, foreground=escrito)
    op2 ["command"] = partial(resp, op2)
    op2.pack(pady=10,padx=10)
    px = Button(pergunta3, text="Próxima pergunta", font="arial 16", background=cor_quadro, foreground=escrito)
    px ["command"] = partial(resp,px)
    px.pack(anchor=SE, expand=True, pady=20)
#quarta pergunta ======================================================
def p4():
    quadro.pack(ipady= 50, ipadx=50)
    pergunta4= LabelFrame(quadro, text="""Quarta Pergunta: Em sala de aula, o professor liga o ar condicionado e os alunos 
    se encontramem divergência sobre qual temperatura usar. 
    Como você lidaria com essa situação?""", font="arial 20", background=cor_quadro, foreground=escrito, bd=0)
    pergunta4.pack(anchor=CENTER, expand=1)

    def resp(op):
            if(op==op1):
                a = Label(pergunta4,text="""Parabéns, essa atitude mostra que você é uma pessoa racional  e empática
                , vamos falar sobre os meios de resolver esse problema?""", font="arial 14", background=cor_quadro, foreground=escrito2)
                arm_respostas.append("4. A) Encontrar, de uma maneira adequada, um consenso para que todos se encontrem em um ambiente agradável.")
                a.pack()
            elif(op==op2):
                b = Label(pergunta4,text="""Hmmmm, talvez essa não seja a melhor opção! Vamos rever isso? Se preocupar somente com você é uma atitude egoísta""", font="arial 14", background=cor_quadro, foreground=escrito2)
                arm_respostas.append("4. B) Se preocupar somente em resolver o seu problema, de uma maneira em que você se encontre mais confortável")
                b.pack()
            else: 
                pergunta4.destroy()
                p5()
    #opção 1
    op1 = Button(pergunta4, text="A) Chegar em um consenso para que todos se encontrem em um ambiente agradável.", font="arial 16", background=cor_quadro, foreground=escrito)
    op1 ["command"] = partial(resp, op1)
    op1.pack(pady=10, padx=10)
    #op 2
    op2 = Button(pergunta4, text="B) Se preocupar somente em resolver o seu problema, de uma maneira em que você se encontre mais confortável", font="arial 16", background=cor_quadro, foreground=escrito)
    op2 ["command"] = partial(resp, op2)
    op2.pack(pady=10,padx=10)
    px = Button(pergunta4, text="Proxima pergunta", font="arial 16", background=cor_quadro, foreground=escrito)
    px ["command"] = partial(resp,px)
    px.pack(anchor=SE, expand=True, pady=20)
#pergunta 5 ======================================
def p5():
    quadro.pack(ipady= 50, ipadx=50)
    pergunta5 = LabelFrame(quadro, text="""Quinta Pergunta: Em uma instituição de estudo, na qual você 
    encontre uma sala organizada e se mantenha nela durante o horario de aula, 
    qual é a maneira mais adequada de deixar a mesma no final?""", font="arial 20", background=cor_quadro, foreground=escrito, bd=0)
    pergunta5.pack(anchor=CENTER, expand=1)

    def resp(op):
            if(op==op1):
                a = Label(pergunta5,text="""Essa é uma atitude correta, assim você facilita a vida do proximo e também dos auxliares de limpeza.""", font="arial 14", background=cor_quadro, foreground=escrito2)
                arm_respostas.append("5. A) Junte seus materiais, confira se tudo esta organizado mantendo a sala adequada para a proxima aula")
                a.pack()
            elif(op==op2):
                b = Label(pergunta5,text="""Hmmm, mais uma vez uma atitude egoísta. Você tem certeza que essa é a melhor escolha? vamos falar sobre...  !""", font="arial 14", background=cor_quadro, foreground=escrito2)
                arm_respostas.append("5. B) Apenas saia.")
                b.pack()
            else: 
                pergunta5.destroy()
                p6()
    #opção 1
    op1 = Button(pergunta5, text="A) Junte seus materiais, confira se tudo esta organizado mantendo a sala adequada para a proxima aula", font="arial 16", background=cor_quadro, foreground=escrito)
    op1 ["command"] = partial(resp, op1)
    op1.pack(pady=10, padx=10)
    #op 2
    op2 = Button(pergunta5, text="B) Apenas saia.", font="arial 16", background=cor_quadro, foreground=escrito)
    op2 ["command"] = partial(resp, op2)
    op2.pack(pady=10, padx=10)
    px = Button(pergunta5, text="Proxima pergunta", font="arial 16", background=cor_quadro, foreground=escrito)
    px ["command"] = partial(resp,px)
    px.pack(anchor=SE, expand=True, pady=20)
#pergunta 6 ===============================================
def p6():
    quadro.pack(ipady= 50, ipadx=50)
    pergunta= LabelFrame(quadro, text="""Sexta Pergunta: Em uma situação em que você perceba que seus colegas 
    de classe estão deixando a sua instituição de estudo desorganizada, 
    o que você faria a respeito?""", font="arial 20", background=cor_quadro, foreground=escrito, bd=0)
    pergunta.pack(anchor=CENTER, expand=1)

    def resp(op):
            if(op==op1):
                a = Label(pergunta,text="""Comunicando com o representante de classe ele 
                encontrará a melhor forma de achar um processo para resolver o problema""", font="arial 14", background=cor_quadro, foreground=escrito2)
                arm_respostas.append("6. A)Conversaria com a pessoa, e daria exemplos para tentar auxiliar na melhoria dela como aluno, influenciando a ser uma pessoa mais educacada e organizada.")
                a.pack()
            elif(op==op2):
                b = Label(pergunta,text="""Você tem certeza? fazer a sua parte com toda certeza é válido, mas talvez so isso 
                não seja o suficiente...Vamos conversar?""", font="arial 14", background=cor_quadro, foreground=escrito2)
                arm_respostas.append("6. B) Me preocuparia apenas em fazer a sua parte. ")
                b.pack()
            else: 
                pergunta.destroy()
                p7()
    #opção 1
    op1 = Button(pergunta, text="""A) Comunicaria o problema com o representante de classe""",font="arial 16", background=cor_quadro, foreground=escrito)
    op1 ["command"] = partial(resp, op1)
    op1.pack(pady=10, padx=10)
    #op 2
    op2 = Button(pergunta, text="B) Me preocuparia apenas em fazer a sua parte.", font="arial 16", background=cor_quadro, foreground=escrito)
    op2 ["command"] = partial(resp, op2)
    op2.pack(pady=10, padx=10)
    px = Button(pergunta, text="Proxima Pergunta", font="arial 16", background=cor_quadro, foreground=escrito)
    px ["command"] = partial(resp,px)
    px.pack(anchor=SE, expand=True, pady=20)
#Pergunta 7
def p7():
    quadro.pack(ipady= 50, ipadx=50)
    pergunta3 = LabelFrame(quadro, text="""Sétima Pergunta: Ao lavar sua marmita na pia, você: """, font="arial 20", background=cor_quadro, foreground=escrito, bd=0)
    pergunta3.pack(anchor=CENTER, expand=1)

    def resp(op):
            if(op==op1):
                a = Label(pergunta3,text="""Não é certo fazer isso, além de causar mal cheiro,
                pode entupir os encanamentos da instituição""", font="arial 14", background=cor_quadro, foreground=escrito2)
                arm_respostas.append("7. A) Joga o resto de comida no ralo")
                a.pack()
            elif(op==op2):
                b = Label(pergunta3,text="""Parabéns, você está contribuindo para o bem-estar da instituição,
                fazendo a sua parte e também influênciando as pessoas á sua volta """, font="arial 14", background=cor_quadro, foreground=escrito2)
                arm_respostas.append("7. B) Descarta os restos no lixo")
                b.pack()
            else: 
                pergunta3.destroy()
                p8()
    #opção 1
    op1 = Button(pergunta3, text="A) Joga o resto de comida no ralo.", font="arial 16", background=cor_quadro, foreground=escrito)
    op1 ["command"] = partial(resp, op1)
    op1.pack(pady=10, padx=10)
    #op 2
    op2 = Button(pergunta3, text="B) Descarta os restos no lixo.", font="arial 16", background=cor_quadro, foreground=escrito)
    op2 ["command"] = partial(resp, op2)
    op2.pack(pady=10,padx=10)
    px = Button(pergunta3, text="Proxima pergunta", font="arial 16", background=cor_quadro, foreground=escrito)
    px ["command"] = partial(resp,px)
    px.pack(anchor=SE, expand=True, pady=20)
#Pergunta 8 ================================================
def p8():
    quadro.pack(ipady= 50, ipadx=50)
    pergunta= LabelFrame(quadro, text="""Oitava Pergunta: Você trás suco ou café dentro da garrafinha. 
    Onde é certo limpa-la?""", font="arial 20", background=cor_quadro, foreground=escrito, bd=0)
    pergunta.pack(anchor=CENTER, expand=1)

    def resp(op):
            if(op==op1):
                a = Label(pergunta,text="""Jogar café ou suco no bebedouro não é certo, se o suco tiver alguma semente 
                ela pode entupir o mesmo e outros líquidos podem contaminar a água""", font="arial 14", background=cor_quadro, foreground=escrito2)
                arm_respostas.append("8. A) Bebedouro")
                a.pack()
            elif(op==op2):
                b = Label(pergunta,text="""Isso mesmo, a pia é o lugar certo para fazer a limpeza adequada""", font="arial 14", background=cor_quadro, foreground=escrito2)
                arm_respostas.append("8. B)Pia da cozinha")
                b.pack()
            else: 
                pergunta.destroy()
                p9()
    #opção 1
    op1 = Button(pergunta, text="A) Bebedouro", font="arial 16", background=cor_quadro, foreground=escrito)
    op1 ["command"] = partial(resp, op1)
    op1.pack(pady=10, padx=10)
    #op 2
    op2 = Button(pergunta, text="B) Pia da cozinha", font="arial 16", background=cor_quadro, foreground=escrito)
    op2 ["command"] = partial(resp, op2)
    op2.pack(pady=10,padx=10)
    px = Button(pergunta, text="Proxima Pergunta", font="arial 16", background=cor_quadro, foreground=escrito)
    px ["command"] = partial(resp,px)
    px.pack(anchor=SE, expand=True, pady=20)
#pergunta 9
def p9():
    quadro.pack(ipady= 50, ipadx=50)
    pergunta= LabelFrame(quadro, text="""Nona Pergunta: Você está esquentando seu almoço no micro-ondas e sem 
    querer acaba sujando o mesmo. Você:""", font="arial 20", background=cor_quadro, foreground=escrito, bd=0)
    pergunta.pack(anchor=CENTER, expand=1)

    def resp(op):
            if(op==op1):
                a = Label(pergunta,text="""Depois de usarmos o microondas, outras pessoas também usarão, então se coloque 
                o no lugar dele e pense se gostaria de utilizar o aparelho todo sujo de comida.""", font="arial 14", background=cor_quadro, foreground=escrito2)
                arm_respostas.append("9. A) Finge que nada aconteceu e sai.")
                a.pack()
            elif(op==op2):
                b = Label(pergunta,text="""Isso mesmo, tudo conversado é entendido, às vezes pode ter acontecido algum 
                engano, ou algo do gênero, conversar evita que a situação piore, e ajuda a solucionar educadamente o 
                problema""", font="arial 14", background=cor_quadro, foreground=escrito2)
                arm_respostas.append("""9. B) Isso aí, do mesmo jeito que você gostaria de utilizar o microondas limpo, o próximo 
                colega que utilizará depois de você gostaria também, assim deixamos o ambiente limpo, e mantemos os 
                aparelhos higienizados""")
                b.pack()
            else: 
                pergunta.destroy()
                hist()
    #opção 1
    op1 = Button(pergunta, text="A) Finge que nada aconteceu e sai.", font="arial 16", background=cor_quadro, foreground=escrito)
    op1 ["command"] = partial(resp, op1)
    op1.pack(pady=10,padx=10)
    #op 2
    op2 = Button(pergunta, text="B) - Você retira e lava o prato do microondas, e também limpa o aparelho", font="arial 16", background=cor_quadro, foreground=escrito)
    op2 ["command"] = partial(resp, op2)
    op2.pack(pady=10,padx=10)
    px = Button(pergunta, text="Finalizar Quiz Pergunta", font="arial 16", background=cor_quadro, foreground=escrito)
    px ["command"] = partial(resp,px)
    px.pack(anchor=SE, expand=True, pady=20)
#resultados ======================================================
def hist():
    quadro.pack(ipady= 50, ipadx=50)
    """result = LabelFrame(quadro, text="Vamos mostrar o seu hitórico de respostas: ",font="arial 14", background=cor_quadro, foreground=escrito,bd=0)
    result.pack(anchor=CENTER, expand=1)
    cont=1
    for i in arm_respostas:
        mostrar = Label(result, text=f"Pergunta {cont}: {i}",font="arial 14", background=cor_quadro, foreground=escrito)
        mostrar.pack()
        cont +=1"""
    result = Label(quadro, text="""PARABÉNS, TERMINAMOS AQUI NOSSO QUIZ  CONTAMOS COM TODOS VOCÊS PARA QUE JUNTOS 
    POSSAMOS CRIAR UM AMBIENTE MAIS AMIGÁVEL E HIGIÊNICO  E ASSIM DEIXAR NOSSO LEGADO COMO
    AS PRIMEIRAS TURMAS DA ESCOLA PROZ EDUCAÇÃO!!""",font="arial 14", background=cor_quadro, foreground=escrito,bd=0)
    result.pack(anchor=CENTER, expand=1)

#menu============================================
quadro1 = PanedWindow(janela, width=480, height=100, relief="raised", bg=cor_menu)#primeiro final janela 
quadro1.pack(fill=BOTH, expand= 0)
titulo_quadro1 = Label(quadro1, text="QUIZ DA CONSCIENTIZAÇÃO", background=cor_menu ,foreground='white', font= "Arial  20")
titulo_quadro1.pack() #o método pack interliga um widget pai em um filho para exibir, dentro dos parenteses você pode formatar 
apresentacao_quadro= PanedWindow(janela,bg=fundo_da_tela, width=200, height=400)
apresentacao_quadro.pack(padx=20, pady=20, ipadx=20, ipady=20)
apresentacao = Label(apresentacao_quadro, text="Olá, sejam bem vindos! A campanha de conscientização, da turma de desenvolvimento de sistemas!", font= "Arial  20", background=fundo_da_tela, foreground="black")
apresentacao.grid(row=10, column=10)

quadro = Frame(janela,background="#C0C0C0", width=600, height=300, bd=2, relief="raised")
quadro.place(x=600, y=500)
quadro.pack(pady=40, padx=100)
text_tamanh=600
menu_quadro = Frame(janela, background="#C0C0C0")
menu_quadro.place(x=575, y=250)

menu =Label(menu_quadro, text="Menu:", font="arial 40", fg=escrito2, background="#C0C0C0")
menu.pack(side=TOP)
botao1 = Button(menu_quadro, text="Iniciar quiz", font="arial 20", background="#C0C0C0", foreground=escrito,)
botao1 ["command"] = partial(acao_menu,botao1)
botao1.pack(side=LEFT, padx=10, pady=10)
botao2 = Button(menu_quadro, text="Sair", font="arial 20", background="#C0C0C0", foreground=escrito )
botao2 ["command"]= janela.quit #quit = comando para fechar
botao2.pack(side=RIGHT, padx=10, pady=10)


janela.mainloop()
