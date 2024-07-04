# Paint Application

This is a simple Paint application created with Python using the `tkinter` library. The application allows users to draw on a canvas, choose brush sizes and colors, and clear the canvas.

## Features

- Draw on a canvas with adjustable brush size.
- Select brush color using a color picker.
- Clear the canvas to start a new drawing.

## Requirements

- Python 3.x
- `tkinter` (usually included with Python installations)
- `PyInstaller` (for creating an executable)

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/paint-app.git
    cd paint-app
    ```

2. **Install the required packages:**

    Since `tkinter` is included with Python, you typically do not need to install it separately. However, you do need to install `PyInstaller` if you plan to create an executable:

    ```sh
    pip install pyinstaller
    ```

## Usage

1. **Run the application:**

    You can run the application directly with Python:

    ```sh
    python main.py
    ```

2. **Create an executable:**

    To create an executable file (.exe) for Windows:

    ```sh
    pyinstaller --onefile --windowed main.py
    ```

    After running this command, the executable will be created in the `dist` directory.

## Files

- `main.py`: The main Python script containing the Paint application code.
- `README.md`: This file, providing an overview and instructions.

## Running the Application

1. Open a terminal or command prompt.
2. Navigate to the directory containing `main.py`.
3. Run the script using Python:

    ```sh
    python main.py
    ```

4. If you created an executable, navigate to the `dist` directory and run the executable file:

    ```sh
    cd dist
    ./main.exe
    ```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an issue.

## Author

- Your Name - [Your GitHub Profile](https://github.com/yourusername)
