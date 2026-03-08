# 🌊 Expérience Sous-Marine 3D 🐟

## 📋 Instructions d'utilisation

### Étape 1 : Télécharger tous les fichiers
Télécharge ces 3 fichiers dans le **même dossier** :
- `underwater_journey.html` (le site web)
- `fish.glb` (le modèle 3D de la truite)
- `serveur.py` (le serveur web local)
- `LANCER_SERVEUR.bat` (pour Windows - optionnel)

### Étape 2 : Lancer le serveur local

#### Option A - Windows (la plus simple) :
1. Double-cliquez sur `LANCER_SERVEUR.bat`
2. Le navigateur s'ouvrira automatiquement

#### Option B - Ligne de commande (Windows/Mac/Linux) :
1. Ouvre un terminal dans le dossier
2. Tape : `python serveur.py` ou `python3 serveur.py`
3. Le navigateur s'ouvrira automatiquement

#### Option C - Avec VS Code :
1. Ouvre le dossier dans VS Code
2. Ouvre un terminal (Ctrl + ù)
3. Tape : `python serveur.py`
4. Ouvre ton navigateur à : http://localhost:8000/underwater_journey.html

### Étape 3 : Profiter de l'expérience !
- Clique et glisse avec la souris pour regarder autour
- La caméra suit automatiquement la truite
- Des textes narratifs apparaissent au fil du voyage

---

## ❓ Problèmes courants

### "Python n'est pas reconnu"
- Installe Python depuis https://www.python.org/downloads/
- ✅ Coche "Add Python to PATH" pendant l'installation

### Le modèle 3D ne charge pas
- Vérifie que `fish.glb` est bien dans le même dossier
- Utilise TOUJOURS le serveur local (ne pas ouvrir directement le HTML)

### Le serveur ne démarre pas
- Vérifie que le port 8000 n'est pas déjà utilisé
- Essaye de fermer d'autres applications

---

## 🎮 Contrôles

- **Souris** : Cliquer et glisser pour pivoter la caméra
- **Vue** : La caméra suit automatiquement le poisson depuis l'arrière gauche

---

## 🛠️ Technologies utilisées

- Three.js (bibliothèque 3D)
- WebGL
- Format glTF 2.0

Bonne exploration sous-marine ! 🌊✨
