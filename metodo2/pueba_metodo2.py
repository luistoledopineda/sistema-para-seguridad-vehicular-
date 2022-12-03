import cv2 # pip install opencv-python
import face_recognition#conda install -c conda-forge face_recognition
import os
import matplotlib.pyplot as plt#pip install matplotlib
img30= "C:/Users/toled/OneDrive/Escritorio/archivos_finales/omg para nalisis de resultados"#ruta en donde tengo las fotos con las que quiero probar
imagesPathList = os.listdir(img30) #en listo las fotos de img30
imgpath= ("C:/Users/toled/OneDrive/Escritorio/archivos_finales/metodo2/usuarios")#imagenes con los rostros registrados con el nombre como titulo 
facesencodins=[]#string donde se guardan los vectores de las caras a reconocer 
facesnames=[]#lista de nombres de las caras a reconocer



faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')#modelo de opencv de reconocimiento de rostros
count = 0#contador para almazanar los rezultado
for file_name in os.listdir(imgpath): # este for me guarda los nombres de los rostros a reconocer y tambien los vectoresde los rostros a reconocer
    image=cv2.imread(imgpath + "/" + file_name)
    image=cv2.cvtColor(image , cv2.COLOR_BGR2RGB)

    f_coding= face_recognition.face_encodings(image,known_face_locations=[(0,150,150,0)])[0]#aqui saca los vectores 
    facesencodins.append(f_coding)
    facesnames.append(file_name.split(".")[0])

for imageName in imagesPathList:#aqui me lee cada imagen de prueba y reconoce las caras de dichas fotos
	image = cv2.imread(img30+'/'+imageName)
	#image= rescla(image1 ,scale= .5)
	imageAux = image.copy()
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)# la pone en escala de grises
	
	faces = faceClassif.detectMultiScale(gray,
	scaleFactor=1.1, #parametres para ajustar el reconocimiento de rostros
	minNeighbors=4,
	minSize=(100,100),
	maxSize=(800,800))

	
	for (x,y,w,h) in faces:
		
		face = imageAux[y:y+h,x:x+w]
		face =cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
		actual_encodin=face_recognition.face_encodings(face,known_face_locations=[(0,w,h,0)])[0]# le saca los vectoresa las caras 
		result= face_recognition.compare_faces(facesencodins,actual_encodin)# en compara los vectores de lasa reconocer y los de la imagenes de prueca y lo guarda en result
		#print(result)#muestra los resultado en un string si se quiere
		#print(facesnames)#muestra una lista con los nombres de las personas a reconoce si se quiere 
		if True in result:# si  hay un verdadero en result significa que una persona a reconocer se encuentra en la foto
			index= result.index(True)
			name=facesnames[index]#identifica cual es la persona reconocida
			coloor=(125,220,0)#define un color verde 
			ace="permitido "
		else:
			name = "desconoicido"#en caso contrario le pone la etiqueta desconocido
			coloor=(50,50,255)#y le da un color rojo
			ace=" no permitido "#y le da un color rojo           
		cv2.rectangle(image, (x,y),(x+w,y+h),coloor,2)#define un rectagulo con el color que se determina en el if
		cv2.putText(image,name,(x,y+h+25),2,1,coloor,1, cv2.LINE_AA)#le pone un nombre o un desconocido dependiendo del if
		cv2.putText(image,ace,(x,y+h+50),2,1,coloor,1, cv2.LINE_AA)#le pone un nombre o un desconocido dependiendo del if        cv2.putText(image,ace,(x,y+h+20),2,1,coloor,1, cv2.LINE_AA)#le pone un nombre o un desconocido dependiendo del i
	cv2.imshow('image',image)#muestra la img
	cv2.waitKey(0)#espera a que una tecla sea presionada
	
	cv2.imwrite('C:/Users/toled/OneDrive/Escritorio/archivos_finales/resultados_metodo2/R_{}.jpg'.format(count),image)#para visualizar mejor los resultados d¿se guardan las imagenes en la carpeta resultados adjunta
	count = count +1#cuenta que sirve para guardar los resultado
	