import matplotlib.pyplot as plt
import textwrap

# Define tasks, start months, and durations
tasks = [
    "Complete courses in statistics and Python",
    "Attend local Data Science meetup",
    "Reach out to 2 mentors",
    "Lead Data Science initiative",
    "Attend NeurIPS conference",
    "Apply for AWS ML certification",
    "Update LinkedIn/Resume",
    "Conduct informational interviews",
    "Apply to 10 VP/Director roles",
    "Prepare for interviews",
    "Negotiate offers",
    "Onboard into new role"
]

start_months = [1, 1, 3, 4, 6, 5, 7, 7, 10, 13, 14, 17]
durations = [2, 1, 1, 2, 1, 2, 1, 3, 3, 1, 3, 2]

## Create figure and axis
#fig, ax = plt.subplots(figsize=(10, 6))
# Wrap task names if longer than 30 characters
wrapped_tasks = ["\\n".join(textwrap.wrap(task, 20)) for task in tasks]
print (wrapped_tasks)

# Create figure and axis with increased height for multiline labels
fig, ax = plt.subplots(figsize=(10, 8))

# Plot horizontal bars for each task
ax.barh(tasks, durations, left=start_months, color='skyblue')

# Set labels and title
ax.set_xlabel('Months')
ax.set_title('18-Month Project Timeline Gantt Chart')

# Set x-axis ticks to show each month
ax.set_xticks(range(1, 19))

# Set y-limit to include space for phase labels
ax.set_ylim(-0.5, len(tasks) + 0.5)

# Define phase labels and milestones
phase_labels = ["Phase 1", "Phase 2", "Phase 3", "Phase 4"]
milestones = [3, 6, 12, 18]

# Add vertical lines and text for each phase end
for m, label in zip(milestones, phase_labels):
    ax.axvline(x=m, color='red', linestyle='--')
    ax.text(m, len(tasks) + 0.2, label, ha='center', va='bottom', color='red', fontsize=10, fontweight='bold')
    
#for m in milestones:
        #ax.axvline(x=m, color='red', linestyle='--', label='Milestone' if m == 3 else "")

# Add an upward arrow to demonstrate progress
##current_month = 1  # Assuming Month 1 as of April 07, 2025; adjust as needed
##ax.annotate('Progress', 
##            xy=(current_month, len(tasks) - 1),  # Arrow tip at top task
##            xytext=(current_month, -0.5),        # Arrow base at bottom
##            arrowprops=dict(facecolor='green', shrink=0.05, width=2, headwidth=8),
##            ha='center', va='bottom', color='green', fontsize=10, fontweight='bold')


# Adjust layout and save the chart
plt.tight_layout()
#plt.savefig('gantt_chart_with_phases.png')
plt.show()
