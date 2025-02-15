import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def dotplot_with_bars(data, sample_names=None, title=None, xlabel=None, ylabel=None,
                      dot_color=None, bar_color=None, bar_width=0.5,
                      figsize=(6, 6), dot_size=50, alpha=0.7, show_legend=False,
                      jitter=0.2, errorbar='std'):
    """
    Generates a dot plot with bars representing the mean and error bars (std or sem).
    Improved aesthetics using Seaborn.

    Args:
        data (list of lists/arrays):  Data for each sample.
        sample_names (list of str, optional):  Labels for each sample.
        title (str, optional): Plot title.
        xlabel (str, optional): X-axis label.
        ylabel (str, optional): Y-axis label.
        dot_color (str or color spec, optional): Dot color.  Defaults to Seaborn palette.
        bar_color (str or color spec, optional): Bar color. Defaults to Seaborn palette.
        bar_width (float, optional): Bar width.
        figsize (tuple, optional): Figure size (width, height).
        dot_size (float, optional): Dot size.
        alpha (float, optional): Dot transparency.
        show_legend (bool, optional): Show legend.
        jitter (float, optional): Horizontal jitter for dots.
        errorbar (str, optional): 'std' (standard deviation) or 'sem' (standard error).

    Returns:
        matplotlib.figure.Figure: The Figure object.
        matplotlib.axes.Axes: The Axes object.
    """

    num_samples = len(data)
    if sample_names is None:
        sample_names = [f"Sample {i+1}" for i in range(num_samples)]
    elif len(sample_names) != num_samples:
        raise ValueError("Number of sample names must match the number of samples.")

    # --- Set up Seaborn styling ---
    sns.set_theme(style="whitegrid", context="notebook", font_scale=1.2, font="Arial")

    fig, ax = plt.subplots(figsize=figsize)

    # --- Use Seaborn color palettes if custom colors are not provided ---
    if dot_color is None:
        dot_color = sns.color_palette("deep")[0]  # Get the first color
    if bar_color is None:
        bar_color = sns.color_palette("pastel")[0]  # Get the first color


    # Calculate means and error values for each sample
    means = [np.mean(sample) for sample in data]
    if errorbar == 'std':
        errors = [np.std(sample) for sample in data]
        error_label = 'Stdev'
    elif errorbar == 'sem':
        errors = [np.std(sample) / np.sqrt(len(sample)) for sample in data]
        error_label = 'SEM'
    else:
        raise ValueError("errorbar must be 'std' or 'sem'")

    # Plot individual data points with jitter
    for i, sample in enumerate(data):
        x_coords = np.ones(len(sample)) * (i + 1) + np.random.uniform(-jitter, jitter, len(sample))
        ax.scatter(x_coords, sample, c=[dot_color], s=dot_size, alpha=alpha, zorder=2, label='Data Points' if i == 0 and show_legend else "") # Use a list

    # Plot mean bars with error bars
    bar_positions = np.arange(1, num_samples + 1)
    ax.bar(bar_positions, means, width=bar_width, color='none', edgecolor=bar_color, linewidth=2, zorder=1, label=f'Mean ± {error_label}' if show_legend else "")
    ax.errorbar(bar_positions, means, yerr=errors, fmt='none', ecolor=bar_color, capsize=5, elinewidth=2, zorder=3)

    # Customize the plot
    ax.set_xticks(bar_positions)
    ax.set_xticklabels(sample_names, rotation=45, ha="right")
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    if show_legend:
        ax.legend(loc='upper right') # Show and set location

    sns.despine(top=True, right=True)

    plt.tight_layout()

    return fig, ax


def main():
    # Example Usage
    # Create some sample data
    sample1 = np.random.normal(5, 1, 50)
    sample2 = np.random.normal(7, 1.5, 60)
    sample3 = np.random.normal(4, 0.8, 40)
    sample4 = np.random.normal(6, 1.2, 70)
    data = [sample1, sample2, sample3, sample4]

    # Create the dot plot
    fig, ax = dotplot_with_bars(
        data,
        sample_names=["Control", "Treatment 1", "Treatment 2", "Treatment 3"],
        title="Dot Plot with Mean and Standard Deviation",
        xlabel="Experimental Group",
        ylabel="Measurement",
        #dot_color="skyblue",   # Optional: Use custom colors
        #bar_color="darkblue",  # Optional: Use custom colors
        show_legend=True,
        errorbar = 'sem'
    )

    plt.show()

if __name__ == "__main__":
    main()