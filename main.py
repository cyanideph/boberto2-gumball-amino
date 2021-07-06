from amino.lib.util import exceptions
from BotAmino import *
from random import *
from time import *
from gtts import gTTS, lang
import os
import wikipedia
import json

print("Iniciando...")

client = BotAmino()
client.wait = 2
client.no_command_message = "Comando inválido"
client.spam_message = ""
wikipedia.set_lang("pt")


# A estética base para as coisas do bot
def esteticabase(titulo, conteudo, subtitulo=""):
    return f"""
[c]┏                    ───                      ┓ 
[C]──   Roberto   ──
[C]✩✼　｡ﾟ･　　ﾟ･　☆　° ｡ 
[C] ❤️’• {titulo}
[C]         ╺╺╺╺╺╺╺╺(☕)
[C] — {subtitulo}
{conteudo}
[C]┗                                                  ┛    
        """


# Sistema de conquistas (a parte do código principal)
def conquista(id, conquista, pontos):

    # Primeiro é rodado para se criar o arquivo JSON se não tiver um
    system(f"python3 scripts/conquistas.py {id} ignore 0")

    # É lodado o arquivo JSON para checar se a conquista já foi conquistada
    userjson = load(open(f"info/{id}.json", "r"))
    
    # É checado
    try:
        if conquista not in userjson["achievements"]:
            system(f"python3 scripts/conquistas.py {id} {conquista} {pontos}")
            # Se o usuário não possuir essa conquista é retornado True
            return True
        else:
            # Se não, é retornado False
            return False
    except KeyError:
        # Em caso de KeyError, é considerado a conquista como não conquistada
        system(f"python3 scripts/conquistas.py {id} {conquista} {pontos}")
        return True


def conquistado(nome, pontos, descript):
    return f"""[c]Conquista
[c]
[bc]{nome}
[ci]{descript}
[cu]+{pontos} pontos"""


# Comando simples que manda msg
@client.command("hello")
def ola(data):
    data.subClient.send_message(data.chatId, "Hello world!")


# !help
@client.command("help")
def ajuda(data):
    if conquista(data.authorId, "ajuda_caralho", 100):
        data.subClient.send_message(data.chatId, conquistado("Ajuda caralho!", 100, "Digite !help pela primeira vez"))
    # Ele verifica a página pedida e então mostra os comandos
    if data.message == "1":
        data.subClient.send_message(data.chatId, esteticabase("help", """
[c]!ship [Pessoa1, Pessoa2] - Shippa duas pessoas
[c]!pvp [1, 2, rounds] - Pvp entre 2 enttidades com um numero certo de rounds
[c]!spam [Quantidade, mensagem] - Spamma uma mensagem X vezes
[c]!msg [Mensagem] - Manda uma mensagem especificada
[c]!diga [texto] - Manda um áudio dizendo um texto
[c]!vsfbot - Manda o bot se fuder
[c]!kid [texto] - fAz O tExtO fIcAr AsSiM
[c]!sorteio [tipo; arumentos] - Sorteia coisas, para ver os tipos digite !help sorrteios
[c]!wiki [coisa] - Procura algo na wikipédia e manda o resultado
[c]!quote [Pessoa, frase]- Cita uma frase 
        """, "Página 1"))
    elif data.message == "2":
        data.subClient.send_message(data.chatId, esteticabase("help", """
[c] !8ball [Pergunta] - Responde sua pergunta com sim ou não
[c] !compatibilidade [pessoa] - Checa sua compatibilidade
[c] !pontos - Vê a quantidade de pontos
[c] !conquistas - Vê suas conquistas
[c] !vote [criar, votar, ver] - Cria, vota ou vê uma enquete. !help vote para mais
[c] !claim [ver, claim] - Ver - Vê quantas acs você pode retirar, claim - retira suas acs (apartir de 10 acs)
        """, "Página 2"))
    elif data.message == "sorteios":
        data.subClient.send_message(data.chatId, esteticabase("help", """
[c]Tipos de sorteios:
[c]     n - Sorteia um número. Argumentos: Numéro inicial, número final
[c]     p - Sorteia nomes. Argumentos: nomes (não possui limites)
        """, "Sorteios"))
    elif data.message == "vote":
        data.subClient.send_message(data.chatId, esteticabase("help", """
[c] Modos:
[c]    criar - cria uma enquete
[c]       Argumentos: !vote criar; opção 1; opção 2; etc...
[c]     votar - vota numa enquete
[c]         Argumentos: !vote votar; id; opção
[c]     ver - vê os resultados da enquete
[c]         Argumentos !vote ver; id
        """, "Vote"))
    else:
        data.subClient.send_message(data.chatId, "Digite o número da página. (Total de páginas: 2)")


