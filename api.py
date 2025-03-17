from fastapi import FastAPI
import random

app = FastAPI()

# Predefined joke list
jokes = [
    {"setup": "Why don’t programmers like nature?", "punchline": "It has too many bugs."},
    {"setup": "Why do Python programmers prefer dark mode?", "punchline": "Because light attracts bugs!"},
    {"setup": "What is a programmer’s favorite place to hang out?", "punchline": "The Foo Bar."},
    {"setup": "Why did the Pakistani cricket fan bring a ladder to the match?", "punchline": "Because he wanted to reach the top order!"},
    {"setup": "Why did the biryani refuse to fight?", "punchline": "Because it was too chicken!"},
    {"setup": "What did the samosa say to the ketchup?", "punchline": "You complete me!"},
    {"setup": "Why do Lahoris love food so much?", "punchline": "Because their stomachs have more storage than their phones!"},
    {"setup": "What’s Karachi’s favorite exercise?", "punchline": "Traffic dodging!"},
    {"setup": "Why did the chai cup get promoted?", "punchline": "Because it had steep experience!"},
    {"setup": "Why was the naan so good at cricket?", "punchline": "Because it had a lot of runs!"},
    {"setup": "Why did the Pakistani student bring a ladder to school?", "punchline": "Because he wanted to reach high grades!"},
    {"setup": "Why did the Karachi traffic light turn red?", "punchline": "Because it saw someone trying to cross!"},
    {"setup": "What do you call a Lahori who loves food?", "punchline": "A normal person!"},
    {"setup": "Why did the Pakistani smartphone user cry?", "punchline": "Because the load shedding took away his charging!"},
    {"setup": "What’s the fastest thing in Pakistan?", "punchline": "A Karachiite running to catch a bus!"},
    {"setup": "Why did the Pakistani student fail his math test?", "punchline": "Because he counted on his fingers but ran out of them!"},
    {"setup": "Why do Pakistanis love cricket so much?", "punchline": "Because it's the only thing that unites the whole country!"},
    {"setup": "Why did the Pakistani wedding take so long?", "punchline": "Because the photographer wouldn’t stop taking pictures!"},
    {"setup": "Why did the Pakistani uncle go to space?", "punchline": "Because he heard there was free chai on Mars!"},
    {"setup": "Why do Pakistani tailors make great politicians?", "punchline": "Because they know how to stitch stories together!"},
    {"setup": "Why was the Pakistani student excited for a blackout?", "punchline": "Because it meant no online class!"},
    {"setup": "Why did the Pakistani kid bring a spoon to school?", "punchline": "Because he heard about a spelling bee!"},
    {"setup": "Why did the Pakistani actor refuse to do a stunt?", "punchline": "Because he didn’t want to be the ‘fall guy’!"},
]

@app.get("/random_joke")
def get_random_joke():
    """Returns a random joke from the list."""
    joke = random.choice(jokes)
    return {"setup": joke["setup"], "punchline": joke["punchline"]}

@app.post("/add_joke")
def add_joke(setup: str, punchline: str):
    """Adds a new joke to the list."""
    new_joke = {"setup": setup, "punchline": punchline}
    jokes.append(new_joke)
    return {"message": "Joke added successfully!", "joke": new_joke}
