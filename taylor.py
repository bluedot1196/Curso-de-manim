from manim import*
import math


class portada(Scene):
	def construct(self):


		ejes = Axes(x_range = [-2*PI, 2*PI, PI/2],
			        y_range = [-2, 2, 1],
			        x_length = 12,
			        y_length = 7,
			        tips = False).set_color(RED_C).to_edge(LEFT).shift(1.5*DOWN)
		label = ejes.get_axis_labels(MathTex("x"), MathTex("y"))

		f_seno = ejes.plot(lambda x: np.cos(x), x_range = [-2*PI, 2*PI], color = TEAL_E)

		f1 = ejes.plot(lambda x: 1, x_range = [-2*PI, 2*PI], color = YELLOW)

		f2 = ejes.plot(lambda x: 1 - (x**2/2), x_range = [-2*PI, 2*PI], color = YELLOW)

		f3 = ejes.plot(lambda x: 1 - (x**2/2) + (x**4/math.factorial(4)), x_range = [-2*PI, 2*PI], color = ORANGE)

		f4 = ejes.plot(lambda x: 1 - (x**2/2) + (x**4/math.factorial(4)) - (x**6/math.factorial(6)), x_range = [-2*PI, 2*PI], color = RED_C)

		f5 = ejes.plot(lambda x: 1 - (x**2/2) + (x**4/math.factorial(4)) - (x**6/math.factorial(6)) + (x**8/math.factorial(8)), x_range = [-2*PI, 2*PI], color = BLUE_C)

		f6 = ejes.plot(lambda x: x - (x**3/6) + (x**5/120) - (x**7/5040) + (x**9/362880) - (x**(11)/39916800), x_range = [-2*PI, 2*PI], color = BLUE_D)

		f7 = ejes.plot(lambda x: x - (x**3/6) + (x**5/120) - (x**7/5040) + (x**9/362880) - (x**(11)/39916800) + (x**(13)/math.factorial(13)), x_range = [-2*PI, 2*PI], color = BLUE_D)

		f8 = ejes.plot(lambda x: x - (x**3/6) + (x**5/120) - (x**7/5040) + (x**9/362880) - (x**(11)/39916800) + (x**(13)/math.factorial(13)) - (x**(15)/math.factorial(15)), x_range = [-2*PI, 2*PI], color = BLUE_D)

		f9 = ejes.plot(lambda x: x - (x**3/6) + (x**5/120) - (x**7/5040) + (x**9/362880) - (x**(11)/39916800) + (x**(13)/math.factorial(13)) - (x**(15)/math.factorial(15)) + (x**(17)/math.factorial(17)), x_range = [-2*PI, 2*PI], color = BLUE_D)


		self.add(ejes, f_seno, f2, f3, f5)




class pendu(Scene):
    def construct(self):
        
        times=ValueTracker(0)
        theta_max= 15*DEGREES  #PI/6
        l=3
        w=np.sqrt(15/3)
        T=2*PI/w

        refpoint = [-4, 3, 0]

        techo = Line([-6, 3, 0], [-2, 3, 0])
        techo.set_stroke(color = GREY_D, width = 10)


        theta=DecimalNumber().set_color(BLACK).move_to(15*RIGHT)
        theta.add_updater(lambda m: m.set_value(theta_max * np.sin(w*times.get_value())))
        self.add(theta)
        

        def get_line1(x,y):
            line = Line(start=ORIGIN+refpoint, end=x*RIGHT+y*UP+refpoint,color=BLUE)
            global verticalline 
            verticalline = DashedLine(start=line.get_start(),end=line.get_start()+3*DOWN)
            return line



        
        line=always_redraw(lambda: get_line1(l*np.sin(theta.get_value()), -l*np.cos(theta.get_value())))


        def angle_arc(theta):
            global angle
            global arc_text
            if theta==0:
                angle=VectorizedPoint().move_to(10*RIGHT)
                arc_text=VectorizedPoint().move_to(10*RIGHT)
            elif theta>0:
                angle = Angle(line, verticalline, quadrant=(1,1), other_angle=True,color=YELLOW, fill_opacity=0)
            else:
                angle = Angle(line, verticalline, quadrant=(1,1), other_angle=False,color=YELLOW, fill_opacity=0)
            return angle

        #

        def get_ball(x,y):
            dot = Circle(
			             stroke_width = 1,
			             stroke_color = WHITE,
			             fill_color = GREY,
			             fill_opacity = 1,
			             sheen_factor = 1,
			             sheen_direction = UL,
			             radius = 0.25).move_to(x*RIGHT+y*UP+refpoint)
            return dot

        ball = always_redraw(lambda: get_ball(l*np.sin(theta.get_value()), -l*np.cos(theta.get_value())))
        longitud_cuerda = MathTex("l").scale(0.8).next_to(line.get_center(), RIGHT, buff = 0.2).shift(0.55*RIGHT+0.1*UP)


        self.play(Create(verticalline), Create(line),
        	      DrawBorderThenFill(ball), Create(techo),
        	      run_time = 2)
        self.wait(2)
        self.play(times.animate.set_value(T/4), rate_func=smooth, run_time = 2)
        angle= always_redraw(lambda: angle_arc(theta.get_value()))
        arctext=MathTex(r"\theta").scale(0.5).add_updater(lambda m: m.next_to(angle, DOWN))
        self.wait(2)
        self.play(Create(angle), Write(arctext), run_time = 2)
        self.wait(2)
        self.play(times.animate.set_value(T/4 + 2*T), rate_func = linear, run_time = 2*T)
        self.wait(2)
        self.play(Write(longitud_cuerda), run_time = 2)
        self.wait(2)


class t0(Scene):
    def construct(self):
        
        times=ValueTracker(0)
        theta_max= 15*DEGREES  #PI/6
        l=3
        w=np.sqrt(15/3)
        T=2*PI/w

        refpoint = [-4, 3, 0]

        techo = Line([-6, 3, 0], [-2, 3, 0])
        techo.set_stroke(color = GREY_D, width = 10)


        theta=DecimalNumber().set_color(BLACK).move_to(15*RIGHT)
        theta.add_updater(lambda m: m.set_value(theta_max * np.cos(w*times.get_value())))
        self.add(theta)
        

        def get_line1(x,y):
            line = Line(start=ORIGIN+refpoint, end=x*RIGHT+y*UP+refpoint,color=BLUE)
            global verticalline 
            verticalline = DashedLine(start=line.get_start(),end=line.get_start()+3*DOWN)
            return line



        
        line=always_redraw(lambda: get_line1(l*np.sin(theta.get_value()), -l*np.cos(theta.get_value())))


        def angle_arc(theta):
            global angle
            global arc_text
            if theta==0:
                angle=VectorizedPoint().move_to(10*RIGHT)
                arc_text=VectorizedPoint().move_to(10*RIGHT)
            elif theta>0:
                angle = Angle(line, verticalline, quadrant=(1,1), other_angle=True,color=YELLOW, fill_opacity=0)
            else:
                angle = Angle(line, verticalline, quadrant=(1,1), other_angle=False,color=YELLOW, fill_opacity=0)
            return angle

        angle= always_redraw(lambda: angle_arc(theta.get_value()))
        #

        arctext=MathTex(r"\theta").scale(0.5).add_updater(lambda m: m.next_to(angle, DOWN))

        #

        def get_ball(x,y):
            dot = Circle(
			             stroke_width = 1,
			             stroke_color = WHITE,
			             fill_color = GREY,
			             fill_opacity = 1,
			             sheen_factor = 1,
			             sheen_direction = UL,
			             radius = 0.25).move_to(x*RIGHT+y*UP+refpoint)
            return dot

        ball = always_redraw(lambda: get_ball(l*np.sin(theta.get_value()), -l*np.cos(theta.get_value())))
        longitud_cuerda = MathTex("l").scale(0.8).next_to(line.get_center(), RIGHT, buff = 0.2).shift(0.55*RIGHT+0.1*UP)


        self.play(Create(verticalline), Create(line),
        	      DrawBorderThenFill(ball), Create(techo),
        	      run_time = 2)
        self.play(Create(angle), Write(arctext), Write(longitud_cuerda), run_time = 2)
        self.wait(2)

        edo = MathTex("{d^2", "\\theta", "\\over", "dt^2}", "+", "\\omega^2", "sen", "\\theta", "=", "0").scale(0.8).shift(2.4*UP + RIGHT)
        ####             0       1          2         3      4          5      6       7        8    9

        edo2 = MathTex("{d^2", "\\theta", "\\over", "dt^2}", "+", "\\omega^2", "\\theta", "=", "0").scale(0.8).next_to(edo, DOWN, buff = 0.3)
        ####             0       1          2         3       4          5         6       7    8    

        edo3 = MathTex("\\theta", "(t)", "=", "\\theta_0", "cos(\\omega t)").scale(0.8).next_to(edo2, DOWN, buff = 0.5)
        ###                0        1     2        3              4

        omega = MathTex("\\omega^2", "=", "{g", "\\over", "l}").scale(0.8).next_to(edo, RIGHT, buff = 1.2)
        ####                 0        1     2      3       4

        cajota = SurroundingRectangle(edo3)

        self.play(ReplacementTransform(arctext[0].copy(), edo[1]), ReplacementTransform(arctext[0].copy(), edo[7]),
        	      Write(edo[0]), Write(edo[3]), GrowFromCenter(edo[2]), GrowFromCenter(edo[4]),
        	      Write(edo[5]), Write(edo[6]), GrowFromCenter(edo[8]), Write(edo[9]), run_time = 2)
        self.wait(2)
        self.play(ReplacementTransform(edo[5].copy(), omega[0]), ReplacementTransform(longitud_cuerda[0], omega[4]),
        	      GrowFromCenter(omega[3]), GrowFromCenter(omega[1]), Write(omega[2]), run_time = 2)
        self.wait(2)

        ##muy dificil de resolver

        cuadro_sen = SurroundingRectangle(edo[6:8]).set_color(RED)
        llave = Brace(edo, direction = DOWN).set_color(ORANGE)
        llave_lab = llave.get_text("Muy dificil de resolver").scale(0.8).shift(0.2*UP)

        aprox = MathTex("sen", "\\theta", "\\approx", "\\theta").scale(0.8).move_to(refpoint).shift(4*DOWN)
        ###               0       1            2           3
        aprox2 = MathTex("\\theta \\ll 1").scale(0.8).next_to(aprox, DOWN, buff = 0.25)

        aprox3 = MathTex("\\theta < 15^{\\circ}").scale(0.8).next_to(aprox2, DOWN, buff = 0.25)

        self.play(Create(cuadro_sen), run_time = 2)
        self.wait(2)
        self.play(GrowFromCenter(llave), Write(llave_lab), run_time = 2)
        self.wait(2)
        self.play(FadeOut(llave), FadeOut(cuadro_sen), FadeOut(llave_lab), run_time = 2)
        self.wait(2)

        ##aprox seno

        self.play(Write(aprox[0]), ReplacementTransform(arctext[0].copy(), aprox[1]),
        	      GrowFromCenter(aprox[2]), ReplacementTransform(arctext[0].copy(), aprox[3]), run_time = 2)
        self.wait(2)
        self.play(Write(aprox2), run_time = 2)
        self.wait(2)
        self.play(Write(aprox3), run_time = 2)
        self.wait(2)

        self.play(*[ReplacementTransform(edo[i].copy(), edo2[i]) for i in range(0, 6)],
        	      ReplacementTransform(edo[8].copy(), edo2[7]),
        	      ReplacementTransform(edo[9].copy(), edo2[8]),
        	      ReplacementTransform(aprox[3].copy(), edo2[6]), run_time = 2)
        self.wait(2)

        self.play(ReplacementTransform(edo2[1].copy(), edo3[0]), GrowFromCenter(edo3[1]), GrowFromCenter(edo3[2]),
        	      Write(edo3[3]), Write(edo3[4]), run_time = 2)
        self.wait(2)
        self.play(Create(cajota), run_time = 2)
        self.wait(2)
        self.play(times.animate.set_value(10*T), rate_func=linear, run_time = 10*T)
        self.wait(3)

