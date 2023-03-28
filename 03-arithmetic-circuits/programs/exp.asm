; Exponentiation (a^b) with Fixed Exponent
set r1 0x02  ; sets r1 to base (a)
set r2 0x03  ; sets r2 to exponent (b)
set r3 0x01  ; sets r3 to result (initially 1)

; Exponentiation loop (unrolled since we don't support loops yet)
mul r3 r3 r1 ; r3 = r3 * r1
mul r3 r3 r1 ; r3 = r3 * r1
mul r3 r3 r1 ; r3 = r3 * r1
