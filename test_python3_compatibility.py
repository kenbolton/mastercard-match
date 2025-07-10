#!/usr/bin/env python3
"""
Test script for MasterCard Match Python 3 SDK

This script demonstrates that the package has been successfully converted to Python 3.
"""

def test_imports():
    """Test that all modules can be imported without errors."""
    try:
        # Test core module imports
        from mastercardmatch.acquirercontactrequest import AcquirerContactRequest
        from mastercardmatch.addterminatedmerchant import AddTerminatedMerchant
        from mastercardmatch.retroactiveinquirydetailsrequest import RetroactiveInquiryDetailsRequest
        from mastercardmatch.retroactiveinquiryrequest import RetroactiveInquiryRequest
        from mastercardmatch.terminationinquiryhistoryrequest import TerminationInquiryHistoryRequest
        from mastercardmatch.terminationinquiryrequest import TerminationInquiryRequest
        from mastercardmatch.resourceconfig import ResourceConfig
        
        print("✓ All module imports successful")
        return True
    except ImportError as e:
        print(f"✗ Import error: {e}")
        return False

def test_singleton_pattern():
    """Test that the ResourceConfig singleton pattern works correctly."""
    try:
        from mastercardmatch.resourceconfig import ResourceConfig
        
        # Create two instances and verify they're the same object
        config1 = ResourceConfig.getInstance()
        config2 = ResourceConfig.getInstance()
        
        if config1 is config2:
            print("✓ Singleton pattern working correctly")
            return True
        else:
            print("✗ Singleton pattern not working - different instances returned")
            return False
    except Exception as e:
        print(f"✗ Singleton test error: {e}")
        return False

def test_operation_config():
    """Test that operation config methods work correctly."""
    try:
        from mastercardmatch.acquirercontactrequest import AcquirerContactRequest
        
        # Test that we can access the configuration
        request = AcquirerContactRequest({})
        uuid = "3f23a81f-ab1e-4c0e-a727-e75ad475efe6"
        config = request.getOperationConfig(uuid)
        
        print("✓ Operation config access working")
        
        # Test invalid UUID (should raise an exception)
        try:
            request.getOperationConfig("invalid-uuid")
            print("✗ Invalid UUID should have raised an exception")
            return False
        except Exception:
            print("✓ Invalid UUID correctly raises exception")
            return True
            
    except Exception as e:
        print(f"✗ Operation config test error: {e}")
        return False

def main():
    """Run all tests."""
    print("Testing MasterCard Match Python 3 SDK")
    print("=" * 40)
    
    tests = [
        test_imports,
        test_singleton_pattern,
        test_operation_config
    ]
    
    passed = 0
    for test in tests:
        if test():
            passed += 1
    
    print("=" * 40)
    print(f"Tests passed: {passed}/{len(tests)}")
    
    if passed == len(tests):
        print("🎉 All tests passed! Python 3 conversion successful!")
        return 0
    else:
        print("❌ Some tests failed. Please check the errors above.")
        return 1

if __name__ == "__main__":
    exit(main())
