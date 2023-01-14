from tkinter import *
import gtts
from playsound import playsound
import os
import datetime
import time


window1 = Tk()
window1.title('BARBER SHOP')

def fala(frase):
    frase = frase
    frase = gtts.gTTS(frase, lang='pt-br')
    frase.save('frase.mp3')
    playsound('frase.mp3')
    os.remove('frase.mp3')

def olaf():
    fala('oi como você está')
ola = PhotoImage(file='ola.png')
ola = ola.subsample(2,2)
btnola = Button(window1, image=ola,
                   font=('impact bold', "50 "),
                   background='black',
                   foreground='yellow',
                   command=olaf
                   )
btnola.place(x=60, y=10)

def bomdiaf():
    fala('Bom dia')
bom_dia= PhotoImage(file='bomdia.png')
bom_dia = bom_dia.subsample(2,2)
btnbomdia = Button(window1, image=bom_dia,
                   font=('impact bold', "50 "),
                   background='black',
                   foreground='yellow',
                   command=bomdiaf
                   )
btnbomdia.place(x=10, y=120)

def boanoitef():
    fala('Boa noite')
boa_noite = PhotoImage(file='boanoite.png')
boa_noite = boa_noite.subsample(2,2)
btnboanoite = Button(window1, image = boa_noite,
                   font=('impact bold', "50 "),
                   background='black',
                   foreground='yellow',
                   command=boanoitef
                   )
btnboanoite.place(x=130, y=120)

def obgf():
    fala('obrigado')
obg = PhotoImage(file='obg.png')
obg = obg.subsample(2,2)
btnobg = Button(window1, image = obg,
                   font=('impact bold', "50 "),
                   background='black',
                   foreground='yellow',
                   command=obgf
                   )
btnobg.place(x=10, y=240)

def desculpaf():
    fala('Desculpa')
desculpa = PhotoImage(file='desculpa.png')
desculpa = desculpa.subsample(2,2)
btndesculpa = Button(window1, image = desculpa,
                   font=('impact bold', "50 "),
                   background='black',
                   foreground='yellow',
                   command=desculpaf
                   )
btndesculpa.place(x=130, y=240)

def teamof():
    fala('Te amo')
te_amo = PhotoImage(file='teamo.png')
te_amo = te_amo.subsample(2,2)
btnteamo = Button(window1, image = te_amo,
                   font=('impact bold', "50 "),
                   background='black',
                   foreground='yellow',
                   command=teamof
                   )
btnteamo.place(x=10, y=360)

def naoquerof():
    fala('Não quero')
nao_quero = PhotoImage(file='naoquero.png')
nao_quero = nao_quero.subsample(2,2)
btnnaoquero = Button(window1, image = nao_quero,
                   font=('impact bold', "50 "),
                   background='black',
                   foreground='yellow',
                   command=naoquerof
                   )
btnnaoquero.place(x=130, y=360)

def horaf():
    hora = str(datetime.datetime.fromtimestamp(int(time.time())).strftime('%H'))
    minutos = str(datetime.datetime.fromtimestamp(int(time.time())).strftime('%M'))
    fala(f'Agora são {hora} e {minutos}')
hora = PhotoImage(file='hora.png')
hora = hora.subsample(2,2)
btnhora = Button(window1, image =hora,
                   font=('impact bold', "50 "),
                   background='black',
                   foreground='yellow',
                   command=horaf
                   )
btnhora.place(x=10, y=480)

def dataf():
    dia = str(datetime.datetime.fromtimestamp(int(time.time())).strftime('%d'))
    mes = str(datetime.datetime.fromtimestamp(int(time.time())).strftime('%m'))
    ano = str(datetime.datetime.fromtimestamp(int(time.time())).strftime('%Y'))
    fala(f'hoje é dia {dia} do mes {mes} e do ano {ano}')
data = PhotoImage(file='data.png')
data = data.subsample(2,2)
btndata = Button(window1, image=data,
                   font=('impact bold', "50 "),
                   background='black',
                   foreground='yellow',
                   command=dataf
                   )
btndata.place(x=130, y=480)

def fomef():
    fala('Estou com fome')
fome = PhotoImage(file='fome.png')
fome = fome.subsample(2,2)
btnfome = Button(window1, image = fome,
                   font=('impact bold', "50 "),
                   background='black',
                   foreground='yellow',
                   command=fomef
                   )
btnfome.place(x=260, y=10)

def sedef():
    fala('Estou com sede')
sede = PhotoImage(file='sede.png')
sede = sede.subsample(2,2)
btnsede = Button(window1, image = sede,
                   font=('impact bold', "50 "),
                   background='black',
                   foreground='yellow',
                   command=sedef
                   )
btnsede.place(x=430, y=10)

def remediof():
    fala('Hora do remédio')
remedio = PhotoImage(file='remedio.png')
remedio = remedio.subsample(2,2)
btnremedio = Button(window1, image = remedio,
                   font=('impact bold', "50 "),
                   background='black',
                   foreground='yellow',
                   command=remediof
                   )
btnremedio.place(x=600, y=10)

def banhof():
    fala('Preciso tomar banho')
banho = PhotoImage(file='banho.png')
banho = banho.subsample(2,2)
btnbanho = Button(window1, image = banho,
                   font=('impact bold', "50 "),
                   background='black',
                   foreground='yellow',
                   command=banhof
                   )
