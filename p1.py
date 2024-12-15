from manim import *

class t1(Scene):
	def construct(self):

		ejes = Axes(x_range = [-3, 5, 1],
			        y_range = [-4, 4, 1],
			        x_length = 13,
			        y_length = 7).add_coordinates()

		f1 = ejes.plot(lambda x: -0.4*x**3 + x**2 + x + 1.4, x_range = [-2,3], color = BLUE)

		f2 = ejes.plot(lambda x: -0.1*x**4 + 1.1*x**2 - 0.1*x - 0.1, x_range = [-2, 3], color = YELLOW)


		x = ValueTracker(-1.5)

		linea = always_redraw(
			lambda: DashedLine(ejes.c2p(x.get_value(), f2.underlying_function(x.get_value())), ejes.c2p(x.get_value(), f1.underlying_function(x.get_value()))).set_color(RED))

		distancia = always_redraw(
			lambda: DecimalNumber(f1.underlying_function(x.get_value()) - f2.underlying_function(x.get_value()), num_decimal_places = 3).scale(0.7).next_to(linea.get_center(), RIGHT, buff = 0.15))

		self.play(Create(ejes))
		self.wait()
		self.play(Create(f1))
		self.wait()
		self.play(Create(f2))
		self.wait()

		self.play(Create(linea), Write(distancia))
		self.wait(2)

		self.play(x.animate.set_value(3), run_time = 10)
		self.wait(2)
