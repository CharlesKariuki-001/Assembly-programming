# Week 1 — Assembly Programming Foundations

## What I Learned

This week focused on understanding the foundations behind Assembly Programming and how software interacts with computer hardware.

### 1. Low Level Programming

I learned that Assembly works much closer to the CPU than languages such as Python.

Instead of hiding the hardware, Assembly allows programmers to work with registers, memory and CPU instructions.

### 2. Number Systems

I learned about:

* Binary — base 2
* Decimal — base 10
* Hexadecimal — base 16

I also learned that:

```text
1 hexadecimal digit = 4 bits
1 byte = 8 bits
1 byte = 2 hexadecimal digits
```

For example:

```text
42 decimal
= 00101010 binary
= 0x2A hexadecimal
```

### 3. Data Representation

I learned about:

* Bits
* Bytes
* Words
* Doublewords
* Quadwords

I also learned how computers represent signed numbers using two's complement.

### 4. Registers

I learned that registers are small and very fast storage locations inside the CPU.

Important x86 registers include:

```text
EAX → calculations and results
EBX → general storage
ECX → counters
EDX → additional data
ESP → stack pointer
EBP → base pointer
EIP → instruction pointer
```

ESP and EIP are particularly important when studying memory corruption and program control flow.

### 5. Translation Pipeline

I learned that Assembly programs go through a basic process:

```text
Assembly Source
      ↓
Assembler
      ↓
Object File
      ↓
Linker
      ↓
Executable
      ↓
Loader
      ↓
Program Running
```

### 6. Security Connection

I learned that low level concepts are important in cybersecurity.

Understanding memory, registers, stacks, binary and hexadecimal helps security professionals analyze vulnerabilities, malware and compiled programs.

## Week 1 Build

### Byte Inspector

I built a small Python command line tool that:

* Converts decimal numbers to binary
* Converts decimal numbers to hexadecimal
* Converts text characters into numeric byte values
* Displays hexadecimal and binary representations
* Checks whether characters are printable ASCII

## What I Achieved

By the end of Week 1, I had a basic understanding of how computers represent data and how the CPU works with registers and memory.

I also completed my first practical project connected to the concepts learned.

## Next Week

I will continue with Assembly syntax, CPU instructions and basic operations.

**Status:** Completed
