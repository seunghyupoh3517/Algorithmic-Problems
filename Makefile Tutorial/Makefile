# declare the variable = what type of compiler to be used
CC=g++

# flag options
CFLAGS=-c -Wall -Werror

# this target will compile all the file 
all: main

main: main.o function1.o function2.o
	 $(CC) main.o function1.o function2.o -o main
#target : command
main.o:	main.cpp
		$(CC) $(CFLAGS) -c main.cpp

function1.o: function1.cpp
		$(CC) $(CFLAGS)	-c function1.cpp

function2.o: function2.cpp
		$(CC) $(CFLAGS) -c function2.cpp

clean:
		rm	-rf	*o	main
