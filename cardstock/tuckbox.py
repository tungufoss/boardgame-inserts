import drawSvg as draw
import math 

class tuckbox:
    def __init__(self, name, cards = 52, height_mm = 89, width_mm = 64, cardwidth_mm=0.24, margin_mm=1, dpi=96):
        self.name = name 
        self.dpi = dpi
        dpmm = dpi/25.4
        self.height = height_mm*dpmm
        self.width = width_mm*dpmm
        depth_mm = max(5,math.ceil(cards*cardwidth_mm))
        self.depth = depth_mm*dpmm
        if depth_mm == 5:
            margin_mm = 0.2
        self.margin = margin_mm*dpmm
        self.tuckmargin = 14*dpmm
        print(f'Tuckbox of size {height_mm}mm x {width_mm}mm x {depth_mm}mm, #{cards} cards')
        image_width = self.width*2+self.depth*3
        image_height = self.height+self.depth*2+self.tuckmargin*1.5
        self.scorecolor = 'red'
        self.img = draw.Drawing(image_width, image_height, displayInline=False)

    def draw(self):        
        # Draw polygon, cut lines
        p = draw.Path(id="cut-tuckbox", 
                      stroke_width=1, stroke='black',
                      fill='white', fill_opacity=0.5)

        x, y = 0, self.depth
        p.M(x,y) # p1
        y += self.height
        p.L(x, y) # p2
        x += self.margin
        p.L(x, y) # p3
        x += self.margin
        y += self.depth
        p.L(x, y) # p4
        x += (self.depth-self.margin*4)
        p.L(x, y) # p5
        x += self.margin
        y -= self.depth
        p.L(x, y) # p6
        x += self.margin
        p.L(x, y) # p7
        y += self.depth
        p.L(x, y) # p8                
        x0 = x
        x += self.width
        p.C(x0+self.tuckmargin,y+self.tuckmargin*1.5,x-self.tuckmargin,y+self.tuckmargin*1.5,x,y) # p9 # curve
        y -= self.depth
        p.L(x,y) # p10
        x += self.margin
        p.L(x,y) # p11
        x += self.margin
        y += self.depth
        p.L(x,y) # p12
        x += (self.depth - 4*self.margin)
        p.L(x,y) # p13
        x += self.margin
        y -= self.depth
        p.L(x,y) # p14
        x += self.margin
        p.L(x,y) # p15        
        x += (self.width-self.tuckmargin)/2
        p.L(x,y) # p16        
        x += self.tuckmargin
        p.A(3,3,10,1,0, x, y) # p17 - curve
        x += (self.width-self.tuckmargin)/2
        p.L(x,y) # p18
        y -= self.margin
        p.L(x,y) # p19
        x += (self.depth - self.margin)
        y -= self.margin
        p.L(x,y) # p20
        y -= (self.height - 4*self.margin)
        p.L(x,y) # p21
        y -= self.margin
        x -= (self.depth - self.margin)
        p.L(x,y) # p22
        y -= self.margin
        p.L(x,y) # p23
        x -= self.margin
        p.L(x,y) # p24
        y -= (self.depth-self.margin)
        p.L(x,y) # p25
        x -= (self.width-2*self.margin)
        p.L(x,y) # p26
        y += (self.depth-self.margin)
        p.L(x,y) # p27
        x -= self.margin
        p.L(x,y) # p28
        x -= self.margin
        p.L(x,y) # p29
        x -= self.margin
        y -= self.depth
        p.L(x,y) # p30
        x -= (self.depth-4*self.margin)
        p.L(x,y) # p31
        x -= self.margin
        y += self.depth
        p.L(x,y) # p32
        x -= self.margin
        p.L(x,y) # p33
        y -= self.depth
        p.L(x,y) # p34
        x -= self.width
        p.L(x,y) # p35
        y += self.depth
        p.L(x,y) # p36
        x -= self.margin
        p.L(x,y) # p37
        y -= self.depth
        x -= self.margin
        p.L(x,y) # p38
        x -= (self.depth-self.margin*4)
        p.L(x,y) # p39
        x -= self.margin
        y += self.depth
        p.L(x,y) # p40        
        x -= self.margin
        p.L(x,y) # 41
        self.img.append(p)
                        
        # Draw score line
        g = draw.Group(id="scoring")
        p = draw.Path(id='score_frontbottom',stroke_width=1, stroke=self.scorecolor,fill='none', stroke_dasharray=5, group="scoring")
        p.M((self.width+self.depth)*2,self.height+self.depth)
        p.L((self.width+self.depth)*2,self.depth)
        p.L(0, self.depth)
        g.append(p)        
        p = draw.Path(id="score_rightback",stroke_width=1, stroke=self.scorecolor,fill='none', stroke_dasharray=5, group="scoring")
        p.M(self.depth, self.depth)
        p.L(self.depth, self.depth+self.height)
        g.append(p)
        p = draw.Path(id="score_backtop",stroke_width=1, stroke=self.scorecolor,fill='none', stroke_dasharray=5, group="scoring")
        p.M(self.depth, self.height+self.depth*2)
        p.L(self.depth+self.width, self.height+self.depth*2)
        g.append(p)
        p = draw.Path(id="score_backleft",stroke_width=1, stroke=self.scorecolor,fill='none', stroke_dasharray=5, group="scoring")
        p.M(self.depth+self.width, self.height+self.depth)
        p.L(self.depth+self.width, self.depth)
        g.append(p)
        p = draw.Path(id="score_leftfronttop",stroke_width=1, stroke=self.scorecolor,fill='none', stroke_dasharray=5, group="scoring")
        p.M(self.depth*2+self.width, self.depth)
        p.L(self.depth*2+self.width, self.depth+self.height)
        p.L(0, self.depth+self.height)
        g.append(p)
        self.img.append(g)
        
    def addText(self, front="", back="", top="", bottom="", right="", left="", fontcolor="blue", fontsize=12) :        
        g = draw.Group(id="text")
        g.append(draw.Text(bottom, fontsize, self.depth+self.width/2, self.depth/2, text_anchor='middle', valign='middle', fill=fontcolor, id="text_bottom"))
        p = draw.Path()        
        p.M(self.depth+self.width, self.height+self.depth+self.depth/2)
        p.L(self.depth, self.height+self.depth+self.depth/2)        
        g.append(draw.Text(top, fontsize, path=p, text_anchor='middle', valign='middle', fill=fontcolor, id="text_top"))
        p = draw.Path()        
        p.M(self.depth/2, self.height+self.depth)
        p.L(self.depth/2, self.depth)        
        g.append(draw.Text(right, fontsize, path=p, text_anchor='middle', valign='middle', fill=fontcolor, id="text_right"))        
        p = draw.Path()
        p.M(self.depth/2+self.depth+self.width, self.depth)
        p.L(self.depth/2+self.depth+self.width, self.height+self.depth)        
        g.append(draw.Text(left, fontsize, path=p, text_anchor='middle', valign='middle', fill=fontcolor, id="text_left"))        
        g.append(draw.Text(back, fontsize, self.depth+self.width/2, self.depth+self.height/2, text_anchor='middle', valign='middle', fill=fontcolor, id="text_back"))
        g.append(draw.Text(front, fontsize, self.depth*2+self.width+self.width/2, self.depth+self.height/2, text_anchor='middle', valign='middle', fill=fontcolor, id="text_front"))
        self.img.append(g)
        
    def save(self):
        self.img.setPixelScale(1)  # Set number of pixels per geometry unit        
        self.img.saveSvg(self.name+'.svg')
        self.img.savePng(self.name+'.png')

