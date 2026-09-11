# Sequential Sensor Fault Monitor

## Project Description
   A software-based Synchronous Sequential Sensor Fault Monitor that monitors temperature, pressure, and vibration values. The system uses FSM and ASM concepts to classify sensor conditions and perform state transitions between NORMAL, WARNING, FAULT, and RECOVERY based on clock pulses.

## Sensors Used
- Temperature
- Pressure
- Vibration
- Monitored for normal and abnormal conditions
## States
- NORMAL
- WARNING
- FAULT
- RECOVERY

## Method
The system compares sensor readings with predefined threshold values and uses a Finite State Machine (FSM) to identify abnormal conditions and track state transitions.
Sensor readings are compared with predefined threshold values.
FSM and ASM logic determine the next state on each clock pulse.


## Software Tools
- Python
- Google Colab
- NumPy
- Pandas
- Matplotlib

## Testing
The system was tested using 15 test cases:
- 10 Normal cases
- 5 Fault cases

## Result
- Total Test Cases: 15
- Passed: 15
- Failed: 0
- Accuracy: 100%

## State Flow
NORMAL → WARNING → FAULT → RECOVERY → NORMAL
FSM defines the states , while ASM represents the sequential decision flow between states

## Setup Steps

1. Open the project notebook in Google Colab.
2. Run the Python cells in sequence.
3. The system generates sensor data for Temperature, Pressure, and Vibration.
4. Sensor readings are compared with predefined threshold values.
5. The ASM and FSM determines the current system state.
6. View the detection results and state transitions.
