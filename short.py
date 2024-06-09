tmp_pixel_height = config.pixel_height
config.pixel_height = config.pixel_width
config.pixel_width = tmp_pixel_height

config.frame_height = config.frame_height / SCALE_FACTOR
config.frame_width = config.frame_height * 9 / 16
FRAME_HEIGHT = config.frame_height
FRAME_WIDTH = config.frame_width


class t1(Scene):
	def setup(self, add_border = False):
		if add_border:
			self.border = Rectangle(
				width = FRAME_WIDTH,
				height = FRAME_HEIGHT,
				color = RED
			)
			self.add(self.border)

	def construct(self):



##Ejemplo de animacion

class t2(Scene):
	def setup(self, add_border = False):
		if add_border:
			self.border = Rectangle(
				width = FRAME_WIDTH,
				height = FRAME_HEIGHT,
				color = RED
			)
			self.add(self.border)

	def construct(self):

		titulo = Tex("Función cuadrática").scale(0.7).to_edge(UP).set_color(YELLOW_B)

		fx = MathTex("f(x) = x^2").scale(0.6).next_to(titulo, DOWN, buff = 0.8)

		ejes = Axes(x_range = [-4, 4, 1],
			        y_range = [-4, 4, 1],
			        x_length = 6,
			        y_length = 6,
			        tips = False).set_color(BLUE).add_coordinates().scale(0.6)
		ejes.shift(0.5*DOWN)

		etiquetas = ejes.get_axis_labels(MathTex("x").scale(0.6), MathTex("y").scale(0.6))

		funcion = ejes.plot(lambda x: x**2, x_range = [-2, 2], color = YELLOW)



		self.play(Write(titulo))
		self.wait()
		self.play(Write(fx))
		self.wait()
		self.play(Create(ejes), Write(etiquetas))
		self.wait(2)
		self.play(Create(funcion), run_time = 2)
		self.wait(2)
