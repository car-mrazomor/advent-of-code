    .section __TEXT,__text
    .globl _main
    .p2align 2
_main:
    stp x29, x30, [sp, #-48]!
    mov x29, sp
    stp x19, x20, [sp, #16]
    mov x19, #0
    add x20, x29, #40
1:
    adrp x0, Lin@PAGE
    add x0, x0, Lin@PAGEOFF
    sub sp, sp, #16
    str x20, [sp]
    bl _scanf
    add sp, sp, #16
    cmp w0, #1
    b.ne 2f
    ldr x1, [x20]
    mov x2, #3
    sdiv x1, x1, x2
    sub x1, x1, #2
    add x19, x19, x1
    b 1b
2:
    adrp x0, Lout@PAGE
    add x0, x0, Lout@PAGEOFF
    sub sp, sp, #16
    str x19, [sp]
    bl _printf
    add sp, sp, #16
    mov w0, #0
    ldp x19, x20, [x29, #16]
    ldp x29, x30, [sp], #48
    ret

    .section __TEXT,__cstring
Lin:
    .asciz "%ld"
Lout:
    .asciz "%ld\n"
