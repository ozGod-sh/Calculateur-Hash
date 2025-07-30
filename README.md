# #️⃣ Calculateur-Hash - Générateur d'Empreintes Cryptographiques

**Créé par ozGod-sh**

## Description

Calculateur-Hash est un outil simple et efficace pour calculer les empreintes cryptographiques (hashes) d'une chaîne de caractères. Il supporte les algorithmes de hachage les plus couramment utilisés en cybersécurité et forensique numérique.

## Fonctionnalités

### 🔐 Algorithmes supportés
- **MD5** : Hash de 128 bits (déprécié mais encore utilisé)
- **SHA1** : Hash de 160 bits (déprécié pour la cryptographie)
- **SHA256** : Hash de 256 bits (recommandé)
- **SHA512** : Hash de 512 bits (très sécurisé)

### ⚡ Caractéristiques
- **Interface simple** : Une seule commande pour tous les hashes
- **Encodage UTF-8** : Support des caractères internationaux
- **Affichage formaté** : Résultats alignés et lisibles
- **Pas de dépendances** : Utilise uniquement la bibliothèque standard Python

## Installation

### Prérequis
- Python 3.6+
- Aucune dépendance externe (utilise la bibliothèque standard)

### Installation
```bash
cd Calculateur-Hash
# Aucune installation requise - utilise uniquement la stdlib Python
```

## Utilisation

### Syntaxe de base
```bash
python calculateur_hash.py <CHAÎNE>
```

### Exemples d'utilisation

#### 1. Hash d'un mot de passe
```bash
python calculateur_hash.py "monmotdepasse123"
```

#### 2. Hash d'une phrase
```bash
python calculateur_hash.py "Hello World!"
```

#### 3. Hash avec caractères spéciaux
```bash
python calculateur_hash.py "Café & Thé ñ 中文"
```

## Structure des fichiers

```
Calculateur-Hash/
├── calculateur_hash.py    # Script principal
└── README.md             # Cette documentation
```

## Logique de fonctionnement

### 1. Encodage de la chaîne
```python
data = input_string.encode('utf-8')
```

### 2. Calcul des hashes
```python
md5_hash = hashlib.md5(data).hexdigest()
sha1_hash = hashlib.sha1(data).hexdigest()
sha256_hash = hashlib.sha256(data).hexdigest()
sha512_hash = hashlib.sha512(data).hexdigest()
```

### 3. Affichage formaté
```python
print(f"MD5:    {md5_hash}")
print(f"SHA1:   {sha1_hash}")
print(f"SHA256: {sha256_hash}")
print(f"SHA512: {sha512_hash}")
```

## Cas d'usage

### Vérification d'intégrité
- **Contrôle de fichiers** : Vérifier qu'un fichier n'a pas été modifié
- **Validation de téléchargements** : Comparer avec les hashes fournis
- **Détection de corruption** : Identifier les données corrompues

### Sécurité des mots de passe
- **Stockage sécurisé** : Générer des hashes pour le stockage
- **Comparaison de mots de passe** : Vérifier sans stocker en clair
- **Audit de sécurité** : Tester la force des mots de passe

### Forensique numérique
- **Identification de fichiers** : Créer des signatures uniques
- **Comparaison de données** : Vérifier l'identité de contenus
- **Chaîne de custody** : Prouver l'intégrité des preuves

## Exemple de sortie

### Pour la chaîne "Hello World!"
```
╔══════════════════════════════════════════════════════════╗
║                                                              ║
║  #️⃣  Calculateur-Hash v1.0.0                             ║
║                                                              ║
║  Calcule les hachages (MD5, SHA1, SHA256) pour une chaîne.  ║
║  Créé par ozGod                                           ║
║                                                              ║
╚══════════════════════════════════════════════════════════╝

[*] Calcul des hachages pour : "Hello World!"

MD5:    ed076287532e86365e841e92bfc50d8c
SHA1:   2ef7bde608ce5404e97d5f042f95f89f1c232871
SHA256: 7f83b1657ff1fc53b92dc18148a1d65dfc2d4b1fa3d677284addd200126d9069
SHA512: 374d794a95cdcfd8b35993185fef9ba368f160d8daf432d08ba9f1ed1e5abe6cc69291e0fa2fe0006a52570ef18c19def4e617c33ce52ef0a6e5fbe318cb0387
```

