Code used during RP1 - MSc SNE UvA

To be able to add Adblock Plus using selenium one has to change the following in the selenium module:

firefox_profile.py:
Change
"with open(os.path.join(addon_path, 'install.rdf'), 'r') as f:"
TO
"with open(os.path.join(addon_path, 'install.rdf'), 'r', encoding='utf-8') as f:"

Futhermore, all paths are hard coded.
