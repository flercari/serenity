from index import db, bcrypt


class User(db.Document):
    email = db.StringField(max_length=255, unique=True)
    password = db.StringField(max_length=255, required=True)

    @staticmethod
    def get_user_with_email_and_password(email, password):
        user = User.objects.get(email=email)
        if user and bcrypt.check_password_hash(user.password, password):
            return user
        else:
            return None
        
    def save(self, *args, **kwargs):
       
        if not self.id and self.password:
            self.password = bcrypt.generate_password_hash(self.password).decode('utf-8')
            print (self.password)
        super(User, self).save(*args, **kwargs)
