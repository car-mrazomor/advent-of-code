    .section __TEXT,__text
    .globl _main
    .p2align 2
_main:
    stp x29, x30, [sp, #-48]!
    mov x29, sp
    stp x19, x20, [sp, #16]
    stp x21, x22, [sp, #32]
    adrp x19, numbers@PAGE
    add x19, x19, numbers@PAGEOFF
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
    b.ne races
    add x20, x20, #1
    b read
races:
    mov x21, #1
    lsr x22, x20, #1
    mov x3, #0
race:
    cmp x3, x22
    b.ge report
    ldr x4, [x19, x3, lsl #3]
    add x5, x3, x22
    ldr x5, [x19, x5, lsl #3]
    mov x6, #0
    mov x7, #0
hold:
    cmp x6, x4
    b.gt race_done
    sub x8, x4, x6
    mul x8, x8, x6
    cmp x8, x5
    cinc x7, x7, gt
    add x6, x6, #1
    b hold
race_done:
    mul x21, x21, x7
    add x3, x3, #1
    b race
report:
    adrp x0, Lout@PAGE
    add x0, x0, Lout@PAGEOFF
    sub sp, sp, #16
    str x21, [sp]
    bl _printf
    add sp, sp, #16
    mov w0, #0
    ldp x21, x22, [sp, #32]
    ldp x19, x20, [sp, #16]
    ldp x29, x30, [sp], #48
    ret

    .section __TEXT,__cstring
Lin:
    .asciz "%*[^0-9]%ld"
Lout:
    .asciz "%ld\n"

    .zerofill __DATA,__bss,numbers,256,3
