#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""-------------------------------------------------------------------------
    Dictionary of commands and snippets.

    author:		Yeison Cardona
    contact:		yeison.eng@gmail.com 
    first release:	03/February/2012
    last release:	31/March/2012
    
    This library is free software; you can redistribute it and/or
    modify it under the terms of the GNU Lesser General Public
    License as published by the Free Software Foundation; either
    version 2.1 of the License, or (at your option) any later version.

    This library is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
    Lesser General Public License for more details.

    You should have received a copy of the GNU Lesser General Public
    License along with this library; if not, write to the Free Software
    Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA
-------------------------------------------------------------------------"""

from time import ctime
t=ctime().split(" ")

from wxgui._ import _

#To extend...

Dictionary = [
    
    #type
    #"void", "BOOL", "char", "unsigned", "short", "int", "long", "float", "double", "byte", "word", "struct", "union",
    #"typedef", "enum", "char", "loop", "setup", 
    
    #reserved
    #"TRUE", "FALSE", "HIGH", "LOW", "INPUT", "OUTPUT", "FOSC", "MIPS", "ON", "OFF", "PORTA", "PORTB", "PORTC", "PORTD",
    
    #directives
    #"define", "include", "ifndef", "endif",
    
    #calificadores
    #"const", "static", "extern", "volatile",
    
    #control
    
]

#TODO: complete list...
Autocompleter = {
    
"directive": ["define", "include", "ifndef", "endif",],
"reserved" : ["TRUE", "FALSE", "HIGH", "LOW", "INPUT", "OUTPUT", "FOSC", "MIPS", "ON", "OFF", "PORTA", "PORTB", "PORTC", "PORTD",
              "if", "switch", "for", "while", "do", "continue", "break", "else", "returndr", "case","void", "BOOL", "char", "unsigned",
              "short", "int", "long", "float", "double", "byte", "word", "struct", "union", "typedef", "enum", "char", "loop", "setup",
              "if", "switch", "for", "while", "do", "continue", "break", "else", "returndr", "case","const", "static", "extern",
              "volatile",],
    
}


Snippet = {}
#Snippet[name {snippet}]=[set position,"to insert"]
Snippet["void {snippet}"] = [5, "void (){\n\n\t}"]
Snippet["while( ) {snippet}"] = [7, "while (){\n\n\t}"]
Snippet["for {snippet}"] = [5, "for (){\n\n\t}"]
Snippet["for (i=0;...{snippet}"] = [7, "for (i =  ;i< ;i++){\n\n\t}"]
Snippet["if...else {snippet}"] = [4, "if (){\n\n\t}\nelse (){\n\n\t}"]
Snippet["if...else if...else {snippet}"] = [4, "if (){\n\n\t}\nelse if (){\n\n\t}\nelse (){\n\n\t}"]
Snippet["switch( ) {snippet}"] = [8, "switch (){\n\tcase:\n\n\t\tbreak;\n\tdefault:\n\n\t}"]
Snippet[_("Bare Minimum")+" {snippet}"] = [59, "void setup() {\n\t// put your setup code here, to run once:\n\t\n\t}\n\nvoid loop() {\n\t// put your main code here, to run repeatedly:\n\n\t}"]
Snippet[_("Insert Date")+" {snippet}"] = [58 + len(_("Author:")),
"""/*----------------------------------------------------- 
%s  --<>
%s %s
%s

-----------------------------------------------------*/
""" %(_("Author:"), _("Date:"), "/".join([t[2], t[1], t[4]]), _("Description:"))]	
