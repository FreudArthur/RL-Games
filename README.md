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

## Résultats actuels 


FrozenLake  

<video src="videos\frozen_lake.mp4" controls width="100%"></video>


MountainCar 

<video src="videos/mountain-car-episode-0.mp4" controls width="100%"></video>




Taxi-v4 

<video src="videos/taxi-v4.mp4" controls width="100%"></video>

## Stack utilisée

- Python 3.12+
- Gymnasium (+ Atari / Box2D selon besoins)
- PyTorch
- Stable-Baselines3
- TensorBoard
