from manim import*

##SUPERFICIES PARAMETRICAS

class p1(ThreeDScene):
	def construct(self):

		## x = r.cos(u)sen(v)
		## y = r.sen(u).sen(v)
		## z = r.cos(v)
		##np.array([x, y, z])
		##Sphere(radius = 2, color = , ....)

		r = 2

		curva = Surface(lambda u, v: np.array([r*np.cos(u)*np.sin(v), r*np.sin(u)*np.sin(v), r*np.cos(v)]),
			            u_range = [0, 2*PI],
			            v_range = [0, PI],
			            checkerboard_colors = [RED_D, RED_E],
			            resolution = (15, 32))

		self.set_camera_orientation(phi = 65*DEGREES, theta = 60*DEGREES)

		self.play(Create(curva), run_time = 2)
		self.wait(5)






class p2(ThreeDScene):
	def construct(self):

		## x = r.cos(u)sen(v)
		## y = r.sen(u).sen(v)
		## z = r.cos(v)

		ejes = ThreeDAxes(x_range = [-4, 4, 1],
			              y_range = [-4, 4, 1],
			              z_range = [-3, 6, 1],
			              y_length = 9,
			              x_length = 9,
			              z_length = 9).add_coordinates()

		r = 2

		##np.array([x, y, z])
		## ejes.c2p(*np.array([x, y, z]))

		curva = Surface(
			lambda u, v: ejes.c2p(*np.array([r*np.cos(u)*np.sin(v), r*np.sin(u)*np.sin(v), r*np.cos(v)])),
			u_range = [0, 2*PI],
			v_range = [0, PI],
			fill_opacity = 0.5)

		self.set_camera_orientation(phi = 65*DEGREES, theta = 60*DEGREES)

		self.play(Create(curva), run_time = 2)
		self.wait(5)



class p3(ThreeDScene):
	def construct(self):

		## x = cos(u).(1-v)
		## y = sen(u).(1+v)
		## z = v

		curva = Surface(lambda u, v: np.array([np.cos(u)*(1-v), np.sin(u)*(1+v), v]),
			            u_range = [-PI, PI],
			            v_range = [-1, 1],
			            checkerboard_colors = [RED_D, RED_E],
			            resolution = (15, 32))

		self.set_camera_orientation(phi = 45*DEGREES, theta = 10*DEGREES)

		self.play(Create(curva), run_time = 2)
		self.wait(2)
		self.move_camera(theta = 200*DEGREES, run_time = 10)
		self.wait(2)
