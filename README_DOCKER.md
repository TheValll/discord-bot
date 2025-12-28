# Discord Bot & Dashboard - Docker Configuration

## Prerequisites

- Docker Desktop installé et en cours d'exécution
- Docker Compose

## Configuration

### 1. Configurer les variables d'environnement

Éditez le fichier `.env` à la racine du projet avec vos paramètres:

```
DISCORD_TOKEN=your_discord_bot_token
CHANNEL_LOG_ID=your_log_channel_id
SKYNOZ_CHANNEL_ID=your_skynoz_channel_id
```

### 2. Structure du projet

```
discord-bot/
├── bot/
│   ├── Dockerfile
│   ├── main.py
│   └── utils.py
├── web/
│   ├── Dockerfile
│   ├── dashboard.py
│   └── templates/
│       └── index.html
├── data/
│   ├── birthdays.json
│   ├── game_logs.txt
│   ├── leaderboard.json
│   └── votes.json
├── requirements.txt
├── docker-compose.yml
├── .env
└── .env.example
```

## Lancer les conteneurs

### Démarrer les services

```bash
docker-compose up -d
```

### Voir les logs

```bash
docker-compose logs -f bot
docker-compose logs -f web
```

### Arrêter les services

```bash
docker-compose down
```

### Reconstruire les images

```bash
docker-compose up -d --build
```

## Accès

- **Dashboard Web**: http://localhost:3018
- **Bot Discord**: Connecté au serveur Discord spécifié

## Services

### Bot (discord-bot)

- Conteneur: `discord-bot`
- Fonction: Gère les anniversaires et le jeu Skynoz sur Discord
- Environnement: Variables du fichier `.env`

### Web Dashboard (discord-dashboard)

- Conteneur: `discord-dashboard`
- Port: **3018**
- Fonction: Interface web pour gérer les données (anniversaires, votes, logs)

## Volumes

Les deux services utilisent un volume partagé pour `/app/data`:

- Synchronisation automatique des fichiers JSON et logs
- Persistance des données entre les redémarrages

## Network

Les services communiquent via un réseau Docker personnalisé (`discord-network`).

## Troubleshooting

### Le web ne démarre pas sur le port 3018

```bash
docker-compose logs web
```

### Vérifier que les données sont bien synchronisées

```bash
docker exec discord-dashboard ls -la /app/data
```

### Vérifier la connexion du bot

```bash
docker-compose logs bot
```