# Comando !ship
@client.command("ship")
def ship(data):
    # Essa parte define as pessoas dadas como argumento (na variavel "pessoas")
    # usando como base o caractére de espaço e, logo após isso verifica a quanti-
    # dade de caracteres em cada nome (no loop for) para que o nome do shipp seja feito sem bugs
    # (ou pelo menos era para não ter bugs)
    # No final, o output é assim: [[pessoa1, False], [pessoa2, True]]
    # Cada item representa a pessoa do argumento mais se o tamanho é menor que 3
    pessoas = (data.message).split(" ")
    pessoas_preserve = (data.message).split(" ")
    for l in range(0, 2):
        if len(pessoas[l]) < 3:
            pessoas[l] = [pessoas[l], True]
        else:
            pessoas[l] = [pessoas[l], False]
    
    shippname = []
    indxlist = []
    # Essa parte é o que define o nome do shipp.
    for index in range(0, 2):
        # Condicional usada para criar o nome do shipp
        if pessoas[index][1]:
            shippname.append(pessoas[index][0])
       # Se essa condição for negativa, será recortado os 3 caracteres iniciais ou os 3 finais
        else:
            if index == 0:
                shippname.append(pessoas[index][0][0:3])
            else:
                reverse = len(pessoas[index][0]) - 4
                for l in range(0, len(pessoas[index][0])+1):
                    reverse += 1
                    shippname.append(pessoas[index][0][reverse])
                    if l == 2:
                        break
    
    # Pega a lista de caracteres gerados e junta em uma string com o nome do ship
    # e então joga tudo para letras minusculas e por fim capitalizando a primeira letra
    shippname = ((''.join(shippname)).lower()).capitalize()

    if shippname.lower() in ["gumwin", "darall"]:
        if conquista(data.authorId, "incesto", 50):
            data.subClient.send_message(data.chatId, conquistado("Eca, incesto", 50, "Ewww..."))
    # Frases, peguei do antigo
    mtruim = ["Mt meloso, eca", "Eles são irmãos, e isso é nojento...", "Eles se odeiam...", "Meh.",
              "Queria muito que isso desse certo, mas nunca vai dar certo.",
              "Eles são apenas amigos...", "Vou ter que te cancelar por shippar isso."]
    ruim = [f"Poderia dar certo se {pessoas[randint(0, 1)][0]} quisesse...", "Okay...", "Eh..."]
    ok = ["Eles ficariam tão bem juntos... Mas fazer o que?", "Confesso que a porcentagem só ta maior que 25 pq eles "
                                                              "são "
                                                              "muito amigos",
          f"{pessoas[0][0]} quer muito ficar com {pessoas[1][0]}, mas {pessoas[1][0]} não quer.", "Não acho que daria "
                                                                                         "certo, mas sempre tem um "
                                                                                         "talvez.",
          "Quem sabe um dia?", "Fofinho, mas nah", f"Eles já estão namorando, mas "
                                                   f"{pessoas[randint(0, 1)][0]} não sabe."]
    bom = ["Eles já estão juntos secretamente.", f"Cara, confesso que só não foi 100% pq {pessoas[randint(0, 1)][0]} é "
                                                 f"kpopper", f"Meu casal <3", "Lindo. Apenas.",
           "Queria ter uma webnamorada :(", ""]
    mtbom = [f"ELES JÁ NAMORAM A {randint(2, 15)} ANOS, COMO VOCÊ NÃO PERCEBEU AINDA??", "Casal muito foda.",
             "É̷͙̪̝̏̿̽̀s̸̳̭̄̅s̸̞̪̊̓̇̂̔e̴̲̰̎͌̌̐͛̍̈́ ̴̡̡̝̙̥̪͕͉͉̈́̎c̸̛̻̼̟̹̭͛̈́͝ͅḁ̶̆̄̿͊̽̕s̶̡̾̑̐a̴̼̱̲̦͍̜̩̖͐̓́̑̆͋̈̅̕l"
             "̷̧̗̬͕͖̯̖͓̻̈́̃̈̒͌̒̚͠ͅ ̴̘̩͖̓͒ͅé̵͔͛͌͐̈́̔̑͛̓̈ ̷͈̹̻̂̈̀̂͋̀͛̃͝t̸̡̛̝̫̯̲̗̻̬͇̎ã̵͖̰̑͆̄̋͒̈̇ő̵͚͓͂̅̈͂̆̃̏̄ "
             "̵̧̮̟͈̟̌͊̑̃͘b̶͉̯͋̕ö̸̧̰͕̥̹͓͙̰͑͐̈́̆̌̄̓͂͝m̴̡̧̰̥̥͖̻̑͌̌͑͐̋ "
             "̵̛͚͕̠̭̳͉͓̘́͜q̴̱̲͓̆͆͗̇̎̅͌̓̈́u̸̧̢̼̞̱͆͑͂̃͋͘͜͠e̴̬̩̬͓̪͍̭͕̓̚͠ ̴̺̍̋͋̆̽͜ṁ̷̱͐́͐͌̈ě̷̛̪̜͔̉͑̀̇̉̑ͅ "
             "̶͍̘̒̾͌̕̕d̸̞̳̱̗͉͙̫̠͖̂͊̋̏̍̆̽̋͜ȃ̴̜̜̮̱̫̺̺̑ "
             "̵̡̨̑̍̓̊̄̅̐̿̊̋ņ̵̬̙̳͕͖̩̫͓̦̍͑͛̅͒̌̇͠o̴̘̯̩͒͆͜j̵͚̖̹̱̠̘̣̟͊̾͂͌͘͝o̸̠͍̳͙̐.̴͑͒́̓̆̕̚͜",
             "Eu fiquei até sem idéia doq escrever de tão bom.", "Aquele casal perfeito...", "bot.exe parou de "
                                                                                             "funcionar."]

    # É definido a porcentagem para que possa ser pego uma frase aleatoria das listas acima
    # Também é definido a variavel do valor restante de porcentagem
    # Esses valores também servirão para criar a barra
    porcentagem = float(f"{uniform(0, 100):.2f}")
    vazio = 100 - porcentagem

    # Por fim, uma condicional para pegar uma string de uma das listas
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

    # Enviar a mensagem final
    data.subClient.send_message(data.chatId, esteticabase(shippname, f"""   
[c]
[c][{"█" * int(porcentagem / 5)}{"⠀" * int(vazio / 5)}]
[ciu]{porcentagem}% de dar certo.
[ci]
[ci]"{quote}"
""", f"{pessoas_preserve[0]} x {pessoas_preserve[1]}"))


