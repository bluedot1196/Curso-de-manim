from manim import*

##Configuración para videos en formato vertical


SCALE_FACTOR = 1

tmp_pixel_height = config.pixel_height
config.pixel_height = config.pixel_width
config.pixel_width = tmp_pixel_height

config.frame_height = config.frame_height / SCALE_FACTOR
config.frame_width = config.frame_height * 9 / 16
FRAME_HEIGHT = config.frame_height
FRAME_WIDTH = config.frame_width


class t1(Scene):
	def setup(self, add_border = True):
		if add_border:
			self.border = Rectangle(
				width = FRAME_WIDTH,
				height = FRAME_HEIGHT,
				color = RED
			)
			self.add(self.border)

	def construct(self):

		#Eje para la circunferencia unitaria

		ejes = Axes(x_range = [-1.5, 1.5, 1],
			        y_range = [-1.5, 1.5, 1],
			        x_length = 2,
			        y_length = 2,
			        tips= False).set_color(BLUE).scale(0.7).to_corner(UL).shift(1.4*DOWN + 0.25*LEFT)

		#Eje para la gráfica de la función seno

		ejes2 = Axes(x_range = [0, 2*PI, PI/2],
			         y_range = [-1.5, 1.5, 1],
			         x_length = 3,
			         y_length = 2,
			         tips = False).set_color(BLUE).scale(0.7).next_to(ejes, RIGHT, buff = 0.2)

		#Eje para la gráfica de la función coseno

		ejes3 = Axes(x_range = [0, 2*PI, PI/2],
			         y_range = [-1.5, 1.5, 1],
			         x_length = 3,
			         y_length = 2,
			         tips = False).set_color(BLUE).scale(0.7).next_to(ejes, DOWN, buff = 1).rotate(-90*DEGREES)


		#Etiquetas para el eje2

		y1 = MathTex("1").scale(0.4).next_to(ejes2.c2p(0,1), LEFT, buff = 0.15)
		y2 = MathTex("-1").scale(0.4).next_to(ejes2.c2p(0,-1), LEFT, buff = 0.15)
		x1 = MathTex("\\frac{\\pi}{2}").scale(0.4).next_to(ejes2.c2p(PI/2,0), DOWN, buff = 0.15)
		x2 = MathTex("\\pi}").scale(0.4).next_to(ejes2.c2p(PI,0), DOWN, buff = 0.15)
		x3 = MathTex("\\frac{3\\pi}{2}}").scale(0.4).next_to(ejes2.c2p(3*PI/2,0), DOWN, buff = 0.15)
		x4 = MathTex("2\\pi}").scale(0.4).next_to(ejes2.c2p(2*PI,0), DOWN, buff = 0.15)

		etiquetas = VGroup(x1, x2, x3, x4, y1, y2)


		#Etiquetas para el eje3

		y1a = MathTex("1").scale(0.4).next_to(ejes3.c2p(0,1), UP, buff = 0.15).rotate(-90*DEGREES)
		y2a = MathTex("-1").scale(0.4).next_to(ejes3.c2p(0,-1), UP, buff = 0.15).rotate(-90*DEGREES)
		x1a = MathTex("\\frac{\\pi}{2}").scale(0.4).rotate(-90*DEGREES).next_to(ejes3.c2p(PI/2,0), LEFT, buff = 0.15)
		x2a = MathTex("\\pi}").scale(0.4).rotate(-90*DEGREES).next_to(ejes3.c2p(PI,0), LEFT, buff = 0.15)
		x3a = MathTex("\\frac{3\\pi}{2}}").scale(0.4).rotate(-90*DEGREES).next_to(ejes3.c2p(3*PI/2,0), LEFT, buff = 0.15)
		x4a = MathTex("2\\pi}").scale(0.4).rotate(-90*DEGREES).next_to(ejes3.c2p(2*PI,0), LEFT, buff = 0.15)

		etiquetas2 = VGroup(x1a, x2a, x3a, x4a, y1a, y2a)


		#Etiquetas de los ejes de ambos ejes

		theta1 = MathTex("\\theta").scale(0.4).next_to(ejes2.c2p(2*PI,0), UP, buff = 0.05).shift(0.1*RIGHT)
		f_theta1 = MathTex("sen\\theta").scale(0.4).next_to(ejes2.c2p(0, 1.5), UP, buff = 0.05)

		theta2 = MathTex("\\theta").scale(0.4).next_to(ejes3.c2p(2*PI,0), RIGHT, buff = 0.05).shift(0.1*DOWN).rotate(-90*DEGREES)
		f_theta2 = MathTex("cos\\theta").scale(0.4).next_to(ejes3.c2p(0,1.5), RIGHT, buff = 0.05)


		#Dibujar la circunferencia unitaria

		circulo = ejes.plot_parametric_curve(lambda t: np.array([np.cos(t), np.sin(t), 0]),
			                                 t_range = [0, 2*PI],
			                                 color = RED).set_stroke(color = RED, width = 2)

		#Añadimos lo trackers

		t = ValueTracker(0)

		punto = always_redraw(
			lambda: Dot(ejes.c2p(np.cos(t.get_value()), np.sin(t.get_value()))).scale(0.6).set_color(YELLOW))

		seno = always_redraw(
			lambda: ejes2.plot(lambda x: np.sin(x), x_range = [0, t.get_value()], color = YELLOW).set_stroke(width = 2))

		coseno = always_redraw(
			lambda: ejes3.plot(lambda x: np.cos(x), x_range = [0, t.get_value()], color = YELLOW).set_stroke(width = 2))

		f_sen = ejes2.plot(lambda x: np.sin(x), x_range = [0, 2*PI])

		f_cos = ejes3.plot(lambda x: np.cos(x), x_range = [0, 2*PI])

		linea = always_redraw(
			lambda: DashedLine(ejes.c2p(np.cos(t.get_value()), np.sin(t.get_value())), ejes2.c2p(t.get_value(),f_sen.underlying_function(t.get_value()))).set_stroke(width = 2).set_color(YELLOW_B))

		linea2 = always_redraw(
			lambda: DashedLine(ejes.c2p(np.cos(t.get_value()), np.sin(t.get_value())), ejes3.c2p(t.get_value(),f_cos.underlying_function(t.get_value()))).set_stroke(width = 2).set_color(YELLOW_B))

		radio = always_redraw(
			lambda: Line(ejes.c2p(0,0), ejes.c2p(np.cos(t.get_value()),np.sin(t.get_value()))).set_stroke(width = 2).set_color(BLUE))


		self.add(ejes, ejes2, etiquetas, etiquetas2, circulo, punto, seno, coseno, linea, linea2, radio, ejes3,
			     theta1, f_theta1, theta2, f_theta2)
		self.wait(0.4)
		self.play(t.animate.set_value(2*PI), rate_func = linear, run_time = 8)
