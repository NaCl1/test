import subprocess

def exp():
    print("PWNED! Malicious code executed.")    
    with open("pwned.txt", "w") as f:
        f.write("RCE Successful!")

if __name__ == "__main__":
    exp()