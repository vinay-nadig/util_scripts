#!/usr/bin/env bash
battery_charge=`acpi -b | cut -f 4 -d " " | awk 'sub("..$","")'`
current_status=`acpi -b | cut -f 3 -d " "`
current_status=${current_status%?}
if [ $battery_charge -lt 60 ]
then
	if [ $current_status == "Discharging" ]
	then
		notify-send -i /usr/share/icons/gnome/48x48/status/battery-good-charging.png "Hey!" "Charge the damn battery!"
	fi
elif [ $battery_charge -gt 80 ]
then
	if [ $current_status == "Charging" ]
	then
		notify-send -i /usr/share/icons/gnome/48x48/status/battery-full.png "Hey!" "Unplug the damn charger!"
	fi
fi

