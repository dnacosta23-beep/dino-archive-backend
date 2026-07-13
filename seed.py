from app import app, db, Dinosaur

starting_dinosaurs = [
    {
        "name": "Tyrannosaurus Rex",
        "species": "Tyrannosaurus rex",
        "diet": "Carnivore",
        "period": "Late Cretaceous",
        "location": "Western North America",
        "description": (
            "A large theropod dinosaur known for its powerful jaws, "
            "large skull, and relatively short arms."
        ),
    },
    {
        "name": "Triceratops",
        "species": "Triceratops horridus",
        "diet": "Herbivore",
        "period": "Late Cretaceous",
        "location": "North America",
        "description": (
            "A four-legged herbivore recognized by its large neck frill "
            "and three facial horns."
        ),
    },
    {
        "name": "Stegosaurus",
        "species": "Stegosaurus stenops",
        "diet": "Herbivore",
        "period": "Late Jurassic",
        "location": "Western North America",
        "description": (
            "A plated dinosaur with two rows of large plates along its "
            "back and spikes near the end of its tail."
        ),
    },
    {
        "name": "Velociraptor",
        "species": "Velociraptor mongoliensis",
        "diet": "Carnivore",
        "period": "Late Cretaceous",
        "location": "Central and Eastern Asia",
        "description": (
            "A relatively small feathered theropod with a curved claw "
            "on each hind foot."
        ),
    },
    {
        "name": "Brachiosaurus",
        "species": "Brachiosaurus altithorax",
        "diet": "Herbivore",
        "period": "Late Jurassic",
        "location": "North America",
        "description": (
            "A tall sauropod with longer front legs than back legs, "
            "giving its body an upward-sloping appearance."
        ),
    },
    {
        "name": "Oviraptor",
        "species": "Oviraptor philoceratops",
        "diet": "Omnivore",
        "period": "Late Cretaceous",
        "location": "Mongolia",
        "description": (
            "A feathered theropod with a toothless beak that may have "
            "eaten plants, small animals, and eggs."
        ),
    },
]


with app.app_context():
    db.drop_all()
    db.create_all()

    dinosaurs = [
        Dinosaur(
            name=item["name"],
            species=item["species"],
            diet=item["diet"],
            period=item["period"],
            location=item["location"],
            description=item["description"],
        )
        for item in starting_dinosaurs
    ]

    db.session.add_all(dinosaurs)
    db.session.commit()

    print(f"Added {len(dinosaurs)} dinosaurs to the database.")