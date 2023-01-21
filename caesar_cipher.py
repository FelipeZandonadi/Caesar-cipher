from string import ascii_letters

alfabeto = ascii_letters + "0123456789"


def Crip():
    msg = str(input('Mensagem: '))
    senha = int(input('Senha: '))
    msg_r = str('')
    for i in range(0, len(msg)):
        if msg[i] == ' ':
            msg_r = msg_r + ' '
        else:
            p = alfabeto.find(msg[i])+senha
            if p >= len(alfabeto):
                p = p - ((p // len(alfabeto)) * len(alfabeto))
            msg_r = msg_r + alfabeto[p]
    print(msg_r)


def Dcrip():
    msg = str(input('Mensagem: '))
    senha = int(input('Senha: '))
    msg_r = str('')
    for i in range(0, len(msg)):
        if msg[i] == ' ':
            msg_r = msg_r + ' '
        else:
            if senha >= len(alfabeto):
                senha = senha - ((senha // len(alfabeto)) * len(alfabeto))
            msg_r = msg_r + alfabeto[alfabeto.find(msg[i])-senha]
    print(msg_r)


def Decrip_PC():
    global senha
    msg = str(input('Mensagem: '))
    pc = str(input('Palavra-chave: '))
    msg_r = str('')
    for senha in range(0, len(alfabeto)):
        for i in range(0, len(msg)):
            if msg[i] == ' ':
                msg_r = msg_r + ' '
            else:
                msg_r = msg_r + alfabeto[alfabeto.find(msg[i]) - senha]
        if pc in msg_r:
            break
        msg_r = ''
    print(msg_r)
    print(senha)


modo = input('Encriptar (c), desencriptar (d) ou desencriptar com Palavra-chave (pc)? ')
if modo == 'c':
    Crip()
elif modo == 'd':
    Dcrip()
elif modo == 'pc':
    Decrip_PC()