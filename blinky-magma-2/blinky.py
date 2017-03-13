import sys
from magma import *         # import base stuff from magma (arrays, wires, and other foundational things)
from mantle import *        # import nice stuff from ice40-specific stuff (flip flops, luts, adders, etc)
from boards.icestick import IceStick

icestick = IceStick()       # define the current icestick
icestick.Clock.on()         # enable the clock, of course

# Initialize all LED GPIO connections
icestick.D1.on()
icestick.D2.on()
icestick.D3.on()
icestick.D4.on()
icestick.D5.on()

# Get main connections for icestick
main = icestick.main()

# enable a memory that has 24-bit width connected to the clock (from mantle)
q = Counter(24)

# last bit of clock
clk_out = q.O[23]

# wire the output to the red led
wire(clk_out, main.D5)

# Register to hold current LED
reg_led = Register(2)

# Write only on clk_out positive edge
wire(clk_out, reg_led.CLK)

# Adder for switching pins
reg_add = Adders(2, cin=False, cout=False)

# Wiring, reg output to adder input 0 
# hard-wired 1 to adder input 1
# adder output to reg input
wire(reg_led.O, reg_add.I0)
wire(array(*[1,0]), reg_add.I1)
wire(reg_add.O, reg_led.I)

# Make equalities work, decode table to LEDs
# Decoder has the following table:
# 00 -> 0001
# 01 -> 0010
# 10 -> 0100
# 11 -> 1000
dec = Decoder(2)
wire(reg_led.O, dec.I)
wire(dec.O[0], main.D1)
wire(dec.O[1], main.D2)
wire(dec.O[2], main.D3)
wire(dec.O[3], main.D4)

# Compile everything above
compile(sys.argv[1], main) 