btnbanho.place(x=770, y=10)

def dordecabecaf():
    fala('Estou com dor de cabeça')
dordecabeca = PhotoImage(file='dordecabeca.png')
dordecabeca = dordecabeca.subsample(2,2)
btndordecabeca = Button(window1, image = dordecabeca,
                   font=('impact bold', "50 "),
                   background='black',
                   foreground='yellow',
                   command=dordecabecaf
                   )
btndordecabeca.place(x=940, y=10)

def silenciof():
    fala('Silencio por favor')
silencio = PhotoImage(file='silencio.png')
silencio = silencio.subsample(2,2)
btnsilencio = Button(window1, image = silencio,
                   font=('impact bold', "50 "),
                   background='black',
                   foreground='yellow',
                   command=silenciof
                   )
btnsilencio.place(x=1110, y=10)

def banheirof():
    fala('Preciso ir ao banheiro')
banheiro = PhotoImage(file='banheiro.png')
banheiro = banheiro.subsample(2,2)
btnbanheiro = Button(window1, image = banheiro,
                   font=('impact bold', "50 "),
                   background='black',
                   foreground='yellow',
                   command=banheirof
                   )
btnbanheiro.place(x=260, y=180)

def roupaf():
    fala('Preciso trocar de roupas')
roupa = PhotoImage(file='roupa.png')
roupa = roupa.subsample(2,2)
btnroupa = Button(window1, image = roupa,
                   font=('impact bold', "50 "),
                   background='black',
                   foreground='yellow',
                   command=roupaf
                   )
btnroupa.place(x=430, y=180)

def tvf():
    fala('Quero assistir televisão')
tv = PhotoImage(file='tv.png')
tv = tv.subsample(2,2)
btntv = Button(window1, image =tv,
                   font=('impact bold', "50 "),
                   background='black',
                   foreground='yellow',
                   command=tvf
                   )
btntv.place(x=600, y=180)

def dormirf():
    fala('Estou com sono quero dormir')
dormir = PhotoImage(file='dormir.png')
dormir = dormir.subsample(2,2)
btndormir = Button(window1, image =dormir,
                   font=('impact bold', "50 "),
                   background='black',
                   foreground='yellow',
                   command=dormirf
                   )
btndormir.place(x=770, y=180)

def levantarf():
    fala('Preciso levantar')
levantar = PhotoImage(file='levantar.png')
levantar = levantar.subsample(2,2)
btnlevantar = Button(window1, image =levantar,
                   font=('impact bold', "50 "),
                   background='black',
                   foreground='yellow',
                   command=levantarf
                   )
btnlevantar.place(x=940, y=180)

def pasearf():
    fala('Vamos passear')
pasear = PhotoImage(file='pasear.png')
pasear = pasear.subsample(2,2)
btnpasear = Button(window1, image =pasear,
                   font=('impact bold', "50 "),
                   background='black',
                   foreground='yellow',
                   command=pasearf
                   )
btnpasear.place(x=1110, y=180)

def familiarumf():
    fala('familiar um')
familiarum = PhotoImage(file='familia.png')
familiarum = familiarum.subsample(2,2)
btnfamiliarum = Button(window1, image =familiarum,
                   font=('impact bold', "50 "),
                   background='black',
                   foreground='yellow',
                   command=familiarumf
                   )
btnfamiliarum.place(x=940, y=350)

def familiardoisf():
    fala('familiar dois')
familiardois = PhotoImage(file='familia.png')
familiardois = familiardois.subsample(2,2)
btnfamiliardois = Button(window1, image =familiardois,
                   font=('impact bold', "50 "),
                   background='black',
                   foreground='yellow',
                   command=familiardoisf
                   )
btnfamiliardois.place(x=1110, y=350)

def familiartresf():
    fala('familiar tres')
familiartres = PhotoImage(file='familia.png')
familiartres = familiartres.subsample(2,2)
btnfamiliartres = Button(window1, image =familiartres,
                   font=('impact bold', "50 "),
                   background='black',
                   foreground='yellow',
                   command=familiartresf
                   )
btnfamiliartres.place(x=940, y=520)

def familiarquatrof():
    fala('familiar quatro')
familiarquatro = PhotoImage(file='familia.png')
familiarquatro = familiarquatro.subsample(2,2)
btnfamiliarquatro = Button(window1, image =familiarquatro,
                   font=('impact bold', "50 "),
                   background='black',
                   foreground='yellow',
                   command=familiarquatrof
                   )
btnfamiliarquatro.place(x=1110, y=520)

def simf():
    fala('Sim')
sim = PhotoImage(file='sim.png')
sim = sim.subsample(2,2)
btnsim = Button(window1, image =sim,
                   font=('impact bold', "50 "),
                   background='black',
                   foreground='yellow',
                   command=simf
                   )
btnsim.place(x=300, y=390)

def naof():
    fala('Não')
nao = PhotoImage(file='nao.png')
nao = nao.subsample(2,2)
btnnao = Button(window1, image =nao,
                   font=('impact bold', "50 "),
                   background='black',
                   foreground='yellow',
                   command=naof
                   )
btnnao.place(x=650, y=390)



window1.configure(background='#cf9bcc')
window1.geometry('1350x800')
window1.mainloop()