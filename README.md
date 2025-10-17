


## TOY-RSA-CLI

**Pure-Python RSA key-gen & encrypt/decrypt demo.**

This repository contains two beginner-friendly security & crypto demos you can fork, play with, and link on your CV:





### 🚀 Prerequisites

* Python 3.8+
* Sympy

  ```bash
  pip install sympy
  ```

### 📥 Installation

```bash
git clone https://github.com/Nehal-Ashraf-pr/Nehal-RSA-CLI.git
cd Nehal-RSA-CLI
```

### 💡 Usage

```bash
python rsa.py
```

Expected output:

```
🏃‍ Running quick 64-bit demo…
 • msg='Hi', recovered='Hi'
 64-bit self-test OK

🔑 Generating real 512-bit keypair…
 ✓e ✓p ✓q
Original message: 'Hello, RSA!'
Encrypted (hex, first 60 chars): 8f3a2d…
Decrypted message: 'Hello, RSA!'
RSA self-test passed!
```

### 🗂 What’s Inside

* **rsa.py**

  * `generate_key(k)` – RSA keypair via `randprime` + `mod_inverse`
  * `encrypt_int` / `decrypt_int` for numeric payloads
  * `str_to_int` / `int_to_str` for UTF-8 message support
  * built-in “64-bit quick demo” & “512-bit self-test” harness

---

## ⚖️ License

MIT © Nehal Ashraf

