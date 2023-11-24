class t3(ThreeDScene):
	def construct(self):

		ejes = ThreeDAxes(x_range = [-6, 6, 1],
			              y_range = [-6, 6, 1],
			              z_range = [-4, 4, 1],
			              x_length = 10,
			              y_length = 10,
			              z_length = 7).add_coordinates()

		etiquetas = ejes.get_axis_labels(
			MathTex("x"), MathTex("y"), MathTex("z"))

		self.set_camera_orientation(phi = 60*DEGREES, theta = 30*DEGREES)

		punto = Dot3D(point = ejes.c2p(2, 2, 3), radius = 0.1, color = BLUE)

		self.play(Create(ejes), Write(etiquetas), run_time = 2)
		self.wait(2)
		self.play(Create(punto))
		self.wait(2)
		self.move_camera(theta = 200*DEGREES, run_time = 6)
		self.wait(2)
