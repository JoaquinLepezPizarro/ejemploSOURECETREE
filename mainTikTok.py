from asyncio.windows_events import NULL
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from time import sleep
import pyautogui
from datetime import datetime
from datetime import date
#import mysql.connector
import MySQLdb
import pymysql.cursors
import pymysql


###         ATENCION: En vista de que habia que priorizar el resultado por la fecha de entre, todas las acciones fueron hechas en UN MISMO archivo.           ###
###         Sabemos que esto no se considera buena practica, pero era para agilizar resultados. En una futura entrega separaremos todo en archivos.           ###


def get(url):
     driver.get(url)

service = Service(executable_path="C:\Program Files\SeleniumBasic/chromedriver.exe")
options = Options()

#pantalla maximizada
options.add_argument('--start-maximized')

#deshabilita extensiones
options.add_argument('--disable-extensions')

#elimina errores consola
options.add_experimental_option('excludeSwitches', ['enable-logging'])

# driver = webdriver.Chrome(options=options)
driver = webdriver.Chrome(service=service, options=options)



#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------CAPTCHA-------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
driver.get('https://www.tiktok.com/')

flag = False
nombreUsuario = ''

sleep(10)

#ITERACIÓN HASTA QUE SE DESACTIVE EL CAPTCHA
while flag == False:
    #MOUSE HACE EL MOVIMIENTO SIEMPRE AL MEDIO PARA DESACTIVAR EL CAPTCHA
    pyautogui.moveTo(543, 536)
    pyautogui.dragTo(684, 532, 0.5, button='left')
    sleep(3)

    #TOMA EL NOMBRE DE USUARIO
    nombreUsuario = (driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div[2]/div[1]/div[4]/div/div[1]/div[1]/a[2]/h3')).text
    if nombreUsuario != '':
        flag = True

sleep(3)




#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------INICIAR SESION CON FACEBOOK-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------

driver.get('https://www.facebook.com/login.php?skip_api_login=1&api_key=1862952583919182&kid_directed_site=0&app_id=1862952583919182&signed_next=1&next=https%3A%2F%2Fwww.facebook.com%2Fv2.9%2Fdialog%2Foauth%2F%3Fclient_id%3D1862952583919182%26response_type%3Dtoken%26redirect_uri%3Dhttps%253A%252F%252Fwww.tiktok.com%252Flogin%252F%26state%3D%257B%2522client_id%2522%253A%25221862952583919182%2522%252C%2522network%2522%253A%2522facebook%2522%252C%2522display%2522%253A%2522popup%2522%252C%2522callback%2522%253A%2522_hellojs_1vkopkzv%2522%252C%2522state%2522%253A%2522%2522%252C%2522redirect_uri%2522%253A%2522https%253A%252F%252Fwww.tiktok.com%252Flogin%252F%2522%252C%2522scope%2522%253A%2522basic%2522%257D%26scope%3Dpublic_profile%26auth_type%3Dreauthenticate%26display%3Dpopup%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D646a07fd-2be7-4644-bfcd-0434ccefa23d%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.tiktok.com%2Flogin%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522client_id%2522%253A%25221862952583919182%2522%252C%2522network%2522%253A%2522facebook%2522%252C%2522display%2522%253A%2522popup%2522%252C%2522callback%2522%253A%2522_hellojs_1vkopkzv%2522%252C%2522state%2522%253A%2522%2522%252C%2522redirect_uri%2522%253A%2522https%253A%252F%252Fwww.tiktok.com%252Flogin%252F%2522%252C%2522scope%2522%253A%2522basic%2522%257D%23_%3D_&display=popup&locale=es_ES&pl_dbl=0')
sleep(3)

#INGRESA CORREO
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,'//*[@id="email"]')))\
    .send_keys('testing.0000.analitic@gmail.com')
sleep(0.1)

#INGRESA CONTRASEÑA
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,'//*[@id="pass"]')))\
    .send_keys('CortexIA00')
sleep(0.1)

#CLICK EN ENTRAR     
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,'//*[@id="loginbutton"]')))\
    .click()
sleep(5)

#CLICK EN ENTRAR     
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div/div[1]/div/div[1]/div[2]/div[3]')))\
    .click()
sleep(9)




#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------SCRAPING: PERFIL DE USUARIO-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
#BUSCA UN USUARIO
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/form/input')))\
    .send_keys('joseantoniokast')#------------------------------------------------------------------------------------------------->¡ACA INGRESAR ID PERFIL PARA HACER SCRAPING!
    #.send_keys('anfp_ilegal')
    #.send_keys('valecaballerof')
    #.send_keys('joseantoniokast')
sleep(0.5)

#HACE CLICK EN BUSCAR
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/form/button')))\
    .click()
sleep(2)

#SELECCIONA LA CUENTA
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div[2]/div[2]/div[2]/div[1]/div/div[1]/div[2]/a[2]/p[1]')))\
    .click()
