import matplotlib.pyplot as plt

def generate_flowchart(text):
    steps = [s.strip() for s in text.split('.') if s.strip()]
    fig, ax = plt.subplots(figsize=(6, len(steps) * 0.8))
    for i, step in enumerate(steps):
        ax.text(0.5, 1 - i * 0.12, f"{i+1}. {step}", ha='center', bbox=dict(facecolor='lightblue'))
    ax.axis('off')
    plt.savefig("flowchart.png")
