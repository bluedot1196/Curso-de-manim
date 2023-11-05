from manim import *


class ejemplo(Scene):
	def construct(self):


		texto1 = Tex("Arriba").scale(2).to_edge(UP).set_color(BLUE) ##UP --> Arriba
		texto2 = Tex("Abajo").scale(2).to_edge(DOWN).set_color(YELLOW) #DOWN --> abajo
		texto3 = Tex("Izquierda").scale(2).to_edge(LEFT).set_color(PINK) #LEFT --> Izquierda
		texto4 = Tex("Derecha").scale(2).to_edge(RIGHT).set_color(ORANGE) #RIGHT --> Derecha

		self.play(Write(texto1), Write(texto2) , run_time = 2)
		self.wait()
		self.play(FadeIn(texto3), run_time = 2)
		self.wait()
		self.play(GrowFromCenter(texto4), run_time = 2)
		self.wait(4)

class ejemplo2(Scene):
	def construct(self):


		tex1 = Tex("arriba izquierda").to_corner(UL)
		tex2 = Tex("arriba derecha").to_corner(UR)
		tex3 = Tex("abajo izquierda").to_corner(DL)
		tex4 = Tex("abajo derecha").to_corner(DR)

		tex5 = Tex("centro")

		self.play(Write(tex1), run_time = 2)
		self.play(FadeIn(tex2), run_time = 2)
		self.play(GrowFromCenter(tex3), run_time = 2)
		self.play(Write(tex4), run_time = 2)
		self.play(GrowFromCenter(tex5), run_time = 2)
		self.wait(2)



class ejemplo3(Scene):
	def construct(self):


		plano_cartesiano = NumberPlane().add_coordinates()


		texto = Tex("Manim").scale(2).move_to([-5, -3, 0])

		self.play(Create(plano_cartesiano), run_time = 2)
		self.play(Write(texto))
		self.wait(5)


class ejemplo4(Scene):
	def construct(self):

		plano_cartesiano = NumberPlane().add_coordinates()

		referencia = Tex("Manim").scale(2).shift(3*UP + 2*RIGHT)

		self.add(plano_cartesiano)
		self.play(GrowFromCenter(referencia))
		self.wait(6)


class cuadratica(Scene):
	def construct(self):

		titulo = Title("Ecuación cuadrática").set_color(YELLOW_B)

		tex1 = Tex("Tiene la forma:").to_corner(UL).shift(DOWN)

		ecuacion = MathTex("ax^{2} + bx + c = 0").shift(1.5*UP)

		tex2 = Tex("Cuyas soluciones están dadas por:").to_corner(UL).shift(3*DOWN)

		formula_general = MathTex("x_{1, 2} = \\frac{-b \\pm \\sqrt{b^2 - 4ac}}{2a}").shift(DOWN)

		self.play(Write(titulo), run_time = 2)
		self.wait()
		self.play(Write(tex1))
		self.wait()
		self.play(Write(ecuacion), run_time = 2)
		self.wait()
		self.play(Write(tex2), run_time = 2)
		self.wait()
		self.play(Write(formula_general), run_time = 2)
		self.wait()

		##Para quitar cosas usamos el comando FadeOut

		self.play(FadeOut(titulo), FadeOut(tex1), FadeOut(ecuacion), FadeOut(tex2))

		##Para mover algo hacemos lo siguiente

		self.play(formula_general.animate.shift(UP), run_time = 2)
		self.wait()
		self.play(formula_general.animate.scale(2), run_time = 2)
		self.wait()
		self.play(formula_general.animate.set_color_by_gradient([RED, BLUE, YELLOW]), run_time = 2)

		self.play(FadeOut(formula_general))


		self.wait(5)




