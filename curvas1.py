from manim import*

##Grafica de funciones de 2 variables: z = f(x,y)

### z = x^2 + y^2
## f(x, y) = x^2 + y^2
##     z = x^2 + y^2

class paraboloide(ThreeDScene):
	def construct(self):

		ejes = ThreeDAxes(x_range = [-4, 4, 1],
			              y_range = [-4, 4, 1],
			              z_range = [-3, 6, 1],
			              y_length = 9,
			              x_length = 9,
			              z_length = 9).add_coordinates()

		etiqueta = MathTex("f(x,y) = x^2 + y^2").to_corner(UL)

		#Surface(lambda u, v: ejes.c2p(*np.array(x, y, z])),  )

		paraboloide = Surface(
			lambda u, v: ejes.c2p(*np.array([u, v, u**2 + v**2])),
			u_range = [-3, 3],
			v_range = [-3, 3],
			fill_opacity = 0.9)

		self.set_camera_orientation(phi = 65*DEGREES, theta = -30*DEGREES)
		self.add_fixed_in_frame_mobjects(etiqueta)
		self.play(Create(ejes), run_time = 2)
		self.wait(2)
		self.play(Write(paraboloide), run_time = 3)
		self.wait(4)




class planos(ThreeDScene):
	def construct(self):

		ejes = ThreeDAxes(x_range = [-4, 4, 1],
			              y_range = [-4, 4, 1],
			              z_range = [-3, 6, 1],
			              y_length = 9,
			              x_length = 9,
			              z_length = 9).add_coordinates()

		#Plano XY: z = 0
		#(x, y, z) = (x, y, 0)

		plano_xy = Surface(
			lambda u, v: ejes.c2p(*np.array([u, v, 0])),
			u_range = [-5, 5],
			v_range = [-5, 5],
			checkerboard_colors = [RED, YELLOW],
			fill_opacity = 0.5)

		#Plano XZ: y = 0

		plano_xz = Surface(
			lambda u, v: ejes.c2p(*np.array([u, 0, v])),
			u_range = [-5, 5],
			v_range = [-5, 5],
			checkerboard_colors = [YELLOW, BLUE],
			fill_opacity = 0.5)

		#Plano YZ: x = 0

		plano_yz = Surface(
			lambda u, v: ejes.c2p(*np.array([0, u, v])),
			u_range = [-5, 5],
			v_range = [-5, 5],
			fill_color = ORANGE,
			checkerboard_colors = [TEAL_E, RED],
			fill_opacity = 0.8)

		self.set_camera_orientation(phi = 65*DEGREES, theta = -30*DEGREES)
		self.play(Create(ejes), run_time = 2)
		self.wait(2)
		self.play(Create(plano_xy), run_time = 3)
		self.wait(2)
		self.play(ReplacementTransform(plano_xy, plano_xz), run_time = 2)
		self.wait(2)
		self.play(ReplacementTransform(plano_xz, plano_yz), run_time = 2)
		self.wait(2)

		### z = 2x + 7y

		## (x, y, z) = (u, v, 2*u + 7*v)



class t1(ThreeDScene):
	def construct(self):

		ejes = ThreeDAxes().add_coordinates()

		x = MathTex("x").move_to(np.array([5, 0.5, 0]))
		y = MathTex("y").move_to(np.array([0.5, 5, 0]))
		text3d = MathTex("z = (x^2 + 3y^2)e^{1 - x^2 - y^2}").to_corner(UL)

		self.set_camera_orientation(phi = 65*DEGREES, theta = 60*DEGREES)
		self.play(Create(ejes), Write(x), Write(y), run_time = 2)
		self.wait(2)

		self.add_fixed_in_frame_mobjects(text3d)
		self.wait(2)

		curva = Surface(lambda u, v: np.array([u, v, (u**2 + 3*v**2)*np.exp(1 - u**2 - v**2)]),
			            u_range = [-3, 3],
			            v_range = [-3, 3],
			            checkerboard_colors = [RED_D, RED_E],
			            resolution = (15, 32))

		self.play(Write(curva))
		self.wait(2)
		self.move_camera(phi = 90*DEGREES)
		self.wait(2)
		self.begin_ambient_camera_rotation(rate=0.50)
		self.wait(8)
