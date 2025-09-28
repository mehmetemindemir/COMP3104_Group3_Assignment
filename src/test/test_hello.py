#!/usr/bin/env python3
"""
Test file for hello.py
Demonstrates testing practices for the group assignment
"""

import sys
import os
import unittest

# Add the main source directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'main'))

from hello import get_group_info

class TestHello(unittest.TestCase):
    """Test cases for the hello module"""
    
    def test_get_group_info(self):
        """Test that group info returns correct information"""
        info = get_group_info()
        
        # Test that we get a dictionary
        self.assertIsInstance(info, dict)
        
        # Test specific values
        self.assertEqual(info['course'], 'COMP3104')
        self.assertEqual(info['group_number'], 3)
        self.assertEqual(info['assignment'], 'Group Assignment')
        self.assertEqual(info['institution'], 'George Brown College')
    
    def test_group_info_keys(self):
        """Test that all expected keys are present"""
        info = get_group_info()
        expected_keys = ['course', 'group_number', 'assignment', 'institution']
        
        for key in expected_keys:
            self.assertIn(key, info)

if __name__ == '__main__':
    unittest.main()