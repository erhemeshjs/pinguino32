/*	----------------------------------------------------------------------------
	FILE:				newlib.c
	PROJECT:			pinguinoX
	PURPOSE:		
	PROGRAMER:		jean-pierre mandon <jp.mandon@gmail.com>
	FIRST RELEASE:	15 may. 2011
	LAST RELEASE:	15 may. 2011
	* 
	* This is a set of system calls beetween newlib and pinguino32
	* 
	----------------------------------------------------------------------------
	This library is free software; you can redistribute it and/or
	modify it under the terms of the GNU Lesser General Public
	License as published by the Free Software Foundation; either
	version 2.1 of the License, or (at your option) any later version.

	This library is distributed in the hope that it will be useful,
	but WITHOUT ANY WARRANTY; without even the implied warranty of
	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
	Lesser General Public License for more details.

	You should have received a copy of the GNU Lesser General Public
	License along with this library; if not, write to the Free Software
	Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
	--------------------------------------------------------------------------*/

#include <__cdc.c>
#include <serial.c>
// TODO include LCD lib, serial lib for UART2 etc.....


// this function is used to allocate space on the heap
// ( called by malloc )

unsigned char *heap_ptr;
extern _heap;

unsigned char *sbrk(int nbbytes)
{
	char *base;
	
	if (!heap_ptr)
		heap_ptr=(char *)&_heap;	// _heap is defined in the linker script
	base=heap_ptr;					// on Pinguino32 heap is 8192 bytes 
	heap_ptr += nbbytes;
	return base;
}

// open
// open a stream output
// success return the number associated with the stream
// else return -1

int open(const char *name, int flags, int mode)
{
if (!strcmp(name,"CDC")) 
	{
		init_CDC(); 
		return(2);
	}
	
if (!strcmp(name,"SERIAL1")) 
	{
		SerialConfigure(UART1, UART_ENABLE,	UART_RX_TX_ENABLED,	9600);
		return(1);
	}
	
// TODO LCD, SPI etc.....
// TODO define a flag to know if the stream is opened
}

// close
// close a stream
// success return 0, failed return -1

int close(int file)
{
	return -1;
	// TODO clear interrupt for some stream
}

// fstat
// called by newlib to know the state of a stream
// return 0 if stream is available
// failed return -1

int fstat(int file, struct stat *st) 
{
	return 0;
}

// isatty
// isatty is called to know if a stream accepts tty
// success return 1
// failed return 0

int isatty(int file)
{
	return 1;
}

// lseek
// lseek set position in a file
// success output is the position in the file
// failed -1

int lseek(int file, int ptr, int dir)
{
        return 0;
}

// read
// read len char in the file and put them in ptr
// success return the number of char read
// failed return -1

int read(int file, char *ptr, int len){
	return 0;
}

// write
// write 'len' char on the 'file' stream
// success: return number of characters written
// failed: return -1

int write(int file, char *ptr, int len)
{
	int todo;
	if (file==1)
		{
		for (todo = 0; todo < len; todo++) SerialUART1WriteChar(*ptr++);
		return len;
		}
}
