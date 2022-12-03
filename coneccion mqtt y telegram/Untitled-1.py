 

from paho.mqtt import client as mqtt_client # libreria para conectarse a un servidor mqtt
import telebot
import time

bot = telebot.TeleBot("5564745727:AAFKODURM-V6NtpqZ3PICE6nJJV7RmK-XLI") #token telebot
broker = 'node02.myqtthub.com'
port = 1883
topic = "Led1"                    #datos necesarios para la coneccion 
client_id = 'python'
username = 'cpc.002'
password = 'cpc.222'




def cenviar(paquete):
    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password) #funcion para en viar un mensaje a al modulo esp01 que esta conectado a ese servidor
    client.connect(broker, port)
    time.sleep(1)
    client.publish(topic, paquete )
    time.sleep(1)
    
@bot.message_handler(commands=["help","start"])
def wea2(message):
    bot.reply_to(message,"hola,que quieres hacer?")
    bot.reply_to(message,"usa /On para activar")              #son los mensajes que enviamos al usuario mediante telegram 
    bot.reply_to(message,"usa /Off para descartivar")

@bot.message_handler(commands=["Off","On"])
def wea(message):
    if message.text == "/On":
     bot.reply_to(message,"activado")                  # si dependiendo del comando que mande se defino lo que envia 
     print(message.text)
     enviar1= "On"
     cenviar(enviar1)
    else:
     bot.reply_to(message,"desactivado")
     print(message.text)
     enviar5="Off"
     cenviar(enviar5)
     


bot.polling()