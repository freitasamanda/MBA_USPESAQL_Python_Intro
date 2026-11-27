import numpy as np

def coef_var(x):
    coeficiente = (np.std(x) / np.mean(x)) * 100
    coeficiente = np.round(coeficiente, decimals=2)
    return f"O coeficiente de variação é {coeficiente}%."