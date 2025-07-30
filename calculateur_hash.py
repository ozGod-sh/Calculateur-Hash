# -*- coding: utf-8 -*-
# Auteur: ozGod

import argparse
import hashlib

def display_banner():
    """Affiche une bannière stylisée pour l'outil."""
    VERSION = "1.0.0"
    AUTHOR = "ozGod"
    banner = f"""
╔══════════════════════════════════════════════════════════╗
║                                                              ║
║  #️⃣  Calculateur-Hash v{VERSION}                             ║
║                                                              ║
║  Calcule les hachages (MD5, SHA1, SHA256) pour une chaîne.  ║
║  Créé par {AUTHOR}                                           ║
║                                                              ║
╚══════════════════════════════════════════════════════════╝
"""
    print(banner)

def calculate_hashes(input_string):
    """Calcule et affiche les différents hachages pour la chaîne d'entrée."""
    print(f"[*] Calcul des hachages pour : "{input_string}"\n")
    data = input_string.encode('utf-8')

    # MD5
    md5_hash = hashlib.md5(data).hexdigest()
    print(f"MD5:    {md5_hash}")

    # SHA1
    sha1_hash = hashlib.sha1(data).hexdigest()
    print(f"SHA1:   {sha1_hash}")

    # SHA256
    sha256_hash = hashlib.sha256(data).hexdigest()
    print(f"SHA256: {sha256_hash}")

    # SHA512
    sha512_hash = hashlib.sha512(data).hexdigest()
    print(f"SHA512: {sha512_hash}")

def main():
    display_banner()
    parser = argparse.ArgumentParser(
        description="Calcule les hachages MD5, SHA1, SHA256, et SHA512 pour une chaîne de caractères.",
        epilog=f"Créé par ozGod."
    )
    parser.add_argument("string", help="La chaîne de caractères à hacher.")
    args = parser.parse_args()

    calculate_hashes(args.string)

if __name__ == "__main__":
    main()
