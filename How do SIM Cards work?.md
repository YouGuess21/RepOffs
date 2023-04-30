## How do SIM Cards work?

A smart card, chip card, is a pocket-sized card that has embedded integrated circuits, mainly include a pattern of metal contacts to electrically connect to the internal chip. 

Chip is smaller than gold connectors, and they just connect with tiny bond wires to there, outer stuff is all plastic.

A phone has two computers…. Because SIM card is actually a tiny computer. Phone computer communicates with tiny embedded sim card computer.

Consider SIM card will have a private key (that is really hard to extract) and you can authenticate to something using public private key cryptography. Basically, private key will never leave a SIM card but if phone computer wants some cryptography to be done, it will ask the SIM to do it. Therefore, only way to clone a SIM card is to know the private key it has. 

What happens if you just steal some SIM card or credit card? That’s why they have a pin. SIM card computer refuses to do crypto-work for your phone computer if you tell it the secret pin.

*“Osmocom SIMtrace or SIMtrace 2 is a software and hardware system for passively tracing the SIM mobile equipment communication.” We use it to intercept the commands and communication between phone and SIM.*

*WireShark is tool to analyze packet (a packet is a small segment of a larger message. Data sent over computer networks, such as the Internet, is divided into packets) based communication.*

Here communication follows GSM (Global System for Mobile Communications) protocol.

When PIN is first entered, its first packet is VERIFY CHV:

VERIFY verifies data with that stored on SIM 

And CHV means Card Holder Verification, basically asking card holder for pin, having 3 attempts.


Then we see SELECT FILE commands: Phone requests content of files stored on SIM Card like IMSI (International Mobile Subscriber Identity [ identify user cellular network]), or contacts stored on SIM card itself, or SIM card menu.


Mainly Java is used in SIM cards. 
