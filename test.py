from PyQt5.QtWidgets import QTreeView,QFileSystemModel,QApplication

class Main(QTreeView):
    def __init__(self):
        QTreeView.__init__(self)
        model = QFileSystemModel()
        model.setRootPath('C:\\')
        self.setModel(model)
  #      self.selectionModel().currentChanged.connect(self.test2)
        self.selectionModel().selectionChanged.connect(self.test2)
 #        self.view.selectionModel().selectionChanged.connect(self.updateActions)
 #     print(selectionModel)
 #    self.doubleClicked.connect(self.test)

    def test(self, signal, signal2):
        file_path=self.model().filePath(signal)
        print(file_path)
    
    def test2(self, selected_indexes, deselected_indexes):
        selected_paths = tuple(self.model().filePath(index) for index in self.selectionModel().selectedRows())
        print('\n'.join(selected_paths))


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    w = Main()
    w.show()
sys.exit(app.exec_())
