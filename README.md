# 🌱 Sustainable Meal Planning System

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Pandas](https://img.shields.io/badge/Pandas-1.5%2B-orange.svg)](https://pandas.pydata.org/)
[![NumPy](https://img.shields.io/badge/NumPy-1.21%2B-lightblue.svg)](https://numpy.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-3.5%2B-red.svg)](https://matplotlib.org/)

## 🔬 Overview

The **Sustainable Meal Planning System** is a comprehensive Python application that generates nutritionally balanced meal plans while minimizing environmental impact. It combines nutritional science and environmental sustainability metrics to help users choose meals that benefit both health and the planet.

The system evaluates over 40 food items across 5 environmental metrics (land use, greenhouse gases, acidification, eutrophication, and water consumption), while ensuring meals meet nutritional requirements.

## ✨ Features

### 🎯 Core Functionalities

* **Personalized Nutrition**: Calculates daily energy needs with Mifflin St Jeor equation.
* **Automated Meals**: Generates meal combinations systematically.
* **Environmental Analysis**: Assesses sustainability using LCA data.
* **Smart Filtering**: Filters meals based on user-defined sustainability thresholds.
* **Dual Architecture**: Functional and object-oriented implementations.

### 🌍 Environmental Impact Analysis

* Measures land use, carbon footprint, water usage, acidification, and eutrophication.
* Allows customizable sustainability thresholds.

### 📊 Data Analysis and Visualization

* Interactive histograms and comparison charts.
* Nutritional and environmental progress tracking.

### 🛠️ Utility Tools

* JSON data persistence.
* PDF report generation (ReportLab).
* Robust input validation and modular code structure.

## 🚀 Technologies

### Core Technologies

* **Python 3.8+**
* **Pandas 1.5+**
* **NumPy 1.21+**
* **Matplotlib 3.5+**

### Additional Libraries

* ReportLab, OpenPyXL, itertools.

### Data Sources

* FAO Nutritional Database.
* Environmental LCA Data (Poore & Nemecek 2018).

## 🔧 Installation

### Prerequisites

* Python 3.8+
* pip

### Quick Installation

```bash
git clone https://github.com/f2ire/environment_project.git
cd environment_project
pip install pandas numpy matplotlib reportlab openpyxl
```

Ensure required data files (`TableS1_augmented_with_FAO_data.xlsx`, `DataS2.xlsx`) are present.

## 🎮 Usage

### Quick Start

Functional version:

```bash
python main.py
```

Object-oriented version:

```bash
cd v_objet
python main.py
```

### Key Configuration Parameters

**User Profile:**

* Gender, age, weight, height, activity level.

**Environmental Thresholds:**

* Land, GHG, acidification, eutrophication, water use.

**Example:**

```python
statUser = ["M", 25, 70, 175, "moderate"]
targetCal = energyrequirement.dailyEnergyRequirement(*statUser)
thresholds = [1.0, 2.0, 15.0, 10.0, 1000.0]
```

### Interactive Features

* Automatic data saving/loading.
* Real-time nutritional validation.
* Adjustable sustainability thresholds.

## 🔬 Scientific and Technical Model

### Nutritional Modeling

* **Mifflin St Jeor equation** for BMR.
* Activity factors (sedentary to very active).

### Meal Optimization

Linear algebra for macronutrient constraints:

* Protein: 12% calories
* Carbohydrates: 66% calories
* Fat: 22% calories

Meal includes protein, carbs, fats, vegetables, fruit, and extras.

### Environmental Impact Assessment

LCA method (Poore & Nemecek, 2018) evaluates:

* Land use, GHG emissions, water stress, acidification, eutrophication.

## 🛠️ Development

### Planned Improvements

* [ ] Web & mobile applications.
* [ ] ML-powered recommendations.
* [ ] Database & API integration.
* [ ] Dietary restriction filters.
* [ ] Seasonal & economic optimizations.
* [ ] Social features & micronutrient analysis.
* [ ] Performance optimization (parallelization).
* [ ] Unit and integration tests.

## 📈 Metrics and Analysis

### Environmental Metrics

* Land use efficiency, carbon intensity, water footprint, acidification, eutrophication.

### Nutritional Metrics

* Macronutrient distribution and caloric accuracy.
* Feasibility of meal plans.

### Visualization Outputs

* Impact distributions, comparative analyses, progress tracking, statistical summaries.

### Generated Reports

* Professional PDF meal plans.
* Nutritional and environmental analyses.

## 📜 License

Licensed under the MIT License - see [LICENSE](LICENSE).

---

*Building a sustainable future, one meal at a time. 🌍*
