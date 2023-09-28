from config import *
import telebot
from telebot.types import InlineKeyboardMarkup
from telebot.types import InlineKeyboardButton
bot = telebot.TeleBot(TELEGRAM_TOKEN)


#Comando de Bienvenida
@bot.message_handler(commands=["start"])
def cmd_start(message):
    bot.send_chat_action(message.chat.id, "typing")
    bot.send_message(message.chat.id, "Bienvenido, mi nombre es Miko y soy un Bot")

#INICIA MEDIO CURSO
#TEMAS DE INTERPOLACION

#Comandos para interpolacion lineal
@bot.message_handler(commands=['ipl'])
def cmd_ipl(message):
    markup = InlineKeyboardMarkup(row_width = 2)
    b1 = InlineKeyboardButton("Quiz", url= "http://t.me/QuizBot?start=aifaqale")
    b2 = InlineKeyboardButton("Archivo", url = "https://www.mediafire.com/file/ylczumfs3nqeu3z/IPL.pdf/file")
    markup.add(b1,b2)
    bot.send_chat_action(message.chat.id, "typing")
    bot.send_message(message.chat.id, "¡Selecciona un apartado! :)", reply_markup=markup)


#comandos para lagrange
@bot.message_handler(commands=['lagrange'])
def cmd_lagrange(message):
    markup = InlineKeyboardMarkup(row_width = 2)
    b1 = InlineKeyboardButton("Quiz", url= "http://t.me/QuizBot?start=uDAiKSLK")
    b2 = InlineKeyboardButton("Archivo", url = "https://www.mediafire.com/file/3c10nl9enui37vr/Lagrange.pdf/file")
    markup.add(b1,b2)
    bot.send_chat_action(message.chat.id, "typing")
    bot.send_message(message.chat.id, "¡Selecciona un apartado! :)", reply_markup=markup)


#comando para Newton Con Diferencias Divididas
@bot.message_handler(commands=['ncdd'])
def cmd_ncdd(message):
    markup = InlineKeyboardMarkup(row_width = 2)
    b1 = InlineKeyboardButton("Quiz", url= "http://t.me/QuizBot?start=O4K0lqtu")
    b2 = InlineKeyboardButton("Archivo", url = "https://www.mediafire.com/file/l4fv0d3sgfwhqwb/NewtonconDiferenciasDivididas.pdf/file")
    markup.add(b1,b2)
    bot.send_chat_action(message.chat.id, "typing")
    bot.send_message(message.chat.id, "¡Selecciona un apartado! :)", reply_markup=markup)


#Comando para Newton hacia adelante
@bot.message_handler(commands=['nha'])
def cmd_nha(message):
    markup = InlineKeyboardMarkup(row_width = 2)
    b1 = InlineKeyboardButton("Quiz", url= "http://t.me/QuizBot?start=0k583gqA")
    b2 = InlineKeyboardButton("Archivo", url = "https://www.mediafire.com/file/097no0lk3cphjfq/NewtonHaciaAdelante+(1).pdf/file")
    markup.add(b1,b2)
    bot.send_chat_action(message.chat.id, "typing")
    bot.send_message(message.chat.id, "¡Selecciona un apartado! :)", reply_markup=markup)


#Comandos  para Newton hacia detras
@bot.message_handler(commands=['nhd'])
def cmd_nhd(message):
    markup = InlineKeyboardMarkup(row_width = 2)
    b1 = InlineKeyboardButton("Quiz", url= "http://t.me/QuizBot?start=A77wrH0w")
    b2 = InlineKeyboardButton("Archivo", url = "https://www.mediafire.com/file/ucm1gfux4xreped/NewtonHaciaAtrás+(1).pdf/file")
    markup.add(b1,b2)
    bot.send_chat_action(message.chat.id, "typing")
    bot.send_message(message.chat.id, "¡Selecciona un apartado! :)", reply_markup=markup)

#TERMINA INTERPOLACION 

#TEMAS DE ECUACIONES NO LINEALES

#Metodo de Bisectriz = Grafico de Bisectriz
@bot.message_handler(commands=['gbisectriz'])
def cmd_gbisectriz(message):
    markup = InlineKeyboardMarkup(row_width = 2)
    b1 = InlineKeyboardButton("Quiz", url= "http://t.me/QuizBot?start=W1R0fZWz")
    b2 = InlineKeyboardButton("Archivo", url = "https://www.mediafire.com/file/6kn410vg6kdnq4b/EcNoLGráficoBisectriz.pdf/file")
    markup.add(b1,b2)
    bot.send_chat_action(message.chat.id, "typing")
    bot.send_message(message.chat.id, "¡Selecciona un apartado! :)", reply_markup=markup)

