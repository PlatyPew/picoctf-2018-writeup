# assembly-2
Points: 250

## Category
Reversing

## Question
>What does asm2(0x7,0x28) return? Submit the flag as a hexadecimal value (starting with '0x'). NOTE: Your submission for this question will NOT be in the normal flag format. [Source](files/loop_asm_rev.S) located in the directory at /problems/assembly-2_4_f8bfecf223768f4cac035751390ea590. 

### Hint
>assembly [conditions](https://www.tutorialspoint.com/assembly_programming/assembly_conditions.htm)

## Solution
```asm
; [ebp + 0xc] = 0x28
; [ebp + 0x8] = 0x7

; [ebp - 0x4] = 0x28
; [ebp-0x8] = 0x7

; 0x7 < 0a1de
; [ebp - 0x4] = 0x29
; [ebp + 0x8] = 0x7d

; eax = 0x29
```

### Flag
``
