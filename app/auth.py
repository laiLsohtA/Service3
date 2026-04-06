from fastapi import Header, HTTPException
import jwt

SECRET = "segredo_super_simples"

def get_current_user(authorization: str = Header(...)):
    try:
        token = authorization.replace("Bearer ", "")
        payload = jwt.decode(token, SECRET, algorithms=["HS256"])
        return payload["id"]
    except Exception:
        raise HTTPException(status_code=401, detail="Token inválido")