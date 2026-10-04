"""
Flappy Bird - version basique
=============================

Un petit jeu fait avec pygame, SANS images ni sprites :
uniquement des formes simples (cercle pour l'oiseau,
rectangles pour les tuyaux et le sol).

Controles :
    ESPACE (ou clic gauche) : battre des ailes (l'oiseau monte)
    Q ou ECHAP              : quitter le jeu

Regles :
    - L'oiseau tombe tout seul a cause de la gravite.
    - Appuie sur ESPACE au bon moment pour le faire monter
      et passer entre les tuyaux.
    - Si tu touches un tuyau, le sol ou le plafond : Game Over.
    - Chaque tuyau franchi rapporte 1 point.
"""

import random
import sys

import pygame

# ----------------------------------------------------------------------
# Reglages du jeu (des constantes faciles a modifier)
# ----------------------------------------------------------------------

LARGEUR = 400
HAUTEUR = 600
FPS = 60

# Oiseau
RAYON_OISEAU = 15
X_OISEAU = 100
GRAVITE = 0.5          # acceleration vers le bas (px par frame au carre)
FORCE_SAUT = -8        # vitesse vers le haut quand on appuie (px par frame)

# Tuyaux
LARGEUR_TUYAU = 70
HAUTEUR_PASSAGE = 150  # espace libre entre le tuyau du haut et celui du bas
VITESSE_TUYAU = 3      # vitesse des tuyaux vers la gauche
DISTANCE_TUYAUX = 220  # distance horizontale entre deux tuyaux

# Sol
HAUTEUR_SOL = 90

# Couleurs (R, V, B)
BLEU_CIEL = (135, 206, 235)
JAUNE = (255, 220, 60)
MARRON = (210, 150, 80)
VERT = (70, 170, 70)
VERT_SOL = (90, 190, 90)
VERT_FONCE = (50, 130, 50)
BLANC = (255, 255, 255)
NOIR = (50, 50, 50)


# ----------------------------------------------------------------------
# L'oiseau
# ----------------------------------------------------------------------

class Oiseau:
    """L'oiseau : un simple cercle jaune qui monte ou descend."""

    def __init__(self):
        self.x = X_OISEAU
        self.y = HAUTEUR // 2
        self.vy = 0  # vitesse verticale (negative = vers le haut)

    def sauter(self):
        """Donne un coup d'aile : l'oiseau repart vers le haut."""
        self.vy = FORCE_SAUT

    def maj(self):
        """Applique la gravite et deplace l'oiseau d'une frame."""
        self.vy += GRAVITE
        self.y += self.vy

    def rectangle(self):
        """Petit rectangle autour de l'oiseau, utilise pour les collisions."""
        return pygame.Rect(
            self.x - RAYON_OISEAU, self.y - RAYON_OISEAU,
            RAYON_OISEAU * 2, RAYON_OISEAU * 2,
        )

    def dessiner(self, ecran):
        # Corps : un cercle jaune
        pygame.draw.circle(ecran, JAUNE, (self.x, self.y), RAYON_OISEAU)
        # Oeil
        pygame.draw.circle(ecran, BLANC, (self.x + 7, self.y - 5), 5)
        pygame.draw.circle(ecran, NOIR, (self.x + 9, self.y - 5), 2)
        # Bec : un petit triangle
        pygame.draw.polygon(ecran, MARRON, [
            (self.x + 12, self.y),
            (self.x + 24, self.y + 2),
            (self.x + 12, self.y + 6),
        ])


# ----------------------------------------------------------------------
# Les tuyaux
# ----------------------------------------------------------------------

class Tuyau:
    """Un tuyau = 2 rectangles verts avec un passage au milieu."""

    def __init__(self, x):
        self.x = x
        # Hauteur du bas du passage, choisie au hasard (mais jamais trop
        # pres du sol ou du plafond pour que ce soit jouable).
        mini = 60
        maxi = HAUTEUR - HAUTEUR_SOL - HAUTEUR_PASSAGE - 60
        self.passe = random.randint(mini, maxi)
        self.compte = False  # le point est-il deja compte ?

    def maj(self):
        """Fait avancer le tuyau vers la gauche."""
        self.x -= VITESSE_TUYAU

    def rectangles(self):
        """Les deux rectangles (haut et bas) pour les collisions."""
        haut = pygame.Rect(self.x, 0, LARGEUR_TUYAU, self.passe)
        bas = pygame.Rect(
            self.x, self.passe + HAUTEUR_PASSAGE, LARGEUR_TUYAU,
            HAUTEUR - HAUTEUR_SOL - (self.passe + HAUTEUR_PASSAGE),
        )
        return haut, bas

    def dessiner(self, ecran):
        haut, bas = self.rectangles()
        # Corps des tuyaux
        pygame.draw.rect(ecran, VERT, haut)
        pygame.draw.rect(ecran, VERT, bas)
        # Petit rebord (plus large) a l'entree du passage
        rebord = 25
        pygame.draw.rect(ecran, VERT_FONCE,
                         (haut.right - 8, haut.bottom - rebord, 16, rebord))
        pygame.draw.rect(ecran, VERT_FONCE,
                         (bas.left - 8, bas.top, 16, rebord))


