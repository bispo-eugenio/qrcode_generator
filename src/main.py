import sys
from display import Display
from my_package.components.main_window import MainWindow
from PySide6.QtWidgets import QApplication

#Definição do main()
def main() -> None:
    #Instância das classes
    app = QApplication(sys.argv)
    main_window = MainWindow()
    display = Display()
    main_window.add_widget(display)
    #Execução do programa
    main_window.show()
    app.exec()

if __name__ == "__main__":
    main()