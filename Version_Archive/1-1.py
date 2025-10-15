import time
from pmk import PMK
from pmk.platform.rgbkeypadbase import RGBKeypadBase as Hardware

import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

# Set up Keybow
keybow = PMK(Hardware())
keys = keybow.keys

# Set up the keyboard and layout
keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard)

# Set up consumer control (used to send media key presses)
consumer_control = ConsumerControl(usb_hid.devices)

# Our layers. The key of item in the layer dictionary is the key number on
# Keybow to map to, and the value is the key press to send.

# Note that key 0 is reserved as the modifier

# purple - numeric keypad
layer_1 =     {7: Keycode.SEVEN, 11: Keycode.EIGHT, 15: Keycode.NINE,
               6: Keycode.FOUR, 10: Keycode.FIVE, 14: Keycode.SIX,
               13: Keycode.THREE, 9: Keycode.TWO, 5: Keycode.ONE,
               4: Keycode.ZERO, 8: Keycode.DELETE, 12: Keycode.ENTER}

# violet- function keys
layer_2 =     {7: ConsumerControlCode.SCAN_PREVIOUS_TRACK, 11: ConsumerControlCode.PLAY_PAUSE, 15: ConsumerControlCode.SCAN_NEXT_TRACK,
               6: Keycode.F4, 10: Keycode.F5, 14: Keycode.F6,
               5: Keycode.F7, 9: Keycode.F8, 13: Keycode.F9,
               4: Keycode.F10, 8: Keycode.F11, 12: Keycode.F12,
               # Yellow left hand side keys
               1: Keycode.F13, 2: Keycode.F14, 3: Keycode.F15}

# green - media controls
layer_3 =     {6: ConsumerControlCode.VOLUME_DECREMENT, 10: ConsumerControlCode.MUTE, 14: ConsumerControlCode.VOLUME_INCREMENT,
               4: ConsumerControlCode.SCAN_PREVIOUS_TRACK, 8: ConsumerControlCode.PLAY_PAUSE, 12: ConsumerControlCode.SCAN_NEXT_TRACK}

# blue - Work
layer_4 =     {4: "Placeholder", 5: "wow",
               9: "Hope this helps!", 13: "Let me know if you need anything else!",
               6: "Thanks for your patience.", 10: "Thank you for your understanding.", 14: "Thanks for your help!",
               8: ["Hi CONTACT,", Keycode.ENTER, Keycode.ENTER,
               "Let's get this fixed straight away. Use this postage address for your return:", Keycode.ENTER, Keycode.ENTER,
               "Core Electronics", Keycode.ENTER,
               "PO Box 37", Keycode.ENTER,
               "Kotara NSW, 2289", Keycode.ENTER, Keycode.ENTER,
               "Also important:", Keycode.ENTER,
               "- Please use a tracked postage method.", Keycode.ENTER,
               "If the product contains a battery or liquid, then ensure it is sent road only (AusPost can provide stickers).", Keycode.ENTER,
               "Please use good packaging; preferably include all the original packaging. In some situations, lost or physically damaged goods are not covered.", Keycode.ENTER,
               "Include a print of this email inside the box (ref 000000).", Keycode.ENTER,
               "Send us the tracking number when you have it, as a reply to this email. We will update our log, ensuring your return is actioned correctly.", Keycode.ENTER,
               "Please backup any data you send us. The repair of your goods may result in the loss of any user-generated data. Please ensure that you have made a copy of any data saved on your goods.", Keycode.ENTER, Keycode.ENTER, Keycode.ENTER,
               "That's it! When we receive your product we will test it using official hardware/software (if appropriate). There are only four outcomes:", Keycode.ENTER,
               "- Minor damage: We will make an assessment of whether a repair or replacement would be appropriate. Afterwards, we will send a fully serviceable product back to you (postage paid by us). Some products might need to be special ordered, this process can take anywhere from 1 day for local stock, to 2+ weeks for special orders.", Keycode.ENTER,
               " Major damage or manufacturing defect: We will post you a free replacement (postage paid by us). Some products might need to be special ordered, this process can take anywhere from 1 day for local stock, to 2+ weeks for special orders. You can also opt for a refund.", Keycode.ENTER,
               " We confirm a user-invoked action led to the damage: (user action leading to mechanical damage, short circuit, reverse voltage, etc): We're unable to sustainably offer a refund or return in this scenario. We can dispose of the product for free, and if you want it back, in some scenarios you may need to pay for the return postage. Either way, our time spent on diagnosis and administration is free (no service fee).", Keycode.ENTER,
               " Can't replicate the fault: We'll detail what steps we took to get it working and ask you for more information if appropriate to replicate the fault. In some scenarios you will have to pay for the postage back to you, however, we will cover the costs of our time spent on diagnosis and administration (no service fee).", Keycode.ENTER, Keycode.ENTER, Keycode.ENTER,
               "Products confirmed damaged/defective are eligible for a refund of postage costs back to us, up to $15. If you discover that postage will cost more, then please reply to this email with an attachment of the quote and we'll help out. When/if return shipping costs are eligible for refund:", Keycode.ENTER,
               "- If a copy of the postage receipt is not sent as a reply to this email, then we'll send the replacement with express postages a free upgrade (which may help get you back on track faster as well).", Keycode.ENTER,
               "If a copy of the postage receipt is sent as a reply to this email: We'll process a refund and send the return with standard post.", Keycode.ENTER, Keycode.ENTER, Keycode.ENTER,
               "Please note that some modified products (soldered or user-modified) are not eligible for return as there are quality factors beyond our control.", Keycode.ENTER],
               12: "7550",
               3: ["shortcuts for web search...", Keycode.ENTER,
               "c : Core Electronics website search", Keycode.ENTER,
               "sku : Core Electronics SKU search", Keycode.ENTER,
               "aus : AusPost Tracking Number Search", Keycode.ENTER,
               "s : Sparkfun website search", Keycode.ENTER,
               "a : Adafruit website search", Keycode.ENTER,
               "d : DFRobot website search", Keycode.ENTER,
               "p : Pololu website search", Keycode.ENTER,
               "ss : Seeed Studio website search", Keycode.ENTER,
               "pim : Pimoroni website search", Keycode.ENTER,
               "w : Waveshare website search"],
               2: ["Alfa, Bravo, Charlie, Delta, Echo, Foxtrot,", Keycode.ENTER,
               "Golf, Hotel, India, Juliett, Kilo, Lima,", Keycode.ENTER,
               "Mike, November, Oscar, Papa, Quebec, Romeo,", Keycode.ENTER,
               "Sierra, Tango, Uniform, Victor, Whiskey, X-ray,", Keycode.ENTER,
               "Yankee, and Zulu."],
               7: ConsumerControlCode.SCAN_PREVIOUS_TRACK, 11: ConsumerControlCode.PLAY_PAUSE, 15: ConsumerControlCode.SCAN_NEXT_TRACK}

