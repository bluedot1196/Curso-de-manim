from manim import*

class deri(Scene):
	def construct(self):

		ejes = Axes(x_range = [-1, 3, 0.5],
			        y_range = [-1, 3, 0.5],
			        x_length = 8,
			        y_length = 5,
			        tips = False).set_color(RED).to_edge(LEFT)
		#ejes.move_to([-4, -1.7, 0])

		labels = ejes.get_axis_labels(MathTex("x"), MathTex("y"))

		f = ejes.plot(lambda x: 2*x**2 - x**3 + 1, x_range = [-4, 4], color = BLUE)

		fx = MathTex("f(x)").set_color(YELLOW_B)
		fx.next_to(ejes.c2p(-0.85, f.underlying_function(-0.85)), RIGHT, buff = 0.2)

		##Trackers

		x = ValueTracker(0.5)

		dx = ValueTracker(1)

		punto_p = always_redraw(
			lambda: Dot().move_to(ejes.c2p(x.get_value(), f.underlying_function(x.get_value()))))

		punto_q = always_redraw(
			lambda: Dot().move_to(ejes.c2p(x.get_value() + dx.get_value(), f.underlying_function(x.get_value() + dx.get_value()))))

		linea_p = always_redraw(
			lambda: ejes.get_lines_to_point(ejes.c2p(x.get_value(), f.underlying_function(x.get_value()))).set_color(YELLOW_B))

		linea_q = always_redraw(
			lambda: ejes.get_lines_to_point(ejes.c2p(x.get_value() + dx.get_value(), f.underlying_function(x.get_value() + dx.get_value()))).set_color(YELLOW_B))

		secante = always_redraw(
			lambda: Line(ejes.c2p(x.get_value(), f.underlying_function(x.get_value())), ejes.c2p(x.get_value() + dx.get_value(), f.underlying_function(x.get_value() + dx.get_value()))).set_length(6).set_color(TEAL_E))


		linea_horizontal = always_redraw(
			lambda: Line(ejes.c2p(x.get_value(), f.underlying_function(x.get_value())), ejes.c2p(x.get_value() + dx.get_value(), f.underlying_function(x.get_value()))).set_stroke(color = YELLOW, width = 1))

		linea_vertical = always_redraw(
			lambda: Line(ejes.c2p(x.get_value() + dx.get_value(), f.underlying_function(x.get_value())), ejes.c2p(x.get_value() + dx.get_value(), f.underlying_function(x.get_value() + dx.get_value()))).set_stroke(color = YELLOW, width = 1))

		##etiquetas ejes

		x_lab = MathTex("x").scale(0.6).next_to(ejes.c2p(0.5, 0), DOWN, buff = 0.15)
		fx_lab = MathTex("f(x)").scale(0.6).next_to(ejes.c2p(0, f.underlying_function(0.5)), LEFT, buff = 0.15)

		xh_lab = MathTex("x + h").scale(0.6).next_to(ejes.c2p(1.5, 0), DOWN, buff = 0.15)
		fxh_lab = MathTex("f(x+h)").scale(0.6).next_to(ejes.c2p(0, f.underlying_function(1.5)), LEFT, buff = 0.15)

		llave_hori = Brace(linea_horizontal, direction = DOWN).set_color(YELLOW)
		llave_label = llave_hori.get_text("$\\triangle x$").scale(0.8).shift(0.2*UP)

		llave_verti = Brace(linea_vertical, direction = RIGHT).set_color(YELLOW)
		llave_label2 = llave_verti.get_text("$\\triangle y$").scale(0.8).shift(0.2*LEFT)


		##Lineas para hallar Delta y

		linea1 = Line(ejes.c2p(0, f.underlying_function(0.5)), ejes.c2p(0, f.underlying_function(1.5))).set_color(YELLOW)
		linea2 = Line(ejes.c2p(1.5, f.underlying_function(0.5)), ejes.c2p(1.5, f.underlying_function(1.5))).set_color(YELLOW)

		linea3 = Line(ejes.c2p(0.5, f.underlying_function(0.5)), ejes.c2p(1.5, f.underlying_function(0.5))).set_color(YELLOW)
		linea4 = Line(ejes.c2p(0.5, 0), ejes.c2p(1.5, 0)).set_color(YELLOW)


		##Definicion de la derivada

		slope = MathTex("{\\triangle y", "\\over", "\\triangle x }","=", "{ f(x + h)","-","f(x)", "\\over"," x + h", "-"," x }")
		########                 0        1              2           3          4      5     6       7         8      9    10
		slope.scale(0.8).shift(1.5 * UP + 3.5 * RIGHT)

		slope2 = MathTex("{ \\triangle y", "\\over", "\\triangle x }","=", "{ f(x + h)","-","f(x)", "\\over"," h }")
		########                    0             1           2           3          4      5     6       7       8
		slope2.scale(0.8).shift(1.5 * UP + 3.5 * RIGHT)

		##Numero para h

		llave_movil = always_redraw(
			lambda: BraceBetweenPoints(ejes.c2p(0.5, 0), ejes.c2p(0.5 + dx.get_value(), 0)).set_color(ORANGE))

		h_label = MathTex("h", "=").scale(0.8)
		###                0    1

		h_decimal = always_redraw(
			lambda: DecimalNumber(dx.get_value(), num_decimal_places = 3).scale(0.8).next_to(h_label[1], RIGHT, buff = 0.2))

		grupo_h = VGroup(h_label, h_decimal).next_to(llave_movil, DOWN, buff = 0.1)
		grupo_h.add_updater(lambda m: m.next_to(llave_movil, DOWN, buff = 0.1))

		h_to_limit = MathTex("h \\rightarrow 0").next_to(grupo_h, DOWN, buff=0.5)

		##definicion de limite

		derivada_limite = MathTex("{dy", "\\over", "dx}", "=", "\\lim_","{h \\rightarrow 0}", "{ f(x + h)","-","f(x)", "\\over"," h }").scale(0.8).shift(0.2 * UP + 3.8 * RIGHT)
		################               0       1       2      3      4              5                 6        7      8    9       10    

		definicion_formal_derivada = MathTex("{d","\\over", "dx}","f(x)","=","\\lim_" ,"{h \\rightarrow 0}", "{ f(x+h)","-","f(x)","\\over",  "h}").scale(0.8).shift(0.2 * UP + 3.8 * RIGHT)
		############################             0      1       2      3     4     5               6               7        8    9      10        11      12       13      

		

		self.play(Create(ejes), Write(labels), run_time = 2)
		self.wait(2)
		self.play(Create(f), Write(fx), run_time = 2)
		self.wait(2)
		self.play(GrowFromCenter(punto_p), GrowFromCenter(punto_q))
		self.wait(2)
		self.play(Create(linea_p), run_time = 2)
		self.wait(2)
		self.play(Write(x_lab), run_time = 2)
		self.wait(2)
		self.play(Write(fx_lab), run_time = 2)
		self.wait(2)
		self.play(Create(linea_q), run_time = 2)
		self.wait(2)
		self.play(Write(xh_lab), run_time = 2)
		self.wait(2)
		self.play(Write(fxh_lab), run_time = 2)
		self.wait(2)
		self.play(Create(secante), run_time = 2)
		self.wait(2)
		self.play(Create(linea_horizontal), Create(linea_vertical), run_time = 2)
		self.wait(2)
		self.play(FadeIn(llave_hori), FadeIn(llave_verti), 
			      Write(llave_label), Write(llave_label2), run_time = 2)
		self.wait(2)


		##Calculo de la secante

		self.play(ReplacementTransform(llave_label[0], slope[2]),
			      ReplacementTransform(llave_label2[0], slope[0]),
			      GrowFromCenter(slope[1]), FadeOut(llave_hori),
			      FadeOut(llave_verti), run_time = 2)
		self.wait(2)
		self.play(GrowFromCenter(slope[3]), run_time = 2)
		self.wait(2)
		self.play(GrowFromCenter(slope[7]), run_time = 2)

		self.play(Create(linea2), run_time = 2)
		self.wait(2)
		self.play(ReplacementTransform(linea2, linea1), run_time = 2)
		self.wait(2)
		self.play(ReplacementTransform(fxh_lab[0], slope[4]), GrowFromCenter(slope[5]),
			      ReplacementTransform(fx_lab[0], slope[6]), run_time = 2)
		self.wait(2)

		self.play(Create(linea3), run_time = 2)
		self.wait(2)
		self.play(ReplacementTransform(linea3, linea4), run_time = 2)
		self.wait(2)
		self.play(ReplacementTransform(xh_lab[0], slope[8]), GrowFromCenter(slope[9]),
			      ReplacementTransform(x_lab[0], slope[10]), run_time = 2)
		self.wait(2)

		self.play(FocusOn(slope[8]), FocusOn(slope[10]))  #1:42
		self.play(ReplacementTransform(slope[0], slope2[0]),ReplacementTransform(slope[1], slope2[1]),
			      ReplacementTransform(slope[2], slope2[2]),ReplacementTransform(slope[3], slope2[3]),
			      ReplacementTransform(slope[4], slope2[4]),ReplacementTransform(slope[5], slope2[5]),
			      ReplacementTransform(slope[6], slope2[6]),ReplacementTransform(slope[7], slope2[7]),FadeOut(slope[8]),
			      FadeOut(slope[9]),FadeOut(slope[10]),GrowFromCenter(slope2[8]),
			      FadeOut(linea1), FadeOut(linea4), run_time=2)
		self.wait(2)

		self.play(FadeIn(llave_movil), Write(grupo_h), run_time = 2)
		self.wait(2)
		self.play(dx.animate.set_value(1.3), run_time = 4)
		self.wait(2)

		self.play(ReplacementTransform(slope2[4].copy(),derivada_limite[6]),ReplacementTransform(slope2[5].copy(),derivada_limite[7]),
			      ReplacementTransform(slope2[6].copy(),derivada_limite[8]),ReplacementTransform(slope2[7].copy(),derivada_limite[9]),
			      ReplacementTransform(slope2[8].copy(),derivada_limite[10]),
			      run_time=2)
		self.wait(2) #2:20
		self.play(Write(h_to_limit)) #2:21
		self.play(GrowFromCenter(derivada_limite[4]))  #2:22
		self.play(ReplacementTransform(h_to_limit[0],derivada_limite[5]),run_time=2)
		self.wait(2)
		self.play(dx.animate.set_value(0.001), run_time = 10)
		self.wait(2)
		self.wait(2)
		self.play(ReplacementTransform(slope2[3].copy(),derivada_limite[3]),ReplacementTransform(slope2[0].copy(),derivada_limite[0]),
			      ReplacementTransform(slope2[1].copy(),derivada_limite[1]),ReplacementTransform(slope2[2].copy(),derivada_limite[2]),run_time=2) #2:58
		self.wait(2)

		self.play(ReplacementTransform(derivada_limite[0],definicion_formal_derivada[0]),ReplacementTransform(derivada_limite[1],definicion_formal_derivada[1]),
			      ReplacementTransform(derivada_limite[2],definicion_formal_derivada[2]),ReplacementTransform(derivada_limite[3],definicion_formal_derivada[4]),
			      ReplacementTransform(derivada_limite[4],definicion_formal_derivada[5]),ReplacementTransform(derivada_limite[5],definicion_formal_derivada[6]),
			      ReplacementTransform(derivada_limite[6],definicion_formal_derivada[7]),ReplacementTransform(derivada_limite[7],definicion_formal_derivada[8]),
			      ReplacementTransform(derivada_limite[8],definicion_formal_derivada[9]),ReplacementTransform(derivada_limite[9],definicion_formal_derivada[10]),
			      ReplacementTransform(derivada_limite[10],definicion_formal_derivada[11]),ReplacementTransform(fx[0],definicion_formal_derivada[3]),run_time=3)  #3:15
		self.wait(2) #3:30

		cuadro_derivada = SurroundingRectangle(definicion_formal_derivada)
		self.play(Create(cuadro_derivada),run_time=2) #3:32
		self.wait(2)
		self.play(x.animate.set_value(2), run_time = 3)
		self.wait(2)