class m1(Scene):
	def construct(self):

		ejes = Axes(x_range = [-2*PI, 2*PI, PI/2],
			        y_range = [-2, 2, 1],
			        x_length = 12,
			        y_length = 7,
			        tips = False).set_color(RED_C)

		label = ejes.get_axis_labels(MathTex("x"), MathTex("y"))

		e1 = MathTex("-2\\pi").next_to(ejes.c2p(-2*PI, 0), DOWN, buff = 0.2)
		e2 = MathTex("-\\pi").next_to(ejes.c2p(-1*PI, 0), DOWN, buff = 0.2)
		e3 = MathTex("\\pi").next_to(ejes.c2p(1*PI, 0), DOWN, buff = 0.2)
		e4 = MathTex("2\\pi").next_to(ejes.c2p(2*PI, 0), DOWN, buff = 0.2)

		etiquetas = VGroup(e1, e2, e3, e4)

		fseno = ejes.plot(lambda x: np.sin(x), x_range = [-2*PI, 2*PI], color = TEAL_E)

		flineal = ejes.plot(lambda x: x, x_range = [-2*PI, 2*PI], color = YELLOW_B)

		label_sen = MathTex("f(x)", "=", "senx").scale(0.8).next_to(ejes.c2p(0.82*PI, fseno.underlying_function(0.82*PI)), RIGHT, buff = 0.2)

		label_x = MathTex("g(x)", "=", "x").scale(0.8).next_to(ejes.c2p(0.6*PI, flineal.underlying_function(0.6*PI)), RIGHT, buff = 0.2)

		approximacion = MathTex("senx", "\\approx", "x").scale(0.8).next_to(label_sen, UP, buff = 1).shift(RIGHT)
		cajitafinal = SurroundingRectangle(approximacion)


		self.play(Write(label), Create(ejes), Write(etiquetas), run_time = 2)
		self.wait(2)
		self.play(Create(fseno), Write(label_sen), run_time = 2)
		self.wait(2)
		self.play(Create(flineal), Write(label_x), run_time = 2)
		self.wait(2)


		##funciones movibles

		x = ValueTracker(0)

		seno = MathTex("f(\\ \\ \\ \\ \\ \\ \\ )", "=", "sen(\\ \\ \\ \\ \\ \\ \\ )", "=", "\\ \\ \\ \\ \\ ").scale(0.8).to_corner(UL)

		equis = MathTex("g(\\ \\ \\ \\ \\ \\ \\ )", "=", "\\ \\ \\ \\ \\ \\ \\ ").scale(0.8).next_to(seno, DOWN, buff = 0.3).to_edge(LEFT)
		#                        0                   1           2

		seno_decimal = always_redraw(
			lambda: DecimalNumber(x.get_value(), num_decimal_places = 3).scale(0.8).next_to(seno[1], LEFT, buff = 0.35))

		seno_decimal2 = always_redraw(
			lambda: DecimalNumber(x.get_value(), num_decimal_places = 3).scale(0.8).next_to(seno[1], RIGHT, buff = 0.9))

		seno_decimal_res = always_redraw(
			lambda: DecimalNumber(fseno.underlying_function(x.get_value()), num_decimal_places = 3).scale(0.8).next_to(seno[3], RIGHT, buff = 0.2))

		cos_decimal = always_redraw(
			lambda: DecimalNumber(x.get_value(), num_decimal_places = 3).scale(0.8).next_to(equis[1], LEFT, buff = 0.35))

		cos_decimal_res = always_redraw(
			lambda: DecimalNumber(flineal.underlying_function(x.get_value()), num_decimal_places = 3).scale(0.8).next_to(equis[1], RIGHT, buff = 0.2))

		self.play(Write(seno), Write(seno_decimal),
			      Write(seno_decimal2), Write(seno_decimal_res),
			      Write(equis), Write(cos_decimal), Write(cos_decimal_res), run_time = 2)
		self.wait(2)

		linea1 = always_redraw(
			lambda: DashedLine(ejes.c2p(-x.get_value(), -4), ejes.c2p(-x.get_value(), 4)).set_color(YELLOW))

		linea2 = always_redraw(
			lambda: DashedLine(ejes.c2p(x.get_value(), -4), ejes.c2p(x.get_value(), 4)).set_color(YELLOW))


		self.play(Create(linea1), Create(linea2), run_time = 2)
		self.wait(2)
		self.play(x.animate.set_value(15*DEGREES), rate_func = linear, run_time = 12)
		self.wait(2)
		self.play(x.animate.set_value(40*DEGREES), rate_func = smooth, run_time = 6)
		self.wait(2)
		self.play(x.animate.set_value(15*DEGREES), run_time = 2)
		self.wait(2)

		rectangulo = Polygon(ejes.c2p(-x.get_value(), -4), ejes.c2p(-x.get_value(), 4),
			                 ejes.c2p(x.get_value(), 4), ejes.c2p(x.get_value(), -4))
		rectangulo.set_fill(color = YELLOW, opacity = 0.3)
		rectangulo.set_stroke(color = BLUE, width = 0)

		self.play(ReplacementTransform(label_sen[1].copy(), approximacion[0]),
			      ReplacementTransform(label_x[1].copy(), approximacion[2]),
			      GrowFromCenter(approximacion[1]),
			      DrawBorderThenFill(rectangulo), Create(cajitafinal), run_time = 2)
		self.wait(2)






