retropie-mausberry-switch
=========================

Script for my "Raspberry Pi Emulation Station in a NES case" project

This script is intended to use with a mausberry shutdown circuit, on a retropie-based game station:
http://mausberry-circuits.myshopify.com/products/shutdown-circuit-use-your-own-switch
http://blog.petrockblock.com/retropie/

Like most such scripts, it sends a continuous "on" signal to the mausberry circuit for it to cut power once shutdown is complete, and it listens on a GPIO pin for an action on a switch in order to send a shutdown command to the OS.

Additionnaly, it listens on a second GPIO pin for an additionnal switch (the NES "Reset" switch in my case).
When this switch is activated, it will look in the current running processes for an emulator, and if found will send an interrupt signal to the process, thus exiting the game and returning to the emulationstation Gui.