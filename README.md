# picoCTF 2018 Writeup
This CTF was done with [@pauxy](https://github.com/pauxy) and [@StopDuckRoll](https://github.com/StopDuckRoll)

Special thanks to [@LFlare](https://github.com/LFlare) for helping out with a few challenges!

### Forensics writeups
Although it states that I may do some of the writeups for the forensics challenges, it's very unlikely it will ever be completed, mostly because those challenges were not solved by me, and I'm lazy. Pull requests are welcomed!

# Content Page
- [Binary Exploitation](#binary-exploitation)
- [Cryptography](#cryptography)
- [Forensics](#forensics)
- [General Skills](#general-skills)
- [Reversing](#reversing)
- [Web Exploitation](#web-exploitation)

## Binary Exploitation
<table>
    <thead>
        <tr class="header">
            <th>Challenges</th>
            <th>Points</th>
            <th>Status</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td markdown="span"><a href="Binary%20Exploitation/buffer%20overflow%200">buffer overflow 0</a></td>
            <td markdown="span">150</td>
            <td markdown="span">Solved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Binary%20Exploitation/buffer%20overflow%201">buffer overflow 1</a></td>
            <td markdown="span">200</td>
            <td markdown="span">Solved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Binary%20Exploitation/leak-me">leak-me</a></td>
            <td markdown="span">200</td>
            <td markdown="span">Solved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Binary%20Exploitation/shellcode">shellcode</a></td>
            <td markdown="span">200</td>
            <td markdown="span">Solved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Binary%20Exploitation/buffer%20overflow%202">buffer overflow 2</a></td>
            <td markdown="span">250</td>
            <td markdown="span">Solved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Binary%20Exploitation/got-2-learn-libc">got-2-learn-libc</a></td>
            <td markdown="span">250</td>
            <td markdown="span">Solved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Binary%20Exploitation/echooo">echooo</a></td>
            <td markdown="span">300</td>
            <td markdown="span">Solved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Binary%20Exploitation/authenticate">authenticate</a></td>
            <td markdown="span">350</td>
            <td markdown="span">Solved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Binary%20Exploitation/got-shell%3F">got-shell?</a></td>
            <td markdown="span">350</td>
            <td markdown="span">Solved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Binary%20Exploitation/rop%20chain">rop chain</a></td>
            <td markdown="span">350</td>
            <td markdown="span">Solved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Binary%20Exploitation/buffer%20overflow%203">buffer overflow 3</a></td>
            <td markdown="span">450</td>
            <td markdown="span">Unsolved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Binary%20Exploitation/echo%20back">echo back</a></td>
            <td markdown="span">500</td>
            <td markdown="span">Unsolved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Binary%20Exploitation/are%20you%20root%3F">are you root?</a></td>
            <td markdown="span">550</td>
            <td markdown="span">Unsolved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Binary%20Exploitation/gps">gps</a></td>
            <td markdown="span">550</td>
            <td markdown="span">Unsolved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Binary%20Exploitation/can-you-gets-me">can-you-gets-me</a></td>
            <td markdown="span">650</td>
            <td markdown="span">Solved</td>
        </tr>
    </tbody>
</table>

## Cryptography
<table>
    <thead>
        <tr class="header">
            <th>Challenges</th>
            <th>Points</th>
            <th>Status</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td markdown="span"><a href="Cryptography/Crypto%20Warmup%201">Crypto Warmup 1</a></td>
            <td markdown="span">75</td>
            <td markdown="span">Solved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Cryptography/Crypto%20Warmup%202">Crypto Warmup 2</a></td>
            <td markdown="span">75</td>
            <td markdown="span">Solved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Cryptography/HEEEEEEERE%27S%20Johnny!">HEEEEEEERE'S Johnny!</a></td>
            <td markdown="span">100</td>
            <td markdown="span">Solved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Cryptography/caesar%20cipher%201">caesar cipher 1</a></td>
            <td markdown="span">150</td>
            <td markdown="span">Solved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Cryptography/hertz">hertz</a></td>
            <td markdown="span">150</td>
            <td markdown="span">Solved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Cryptography/blaise%27s%20cipher">blaise's cipher</a></td>
            <td markdown="span">200</td>
            <td markdown="span">Solved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Cryptography/hertz%202">hertz 2</a></td>
            <td markdown="span">200</td>
            <td markdown="span">Solved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Cryptography/Safe%20RSA">Safe RSA</a></td>
            <td markdown="span">250</td>
            <td markdown="span">Solved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Cryptography/caesar%20cipher%202">caesar cipher 2</a></td>
            <td markdown="span">250</td>
            <td markdown="span">Solved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Cryptography/rsa-madlibs">rsa-madlibs</a></td>
            <td markdown="span">250</td>
            <td markdown="span">Solved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Cryptography/SpyFi">SpyFi</a></td>
            <td markdown="span">300</td>
            <td markdown="span">Unsolved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Cryptography/Super%20Safe%20RSA">Super Safe RSA</a></td>
            <td markdown="span">350</td>
            <td markdown="span">Solved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Cryptography/Super%20Safe%20RSA%202">Super Safe RSA 2</a></td>
            <td markdown="span">425</td>
            <td markdown="span">Solved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Cryptography/Magic%20Padding%20Oracle">Magic Padding Oracle</a></td>
            <td markdown="span">450</td>
            <td markdown="span">Unsolved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Cryptography/Super%20Safe%20RSA%203">Super Safe RSA 3</a></td>
            <td markdown="span">600</td>
            <td markdown="span">Solved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Cryptography/James%20Brahm%20Returns">James Brahm Returns</a></td>
            <td markdown="span">700</td>
            <td markdown="span">Unsolved</td>
        </tr>
    </tbody>
</table>

## Forensics
<table>
    <thead>
        <tr class="header">
            <th>Challenges</th>
            <th>Points</th>
            <th>Status</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td markdown="span"><a href="Forensics/Forensics%20Warmup%201">Forensics Warmup 1</a></td>
            <td markdown="span">50</td>
            <td markdown="span">Solved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Forensics/Forensics%20Warmup%202">Forensics Warmup 2</a></td>
            <td markdown="span">50</td>
            <td markdown="span">Solved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Forensics/Desrouleaux">Desrouleaux</a></td>
            <td markdown="span">150</td>
            <td markdown="span">Solved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Forensics/Reading%20Between%20the%20Eyes">Reading Between the Eyes</a></td>
            <td markdown="span">150</td>
            <td markdown="span">Solved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Forensics/Recovering%20From%20the%20Snap">Recovering From the Snap</a></td>
            <td markdown="span">150</td>
            <td markdown="span">Solved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Forensics/admin%20panel">admin panel</a></td>
            <td markdown="span">150</td>
            <td markdown="span">Solved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Forensics/hex%20editor">hex editor</a></td>
            <td markdown="span">150</td>
            <td markdown="span">Solved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Forensics/Truly%20an%20Artist">Truly an Artist</a></td>
            <td markdown="span">200</td>
            <td markdown="span">Solved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Forensics/now%20you%20don%27t">now you don't</a></td>
            <td markdown="span">200</td>
            <td markdown="span">Solved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Forensics/Ext%20Super%20Magic">Ext Super Magic</a></td>
            <td markdown="span">250</td>
            <td markdown="span">Unsolved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Forensics/Lying%20Out">Lying Out</a></td>
            <td markdown="span">250</td>
            <td markdown="span">Solved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Forensics/What%27s%20My%20Name%3F">What's My Name?</a></td>
            <td markdown="span">250</td>
            <td markdown="span">Solved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Forensics/core">core</a></td>
            <td markdown="span">350</td>
            <td markdown="span">Unsolved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Forensics/Malware%20Shops">Malware Shops</a></td>
            <td markdown="span">400</td>
            <td markdown="span">Unsolved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Forensics/LoadSomeBits">LoadSomeBits</a></td>
            <td markdown="span">550</td>
            <td markdown="span">Solved</td>
        </tr>
    </tbody>
</table>

## General Skills
<table>
    <thead>
        <tr class="header">
            <th>Challenges</th>
            <th>Points</th>
            <th>Status</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td markdown="span"><a href="General%20Skills/General%20Warmup%201">General Skills 1</a></td>
            <td markdown="span">50</td>
            <td markdown="span">Solved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="General%20Skills/General%20Warmup%202">General Skills 2</a></td>
            <td markdown="span">50</td>
            <td markdown="span">Solved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="General%20Skills/General%20Warmup%203">General Skills 3</a></td>
            <td markdown="span">50</td>
            <td markdown="span">Solved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="General%20Skills/Resources">Resources</a></td>
            <td markdown="span">50</td>
            <td markdown="span">Solved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="General%20Skills/grep%201">grep 1</a></td>
            <td markdown="span">75</td>
            <td markdown="span">Solved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="General%20Skills/net%20cat">net cat</a></td>
            <td markdown="span">75</td>
            <td markdown="span">Solved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="General%20Skills/strings">strings</a></td>
            <td markdown="span">100</td>
            <td markdown="span">Solved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="General%20Skills/pipe">pipe</a></td>
            <td markdown="span">110</td>
            <td markdown="span">Solved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="General%20Skills/grep%202">grep 2</a></td>
            <td markdown="span">125</td>
            <td markdown="span">Solved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="General%20Skills/Aca-Shell-A">Aca-Shell-A</a></td>
            <td markdown="span">150</td>
            <td markdown="span">Solved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="General%20Skills/environ">environ</a></td>
            <td markdown="span">150</td>
            <td markdown="span">Solved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="General%20Skills/ssh-keyz">ssh-keyz</a></td>
            <td markdown="span">150</td>
            <td markdown="span">Solved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="General%20Skills/what%20base%20is%20this%3F">what base is this?</a></td>
            <td markdown="span">200</td>
            <td markdown="span">Solved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="General%20Skills/you%20can%27t%20see%20me">you can't see me</a></td>
            <td markdown="span">200</td>
            <td markdown="span">Solved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="General%20Skills/absolutely%20relative">absolutely relative</a></td>
            <td markdown="span">200</td>
            <td markdown="span">Solved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="General%20Skills/in%20out%20error">in out error</a></td>
            <td markdown="span">275</td>
            <td markdown="span">Solved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="General%20Skills/learn%20gdb">learn gdb</a></td>
            <td markdown="span">300</td>
            <td markdown="span">Solved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="General%20Skills/roulette">roulette</a></td>
            <td markdown="span">350</td>
            <td markdown="span">Solved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="General%20Skills/store">store</a></td>
            <td markdown="span">400</td>
            <td markdown="span">Solved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="General%20Skills/script%20me">script me</a></td>
            <td markdown="span">500</td>
            <td markdown="span">Solved (<a href="https://github.com/plusline">@plusline</a>)</td>
        </tr>
        <tr>
            <td markdown="span"><a href="General%20Skills/Dog%20or%20Frog">Dog or Frog</a></td>
            <td markdown="span">900</td>
            <td markdown="span">Unsolved</td>
        </tr>
    </tbody>
</table>

## Reversing
<table>
    <thead>
        <tr class="header">
            <th>Challenges</th>
            <th>Points</th>
            <th>Status</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td markdown="span"><a href="Reversing/Reversing%20Warmup%201">Reversing Warmup 1</a></td>
            <td markdown="span">50</td>
            <td markdown="span">Solved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Reversing/Reversing%20Warmup%202">Reversing Warmup 2</a></td>
            <td markdown="span">50</td>
            <td markdown="span">Solved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Reversing/assembly-0">assembly-0</a></td>
            <td markdown="span">150</td>
            <td markdown="span">Solved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Reversing/assembly-1">assembly-1</a></td>
            <td markdown="span">200</td>
            <td markdown="span">Solved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Reversing/be-quick-or-be-dead-1">be-quick-or-be-dead-1</a></td>
            <td markdown="span">200</td>
            <td markdown="span">Solved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Reversing/quackme">quackme</a></td>
            <td markdown="span">200</td>
            <td markdown="span">Solved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Reversing/assembly-2">assembly-2</a></td>
            <td markdown="span">250</td>
            <td markdown="span">Solved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Reversing/be-quick-or-be-dead-2">be-quick-or-be-dead-2</a></td>
            <td markdown="span">275</td>
            <td markdown="span">Solved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Reversing/be-quick-or-be-dead-3">be-quick-or-be-dead-3</a></td>
            <td markdown="span">350</td>
            <td markdown="span">Solved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Reversing/quackme%20up">quackme up</a></td>
            <td markdown="span">350</td>
            <td markdown="span">Unsolved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Reversing/Radix%27s%20Terminal">Radix's Terminal</a></td>
            <td markdown="span">400</td>
            <td markdown="span">Solved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Reversing/assembly-3">assembly-3</a></td>
            <td markdown="span">400</td>
            <td markdown="span">Solved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Reversing/keygen-me-1">keygen-me-1</a></td>
            <td markdown="span">400</td>
            <td markdown="span">Unsolved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Reversing/assembly-4">assembly-4</a></td>
            <td markdown="span">550</td>
            <td markdown="span">Solved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Reversing/special-pw">special-pw</a></td>
            <td markdown="span">600</td>
            <td markdown="span">Unsolved</td>
        </tr>
    </tbody>
</table>

## Web Exploitation
<table>
    <thead>
        <tr class="header">
            <th>Challenges</th>
            <th>Points</th>
            <th>Status</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td markdown="span"><a href="Web%20Exploitation%2FInspect%20Me">Inspect Me</a></td>
            <td markdown="span">125</td>
            <td markdown="span">Solved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Web%20Exploitation/Client%20Side%20is%20Still%20Bad">Client Side is Still Bad</a></td>
            <td markdown="span">150</td>
            <td markdown="span">Solved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Web%20Exploitation/Logon">Logon</a></td>
            <td markdown="span">150</td>
            <td markdown="span">Solved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Web%20Exploitation/Irish%20Name%20Repo">Irish Name Repo</a></td>
            <td markdown="span">200</td>
            <td markdown="span">Solved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Web%20Exploitation/Mr.%20Robots">Mr. Robots</a></td>
            <td markdown="span">200</td>
            <td markdown="span">Solved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Web%20Exploitation/No%20Login">No Login</a></td>
            <td markdown="span">200</td>
            <td markdown="span">Solved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Web%20Exploitation/Secret%20Agent">Secret Agent</a></td>
            <td markdown="span">200</td>
            <td markdown="span">Solved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Web%20Exploitation/Buttons">Buttons</a></td>
            <td markdown="span">250</td>
            <td markdown="span">Solved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Web%20Exploitation/The%20Vault">The Vault</a></td>
            <td markdown="span">250</td>
            <td markdown="span">Solved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Web%20Exploitation/Artisinal%20Handcrafted%20HTTP%203">Artisinal Handcrafted HTTP 3</a></td>
            <td markdown="span">300</td>
            <td markdown="span">Solved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Web%20Exploitation/Flaskcards">Flaskcards</a></td>
            <td markdown="span">350</td>
            <td markdown="span">Solved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Web%20Exploitation/fancy-alive-monitoring">fancy-alive-monitoring</a></td>
            <td markdown="span">400</td>
            <td markdown="span">Solved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Web%20Exploitation/Secure%20Logon">Secure Logon</a></td>
            <td markdown="span">500</td>
            <td markdown="span">Unsolved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Web%20Exploitation/Flaskcards%20Skeleton%20Key">Flaskcards Skeleton Key</a></td>
            <td markdown="span">600</td>
            <td markdown="span">Unsolved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Web%20Exploitation/Help%20Me%20Reset%202">Help Me Reset 2</a></td>
            <td markdown="span">600</td>
            <td markdown="span">Solved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Web%20Exploitation/A%20Simple%20Question">A Simple Question</a></td>
            <td markdown="span">650</td>
            <td markdown="span">Solved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="LambDash%203">LambDash 3</a></td>
            <td markdown="span">800</td>
            <td markdown="span">Unsolved</td>
        </tr>
    </tbody>
</table>
