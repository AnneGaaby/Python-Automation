# Étude de cas — J.A.R.V.I.S., assistant local et automatisation

## Objectif

J.A.R.V.I.S. est un projet personnel visant à expérimenter un assistant local capable de réunir une interface, un serveur applicatif, des modèles d'intelligence artificielle et des outils système.

L'idée est de réduire les interactions manuelles entre plusieurs outils et de construire progressivement une architecture où des composants spécialisés communiquent entre eux.

## Architecture explorée

Les éléments travaillés ou testés comprennent :

- **Python** : serveur applicatif et logique de l'assistant.
- **Interface web locale** : point d'interaction avec l'assistant.
- **LM Studio** : exécution locale de modèles de langage, notamment des modèles Qwen.
- **Whisper large-v3** : reconnaissance vocale testée avec accélération CUDA et calcul float16.
- **Kokoro** : expérimentation de synthèse vocale.
- **PowerShell** : automatisations et lancement de tâches dans l'environnement Windows.
- **Docker / OpenHands** : expérimentation d'un environnement d'agent et de services associés.

Cette architecture représente les composants explorés. Elle ne signifie pas que toute la chaîne fonctionne déjà de bout en bout.

## Automatisation Windows

Le projet utilise des scripts PowerShell pour automatiser certaines opérations de l'environnement local. Le script nommé `Automacao_JARVIS.ps1` fait partie du projet privé.

Les scripts Python `server.py` et `server_com_memoria.py` font également partie du travail réalisé. Leur code n'est pas publié dans ce dépôt.

## Tests et observations

Les éléments suivants ont été testés séparément dans le laboratoire :

- serveur Whisper démarré avec le modèle large-v3 chargé ;
- accélération CUDA et calcul float16 détectés pour Whisper ;
- interface locale de l'environnement OpenHands accessible pendant les essais ;
- expérimentation de modèles locaux avec LM Studio ;
- démarrage et essais de synthèse vocale avec Kokoro.

Des difficultés ont également été rencontrées, notamment avec la détection du microphone sans fil Logitech et l'intégration des composants audio.

## Points qui restent à valider

- fonctionnement complet et stable de la chaîne microphone → reconnaissance vocale → assistant → synthèse vocale ;
- gestion persistante de la mémoire et du contexte ;
- contrôle sécurisé de fichiers locaux ;
- exécution d'actions avec confirmation et gestion des erreurs ;
- tests reproductibles après redémarrage.

## Principes de sécurité

Un assistant qui peut lancer des commandes ou accéder à des fichiers doit être conçu avec des limites strictes :

- accès limité à des dossiers explicitement autorisés ;
- confirmation avant les actions destructrices ;
- séparation entre conversation et exécution de commandes ;
- journalisation des actions ;
- absence de secrets dans les fichiers publics ;
- possibilité d'arrêter les services et révoquer les accès.

## Ce que cette expérimentation m'a appris

- structurer une application composée de plusieurs services ;
- connecter des composants Python à des outils externes ;
- travailler avec des modèles d'IA exécutés localement ;
- expérimenter la reconnaissance et la synthèse vocales ;
- automatiser des opérations Windows avec PowerShell ;
- diagnostiquer les problèmes d'intégration entre matériel, logiciels et services.

Le code source, les paramètres privés et les configurations de la machine ne sont pas publiés. Cette documentation décrit le travail et les tests sans exposer l'implémentation privée.
