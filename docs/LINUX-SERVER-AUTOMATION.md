# Automatisation Linux et gestion de services

## Contexte

Dans le cadre de mon projet de serveur privé Talisman Online, j'ai travaillé sur des environnements Linux et automatisé certaines tâches liées à l'administration du serveur. Des opérations ont été automatisées sur Ubuntu ; l'environnement serveur documenté par la suite utilisait CentOS 7.9 dans une machine virtuelle.

Cette distinction est importante : les commandes et fichiers de services peuvent varier selon la distribution et la configuration.

## Pourquoi automatiser un serveur ?

Un serveur applicatif est composé de plusieurs processus qui doivent être lancés, arrêtés et contrôlés correctement. Répéter manuellement les mêmes commandes peut entraîner des oublis ou un mauvais ordre de démarrage.

L'automatisation permet notamment de :
- standardiser les opérations récurrentes ;
- démarrer les composants dans un ordre défini ;
- vérifier l'état des services ;
- consulter rapidement les journaux ;
- faciliter le diagnostic après un redémarrage.

## Services du laboratoire Talisman

Les composants observés dans l'environnement étaient :

- `db_server` : composant associé au service DB ;
- `login_server` : composant associé à la connexion ;
- `game_server` : composant associé au jeu.

Les unités systemd rencontrées comprenaient :

- `talisman-mysql-socket.service`
- `talisman-db.service`
- `talisman-login.service`
- `talisman-game.service`

Une séquence de démarrage testée consistait à préparer le socket MySQL, puis à démarrer le service DB, le service de connexion et enfin le service de jeu.

## Exemple de contrôle des services

Les commandes ci-dessous illustrent comment contrôler l'état d'une unité systemd :

```bash
systemctl status talisman-db.service
systemctl is-active talisman-db.service
sudo journalctl -u talisman-db.service -n 100
```

Pour les autres unités, remplacer le nom du service. Ces commandes supposent que les unités existent sur le système.

## Vérification des processus et des ports

Pendant les tests, les processus et ports étaient contrôlés avec des outils Linux :

```bash
ps aux | grep -E 'db_server|login_server|game_server' | grep -v grep
ss -lntp
```

Il est important de distinguer :
- un service systemd déclaré actif ;
- un processus réellement présent ;
- un port en écoute ;
- une application qui répond correctement aux requêtes.

Ces vérifications ne prouvent pas toutes la même chose. Un service peut être actif sans que le test fonctionnel attendu soit réussi.

## Bonnes pratiques pour un script d'administration

Un script destiné à gérer des services devrait :
1. vérifier les privilèges nécessaires ;
2. confirmer que les unités attendues existent ;
3. exécuter les opérations dans l'ordre ;
4. contrôler le code de retour de chaque commande ;
5. arrêter la procédure si une étape critique échoue ;
6. afficher un message clair ;
7. conserver un journal sans données sensibles.

## Limites et sécurité

Les fichiers de configuration du serveur Talisman, les binaires, les identifiants, les adresses privées et les scripts opérationnels privés ne sont pas inclus dans ce dépôt public.

Les exemples présentés sont des commandes d'administration et des principes de conception. Ils ne constituent pas un script universel prêt à être exécuté sur un autre serveur.
