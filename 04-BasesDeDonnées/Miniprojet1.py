import sqlite3



# Création de la base de données et de la table
def create_database():
    connexion = sqlite3.connect('mynewbase.db')
    c = connexion.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS bulletin(
        Nom TEXT PRIMARY KEY,
        Prenom TEXT NOT NULL,
        Note INT);
    """)
    connexion.commit()
    connexion.close()

# Ajout des données avec une boucle
def insert_data_loop():
    connexion = sqlite3.connect('mynewbase.db')
    c = connexion.cursor()

    while True:
        nom = input("Entrez le nom de l'élève (ou 'Q' pour quitter) : ").strip()
        if nom == "q" or "Q":
            break
        prenom = input("Entrez le prénom de l'élève : ").strip()
        try:
            note = int(input("Entrez la note de l'élève : ").strip())
        except ValueError:
            print("La note doit être un nombre entier.")
            continue

        try:
            c.execute("INSERT INTO bulletin VALUES (?, ?, ?)", (nom, prenom, note))
            connexion.commit()
            print("Données enregistrées avec succès.")
        except sqlite3.IntegrityError:
            print("Un élève avec ce nom existe déjà.")

    connexion.close()

# Lecture des enregistrements
def view_data():
    connexion = sqlite3.connect('mynewbase.db')
    c = connexion.cursor()

    nom = input("Entrez le nom de l'élève à consulter (ou 'Tous' pour afficher tous les élèves) : ").strip()
    if nom.lower() == 'tous':
        c.execute("SELECT * FROM bulletin")
        rows = c.fetchall()
    else:
        c.execute("SELECT * FROM bulletin WHERE Nom = ?", (nom,))
        rows = c.fetchall()

    if rows:
        for row in rows:
            print(f"Nom: {row[0]}, Prénom: {row[1]}, Note: {row[2]}")
    else:
        print("Aucun enregistrement trouvé.")

    connexion.close()

    # Suppression d'un élève
def delete_student():
    connexion = sqlite3.connect('mynewbase.db')
    c = connexion.cursor()

    nom = input("Entrez le nom de l'élève à supprimer : ").strip()
    c.execute("DELETE FROM bulletin WHERE Nom = ?", (nom,))
    connexion.commit()

    if c.rowcount > 0:
        print("Élève supprimé avec succès.")
    else:
        print("Aucun élève trouvé avec ce nom.")

    connexion.close()

# Modification d'une note
def update_grade():
    connexion = sqlite3.connect('mynewbase.db')
    c = connexion.cursor()

    nom = input("Entrez le nom de l'élève à modifier : ").strip()
    try:
        new_grade = int(input("Entrez la nouvelle note : ").strip())
        c.execute("UPDATE bulletin SET Note = ? WHERE Nom = ?", (new_grade, nom))
        connexion.commit()

        if c.rowcount > 0:
            print("Note mise à jour avec succès.")
        else:
            print("Aucun élève trouvé avec ce nom.")
    except ValueError:
        print("La note doit être un nombre entier.")
    connexion.close()

# Classement des élèves par note
def display_rankings():
    connexion = sqlite3.connect('mynewbase.db')
    c = connexion.cursor()

    c.execute("SELECT * FROM bulletin ORDER BY Note DESC")
    rows = c.fetchall()

    print("Classement des élèves :")
    for rank, row in enumerate(rows, start=1):
        print(f"{rank}. Nom: {row[0]}, Prénom: {row[1]}, Note: {row[2]}")

    connexion.close()

# Calcul de la moyenne générale
def calculate_average():
    connexion = sqlite3.connect('mynewbase.db')
    c = connexion.cursor()

    c.execute("SELECT AVG(Note) FROM bulletin")
    average = c.fetchone()[0]

    if average is not None:
        print(f"La moyenne générale est : {average:.2f}")
    else:
        print("Aucune donnée pour calculer la moyenne.")

    connexion.close()

if __name__ == "__main__":
    create_database()
    while True:
        print("\nMenu Principal :")
        print("1. Ajouter des notes")
        print("2. Consulter des notes")
        print("3. Supprimer un élève")
        print("4. Modifier une note")
        print("5. Classement par note")
        print("6. Moyenne générale")
        print("7. Quitter")

        choice = input("Choisissez une option : ").strip()
        if choice == "1":
            insert_data_loop()
        elif choice == "2":
            view_data()
        elif choice == "3":
            delete_student()
        elif choice == "4":
            update_grade()
        elif choice == "5":
            display_rankings()
        elif choice == "6":
            calculate_average()
        elif choice == "7":
            print("Au revoir !")
            break
        else:
            print("Option invalide. Veuillez réessayer.")
