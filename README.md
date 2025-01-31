# Three New Information Extraction (IE) Models Compared

This is the source code for the blog post, "Three New Information Extraction (IE) Models Compared", available at <https://blog.graphlet.ai>

## Introduction

In this blog post, we will compare three new information extraction (IE) models:

1. ReLiK ([paper](https://arxiv.org/abs/2501.03172)) ([github](https://github.com/SapienzaNLP/relik)) ([model](https://huggingface.co/sapienzanlp/relik-entity-linking-base)) ([langchain](https://python.langchain.com/api_reference/experimental/graph_transformers/langchain_experimental.graph_transformers.relik.RelikGraphTransformer.html)) - Retrieve, Read and LinK: Fast and Accurate Entity Linking and Relation Extraction on an Academic Budget
2. GLiREL ([paper](https://arxiv.org/abs/2501.03172)) ([github](https://github.com/jackboyla/GLiREL)) ([model](https://huggingface.co/jackboyla/glirel-large-v0)) ([langchain](https://python.langchain.com/api_reference/experimental/graph_transformers/langchain_experimental.graph_transformers.gliner.GlinerGraphTransformer.html)) - Generalist and Lightweight model for Zero-Shot Relation Extraction
3. NuExtract (no code) ([model](https://huggingface.co/numind/NuExtract)) ([blog](https://numind.ai/blog/nuextract-a-foundation-model-for-structured-extraction)) - a lightweight text-to-JSON LLM. NuExtract allows to extract arbitrarily complex information from text and turns it into structured data.

## Pre-Requisites

To run the code in this repository, you need to have the following software installed.

- Docker - you can [install docker](https://docs.docker.com/engine/install/) and then check the [Get Started](https://www.docker.com/get-started/) page if you aren't familiar.

OR

- Python 3 - you can download Anaconda Python here: [https://www.anaconda.com/download](https://www.anaconda.com/download)

Supported operating systems:

- Mac OS X
- Ubuntu Linux
- Other Linux will work, but you may need to adjust the instructions for Fedora, CentOS, etc.

Windows is not supported. I'd appreciate Windows support as a contribution!

## Running the Code with Jupyter on Docker

You can run Jupyter in Docker with the following command:

```bash
docker compose up -d
```

Note: _I have disabled tokens and passwords as this is a test environment. You should not do this in production._

Now open your browser and go to [http://localhost:8888/lab](http://127.0.0.1:8888/lab) to access Jupyter.

To shut down the Docker container, run:

```bash
docker compose down
```

## Development Environment Setup

If you're building software and want to experiment and explore this code and its dependencies, you can load the code in Visual Studio Code or another editor.

### Python Virtual Environment

We use a Python virtual environment to run the code in this repository in a local environment. This will help you avoid conflicts with other Python projects you may have on your system.

#### Anaconda Python

If you are using Anaconda Python, create a new conda environment named `iecompare` using the following command:

```bash
conda create -n iecompare python=3.11 -y
```

Then activate the environment:

```bash
conda activate iecompare
```

To deactivate the environment:

```bash
conda deactivate
```

#### Other Python

You can use a Python venv environment to run the code in this repository. To create a new virtual environment named `iecompare`, use the following command:

```bash
python3 -m venv iecompare
```

Then activate the environment:

```bash
source iecompare/bin/activate
```

## Installing Python Dependencies

The project uses [Python Poetry](https://python-poetry.org/) for package management. Try it - you'll forget the headaches common to `pip` and `requirements.txt` files.

### Install Poetry

To install Poetry (see [install docs](https://python-poetry.org/docs/)), you can use [pipx](https://github.com/pypa/pipx) or `curl` a script.

#### Install Poetry Using `curl`

To install using `curl`, just run:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

#### Install Poetry using `pipx`

To first install `pipx`, on Mac OS X run:

```bash
brew install pipx
pipx ensurepath
sudo pipx ensurepath --global # optional to allow pipx actions with --global argument
```

On Ubuntu Linux, run:

```bash
sudo apt update
sudo apt install pipx
pipx ensurepath
sudo pipx ensurepath --global # optional to allow pipx actions with --global argument
```

Then install Poetry using `pipx`:

```bash
pipx install poetry
```

It will now be outside your virtual environment and available to all your Python projects.

### Install Dependencies

Now we can use `poetry` to install our Python dependencies. Run the following command:

```bash
poetry install
```

And our setup is complete!
