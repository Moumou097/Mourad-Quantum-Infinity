"""
اختبارات الدوائر الكمومية
"""

import pytest
import numpy as np
from quantum_computing import QuantumCircuit


class TestQuantumCircuit:
    """
    فئة اختبار الدوائر الكمومية
    """
    
    def setup_method(self):
        """تهيئة قبل كل اختبار"""
        self.qc = QuantumCircuit(n_qubits=2)
    
    def test_initialization(self):
        """اختبار التهيئة"""
        assert self.qc.n_qubits == 2
        assert len(self.qc.gates) == 0
    
    def test_add_hadamard_gate(self):
        """اختبار إضافة بوابة Hadamard"""
        self.qc.add_h_gate(0)
        assert len(self.qc.gates) == 1
        assert self.qc.gates[0][0] == "H"
    
    def test_add_cnot_gate(self):
        """اختبار إضافة بوابة CNOT"""
        self.qc.add_cnot_gate(0, 1)
        assert len(self.qc.gates) == 1
        assert self.qc.gates[0][0] == "CNOT"
    
    def test_measure(self):
        """اختبار القياس"""
        self.qc.add_h_gate(0)
        results = self.qc.measure(shots=100)
        
        assert isinstance(results, dict)
        assert sum(results.values()) == 100


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