# !pvp
@client.command("pvp")
def fight(data):
    # Argumentos
    args = (data.message).split(" ")
    args.append(5)

    # Aqui acontece o jogo em si
    score = [0, 0]
    r = 0
    for l in range(0, int(args[2])):
        r +=1
        score[0] = score[0] + randint(0, 1)
        score[1] = score[1] + randint(0, 1)

        # É definido o vencedor desse round
        if score[0] > score[1]:
            winner = args[0]
        elif score[0] < score[1]:
            winner = args[1]
        else:
            winner = "Ninguém"
        data.subClient.send_message(data.chatId, esteticabase("PvP", f"""
[cu]{args[0]} {score[0]} x {score[1]} {args[1]}
[c]
[c]{winner} está em vantagem!
        """, f"Round {r}"))
        sleep(1)
    data.subClient.send_message(data.chatId, f"{winner} venceu.")


# !spam
@client.command("spam")
def flood(data):
    args = (data.message).split(" ")
    for l in range(0, int(args[0])):
        data.subClient.send_message(data.chatId, ' '.join(args[1:]))
        sleep(1)


# !msg
@client.command("msg")
def sms(data):
    data.subClient.send_message(data.chatId, data.message)


# !cancelar
@client.command("cancelar")
def cancel(data):
    # A pessoa cancelada em questão
    pessoa = data.message

    # Os motivos de cancelamentos estão aqui:
    data.subClient.send_message(data.chatId, esteticabase(f"Cancelado", subtitulo=f"{pessoa} foi enviado(a) para a prisão após sofrer cancelamento.",
    conteudo=f"""
[c]
[c]O motivo é que {pessoa} {choice(['shippou incesto', 'disse que não gosta de gatos', 'a',
'gosta do Felipe Neto', "não gosta de Gumball", "é o Neymar", "é gado para caralho", "é lindo dms", "gosta de Kpop", 
"não fez nada", "é comunista", "apoia o anarcocapitalismo", "apoia o narcotráfico", "被中共黑了", "é chato pra krl",
"odeia cachorros", "assiste boku no hero", "não gosta do Felipe Neto", "dbdzkfhgvkdhf", "é hacker", 
"gosta do bts", "não gosta do bts", "falou que gosta de gumwin", "é shitposter", "assiste tio orochi", "usa windows", "usa linux",
"apoia o comunismo", "apoia o monarquismo", "come figado de frango", "eu quero mijar"])}."""))


