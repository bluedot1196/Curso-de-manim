class t4(ThreeDScene):
	def construct(self):

		ejes = ThreeDAxes(x_range = [-6, 6, 1],
			              y_range = [-6, 6, 1],
			              z_range = [-4, 4, 1],
			              x_length = 10,
			              y_length = 10,
			              z_length = 7).add_coordinates()

		etiquetas = ejes.get_axis_labels(
			MathTex("x"), MathTex("y"), MathTex("z"))

		linea = Line3D(start = ejes.c2p(0,0,0), end = ejes.c2p(3, 2, 2), color = YELLOW)

		self.set_camera_orientation(phi = 80*DEGREES, theta = -30*DEGREES)

		self.play(Create(ejes), Write(etiquetas), run_time = 2)
		self.wait()
		self.play(Create(linea), run_time = 2)
		self.wait(2)
