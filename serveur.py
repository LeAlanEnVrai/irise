#!/usr/bin/env python3
"""
Serveur web local pour visualiser le site 3D
Double-cliquez sur ce fichier ou exécutez: python serveur.py
Puis ouvrez votre navigateur à l'adresse: http://localhost:8000
"""

import http.server
import socketserver
import webbrowser
import os
import mimetypes

PORT = 8000

# Ajouter le type MIME pour les fichiers GLB
mimetypes.add_type('model/gltf-binary', '.glb')
mimetypes.add_type('model/gltf+json', '.gltf')

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Ajouter les headers CORS pour éviter les problèmes
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET')
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        super().end_headers()
    
    def guess_type(self, path):
        """Override pour s'assurer que les fichiers GLB ont le bon MIME type"""
        if path.endswith('.glb'):
            return 'model/gltf-binary'
        elif path.endswith('.gltf'):
            return 'model/gltf+json'
        return super().guess_type(path)

print("=" * 60)
print("🌊 SERVEUR WEB LOCAL POUR L'EXPÉRIENCE SOUS-MARINE 🐟")
print("=" * 60)
print(f"\n✅ Serveur démarré sur le port {PORT}")
print(f"\n🌐 Ouvrez votre navigateur à l'adresse:")
print(f"   👉 http://localhost:{PORT}/underwater_journey.html")
print("\n📁 Fichiers dans le dossier:")

# Lister les fichiers présents
for file in os.listdir('.'):
    if file.endswith(('.html', '.glb', '.gltf')):
        size = os.path.getsize(file)
        size_mb = size / (1024 * 1024)
        print(f"   - {file} ({size_mb:.2f} MB)")

print("\n📌 Pour arrêter le serveur: Appuyez sur Ctrl+C")
print("=" * 60 + "\n")

# Ouvrir automatiquement le navigateur
webbrowser.open(f'http://localhost:{PORT}/underwater_journey.html')

# Démarrer le serveur
with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n\n🛑 Serveur arrêté.")
