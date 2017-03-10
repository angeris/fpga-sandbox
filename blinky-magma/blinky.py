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
q = Counter(24)
# last bit of clock
clk_out = q.O[23]

# wire the output to the red led
wire(clk_out, main.D5)

# register to hold which LED is on (2 bits)
reg_led = Register(2, s=True)

# register to hold next assignment (2 bits)
reg_led_next = Register(2, s=True)

# on rise edge, set the first register to be written
wire(clk_out, reg_led.SET)

# on fall edge, set the second register to be written
not_clk_out = Not()(clk_out)
wire(not_clk_out, reg_led_next.SET)

# adder to keep track of current clock
reg_adder = Adders(2, cin=False, cout=False)
# output of reg goes to adder to keep track
wire(reg_led.O, reg_adder.I0)
# each output should be added by one
wire(array(*int2seq(1, 2)), reg_adder.I1)

wire(reg_led_next.O, reg_led.I)

# reg output goes to led
wire(reg_led.O[1], main.D1)


compile(sys.argv[1], main) 