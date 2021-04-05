![test](https://github.com/hackenbergstefan/coffeebuddy/workflows/test/badge.svg)
![flake8](https://github.com/hackenbergstefan/coffeebuddy/workflows/flake8/badge.svg)

# coffeebuddy

Do you use a paper based tally sheet to count your team's coffee consumption? Throw it away and use `coffeebuddy`!

## Usage

1. Optional: Create virtual environment
    ```bash
    python3 -m venv .env
    . .env/bin/activate
    pip install -r requirements.txt
    ```
    If `pyscard` fails building you might need to install dependencies. For Debian based distributions this would be
    ```sh
    sudo apt install swig libpcsclite-dev
    ```
2. Connect a pcsc smart card reader. I use a [uTrust 4701f](https://support.identiv.com/4701f/). Drivers for Ubuntu can be installed for example by
    ```sh
    sudo apt install pcscd pcsc-tools
    ```
3. Start `production` environment
    ```sh
    ./bin/run.py
    ```
    or `development` environment
    ```sh
    FLASK_ENV=development ./bin/run.py
    ```

## Tests
Run tests with `python -m unittest test/test_app.py`


## Application

The final application uses a Raspberry Pi attached to a 7" touchscreen. Thus, the HTML an CSS is optimized for a display with a resolution of 1024x600.
