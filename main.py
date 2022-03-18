import pyxel as px
import gfx



pico8_PAL=[0x000000,0x1D2B53,0x7E2553,0x008751,0xAB5236,0x5F574F,0xC2C3C7,0xFFF1E8,
            0xFF004D,0xFFA300,0xFFEC27,0x00E436,0x29ADFF,0x83769C,0xFF77A8,0xFFCCAA]





class APP:
    def __init__(self):
        
        px.init(128, 128, title="Pyxel")
        px.colors.from_list(pico8_PAL)
        self.CurrentUpdate= TestUpdate
        self.CurrentDraw = TestDraw
        
        px.run(self.update,self.draw)
        

    def update(self):
        self.CurrentUpdate()

    def draw(self):
        self.CurrentDraw()
        


def TestUpdate():
    pass

def TestDraw():
    px.cls(1)
    gfx.Tline(5,8,20,10,1,1)
    #px.line(10,8,25,10,3)
    


APP()
