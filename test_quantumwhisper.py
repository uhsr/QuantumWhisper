# test_quantumwhisper.py
"""
Tests for QuantumWhisper module.
"""

import unittest
from quantumwhisper import QuantumWhisper

class TestQuantumWhisper(unittest.TestCase):
    """Test cases for QuantumWhisper class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = QuantumWhisper()
        self.assertIsInstance(instance, QuantumWhisper)
        
    def test_run_method(self):
        """Test the run method."""
        instance = QuantumWhisper()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
