"""Script that tests Relik's relation extraction and entity linking on the GraphFrames Paper: https://people.eecs.berkeley.edu/~matei/papers/2016/grades_graphframes.pdf"""

import warnings
from relik import Relik  # type: ignore
from relik.inference.data.objects import RelikOutput  # type: ignore

# Squash Relik's warnings for prettier screenshots
warnings.simplefilter("ignore")

# Load the GraphFrames' paper text
with open("data/grades_graphframes.txt") as f:
    text = f.read()

# Load the
relik = Relik.from_pretrained("sapienzanlp/relik-relation-extraction-nyt-large")

graphlet_bio = """Graphlet AI is a data engineering, data science and artificial intelligence 
consultancy specializing in knowledge graph construction, also known as property graph construction.
We build data pipelines that take raw data and feed your graph database clean data. We transform and
refine raw data on your data lake to build large networks ranging in the millions, billions or even
trillions of nodes and edges that model entire business domains to solve complex problems with global
footprints. We love big data and large networks. We use big data tools to scale data pipelines that 
go beyond traditional ETL and entity resolution using artificial intelligenecs - graph machine 
learning - to construct a high fidelity network model of your business domain that maps directly to 
solutions to your business problems. It lets you run the queries that answer problems vexing you and
driving features your customers demand. Using a modern graph database, your data science and machine
learning teams can then efficiently mine this refined graph to find solutions to your most pressing
data science problems.""".replace(
    "\n", " "
)

relik_out: RelikOutput = relik(graphlet_bio)

# Have a looksee!
relik_out.triplets
