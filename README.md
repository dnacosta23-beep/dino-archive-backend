# Dino Archive Backend

The Dino Archive backend is a Flask API that stores dinosaur records in a local SQLite database.

## Technologies

- Python
- Flask
- Flask-SQLAlchemy
- Flask-CORS
- SQLite

## Features

- Store dinosaur records in a SQLite database
- Retrieve all dinosaurs
- Create new dinosaur records
- Return JSON responses for the React frontend


### GET /

Returns a message showing the API is running.

Example Response

```json
{
  "message": "Welcome to the Dino Archive API"
}
```

---

### GET /dinosaurs

Returns every dinosaur stored in the database.

---

### POST /dinosaurs

Creates a new dinosaur.

Example Request

```json
{
  "name": "Allosaurus",
  "species": "Allosaurus fragilis",
  "diet": "Carnivore",
  "period": "Late Jurassic",
  "location": "North America",
  "description": "A large carnivorous theropod dinosaur."
}
```

## How to Run

Clone the repository.

```bash
git clone YOUR-BACKEND-REPOSITORY-URL
```

Navigate into the project.

```bash
cd dino-archive-backend
```

Create a virtual environment.

```bash
python3 -m venv .venv
```

Activate the virtual environment.

macOS/Linux

```bash
source .venv/bin/activate
```

Windows

```bash
.venv\Scripts\activate
```

Install the required packages.

```bash
pip install -r requirements.txt
```

Seed the database.

```bash
python3 seed.py
```

Run the Flask server.

```bash
python3 app.py
```

The API will be available at:

```text
http://127.0.0.1:5000
```