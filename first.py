#Primer programa en python, dibujar con dos puntos en pantalla
import turtle

window = turtle.Screen()
jhon= turtle.Turtle()
diana =turtle.Turtle()

for x in range(1,9):
	jhon.forward(50)
	diana.forward(50)

	jhon.left(45)
	diana.left(135)

	jhon.forward(50)
	diana.forward(50)

	jhon.left(45)
	diana.left(135)

	jhon.forward(50)
	diana.forward(50)

	jhon.left(45)
	diana.left(135)

	diana.forward(50)
	jhon.forward(50)

	x=x+1
		
	pass

#for y in range(1,10):
#y=y+1
#	pass

turtle.mainloop()