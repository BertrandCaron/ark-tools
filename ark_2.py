"""Module de gestion des chaînes de caractères ARK BnF"""


import sys


ALPHABET = '0123456789bcdfghjkmnpqrstvwxz'


class ChaineARKBnF():
    """Classe principale de gestion des chaînes ARK BnF"""

    def __init__(self, valeur=''):
        """Constructeur

        Il définit l'attribut unique d'une chaîne de
        caractères ARK BnF : sa valeur."""
        self.valeur = valeur

    def valider(self):
        """Méthode de validation d'une chaîne

        Elle renvoie un tuple avec en première valeur un booléen et en
        seconde un message qui spécifie le cas échéant les caractères
        invalides."""
        invalides = []
        for carac in self.valeur:
            if carac not in ALPHABET:
                invalides.append(carac)
        if not invalides:
            valide = True
            msg = "La chaîne est valide au regard de l'alphabet BnF."
        else:
            valide = False
            msg = ("La chaîne n'est pas valide, le(s) caractère(s) {} "
                   "ne figurent pas dans l'alphabet BnF.").format(set(invalides))
        return (valide, msg)

    def calculer_controle(self):
        """Méthode de calcul du caractère de contrôle

        Elle renvoie le caractère de contrôle si la chaîne est valide et
        gère les erreurs."""
        try:
            addition = 0
            for indice, carac in enumerate(self.valeur):
                addition += ALPHABET.index(carac) * (indice+1)
            controle = ALPHABET[addition % 29]
            return controle
        except ValueError:
            valide = self.valider()
            if not valide[0]:
                print(valide[1], file=sys.stderr)
            return ''


def main(args):
    """Fonction principale

    Elle calcule le caractère de contrôle de toute chaîne ARK BNF passée en
    argument."""
    valeur = args[1] if len(args) > 1 else "t3st"
    chaine = ChaineARKBnF(valeur)
    controle = chaine.calculer_controle()
    msg = "Pour {}, le caractère de contrôle est {}"
    print(msg.format(valeur, controle))


if __name__ == '__main__':
    main(sys.argv)
