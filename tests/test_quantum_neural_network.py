"""
اختبارات شبكة عصبية كمومية
"""

import pytest
import numpy as np
from quantum_ai import QuantumNeuralNetwork


class TestQuantumNeuralNetwork:
    """
    فئة اختبار الشبكة العصبية الكمومية
    """
    
    def setup_method(self):
        """تهيئة قبل كل اختبار"""
        self.qnn = QuantumNeuralNetwork(n_qubits=4, n_layers=2)
    
    def test_initialization(self):
        """اختبار التهيئة"""
        assert self.qnn.n_qubits == 4
        assert self.qnn.n_layers == 2
        assert self.qnn.parameters is not None
    
    def test_parameter_shape(self):
        """اختبار شكل المعاملات"""
        expected_size = 4 * 2 * 3  # n_qubits * n_layers * 3
        assert len(self.qnn.parameters) == expected_size
    
    def test_train(self):
        """اختبار التدريب"""
        X = np.random.randn(10, 4)
        y = np.random.randint(0, 2, 10)
        
        # يجب ألا يرفع استثناء
        self.qnn.train(X, y, epochs=5)
    
    def test_predict(self):
        """اختبار التنبؤ"""
        X = np.random.randn(5, 4)
        predictions = self.qnn.predict(X)
        
        assert len(predictions) == 5
        assert all(p in [0, 1] for p in predictions)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
