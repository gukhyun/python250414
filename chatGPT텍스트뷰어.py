import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QAction, QFileDialog

class TextViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("텍스트 뷰어")
        self.setGeometry(100, 100, 800, 600)

        # 텍스트 에디터 위젯
        self.text_edit = QTextEdit(self)
        self.setCentralWidget(self.text_edit)

        # 메뉴바
        menubar = self.menuBar()
        file_menu = menubar.addMenu("파일")

        # 파일 열기 액션
        open_action = QAction("열기", self)
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)

    def open_file(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "파일 열기", "", "텍스트 파일 (*.txt);;모든 파일 (*)", options=options)
        if file_path:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                self.text_edit.setText(content)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    viewer = TextViewer()
    viewer.show()
    sys.exit(app.exec_())