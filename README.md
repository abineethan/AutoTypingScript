# AutoTyper - Keyboard Automation Script

A Python script that simulates human typing behavior with customizable speed, formatting, and repetition options.

## Features

- Types any given text with adjustable character delay
- Supports two output formats:
  - Newline-separated (each repetition on a new line)
  - Continuous text (all repetitions concatenated)
- Customizable repetition count
- Proper handling of:
  - Uppercase letters (using Shift key)
  - Special characters (Enter, Space, Tab)
  - Emojis and Unicode characters (via clipboard)
- Progress tracking during typing
- Countdown before execution begins

## Requirements

- Python 3.x
- Required packages:
  - `keyboard` (`pip install keyboard`)
  - `pyperclip` (`pip install pyperclip`)

## Installation

1. Clone this repository or download the script
2. Install required packages:
   ```bash
   pip install keyboard pyperclip