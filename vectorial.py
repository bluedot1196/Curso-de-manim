from manim import*


class helice(ThreeDScene):
	def construct(self):

		ejes = ThreeDAxes(x_range = [-3, 3, 1],
			              y_range = [-3, 3, 1],
			              z_range = [-3, 3, 1],
			              x_length = 7,
			              y_length = 7,
			              z_length = 7,
			              tips = False).set_color(BLUE).add_coordinates()

		fijo = MathTex("\\vec{r}(t) = \\langle cost, sent, 0.2t  \\rangle").to_corner(UL)

		t = ValueTracker(-4*PI)

		a = 0.2

		vector = always_redraw(
			lambda: Arrow3D(ejes.c2p(0, 0, 0), ejes.c2p(np.cos(t.get_value()), np.sin(t.get_value()), a*t.get_value())).set_color(RED))

		punto3d = always_redraw(
			lambda: Dot3D().set_color(ORANGE).move_to(ejes.c2p(np.cos(t.get_value()), np.sin(t.get_value()), a*t.get_value())))

		trayectoria = always_redraw(
			lambda: ejes.plot_parametric_curve(lambda t: np.array([np.cos(t), np.sin(t), a*t]),
				         t_range = [-4*PI, t.get_value()],
				         color = YELLOW))

		curva = ejes.plot_parametric_curve(lambda t: np.array([np.cos(t), np.sin(t), a*t]),
			         t_range = [-4*PI, 4*PI],
			         color = YELLOW)

		self.set_camera_orientation(phi = 65*DEGREES, theta = -30*DEGREES)
		self.add_fixed_in_frame_mobjects(fijo)

		self.play(Create(ejes), run_time = 2)
		self.wait(2)
		
		self.play(Create(vector), GrowFromCenter(punto3d),
			      Create(trayectoria), run_time = 2)
		self.wait(2)
		self.play(t.animate.set_value(4*PI), run_time = 10)
		self.play(Create(curva))
		self.wait(2)
