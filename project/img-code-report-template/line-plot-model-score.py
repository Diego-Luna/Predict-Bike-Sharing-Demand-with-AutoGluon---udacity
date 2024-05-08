import matplotlib.pyplot as plt

# Define the model names and their corresponding scores
models = ['initial', 'add_features', 'hpo']
scores = [-50.108046, -27.927221, -34.629788]

# Plot the line plot
plt.figure(figsize=(10, 6))
plt.plot(models, scores, marker='o', linestyle='-')
plt.title('Top Model Score for Different Training Runs')
plt.xlabel('Training Runs')
plt.ylabel('Top Model Score')
plt.grid(True)
plt.tight_layout()

# Annotate the points with their respective scores
for i, score in enumerate(scores):
    plt.annotate(f'{score:.5f}', (models[i], scores[i]), textcoords="offset points", xytext=(0,10), ha='center')

plt.savefig('top_model_scores.png')

