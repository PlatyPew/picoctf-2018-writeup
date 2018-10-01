# Aca-Shell-A
Points: 150

## Category
General Skills

## Question
>It's never a bad idea to brush up on those linux skills or even learn some new ones before you set off on this adventure! Connect with `nc 2018shell1.picoctf.com 33158`.

### Hint
>Linux for [Beginners](https://maker.pro/education/basic-linux-commands-for-beginners)

## Solution
This challenge teaches you the basic commands of Linux.

- `ls`
- `cd`
- `rm`
- How to execute files
- `whoami`
- `cat`

Follow the instructions and get the flag.

```
$ nc 2018shell1.picoctf.com 33158
Sweet! We have gotten access into the system but we aren't root.
It's some sort of restricted shell! I can't see what you are typing
but I can see your output. I'll be here to help you along.
If you need help, type "echo 'Help Me!'" and I'll see what I can do
There is not much time left!
~/$ ls
blackmail
executables
passwords
photos
secret
~/$ cd secret
Now we are cookin'! Take a look around there and tell me what you find!
~/secret$ ls
intel_1
intel_2
intel_3
intel_4
intel_5
profile_AipieG5Ua9aewei5ieSoh7aph
profile_Xei2uu5suwangohceedaifohs
profile_ahShaighaxahMooshuP1johgo
profile_ahqueith5aekongieP4ahzugi
profile_aik4hah9ilie9foru0Phoaph0
profile_bah9Ech9oa4xaicohphahfaiG
profile_ie7sheiP7su2At2ahw6iRikoe
profile_of0Nee4laith8odaeLachoonu
profile_poh9eij4Choophaweiwev6eev
profile_poo3ipohGohThi9Cohverai7e
Sabatoge them! Get rid of all their intel files!
~/secret$ rm intel*
Nice! Once they are all gone, I think I can drop you a file of an exploit!
Just type "echo 'Drop it in!' " and we can give it a whirl!
~/secret$ echo 'Drop it in!'
Drop it in!
I placed a file in the executables folder as it looks like the only place we can execute from!
Run the script I wrote to have a little more impact on the system!
~/secret$ cd ..
~/$ cd executables
~/executables$ ls  
dontLookHere
~/executables$ ./dontLookHere
...
...
...
Looking through the text above, I think I have found the password. I am just having trouble with a username.
Oh drats! They are onto us! We could get kicked out soon!
Quick! Print the username to the screen so we can close are backdoor and log into the account directly!
You have to find another way other than echo!
~/executables$ whoami
l33th4x0r
Perfect! One second!
Okay, I think I have got what we are looking for. I just need to to copy the file to a place we can read.
Try copying the file called TopSecret in tmp directory into the passwords folder.
~/executables$ cp /tmp/TopSecret passwords
Server shutdown in 10 seconds...
Quick! go read the file before we lose our connection!
~/executables$ cd ..
~/$ ls
blackmail
executables
passwords
photos
secret
~/$ cd passwords
~/passwords$ ls
TopSecret
~/passwords$ cat TopSecret
Major General John M. Schofield's graduation address to the graduating class of 1879 at West Point is as follows: The discipline which makes the soldiers of a free country reliable in battle is not to be gained by harsh or tyrannical treatment.On the contrary, such treatment is far more likely to destroy than to make an army.It is possible to impart instruction and give commands in such a manner and such a tone of voice as to inspire in the soldier no feeling butan intense desire to obey, while the opposite manner and tone of voice cannot fail to excite strong resentment and a desire to disobey.The one mode or other of dealing with subordinates springs from a corresponding spirit in the breast of the commander.He who feels the respect which is due to others, cannot fail to inspire in them respect for himself, while he who feels,and hence manifests disrespect towards others, especially his subordinates, cannot fail to inspire hatred against himself.
picoCTF{CrUsHeD_It_9edaa84a}
```

### Flag
`picoCTF{CrUsHeD_It_9edaa84a}`
