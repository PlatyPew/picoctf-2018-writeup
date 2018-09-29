# ssh-keyz
Points: 150

## Category
General Skills

## Question
>As nice as it is to use our webshell, sometimes its helpful to connect directly to our machine. To do so, please add your own public key to ~/.ssh/authorized_keys, using the webshell. The flag is in the ssh banner which will be displayed when you login remotely with ssh to with your username.

### Hint
>key generation [tutorial](https://confluence.atlassian.com/bitbucketserver/creating-ssh-keys-776639788.html)
>
>We also have an expert demonstrator to help you along. [link](https://www.youtube.com/watch?v=3CN65ccfllU&list=PLJ_vkrXdcgH-lYlRV8O-kef2zWvoy79yP&index=4)

## Solution
Add your public key to _~/.ssh/authorized_keys_. You can generate your key by doing `ssh-keygen -t rsa`

Connect to web shell by doing `ssh <user>@2018shell1.picoctf.com`

```
# ssh Platy@2018shell1.picoctf.com
The authenticity of host '2018shell1.picoctf.com (18.223.208.176)' can't be established.
ECDSA key fingerprint is SHA256:zCX5ip3tx1RMbsJBc70jEazd+gAFzlbC1Q2iDI8LA/k.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added '2018shell1.picoctf.com,18.223.208.176' (ECDSA) to the list of known hosts.
picoCTF{who_n33ds_p4ssw0rds_38dj21}
Welcome to Ubuntu 16.04.5 LTS (GNU/Linux 4.4.0-1067-aws x86_64)
...
...
...
```

### Flag
`picoCTF{who_n33ds_p4ssw0rds_38dj21}`
