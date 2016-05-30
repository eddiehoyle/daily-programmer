

#include <iostream>
#include <random>
#include <unistd.h>

static const char alphanum[] =
    "0123456789"
    "!@#$%^&*"
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    "abcdefghijklmnopqrstuvwxyz";

static void seed();
int randn(int &a, int &b);
char randchar();
const std::string randstring( std::string::size_type size );

