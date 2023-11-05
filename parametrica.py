class parametrica(Scene):
    def construct(self):

    	#Curva parametrica: x = x(t)
    	#  y = y(t)
    	# z = z(t)
    	#lambda t: np.array([x(t), y(t), 0])

        ejes = Axes(x_range = [-6, 6, 1],
        	        y_range = [-4, 4, 1],
        	        x_length = 8,
        	        y_length = 7)

        cardiode = ejes.plot_parametric_curve(
            lambda t: np.array(
                [np.exp(1) * np.cos(t) * (1 - np.cos(t)),
                 np.exp(1) * np.sin(t) * (1 - np.cos(t)),
                 0]),
            t_range = [0, 2*PI],
            color= BLUE)

        self.play(Create(ejes), run_time = 2)
        self.wait(2)
        self.play(Create(cardiode), run_time = 4)
        self.wait(2)







class parametrica2(Scene):
    def construct(self):
        ejes = PolarPlane()
        cardiode = ejes.plot_parametric_curve(
            lambda t: np.array(
                [np.exp(1) * np.cos(t) * (1 - np.cos(t)),
                 np.exp(1) * np.sin(t) * (1 - np.cos(t)),
                 0]),
            t_range=[0, 2 * PI],
            color= BLUE)

        self.play(Create(ejes), run_time = 2)
        self.wait(2)
        self.play(Create(cardiode), run_time = 4)
        self.wait(2)






class parametrica3(Scene):
    def construct(self):

        ejes = Axes(x_range = [-3, 3, 1],
        	        y_range = [-3, 3, 1],
        	        x_length = 7,
        	        y_length = 7)

        curva = ejes.plot_parametric_curve(
            lambda t: np.array(
                [np.sin(t)+0.5*np.cos(5*t)+0.25*np.sin(13*t),
                 np.cos(t)+0.5*np.sin(5*t)+0.25*np.cos(13*t),
                 0]),
            t_range=[0, 2 * PI],
            color= BLUE)

        self.play(Create(ejes), run_time = 2)
        self.wait(2)
        self.play(Create(curva), run_time = 4)
        self.wait(2)

##Sin ejes

class parametrica4(Scene):
    def construct(self):

        curva = ParametricFunction(
            lambda t: np.array(
                [np.sin(t)+0.5*np.cos(5*t)+0.25*np.sin(13*t),
                 np.cos(t)+0.5*np.sin(5*t)+0.25*np.cos(13*t),
                 0]),
            t_range=[0, 2 * PI],
            color= BLUE)

        self.play(Create(curva), run_time = 4)
        self.wait(2)



class mariposa(Scene):
    def construct(self):

        curva = ParametricFunction(
            lambda t: np.array(
                [np.sin(t)*(np.exp(np.cos(t))-2*np.cos(4*t)-np.sin(t/12)**5),
                 np.cos(t)*(np.exp(np.cos(t))-2*np.cos(4*t)-np.sin(t/12)**5),
                 0]),
            t_range=[0, 12*PI],
            color= [YELLOW, RED, BLUE])

        eq1 = MathTex("x= \\sin(t) (e^{\\cos(t)} - 2\\cos(4t) - \\sin^5(t/12))").scale(0.8).to_edge(LEFT).shift(0.7*UP)

        eq2 = MathTex("y= \\cos(t) (e^{\\cos(t)} - 2\\cos(4t) - \\sin^5(t/12))").scale(0.8).next_to(eq1, DOWN, buff = 0.4).to_edge(LEFT)


        curva.to_edge(RIGHT)

        self.play(Write(eq1), Write(eq2), run_time = 2)
        self.wait(2)

        self.play(Create(curva), run_time = 6)
        self.wait(2)
