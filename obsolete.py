# -*- coding: utf-8 -*-
from BotAmino import *
from random import uniform, choice, randint
import time
import os
from gtts import gTTS, lang

print("Iniciando... (Boberto I)")

client = BotAmino()
client.wait = 2
client.no_command_message = "Comando inválido"
client.bio = "Boberto I - Gumball Amino (2016-2021)"
client.spam_message = ""
client.prefix = "+"

def éDaStaff(authid):
    ids = ["2ddaa4b1-8562-45c4-a87e-e494ac4c291d", "07475577-4a02-4759-baeb-afb996560354"]
    if authid not in ids:
        return False
    else:
        return True


def estaBanido(authid):
    ids = [] # Você coloca os ids banidos entre os colchetes
    if authid not in ids:
        return True
    else:
        return False


#@client.on_member_join_chat()
#def welcomeit(data):
#    print("Membro entrou")
#    img = open("gum.png", "rb")
#    data.subClient.send_message(data.chatId, message=f'{data.author}', embedTitle='...', embedContent='...', embedImage=img)



@client.command("pato")
def emb(data):
    img = open("pato.jpg", "rb")
    data.subClient.send_message(data.chatId, message='Aqui está um pato', embedTitle='Pato', embedContent='Pato >:(', embedImage=img)


@client.command("F")
def f(data):
    img = open("F.png", "rb")
    data.subClient.send_message(data.chatId, message='Press F to pray respect.', embedTitle='F', embedContent='F', embedImage=img)


@client.command("planta")
def embe(data):
    img = open("planta.jpg", "rb")

    data.subClient.send_message(data.chatId, message='Platinha', embedTitle='Planta', embedContent='Não toca na minha plantinha >:(', embedImage=img)


@client.command("cookie")
def embf(data):
    img = open("cookie.jpg", "rb")
    data.subClient.send_message(data.chatId, message=f'Um cookie para {data.author}!', embedTitle='Cookie', embedContent='Alguém quer um cookie?', embedImage=img)



@client.command("sairtd")
def leaveall(data):
    if éDaStaff(data.authorId):
        pass
    else:
        return False
    data.subClient.send_message(chatId=data.chatId, message="Okay")
    data.subClient.leave_all_chats()
    data.subClient.send_message(chatId=data.chatId, message="Pronto")


@client.command("entrartd")
def joinall(data):
    if éDaStaff(data.authorId):
        pass
    else:
        data.subClient.send_message(chatId=data.chatId, message="Você não tem permissão para isso.")
        return False

    print(type(data))
    while True:
        try:
            data.subClient.send_message(chatId=data.chatId, message="Entrando...")
            data.subClient.join_all_chat()
            data.subClient.send_message(chatId=data.chatId, message="Pronto.")
            break
        except:
            print(f"Erro... Tentando novamente em 5 segundos.")
            time.sleep(5)
    value = int(''.join(open("value", 'r').readlines()))
    value = value + 1
    print(value)


