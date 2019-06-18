# Recovering From the Snap
Points: 150

## Category
Forensics

## Question
>There used to be a bunch of [animals](files/animals.dd) here, what did Dr. Xernon do to them? 

### Hint
>Some files have been deleted from the disk image, but are they really gone?.

## Solution
install photoRec [as per your OS and architecture]
```https://www.cgsecurity.org/wiki/TestDisk_Download```

run ```photoRec animals.dd```

<br>
It will recover 4 .JPG files
<br>
3 of them are animal photos and 4th one contains the flag.
<br>

### Flag
`picoCTF{th3_5n4p_happ3n3d}`