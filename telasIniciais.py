
import tkinter as tk
from tkinter import *



class janelaInicial():
    def __init__(self):
        #FUNÇÕES

        def logar():    
            if self.entryUser.get() == '' or self.entrySenha.get() == '':                
                frameErro= Frame(self.telaInicial, bg= '#111111')
                frameErro.place(rely=0.05, relx=0.12, relwidth=0.75, relheight=0.15)
                textErro= ''
                if self.entryUser.get() == '':
                    textErro += 'Usuário Errado'
                if self.entrySenha.get() == '':
                    textErro += ' Senha Errado'
                Label(frameErro, text= textErro, bg= '#111111', fg= 'white').place(rely=0.25, relx=0.25)
                Button(frameErro, text= 'x', border=0, bg= '#111111', fg= 'white', command=lambda: frameErro.destroy()).place(rely=0.35, relx=0.9, relheight=0.35)
            else:
                def voltarInicial():
                    self.telaLogada.destroy()
                    janelaInicial()
                    
                #LAYOUT

                self.telaInicial.destroy()
                self.telaLogada= Tk()
                self.telaLogada.geometry('450x650+450+30')

                Label(self.telaLogada, text= 'Nome').place(rely=0.1, relx=0.05)
                Label(self.telaLogada, text= 'Idade').place(rely=.13, relx=0.05)
                Label(self.telaLogada, text= 'Endereço').place(rely=0.16, relx=0.05)
                Label(self.telaLogada, text= 'CPF/CNPJ').place(rely=0.19, relx=0.05)
                Label(self.telaLogada, text= 'RG').place(rely=0.22, relx=0.05)
                Label(self.telaLogada, text= 'Tipo de Serviço').place(rely=0.25, relx=0.05)                    
                Label(self.telaLogada, text= 'Período de Serviço').place(rely=0.28, relx=0.05)
                Label(self.telaLogada, text= 'Data da Contratação').place(rely=0.31, relx=0.05)
                Label(self.telaLogada, text= 'Valor Médio Do Serviço').place(rely=0.34, relx=0.05)


                Button(text= 'Sair', command= voltarInicial).place(rely=0.90, relx=0.85, relwidth=0.15)
                self.telaLogada.mainloop()

            

        def esqueciSenha():
            #FUNÇÕES
            def voltarInicial():
                self.telaEsquiSenha.destroy()
                janelaInicial()
            
            #LAYOUT
            self.telaInicial.destroy()
            self.telaEsquiSenha= Tk()
            self.telaEsquiSenha.geometry('500x250+420+220')

            self.botaoVoltar= Button(self.telaEsquiSenha, text= 'Voltar', command= voltarInicial).place(rely=0.5, relx=0.5)

            self.telaEsquiSenha.mainloop()
       
        def cadastro():
            #FUNÇÕES
            def salvar():
                voltarInicial()            


            def voltarInicial():
                self.telaCadastro.destroy()
                janelaInicial()

            def continuar():     
                def erro():
                    topErro= Toplevel(self.telaCadastro, bg= '#111111')
                    topErro.geometry('350x150+480+250')
                        
                    Label(topErro, text= " ERRO! ALGUM ESPAÇAMETRO\n INCOMPLETO!", bg= '#111111', fg= 'red').place(rely=0.2, relx=0.25)
                    Button(topErro, text= 'OK', bg= '#212121', fg= 'white', border=0, command=lambda: topErro.destroy()).place(rely=0.5, relx=0.43, relwidth=0.15)

                def userConfirmar():
                    if user.get() == '' or senha.get() == '':
                        erro()
                    else:
                        topUser.destroy()
                        topConfirmar= Toplevel(self.telaCadastro, bg= '#111111')
                        topConfirmar.geometry('250x150+530+250')

                        Label(topConfirmar, text= 'Desejar Realmente Fazer O Cadastro?', bg= '#111111', fg= 'white').place(rely=0.1,relx=0.1)
                        Button(topConfirmar, text= 'Sim', bg= "#212121", fg= 'white', border=0, command= salvar).place(rely=0.5, relx=0.3, relwidth=0.15)
                        Button(topConfirmar, text= 'Não', bg= '#212121', fg= 'white', border=0, command= voltarInicial).place(rely=0.5, relx=0.6, relwidth=0.15)

                cont = 0
                listaDados= [respostaRecuperacao, nome, idade, endereco, cpfCnpj, rg, tempoContrato, inicioContrato, mediaServico]
                for dados in listaDados:
                    if dados.get() == '':
                        cont += 1
                if cont > 0:
                    erro()
                if cont == 0:
                    topUser= Toplevel(self.telaCadastro, bg= '#111111')
                    topUser.geometry('350x150+480+250')

                    Label(topUser, text= 'Usuário:', bg= '#111111', fg= 'white').place(rely=0.3, relx=0.1)
                    Label(topUser, text= 'Senha', bg= '#111111', fg= 'white').place(rely=0.4, relx=0.1)
                    user= Entry(topUser)
                    senha= Entry(topUser)
                    Button(topUser, text= 'Confirmar', bg= "#212121", fg= 'white', border=0, command= userConfirmar).place(rely=0.7, relx=0.1)
                    Button(topUser, text= 'Cancelar',bg= '#212121', fg= 'white', border=0, command=lambda: topUser.destroy()).place(rely=0.7, relx=0.7)

                    user.place(rely=0.3, relx=0.25, relwidth=0.4)
                    senha.place(rely=0.4, relx=0.25, relwidth=0.4)

            #LAYOUT
            self.telaInicial.destroy()
            self.telaCadastro= Tk()
            self.telaCadastro.geometry('300x600+420+50')
            self.telaCadastro.minsize(450, 600)
            self.telaCadastro['bg']= '#313131'
            
            nome= Entry(self.telaCadastro, bg= '#111111', fg= 'white')
            idade= Entry(self.telaCadastro, bg= '#111111', fg= 'white')
            endereco= Entry(self.telaCadastro, bg= '#111111', fg= 'white')
            cpfCnpj= Entry(self.telaCadastro, bg= '#111111', fg= 'white')
            rg= Entry(self.telaCadastro, bg= '#111111', fg= 'white')
            servico= Entry(self.telaCadastro, bg= '#111111', fg= 'white')
            tempoContrato= Entry(self.telaCadastro, bg= '#111111', fg= 'white')
            inicioContrato= Entry(self.telaCadastro, bg= '#111111', fg= 'white')
            mediaServico= Entry(self.telaCadastro, bg= '#111111', fg= 'white')
            respostaRecuperacao= Entry(self.telaCadastro, bg= '#111111', fg= 'white')
            
            nome.place(rely=0.1, relx=0.15, relwidth=0.8)
            idade.place(rely=0.13, relx=0.15, relwidth=0.8)
            endereco.place(rely=0.16, relx=0.2, relwidth=0.75)
            cpfCnpj.place(rely=0.19, relx=0.2, relwidth=0.75)
            rg.place(rely=0.22, relx=0.2, relwidth=0.75)
            servico.place(rely=0.25, relx=0.25, relwidth=0.7)
            tempoContrato.place(rely=0.28, relx=0.3, relwidth=0.65)
            inicioContrato.place(rely=0.31, relx=0.32, relwidth=0.63)
            mediaServico.place(rely=0.34, relx=0.35, relwidth=0.6)
            respostaRecuperacao.place(rely=0.55, relx=0.37, relwidth=0.6)

            nome.focus()

            listaPerguntas = ['Nome do cachorro', 'Qual cor você gosta?', 'Jogo prefirido', 'Comida preferido', 'Nome da escola', 'Nome do esporte favorito']

            Label(self.telaCadastro, text= 'Nome', bg= '#313131').place(rely=0.1, relx=0.05)
            Label(self.telaCadastro, text= 'Idade', bg= '#313131').place(rely=.13, relx=0.05)
            Label(self.telaCadastro, text= 'Endereço', bg= '#313131').place(rely=0.16, relx=0.05)
            Label(self.telaCadastro, text= 'CPF/CNPJ', bg= '#313131').place(rely=0.19, relx=0.05)
            Label(self.telaCadastro, text= 'RG', bg= '#313131').place(rely=0.22, relx=0.05)
            Label(self.telaCadastro, text= 'Tipo de Serviço', bg= '#313131').place(rely=0.25, relx=0.05)                    
            Label(self.telaCadastro, text= 'Período de Serviço', bg= '#313131').place(rely=0.28, relx=0.05)
            Label(self.telaCadastro, text= 'Data da Contratação', bg= '#313131').place(rely=0.31, relx=0.05)
            Label(self.telaCadastro, text= 'Valor Médio Do Serviço', bg= '#313131').place(rely=0.34, relx=0.05)
            Label(self.telaCadastro, text= 'Pergunta de Recupeção de Conta', bg= '#313131').place(rely=0.5, relx=0.05)
            spinBoxRecuperacao= Spinbox(self.telaCadastro, values=listaPerguntas, wrap= True, bg= '#111111', fg= 'white')
            spinBoxRecuperacao.place(rely=0.5, relx=0.47, relwidth= 0.5)
            Label(self.telaCadastro, text= 'Resposta Para a Pergunta', bg= '#313131').place(rely=0.55, relx=0.05)

            self.cadastrarBotao= Button(self.telaCadastro, text= 'Continuar', bg= '#111111', fg= 'white', border=0, command= continuar).place(rely=0.9, relx=0.08, relwidth=0.2)
            self.botaoVoltar= Button(self.telaCadastro, text= 'Voltar', bg= '#111111', fg= 'white', border=0, command= voltarInicial).place(rely=0.9, relx=0.8, relwidth=0.2)

            self.telaCadastro.mainloop()



        #LAYOUT TELA INICIAL


        self.telaInicial= Tk()
        self.telaInicial.geometry('500x250+420+220')
        self.telaInicial.maxsize(500, 250)
        self.telaInicial['bg']= 'Black'

        self.labelUser = Label(self.telaInicial, bg= 'black', fg= 'white', text= 'Usuário').place(rely=0.35, relx=0.2)
        self.labelSenha= Label(self.telaInicial, bg= 'black', fg= 'white', text= 'Senha').place(rely=0.45, relx=0.2)

        self.entryUser= Entry(self.telaInicial  )
        self.entrySenha= Entry(self.telaInicial, show= '*')
        self.entryUser.place(rely=0.35, relx=0.3, relwidth=0.4)
        self.entrySenha.place(rely=0.45, relx=0.3, relwidth=0.4)
        

        self.botaoLogar= Button(self.telaInicial, text= 'Logar',border=0, fg= 'white', bg= '#414141', command= logar).place(rely=0.55, relx=0.63)
        self.botaoCadastro= Button(self.telaInicial, text= 'Cadastrar', border=0, bg= 'black', fg= 'white',  command= cadastro).place(rely=0.85, relx=0.05)
        self.botaoSeEsq= Button(self.telaInicial, text= 'Esqueceu a Senha?', border=0, bg= 'black', fg= 'white', command= esqueciSenha).place(rely=0.85, relx=0.75)

        self.entryUser.focus()

        self.telaInicial.mainloop()






janelaInicial()

