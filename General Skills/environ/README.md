# environ
Points: 150

## Category
General Skills

## Question
>Sometimes you have to configure environment variables before executing a program. Can you find the flag we've hidden in an environment variable on the shell server? 

### Hint
>unix [env](https://www.tutorialspoint.com/unix/unix-environment.htm)

## Solution
We can use the _printenv_ command to show all the environment variables running in the system. Pipe output to _grep_ and get the flag.

```
# Execute this command in the web shell
$ printenv | grep picoCTF
SECRET_FLAG=picoCTF{eNv1r0nM3nT_v4r14Bl3_fL4g_3758492}
```

### Flag
`picoCTF{eNv1r0nM3nT_v4r14Bl3_fL4g_3758492}`
