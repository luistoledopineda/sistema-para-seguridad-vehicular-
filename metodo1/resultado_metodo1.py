import cv2
import os

dataPath = 'C:/Users/toled/OneDrive/Escritorio/archivos_finales/metodo1/data__metodo1' #Cambia a la ruta donde hayas almacenado Data
imagePaths = os.listdir(dataPath)# en lista las carpetas en el dat 

print('imagePaths=',imagePaths)#imprime la lista de carpetas en el data 


if not os.path.exists('Rostros encontrados'):#creo una carpeta para guardar los rostros si no existe 
	print('Carpeta creada: Rostros encontrados')
	os.makedirs('Rostros encontrados')

face_recognizer = cv2.face.LBPHFaceRecognizer_create() #defino metodo de roconocimiento


# Leyendo el modelo
face_recognizer.read('modeloLBPHFace.xml') 

cap = cv2.VideoCapture(0)#defino la camar a utilizar 

faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')#modelo para reconocer rostros
count =0  #contador

def prueba():
    cv2.imwrite('Rostros encontrados/rostro_{}.jpg'.format(count),rostro)
    cv2.imshow('rostro',rostro)
    
while True: 
	ret,frame = cap.read()
	if ret == False: break
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	auxFrame = gray.copy()

	faces = faceClassif.detectMultiScale(gray,1.3,5)
	k = cv2.waitKey(1)
    
	if k == 27:
		break
	

	for (x,y,w,h) in faces:
		rostro = auxFrame[y:y+h,x:x+w]
		rostro = cv2.resize(rostro,(150,150),interpolation= cv2.INTER_CUBIC)
		result = face_recognizer.predict(rostro)

		cv2.putText(frame,'{}'.format(result),(x,y-5),1,1.3,(255,255,0),1,cv2.LINE_AA)
		if k== ord("s"):
			prueba()
		if result[1] < 70 :
			cv2.putText(frame,'{}'.format(imagePaths[result[0]]),(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
			cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
			
			
		else:
			cv2.putText(frame,'Desconocido',(x,y-20),2,0.8,(0,0,255),1,cv2.LINE_AA)
			cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)
			
		
    
	cv2.imshow('frame',frame)
	


    
    

cap.release()
cv2.destroyAllWindows()
# simplificar esta
# comparar camaras 
# medicion tiempo ?