sleep(2)

#TOMA LA ID DEL PERFIL (i)
idPerfil = (driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div[2]/div/div[1]/div[1]/div[2]/h2')).text
#print("idPerfil: " + idPerfil)

#TOMA EL NOMBRE DEL PERFIL
nombrePerfil = (driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div[2]/div/div[1]/div[1]/div[2]/h1')).text
#print("nombrePerfil: " + nombrePerfil)

#FUNCION PARA TRANSFORMAR CANTIDADES------------------------------------------------------------------->(ESTE METODO NO ES DE CREACION PROPIA, FUE EXTRAIDO DE LA VERSION ANTERIOR DEL PROYECTO)
def transformarCantidad(cantidad):
    if cantidad.isnumeric():
        return int(cantidad)
    mult = 0
    splitted = ''
    if 'K' in cantidad:
        mult = 1000
        splitted = cantidad.split('K')[0]
    if 'M' in cantidad:
        mult = 1000000
        splitted = cantidad.split('M')[0]
    if 'B' in cantidad:
        mult = 1000000000
        splitted = cantidad.split('B')[0]
    if '.' not in splitted:
        return int(splitted)*mult
    numb = splitted.split('.')
    numK = int(numb[0])*mult
    numC = int(numb[1])*mult/10
    num = numK + numC
    return int(num)

#TOMA LA CANTIDAD DE SEGUIDORES
seguidoresPerfil = (driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div[2]/div/div[1]/h2[1]/div[2]/strong')).text
seguidoresPerfil = transformarCantidad(seguidoresPerfil)
#print("seguidoresPerfil: " + str(seguidoresPerfil))

#TOMA LA CANTIDAD DE SIGUIENDO   
siguiendoPerfil = (driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div[2]/div/div[1]/h2[1]/div[1]/strong')).text
siguiendoPerfil = transformarCantidad(siguiendoPerfil)
#print("siguiendoPerfil: " + str(siguiendoPerfil))

#TOMA LA CANTIDAD DE ME GUSTA DEL PERFIL
meGustaPerfil = (driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div[2]/div/div[1]/h2[1]/div[3]/strong')).text
meGustaPerfil = transformarCantidad(meGustaPerfil)
#print("meGustaPerfil: " + str(meGustaPerfil))

#TOMA LA DESCRIPCION DEL PERFIL
descripcionPerfil = (driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div[2]/div/div[1]/h2[2]')).text
#print("descripcionPerfil: " + descripcionPerfil)

#TOMA LA URL DEL PERFIL
urlPerfil = driver.current_url




#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------SCRAPING: VIDEOS DE PERFIL------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
#BUCLE DE METODOS SOBRE TODOS LOS VIDEOS DE UNA CUENTA PARA EL SCRAPING
listaReproduccionesVideo = []
contVideos = 0
flagTotalVideos = False

#HACER SCROLL DOWN HASTA EL FINAL DE LA PAGINA, PARA TOMAR TODOS LOS VIDEOS
def finalDePagina(driver):
    posisionNueva = None
    posicionActual = 0

    #BUCLE HASTA LLEGAR AL FINAL DE LA PAGINA. SE VA A REPETIR HASTA QUE NO HAYAN MAS "NUEVAS POSICIONES"
    while posisionNueva != posicionActual:

        #DETERMINAR POSICION ANTIGUA    
        posicionActual = driver.execute_script((   "return (window.pageYOffset !== undefined) ?"
                                                    " window.pageYOffset : (document.documentElement ||"
                                                    " document.body.parentNode || document.body);"))
        #PAUSA PARA DEJAR QUE CARGUEN LOS NUEVOS VIDEOS. SI SE CAE, HAY QUE SUMAR TIEMPO ACA
        #sleep(3)
        
        #HACER EL SCROLL
        driver.execute_script((     "var scrollingElement = (document.scrollingElement ||"
                                    " document.body);scrollingElement.scrollTop ="
                                    " scrollingElement.scrollHeight;"))
        sleep(3)

        #DETERMINAR LA NUEVA POSICION
        posisionNueva = driver.execute_script((    "return (window.pageYOffset !== undefined) ?"
                                                    " window.pageYOffset : (document.documentElement ||"
                                                    " document.body.parentNode || document.body);"))
finalDePagina(driver)


#BUCLE INICIAL PARA OBTENER LA CANTIDAD DE VIDEOS Y LA CANTIDAD DE REPRODUCCIONES POR VIDEO 
while flagTotalVideos == False:
    #CONVIERTE EL INDICE DE VIDEOS A STRING
    contVideos = contVideos + 1
    stringcontVideos = str(contVideos)


    #PARA HACER EL SIGUIENTE BUCLE FUE NECESARIO CONSIDERAR DOS FORMATOS DE XPATH DISTINTOS, SEGUN SI TENIAN UNA ALERTA EN RELACION O AL COVID O SOBRE EL RIESGO DE LA ACTIVIDAD IMPLICADA
    #VE SI EXISTE UN SIGUIENTE VIDEO SIN MENSAJE DE ALERTA 
    try:
        reproduccionesVideo = (driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div[2]/div/div[2]/div[2]/div/div[REEMPLAZAR]/div[1]/div/div/a/div/div[2]/strong'.replace('REEMPLAZAR',stringcontVideos))).text
        reproduccionesVideo = transformarCantidad(reproduccionesVideo)
        listaReproduccionesVideo.append(reproduccionesVideo)
    
    except:
        #VE SI EXISTE UN SIGUIENTE VIDEO CON MENSAJE DE ALERTA
        try:
            reproduccionesVideo = (driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div[2]/div/div[2]/div[2]/div/div[REEMPLAZAR]/div/div/div/a/div/div[3]/strong'.replace('REEMPLAZAR',stringcontVideos))).text
            reproduccionesVideo = transformarCantidad(reproduccionesVideo)
            listaReproduccionesVideo.append(reproduccionesVideo)
        except:
            #print("NO HAY MAS VIDEOS")
            flagTotalVideos = True

#CLICK EN EL PRIMER VIDEO PARA LA EXTRACCION DE LOS DATOS RESTANTES
WebDriverWait(driver, 2)\
    .until(EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div[2]/div[2]/div/div[2]/div[2]/div/div[1]/div[1]/div/div/a/div/div[1]')))\
    .click()
sleep(1)

#SE DECLARAN LISTAS PARA ALMACENAR LOS DATOS RESTANTES DE CADA VIDEO (O SEA, TODOS MENOS LA CANTIDAD DE REPRODUCCIONES, QUE YA SE TOMO)
listaDescripcionVideo = []
listaMeGustaVideo = []
listaComentariosVideo = []
listaCancionVideo = []
listaEngagementVideo = []
listaUrlVideo = []
listaIdFechaVideo = []
listaFechaVideo = []

#OBTENER LOS DATOS RESTANTES DEL VIDEO
for i in range(contVideos-1):

    #TOMA LA DESCRIPCIÓN DEL VIDEO
    descripcionVideo = (driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div[3]/div[2]/div[2]/div[1]')).text
    listaDescripcionVideo.append(descripcionVideo)
    #print("descripcionVideo: " + descripcionVideo)

    #TOMA LOS ME GUSTA DE UN VIDEO
    meGustaVideo = (driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div[3]/div[2]/div[2]/div[2]/div[1]/div[1]/button[1]/strong')).text
    meGustaVideo = transformarCantidad(meGustaVideo)
    listaMeGustaVideo.append(meGustaVideo)
    #print("meGustaVideo: " + meGustaVideo)

    #TOMA LA CANTIDAD DE COMENTARIOS DE UN VIDEO
    comentariosVideo = (driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div[3]/div[2]/div[2]/div[2]/div[1]/div[1]/button[2]/strong')).text
    comentariosVideo = transformarCantidad(comentariosVideo)
    listaComentariosVideo.append(comentariosVideo)
    #print("comentariosVideo: " + comentariosVideo)

    #TOMA LA CANCIÓN DEL VIDEO
    cancionVideo = (driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div[3]/div[2]/div[2]/h4/a')).text
    listaCancionVideo.append(cancionVideo)
    #print("cancionVideo: " + cancionVideo)

    #TOMA LA URL DEL VIDEO
    urlVideo = driver.current_url
    listaUrlVideo.append(urlVideo)

    #TOMA LA ID DEL VIDEO A PARTIR DE LA URL
    splitPorInterrogacion = urlVideo.split("?")
    splitPorSlash = splitPorInterrogacion[0].split("/")
    idFechaVideo = splitPorSlash[-1]
    listaIdFechaVideo.append(idFechaVideo)

    #METODO PARA TRANSFORMAR LA ID DE VIDEO EN FECHA
    def fechaxId(idFechaVideo):
        numero = int(idFechaVideo)
        numero = '0' + f'{numero:08b}'
        numero = int(numero[:32], 2)
        fecha = datetime.utcfromtimestamp(numero)
        return fecha
    
    #OBTIENE LA FECHA A PARTIR DE LA ID
    fechaVideo = fechaxId(idFechaVideo)
    listaFechaVideo.append(fechaVideo)

    #OBTIENE EL ENGAGMENET
    engagementVideo = ((int(meGustaVideo) + int(comentariosVideo)) / int(listaReproduccionesVideo[i])) * 100
    listaEngagementVideo.append(engagementVideo)

    #DETERMINAR SI HAY UN VIDEO SIGUIENTE PARA CONTINUAR LA EXTRACCION DE DATOS
    try:
        WebDriverWait(driver, 5)\
            .until(EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div[2]/div[3]/div[1]/button[3]')))\
            .click()
        sleep(2)
    except:
        print("Scraping realizado con exito.")


# #TESTING SCRAPING
# for i in range(contVideos-1):
#     print('')
#     print('')
#     print("DATOS DEL VIDEO NUMERO: " + str(i))
#     print("   Reproducciones x video: " + str(listaReproduccionesVideo[i]))
#     print("   Descripcion x video: " + str(listaDescripcionVideo[i]))
#     print("   Me gusta x video: " + str(listaMeGustaVideo[i]))
#     print("   Comentarios x video: " + str(listaComentariosVideo[i]))
#     print("   Cancion x video: " + str(listaCancionVideo[i]))
#     print("   Url x video: " + str(listaUrlVideo[i]))
#     print("   Id x video: " + str(listaIdFechaVideo[i]))
#     print("   Fecha x video: " + str(listaFechaVideo[i]))
#     print("   Engagement x video: " + str(listaEngagementVideo[i]))  




#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------BASE DE DATOS-------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
#CONECTAR A LA BASE DE DATOS
bd = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    db='tiktok'
)

# #CONECTAR A LA BASE DE DATOS DE PERFILES
# bd = pymysql.connect(
# #bd = pymysql.connector.connect(
#     host = 'localhost',
#     user = 'root',
#     password = '',
#     db='perfiles'
# )

# #CONECTAR A LA BASE DE DATOS DE VIDEOS
# bdVideos = pymysql.connect(
# #bdVideos = pymysql.connector.connect(
#     host = 'localhost',
#     user = 'root',
#     password = '',
#     db='videosxPerfil'
# )


#GUARDAR LOS DATOS DE UN PERFIL
fechaActualizacionPerfil = datetime.today()
tiktok = bd.cursor()
sqlPerfilConsulta = "INSERT INTO perfil (idPerfil, nombrePerfil, seguidoresPerfil, siguiendoPerfil, meGustaPerfil, descripcionPerfil, fechaActualizacionPerfil, urlPerfil) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
sqlPerfilDatos = (idPerfil, nombrePerfil, seguidoresPerfil, siguiendoPerfil, meGustaPerfil, descripcionPerfil, fechaActualizacionPerfil, urlPerfil)
tiktok.execute(sqlPerfilConsulta, sqlPerfilDatos)
bd.commit()
tiktok.close()



#GUARDAR LOS DATOS DE TODOS LOS VIDEOS DE UN PERFIL EN LA BASE DE DATOS
tiktok = bd.cursor()
for i in range(contVideos-1):
    sqlVideosConsulta = "INSERT INTO videosxPerfil (reproduccionesVideo, descripcionVideo, meGustaVideo, comentariosVideo, cancionVideo, engagementVideo, urlVideo, idFechaVideo, fechaVideo, idPerfil) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    sqlVideosDatos = (listaReproduccionesVideo[i], listaDescripcionVideo[i], listaMeGustaVideo[i], listaComentariosVideo[i], listaCancionVideo[i], listaEngagementVideo[i], listaUrlVideo[i], listaIdFechaVideo[i], listaFechaVideo[i], idPerfil)
    tiktok.execute(sqlVideosConsulta, sqlVideosDatos)
    bd.commit()
tiktok.close()

print("Datos almacenados en la base de datos.")


    






#---------------------------PENDIENTES---------------------------
#RECIBIR EL ID DE CUENTA PARA EVALUAR SI EXISTE EN LA BD


#EXISTE: ACTUALIZAR SCRAPING DEL PERFIL


#NO EXISTE: REALIZAR SCRAPING DEL PERFIL







#-----------------------------EXTRAS-----------------------------
# #SELECCIONA EL NOMBRE DE TODOS LOS PERFILES
# def selectidPerfil():
#     tiktok = bd.cursor()
#     tiktok.execute("SELECT nombre FROM perfiles")
#     datos = tiktok.fetchall()
#     tiktok.close()
#     bd.close()
#     return datos 

# #SELECCIONA TODOS DATOS DE UN PERFIL
# def selectDatosPerfil(idPerfil):
#     tiktok = bd.cursor()
#     tiktok.execute("SELECT * FROM perfiles WHERE idPerfil='{}'".format(idPerfil))
#     datos = tiktok.fetchall()
#     tiktok.close()
#     bd.close()
#     return datos 

# #SELECCIONA TODOS LOS VIDEOS DE UN PERFIL
# def selectVideosxPerfil(idPerfil):
#     tiktok = bdVideos.cursor()
#     tiktok.execute("SELECT * FROM videosxPerfil WHERE idPerfil='{}'".format(idPerfil))
#     datos = tiktok.fetchall()
#     tiktok.close()
#     bdVideos.close()
#     return datos 