var wpi = require('wiring-pi');

var pin = 7;

wpi.setup('wpi');



wpi.pinMode(pin, wpi.OUTPUT);

var value = 1;

setInterval(function(){
  wpi.digitalWrite(pin, value);
  value = +!value;
}, 500)

