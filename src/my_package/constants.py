from pathlib import Path


# ===========================
# CAMINHO ABSOLUTO DO PROJETO
# ===========================

MAIN_PATH = Path(__file__).parents[2] 

# ==================== # ====================

# ====================
# Style do MainWindow
# ====================

STYLE_MAIN_WINDOW = """
    background-color: #034159;
    border: 3.5px solid #025951;
"""

# =====================
# Tamanho da MainWindow
# =====================

WIDTH = 600
HEIGTH = 800

# ====================
# Style do Display
# ====================

STYLE_DISPLAY = """
    background-color: #FFFFFF;
    border: 3.5px solid #025951;
"""

# ==================
# Tamanho do QR Code
# ==================

SIZE_QRCODE = 290 #1 polegada convertido em pixels 115