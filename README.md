# Financial Calculator

A Python-based financial calculator application for Android. Built with Kivy.

## Features

### Calculator
- Basic arithmetic operations (+, -, ×, ÷)
- Percentage calculations
- Answer memory (Ans button)
- Clear and backspace functionality

### Time Value of Money (TVM)
- Future Value (FV)
- Present Value (PV)
- Payment (PMT)
- Number of Periods (NPER)

### Assets Valuation
- Straight-line depreciation
- Declining balance depreciation

## Requirements

- Python 3.x
- Kivy
- Pillow

## Installation

```bash
pip install -r requirements.txt
```

## Running Locally

```bash
python main.py
```

## Building for Android

The project uses GitHub Actions for building. Push to main branch and the APK will be built automatically.

Or build locally:

```bash
buildozer android debug
```

## Project Structure

```
calc(kivy)/
├── main.py              # App entry point and Screen Manager
├── buildozer.spec       # Buildozer configuration
├── requirements.txt     # Python dependencies
├── assets/
│   ├── calculator/      # Calculator screen (calculator.py)
│   ├── tvm/             # Time Value of Money screen (tvm.py)
│   └── assets_val/      # Assets Valuation screen (assets_val.py)
└── .github/
    └── workflows/      # GitHub Actions CI/CD
```

## Screens

1. **Calculator** - Basic calculator with modern UI
2. **TVM** - Time Value of Money calculations
3. **Assets** - Asset depreciation calculations

## License

MIT