# ----------------------------------------------------------------------
# Fonctions utilitaires
# ----------------------------------------------------------------------

def collision(oiseau, tuyaux):
    """Renvoie True si l'oiseau touche un tuyau, le sol ou le plafond."""
    # Sol et plafond
    if oiseau.y - RAYON_OISEAU <= 0:
        return True
    if oiseau.y + RAYON_OISEAU >= HAUTEUR - HAUTEUR_SOL:
        return True
    # Tuyaux
    for tuyau in tuyaux:
        for rect in tuyau.rectangles():
            if oiseau.rectangle().colliderect(rect):
                return True
    return False


def afficher_texte(ecran, texte, taille, couleur, y):
    """Affiche un texte centre horizontalement a la hauteur y."""
    font = pygame.font.SysFont("Arial", taille)
    surface = font.render(texte, True, couleur)
    x = LARGEUR // 2 - surface.get_width() // 2
    ecran.blit(surface, (x, y))


# ----------------------------------------------------------------------
# Boucle principale
# ----------------------------------------------------------------------

def main():
    pygame.init()
    ecran = pygame.display.set_mode((LARGEUR, HAUTEUR))
    pygame.display.set_caption("Flappy Bird - version basique")
    horloge = pygame.time.Clock()

    etat = "menu"      # "menu", "jeu" ou "mort"
    oiseau = Oiseau()
    tuyaux = []
    score = 0

    while True:
        # ----- 1. Lire les evenements (clavier / souris / fermeture) -----
        for evenement in pygame.event.get():
            if evenement.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evenement.type == pygame.KEYDOWN:
                if evenement.key in (pygame.K_ESCAPE, pygame.K_q):
                    pygame.quit()
                    sys.exit()

                if evenement.key == pygame.K_SPACE:
                    if etat == "menu":
                        etat = "jeu"
                    elif etat == "jeu":
                        oiseau.sauter()
                    elif etat == "mort":
                        # On recommence une partie
                        etat = "jeu"
                        oiseau = Oiseau()
                        tuyaux = []
                        score = 0

            if evenement.type == pygame.MOUSEBUTTONDOWN and etat == "jeu":
                oiseau.sauter()

        # ----- 2. Mettre a jour le jeu -----
        if etat == "jeu":
            oiseau.maj()

            # Faire apparaître un nouveau tuyau quand le dernier est assez loin
            if not tuyaux or tuyaux[-1].x <= LARGEUR - DISTANCE_TUYAUX:
                tuyaux.append(Tuyau(LARGEUR))

            for tuyau in tuyaux:
                tuyau.maj()

            # Un point a chaque tuyau depasse
            for tuyau in tuyaux:
                if not tuyau.compte and tuyau.x + LARGEUR_TUYAU < oiseau.x:
                    tuyau.compte = True
                    score += 1

            # Enlever les tuyaux sortis de l'ecran
            tuyaux = [t for t in tuyaux if t.x + LARGEUR_TUYAU > 0]

            if collision(oiseau, tuyaux):
                etat = "mort"

        # ----- 3. Dessiner -----
        ecran.fill(BLEU_CIEL)

        for tuyau in tuyaux:
            tuyau.dessiner(ecran)

        oiseau.dessiner(ecran)

        # Sol : un grand rectangle vert
        pygame.draw.rect(ecran, VERT_SOL,
                         (0, HAUTEUR - HAUTEUR_SOL, LARGEUR, HAUTEUR_SOL))
        # Petite ligne d'herbe plus foncee sur le dessus du sol
        pygame.draw.rect(ecran, VERT_FONCE,
                         (0, HAUTEUR - HAUTEUR_SOL, LARGEUR, 8))

        afficher_texte(ecran, str(score), 40, BLANC, 20)

        if etat == "menu":
            afficher_texte(ecran, "FLAPPY BIRD", 50, BLANC, 180)
            afficher_texte(ecran, "Appuie sur ESPACE pour commencer",
                           22, BLANC, 230)
        elif etat == "mort":
            afficher_texte(ecran, "Game Over !", 44, BLANC, 180)
            afficher_texte(ecran, "Score : " + str(score), 24, BLANC, 230)
            afficher_texte(ecran, "ESPACE pour rejouer", 22, BLANC, 270)

        pygame.display.flip()
        horloge.tick(FPS)


if __name__ == "__main__":
    main()
