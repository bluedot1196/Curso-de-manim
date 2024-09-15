from manim import *

class derivada(Scene):
	def construct(self):

		ejes = Axes(x_range = [-3, 3, 1],
			        y_range = [-1, 8, 2],
			        x_length = 10,
			        y_length = 7).add_coordinates()

		funcion = ejes.plot(lambda x: x**2, x_range = [-3, 3], color = BLUE)


		##Vamos a construir la recta secante a la funcion

		secante = ejes.get_secant_slope_group(
			x = -2,
			dx = 0.001,
			graph = funcion,
			dx_label = "horizontal",
			dy_label = "vertical",
			dx_line_color = YELLOW,
			dy_line_color = RED,
			secant_line_length = 6,
			secant_line_color = YELLOW_B)

		self.play(Create(ejes), Create(funcion))
		self.wait(2)

		self.play(Create(secante), run_time = 2)
		self.wait(2)


class derivada2(Scene):
	def construct(self):

		ejes = Axes(x_range = [-3, 3, 1],
			        y_range = [-1, 8, 2],
			        x_length = 10,
			        y_length = 7).add_coordinates()

		funcion = ejes.plot(lambda x: x**2, x_range = [-3, 3], color = BLUE)

		x = ValueTracker(1)
		dx = ValueTracker(1)

		##animacion para la secante en tangente (always_redraw())

		derivada = always_redraw(
			lambda: ejes.get_secant_slope_group(
				x = x.get_value(),
				dx = _value(),dx.get
				graph = funcion,
				dx_label = "dx",
				dy_label = "dy",
				dx_line_color = YELLOW,
				dy_line_color = RED,
				secant_line_length = 6,
				secant_line_color = YELLOW_B))

		self.play(Create(ejes), Create(funcion), run_time = 2)
		self.wait(2)

		self.play(Create(derivada), run_time = 2)
		self.wait(2)

		##animar de secante a derivada

		self.play(dx.animate.set_value(0.01), run_time = 6)
		self.wait(2)

		#mover la tangente

		self.play(x.animate.set_value(-2), run_time = 4)
		self.wait(2)
		self.play(x.animate.set_value(2), run_time = 4)
		self.wait(2)
