# Ativa o Fail-Safe por segurança (arrastar o mouse pro canto da tela para o código)

import pyautogui

import pydirectinput

import time

import random

import math

import keyboard

import datetime



pydirectinput.FAILSAFE = True



def mover_humano(x_destino, y_destino):

    #move o mouse até o lugar (NAO CLICA)

    try:

        x_inicial, y_inicial = pydirectinput.position()



        dx = x_destino - x_inicial

        dy = y_destino - y_inicial



        distancia = math.hypot(dx, dy)



        # Quantidade de passos baseada na distância

        passos = max(random.randint(10,15), int(distancia / random.randint(7,10)))



        # Intensidade da curva

        curva = min(distancia * 0.15, 50)

        curva *= random.choice([-1, 1])



        for i in range(passos + 1):



            # Progresso 0 -> 1

            t = i / passos



            # Ease In-Out

            t_suave = (1 - math.cos(math.pi * t)) / 2



            # Movimento principal

            x = x_inicial + dx * t_suave

            y = y_inicial + dy * t_suave



            # Curva perpendicular

            offset = math.sin(t * math.pi) * curva



            if distancia > 0:

                perp_x = -dy / distancia

                perp_y = dx / distancia



                x += perp_x * offset

                y += perp_y * offset



            pydirectinput.moveTo(int(x), int(y))

            if keyboard.is_pressed('f12'):

                print("Movimento cancelado!")

                return

            # Pequena variação no tempo

            time.sleep(random.uniform(0.004, 0.012))



    except Exception as e:

        print("Erro ao mover o mouse:", e)



def procurar_img(nome_imagem, clicar, ir = True):

    # Recebe como parâmetro o nome do arquivo da imagem e clicar True se quiser q clique ou False e se quiser

    #se encontrar retorna img_encontrada True e erro None

    #se nao encontrar retorna img_encontrada False e o tipo de erro e tb printa NAO ENCONTRADO OU ERRO INTERNO



    try:

        pos_img = pyautogui.locateOnScreen(f"{nome_imagem}.png", confidence=0.9)

       

        if pos_img:

            if ir == True:

                centro = pyautogui.center(pos_img)

                mover_humano(centro.x, centro.y)

                time.sleep(random.uniform(0.004, 0.012))

                if clicar == True:

                    pydirectinput.click()                            

            img_encontrada = True

            erro = None

            return img_encontrada, erro                      



        # Se não achou a imagem, tratamos como falso para o loop continuar

        return False, None



    except Exception as e:

        img_encontrada = False

        erro = type(e)

        # print(f"{nome_imagem} NÃO ENCONTRADO OU ERRO INTERNO !!! \n", erro)

        return img_encontrada, erro

   



def abrir_menu():

    #Apenas abre o menu e retorna uma string 'Menu aberto'

    while True:

        confirmado = False

        status_menu = ''

        while True:

            print('--Procurando menu')

            # Vejo se o menu ja esta aberto

            abrir_menu = procurar_img('menu_aberto', False)  

            if True in abrir_menu:

                break

            # caso nao esteja                

            abrir_menu = procurar_img('menu', True)

            if True in abrir_menu:

                break

            abrir_menu = procurar_img('menu2', True)  

            if True in abrir_menu:

                break            

            time.sleep(1)

        # verificando se o bau realmente abriu        

        abrir_menu = procurar_img('menu_aberto', False)  

        if True in abrir_menu:

            break

    return 'Menu aberto'



def mapa_finalizado():

    #verifica o horario da janela de log se ele mudar indica que o mapa foi limpo

    #retorna True

    #se identificar a mudança ou por algum motivo nao atualizar o log vai ficar aqui pra sempre

    regiao = (1465, 895, 40, 14)

    imagem_anterior = pyautogui.screenshot(region=regiao).tobytes()

    while True:

        imagem_atual = pyautogui.screenshot(region=regiao).tobytes()



        if imagem_atual != imagem_anterior:

            break

        time.sleep(1)

    return(True)                





# print(abrir_menu())



#resolver o bug do bau atrasado

#a ideia é:

# tem uma lista de baus 1, 5, 10, 15, 20, 30, 40, 50, 65, 80

# tem uma lista de mapas 1-1, 1-4, 1-8, 2-8 ...

# inicia o mapa 1-1 quando acabar o mapa muda para o mapa 1-4

# espera 10 segundos verifica se dropou bau se dropou bau remove o 1-1 da lista

#



def alterar_dificuldade():

    mover_humano(random.randint(1350, 1535), random.randint(290, 315))

    pydirectinput.click()