class t1(Scene):
	def construct(self):

		fx = MathTex("f(x) = cosx").scale(0.8).to_corner(UL)
		fx2 = MathTex("f(0)", "=", "cos(0)", "=", "1").scale(0.8).next_to(fx, DOWN, buff = 0.3).to_edge(LEFT)
		###             0     1      2       3     4

		fxprima = MathTex("f'(x) = -senx").scale(0.8).next_to(fx, DOWN, buff = 0.3).to_edge(LEFT)
		fxprima0 = MathTex("f'(0) = -sen(0) = 0").scale(0.8).next_to(fxprima, DOWN, buff = 0.26).to_edge(LEFT)

		fx2prima = MathTex("f''(x) = -cosx").scale(0.8).next_to(fxprima, DOWN, buff = 0.3).to_edge(LEFT)
		fx2prima0 = MathTex("f''(0) = -cos(0) = -1").scale(0.8).next_to(fx2prima, DOWN, buff = 0.26).to_edge(LEFT)

		fx3prima = MathTex("f'''(x) = senx").scale(0.8).next_to(fx2prima, DOWN, buff = 0.3).to_edge(LEFT)
		fx3prima0 = MathTex("f'''(0) = sen(0) = 0").scale(0.8).next_to(fx3prima, DOWN, buff = 0.26).to_edge(LEFT)

		fx4prima = MathTex("f^{(4)}(x) = cosx").scale(0.8).next_to(fx3prima, DOWN, buff = 0.3).to_edge(LEFT)
		fx4prima0 = MathTex("f^{(4)}(0) = cos(0) = 1").scale(0.8).next_to(fx4prima, DOWN, buff = 0.26).to_edge(LEFT)

		ejes = Axes(x_range = [-2*PI, 2*PI, PI/2],
			        y_range = [-2, 2, 1],
			        x_length = 12,
			        y_length = 7).set_color(RED_C).shift(1.9*DOWN)
		label = ejes.get_axis_labels(MathTex("x"), MathTex("y"))

		e1 = MathTex("-2\\pi").next_to(ejes.c2p(-2*PI, 0), DOWN, buff = 0.2)
		e2 = MathTex("-\\pi").next_to(ejes.c2p(-1*PI, 0), DOWN, buff = 0.2)
		e3 = MathTex("\\pi").next_to(ejes.c2p(1*PI, 0), DOWN, buff = 0.2)
		e4 = MathTex("2\\pi").next_to(ejes.c2p(2*PI, 0), DOWN, buff = 0.2)

		etiquetas = VGroup(e1, e2, e3, e4)


		funcion = ejes.plot(lambda x: np.cos(x), x_range = [-2*PI, 2*PI], color = BLUE)

		##tangente

		x = ValueTracker(-PI)

		secante = always_redraw(
			lambda: ejes.get_secant_slope_group(
				x = x.get_value(),
				graph = funcion,
				dx = 0.01,
				secant_line_length = 4,
				secant_line_color = TEAL_E))

		f2 = ejes.plot(lambda x: np.cos(x), x_range = [-PI/2, PI/2], color = YELLOW)

		px = MathTex("P(x)", "=", "a_0", "+", "a_1 x", "+", "a_2 x^2").scale(0.8).shift(3.3*UP + 3.5*RIGHT)
		##             0      1     2     3     4       5       6

		px1 = MathTex("P(x)", "=", "1", "+", "a_1 x", "+", "a_2 x^2").scale(0.8).shift(3.3*UP + 3.5*RIGHT)

		px2 = MathTex("P(x)", "=", "1", "+", "0 x", "+", "a_2 x^2").scale(0.8).shift(3.3*UP + 3.5*RIGHT)

		px3 = MathTex("P(x)", "=", "1", "+", "0 x", "+", "\\left(-\\frac{1}{2} \\right) x^2").scale(0.8).shift(3.3*UP + 3.5*RIGHT)
		###              0    1     2    3     4     5                     6

		px4 = MathTex("P(x)", "=", "1", "+", "0 x", "+", "\\left(-\\frac{1}{2} \\right) x^2" ,"+", "a_3 x^3").scale(0.8).shift(3.3*UP + 3.2*RIGHT)
		###             0      1    2    3     4     5                  6                      7       8

		px5 = MathTex("P(x)", "=", "1", "+", "0 x", "+", "\\left(-\\frac{1}{2} \\right) x^2" ,"+", "0 x^3").scale(0.8).shift(3.3*UP + 3.2*RIGHT)
		###             0      1    2    3     4     5                  6                      7       8

		px6 = MathTex("P(x)", "=", "1", "+", "0 x", "+", "\\left(-\\frac{1}{2} \\right) x^2" ,"+", "0 x^3", "+", "a_4 x^4").scale(0.8).shift(3.3*UP + 2.6*RIGHT)
		###             0      1    2    3     4     5                  6                      7       8    9     10

		px7 = MathTex("P(x)", "=", "1", "+", "0 x", "+", "\\left(-\\frac{1}{2} \\right) x^2" ,"+", "0 x^3", "+", "\\frac{1}{24} x^4").scale(0.8).shift(3.3*UP + 2.6*RIGHT)
		###             0      1    2    3     4     5                  6                      7       8    9     10

		rectangulofondo = BackgroundRectangle(px7, color = WHITE, fill_opacity = 0.2)


		pxprima = MathTex("P'(x)", "=", "0", "+", "a_1", "+", "2a_2x").scale(0.8).next_to(px1, DOWN, buff = 0.28)
		##                   0      1    2    3     4     5       6

		pxprima2 = MathTex("P'(0)", "=", "0", "+", "a_1", "+", "2a_2(0)").scale(0.8).next_to(px1, DOWN, buff = 0.28)

		pxprima3 = MathTex("0", "=", "a_1").scale(0.8).next_to(pxprima2, DOWN, buff = 0.25)

		##segunda derivada

		px2prima = MathTex("P''(x)", "=", "2a_2").scale(0.8).next_to(px1, DOWN, buff = 0.28)

		px2prima2 = MathTex("P''(0)", "=", "2a_2").scale(0.8).next_to(px1, DOWN, buff = 0.28)

		px2prima3 = MathTex("-1", "=", "2a_2").scale(0.8).next_to(px2prima2, DOWN, buff = 0.28)

		px2prima4 = MathTex("a_2", "=", "- \\frac{1}{2}").scale(0.8).next_to(px2prima3, DOWN, buff = 0.28)

		##tercera derivada

		px3prima = MathTex("P'''(x)", "=", "3.2.1.a_3").scale(0.8).next_to(px1, DOWN, buff = 0.38)

		px3prima2 = MathTex("P'''(0)", "=", "6a_3").scale(0.8).next_to(px1, DOWN, buff = 0.38)

		px3prima3 = MathTex("0", "=", "6a_3").scale(0.8).next_to(px2prima2, DOWN, buff = 0.28)

		px3prima4 = MathTex("a_3", "=", "0").scale(0.8).next_to(px2prima3, DOWN, buff = 0.28)


		##cuarta derivada

		px4prima = MathTex("P^{(4)}(x)", "=", "4.3.2.1.a_4").scale(0.8).next_to(px1, DOWN, buff = 0.38)

		px4prima2 = MathTex("P^{(4)}(0)", "=", "24a_4").scale(0.8).next_to(px1, DOWN, buff = 0.38)

		px4prima3 = MathTex("1", "=", "24a_4").scale(0.8).next_to(px2prima2, DOWN, buff = 0.28)

		px4prima4 = MathTex("a_4", "=", "\\frac{1}{24}").scale(0.8).next_to(px2prima3, DOWN, buff = 0.28)


		a0 = MathTex("a_0", "=").scale(0.8).next_to(px, DOWN, buff = 0.4).shift(0.3*LEFT)

		a1 = MathTex("a_1", "=").scale(0.8).next_to(a0, DOWN, buff = 0.25)

		a2 = MathTex("a_2", "=").scale(0.8).next_to(a1, DOWN, buff = 0.25)

		a3 = MathTex("a_3", "=").scale(0.8).next_to(px, DOWN, buff = 0.7)

		a4 = MathTex("a_4", "=").scale(0.8).next_to(a3, DOWN, buff = 0.25)

		##polinomio aproox

		px0 = MathTex("P(0)", "=", "a_0", "+", "a_1 (0)", "+", "a_2(0)^2").scale(0.8).next_to(px, DOWN, buff = 0.3)
		###             0      1     2     3       4       5       6

		px02 = MathTex("1", "=", "a_0").scale(0.8).next_to(px0, DOWN, buff = 0.26)
		###             0    1     2

		##Trackers

		a0_num = ValueTracker(0.5)

		a1_num = ValueTracker(0.5)

		a2_num = ValueTracker(0.5)

		a3_num = ValueTracker(0)

		a4_num = ValueTracker(0)

		a0_deci = always_redraw(
			lambda: DecimalNumber(a0_num.get_value(), num_decimal_places = 3).scale(0.8).next_to(a0[1], RIGHT, buff = 0.2))

		a1_deci = always_redraw(
			lambda: DecimalNumber(a1_num.get_value(), num_decimal_places = 3).scale(0.8).next_to(a1[1], RIGHT, buff = 0.2))

		a2_deci = always_redraw(
			lambda: DecimalNumber(a2_num.get_value(), num_decimal_places = 3).scale(0.8).next_to(a2[1], RIGHT, buff = 0.2))

		a3_deci = always_redraw(
			lambda: DecimalNumber(a3_num.get_value(), num_decimal_places = 3).scale(0.8).next_to(a3[1], RIGHT, buff = 0.2))

		a4_deci = always_redraw(
			lambda: DecimalNumber(a4_num.get_value(), num_decimal_places = 3).scale(0.8).next_to(a4[1], RIGHT, buff = 0.2))

		a_grupo = VGroup(a0, a1, a2, a0_deci, a1_deci, a2_deci)

		f_aprox = always_redraw(
			lambda: ejes.plot(lambda x: a0_num.get_value() + a1_num.get_value()*x + a2_num.get_value()*x**2 + a3_num.get_value()*x**3 + a4_num.get_value()*x**4, x_range = [-2*PI, 2*PI], color = YELLOW))

		como = Tex("¿Como encontramos los\\\\\\\
			         coeficientes adecuados?").scale(0.8).next_to(a2, DOWN, buff = 0.3)

		self.play(Write(fx), run_time = 2)
		self.wait(2)
		self.play(Create(ejes), Write(label), Write(etiquetas), run_time = 2)
		self.wait(2)
		self.play(Create(funcion), run_time = 2)
		self.wait(2)
		self.play(Create(f2), run_time = 2)
		self.wait(2)
		self.play(f2.animate.shift(3*LEFT + 1.5*UP), run_time = 2)
		parabola = Tex("Parábola").scale(0.7).next_to(f2.get_top(), UP, buff = 0.1)
		self.wait(2)
		self.play(Write(parabola), run_time = 2)
		self.wait(2)
		self.play(FadeOut(parabola), FadeOut(f2))
		self.wait(2)
		self.play(Write(px), run_time = 2)
		self.wait(2)
		self.play(Write(a0), Write(a1), Write(a2), Write(a0_deci),
			      Write(a1_deci), Write(a2_deci), Create(f_aprox), run_time = 2)
		self.wait(2)

		##parabola hacia abajo

		self.play(a2_num.animate.set_value(-0.8), run_time = 3)
		self.wait(2)
		self.play(a0_num.animate.set_value(1), run_time = 3)
		self.wait(2)
		self.play(a1_num.animate.set_value(0), run_time = 3)
		self.wait(2)
		self.play(a2_num.animate.set_value(-0.5), run_time = 3)
		self.wait(2)
		self.play(Write(como), run_time = 2)
		self.wait(2)
		self.play(FadeOut(como), a_grupo.animate.shift(2.7*DOWN + 0.6*LEFT), run_time = 2)
		self.wait(2)

		punto1 = Dot().move_to(ejes.c2p(0, 1)).set_color(ORANGE)

		self.play(Write(fx2), run_time = 2)
		self.wait(2)
		self.play(ReplacementTransform(fx2[4].copy(), punto1), run_time = 2)
		self.wait(2)
		self.play(Write(px0), run_time = 2)
		self.wait(2)
		self.play(ReplacementTransform(px0[0].copy(), px02[0]), ReplacementTransform(px0[1].copy(), px02[1]),
			      ReplacementTransform(px0[2].copy(), px02[2]), run_time = 2)
		self.wait(2)
		self.play(*[ReplacementTransform(px[i], px1[i]) for i in range(0, 7)], run_time = 2)
		self.wait(2)
		self.play(a1_num.animate.set_value(3),
			      a2_num.animate.set_value(4), rate_func = there_and_back,
			      run_time = 8)
		self.wait(2)
		self.play(FadeOut(px0), FadeOut(px02), FadeOut(fx2), run_time = 2)
		self.wait(2)

		##primera derivada

		self.play(Write(fxprima), run_time = 2)
		self.wait(2)
		self.play(Create(secante), run_time = 2)
		self.wait(2)
		self.play(Write(fxprima0), run_time = 2)	
		self.wait(2)
		self.play(x.animate.set_value(0), run_time = 4)
		self.wait(2)
		self.play(Write(pxprima[0]), GrowFromCenter(pxprima[1]), run_time = 2)
		self.wait(2)
		self.play(Write(pxprima[2:7]), run_time = 2)
		self.wait(2)
		self.play(*[ReplacementTransform(pxprima[i], pxprima2[i]) for i in range(0, 7)], run_time = 2)
		self.wait(2)
		self.play(ReplacementTransform(pxprima2[0].copy(), pxprima3[0]),
			      ReplacementTransform(pxprima2[1].copy(), pxprima3[1]),
			      ReplacementTransform(pxprima2[4].copy(), pxprima3[2]), run_time = 2)
		self.wait(2)
		self.play(*[ReplacementTransform(px1[i], px2[i]) for i in range(0, 7)],
			      FadeOut(fxprima0), FadeOut(pxprima2), FadeOut(pxprima3), run_time = 2)
		self.wait(2)

		##segunda derivada

		self.play(Write(fx2prima), run_time = 2)
		self.wait(2)
		self.play(Write(fx2prima0), run_time = 2)
		self.wait(2)
		self.play(Write(px2prima), run_time = 2)
		self.wait(2)
		self.play(*[ReplacementTransform(px2prima[i], px2prima2[i]) for i in range(0,3)], run_time = 2)
		self.wait(2)
		self.play(*[ReplacementTransform(px2prima2[i].copy(), px2prima3[i]) for i in range(0, 3)], run_time = 2)
		self.wait(2)
		self.play(Write(px2prima4), run_time = 2)
		self.wait(2)
		self.play(*[ReplacementTransform(px2[i], px3[i]) for i in range(0, 7)], run_time = 2)
		self.wait(2)
		self.play(FadeOut(px2prima2), FadeOut(px2prima3),
			      FadeOut(px2prima4), FadeOut(fx2prima0),
			      FadeOut(secante), FadeOut(punto1),
			      run_time = 2)
		self.wait(2)
		self.play(*[ReplacementTransform(px3[i], px4[i]) for i in range(0, 7)], GrowFromCenter(px4[7]),
			      Write(px4[8]), run_time = 2)
		self.wait(2)

		##Tercera derivada

		self.play(Write(fx3prima), run_time = 2)
		self.wait(2)
		self.play(Write(fx3prima0), run_time = 2)
		self.wait(2)

		self.play(Write(px3prima), run_time = 2)
		self.wait(2)
		self.play(*[ReplacementTransform(px3prima[i], px3prima2[i]) for i in range(0,3)], run_time = 2)
		self.wait(2)
		self.play(*[ReplacementTransform(px3prima2[i].copy(), px3prima3[i]) for i in range(0, 3)], run_time = 2)
		self.wait(2)
		self.play(Write(px3prima4), run_time = 2)
		self.wait(2)

		self.play(*[ReplacementTransform(px4[i], px5[i]) for i in range(0, 9)], run_time = 2)
		self.wait(2)
		self.play(FadeOut(px3prima2), FadeOut(px3prima3), FadeOut(px3prima4),
			      FadeOut(fx3prima0), run_time = 2)
		self.wait(2)
		self.play(Write(a3), Write(a3_deci), run_time = 2)
		self.wait(2)
		self.play(a3_num.animate.set_value(3), rate_func = there_and_back, run_time = 6)
		self.play(a3_num.animate.set_value(-3), rate_func = there_and_back, run_time = 6)
		self.wait(2)
		self.play(FadeOut(a3), FadeOut(a3_deci), run_time = 2)
		self.wait(2)

		##cuarta

		self.play(*[ReplacementTransform(px5[i], px6[i]) for i in range(0, 9)], GrowFromCenter(px6[9]),
			      Write(px6[10]), run_time = 2)
		self.wait(2)

		self.play(Write(fx4prima), run_time = 2)
		self.wait(2)
		self.play(Write(fx4prima0), run_time = 2)
		self.wait(2)

		self.play(Write(px4prima), run_time = 2)
		self.wait(2)
		self.play(*[ReplacementTransform(px4prima[i], px4prima2[i]) for i in range(0,3)], run_time = 2)
		self.wait(2)
		self.play(*[ReplacementTransform(px4prima2[i].copy(), px4prima3[i]) for i in range(0, 3)], run_time = 2)
		self.wait(2)
		self.play(Write(px4prima4), run_time = 2)
		self.wait(2)

		self.play(*[ReplacementTransform(px6[i], px7[i]) for i in range(0, 11)], run_time = 2)
		self.wait(2)
		self.play(FadeOut(px4prima2), FadeOut(px4prima3), FadeOut(px4prima4),
			      FadeOut(fx4prima0), run_time = 2)
		self.wait(2)
		self.play(a_grupo.animate.shift(2.4*UP + 0.95*RIGHT), run_time = 2)
		a3.next_to(a2, DOWN, buff = 0.25)
		a4.next_to(a3, DOWN, buff = 0.25)
		a3_deci.next_to(a3[1], RIGHT, buff = 0.2)
		a4_deci.next_to(a4[1], RIGHT, buff = 0.2)

		self.play(Write(a3), Write(a3_deci), Write(a4), Write(a4_deci), run_time = 2)
		self.wait(2)
		self.play(a4_num.animate.set_value(3), rate_func = there_and_back, run_time = 6)
		self.play(a4_num.animate.set_value(-3), rate_func = there_and_back, run_time = 6)
		self.wait(2)
		self.play(a4_num.animate.set_value(1/24), run_time = 4)
		self.wait(2)
		cuadro = SurroundingRectangle(px7)
		self.play(FadeIn(rectangulofondo), run_time = 2)
		self.wait(2)