@bot.message_handler(commands=['mgrafico'])
def cmd_mgrafico(message):
    markup = InlineKeyboardMarkup(row_width = 2)
    b1 = InlineKeyboardButton("Quiz", url= "http://t.me/QuizBot?start=K6qp3kfo")
    b2 = InlineKeyboardButton("Archivo", url = "https://www.mediafire.com/file/81sjt64fehyf6k0/Metodo+grafico.pdf/file")
    markup.add(b1,b2)
    bot.send_chat_action(message.chat.id, "typing")
    bot.send_message(message.chat.id, "¡Selecciona un apartado! :)", reply_markup=markup)


#Metodo Falsa posicion
@bot.message_handler(commands=['fp'])
def cmd_fp(message):
    markup = InlineKeyboardMarkup(row_width = 2)
    b1 = InlineKeyboardButton("Quiz", url= "http://t.me/QuizBot?start=KJoeVsOX")
    b2 = InlineKeyboardButton("Archivo", url = "https://www.mediafire.com/file/rq6w387uukqbk7s/FPosición.pdf/file")
    markup.add(b1,b2)
    bot.send_chat_action(message.chat.id, "typing")
    bot.send_message(message.chat.id, "¡Selecciona un apartado! :)", reply_markup=markup)


#Metodo Newton Raphson
@bot.message_handler(commands=['nr'])
def cmd_nr(message):
    markup = InlineKeyboardMarkup(row_width = 2)
    b1 = InlineKeyboardButton("Quiz", url= "http://t.me/QuizBot?start=rLJXyG0i")
    b2 = InlineKeyboardButton("Archivo", url = "https://www.mediafire.com/file/xucmmxwyyufp66s/NR+(1).pdf/file")
    markup.add(b1,b2)
    bot.send_chat_action(message.chat.id, "typing")
    bot.send_message(message.chat.id, "¡Selecciona un apartado! :)", reply_markup=markup)


#Metodo Punto Fijo 
@bot.message_handler(commands=['pf'])
def cmd_pf(message):
    markup = InlineKeyboardMarkup(row_width = 2)
    b1 = InlineKeyboardButton("Quiz", url= "http://t.me/QuizBot?start=DIO3oxAH")
    b2 = InlineKeyboardButton("Archivo", url = "https://www.mediafire.com/file/tcc0zv2jhq89eup/PFIJO+(1).pdf/file")
    markup.add(b1,b2)
    bot.send_chat_action(message.chat.id, "typing")
    bot.send_message(message.chat.id, "¡Selecciona un apartado! :)", reply_markup=markup)


#Metodo Secante
@bot.message_handler(commands=['secante'])
def cmd_secante(message):
    markup = InlineKeyboardMarkup(row_width = 2)
    b1 = InlineKeyboardButton("Quiz", url= "http://t.me/QuizBot?start=cxLnVnQA")
    b2 = InlineKeyboardButton("Archivo", url = "https://www.mediafire.com/file/dt8beyobjwt4gv1/Secante+(1).pdf/file")
    markup.add(b1,b2)
    bot.send_chat_action(message.chat.id, "typing")
    bot.send_message(message.chat.id, "¡Selecciona un apartado! :)", reply_markup=markup)


#TERMINA ECUACIONES NO LINEALES - MC

#EMPIEZA ECUACIONES LINEALES

#Metodo gauss-seidel
@bot.message_handler(commands=['gs'])
def cmd_gs(message):
    markup = InlineKeyboardMarkup(row_width = 2)
    b1 = InlineKeyboardButton("Quiz", url= "http://t.me/QuizBot?start=lJseQOQ6")
    b2 = InlineKeyboardButton("Archivo", url = "https://www.mediafire.com/file/7uj4g2xevy2wanw/Gauss-Seidel.pdf/file")
    markup.add(b1,b2)
    bot.send_chat_action(message.chat.id, "typing")
    bot.send_message(message.chat.id, "¡Selecciona un apartado! :)", reply_markup=markup)


