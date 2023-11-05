from manim import*

class implicit(Scene):
	def construct(self):

		plano = NumberPlane()

		grafica = ImplicitFunction(
			lambda x, y: x**2 + y**2 - 4,
			color = YELLOW)

		self.play(Create(plano), run_time = 2)
		self.wait(2)
		self.play(Create(grafica), run_time = 2)
		self.wait(2)


class implicit2(Scene):
	def construct(self):

		plano = NumberPlane()

		grafica = ImplicitFunction(
			lambda x, y: x * y ** 2 - x ** 2 * y - 2,
			color = YELLOW)

		self.play(Create(plano), run_time = 2)
		self.wait(2)
		self.play(Create(grafica), run_time = 2)
		self.wait(2)



class implicit3(Scene):
	def construct(self):

		plano = NumberPlane()

		## f(x, y) = sen(x^2 + y^2)

		grafica = ImplicitFunction(
			lambda x, y: np.sin(x**2 + y**2),
			color = YELLOW)

		self.play(Create(plano), run_time = 2)
		self.wait(2)
		self.play(Create(grafica), run_time = 2)
		self.wait(2)
