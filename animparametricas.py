from manim import*

class t3(Scene):
	def construct(self):


		# (x, y) = (acos(t), bsen(t))

		#Elipse: x = acos(t)
		#        y = bsen(t)

		ejes = Axes(x_range = [-4, 4, 1],
			        y_range = [-4, 4, 1],
			        x_length = 6,
			        y_length = 6).set_color(BLUE).add_coordinates().to_edge(LEFT)

		#Trackers

		a = ValueTracker(1)
		b = ValueTracker(1)

		## (x, y, 0)


		elipse = always_redraw(
			lambda: ejes.plot_parametric_curve(lambda t: np.array([a.get_value()*np.cos(t), b.get_value()*np.sin(t), 0]), t_range = [0, 2*PI], color = YELLOW))
		
		x = always_redraw(
			lambda: MathTex(f"x = {a.get_value():.2f}\\cos\\theta").shift(3*RIGHT + 1*UP))

		y = always_redraw(
			lambda: MathTex(f"y = {b.get_value():.2f}\\sin\\theta").shift(3*RIGHT + 0.5*DOWN))

		self.add(ejes, elipse, x, y)
		self.wait(0.5)
		self.play(a.animate.set_value(4), run_time = 4)
		self.wait()
		self.play(b.animate.set_value(4), run_time = 4)
		self.wait()
