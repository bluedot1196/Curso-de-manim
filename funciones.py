from manim import *

class funcion(Scene):
	def construct(self):


		plano = Axes(x_range = [-3, 3, 1],
			         y_range = [-1, 4, 1]).add_coordinates()

		etiquetas_ejes = plano.get_axis_labels(MathTex("x"), MathTex("f(x)"))

		self.play(Create(plano), Write(etiquetas_ejes))
		self.wait(2)

		funcion = plano.plot(lambda x: x**2, x_range = [-3, 3], color = BLUE)
		self.play(Create(funcion))
		self.wait(2)

class funcion2(Scene):
	def construct(self):

		ejes = Axes(x_range = [-3, 3, 1], 
			        y_range = [-3, 3, 1],
			        x_length = 8,
			        y_length = 7).add_coordinates()
		ejes.to_edge(LEFT)

		etiquetas_ejes = ejes.get_axis_labels(MathTex("x"), MathTex("f(x)"))

		funcion = ejes.plot(lambda x: x**3, x_range = [-4, 4], color = BLUE)

		funcion_cubica = MathTex("f(x) = x^3").scale(0.9).shift(3*UP + 4*RIGHT)

		punto = Dot().move_to(ejes.c2p(1, 1)).set_color(YELLOW)

		lineas_punto = ejes.get_lines_to_point(ejes.c2p(1,1)).set_color(RED)

		coordenadas = MathTex("(1, 1)").scale(0.9).next_to(punto, RIGHT, buff = 0.1)

		horizontal = ejes.get_horizontal_line(ejes.c2p(-1.1, funcion.underlying_function(-1.1)))

		vertical = ejes.get_vertical_line(ejes.c2p(-1.1, funcion.underlying_function(-1.1)))

		self.play(Create(ejes), Write(etiquetas_ejes), run_time = 2)
		self.wait(2)
		self.play(Create(funcion), run_time = 2)
		self.wait(2)
		self.play(Write(funcion_cubica), run_time = 2)
		self.wait(2)
		self.play(FadeIn(punto), Create(lineas_punto), Write(coordenadas), run_time = 2)
		self.wait(2)
		self.play(Create(horizontal), run_time = 2 )
		self.wait(2)
		self.play(Create(vertical), run_time = 2)
		self.wait(3)


class cuadratica(Scene):
	def construct(self):

		ejes = Axes(x_range = [-3,3,1],
			        y_range = [-1,6,1],
			        y_length = 7,
			        x_length = 8).add_coordinates()
		etiquetas_ejes = ejes.get_axis_labels(MathTex("x"), MathTex("f(x)"))

		funcion = ejes.plot(lambda x: x**2, x_range = [-4, 4], color = BLUE)

		self.play(Create(ejes), Write(etiquetas_ejes), run_time = 2)
		self.wait(2)
		self.play(Create(funcion), run_time = 2)
		self.wait(2)

		punto = Dot().move_to(ejes.c2p(-2, 4)).set_color(YELLOW)

		lineas = ejes.get_lines_to_point(ejes.c2p(-2,4))

		self.play(GrowFromCenter(punto), Create(lineas), run_time= 2)
		self.wait(2)

		## y = x**2   f(x)

		x = ValueTracker(-1)

		punto_movil = always_redraw(
			lambda: Dot().set_color(RED).move_to(ejes.c2p(x.get_value(), funcion.underlying_function(x.get_value()))) )

		linea_movil = always_redraw(
			lambda: ejes.get_lines_to_point(ejes.c2p(x.get_value(), funcion.underlying_function(x.get_value()))).set_color(YELLOW))

		self.play(Create(punto_movil), Create(linea_movil))
		self.wait(2)

		##Para mover el punto

		self.play(x.animate.set_value(2), run_time = 6)
		self.wait(2)


class grafica(Scene):
	def construct(self):

		ejes = Axes().add_coordinates()

		#f(x) = ax^2

		funcion = ejes.plot(lambda x: x**2, x_range = [-3, 3], color = BLUE)

		a = ValueTracker(1)
		b = ValueTracker(0)
		c = ValueTracker(0)

		##f(x) = ax^2 + bx + c

		funcion_movil = always_redraw(
			lambda: ejes.plot(lambda x: a.get_value()*x**2 + b.get_value()*x + c.get_value(), x_range = [-3, 3], color = YELLOW))

		self.play(Create(ejes))
		self.wait(2)
		self.play(Create(funcion))
		self.wait(2)
		self.play(Create(funcion_movil))
		self.wait(2)

		##animar para el valor de a

		self.play(a.animate.set_value(10), run_time = 5)
		self.wait(2)
		self.play(a.animate.set_value(-10), rate_func = there_and_back, run_time = 6)
		self.wait(2)
		self.play(b.animate.set_value(3), c.animate.set_value(-3), run_time = 5)
		self.wait(2)
