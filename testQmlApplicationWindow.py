import sys
import logging

from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtQml


class TestApp(QtGui.QGuiApplication):
    def __init__(self, argv):
        super(TestApp, self).__init__(argv)

#    def notify(self, receiver, event):
#        try:
#            return QtGui.QGuiApplication.notify(self, receiver, event)
#        except Exception as e:
#            logging.exception("QApp notify exception: " + str(e))
#            import traceback
#            traceback.print_exc()
#            return False

def main(argv):
    
    # Create the application instance.
    app = TestApp(sys.argv)
    
    print("A")
    
    # Create a QML engine.
    engine = QtQml.QQmlEngine(app)
    print("B")
    
    # Create a component factory and load the QML script.
    component = QtQml.QQmlComponent(engine)
    print("C")
    component.loadUrl(QtCore.QUrl("example.qml"))
    
    print("D")
    # Create an instance of the component.
    topLevel = component.create()
    
    print("E")
    if topLevel is not None:
        topLevel.show()
    else:
        # Print all errors that occurred.
        for error in component.errors():
            print(error.toString())
    
    print("F")

    app.exec_()
    
    print("Z")


if __name__ == '__main__':

    main(sys.argv)
    print("End")

