#include <iostream>
#include <random>
#include "myrand.hh"

/*
 * Challenge 004 - https://www.reddit.com/r/dailyprogrammer/comments/pm6oj/2122012_challenge_4_easy/
 *  1. Make a random password generator
 *  2. Allow user to generate multiple passwords
 *  3. Allow user to specify size of the passwords
 */

static void seed() {
    unsigned int time_ui = static_cast<unsigned int>( time( NULL ) );
    std::srand( time_ui );
}

int randn(int &a, int &b) {
    return (rand() % (b - a)) + a;
}

char randchar() {
    int start = 0;
    int end = (sizeof( alphanum ) - 1);
    int char_index = randn(start, end);
    return alphanum[char_index];
}

const std::string randstring( std::string::size_type size ) {
    int i = 0;
    std::string result;
    while ( i < size ) {
        result = result + randchar();
        ++i;
    }
    return result;
}

int main( int argc, char* argv[] ) {

    seed();

    int size16 = 16;
    int size32 = 32;

    const std::string password16 = randstring( size16 );
    const std::string password32 = randstring( size32 );

    std::cout << "16char password: " << password16 << std::endl;
    std::cout << "32char password: " << password32 << std::endl;

    return 0;
}