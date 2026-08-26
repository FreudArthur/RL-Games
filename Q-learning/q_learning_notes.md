# Q-Learning est l'algorithme d'apprentissage par renforcement qui

- Entraîne une fonction Q , une fonction valeur-action encodée, en mémoire interne, par une table Q contenant toutes les valeurs de paires état-action.

- Étant donné un état et une action, notre fonction Q recherchera la valeur correspondante dans sa table Q.

- Une fois l'entraînement terminé, nous obtenons une fonction Q optimale, ou, de manière équivalente, une table Q optimale.

- Et si nous avons une fonction Q optimale , nous avons une politique optimale, puisque nous connaissons, pour chaque état, la meilleure action à entreprendre.

Au départ, notre table Q est inutile car elle attribue des valeurs arbitraires à chaque paire état-action (la plupart du temps, nous l'initialisons à zéro) . Cependant, à mesure que nous explorons l'environnement et mettons à jour notre table Q, elle nous fournira une approximation de plus en plus précise.

# Stratégies pour trouver la politique optimale

## Méthodes basées sur des politiques

La politique est généralement entraînée à l'aide d'un réseau de neurones afin de déterminer l'action à entreprendre en fonction de l'état. Dans ce cas, c'est le réseau de neurones qui détermine l'action que l'agent doit effectuer, plutôt qu'une fonction de valeur. En fonction de l'expérience acquise dans l'environnement, le réseau de neurones est réajusté et propose des actions plus efficaces.

## Méthodes basées sur la valeur

Dans ce cas, une fonction de valeur est entraînée à prédire la valeur d'un état ou d'une paire état-action qui représente notre politique. Cependant, cette valeur ne définit pas l'action que l'agent doit entreprendre. Au contraire, nous devons spécifier le comportement de l'agent en fonction de la valeur de la fonction de valeur. Par exemple, nous pourrions décider d'adopter une politique consistant à toujours privilégier l'action qui maximise la récompense (politique gloutonne). En résumé, la politique est une politique gloutonne (ou toute autre décision prise par l'utilisateur) qui utilise les valeurs de la fonction de valeur pour déterminer les actions à entreprendre.

## Parmi les méthodes fondées sur les valeurs on a

- La fonction de valeur d'état. Pour chaque état, la fonction de valeur d'état représente le rendement attendu si l'agent démarre dans cet état et suit la politique jusqu'à la fin.

- La fonction valeur d'action. Contrairement à la fonction valeur d'état, la fonction valeur d'action calcule, pour chaque paire état-action, le rendement attendu si l'agent démarre dans cet état, effectue cette action, puis suit la politique de manière permanente.

# Quelques statégies

## Stratégie Epsilon-greedy

- Stratégie courante utilisée en apprentissage par renforcement, qui consiste à équilibrer exploration et exploitation.
- Choisit l'action ayant la récompense attendue la plus élevée avec une probabilité de 1-epsilon.
- Choisit une action aléatoire avec une probabilité epsilon.
- Epsilon diminue généralement au fil du temps pour privilégier l'exploitation.

## Stratégie gourmande

- Cela implique de toujours choisir l'action susceptible de générer la plus grande récompense, en fonction des connaissances actuelles de l'environnement. (Exploitation uniquement)
- Choisis toujours l'action offrant la récompense attendue la plus élevée.
- N'inclut aucune exploration.
- Peut s'avérer désavantageux dans des environnements incertains ou lorsque les actions optimales sont inconnues.

## Off-policy vs on-policy algorithms

- Algorithmes off-policy : une stratégie différente est utilisée lors de l’entraînement et lors de l’inférence.
- Algorithmes on-policy : la même politique est utilisée lors de l’entraînement et de l’inférence.

## Stratégies d'apprentissage de Monte Carlo et de différence temporelle

- Monte Carlo (MC) : Apprentissage en fin d’épisode. Avec la méthode de Monte Carlo, on attend la fin de l’épisode pour mettre à jour la fonction de valeur (ou fonction de politique) à partir des données de l’épisode complet.

