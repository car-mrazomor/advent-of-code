    .section __TEXT,__text
    .globl _main
    .p2align 2
_main:
    stp x29, x30, [sp, #-48]!
    mov x29, sp
    stp x19, x20, [sp, #16]
    stp x21, x22, [sp, #32]
    adrp x19, depths@PAGE
    add x19, x19, depths@PAGEOFF
    mov x20, #0
read:
    adrp x0, Lin@PAGE
    add x0, x0, Lin@PAGEOFF
    add x1, x19, x20, lsl #3
    sub sp, sp, #16
    str x1, [sp]
    bl _scanf
    add sp, sp, #16
    cmp w0, #1
    b.ne count
    add x20, x20, #1
    b read
count:
    mov x21, #0
    mov x22, #0
    mov x3, #1
loop:
    cmp x3, x20
    b.ge report
    ldr x4, [x19, x3, lsl #3]
    sub x5, x3, #1
    ldr x6, [x19, x5, lsl #3]
    cmp x4, x6
    cinc x21, x21, gt
    cmp x3, #3
    b.lt next
    sub x5, x3, #3
    ldr x6, [x19, x5, lsl #3]
    cmp x4, x6
    cinc x22, x22, gt
next:
    add x3, x3, #1
    b loop
report:
    mov x0, x21
    bl print
    mov x0, x22
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
    .asciz "%ld"
Lout:
    .asciz "%ld\n"

    .zerofill __DATA,__bss,depths,32768,3
