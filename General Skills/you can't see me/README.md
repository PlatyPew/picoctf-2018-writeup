# you can't see me
Points: 200

## Category
General Skills

## Question
>'...reading transmission... Y.O.U. .C.A.N.'.T. .S.E.E. .M.E. ...transmission ended...' Maybe something lies in /problems/you-can-t-see-me_3_1a39ec6c80b3f3a18610074f68acfe69.  

### Hint
>What command can see/read files?
>
>What's in the manual page of ls?

## Solution
Doing `ls -la`, you can see the file with the period character as its name. As this character has special meaning when it comes to the linux file systems, when you try to _cat_ it normally, you get the error saying that the period character is a directory.

Therefore you, can try using the _cat_ command by listing all files using the _*_ special character.

Do `cat .*` to get the flag.

### Flag
`picoCTF{j0hn_c3na_paparapaaaaaaa_paparapaaaaaa_cf5156ef}`
