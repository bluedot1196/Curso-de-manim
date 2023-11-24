from manim import*

class t1(ThreeDScene):
	def construct(self):

		ejes = ThreeDAxes().add_coordinates()

		self.play(Create(ejes), run_time = 2)
		self.wait(5)






class t2(ThreeDScene):
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
		self.move_camera(phi = 45*DEGREES, run_time = 4)
		self.wait(2)
		self.move_camera(theta = 45*DEGREES, run_time = 4)
		self.wait(2)
