PROJ_NAME = blinky
PCF_FILE = $(PROJ_NAME).pcf

all: $(PROJ_NAME).bin

%.bin: %.asc
	icepack $< $@

%.asc: %.blif
	arachne-pnr -d 1k -o $@ -p $(PCF_FILE) $<

%.blif: %.v
	yosys -p 'synth_ice40 -top main -blif $@' $<

upload: $(PROJ_NAME).bin
	iceprog $<

explain: $(PROJ_NAME).asc
	icebox_explain $<

timing: $(PROJ_NAME).asc
	icetime -tmd hx1k $<

clean:
	rm -rf *.bin *.asc *.blif

.PHONY: all upload explain clean

.PRECIOUS: %.bin %.pnr %.blif