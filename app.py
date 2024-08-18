import random
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Example comments data
comments = [
"Love this post! ❤️"
"Amazing content! Keep it up!"
"Wow, this is so inspiring!"
"Great job! 👏"
"This made my day! 😊"
"I totally agree with you!"
"Fantastic work!"
"This is so helpful, thanks for sharing!"
"You nailed it!"
"Such a great insight!"
"I can't stop watching this!"
"You're so talented!"
"Incredible! 🤩"
"This is awesome!"
"So true!"
"I'm loving this!"
"Absolutely brilliant!"
"You always post the best content!"
"This is gold!"
"I'm learning so much from you!"
"You're amazing!"
"Such a great perspective!"
"This is exactly what I needed today!"
"Thank you for sharing this!"
"You have such a creative mind!"
"This is fantastic!"
"I can't get enough of this!"
"You're a genius!"
"This is epic!"
"You always inspire me!"
"This is just perfect!"
"Keep up the great work!"
"So much talent in one post!"
"I'm obsessed with this!"
"This is next level!"
"You never cease to amaze me!"
"This is so beautiful!"
"You make it look so easy!"
"This is pure art!"
"I wish I could like this twice!"
"You're on fire!"
"This is so entertaining!"
"I'm so impressed!"
"Your content is always top-notch!"
"This is a game-changer!"
"You're killing it!"
"This is mind-blowing!"
"You always brighten my day!"
"This is simply amazing!"
"Your creativity knows no bounds!"
"This is so innovative!"
"You have a gift!"
"This is pure genius!"
"You're a rockstar!"
"This is so cool!"
"I'm blown away!"
"This is beyond awesome!"
"You have such a unique style!"
"This is so well done!"
"You always come up with the best ideas!"
"This is so refreshing!"
"You're a true artist!"
"This is so impressive!"
"I'm loving every bit of this!"
"This is so captivating!"
"You're a true inspiration!"
"This is so insightful!"
"I'm so glad I found your page!"
"This is absolutely stunning!"
"You're a natural!"
"This is pure perfection!"
"You have outdone yourself!"
"This is so well-executed!"
"I'm in awe of your talent!"
"This is so relatable!"
"You're a master at this!"
"This is just too good!"
"I'm addicted to your content!"
"This is so thoughtful!"
"You make it look so fun!"
"This is absolutely fantastic!"
"You're a wizard!"
"This is top-tier content!"
"I'm so inspired by you!"
"This is just what I needed!"
"You're a breath of fresh air!"
"This is so enlightening!"
"I'm so grateful for your content!"
"This is a masterpiece!"
"You have such a great eye for detail!"
"This is pure magic!"
"I'm always looking forward to your posts!"
"This is so engaging!"
"You're a trendsetter!"
"This is pure joy!"
"I'm so impressed by your work!"
"This is so heartwarming!"
"You're a legend!"
"This is so thought-provoking!"
"I'm so proud of you!"
"This is pure brilliance!"
"You have such a way with words!"
"This is so well-crafted!"
"You're a true visionary!"
"This is so mind-blowing!"
"I'm so inspired by this!"
"This is so motivating!"
"You're a true pioneer!"
"This is pure inspiration!"
"I'm so impressed with this!"
"This is so well-put!"
"You're a true leader!"
"This is so impactful!"
"I'm so grateful for this!"
"This is pure excellence!"
"You have such a unique voice!"
"This is so well-explained!"
"You're a true genius!"
"This is so informative!"
"I'm so in love with this!"
"This is pure class!"
"You have such a great sense of style!"
"This is so well-thought-out!"
"You're a true icon!"
"This is so eye-opening!"
"I'm so fascinated by this!"
"This is pure sophistication!"
"You have such a sharp mind!"
"This is so well-done!"
"You're a true maverick!"
"This is so enlightening!"
"I'm so drawn to this!"
"This is pure charm!"
"You have such a clear vision!"
"This is so well-presented!"
"You're a true trailblazer!"
"This is so revolutionary!"
"I'm so intrigued by this!"
"This is pure genius!"
"You have such a great perspective!"
"This is so well-structured!"
"You're a true innovator!"
"This is so empowering!"
"I'm so motivated by this!"
"This is pure gold!"
"You have such a clear understanding!"
"This is so well-developed!"
"You're a true mastermind!"
"This is so uplifting!"
"I'm so energized by this!"
"This is pure wisdom!"
"You have such a profound insight!"
"This is so well-conceived!"
"You're a true prodigy!"
"This is so inspiring!"
"I'm so encouraged by this!"
"This is pure enlightenment!"
"You have such a deep knowledge!"
"This is so well-reasoned!"
"You're a true scholar!"
"This is so illuminating!"
"I'm so enlightened by this!"
"This is pure clarity!"
"You have such a thorough understanding!"
"This is so well-analyzed!"
"You're a true expert!"
"This is so thought-out!"
"I'm so impressed by your insight!"
"This is pure insight!"
"You have such a comprehensive view!"
"This is so well-researched!"
"You're a true professional!"
"This is so expertly crafted!"
"I'm so amazed by your expertise!"
"This is pure knowledge!"
"You have such an expert grasp!"
"This is so well-structured!"
"You're a true savant!"
"This is so articulate!"
"I'm so impressed by your understanding!"
"This is pure brilliance!"
"You have such a clear grasp!"
"This is so precise!"
"You're a true maestro!"
"This is so well-executed!"
"I'm so impressed by your proficiency!"
"This is pure talent!"
"You have such a masterful approach!"
"This is so flawlessly done!"
"You're a true virtuoso!"
"This is so impeccably crafted!"
"I'm so impressed by your skill!"
"This is pure artistry!"
"You have such an exceptional talent!"
]

# Tokenize comments
words = [comment.split() for comment in comments]

# Create a dictionary of transitions
transitions = {}
for comment in words:
    for i in range(len(comment) - 1):
        current_word = comment[i]
        next_word = comment[i + 1]
        if current_word in transitions:
            transitions[current_word].append(next_word)
        else:
            transitions[current_word] = [next_word]

# Function to generate comments
def generate_comment(seed_word, next_words):
    current_word = seed_word
    generated_comment = seed_word
    for _ in range(next_words):
        if current_word in transitions:
            next_word = random.choice(transitions[current_word])
            generated_comment += " " + next_word
            current_word = next_word
        else:
            break
    return generated_comment

# API endpoint to generate comments
@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    seed_word = data.get('seed_word')
    next_words = int(data.get('next_words', 5))  # Convert next_words to integer
    
    if not seed_word:
        return jsonify({'error': 'seed_word is required'}), 400
    
    generated_comment = generate_comment(seed_word, next_words)
    return jsonify({'generated_comment': generated_comment})

# Serve the web interface
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5001)