# white - Multiple key input shortcuts
layer_6 =     {15: (Keycode.LEFT_CONTROL, Keycode.A),
               4: (Keycode.LEFT_CONTROL, Keycode.X),
               8: (Keycode.LEFT_CONTROL, Keycode.C),
               12: (Keycode.LEFT_CONTROL, Keycode.V),
               10: (Keycode.WINDOWS, Keycode.SHIFT, Keycode.S),
               # Paste from copy history, only works if this setting is turn on inside windows 10
               13: (Keycode.WINDOWS, Keycode.V),
               9: (Keycode.WINDOWS, Keycode.SHIFT, Keycode.C),
               3: (Keycode.LEFT_CONTROL, Keycode.S)}

# yellow - debug output shortcuts for Java
layer_9 =     {6: 'System.out.println("Flag_01"); ', 10: 'System.out.println("Flag_02"); ', 14: 'System.out.println("Flag_03"); ',
               5: 'System.out.println("Flag_04"); ', 9: 'System.out.println("Flag_05"); ', 13: 'System.out.println("Flag_06"); ',
               4: 'System.out.println("Flag_07"); ', 8: 'System.out.println("Flag_08"); ', 12: 'System.out.println("Flag_09"); '}

# orange - debug output shortcuts for Arduino
layer_10 =     {6: 'Serial.println("Flag_01"); ', 10: 'Serial.println("Flag_02"); ', 14: 'Serial.println("Flag_03"); ',
               5: 'Serial.println("Flag_04"); ', 9: 'Serial.println("Flag_05"); ', 13: 'Serial.println("Flag_06"); ',
               4: 'Serial.println("Flag_07"); ', 8: 'Serial.println("Flag_08"); ', 12: 'Serial.println("Flag_09"); '}

# red - debug output shortcuts for python
layer_11 =     {6: 'print("Flag_01") ', 10: 'print("Flag_02") ',  14: 'print("Flag_03") ',
               5: 'print("Flag_04") ', 9: 'print("Flag_05") ', 13: 'print("Flag_06") ',
               4: 'print("Flag_07") ', 8: 'print("Flag_08") ', 12: 'print("Flag_09") '}

layers =      {3: layer_1, 2: layer_2,
               7: layer_3,
               11: layer_4, 10: layer_4,
               15: layer_6, 14: layer_6, 13: layer_6,
               4: layer_9, 8: layer_10, 12: layer_11}

selectors =   {3: keys[3], 2: keys[2],
               7: keys[7],
               11: keys[11], 10: keys[10],
               15: keys[15], 14: keys[14], 13: keys[13],
               4: keys[4], 8: keys[8], 12: keys[12]}

# The colours for each layer
colours = {3: (255, 0, 255), 2: (50, 0, 100),
           7: (0, 255, 0),
           11: (0, 80, 80), 10: (0, 0, 255),
           15: (50, 128, 50), 14: (128, 50, 50), 13: (50, 50, 128),
           4: (255, 255, 0), 8: (255, 100, 0), 12: (255, 0, 0)}