@client.command("ship")
def ship(data):
    casal = data.message + " null null "
    pessoas = casal.split(" ")
    porcentagem = uniform(0, 100)
    quote = ' '
    mtruim = ["Mt meloso, eca", "Eles são irmãos, e isso é nojento...", "Eles se odeiam...", "Meh.",
              "Queria muito que isso desse certo, mas nunca vai dar certo.",
              "Eles são apenas amigos...", "Vou ter que te cancelar por shippar isso."]
    ruim = [f"Poderia dar certo se {pessoas[randint(0, 1)]} quisesse...", "Okay...", "Eh..."]
    ok = ["Eles ficariam tão bem juntos... Mas fazer o que?", "Confesso que a porcentagem só ta maior que 25 pq eles "
                                                              "são "
                                                              "muito amigos",
          f"{pessoas[0]} quer muito ficar com {pessoas[1]}, mas {pessoas[1]} não quer.", "Não acho que daria "
                                                                                         "certo, mas sempre tem um "
                                                                                         "talvez.",
          "Quem sabe um dia?", "Fofinho, mas nah", f"Eles já estão namorando, mas "
                                                   f"{pessoas[randint(0, 1)]} não sabe."]
    bom = ["Eles já estão juntos secretamente.", f"Cara, confesso que só não foi 100% pq {pessoas[randint(0, 1)]} é "
                                                 f"kpopper", f"Meu casal <3", "Lindo. Apenas.",
           "Queria ter uma webnamorada :(", ""]
    mtbom = [f"ELES JÁ NAMORAM A {randint(2, 15)} ANOS, COMO VOCÊ NÃO PERCEBEU AINDA??", "Casal muito foda.",
             "É̷͙̪̝̏̿̽̀s̸̳̭̄̅s̸̞̪̊̓̇̂̔e̴̲̰̎͌̌̐͛̍̈́ ̴̡̡̝̙̥̪͕͉͉̈́̎c̸̛̻̼̟̹̭͛̈́͝ͅḁ̶̆̄̿͊̽̕s̶̡̾̑̐a̴̼̱̲̦͍̜̩̖͐̓́̑̆͋̈̅̕l"
             "̷̧̗̬͕͖̯̖͓̻̈́̃̈̒͌̒̚͠ͅ ̴̘̩͖̓͒ͅé̵͔͛͌͐̈́̔̑͛̓̈ ̷͈̹̻̂̈̀̂͋̀͛̃͝t̸̡̛̝̫̯̲̗̻̬͇̎ã̵͖̰̑͆̄̋͒̈̇ő̵͚͓͂̅̈͂̆̃̏̄ "
             "̵̧̮̟͈̟̌͊̑̃͘b̶͉̯͋̕ö̸̧̰͕̥̹͓͙̰͑͐̈́̆̌̄̓͂͝m̴̡̧̰̥̥͖̻̑͌̌͑͐̋ "
             "̵̛͚͕̠̭̳͉͓̘́͜q̴̱̲͓̆͆͗̇̎̅͌̓̈́u̸̧̢̼̞̱͆͑͂̃͋͘͜͠e̴̬̩̬͓̪͍̭͕̓̚͠ ̴̺̍̋͋̆̽͜ṁ̷̱͐́͐͌̈ě̷̛̪̜͔̉͑̀̇̉̑ͅ "
             "̶͍̘̒̾͌̕̕d̸̞̳̱̗͉͙̫̠͖̂͊̋̏̍̆̽̋͜ȃ̴̜̜̮̱̫̺̺̑ "
             "̵̡̨̑̍̓̊̄̅̐̿̊̋ņ̵̬̙̳͕͖̩̫͓̦̍͑͛̅͒̌̇͠o̴̘̯̩͒͆͜j̵͚̖̹̱̠̘̣̟͊̾͂͌͘͝o̸̠͍̳͙̐.̴͑͒́̓̆̕̚͜ quero dizer, esse casal é mt "
             "bom.",
             "Eu fiquei até sem idéia doq escrever de tão bom.", "Aquele casal perfeito...", "bot.exe parou de "
                                                                                             "funcionar."]

    if porcentagem <= 10:
        quote = choice(mtruim)
    elif 10 <= porcentagem <= 25:
        quote = choice(ruim)
    elif 25 <= porcentagem <= 50:
        quote = choice(ok)
    elif 50 <= porcentagem <= 75:
        quote = choice(bom)
    elif 75 <= porcentagem <= 100:
        quote = choice(mtbom)
    vazio = 100 - porcentagem
    shipname = []
    c = -1
    for loop in pessoas[0]:
        c = c + 1
        if c <= 2:
            try:
                shipname.append(str(pessoas[0])[c])
            except IndexError:
                break
        else:
            break
    c = (len(pessoas[1]) * -1)
    ns = []
    for d in range(c, 0):
        ns.append(str(d))
    b = -1
    e = -4
    for loop in pessoas[1]:
        e = e + 1
        try:
            c = int(ns[e])
        except IndexError:
            pass
        b = b + 1
        if b <= 2:
            try:
                shipname.append(str(pessoas[1])[c])
            except IndexError:
                break
        else:
            break
    if ''.join(shipname).lower() in ["kotrto", "bobomi"]:
        porcentagem = 1000.00
        quote = "É CANNON..."
    while True:
        try:
            data.subClient.send_message(chatId=data.chatId, message=f"""

[bc]━── ─ ─ ※ ─ ─ ──━
[bc]░◤◢♤{''.join(shipname)}♤◣◥░
[cu]{pessoas[0]} x {pessoas[1]}
[c]"{quote}"
[c]
[ic]{porcentagem:.2f}% de chance de dar certo
[c][{"█" * int(porcentagem / 5)}{"⠀" * int(vazio / 5)}]
[c]━─━───【♤】───━─━
        """)
            break
        except:
            print(f"Erro... Tentando novamente em 5 segundos.")
            time.sleep(5)


