

#from pickle import TRUE
from paho.mqtt import client as mqtt_client
import telebot
import cv2 
import os
import face_recognition
import time
import threading #libreria para crear un hilo
from telebot.types import InlineKeyboardMarkup #para crear botonera inline
from telebot.types import InlineKeyboardButton # para definir botones 
import urllib.request
import numpy as np
#url='http://192.168.1.151/cam-hi.jpg'
url='http://192.168.1.151/cam-lo.jpg'


imgpath= ("C:/Users/toled/OneDrive/Escritorio/archivos_finales/metodo2/usuarios")
faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
facesencodins=[]
facesnames=[]
cjm=[]
bot = telebot.TeleBot("5564745727:AAFKODURM-V6NtpqZ3PICE6nJJV7RmK-XLI")#defino bot dando el token
id = '5596827405'#id de mi telegram
broker = 'node02.myqtthub.com'
port = 1883
topic = "Led1"
client_id = 'python'
username = 'cpc.002'
password = 'cpc.222'
count=0
for file_name in os.listdir(imgpath):
    image=cv2.imread(imgpath + "/" + file_name)
    image=cv2.cvtColor(image , cv2.COLOR_BGR2RGB)

    f_coding= face_recognition.face_encodings(image,known_face_locations=[(0,150,150,0)])[0]
    facesencodins.append(f_coding)
    facesnames.append(file_name.split(".")[0])
if not os.path.exists('Rostros encontrados40'):#creo una carpeta para guardar los rostros si no existe 
	print('Carpeta creada: Rostros encontrados40')
	os.makedirs('Rostros encontrados40')
#print(facesencodins)
#print(facesnames)
def recive():
	bot.polling()
def cenviar(paquete):
    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.connect(broker, port)
    time.sleep(1)
    client.publish(topic, paquete )
    time.sleep(1)
def prueba(wena):
    #count=count +1
    cv2.imwrite('Rostros encontrados40/rostro_{}.jpg'.format(count),frame.copy())
    cv2.imshow('rostro',frame.copy()) 
    #bot.send_message( id,wena  )
    bot.send_photo(id,open("C:/Users/toled/Rostros encontrados40/rostro_{}.jpg".format(count),'rb'),wena + " esta en tu vehiculo")
    markup = InlineKeyboardMarkup(row_width= 2)
    b1 = InlineKeyboardButton("activar ", callback_data="On")
    b2 = InlineKeyboardButton("desactivar  ", callback_data="Off")
    markup.add(b1 ,b2,)
    bot.send_message(id ,"quieres realizar alguna accion ? ",reply_markup=markup)
    

    
cap= cv2.VideoCapture(0)
hilo_bot= threading.Thread(name="hilo_bot",target=recive)  
hilo_bot.start()
while True:
    #ret,frame =cap.read()
    #if ret == False:break
   # frame = cv2.flip(frame ,1)
    imgResponse=urllib.request.urlopen(url)
    imgnp=np.array(bytearray(imgResponse.read()),dtype=np.uint8)
    frame=cv2.imdecode(imgnp,-1)
    orig=frame.copy()
    faces= faceClassif.detectMultiScale(frame,1.1 ,5)
    k = cv2.waitKey(1)
    face_locations= face_recognition.face_locations(frame)
    @bot.message_handler(commands=["help","start"])
    def wea3(message):
        id=message.chat.id
        markup = InlineKeyboardMarkup(row_width= 2)
        b1 = InlineKeyboardButton("activar ", callback_data="On")
        b2 = InlineKeyboardButton("desactivar  ", callback_data="Off")
        markup.add(b1 ,b2)
        bot.send_message(message.chat.id ,"hola que quieres hacer? ",reply_markup=markup)
    
    @bot.callback_query_handler(func=lambda x: True)
    def wea9(call):
        if call.data == "On":
            bot.send_message(call.from_user.id,"activado")
            print(call.data)
            enviar1= "On"
            cenviar(enviar1)
        else:
            bot.send_message(call.from_user.id,"desactivado")
            print(call.data)
            enviar5= "Off"
            cenviar(enviar5)
 


    
    for(x,y,w,h) in faces:
        face = orig[y:y+h,x:x+w]
        face =cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
        actual_encodin=face_recognition.face_encodings(face,known_face_locations=[(0,w,h,0)])[0]
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        
        cjm= face_recognition.compare_faces(facesencodins,actual_encodin)
        print(cjm)

    if True in cjm:
        index= cjm.index(True)
        name=facesnames[index]
        coloor=(125,220,0)
        
        

    else:
        name = "una persona desconocida"
        coloor=(50,50,255)

    if k== ord("s"):
        count=count +1
        prueba(name)
        





    cv2.imshow("frame",frame)
    
    if k ==27 & 0xff: 
        break
 

cap.release()
cv2.destroyAllWindows()
