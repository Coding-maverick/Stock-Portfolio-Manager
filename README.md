# Stock Portfolio Management System

A stock portfolio management and analysis system built from scratch to explore how stocks can be searched, evaluated, tracked, and managed using real-world market data and automated analysis.

## Overview

My interest in the stock market started without any prior knowledge of investing or financial markets. Rather than simply learning the concepts theoretically, I decided to understand the process by building something myself.

That exploration eventually led to the development of this **Stock Portfolio Management System**.

The project started as a way to understand stock-market fundamentals and gradually evolved into a system capable of:

* Searching and identifying stocks
* Retrieving current market data
* Managing portfolios
* Maintaining watchlists
* Performing fundamental analysis
* Evaluating stocks using multiple weighted parameters
* Generating investment insights
* Analyzing an overall portfolio
* Exporting portfolio and watchlist data to Excel
* Using LLMs to assist with stock analysis and interpretation

The project is still actively being developed, with the next major focus being a proper graphical interface and dashboard.

---

## Key Features

### 1. Stock Search by Company Name

Users do not need to remember stock tickers.

Instead of entering a ticker such as:

```text
TATAMOTORS
```

a user can simply search:

```text
Tata
```

The system searches its stock database and returns relevant companies along with their corresponding tickers.

This makes stock discovery more intuitive, particularly for users who are unfamiliar with ticker symbols.

---

### 2. Automatic Ticker Identification

Once the user selects a company from the search results, the system automatically identifies the corresponding ticker.

This creates a simple workflow:

```text
Company Name
      ↓
Stock Database Search
      ↓
Matching Companies
      ↓
User Selection
      ↓
Ticker Identification
```

This separates the user-facing company identification process from the underlying market-data APIs that generally require ticker symbols.

---

### 3. Current Market Data

The system retrieves current/latest available market information for selected stocks.

This provides the underlying data required for portfolio tracking and stock evaluation.

The market-data layer is designed to keep data retrieval separate from the analysis and portfolio-management logic.

---

### 4. Portfolio Management

Users can maintain and track their stock holdings.

The portfolio system is designed to keep track of relevant information associated with holdings and provide an overall view of the portfolio.

Portfolio data can also be exported to **Excel** for:

* Offline analysis
* Record keeping
* Future reference
* Sharing
* Additional spreadsheet-based analysis

---

### 5. Watchlist

Users can maintain a separate watchlist for stocks they are interested in but do not currently own.

The watchlist allows potential investments to be tracked without adding them to the actual portfolio.

Watchlist data can also be exported to Excel.

```text
Portfolio
   ├── Current Holdings
   └── Portfolio Analysis

Watchlist
   ├── Stocks Being Monitored
   └── Watchlist Export
```

---

### 6. Buy / Hold Decision Support

The system provides decision-support insights based on the available stock data and evaluation framework.

Rather than simply returning a numerical score, the system attempts to explain **why** a stock receives its particular evaluation.

The objective is to make the analysis interpretable rather than treating the final recommendation as a black box.

> The output is intended as decision support and not as financial advice.

---

### 7. Fundamental Stock Analysis

The system evaluates stocks using fundamental financial and business characteristics.

The analysis considers factors such as:

* Business quality
* Management
* Financial strength
* Earnings growth
* Valuation
* Risk
* Future relevance

These factors are combined into a broader evaluation of the company's overall position.

---

## 8. Weighted 10-Parameter Evaluation System

One of the core components of the project is a **weighted stock evaluation framework**.

Instead of evaluating a company based on a single metric, the system considers multiple parameters and assigns appropriate weights to them.

The general concept is:

```text
Parameter 1 ──┐
Parameter 2 ──┤
Parameter 3 ──┤
Parameter 4 ──┤
Parameter 5 ──┼──> Weighted Evaluation ──> Overall Score
Parameter 6 ──┤
Parameter 7 ──┤
Parameter 8 ──┤
Parameter 9 ──┤
Parameter 10 ─┘
```

