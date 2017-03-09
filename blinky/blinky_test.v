`timescale 8 ns / 100 ps

module blinky_test;

initial begin
    $dumpfile("blinky_dump.vcd");
    $dumpvars(0, blinky_test);
    #1400000 $finish;
end

reg clk = 0; //12 MHz clock signal
    
wire pin_d1;
wire pin_d2;
wire pin_d3;
wire pin_d4;
wire pin_d5;

top top_test(
    .clk(clk),
    .pin_d1(pin_d1),
    .pin_d2(pin_d2),
    .pin_d3(pin_d3),
    .pin_d4(pin_d4),
    .pin_d5(pin_d5)
);

always #1 clk <= ~clk;


endmodule