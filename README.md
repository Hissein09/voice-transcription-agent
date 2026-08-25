````markdown
# Voice Transcription Agent 🎤

Un système complet de transcription vocale (Speech-to-Text) et d'exécution de commandes vocales pour agents IA. Supporte **DeepSeek**, **Harness** et autres agents intelligents.

## 🎯 Fonctionnalités

- ✅ **Transcription vocale en temps réel** - Conversion de la parole en texte
- ✅ **Multi-agents** - Support pour DeepSeek, Harness, OpenAI et extensible
- ✅ **Voice Activity Detection (VAD)** - Détection automatique de la parole
- ✅ **API REST complète** - Endpoints pour transcription et exécution de commandes
- ✅ **Mode interactif** - Interface en ligne de commande pour les tests
- ✅ **Gestion de l'historique** - Contexte conversationnel persistant
- ✅ **Support multi-langue** - Français, anglais et autres langues

## 📋 Prérequis

- Python 3.8+
- pip ou conda
- Clés API pour les services (OpenAI, DeepSeek, Harness)
- Microphone fonctionnel

## 🚀 Installation

### 1. Cloner le repository

```bash
git clone https://github.com/Hissein09/voice-transcription-agent.git
cd voice-transcription-agent
```

### 2. Créer un environnement virtuel

```bash
python -m venv venv
source venv/bin/activate  # Sur Windows: venv\Scripts\activate
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 4. Configurer les variables d'environnement

```bash
cp .env.example .env
# Éditer .env et ajouter vos clés API
```

**Variables requises dans `.env`:**

```env
# Transcription
OPENAI_API_KEY=sk-...

# Agents
DEEPSEEK_API_KEY=your_key
DEEPSEEK_BASE_URL=https://api.deepseek.com/v1

HARNESS_API_KEY=your_key
HARNESS_BASE_URL=https://api.harness.io
HARNESS_ACCOUNT_ID=your_account_id
```

## 💻 Utilisation

### Mode Interactif

Écoutez et traitez les commandes vocales en temps réel :

```bash
python main.py --mode interactive --provider openai --language fr-FR
```

**Options :**
- `--mode` : `interactive` ou `server`
- `--provider` : `openai`, `deepseek`, `google`
- `--language` : Code langue (ex: `fr-FR`, `en-US`)

### Mode Serveur API

Lancez le serveur REST :

```bash
python main.py --mode server --host 0.0.0.0 --port 8000
```

API disponible sur `http://localhost:8000`
Documentation interactive : `http://localhost:8000/docs`

## 🔌 API Endpoints

### 1. Transcription audio

```bash
curl -X POST "http://localhost:8000/transcribe" \
  -F "file=@audio.wav" \
  -F "provider=openai" \
  -F "language=fr-FR"
```

**Réponse :**
```json
{
  "success": true,
  "text": "Bonjour comment allez vous",
  "provider": "openai"
}
```

### 2. Exécuter une commande

```bash
curl -X POST "http://localhost:8000/command" \
  -H "Content-Type: application/json" \
  -d '{
    "command": "Qu'"'"'est-ce que le machine learning?",
    "agent_id": "deepseek"
  }'
```

**Réponse :**
```json
{
  "success": true,
  "command": "Qu'"'"'est-ce que le machine learning?",
  "result": "Le machine learning est...",
  "agent": "deepseek"
}
```

### 3. Lister les agents disponibles

```bash
curl "http://localhost:8000/agents"
```

**Réponse :**
```json
{
  "agents": {
    "deepseek": {
      "name": "DeepSeek",
      "connected": true,
      "active": true
    },
    "harness": {
      "name": "Harness",
      "connected": true,
      "active": false
    }
  },
  "active_agent": "deepseek"
}
```

### 4. Activer un agent

```bash
curl -X POST "http://localhost:8000/agents/harness/activate"
```

### 5. Enregistrer et traiter

```bash
curl -X POST "http://localhost:8000/record-and-process?agent_id=deepseek"
```

Enregistre 5 secondes de voix, transcrit et traite via l'agent.

## 📁 Structure du projet

