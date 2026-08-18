# CPE106L-4: Laboratory Activity 4 - Factory Design Pattern

---

## Project Overview
This laboratory activity demonstrates the implementation of the **Design Pattern** and automated **Unit Testing (`unittest`)** in Python. 

The application models a fictional railway manufacturing system (**Yuan's Rolling Stock Factory (RSF)**) where different types of trains are 'manufactured' through a centralized factory class based on the vehicle type.

---

## Design Pattern: Factory Method

### 1. Rolling Stock Hierarchy
* **Base Class (`RollingStock`):** Defines standard attributes shared by all Yuan RSF railway vehicles (`model`, `type`, `gauge_type`) and provides the base description method.
* **Derived Products:**
  * `PassengerTrain`: Specialized rolling stock for commuter/passenger transport.
  * `FreightTrain`: Heavy cargo-hauling locomotive.
  * `HighSpeedTrain`: Standard-gauge electric multiple unit (EMU) optimized for rapid transit. Concept inspired by Japan's Shinkansen

### 2. Factory Class (`TrainFactory`)
* Encapsulates the instantiation logic via the static method `create_train()`.
* Decouples the client code from concrete train classes, allowing new train variants to be added without modifying existing client logic.
* Validates inputs and raises a `ValueError` for unsupported train types.

---

## Project Structure

```text
CPE106L-4-laboratory-4/
├── screenshots/         # Terminal test run evidence
│   └── test_case_lab4_screenshots.pdf
├── src/
│   ├── main.py          # Rolling stock classes, factory, and CLI demonstration
│   └── test.py          # Automated unit test suite using Python unittest
└── README.md            # Activity documentation and instructions
```

---

## How to run

1. Navigate to the project directory in your terminal
  
2. Run the application using Python3 in Ubuntu WSL or any IDE:
   ```bash
   python3 src/main.py
   ```
3. Run unittest
    ```bash
   python3 src/test.py
   ```

## AI-Disclosure
AI assistant (Gemini) has been used to help me debug any problems during the development of this program.