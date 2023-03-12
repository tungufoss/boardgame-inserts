import drawsvg as draw
import math


class tuckbox:
    def __init__(self, name, cards=52, height_mm=89, width_mm=64,
                 cardwidth_mm=0.24, margin_mm=2, dpi=96):
        self.name = name
        self.dpi = dpi
        dpmm = dpi / 25.4
        self.height = height_mm * dpmm
        self.width = width_mm * dpmm
        depth_mm = max(5, math.ceil(cards * cardwidth_mm))
        self.depth = depth_mm * dpmm
        self.margin = margin_mm * dpmm
        self.tuckmargin = 18 * dpmm
        self.tuckcut = self.tuckmargin / 2
        self.gluedepth = min(15, depth_mm - margin_mm) * dpmm
        self.dustdepth = (self.tuckmargin + self.depth) / 2

        image_width = self.width * 2 + self.depth * 2 + self.gluedepth
        image_height = self.height + self.depth * 2 + self.tuckmargin * 3
        height_in = image_height / dpmm / 25.4
        width_in = image_width / dpmm / 25.4

        print(
            f'{name}:\tTuckbox of size {height_mm}mm x {width_mm}mm x '
            f'{depth_mm}mm, #{cards} cards\t(bounding box: {width_in:.2f}" x '
            f'{height_in:.2f}")')
        self.scorecolor = 'red'
        self.img = draw.Drawing(image_width, image_height, displayInline=False)

    def draw(self):
        """
        This code draws a polygon using the drawSvg library in Python. The
        polygon being drawn is a tuck box, which is a type of box that is
        closed using tuck flaps that are inserted into slots in the sides of
        the box.

        The code sets the starting position of the polygon by defining the x and
        y coordinates of the first point as self.x0 and self.y0. The polygon is
        then drawn using a series of move (M), line (L), and curve (C) commands.
        Each point in the polygon is given a label such as p6 or p17 to help
        keep track of its position.

        The code includes several variables such as self.depth, self.width, and
        self.margin, which control the size and shape of the box. The tuck flaps
        are also included in the polygon using variables such as self.tuckcut
        and self.tuckmargin.
        """
        # Set the initial x and y coordinates for drawing the tuck box
        self.x0, self.y0 = 0, self.depth + self.tuckmargin * 1.5

        # Create a new path object for drawing the tuck box
        p = draw.Path(id="cut-tuckbox", stroke_width=3, stroke='black',
                      fill='white')

        # Calculate the starting coordinates for the first segment of the path
        x = self.x0 + self.depth
        y = self.y0 + self.height

        # Start drawing the path
        # MOVE to (x + self.tuckcut, y + self.margin)
        p.M(x + self.tuckcut, y + self.margin)

        # Draw a LINE to (x + self.tuckcut, y)
        p.L(x + self.tuckcut, y)

        # Draw a LINE to (x, y)
        p.L(x, y)  # p6

        # Draw a LINE to (x, y + self.depth)
        y += self.depth
        p.L(x, y)  # p7

        # Record the current x-coordinate
        x0 = x

        # Move the current x-coordinate to the right by self.width
        x += self.width

        # Draw a CURVE to (x, y) using the control points (x0 + self.tuckmargin, y + self.tuckmargin * 2) and
        # (x - self.tuckmargin, y + self.tuckmargin * 2)
        p.C(x0 + self.tuckmargin, y + self.tuckmargin * 2, x - self.tuckmargin,
            y + self.tuckmargin * 2, x, y)  # p8 # FRONT CURVE

        # Draw a LINE to (x, y - self.depth)
        y -= self.depth
        p.L(x, y)  # p9

        # Draw a LINE to (x - self.tuckcut, y)
        p.L(x - self.tuckcut, y)

        # Draw a LINE to (x - self.tuckcut, y + self.margin)
        p.L(x - self.tuckcut, y + self.margin)

        # Move the y-coordinate down by self.dustdepth
        y += self.dustdepth

        # MOVE to (x, y - missing) if self.dustdepth > self.depth
        # Otherwise, MOVE to (x, y)
        if self.dustdepth > self.depth:
            missing = self.dustdepth - self.depth
            p.M(x, y - missing)
            p.L(x, y)
        else:
            p.M(x, y)  # p10

        # Move the current x-coordinate to the left by (self.depth - 2 * self.margin)
        x += (self.depth - 2 * self.margin)

        # Draw a LINE to (x, y)
        p.L(x, y)  # p11

        # Move the current x-coordinate to the left by self.margin
        x += self.margin

        # Move the current y-coordinate down by (self.dustdepth * 2 / 3)
        y -= self.dustdepth * 2 / 3

        # Draw a LINE to (x, y)
        p.L(x, y)  # p12

        # Move the current x-coordinate to the left by self.margin
        x += self.margin

        # Move the current y-coordinate down by (self.dustdepth * 1 / 3)
        y -= self.dustdepth * 1 / 3

        # Draw a LINE to (x, y)
        p.L(x, y)  # p13

        # Move the current x-coordinate to the left by ((self.width -
        # self.tuckmargin) / 2)
        x += (self.width - self.tuckmargin) / 2

        # Draw a LINE to (x,y)
        p.L(x, y)  # p14

        # Shift the x-coordinate by the tuck margin
        x += self.tuckmargin

        # Draw a mirrored curve with control point (3,3) at (x,y)
        p.A(3, 3, 0, 0, 1, x, y)  # p15 MIRRORED CURVE

        # Shift the x-coordinate by half the width minus the tuck margin
        x += (self.width - self.tuckmargin) / 2

        # Draw a line from the current position to (x,y - margin)
        p.L(x, y)  # p16
        y -= self.margin

        # Draw a line from the current position to (x, y - 2*margin - height)
        p.L(x, y)  # p17

        # Shift the x-coordinate by the glue depth
        x += self.gluedepth

        # Draw a line from the current position to (x, y - 3*margin - height)
        y -= self.margin
        p.L(x, y)  # p18

        # Draw a line from the current position to (x, y - 3*margin - height - depth)
        y -= (self.height - 4 * self.margin)
        p.L(x, y)  # p19

        # Shift the x-coordinate by negative glue depth
        y -= self.margin
        x -= self.gluedepth

        # Draw a line from the current position to (x - width, y - 3*margin - height - depth)
        p.L(x, y)  # p20

        # Draw a line from the current position to (x - width, y - 4*margin - height - depth)
        y -= self.margin
        p.L(x, y)  # p21

        # Shift the x-coordinate by negative width
        x -= self.width

        # Draw a line from the current position to (x - margin, y - 4*margin - height - depth - dust depth * 1/3)
        p.L(x, y)  # p22
        x -= self.margin
        y -= self.dustdepth * 1 / 3

        # Draw a line from the current position to (x - margin, y - 4*margin - height - depth - dust depth * 3/3)
        p.L(x, y)  # p23
        x -= self.margin
        y -= self.dustdepth * 2 / 3

        # Draw a line from the current position to (x - depth + 2margin, y - 4margin - height - depth - dust depth * 3/3)
        p.L(x, y)  # p24
        x -= (self.depth - 2 * self.margin)
        p.L(x, y)  # p25

        # If the dust depth is greater than the depth, adjust the y-coordinate to make up for the difference
        if self.dustdepth > self.depth:
            missing = self.dustdepth - self.depth
            y += missing
            p.L(x, y)
            y += self.dustdepth - missing
        else:
            y += self.dustdepth

        # Move the current position to (x - tuck cut, y - margin)
        p.M(x - self.tuckcut, y - self.margin)

        # Draw a line from the current position to (x - tuck cut, y)
        p.L(x - self.tuckcut, y)

        # Draw a line from the current position to (x, y)
        p.L(x, y)  # p26

        # Draw a line from the current position to (x, y - depth)
        y -= self.depth
        p.L(x, y)  # p27

        # Store the current x-coordinate as x0, and shift the x-coordinate
        x0 = x
        x -= self.width
        p.C(x0 - self.tuckmargin, y - self.tuckmargin * 1.5, x +
            self.tuckmargin, y - self.tuckmargin * 1.5, x, y)  # p28 # CURVE
        y += self.depth
        p.L(x, y)  # p29
        p.L(x + self.tuckcut, y)
        p.L(x + self.tuckcut, y - self.margin)
        y -= self.dustdepth
        # MOVE
        if self.dustdepth > self.depth:
            missing = self.dustdepth - self.depth
            p.M(x, y + missing)
            p.L(x, y)
        else:
            p.M(x, y)  # p30
        x -= (self.depth - self.margin * 2)
        p.L(x, y)  # p31
        x -= self.margin
        y += self.dustdepth * 2 / 3
        p.L(x, y)  # p32
        x -= self.margin
        y += self.dustdepth * 1 / 3
        p.L(x, y)  # p33        
        y += self.height
        p.L(x, y)  # p2
        x += self.margin
        y += self.dustdepth * 1 / 3
        p.L(x, y)  # p3
        x += self.margin
        y += self.dustdepth * 2 / 3
        p.L(x, y)  # p4
        x += (self.depth - self.margin * 2)
        p.L(x, y)  # p5
        if self.dustdepth > self.depth:
            missing = self.dustdepth - self.depth
            y -= missing
            p.L(x, y)
            y -= self.dustdepth - missing
        else:
            y -= self.dustdepth

        self.img.append(p)

        # Draw score line
        p = draw.Path(id='scoring', stroke_width=1,
                      stroke=self.scorecolor, fill='none', stroke_dasharray=5)
        p.M(self.x0 + (self.width + self.depth) * 2, self.y0 + self.height)
        p.L(self.x0 + (self.width + self.depth) * 2, self.y0)
        p.M(self.x0 + self.width + self.depth * 2, self.y0)
        p.L(self.x0, self.y0)
        p.M(self.x0 + self.depth, self.y0)
        p.L(self.x0 + self.depth, self.y0 + self.height)
        p.M(self.x0 + self.depth, self.y0 + self.height + self.depth)
        p.L(self.x0 + self.depth + self.width,
            self.y0 + self.height + self.depth)
        p.M(self.x0 + self.depth + self.width, self.y0 + self.height)
        p.L(self.x0 + self.depth + self.width, self.y0)
        p.M(self.x0 + self.depth * 2 + self.width, self.y0)
        p.L(self.x0 + self.depth * 2 + self.width, self.y0 + self.height)
        p.L(self.x0, self.y0 + self.height)
        p.M(self.x0 + self.depth, self.y0 - self.depth)
        p.L(self.x0 + self.depth + self.width, self.y0 - self.depth)
        self.img.append(p)

    def addText(self, front="", rear="", top="", bottom="", right="", left="",
                fontcolor="blue", fontsize=12):
        g = draw.Group(id="text")
        g.append(
            draw.Text(bottom, fontsize, self.x0 + self.depth + self.width / 2,
                      self.y0 -
                      self.depth / 2, text_anchor='middle', valign='middle',
                      fill=fontcolor, id="text_bottom"))
        p = draw.Path()
        p.M(self.x0 + self.depth + self.width,
            self.y0 + self.height + self.depth / 2)
        p.L(self.x0 + self.depth, self.y0 + self.height + self.depth / 2)
        g.append(draw.Text(top, fontsize, path=p, text_anchor='middle',
                           valign='middle', fill=fontcolor, id="text_top"))
        p = draw.Path()
        p.M(self.x0 + self.depth / 2, self.y0 + self.height)
        p.L(self.x0 + self.depth / 2, self.y0)
        g.append(draw.Text(right, fontsize, path=p, text_anchor='middle',
                           valign='middle', fill=fontcolor, id="text_right"))
        p = draw.Path()
        p.M(self.x0 + self.depth / 2 + self.depth + self.width, self.y0)
        p.L(self.x0 + self.depth / 2 + self.depth + self.width,
            self.y0 + self.height)
        g.append(draw.Text(left, fontsize, path=p, text_anchor='middle',
                           valign='middle', fill=fontcolor, id="text_left"))
        g.append(
            draw.Text(rear, fontsize, self.x0 + self.depth + self.width / 2,
                      self.y0 +
                      self.height / 2, text_anchor='middle', valign='middle',
                      fill=fontcolor, id="text_rear"))
        g.append(draw.Text(front, fontsize,
                           self.x0 + self.depth * 2 + self.width + self.width / 2,
                           self.y0 +
                           self.height / 2, text_anchor='middle',
                           valign='middle', fill=fontcolor, id="text_front"))
        self.img.append(g)

    def save(self):
        self.img.set_pixel_scale(1)  # Set number of pixels per geometry unit
        self.img.save_svg(self.name + '.svg')
        self.img.save_png(self.name + '.png')


