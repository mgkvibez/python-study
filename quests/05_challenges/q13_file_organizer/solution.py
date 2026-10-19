def organize_files(paths):
    """Group file paths by extension."""
    groups = {}
    for path in paths:
        if "." not in path:
            key = "no_extension"
        else:
            key = path.rsplit(".", 1)[1].lower()
        groups.setdefault(key, []).append(path)
    return groups
