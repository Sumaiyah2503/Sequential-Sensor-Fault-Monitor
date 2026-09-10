# Sequential Sensor Fault Monitor

## Project Description
A software-based sequential fault detection system for monitoring temperature, pressure, and vibration sensor data.

## Sensors Used
- Temperature
- Pressure
- Vibration

## States
- NORMAL
- WARNING
- FAULT
- RECOVERY

## Method
The system compares sensor readings with predefined threshold values and uses a Finite State Machine (FSM) to identify abnormal conditions and track state transitions.

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
