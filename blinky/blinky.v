module top(
    input wire clk, //12 MHz clock signal
    
    output wire pin_d5,
    output wire pin_d1,
    output wire pin_d2,
    output wire pin_d3,
    output wire pin_d4
);
    reg led_on = 0;
    reg [1:0] curr_led = 0;
    reg [23:0] curr_time; // Holds the current time

    assign pin_d5 = led_on;

    // Switch pin every half-second
    always @(posedge clk) begin
        if (currtime[23]) begin
            led_on <= ~led_on;
            curr_time <= 0;
            curr_led <= (curr_led == 3) ? 0 : curr_led + 1;
        end
        else
            curr_time <= curr_time + 1;
    end

    // Do the assignments for the red leds
    assign pin_d1 = (curr_led == 0);
    assign pin_d2 = (curr_led == 1);
    assign pin_d3 = (curr_led == 2);
    assign pin_d4 = (curr_led == 3);

endmodule