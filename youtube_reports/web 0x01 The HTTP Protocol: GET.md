## The HTTP Protocol: GET /test.html - web 0x01

*“A server… is just a program that gives you files if you ask for them. A server is a software or hardware device that accepts and responds to requests made over a network. The device that makes the request, and receives a response from the server, is called a client.”*

127.0.0.1 special IP referencing localhost, port 80 default port for websites.

```php -S <IP address>:<port>``` where to listen from.<br>
`$ php -S 127.0.0.1:8080`

A port is just a number inside of tcp (transfer control protocol) packet. When network card and operating system receives a tcp packet, it will look at port number inside that packet of bytes. Then it checks if progams is listening, meaning it’s waiting for packet on that particular port. Then the operating system will give the content of the packet to that program.

Favicons.ico ...tiny icons of websites in titles…

*Netcat is a simple unix utility which reads and writes data across network connections, using tcp or udp (user datagram protocol {comparing to tcp, udp is faster but less reliable and unlike tcp its connectionless})*

HTTP [<html>] is built on top of TCP [port:8080] which in turn sits on IP layer [dest: 127.0.0.1]
  
IP layer identifies IP addresses that identify receiving computer in a network, ports are used by operating system to decide to which application it should forward the content of tcp packet, and the content is in a special formal – HTTP.
  
`$ nc 127.0.0.1 8080`

GET /test.html
  
  
  Server responds with HTTP status code (200 OK), HTTP headers (key value pairs...what type…how long), content (the webpage).
  
  Therefore, HTTP is just plaintext sent between our browser and webserver, thereby inefficient but easy to understand for humans.
  
  Browser too sends Request Headers (user agent, accept types).
