#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

"""-------------------------------------------------------------------------
	Pinguino Boards List

	author:			Regis Blanchot
	contact:		rblanchot@gmail.com 
	first release:	2011-10-23
	last release:	2011-11-19
	
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

import wx	# wx.NewId()

# vendors id
MICROCHIP_ID = 0x04D8

# products id
PIC8_ID = 0xFEAA
PIC32_ID = 0x003C

class Vasco2550:
	name='Generic 18F2550 + Vasco Bldr.'
	id=wx.NewId()
	arch=8
	bldr='vasco'
	proc='18f2550'
	board='PIC18F2550'
	vendor=MICROCHIP_ID
	product=PIC8_ID
	memstart=0x2000
	memend=0x7fff
	shortarg='-g'
	longarg='--vasco2550'

class Vasco4550:
	name='Generic 18F4550 + Vasco Bldr.'
	id=wx.NewId()
	arch=8
	bldr='vasco'
	proc='18f4550'
	board='PIC18F4550'
	vendor=MICROCHIP_ID
	product=PIC8_ID
	memstart=0x2000
	memend=0x7fff
	shortarg='-G'
	longarg='--vasco4550'

class Diolan2550:
	name='Generic 18F2550 + Diolan Bldr.'
	id=wx.NewId()
	arch=8
	bldr='diolan'
	proc='18f2550'
	board='PIC18F2550'
	vendor=MICROCHIP_ID
	product=PIC8_ID
	memstart=0x800
	memend=0x7fff
	shortarg='-d'
	longarg='--diolan2550'

class Diolan26J50:
	name='Generic 18F26J50 + Diolan Bldr.'
	id=wx.NewId()
	arch=8
	bldr='diolan'
	proc='18f26j50'
	board='PIC18F26J50'
	vendor=MICROCHIP_ID
	product=PIC8_ID
	memstart=0x800
	memend=0xffff
	shortarg='-d2'
	longarg='--diolan26j50'

class Diolan4550:
	name='Generic 18F4550 + Diolan Bldr.'
	id=wx.NewId()
	arch=8
	bldr='diolan'
	proc='18f4550'
	board='PIC18F4550'
	vendor=MICROCHIP_ID
	product=PIC8_ID
	memstart=0x800
	memend=0x7fff
	shortarg='-D'
	longarg='--diolan4550'

class PICuno_Equo:
	name='PICuno Equo'
	id=wx.NewId()
	arch=8
	bldr='vasco'
	proc='18f4550'
	board='PICUNO_EQUO'
	vendor=MICROCHIP_ID
	product=PIC8_ID
	memstart=0x2000
	memend=0x7fff
	shortarg='-p'
	longarg='--picunoequo'

class FreeJALduino:
	name='FreeJALduino'
	id=wx.NewId()
	arch=8
	bldr='vasco'
	proc='18f2550'
	board='FREEJALDUINO'
	vendor=MICROCHIP_ID
	product=PIC8_ID
	memstart=0x2000
	memend=0x7fff
	shortarg='-j'
	longarg='--freejalduino'

class PIC32_Pinguino:
	name='PIC32 Pinguino'
	id=wx.NewId()
	arch=32
	bldr='microchip'
	proc='32MX440F256H'
	board='PIC32_PINGUINO'
	vendor=MICROCHIP_ID
	product=PIC32_ID
	memstart=0x00000
	memend=0x40000
	shortarg='-o'
	longarg='--olimex440'

class PIC32_Pinguino_OTG:
	name='PIC32 Pinguino OTG'
	id=wx.NewId()
	arch=32
	bldr='microchip'
	proc='32MX440F256H'
	board='PIC32_PINGUINO_OTG'
	vendor=MICROCHIP_ID
	product=PIC32_ID
	memstart=0x00000 #0x9D000000
	memend=0x40000
	shortarg='-O'
	longarg='--olimex440OTG'

class PIC32_Pinguino_Micro:
	name='PIC32 Pinguino Micro'
	id=wx.NewId()
	arch=32
	bldr='microchip'
	proc='32MX440F256H'
	board='PIC32_PINGUINO_MICRO'
	vendor=MICROCHIP_ID
	product=PIC32_ID
	memstart=0x00000
	memend=0x40000
	shortarg='-M'
	longarg='--olimex440Micro'

class PIC32_Pinguino_220:
	name='PIC32_Pinguino_220'
	id=wx.NewId()
	arch=32
	bldr='microchip'
	proc='32MX220F032D'
	board='PIC32_PINGUINO_220'
	vendor=MICROCHIP_ID
	product=PIC32_ID
	memstart=0x00000
	memend=0x07FFF
	shortarg='-m'
	longarg='--olimex220'

class Emperor_460:
	name='Emperor 460'
	id=wx.NewId()
	arch=32
	bldr='microchip'
	proc='32MX460F512L'
	board='EMPEROR460'
	vendor=MICROCHIP_ID
	product=PIC32_ID
	memstart=0x00000
	memend=0x80000
	shortarg='-e'
	longarg='--emperor460'

class Emperor_795:
	name='Emperor 795'
	id=wx.NewId()
	arch=32
	bldr='microchip'
	proc='32MX795F512L'
	board='EMPEROR795'
	vendor=MICROCHIP_ID
	product=PIC32_ID
	memstart=0x00000
	memend=0x80000
	shortarg='-E'
	longarg='--emperor795'

class UBW32_460:
	name='UBW32 460'
	id=wx.NewId()
	arch=32
	bldr='microchip'
	proc='32MX460F512L'
	board='UBW32_460'
	vendor=MICROCHIP_ID
	product=PIC32_ID
	memstart=0x00000
	memend=0x80000
	shortarg='-u'
	longarg='--ubw460'

class UBW32_795:
	name='UBW32 795'
	id=wx.NewId()
	arch=32
	bldr='microchip'
	proc='32MX795F512L'
	board='UBW32_795'
	vendor=MICROCHIP_ID
	product=PIC32_ID
	memstart=0x00000
	memend=0x80000
	shortarg='-U'
	longarg='--ubw795'

boardlist = [
				Vasco2550, Vasco4550,
				Diolan2550, Diolan26J50, Diolan4550,
				PICuno_Equo, FreeJALduino,
				PIC32_Pinguino, PIC32_Pinguino_OTG,
				PIC32_Pinguino_Micro, PIC32_Pinguino_220,
				Emperor_460, Emperor_795,
				UBW32_460, UBW32_795
			]