class t2(Scene):
	def construct(self):

		fx = MathTex("f(x) = senx").scale(0.8).to_corner(UL)

		taylor = MathTex("P(x) = f(a) + \\frac{f'(a)}{1!}(x - a) + \\frac{f''(a)}{2!}(x-a)^2 + \\frac{f'''(a)}{3!}(x - a)^3 + ... + \\frac{f^{(n)(a)}}{n!} (x - a)^n").scale(0.7)
		taylor.shift(2.4*UP)
		cuadro = SurroundingRectangle(taylor)

		taylor2 = MathTex("P(x)", "=", "f(0)", "+", "\\frac{f'(0)}{1!}", "x", "+", "\\frac{f''(0)}{2!}", "x^2", "+", "\\frac{f'''(0)}{3!}", "x^3", "+ ... +", "\\frac{f^{(n)}(0)}{n!}", "x^n").scale(0.7).next_to(taylor, DOWN, buff = 0.4)
		#######             0      1     2      3             4           5    6            7              8     9             10             11      12              13

		taylor3 = MathTex("P(x)", "=", "x", "-", "{x^3",  "\\over", "3!}", "+", "\\frac{x^5}{5!}", "-", "\\frac{x^7}{7!}", "+", "\\frac{x^9}{9!}", "-", "\\frac{x^{11}}{11!}", "+", "...").scale(0.7).shift(1.2*UP)
		####                0      1    2    3      4         5      6      7            8          9          10           11         12           13             14           15    16


		llave1 = Brace(taylor2[2], direction = UP).set_color(RED).shift(1*UP)
		llave2 = Brace(taylor2[4], direction = UP).set_color(RED).shift(1*UP)
		llave3 = Brace(taylor2[7], direction = UP).set_color(RED).shift(1*UP)
		llave4 = Brace(taylor2[10], direction = UP).set_color(RED).shift(1*UP)

		et1 = llave1.get_text("$0$").scale(0.8).shift(0.2*DOWN)
		et2 = llave2.get_text("$1$").scale(0.8).shift(0.2*DOWN)
		et3 = llave3.get_text("$0$").scale(0.8).shift(0.2*DOWN)
		et4 = llave4.get_text("$-1$").scale(0.8).shift(0.2*DOWN)

		self.play(Write(fx), run_time = 2)
		self.wait(2)
		self.play(Write(taylor), Create(cuadro), run_time = 2)
		self.wait(2)
		self.play(Write(taylor2), run_time = 2)
		self.wait(2)
		self.play(FadeOut(taylor), FadeOut(cuadro),
			      taylor2.animate.shift(1.2*UP), run_time = 2)
		self.wait(2)

		senx = MathTex("f(x) = senx", "\\longrightarrow", "f(0) =", "0").scale(0.7).to_corner(UL).shift(3.3*DOWN)
		####                  0                1            2        3      

		senx1 = MathTex("f'(x) = cosx", "\\longrightarrow", "f'(0) =", "1").scale(0.7).next_to(senx, DOWN, buff = 0.3).to_edge(LEFT)

		senx2 = MathTex("f''(x) = -senx", "\\longrightarrow", "f''(0) =", "0").scale(0.7).next_to(senx1, DOWN, buff = 0.3).to_edge(LEFT)

		senx3 = MathTex("f'''(x) = -cosx", "\\longrightarrow", "f'''(0) =", "-1").scale(0.7).next_to(senx2, DOWN, buff = 0.3).to_edge(LEFT)

		senx4 = MathTex("f^{(4)}(x) = senx", "\\longrightarrow", "f^{(4)}(0) =", "0").scale(0.7).next_to(senx3, DOWN, buff = 0.3).to_edge(LEFT)

		senx5 = MathTex("f^{(5)}(x) = cosx", "\\longrightarrow", "f^{(5)}(0) =", "1").scale(0.7).next_to(senx4, DOWN, buff = 0.3).to_edge(LEFT)

		senx[1].set_color(YELLOW_B)
		senx1[1].set_color(YELLOW_B)
		senx2[1].set_color(YELLOW_B)
		senx3[1].set_color(YELLOW_B)
		senx4[1].set_color(YELLOW_B)
		senx5[1].set_color(YELLOW_B)

		self.play(Write(senx[0]), Write(senx1[0]), Write(senx2[0]),
			      Write(senx3[0]), Write(senx4[0]), Write(senx5[0]), run_time = 2)
		self.wait(2)
		self.play(GrowFromCenter(senx[1]), GrowFromCenter(senx1[1]), 
			      GrowFromCenter(senx2[1]), GrowFromCenter(senx3[1]),
			      GrowFromCenter(senx4[1]), GrowFromCenter(senx5[1]), run_time  = 2)
		self.wait(2)
		self.play(Write(senx[2:4]), Write(senx1[2:4]), Write(senx2[2:4]),
			      Write(senx3[2:4]), Write(senx4[2:4]), Write(senx5[2:4]), run_time = 2)
		self.wait(2)
		self.play(GrowFromCenter(llave1), GrowFromCenter(llave2), GrowFromCenter(llave3),
			      GrowFromCenter(llave4), ReplacementTransform(senx[3].copy(), et1[0]),
			      ReplacementTransform(senx1[3].copy(), et2[0]),
			      ReplacementTransform(senx2[3].copy(), et3[0]),
			      ReplacementTransform(senx3[3].copy(), et4[0]), run_time = 2)
		self.wait(2)

		self.play(ReplacementTransform(taylor2[0].copy(), taylor3[0]),
			      ReplacementTransform(taylor2[1].copy(), taylor3[1]),
			      ReplacementTransform(taylor2[5].copy(), taylor3[2]),
			      GrowFromCenter(taylor3[3]), ReplacementTransform(taylor2[11].copy(), taylor3[4]),
			      GrowFromCenter(taylor3[5]), Write(taylor3[6]), Write(taylor3[7:17]), run_time = 2)
		self.wait(2)
		self.play(FadeOut(llave1), FadeOut(llave2), FadeOut(llave3), FadeOut(llave4),
			      FadeOut(et1), FadeOut(et2), FadeOut(et3), FadeOut(et4),
			      FadeOut(taylor2), FadeOut(senx), FadeOut(senx1),
			      FadeOut(senx2), FadeOut(senx3), FadeOut(senx4), FadeOut(senx5),
			      taylor3.animate.to_corner(UR), run_time = 2)
		self.wait(2)


		##EJES

		ejes = Axes(x_range = [-2*PI, 2*PI, PI/2],
			        y_range = [-2, 2, 1],
			        x_length = 12,
			        y_length = 7,
			        tips = False).set_color(RED_C).to_edge(LEFT).shift(DOWN)
		label = ejes.get_axis_labels(MathTex("x"), MathTex("y"))

		self.play(Create(ejes), Write(label))

		f_seno = ejes.plot(lambda x: np.sin(x), x_range = [-2*PI, 2*PI], color = TEAL_E)

		f1 = ejes.plot(lambda x: x, x_range = [-2*PI, 2*PI], color = BLUE_D)

		f2 = ejes.plot(lambda x: x - (x**3/6), x_range = [-2*PI, 2*PI], color = BLUE_D)

		f3 = ejes.plot(lambda x: x - (x**3/6) + (x**5/120), x_range = [-2*PI, 2*PI], color = BLUE_D)

		f4 = ejes.plot(lambda x: x - (x**3/6) + (x**5/120) - (x**7/5040), x_range = [-2*PI, 2*PI], color = BLUE_D)

		f5 = ejes.plot(lambda x: x - (x**3/6) + (x**5/120) - (x**7/5040) + (x**9/362880), x_range = [-2*PI, 2*PI], color = BLUE_D)

		f6 = ejes.plot(lambda x: x - (x**3/6) + (x**5/120) - (x**7/5040) + (x**9/362880) - (x**(11)/39916800), x_range = [-2*PI, 2*PI], color = BLUE_D)

		f7 = ejes.plot(lambda x: x - (x**3/6) + (x**5/120) - (x**7/5040) + (x**9/362880) - (x**(11)/39916800) + (x**(13)/math.factorial(13)), x_range = [-2*PI, 2*PI], color = BLUE_D)

		f8 = ejes.plot(lambda x: x - (x**3/6) + (x**5/120) - (x**7/5040) + (x**9/362880) - (x**(11)/39916800) + (x**(13)/math.factorial(13)) - (x**(15)/math.factorial(15)), x_range = [-2*PI, 2*PI], color = BLUE_D)

		f9 = ejes.plot(lambda x: x - (x**3/6) + (x**5/120) - (x**7/5040) + (x**9/362880) - (x**(11)/39916800) + (x**(13)/math.factorial(13)) - (x**(15)/math.factorial(15)) + (x**(17)/math.factorial(17)), x_range = [-2*PI, 2*PI], color = BLUE_D)

		brace1 = Brace(taylor3[2]).set_color(YELLOW)
		brace2 = Brace(taylor3[2:5]).set_color(YELLOW)
		brace3 = Brace(taylor3[2:9]).set_color(YELLOW)
		brace4 = Brace(taylor3[2:11]).set_color(YELLOW)
		brace5 = Brace(taylor3[2:13]).set_color(YELLOW)
		brace6 = Brace(taylor3[2:15]).set_color(YELLOW)
		brace7 = Brace(taylor3[2:17]).set_color(YELLOW)

		self.play(Create(f_seno), run_time = 2)
		self.wait(2)
		self.play(Create(f1), GrowFromCenter(brace1), run_time = 2)
		self.wait(2)
		self.play(ReplacementTransform(f1, f2), ReplacementTransform(brace1, brace2), run_time = 2)
		self.wait(2)
		self.play(ReplacementTransform(f2, f3), ReplacementTransform(brace2, brace3), run_time = 2)
		self.wait(2)
		self.play(ReplacementTransform(f3, f4), ReplacementTransform(brace3, brace4), run_time = 2)
		self.wait(2)
		self.play(ReplacementTransform(f4, f5), ReplacementTransform(brace4, brace5), run_time = 2)
		self.wait(2)
		self.play(ReplacementTransform(f5, f6), ReplacementTransform(brace5, brace6), run_time = 2)
		self.wait(2)
		self.play(ReplacementTransform(f6, f7), ReplacementTransform(brace6, brace7), run_time = 2)
		self.wait(2)
		self.play(ReplacementTransform(f7, f8), run_time = 2)
		self.wait(2)
		self.play(ReplacementTransform(f8, f9), run_time = 2)
		self.wait(2)


class t3(Scene):
	def construct(self):

		aprox = MathTex("sen x", "\\approx", "x - \\frac{x^3}{3!} + \\frac{x^5}{5!} - \\frac{x^7}{7!}", "+ \\frac{x^9}{9!} - \\frac{x^{11}}{11!} + ...")
		###               0             1                           2                                                3
		aprox.scale(1.2)

		llave = Brace(aprox[2:4], direction = UP).set_color(RED)
		llave_tex = llave.get_text("Serie de Taylor").scale(0.9).shift(0.2*DOWN)

		llave_polinomio = Brace(aprox[2], direction = DOWN).set_color(RED)
		polinomio = llave_polinomio.get_text("Polinomio de Taylor").scale(0.9).shift(0.2*UP)

		self.play(Write(aprox[0]), GrowFromCenter(aprox[1]), run_time = 2)
		self.wait(2)
		self.play(Write(aprox[2:4]), run_time = 2)
		self.wait(2)
		self.play(GrowFromCenter(llave), Write(llave_tex), run_time = 2)
		self.wait(2)
		self.play(GrowFromCenter(llave_polinomio), Write(polinomio), run_time = 2)
		self.wait(2)


