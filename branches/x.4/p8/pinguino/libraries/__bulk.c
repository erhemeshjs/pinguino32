// cdc module for Pinguino
// Jean-Pierre Mandon 2010

#ifndef __USBBULK
#define __USBBULK

#define USB_USE_BULK
//#define BULKDEBUG

#include <usb/usb_bulk.h>
#include <usb/usb_config.c>
#include <usb/picUSB.c>
#include <usb/usb_bulk.c>
#include <delay.c>
#ifdef BULKDEBUG
#include <serial.c>
#endif

void bulk_init()
{
    #ifdef BULKDEBUG
    serial_begin(9600);
    #endif

    // Init
    INTCON=0;
    INTCON2=0xC0;
    UCON=0;
    UCFG=0;
    UEP0=0;UEP1=0;UEP2=0;UEP3=0;UEP4=0;UEP5=0;
    UEP6=0;UEP7=0;UEP8=0;UEP9=0;UEP10=0;UEP11=0;
    UEP12=0;UEP13=0;UEP14=0;UEP15=0;
    // and wait 5 seconds
    Delayms(2000);

    // Initialize USB for CDC
    UCFG = 0x14; 				// Enable pullup resistors; full speed mode
    deviceState = DETACHED;
    remoteWakeup = 0x00;
    currentConfiguration = 0x00;

    // enable USB module
    while(deviceState != CONFIGURED)
    {
      EnableUSBModule();
      ProcessUSBTransactions();
    }

    // Enable Interrupt
    #if defined(__18f25k50) || defined(__18f45k50)
        PIR3bits.USBIF = 0;     // clear usb interrupt flag
        PIE3bits.USBIE = 1;     // enable usb interrupt
        IPR3bits.USBIP = 1;     // high priority interrupt
    #else
        PIR2bits.USBIF = 0;     // clear usb interrupt flag
        PIE2bits.USBIE = 1;     // enable usb interrupt
        IPR2bits.USBIP = 1;     // high priority interrupt
    #endif
    INTCONbits.GIEH = 1;   // Enable global HP interrupts
    INTCONbits.GIEL = 1;   // Enable global LP interrupts
}

void bulk_interrupt(void)
{
    #if defined(__18f25k50) || defined(__18f45k50)
    if(PIR3bits.USBIF)
    #else
    if(PIR2bits.USBIF)
    #endif
    {
        ProcessUSBTransactions();
        UIRbits.SOFIF = 0;
        UIRbits.URSTIF = 0;
        #if defined(__18f25k50) || defined(__18f45k50)
        PIR3bits.USBIF = 0;
        #else
        PIR2bits.USBIF = 0;
        #endif
        UEIR = 0;
    }
}

#endif
