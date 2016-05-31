#ifndef MORSE_H
#define MORSE_H

#include <map>
#include <string>

typedef std::map< char, std::string > MorseMap;
const MorseMap _createMorseMap();
const char getCharFromMorse( std::string, MorseMap& );
const std::string getMorseFromChar( char, MorseMap& );

#endif /* MORSE_H */