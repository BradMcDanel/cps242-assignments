## Some notes on how ALU programs are formatted:
* Register names map to indexes as follow:
  * `r0 -> 00`
  * `r1 -> 01`
  * `r2 -> 10`
  * `r3 -> 11`
* Memory addresses are in hexadecimal, starting with `0x`
  * For instance, `load r0 0xa` means load the contents at address `10` to `r0`
* I suggest to first write down each instruction in binary before converting to hexadecimal (what Logisim expects)
  * Use a binary-to-hexadecimal converter (either in terminal or online) to save youserlf from making a mistake in this step! (you could even write a program to do this if you want)
* Remember to reset your data memory, registers, and PC after each execution of the program.
* You can edit memory files by hand if you prefer that to editing them in Logisim
  * Check out the `.mem` files in [programs/01-add-sub](https://github.com/BradMcDanel/cps242-assignments/tree/main/03-arithmetic-circuits/programs/01-add-sub)
  * These files are plaintext except for the first line which must contain `v2.0 raw`
* All numbers are in two's complement. So if you see a large number it is likely a small negative number!
