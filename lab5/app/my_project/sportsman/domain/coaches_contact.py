from my_project.database import db


class Coach(db.Model):
    __tablename__ = "coach_contact"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50), nullable=False)
    coach_specialization_id = db.Column(db.Integer, db.ForeignKey('coach_specialization.id'))
    contact_id = db.Column(db.Integer, db.ForeignKey('coach_contact.id'))  # <--- add this

    contact = db.relationship('CoachesContact', back_populates='coaches')

    def to_dict(self):
        return {
            "id": self.id,
            "phone": self.phone,
            "email": self.email,
            "contact_id": self.contact_id,
        }
