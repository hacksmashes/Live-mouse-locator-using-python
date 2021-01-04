from pynput.mouse import Listener

def mouse_move(x,y):
    print("Mouse position is : ",format((x,y)))
    
with Listener(on_move=mouse_move) as listener:
    listener.join()












