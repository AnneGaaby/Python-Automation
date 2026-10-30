# Automatisation Windows avec PowerShell

## Pourquoi PowerShell ?

PowerShell est un environnement de ligne de commande et un langage de script adapté à l'administration Windows. Il permet d'automatiser des opérations, d'appeler des programmes, de manipuler des fichiers et de coordonner des tâches.

Dans mes projets, PowerShell a été utilisé pour automatiser certaines opérations de mon environnement Windows et participer au lancement et à l'orchestration du projet J.A.R.V.I.S.

## Exemple de structure d'un script

Un script d'automatisation maintenable devrait généralement contenir :

- une description de son objectif ;
- des paramètres clairement nommés ;
- des vérifications préalables ;
- les opérations à exécuter ;
- une gestion des erreurs ;
- des messages et journaux compréhensibles ;
- un code de sortie cohérent.

## Exemple pédagogique : vérifier la présence d'un programme

```powershell
$program = "python"

$command = Get-Command $program -ErrorAction SilentlyContinue

if ($null -eq $command) {
    Write-Error "Le programme '$program' est introuvable."
    exit 1
}

Write-Host "Programme trouvé : $($command.Source)"
exit 0
```

Cet exemple est un modèle pédagogique autonome, pas un extrait du script privé J.A.R.V.I.S.

## Exemple pédagogique : vérifier un service Windows

```powershell
$serviceName = "Spooler"

$service = Get-Service -Name $serviceName -ErrorAction SilentlyContinue

if ($null -eq $service) {
    Write-Error "Service introuvable : $serviceName"
    exit 1
}

Write-Host "Service : $($service.Name)"
Write-Host "État : $($service.Status)"
```

## Exécuter un script avec prudence

Avant d'exécuter un script :
- lire son contenu ;
- vérifier les chemins et les commandes appelées ;
- éviter les privilèges administrateur si non nécessaires ;
- ne pas désactiver globalement les protections de sécurité ;
- tester dans un environnement contrôlé ;
- prévoir une procédure de retour arrière pour les changements importants.

La politique d'exécution PowerShell et les droits disponibles dépendent de la configuration Windows. Ne pas contourner les protections d'une machine administrée par une organisation.

## Automatisation et J.A.R.V.I.S.

Le projet privé contient notamment le script `Automacao_JARVIS.ps1`. Il participe aux automatisations de l'environnement local de l'assistant. Le code source et les chemins personnels ne sont pas publiés ici.

Cette documentation sépare volontairement les exemples pédagogiques publics des scripts privés réellement utilisés.
