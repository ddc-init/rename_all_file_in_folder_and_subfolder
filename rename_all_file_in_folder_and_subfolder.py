import os

def rename_all_file_in_folder_and_subfolder(root_path):
    # Attraversa tutte le cartelle e i file nel percorso specificato
    for root, dirs, files in os.walk(root_path):
        for file in files:
            # Verifica se l'estensione del file è .yml
            if file.endswith(".yml"):
                # Rinomina il file con estensione .yaml
                old_path = os.path.join(root, file)
                new_path = os.path.join(root, file.replace(".yml", ".yaml"))
                
                try:
                    os.rename(old_path, new_path)
                    print(f'Rinominato: {old_path} -> {new_path}')
                except Exception as e:
                    print(f'Errore durante la rinomina di {old_path}: {e}')

# Specifica il percorso della cartella principale
folder_path = "C:/Users/Davide/Documents/projects/gitlab.alm.poste.it/bpm-dossier-archive-service"

# Chiama la funzione per rinominare i file
rename_all_file_in_folder_and_subfolder(folder_path)
