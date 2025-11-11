from pathlib import Path
import glob

def note_paths(vault_root,file_name):
    """
    Returns a list of paths from vault_root containing file_name.

        vault_root : string
            Path to the Obsidian vault's root directory.

        file_name : string
            Name or partial name of an Obsidian Markdown file, with or without
            the *.md suffix.

        returns : list of pathlib.Path objects.
    """
    md_files = glob.glob(str(vault_root) + "**/*.md",recursive=True)

    return [Path(file_path) for file_path in md_files if file_name in file_path]