@client.command("spam")
def spam(data):
    import time
    msg = data.message
    msg = msg.split(" ")
    msg.append(" ")
    msg[1] = ' '.join(msg[1:])
    if int(msg[0]) >= 5:
        #return False
        pass
    try:
        num = int(msg[0])
    except (TypeError, ValueError):
        while True:
            try:
                data.subClient.send_message(chatId=data.chatId, message="Digite a quantidade de vezes antes da frase.")
                break
            except:
                print(f"Erro... Tentando novamente em 5 segundos.")
                time.sleep(5)
        return False

    for loop in range(1, num + 1):
        while True:
            try:
                data.subClient.send_message(chatId=data.chatId, message=msg[1])
                break
            except:
                print(f"Erro... Tentando novamente em 5 segundos.")
                time.sleep(1)
        time.sleep(1)


@client.command("cancelar")
def cancel(data):
    msg = data.message
    motivos = ["ser um gostoso(a)", "ser foda", "ser muito gado", "ser corno", "por que sim, fodase",
               'ser um bostakkk', 'ser sensato', 'gostar do Felipe Neto', 'gostar de kpop', 'ser anarcocapitalista',
               'ser comunista', 'shippar incesto', 'não gostar do Ednaldo Pereira, o mestre', 'ser o nego ney',
               'ser um Pedro', 'apenas existir']
    while True:
        try:
            data.subClient.send_message(chatId=data.chatId, message=f"""
            [cu]{msg} foi cancelado por {data.author} por {choice(motivos)}!
            """)
            break
        except:
            print(f"Erro... Tentando novamente em 5 segundos.")
            time.sleep(5)


@client.command("help")
def hel(data):
    pg = data.message
    while True:
        try:
            if pg == '1':
                data.subClient.send_message(chatId=data.chatId, message="""
[bc]━─━───【♤】───━─━ 
[bc]༺「𝑩𝒐𝒃𝒆𝒓𝒕𝒐」༻ 
[c]
[ic]Página 1
[c]!ship (Pessoa1, Pessoa2) - Shippa 2 pessoas
[c]!spam [vezes] [Texto]- Flooda uma msg especifica em uma quantidade especifica de vezes (Máximo é 4)
[c]!help - Ajuda
[c]!cancelar [Pessoa] - Cancela alguém
[c]!entrar_em [link ou id] - Entra no chat 
[c]!vsfbot - Manda o bot se fuder
[c]!google [pesquisa]- Pesquisa no google
[c]!kid [TEXTO] - fAz O tExTo FiCaR AsSiM
[c]!pvp [rounds, player1, player2] - Pvp.
[c]!coin - Cara ou coroa?
[c]
[bc]━━༺༻━━━━ 

             """)
            elif pg == "2":
                data.subClient.send_message(chatId=data.chatId, message="""
[bc]━─━───【♤】───━─━ 
[bc]༺「𝑩𝒐𝒃𝒆𝒓𝒕𝒐」༻ 
[c]
[ic]Página 2
[c]!sortear [pessoas...] -  Sorteia alguma coisa
[c]!fala [FRASE] - Cita o texto como se algum famoso tivesse falado
[c]!calc [num1, conta, num2] - Resultado de uma conta
[c]!diga [texto] - Manda um áudio falando algo
[c]!pato - Pato
[c]!cookie - Cookie
[c]!planta - Planta
[c]!id - Qual meu id?
[c]!kill [Pessoa] - Mata alguém
[c]!F - F
[c]
[bc]━━༺༻━━━━ 
            """)
            elif pg == 'mod':
                data.subClient.send_message(chatId=data.chatId, message="""
[bc]━─━───【♤】───━─━ 
[bc]༺「𝑩𝒐𝒃𝒆𝒓𝒕𝒐」༻ 
[c]
[ic]Comandos de MOD (Staff apenas)
[c][c]!entrartd - Entra em todos os chats publicos
[c]!sairtd - Sai de todos os chats publicos
[c]
[bc]━━༺༻━━━━ 
            """)
            else:
                data.subClient.send_message(data.chatId, message="Você não informou a página ou a página informada é inválida.")
            break
        except:
            print(f"Erro... Tentando novamente em 5 segundos.")
            time.sleep(5)

