# electricity-monitor
Simple python script to monitor electricity

This is a simple python script running on a pi.
The pi is connected to the fusebox via the output pins of a din counter.

The counter can be gotten here [DIN Counter](https://www.amazon.co.uk/dp/B00T7UEZFK/ref=pe_3187911_185740111_TE_item)

The results are displayed on grafana



![alt text](https://github.com/ronandoolan2/electricity-monitor/blob/master/Sample-usage.png)

# Set up 

First turn off your mains. Then attach the DIN counter in series with your main breaker. The DIN is only rated to 30A so make sure the breaker before it is 30A. If not install a 30A breaker before it. 

Next attach two wires to the counter pins to your raspberry pi. The DIN requires 5V so I made a simple voltage divider to make sure only 3.3V was going to the pi.
![alt text](https://i.stack.imgur.com/UEQNP.png)

Set up the counter scipt to run on boot by adding the following lines to ~/.config/lxsession/LXDE-pi/autostart

@/home/pi/counter3.py 

Afterwards you can install apache to view your results and then install telegraf, influxdb and grafana to view the graphes.
