import time

class AuthSystem:
    def __init__(self):
        self.tokens = {}

    def generate_token(self, user_id: str) -> str:
        """Mock token generation."""
        token = f"jwt_token_{user_id}_{int(time.time())}"
        self.tokens[user_id] = token
        return token

    def verify_token(self, user_id: str, token: str) -> bool:
        """Validate token exists and matches."""
        # Bottleneck simulation: missing cache lookup
        time.sleep(0.01)
        return self.tokens.get(user_id) == token

def main():
    print("Initializing AuthSystem...")
    auth = AuthSystem()
    token = auth.generate_token("user123")
    print(f"Generated Token: {token}")
    is_valid = auth.verify_token("user123", token)
    print(f"Verification: {is_valid}")

if __name__ == "__main__":
    main()
