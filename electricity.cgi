#!/bin/bash
echo "Content-type: text/html"
echo ""
echo "<html><head><title>Bash as CGI"
echo "</title></head><body>"

echo "<h1>General system information for internet connection $(hostname -s)</h1>"
echo ""

echo "<h1>Current elecy usage</h1>"
echo "<h1> $(tail -1 /home/pi/elecy.cvs | cut -d" " -f4) </h1>"

echo "<h1>Total elecy usage</h1>"
echo "<h1> $(tail -1 /home/pi/elecy.cvs | cut -d" " -f3) </h1>"

echo "<h1>Day elecy usage</h1>"
echo "<h1> $(tail -1 /home/pi/elecy.cvs | cut -d" " -f5) </h1>"

echo "<h1>Night elecy usage</h1>"
echo "<h1> $(tail -1 /home/pi/elecy.cvs | cut -d" " -f6) </h1>"

echo "<center>Information generated on $(date)</center>"
echo "</body></html>"
