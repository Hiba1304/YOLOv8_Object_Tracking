 Description du projet

Ce projet met en œuvre **YOLOv8** pour la détection et le suivi d’objets dans une vidéo.  
Il permet de détecter automatiquement des **personnes**, des **sacs à dos** et des **sacs à main** dans une scène urbaine, puis de leur attribuer un **ID unique** grâce à l’algorithme **BoT-SORT**.


Le script `main.py` applique la détection et le suivi d’objets dans une vidéo en utilisant **YOLOv8** et l’algorithme de tracking **BoT-SORT**.

Fonctionnement :
1. Chargement du modèle YOLOv8 pré-entraîné (`yolov8n.pt`).
2. Lecture d’une vidéo d’entrée (`video/video_input.mp4`).
3. Détection des classes suivantes :
   - **person** 👤
   - **backpack** 🎒
   - **handbag** 👜
4. Attribution d’un **ID unique** à chaque objet détecté pour assurer son suivi image par image.
5. Annotation des objets avec :
   - Une **boîte englobante** colorée selon la classe
   - Le **nom de la classe**
   - L’**identifiant du suivi (ID)**
   - Le **score de confiance**
6. Sauvegarde d’une nouvelle vidéo annotée (`video/video_detected.mp4`).
7. Affichage en temps réel de la détection (appuyez sur `q` pour fermer la fenêtre).

 Résultat :
Chaque personne, sac à dos ou sac à main présent dans la vidéo est détecté, suivi et annoté avec un ID persistant au fil des images.


 Exemple d’utilisation : suivi de piétons dans une rue animée.  
La vidéo utilisée comme input provient de [Pexels](https://www.pexels.com/video/busy-snowy-city-street-with-walking-people-30820647/).

Le script :
- Charge la vidéo d’entrée `video/video_input.mp4`
- Applique la détection et le tracking avec YOLOv8
- Génère une nouvelle vidéo annotée `video/video_detected.mp4`
- Affiche les résultats en temps réel avec boîtes englobantes, scores de confiance et IDs de suivi.

 La vidéo d’entrée n’est pas incluse dans le dépôt (trop lourde). Vous pouvez télécharger l’exemple depuis le lien ci-dessus et la placer dans le dossier `video/`.
