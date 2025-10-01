from my_project.database import db
from sqlalchemy import ForeignKey


class CoachesContact(db.Model):
    __tablename__ = "coaches_contact"


    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    coach_id = db.Column(db.Integer, ForeignKey('coach.id'), unique=True, nullable=False)

    coaches = db    .relationship('Coach', back_populates= 'contact')

    def to_dict(self):
        return {
            "id": self.id,
            "phone": self.phone,
            "email": self.email,
            'coach_id': self.coach_id
        }
