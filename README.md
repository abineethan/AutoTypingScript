# AutoTyper - Keyboard Automation Script

A Python script that simulates human typing behavior with customizable speed, formatting, and repetition options.

## Features

* Types any given text with adjustable character delay
* Supports two output formats:

  * **Newline-separated** (each repetition on a new line)
  * **Continuous text** (all repetitions concatenated)
* Customizable repetition count
* Proper handling of:

  * Uppercase letters (using **Shift** key)
  * Special characters (**Enter**, **Space**, **Tab**)
  * Emojis and Unicode characters (via clipboard)
* Progress tracking during typing
* Countdown before execution begins

## Requirements

* Python 3.x
* Required packages:

  ```bash
  pip install keyboard pyperclip
  ```

## Installation

### Step 1: Download or Clone the Repository

```bash
git clone https://github.com/abineethan/AutoTypingScript.git

```

Or just download the `.py` file directly.

### Step 2: Install Required Packages

```bash
pip install keyboard pyperclip
```

## Usage

1. Run the script:

   ```bash
   python autotyper.py
   ```

2. Enter the text you want to type.

3. Choose the output format:

   * `newline` — each repetition appears on a new line
   * `continuous` — all repetitions typed in one line

4. Set the delay between characters (in seconds).

5. Set how many times to repeat the text.

6. The script will start typing after a short countdown.

## Demo Video

[![Watch Demo](https://img.youtube.com/vi/hzaWfCkorn8/0.jpg)](https://www.youtube.com/watch?v=hzaWfCkorn8)

📺 Click the image above or [watch on YouTube](https://www.youtube.com/watch?v=hzaWfCkorn8)
