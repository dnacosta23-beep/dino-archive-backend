from flask import Flask, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)

# Configure SQLite database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///dinosaurs.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)



# Database Model

class Dinosaur(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    species = db.Column(db.String(150), nullable=False)
    diet = db.Column(db.String(50), nullable=False)
    period = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "species": self.species,
            "diet": self.diet,
            "period": self.period,
            "location": self.location,
            "description": self.description,
        }



# Home Route

@app.route("/")
def home():
    return {
        "message": "Welcome to the Dino Archive API"
    }



# GET All Dinosaurs

@app.route("/dinosaurs", methods=["GET"])
def get_dinosaurs():
    dinosaurs = db.session.execute(
        db.select(Dinosaur).order_by(Dinosaur.name)
    ).scalars().all()

    return [dinosaur.to_dict() for dinosaur in dinosaurs]



# POST New Dinosaur

@app.route("/dinosaurs", methods=["POST"])
def create_dinosaur():
    data = request.get_json()

    if not data:
        return {
            "error": "Request body must contain JSON data."
        }, 400

    required_fields = [
        "name",
        "species",
        "diet",
        "period",
        "location",
        "description",
    ]

    # Check that every required field exists and isn't empty
    for field in required_fields:
        value = data.get(field)

        if not value or not str(value).strip():
            return {
                "error": f"{field.capitalize()} is required."
            }, 400

    allowed_diets = [
        "Herbivore",
        "Carnivore",
        "Omnivore",
    ]

    if data["diet"] not in allowed_diets:
        return {
            "error": "Diet must be Herbivore, Carnivore, or Omnivore."
        }, 400

    new_dinosaur = Dinosaur(
        name=data["name"].strip(),
        species=data["species"].strip(),
        diet=data["diet"],
        period=data["period"].strip(),
        location=data["location"].strip(),
        description=data["description"].strip(),
    )

    db.session.add(new_dinosaur)
    db.session.commit()

    return new_dinosaur.to_dict(), 201

# Run the App

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)

