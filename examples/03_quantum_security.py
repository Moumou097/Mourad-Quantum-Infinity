"""
مثال: الأمان السيبراني الكمومي

هذا المثال يوضح تطبيقات الأمان السيبراني الكمومي
"""

from quantum_security import PostQuantumCrypto, QuantumKeyDistribution


def main():
    print("="*50)
    print("مثال: الأمان السيبراني الكمومي")
    print("="*50)
    
    print(f"\n1️⃣ التشفير ما بعد الكمومي")
    print("-" * 50)
    
    message = b"رسالة سرية جداً"
    pqc = PostQuantumCrypto()
    
    hash_value = pqc.generate_hash(message)
    print(f"الرسالة الأصلية: {message}")
    print(f"Hash (SHA-256): {hash_value}")
    
    is_valid = pqc.verify_integrity(message, hash_value)
    print(f"التحقق من السلامة: {'✓ صحيح' if is_valid else '✗ خاطئ'}")
    
    signature = pqc.hash_based_signature(message)
    print(f"التوقيع (SHA-512): {signature[:32]}...")
    
    print(f"\n2️⃣ توزيع المفاتيح الكمومية (BB84)")
    print("-" * 50)
    
    qkd = QuantumKeyDistribution(n_qubits=256)
    
    shared_key, full_bits = qkd.bb84_protocol()
    print(f"المفتاح المشترك: {shared_key.hex()[:32]}...")
    
    is_secure = qkd.validate_channel()
    
    print(f"\n" + "="*50)
    print("✓ انتهى المثال بنجاح!")
    print("="*50)


if __name__ == "__main__":
    main()
