#include <iostream>
#include "morse.hh"

/*
 * Write a program that can translate Morse code in the format of ...---...
 * A space and a slash will be placed between words. ..- / --.-
 * For bonus, add the capability of going from a string to Morse code.
 * Super-bonus if your program can flash or beep the Morse.
 * This is your Morse to translate:
 *      .... . .-.. .-.. --- / -.. .- .. .-.. -.-- / .--. .-. --- --. .-. .- -- -- . .-. / --. --- --- -..\
 *       / .-.. ..- -.-. -.- / --- -. / - .... . / -.-. .... .- .-.. .-.. . -. --. . ... / - --- -.. .- -.--
 */


int main( int argc, char* argv[] ) {

    MorseMap mm = _createMorseMap();
    std::string mtest = ".-";
    char ctest = 'd';

    std::cout << "'.-' char: " << getCharFromMorse( mtest, mm ) << std::endl;
    std::cout << "'d' morse: " << getMorseFromChar( ctest, mm ) << std::endl;

//    MorseMap::const_iterator iter;
//    for ( iter = mm.begin(); iter != mm.end(); ++iter ) {
//        std::string key = iter->first;
//        char value = iter->second;
//        std::cout << "Got pair: " << key << ", " << value << std::endl;
//    }
    return 0;
}
