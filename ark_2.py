"""Module de gestion des ark"""
import sys


class ChaineArkBnf():
    """Classe de gestion des identifiants ARK BnF"""

    ALPHABET = '0123456789bcdfghjkmnpqrstvwxz'

    @staticmethod
    def trouver_indice(carac):
        """Trouve l'indice du caractère dans l'alphabet à 29 lettres"""
        if len(carac) != 1:
            msg = "Il faut fournir un seul caractère :{}".format(carac)
            raise ValueError(msg)
        try:
            return ChaineArkBnf.ALPHABET.index(carac)
        except ValueError:
            msg = "{} n'est pas un caractère de l'alphabet ARK BnF valide"
            raise ValueError(msg.format(carac))

    def __init__(self, valeur=''):
        """Constructeur"""
        self.valeur = valeur

    def valider(self):
        """Valide les caractères contenus dans la chaîne ark"""
        invalides = []
        for carac in self.valeur:
            if carac not in ChaineArkBnf.ALPHABET:
                invalides.append(carac)
        if len(invalides) == 0:
            return (True, "La chaîne est valide au regard de l'alphabet BnF.")
        msg = ("La chaîne n'est pas valide,"
               "les caractères {} ne figurent pas dans l'alphabet BnF.")
        return (False, msg.format(set(invalides)))

    def calculer_controle(self):
        """Calcule le caractère de contrôle associé à la chaîne ark"""
        try:
            addition = 0
            for (i, carac) in enumerate(self.valeur):
                addition += ChaineArkBnf.ALPHABET.index(carac) * (i + 1)
            controle = ChaineArkBnf.ALPHABET[addition % 29]
            return controle
        except ValueError:
            valide = self.valider()
            if not valide[0]:
                print(valide[1], file=sys.stderr)
            return ''


def main(args):
    """Fonction principale"""
    value = args[1] if len(args) > 1 else "t3st"
    ark = ChaineArkBnf(value)
    msg = "Pour {}, le caractère de contrôle est {}"
    print(msg.format(value, ark.calculer_controle()))

if __name__ == '__main__':
    main(sys.argv)

