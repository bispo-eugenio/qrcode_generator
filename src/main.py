import sys
from PySide6.QtWidgets import QApplication
from my_package.components.main_layout import MainLayout
from my_package.components.main_window import MainWindow

#Definição do main()
def main() -> None:

    #Instância das classes
    app = QApplication(sys.argv)
    main_window = MainWindow()
    layout = MainLayout()

    #Configurações do MainWindow
    main_window.add_layout(layout)
    
    #Execução do programa
    main_window.show()
    app.exec()

if __name__ == "__main__":
    main()