import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QPushButton, QLabel, QSpinBox
from PyPDF2 import PdfReader, PdfWriter

class PDFPageSelector(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Seleziona Pagina PDF")
        self.setGeometry(100, 100, 400, 200)

        self.input_file = None
        self.output_file = None

        self.label = QLabel("Seleziona il numero di pagina di output:")
        self.label.setGeometry(20, 20, 300, 30)

        self.page_spinbox = QSpinBox(self)
        self.page_spinbox.setGeometry(20, 60, 100, 30)

        self.load_input_button = QPushButton("Seleziona file di input", self)
        self.load_input_button.setGeometry(20, 100, 150, 30)
        self.load_input_button.clicked.connect(self.load_input_file)

        self.load_output_button = QPushButton("Seleziona file di output", self)
        self.load_output_button.setGeometry(200, 100, 150, 30)
        self.load_output_button.clicked.connect(self.load_output_file)

        self.extract_button = QPushButton("Estrai pagina", self)
        self.extract_button.setGeometry(20, 140, 150, 30)
        self.extract_button.clicked.connect(self.extract_page)

    def load_input_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        self.input_file, _ = QFileDialog.getOpenFileName(self, "Seleziona file di input", "", "PDF Files (*.pdf);;All Files (*)", options=options)

    def load_output_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        self.output_file, _ = QFileDialog.getSaveFileName(self, "Seleziona file di output", "", "PDF Files (*.pdf);;All Files (*)", options=options)

    def extract_page(self):
        if self.input_file and self.output_file:
            try:
                page_number = self.page_spinbox.value()
                pdf_reader = PdfReader(self.input_file)
                pdf_writer = PdfWriter()
                pdf_writer.add_page(pdf_reader.pages[(page_number - 1)])

                with open(self.output_file, "wb") as output_stream:
                    pdf_writer.write(output_stream)
                print(f"Pagina {page_number} estratta con successo e salvata in {self.output_file}")
            except Exception as e:
                print(f"Errore durante l'estrazione della pagina: {e}")
        else:
            print("Seleziona sia il file di input che il file di output.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PDFPageSelector()
    window.show()
    sys.exit(app.exec_())
