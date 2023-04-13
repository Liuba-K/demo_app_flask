import os
from werkzeug.security import generate_password_hash
from blog.app import app
from blog.models.database import db


@app.cli.command("create-admin")
def create_users():
    """
    Run in your terminal:
    flask create-admin
    > done! created users: <User #1 'admin'> <User #2 'james'>
    """
    from blog.models import User
    admin = User(username="admin", is_staff=True, email='dfsfbcv@email.com')
    admin.password = os.environ.get("ADMIN_PASSWORD") or "adminpass"

    db.session.add(admin)
    db.session.commit()
    print("done! created admin:", admin)

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        debug=True,
        #port=5010,
    )


