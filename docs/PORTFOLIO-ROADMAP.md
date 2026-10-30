# Feuille de route — Python & Automation

Ce document distingue les éléments déjà explorés des améliorations à réaliser pour rendre le dépôt plus démonstratif et reproductible.

## Travail déjà exploré

- Automatisation de tâches dans des environnements Linux pour le projet serveur Talisman.
- Scripts PowerShell dans l'environnement Windows du projet J.A.R.V.I.S.
- Serveur applicatif Python et interface locale pour J.A.R.V.I.S.
- Expérimentation de composants IA locaux et de services vocaux.
- Utilisation de Docker/OpenHands dans un environnement de test.
- Vérification de services, processus et journaux pendant les opérations serveur.

## Améliorations possibles

### Exemples Python indépendants
Ajouter de petits scripts publics, autonomes et sûrs :
- organiser des fichiers avec mode simulation ;
- vérifier la disponibilité d'un service ;
- surveiller l'espace disque ;
- analyser des fichiers journaux ;
- produire un rapport de diagnostic.

### Qualité logicielle
- ajouter des tests unitaires avec pytest ;
- utiliser logging plutôt que des impressions dispersées ;
- gérer les erreurs et codes de retour ;
- documenter les dépendances ;
- fournir un fichier de configuration d'exemple sans secret ;
- ajouter un workflow d'intégration continue.

### Démonstrations
- captures d'écran anonymisées ;
- exemples d'entrée et de sortie ;
- diagrammes de flux ;
- instructions de lancement ;
- limites connues et résultats des tests.

## Critères avant publication

Chaque nouveau script public devrait :
1. avoir un objectif clair ;
2. être testé dans un environnement propre ;
3. expliquer les paramètres et dépendances ;
4. ne contenir aucun secret ni chemin personnel ;
5. éviter les opérations destructrices par défaut ;
6. inclure une démonstration ou un test ;
7. préciser s'il s'agit d'un exemple pédagogique ou d'un outil réellement utilisé.

## Objectif professionnel

Le but est de montrer une démarche utile pour des rôles de junior IT support, technicienne systèmes, automatisation, scripting ou développement backend : comprendre un besoin, concevoir une procédure, l'implémenter, la tester, diagnostiquer les erreurs et documenter le résultat.
