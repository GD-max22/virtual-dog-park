# Simple Dog Breed Wiki
dog_wiki = {
    "Labrador": {
        "origin": "Canada",
        "traits": "Friendly, outgoing, high energy"
    },
    "Poodle": {
        "origin": "Germany/France",
        "traits": "Intelligent, active, hypoallergenic"
    },
    "Bulldog": {
        "origin": "England",
        "traits": "Calm, courageous, friendly"
    }
}

def show_breed(name):
    if name in dog_wiki:
        print(f"Breed: {name}")
        print(f"Origin: {dog_wiki[name]['origin']}")
        print(f"  Traits: {dog_wiki[name]['traits']}")
    else:
        print("Breed not found.")

if __name__ == "__main__":
    show_breed("Labrador")
    show_breed("Poodle")