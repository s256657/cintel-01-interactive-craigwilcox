import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from shiny.express import ui, input, render


# Add page options
ui.page_opts(title="PyShiny Practice plots")

sns.set_theme(style="dark")

with ui.sidebar():
    ui.input_slider("selected_number_of_bins", "Number of Bins", 0, 100, 20)


@render.plot(alt="A histogram")
def histogram():
    np.random.seed(19680801)
    x = 100 + 15 * np.random.randn(437)
    plt.hist(x, input.selected_number_of_bins(), density=True)

    # Seaborn histogram instead of plt.hist
    sns.histplot(x, bins=input.selected_number_of_bins(), stat="density", kde=False)
    
    plt.title("Histogram using Seaborn")
    plt.xlabel("Value")
    plt.ylabel("Density")

