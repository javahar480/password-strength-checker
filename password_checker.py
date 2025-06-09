import re
import socket

def print_banner():
    banner = r"""
    ***************************************
    *     PASSWORD STRENGTH CHECKER       *
    ***************************************
    """
    print(banner)

def get_ip_address():
    try:
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        print(f"[INFO] Local IP Address: {ip_address}")
    except Exception as e:
        print(f"[ERROR] Could not get IP Address: {e}")

def check_password_strength(password):
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    errors = {
        "Too short (minimum 8 characters)": length_error,
        "No digit": digit_error,
        "No uppercase letter": uppercase_error,
        "No lowercase letter": lowercase_error,
        "No special character": symbol_error
    }

    if any(errors.values()):
        print("[WEAK] Password failed the following checks:")
        for error, failed in errors.items():
            if failed:
                print(f" - {error}")
    else:
        print("[STRONG] Password meets all strength criteria.")

if __name__ == "__main__":
    print_banner()
    get_ip_address()
    password = input("Enter a password to check: ")
    check_password_strength(password)
