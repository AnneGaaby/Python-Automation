# Python & Automation

**Automatisation de tâches · Python · PowerShell · Linux · Windows · APIs · Systèmes**

Ce dépôt présente mes projets et expérimentations autour de l'automatisation informatique. Mon objectif est de réduire les tâches répétitives, fiabiliser les opérations et relier différents outils et services grâce à des scripts et des workflows documentés.

**Autrice :** Anne Gabrielly Alves  
**Formation :** Développement Web et Web Mobile — Skill&You Suisse  
**Environnement :** Windows 11 · Linux · Python · PowerShell · Docker · services système  
**Statut :** portfolio personnel et documentation technique

---

## Pourquoi l'automatisation ?

Dans une équipe informatique, de nombreuses tâches reviennent régulièrement : préparer un environnement, vérifier qu'un service fonctionne, organiser des fichiers, lancer des opérations dans le bon ordre, contrôler des journaux ou relier plusieurs outils.

L'automatisation consiste à transformer ces étapes en procédures reproductibles exécutées par un programme ou un script. Elle peut faire gagner du temps, réduire les erreurs manuelles et rendre les opérations plus faciles à suivre.

Ce dépôt montre comment j'apprends et applique ces principes dans des environnements Windows et Linux, notamment à travers des scripts Python et PowerShell et des expérimentations d'automatisation de services.

## Domaines de travail

| Domaine | Exemples de tâches |
|---|---|
| Automatisation Windows | Scripts PowerShell, lancement de programmes, opérations répétitives et orchestration locale |
| Automatisation Linux | Commandes système, vérification de services, démarrage coordonné et opérations serveur |
| Administration de services | Contrôle d'état, démarrage, arrêt, redémarrage et consultation des journaux |
| Automatisation Python | Scripts, logique applicative, intégration entre composants et services |
| Environnements de développement | Préparation et lancement d'outils, services locaux et environnements de test |
| IA locale et assistants | Expérimentations d'orchestration autour d'un assistant personnel local |
| Documentation et fiabilité | Procédures reproductibles, gestion des erreurs et séparation de la configuration |

## Exemples Python exécutables

Le dépôt contient maintenant des scripts autonomes, avec des cas d'usage concrets :

- `examples/file_organizer.py` — organisation de fichiers avec aperçu par défaut ;
- `examples/disk_usage_report.py` — rapport d'espace disque ;
- `examples/tcp_health_check.py` — vérification d'un port TCP avec adresse fictive de documentation ;
- `examples/log_analyzer.py` — comptage des niveaux dans un fichier journal ;
- `examples/backup_to_zip.py` — création d'une archive ZIP horodatée.

Les instructions d'exécution sont dans [Exemples Python](docs/PYTHON-EXAMPLES.md). Des tests unitaires sont disponibles dans `tests/`.

## Projets et cas pratiques documentés

### 1. J.A.R.V.I.S. — assistant local et automatisation Windows

Expérimentation d'un assistant personnel local qui rassemble plusieurs composants : serveur Python, interface web, modèles locaux via LM Studio, reconnaissance vocale avec Whisper, synthèse vocale et automatisations PowerShell.

Les scripts privés incluent notamment `server.py`, `server_com_memoria.py` et `Automacao_JARVIS.ps1`. Le code source et les configurations privées ne sont pas publiés dans ce dépôt.

Voir [Étude de cas J.A.R.V.I.S.](docs/CASE-STUDY-JARVIS.md).

### 2. Automatisation d'un serveur Linux

Travail pratique autour d'un serveur Talisman Online dans un environnement Linux. L'environnement serveur a été documenté autour de services Linux, de leur ordre de démarrage et de leurs vérifications.

Les composants serveur et fichiers privés ne sont pas distribués ici.

Voir [Automatisation Linux et services](docs/LINUX-SERVER-AUTOMATION.md).

### 3. Scripts et automatisation Windows avec PowerShell

PowerShell a été utilisé pour automatiser des opérations locales et participer à l'orchestration de l'environnement J.A.R.V.I.S.

