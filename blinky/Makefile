# Quick makefile written for icestick40 (1k) using icestorm toolchain

SRC_FILES=blinky.v
PCF_FILES=blinky.pcf
BLIF_FILES=$(OUTPUT:.bin=.blif)
ASC_FILES=$(OUTPUT:.bin=.asc)
OUTPUT=blinky.bin
SCANSION_PATH=/Applications/Scansion.app/Contents/MacOS/Scansion
SRC_TEST=$(OUTPUT:%.bin=%_test.v)
VFC_DUMP=$(OUTPUT:%.bin=%_dump.vcd)

all: $(OUTPUT)

$(OUTPUT): $(ASC_FILES)
	icepack $< $@

$(ASC_FILES): $(BLIF_FILES)
	arachne-pnr -d 1k -p $(PCF_FILES) $< -o $@

$(BLIF_FILES):
	yosys -p "synth_ice40 -blif $@" $(SRC_FILES)

upload: $(OUTPUT)
	iceprog $<

clean:
	$(RM) *.bin *.blif *.asc

timing: $(ASC_FILES)
	icetime -tmd hx1k $<

test: $(SRC_FILES) $(SRC_TEST)
	iverilog -o $(SRC_TEST:%.v=%) $(SRC_FILES) $(SRC_TEST)
	vvp $(SRC_TEST:%.v=%)
	@echo '[Scansion] $(VFC_DUMP)'
	$(SCANSION_PATH) $(VFC_DUMP)
