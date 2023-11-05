from manim import *

class texto(Scene):
	def construct(self):

		hola = Tex("M","a","n","i","m")  #Tex: Sirve para guardar texto
		#           0   1   2   3   4

		hola.scale(3)   #scale: modifica el tamaño
		hola[0].set_color(RED)  #set_color: cambia el color
		hola[1].set_color(YELLOW)
		hola[2].set_color(BLUE)
		hola[3].set_color(ORANGE)
		hola[4].set_color(PINK)


		self.play(Write(hola), run_time = 3)
		self.wait(5)

class texto2(Scene):
	def construct(self):

		hola = Tex("Holaaaaa: $2x + 1$")

		self.play(Write(hola), run_time = 2)
		self.wait(2)




class ecuacion(Scene):
	def construct(self):

		mi_ecuacion = MathTex("3","x", "+", "5", "=", "17").scale(2)
		#                      0   1    2    3    4    5

		mi_ecuacion[1].set_color(YELLOW)
		mi_ecuacion[2].set_color(RED)
		mi_ecuacion[4].set_color(RED)
    
		self.play(Write(mi_ecuacion), run_time = 2)
		self.wait(2)


class ecuacion2(Scene):
	def construct(self):

		variable = MathTex(" x_{1, 2} = \\frac{-b \\pm \\sqrt{b^2 - 4ac} }{2a} ").scale(2.4)

		self.play(Write(variable), run_time = 2)
		self.wait(4)

class ecuacion3(Scene):
	def construct(self):

		variable = MathTex("\\int_{2}^{10} f(x) dx = 45").scale(2)

		self.play(Write(variable), run_time = 2)
		self.wait(4)


class ecuacion4(Scene):
	def construct(self):

		variable = MathTex("\\clubsuit").scale(2)

		self.play(Write(variable), run_time = 2)
		self.wait(4)