if True:
    tb = tuckbox("sequence_junior", 42 + 5, 89, 59)
    tb.draw()
    tb.addText(left="Sequence junior", right="Sequence junior",
               top="Sequence junior", bottom="Sequence junior")
    tb.save()
if True:
    tb = tuckbox("isle_of_cats_main", cards=150)
    tb.draw()
    tb.addText(front="Isle of Cats:\nDiscovery Cards",
               rear="Isle of Cats:\nDiscovery Cards",
               top="Isle of Cats:\nDiscovery Cards",
               bottom="Isle of Cats:\nDiscovery Cards",
               left="Isle of Cats:\nDiscovery Cards",
               right="Isle of Cats:\nDiscovery Cards",
               fontsize=24)
    tb.save()

    tb = tuckbox("isle_of_cats_family", cards=18)
    tb.draw()
    tb.addText(front="Isle of Cats:\nFamily Cards",
               rear="Isle of Cats:\nFamily Cards",
               top="Isle of Cats: Family Cards",
               bottom="Isle of Cats: Family Cards",
               left="Isle of Cats: Family Cards",
               right="Isle of Cats: Family Cards")
    tb.save()

    tb = tuckbox("isle_of_cats_solo", cards=5 + 23 + 10 + 9 + 4)
    tb.draw()
    tb.addText(front="Isle of Cats:\nSolo Cards",
               rear="Isle of Cats:\nSolo Cards",
               top="Isle of Cats: Solo Cards",
               bottom="Isle of Cats: Solo Cards",
               left="Isle of Cats: Solo Cards",
               right="Isle of Cats: Solo Cards")
    tb.save()

    tb = tuckbox("isle_of_cats_baskets", cards=10, cardwidth_mm=.5)
    tb.draw()
    tb.addText(front="Isle of Cats:\nBasket tokens",
               rear="Isle of Cats:\nBasket tokens",
               top="Isle of Cats: Basket tokens",
               bottom="Isle of Cats: Basket tokens",
               left="Isle of Cats: Basket tokens",
               right="Isle of Cats: Basket tokens")
    tb.save()
