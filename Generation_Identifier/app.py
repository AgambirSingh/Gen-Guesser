from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
 ##use separate files for all arrays
# Generation keywords
GEN_Z_KEYWORDS = [
    "no cap", "mid", "slay", "low-key", "extra", "simp", "ghost", "flex", 
    "clout", "mood", "yeet", "stan", "slaps", "tea", "high-key", "deadass", 
    "periodt", "trash", "cringe", "sus", "vibe check", "on fleek", 
    "savage", "bussin", "snatched", "shook", "fam", "big yikes", "bet", 
    "for real", "say less", "go off", "pushing P", "drip", "ratio", "valid", 
    "heat", "receipts", "hits different", "chill vibes", "caught lacking", 
    "stay woke", "cancelled", "main character energy", "glow up", "straight up", 
    "it's giving", "stan", "extra", "guap", "shooketh","lit","bro"
]


BOOMER_KEYWORDS = [
    "groovy", "far out", "hip", "cool", "dig it", "right on", "boss", 
    "bread", "bread and butter", "hang loose", "square", "blast", 
    "happening", "cat", "daddy-o", "fab", "gear", "peachy keen", "solid", 
    "sweet", "rad", "killer", "awesome", "dynamite", "neat", "swell", 
    "good egg", "copacetic", "hunky-dory", "jive", "pad", "flip side", 
    "outta sight", "stoked", "jam", "all that jazz", "cool beans", "decked out", 
    "in the groove", "steady", "groove", "shindig", "right on time", "hip cat", 
    "upbeat", "ace", "smooth operator", "can you dig it?", "go-getter", 
    "swinger", "golden"
]


GEN_ALPHA_KEYWORDS = [
    "skibidi", "rizz", "core", "understood the assignment", "npc", 
    "unhinged", "main character energy", "touch grass", "ratio", "based", 
    "cheugy", "yassification", "chronically online", "feral", "goblin mode", 
    "coded", "kinnie", "hyperfix", "delulu", "situationship", "lowkey", 
    "highkey", "sussy", "amogus", "oof", "pog", "poggers", "sheesh", 
    "cracked", "bruh moment", "dog water", "sweaty", "yeet", "big brain", 
    "small brain", "main", "alt", "v-bucks", "glitch", "spawn", "afk", 
    "clutch", "combo", "xp", "gamer moment", "irl", "1v1 me", "skin", 
    "emote", "stan twitter", "pink sauce", "slay queen","fire","bruh"
]


def identify_generation(text):
    gen_z_match = any(word in text.lower() for word in GEN_Z_KEYWORDS)
    boomer_match = any(word in text.lower() for word in BOOMER_KEYWORDS)
    gen_alpha_match = any(word in text.lower() for word in GEN_ALPHA_KEYWORDS)
    
    generations = []
    if gen_z_match:
        generations.append("Gen Z")
    if boomer_match:
        generations.append("Boomer")
    if gen_alpha_match:
        generations.append("Gen Alpha")

    if not generations:
        return "Generation Unknown"
    return " and ".join(generations)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/identify', methods=['POST'])
def identify():
    data = request.json
    text = data.get('text', '')
    result = identify_generation(text)
    return jsonify({"generation": result})

if __name__ == '__main__':
    app.run(debug=True)