#Metodo jacobi
@bot.message_handler(commands=['jacobi'])
def cmd_jacobi(message):
    markup = InlineKeyboardMarkup(row_width = 2)
    b1 = InlineKeyboardButton("Quiz", url= "http://t.me/QuizBot?start=sBnvH9gp")
    b2 = InlineKeyboardButton("Archivo", url = "https://www.mediafire.com/file/c29wcudati6o9wz/Jacobi.pdf/file")
    markup.add(b1,b2)
    bot.send_chat_action(message.chat.id, "typing")
    bot.send_message(message.chat.id, "¡Selecciona un apartado! :)", reply_markup=markup)


#Metodo Montante
@bot.message_handler(commands=['montante'])
def cmd_montante(message):
    markup = InlineKeyboardMarkup(row_width = 2)
    b1 = InlineKeyboardButton("Quiz", url= "http://t.me/QuizBot?start=Fv6w71Cm")
    b2 = InlineKeyboardButton("Archivo", url = "https://www.mediafire.com/file/he7ifbz4yc629sd/Método+de+Montante.pdf/file") 
    markup.add(b1,b2)  
    bot.send_chat_action(message.chat.id, "typing")
    bot.send_message(message.chat.id, "¡Selecciona un apartado! :)", reply_markup=markup)


#Metodo Gauss-Jordan
@bot.message_handler(commands=['gj'])
def cmd_gj(message):
    markup = InlineKeyboardMarkup(row_width = 2)
    b1 = InlineKeyboardButton("Quiz", url= "http://t.me/QuizBot?start=1nvm42Th")
    b2 = InlineKeyboardButton("Archivo", url = "https://www.mediafire.com/file/7uj4g2xevy2wanw/Gauss-Seidel.pdf/file")
    markup.add(b1,b2)
    bot.send_chat_action(message.chat.id, "typing")
    bot.send_message(message.chat.id, "¡Selecciona un apartado! :)", reply_markup=markup)

#Metodo Eliminacion Gaussiana
@bot.message_handler(commands=['eg'])
def cmd_eg(message):
    markup = InlineKeyboardMarkup(row_width = 2)
    b1 = InlineKeyboardButton("Quiz", url= "http://t.me/QuizBot?start=9hI4w9dr")
    b2 = InlineKeyboardButton("Archivo", url = "https://www.mediafire.com/file/z9pwn03cpaawdip/Eliminación+Gaussiana.pdf/file")
    markup.add(b1,b2)
    bot.send_chat_action(message.chat.id, "typing")
    bot.send_message(message.chat.id, "¡Selecciona un apartado! :)", reply_markup=markup)

#INICIA TERMARIO ORDINARIO

#Inicia  temas de Minimos Cuadrados

#Metodos Cuadratica 
@bot.message_handler(commands=['cuadratica'])
def cmd_cuadratica(message):
    markup = InlineKeyboardMarkup(row_width = 2)
    b1 = InlineKeyboardButton("Quiz", url= "http://t.me/QuizBot?start=BtvLPjNN")
    b2 = InlineKeyboardButton("Archivo", url = "https://www.mediafire.com/file/67sc3j81svct6ty/CuadráticaCúbica.pdf/file")
    markup.add(b1,b2)
    bot.send_chat_action(message.chat.id, "typing")
    bot.send_message(message.chat.id, "¡Selecciona un apartado! :)", reply_markup=markup)

#cubica
@bot.message_handler(commands=['cubica'])
def cmd_cubica(message):
    markup = InlineKeyboardMarkup(row_width = 2)
    b1 = InlineKeyboardButton("Quiz", url= "http://t.me/QuizBot?start=sdKiWvyF")
    b2 = InlineKeyboardButton("Archivo", url = "https://www.mediafire.com/file/67sc3j81svct6ty/CuadráticaCúbica.pdf/file")
    markup.add(b1,b2)
    bot.send_chat_action(message.chat.id, "typing")
    bot.send_message(message.chat.id, "¡Selecciona un apartado! :)", reply_markup=markup)

#Metodo Lineal con funcion
@bot.message_handler(commands=['lcf'])
def cmd_lcf(message):
    markup = InlineKeyboardMarkup(row_width = 2)
    b1 = InlineKeyboardButton("Quiz", url= "http://t.me/QuizBot?start=u4xtPQSc")
    b2 = InlineKeyboardButton("Archivo", url = "https://www.mediafire.com/file/u2u9mgz45ve5mmb/LinealCuadráticaFunción.pdf/file")
    markup.add(b1,b2)
    bot.send_chat_action(message.chat.id, "typing")
    bot.send_message(message.chat.id, "¡Selecciona un apartado! :)", reply_markup=markup)

