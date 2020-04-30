# TP ARK avec python

## Le contexte...
Depuis le début du confinement, j'ai décidé de remettre le nez dans Python, langage sur lequel nous avions eu une formation dispensée par Logilab il y a quelques années. Je n'avais pas pratiqué et j'ai pensé avoir un peu de temps pour m'y consacrer. En réalité, je l'ai fait essentiellement sur mon temps de loisir...

Influencé par un collègue qui m'avait confié ne plus vouloir apprendre des langages liés à un formalisme spécifique, j'avais pour objectif d'apprendre à traiter des données qui n'étaient pas dans des formats dont j'avais l'habitude - XML et RDF, pour ne pas les nommer.

Je cherchais donc un sujet sur lequel essayer mes toutes fraîches compétences. Et l'identifiant ARK s'est vite présenté comme une évidence ! Je vous propose donc ce notebook Jupyter
* pour les bibliothécaires, BnF ou non, qui apprennent python et veulent s'essayer à un petit TP sur un sujet maison (niveau "grand débutant", avoir suivi jusqu'au bout les deux premières ressources ci-dessous devrait suffire à s'en sortir avec brio),
* pour les personnes qui s'intéressent à ARK - celles-ci se dispenseront de regarder le code, mais pourraient être intéressées par le texte qui l'entoure -,
* pour moi-même aussi ;-) afin de partager ma progression et recueillir les conseils de programmeurs chevronnés,
* comme une "preuve de concept" sur l'intérêt d'utiliser les Jupyter notebooks pour partager nos expériences de bibliothécaires apprentis ~~sorciers~~ codeurs.

Mon objectif est donc de proposer plusieurs TP afin de progresser en python et de partager des réflexions sur l'identifiant ARK et en montrer la logique.

J'ai également les [notebooks Jupyter](https://fr.wikipedia.org/wiki/Jupyter) pour commenter mon code et vous permettre de le manipuler dynamiquement. Pour cela, outre les fichiers python et les fichiers .jpynb, que vous pouvez télécharger et lancer avec vos applications python favorites, j'utilise Binder qui vous permet de disposer d'un environnement en ligne pour exécuter et modifier le code sans rient installer. En cliquant sur le bouton "launch" (et en patientant plusieurs dizaines de secondes, soyez patients), Binder vous ouvrira le repository "ark-tools" dans un environnement Jupyter Notebooks et vous pourrez manipuler les TP comme si vous aviez installé un environnement complet.

C'est parti ? [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/BertrandCaron/ark-tools/master)

## Ressources consultées

* Library Carpentry, _Python for libraries_. Disponible en ligne sur https://librarycarpentry.org/lc-python-intro/.
* Benjamin Marlé, Alexis Perrier, _Initiez-vous à Python pour l'analyse de données_, OpenClassrooms, mise à jour du 27/04/2020. Disponible en ligne sur https://openclassrooms.com/fr/courses/6204541-initiez-vous-a-python-pour-lanalyse-de-donnees. 
* Jason R. Briggs, _Python for Kids: A Playful Introduction to Programming_, No Starch Press : San Francisco, 2013.
* Vincent Le Goff, _Apprenez à programmer en Python_, OpenClassrooms, mise à jour 7/02/2020. Disponible en ligne sur https://openclassrooms.com/fr/courses/235344-apprenez-a-programmer-en-python/232431-utilisez-des-fichiers. 

## Ressources encore à découvrir...

* Ali Neishabouri, _Découvrez les librairies Python pour la Data Science_, OpenClassrooms, mise à jour du 31/03/2020. Disponible en ligne sur https://openclassrooms.com/fr/courses/4452741-decouvrez-les-librairies-python-pour-la-data-science.

## Petit rappel sur ARK

Vous trouverez de l'information sur le sujet de l'identifiant ARK dans les documents suivants :
* John Kunze (éd.), Bertrand Caron (trad. en français), _Foire aux questions sur l'identifiant ARK_, Projet ARKs-In-The-Open, version du 13 mars 2020. Disponible en ligne sur https://wiki.lyrasis.org/pages/viewpage.action?pageId=178880619.
* Bibliothèque nationale de France, _L’identifiant ARK (Archival Resource Key)_. Disponible en ligne sur https://www.bnf.fr/fr/lidentifiant-ark-archival-resource-key.

Sur la politique de la BnF concernant ARK, on trouvera aussi des informations dans le document suivant :
* Bibliothèque nationale de France, _Préconisations pour l'implémentation d'ARK par les sous-autorités nommantes et autorités d'adressage BnF_, version 2 du 7 mars 2019, identifiant : BnF-ADM-2018-022324-02. Disponible en ligne sur https://multimedia-ext.bnf.fr/pdf/ark_preconisations_bnf.pdf.
