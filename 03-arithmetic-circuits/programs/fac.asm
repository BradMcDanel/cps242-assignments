; Factorial (n!) with Fixed n
set r1 0x04  ; sets r1 to n (factorial input)
set r2 0x01  ; sets r2 to result (initially 1)
set r3 0x01  ; sets r3 to 1 (for decrementing)

; Factorial loop (assuming n = 4)
mul r2 r1 r2 ; r2 = r1 * r2 (4)
sub r1 r1 r3 ; r1 = r1 - 1 (3)

mul r2 r1 r2 ; r2 = r1 * r2 (12)
sub r1 r1 r3 ; r1 = r1 - 1 (2)

mul r2 r1 r2 ; r2 = r1 * r2 (24)