@client.command("entrar_em")
def joinchat(data):
    while True:
        try:
            data.subClient.send_message(chatId=data.chatId, message="Entrando, por favor aguarde...")
            data.subClient.join_chatroom(data.message)
            data.subClient.send_message(chatId=data.chatId, message=f"Pronto.")
            break
        except:
            print(f"Erro... Tentando novamente em 5 segundos.")
            time.sleep(5)


@client.command("vsfbot")
def vsfbot(data):
    msg = choice(["vai tomar no cu", "vai se fuder", "vai se fuder tu oxi", 
    "QUERO MAIS É QUE SE FODA", "aIn vAI sE fUdEr BoT aInn"])
    while True:
        try:
            data.subClient.send_message(chatId=data.chatId, message=msg)
            break
        except:
            print(f"Erro... Tentando novamente em 5 segundos.")
            time.sleep(5)


@client.command("google")
def google(data):
    msg = data.message.split(" ")
    msg = '+'.join(msg)
    while True:
        try:
            data.subClient.send_message(chatId=data.chatId, message=f"https://www.google.com/search?q={msg}")
            break
        except:
            print(f"Erro... Tentando novamente em 5 segundos.")
            time.sleep(5)


@client.command("kid")
def sarcasmo(data):
    msg = data.message
    res = []
    for loop in msg:
        if randint(0, 1) == 1:
            res.append(loop.upper())
        else:
            res.append(loop)

    res = ''.join(res)
    while True:
        try:
            data.subClient.send_message(chatId=data.chatId, message=res)
            break
        except:
            print(f"Erro... Tentando novamente em 5 segundos.")
            time.sleep(5)


@client.command("pvp")
def pvp(data):
    import time
    msg = data.message + " null null "
    msg = msg.split(" ")
    try:
        rounds = int(msg[0])
    except (TypeError, ValueError):
        rounds = 5
        msg[2] = msg[1]
        msg[1] = msg[0]
        msg[0] = 5

    if msg[1] == '' or msg[1] == ' ' or msg[1] == 'null':
        msg[1] = data.author
    if msg[2] == '' or msg[1] == ' ' or msg[2] == 'null':
        msg[2] = data.author
    if msg[1] == msg[2]:
        msg[2] = f'Reverse_{msg[1]}'

    while True:
        try:
            data.subClient.send_message(chatId=data.chatId, message=f"[icu]{data.author} iniciou um PvP."
                                                                    f"\n[ci]{msg[1]} ⚔ {msg[2]}"
                                                                    f'\n[ci]Que o melhor vença!')
            break
        except:
            print(f"Erro... Tentando novamente em 5 segundos.")
            time.sleep(5)
    win1 = 0
    win2 = 0
    roundi = 0
    for tpvp in range(0, rounds):
        roundi = roundi + 1
        punch = randint(0, 1)
        if punch == 0:
            win1 = win1 + 1
            agress = msg[1]
            defens = msg[2]
        else:
            win2 = win2 + 1
            agress = msg[2]
            defens = msg[1]
        time.sleep(4)
        while True:
            try:
                data.subClient.send_message(chatId=data.chatId, message=f"[cu]Round {roundi}"
                                                                        f"\n[ci]{msg[1]} ⚔ {msg[2]}"
                                                                        f"\n[ic] {agress} destruiu {defens}!")
                break
            except:
                print(f"Erro... Tentando novamente em 5 segundos.")
                time.sleep(5)
    while True:
        try:
            if win1 > win2:
                data.subClient.send_message(chatId=data.chatId, message=f"[bcu]{msg[1]} ganhou!"
                                                                        f"\n[ciu][{win1} x {win2}]")
            elif win1 < win2:
                data.subClient.send_message(chatId=data.chatId, message=f"[bcu]{msg[2]} ganhou!"
                                                                        f"\n[cic][{win1}x{win2}]")
            elif win1 == win2:
                data.subClient.send_message(chatId=data.chatId, message=f"[iC]Empate.")
            break
        except:
            print(f"Erro... Tentando novamente em 5 segundos.")
            time.sleep(5)


@client.command("coin")
def caracoroa(data):
    moeda = ["Cara", "Coroa"]
    while True:
        try:
            data.subClient.send_message(chatId=data.chatId, message=f"[bc]{choice(moeda)}")
            break
        except:
            print(f"Erro... Tentando novamente em 5 segundos.")
            time.sleep(5)

@client.command("sortear")
def sorteio(data):
    moeda = data.message.split(" ")
    while True:
        try:
            data.subClient.send_message(chatId=data.chatId, message=f"[bc]Foi sorteado {choice(moeda)}!")
            break
        except:
            print(f"Erro... Tentando novamente em 5 segundos.")
            time.sleep(5)