# Define the modifier key and layer selector keys
modifier = keys[0]
# Define the start layer
current_layer = 11

# Variables used to store state information of the program
layer_keys = range(0, 16)
mode = 0
count = 0
# Button debounce time and press boolean
debounce = 0.10
fired = False
# Colour values for cycling colour layer select key
colour_stage = 0
rgb = [100, 0, 0]
# Define RGB adjustments for each colour stage
colour_changes = [ (0, 1, 0), (-1, 0, 0),(0, 0, 1),(0, -1, 0),(1, 0, 0), (0, 0, -1) ]

# Set the LEDs for each key in the current layer
def setLayerColours():
    for k in layer_keys:
        keys[k].set_led(0, 0, 0)
    for k in layers[current_layer].keys():
        keys[k].set_led(*colours[current_layer])
    # Special LED assignments for particular layers
    if current_layer in {10, 11}:
        for key in [7, 11, 15]:
            keys[key].set_led(0, 255, 0)
        for key in [4, 5]:
            keys[key].set_led(0, 255, 80)
        for key in [9, 13]:
            keys[key].set_led(128, 50, 50)
        for key in [8, 12]:
            keys[key].set_led(50, 50, 128)
        for key in [1, 2, 3]:
            keys[key].set_led(255, 69, 10)
    elif current_layer ==  2:
        for key in [1, 2, 3]:
            keys[key].set_led(55, 55, 0)
        for key in [7, 11, 15]:
            keys[key].set_led(0, 255, 80)

# Update cycling colour special key
def cycle_modifier_key_colour(rgb, colour_changes, colour_stage, keys, current_layer):
    # Cycle the modifier key colour
    for colour in range(3):
        rgb[colour] += colour_changes[colour_stage][colour]

    keys[0].set_led(rgb[0], rgb[1], rgb[2])

    # Check if we need to transition to the next colour stage
    if (rgb[0] + rgb[1] + rgb[2]) in [100, 200]:
        # Update and return the new colour stage
        colour_stage = (colour_stage + 1) % len(colour_changes)

    return colour_stage

# Decide what USB command type to send
def pressButton(key_press):
     # Get all ConsumerControlCode values
    media_codes = [getattr(ConsumerControlCode, attr) for attr in dir(ConsumerControlCode)
                  if not attr.startswith('__')]

    # Check if key_press is a string
    if isinstance(key_press, str):
        layout.write(key_press)
    # Check if key_press is a tuple (e.g., multiple keycodes)
    elif isinstance(key_press, tuple):
        keyboard.press(*key_press)
        keyboard.release_all()
    # Check if key_press is a media control code
    elif key_press in media_codes:
        consumer_control.send(key_press)
    # Check if key_press is a single Keycode (often an integer)
    elif isinstance(key_press, Keycode) or isinstance(key_press, int):
        keyboard.send(key_press)
    # Handle unrecognized types
    else:
        print("Unrecognized key press type:", type(key_press))

while True:
    # Always remember to call keybow.update()
    keybow.update()

    # if no key is pressed ensure not locked in layer change mode
    if ((mode == 2) & keybow.none_pressed()):
        mode = 0

    if modifier.pressed:
        # set to looking to change the keypad layer
        for layer in layers.keys():
            # If the modifier key is held, light up the layer selector keys
            if mode == 1:
                # Set the LEDs for each key in selectors
                for k in layer_keys:
                    keys[k].set_led(0, 0, 0)
                for k in selectors.keys():
                    keys[k].set_led(*colours[k])
                # keys[0].set_led(255, 255, 0)
                mode = 2

            # Change current layer if layer key is pressed
            if selectors[layer].pressed:
                if mode >= 1:
                    mode = 0
                    current_layer = layer
                    # Set the LEDs for each key in the current layer
                    setLayerColours()
                fired = True
    else:
        # Update cycling colour keys
        colour_stage = cycle_modifier_key_colour(rgb, colour_changes, colour_stage, keys, current_layer)

        # set to look for a key presses
        if mode == 0:
            mode = 1
            # Set the LEDs for each key in the current layer
            setLayerColours()

    # Loop through all of the keys in the layer and if they're pressed, get the
    # key code from the layer's key map
    for k in layers[current_layer].keys():
        if keys[k].pressed:
            key_press = layers[current_layer][k]
            # If the key hasn't just fired (prevents refiring)
            if not fired:
                fired = True
                # handle output of multiple sequential key presses
                if isinstance(key_press, list):
                    for i in key_press:
                        pressButton(i)
                        time.sleep(0.1)
                else:
                    # Send key code
                    pressButton(key_press)

    # If enough time has passed, reset the fired variable
    if fired and time.monotonic() - keybow.time_of_last_press > debounce:
        fired = False
