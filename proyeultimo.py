import pygame
from pygame.locals import *
# Autores: Luiggy Allauca, Juan Mite y Daniel Cuadrado
def main ():
	pygame.init()	#Inicializa la libreria pygame
	pantalla=pygame.display.set_mode((400,400))  	#Se definen las dimenciones de la pantalla
	pygame.display.set_caption("Escape Plan")	#se definio el nombre a la ventana
	salir=False
	fondo=pygame.image.load("logo.jpg")	#Se carga la imagen de fondo de la pantalla
	#Se cargan todos los sonidos del juego a una variable
	sontrapo=pygame.mixer.Sound("trapo_brazo.wav")
	sonrobarfarma=pygame.mixer.Sound("final_robar_farmacia.wav")
	sonprella=pygame.mixer.Sound("preguntar_si_llamar.wav")
	sonircasa=pygame.mixer.Sound("ir a casa.wav")
	sonfincasa=pygame.mixer.Sound("fin casa.wav")
	sonopcalle=pygame.mixer.Sound("opcion_calle.wav")
	sonenelbar=pygame.mixer.Sound("en el bar.wav")
	soncasajack=pygame.mixer.Sound("casa de jack.wav")
	sonfinxrobo=pygame.mixer.Sound("fin_por_robo.wav")
	sonroboauto=pygame.mixer.Sound("robo_auto.wav")
	sonfronsinami=pygame.mixer.Sound("en la frontera sin amigo.wav")
	sonarresto=pygame.mixer.Sound("arresto.wav")
	sonpenultima=pygame.mixer.Sound("penultima.wav")
	sonhuidafin=pygame.mixer.Sound("uida_final.wav")
	sonfinexito=pygame.mixer.Sound("final_exitoso.wav")
	sonintro=pygame.mixer.Sound("intro.wav")
	sonirfincasa=pygame.mixer.Sound("audio1_ircasa_fincasa.wav")
	sonarrestofonxrobo=pygame.mixer.Sound("audio2_arresto_finxrobo.wav")
	sonarrefinrobo=pygame.mixer.Sound("audio3_arresto_finxrobo.wav")
	sonhuidafinexitoso=pygame.mixer.Sound("audio4_huidafinal_finalexitoso.wav")
	sonintro.play()	#Se da inicio al sonido introductorio
	
	while salir!=True:
	
		for event in pygame.event.get():
			
			if event.type == pygame.QUIT:
				salir = True
			if event.type == pygame.KEYDOWN:	#Identifica que se presiono una tecla
				if event.key == pygame.K_a:	#Comprueba que se presiono la tecla "a" que da inicio a la historia en la que el brazo del fugitivo se ve herido
					pygame.mixer.stop()	#Para todos los sonidos que se estuvieran ejecutandoce en el juego
					sontrapo.play()	#Se da inicio al sonido
									
				elif event.key == pygame.K_0:	#Comprueba que se presiono la tecla "0" donde el fugitivo puede ir a la casa y permanecer oculto
					pygame.mixer.stop()	#Para todos los sonidos que se estuvieran ejecutandoce en el juego
					sonirfincasa.play()	#Se da inicio al sonido
										
				elif event.key == pygame.K_1:	#Comprueba que se presiono la tecla "0" donde el fugitivo puede ir a la casa y permanecer oculto
					pygame.mixer.stop()	#Para todos los sonidos que se estuvieran ejecutandoce en el juego
					sonirfincasa.play()	#Se da inicio al sonido
								
				elif event.key == pygame.K_2:	#Comprueba que se presiono la tecla "2" donde el fugitivo muere
					pygame.mixer.stop()	#Para todos los sonidos que se estuvieran ejecutandoce en el juego
					sonfincasa.play()	#Se da inicio al sonido
							
				elif event.key == pygame.K_3:	#Comprueba que se presiono la tecla "3" donde el fugitivo permanece en la calle
					pygame.mixer.stop()	#Para todos los sonidos que se estuvieran ejecutandoce en el juego
					sonopcalle.play()	#Se da inicio al sonido
							
				elif event.key == pygame.K_o:	#Comprueba que se presiono la tecla "o" donde el fugitivo entra a la cantina
					pygame.mixer.stop()	#Para todos los sonidos que se estuvieran ejecutandoce en el juego
					sonenelbar.play()	#Se da inicio al sonido

				elif event.key == pygame.K_4:	#Comprueba que se presiono la tecla "4" donde el fugitivo muere
					pygame.mixer.stop()	#Para todos los sonidos que se estuvieran ejecutandoce en el juego
					sonfincasa.play()	#Se da inicio al sonido

				elif event.key == pygame.K_i:	#Comprueba que se presiono la tecla "i" donde el fugitivo pide ayuda a un amigo
					pygame.mixer.stop()	#Para todos los sonidos que se estuvieran ejecutandoce en el juego
					soncasajack.play()	#Se da inicio al sonido
								
				elif event.key == pygame.K_5:	#Comprueba que se presiono la tecla "5" donde el fugitivo entra a la cantina
					pygame.mixer.stop()	#Para todos los sonidos que se estuvieran ejecutandoce en el juego
					sonenelbar.play()	#Se da inicio al sonido
							

				elif event.key == pygame.K_h:	#Comprueba que se presiono la tecla "h" donde el fugitivo escapa de la prision y tiene un final exitoso
					pygame.mixer.stop()	#Para todos los sonidos que se estuvieran ejecutandoce en el juego
					sonhuidafinexitoso.play()	#Se da inicio al sonido
								
				elif event.key == pygame.K_j:	#Comprueba que se presiono la tecla "j" donde el fugitivo escapa de la prision y tiene un final exitoso
					pygame.mixer.stop()	#Para todos los sonidos que se estuvieran ejecutandoce en el juego
					sonhuidafinexitoso.play()	#Se da inicio al sonido


				elif event.key == pygame.K_6:	#Comprueba que se presiono la tecla "6" donde el fugitivo muere
					pygame.mixer.stop()	#Para todos los sonidos que se estuvieran ejecutandoce en el juego
					sonfincasa.play()	#Se da inicio al sonido

				elif event.key == pygame.K_p: #Comprueba que se presiono la tecla "p" donde el fugitivo se retira de la compañia del amigo
					pygame.mixer.stop()	#Para todos los sonidos que se estuvieran ejecutandoce en el juego
					sonfinxrobo.play()	#Se da inicio al sonido

				elif event.key == pygame.K_x: #Comprueba que se presiono la tecla "x" donde el fugitivo huye de la policia
					pygame.mixer.stop()	#Para todos los sonidos que se estuvieran ejecutandoce en el juego
					sonfinxrobo.play()	#Se da inicio al sonido

				elif event.key == pygame.K_u:	#Comprueba que se presiono la tecla "u" donde el fugitivo elige entre confrontar y huir
					pygame.mixer.stop()	#Para todos los sonidos que se estuvieran ejecutandoce en el juego
					sonfronsinami.play()	#Se da inicio al sonido

				elif event.key == pygame.K_y:	#Comprueba que se presiono la tecla "u" donde el fugitivo elige entre confrontar y huir
					pygame.mixer.stop()	#Para todos los sonidos que se estuvieran ejecutandoce en el juego
					sonpenultima.play()	#Se da inicio al sonido
								
	
				elif event.key == pygame.K_7:	#Comprueba que se presiono la tecla "7" donde el fugitivo pide ayuda a un amigo
					pygame.mixer.stop()	#Para todos los sonidos que se estuvieran ejecutandoce en el juego
					soncasajack.play()	#Se da inicio al sonido
									
				elif event.key == pygame.K_8:	#Comprueba que se presiono la tecla "8" donde el fugitivo muere despues del robo que hizo
					pygame.mixer.stop()	#Para todos los sonidos que se estuvieran ejecutandoce en el juego
					sonarrestofonxrobo.play()	#Se da inicio al sonido
									
				elif event.key == pygame.K_9:	#Comprueba que se presiono la tecla "9" donde el fugitivo roba un auto
					pygame.mixer.stop()	#Para todos los sonidos que se estuvieran ejecutandoce en el juego
					sonroboauto.play()	#Se da inicio al sonido
					
				elif event.key == pygame.K_b:	#Comprueba que se presiono la tecla "b" donde el fugitivo va a robar a la farmacia
					pygame.mixer.stop()	#Para todos los sonidos que se estuvieran ejecutandoce en el juego
					sonrobarfarma.play()	#Se da inicio al sonido
					
		pantalla.fill((255,255,255))	#Se pinta de color blanco al fondo de la ventana
		pantalla.blit(fondo,(60,60))	#Se agrega la imagen de fondo a la ventana
		pygame.display.update()	#Actualiza la ventana
	pygame.quit()	#finaliza la libreria pygame
		
	
main()
