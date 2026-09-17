import streamlit as st

# -----------------------------
# PROJECT SETTINGS
# -----------------------------

TEMP_LIMIT = 50
PRESSURE_MIN = 90
PRESSURE_MAX = 110
VIBRATION_LIMIT = 5


# -----------------------------
# SENSOR CONDITION
# -----------------------------

def get_condition(temperature, pressure, vibration):

    temp_fault = temperature > TEMP_LIMIT

    pressure_fault = (
        pressure < PRESSURE_MIN
        or pressure > PRESSURE_MAX
    )

    vibration_fault = vibration > VIBRATION_LIMIT

    if temp_fault or pressure_fault or vibration_fault:
        return "ABNORMAL"

    return "NORMAL"


# -----------------------------
# FSM STATE TRANSITION
# -----------------------------

def next_state(current_state, condition):

    if current_state == "NORMAL":

        if condition == "ABNORMAL":
            return "WARNING"

    elif current_state == "WARNING":

        if condition == "ABNORMAL":
            return "FAULT"
        else:
            return "NORMAL"

    elif current_state == "FAULT":

        if condition == "NORMAL":
            return "RECOVERY"

    elif current_state == "RECOVERY":

        if condition == "NORMAL":
            return "NORMAL"
        else:
            return "FAULT"

    return current_state


# -----------------------------
# STREAMLIT PAGE
# -----------------------------

st.set_page_config(
    page_title="Sequential Sensor Fault Monitor",
    page_icon="⚙️",
    layout="wide"
)

st.title("SEQUENTIAL SENSOR FAULT MONITOR")

st.write(
    "Software-Based Sequential Fault Detection System"
)

st.divider()


# -----------------------------
# SESSION STATE
# -----------------------------

if "current_state" not in st.session_state:
    st.session_state.current_state = "NORMAL"

if "previous_state" not in st.session_state:
    st.session_state.previous_state = "NORMAL"

if "last_condition" not in st.session_state:
    st.session_state.last_condition = "NORMAL"


# -----------------------------
# SENSOR INPUTS
# -----------------------------

st.subheader("Sensor Inputs")

col1, col2, col3 = st.columns(3)

with col1:
    temperature = st.number_input(
        "Temperature (°C)",
        value=30.0,
        step=1.0
    )

with col2:
    pressure = st.number_input(
        "Pressure (kPa)",
        value=100.0,
        step=1.0
    )

with col3:
    vibration = st.number_input(
        "Vibration (mm/s)",
        value=2.0,
        step=0.1
    )


# -----------------------------
# THRESHOLDS
# -----------------------------

st.subheader("Threshold Values")

st.write(
    f"Temperature ≤ {TEMP_LIMIT} °C  |  "
    f"Pressure = {PRESSURE_MIN}–{PRESSURE_MAX} kPa  |  "
    f"Vibration ≤ {VIBRATION_LIMIT} mm/s"
)


# -----------------------------
# CURRENT SENSOR CONDITION
# -----------------------------

condition = get_condition(
    temperature,
    pressure,
    vibration
)

if condition == "NORMAL":
    st.success("Sensor Condition: NORMAL")
else:
    st.error("Sensor Condition: ABNORMAL")


# -----------------------------
# BUTTONS
# -----------------------------

col4, col5 = st.columns(2)

with col4:

    clock_pressed = st.button(
        "CLOCK PULSE",
        type="primary",
        use_container_width=True
    )

with col5:

    reset_pressed = st.button(
        "RESET",
        use_container_width=True
    )


# -----------------------------
# CLOCK PULSE
# -----------------------------

if clock_pressed:

    previous = st.session_state.current_state

    new_state = next_state(
        previous,
        condition
    )

    st.session_state.previous_state = previous
    st.session_state.current_state = new_state
    st.session_state.last_condition = condition


# -----------------------------
# RESET
# -----------------------------

if reset_pressed:

    st.session_state.current_state = "NORMAL"
    st.session_state.previous_state = "NORMAL"
    st.session_state.last_condition = "NORMAL"


# -----------------------------
# CURRENT STATE DISPLAY
# -----------------------------

st.divider()

st.subheader("ASM State Monitor")

state = st.session_state.current_state

if state == "NORMAL":

    st.success(f"CURRENT STATE: {state}")

elif state == "WARNING":

    st.warning(f"CURRENT STATE: {state}")

elif state == "FAULT":

    st.error(f"CURRENT STATE: {state}")

elif state == "RECOVERY":

    st.info(f"CURRENT STATE: {state}")


# -----------------------------
# STATE TRANSITION
# -----------------------------

st.write(
    "Previous State :",
    st.session_state.previous_state
)

st.write(
    "Sensor Condition :",
    st.session_state.last_condition
)

st.write(
    "State Transition :",
    f"{st.session_state.previous_state} → "
    f"{st.session_state.current_state}"
)


# -----------------------------
# STATE FLOW
# -----------------------------

st.divider()

st.subheader("FSM State Flow")

st.code(
    """
NORMAL
   ↓
WARNING
   ↓
FAULT
   ↓
RECOVERY
   ↓
NORMAL
"""
)


# -----------------------------
# PROJECT INFORMATION
# -----------------------------

st.divider()

st.subheader("Project Information")

st.write("Sensors: Temperature, Pressure, Vibration")
st.write("FSM States: NORMAL, WARNING, FAULT, RECOVERY")
st.write("Sequential synchronous state transition using CLOCK PULSE.")