@client.command("fala")
def quote(data):
    famosos = ["Ednaldo Pereira", "Gumball Watterson", "Darwin Watterson", "Felipe Neto", "Diggo", "Juilo Caesar"
               , "Aristoceles", "Isaac Newton", "Albert Einsten", "Joseph Stalin", "Vladmir Putin", "Karl Marx"
               , "Vladmir Lenin", "Jesus Cristo", "Mark Zuckerberg", "Bill Gates", "Steve Jobs", "Autor Desconhecido",
               "Dom Pedro II do Brasil", "Dom Pedro I do Brasil", "Pitagoras", "Galileu Galileu", "Pedro"
               , "Stephen Hawking"]
    while True:
        try:
            data.subClient.send_message(chatId=data.chatId, message=f'[ic]"{data.message}" ~{choice(famosos)}')
            break
        except:
            print(f"Erro... Tentando novamente em 5 segundos.")
            time.sleep(5)


@client.command("calc")
def math(data):
    conta = data.message.split(" ")
    for l in range(0, 3):
        conta.append("null")
    try:
        num1 = int(conta[0])
        num2 = int(conta[2])
    except (TypeError, ValueError):
        return None
    resultado = 0
    if conta[1] in "*+/-":
            if conta[1] == "*":
                resultado = num1*num2
            elif conta[1] == "+":
                resultado = num1+num2
            elif conta[1] == "/":
                try:
                    resultado = num1/num2
                except ZeroDivisionError:
                    data.subClient.send_message(chatId=data.chatId, message=f"💥💥💥")
                    return None
            elif conta[1] == "-":
                resultado = num1-num2
    else:
        return None

    while True:
        try:
            data.subClient.send_message(chatId=data.chatId, message=f"{num1}{conta[1]}{num2}={resultado}")
            break
        except:
            print(f"Erro... Tentando novamente em 5 segundos.")
            time.sleep(5)


@client.command("diga")
def say_something(data):
    audio_file = f"audios/ttp.mp3"
    gTTS(text=data.message, lang='pt', slow=False).save(audio_file)
    with open(audio_file, 'rb') as fp:
        while True:
            try:
                data.subClient.send_message(data.chatId, file=fp, fileType="audio")
                break
            except:
                print("Erro... Tentando novamente em 5 segundos.")
                time.sleep(5)
        os.remove(audio_file)


@client.command("c")
def talk(data):
    olás = ['eae', "oi", "olá", "ola", "iae", "iai", "oie", "oiee", "oin", "oieh", "oih"
                                ,"i"]
    resposta = ''
    for aaa in data.message.split(" "):
        if aaa in olás:
            resposta = choice(['eae', "oi", "olá", "ola", "iae", "iai", "oie", "oiee", "oin", "oieh", "oih"
                                  , "i", "eae, blz?", "eae, beleza?", "olá, tudo bem com vc?"]).capitalize()
            break
        else:
            pass

    while True:
        try:
            data.subClient.send_message(chatId=data.chatId, message=f'Esse comando não está pronto, tente novamente'
                                                                    f' mais tarde.')
            break
        except:
            print(f"Erro... Tentando novamente em 5 segundos.")
            time.sleep(5)


@client.command("curiosidade")
def curiosity(data):
    msg = ["O monte Everest cresce 4 milímetros por ano.", "Vacas não consegue descer escadas.",
           "Certamente, a maior palavra da língua portuguesa refere-se a uma doença causada pela respiração de cinzas "
           "vulcânicas: pneumoultramicroscopicossilicovulcanoconiótico.",
           '"hippopotomonstrosesquippedaliofobia." é o nome da fobia de palavras grandes.',
           "Alguém já pagou 50k em uma arte invisivel.", "O Brasil é o país que possui a maior comunidade japonesa fo"
                                                         "ra do Japão. ",
            "Só em São Paulo, moram mais de 600 mil japoneses.", "A china censurou a palavra 'censura'...",
           "O corpo humano brilha. Porém, ele brilha 1000x menos que a coisa menos brilhosa que conseguimos ver",
           "O inventor do algodaão-doce foi um dentista.", "O universo cheira a carne podre", "Você é linda, namora "
            "cmg", ""]
    while True:
        try:
            data.subClient.send_message(chatId=data.chatId, message=f"{choice(msg)}")
            break
        except:
            print(f"Erro... Tentando novamente em 5 segundos.")
            time.sleep(5)


