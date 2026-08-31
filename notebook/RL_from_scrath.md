# Coder la Policy Gradient

## Le jeu  CartPole-v1

1. Les Contraintes et Conditions d'Arrêt

L'environnement n'applique pas de "barrière physique", mais il définit des limites géométriques et temporelles. L'épisode s'arrête immédiatement dès qu'une contrainte est enfreinte (Terminated ou Truncated)

* Contrainte d'angle (La Perche)

L'angle de la perche ne doit pas dépasser 12 degrés (soit environ 0,2095 radians) par rapport à la verticale. Si la perche penche trop, elle est considérée comme tombée.

* Contrainte d'espace (Le Chariot)

La position du chariot x ne doit pas dépasser ( 2,4 unités) par rapport au centre du rail (l'origine 0). Si le chariot sort de l'écran ou de cette zone, la partie s'arrête.

* Contrainte de temps (Limite d'étapes)

L'épisode s'arrête automatiquement si l'agent réussit à survivre jusqu'à la limite de temps. Cette limite est fixée à 500 étapes pour la version CartPole-v1.

2. Le Système de Récompenses (Rewards)

Par défaut, la philosophie du CartPole récompense la survie plutôt que d'évaluer la qualité de la position.

Règle standard : L'agent reçoit une récompense fixe de +1 à chaque étape de calcul (Time Step) où la perche reste en équilibre et le chariot dans les limites. Objectif : Maximiser la somme cumulée de ces récompenses. Le score maximal théorique est donc de 500 (v1). On considère généralement l'environnement "résolu" si l'agent maintient un score moyen de 475 sur 100 essais consécutifs.

## Récap complet du pipeline RL

## Le principe de base

Un environnement (Gymnasium) expose une interface standard : reset() te donne un état initial, step(action) fait avancer le monde et te renvoie nouvel état, récompense, et si c'est terminé. L'agent, lui, ne connaît jamais les rouages internes de l'environnement, il voit juste état → action → récompense.

## Les deux familles d'algos

Value-based (Q-learning, DQN) : apprend "combien vaut chaque action dans cet état", et choisit toujours la meilleure. Marche seulement avec actions discrètes.

Policy-based (REINFORCE, et acteur-critique comme A2C, PPO, SAC) : apprend directement une politique, une fonction état → action ou distribution d'actions. Marche avec discret ET continu. PPO ajoute un garde-fou anti-mise à jour brutale. SAC ajoute un bonus d'exploration via l'entropie.

## Le pipeline REINFORCE, étape par étape

`forward_pass` : tu joues un épisode complet avec la politique actuelle. À chaque étape, l'observation passe dans le réseau → logits → softmax → distribution catégorielle → tu tires une action au hasard pondéré → tu gardes le log_prob de cette action et la récompense reçue.

`calculate_stepwise_returns` : après l'épisode, tu recalcules, en partant de la fin, le retour cumulé actualisé à chaque étape (R = r + R * gamma), puis tu normalises (moyenne 0, écart-type 1) pour avoir un signal relatif propre, "mieux ou pire que la moyenne de l'épisode".

`calculate_loss` : -(returns * log_probs).sum(). Le signe moins transforme "maximiser le retour" en "minimiser la loss", ce que PyTorch sait faire nativement.

`update_policy` : backward + step de l'optimiseur, classique.
