# دليل المساهمة

شكراً لاهتمامك بالمساهمة في مشروع Mourad Quantum Infinity!

## كيفية المساهمة

### 1. Fork المستودع

```bash
git clone https://github.com/Moumou097/Mourad-Quantum-Infinity.git
cd Mourad-Quantum-Infinity
```

### 2. إنشاء فرع للميزة الجديدة

```bash
git checkout -b feature/اسم-الميزة
```

### 3. إجراء التغييرات

- اتبع معايير الكود
- أضف اختبارات للميزات الجديدة
- حدّث التوثيق إذا لزم الأمر

### 4. اختبار الكود

```bash
pytest tests/
flake8 .
mypy .
```

### 5. Commit التغييرات

```bash
git commit -m "الوصف المختصر للتغييرات"
```

### 6. Push إلى الفرع

```bash
git push origin feature/اسم-الميزة
```

### 7. فتح Pull Request

افتح PR مع وصف مفصل للتغييرات

## معايير الكود

- اتبع PEP 8
- استخدم type hints
- أضف docstrings لكل دالة
- اكتب اختبارات شاملة

## الإبلاغ عن الأخطاء

إذا وجدت خطأ، يرجى:

1. التحقق من أنه لم يتم الإبلاغ عنه بالفعل
2. فتح issue مع:
   - وصف واضح للمشكلة
   - خطوات لإعادة إنتاج الخطأ
   - النسخة المستخدمة
   - النظام المستخدم

## الأسئلة؟

لا تتردد في فتح discussion أو issue!

شكراً لمساهمتك! 🙏
