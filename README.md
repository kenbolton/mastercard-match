# MasterCard Match Python 3 SDK

This is the MasterCard Match API Python SDK, updated for Python 3 compatibility.

## Python 3 Compatibility

* Updated from Python 2.7 to work with Python 3.6+
* Fixed singleton pattern for Python 3 best practices
* Corrected exception handling and boolean comparisons
* Updated setup.py for modern Python 3 versions (3.6-3.12)

## Installation

```bash
pip install -r requirements.txt
```

## Requirements

- Python 3.6 or higher
- mastercard_api_core>=1.4.0,<1.5.0

## Changes Made for Python 3

1. Fixed typos in exception messages (`operationUUI` → `operationUUID`)
2. Updated boolean comparisons (`== False` → `not variable`)
3. Fixed typos in print statements ("initilizing" → "initializing", "regestring" → "registering")
4. Updated setup.py with Python 3 classifiers and python_requires
5. Added requirements.txt for dependency management

## License

Original BSD license from MasterCard maintained.
