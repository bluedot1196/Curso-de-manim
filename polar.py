from manim import *


class polar(Scene):
	def construct(self):

		plano_polar = PolarPlane(
			          radius_max = 5, 
			          azimuth_units = "PI radians",
			          size = 6).add_coordinates()


		plano = NumberPlane()
		self.play(Create(plano))

		##Pi radians, degrees, gradians

		self.play(Create(plano_polar), run_time = 2)
		self.wait(2)



class polar2(Scene):
	def construct(self):

		plano = PolarPlane(radius_max = 5,
			               azimuth_units = "PI radians",
			               size = 6).add_coordinates()
		plano.to_edge(RIGHT)

		texto = Tex("Curva Polar").shift(3*LEFT)

		polar = plano.plot_polar_graph(lambda theta: 4*np.sin(2*theta), 
			                           theta_range = [0, 2*PI], 
			                           color = RED)

		self.play(Create(plano), Write(texto))
		self.wait(2)
		self.play(Create(polar), run_time = 4)
		self.wait(2)


class polar3(Scene):
	def construct(self):

		plano = PolarPlane(radius_max = 3,
			               azimuth_units = "PI radians",
			               size = 6).add_coordinates()

		polar = plano.plot_polar_graph(lambda theta: 1 + np.cos(theta), 
			                           theta_range = [0, 2*PI], 
			                           color = RED)

		self.play(Create(plano))
		self.wait(2)
		self.play(Create(polar), run_time = 4)
		self.wait(2)
