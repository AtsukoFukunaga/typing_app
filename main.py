import tkinter
import random
import time

FONT = ('Arial', 20, 'bold')
WORD_LIST = [
    'the', 'of', 'to', 'and', 'in', 'is', 'it', 'you', 'that', 'he',
    'was', 'for', 'on', 'are', 'with', 'as', 'his', 'they', 'be', 'at',
    'one', 'have', 'this', 'from', 'or', 'had', 'by', 'hot', 'but', 'some',
    'what', 'there', 'we', 'can', 'out', 'other', 'were', 'all', 'your', 'when',
    'up', 'use', 'word', 'how', 'said', 'an', 'each', 'she', 'which', 'do',
    'their', 'time', 'if', 'will', 'way', 'about', 'many', 'then', 'them', 'would',
    'write', 'like', 'so', 'these', 'her', 'long', 'make', 'thing', 'see', 'him',
    'two', 'has', 'look', 'more', 'day', 'could', 'go', 'come', 'did', 'my',
    'sound', 'no', 'most', 'number', 'who', 'over', 'know', 'water', 'than', 'call',
    'first', 'people', 'may', 'down', 'side', 'been', 'now', 'find', 'any', 'new',
    'work', 'part', 'take', 'get', 'place', 'made', 'live', 'where', 'after', 'back',
    'little', 'only', 'round', 'man', 'year', 'came', 'show', 'every', 'good', 'me',
    'give', 'our', 'under', 'name', 'very', 'through', 'just', 'form', 'much', 'great',
    'think', 'say', 'help', 'low', 'line', 'before', 'turn', 'cause', 'same', 'mean',
    'differ', 'move', 'right', 'boy', 'old', 'too', 'does', 'tell', 'sentence', 'set',
    'three', 'want', 'air', 'well', 'also', 'play', 'small', 'end', 'put', 'home',
    'read', 'hand', 'port', 'large', 'spell', 'add', 'even', 'land', 'here', 'must',
    'big', 'high', 'such', 'follow', 'act', 'why', 'ask', 'men', 'change', 'went',
    'light', 'kind', 'off', 'need', 'house', 'picture', 'try', 'us', 'again', 'animal',
    'point', 'mother', 'world', 'near', 'build', 'self', 'earth', 'father', 'head', 'stand',
    'own', 'page', 'should', 'country', 'found', 'answer', 'school', 'grow', 'study', 'still',
    'learn', 'plant', 'cover', 'food', 'sun', 'four', 'thought', 'let', 'keep', 'eye',
    'never', 'last', 'door', 'between', 'city', 'tree', 'cross', 'since', 'hard', 'start',
    'might', 'story', 'saw', 'far', 'sea', 'draw', 'left', 'late', 'run', 'while',
    'press', 'close', 'night', 'real', 'life', 'few', 'stop', 'open', 'seem', 'together',
    'next', 'white', 'children', 'begin', 'got', 'walk', 'example', 'ease', 'paper', 'often',
    'always', 'music', 'those', 'both', 'mark', 'book', 'letter', 'until', 'mile', 'river',
    'car', 'feet', 'care', 'second', 'group', 'carry', 'took', 'rain', 'eat', 'room',
    'friend', 'began', 'idea', 'fish', 'mountain', 'north', 'once', 'base', 'hear', 'horse',
    'cut', 'sure', 'watch', 'color', 'face', 'wood', 'main', 'enough', 'plain', 'girl']


class TypingApp(tkinter.Tk):
    def __init__(self):
        super().__init__()

        self.score = 0
        self.start_time = None
        self.end_time = None
        self.words = random_words_list

        self.title('How fast can you type?')
        self.config(padx=10, pady=10, bg='#f7f5dd')
        self.bind('<space>', self.key_pressed)

        self.label_title = tkinter.Label(self, text='Type these words as fas as you can!', width=50, bg='#f7f5dd',
                                         font=FONT)
        self.label_title.grid(column=0, row=0)

        instruction = '''
        Type the words below, each followed by space. 
        The first word is always "start" to start the timer. It is not included in the word count.
        The timer automatically stops when there is no word left.
        '''

        self.label_instruction = tkinter.Label(self, text=instruction, width=50, wraplength=400, bg='#f7f5dd')
        self.label_instruction.grid(column=0, row=1, pady=10)

        self.label_words = tkinter.Label(self, text=f'{"    ".join(self.words)}', width=50, height=20, wraplength=500,
                                         font=FONT)
        self.label_words.grid(column=0, row=2, pady=10)

        self.entry_word = tkinter.Entry(width=15, font=FONT)
        self.entry_word.grid(column=0, row=3, pady=10)

        self.button_exit = tkinter.Button(self, text='Exit', font=FONT, command='exit')
        self.button_exit.grid(column=0, row=4, pady=10)

    def key_pressed(self, event=None):
        word_to_type = self.words[0]
        if word_to_type == 'start':
            self.start_time = time.time()
            print(self.start_time)
        else:
            if self.entry_word.get().strip() == word_to_type:
                self.score += 1
        self.words.remove(word_to_type)
        self.label_words.config(text='    '.join(self.words))
        if len(self.words) == 0:
            self.end_time = time.time()
            print(self.end_time)
            time_taken = round((self.end_time - self.start_time) / 60, 2)
            rate = round(self.score / time_taken, 2)
            self.label_words.config(text=f'You typed {self.score} words correctly in {time_taken} min.\n '
                                    f'Your typing speed is {rate} words/min.')
        self.entry_word.delete(0, 'end')


random_words_list = random.sample(WORD_LIST, 101)
random_words_list[0] = 'start'

if __name__ == '__main__':
    app = TypingApp()
    app.mainloop()
