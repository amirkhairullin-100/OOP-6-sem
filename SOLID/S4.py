import hashlib
import secrets

class PasswordHasher:
    @staticmethod
    def check_password(plain: str, hashed: str) -> bool:
        return hashlib.sha256(plain.encode()).hexdigest() == hashed

class TokenGenerator:
    @staticmethod
    def generate_token() -> str:
        return secrets.token_hex(32)

class SessionManager:
    @staticmethod
    def save_session(user_id: int, token: str):
        print(f"[DB] Сессия сохранена: user_id={user_id}, token={token[:8]}...")
        
def main():
    stored_hash = hashlib.sha256("secret".encode()).hexdigest()
    if PasswordHasher.check_password("secret", stored_hash):
        token = TokenGenerator.generate_token()
        SessionManager.save_session(42, token)
        print(f"Токен: {token[:8]}...")

if __name__ == "__main__":
    main()