# CONSTANTS

DIGITS =  '0123456789'

# TOKENS

TT_INT = 'TT_INT'
TT_FLOAT = 'FLOAT'
TT_PLUS = 'PLUS'
TT_MINUS = 'MINUS'
TT_MUL = 'MUL'
TT_DIV = 'DIV'
TT_LPAREN = 'LAPREN'
TT_RPAREN = 'RAPREN'


class Token:
    def __init__(self, type_, value=None):
        self.type = type_
        self.value = value

    def __repr__(self):
        if self.value: return f'{self.type}:{self.value}'
        return f'{self.type}'

# ERROR
class Error:
    def __init__(self, error_name, details):
        self.error_name = error_name
        self.details = details

    def as_string(self):
        result = f'{self.error_name}: {self.details}'
        return result

class IllegalCharError(Error):
    def __init__(self, details):
        super().__init__('Illegal Character', details)  


# LEXER

class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = -1
        self.current_char = None
        self.adanvace()

    def adanvace(self):
        self.pos += 1
        self.current_char = self.text[self.pos] if self.pos < len(self.text) else None 
    
    def make_tokens(self):
        tokens = []

        while self.current_char != None:

            if self.current_char in ' \t':
                self.adanvace()
            elif self.current_char in DIGITS:
                tokens.append(self.make_number())
            elif self.current_char == '+':
                tokens.append(Token(TT_PLUS))
                self.adanvace()
            elif self.current_char == '-':
                tokens.append(Token(TT_MINUS))
                self.adanvace()
            elif self.current_char == '*':
                tokens.append(Token(TT_MUL))
                self.adanvace()
            elif self.current_char == '/':
                tokens.append(Token(TT_DIV))
                self.adanvace()
            elif self.current_char == '(':
                tokens.append(Token(TT_LPAREN))
                self.adanvace()
            elif self.current_char == ')':
                tokens.append(Token(TT_RPAREN))
                self.adanvace()
            else:
                #return some error if the character that not found
                char = self.current_char
                self.adanvace()
                return [], IllegalCharError("'" + char + "'")


        return tokens, None

    def make_number(self):
        num_str = ''
        dot_count = 0

        while self.current_char != None and self.current_char in DIGITS + '.':
            if self.current_char == '.':
                if dot_count == 1:
                     break
                dot_count += 1
                num_str += '.'
            else:
                num_str += self.current_char
            self.adanvace()

        if dot_count == 0:
            return Token(TT_INT, int(num_str))
        else:
            return Token(TT_FLOAT, float(num_str))

# RUN

def run(text):
    lexer = Lexer(text)
    tokens, error = lexer.make_tokens()

    return tokens, error