from manim import*

class cubo(ThreeDScene):
	def construct(self):

		self.set_camera_orientation(phi = 60*DEGREES, theta = 50*DEGREES)

		ejes = ThreeDAxes()

		cubo = Cube(side_length = 2, fill_opacity = 0.8, fill_color = RED)

		self.play(Create(ejes))
		self.wait()
		self.play(Create(cubo))
		self.wait(2)
