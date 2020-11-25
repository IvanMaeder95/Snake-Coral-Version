#FALTA VER PAUSA. Los segmentos se apilan uno encima de otro al pulsar "p".


import turtle
import time
import random

posponer = 0.12 #Para que corra más lento.
score = 0
high_score = 0

#Pantalla
window = turtle.Screen()
window.title("Snake: Coral Version")
window.bgcolor("yellowgreen")
window.setup(width = 500, height = 510)
window.tracer(0) #Mejora efecto visual ?)

#Cabeza
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white", "black")
head.penup() #Evita que quede el rastro por donde se movió nuestro objeto. En este caso head.
head.goto(0,0) #Establece la posición inicial de la serpiente.
head.direction = "stop"

#Comida
food = turtle.Turtle()
food.speed(0)
food.shape("turtle")
food.color("grey")
food.penup() #Evita que quede el rastro por donde se movió nuestro objeto. En este caso head.
food.goto(0,100) #Establece la posición inicial de la serpiente.

#Segmentos del cuerpo
segmentos = list()

#Puntaje
texto = turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0, 220)
texto.write("Score: 0     High Score: 0", align="center", font=("Bookman Old Style", 22, "bold"))


#Funciones

def up():
	head.direction = "up"

def down():
	head.direction = "down"

def left():
	head.direction = "left"

def right():
	head.direction = "right"

def pause():
	head.direction = "pause"

def movement():
	if head.direction == "up":
		y = head.ycor() #Almacena dónde está la variable "y".
		head.sety(y + 20) #Actualiza el valor de mi variable "y" para modificar la posición.

	if head.direction == "down":
		y = head.ycor() 
		head.sety(y - 20)

	if head.direction == "right":
		x = head.xcor() 
		head.setx(x + 20)

	if head.direction == "left":
		x = head.xcor() 
		head.setx(x - 20)
"""
REVISAR: debería detener todos los segmentos de la serpiente cuando se pone pausa pero no sucede.
	for segmento in segmentos:

	if head.direction == "pause" :
		x = head.xcor()
		head.setx(x)
		y = head.ycor()
		head.sety(y)
		for segmento in segmentos:
				x = segmento.xcor()
				segmento.setx(x)
				y = segmento.ycor()
				segmento.sety(y)
"""

#Teclado: Para que nuestro juego responda a nuestro teclado, nuestra ventana estará atenta a los movimientos.
window.listen()
window.onkeypress(up, "Up")
window.onkeypress(down, "Down")
window.onkeypress(left, "Left")
window.onkeypress(right, "Right")
#window.onkeypress(pause, "p") REVISAR (pausa).

while True:

	window.update() #Mantiene actualizada constantemente mi ventana donde corre el juego.

	#Colisiones borde
	if head.xcor() >= 250 or head.xcor() <= -250 or head.ycor() >= 250 or head.ycor() <= -250:
		time.sleep(1)
		head.goto(0,0)
		head.direction = "stop"
		
		for segmento in segmentos: #Esconder los segmentos ?)
			segmento.goto(1000, 1000)
		segmentos.clear() #Limpia la lista.

		#Borrar puntaje.
		texto.clear()
		score = 0
		texto.write(f"Score: {score}     High Score: {high_score}", align="center", font=("Bookman Old Style", 22, "bold"))

	#Colisión con el cuerpo de la serpiente.
	for segmento in segmentos:
		if segmento.distance(head) < 20:
			time.sleep(1)
			head.goto(0,0)
			head.direction = "stop"

			for segmento in segmentos: #Esconder los segmentos ?)
				segmento.goto(1000, 1000)
			segmentos.clear() #Limpia la lista.
				
			#Borrar puntaje.
			texto.clear()
			score = 0
			texto.write(f"Score: {score}     High Score: {high_score}", align="center", font=("Bookman Old Style", 22, "bold"))

	#Contacto con manzanas.
	# Condicional para reaparecer la comida en otro sitio si la serpiente la come.
	if head.distance(food) < 20:
		x = random.randint(-210, 210)
		y = random.randint(-210, 210)
		while x == head.xcor() or y == head.ycor():
			x = random.randint(-210, 210)
			y = random.randint(-210, 210)

		#REVISAR si funciona, debería evitar que se genere el alimento en donde está el cuerpo.
		for segmento in segmentos:
			while x == segmento.xcor() or y == segmento.ycor():
				x = random.randint(-210, 210)
				y = random.randint(-210, 210)
		food.goto(x, y)

		new_segmento = turtle.Turtle()
		new_segmento.speed(0)
		new_segmento.shape("square")
		new_segmento.penup() #Evita que quede el rastro por donde se movió nuestro objeto. En este caso head.
		segmentos.append(new_segmento)
		
		#Puntaje
		score += 1
		if score > high_score:
			high_score = score
		texto.clear()
		texto.write(f"Score: {score}     High Score: {high_score}", align="center", font=("Bookman Old Style", 22, "bold"))

		if (segmentos.index(new_segmento)) % 4 == 0:
			new_segmento.color("red")
		elif (segmentos.index(new_segmento)) % 2 != 0:
			new_segmento.color("white")
		else:
			new_segmento.color("black")
	#Negro - Blanco - Negro - Rojo

	#Movimiento de segmentos.
	total_segmentos = len(segmentos)
	for i in range(total_segmentos-1, 0, -1): #Permite que un elemento de mi lista pase a la posición de siguiente y así sucesivamente.
		x = segmentos[i - 1].xcor()
		y = segmentos[i - 1].ycor()
		segmentos[i].goto(x,y)

	if total_segmentos > 0:
		x = head.xcor()
		y = head.ycor()
		segmentos[0].goto(x,y)
	
	movement()

	time.sleep(posponer) #Para que el avance sea más lento se ejecuta el método con mi const "posponer".