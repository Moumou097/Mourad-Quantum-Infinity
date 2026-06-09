"""
Quantum Gates Implementation

تطبيق البوابات الكمومية
"""

import numpy as np


class QuantumGates:
    """
    مجموعة من البوابات الكمومية
    """
    
    @staticmethod
    def hadamard() -> np.ndarray:
        """
        بوابة Hadamard
        
        Returns:
            np.ndarray: مصفوفة Hadamard
        """
        return np.array([
            [1, 1],
            [1, -1]
        ]) / np.sqrt(2)
    
    @staticmethod
    def pauli_x() -> np.ndarray:
        """
        بوابة Pauli-X (NOT)
        
        Returns:
            np.ndarray: مصفوفة Pauli-X
        """
        return np.array([
            [0, 1],
            [1, 0]
        ])
    
    @staticmethod
    def pauli_y() -> np.ndarray:
        """
        بوابة Pauli-Y
        
        Returns:
            np.ndarray: مصفوفة Pauli-Y
        """
        return np.array([
            [0, -1j],
            [1j, 0]
        ])
    
    @staticmethod
    def pauli_z() -> np.ndarray:
        """
        بوابة Pauli-Z
        
        Returns:
            np.ndarray: مصفوفة Pauli-Z
        """
        return np.array([
            [1, 0],
            [0, -1]
        ])
    
    @staticmethod
    def phase_gate(theta: float) -> np.ndarray:
        """
        بوابة المرحلة
        
        Args:
            theta (float): الزاوية
            
        Returns:
            np.ndarray: مصفوفة بوابة المرحلة
        """
        return np.array([
            [1, 0],
            [0, np.exp(1j * theta)]
        ])
    
    @staticmethod
    def cnot() -> np.ndarray:
        """
        بوابة CNOT
        
        Returns:
            np.ndarray: مصفوفة CNOT
        """
        return np.array([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 1],
            [0, 0, 1, 0]
        ])