def scroll_mapa(direcao):

    #posso usar tb pra resetar o mapa

    #apenas scrola o mapa lembrando q o mapa ja deve estar aberto e tb rodado a escolha de dificuldade antes

    x_aleatorio = random.randint(1245, 1340)

    y_aleatorio = random.randint(490, 620)

    mover_humano(x_aleatorio, y_aleatorio)

    time.sleep(random.random())

    pydirectinput.mouseDown()

    time.sleep(random.random())

    if direcao == 'cima':

        mover_humano(x_aleatorio + random.randint(0, 80) ,y_aleatorio+random.randint(200, 300))

    elif direcao == 'baixo':      

        mover_humano(x_aleatorio - random.randint(0, 80) ,y_aleatorio-random.randint(200, 300))

    time.sleep(random.random())

    pydirectinput.mouseUp()





# escolher mapa

def escolher_dificuldade(dificuldade):

    #dificuldade -> 1 = normal , 2 = nightmare, 3= hell, 4= torment

    if dificuldade == 1:

        alterar_dificuldade()

        mover_humano(random.randint(1350, 1535), random.randint(330, 350))

    elif dificuldade == 2:

        alterar_dificuldade()

        mover_humano(random.randint(1350, 1535), random.randint(360, 380))

    elif dificuldade == 3:

        alterar_dificuldade()

        mover_humano(random.randint(1350, 1535), random.randint(390, 410))

    elif dificuldade == 4:

        alterar_dificuldade()

        mover_humano(random.randint(1350, 1535), random.randint(420, 440))

    time.sleep(random.random())        

    pydirectinput.click()                    



def escolher_ato(ato):

    if ato == 1:

        mover_humano(random.randint(1225, 1305), random.randint(345, 375))

    elif ato == 2:        

        mover_humano(random.randint(1320, 1400), random.randint(345, 375))

    elif ato == 3:        

        mover_humano(random.randint(1429, 1500), random.randint(345, 375))

    time.sleep(random.random())        

    pydirectinput.click()



def escolher_fase(ato, fase):

    num_fase = int(fase)

    fase = f'{ato}-{fase}'

    for i in range(3):



        entrou, erro = procurar_img(fase, False, True)

        if entrou == True:

            time.sleep(random.random())

            x, y = pydirectinput.position()

            mover_humano(x - random.randint(40, 60), y - random.randint(0, 15))

            return True



        if num_fase >= 4:

            scroll_mapa('cima')

        else:

            scroll_mapa('baixo')            

        time.sleep(random.random())





def run(baulvl, click = True):

    lista_baus = ['baulvl1', 'baulvl5', 'baulvl10', 'baulvl15', 'baulvl20', 'baulvl30', 'baulvl40', 'baulvl50', 'baulvl65', 'baulvl80']

    lista_mapas = [(1,1,1), (1,4,1), (1,8,1), (2,3,1), (2,8,1), (3,8,1), (1,9,2), (3,5,2), (2,5,3), (1,3,4)]

    ato, fase, dificuldade = lista_mapas[lista_baus.index(baulvl)]

    escolher_dificuldade(dificuldade)

    escolher_ato(ato)

    entrou = escolher_fase(ato, fase)

    if click == True:

        pydirectinput.click()

    return entrou

   







       

# escolher_mapa(0,4)

def verificar_cd_baus(dicionario_dos_baus):

    for bau in dicionario_dos_baus:

        horario_liberacao_bau = dicionario_dos_baus[bau]

        if horario_liberacao_bau != 0:

            #verificar se ja pode tentar farmar ele dnv

            cd = horario_liberacao_bau - time.time()

            if cd <= 0:

                dicionario_dos_baus[bau] = 0

    return dicionario_dos_baus  





def esperando_dropar():

    with open(caminho_log, "r", encoding="utf-8", errors="ignore") as log:

        print('================================  LENDO O LOG  ===================================')



        # Vai para o final do arquivo

        log.seek(0, 2)



        while True:

            linha = log.readline()

            if linha != '':

                print(linha, datetime.datetime.now().strftime("%H:%M:%S"), end='')

            if 'GetBoxCount Success Count' in linha:

                print('\nDropou')

                return



            else:

                time.sleep(1)



##########abrir bau só pode ser confirmado qunado sumir o bau nao é só clikar



# dicionario_baus = {'baulvl1':0, 'baulvl5':0, 'baulvl10':0, 'baulvl15':0, 'baulvl20': 0, 'baulvl30':0, 'baulvl40':0, 'baulvl50':0, 'baulvl65':0}

caminho_log = r"C:\Users\Zupo\AppData\LocalLow\TesseractStudio\TaskbarHero\Player.log"

#dicionario_baus = {'baulvl50':0, 'baulvl65':0, 'baulvl80':0}

dicionario_baus = { 'baulvl65':0, 'baulvl80':0,'baulvl50':0}





while True:

    for item in dicionario_baus:

        run(item, True)

        esperando_dropar()

        mover_humano(random.randint(1400, 1430), random.randint(951,985))

        time.sleep(random.randint(1,10))

        pydirectinput.click() 

