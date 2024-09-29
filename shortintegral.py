from manim import*

class integral(Scene):
	def setup(self, add_border = False):
		if add_border:
			self.border = Rectangle(
				width = FRAME_WIDTH,
				height = FRAME_HEIGHT,
				color = RED
			)
			self.add(self.border)

	def construct(self):

		ejes = Axes(x_range = [-0.5, 4, 0.5],
			        y_range = [-1, 7, 1],
			        x_length = 7,
			        y_length = 4).set_color(BLUE).scale(0.6).shift(0.76*DOWN)

		labels = ejes.get_axis_labels(MathTex("x").scale(0.6), MathTex("f(x)").scale(0.6))

		f = ejes.plot(lambda x: 2*(x-1)**2 - (x-1)**3 + 3, x_range = [-1, 4], color = TEAL_E)

		titulo = Tex("¿Qué es la integral definida?").scale(0.7).set_color(YELLOW_B).to_edge(UP)

		self.play(Create(ejes), Write(labels), Write(titulo), run_time = 2)
		self.wait(2)
		self.play(Create(f), run_time = 2)
		self.wait(2)

		##Marcador movible

		sweeper = Triangle().scale(0.15).move_to(ejes.c2p(0.5, 0)).scale(0.5)
		sweeper.shift(0.15*DOWN).scale(0.5)
		#sweeper.shift((sweeper.get_top()[1] - sweeper.get_center()[1])*DOWN)

		l_pivot = sweeper.copy()
		r_pivot = sweeper.copy().shift(2.5*ejes.get_x_unit_size()*RIGHT)

		a = MathTex("a").scale(0.6).next_to(ejes.c2p(0.5, 0), DOWN, buff = 0.26)
		b = MathTex("b").scale(0.6).next_to(ejes.c2p(3, 0), DOWN, buff = 0.26)

		##Trackers

		t = ValueTracker(0.5)

		area = always_redraw(
			lambda: ejes.get_area(
				f,
				x_range = [0.5, t.get_value()],
				color = ["#d40b37","#d4b90b"],
				opacity = 0.8))

		self.play(Create(sweeper), Create(l_pivot), 
			      FadeIn(area), run_time = 2)
		self.wait(2)
		self.play(Write(a), run_time = 1)
		self.wait(2)

		self.play(sweeper.animate.move_to(r_pivot), 
			      t.animate.set_value(3), rate_fun = smooth, 
			      run_time = 3)
		self.play(Write(b), run_time = 1)
		self.wait(2)

		##Pregunta para hallar el área

		busco_area = Tex("Area\\ ", "= ?").scale(0.6).move_to(area.get_center())
		self.play(GrowFromCenter(busco_area), run_time = 2)
		self.wait(2)
		self.play(FadeOut(busco_area))
		self.wait(2)

		##Rectangulos de Riemann

		dx = ValueTracker(0.5)

		dx_label = MathTex("\\triangle x", "=").scale(0.5).to_edge(UP).shift(1.9*DOWN).shift(1.2*LEFT)

		dx_decimal = always_redraw(
			lambda: DecimalNumber(dx.get_value(), num_decimal_places = 4).scale(0.5).next_to(dx_label[1], RIGHT, buff = 0.2))

		n_lab = MathTex("n", "=").scale(0.5).next_to(dx_decimal, RIGHT, buff = 0.6)
		n_decimal = always_redraw(
			lambda: DecimalNumber(2.5/dx.get_value(), num_decimal_places = 0).scale(0.5).next_to(n_lab[1], RIGHT, buff = 0.2))


		riemann_rectangles = always_redraw(
			lambda: ejes.get_riemann_rectangles(
				graph = f,
				x_range = [0.5, 3],
				dx = dx.get_value(),
				color = ["#d40b37","#d4b90b"],
				fill_opacity = 0.9,
				stroke_width = 0.1,
				stroke_color = "#aa9f4b",
				input_sample_type = "right"))

		##Lineas division

		lineas_divisoras = VGroup()  ##Grupo donde se guardara las lineas

		for i in np.arange(1, 3.5, dx.get_value()):
			linea = Line(ejes.c2p(i, 0), ejes.c2p(i, f.underlying_function(i)))
			lineas_divisoras.add(linea)

		llave_dx = Brace(riemann_rectangles[2], direction = DOWN, buff = 0.1).set_color(YELLOW)
		llave_dx.add_updater(
			lambda b: b.become(Brace(riemann_rectangles[2], direction = DOWN, buff = 0.1)))

		llave_label = MathTex("\\triangle x").scale(0.5).next_to(llave_dx.get_center(), DOWN, buff = 0.1)
		llave_label.add_updater(
			lambda b: b.next_to(llave_dx.get_center(), DOWN, buff = 0.1))

		##Grupo para las llaves de la altura f(x)

		llave_altura = VGroup()

		for i in np.arange(0, 5, 1):
			llaves = Brace(riemann_rectangles[i], direction = LEFT, buff = 0.1).set_color(YELLOW)
			llave_altura.add(llaves)

		etiquetas = VGroup()

		for i in np.arange(0, 5, 1):
			etiqueta = llave_altura[i].get_text("$f(x_i)$").scale(0.3).shift(0.6*RIGHT)
			etiquetas.add(etiqueta)

		self.play(Create(lineas_divisoras), run_time = 2)
		self.wait(2)

		self.play(*[GrowFromEdge(rectangulos, linea.get_start())
			        for rectangulos, linea in zip(riemann_rectangles, lineas_divisoras)],
			        *[FadeOut(linea) for linea in lineas_divisoras],
			        lag_ratio = 0.15,
			        run_time = 2)
		self.wait(2)
		self.play(FadeIn(llave_dx), Write(llave_label), run_time = 2)
		self.add(llave_dx, llave_label)
		self.wait(2)
		self.add(riemann_rectangles)

		self.play(*[GrowFromCenter(llave) for llave in llave_altura],
			      *[Write(label) for label in etiquetas], run_time = 2)
		self.wait(2)

		suma_de_areas = MathTex("A", "\\approx",  "\\sum_{i=1}^n", "f(x_i)", "\\triangle x").shift(2.4*UP).scale(0.5) ##3up
		###                      0       1               2             3             4

		self.play(Write(suma_de_areas[0]), GrowFromCenter(suma_de_areas[1]), run_time = 2)
		self.wait(2)

		self.play(Write(suma_de_areas[2]),
			      *[ReplacementTransform(etiquetas[i][0].copy(), suma_de_areas[3]) for i in np.arange(0, 5, 1)],
			      ReplacementTransform(llave_label.copy(), suma_de_areas[4]), run_time = 4)
		self.wait(2)
		self.play(*[FadeOut(llaves) for llaves in llave_altura],
			      *[FadeOut(etiqueta) for etiqueta in etiquetas], run_time = 2)
		self.wait(2)

		self.play(ReplacementTransform(llave_label[0].copy(), dx_label[0]),
			      Write(dx_label[1]), Write(dx_decimal),
			      Write(n_lab), Write(n_decimal), run_time = 2)
		self.wait(2)


		suma_de_areas2 = MathTex("A", "=", "\\lim_{n \\rightarrow \\infty}",  "\\sum_{i=1}^n", "f(x_i)", "\\triangle x").shift(2.4*UP).scale(0.5)
		###                       0    1                     2                       3             4           5

		self.play(ReplacementTransform(suma_de_areas[0], suma_de_areas2[0]),
			      ReplacementTransform(suma_de_areas[1], suma_de_areas2[1]),
			      GrowFromCenter(suma_de_areas2[2]), ReplacementTransform(suma_de_areas[2], suma_de_areas2[3]),
			      ReplacementTransform(suma_de_areas[3], suma_de_areas2[4]),
			      ReplacementTransform(suma_de_areas[4], suma_de_areas2[5]), run_time = 2)
		self.wait(2)
		self.play(dx.animate.set_value(0.0025), run_time = 10)
		self.wait(2)

		suma_de_areas3 = MathTex("A", "=", "\\lim_{n \\rightarrow \\infty}",  "\\sum_{i=1}^n", "f(x_i)", "\\triangle x", "=", "\\int_{a}^{b}f(x)dx").shift(2.4*UP + 0*LEFT).scale(0.5)
		###                       0    1                     2                       3             4           5          6              7

		caja = SurroundingRectangle(suma_de_areas3)

		self.play(*[ReplacementTransform(suma_de_areas2[i], suma_de_areas3[i]) for i in np.arange(0, 6, 1)],
			      GrowFromCenter(suma_de_areas3[6]), Write(suma_de_areas3[7]), FadeOut(suma_de_areas[3]), run_time = 2)
		self.wait(2)
		self.play(Create(caja), run_time = 2)
		self.wait(2)
