from manim import*

class t1(Scene):
	def construct(self):

		eje = PolarPlane().scale(0.8).add_coordinates().to_edge(LEFT)

		#trackers

		a = ValueTracker(4)
		n = ValueTracker(2)

		## r = acos(n*theta)


		curva_polar = always_redraw(
			lambda: eje.plot_polar_graph(lambda theta: a.get_value()*np.cos(n.get_value()*theta), [0, 2*PI], color = YELLOW))

		etiqueta = always_redraw(
			lambda: MathTex(f"{a.get_value():.2f}\\cos({n.get_value():.2f}\\theta)").shift(3*RIGHT))

		self.add(eje, curva_polar, etiqueta)
		self.wait(0.2)
		self.play(n.animate.set_value(10), rate_func = there_and_back, run_time = 10)
		self.wait()
		self.play(a.animate.set_value(2), rate_func = there_and_back, run_time = 4)
		self.wait(2)
