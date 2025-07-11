# Changelog

All notable changes to this project will be documented in this file.

## [1.0.8] - 2025-07-11

### Added
- Full Python 3 compatibility (Python 3.8+)
- Python 3 compatibility verification scripts
- Installation verification script
- requirements.txt for easier dependency management
- Enhanced README.md with Python 3 compatibility information

### Changed
- **BREAKING CHANGE**: Dropped Python 2.7 support (end-of-life January 1, 2020)
- Updated minimum Python version requirement to 3.8
- Relaxed mastercard-api-client dependency version constraint (>=2.0.3 instead of ==2.0.3)
- Updated package classifiers to reflect Python 3 only support
- Optimized dictionary operations for Python 3 (removed unnecessary list() calls)

### Fixed
- Fixed critical string concatenation bug in exception messages across all API classes
  - `operationUUI` typo corrected to `operationUUID` in all getOperationConfig methods
  - This was causing NameError exceptions in Python 3
- Improved dictionary membership testing in ResourceConfig.setEnvironment()

### Removed
- Python 2.7 support and related configuration
- Python 3.5, 3.6, 3.7 support (these versions have reached end-of-life)

## [1.0.7] - Previous Version
- Legacy version with Python 2.7 support

---

### Migration Guide from 1.0.7 to 1.0.8

If you're upgrading from version 1.0.7:

1. **Python Version**: Ensure you're using Python 3.8 or higher
2. **Dependencies**: The mastercard-api-client dependency constraint has been relaxed
3. **No Code Changes Required**: All existing Python 3 code should work without modification
4. **Python 2.7**: No longer supported - you must migrate to Python 3.8+

### Compatibility Testing

Run the included verification scripts to ensure everything works correctly:

```bash
python verify_python3.py          # Verify Python 3 compatibility
python verify_installation.py     # Verify package installation
```