class t4(Scene):
	def construct(self):

		suma = MathTex("\\frac{1}{2} + \\frac{1}{4}", "+ \\frac{1}{8}", "+ \\frac{1}{16}", "+ \\frac{1}{32}", "+ \\frac{1}{64}", "+ \\frac{1}{128}", "+ \\frac{1}{256}", "+ ...", "=", "1")
		###                            0                    1                    2                  3                 4                5                   6                 7     8    9

		l1 = Brace(suma[0], direction = DOWN).set_color(ORANGE)
		l2 = Brace(suma[0:2], direction = DOWN).set_color(ORANGE)
		l3 = Brace(suma[0:3], direction = DOWN).set_color(ORANGE)
		l4 = Brace(suma[0:4], direction = DOWN).set_color(ORANGE)
		l5 = Brace(suma[0:5], direction = DOWN).set_color(ORANGE)
		l6 = Brace(suma[0:6], direction = DOWN).set_color(ORANGE)
		l7 = Brace(suma[0:7], direction = DOWN).set_color(ORANGE)
		l8 = Brace(suma[0:8], direction = DOWN).set_color(ORANGE)
		
		t1 = l1.get_text("0.75").scale(0.8).shift(0.2*UP)
		t2 = l2.get_text("0.875").scale(0.8).shift(0.2*UP)
		t3 = l3.get_text("0.9375").scale(0.8).shift(0.2*UP)
		t4 = l4.get_text("0.96875").scale(0.8).shift(0.2*UP)
		t5 = l5.get_text("0.984375").scale(0.8).shift(0.2*UP)
		t6 = l6.get_text("0.992188").scale(0.8).shift(0.2*UP)
		t7 = l7.get_text("0.996094").scale(0.8).shift(0.2*UP)
		t8 = l8.get_text("0.999023").scale(0.8).shift(0.2*UP)

		converte = Tex("Converge", "\\ a  $1$").next_to(suma, UP, buff = 1.2)
		converte[0].set_color(YELLOW)

		self.play(Write(suma[0:8]), run_time = 2)
		self.wait()
		self.play(GrowFromCenter(l1), Write(t1), run_time = 2)
		self.wait()
		self.play(ReplacementTransform(l1, l2), ReplacementTransform(t1, t2))
		self.wait()
		self.play(ReplacementTransform(l2, l3), ReplacementTransform(t2, t3))
		self.wait()
		self.play(ReplacementTransform(l3, l4), ReplacementTransform(t3, t4))
		self.wait()
		self.play(ReplacementTransform(l4, l5), ReplacementTransform(t4, t5))
		self.wait()
		self.play(ReplacementTransform(l5, l6), ReplacementTransform(t5, t6))
		self.wait()
		self.play(ReplacementTransform(l6, l7), ReplacementTransform(t6, t7))
		self.wait()
		self.play(ReplacementTransform(t7, t8), ReplacementTransform(l7, l8))
		self.wait()
		self.play(Write(converte), run_time =  2)
		self.wait(2)
		self.play(GrowFromCenter(suma[8]), Write(suma[9]), run_time = 2)
		self.wait(2)


class t5(Scene):
	def construct(self):

		fx = MathTex("f(x) = e^x").scale(0.8).to_corner(UL)

		ejes = Axes(x_range = [-3, 4, 1],
			        y_range = [-1, 20, 1],
			        x_length = 9,
			        y_length = 7,
			        tips = False).set_color(RED_C).shift(LEFT)

		f_exp = ejes.plot(lambda x: np.exp(x), x_range = [-3, 4], color = BLUE_D)


		ex = MathTex("f(x) = e^x", "\\longrightarrow", "f(0) =", "1").scale(0.7).to_corner(UL).shift(1.5*DOWN)
		####                  0                1            2        3      

		ex1 = MathTex("f'(x) = e^x", "\\longrightarrow", "f'(0) =", "1").scale(0.7).next_to(ex, DOWN, buff = 0.3).to_edge(LEFT)

		ex2 = MathTex("f''(x) = e^x", "\\longrightarrow", "f''(0) =", "1").scale(0.7).next_to(ex1, DOWN, buff = 0.3).to_edge(LEFT)

		ex3 = MathTex("f'''(x) = e^x", "\\longrightarrow", "f'''(0) =", "1").scale(0.7).next_to(ex2, DOWN, buff = 0.3).to_edge(LEFT)

		ex4 = MathTex("f^{(4)}(x) = e^x", "\\longrightarrow", "f^{(4)}(0) =", "1").scale(0.7).next_to(ex3, DOWN, buff = 0.3).to_edge(LEFT)

		taylor = MathTex("e^x", "\\approx", "1", "+", "1", "\\frac{x}{1!}", "+", "1", "\\frac{x^2}{2!}", "+", "1", "\\frac{x^3}{3!}", "+", "1", "\\frac{x^4}{4!}", "+", "...", "").scale(0.8).to_corner(UR).shift(0.2*LEFT)
		####               0         1       2    3    4         5           6    7           8           9    10       11             12   13         144          15    16   17

		taylor2 = MathTex("e^x", "=", "1", "+", "1", "\\frac{x}{1!}", "+", "1", "\\frac{x^2}{2!}", "+", "1", "\\frac{x^3}{3!}", "+", "1", "\\frac{x^4}{4!}", "+", "...", "").scale(0.8).to_corner(UR).shift(0.2*LEFT)
		####               0         1       2    3    4         5           6    7           8           9    10       11             12   13         144           15

		rectangle = BackgroundRectangle(taylor,color=WHITE, fill_opacity=0.15)


		ex[1].set_color(YELLOW_B)
		ex1[1].set_color(YELLOW_B)
		ex2[1].set_color(YELLOW_B)
		ex3[1].set_color(YELLOW_B)
		ex4[1].set_color(YELLOW_B)

		self.play(Write(fx), run_time = 2)
		self.wait(2)
		self.play(Create(ejes), run_time = 2)
		self.wait(2)
		self.play(Create(f_exp), run_time = 2)
		self.wait(2)
		self.play(Write(ex[0]), Write(ex1[0]), Write(ex2[0]),
			      Write(ex3[0]), Write(ex4[0]), GrowFromCenter(ex[1]),
			      GrowFromCenter(ex1[1]), GrowFromCenter(ex2[1]),
			      GrowFromCenter(ex3[1]), GrowFromCenter(ex4[1]),
			      Write(ex[2:4]), Write(ex1[2:4]), Write(ex2[2:4]),
			      Write(ex3[2:4]), Write(ex4[2:4]), run_time = 2)
		self.wait(2)
		self.play(ReplacementTransform(ex[3].copy(), taylor[2]), ReplacementTransform(ex1[3].copy(), taylor[4]),
			      ReplacementTransform(ex2[3].copy(), taylor[7]), ReplacementTransform(ex3[3].copy(), taylor[10]),
			      ReplacementTransform(ex4[3].copy(), taylor[13]), run_time = 2)
		self.play(Write(taylor[0]), GrowFromCenter(taylor[1]), GrowFromCenter(taylor[3]),
			      Write(taylor[5]), GrowFromCenter(taylor[6]), Write(taylor[8]),
			      GrowFromCenter(taylor[9]), Write(taylor[11]), GrowFromCenter(taylor[12]),
			      Write(taylor[14]), Write(taylor[15]), Write(taylor[16]), FadeIn(rectangle), run_time = 2)
		self.wait(2)

		punto_ref = Dot().move_to(ejes.input_to_graph_point(x = 2, graph = f_exp)).set_color(YELLOW)
		linea_vertical = ejes.get_vertical_line(ejes.input_to_graph_point(x = 2, graph = f_exp)).set_color(YELLOW_B)

		self.play(GrowFromCenter(punto_ref), Create(linea_vertical), run_time = 2)
		self.wait(2)

		##aproximaciones de taylor

		a1 = ejes.plot(lambda x: 1, x_range = [-3, 4], color = ORANGE)
		p1 = Dot().move_to(ejes.input_to_graph_point(x = 2, graph = a1)).set_color(YELLOW)
		b1 = Brace(taylor[2]).set_color(YELLOW_B)		

		a2 = ejes.plot(lambda x: 1 + x/1, x_range = [-3, 4], color = ORANGE)
		p2 = Dot().move_to(ejes.input_to_graph_point(x = 2, graph = a2)).set_color(YELLOW)
		b2 = Brace(taylor[2:6]).set_color(YELLOW_B)
		
		a3 = ejes.plot(lambda x: 1 + x/1 + x**2/math.factorial(2), x_range = [-3, 4], color = ORANGE)
		p3 = Dot().move_to(ejes.input_to_graph_point(x = 2, graph = a3)).set_color(YELLOW)
		b3 = Brace(taylor[2:9]).set_color(YELLOW_B)
		
		a4 = ejes.plot(lambda x: 1 + x/1 + x**2/math.factorial(2) + x**3/math.factorial(3), x_range = [-3, 4], color = ORANGE)
		p4 = Dot().move_to(ejes.input_to_graph_point(x = 2, graph = a4)).set_color(YELLOW)
		b4 = Brace(taylor[2:12]).set_color(YELLOW_B)
		
		a5 = ejes.plot(lambda x: 1 + x/1 + x**2/math.factorial(2) + x**3/math.factorial(3) + x**4/math.factorial(4), x_range = [-3, 4], color = ORANGE)
		p5 = Dot().move_to(ejes.input_to_graph_point(x = 2, graph = a5)).set_color(YELLOW)
		b5 = Brace(taylor[2:15]).set_color(YELLOW_B)

		a6 = ejes.plot(lambda x: 1 + x/1 + x**2/math.factorial(2) + x**3/math.factorial(3) + x**4/math.factorial(4) + x**5/math.factorial(5), x_range = [-3, 4], color = ORANGE)
		p6 = Dot().move_to(ejes.input_to_graph_point(x = 2, graph = a6)).set_color(YELLOW)
		b6 = Brace(taylor[2:17]).set_color(YELLOW_B)

		a7 = ejes.plot(lambda x: 1 + x/1 + x**2/math.factorial(2) + x**3/math.factorial(3) + x**4/math.factorial(4) + x**5/math.factorial(5) + x**6/math.factorial(6), x_range = [-3, 4], color = ORANGE)
		p7 = Dot().move_to(ejes.input_to_graph_point(x = 2, graph = a7)).set_color(YELLOW)
		b7 = Brace(taylor[2:18]).set_color(YELLOW_B)

		self.play(Create(a1), GrowFromCenter(p1), GrowFromCenter(b1), run_time = 2)
		self.wait(2)
		self.play(ReplacementTransform(a1, a2), ReplacementTransform(p1, p2), ReplacementTransform(b1, b2))
		self.wait()
		self.play(ReplacementTransform(a2, a3), ReplacementTransform(p2, p3), ReplacementTransform(b2, b3))
		self.wait()
		self.play(ReplacementTransform(a3, a4), ReplacementTransform(p3, p4), ReplacementTransform(b3, b4))
		self.wait()
		self.play(ReplacementTransform(a4, a5), ReplacementTransform(p4, p5), ReplacementTransform(b4, b5))
		self.wait()
		self.play(ReplacementTransform(a5, a6), ReplacementTransform(p5, p6), ReplacementTransform(b5, b6))
		self.wait()
		self.play(ReplacementTransform(a6, a7), ReplacementTransform(p6, p7), ReplacementTransform(b6, b7))
		self.wait()
		self.play(FadeOut(a7), FadeOut(b7), FadeOut(p7))
		self.wait(2)

		punto_ref2 = Dot().move_to(ejes.input_to_graph_point(x = 2.5, graph = f_exp)).set_color(YELLOW)
		linea_vertical2 = ejes.get_vertical_line(ejes.input_to_graph_point(x = 2.5, graph = f_exp)).set_color(YELLOW_B)

		self.play(ReplacementTransform(punto_ref, punto_ref2), ReplacementTransform(linea_vertical, linea_vertical2), run_time = 2)
		self.wait(2)


		##aproximaciones de taylor

		a11 = ejes.plot(lambda x: 1, x_range = [-3, 4], color = ORANGE)
		p11 = Dot().move_to(ejes.input_to_graph_point(x = 2.5, graph = a11)).set_color(YELLOW)
		b11 = Brace(taylor[2]).set_color(YELLOW_B)		

		a22 = ejes.plot(lambda x: 1 + x/1, x_range = [-3, 4], color = ORANGE)
		p22 = Dot().move_to(ejes.input_to_graph_point(x = 2.5, graph = a22)).set_color(YELLOW)
		b22 = Brace(taylor[2:6]).set_color(YELLOW_B)
		
		a33 = ejes.plot(lambda x: 1 + x/1 + x**2/math.factorial(2), x_range = [-3, 4], color = ORANGE)
		p33 = Dot().move_to(ejes.input_to_graph_point(x = 2.5, graph = a33)).set_color(YELLOW)
		b33 = Brace(taylor[2:9]).set_color(YELLOW_B)
		
		a44 = ejes.plot(lambda x: 1 + x/1 + x**2/math.factorial(2) + x**3/math.factorial(3), x_range = [-3, 4], color = ORANGE)
		p44 = Dot().move_to(ejes.input_to_graph_point(x = 2.5, graph = a44)).set_color(YELLOW)
		b44 = Brace(taylor[2:12]).set_color(YELLOW_B)
		
		a55 = ejes.plot(lambda x: 1 + x/1 + x**2/math.factorial(2) + x**3/math.factorial(3) + x**4/math.factorial(4), x_range = [-3, 4], color = ORANGE)
		p55 = Dot().move_to(ejes.input_to_graph_point(x = 2.5, graph = a55)).set_color(YELLOW)
		b55 = Brace(taylor[2:15]).set_color(YELLOW_B)

		a66 = ejes.plot(lambda x: 1 + x/1 + x**2/math.factorial(2) + x**3/math.factorial(3) + x**4/math.factorial(4) + x**5/math.factorial(5), x_range = [-3, 4], color = ORANGE)
		p66 = Dot().move_to(ejes.input_to_graph_point(x = 2.5, graph = a66)).set_color(YELLOW)
		b66 = Brace(taylor[2:17]).set_color(YELLOW_B)

		a77 = ejes.plot(lambda x: 1 + x/1 + x**2/math.factorial(2) + x**3/math.factorial(3) + x**4/math.factorial(4) + x**5/math.factorial(5) + x**6/math.factorial(6), x_range = [-3, 4], color = ORANGE)
		p77 = Dot().move_to(ejes.input_to_graph_point(x = 2.5, graph = a77)).set_color(YELLOW)
		b77 = Brace(taylor[2:18]).set_color(YELLOW_B)

		a88 = ejes.plot(lambda x: 1 + x/1 + x**2/math.factorial(2) + x**3/math.factorial(3) + x**4/math.factorial(4) + x**5/math.factorial(5) + x**6/math.factorial(6) + x**7/math.factorial(7), x_range = [-3, 4], color = ORANGE)
		p88 = Dot().move_to(ejes.input_to_graph_point(x = 2.5, graph = a88)).set_color(YELLOW)
		b88 = Brace(taylor[2:18]).set_color(YELLOW_B)

		a99 = ejes.plot(lambda x: 1 + x/1 + x**2/math.factorial(2) + x**3/math.factorial(3) + x**4/math.factorial(4) + x**5/math.factorial(5) + x**6/math.factorial(6) + x**7/math.factorial(7) + x**8/math.factorial(8), x_range = [-3, 4], color = ORANGE)
		p99 = Dot().move_to(ejes.input_to_graph_point(x = 2.5, graph = a99)).set_color(YELLOW)
		b99 = Brace(taylor[2:18]).set_color(YELLOW_B)

		self.play(Create(a11), GrowFromCenter(p11), GrowFromCenter(b11), run_time = 2)
		self.wait(2)
		self.play(ReplacementTransform(a11, a22), ReplacementTransform(p11, p22), ReplacementTransform(b11, b22))
		self.wait()
		self.play(ReplacementTransform(a22, a33), ReplacementTransform(p22, p33), ReplacementTransform(b22, b33))
		self.wait()
		self.play(ReplacementTransform(a33, a44), ReplacementTransform(p33, p44), ReplacementTransform(b33, b44))
		self.wait()
		self.play(ReplacementTransform(a44, a55), ReplacementTransform(p44, p55), ReplacementTransform(b44, b55))
		self.wait()
		self.play(ReplacementTransform(a55, a66), ReplacementTransform(p55, p66), ReplacementTransform(b55, b66))
		self.wait()
		self.play(ReplacementTransform(a66, a77), ReplacementTransform(p66, p77), ReplacementTransform(b66, b77))
		self.wait()
		self.play(ReplacementTransform(a77, a88), ReplacementTransform(p77, p88), ReplacementTransform(b66, b77))
		self.wait()
		self.play(ReplacementTransform(a88, a99), ReplacementTransform(p88, p99), ReplacementTransform(b88, b99))
		self.wait()

		cajafeliz = SurroundingRectangle(taylor2)

		self.play(*[ReplacementTransform(taylor[i], taylor2[i]) for i in range(0, 17)], Create(cajafeliz), run_time = 2)
		self.wait(2)