@client.command("manutenção")
def caracoroa(data):
    if data.message.split(" ")[0] == 'on':
        while True:
            try:
                data.subClient.send_message(chatId=data.chatId, message=f"[cu] ⚠️ O bot está temporariamente desativado️"
                                                                        f" para manutenção ⚠️")
                break
            except:
                print(f"Erro... Tentando novamente em 5 segundos.")
                time.sleep(5)
    elif data.message.split(" ")[0] == 'off':
        while True:
            try:
                data.subClient.send_message(chatId=data.chatId, message=f"[CU]O bot voltou!")
                break
            except:
                print(f"Erro... Tentando novamente em 5 segundos.")
                time.sleep(5)


@client.command("console")
def console(data):
    print("Modo console ativado.")
    id = data.subClient.get_chat_id(input("Link do chat: "))
    while True:
        csl = input(">>> ")
        if csl != '':
            data.subClient.send_message(id, message=csl)
        else:
            break


@client.command("id")
def id(data):
    while True:
        try:
            data.subClient.send_message(chatId=data.chatId, message=f'{data.authorId}')
            break
        except:
            print(f"Erro... Tentando novamente em 5 segundos.")
            time.sleep(5)


@client.command("info")
def info(data):
    
    for a in client.sub_clients().aminoId:
        info = client.get_community_info(a)
        print(info)

    while True:
        try:
            data.subClient.send_message(chatId=data.chatId, message=f'{data.authorId}')
            break
        except:
            print(f"Erro... Tentando novamente em 5 segundos.")
            time.sleep(5)


@client.command("msgs")
def msgs(data):
    msglist = (data.message).split(" ")
    prefix = msglist[0]
    for l in msglist[1:]:
        try:
            data.subClient.send_message(chatId=data.chatId, message=f'{prefix}{l}')
        except:
            print("Erro...")
        time.sleep(3)


@client.command("ping")
def ping(data):
    erro = 0
    if data.message == "":
        data.message = 5
    for l in range(0, int(data.message)):
        try:
            data.subClient.send_message(chatId=data.chatId, message=f'Quantidade de erros: {erro}')
            data.subClient.send_message(chatId=data.chatId, message=f'Pong! {l}')
        except:
            erro = erro + 1
        time.sleep(3)


@client.command("Aceitar")
def accept(args):
    if éDaStaff:
        pass
    else:
        return False

    if args.subClient.accept_role(args.chatId):
        args.subClient.send_message(args.chatId, "Accepted!")
        return
    val = args.subClient.get_notices(start=0, size=25)
    for elem in val:
        print(elem["title"])

    res = None
    

    for elem in val:
        if 'become' in elem['title'] or "host" in elem['title']:
            res = elem['noticeId']

        if res and args.subClient.accept_role(res):
            args.subClient.send_message(args.chatId, "Accepted!")
            return
    else:
        args.subClient.send_message(args.chatId, "Error!")


@client.command("kill")
def murder(data):
    msg = data.message
    armas = ["AK-47", "metralhadora", "espada", "faca", "colher", "pá", "banana", "vaca", "sua mãe", 
    "duas mãos", "queijo", "pote de nescau do bob esponja", "um colete salva-vidas"]
    murdereasons = [f"foi assasinado por {data.author} usando {choice(armas)}"]
    while True:
        try:
            data.subClient.send_message(chatId=data.chatId, message=f'{msg} {choice(murdereasons)}.')
            break
        except:
            print(f"Erro... Tentando novamente em 5 segundos.")
            time.sleep(5)


@client.command("bobertomayliveforever")
def death(data):
    while True:
        try:
            data.subClient.send_message(chatId=data.chatId, message=f"""
            
[ci]Boberto I estará morto dia 1 de Julho. Foi bom enquanto durou.
[ci]Foi muito legal desenvolver isso...
[c]
[ci]MAS ainda não é o fim... Assim que possivel, irei recriar tudo do zero e assim será criado o filho do Boberto...
[c]
[bc]Boberto II (fruto de Kotomi x Boberto hmmm)
[c]
[cis]Legends never die...
[ci]~Gumball Amino, 2016-2021
            """)
            break
        except:
            print(f"Erro... Tentando novamente em 5 segundos.")
            time.sleep(5)


client.launch()
print("Pronto")