#Cuadratica con funcion
@bot.message_handler(commands=['cf'])
def cmd_cf(message):
    markup = InlineKeyboardMarkup(row_width = 2)
    b1 = InlineKeyboardButton("Quiz", url= "http://t.me/QuizBot?start=JwXJ3ypt")
    b2 = InlineKeyboardButton("Archivo", url = "https://www.mediafire.com/file/u2u9mgz45ve5mmb/LinealCuadráticaFunción.pdf/file")
    markup.add(b1,b2)
    bot.send_chat_action(message.chat.id, "typing")
    bot.send_message(message.chat.id, "¡Selecciona un apartado! :)", reply_markup=markup)


#Metodo linea recta
@bot.message_handler(commands=['lr'])
def cmd_lr(message):
    markup = InlineKeyboardMarkup(row_width = 2)
    b1 = InlineKeyboardButton("Quiz", url= "http://t.me/QuizBot?start=nDbpOseT")
    b2 = InlineKeyboardButton("Archivo", url = "https://www.mediafire.com/file/3jayj2czqz4n3ck/LíneaRecta.pdf/file")
    markup.add(b1,b2)
    bot.send_chat_action(message.chat.id, "typing")
    bot.send_message(message.chat.id, "¡Selecciona un apartado! :)", reply_markup=markup)


#INICIA INTEGRACION - ORDINARIO

#Integracion

#Metodo regla trapezoidal 
@bot.message_handler(commands=['rt'])
def cmd_rt(message):
    markup = InlineKeyboardMarkup(row_width = 2)
    b1 = InlineKeyboardButton("Quiz", url= "http://t.me/QuizBot?start=iSaOE7nR")
    b2 = InlineKeyboardButton("Archivo", url = "https://www.mediafire.com/file/4wcz85lc6khh7ex/RTMN.pdf/file")
    markup.add(b1,b2)
    bot.send_chat_action(message.chat.id, "typing")
    bot.send_message(message.chat.id, "¡Selecciona un apartado! :)", reply_markup=markup)


#Newton-cotes  abiertas ed
@bot.message_handler(commands=['nca'])
def cmd_nca(message):
    markup = InlineKeyboardMarkup(row_width = 2)
    b1 = InlineKeyboardButton("Quiz", url= "http://t.me/QuizBot?start=cGZKKARO")
    b2 = InlineKeyboardButton("Archivo", url = "https://www.mediafire.com/file/6pajoqlno1n1r8f/TNewtonCotesAyC.pdf/file")
    markup.add(b1,b2)
    bot.send_chat_action(message.chat.id, "typing")
    bot.send_message(message.chat.id, "¡Selecciona un apartado! :)", reply_markup=markup)


#Newton-cotes cerradas ed
@bot.message_handler(commands=['ncc'])
def cmd_ncc(message):
    markup = InlineKeyboardMarkup(row_width = 2)
    b1 = InlineKeyboardButton("Quiz", url= "http://t.me/QuizBot?start=NlU4mPEr")
    b2 = InlineKeyboardButton("Archivo", url = "https://www.mediafire.com/file/aydcubvkjcc73i2/RNewtonC-Cerradas.pdf/file")
    markup.add(b1,b2)
    bot.send_chat_action(message.chat.id, "typing")
    bot.send_message(message.chat.id, "¡Selecciona un apartado! :)", reply_markup=markup)


#Regla 1/3 Simpson
@bot.message_handler(commands=['r13s'])
def cmd_r13s(message):
    markup = InlineKeyboardMarkup(row_width = 2)
    b1 = InlineKeyboardButton("Quiz", url= "http://t.me/QuizBot?start=Tt9LOhIc")
    b2 = InlineKeyboardButton("Archivo", url = "https://www.mediafire.com/file/w1kcgwijwj7j8qs/R1tercioSimpson.pdf/file")
    markup.add(b1,b2)
    bot.send_chat_action(message.chat.id, "typing")
    bot.send_message(message.chat.id, "¡Selecciona un apartado! :)", reply_markup=markup)


