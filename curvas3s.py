from manim import*

class ejm1(ThreeDScene):
    def construct(self):

    	### (x, y, z) = (1.2cost, 1.2sent, 0.05t)
    	###np.array([x, y, z])


        curve1 = ParametricFunction(
            lambda t: np.array([1.2 * np.cos(t), 1.2 * np.sin(t), t * 0.05]), 
            color=RED, t_range = [-6*PI, 5*PI])
        
        axes = ThreeDAxes()
        self.add(axes, curve1)
        self.set_camera_orientation(phi=80 * DEGREES, theta=-60 * DEGREES)
        self.wait()





class curvas(ThreeDScene):
	def construct(self):

		ejes = ThreeDAxes(x_range = [-4, 4, 1],
			              y_range = [-4, 4, 1],
			              z_range = [-20, 20, 5],
			              y_length = 9,
			              x_length = 9,
			              z_length = 9).add_coordinates()

		#Curva x = cost, y = sent, z = t

		curva = ejes.plot_parametric_curve(
			lambda t: np.array([np.cos(t), np.sin(t), t]),
			color = YELLOW,
			t_range = [-6*PI, 6*PI])

		self.set_camera_orientation(phi = 65*DEGREES, theta = -30*DEGREES)
		self.play(Create(ejes), run_time = 2)
		self.wait(2)
		self.play(Create(curva), run_time = 4)
		self.wait(2)


class curvas2(ThreeDScene):
	def construct(self):

		ejes = ThreeDAxes(x_range = [-6, 6, 1],
			              y_range = [-6, 6, 1],
			              z_range = [-6, 6, 1],
			              y_length = 9,
			              x_length = 9,
			              z_length = 9).add_coordinates()

		#curva: x = (4 + sen20t)cost; y = (4 + sen20t)sent; z = cos20t

		curva = ejes.plot_parametric_curve(
			lambda t: np.array([(4 + np.sin(20*t))*np.cos(t), (4 + np.sin(20*t))*np.sin(t), np.cos(20*t)]),
			color = YELLOW,
			t_range = [-6*PI, 6*PI])

		self.set_camera_orientation(phi = 55*DEGREES, theta = -30*DEGREES)
		self.play(Create(ejes), run_time = 2)
		self.wait(2)
		self.play(Create(curva), run_time = 4)
		self.wait(2)
