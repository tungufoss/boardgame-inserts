import drawSvg as draw
import math

class tuckbox:
    def __init__(self, name, cards=52, height_mm=89, width_mm=64, cardwidth_mm=0.24, margin_mm=3, dpi=96):
        self.name = name
        self.dpi = dpi
        dpmm = dpi/25.4
        self.height = height_mm*dpmm
        self.width = width_mm*dpmm
        depth_mm = max(5, math.ceil(cards*cardwidth_mm))
        self.depth = depth_mm*dpmm
        if depth_mm == 5:
            margin_mm = 1
        self.margin = margin_mm*dpmm
        self.tuckmargin = 14*dpmm
        self.tuckcut = self.tuckmargin/2
        self.gluedepth = min(15, depth_mm-margin_mm)*dpmm
        self.dustdepth = (self.tuckmargin+self.depth)/2

        print(
            f'{name}:\tTuckbox of size {height_mm}mm x {width_mm}mm x {depth_mm}mm, #{cards} cards')
        image_width = self.width*2+self.depth*2+self.gluedepth
        image_height = self.height+self.depth*2+self.tuckmargin*3
        self.scorecolor = 'red'
        self.img = draw.Drawing(image_width, image_height, displayInline=False)        

    def draw(self):
        self.x0, self.y0 = 0, self.depth+self.tuckmargin*1.5
        # Draw polygon, cut lines
        p = draw.Path(id="cut-tuckbox",
                      stroke_width=3, stroke='black',
                      fill='white')       
        x = self.x0+self.depth
        y = self.y0+self.height
        # MOVE
        p.M(x+self.tuckcut, y+self.margin)
        p.L(x+self.tuckcut, y)
        p.L(x, y)  # p6
        y += self.depth
        p.L(x, y)  # p7
        x0 = x
        x += self.width
        p.C(x0+self.tuckmargin, y+self.tuckmargin*1.5, x -
            self.tuckmargin, y+self.tuckmargin*1.5, x, y)  # p8 # CURVE
        y -= self.depth
        p.L(x, y)  # p9
        p.L(x-self.tuckcut, y)
        p.L(x-self.tuckcut, y+self.margin)
        y += self.dustdepth
        # MOVE
        if self.dustdepth > self.depth:
            missing = self.dustdepth-self.depth
            p.M(x, y-missing)
            p.L(x, y)
        else:
            p.M(x, y)  # p10
        x += (self.depth - 2*self.margin)
        p.L(x, y)  # p11
        x += self.margin
        y -= self.dustdepth*2/3
        p.L(x, y)  # p12
        x += self.margin
        y -= self.dustdepth*1/3
        p.L(x, y)  # p13
        x += (self.width-self.tuckmargin)/2
        p.L(x, y)  # p14
        x += self.tuckmargin
        p.A(3, 3, 10, 1, 0, x, y)  # p15 # CURVE
        x += (self.width-self.tuckmargin)/2
        p.L(x, y)  # p16
        y -= self.margin
        p.L(x, y)  # p17
        x += self.gluedepth
        y -= self.margin
        p.L(x, y)  # p18
        y -= (self.height - 4*self.margin)
        p.L(x, y)  # p19
        y -= self.margin
        x -= self.gluedepth
        p.L(x, y)  # p20
        y -= self.margin
        p.L(x, y)  # p21
        x -= self.width
        p.L(x, y)  # p22
        x -= self.margin
        y -= self.dustdepth*1/3
        p.L(x, y)  # p23
        x -= self.margin
        y -= self.dustdepth*2/3
        p.L(x, y)  # p24
        x -= (self.depth-2*self.margin)
        p.L(x, y)  # p25
        if self.dustdepth > self.depth:
            missing = self.dustdepth-self.depth
            y += missing
            p.L(x, y)
            y += self.dustdepth-missing
        else:
            y += self.dustdepth
        # MOVE
        p.M(x-self.tuckcut, y-self.margin)
        p.L(x-self.tuckcut, y)
        p.L(x, y)  # p26
        y -= self.depth
        p.L(x, y)  # p27
        x0 = x
        x -= self.width
        p.C(x0-self.tuckmargin, y-self.tuckmargin*1.5, x +
            self.tuckmargin, y-self.tuckmargin*1.5, x, y)  # p28 # CURVE
        y += self.depth
        p.L(x, y)  # p29
        p.L(x+self.tuckcut, y)
        p.L(x+self.tuckcut, y-self.margin)
        y -= self.dustdepth
        # MOVE
        if self.dustdepth > self.depth:
            missing = self.dustdepth-self.depth
            p.M(x, y+missing)
            p.L(x, y)
        else:
            p.M(x, y)  # p30
        x -= (self.depth-self.margin*2)
        p.L(x, y)  # p31
        x -= self.margin
        y += self.dustdepth*2/3
        p.L(x, y)  # p32
        x -= self.margin
        y += self.dustdepth*1/3
        p.L(x, y)  # p33        
        y += self.height
        p.L(x, y)  # p2
        x += self.margin
        y += self.dustdepth*1/3
        p.L(x, y)  # p3
        x += self.margin
        y += self.dustdepth*2/3
        p.L(x, y)  # p4
        x += (self.depth-self.margin*2)
        p.L(x, y)  # p5
        if self.dustdepth > self.depth:
            missing = self.dustdepth-self.depth
            y -= missing
            p.L(x, y)
            y -= self.dustdepth-missing
        else:
            y -= self.dustdepth
        
        
        
        self.img.append(p)

        # Draw score line
        p = draw.Path(id='scoring', stroke_width=1,
                      stroke=self.scorecolor, fill='none', stroke_dasharray=5)
        p.M(self.x0+(self.width+self.depth)*2, self.y0+self.height)
        p.L(self.x0+(self.width+self.depth)*2, self.y0)
        p.M(self.x0+self.width+self.depth*2, self.y0)
        p.L(self.x0, self.y0)
        p.M(self.x0+self.depth, self.y0)
        p.L(self.x0+self.depth, self.y0+self.height)
        p.M(self.x0+self.depth, self.y0+self.height+self.depth)
        p.L(self.x0+self.depth+self.width, self.y0+self.height+self.depth)
        p.M(self.x0+self.depth+self.width, self.y0+self.height)
        p.L(self.x0+self.depth+self.width, self.y0)
        p.M(self.x0+self.depth*2+self.width, self.y0)
        p.L(self.x0+self.depth*2+self.width, self.y0+self.height)
        p.L(self.x0, self.y0+self.height)
        p.M(self.x0+self.depth, self.y0-self.depth)
        p.L(self.x0+self.depth+self.width, self.y0-self.depth)
        self.img.append(p)

    def addText(self, front="", rear="", top="", bottom="", right="", left="", fontcolor="blue", fontsize=12):
        g = draw.Group(id="text")
        g.append(draw.Text(bottom, fontsize, self.x0+self.depth+self.width/2, self.y0 -
                 self.depth/2, text_anchor='middle', valign='middle', fill=fontcolor, id="text_bottom"))
        p = draw.Path()
        p.M(self.x0+self.depth+self.width, self.y0+self.height+self.depth/2)
        p.L(self.x0+self.depth, self.y0+self.height+self.depth/2)
        g.append(draw.Text(top, fontsize, path=p, text_anchor='middle',
                 valign='middle', fill=fontcolor, id="text_top"))
        p = draw.Path()
        p.M(self.x0+self.depth/2, self.y0+self.height)
        p.L(self.x0+self.depth/2, self.y0)
        g.append(draw.Text(right, fontsize, path=p, text_anchor='middle',
                 valign='middle', fill=fontcolor, id="text_right"))
        p = draw.Path()
        p.M(self.x0+self.depth/2+self.depth+self.width, self.y0)
        p.L(self.x0+self.depth/2+self.depth+self.width, self.y0+self.height)
        g.append(draw.Text(left, fontsize, path=p, text_anchor='middle',
                 valign='middle', fill=fontcolor, id="text_left"))
        g.append(draw.Text(rear, fontsize, self.x0+self.depth+self.width/2, self.y0 +
                 self.height/2, text_anchor='middle', valign='middle', fill=fontcolor, id="text_rear"))
        g.append(draw.Text(front, fontsize, self.x0+self.depth*2+self.width+self.width/2, self.y0 +
                 self.height/2, text_anchor='middle', valign='middle', fill=fontcolor, id="text_front"))
        self.img.append(g)

    def save(self):
        self.img.setPixelScale(1)  # Set number of pixels per geometry unit
        self.img.saveSvg(self.name+'.svg')
        self.img.savePng(self.name+'.png')


if True:
    tb = tuckbox("sequence_junior", 42, 88, 58)
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

    tb = tuckbox("isle_of_cats_solo", cards=5+23+10+9+4)
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