# !diga
@client.command("diga")
def say_something(data):
    audio_file = f"audios/ttp.mp3"
    gTTS(text=data.message, lang='pt', slow=False).save(audio_file)
    with open(audio_file, 'rb') as fp:
        data.subClient.send_message(data.chatId, file=fp, fileType="audio")
        os.remove(audio_file)


# !vsfbot
@client.command("vsfbot")
def vsf(data):
    data.subClient.send_message(data.chatId, f"""{choice([
"vai se fuder", "vai tomar no cu", "vai tu arrombado", "vsf seu humano", "Si yo fuera un rey, serías mi subordinado.",
"vsf vsf vsf vsf vsf vsf vsf vsf vsf vsf", "vai tu babaca", "vsf ban", "ainnn vsfff bot ainn AinAIn"
    ])}""")


# !kid
@client.command("kid")
def kid(data):
    # Primeiro a frase inteira é transformada em lowercase
    frase = (data.message).lower()
    frasekid = []

    # Logo em seguida, é randomizado o .upper() e adicionado na lista "frasekid"
    for l in frase:
        kiddy = randint(0, 1)
        if kiddy == 0:
            l = l.upper()
        
        frasekid.append(l)


    data.subClient.send_message(data.chatId, "".join(frasekid))


# !sorteio
@client.command("sorteio")
def luck(data):
    args = (data.message).split(";")
    
    # Primeiro se define o tipo de sorteio
    if args[0] == 'n':
        
        # No caso de sorteios numericos, é usado randint() para sorteiar um numero entre especificados. os ranges 
        # especificados são colocados na lista argx
        argsx = args[1].split(" ")
        if argsx[0] == "" or argsx[0] == " ":
            del argsx[0]
        num = randint(int(argsx[0]), int(argsx[1]))
        data.subClient.send_message(data.chatId, str(num))
    elif args[0] == 'p':
        
        # Mesmo esquema do anterior, só munda a função da bibilioteca random. Isso escolhe nomes em uma lista
        argsx = args[1].split(" ")
        if argsx[0] == "" or argsx[0] == " ":
            del argsx[0]
        p = choice(argsx)
        data.subClient.send_message(data.chatId, p)


# !wiki
@client.command("wiki")
def wiki(data):
    # Pega a página e o resumo e depois splita para que possa caber no limite
    try:
        wp = wikipedia.page(data.message)
    except wikipedia.exceptions.DisambiguationError as e:
        # Se cair em uma página de disambiguation, é printado erro
        may_referir_a = '\n[c]'.join(e.options)
        data.subClient.send_message(data.chatId, esteticabase("Disambuiguição", f"""[c]{may_referir_a}""", 
        f"{data.message} pode se referir a: "))
        return False
    wpr = (wp.content).split("\n")
    
    # Manda o primeiro paragrafo
    data.subClient.send_message(data.chatId, esteticabase(wp.title, f"""[c]{wpr[0]}

[c]Mais informação em: {wp.url}""", f"Sumário de {wp.title}"))


# !quote
@client.command("quote")
def fala(data):
    args = (data.message).split(" ")
    if args[0] == 'r':
        args[0] = choice(["Ednaldo Pereira", "Gumball Watterson", "Darwin Watterson", "Felipe Neto", "Diggo", "Juilo Caesar"
               , "Aristoceles", "Isaac Newton", "Albert Einsten", "Joseph Stalin", "Vladmir Putin", "Karl Marx"
               , "Vladmir Lenin", "Jesus Cristo", "Mark Zuckerberg", "Bill Gates", "Steve Jobs", "Autor Desconhecido",
               "Dom Pedro II do Brasil", "Dom Pedro I do Brasil", "Pitagoras", "Galileu Galileu", "Pedro"
               , "Stephen Hawking"])
    data.subClient.send_message(data.chatId, f"[cui]{' '.join(args[1:])} ~{args[0]}")


# !8ball (Inspirado na Kotomi)
@client.command("8ball")
def kotomi_8ball(data):
    
    # Bloqueia algumas palavras chaves
    blocklist = ["nazi", "nazista", "nazismo", "homofobia", "homofóbico", "racismo", 
    "racista", "fascista", "fascismo", "n4z1st4", "n4z1sm0", "n4z1", "preconceito", 
    "preconceituoso", "xenofobia", "xenofobico", "xenofóbico", "homofobico"]
    for l in ((data.message).replace("?", "")).split(" "):
        if l.lower() in blocklist:
            
            # Fala que não vai responder caso alguma palavra esteja na lista de palavras chaves
            data.subClient.send_message(data.chatId, "Não vou responder a isso.")
            return False

    # Manda a resposta
    data.subClient.send_message(data.chatId, choice(["Não", "Sim", "Claro que não", 
    "Claro que sim", "Não KKKK lol xD", "Talvez, quem sabe?", "será?", 
    "Nunca", "Isso se quer é uma pergunta?", "Nem fudendo", "Óbvio",
    "MAS É CLARO", "Uhum", "Lógico que não '-'", "Lógico", "Talvez sim, talvez não."]))


