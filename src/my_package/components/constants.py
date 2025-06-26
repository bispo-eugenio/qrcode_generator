from pathlib import Path


# ===========================
# CAMINHO ABSOLUTO DO PROJETO
# ===========================

MAIN_PATH = Path(__file__).parents[2]
ICON_PATH = MAIN_PATH / "my_package/assets/icon/qrcode-generator.png"
PNG_PATH = Path(__file__).parents[3] / ".png"


# ==================== # ====================

# ====================
# Estilo do MainWindow
# ====================

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

# =================
# Estilo do Display
# =================

STYLE_DISPLAY = """
    background-color: #FFFFFF;
    border: 1px solid #000000;
"""

# ==================
# Tamanho do QR Code
# ==================

SIZE_QRCODE = 300
"""
Normalmente é utilizidado
1 polegada que convertido em pixels dá 
115X115. No entanto, deixe o padrão como  300 px. 
(OBS: Essa constante está contida no slot() de QR Code e na classe Display,
 a alteração de valores pode alterar o layout do MainWindow)
"""

# ===================
# Estilo do InputText
# ===================

STYLE_INPUT_TEXT = """
    background-color: #3D3D3D;
    color: #FFFFFF;
    font-size: 15px;
    border: 1px solid #3D3D3D;
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


# ======================
# Estilo do Botão QRCode
# ======================

STYLE_QRCODE_BUTTON ="""
    QPushButton {
        background-color: #9FC131;
        color: #FFFFFF;
        font-weight: bold;
        border: 1px solid #000000;
    }
    QPushButton:hover {
        background-color: #8DAB2B;
        color: #EFEEEE;
    }
    QPushButton:pressed {
        background-color: #738C21;
        color: #DBDBDB;
    }
"""


# =========================
# Estilo do Botão de Limpar
# =========================

STYLE_CLEAR_BUTTON = """
    QPushButton{
        background-color: #BE1D1D;
        color: #FFFFFF;
        font-weight: bold;
        border: 1px solid #000000;
    }
    QPushButton:hover {
        background-color: #9D1717;
        color: #EFEEEE;
    }
    QPushButton:pressed {
        background-color: #8B1414;
        color: #DBDBDB;
    }
"""

# =========================
# Estilo do Botão de Salvar
# =========================

STYLE_SAVE_BUTTON = """
    QPushButton{
        background-color: #1AD75D;
        color: #FFFFFF;
        font-weight: bold;
        border: 1px solid #000000;
    }
    QPushButton:hover {
        background-color: #18B44F;
        color: #EFEEEE;
    }
    QPushButton:pressed {
        background-color: #149C44;
        color: #EFEEEE;
    }
"""