The evaluation considers dimensions including:

| Category           | What it attempts to evaluate                    |
| ------------------ | ----------------------------------------------- |
| Business Quality   | Strength and quality of the underlying business |
| Management         | Management quality and execution                |
| Financial Strength | Balance-sheet and financial health              |
| Earnings Growth    | Growth and consistency of earnings              |
| Valuation          | Whether the stock appears reasonably valued     |
| Risk               | Key business and financial risks                |
| Future Relevance   | Long-term relevance and growth potential        |

The remaining parameters complement these broader categories to produce a more comprehensive evaluation.

### Explainable Scoring

A major objective of the system is **explainability**.

Instead of producing:

```text
Score: 78/100
```

the system attempts to provide:

```text
Overall Score: 78/100

Business Quality:       16/20
Financial Strength:     15/20
Earnings Growth:        14/15
Valuation:              11/15
Management:             10/10
Risk:                    6/10
...
```

along with an explanation of the factors contributing to each score.

This makes the evaluation easier to inspect and challenge rather than blindly accepting the final number.

---

## 9. Portfolio-Level Analysis

The project is not limited to analyzing individual stocks.

The system can also evaluate the **overall portfolio**.

The objective is to move from:

```text
"Is this stock good?"
```

towards:

```text
"How does this collection of stocks perform as a portfolio?"
```

Portfolio analysis can consider factors such as:

* Overall portfolio quality
* Individual holding scores
* Distribution of holdings
* Concentration
* Risk characteristics
* Strengths and weaknesses across holdings

This provides a higher-level perspective beyond evaluating individual companies independently.

---

## 10. LLM Integration

One of the most valuable parts of this project has been integrating an **LLM into the analysis workflow**.

The LLM is not intended to replace the underlying financial calculations.

Instead, it can be used to help transform structured financial information into more understandable insights.

This distinction is important.

The numerical evaluation should be based on defined rules, calculations, and financial data, while the LLM can help explain those results in natural language.

Working on this integration has also exposed several gaps in my understanding of LLM-based systems and given me a much clearer direction for what I need to learn next.

---

# UI / UX

The biggest area for improvement at the moment is the user interface.

The current implementation focuses primarily on getting the underlying functionality working correctly rather than providing a polished visual experience.

At present, the system is largely terminal-based.

While this works functionally, the presentation is not yet where I want it to be.

The next stage of development is therefore focused on building a cleaner interface with the goal of eventually turning the project into an intuitive **stock analysis and portfolio dashboard**.

---

# What I Learned

This project has been as much about learning as it has been about building.

Building the system from scratch helped me understand how different components of a larger application interact with one another.

Some of the major areas I worked with include:

* API integration
* Market-data retrieval
* Data processing
* Database/search logic
* Portfolio management
* Financial analysis
* Weighted scoring systems
* Excel data export
* LLM integration
* Backend architecture
* Designing systems around real-world data

More importantly, the project exposed several gaps in my existing knowledge.

That has been one of the most useful outcomes of the project.

Instead of simply learning technologies in isolation, I now have a much clearer understanding of **why certain technologies and concepts are necessary** and which areas I need to strengthen next.

# Disclaimer

This project is intended for **educational and informational purposes only**.

I am **not a SEBI-registered financial advisor**, and this tool does not provide professional financial or investment advice.

The scores, analysis, insights, and Buy/Hold decision-support outputs generated by this system should **not** be treated as recommendations to buy, sell, or hold any security.

Users are solely responsible for conducting their own research, evaluating the underlying data, understanding the associated risks, and making their own informed and conscious investment decisions.

Past performance and model-based evaluations do not guarantee future results.


## Feedback

This project is still evolving, and I would genuinely appreciate feedback, suggestions, and technical criticism.

If you have ideas for improving the architecture, analysis methodology, UI/UX, or overall system, feel free to open an issue or start a discussion.

**Built from curiosity, developed through experimentation, and still evolving.**
