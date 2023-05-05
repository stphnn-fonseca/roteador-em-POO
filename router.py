class Router():
    def __init__(self, marca, modelo, IP_router, senha_ADM='Ab@123', senha_router='1234', router_ligando=False):

        self.router_ligando       = router_ligando
        self.marca                = marca
        self.modelo               = modelo
        self.IP_router            = IP_router
        self.senha_router         = senha_router
        self.senha_ADM            = senha_ADM
        self.tabela_conectados    = []
        self.desconectadas        = []


#ligando ou desligando o roteador
    def ligando_router(self):
        if self.router_ligando == True:
            print('Roteador esta ligado.')
            return
        
        self.router_ligando = True
        print('Roteador está ligado.')
        
    def deligando_router(self):
        if self.router_ligando == False:
            print('ATENÇÃO!!! O Roteador esta desligado.')

        self.router_ligando = False
        print('Desligando roteador.')


#adcionando ou retirando aparelhos ao roteador
    def conectar_maquina (self, conectar_maquina , senha_router):
        if senha_router == self.senha_router:
            self.tabela_conectados.append(conectar_maquina, )
            print(f'{conectar_maquina } conectado ao roteador {self.marca}, {self.modelo}.')
        else:
            print('Esta senha é inválida.') 

    def desconectando_maquina(self, conectar_maquina):
        if conectar_maquina in self.tabela_conectados:
            self.desconectadas.append(conectar_maquina)
            self.tabela_conectados.remove(conectar_maquina)
            print(f'{conectar_maquina} desconectado do roteador {self.marca}, {self.modelo}.')


#para mudar a senha do roteador é necessário ter acesso a senha de administrador
    def mudar_senha_router(self, senha_ADM):
        self.senha_ADM = senha_ADM
        print(f'A senha do roteador {self.marca}, {self.modelo} foi alterada com sucesso.')


#menu de informações
    def menu_de_informacao(self):
        print('\n Menu de informações: \n')
        print(f'Marca: {self.marca}')
        print(f'Modelo: {self.modelo}')
        print(f'IP do roteador: {self.IP_router}') 
        print(f'Aparelhos conectados: {self.tabela_conectados}')  
        print(f'Aparelhos desconectados: {self.desconectadas}')


roteador_1 = Router('Cisco', 'D-Link', '192.168.1.0')
roteador_1.ligando_router()

roteador_1.conectar_maquina('Pc','1234')
roteador_1.conectar_maquina('Pc2','1234')
roteador_1.conectar_maquina('Leptop','1234')
roteador_1.conectar_maquina('Dispositivo móvel','1234')
roteador_1.menu_de_informacao()


roteador_1.desconectando_maquina('Pc2')
roteador_1.menu_de_informacao()


roteador_1.mudar_senha_router('Senha$123')
roteador_1.menu_de_informacao()
