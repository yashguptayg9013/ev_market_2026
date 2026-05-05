# 🔌 EV Market Analysis 2026

A comprehensive exploratory data analysis (EDA) of the global electric vehicle (EV) market using a dataset of 2026 EV models across major brands, segments, and regions.

---

## 📋 Project Overview

This project dives deep into the EV landscape of 2026, analyzing pricing trends, performance metrics, market segmentation, and sales patterns across brands like Tesla, BYD, Volkswagen, BMW, Hyundai, Kia, Mercedes, Ford, Audi, and more.

As a business analyst, this project aims to surface actionable insights for stakeholders in the automotive, investment, and policy sectors.

---

## 📂 Dataset

**File:** `ev_market_2026.csv`

| Column | Description |
|---|---|
| `brand` | Manufacturer name |
| `model` | Vehicle model |
| `year` | Model year (2020–2026) |
| `variant` | Trim level (Base, Standard, Premium, Long Range, Performance) |
| `price_usd` | Retail price in USD |
| `battery_capacity_kwh` | Battery size in kWh |
| `range_miles` | Estimated driving range (miles) |
| `charging_speed_kw` | Max charging speed (kW) |
| `acceleration_0_60_mph` | 0–60 mph time (seconds) |
| `top_speed_mph` | Top speed (mph) |
| `horsepower` | Motor output (hp) |
| `torque_nm` | Torque (Newton-meters) |
| `drive_type` | Drivetrain (AWD / FWD / RWD) |
| `seating_capacity` | Number of seats |
| `body_type` | Vehicle body style |
| `cargo_volume_cubic_ft` | Cargo space (cubic ft) |
| `weight_kg` | Vehicle weight (kg) |
| `safety_rating` | Safety score (1–5) |
| `autopilot_level` | SAE autonomy level (0–3) |
| `country_of_origin` | Manufacturing country |
| `market_segment` | Budget / Mid-range / Premium / Luxury |
| `annual_sales_units` | Units sold per year |
| `customer_rating` | Customer satisfaction score |
| `warranty_years` | Warranty duration (years) |

---

## 🔍 Key Insights

- **Tesla** leads in Luxury segment annual sales, with Model Y regularly exceeding **400,000 units/year**
- **BYD** dominates the Budget segment with models like the Seagull starting at **~$16,000** — making EVs accessible at scale
- **Price range** spans from **$16K to $210K+**, reflecting a maturing, multi-tier market
- **China & US** are the top EV-producing countries by volume in this dataset
- **AWD** drivetrain is strongly associated with Performance variants and higher price points
- **Autopilot Level 3** is exclusively found in Tesla vehicles in this dataset
- **Safety ratings** average around 4/5 across all brands, showing industry-wide safety maturity
- **Battery capacity** strongly correlates with range — but charging speed has become a key differentiator

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python 3.10+ | Core programming language |
| Pandas | Data loading, cleaning & manipulation |
| NumPy | Numerical operations |
| Matplotlib | Static charts and plots |
| Seaborn | Statistical visualizations |
| Plotly | Interactive visualizations |
| Jupyter Notebook | Interactive analysis environment |

---

## 📁 Project Structure

```
ev-market-analysis-2026/
│
├── data/
│   └── ev_market_2026.csv          # Raw dataset
│
├── ev_analysis.ipynb               # Jupyter Notebook (full EDA)
├── ev_analysis.py                  # Python analysis script
├── requirements.txt                # Python dependencies
└── README.md                       # Project documentation
```

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/ev-market-analysis-2026.git
cd ev-market-analysis-2026
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the analysis script
```bash
python ev_analysis.py
```

### 4. Or open the Jupyter Notebook
```bash
jupyter notebook ev_analysis.ipynb
```

---

## 📦 Requirements

```
pandas>=2.0
numpy>=1.24
matplotlib>=3.7
seaborn>=0.12
plotly>=5.15
jupyter>=1.0
```

> Save these in a `requirements.txt` file in your repo root.

---

## 📊 Analysis Sections

1. **Data Overview** — Shape, dtypes, missing values, summary statistics
2. **Brand Analysis** — Sales volume, average pricing, model count by brand
3. **Market Segmentation** — Budget vs Mid-range vs Premium vs Luxury breakdown
4. **Price Analysis** — Distribution by segment, brand, and country of origin
5. **Performance Metrics** — Range, horsepower, acceleration by brand and variant
6. **Autopilot & Technology** — Autonomy level distribution across brands
7. **Correlation Analysis** — Heatmap of numeric features
8. **Geographic Insights** — Country-wise market share and segment positioning

---

## 👤 Author

**Yash Gupta**
Business Analyst | Data Enthusiast
📧 yashguptayg9013@gmail.com
🔗 [LinkedIn](https://www.linkedin.com/in/YOUR_LINKEDIN) | [GitHub](https://github.com/YOUR_USERNAME)

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

*Dataset covers EV models from model years 2020–2026 across global markets.*
