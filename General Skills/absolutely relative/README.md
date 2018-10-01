# absolutely relative
Points: 250

## Category
General Skills

## Question
>In a filesystem, everything is relative ¯\\\_(ツ)\_/¯. Can you find a way to get a flag from this [program](files/absolutely-relative)? You can find it in /problems/absolutely-relative_1_15eb86fcf5d05ec169cc417d24e02c87 on the shell server. [Source](files/absolutely-relative.c). 

### Hint
>Do you have to run the program in the same directory? (⊙.☉)7
>
>Ever used a text editor? Check out the program 'nano'

## Solution
Reading the source code, the binary wants a file _permission.txt_ with the contents _yes_ in it.

Just open the web shell, create the file in a directory which you have write permissions.

Run the binary from current directory.

```
$ pwd
/home/Platy
$ echo -n "yes" > permissions.txt
$ /problems/absolutely-relative_1_15eb86fcf5d05ec169cc417d24e02c87/absolutely-relative
You have the write permissions.
picoCTF{3v3r1ng_1$_r3l3t1v3_a97be50e}
```

This works because the file _flag.txt_ is referenced using an absolute path while the _permission.txt_ is being referenced from your local directory.

### Flag
`picoCTF{3v3r1ng_1$_r3l3t1v3_a97be50e}`
