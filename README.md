 Description du projet

Ce projet met en œuvre **YOLOv8** pour la détection et le suivi d’objets dans une vidéo.  
Il permet de détecter automatiquement des **personnes**, des **sacs à dos** et des **sacs à main** dans une scène urbaine, puis de leur attribuer un **ID unique** grâce à l’algorithme **BoT-SORT**.

 Exemple d’utilisation : suivi de piétons dans une rue animée.  
La vidéo utilisée comme input provient de [Pexels](https://www.pexels.com/video/busy-snowy-city-street-with-walking-people-30820647/).

Le script :
- Charge la vidéo d’entrée `video/video_input.mp4`
- Applique la détection et le tracking avec YOLOv8
- Génère une nouvelle vidéo annotée `video/video_detected.mp4`
- Affiche les résultats en temps réel avec boîtes englobantes, scores de confiance et IDs de suivi.

 La vidéo d’entrée n’est pas incluse dans le dépôt (trop lourde). Vous pouvez télécharger l’exemple depuis le lien ci-dessus et la placer dans le dossier `video/`.
