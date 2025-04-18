#Run on command prompt (cmd): pip install graphviz
#Download from website: https://graphviz.org/download/
#https://gitlab.com/api/v4/projects/4207231/packages/generic/graphviz-releases/12.2.1/windows_10_cmake_Release_graphviz-install-12.2.1-win64.exe
#ensure the PATH is set for you or all in the computer
#restart python service


from graphviz import Digraph

# Create a new directed graph
dot = Digraph(comment='Causal DAG for RAS Intervention', format='png')

# Add nodes
dot.node('I', 'Intervention\n(UFC Subcommittee & SAB)')
dot.node('FI', 'Faculty Input\nin SOPs')
dot.node('CQ', 'Communication\nQuality')
dot.node('FS', 'Faculty\nSatisfaction')
dot.node('AB', 'Administrative\nBurden')
dot.node('FRA', 'Financial Report\nAccuracy')
dot.node('FE', 'Faculty\nExperience Level')
dot.node('RUM', 'RAS Unit\nMaturity')

# Add edges (causal relationships) as tuples
edges = [
    ('I', 'FI'), ('I', 'CQ'), 
    ('FI', 'AB'), ('FI', 'FRA'), 
    ('CQ', 'FS'), ('AB', 'FS'), ('FRA', 'FS'),
    ('FE', 'I'), ('FE', 'FS'), 
    ('RUM', 'I'), ('RUM', 'FS')
]
dot.edges(edges)

# Save and render the graph
dot.render('causal_dag_ras_intervention', view=True)
