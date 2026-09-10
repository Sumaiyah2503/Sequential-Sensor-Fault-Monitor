import ipywidgets as widgets
from IPython.display import display, clear_output

# Initial state
current_state = "NORMAL"

# Sensor input boxes
temperature = widgets.FloatText(
    value=30,
    description="Temperature:"
)

pressure = widgets.FloatText(
    value=100,
    description="Pressure:"
)

vibration = widgets.FloatText(
    value=2,
    description="Vibration:"
)

# Buttons
check_button = widgets.Button(
    description="CHECK SENSOR",
    button_style="success"
)

reset_button = widgets.Button(
    description="RESET"
)

output = widgets.Output()


def check_sensor(b):
    global current_state

    temp = temperature.value
    press = pressure.value
    vib = vibration.value

    # Threshold checking
    abnormal = (
        temp > 50 or
        press < 90 or
        press > 110 or
        vib > 5
    )

    condition = "ABNORMAL" if abnormal else "NORMAL"

    # Sequential FSM
    if current_state == "NORMAL":
        if condition == "ABNORMAL":
            current_state = "WARNING"

    elif current_state == "WARNING":
        if condition == "ABNORMAL":
            current_state = "FAULT"
        else:
            current_state = "NORMAL"

    elif current_state == "FAULT":
        if condition == "NORMAL":
            current_state = "RECOVERY"

    elif current_state == "RECOVERY":
        if condition == "NORMAL":
            current_state = "NORMAL"
        else:
            current_state = "FAULT"

    with output:
        clear_output()

        print("===== SENSOR MONITOR RESULT =====")
        print("Temperature :", temp, "°C")
        print("Pressure    :", press, "kPa")
        print("Vibration   :", vib, "mm/s")
        print("---------------------------------")
        print("Sensor Condition :", condition)
        print("Current State    :", current_state)


def reset_system(b):
    global current_state

    current_state = "NORMAL"

    with output:
        clear_output()
        print("System reset successfully.")
        print("Current State : NORMAL")


check_button.on_click(check_sensor)
reset_button.on_click(reset_system)


display(widgets.HTML(
    "<h2>SEQUENTIAL SENSOR FAULT MONITOR</h2>"
))

display(temperature)
display(pressure)
display(vibration)

display(widgets.HBox([
    check_button,
    reset_button
]))

display(output)
