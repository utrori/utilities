import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns  # Import Seaborn


def paired_dotplot_with_bars(data, sample_names=None, group_names=("Group 1", "Group 2"),
                             title=None, xlabel=None, ylabel=None,
                             dot_colors=None, bar_colors=None,  # Allow None for Seaborn defaults
                             bar_width=0.35, figsize=(6, 6), dot_size=50, alpha=0.7,
                             show_legend=True, jitter=0.1, errorbar='std'):
    """
    Generates a paired dot plot with bars (improved aesthetics).
    """
    num_samples = len(data)
    if sample_names is None:
        sample_names = [f"Sample {i+1}" for i in range(num_samples)]
    if len(sample_names) != num_samples:
        raise ValueError("Number of sample names must match number of samples.")
    if len(group_names) != 2:
        raise ValueError("group_names must have length 2")

    # --- Set up Seaborn styling ---
    sns.set_theme(style="whitegrid", context="notebook", font_scale=1.2,
                  font="Arial") # Use Arial

    fig, ax = plt.subplots(figsize=figsize)

    # --- Use Seaborn color palettes if custom colors are not provided ---
    if dot_colors is None:
        dot_colors = sns.color_palette("deep")[:2]  # Get first two colors
    if bar_colors is None:
        bar_colors = sns.color_palette("pastel")[:2]


    for i, sample in enumerate(data):
        if len(sample) != 2:
            raise ValueError("Each sample must contain exactly two groups.")

        group1_data = sample[0]
        group2_data = sample[1]

        mean1 = np.mean(group1_data)
        mean2 = np.mean(group2_data)
        if errorbar == 'std':
            error1 = np.std(group1_data)
            error2 = np.std(group2_data)
            error_label = 'Stdev'
        elif errorbar == 'sem':
            error1 = np.std(group1_data) / np.sqrt(len(group1_data))
            error2 = np.std(group2_data) / np.sqrt(len(group2_data))
            error_label = 'SEM'
        else:
            raise ValueError("errorbar must be 'std' or 'sem'")

        # Dot Plot
        x_coords1 = np.ones(len(group1_data)) * (i + 1 - bar_width/2) + np.random.uniform(-jitter, jitter, len(group1_data))
        x_coords2 = np.ones(len(group2_data)) * (i + 1 + bar_width/2) + np.random.uniform(-jitter, jitter, len(group2_data))
        ax.scatter(x_coords1, group1_data, c=[dot_colors[0]], s=dot_size, alpha=alpha, zorder=2, label=f'{group_names[0]} Data' if i == 0 and show_legend else "")  # Use a list for color
        ax.scatter(x_coords2, group2_data, c=[dot_colors[1]], s=dot_size, alpha=alpha, zorder=2, label=f'{group_names[1]} Data' if i == 0 and show_legend else "")  # Use a list for color


        # Bar Plot (Outlines Only)
        bar_pos1 = i + 1 - bar_width / 2
        bar_pos2 = i + 1 + bar_width / 2
        ax.bar(bar_pos1, mean1, width=bar_width, color='none', edgecolor=bar_colors[0], linewidth=2, zorder=1, label=f'{group_names[0]} Mean ± {error_label}' if i==0 and show_legend else "")
        ax.bar(bar_pos2, mean2, width=bar_width, color='none', edgecolor=bar_colors[1], linewidth=2, zorder=1, label=f'{group_names[1]} Mean ± {error_label}' if i==0 and show_legend else "")
        ax.errorbar(bar_pos1, mean1, yerr=error1, fmt='none', ecolor=bar_colors[0], capsize=5, elinewidth=2, zorder=3)
        ax.errorbar(bar_pos2, mean2, yerr=error2, fmt='none', ecolor=bar_colors[1], capsize=5, elinewidth=2, zorder=3)

    # Customize Plot
    ax.set_xticks(np.arange(1, num_samples + 1))
    ax.set_xticklabels(sample_names, rotation=45, ha="right")
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    if show_legend:
      ax.legend(loc='upper right') # place legend outside
    sns.despine(top=True, right=True)  # Remove top and right spines

    plt.tight_layout()
    return fig, ax

def main():
    # Example Usage:
    # Create sample data for paired comparisons
    sample1_group1 = np.random.normal(5, 1, 50)
    sample1_group2 = np.random.normal(6, 1.2, 50)
    sample2_group1 = np.random.normal(7, 1.5, 60)
    sample2_group2 = np.random.normal(7.5, 1.6, 60)
    sample3_group1 = np.random.normal(4, 0.8, 40)
    sample3_group2 = np.random.normal(3.5, 0.7, 40)

    data = [
        [sample1_group1, sample1_group2],
        [sample2_group1, sample2_group2],
        [sample3_group1, sample3_group2],
    ]

    sample_names = ["Sample 1", "Sample 2", "Sample 3"]
    group_names = ("Control", "Treatment")

    fig, ax = paired_dotplot_with_bars(
        data,
        sample_names=sample_names,
        group_names=group_names,
        title="Paired Dot Plot with Mean and Standard Deviation",
        xlabel="Sample",
        ylabel="Measurement",
        #dot_colors=("dimgray", "darkgray"),  # Optional: Use custom colors
        #bar_colors=("tomato", "lightcoral"),  # Optional: Use custom colors
        show_legend=True,
        errorbar='sem',
        jitter=0.15,  # Reduced jitter
        dot_size=40,   # Smaller dots
        alpha=0.6,
        figsize=(8,6)
    )

    plt.show()
    # Save the figure in high resolution
    #fig.savefig("paired_dotplot_publication.png", dpi=300)
    #fig.savefig("paired_dotplot_publication.pdf") # Or save as PDF (vector format)

if __name__ == "__main__":
    main()