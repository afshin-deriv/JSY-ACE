TARGET = "submit_flag_bulk"
SRC=$(wildcard *.py)
DST=bin

all:
	mkdir $(DST) || true
	cp $(SRC) $(DST)/$(TARGET)
	chmod +x  $(DST)/$(TARGET)
%:
	cp $@.py $@
	chmod +x $@


clean:
	rm -rf $(TARGET) $(DST)
.PHONY: clean