#Regla 3/8 Simpson
@bot.message_handler(commands=['r38s'])
def cmd_r38s(message):
    markup = InlineKeyboardMarkup(row_width = 2)
    b1 = InlineKeyboardButton("Quiz", url= "http://t.me/QuizBot?start=2rYkkiVz")
    b2 = InlineKeyboardButton("Archivo", url = "https://www.mediafire.com/file/9s8ts5nrd1s5xb7/R3octavosSimpson.pdf/file")
    markup.add(b1,b2)
    bot.send_chat_action(message.chat.id, "typing")
    bot.send_message(message.chat.id, "¡Selecciona un apartado! :)", reply_markup=markup)


#Runge kutta 2er orden (ECD) 
@bot.message_handler(commands=['rk2doo'])
def cmd_rk2doo(message):
    markup = InlineKeyboardMarkup(row_width = 2)
    b1 = InlineKeyboardButton("Quiz", url= "http://t.me/QuizBot?start=57DGUJpr")
    b2 = InlineKeyboardButton("Archivo", url = "https://www.mediafire.com/file/vunwbix11rxgrrm/Método+Runge-kutta+de+2do+orden.pdf/file")
    markup.add(b1,b2)
    bot.send_chat_action(message.chat.id, "typing")
    bot.send_message(message.chat.id, "¡Selecciona un apartado! :)", reply_markup=markup)
       
#Runge kutta 3er orden (ECD)
@bot.message_handler(commands=['rk3ero'])
def cmd_rk3ero(message):
    markup = InlineKeyboardMarkup(row_width = 2)
    b1 = InlineKeyboardButton("Quiz", url= "http://t.me/QuizBot?start=QJtL9Zcp")
    b2 = InlineKeyboardButton("Archivo", url = "https://www.mediafire.com/file/raw9vsktcqxufli/Método+Runge-kutta+de+tercer+orden.pdf/file")
    markup.add(b1,b2)
    bot.send_chat_action(message.chat.id, "typing")
    bot.send_message(message.chat.id, "¡Selecciona un apartado! :)", reply_markup=markup)


#Runge-Kutta de 1/3 de Simpson
@bot.message_handler(commands=['rk13s'])
def cmd_rk13s(message):
    markup = InlineKeyboardMarkup(row_width = 2)
    b1 = InlineKeyboardButton("Quiz", url= "http://t.me/QuizBot?start=D6H3A0Mf")
    b2 = InlineKeyboardButton("Archivo", url = "https://sites.google.com/site/tasksnumericalmethods/unidad-4---diferenciacion-e-integracion-numericas/metodo-de-simpson-1-3")
    markup.add(b1,b2)
    bot.send_chat_action(message.chat.id, "typing")
    bot.send_message(message.chat.id, "¡Selecciona un apartado! :)", reply_markup=markup)

#Runge-Kutta de 3/8 de Simpson
@bot.message_handler(commands=['rk38s'])
def cmd_rk38s(message):
    markup = InlineKeyboardMarkup(row_width = 2)
    b1 = InlineKeyboardButton("Quiz", url= "http://t.me/QuizBot?start=giARpSF5")
    b2 = InlineKeyboardButton("Archivo", url = "https://www.mediafire.com/file/yfn57oepbuj0rlc/R-K4toOrd3OctavosS.pdf/file")
    markup.add(b1,b2)
    bot.send_chat_action(message.chat.id, "typing")
    bot.send_message(message.chat.id, "¡Selecciona un apartado! :)", reply_markup=markup)

#orden superior
@bot.message_handler(commands=['ors'])
def cmd_ors(message):
    markup = InlineKeyboardMarkup(row_width = 2)
    b1 = InlineKeyboardButton("Quiz", url= "http://t.me/QuizBot?start=hZx8ekEz")
    b2 = InlineKeyboardButton("Archivo", url = "http://ocw.upm.es/pluginfile.php/551/mod_label/intro/tema2.pdf")
    markup.add(b1,b2)
    bot.send_chat_action(message.chat.id, "typing")
    bot.send_message(message.chat.id, "¡Selecciona un apartado! :)", reply_markup=markup)


#Euler
@bot.message_handler(commands=['euler'])
def cmd_euler(message):
    markup = InlineKeyboardMarkup(row_width = 2)
    b1 = InlineKeyboardButton("Quiz", url= "http://t.me/QuizBot?start=YtAm2ain")
    markup.add(b1)
    bot.send_chat_action(message.chat.id, "typing")
    bot.send_message(message.chat.id, "¡Selecciona un apartado! :)", reply_markup=markup)


