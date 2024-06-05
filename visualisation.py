import sys
import os
import pyqtgraph as pg
from data import vertices
from simulated_annealing import simulated_annealing
from PySide6 import QtCore, QtWidgets


basedir = os.path.dirname(__file__)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, SA_result):
        super().__init__()
        self.SA_result = SA_result
        self.loop = 0

        #Create a widget
        self.plot_graph = pg.PlotWidget()
        self.setCentralWidget(self.plot_graph)
        pen = pg.mkPen(width = 3)

        #Draw a graph
        self.line = self.plot_graph.plot(self.SA_result[1][0], self.SA_result[2][0], pen = pen, symbol = 'o')
        self.plot_graph.setTitle("Simulated Annealing", size = "20pt")
        self.plot_graph.showGrid(x=True, y=True)
        
        #Add label to points
        self.draw_label_of_first_state(self.plot_graph, self.SA_result[0][0])


        
       

        #Update plot
        self.timer = QtCore.QTimer(self)
        self.timer.setInterval(300)
        if self.timer.timeout:
            self.timer.timeout.connect(self.update_plot)
        self.timer.start()
    
   
    def update_plot(self):
        ##Simulated Annealing goes in here
        solution = self.SA_result[0]
        coordinate_X = self.SA_result[1]
        coordinate_Y = self.SA_result[2]
        best_solution = self.SA_result[3]
        if self.loop == len(solution) - 1:
            best_X = [x.horizon for x in best_solution]
            best_Y = [y.vertical for y in best_solution]
            temp = [point.element for point in best_solution]
            print(temp)
            self.line.setData(best_X, best_Y)
        else:
            self.line.setData(coordinate_X[self.loop], coordinate_Y[self.loop])
        self.loop += 1

        # for i in range(len(solution)):
        #     self.line.setData(coordinate_X[i], coordinate_Y[i])
            # list_point = solution[i]
            # for j in range(len(self.text_items)):
            #     self.text_items[j].setText(list_point[j].element)
            #     self.text_items[j].setPos(list_point[j].horizon*0.99, list_point[j].vertical*0.99)
        
        # for item, point in self.text_items, best_solution:
        #     self.line.setData(X, Y)
        #     item.setText(point.element)
        #     item.setPos(point.horizon*0.99, point.vertical*0.99)


    def draw_label_of_first_state(self, plotwidget, vertices):
        for vertex in vertices:
            temp = pg.TextItem(vertex.element)
            temp.setPos(vertex.horizon*0.99, vertex.vertical*0.99)
            # self.text_items.append(temp)
            plotwidget.addItem(temp)
      

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    result = simulated_annealing(vertices)
    # print(len(result[0]), len(result[1]), len(result[2]), len(result[3]))
    main = MainWindow(result)
    main.show()
    app.exec()