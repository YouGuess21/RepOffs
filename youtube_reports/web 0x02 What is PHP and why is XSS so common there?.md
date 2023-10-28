## What is PHP and why is XSS so common there? – web 0x02

*“PHP (Hypertext Processor) is a general-purpose scripting language and interpreter that is freely available and widely used for web development. Makes dynamic webpages”*

PHP code can be mixed with HTML. Raw HTML source code the browser receives when it requests a file doesn’t contain PHP code. PHP code is never part of the response, it always gets removed. But php code can modify the response… same file different response.

URL Structure: <br> `127.0.0.1:8080/form_get_php?name=example&age=13` <br>
Domain: 127.0.0.1:8080	Path: form_get_php?	
<br>GET Parameter: name=example&age=13

When PHP code runs and echoes variables back, giving info we put back to us, this behaviour is called as “reflected”.

But who prevents us from injecting HTML code or Javascript.<br>
Javascript… XSS Auditor… refuses to execute scripts. It prevents Cross site scripting attacks, that is, injecting a script into a webpage. Does it tho?

How to fix this? We need to escape user supplied input before we echo, or reflect it into page.<br>
PHP function for this is ‘htmlspecialchars’…which replaces characters to some other other character which while outputting get reverted back to the original characters.

For example, < (less than) replaced by &lt; > (greater than) replaced by &gt; & (ampersand) replaced by &amp; “ (double quote) replaced by &quot