## Comparaison des algorithmes

### MD5 (Message Digest 5)
- **Taille** : 128 bits (32 caractères hex)
- **Vitesse** : Très rapide
- **Sécurité** : ❌ Vulnérable aux collisions
- **Usage** : Vérification d'intégrité uniquement

### SHA1 (Secure Hash Algorithm 1)
- **Taille** : 160 bits (40 caractères hex)
- **Vitesse** : Rapide
- **Sécurité** : ⚠️ Déprécié depuis 2017
- **Usage** : Legacy, Git (en transition)

### SHA256 (SHA-2 256 bits)
- **Taille** : 256 bits (64 caractères hex)
- **Vitesse** : Modérée
- **Sécurité** : ✅ Sécurisé actuellement
- **Usage** : Recommandé pour la plupart des cas

### SHA512 (SHA-2 512 bits)
- **Taille** : 512 bits (128 caractères hex)
- **Vitesse** : Plus lente
- **Sécurité** : ✅ Très sécurisé
- **Usage** : Applications haute sécurité

## Intégration avec d'autres outils

### Vérification de fichiers
```bash
# Calculer le hash d'un fichier
python -c "import hashlib; print(hashlib.sha256(open('file.txt','rb').read()).hexdigest())"
# Comparer avec notre outil pour les chaînes
python calculateur_hash.py "contenu du fichier"
```

### Scripts d'automatisation
```python
import subprocess

def get_hashes(text):
    result = subprocess.run(['python', 'calculateur_hash.py', text], 
                          capture_output=True, text=True)
    return result.stdout
```

### Validation de mots de passe
```bash
# Générer le hash d'un mot de passe
python calculateur_hash.py "motdepasse" | grep SHA256
```

## Bonnes pratiques de sécurité

### Pour le stockage de mots de passe
❌ **Ne pas faire** :
```python
# Stockage direct du hash (vulnérable aux rainbow tables)
password_hash = hashlib.sha256("password".encode()).hexdigest()
```

✅ **Recommandé** :
```python
# Utiliser un salt et des fonctions dédiées comme bcrypt, scrypt, ou Argon2
import bcrypt
password_hash = bcrypt.hashpw("password".encode(), bcrypt.gensalt())
```

### Pour la vérification d'intégrité
✅ **Recommandé** :
- Utiliser SHA256 ou SHA512 pour les nouvelles applications
- Combiner avec des signatures numériques pour l'authentification
- Stocker les hashes de manière sécurisée

## Limitations

### Sécurité
- **Pas de salt** : Vulnérable aux rainbow tables pour les mots de passe
- **Pas de stretching** : Rapide à calculer (mauvais pour les mots de passe)
- **MD5/SHA1** : Algorithmes dépréciés inclus pour compatibilité

### Fonctionnalités
- **Chaînes uniquement** : Ne traite pas directement les fichiers
- **Pas de vérification** : Ne compare pas avec des hashes existants
- **Format fixe** : Sortie uniquement en hexadécimal

## Améliorations futures

### Nouvelles fonctionnalités
- Support des fichiers en entrée
- Comparaison avec des hashes de référence
- Export en différents formats (base64, binaire)
- Support d'algorithmes additionnels (BLAKE2, SHA3)

### Interface
- Mode interactif pour plusieurs chaînes
- Interface graphique
- API REST pour intégration
- Plugin pour éditeurs de texte

## Alternatives et outils similaires

### Outils système
```bash
# Linux/macOS
echo -n "Hello World!" | md5sum
echo -n "Hello World!" | sha256sum

# Windows
certutil -hashfile file.txt SHA256
```

### Outils en ligne
- **Attention** : Ne jamais utiliser d'outils en ligne pour des données sensibles
- Préférer les outils locaux pour la confidentialité

## Sécurité et éthique

⚠️ **Bonnes pratiques**
- Ne jamais hasher des mots de passe sans salt
- Utiliser des algorithmes appropriés selon le contexte
- Protéger les hashes comme des données sensibles
- Respecter la confidentialité des données traitées

## Licence

MIT License - Voir le fichier LICENSE pour plus de détails.

---

**Calculateur-Hash v1.0.0** | Créé par ozGod-sh