tb = tuckbox("sequence_junior", 42, 88, 58)
tb.draw()
tb.addText(left="Sequence junior",right="Sequence junior",top="Sequence junior",bottom="Sequence junior")
tb.save()

tb = tuckbox("isle_of_cats_main", cards=150)
tb.draw()
tb.addText(front="Isle of Cats:\nDiscovery Cards",
           back="Isle of Cats:\nDiscovery Cards",
           top="Isle of Cats: Discovery Cards",
           bottom="Isle of Cats: Discovery Cards",
           left="Isle of Cats: Discovery Cards",
           right="Isle of Cats: Discovery Cards")
tb.save()

tb = tuckbox("isle_of_cats_family", cards=18)
tb.draw()
tb.addText(front="Isle of Cats:\nFamily Cards",
           back="Isle of Cats:\nFamily Cards",
           top="Isle of Cats: Family Cards",
           bottom="Isle of Cats: Family Cards",
           left="Isle of Cats: Family Cards",
           right="Isle of Cats: Family Cards")
tb.save()

tb = tuckbox("isle_of_cats_solo", cards=5+23+10+9+4)
tb.draw()
tb.addText(front="Isle of Cats:\nSolo Cards",
           back="Isle of Cats:\nSolo Cards",
           top="Isle of Cats: Solo Cards",
           bottom="Isle of Cats: Solo Cards",
           left="Isle of Cats: Solo Cards",
           right="Isle of Cats: Solo Cards")
tb.save()

tb = tuckbox("isle_of_cats_baskets", cards=10, cardwidth_mm=.5)
tb.draw()
tb.addText(front="Isle of Cats:\nBasket tokens",
           back="Isle of Cats:\nBasket tokens",
           top="Isle of Cats: Basket tokens",
           bottom="Isle of Cats: Basket tokens",
           left="Isle of Cats: Basket tokens",
           right="Isle of Cats: Basket tokens")
tb.save()
