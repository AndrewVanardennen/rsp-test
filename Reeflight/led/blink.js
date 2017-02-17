var wpi = require('wiring-pi');

wpi.setup('gpio');

wpi.pinMode(2, wpi.modes.OUTPUT);


wpi.digitalWrite(2, wpi.HIGH);