Voir [Automatisation Windows avec PowerShell](docs/POWERSHELL-WINDOWS.md).

## Comment aborder un problème d'automatisation

Ma démarche de travail :

1. **Comprendre la tâche** : identifier ce qui est répétitif, les entrées, les sorties et les contraintes.
2. **Définir le résultat attendu** : décrire précisément ce que le script doit faire.
3. **Découper le processus** : séparer les étapes en opérations simples.
4. **Choisir l'outil adapté** : Python pour la logique et l'intégration, PowerShell pour les opérations Windows, shell et outils Linux pour l'administration système.
5. **Gérer les erreurs** : prévoir les fichiers absents, les services indisponibles, les droits insuffisants et les interruptions.
6. **Tester** : commencer dans un environnement contrôlé et vérifier les résultats.
7. **Documenter** : expliquer l'installation, l'exécution, les paramètres et les limites.

## Technologies et outils explorés

- **Python** — scripts, logique d'automatisation et serveur applicatif.
- **PowerShell** — automatisation et orchestration sous Windows.
- **Linux / Bash** — opérations système et administration de services.
- **systemd** — gestion de services Linux.
- **Docker** — expérimentation d'environnements conteneurisés.
- **LM Studio** — exécution locale de modèles de langage.
- **Whisper** — reconnaissance vocale locale.
- **Kokoro** — expérimentation de synthèse vocale.
- **OpenHands** — expérimentation d'un environnement d'agent de développement.

La présence d'un outil dans cette liste signifie qu'il a été exploré dans le cadre des projets ; elle ne signifie pas que chaque intégration est finalisée ou déployée en production.

## Compétences mises en pratique

- Décomposer un processus en étapes automatisables.
- Écrire et organiser des scripts.
- Travailler dans des environnements Windows et Linux.
- Lancer et contrôler des services.
- Relier plusieurs composants logiciels.
- Lire des journaux et rechercher des erreurs.
- Utiliser des outils en ligne de commande.
- Documenter des procédures techniques.
- Distinguer une expérimentation d'une fonctionnalité validée.

## Sécurité et qualité

Un script d'automatisation peut agir sur des fichiers, des services et des données. Il doit donc être conçu avec prudence.

- Ne jamais intégrer de mots de passe, tokens ou clés dans le code.
- Utiliser des variables d'environnement ou un gestionnaire de secrets adapté.
- Vérifier les chemins et les paramètres avant de modifier des fichiers.
- Limiter les privilèges au strict nécessaire.
- Prévoir des journaux utiles sans enregistrer de données sensibles.
- Gérer les erreurs et les codes de retour.
- Tester d'abord dans un environnement non critique.
- Éviter les suppressions ou modifications irréversibles sans confirmation et sauvegarde.

Voir [SECURITY.md](SECURITY.md).

## Structure du dépôt

```text
Python-Automation/
├── README.md
├── SECURITY.md
├── examples/
├── tests/
└── docs/
    ├── PYTHON-EXAMPLES.md
    ├── CASE-STUDY-JARVIS.md
    ├── LINUX-SERVER-AUTOMATION.md
    ├── POWERSHELL-WINDOWS.md
    └── PORTFOLIO-ROADMAP.md
```

## Prochaines améliorations

Le dépôt sera enrichi avec des exemples de scripts autonomes, tests, journaux d'exécution anonymisés et captures d'écran lorsque ceux-ci pourront être publiés sans exposer les environnements privés.

Voir [Feuille de route](docs/PORTFOLIO-ROADMAP.md).

## À propos

Je suis Anne Gabrielly, basée dans le canton de Vaud, en Suisse, et en formation en développement Web et Web Mobile chez Skill&You Suisse. Je m'intéresse particulièrement à l'automatisation, aux systèmes, au support informatique, aux infrastructures et aux outils d'IA locaux.

- **Portfolio :** https://annegaaby.github.io/Anne-Gabrielly/
- **GitHub :** https://github.com/AnneGaaby

---

*Ce dépôt documente des projets personnels et des expérimentations. Il ne prétend pas présenter des déploiements en production ni des fonctionnalités qui n'ont pas été validées.*