```
voice-transcription-agent/
├── src/
│   ├── __init__.py
│   ├── audio/
│   │   ├── recorder.py         # Enregistrement audio
│   │   └── vad.py              # Voice Activity Detection
│   ├── transcription/
│   │   └── transcriber.py      # Support multi-providers
│   ├── agents/
│   │   ├── base_agent.py       # Classe de base
│   │   ├── deepseek_agent.py   # Agent DeepSeek
│   │   ├── harness_agent.py    # Agent Harness
│   │   └── agent_manager.py    # Gestionnaire d'agents
│   ├── api/
│   │   └── server.py           # Serveur FastAPI
│   │   └── __init__.py         # Init package
│   ├── core/
│   │   ├── pipeline.py         # Pipeline principal
│   │   └── __init__.py         # Init package
│   └── agents/
│       └── __init__.py         # Init package
├── config/
│   └── config.yaml             # Configuration
├── main.py                      # Point d'entrée
├── requirements.txt             # Dépendances
├── .env.example                 # Template variables
└── README.md                    # Cette documentation
```

## 🔧 Configuration

Éditez `config/config.yaml` pour personnaliser :

```yaml
audio:
  sample_rate: 16000
  channels: 1
  chunk_size: 1024

transcription:
  provider: openai
  language: fr-FR
  model: whisper-1

agents:
  deepseek:
    enabled: true
    model: deepseek-chat
  harness:
    enabled: true
```

## 🔐 Sécurité

- ✅ Jamais committer les clés API
- ✅ Utiliser `.env` pour les variables sensibles
- ✅ Limiter l'accès à l'API en production
- ✅ Utiliser HTTPS/TLS

**Bonnes pratiques :**

```bash
# Ne pas committer
git rm --cached .env

# Ajouter au .gitignore
echo ".env" >> .gitignore
```

## 📖 Exemples d'utilisation

### Python

```python
from src.core.pipeline import VoiceCommandPipeline

# Créer le pipeline
pipeline = VoiceCommandPipeline(transcriber_provider="openai")

# Initialiser les agents
pipeline.initialize_agents()

# Enregistrer et traiter
audio_data = pipeline.record_voice_command()
audio_path = pipeline.recorder.save_audio(audio_data)
text = pipeline.transcribe_audio(audio_path)
result = pipeline.process_command(text, agent_id="deepseek")

print(result)
```

### cURL pour l'API

```bash
# Santé du serveur
curl http://localhost:8000/health

# Transcriber un fichier
curl -X POST -F "file=@mon_audio.wav" \
  http://localhost:8000/transcribe

# Exécuter une commande
curl -X POST -H "Content-Type: application/json" \
  -d '{"command":"Fais un résumé de ceci"}' \
  http://localhost:8000/command
```

## 🐛 Dépannage

### Problème : Microphone non détecté
```bash
# Vérifier les appareils audio disponibles
python -c "import pyaudio; p = pyaudio.PyAudio(); print(p.get_device_count())"
```

### Problème : Clés API invalides
```bash
# Vérifier les variables d'environnement
python -c "import os; print(os.getenv('OPENAI_API_KEY'))"
```

### Problème : Transcription lente
- Réduire `max_duration` dans la config
- Utiliser un provider plus rapide
- Augmenter les ressources système

## 🤝 Contributing

Les contributions sont bienvenues ! N'hésitez pas à :

1. Fork le projet
2. Créer une branche (`git checkout -b feature/AmazingFeature`)
3. Commit les changements (`git commit -m 'Add AmazingFeature'`)
4. Push vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrir une Pull Request

## 📝 Licence

Ce projet est sous licence MIT - voir le fichier LICENSE pour plus de détails.

## 📞 Support

Pour les problèmes ou questions :

- 📧 Ouvrir une issue sur GitHub
- 💬 Utiliser les discussions
- 🐛 Rapporter les bugs

## 🚀 Roadmap

- [ ] Support Google Cloud Speech
- [ ] Support Azure Speech Services
- [ ] Cache de transcription
- [ ] Tests unitaires complets
- [ ] Docker container
- [ ] Documentation API OpenAPI complète
- [ ] Support WebSocket pour streaming temps réel
- [ ] Interface web de gestion

## ⭐ Remerciements

- OpenAI pour Whisper
- DeepSeek pour l'API
- Harness pour l'intégration
- Communauté open-source

---

**Créé avec ❤️ par Hissein09**

Dernière mise à jour : 2026-08-25
````
