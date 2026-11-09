    .section __TEXT,__text
    .globl _main
    .p2align 2
_main:
    stp x29, x30, [sp, #-64]!
    mov x29, sp
    stp x19, x20, [sp, #16]
    stp x21, x22, [sp, #32]
    stp x23, x24, [sp, #48]
    adrp x19, nums@PAGE
    add x19, x19, nums@PAGEOFF
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
    b.ne pairs
    add x20, x20, #1
    b read
pairs:
    mov x21, #0
pair_i:
    cmp x21, x20
    b.ge triples
    add x22, x21, #1
pair_j:
    cmp x22, x20
    b.ge pair_next
    ldr x0, [x19, x21, lsl #3]
    ldr x1, [x19, x22, lsl #3]
    add x2, x0, x1
    cmp x2, #2020
    b.ne pair_skip
    mul x0, x0, x1
    bl print
    b triples
pair_skip:
    add x22, x22, #1
    b pair_j
pair_next:
    add x21, x21, #1
    b pair_i
triples:
    mov x21, #0
tri_i:
    cmp x21, x20
    b.ge done
    add x22, x21, #1
tri_j:
    cmp x22, x20
    b.ge tri_i_next
    add x23, x22, #1
tri_k:
    cmp x23, x20
    b.ge tri_j_next
    ldr x0, [x19, x21, lsl #3]
    ldr x1, [x19, x22, lsl #3]
    ldr x2, [x19, x23, lsl #3]
    add x3, x0, x1
    add x3, x3, x2
    cmp x3, #2020
    b.ne tri_k_next
    mul x0, x0, x1
    mul x0, x0, x2
    bl print
    b done
tri_k_next:
    add x23, x23, #1
    b tri_k
tri_j_next:
    add x22, x22, #1
    b tri_j
tri_i_next:
    add x21, x21, #1
    b tri_i
done:
    mov w0, #0
    ldp x23, x24, [sp, #48]
    ldp x21, x22, [sp, #32]
    ldp x19, x20, [sp, #16]
    ldp x29, x30, [sp], #64
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

    .zerofill __DATA,__bss,nums,8192,3
