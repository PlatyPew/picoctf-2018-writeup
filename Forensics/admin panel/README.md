# admin panel
Points: 150

## Category
Forensics

## Question
>We captured some [traffic](files/admin_panel.pcap) logging into the admin panel, can you find the password?

### Hint
>Tools like wireshark are pretty good for analyzing pcap files.

## Solution
open data.pcap in wireshark and look through the data by following the packets, on `tcp.stream 5` the plaintext password and username will be shown
```
POST /login HTTP/1.1
Host: 192.168.3.128
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: http://192.168.3.128/
Content-Type: application/x-www-form-urlencoded
Content-Length: 53
Connection: keep-alive
Upgrade-Insecure-Requests: 1

user=admin&password=picoCTF{n0ts3cur3_13597b43}
```

### Flag
`picoCTF{n0ts3cur3_13597b43}`
