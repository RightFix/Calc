# Financial Calculator

A Python-based financial calculator application for Android. Built with Kivy.

## Features

### Calculator
- Basic arithmetic operations (+, -, ×, ÷)
- Percentage calculations
- Answer memory (Ans button)
- Clear and backspace functionality

### Scientific Calculator
- Trigonometric functions: sin, cos, tan
- Logarithmic functions: log, ln
- Square root (√)
- Power operator (^)
- Constants: π, e
- Degree/Radian mode toggle (DEG button)
- Answer memory (Ans button)

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
│   ├── images/          # App icon and presplash
│   ├── pages/
│   │   ├── calculator.py    # Basic calculator screen
│   │   ├── scientific.py     # Scientific calculator screen
│   │   ├── tvm.py            # Time Value of Money screen
│   │   └── assets_val.py     # Assets Valuation screen
│   └── ui_custom.py     # Custom UI components
└── .github/
    └── workflows/      # GitHub Actions CI/CD
```

## Navigation

The app uses a bottom navigation bar on each screen:
- **Calc** - Basic calculator
- **Sci** - Scientific calculator with trigonometric and logarithmic functions
- **TVM** - Time Value of Money calculations
- **Assets** - Asset depreciation calculations

## Screens

1. **Calculator** - Basic calculator with modern UI
2. **Scientific** - Scientific calculator with sin, cos, tan, log, ln, √, ^, π, e functions
3. **TVM** - Time Value of Money calculations
4. **Assets** - Asset depreciation calculations

## License

MIT