"""Module de gestion des chaînes de caractères ARK BnF"""


import sys


ALPHABET = '0123456789bcdfghjkmnpqrstvwxz'

class InvalidCharError(Exception):
    def __init__(self, char):
        self.char = char

    def __str__(self):
        return repr(("La chaîne n'est pas valide, le caractère {} ne figure pas dans l'alphabet BnF.").format(self.char))
    
class InputLengthTooLongError(Exception):
    def __init__(self, str_len):
        self.len = str(str_len)
    
    def __str__(self):
        return repr(("La chaîne est trop longue pour être validée : {}").format(self.len))
    
class InputLengthTooShortError(Exception):
    def __init__(self, str_len):
        self.len = str(str_len)
    
    def __str__(self):
        return repr(("La chaîne est trop courte pour être validée : {}").format(self.len))


class ChaineARKBnF():
    """Classe principale de gestion des chaînes ARK BnF"""

    def __init__(self, valeur=''):
        """Constructeur

        Il définit l'attribut unique d'une chaîne de
        caractères ARK BnF : sa valeur."""
        self.valeur = valeur

    def valider(self):
        """Méthode de validation d'une chaîne

        Valide une chaine de caractère en se basant sur son caractère de contrôle"""
        unqualified_id = self.valeur[:-1]
        checksum_char = self.valeur[-1]

        try:
            return ChaineARKBnF(unqualified_id).calculer_controle() == checksum_char
        except Exception as e:
            return e

    def calculer_controle(self):
        """Méthode de calcul du caractère de contrôle

        Elle renvoie le caractère de contrôle si la chaîne est valide et
        gère les erreurs."""
        input_len = len(self.valeur)
        
        if input_len < 1:
            raise InputLengthTooShortError(input_len)
        if input_len > len(ALPHABET):
            raise InputLengthTooLongError(input_len)
        
        addition = 0
        
        for indice, carac in enumerate(self.valeur):
            try:
                addition += ALPHABET.index(carac) * (indice+1)
            except ValueError:
                raise InvalidCharError(carac)
                
        controle = ALPHABET[addition % 29]
        return controle

def main(args):
    """Fonction principale

    Elle calcule le caractère de contrôle de toute chaîne ARK BNF passée en
    argument."""
    valeur = args[1] if len(args) > 1 else "t3st"
    chaine = ChaineARKBnF(valeur)
    
    try:
        controle = chaine.calculer_controle()
        msg = "Pour {}, le caractère de contrôle est {}" 
        print(msg.format(valeur, controle))
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main(sys.argv)
