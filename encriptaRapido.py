import bcrypt

contraseña = "contraseñaDeLaAdministracion"

hashed = bcrypt.hashpw(contraseña.encode("utf-8"), bcrypt.gensalt())
hash_string = hashed.decode()

print(hash_string)
