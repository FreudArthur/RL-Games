<div align="center">

# 🎮 RL-Games

### Un laboratoire d'apprentissage par renforcement (Reinforcement Learning), pensé pour apprendre en codant 🤖

![Python 3.12+](https://img.shields.io/badge/Python-3.12%2B-3776AB?logo=python&logoColor=white)
![Gymnasium](https://img.shields.io/badge/Gymnasium-1.3+-2ECC71)
![PyTorch](https://img.shields.io/badge/PyTorch-2.x-EE4C2C?logo=pytorch&logoColor=white)
![Stable-Baselines3](https://img.shields.io/badge/Stable%20Baselines3-2.x-9B1C31)

</div>

---

> 🧠 **Ce dépôt est avant tout un parcours d'apprentissage.** L'objectif n'est pas d'utiliser les bibliothèques comme des boîtes noires, mais de **comprendre chaque algorithme en le codant soi-même**, étape par étape, avant de le comparer aux implémentations de référence.

## ✨ La philosophie pédagogique

Ce projet est né d'une conviction simple : **on ne comprend vraiment le Reinforcement Learning qu'en implémentant les algorithmes soi-même**. Plutôt que de rester sur des formules, l'idée est de :

1. **Apprendre les concepts** — le processus RL, les équations de Bellman, l'exploration vs l'exploitation, avec des notes rédigées au fil de l'apprentissage ;
2. **Coder les algorithmes de zéro** — une Q-table en pur NumPy, un DQN avec PyTorch, un PPO complet (Actor-Critic, GAE, clipping)… ;
3. **Comparer avec les références** — Stable-Baselines3, pour vérifier que nos implémentations tiennent la route ;
4. **Observer les résultats** — sauvegarder les modèles entraînés et enregistrer des vidéos des parties pour **visualiser le progrès** 👀.


##  Le parcours pédagogique

Les notebooks sont organisés comme une vraie progression : on part des fondamentaux, on code nos premiers agents, puis on explore les algorithmes modernes.

| # | Étape | Algorithme(s) | Environnements | Où ça se passe ? |
|---|-------|---------------|----------------|------------------|
| 1 | Les fondamentaux | API Gymnasium (`reset`/`step`), politique, rendement | 🛒 CartPole | [`notebook/carpool.ipynb`](notebook/carpool.ipynb) |
| 2 | Q-Learning tabulaire | Q-Learning, ε-greedy, équation de Bellman | ❄️ FrozenLake, 🚕 Taxi | [`taxi-frozen_lake.ipynb`](taxi-frozen_lake.ipynb) · [`Q-learning/`](Q-learning/) |
| 3 | Deep Q-Learning | DQN, target network, experience replay | ⛰️ MountainCar, 👾 Atari | [`mountain-car.ipynb`](mountain-car.ipynb) · [`Q-learning/`](Q-learning/) |
| 4 | Méthodes basées sur les politiques | REINFORCE (policy gradient) | 🛒 CartPole, 🚁 PixelCopter | [`politique_based/`](politique_based/) |
| 5 | Actor-Critic | A2C | 🤖 Panda-Gym (robotique) | [`PPO et A2C/`](PPO%20et%20A2C/) |
| 6 | PPO | PPO, Actor-Critic, GAE, clipping | 🚀 LunarLander | [`lunar-lander.ipynb`](lunar-lander.ipynb) · [`PPO et A2C/`](PPO%20et%20A2C/) |
| 7 | Aller plus loin | Sample Factory, RL avancé | 🔥 Doom (pixels) | [`PPO et A2C/`](PPO%20et%20A2C/) |

**Une idée forte du parcours** : les méthodes *value-based* (on apprend « combien vaut chaque action ») vs *policy-based* (on apprend directement la politique). Le dépôt explore les deux familles, du discret au continu, avec des notes pédagogiques dédiées :

- 📝 [`Q-learning/q_learning_notes.md`](Q-learning/q_learning_notes.md) — Q-Learning, DQN, target network, experience replay
- 📝 [`politique_based/notes.md`](politique_based/notes.md) — REINFORCE, policy gradient, PPO et SAC
- 📝 [`notebook/RL_from_scrath.md`](notebook/RL_from_scrath.md) — coder un agent policy gradient de A à Z

## 🎬 Résultats en vidéo — lecture automatique

Chaque agent entraîné a été évalué et filmé. Les vidéos ci-dessous se lancent **automatiquement** (sans son, en boucle) : il suffit de regarder l'agent jouer 👀.

### 🤖 Les agents entraînés

<table align="center">
  <tr>
    <td align="center">
      <strong>❄️ FrozenLake — Q-Learning</strong><br>
      <em>traverser le lac gelé jusqu'à la sortie</em><br>
      <video src="videos/frozen_lake.mp4" autoplay muted loop playsinline controls width="100%"></video>
    </td>
    <td align="center">
      <strong>🚕 Taxi-v3 — Q-Learning</strong><br>
      <em>prendre le passager et le déposer</em><br>
      <video src="videos/taxi-v4.mp4" autoplay muted loop playsinline controls width="100%"></video>
    </td>
  </tr>
  <tr>
    <td align="center">
      <strong>⛰️ MountainCar — DQN</strong><br>
      <em>prendre de l'élan pour atteindre le sommet</em><br>
      <video src="videos/mountain-car-episode-3.mp4" autoplay muted loop playsinline controls width="100%"></video>
    </td>
    <td align="center">
      <strong>🚀 LunarLander — PPO (codé de zéro)</strong><br>
      <em>atterrir en douceur sur la Lune</em><br>
      <video src="videos/lunarlander-discret-episode-0.mp4" autoplay muted loop playsinline controls width="100%"></video>
    </td>
  </tr>
</table>

### 🏗️ Nos implémentations « from scratch »

Les mêmes environnements, résolus cette fois par nos **propres implémentations** du Q-Learning, codées à la main (sans bibliothèque d'apprentissage par renforcement) :

<table align="center">
  <tr>
    <td align="center">
      <strong>❄️ FrozenLake — Q-Learning maison</strong><br>
      <em>Q-table 16 × 4 écrite en NumPy</em><br>
      <video src="videos/frozen-lake-scratch-episode-0.mp4" autoplay muted loop playsinline controls width="100%"></video>
    </td>
    <td align="center">
      <strong>🚕 Taxi-v3 — Q-Learning maison</strong><br>
      <em>Q-table 500 × 6 écrite en NumPy</em><br>
      <video src="videos/taxi-scratch-episode-0.mp4" autoplay muted loop playsinline controls width="100%"></video>
    </td>
  </tr>
</table>

> ⚠️ **Note technique** : les navigateurs n'autorisent l'autoplay que si la vidéo est **sans son** (`muted`) — c'est pourquoi les vidéos sont volontairement muettes. Si l'autoplay ne se déclenche pas chez vous, appuyez simplement sur ▶️.


## Modèles entraînés

Les agents les plus aboutis sont sauvegardés dans [`models/`](models/) et peuvent être rechargés pour rejouer des parties :

| Fichier | Environnement | Algorithme |
|---|---|---|
| `q-table-frozenlake.pkl` | ❄️ FrozenLake-v1 | Q-Learning (table 16×4) |
| `q-table-taxi.pkl` | 🚕 Taxi-v3 | Q-Learning (table 500×6) |
| `mountain-car.pt` | ⛰️ MountainCar-v0 | DQN |
| `lunarlanderdiscret-actor.pt` / `lunarlanderdiscret-critic.pt` | 🚀 LunarLander-v3 | PPO (Actor-Critic) |

## 🚀 Installer et lancer

Le projet est géré avec [`uv`](https://docs.astral.sh/uv/) (Python 3.12+) :




## 🛠️ Stack technique

- **Python 3.12+** — gestion de projet avec `uv`
- **Gymnasium** — les environnements (FrozenLake, Taxi, MountainCar, CartPole, LunarLander, Atari, Doom…)
- **PyTorch** — implémentations maison (DQN, PPO, policy gradient)
- **Stable-Baselines3** — implémentations de référence pour comparaison
- **TensorBoard** — suivi des entraînements (logs dans `notebook/logs/`)
- **MoviePy / FFmpeg** — enregistrement des vidéos

## 📚 Ressources et crédits

- [Hugging Face Deep RL Course](https://huggingface.co/deep-rl-course/unit0/introduction)
- [Documentation Gymnasium](https://gymnasium.farama.org/)
- [Documentation Stable-Baselines3](https://stable-baselines3.readthedocs.io/)

## 📄 Licence

Ce projet est distribué sous licence **Apache 2.0** — voir [`LICENSE`](LICENSE).