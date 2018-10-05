# unusable_report_uploader_by_selenium
Test python code to play with selenuim. It's not useful and not fun(Using personal server)

It can't be reusuable for one reason
>using personal server(html, css is different)

but anyway im going to keep using it.


Evaluation
========================================================================================
1. I get confused How to divide into class.
So just bunch of functions. I still can't figure it out 

2. Slow 
Just bunch of time.sleep() (Able to fix)

3. Server
The server that I am using to upload report itself slow (Can't help with it)
Actually that server is not mine. which means I might able to break it? ﾊｧ━(-д-；)━ｧ…


Problems that I got during the coding a& Refs
========================================================================================
1. selenium docs    
 https://selenium-python.readthedocs.io/waits.html
 
2. UnicodeDecodeError: 'utf8' codec can't decode byte 0xff in position 0: invalid start byte    
 [stackoverflow](https://stackoverflow.com/questions/42339876/error-unicodedecodeerror-utf-8-codec-cant-decode-byte-0xff-in-position-0-in)     
>Use this solution it will strip out (ignore) the characters and return the string without them. Only use this if your need is to strip them not convert them.
with open(path, encoding="utf8", errors='ignore') as f:
Using errors='ignore' You'll just lose some characters. but if your don't care about them as they seem to be extra characters originating from a the bad formatting and programming of the clients connecting to my socket server. Then its a easy direct solution. reference
[python docs](docs.python.org/3/howto/unicode.html#the-string-type) 

3.timestmap formatting snippest    
``` 
from datetime import datetime as dt

date = str(dt.today().strftime("%Y-%m-%d"))
hour = str(dt.now().strftime("%H"))
``` 

 
4.instead of time.sleep()....here is..webdriver.wait()      
[source](https://beomi.github.io/2017/10/29/HowToMakeWebCrawler-ImplicitWait-vs-ExplicitWait/)    
But, still don't understand. need to be fixed     


5.having trobule to fetch chromedriver due to the name of path     
[source](https://stackoverflow.com/questions/4780088/what-does-preceding-a-string-literal-with-r-mean)
>The r means that the string is to be treated as a raw string, which means all escape codes will be ignored.     
For an example:
'\n' will be treated as a newline character, while r'\n' will be treated as the characters \ followed by n.
When an 'r' or 'R' prefix is present, a character following a backslash is included in the      
string without change, and all backslashes are left in the string. For example, the string      
literal r"\n" consists of two characters: a backslash and a lowercase 'n'. String quotes can      
be escaped with a backslash, but the backslash remains in the string; for example, r"\"" i    
s a valid string literal consisting of two characters: a backslash and a double quote; r"\"     
is not a valid string literal (even a raw string cannot end in an odd number of backslashes).     
Specifically, a raw string cannot end in a single backslash (since the backslash would escape the    
following quote character). Note also that a single backslash followed by a     
newline is interpreted as those two characters as part of the string, not as a line continuation.
[pythondocs](https://docs.python.org/3/reference/lexical_analysis.html#string-literals)
