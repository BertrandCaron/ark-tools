# TP ARK avec python

## Le contexte...
Depuis le début du confinement, j'ai décidé de remettre le nez dans Python, langage sur lequel nous avions eu une formation dispensée par Logilab il y a quelques années. Je n'avais pas pratiqué et j'ai pensé avoir un peu de temps pour m'y consacrer. En réalité, je l'ai fait essentiellement sur mon temps de loisir...

Influencé par un collègue qui m'avait confié ne plus vouloir apprendre des langages liés à un formalisme spécifique, j'avais pour objectif d'apprendre à traiter des données qui n'étaient pas dans des formats dont j'avais l'habitude - XML et RDF, pour ne pas les nommer.

Je cherchais donc un sujet sur lequel essayer mes toutes fraîches compétences. Et l'identifiant ARK s'est vite présenté comme une évidence ! Je vous propose donc de publier plusieurs notebooks Jupyter incrémentaux
* pour les bibliothécaires, BnF ou non, qui apprennent python et veulent s'essayer à un petit TP sur un sujet maison (niveau "grand débutant", avoir suivi jusqu'au bout les deux premières ressources ci-dessous devrait suffire à s'en sortir avec brio),
* comme base de réflexion sur l'identifiant ARK et sa logique, tant il est vrai qu'on comprend mieux quand on manipule soi-même,
* pour moi ;-) afin de partager ma progression et recueillir les conseils de programmeurs chevronnés,
* comme une "preuve de concept" sur l'intérêt d'utiliser les notebooks Jupyter pour partager nos expériences de bibliothécaires apprentis ~~sorciers~~ codeurs.

Pour vous permettre de manipuler dynamiquement les fichiers python et les [notebooks Jupyter](https://fr.wikipedia.org/wiki/Jupyter) (fichiers .jpynb), j'utilise [Binder](https://mybinder.org/). En cliquant sur le bouton "launch" (ça prend plusieurs dizaines de secondes, soyez patients), Binder vous ouvrira le repository "ark-tools" dans un environnement Jupyter Notebooks et vous pourrez manipuler les TP comme si vous aviez installé un environnement python complet.

C'est parti ? [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/BertrandCaron/ark-tools/master)

## Ressources consultées sur python

* Library Carpentry, _Python for libraries_. Disponible en ligne sur https://librarycarpentry.org/lc-python-intro/.
* Benjamin Marlé, Alexis Perrier, _Initiez-vous à Python pour l'analyse de données_, OpenClassrooms, mise à jour du 27/04/2020. Disponible en ligne sur https://openclassrooms.com/fr/courses/6204541-initiez-vous-a-python-pour-lanalyse-de-donnees. 
* Jason R. Briggs, _Python for Kids: A Playful Introduction to Programming_, No Starch Press : San Francisco, 2013.
* Vincent Le Goff, _Apprenez à programmer en Python_, OpenClassrooms, mise à jour 7/02/2020. Disponible en ligne sur https://openclassrooms.com/fr/courses/235344-apprenez-a-programmer-en-python/232431-utilisez-des-fichiers. 

## Ressources encore à découvrir sur python...

* Ali Neishabouri, _Découvrez les librairies Python pour la Data Science_, OpenClassrooms, mise à jour du 31/03/2020. Disponible en ligne sur https://openclassrooms.com/fr/courses/4452741-decouvrez-les-librairies-python-pour-la-data-science.

## Ressources sur ARK

Vous trouverez de l'information sur le sujet de l'identifiant ARK dans les documents suivants :
* John Kunze (éd.), Bertrand Caron (trad. en français), _Foire aux questions sur l'identifiant ARK_, Projet ARKs-In-The-Open, version du 13 mars 2020. Disponible en ligne sur https://wiki.lyrasis.org/pages/viewpage.action?pageId=178880619.
* Bibliothèque nationale de France, _L’identifiant ARK (Archival Resource Key)_. Disponible en ligne sur https://www.bnf.fr/fr/lidentifiant-ark-archival-resource-key.

Sur la politique de la BnF concernant ARK, on trouvera aussi des informations dans le document suivant :
* Bibliothèque nationale de France, _Préconisations pour l'implémentation d'ARK par les sous-autorités nommantes et autorités d'adressage BnF_, version 2 du 7 mars 2019, identifiant : BnF-ADM-2018-022324-02. Disponible en ligne sur https://multimedia-ext.bnf.fr/pdf/ark_preconisations_bnf.pdf.
