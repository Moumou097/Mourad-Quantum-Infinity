"""
Quantum Computing Module

هذه الوحدة توفر أدوات للعمل مع الدوائر الكمومية والحوسبة الكمومية
"""

__version__ = "0.1.0"
__author__ = "Moumou097"

from .quantum_circuit import QuantumCircuit
from .quantum_gates import QuantumGates

__all__ = [
    "QuantumCircuit",
    "QuantumGates",
]
