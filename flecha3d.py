from manim import*

class flecha(ThreeDScene):
	def construct(self):

		ejes = ThreeDAxes(x_range = [-6, 6, 1],
			              y_range = [-6, 6, 1],
			              z_range = [-4, 4, 1],
			              x_length = 10,
			              y_length = 10,
			              z_length = 7).add_coordinates()

		flecha = Arrow3D(
			start = ejes.c2p(0, 0, 0),
			end = ejes.c2p(3, 3, 3))
		flecha.set_color(YELLOW)

		self.set_camera_orientation(phi = 75*DEGREES, theta = 25*DEGREES)

		self.play(Create(ejes))
		self.wait()
		self.play(Create(flecha))
		self.wait(2)
