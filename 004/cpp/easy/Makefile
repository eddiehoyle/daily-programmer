TARGET = run
CC = g++

run:
	$(CC) -c main.cc -o main.o
	$(CC) -c myrand.hh -o myrand.o
	$(CC) main.o myrand.o -o $(TARGET)

clean:
	rm *.o $(TARGET)