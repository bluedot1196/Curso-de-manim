from manim import *

class esfera(ThreeDScene):
	def construct(self):

		self.set_camera_orientation(phi = 60*DEGREES, theta = 30*DEGREES)

		ejes = ThreeDAxes(x_range = [-6, 6, 1],
			              y_range = [-6, 6, 1],
			              z_range = [-4, 4, 1],
			              x_length = 10,
			              y_length = 10,
			              z_length = 7).add_coordinates()

		esfera = Sphere(
			center = (0, 0 ,0), 
			radius = 1,
			resolution = (20, 20))

		esfera.set_color(RED)


		esfera2 = Sphere(
			center = (3, 3 ,3),
			radius = 0.6,
			resolution = (50, 50))

		esfera2.set_color(YELLOW)

		self.play(Create(ejes), run_time = 2)
		self.wait()
		self.play(Create(esfera), Write(esfera2), run_time = 2)
		self.wait(2)
		self.move_camera(theta = 200*DEGREES, run_time = 6)
		self.wait(2)
