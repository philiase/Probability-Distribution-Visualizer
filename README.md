```markdown
# Probability Distribution Visualizer

This script provides a graphical interface for visualizing probability density functions of various statistical distributions. Users can select a distribution, set its parameters, and view the resulting probability density function plot.

## Setup Instructions

1. Ensure that you have the prerequisite Python libraries installed on your local machine:

```bash
pip install streamlit numpy scipy matplotlib
```

2. Clone the repository to your local machine:

```bash
git clone https://github.com/{your-account-name}/Probability-Distribution-Visualizer.git
```

3. Navigate to the base directory of the cloned repository:

```bash
cd Probability-Distribution-Visualizer/
```

4. Start the Streamlit app:

```bash
streamlit run DistributionVisualizer.py
```

If the web server initializes successfully, you should see the following message in your terminal:

```
You can now view your Streamlit app in your browser.

Local URL: http://localhost:8501
Network URL: http://192.168.0.177:8501
```

You will also be automatically directed to the base page of your web app.

## Supported Distributions

The script supports the following probability distributions:

- Binomial
- Cauchy
- Chi-square
- Exponential
- F
- Gamma
- Geometric
- Hypergeometric
- Lognormal
- Normal
- Poisson
- Uniform
- Beta

For each distribution, you can input the required parameters and generate the corresponding probability density function plot.

## Author

This script was authored by Lebuso Philly Tsilo.
```