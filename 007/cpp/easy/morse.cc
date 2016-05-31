#include <map>
#include <string>
#include "morse.hh"


/// Create a morse to alpha map
const MorseMap _createMorseMap() {
    MorseMap m;
    m.insert( std::make_pair( 'a',    ".-"    ) );
    m.insert( std::make_pair( 'b',    "-..."  ) );
    m.insert( std::make_pair( 'c',    "-.-."  ) );
    m.insert( std::make_pair( 'd',    "-.."   ) );
    m.insert( std::make_pair( 'e',    "."     ) );
    m.insert( std::make_pair( 'f',    "..-."  ) );
    m.insert( std::make_pair( 'g',    "--."   ) );
    m.insert( std::make_pair( 'h',    "...."  ) );
    m.insert( std::make_pair( 'i',    ".."    ) );
    m.insert( std::make_pair( 'j',    ".---"  ) );
    m.insert( std::make_pair( 'k',    "-.-"   ) );
    m.insert( std::make_pair( 'l',    ".-.."  ) );
    m.insert( std::make_pair( 'm',    "--"    ) );
    m.insert( std::make_pair( 'n',    "-."    ) );
    m.insert( std::make_pair( 'o',    "---"   ) );
    m.insert( std::make_pair( 'p',    ".--."  ) );
    m.insert( std::make_pair( 'q',    "--.-"  ) );
    m.insert( std::make_pair( 'r',    ".-."   ) );
    m.insert( std::make_pair( 's',    "..."   ) );
    m.insert( std::make_pair( 't',    "-"     ) );
    m.insert( std::make_pair( 'u',    "..-"   ) );
    m.insert( std::make_pair( 'v',    "...-"  ) );
    m.insert( std::make_pair( 'w',    ".--"   ) );
    m.insert( std::make_pair( 'x',    "-..-"  ) );
    m.insert( std::make_pair( 'y',    "-.--"  ) );
    m.insert( std::make_pair( 'z',    "--.."  ) );
    m.insert( std::make_pair( '0',    "-----" ) );
    m.insert( std::make_pair( '1',    ".----" ) );
    m.insert( std::make_pair( '2',    "..---" ) );
    m.insert( std::make_pair( '3',    "...--" ) );
    m.insert( std::make_pair( '4',    "....-" ) );
    m.insert( std::make_pair( '5',    "....." ) );
    m.insert( std::make_pair( '6',    "-...." ) );
    m.insert( std::make_pair( '7',    "--..." ) );
    m.insert( std::make_pair( '8',    "---.." ) );
    m.insert( std::make_pair( '9',    "----." ) );
    m.insert( std::make_pair( ' ',    " / "   ) );
    return m;
}

const char getCharFromMorse( std::string morse, MorseMap& mm ) {
    char result;
    MorseMap::const_iterator iter;
    for ( iter = mm.begin(); iter != mm.end(); iter++ ) {
        if ( iter->second == morse ) {
            result = iter->first;
            break;
        }
    }
    return result;
}

const std::string getMorseFromChar( char alpha, MorseMap& mm ) {
    std::string result;
    MorseMap::const_iterator iter = mm.find( alpha );
    if ( iter != mm.end() ) {
        result = iter->second;
    }
    return result;
}
