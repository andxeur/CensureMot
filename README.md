# CensureMot
Ce projet vise à faire des vérifications de mots sensibles dans une phrase même si ce mot est masqué par des caractères spéciaux.  
Exp : merde -> m*rde / m#rd.

Il fournit des fonctions pour vérifier la présence de mots sensibles dans un texte ou le taux de similarité afin d'effectuer la vérification.

# Description

Ce module est conçu pour vérifier la présence de mots sensibles dans une phrase. Il utilise la distance de Levenshtein pour calculer le taux de similarité entre les mots. Le module est conçu pour être utilisé dans des applications où la vérification de la présence de mots sensibles est cruciale, tels que les systèmes de modération de contenu ou les outils de détection de spam.

## Fonctionnalités

* Vérification de la présence de mots sensibles dans une phrase
* Calcul du taux de similarité entre les mots en utilisant la distance de Levenshtein
* Lister les mots à censurer et les caractères spéciaux utilisés couramment afin de cacher un mot sensible ou censuré

## Utilisation


### Installation

Pour utiliser ce module, il suffit de l'importer dans votre code Python.

```python
import module
```

### Exemple d'utilisation

```python
import module

module.verifier_mot_censurer("Ceci est un exemple de phrase")
module.verifier_mot_censurer("merde")

```

## Fonctions

### `taux_similarite(mot1, mot2)`

Calcule le taux de similarité entre deux mots en utilisant la distance de Levenshtein.

* **Paramètres** :
	+ `mot1` : premier mot à comparer (str)
	+ `mot2` : deuxième mot à comparer (str)
* **Retourne** : le taux de similarité entre les deux mots 
* **But** : Cette fonction est utilisée pour calculer le taux de similarité entre deux mots. Elle est utilisée dans la fonction `verifier_mot_censurer` pour déterminer si un mot est similaire à un mot censuré.

### `verifier_mot_censurer(phrase)`

Vérifie la présence de mots sensibles dans une phrase.

* **Paramètres** :
	+ `phrase` : phrase à vérifier (str)
* **But** : Cette fonction est utilisée pour vérifier la présence de mots sensibles dans une phrase. Elle utilise la fonction `taux_similarite` pour calculer le taux de similarité entre les mots de la phrase et les mots censurés.

## Liste de mots censurés

La liste de mots censurés est stockée dans la variable `liste_mot_censurer`. Vous pouvez ajouter ou supprimer des mots de cette liste.

## Liste de caractères spéciaux

La liste de caractères spéciaux est stockée dans la variable `caracteres_speciaux`. Vous pouvez ajouter ou supprimer des caractères de cette liste en fonction de vos besoins.

## Auteur
Assammond Andre 