#Euler mod
@bot.message_handler(commands=['eulermod'])
def cmd_eulermod(message):
    markup = InlineKeyboardMarkup(row_width = 2)
    b1 = InlineKeyboardButton("Quiz", url= "http://t.me/QuizBot?start=ijAcz6xe")
    markup.add(b1)
    bot.send_chat_action(message.chat.id, "typing")
    bot.send_message(message.chat.id, "¡Selecciona un apartado! :)", reply_markup=markup)



@bot.message_handler(commands=['eulerha'])
def cmd_eulerha(message):
    markup = InlineKeyboardMarkup(row_width = 2)
    b1 = InlineKeyboardButton("Quiz", url= " ")
    markup.add(b1)
    bot.send_chat_action(message.chat.id, "typing")
    bot.send_message(message.chat.id, "¡Selecciona un apartado! :)", reply_markup=markup)


#Comandos para textos y comandos no validos
@bot.message_handler(content_types=["text"])
def bot_mensajes_texto(message):
    if message.text.startswith("/"):
        bot.send_chat_action(message.chat.id, "typing")
        bot.send_message(message.chat.id, "Introduce un comando valido!")
    else:
        bot.send_chat_action(message.chat.id, "typing")
        bot.send_message(message.chat.id, "Mi creador no me permite responder eso, ademas de que solo funciono mediante comandos </3")




if __name__=='__main__':
    
    bot.set_my_commands([
        telebot.types.BotCommand("/start", "Da la bienvenida"),
        telebot.types.BotCommand("/ipl", "interpolación lineal"),
        telebot.types.BotCommand("/lagrange", "Lagrange"),
        telebot.types.BotCommand("/ncdd", "Newton con diferencias divididas"),
        telebot.types.BotCommand("/nha", "Newton hacia adelante"),
        telebot.types.BotCommand("/nhd", "Newton hacia atrás"),
        telebot.types.BotCommand("/gbisectriz", "Grafico de Bisectriz"),
        telebot.types.BotCommand("/mgrafico","Método Gráfico"),
        telebot.types.BotCommand("/fp", "Falsa posición"),
        telebot.types.BotCommand("/nr", "Newton Raphson"),
        telebot.types.BotCommand("/pf", "Punto fijo"),
        telebot.types.BotCommand("/secante", "Secante"),
        telebot.types.BotCommand("/gs", "Gauss-Seidel"),
        telebot.types.BotCommand("/eg", "Eliminación Gaussiana"),
        telebot.types.BotCommand("/jacobi", "Jacobi"), 
        telebot.types.BotCommand("/montante","Montante"),
        telebot.types.BotCommand("/gj","Gauss-Jordán"),
        telebot.types.BotCommand("/cuadratica", "Cuadratica"),
        telebot.types.BotCommand("/cubica", " cúbica"),
        telebot.types.BotCommand("/lcf", "Lineal con función"),
        telebot.types.BotCommand("/cf", "cuadrática con función"),
        telebot.types.BotCommand("/lr", "Linea recta"),
        telebot.types.BotCommand("/rt", "Regla trapezoidal"),
        telebot.types.BotCommand("/nca","Newton-Cotes abiertas "),
        telebot.types.BotCommand("/ncc","Newton-Cotes cerradas"),
        telebot.types.BotCommand("/r13s","Regla 1/3 Simpson"),
        telebot.types.BotCommand("/r38s","Regla 3/8 Simpson"),
        telebot.types.BotCommand("/rk2doo","Runge-Kutta 2to orden"),
        telebot.types.BotCommand("/rk3ero","Runge-Kutta 3er orden"),
        telebot.types.BotCommand("/rk13s","Runge-Kutta de 4to orden por 1/3 de Simpson"),
        telebot.types.BotCommand("/rk38s","Runge-Kutta de 4to orden por 3/8 de Simpson"),
        telebot.types.BotCommand("/ors","Runge-Kutta de orden Superior"),
        telebot.types.BotCommand("/euler","Euler hacia adelante"),
        telebot.types.BotCommand("/eulermod","Euler modificado"),
        telebot.types.BotCommand("/eulerha","Euler hacia atrás"),
        
     ])
    
    print('Iniciando bot...')
    bot.infinity_polling()
    print('Fin')