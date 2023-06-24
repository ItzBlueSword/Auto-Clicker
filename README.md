# Auto Clicker

The Auto Clicker is a simple Python script that allows you to automate mouse clicks. It provides a customizable click speed and the ability to start/stop the clicker with a key press or through a graphical user interface (GUI).

## Prerequisites
- **Python 3.x**
- **Install pynput library**

## Features
- **Toggle Clicker**: Press the 't' key on your keyboard to start or stop the clicker. When the clicker is active, it will continuously perform mouse clicks at the specified click speed.

- **Adjust Click Speed**: Use the GUI buttons provided in the pop-up window to adjust the click speed:
- "Speed Up" button: Increases the click speed by 0.001 seconds.
- "Speed Down" button: Decreases the click speed by 0.001 seconds.

- **Customization**: You can customize the script according to your requirements. Here are some possible modifications:
- Change the toggle key: Modify the `TOGGLE_KEY` variable in the script to use a different key for toggling the clicker.
- Modify the initial click speed: Adjust the `click_speed` variable to set a different initial click speed (in seconds) for the auto clicker.
- Extend functionality: Add additional features such as different click types, configurable coordinates, or specific click intervals.

## How to Run
To run the Auto Clicker, follow these steps:

1. Clone the repository or download the clicker.py file.

2. Ensure that you have Python 3.x installed on your system.

3. Install the required dependencies by opening a terminal or command prompt and running the following command:
    ``````````````````
    pip install pynput
    ``````````````````
4. Open a terminal or command prompt and navigate to the directory where the `clicker.py` file is located.

5. Run the script using the following command:
   ```````````````````
   python clicker.py
   ```````````````````
6. The auto clicker will start running in the background. By default, the click speed is set to 0.007 seconds.

7. To start or stop the clicker, press the 't' key on your keyboard.

8. To adjust the click speed, use the GUI buttons provided in the pop-up window:
* "Speed Up" button and 'u' key: Increases the click speed by 0.001 seconds.
* "Speed Down" button and 'd' key: Decreases the click speed by 0.001 seconds.

## Disclaimer

Please use this auto clicker responsibly and in accordance with the terms and conditions of the applications or websites you are using it with. Misuse or unauthorized use of this script may violate terms of service or terms of use.

## License
This project is licensed under the **MIT License**.
