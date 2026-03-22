# ACPPL – Causal Security Analysis Engine

ACPPL هو محرك تحليل أمني سببي.

بدلاً من أن يخبرك "ماذا حدث"، يخبرك "لماذا حدث".

## 💡 الفكرة

بدل:
failed_logins → alert

ACPPL يقول:
weak_passwords + no_rate_limiting → brute_force → account_compromise

---

## 🚀 مثال استخدام

```python
from acppl import CausalEngine, Event

engine = CausalEngine()

engine.add_event(Event("failed_logins", "now"))

results = engine.analyze()

print(results)
