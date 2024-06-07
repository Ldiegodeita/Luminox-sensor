# Luminox-sensor
Simple GUI python to send commands to a LOX-02 Luminox sensor
This is a very simple python code to send serial comunnication commands to a oxygen LOX-02 Luminox sensor

this is the list of commands
"M" OUTPUT MODE 0=STREAM, 1=POLL, 2= OFF. "M 0" mode is set by default, you have to add a separator (space) between "M" and the number
“O” Request current ppO2 in mbar
“%” Request percent current O2 valuec
“T” current temperature inside sensor in °C
“P” Request current barometric pressurec
“e” Sensor Status “e 0000\r\n” = Sensor Status Good “e xxxx\r\n” = Any other response, contact SST Sensing for advice
“A” Request all values (see above: O, %, T, P and e)
“#” Sensor Information 0 = Date of manufacture, 1 = Serial Number, 2 = Software Revision, “# YYYYY DDDDD\r\n”, “# xxxxx xxxxx\r\n”, “# xxxxx\r\n”
