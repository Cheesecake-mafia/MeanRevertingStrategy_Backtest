# MeanRevertingStrategy_Backtest
Sure! Below is a sample `README.md` file for your backtesting project that you can upload to GitHub. Feel free to customize it with additional information or formatting as needed.

```markdown
# Bank NIFTY Backtesting Project

This repository contains a Python project for backtesting trading strategies on the Bank NIFTY index. The backtesting is performed using the `backtesting` library in Python, and various strategies are implemented and optimized to analyze their performance on historical Bank NIFTY data.

## Project Overview

The project consists of the following components:

1. `data`: Contains the historical stock data for the Bank NIFTY index fetched from Yahoo Finance using the `yfinance` library. The data is preprocessed and used for backtesting the strategies.

2. `backtesting_strategies.py`: A Python script that defines and implements different trading strategies using the `backtesting` library. The strategies include variations with and without stop-loss settings.

3. `backtest_results`: Contains the backtest results and statistics for each strategy.

## Setup

1. Install the required libraries:
   - pandas
   - numpy
   - datetime
   - pandas_ta
   - missingno
   - yfinance
   - backtesting

2. Clone the repository:
   ```
   git clone https://github.com/your-username/bank-nifty-backtesting.git
   cd bank-nifty-backtesting
   ```

3. Run the `backtesting_strategies.py` script to perform the backtesting and obtain the results.

## Backtesting Strategies

### Strategy 1: Trades

This strategy performs simple buy and sell trades based on the `Signal` column from the DataFrame. It buys when the signal is 1 (long) and sells when the signal is -1 (short). The strategy uses a fixed position size of 25 and is executed without stop-loss.

### Strategy 2: Trades_with_SL

This strategy is similar to the previous one but includes a stop-loss feature. It buys with a stop-loss set at 85% of the current price (when the signal is 1) and sells with a stop-loss set at 115% of the current price (when the signal is -1). The position size remains fixed at 25.

### Strategy 3: Trades_opt

This strategy also includes stop-loss settings but with two parameters (`buy_stop` and `sell_stop`) that can be optimized. The `backtesting` library is used to perform a grid search over these parameters to find the best combination that maximizes the Sharpe Ratio.

## Backtest Results

The backtest results for each strategy, including performance metrics, trade statistics, and visualizations, can be found in the `backtest_results` folder.

## Usage

You can use this project as a starting point to test and optimize your own trading strategies on the Bank NIFTY data. Feel free to modify the strategies, add more indicators, or customize the backtesting process according to your requirements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```

Replace "Your Name" and "your-username" in the `README.md` file with your actual name and GitHub username. Additionally, if you have a specific license for your project, make sure to replace the license information in the License section accordingly.

After creating the `README.md` file, you can commit and push it to your GitHub repository using the following commands:

```bash
git add README.md
git commit -m "Add README.md"
git push origin main
```

This will make the `README.md` file available on your GitHub repository for anyone visiting the repository to read and understand your project.

Let me know if you need further assistance or have any other questions!
