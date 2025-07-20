import os
import re
import openai
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY not found in .env file.")

client = openai.OpenAI(api_key=OPENAI_API_KEY)

# --- Game Variables ---
topic = "A day at the zoo"
prompt = (
    "You are a caveman who can only use words with one beat (one syllable). "
    "Tell a short story about the topic below. Do NOT use words with more than one beat. "
    "If you use a word with more than one beat, you lose.\n"
    "Topic: {topic}"
)

# --- Helper Functions ---
def count_syllables(word):
    # Simple syllable counter (not perfect, but works for most English words)
    word = word.lower()
    word = re.sub(r'[^a-z]', '', word)
    if len(word) == 0:
        return 0
    vowels = 'aeiouy'
    count = 0
    prev_char_was_vowel = False
    for char in word:
        is_vowel = char in vowels
        if is_vowel and not prev_char_was_vowel:
            count += 1
        prev_char_was_vowel = is_vowel
    # Remove silent 'e'
    if word.endswith('e') and count > 1:
        count -= 1
    return count

def find_multisyllabic_word(text):
    words = re.findall(r'\b\w+\b', text)
    for word in words:
        if count_syllables(word) > 1:
            return word
    return None

def get_story(topic, prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a caveman who can only use words with one syllable."},
            {"role": "user", "content": prompt.format(topic=topic)}
        ],
        max_tokens=100,
        temperature=0.7,
    )
    return response.choices[0].message.content.strip()

# --- Main Game Loop ---
MAX_TRIES = 3
tries = 0
while tries < MAX_TRIES:
    story = get_story(topic, prompt)
    print(f"\nBot's story:\n{story}\n")
    bad_word = find_multisyllabic_word(story)
    if bad_word:
        print(f'NO! *smash with stick* you said "{bad_word}". Try again.')
        tries += 1
    else:
        print('Good. Bot say nice words. You win game.')
        break
else:
    print('Bot not smart. Too dumb to play game. It stop now')