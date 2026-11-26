def signup(username: str, password: str) -> str:
    if not username or not username.strip():
        return "Error: Username cannot be empty."
    if len(password) < 6:
        return "Error: Password must contain at least 6 characters."
    return f"Signup Successful!\nUsername: {username}"


if __name__ == "__main__":
    username = "mohith"
    password = "Mohith.1436"
    print(signup(username, password))
