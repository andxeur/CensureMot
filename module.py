"""
Module de vérification de mots sensibles

Ce module fournit des fonctions pour vérifier la présence de mots sensibles dans un texte.
"""

from __future__ import annotations

__author__: str = "Assammond Andre"
__license__: str = "GPL"
__version__: str = "0.1"

import Levenshtein

__all__ = ['taux_similarite', 'verifier_mot_censurer']

liste_mot_censurer = ["merde", "pute", "chien", "chienne", "salo", "nègre", "tuer", "meurtre", "viol"]
caracteres_speciaux = "*#@$%&-"


def taux_similarite(mot1, mot2):
    """
        Calcule le taux de similarité entre deux mots en utilisant la distance de Levenshtein

        Args:
            mot1 (str): Premier mot à comparer
            mot2 (str): Deuxième mot à comparer

        Returns:
            float: Taux de similarité entre les deux mots
    """

    mot1 = mot1.lower()
    mot2 = mot2.lower()

    # Calcul de la distance de Levenshtein entre les deux mots
    distance = Levenshtein.distance(mot1, mot2)

    # Calcul de la longueur maximale entre les deux mots
    longueur_max = max(len(mot1), len(mot2))

    # Calcul du taux de similarité
    similarite = (longueur_max - distance) / longueur_max

    # Conversion en pourcentage
    return int(similarite * 100)


def verifier_mot_censurer(phrase):
    """
        Vérifie la présence de mots sensibles dans une phrase et affiche un message si un mot sensible est trouvé

        Args:
            phrase (str): Phrase à vérifier

        Returns:
            None
        """

    mot_censurer_trouver = False
    phrase = phrase.lower()
    phrase = phrase.split()

    for mots in phrase:

        if mots in liste_mot_censurer:
            print(f"Le mot '{mots}' est un mot censurer.")
            mot_censurer_trouver = True
            break
        # elif "*" or "#" or "@" or "&" or "$" or "%" or "-" in mots:
        elif any(caractere in mots for caractere in caracteres_speciaux):

            for caractere in caracteres_speciaux:
                compteur = mots.count(caractere)
                if compteur > 1:
                    print(
                        f"Desole le caractère '{caractere}' est répété plus de {compteur} fois dans le mot '{mots}' afin de l'identifier correctement.")
                    mot_censurer_trouver = True
                    break

            for censure in liste_mot_censurer:
                taux = taux_similarite(mots, censure)

                if taux >= 75:
                    print(
                        f"Le mot '{mots}' est similaire au mot '{censure}' avec un taux de similarité de {taux:.2f}%.")
                    print("Veuiller ecrire le mot sans de caractere specifique.")
                    mot_censurer_trouver = True
                    break

    if not mot_censurer_trouver:
        print("aucun mot censurer trouvé")
