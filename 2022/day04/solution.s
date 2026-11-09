    .section __TEXT,__text
    .globl _main
    .p2align 2
_main:
    stp x29, x30, [sp, #-64]!
    mov x29, sp
    stp x19, x20, [sp, #16]
    mov x19, #0
    add x20, x29, #32
loop:
    adrp x0, Lin@PAGE
    add x0, x0, Lin@PAGEOFF
    sub sp, sp, #32
    str x20, [sp]
    add x1, x20, #4
    str x1, [sp, #8]
    add x1, x20, #8
    str x1, [sp, #16]
    add x1, x20, #12
    str x1, [sp, #24]
    bl _scanf
    add sp, sp, #32
    cmp w0, #4
    b.ne report
    ldp w1, w2, [x20]
    ldp w3, w4, [x20, #8]
    cmp w1, w3
    b.gt check_other
    cmp w2, w4
    b.ge count
check_other:
    cmp w3, w1
    b.gt loop
    cmp w4, w2
    b.lt loop
count:
    add x19, x19, #1
    b loop
report:
    adrp x0, Lout@PAGE
    add x0, x0, Lout@PAGEOFF
    sub sp, sp, #16
    str x19, [sp]
    bl _printf
    add sp, sp, #16
    mov w0, #0
    ldp x19, x20, [sp, #16]
    ldp x29, x30, [sp], #64
    ret

    .section __TEXT,__cstring
Lin:
    .asciz "%d-%d,%d-%d"
Lout:
    .asciz "%ld\n"
