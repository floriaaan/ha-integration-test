# Mon Intégration Custom pour Home Assistant

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/custom-components/hacs)

Intégration Home Assistant minimaliste pour tester et expérimenter.

## Installation via HACS

### Méthode 1 : Dépôt custom (recommandé pour débuter)

1. Ouvre HACS dans Home Assistant
2. Clique sur les 3 points en haut à droite
3. Sélectionne "Dépôts personnalisés"
4. Ajoute l'URL de ton repo GitHub : `https://github.com/votre-username/mon-integration-ha`
5. Sélectionne la catégorie "Integration"
6. Clique sur "Ajouter"
7. Trouve "Mon Intégration Custom" dans HACS et installe-le
8. Redémarre Home Assistant

### Méthode 2 : Installation manuelle

1. Télécharge le dossier `custom_components/mon_integration`
2. Copie-le dans `config/custom_components/`
3. Redémarre Home Assistant

## Configuration

1. Va dans **Paramètres** → **Appareils et services**
2. Clique sur **+ Ajouter une intégration**
3. Recherche **Mon Intégration Custom**
4. Ajoute l'intégration

## Entités fournies

### Sensors
- `sensor.mon_sensor_temperature` - Température exemple (20.5°C)
- `sensor.mon_sensor_humidite` - Humidité exemple (65%)

### Todo List
- `todo.ma_liste_de_taches` - Liste de tâches avec exemples

## Développement

Cette intégration est un socle minimal pour expérimenter. Tu peux facilement :
- Ajouter de nouveaux sensors
- Modifier les valeurs dynamiquement
- Étendre les fonctionnalités de la todo list

## Support

Pour tout problème ou question, ouvre une issue sur GitHub.