###Ln(x)


class t6(Scene):
	def construct(self):

		fx = MathTex("f(x) = \\ln x").scale(0.6).to_corner(UL)

		ejes = Axes(x_range = [-1, 5, 1],
			        y_range = [-2, 3, 1],
			        x_length = 9,
			        y_length = 7,
			        tips = False).set_color(RED_C).shift(LEFT + DOWN).add_coordinates()

		f_exp = ejes.plot(lambda x: np.log(x), x_range = [0.1, 5], color = BLUE_D)


		taylor = MathTex("\\ln x",  "\\approx", "(x-1)", "-", "\\frac{(x-1)^2}{2}", "+", "\\frac{(x-1)^3}{3}", "-", "\\frac{(x-1)^4}{4}", "+", "\\frac{(x-1)^5}{5}", "-", "\\frac{(x-1)^6}{6}", "+", "\\frac{(x-1)^7}{7}", "+", "...").scale(0.6).next_to(fx, RIGHT, buff = 0.6).shift(0.1*UP)
		###                  0           1         2      3             4            5            6             7          8               9             10          11            12            13             14          15
		####                

		taylor2 = MathTex("\\ln x",  "\\approx", "(x-1)", "-", "\\frac{(x-1)^2}{2}", "+", "\\frac{(x-1)^3}{3}", "-", "\\frac{(x-1)^4}{4}", "+", "\\frac{(x-1)^5}{5}", "-", "\\frac{(x-1)^6}{6}", "+", "\\frac{(x-1)^7}{7}", "+", "...").scale(0.6).next_to(fx, RIGHT, buff = 0.6).shift(0.1*UP)
		####                  0            1        2      3             4            5             6            7                8         9            10            11          12            13          14             15     16         

		rectangle = BackgroundRectangle(taylor,color= WHITE, fill_opacity= 0.25)

		dash1 = DashedLine(ejes.c2p(0, -2), ejes.c2p(0, 2))
		dash2 = DashedLine(ejes.c2p(2, -2), ejes.c2p(2, 2))

		centro = Dot().move_to(ejes.c2p(1, 0))


		

		self.play(Write(fx), run_time = 2)
		self.wait(2)
		self.play(Create(ejes), run_time = 2)
		self.wait(2)
		self.play(Create(f_exp), GrowFromCenter(centro), run_time = 2)
		self.wait(2)
		self.play(Write(taylor), FadeIn(rectangle), run_time = 2)
		self.wait(2)
		self.play(Create(dash1), Create(dash2), run_time = 2)
		self.wait(2)


		

		punto_ref = Dot().move_to(ejes.input_to_graph_point(x = 1.8, graph = f_exp)).set_color(YELLOW).scale(1)
		linea_vertical = ejes.get_vertical_line(ejes.input_to_graph_point(x = 1.8, graph = f_exp)).set_color(YELLOW_B)

		self.play(GrowFromCenter(punto_ref), Create(linea_vertical), run_time = 2)
		self.wait(2)

		##aproximaciones de taylor

		a1 = ejes.plot(lambda x: (x-1), x_range = [0.1, 5], color = ORANGE)
		p1 = Dot().move_to(ejes.input_to_graph_point(x = 1.8, graph = a1)).set_color(YELLOW).scale(1)
		b1 = Brace(taylor[2]).set_color(YELLOW_B)		

		a2 = ejes.plot(lambda x: (x-1) - (x-1)**2/2, x_range = [0.1, 5], color = ORANGE)
		p2 = Dot().move_to(ejes.input_to_graph_point(x = 1.8, graph = a2)).set_color(YELLOW).scale(1)
		b2 = Brace(taylor[2:5]).set_color(YELLOW_B)
		
		a3 = ejes.plot(lambda x: (x-1) - (x-1)**2/2 + (x-1)**3/3, x_range = [0.1, 5], color = ORANGE)
		p3 = Dot().move_to(ejes.input_to_graph_point(x = 1.8, graph = a3)).set_color(YELLOW).scale(1)
		b3 = Brace(taylor[2:7]).set_color(YELLOW_B)
		
		a4 = ejes.plot(lambda x: (x-1) - (x-1)**2/2 + (x-1)**3/3 - (x-1)**4/4, x_range = [0.1, 5], color = ORANGE)
		p4 = Dot().move_to(ejes.input_to_graph_point(x = 1.8, graph = a4)).set_color(YELLOW).scale(1)
		b4 = Brace(taylor[2:9]).set_color(YELLOW_B)
		
		a5 = ejes.plot(lambda x: (x-1) - (x-1)**2/2 + (x-1)**3/3 - (x-1)**4/4 + (x-1)**5/5, x_range = [0.1, 5], color = ORANGE)
		p5 = Dot().move_to(ejes.input_to_graph_point(x = 1.8, graph = a5)).set_color(YELLOW).scale(1)
		b5 = Brace(taylor[2:11]).set_color(YELLOW_B)

		a6 = ejes.plot(lambda x: (x-1) - (x-1)**2/2 + (x-1)**3/3 - (x-1)**4/4 + (x-1)**5/5 - (x-1)**6/6, x_range = [0.1, 5], color = ORANGE)
		p6 = Dot().move_to(ejes.input_to_graph_point(x = 1.8, graph = a6)).set_color(YELLOW).scale(1)
		b6 = Brace(taylor[2:13]).set_color(YELLOW_B)

		a7 = ejes.plot(lambda x: (x-1) - (x-1)**2/2 + (x-1)**3/3 - (x-1)**4/4 + (x-1)**5/5 - (x-1)**6/6 + (x-1)**7/7, x_range = [0.1, 5], color = ORANGE)
		p7 = Dot().move_to(ejes.input_to_graph_point(x = 1.8, graph = a7)).set_color(YELLOW).scale(1)
		b7 = Brace(taylor[2:15]).set_color(YELLOW_B)

		self.play(Create(a1), GrowFromCenter(p1), GrowFromCenter(b1), run_time = 2)
		self.wait(2)
		self.play(ReplacementTransform(a1, a2), ReplacementTransform(p1, p2), ReplacementTransform(b1, b2))
		self.wait()
		self.play(ReplacementTransform(a2, a3), ReplacementTransform(p2, p3), ReplacementTransform(b2, b3))
		self.wait()
		self.play(ReplacementTransform(a3, a4), ReplacementTransform(p3, p4), ReplacementTransform(b3, b4))
		self.wait()
		self.play(ReplacementTransform(a4, a5), ReplacementTransform(p4, p5), ReplacementTransform(b4, b5))
		self.wait()
		self.play(ReplacementTransform(a5, a6), ReplacementTransform(p5, p6), ReplacementTransform(b5, b6))
		self.wait()
		self.play(ReplacementTransform(a6, a7), ReplacementTransform(p6, p7), ReplacementTransform(b6, b7))
		self.wait()
		self.play(FadeOut(a7), FadeOut(b7), FadeOut(p7))
		self.wait(2)

		punto_ref2 = Dot().move_to(ejes.input_to_graph_point(x = 2.5, graph = f_exp)).set_color(YELLOW)
		linea_vertical2 = ejes.get_vertical_line(ejes.input_to_graph_point(x = 2.5, graph = f_exp)).set_color(YELLOW_B)

		self.play(ReplacementTransform(punto_ref, punto_ref2), ReplacementTransform(linea_vertical, linea_vertical2), run_time = 2)
		self.wait(2)


		##aproximaciones de taylor

		a11 = ejes.plot(lambda x: (x-1), x_range = [0.1, 5], color = ORANGE)
		p11 = Dot().move_to(ejes.input_to_graph_point(x = 2.5, graph = a11)).set_color(YELLOW).scale(1)
		b11 = Brace(taylor[2]).set_color(YELLOW_B)		

		a22 = ejes.plot(lambda x: (x-1) - (x-1)**2/2, x_range = [0.1, 5], color = ORANGE)
		p22 = Dot().move_to(ejes.input_to_graph_point(x = 2.5, graph = a22)).set_color(YELLOW).scale(1)
		b22 = Brace(taylor[2:5]).set_color(YELLOW_B)
		
		a33 = ejes.plot(lambda x: (x-1) - (x-1)**2/2 + (x-1)**3/3, x_range = [0.1, 5], color = ORANGE)
		p33 = Dot().move_to(ejes.input_to_graph_point(x = 2.5, graph = a33)).set_color(YELLOW).scale(1)
		b33 = Brace(taylor[2:7]).set_color(YELLOW_B)
		
		a44 = ejes.plot(lambda x: (x-1) - (x-1)**2/2 + (x-1)**3/3 - (x-1)**4/4, x_range = [0.1, 5], color = ORANGE)
		p44 = Dot().move_to(ejes.input_to_graph_point(x = 2.5, graph = a44)).set_color(YELLOW).scale(1)
		b44 = Brace(taylor[2:9]).set_color(YELLOW_B)
		
		a55 = ejes.plot(lambda x: (x-1) - (x-1)**2/2 + (x-1)**3/3 - (x-1)**4/4 + (x-1)**5/5, x_range = [0.1, 5], color = ORANGE)
		p55 = Dot().move_to(ejes.input_to_graph_point(x = 2.5, graph = a55)).set_color(YELLOW).scale(1)
		b55 = Brace(taylor[2:11]).set_color(YELLOW_B)

		a66 = ejes.plot(lambda x: (x-1) - (x-1)**2/2 + (x-1)**3/3 - (x-1)**4/4 + (x-1)**5/5 - (x-1)**6/6, x_range = [0.1, 5], color = ORANGE)
		p66 = Dot().move_to(ejes.input_to_graph_point(x = 2.5, graph = a66)).set_color(YELLOW).scale(1)
		b66 = Brace(taylor[2:13]).set_color(YELLOW_B)

		a77 = ejes.plot(lambda x: (x-1) - (x-1)**2/2 + (x-1)**3/3 - (x-1)**4/4 + (x-1)**5/5 - (x-1)**6/6 + (x-1)**7/7, x_range = [0.1, 5], color = ORANGE)
		p77 = Dot().move_to(ejes.input_to_graph_point(x = 2.5, graph = a77)).set_color(YELLOW).scale(1)
		b77 = Brace(taylor[2:15]).set_color(YELLOW_B)

		a88 = ejes.plot(lambda x: (x-1) - (x-1)**2/2 + (x-1)**3/3 - (x-1)**4/4 + (x-1)**5/5 - (x-1)**6/6 + (x-1)**7/7 -(x-1)**8/8, x_range = [0.1, 5], color = ORANGE)
		p88 = Dot().move_to(ejes.input_to_graph_point(x = 2.5, graph = a88)).set_color(YELLOW).scale(1)
		b88 = Brace(taylor[2:15]).set_color(YELLOW_B)

		a99 = ejes.plot(lambda x: (x-1) - (x-1)**2/2 + (x-1)**3/3 - (x-1)**4/4 + (x-1)**5/5 - (x-1)**6/6 + (x-1)**7/7 -(x-1)**8/8 + (x-1)**9/9, x_range = [0.1, 5], color = ORANGE)
		p99 = Dot().move_to(ejes.input_to_graph_point(x = 2.5, graph = a99)).set_color(YELLOW).scale(1)
		b99 = Brace(taylor[2:15]).set_color(YELLOW_B)

		self.play(Create(a11), GrowFromCenter(p11), GrowFromCenter(b11), run_time = 2)
		self.wait(2)
		self.play(ReplacementTransform(a11, a22), ReplacementTransform(p11, p22), ReplacementTransform(b11, b22))
		self.wait()
		self.play(ReplacementTransform(a22, a33), ReplacementTransform(p22, p33), ReplacementTransform(b22, b33))
		self.wait()
		self.play(ReplacementTransform(a33, a44), ReplacementTransform(p33, p44), ReplacementTransform(b33, b44))
		self.wait()
		self.play(ReplacementTransform(a44, a55), ReplacementTransform(p44, p55), ReplacementTransform(b44, b55))
		self.wait()
		self.play(ReplacementTransform(a55, a66), ReplacementTransform(p55, p66), ReplacementTransform(b55, b66))
		self.wait()
		self.play(ReplacementTransform(a66, a77), ReplacementTransform(p66, p77), ReplacementTransform(b66, b77))
		self.wait()
		#self.play(ReplacementTransform(a77, a88), ReplacementTransform(p77, p88), ReplacementTransform(b66, b77))
		#self.wait()
		#self.play(ReplacementTransform(a88, a99), ReplacementTransform(p88, p99), ReplacementTransform(b88, b99))
		self.wait()

		cajafeliz = SurroundingRectangle(taylor2)

		self.play(*[ReplacementTransform(taylor[i], taylor2[i]) for i in range(0, 17)], run_time = 2)
		self.wait(2)

		diverge = Tex("Diverge").scale(0.8).next_to(p77, RIGHT, buff = 1.2)

		flecha = Arrow(diverge.get_left(), p77.get_center())

		self.play(GrowArrow(flecha), Write(diverge), run_time = 2)
		self.wait(2)

		radio = Line(ejes.c2p(1, 0), ejes.c2p(2, 0)).set_color(YELLOW)
		radio.set_stroke(color = YELLOW, width = 10)

		llave_radio = Brace(radio, direction = DOWN).set_color(RED)
		etiqueta = llave_radio.get_text("Radio de convergencia").scale(0.8).shift(0.2*UP)

		self.play(Create(radio), GrowFromCenter(llave_radio), run_time = 2)
		self.wait(2)
		self.play(Write(etiqueta), run_time = 2)
		self.wait(2)


