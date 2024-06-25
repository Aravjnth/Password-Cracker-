Password Cracker

## Overview

The Password Cracker is a Python-based tool designed to attempt to crack passwords using different techniques such as dictionary attacks and brute force attacks. This tool is intended for educational purposes and security testing only.

## Features

- Perform dictionary attacks using a list of potential passwords.
- Perform brute force attacks by trying all possible combinations within a specified character set.
- Supports customizable character sets and password lengths.
- Logs successful login attempts.
- Handles common errors gracefully.

## Requirements

- Python 3.x

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Aravjnth/Password-Cracker-.git
    cd password-cracker
    ```

2. Install the required dependencies (if any):
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the tool to perform a dictionary attack or brute force attack:
    ```bash
    python password_cracker.py -m <mode> -t <target> -u <username> -w <wordlist> -c <charset> -l <length>
    ```

    Replace `<mode>`, `<target>`, `<username>`, `<wordlist>`, `<charset>`, and `<length>` with the actual values.

### Example

Perform a dictionary attack on a target with a given username and wordlist:

```bash
python password_cracker.py -m dictionary -t target-site.com -u username -w wordlist.txt
```

Perform a brute force attack with a specific character set and length:

```bash
python password_cracker.py -m brute -t target-site.com -u username -c abc123 -l 6
```

## Options

- `-m, --mode`: Mode of operation (dictionary or brute).
- `-t, --target`: Target site or service.
- `-u, --username`: Username to crack the password for.
- `-w, --wordlist`: Path to the wordlist file (required for dictionary mode).
- `-c, --charset`: Character set to use for brute force attack (required for brute mode).
- `-l, --length`: Length of the password to attempt (required for brute mode).

## Legal Disclaimer

This tool is intended for educational purposes and ethical hacking only. Unauthorized use of this tool to attack targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state, and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or suggestions, feel free to contact me at  www.linkedin.com/in/aravinth-aj
