import sys

from PyQt5.QtCore import QCoreApplication, QUrl
from PyQt5.QtQml import QQmlComponent, QQmlEngine

# Create the application instance.
app = QCoreApplication(sys.argv)

print("A")

# Create a QML engine.
engine = QQmlEngine(app)
print("B")

# Create a component factory and load the QML script.
component = QQmlComponent(engine)
print("C")
component.loadUrl(QUrl('example.qml'))

print("D")
# Create an instance of the component.
topLevel = component.create()

print("E")
if topLevel is not None:
    help(topLevel)
    topLevel.show()
else:
    # Print all errors that occurred.
    for error in component.errors():
        print(error.toString())

print("Z")

