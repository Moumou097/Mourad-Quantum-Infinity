"""
Quantum Circuit Implementation

تطبيق الدوائر الكمومية
"""

import numpy as np
from typing import List, Optional


class QuantumCircuit:
    """
    دارة كمومية
    
    Attributes:
        n_qubits (int): عدد الكيوبتات
        gates (List): قائمة البوابات
    """
    
    def __init__(self, n_qubits: int = 4):
        """
        تهيئة الدارة الكمومية
        
        Args:
            n_qubits (int): عدد الكيوبتات (افتراضي: 4)
        """
        self.n_qubits = n_qubits
        self.gates = []
        self.state = self._initialize_state()
    
    def _initialize_state(self) -> np.ndarray:
        """
        تهيئة حالة الكيوبتات
        
        Returns:
            np.ndarray: حالة الكيوبتات الأولية
        """
        # الحالة الأولية: جميع الكيوبتات في حالة |0>
        state = np.zeros(2**self.n_qubits)
        state[0] = 1.0
        return state
    
    def add_h_gate(self, qubit: int) -> None:
        """
        إضافة بوابة Hadamard
        
        Args:
            qubit (int): رقم الكيوبت
        """
        self.gates.append(("H", qubit))
        print(f"تم إضافة بوابة Hadamard على الكيوبت {qubit}")
    
    def add_cnot_gate(self, control: int, target: int) -> None:
        """
        إضافة بوابة CNOT
        
        Args:
            control (int): الكيوبت التحكم
            target (int): الكيوبت الهدف
        """
        self.gates.append(("CNOT", control, target))
        print(f"تم إضافة بوابة CNOT: {control} -> {target}")
    
    def add_rx_gate(self, qubit: int, angle: float) -> None:
        """
        إضافة بوابة RX
        
        Args:
            qubit (int): رقم الكيوبت
            angle (float): الزاوية بالراديان
        """
        self.gates.append(("RX", qubit, angle))
        print(f"تم إضافة بوابة RX على الكيوبت {qubit} بزاوية {angle}")
    
    def measure(self, shots: int = 1000) -> dict:
        """
        قياس الدارة الكمومية
        
        Args:
            shots (int): عدد مرات القياس (افتراضي: 1000)
            
        Returns:
            dict: نتائج القياسات
        """
        probabilities = np.abs(self.state) ** 2
        measurements = np.random.choice(
            range(2**self.n_qubits),
            size=shots,
            p=probabilities
        )
        
        results = {}
        for measurement in measurements:
            binary = format(measurement, f'0{self.n_qubits}b')
            results[binary] = results.get(binary, 0) + 1
        
        return results
    
    def display_circuit(self) -> None:
        """
        عرض الدارة الكمومية
        """
        print(f"الدارة الكمومية: {self.n_qubits} كيوبتات")
        print(f"عدد البوابات: {len(self.gates)}")
        for i, gate in enumerate(self.gates):
            print(f"  {i+1}. {gate}")
