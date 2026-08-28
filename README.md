# RL-Games

Un projet personnel d'exploration de l'Apprentissage par Renforcement (Reinforcement Learning), construit comme un laboratoire pratique pour entraîner des agents sur des environnements classiques de Gymnasium.

## L'histoire du projet

Ce repo est né d'un objectif simple : **passer de la théorie RL à des implémentations concrètes**.
Au lieu de rester sur des formules, j'ai voulu entraîner des agents, observer leurs comportements, sauvegarder des modèles et générer des vidéos des épisodes pour visualiser les progrès.

## Objectif

L'objectif est de :

- implémenter et comprendre des approches **value-based** (ex: Q-learning, DQN),
- comparer avec des idées **policy-based**,
- appliquer ces méthodes à des problèmes connus (MountainCar, FrozenLake, Taxi),
- documenter les résultats et garder une trace visuelle des performances.

## Vue d'ensemble du repo

```text
.
├── Q-learning/              # Notes et concepts autour de Q-learning / DQN
├── politique_based/         # Notes sur les méthodes policy-based
├── models/                  # Modèles entraînés (ex: mountain-car.pt)
├── videos/                  # Vidéos de résultats (épisodes enregistrés)
└── pyproject.toml           # Dépendances du projet
```

## Résultats actuels (vidéos)

Les vidéos suivantes montrent l'état actuel des agents entraînés :

| Environnement | Vidéo | Détails |
|---|---|---|
| FrozenLake | [frozen_lake.mp4](videos/frozen_lake.mp4) | 7s - 256x256 |
| MountainCar | [mountain-car-episode-0.mp4](videos/mountain-car-episode-0.mp4) | 6.7s - 600x400 - 201 frames |
| MountainCar | [mountain-car-episode-3.mp4](videos/mountain-car-episode-3.mp4) | 6.7s - 600x400 - 201 frames |
| MountainCar | [rl-video-episode-0.mp4](videos/rl-video-episode-0.mp4) | 6.7s - 600x400 - 201 frames |
| Taxi-v4 | [taxi-v4.mp4](videos/taxi-v4.mp4) | 13s - 560x352 |

Ces vidéos servent de vitrine rapide pour voir le comportement des politiques apprises sur différents jeux RL.

## Stack utilisée

- Python 3.12+
- Gymnasium (+ Atari / Box2D selon besoins)
- PyTorch
- Stable-Baselines3
- TensorBoard
