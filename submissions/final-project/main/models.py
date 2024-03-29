from main import db
    
class Website(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    website = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(150))
    
    def __repr__(self):
        return '<Website %r>' % self.website