from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(width, height):
        self.__root = Tk()
        self.__root.title("Mazer")
        self.__canvas = Canvas(self.__root)
        self.__canvas.pack()
        self.__running = False

def main():
    pass
