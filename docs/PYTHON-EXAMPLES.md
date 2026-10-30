# Exemples Python — automatisations pratiques

Ce dossier contient des petits outils indépendants, conçus pour illustrer des tâches concrètes d'automatisation. Ils utilisent uniquement la bibliothèque standard de Python : aucune dépendance externe n'est nécessaire.

## Prérequis

- Python 3.10 ou version ultérieure recommandée.
- Terminal Windows, PowerShell, macOS ou Linux.
- Accès en lecture/écriture aux dossiers concernés.

Vérifier Python :

```bash
python --version
```

Sur certaines installations Linux/macOS, la commande peut être `python3`.

## 1. Organiser automatiquement des fichiers

Fichier : `examples/file_organizer.py`

Le script classe les fichiers d'un dossier par catégorie (images, documents, archives, etc.). Par sécurité, il fonctionne en mode aperçu par défaut et ne déplace rien sans l'option `--apply`.

Aperçu :

```bash
python examples/file_organizer.py ./demo-files
```

Appliquer les déplacements après vérification :

```bash
python examples/file_organizer.py ./demo-files --apply
```

En cas de nom déjà utilisé, le script ajoute un suffixe au lieu d'écraser le fichier existant.

## 2. Vérifier l'espace disque

Fichier : `examples/disk_usage_report.py`

```bash
python examples/disk_usage_report.py
python examples/disk_usage_report.py C:\\
```

Le rapport affiche l'espace total, utilisé et disponible pour le chemin demandé.

## 3. Tester un port TCP

Fichier : `examples/tcp_health_check.py`

Le script vérifie si un hôte accepte une connexion TCP sur un port donné. L'adresse par défaut `192.0.2.10` appartient à une plage réservée à la documentation : elle est fictive et sert uniquement d'exemple.

Exemple avec une cible de laboratoire que vous êtes autorisé à tester :

```bash
python examples/tcp_health_check.py --host 192.0.2.10 --port 8080
```

Remplacez l'adresse et le port par ceux de votre propre environnement de test. Le script vérifie uniquement l'ouverture TCP, pas le bon fonctionnement applicatif du service.

## 4. Analyser un fichier journal

Fichier : `examples/log_analyzer.py`

```bash
python examples/log_analyzer.py ./sample.log
```

Le script compte les lignes contenant les niveaux CRITICAL, ERROR, WARNING, INFO et DEBUG. Il s'agit d'un analyseur pédagogique simple : il ne remplace pas un parseur adapté au format réel de chaque application.

## 5. Créer une sauvegarde ZIP

Fichier : `examples/backup_to_zip.py`

```bash
python examples/backup_to_zip.py ./demo-files --destination ./backups
```

Le script crée une archive ZIP horodatée. Vérifiez le contenu de l'archive et testez régulièrement la restauration : une sauvegarde n'est utile que si elle peut être restaurée.

## Bonnes pratiques

- Tester d'abord avec des dossiers et fichiers de démonstration.
- Vérifier les chemins avant de lancer une opération.
- Garder une copie des données importantes.
- Ne pas lancer de tests réseau contre des systèmes sans autorisation.
- Ne jamais inclure de mots de passe, tokens, adresses privées réelles ou données personnelles dans les exemples publics.
