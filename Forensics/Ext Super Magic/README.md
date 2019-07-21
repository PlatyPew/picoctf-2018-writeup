# Ext Super Magic
Points: 250

## Category
Forensics

## Question
>We salvaged a ruined Ext SuperMagic II-class mech recently and pulled the [filesystem](files/ext-super-magic.img) out of the black box. It looks a bit corrupted, but maybe there's something interesting in there. You can also find it in /problems/ext-super-magic_4_f196e59a80c3fdac37cc2f331692ef13 on the shell server. 

### Hint
>Are there any [tools](https://en.wikipedia.org/wiki/Fsck) for diagnosing corrupted filesystems? What do they say if you run them on this one?
>
>How does a linux machine know what [type](https://www.garykessler.net/library/file_sigs.html) of file a [file](https://linux.die.net/man/1/file) is?
>
>You might find this [doc](http://www.nongnu.org/ext2-doc/ext2.html) helpful.
>
>Be careful with [endianness](https://en.wikipedia.org/wiki/Endianness) when making edits.
>
>Once you've fixed the corruption, you can use /sbin/[debugfs](https://linux.die.net/man/8/debugfs) to pull the flag file out.

## Solution
To do.

### Flag
`picoCTF{a7DB29eCf7dB9960f0A19Fdde9d00Af0}`
