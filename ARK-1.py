alphabet ='0123456789bcdfghjkmnpqrstvwxz'

def indiceDansAlphabetARKBnF(caracArkBnf):
    if len(caracArkBnf) == 1 and caracArkBnf in alphabet:
        i = 0
        while i < len(alphabet):
            if alphabet[i] == caracArkBnf:
                    return i
            i += 1
    else:
        print('Cela n\'est pas un caractère de l\'alaphabet ARK BnF valide.')

class chaineArkBnf():
    def __init__(self, valeur=''):
        self.valeur = valeur

    def valider(self):
        caracInvalides = []
        for carac in self.valeur:
            if carac not in alphabet:
                caracInvalides.append(carac)
        if len(caracInvalides) == 0:
            return (True, 'La chaîne est valide au regard de l\'alphabet BnF.')
        else:
            return (False, 'La chaîne n\'est pas valide, les caractères %s ne figurent pas dans l\'alphabet BnF.' % str(set(caracInvalides)))

    def calculCaracControle(self):
        valide = self.valider()
        if valide[0] == True:
            addition = 0
            i = 0
            while i < len(self.valeur):
                addition += indiceDansAlphabetARKBnF(self.valeur[i]) * (i + 1)
                i += 1
            caracControle = alphabet[addition % 29]
            return caracControle
        else:
            return valide[1]