# !compatibilidade
@client.command("compatibilidade")
def kotomi_compatibilidad(data):
    # Porcentagem de compatiblidade
    porcentagem = float(f"{uniform(0, 100):.2f}")
    resto = 100 - porcentagem

    data.subClient.send_message(data.chatId, esteticabase("Compatibilidade", f"""
[c] As chances de {data.author} e {data.message} combinarem são de {porcentagem}%
[c]
[c][{"█"*int(porcentagem/5)}{"⠀"*int(resto/5)}]
    """, 
    f"{data.message} x {data.author}"))


# Isso aqui é só pra testar, ignorar
@client.command("teste")
def teste(data):
    if data.message == "0":
        os.system("python3 scripts/filewriter.py")
        data.subClient.send_message(data.chatId, str(''.join(open("scripts/file", "r").readlines())))


# !pontos
@client.command("pontos")
def points(data):
    # Olha a quantidades de pontos
    pontos = load(open(f"info/{data.authorId}.json", "r"))
    pontos = str(pontos["points"])
    
    data.subClient.send_message(data.chatId, pontos)


# !conquistas
@client.command("conquistas")
def conquistas(data):
    # Loda o arquivo JSON
    conq = load(open(f"info/{data.authorId}.json", "r"))
    conqs = conq["achievements"]
    conqsform = []

    # Faz as conquistas ficarem formatadas
    for l in range(0, len(conqs)):
        conqsform.append((conqs[l].replace("_", " ")).capitalize())
    conqsform = "\n[c]".join(conqsform)

    # Manda as conquistas
    data.subClient.send_message(data.chatId, esteticabase("Conquistas", 
    f"""
[c]
[c]{conqsform}""", f"Conquistas de {data.author}"))


# !vote
@client.command("vote")
def votar(data):
    args = (data.message).split(";")
    # Cria uma eqnuete com pollid
    if args[0] == "criar":
        pollid = randint(0, 9999)
        # Arquivos JSON não suportam espaços
        for l in range(0, len(args[1:])):
            args[l+1] = (args[l+1].strip(" ")).replace(" ", "_")

        system(f"python3 scripts/polls.py criar {pollid} {' '.join(args[1:])}")
        data.subClient.send_message(data.chatId, f"Criada uma enquete com o ID '{pollid}'")
    elif args[0] == "votar":
        args[2] = (args[2].strip(" ")).replace(" ", "_")
        system(f"python3 scripts/polls.py votar {args[1]} {args[2]}")
        data.subClient.send_message(data.chatId, "Votado!")
    elif args[0] == "ver":
        polljson = load(open(f"enquetes/{args[1].strip(' ')}.json", "r"))
        # Salva os valores em uma lista
        jvalues = []
        for k, v in polljson.items():
            jvalues.append(f"\n[c]{k}: {v}")
        
        # Mostra os resultados
        data.subClient.send_message(data.chatId, esteticabase("Enquete", f"{''.join(jvalues)}", "Resultados"))


# !claim (comando pegado e adaptado o servidor do discord do Phoenix)
@client.command("claim")
def claim(args):
    jclaims = load(open(f"info/{args.authorId}.json", "r"))
    
    coins = args.subClient.get_wallet_amount()
    if coins >= 1 and jclaims["claims"] >= 1 and args.message == "claim":
        args.subClient.pay(int(jclaims["claims"])*10, chatId=args.chatId)
        args.subClient.send_message(args.chatId, "Enviado!")
        if conquista(args.authorId, "o_capitalista", 1000):
            args.subClient.send_message(args.chatId, conquistado("O capitalista", 1000, "Dê !claim e ganhe acs pela primeira vez."))
        system(f"python3 scripts/ranking.py {args.authorId} ! {jclaims['claims']*1000}")
    elif args.message == "ver":
        args.subClient.send_message(args.chatId, f"Você pode pegar {jclaims['claims']*10} acs.")
    else:
        args.subClient.send_message(args.chatId, "Erro!")


# !musica
@client.command("musica")
def chamada(data):
    client.play(data.chatId, data.comId, data.message)


client.launch()
print("pronto")
