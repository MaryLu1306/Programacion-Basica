import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox

class CalculatorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora con PyQt5")
        self.setGeometry(100, 100, 350, 200)
        
        self.initUI()

    def initUI(self):
    
        self.label1 = QLabel("Número 1:", self)
        self.text_input1 = QLineEdit(self)

        self.label2 = QLabel("Número 2:", self)
        self.text_input2 = QLineEdit(self)

        self.result_label = QLabel("Resultado:", self)

        self.suma_button = QPushButton("+", self)
        self.resta_button = QPushButton("-", self)
        self.multi_button = QPushButton("x", self)
        self.div_button = QPushButton("/", self)

        self.suma_button.clicked.connect(self.sumar)
        self.resta_button.clicked.connect(self.restar)
        self.multi_button.clicked.connect(self.multiplicar)
        self.div_button.clicked.connect(self.dividir)
                            
        layout = QVBoxLayout()
        layout.addWidget(self.label1)
        layout.addWidget(self.text_input1)
        layout.addWidget(self.label2)
        layout.addWidget(self.text_input2)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.suma_button)
        button_layout.addWidget(self.resta_button)
        button_layout.addWidget(self.multi_button)
        button_layout.addWidget(self.div_button)

        layout.addLayout(button_layout)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def get_inputs(self):
        try:
            num1 = float(self.text_input1.text())
            num2 = float(self.text_input2.text())
            return num1, num2
        except ValueError:
            QMessageBox.warning(self, "Error", "Por favor ingresa números válidos.")
            return None, None

    def sumar(self):
        num1, num2 = self.get_inputs()
        if num1 is not None:
            resultado = num1 + num2
            self.result_label.setText(f"Resultado: {resultado}")

    def restar(self):
        num1, num2 = self.get_inputs()
        if num1 is not None:
            resultado = num1 - num2
            self.result_label.setText(f"Resultado: {resultado}")

    def multiplicar(self):
        num1, num2 = self.get_inputs()
        if num1 is not None:
            resultado = num1 * num2
            self.result_label.setText(f"Resultado: {resultado}")

    def dividir(self):
        num1, num2 = self.get_inputs()
        if num1 is not None:
            if num2 != 0:
                resultado = num1 / num2
                self.result_label.setText(f"Resultado: {resultado}")
            else:
                QMessageBox.warning(self, "Error", "No se puede dividir entre cero.")
                
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.text_input)
        layout.addWidget(self.button)
        layout.addWidget(self.result_label)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = CalculatorApp()
    ventana.show()
    sys.exit(app.exec_())