#!/bin/bash

computer="$(hostname)"
echo $computer

if [ $computer = "arch-desktop" ]; then
    # Find monitor connection and set refresh rate to 144Hz
    monitorInput="$(xrandr --listactivemonitors | awk '/0/ {print $4}')"
    xrandr --output $monitorInput --mode 1920x1080 --rate 144

    # Adjust mouse sensitivity and acceleration
    xinput --set-prop 'pointer:''Logitech G403 HERO Gaming Mouse' 'libinput Accel Speed' 0
    xinput --set-prop 'pointer:''Logitech G403 HERO Gaming Mouse' 'libinput Accel Profile Enabled' 0, 1
fi
