    .section __TEXT,__text
    .globl _main
    .p2align 2
_main:
    stp x29, x30, [sp, #-48]!
    mov x29, sp
    stp x19, x20, [sp, #16]
    stp x21, x22, [sp, #32]
    mov x19, #50
    mov x20, #0
    mov x21, #0
    mov x22, #100
loop:
    adrp x0, Lin@PAGE
    add x0, x0, Lin@PAGEOFF
    sub sp, sp, #16
    adrp x1, dir@PAGE
    add x1, x1, dir@PAGEOFF
    str x1, [sp]
    adrp x1, clicks@PAGE
    add x1, x1, clicks@PAGEOFF
    str x1, [sp, #8]
    bl _scanf
    add sp, sp, #16
    cmp w0, #2
    b.ne report
    adrp x1, dir@PAGE
    ldrb w1, [x1, dir@PAGEOFF]
    adrp x2, clicks@PAGE
    ldr x2, [x2, clicks@PAGEOFF]
    cmp w1, #'R'
    b.ne left
    add x3, x19, x2
    udiv x4, x3, x22
    add x21, x21, x4
    msub x19, x4, x22, x3
    b check
left:
    cbz x19, left_from_zero
    cmp x2, x19
    b.lt turn_left
    sub x3, x2, x19
    udiv x4, x3, x22
    add x4, x4, #1
    add x21, x21, x4
    b turn_left
left_from_zero:
    udiv x4, x2, x22
    add x21, x21, x4
turn_left:
    udiv x4, x2, x22
    msub x5, x4, x22, x2
    subs x19, x19, x5
    b.ge check
    add x19, x19, #100
check:
    cmp x19, #0
    cinc x20, x20, eq
    b loop
report:
    mov x0, x20
    bl print
    mov x0, x21
    bl print
    mov w0, #0
    ldp x21, x22, [sp, #32]
    ldp x19, x20, [sp, #16]
    ldp x29, x30, [sp], #48
    ret

print:
    stp x29, x30, [sp, #-16]!
    mov x29, sp
    sub sp, sp, #16
    str x0, [sp]
    adrp x0, Lout@PAGE
    add x0, x0, Lout@PAGEOFF
    bl _printf
    add sp, sp, #16
    ldp x29, x30, [sp], #16
    ret

    .section __TEXT,__cstring
Lin:
    .asciz " %c%ld"
Lout:
    .asciz "%ld\n"

    .zerofill __DATA,__bss,dir,8,3
    .zerofill __DATA,__bss,clicks,8,3
