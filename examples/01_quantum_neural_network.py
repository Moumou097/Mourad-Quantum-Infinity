"""
مثال: شبكة عصبية كمومية بسيطة

هذا المثال يوضح كيفية إنشاء واستخدام شبكة عصبية كمومية
"""

import numpy as np
from quantum_ai import QuantumNeuralNetwork


def main():
    print("="*50)
    print("مثال: شبكة عصبية كمومية")
    print("="*50)
    
    # إنشاء شبكة عصبية كمومية
    qnn = QuantumNeuralNetwork(n_qubits=4, n_layers=2)
    print(f"✓ تم إنشاء شبكة عصبية كمومية")
    print(f"  - عدد الكيوبتات: 4")
    print(f"  - عدد الطبقات: 2")
    
    # إنشاء بيانات تدريب
    X_train = np.random.randn(20, 4)
    y_train = np.random.randint(0, 2, 20)
    print(f"\n✓ تم توليد بيانات التدريب")
    print(f"  - حجم البيانات: {X_train.shape}")
    
    # تدريب الشبكة
    print(f"\n📚 بدء التدريب...")
    qnn.train(X_train, y_train, epochs=10)
    
    # الاختبار
    X_test = np.random.randn(5, 4)
    print(f"\n🔮 التنبؤ بنتائج الاختبار...")
    predictions = qnn.predict(X_test)
    print(f"  - التنبؤات: {predictions}")
    
    print(f"\n" + "="*50)
    print("✓ انتهى المثال بنجاح!")
    print("="*50)


if __name__ == "__main__":
    main()
