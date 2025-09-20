def parse_nl_command(query: str):
    q = query.lower()

    if "list files" in q or "show files" in q:
        return "ls"
    if "current directory" in q or "where am i" in q:
        return "pwd"
    if "make folder" in q or "create folder" in q:
        parts = q.split()
        if "folder" in parts:
            idx = parts.index("folder")
            if idx + 1 < len(parts):
                return f"mkdir {parts[idx+1]}"
    if "delete" in q and "folder" in q:
        parts = q.split()
        if "folder" in parts:
            idx = parts.index("folder")
            if idx + 1 < len(parts):
                return f"rm {parts[idx+1]}"
    if "cpu" in q:
        return "cpu"
    if "memory" in q or "ram" in q:
        return "mem"

    return None
