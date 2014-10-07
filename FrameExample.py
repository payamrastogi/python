# SimpleGUI program template

# Import the module
import simplegui

# Define global variables (program state)
counter = 0

# Define "helper" functions
def increment():
    global counter
    counter = counter + 1

# Define event handler functions
def tick():
    increment()
    print counter
    
def button_press():
    global counter
    counter = 0
# Create a frame
frame = simplegui.create_frame("SimpleGUITest", 100, 100)
# Register event handlers
timer = simplegui.create_timer(1000, tick)
frame.add_button("Click me!", button_press)
# Start frame and timers
frame.start()
timer.start()