from exts import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(11), nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self):
        return '<User %r>' % self.username

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    @staticmethod
    def get_all():
        return User.query.all()

    @staticmethod
    def get_by_id(id):
        return User.query.get(id)

    @staticmethod
    def get_by_username(username):
        return User.query.filter_by(username=username).first()

    @staticmethod
    def get_by_email(email):
        return User.query.filter_by(email=email).first()

    @staticmethod
    def get_by_phone(phone):
        return User.query.filter_by(phone=phone).first()

    @staticmethod
    def get_by_username_password(username, password):
        return User.query.filter_by(username=username, password=password).first()

    @staticmethod
    def get_by_email_password(email, password):
        return User.query.filter_by(email=email, password=password).first()

    @staticmethod
    def get_by_phone_password(phone, password):
        return User.query.filter_by(phone=phone, password=password).first()

    @staticmethod
    def get_by_username_email(username, email):
        return User.query.filter_by(username=username, email=email).first()
