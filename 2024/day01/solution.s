    .section __TEXT,__text
    .globl _main
    .p2align 2
_main:
    stp x29, x30, [sp, #-48]!
    mov x29, sp
    stp x19, x20, [sp, #16]
    stp x21, x22, [sp, #32]
    adrp x19, left@PAGE
    add x19, x19, left@PAGEOFF
    adrp x20, right@PAGE
    add x20, x20, right@PAGEOFF
    mov x21, #0
read:
    adrp x0, Lin@PAGE
    add x0, x0, Lin@PAGEOFF
    sub sp, sp, #16
    add x1, x19, x21, lsl #3
    str x1, [sp]
    add x1, x20, x21, lsl #3
    str x1, [sp, #8]
    bl _scanf
    add sp, sp, #16
    cmp w0, #2
    b.ne sort
    add x21, x21, #1
    b read
sort:
    mov x0, x19
    mov x1, x21
    mov x2, #8
    adrp x3, compare@PAGE
    add x3, x3, compare@PAGEOFF
    bl _qsort
    mov x0, x20
    mov x1, x21
    mov x2, #8
    adrp x3, compare@PAGE
    add x3, x3, compare@PAGEOFF
    bl _qsort
    mov x22, #0
    mov x3, #0
sum:
    cmp x3, x21
    b.ge report
    ldr x4, [x19, x3, lsl #3]
    ldr x5, [x20, x3, lsl #3]
    subs x6, x4, x5
    cneg x6, x6, lt
    add x22, x22, x6
    add x3, x3, #1
    b sum
report:
    adrp x0, Lout@PAGE
    add x0, x0, Lout@PAGEOFF
    sub sp, sp, #16
    str x22, [sp]
    bl _printf
    add sp, sp, #16
    mov w0, #0
    ldp x21, x22, [sp, #32]
    ldp x19, x20, [sp, #16]
    ldp x29, x30, [sp], #48
    ret

compare:
    ldr x0, [x0]
    ldr x1, [x1]
    cmp x0, x1
    cset w2, gt
    csetm w3, lt
    orr w0, w2, w3
    ret

    .section __TEXT,__cstring
Lin:
    .asciz "%ld %ld"
Lout:
    .asciz "%ld\n"

    .zerofill __DATA,__bss,left,16384,3
    .zerofill __DATA,__bss,right,16384,3