class t7(Scene):
	def construct(self):

		ejes = Axes(x_range = [-0.5, 5, 1],
			        y_range = [-1, 5, 1],
			        x_length = 7,
			        y_length = 8,
			        tips = False).scale(0.65).set_color(RED_C).to_edge(LEFT).shift(0.5*LEFT)

		f1 = ejes.plot(lambda x: 0.03*np.exp(x) + 1, x_range = [-1, 4.4], color = DARK_BLUE)
		f1_label = MathTex("f(x)").next_to(ejes.c2p(4.3, f1.underlying_function(4.3)), LEFT, buff = 0.25).scale(0.8)

		faprox = ejes.plot(lambda x: 1.22 + 0.22*(x - 2) + 0.11*(x-2)**2, x_range = [-1, 4.4], color = TEAL_E)
		faprox_lab = MathTex("P(x)").scale(0.8).next_to(ejes.c2p(4, faprox.underlying_function(4)), DOWN, buff = 0.3)

		puntoa = Dot().move_to(ejes.c2p(2, f1.underlying_function(2))).set_color(YELLOW)
		lineasa = ejes.get_lines_to_point(ejes.c2p(2, f1.underlying_function(2))).set_color(YELLOW_B)
		lab_a = MathTex("a").scale(0.8).next_to(ejes.c2p(2, 0), DOWN, buff = 0.2)

		self.play(Create(ejes), run_time = 2)
		self.wait(2)
		self.play(Write(f1_label), Create(f1), run_time = 2)
		self.wait(2)
		self.play(GrowFromCenter(puntoa), Create(lineasa), Write(lab_a), run_time = 2)
		self.wait(2)
		self.play(Create(faprox), Write(faprox_lab), run_time = 2)
		self.wait(2)

		px = MathTex("P(x)", "=", "a_0", "+", "a_1", "(x-a)", "+", "a_2", "(x-a)^2", "+", "a_3", "(x-a)^3", "+", "\\ldots", "+", "a_n"," (x-a)^n").scale(0.55).to_corner(UR).shift(0.3*LEFT)
		###            0      1     2     3     4       5      6     7         8      9     10       11      12      13     14       15      16

		px1 = MathTex("P'(x) = a_1 + 2a_2(x-a) + 3a_3(x-a)^2 + 4a_4(x-a)^3 + \\ldots + n a_n (x-a)^{n-1}").scale(0.55).next_to(px, DOWN, buff = 0.3)

		px2 = MathTex("P''(x) = 2a_2 + 2.3 a_3(x-a) + 3.4a_4(x-a)^2 + \\ldots + n(n-1) a_n(x-a)^{n-2}").scale(0.55).next_to(px1, DOWN, buff = 0.3)

		px3 = MathTex("P'''(x) =  1.2.3a_3 + 2.3.4a_4(x-a) + \\ldots + n(n-1)(n-2)a_n(x-a)^{n-3}").scale(0.55).next_to(px2, DOWN, buff = 0.3)

		self.play(ReplacementTransform(faprox_lab[0].copy(), px[0]),
			      GrowFromCenter(px[1]), Write(px[2:17]), run_time = 2)
		self.wait(2)
		self.play(Write(px1), run_time = 2)
		self.wait(2)
		self.play(Write(px2), run_time = 2)
		self.wait(2)
		self.play(Write(px3), run_time = 2)
		self.wait(2)

		c1 = MathTex("P(a)", "=", "f(a)").scale(0.55).shift(0.5*UP + 1.5*LEFT)
		n1 = MathTex("a_0", "=", "f(a)").scale(0.55).next_to(c1, DOWN, buff = 0.3)
		##3            0     1     2

		c2 = MathTex("P'(a)", "=", "f'(a)").scale(0.55).next_to(c1, RIGHT, buff = 0.8)
		n2 = MathTex("a_1", "=", "f'(a)").scale(0.55).next_to(c2, DOWN, buff = 0.3)

		c3 = MathTex("P''(a)", "=", "f''(a)").scale(0.55).next_to(c2, RIGHT, buff = 0.8)
		n3 = MathTex("2a_2", "=", "f''(a)").scale(0.55).next_to(c3, DOWN, buff = 0.3)
		n32 = MathTex("a_2", "=", "\\frac{f''(a)}{2!}").scale(0.55).next_to(n3, DOWN, buff = 0.3)

		c4 = MathTex("P'''(a)", "=", "f'''(a)").scale(0.55).next_to(c3, RIGHT, buff = 0.8)
		n4 = MathTex("1.2.3a_3", "=", "f'''(a)").scale(0.55).next_to(c4, DOWN, buff = 0.3)
		n42 = MathTex("a_3", "=", "\\frac{f'''(a)}{3!}").scale(0.55).next_to(n4, DOWN, buff = 0.3)


		self.play(Write(c1), Write(c2), Write(c3), Write(c4), run_time = 2)
		self.wait(2)

		caja1 = SurroundingRectangle(px)
		caja2 = SurroundingRectangle(px1)
		caja3 = SurroundingRectangle(px2)
		caja4 = SurroundingRectangle(px3)

		##primero

		self.play(Create(caja1), run_time = 2)
		self.wait(2)
		self.play(Write(n1[0]), ReplacementTransform(c1[1].copy(), n1[1]),
			      ReplacementTransform(c1[2].copy(), n1[2]), run_time = 2)
		self.wait(2)

		##segundo
		self.play(ReplacementTransform(caja1, caja2), run_time = 2)
		self.wait(2)
		self.play(Write(n2[0]), ReplacementTransform(c2[1].copy(), n2[1]),
			      ReplacementTransform(c2[2].copy(), n2[2]), run_time = 2)
		self.wait(2)

		##tercero
		self.play(ReplacementTransform(caja2, caja3), run_time = 2)
		self.wait(2)
		self.play(Write(n3[0]), ReplacementTransform(c3[1].copy(), n3[1]),
			      ReplacementTransform(c3[2].copy(), n3[2]), run_time = 2)
		self.wait(2) 
		self.play(Write(n32), run_time = 2)
		self.wait(2)

		##cuarto

		##tercero
		self.play(ReplacementTransform(caja3, caja4), run_time = 2)
		self.wait(2)
		self.play(Write(n4[0]), ReplacementTransform(c4[1].copy(), n4[1]),
			      ReplacementTransform(c4[2].copy(), n4[2]), run_time = 2)
		self.wait(2) 
		self.play(Write(n42), run_time = 2)
		self.wait(2)
		self.play(FadeOut(px1), FadeOut(px2), FadeOut(px3),
			      FadeOut(caja4), run_time = 2)
		self.wait(2)

		#px = MathTex("P(x)", "=", "a_0", "+", "a_1", "(x-a)", "+", "a_2", "(x-a)^2", "+", "a_3", "(x-a)^3", "+", "\\ldots", "+", "a_n", "(x-a)^n").scale(0.55).to_corner(UR).shift(0.3*LEFT)
		###            0      1     2     3     4       5      6     7         8      9     10       11      12      13     14       15     16

		taylor_p = MathTex("P(x)", "=", "f(a)", "+", "{f'(a)", "\\over", "1!}", "(x-a)", "+", "\\frac{f''(a)}{2!}" , "(x-a)^2", "+", "\\frac{f'''(a)}{3!}", "(x-a)^3", "+", "\\ldots", "+" , "\\frac{f^{(n)}(a)}{n!}", "(x-a)^n").scale(0.55).next_to(px, DOWN, buff = 0.3).shift(0.5*LEFT)
		##########3          0      1     2      3       4        5        6       7      8               9             10       11            12              13       14       15     16              17                18

		self.play(ReplacementTransform(px[0].copy(), taylor_p[0]), ReplacementTransform(px[1].copy(), taylor_p[1]), run_time = 2)
		self.wait(2)
		self.play(FocusOn(px[2]))
		self.wait(2)
		self.play(ReplacementTransform(n1[2].copy(), taylor_p[2]), run_time = 2)
		self.wait(2)
		self.play(ReplacementTransform(px[3].copy(), taylor_p[3]), run_time = 2)
		self.wait(2)
		self.play(FocusOn(px[4]))
		self.wait(2)
		self.play(ReplacementTransform(n2[2].copy(), taylor_p[4]), ReplacementTransform(px[5].copy(), taylor_p[7]),
			      GrowFromCenter(taylor_p[5]), Write(taylor_p[6]), run_time = 2)
		
		self.wait(2)

		self.play(ReplacementTransform(px[6].copy(), taylor_p[8]), run_time = 2)

		self.play(FocusOn(px[7]))
		self.wait(2)
		self.play(ReplacementTransform(n32[2].copy(), taylor_p[9]), ReplacementTransform(px[8].copy(), taylor_p[10]),
			      run_time = 2)
		
		self.wait(2)

		self.play(ReplacementTransform(px[9].copy(), taylor_p[11]), run_time = 2)

		self.play(FocusOn(px[10]))
		self.wait(2)
		self.play(ReplacementTransform(n42[2].copy(), taylor_p[12]), ReplacementTransform(px[11].copy(), taylor_p[13]),
			      run_time = 2)
		self.wait(2)

		self.play(ReplacementTransform(px[12].copy(), taylor_p[14]),
			      ReplacementTransform(px[13].copy(), taylor_p[15]),
			      ReplacementTransform(px[14].copy(), taylor_p[16]), run_time = 2)
		self.wait(2)
		self.play(FocusOn(px[15]))
		self.wait(2)
		self.play(Write(taylor_p[15]), ReplacementTransform(px[16].copy(), taylor_p[18]), Write(taylor_p[17]), run_time = 2)
		self.wait(2)

		caja = SurroundingRectangle(taylor_p)
		poli = Tex("Polinomio de Taylor").scale(0.8).next_to(caja, DOWN, buff = 0.2)

		self.play(Create(caja), Write(poli), FadeOut(c1), FadeOut(n1), FadeOut(c2), FadeOut(n2), FadeOut(c3), FadeOut(n3), FadeOut(n32), FadeOut(c4), FadeOut(n4), FadeOut(n42), run_time = 2)
		self.wait(2)


