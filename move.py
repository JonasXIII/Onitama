
class Transform:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self) -> str:
        return f'({self.x}, {self.y})'
        
class Move:
    def __init__(self, name, transforms):
        self.name = name
        self.transforms = transforms
        self.flipped = [Transform(-t.x, -t.y) for t in self.transforms]

    def __str__(self) -> str:
        return f'{self.name}: {self.transforms}'

    def generate_moves():
    ret = []
    ret.append(Move('Tiger', [Transform(0, 2), Transform(0, -1)]))
    ret.append(Move('Horse', [Transform(-1, 0), Transform(0, 1), Transform(0, -1)]))
    ret.append(Move('Ox', [Transform(1, 0), Transform(0, 1), Transform(0, -1)]))
    ret.append(Move('Frog', [Transform(-2, 0), Transform(-1, 1), Transform(1, -1)]))
    ret.append(Move('Crab', [Transform(-2, 0), Transform(0, 1), Transform(2, 0)]))
    ret.append(Move('Elephant', [Transform(-1, 1), Transform(1, 0), Transform(1, 1), Transform(-1, 0)]))
    ret.append(Move('Goose', [Transform(-1, 1), Transform(1, 0), Transform(-1, 0), Transform(1, -1)]))
    ret.append(Move('Monkey', [Transform(-1, 1), Transform(1, 1), Transform(-1, -1), Transform(1, -1)]))
    ret.append(Move('Rooster', [Transform(-1, 0), Transform(1, 0), Transform(-1, -1), Transform(1, 1)]))
    ret.append(Move('Dragon', [Transform(-2, 1), Transform(-1, -1), Transform(1, -1), Transform(2, 1)]))
    ret.append(Move('Mantis', [Transform(-1, 1), Transform(0, -1), Transform(1, 1)]))
    ret.append(Move('Boar', [Transform(-1, 0), Transform(0, 1), Transform(1, 0)]))
    ret.append(Move('Eel', [Transform(-1, 1), Transform(-1, -1), Transform(1, 0)]))
    ret.append(Move('Cobra', [Transform(-1, 0), Transform(1, 1), Transform(1, -1)]))
    ret.append(Move('Rabbit', [Transform(-1, -1), Transform(1, 1), Transform(2, 0)]))
    ret.append(Move('Crane', [Transform(-1, -1), Transform(1, -1), Transform(0, 1)]))
    return ret

all_moves = generate_moves()



