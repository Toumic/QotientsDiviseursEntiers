#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vicenté quantic cabviva
"""Les imbrications des diviseurs : Ce qui change par rapport à l'ancienne version,
est que les divisions se font en boucles."""
# Import module
from decimal import *
getcontext().prec = 15  # Précision donnée pour une quantité de chiffres affichés.
# Les outils
quotients_dic = {}  # Dictionnaire chargé de stocker les quotients et leurs assimilations.
entiers_dic, dec_ent_dic = {}, {}
restes_dic_q, restes_dic_e, restes_dic_d = {}, {}, {}
liste_entiers = list(range(1, 25))  # Liste des entiers, pour un premier traitement.


def mutation(mut0):
    """Fonction de transformation du quotient décimal en quotient entier"""
    mut60, pnt61 = "", False
    for x in str(mut0):
        if pnt61:
            mut60 += x  # , mut61 = Assemblage des décimales.
        if x == ".":
            pnt61 = True
    if mut0 == 0 or mut60 == "":
        mut60 = "0"
    return mut60


# Production des quotients.
for le in liste_entiers:  # 'le' devient le diviseur commun.
    if le != 1:
        tab_val1, tab_val2, tab_val3, visu = [], [], [], 0  # Mettre 'visu' à zéro pour ne pas afficher les prints.
        # print("__________Ligne de séparation_______________", le)
        for lo in liste_entiers:  # 'lo' devient le premier dividende.
            tab_val1.clear()
            tab_val2.clear()
            tab_val3.clear()
            tab_top1, tab_top2, tab_top3 = True, True, True
            dividende = dividende1 = lo
            quotients_dic[lo, le] = []  # Traitement des quotients réels.
            entiers_dic[lo, le] = []  # Partie entière du nombre réel.
            dec_ent_dic[lo, le] = []  # Partie décimale du nombre réel transformé en entier.
            valise, sacoche = [], []
            while tab_top1 or tab_top2:  # Avec sept (7) c'est pour mieux jauger les cycles en cascade.
                quotient = Decimal(dividende) / le  # Premier quotient original.
                quotient1 = dividende1 / le
                reste2 = int(dividende1 % le)  # Le reste est modifié entier. La partie décimale = Celle du quotient.
                quote_ent = int(quotient)
                quote_dec = quotient - int(quotient)  # Part entière de la partie décimale du quotient.
                dividende = mutation(quote_dec)  # Retour de la part entière de la partie décimale.
                reste1 = quote_ent % le
                reste = int(dividende) % le  # 'reste' = Le reste de la division des décimales mutées.
                chariot = [quotient1, reste2]
                sacoche = [quote_ent, reste1]
                valise = [dividende, reste]
                dividende1 = quotient1  # Passage de la valeur du quotient1 au dividende1.
                if tab_top3:
                    if chariot not in tab_val3:
                        quotients_dic[lo, le].append(chariot)
                        tab_val3.append(chariot)
                    else:
                        chariot = "Doublon = Fin."
                        quotients_dic[lo, le].append(chariot)
                        tab_top3 = False
                if tab_top2:
                    if sacoche not in tab_val2:
                        entiers_dic[lo, le].append(sacoche)
                        tab_val2.append(sacoche)
                    else:
                        sacoche.append("Doublon = Fin.")
                        entiers_dic[lo, le].append(sacoche)
                        restes_dic_e[lo, le] = set(list(e[1] for e in tab_val2))
                        tab_top2 = False
                if tab_top1:
                    if valise not in tab_val1:
                        dec_ent_dic[lo, le].append(valise)  # Enregistrement progressif du dictionnaire.
                        tab_val1.append(valise)
                    else:
                        valise.append("Doublon = Fin.")
                        dec_ent_dic[lo, le].append(valise)  # Enregistrement progressif du dictionnaire.
                        restes_dic_d[lo, le] = set(list(d[1] for d in tab_val1))
                        tab_top1 = False
                if le == visu:  # Uniquement lorsque 'visu' n'est pas égal à zéro.
                    # print("Sacoche tab_val2", tab_val2)
                    # print("Valise tab_val1", tab_val1)
                    print(lo, le, "Reste2", reste2, chariot)
            restes_dic_q[lo, le] = set(list(q[1] for q in tab_val3))
            if le == visu:      # Uniquement lorsque 'visu' n'est pas égal à zéro.
                print(" _ Ligne intermédiaire _ le", le, "lo", lo, "\n")
("quotients_dic keys", quotients_dic.keys())
# Affichage du dictionnaire
for qdk, qdv in dec_ent_dic.items():
    if qdk[1] == 3:
        print("Q qdk", qdk, "quotients_dic", quotients_dic[qdk], "\t Restes", restes_dic_q[qdk])
        print("E qdk", qdk, "entiers_dic", entiers_dic[qdk], "\t Restes", restes_dic_e[qdk])
        print("D qdk", qdk, "dec_ent_dic", dec_ent_dic[qdk], "\t Restes", restes_dic_d[qdk])
        print()
