# Financial Calculator

A KivyMD-based financial calculator application for Android. Built with Python, Kivy, and KivyMD.

## Features

### Calculator
- Basic arithmetic operations (+, -, ×, ÷)
- Percentage calculations
- Answer memory (Ans button)

### Time Value of Money (TVM)
- Future Value (FV)
- Present Value (PV)
- Payment (PMT)
- Number of Periods (Nper)
- Interest Rate calculation

### Assets Valuation
- Straight-line depreciation
- Declining balance depreciation
- Return on Investment (ROI)
- Net Present Value (NPV)
- Internal Rate of Return (IRR)

## Requirements

- Python 3.x
- Kivy
- KivyMD
- Buildozer (for Android build)

## Installation

```bash
pip install kivy kivymd pillow
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
├── main.py              # App entry point
├── main.kv              # Screen manager
├── buildozer.spec       # Buildozer configuration
├── assets/
│   ├── calculator/      # Calculator screen
│   ├── tvm/             # Time Value of Money screen
│   └── assets_val/     # Assets Valuation screen
```

## License

MIT
