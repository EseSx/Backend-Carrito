# --- Hashing/Codificado de Bcript ---
import bcrypt

# ------------------------
# Generar hash de contraseña
# ------------------------


def hash_password(plain_password: str) -> bytes:
    """
    Hashea una contraseña en texto plano.
    Retorna el hash generado (bytes).
    """
    hashed = bcrypt.hashpw(plain_password.encode("utf-8"), bcrypt.gensalt())
    return hashed


# ------------------------
# Verificar contraseña ingresada
# ------------------------


def verify_password(plain_password: str, hashed_password: bytes) -> bool:
    """
    Verifica si la contraseña en texto plano coincide con el hash almacenado.
    """
    return bcrypt.checkpw(plain_password.encode("utf-8"), hashed_password)
