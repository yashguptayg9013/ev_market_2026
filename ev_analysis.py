"""
EV Market Analysis 2026
========================
Author: Yash Gupta
Description: Exploratory Data Analysis of the global EV market dataset.
             Covers pricing, performance, market segmentation, brand comparison,
             and geographic insights.

Tech Stack: Python, Pandas, NumPy, Matplotlib, Seaborn, Plotly
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns
import warnings

warnings.filterwarnings("ignore")

# ── Styling ───────────────────────────────────────────────────────────────────
sns.set_theme(style="whitegrid", palette="muted")
plt.rcParams.update({"figure.dpi": 130, "axes.titlesize": 14, "axes.labelsize": 12})

# ─────────────────────────────────────────────────────────────────────────────
# 1. LOAD DATA
# ─────────────────────────────────────────────────────────────────────────────

def load_data(filepath: str = "data/ev_market_2026.csv") -> pd.DataFrame:
    df = pd.read_csv(filepath)
    print(f"✅ Dataset loaded: {df.shape[0]:,} rows × {df.shape[1]} columns\n")
    return df


# ─────────────────────────────────────────────────────────────────────────────
# 2. DATA OVERVIEW
# ─────────────────────────────────────────────────────────────────────────────

def data_overview(df: pd.DataFrame) -> None:
    print("=" * 60)
    print("DATA OVERVIEW")
    print("=" * 60)

    print("\n📐 Shape:", df.shape)
    print("\n📋 Column Data Types:")
    print(df.dtypes)

    missing = df.isnull().sum()
    print("\n❓ Missing Values:")
    print(missing[missing > 0] if missing.any() else "  → No missing values found!")

    print("\n📊 Descriptive Statistics:")
    print(df.describe().round(2).to_string())

    print("\n🏷️  Unique Brands:", df["brand"].nunique())
    print("🚗 Unique Models:", df["model"].nunique())
    print("📅 Year Range:", df["year"].min(), "–", df["year"].max())
    print("🌍 Countries:", df["country_of_origin"].unique().tolist())
    print("📦 Market Segments:", df["market_segment"].unique().tolist())
    print()


# ─────────────────────────────────────────────────────────────────────────────
# 3. BRAND ANALYSIS
# ─────────────────────────────────────────────────────────────────────────────

def brand_analysis(df: pd.DataFrame) -> None:
    print("=" * 60)
    print("BRAND ANALYSIS")
    print("=" * 60)

    # Total annual sales by brand
    brand_sales = (
        df.groupby("brand")["annual_sales_units"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )
    print("\n🏆 Top 10 Brands by Total Annual Sales:")
    print(brand_sales.head(10).to_string(index=False))

    # Average price by brand
    brand_price = (
        df.groupby("brand")["price_usd"]
        .mean()
        .sort_values(ascending=False)
        .reset_index()
    )
    brand_price["price_usd"] = brand_price["price_usd"].round(0)
    print("\n💰 Average Price by Brand (USD):")
    print(brand_price.to_string(index=False))

    # Plotting
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))
    fig.suptitle("Brand-Level Analysis", fontsize=16, fontweight="bold")

    # Plot 1: Sales
    top_brands = brand_sales.head(10)
    sns.barplot(
        data=top_brands, y="brand", x="annual_sales_units",
        palette="Blues_d", ax=axes[0]
    )
    axes[0].set_title("Top 10 Brands by Annual Sales")
    axes[0].set_xlabel("Total Annual Sales (Units)")
    axes[0].set_ylabel("Brand")
    axes[0].xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{x/1e6:.1f}M"))

    # Plot 2: Avg Price
    sns.barplot(
        data=brand_price, y="brand", x="price_usd",
        palette="Oranges_d", ax=axes[1]
    )
    axes[1].set_title("Average Vehicle Price by Brand")
    axes[1].set_xlabel("Average Price (USD)")
    axes[1].set_ylabel("")
    axes[1].xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"${x/1000:.0f}K"))

    plt.tight_layout()
    plt.savefig("brand_analysis.png", bbox_inches="tight")
    plt.show()
    print("  → Chart saved: brand_analysis.png\n")


# ─────────────────────────────────────────────────────────────────────────────
# 4. PRICE ANALYSIS
# ─────────────────────────────────────────────────────────────────────────────

def price_analysis(df: pd.DataFrame) -> None:
    print("=" * 60)
    print("PRICE ANALYSIS")
    print("=" * 60)

    seg_order = ["Budget", "Mid-range", "Premium", "Luxury"]

    print("\n💵 Price Statistics by Market Segment:")
    seg_price = df.groupby("market_segment")["price_usd"].agg(["mean", "min", "max"]).round(0)
    seg_price.columns = ["Avg Price", "Min Price", "Max Price"]
    print(seg_price.reindex(seg_order).to_string())

    fig, axes = plt.subplots(1, 2, figsize=(16, 6))
    fig.suptitle("Price Analysis", fontsize=16, fontweight="bold")

    # Distribution
    axes[0].hist(df["price_usd"], bins=40, color="#4C72B0", edgecolor="white", alpha=0.85)
    axes[0].set_title("Price Distribution (All EVs)")
    axes[0].set_xlabel("Price (USD)")
    axes[0].set_ylabel("Count")
    axes[0].xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"${x/1000:.0f}K"))

    # Box plot by segment
    sns.boxplot(
        data=df, x="market_segment", y="price_usd",
        order=seg_order, palette="Set2", ax=axes[1]
    )
    axes[1].set_title("Price Distribution by Market Segment")
    axes[1].set_xlabel("Market Segment")
    axes[1].set_ylabel("Price (USD)")
    axes[1].yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"${x/1000:.0f}K"))

    plt.tight_layout()
    plt.savefig("price_analysis.png", bbox_inches="tight")
    plt.show()
    print("  → Chart saved: price_analysis.png\n")


# ─────────────────────────────────────────────────────────────────────────────
# 5. PERFORMANCE METRICS
# ─────────────────────────────────────────────────────────────────────────────

def performance_analysis(df: pd.DataFrame) -> None:
    print("=" * 60)
    print("PERFORMANCE ANALYSIS")
    print("=" * 60)

    print("\n⚡ Average Range & Horsepower by Brand:")
    perf = (
        df.groupby("brand")[["range_miles", "horsepower", "acceleration_0_60_mph"]]
        .mean()
        .round(1)
        .sort_values("range_miles", ascending=False)
    )
    print(perf.to_string())

    fig, axes = plt.subplots(1, 2, figsize=(16, 6))
    fig.suptitle("Performance Analysis", fontsize=16, fontweight="bold")

    # Range vs Price scatter
    axes[0].scatter(
        df["range_miles"], df["price_usd"],
        c=df["battery_capacity_kwh"], cmap="viridis",
        alpha=0.6, edgecolors="none", s=30
    )
    axes[0].set_title("Range vs Price\n(color = battery capacity)")
    axes[0].set_xlabel("Range (miles)")
    axes[0].set_ylabel("Price (USD)")
    axes[0].yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"${x/1000:.0f}K"))

    # Avg range by brand (top 10 brands by count)
    top_brands = df["brand"].value_counts().head(10).index
    avg_range = df[df["brand"].isin(top_brands)].groupby("brand")["range_miles"].mean().sort_values()
    avg_range.plot(kind="barh", ax=axes[1], color="#55A868")
    axes[1].set_title("Average Range by Brand (Top 10)")
    axes[1].set_xlabel("Average Range (miles)")
    axes[1].set_ylabel("Brand")

    plt.tight_layout()
    plt.savefig("performance_analysis.png", bbox_inches="tight")
    plt.show()
    print("  → Chart saved: performance_analysis.png\n")


# ─────────────────────────────────────────────────────────────────────────────
# 6. MARKET SEGMENTATION
# ─────────────────────────────────────────────────────────────────────────────

def segment_analysis(df: pd.DataFrame) -> None:
    print("=" * 60)
    print("MARKET SEGMENTATION")
    print("=" * 60)

    seg_order = ["Budget", "Mid-range", "Premium", "Luxury"]
    seg_counts = df["market_segment"].value_counts().reindex(seg_order)
    seg_sales = df.groupby("market_segment")["annual_sales_units"].sum().reindex(seg_order)

    print("\n📦 Listings per Segment:")
    print(seg_counts.to_string())
    print("\n📈 Total Annual Sales per Segment:")
    print(seg_sales.to_string())

    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    fig.suptitle("Market Segmentation", fontsize=16, fontweight="bold")

    colors = ["#2ecc71", "#3498db", "#9b59b6", "#e74c3c"]

    axes[0].pie(seg_counts, labels=seg_order, autopct="%1.1f%%", colors=colors, startangle=140)
    axes[0].set_title("Model Listings by Segment")

    axes[1].pie(seg_sales, labels=seg_order, autopct="%1.1f%%", colors=colors, startangle=140)
    axes[1].set_title("Annual Sales Volume by Segment")

    plt.tight_layout()
    plt.savefig("segment_analysis.png", bbox_inches="tight")
    plt.show()
    print("  → Chart saved: segment_analysis.png\n")


# ─────────────────────────────────────────────────────────────────────────────
# 7. GEOGRAPHIC INSIGHTS
# ─────────────────────────────────────────────────────────────────────────────

def geographic_analysis(df: pd.DataFrame) -> None:
    print("=" * 60)
    print("GEOGRAPHIC INSIGHTS")
    print("=" * 60)

    country_sales = (
        df.groupby("country_of_origin")["annual_sales_units"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )
    print("\n🌍 Total Annual Sales by Country:")
    print(country_sales.to_string(index=False))

    fig, axes = plt.subplots(1, 2, figsize=(16, 6))
    fig.suptitle("Geographic Insights", fontsize=16, fontweight="bold")

    sns.barplot(
        data=country_sales, x="country_of_origin", y="annual_sales_units",
        palette="coolwarm", ax=axes[0]
    )
    axes[0].set_title("Annual Sales by Country of Origin")
    axes[0].set_xlabel("Country")
    axes[0].set_ylabel("Total Annual Sales")
    axes[0].yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{x/1e6:.1f}M"))
    axes[0].tick_params(axis="x", rotation=15)

    # Segment share by country
    country_seg = df.groupby(["country_of_origin", "market_segment"])["annual_sales_units"].sum().unstack(fill_value=0)
    country_seg.plot(kind="bar", ax=axes[1], colormap="Set2", edgecolor="white")
    axes[1].set_title("Sales by Country & Segment")
    axes[1].set_xlabel("Country")
    axes[1].set_ylabel("Annual Sales")
    axes[1].tick_params(axis="x", rotation=15)
    axes[1].legend(title="Segment", bbox_to_anchor=(1.01, 1), loc="upper left")
    axes[1].yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{x/1e6:.1f}M"))

    plt.tight_layout()
    plt.savefig("geographic_analysis.png", bbox_inches="tight")
    plt.show()
    print("  → Chart saved: geographic_analysis.png\n")


# ─────────────────────────────────────────────────────────────────────────────
# 8. CORRELATION ANALYSIS
# ─────────────────────────────────────────────────────────────────────────────

def correlation_analysis(df: pd.DataFrame) -> None:
    print("=" * 60)
    print("CORRELATION ANALYSIS")
    print("=" * 60)

    numeric_cols = [
        "price_usd", "battery_capacity_kwh", "range_miles", "charging_speed_kw",
        "acceleration_0_60_mph", "horsepower", "torque_nm",
        "safety_rating", "autopilot_level", "annual_sales_units", "customer_rating"
    ]

    corr = df[numeric_cols].corr().round(2)
    print("\n📐 Correlation Matrix (top absolute correlations with price_usd):")
    print(corr["price_usd"].sort_values(ascending=False).to_string())

    plt.figure(figsize=(12, 9))
    mask = np.triu(np.ones_like(corr, dtype=bool))
    sns.heatmap(
        corr, mask=mask, annot=True, fmt=".2f",
        cmap="RdYlGn", center=0, linewidths=0.5,
        annot_kws={"size": 8}
    )
    plt.title("Feature Correlation Heatmap", fontsize=14, fontweight="bold")
    plt.tight_layout()
    plt.savefig("correlation_heatmap.png", bbox_inches="tight")
    plt.show()
    print("  → Chart saved: correlation_heatmap.png\n")


# ─────────────────────────────────────────────────────────────────────────────
# 9. AUTOPILOT & TECHNOLOGY
# ─────────────────────────────────────────────────────────────────────────────

def technology_analysis(df: pd.DataFrame) -> None:
    print("=" * 60)
    print("AUTOPILOT & TECHNOLOGY")
    print("=" * 60)

    autopilot_dist = df["autopilot_level"].value_counts().sort_index()
    print("\n🤖 Autopilot Level Distribution:")
    print(autopilot_dist.to_string())

    drive_dist = df["drive_type"].value_counts()
    print("\n🔧 Drive Type Distribution:")
    print(drive_dist.to_string())

    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    fig.suptitle("Technology Insights", fontsize=16, fontweight="bold")

    labels_ap = [f"Level {i}" for i in autopilot_dist.index]
    axes[0].bar(labels_ap, autopilot_dist.values, color=["#95a5a6", "#3498db", "#2ecc71", "#e74c3c"])
    axes[0].set_title("SAE Autopilot Level Distribution")
    axes[0].set_xlabel("Autopilot Level")
    axes[0].set_ylabel("Number of Models")

    axes[1].pie(
        drive_dist.values, labels=drive_dist.index,
        autopct="%1.1f%%", colors=["#3498db", "#e67e22", "#2ecc71"], startangle=90
    )
    axes[1].set_title("Drive Type Distribution")

    plt.tight_layout()
    plt.savefig("technology_analysis.png", bbox_inches="tight")
    plt.show()
    print("  → Chart saved: technology_analysis.png\n")


# ─────────────────────────────────────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────────────────────────────────────

def main():
    print("\n" + "=" * 60)
    print("  EV MARKET ANALYSIS 2026 — by Yash Gupta")
    print("=" * 60 + "\n")

    df = load_data("data/ev_market_2026.csv")

    data_overview(df)
    brand_analysis(df)
    price_analysis(df)
    performance_analysis(df)
    segment_analysis(df)
    geographic_analysis(df)
    correlation_analysis(df)
    technology_analysis(df)

    print("\n✅ Analysis complete! All charts saved to the current directory.")


if __name__ == "__main__":
    main()
