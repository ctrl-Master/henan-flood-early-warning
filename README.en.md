# Henan Central Flood Early-Warning · Open-Source Reference

> A monitoring & early-warning system for extreme rainfall and typhoon-driven flooding in central Henan (Zhengzhou — Xuchang — Luohe).
> A complete reference implementation: system design + Python algorithm engine + interactive demo.

[中文文档](./README.md) · [Contributing](./CONTRIBUTING.md) · [Disclaimer](./DISCLAIMER.md)

---

## Read this first: what it is, and what it is NOT

**This IS:**

- An open-source **reference architecture and algorithm prototype** for learning how a flood early-warning system is roughly put together.
- Runnable code: DFRI composite risk index, Muskingum flood routing, probabilistic / uncertainty propagation, data-quality scoring, and a 4-level warning + evacuation engine.

**This is NOT:**

- A **production-grade** system that has been operationally calibrated and validated for real flood command.
- Something you should use to make real evacuation decisions, or a replacement for official warnings from the meteorological / water-resources authorities.

> For the full, serious liability and legal disclaimer, read **[DISCLAIMER.md](./DISCLAIMER.md)** — please do so first.
> Short version: open-sourcing does not transfer liability. If you misuse it, the responsibility is yours.

---

## Repository layout

```
.
├── 系统设计方案.md            # Full technical design (CN, with Mermaid / JSON Schema / formulas)
├── algorithms/
│   └── flood_risk_engine.py  # Python core engine (DFRI / Muskingum / probabilistic / DQS / verification / warning lifecycle)
├── data/
│   └── sample_data.json      # Synthetic, de-identified sample data for 3 cities / 8 sites
├── demo/
│   └── index.html            # Interactive demo (dark dashboard + 6 advanced panels)
├── start.py                  # One-click launcher (static server + opens browser)
├── LICENSE                   # MIT
└── DISCLAIMER.md             # Liability & disclaimer
```

---

## Quick start

```bash
# 1) Clone and enter the directory
cd henan-flood-early-warning

# 2) Launch the demo (starts a local server and opens your browser)
python start.py

# 3) Or run the algorithm engine's built-in examples directly
python algorithms/flood_risk_engine.py
```

`start.py` auto-selects a port (default 8090, +1 if busy), starts a static server, and tries to open your default browser; press `Ctrl+C` to stop.
(It's a `.py` rather than a `.bat` on purpose, to avoid encoding issues with the Chinese path.)

---

## Core capabilities

| Module | Notes |
|--------|-------|
| **DFRI composite risk index** | Rainfall / topography / reservoir / population, with data-quality factor $Q_i$ and adaptive weights |
| **Probabilistic output** | Monte-Carlo / ensemble → point estimate + 5%~95% interval + dominant risk-factor decomposition |
| **Muskingum flood routing** | Reservoir → river → urban: arrival time and over-warning probability |
| **Data-quality scoring (DQS)** | Missing / staleness / jump / sensor-status → auto down-weight + imputation fallback |
| **4-level warning + lifecycle** | Blue / Yellow / Orange / Red; persistent + spatial-consistency triggers, clearance, review |
| **Explainability** | Contribution decomposition — why a warning fired, in plain terms |

---

## Tech stack

- **Algorithm / backend reference**: Python 3.11+ (standard library only — no heavy deps)
- **Demo frontend**: plain HTML/CSS/JS + Leaflet (maps) + Apache ECharts (charts), via public CDN
- **Design docs**: Markdown + Mermaid

---

## Third-party licenses

The demo loads these open-source libraries via public CDN (copyright belongs to their respective authors; this project only references them):

- **Leaflet** — BSD-2-Clause
- **Apache ECharts** — Apache-2.0

All original code, docs, and sample data here are open-sourced under the **MIT License** (see [LICENSE](./LICENSE)).

---

## License

[MIT](./LICENSE) © 2026 ZHX NEXUS Studio

---

## Author / brand

**ZHX NEXUS Studio** — an independent personal project.
The business model is abstracted from real hydrological scenarios and de-identified; it does not represent any real client or employer system.
