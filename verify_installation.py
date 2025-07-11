#!/usr/bin/env python3
"""
Installation verification script for mastercard-match package.
Run this after installing the package to verify it works correctly.
"""

import sys

def verify_installation():
    """Verify that the package can be imported and basic functionality works."""
    print(f"Python version: {sys.version}")
    print()
    
    try:
        # Test basic import
        print("Testing package imports...")
        import mastercardmatch
        from mastercardmatch.resourceconfig import ResourceConfig
        print("✓ Package imports successful")
        
        # Test ResourceConfig singleton
        print("\nTesting ResourceConfig...")
        config = ResourceConfig.getInstance()
        print(f"✓ ResourceConfig version: {config.getVersion()}")
        print(f"✓ ResourceConfig name: {config.getName()}")
        
        # Test class imports
        print("\nTesting API classes...")
        from mastercardmatch.acquirercontactrequest import AcquirerContactRequest
        from mastercardmatch.addterminatedmerchant import AddTerminatedMerchant
        from mastercardmatch.retroactiveinquirydetailsrequest import RetroactiveInquiryDetailsRequest
        from mastercardmatch.retroactiveinquiryrequest import RetroactiveInquiryRequest
        from mastercardmatch.terminationinquiryhistoryrequest import TerminationInquiryHistoryRequest
        from mastercardmatch.terminationinquiryrequest import TerminationInquiryRequest
        print("✓ All API classes imported successfully")
        
        print("\n🎉 Installation verification successful!")
        print("\nThe mastercard-match package is properly installed and")
        print("compatible with Python 3. You can now use it in your projects.")
        
        return True
        
    except ImportError as e:
        print(f"✗ Import error: {e}")
        print("\nPlease ensure the package is properly installed:")
        print("pip install mastercard-match")
        return False
    except Exception as e:
        print(f"✗ Unexpected error: {e}")
        return False

if __name__ == "__main__":
    if verify_installation():
        sys.exit(0)
    else:
        sys.exit(1)
