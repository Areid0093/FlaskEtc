from myproject import db

class Puppy(db.Model):
    
    __tablename__ = 'puppies'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)
    owner = db.relationship('Owner',backref='puppy',uselist=False)
    
    def __init__(self,name):
        self.name = name
    
    def __repr__(self):
        if self.owner:
            return "Puppy name is %s and owner is %s" % (self.name,self.owner.name)
        else:
            return "Puppy name is %s and has no owner yet!" % (self.name)
         
class Owner(db.Model):
    
   __tablename__ = 'owners'
   id = db.Column(db.Integer,primary_key=True)
   name = db.Column(db.Text)
   puppy_id = db.Column(db.Integer,db.ForeignKey('puppies.id'))

   def __init__(self, name,puppy_id):
        self.name = name
        self.puppy_id = puppy_id
        
   def __repr__(self):
      return "Owner name: %s" % (self.name)