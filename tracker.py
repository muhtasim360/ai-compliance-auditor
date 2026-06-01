import json
import os
from dotenv import load_dotenv
from audit_logic import analyze_password

load_dotenv()

def main():
    try:
        with open("policy.txt", "r") as f:
            policy = f.read()
    except FileNotFoundError:
        print("Error: policy.txt missing.")
        return


    test_passwords = [
        "SecurePassword123!",
        "12345678901234",
        "VANYCS_Consultant_2026",
        "short",

    ]

    print("--- VANYCS Automated Compliance Audit ---\n")
    for pwd in test_passwords:
        print(f"Auditing: {pwd}")
        result = analyze_password(pwd, policy)

        data = json.loads(result)
        print(json.dumps(data, indent=2))
        print("-" * 30)

        if __name__ == "__main__":
            main()
