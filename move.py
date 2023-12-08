
class Transform:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self) -> str:
        return f'({self.x}, {self.y})'

class Move:
    def __init__(self, piece_cords, transform, move_card):
        self.piece_cords = piece_cords
        self.transform = transform
        self.move_card = move_card
    def __repr__(self) -> str:
        return f'{self.piece} {self.transform} {self.move_card}'

class MoveCard:
    def __init__(self, name, transforms):
        self.name = name
        self.transforms = transforms
        self.transforms_flipped = [Transform(-t.x, -t.y) for t in self.transforms]

    def __str__(self) -> str:
        return f'{self.name}: {self.transforms}'

def generate_move_cards():
    ret = []
    ret.append(MoveCard('Tiger', [Transform(0, 2), Transform(0, -1)]))
    ret.append(MoveCard('Horse', [Transform(-1, 0), Transform(0, 1), Transform(0, -1)]))
    ret.append(MoveCard('Ox', [Transform(1, 0), Transform(0, 1), Transform(0, -1)]))
    ret.append(MoveCard('Frog', [Transform(-2, 0), Transform(-1, 1), Transform(1, -1)]))
    ret.append(MoveCard('Crab', [Transform(-2, 0), Transform(0, 1), Transform(2, 0)]))
    ret.append(MoveCard('Elephant', [Transform(-1, 1), Transform(1, 0), Transform(1, 1), Transform(-1, 0)]))
    ret.append(MoveCard('Goose', [Transform(-1, 1), Transform(1, 0), Transform(-1, 0), Transform(1, -1)]))
    ret.append(MoveCard('Monkey', [Transform(-1, 1), Transform(1, 1), Transform(-1, -1), Transform(1, -1)]))
    ret.append(MoveCard('Rooster', [Transform(-1, 0), Transform(1, 0), Transform(-1, -1), Transform(1, 1)]))
    ret.append(MoveCard('Dragon', [Transform(-2, 1), Transform(-1, -1), Transform(1, -1), Transform(2, 1)]))
    ret.append(MoveCard('Mantis', [Transform(-1, 1), Transform(0, -1), Transform(1, 1)]))
    ret.append(MoveCard('Eel', [Transform(-1, 1), Transform(-1, -1), Transform(1, 0)]))
    ret.append(MoveCard('Cobra', [Transform(-1, 0), Transform(1, 1), Transform(1, -1)]))
    ret.append(MoveCard('Rabbit', [Transform(-1, -1), Transform(1, 1), Transform(2, 0)]))
    ret.append(MoveCard('Crane', [Transform(-1, -1), Transform(1, -1), Transform(0, 1)]))
    return ret

all_move_crads = generate_move_cards()



