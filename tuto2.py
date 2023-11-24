class camara(ThreeDScene):
	def construct(self):

		ejes = ThreeDAxes(x_range = [-4, 4, 1],
			              y_range = [-4, 4, 1],
			              z_range = [-4, 4, 1],
			              x_length = 7,
			              y_length = 7,
			              z_length = 7).add_coordinates()
		etiquetas = ejes.get_axis_labels(
			MathTex("x"), MathTex("y"), MathTex("z"))

		self.play(Create(ejes), Write(etiquetas), run_time = 2)
		self.wait(2)
		self.move_camera(phi = 50*DEGREES, run_time = 10)
		self.wait(2)
		self.move_camera(theta = 360*DEGREES, run_time = 10)
		self.wait(2)
