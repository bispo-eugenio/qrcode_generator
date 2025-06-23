import re

# ========== Funções de Utilidades ==========

def validated_link(url:str) -> bool:
    pattern = re.compile(r"https?://[a-zA-Z0-9.-]+\.[a-z]{2,}")
    return pattern.match(url) is not None

def is_empty(string: str) -> bool:
    return len(string) == 0 