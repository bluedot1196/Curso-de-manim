from manim import*


class triangulo(Scene):
	def construct(self):


		ejes = NumberPlane().add_coordinates()

		cateto1 = Line([-2, -2, 0], [2, -2, 0]).set_color(YELLOW)
		cateto2 = Line([2, -2, 0], [2, 3, 0]).set_color(YELLOW)
		hipotenusa = Line([-2, -2, 0], [2, 3, 0]).set_color(YELLOW)

		angulo1 = Angle(cateto1, hipotenusa, quadrant = (1, 1))
		angulo2 = Angle(hipotenusa, cateto2, quadrant = (-1, -1))
		recto = RightAngle(cateto1, cateto2, quadrant = (-1, 1))

		self.add(ejes)

		self.play(Create(cateto1), Create(cateto2), Create(hipotenusa))
		self.wait(2)
		self.play(GrowFromCenter(angulo1), GrowFromCenter(angulo2))
		self.wait(2)
		self.play(GrowFromCenter(recto))
		self.wait(2)