- Apprentissage par différence temporelle (TD) : apprentissage à chaque étape. L’apprentissage par différence temporelle permet de mettre à jour la fonction de valeur (ou fonction de politique) à chaque étape, sans nécessiter un épisode complet.

## Analogie magique

Q_new = Q_old + α[Target−Q_old]

Q_new = Q_old + αTarget −αQ_old

Donc :
Q_new=(1−α)Q_old + αTarget

# Evolution du Q-learning pour stabiliser l'entrainement

## Le problème que DQN vient résoudre

Ta table Q, elle marche super bien tant que t'as un nombre limité d'états, genre FrozenLake avec 16 cases. Mais imagine Atari : l'état, c'est une image de pixels. Le nombre d'états possibles est astronomique, littéralement impossible de faire une table avec une ligne par état. Tu peux jamais tous les visiter, encore moins les stocker.

## L'idée de DQN

Au lieu d'une table qui stocke Q(s,a) pour chaque paire, tu utilises un réseau de neurones qui APPREND à approximer cette fonction. Tu donnes l'état en entrée, genre les pixels ou dans notre cas position/vitesse pour Mountain Car, et le réseau te sort directement les valeurs Q pour CHAQUE action possible, en une seule passe.

Au lieu de faire table[état][action], tu fais réseau(état)[action]. C'est exactement le même rôle, juste une autre façon de stocker et calculer l'info, un réseau qui généralise au lieu d'une table qui mémorise case par case.

Comment on l'entraîne, le lien direct avec Bellman

La Bellman error r + gamma × max Q(s',a') - Q(s,a). Et bien DQN entraîne littéralement son réseau à minimiser cette erreur, mais formulée comme une vraie loss de deep learning, genre erreur quadratique :

loss = (target - prédiction)²
target = r + gamma × max Q(s', a')  [calculé par le réseau lui-même]
prédiction = Q(s,a)  [aussi calculé par le réseau]

Concrètement, on fait un forward pass pour prédire Q(s,a), un autre forward pass sur s' pour estimer le "target", on calcules l'écart, et on backpropage exactement comme n'importe quel réseau classique.

## Les deux gros pièges spécifiques à DQN et comment on les résouds

### Target Network → règle le problème de "chasing its own tail".

Vu que le target dépend lui aussi du même réseau qui est en train d'apprendre, à chaque mise à jour, la cible bouge aussi. C'est comme essayer de viser une cible qui bouge parce que ON la bouge nous-même en s'entraînant. Ça rend l'apprentissage instable, ça peut diverger.
Autrement dit la cible c'est y=r+γa′max​Q(s′,a′) et Le même réseau sert à calculer la prédiction ET la cible.

La solution : *le target network*. On gardes une copie séparée et figée du réseau, qu'on appelle le target network, on l'utilises UNIQUEMENT pour calculer le target, r + gamma × max Q_target(s',a'), pendant que le réseau principal continue de s'entraîner normalement. Toutes les quelques milliers de steps, on copies les poids du réseau principal vers le target network. Ça stabilise énormément, la cible ne bouge plus à chaque step, juste de temps en temps.

### Experience Replay → règle en grande partie le problème de corrélation des expériences.

Deuxième piège, la corrélation entre les données. En deep learning classique, les données d'entraînement sont mélangées aléatoirement, indépendantes les unes des autres. En RL, les états consécutifs d'un épisode sont hyper corrélés, l'état à t+1 ressemble énormément à l'état à t. Si on entraînes directement sur la séquence chronologique, le réseau overfit sur des patterns temporels locaux au lieu d'apprendre une vraie généralisation.

La solution : le replay buffer. On stockes toutes tes transitions (s, a, r, s') dans une grosse mémoire, et au lieu d'entraîner directement sur l'expérience du moment, on pioche des batchs ALÉATOIRES depuis ce buffer à chaque update. Ça casse la corrélation temporelle et ça permet de réutiliser une même expérience plusieurs fois, plus efficace en échantillons.

## D'autres algos  

Depuis ces trois améliorations apportées à l'apprentissage par renforcement profond (Deep Q-Learning), de nombreuses autres ont été intégrées, telles que la relecture d'expérience prioritaire et l'apprentissage par renforcement profond en duel (Dueling Deep Q-Learning).

