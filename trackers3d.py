from manim import*


class elipsoide(ThreeDScene):
	def construct(self):

		## x = a.cos(u)cos(v)
		## y = b.sen(u)cos(v)
		## z = c.sen(v)
		##np.array([x, y, z])
		##Sphere(radius = 2, color = , ....)


		ejes = ThreeDAxes(x_range = [-6, 6, 1],
			              y_range = [-6, 6, 1],
			              z_range = [-6, 6, 1],
			              x_length = 7,
			              y_length = 7,
			              z_length = 7).add_coordinates()

		a = ValueTracker(1)
		b = ValueTracker(1)
		c = ValueTracker(1)

		elipsoide = always_redraw(
			lambda: Surface(lambda u, v: ejes.c2p(*np.array([a.get_value()*np.cos(u)*np.cos(v), 
				            b.get_value()*np.sin(u)*np.cos(v), 
				            c.get_value()*np.sin(v)])),
				            u_range = [0, PI],
				            v_range = [0, 2*PI]))


		self.set_camera_orientation(phi = 65*DEGREES, theta = 60*DEGREES)
		self.play(Create(ejes), run_time = 2)
		self.wait(2)

		self.play(Create(elipsoide), run_time = 2)
		self.wait(2)
		self.play(a.animate.set_value(5), rate_func = there_and_back, run_time = 8) 
		self.wait(2)
		self.play(b.animate.set_value(5), rate_func = there_and_back, run_time = 8) 
		self.wait(2)
		self.play(c.animate.set_value(5), rate_func = there_and_back, run_time = 8) 
		self.wait(2)