class resumen(Scene):
	def construct(self):

		titu1 = Title("Polinomio de Taylor").set_color(YELLOW_B)

		t1 = Tex("Un polinomio de Taylor es un polinomio que se utiliza para\\\\\\\
			      aproximar una función en un punto dado. Dada una función $f(x)$\\\\\\\
			      y un punto $a$, el polinomio de Taylor de grado $n$ centrado en\\\\\\\
			      $a$ se denota por $P_n(x)$ y se expresa de la siguiente manera:").scale(0.8).next_to(titu1, DOWN, buff = 0.6)

		p1 = MathTex("P_n(x) = f(a) + \\frac{f'(a)}{1!}(x-a) + \\frac{f''(a)}{2!}(x-a)^2 + \\frac{f'''(a)}{3!}(x-a)^3 + \\ldots + \\frac{f^{n}(a)}{n!}(x-a)^n").scale(0.7).next_to(t1, DOWN, buff = 0.8)
		caja = SurroundingRectangle(p1)

		self.play(Write(titu1), run_time = 2)
		self.wait(2)
		self.play(Write(t1), run_time = 2)
		self.wait(2)
		self.play(Write(p1), Create(caja), run_time = 2)
		self.wait(2)


class resumen2(Scene):
	def construct(self):

		titu1 = Title("Serie de Taylor").set_color(YELLOW_B)

		t1 = Tex("La serie de Taylor de una función $f(x)$ es la suma infinita de\\\\\\\
			      los términos de su expansión en polinomios de Taylor. Se denota por").scale(0.8).next_to(titu1, DOWN, buff = 0.6)

		p1 = MathTex("f(x) = f(a) + \\frac{f'(a)}{1!}(x-a) + \\frac{f''(a)}{2!}(x-a)^2 + \\frac{f'''(a)}{3!}(x-a)^3 + \\ldots").scale(0.8).next_to(t1, DOWN, buff = 0.8)
		caja = SurroundingRectangle(p1)

		t2 = Tex("La convergencia de la serie de Taylor a la función original depende\\\\\\\
			      de las propiedades de la función y del punto en el que esta centrado.\\\\\\\
			      En particular, si $a = 0$, la serie se llama: serie de Maclaurin.").scale(0.8).next_to(p1, DOWN, buff = 0.6)
		t3 = Tex("")

		self.play(Write(titu1), run_time = 2)
		self.wait(2)
		self.play(Write(t1), run_time = 2)
		self.wait(2)
		self.play(Write(p1), Create(caja), run_time = 2)
		self.wait(2)
		self.play(Write(t2), run_time = 2)
		self.wait(2)

class ejm(Scene):
	def construct(self):

		t1 = Tex("$e^x = 1 + x + \\frac{x^2}{2!} + \\frac{x^3}{3!} + \\frac{x^4}{4!} + \\ldots$\\ para toda $x$").shift(2.8*UP)

		t2 = Tex("$senx = x - \\frac{x^3}{3!} + \\frac{x^5}{5!} - \\frac{x^7}{7!} + \\ldots$\\ para toda $x$").next_to(t1, DOWN, buff = 0.5)

		t3 = Tex("$cosx = 1 - \\frac{x^2}{2!} + \\frac{x^4}{4!} - \\frac{x^6}{6!} + \\ldots$\\ para toda $x$").next_to(t2, DOWN, buff = 0.5)

		t4 = Tex("$\\ln(1+x) = x - \\frac{x^2}{2} + \\frac{x^3}{3} - \\frac{x^4}{4} + \\ldots$\\ para $|x| < 1$").next_to(t3, DOWN, buff = 0.5)

		t5 = Tex("$tan^{-1}x = x - \\frac{x^3}{3} + \\frac{x^5}{5} - \\frac{x^7}{7} + \\ldots$\\ para $|x| < 1$").next_to(t4, DOWN, buff = 0.5)

		self.play(Write(t1), Write(t2), Write(t3), Write(t4), Write(t5), run_time = 2)
		self.wait(2)








class t8(Scene):
	def construct(self):

		ejes = Axes(x_range = [-2*PI, 2*PI, PI/2],
			        y_range = [-2, 2, 1],
			        x_length = 12,
			        y_length = 7,
			        tips = False).set_color(RED_C).to_edge(LEFT).shift(DOWN)
		label = ejes.get_axis_labels(MathTex("x"), MathTex("y"))


		seno = ejes.plot(lambda x: np.sin(x), x_range = [-2*PI, 2*PI], color = TEAL_E)

		a = ValueTracker(0)

		seno_aprox = always_redraw(
			lambda: ejes.plot(lambda x: (x - a.get_value()) - ((x - a.get_value())**3/6) + ((x - a.get_value())**5/120) - ((x - a.get_value())**7/5040) + ((x - a.get_value())**9/362880), x_range = [-2*PI, 2*PI], color = BLUE_D))

		punto = always_redraw(
			lambda: Dot().set_color(YELLOW).move_to(ejes.c2p(a.get_value(), seno.underlying_function(a.get_value()))))

		lineas = always_redraw(
			lambda: ejes.get_lines_to_point(ejes.c2p(a.get_value(), seno.underlying_function(a.get_value()))).set_color(YELLOW_B))

		#seno_aprox = ejes.plot(lambda x: x - (x**3/6) + (x**5/120) - (x**7/5040) + (x**9/362880) - (x**(11)/39916800) + (x**(13)/math.factorial(13)) - (x**(15)/math.factorial(15)) + (x**(17)/math.factorial(17)), x_range = [-2*PI, 2*PI], color = BLUE_D)

		self.play(Create(ejes), Write(label), run_time = 2)
		self.wait(2)
		self.play(Create(seno), run_time = 2)
		self.wait(2)
		self.play(Create(seno_aprox), Create(lineas), GrowFromCenter(punto), run_time = 2)
		self.wait(2)
		self.play(a.animate.set_value(PI/2), run_time = 6)
		self.wait(2)


		#seno_aprox = always_redraw(
		#	lambda: ejes.plot(lambda x: (x - a.get_value()) - ((x - a.get_value())**3/6) + ((x - a.get_value())**5/120) - ((x - a.get_value())**7/5040) + ((x - a.get_value())**9/362880) - ((x - a.get_value())**(11)/39916800) + ((x - a.get_value())**(13)/math.factorial(13)) - ((x - a.get_value())**(15)/math.factorial(15)) + ((x - a.get_value())**(17)/math.factorial(17)), x_range = [-2*PI, 2*PI], color = BLUE_D))







###OTROS

###ANIMACIONES


class pendulo(Scene):
	def construct(self):

		ejes = Axes()

		##parametros

		l = 3

		g = 9.8

		theta_max = 10

		w = np.sqrt(g/l)

		T = 2*PI/w


		t = ValueTracker(0)

		plano = NumberPlane().add_coordinates()

		techo = Line([-5, 3, 0], [-2, 3, 0]).set_color(TEAL_E)

		cuerda = Line(techo.get_center(), techo.get_center() + l*DOWN).set_color(ORANGE)
		cuerda.set_length(l)

		bola = Circle(
			stroke_width = 1,
			stroke_color = WHITE,
			fill_color = GREY,
			fill_opacity = 1,
			sheen_factor = 1,
			sheen_direction = UL,
			radius = 0.25).move_to(cuerda.get_end())

		self.play(Create(cuerda), Create(techo), DrawBorderThenFill(bola), run_time = 2)

		pendulo = VGroup(cuerda, bola)

		self.wait(2)
		self.play(pendulo.animate.rotate(10*DEGREES, about_point = techo.get_center()),
			      run_time = 2)
		self.wait(2)

		pendulo.add_updater(
			lambda m: m.rotate(-1.1*np.cos(w*t.get_value())*DEGREES, about_point = techo.get_center()))
	
		
		self.play(t.animate.set_value(3*T), rate_func = linear, run_time = 3*T )
		self.wait(2)