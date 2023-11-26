### Description:

`ASC2PET` is a tool for converting between `ASCII` and `PETSCII` representations of strings. It is designed to be called though the main script, but can also be run as a standalone file. Currently, this program can only operate on shared characters, but sequences for `PETSCII` only characters are planned.

---

### Usage:

`python3 asc2pet.py word [word2 ...]`

---

### Current Features:

- `ASCII -> PETSCII` for simple strings

- `PETSCII -> ASCII` for simple strings

---

### Planned Features:

- File-wise processing -- `-f=[FILE_NAME]` option
  
  - `.txt -> .pet` -- `-t=txt` modifier option
  
  - `.pet -> .txt` -- `-t=pet` modifier option

- `PETSCII` specific escape sequences -- will always be active

- In-script output redirection

---

### Credits:

`ASC2PET` created by Mike Hensley in 2023

Heavily inspired by `BasText`
