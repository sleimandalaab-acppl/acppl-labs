🔬 ACPPL – Causal Security Analysis Engine

«Understand why attacks happen — not just what happened.»

---

🚨 The Problem

Most security tools like SIEM, IDS, and monitoring systems tell you:

- ⚠️ High failed logins
- ⚠️ Suspicious activity detected
- ⚠️ Possible brute force attack

But they fail to answer the most critical question:

«❗ Why did this attack happen?»

---

💡 The Solution: ACPPL

ACPPL (Causal Security Analysis Engine) connects events with their root causes to provide a full causal explanation of security incidents.

Instead of alerts like:

Brute force attack detected

ACPPL explains:

weak_passwords + no_rate_limiting → brute_force → account_compromise

---

⚙️ How It Works

ACPPL follows a causal reasoning pipeline:

1. 📥 Collect security events
2. 🧠 Apply causal policies
3. 🔗 Build causal graph
4. 📊 Calculate probability
5. 📤 Output:
   - Risk level
   - Causal path
   - Recommendations

---

🚀 Quick Example

from acppl import CausalEngine, Event
from acppl.analyzers import brute_force_policy
from datetime import datetime

engine = CausalEngine()
engine.register_policy(brute_force_policy)

engine.add_event(Event("failed_logins", datetime.now(), count=150))

results = engine.analyze()

for r in results:
    print(r.summary())

---

📊 Example Output

[CRITICAL] brute_force
Probability: 87%

Causal Path:
no_rate_limiting → failed_logins → brute_force

Recommendations:
- Enable rate limiting
- Block suspicious IPs
- Enforce stronger passwords

---

🎯 Why ACPPL is Different

Tool Type| What it does
SIEM (e.g. Splunk)| Detects events
IDS/IPS| Detects attacks
🔥 ACPPL| Explains root causes

---

🧠 Use Cases

- 🔍 Post-incident analysis
- 🛡️ Root cause detection
- ⚙️ Security policy improvement
- 👨‍💻 SOC team support
- 📊 Risk explanation for decision-makers

---

📦 Installation

pip install -e .

---

🛠️ Project Status

ACPPL is currently an MVP (Minimum Viable Product).

It is suitable for:

- experimentation
- prototyping
- research
- early-stage security analysis

---

🧩 Roadmap

- [ ] Real log integrations (SIEM / API)
- [ ] AI-assisted policy generation
- [ ] Advanced Bayesian inference
- [ ] Visualization dashboard
- [ ] SaaS version

---

🤝 Contributing

Contributions are welcome!

You can help by:

- Reporting bugs
- Suggesting features
- Adding new attack patterns
- Improving documentation

---

📄 License

MIT License

---

📬 Contact

Interested in using ACPPL in your company?

Open an issue or reach out via GitHub.

---

⭐ Support the Project

If you find this project useful:

👉 Star the repository
👉 Share it with security engineers
👉 Contribute to its growth

---

ACPPL – Turning security alerts into understanding.
