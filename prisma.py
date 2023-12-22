from manim import*

class prisma(ThreeDScene):
	def construct(self):

		ejes = ThreeDAxes()
		etiquetas = ejes.get_axis_labels(
			MathTex("x"), MathTex("y"), MathTex("z"))

		self.set_camera_orientation(phi = 60*DEGREES, theta = 50*DEGREES)

		prisma = Prism(dimensions = [1, 2, 3])
		prisma.move_to([0,0,0])

		prisma2 = Prism(dimensions = [2, 3, 1])
		prisma2.move_to([2,2,2]).set_color(RED)

		self.play(Create(ejes), Write(etiquetas))
		self.wait()
		self.play(Create(prisma))
		self.wait()
		self.play(Create(prisma2))
		self.wait(2)
