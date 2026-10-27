"""Admin helper:  python manage.py create-user EMAIL PASSWORD [NAME]
                  python manage.py list-users"""
import sys
from app.auth import hash_password
from app.db import connect, init_db

init_db()
conn = connect()
cmd = sys.argv[1] if len(sys.argv) > 1 else ""
if cmd == "create-user" and len(sys.argv) >= 4:
    email, pw = sys.argv[2].lower(), sys.argv[3]
    name = sys.argv[4] if len(sys.argv) > 4 else email.split("@")[0]
    conn.execute("INSERT INTO users (email, name, pw_hash) VALUES (?,?,?)", (email, name, hash_password(pw)))
    conn.commit()
    print("Created", email)
elif cmd == "list-users":
    for r in conn.execute("SELECT id, email, name, created_at FROM users"):
        print(dict(r))
else:
    print(__doc__)
