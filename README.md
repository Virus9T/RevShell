### Python Reverse Shell

A simple reverse shell implementation in Python for educational and penetration testing purposes. This tool consists of two scripts: a **client** (reverse shell) and a **server** (command listener), which enables remote command execution.

---

## ⚠️ Disclaimer

> This project is **intended for educational and ethical penetration testing** purposes only.  
> **Do not** use this code on any system you do not own or have explicit permission to test.  
> Unauthorized access to systems is illegal and punishable under various cyber laws.  
> The author is **not responsible** for any misuse or damage caused by this tool.

---


##  Requirements

- Python 3.x
- Works on Linux, macOS, and Windows (may require some permissions on target system)
- pyinstaller (if need to convert into windows executable)

---

### Using method with examle:

## Run on Server Side:
$ Shell_server.py

## Run on Target Side:
$ Reverse_shell.py

### Note

if you want to make the rever shell in to windows executable(.exe) then use commans

$ pip3 install pyinstaller
$ pyinstaller --onefile Reverse_shell.py
