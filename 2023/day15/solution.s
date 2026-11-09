    .section __TEXT,__text
    .globl _main
    .p2align 2
_main:
    stp x29, x30, [sp, #-48]!
    mov x29, sp
    stp x19, x20, [sp, #16]
    stp x21, x22, [sp, #32]
    mov x19, #0
    mov x20, #0
    mov x21, #17
next_char:
    bl _getchar
    cmn w0, #1
    b.eq finish
    cmp w0, #','
    b.eq end_step
    cmp w0, #'\n'
    b.eq next_char
    add x20, x20, x0
    mul x20, x20, x21
    and x20, x20, #0xff
    b next_char
end_step:
    add x19, x19, x20
    mov x20, #0
    b next_char
finish:
    add x19, x19, x20
    adrp x0, Lout@PAGE
    add x0, x0, Lout@PAGEOFF
    sub sp, sp, #16
    str x19, [sp]
    bl _printf
    add sp, sp, #16
    mov w0, #0
    ldp x21, x22, [sp, #32]
    ldp x19, x20, [sp, #16]
    ldp x29, x30, [sp], #48
    ret

    .section __TEXT,__cstring
Lout:
    .asciz "%ld\n"
