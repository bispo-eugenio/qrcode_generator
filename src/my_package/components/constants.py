from pathlib import Path


# ===========================
# CAMINHO ABSOLUTO DO PROJETO
# ===========================

MAIN_PATH = Path(__file__).parents[2] 

# ==================== # ====================

# ===================
# Style do MainWindow
# ===================

STYLE_MAIN_WINDOW = """
    background-color: #034159;
    border: 3.5px solid #025951;
"""

# =====================
# Tamanho da MainWindow
# =====================

WIDTH = 450
"""Width do Main Window (recomendo não alterar)"""
HEIGTH = 500
"""Height do Main Window (recomendo não alterar)"""

# ================
# Style do Display
# ================

STYLE_DISPLAY = """
    background-color: #FFFFFF;
    border: 3.5px solid #025951;
"""

# ==================
# Tamanho do QR Code
# ==================

SIZE_QRCODE = 300
"""
Normalmente é utilizidado
1 polegada que convertido em pixels dá 
115 px. No entanto, deixe o padrão como  300 px.
"""

# ==================
# Style do InputText
# ==================

STYLE_INPUT_TEXT = """
    background-color: #3D3D3D;
    color: #FFFFFF;
    font-size: 15px;
"""

# ====================
# Tamanho do InputText
# ====================

INPUT_SIZE_W = 300 
"""Width do input_text (redomendo não alterar)""" 
INPUT_SIZE_H = 40
"""Height do input_text (redomendo não alterar)""" 

# ==================
# MARGIN do InputText
# ==================

MARGIN = 5
"""Margin do InputText"""



# ==================
# Tamanho dos Botões
# ==================

WIDTH_BUTTON = 75
HEIGHT_BUTTON = 25


# =====================
# Style do Botão QRCode
# =====================

STYLE_QRCODE_BUTTON = """
    background-color: #9FC131;
    color: #FFFFFF;
    font-weight: bold;
    border: 1px solid #038C3E;
"""


# ========================
# Style do Botão de Limpar
# ========================

STYLE_CLEAR_BUTTON = """
    background-color: #D92525;
    color: #FFFFFF;
    font-weight: bold;
    border: 1px solid #038C3E;
"""

STYLE_SAVE_BUTTON = """
    background-color: #0CF25D;
    color: #FFFFFF;
    font-weight: bold;
    border: 1px solid #038C3E;
"""