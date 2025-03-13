SRCS = $(wildcard *.c)
PROGS = $(patsubst %.c, %, $(SRCS))

all: $(PROGS)
% : %.clean
	gcc -o $@ $^
clean : $(PROGS)