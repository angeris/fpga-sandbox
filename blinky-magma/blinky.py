import sys
from magma import *         # import base stuff from magma (arrays, wires, and other foundational things)
from mantle import *        # import nice stuff from ice40-specific stuff (flip flops, luts, adders, etc)
from boards.icestick import IceStick

icestick = IceStick()       # define the current icestick
icestick.Clock.on()         # enable the clock, of course
icestick.D1.on()
icestick.D2.on()
icestick.D3.on()
icestick.D4.on()
icestick.D5.on()

main = icestick.main()

# enable a memory that has 24-bit width connected to the clock (from mantle)
q = Counter(25)
# last bit of clock
clk_out = q.O[23]

# wire the output to the red led
wire(clk_out, main.D5)

# Make equalities work
dec = Decoder(2)
wire(q.O[23:25], dec.I)
wire(dec.O[0], main.D1)
wire(dec.O[1], main.D2)
wire(dec.O[2], main.D3)
wire(dec.O[3], main.D4)


compile(sys.argv[1], main) 