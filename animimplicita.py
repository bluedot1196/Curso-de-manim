from manim import*

class t2(Scene):
	def construct(self):

		ejes = Axes(x_range = [-10, 10, 2],
			        y_range = [-10, 10, 2]).shift(DOWN)

		a = ValueTracker(-5)

		# f(x, y) = 0
		# y = sen(ax) + asen(x)
		# y - sen(ax) - asen(x) = 0

		curva = always_redraw(
			lambda: ejes.plot_implicit_curve(lambda x, y: y - np.sin(a.get_value()*x) - a.get_value()*np.sin(x), color = YELLOW))

		etiqueta = MathTex("y = sen(ax) + asen(x)").scale(0.8).to_edge(UP)
		etiqueta2 = MathTex("a", "=").scale(0.8).next_to(etiqueta, DOWN, buff = 0.4).shift(0.4*LEFT)

		a_etiqueta = always_redraw(
			lambda: DecimalNumber(a.get_value()).scale(0.8).next_to(etiqueta2[1], RIGHT, buff = 0.2))

		self.add(ejes, curva, etiqueta, etiqueta2, a_etiqueta)
		self.wait(0.4)
		self.play(a.animate.set_value(18), run_time = 10)
		self.wait(2)
