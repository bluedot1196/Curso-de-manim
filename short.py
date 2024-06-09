tmp_pixel_height = config.pixel_height
config.pixel_height = config.pixel_width
config.pixel_width = tmp_pixel_height

config.frame_height = config.frame_height / SCALE_FACTOR
config.frame_width = config.frame_height * 9 / 16
FRAME_HEIGHT = config.frame_height
FRAME_WIDTH = config.frame_width


class t1(Scene):
	def setup(self, add_border = False):
		if add_border:
			self.border = Rectangle(
				width = FRAME_WIDTH,
				height = FRAME_HEIGHT,
				color = RED
			)
			self.add(self.border)

	def construct(self):   
