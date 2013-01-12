import pygame
from pygame.locals import *
# Autores: Luiggy Allauca, Juan Mite y Daniel Cuadrado
def main ():
	pygame.init()
	pantalla=pygame.display.set_mode((400,400))  	#Se definen las dimenciones de la pantalla
	pygame.display.set_caption("Escape Plan")
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
	sonintro.play()	#Se da inicio a un sonido
	
	while salir!=True:
	
		for event in pygame.event.get():
			
			if event.type == pygame.QUIT:
				salir = True
			if event.type == pygame.KEYDOWN:	#Identifica que se presiono una tecla
				if event.key == pygame.K_a:	#Comprobueba que se presiono la tecla "a"
					pygame.mixer.stop()	#Para todos los sonidos que se estuvieran ejecutandoce en el juego
					sontrapo.play()	#Se da inicio a un sonido
									
				elif event.key == pygame.K_0:
					pygame.mixer.stop()
					sonirfincasa.play()
										
				elif event.key == pygame.K_1:
					pygame.mixer.stop()	
					sonirfincasa.play()
								
				elif event.key == pygame.K_2:
					pygame.mixer.stop()
					sonfincasa.play()
							
				elif event.key == pygame.K_3:
					pygame.mixer.stop()	
					sonopcalle.play()
							
				elif event.key == pygame.K_o:
					pygame.mixer.stop()
					sonenelbar.play()		

				elif event.key == pygame.K_4:
					pygame.mixer.stop()
					sonfincasa.play()

				elif event.key == pygame.K_i:
					pygame.mixer.stop()		
					soncasajack.play()
								
				elif event.key == pygame.K_5:
					pygame.mixer.stop()
					sonenelbar.play()
							

				elif event.key == pygame.K_h:
					pygame.mixer.stop()		
					sonhuidafinexitoso.play()
								
				elif event.key == pygame.K_j:
					pygame.mixer.stop()
					sonhuidafinexitoso.play()


				elif event.key == pygame.K_6:
					pygame.mixer.stop()
					sonfincasa.play()

				elif event.key == pygame.K_p:
					pygame.mixer.stop()
					sonfinxrobo.play()

				elif event.key == pygame.K_x:
					pygame.mixer.stop()
					sonfinxrobo.play()

				elif event.key == pygame.K_u:
					pygame.mixer.stop()		
					sonfronsinami.play()

				elif event.key == pygame.K_y:
					pygame.mixer.stop()			
					sonpenultima.play()		
								
	
				elif event.key == pygame.K_7:
					pygame.mixer.stop()
					soncasajack.play()
									
				elif event.key == pygame.K_8:
					pygame.mixer.stop()
					sonarrestofonxrobo.play()
									
				elif event.key == pygame.K_9:
					pygame.mixer.stop()		
					sonroboauto.play()
					
				elif event.key == pygame.K_b:
					pygame.mixer.stop()
					sonrobarfarma.play()
					
		pantalla.fill((255,255,255))	#Se pinta de color blanco al fondo de la ventana
		pantalla.blit(fondo,(60,60))	#Se agrega la imagen de fondo a la ventana
		pygame.display.update()	#Actualiza la ventana
	pygame.quit()	
		
	
main()
