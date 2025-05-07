from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

bmw_data = {
    "bmw m5 competition": {
        "keywords": ["m5", "bmw m5", "m5 competition", "bmw m5 competition"],
        "response": "BMW M5 Competition: A high-performance luxury sedan with a 4.4L V8 TwinPower Turbo engine producing 617 horsepower."
    },
    "bmw m3 competition": {
        "keywords": ["m3", "bmw m3", "m3 competition", "bmw m3 competition"],
        "response": "BMW M3 Competition: A sporty, high-performance sedan with a 3.0L TwinPower Turbo inline-6 engine producing 503 horsepower."
    },
    "bmw x5 m": {
        "keywords": ["x5 m", "bmw x5 m", "x5m"],
        "response": "BMW X5 M: A mid-size luxury SUV with a 4.4L V8 TwinPower Turbo engine producing over 600 horsepower."
    },
    "bmw m8 competition": {
        "keywords": ["m8", "bmw m8", "m8 competition", "bmw m8 competition"],
        "response": "BMW M8 Competition: A luxury coupe with a 4.4L TwinPower Turbocharged V8 engine delivering 617 horsepower."
    },
    "bmw z4 m40i": {
        "keywords": ["z4", "bmw z4", "z4 m40i", "bmw z4 m40i"],
        "response": "BMW Z4 M40i: A stylish and powerful two-seater roadster with a 3.0L inline-6 TwinPower Turbo engine producing 382 horsepower."
    },
    "bmw m2 competition": {
        "keywords": ["m2", "bmw m2", "m2 competition", "bmw m2 competition"],
        "response": "BMW M2 Competition: A compact, high-performance coupe with a 3.0L inline-6 TwinPower Turbo engine delivering 405 horsepower."
    },
    "bmw m4 competition": {
        "keywords": ["m4", "bmw m4", "m4 competition", "bmw m4 competition"],
        "response": "BMW M4 Competition: A dynamic, high-performance coupe featuring a 3.0L TwinPower Turbo inline-6 engine with 503 horsepower."
    },
    "bmw x6 m": {
        "keywords": ["x6 m", "bmw x6 m", "x6m"],
        "response": "BMW X6 M: A powerful, stylish SUV coupe powered by a 4.4L V8 TwinPower Turbo engine producing 600+ horsepower."
    },
    "bmw m6 gran coupe": {
        "keywords": ["m6", "bmw m6", "m6 gran coupe", "bmw m6 gran coupe"],
        "response": "BMW M6 Gran Coupe: A luxurious, high-performance four-door coupe with a 4.4L TwinPower Turbo V8 engine making 560 horsepower."
    },
    "bmw m550i xdrive": {
        "keywords": ["m550i", "bmw m550i", "m550i xdrive", "bmw m550i xdrive"],
        "response": "BMW M550i xDrive: A fast and refined sedan with a 4.4L TwinPower Turbo V8 engine producing 523 horsepower."
    },
    "bmw i8": {
        "keywords": ["i8", "bmw i8", "bmw i8 hybrid", "i8 hybrid"],
        "response": "BMW i8: A plug-in hybrid sports car with a sleek design, featuring a 1.5L turbocharged engine paired with an electric motor producing a combined 369 horsepower."
    },
    "bmw x7": {
        "keywords": ["x7", "bmw x7", "bmw x7 suv"],
        "response": "BMW X7: A full-size luxury SUV offering a combination of elegance, comfort, and performance with a range of engine options, including a 4.4L V8 TwinPower Turbo engine."
    },
    "bmw 7 series": {
        "keywords": ["7 series", "bmw 7 series", "bmw 7 series luxury"],
        "response": "BMW 7 Series: A luxury sedan with advanced technology and a range of powerful engines, including a 4.4L TwinPower Turbo V8."
    },
    "bmw 3 series": {
        "keywords": ["3 series", "bmw 3 series", "bmw 3 series sedan"],
        "response": "BMW 3 Series: A premium compact sedan known for its sporty handling and available with various engine options, including a 2.0L turbocharged inline-4."
    },

    # Additional BMW Models
    "bmw m1": {
        "keywords": ["m1", "bmw m1"],
        "response": "BMW M1: A legendary, mid-engine sports car produced in the late 1970s and early 1980s, known for its sharp handling and unique design."
    },
    "bmw 2 series": {
        "keywords": ["2 series", "bmw 2 series", "bmw 2 series coupe"],
        "response": "BMW 2 Series: A compact luxury coupe that offers sporty performance and agility with a range of turbocharged engines."
    },

    # Casual Greetings and Conversations
    "hi": {
        "keywords": ["hi", "hello", "hey", "hiya"],
        "response": "Hello! How can I assist you today?"
    },
    "how are you": {
        "keywords": ["how are you", "how's it going", "how do you do", "how's everything"],
        "response": "I'm doing great, thanks for asking! How about you?"
    },
    "bye": {
        "keywords": ["bye", "goodbye", "see you", "take care"],
        "response": "Goodbye! Have a great day!"
    },
    "thank you": {
        "keywords": ["thank you", "thanks", "appreciate it"],
        "response": "You're welcome! Let me know if you need anything else."
    },
    "you're welcome": {
        "keywords": ["you're welcome", "no problem", "don't mention it"],
        "response": "It's my pleasure to help!"
    },
    "help": {
        "keywords": ["help", "assist", "support"],
        "response": "How can I help you today? Let me know what you're looking for."
    },
    "what's your name": {
        "keywords": ["what's your name", "who are you", "what is your name"],
        "response": "I'm a BMW assistant here to help you with all things BMW! How can I assist you today?"
    },
    "i need information about bmw": {
        "keywords": ["bmw", "information about bmw", "bmw cars", "bmw models"],
        "response": "I can help with that! Just ask about any BMW model or feature, and I'll provide you with the details!"
    },
    "tell me about bmw m5": {
        "keywords": ["tell me about bmw m5", "bmw m5 details", "m5 specifications"],
        "response": "The BMW M5 is a high-performance sedan with a 4.4L V8 TwinPower Turbo engine, delivering 617 horsepower. It’s a perfect blend of luxury and performance."
    },
    "what's new in bmw m3": {
        "keywords": ["what's new in bmw m3", "bmw m3 updates", "bmw m3 new features"],
        "response": "The BMW M3 now comes with more aggressive styling, upgraded tech features, and even better performance thanks to its 3.0L TwinPower Turbo inline-6 engine."
    }
}



def get_response(user_input):
    user_input = user_input.lower()
    response = "Sorry, I couldn't understand. Please ask about a BMW model like 'M5 Competition' or 'X5 M'."

    for model, info in bmw_data.items():
        for keyword in info["keywords"]:
            if keyword in user_input:
                response = info["response"]
                return response
    return response

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def chat():
    user_input = request.json["message"]
    response = get_response(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
