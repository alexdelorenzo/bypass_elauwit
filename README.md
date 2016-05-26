# auto_elauwit

Bypass Elauwit's captive portal. It's really annoying, so here's my quickly hacked up solution.

## Usage
AP MAC is currently hardcoded, so this script isn't ready to be used without hand editting in your AP MAC address.
This is easily fixed as the MAC address is returned to you as a URL parameter when you are redirected to Elauwit's portal.

Supply your MAC at runtime through STDIN

On Mac OS X
`ifconfig en0 | grep ether | sed 's/.*ether \(.*\) $/\1/' | python3 bypass_portal.py`
