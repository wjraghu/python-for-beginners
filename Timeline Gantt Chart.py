import matplotlib.pyplot as plt

# Define tasks, start months, and durations
tasks = [
    "Complete courses",
    "Attend meetup",
    "Reach out to mentors",
    "Lead initiative",
    "Attend conference",
    "Apply for certification",
    "Update LinkedIn",
    "Conduct interviews",
    "Apply to roles",
    "Prepare for interviews",
    "Negotiate offers",
    "Onboard into new role"
]

start_months = [1, 1, 3, 4, 6, 5, 7, 7, 10, 13, 14, 17]
durations = [2, 1, 1, 2, 1, 2, 1, 3, 3, 1, 3, 2]

# Create figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Plot horizontal bars for each task
ax.barh(tasks, durations, left=start_months, color='skyblue')

# Set labels and title
ax.set_xlabel('Months')
ax.set_title('18-Month Project Timeline Gantt Chart')

# Set x-axis ticks to show each month
ax.set_xticks(range(1, 19))

# Add vertical lines for milestones (e.g., at months 3, 6, 12, 18)
milestones = [3, 6, 12, 18]
for m in milestones:
        ax.axvline(x=m, color='red', linestyle='--', label='Milestone' if m == 3 else "")

# Add legend for milestones
ax.legend()

# Adjust layout and display the chart
plt.tight_layout()
plt.show()
