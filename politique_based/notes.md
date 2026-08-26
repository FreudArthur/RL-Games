# Les méthodes basées sur les politiques

C'est pas vrai que policy-based est réservé aux espaces infinis. REINFORCE, qu'on a vu sur Mountain Car, action discrète, gauche/rien/droite, c'est policy-based, et ça marche très bien. PPO aussi marche sur discret ET continu. Donc la règle c'est pas "value-based = fini, policy-based = infini", c'est plutôt :

Value-based, DQN inclus, ne marche QUE sur discret, à cause de l'argmax qu'on ne peut pas calculer sur un espace infini.
Policy-based marche sur les DEUX, discret et continu, c'est plus flexible, pas restreint à un seul cas.

## Les méthodes utilisé pour choisir une action dans un ensemble infini

On ne peux pas faire un softmax sur une infinité de valeurs possibles, contrairement au discret. Mais la solution est élégante : au lieu d'une distribution catégorielle (une proba par action discrète), tu utilises une distribution CONTINUE, typiquement une gaussienne, distribution normale.

Le réseau, au lieu de sortir des probabilités par action, sort juste DEUX nombres : une moyenne (mu) et un écart-type (sigma), qui définissent une courbe de Gauss sur l'espace d'actions continu.

## Les méthodes de gradient de politique peuvent apprendre une politique stochastique

Les méthodes de gradient de politique peuvent  apprendre une politique stochastique, contrairement aux fonctions de valeur .

Cela a deux conséquences :

Il n'est pas nécessaire d'implémenter manuellement un compromis exploration/exploitation . Puisque nous générons une distribution de probabilité sur les actions, l'agent explore  l'espace d'états sans toujours emprunter la même trajectoire.

Nous éliminons également le problème du repliement de spectre perceptuel . Le repliement de spectre perceptuel se produit lorsque deux états semblent (ou sont) identiques mais nécessitent des actions différentes.

## Inconvénients

Bien entendu, les méthodes de gradient de politique présentent également certains inconvénients :

* Les méthodes de gradient de politique convergent fréquemment vers un maximum local plutôt que vers un optimum global.
* La méthode du gradient de politique avance plus lentement,  étape par étape : l’entraînement peut prendre plus de temps (inefficace).
* Le gradient de politique peut présenter une forte variance.

## PPO et SAC

Dans l'apprentissage par renforcement (RL), prédire une moyenne μ et un écart-type σ est précisément la méthode standard pour gérer des actions continues (comme choisir l'angle exact d'un volant ou la force d'un moteur). Le réseau de neurones (l'Acteur) prend l'état actuel en entrée et génère les paramètres d'une distribution normale dans laquelle le robot va piocher son action.PPO (Proximal Policy Optimization) et SAC (Soft Actor-Critic) sont les deux algorithmes les plus populaires pour résoudre ce problème, mais ils abordent l'apprentissage de manière très différente.

### PPO

### SAC

## Comment maximiser ou minimiser la fonction objectif

La fonction objectif nous donne la performance de l'agent étant donné une trajectoire (séquence d'états et d'actions sans tenir compte de la récompense (contrairement à un épisode)), et elle produit la récompense cumulative attendue . En gros c'est moyen pour mesurer notre politique

La fonction de performance \(J(\theta)\) est l'espérance mathématique de la récompense totale \(R(\tau)\) sous la distribution de probabilité induite par la politique \(\theta \).En théorie des probabilités, l'espérance d'une variable aléatoire \(X\) se calcule par la somme (ou l'intégrale) des valeurs possibles multipliées par leur probabilité :
\(J(\theta )=\mathbb{E}_{\tau \sim P(\cdot ;\theta )}[R(\tau )]=\sum _{\tau }P(\tau ;\theta )R(\tau )\)

### L'algorithme Reinforce (Monte Carlo Reinforce)

L'algorithme Reinforce, également appelé gradient de politique Monte-Carlo, est un algorithme de gradient de politique qui utilise un rendement estimé d'un épisode complet pour mettre à jour le paramètre de politiqueθ

En boucle :
Utilisez la politique πθ pour collecter un épisode τ
Utilisez cet épisode pour estimer le gradient.
g=∇θJ(θ)

En résumé c'est un algorithme de gradient de politique qui utilise un rendement estimé d'un épisode entier pour mettre à jour le paramètre de politique.