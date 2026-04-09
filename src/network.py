import socket
import threading
import json
import time
import numpy as np
from .engine import CommunicationEngine
from .models import CosmicMessage

class CosmicNode:
    """عقدة كونية مطورة بنظام التوجيه الهايبربولويدي (Hyperboloid Routing)"""
    
    def __init__(self, host='0.0.0.0', port=9999):
        self.host = host
        self.port = port
        self.engine = CommunicationEngine()
        self.running = False
        self.server_thread = None
        self.received_messages = []
        # إحداثيات العقدة في الفضاء الهايبربولويدي
        self.coords = (np.random.uniform(-1, 1), np.random.uniform(-1, 1))
        self.z_coord = self.coords[1]**2 - self.coords[0]**2

    def start_receiver(self):
        self.running = True
        self.server_thread = threading.Thread(target=self._run_server, daemon=True)
        self.server_thread.start()
        print(f"📡 [العقدة الهايبربولويدية]: نشطة على {self.host}:{self.port}")
        print(f"📍 [الإحداثيات البعدية]: X={self.coords[0]:.2f}, Y={self.coords[1]:.2f}, Z={self.z_coord:.2f}")

    def _run_server(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.host, self.port))
            s.listen()
            while self.running:
                conn, addr = s.accept()
                with conn:
                    data = conn.recv(4096)
                    if data:
                        payload = json.loads(data.decode())
                        encrypted_content = payload.get('content')
                        decrypted_content = self.engine.simulate_entanglement(encrypted_content)
                        
                        # حساب "انحناء الزمكان" للرسالة الواردة
                        target_z = payload.get('z_coord', 0)
                        curvature_diff = abs(self.z_coord - target_z)
                        
                        print(f"\n📥 [إشارة عابرة للأبعاد من {addr[0]}]: {decrypted_content}")
                        print(f"🌀 [انحناء المسار]: {curvature_diff:.4f} (Hyperboloid Metric)")
                        
                        # توليد رد آلي ذكي بناءً على طاقة الرسالة
                        response = self.engine.process_message(CosmicMessage(decrypted_content))
                        print(f"🌌 [رد كوني]: {response.content}")
                        print("🌌 أدخل رسالتك الكونية (أو 'خروج' للإنهاء): ", end="", flush=True)

    def send_message(self, target_host, target_port, content, sender_id="Earth-Node-1"):
        try:
            encrypted_content = self.engine.simulate_entanglement(content)
            payload = {
                'sender_id': sender_id,
                'content': encrypted_content,
                'timestamp': time.time(),
                'z_coord': self.z_coord # إرسال البعد الثالث للرسالة
            }
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(5)
                s.connect((target_host, target_port))
                s.sendall(json.dumps(payload).encode())
            return True
        except Exception as e:
            print(f"❌ [خطأ في بوابة الأبعاد]: العقدة المستهدفة غير موجودة في هذا المسار الجيوديسي. ({e})")
            return False

    def stop(self):
        self.running = False
        if self.server_thread:
            self.server_thread.join(timeout=1)
