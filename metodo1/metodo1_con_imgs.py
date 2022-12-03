import cv2
import os

dataPath = 'C:/Users/toled/OneDrive/Escritorio/archivos_finales/metodo1/data__metodo1' #Cambia a la ruta donde hayas almacenado Data
imagePaths = os.listdir(dataPath)# en lista las carpetas en el dat 
ingresult="C:/Users/toled/OneDrive/Escritorio/archivos_finales/omg para nalisis de resultados"
imagesPathList = os.listdir(ingresult) 
print('imagePaths=',imagePaths)#imprime la lista de carpetas en el data 



face_recognizer = cv2.face.LBPHFaceRecognizer_create() #defino metodo de roconocimiento


# Leyendo el modelo
#face_recognizer.read('modeloLBPHFace.xml') 
#face_recognizer.read('modeloFisherFace.xml') 
face_recognizer.read('modeloEigenFace.xml') 
cap = cv2.VideoCapture(0)#defino la camar a utilizar 

faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')#modelo para reconocer rostros
count =0  #contador


for imageName in imagesPathList:#aqui me lee cada imagen de prueba y reconoce las caras de dichas fotos
	image = cv2.imread(ingresult+'/'+imageName)
	#image= rescla(image1 ,scale= .5)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)# la pone en escala de grises
	imageAux = gray.copy()
	
	
	faces = faceClassif.detectMultiScale(gray,
	scaleFactor=1.1, #parametres para ajustar el reconocimiento de rostros
	minNeighbors=4,
	minSize=(10,10),
	maxSize=(800,800))
	for (x,y,w,h) in faces:
		rostro = imageAux[y:y+h,x:x+w]
		rostro = cv2.resize(rostro,(150,150),interpolation= cv2.INTER_CUBIC)
		result = face_recognizer.predict(rostro)
		cv2.putText(image,'{}'.format(result),(x,y-5),1,1.3,(255,255,0),1,cv2.LINE_AA)
		if result[1] < 70 :
			cv2.putText(image,'{}'.format(imagePaths[result[0]]),(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
			cv2.rectangle(image, (x,y),(x+w,y+h),(0,255,0),2)
			
		else:
			cv2.putText(image,'Desconocido',(x,y-20),2,0.8,(0,0,255),1,cv2.LINE_AA)
			cv2.rectangle(image, (x,y),(x+w,y+h),(0,0,255),2)
			
		
    
	cv2.imshow('image',image)
	
	cv2.imwrite('C:/Users/toled/OneDrive/Escritorio/archivos_finales/resultados_metodo1/A_{}.jpg'.format(count),image)
	count=count+1
	cv2.waitKey(1)
	
	
cv2.destroyAllWindows()


	


