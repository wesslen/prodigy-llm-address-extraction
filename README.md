<!-- SPACY PROJECT: AUTO-GENERATED DOCS START (do not remove) -->

# 🪐 spaCy Project: Prodigy Address Extraction model bootstrapped with LLM's

This project creates an address extraction model. To improve annotation efficiency,
we'll experiment with using LLM's to speed up the development process.


## 📋 project.yml

The [`project.yml`](project.yml) defines the data assets required by the
project, as well as the available commands and workflows. For details, see the
[spaCy projects documentation](https://spacy.io/usage/projects).

### ⏯ Commands

The following commands are defined by the project. They
can be executed using [`spacy project run [name]`](https://spacy.io/api/cli#project-run).
Commands are only re-run if their inputs have changed.

| Command | Description |
| --- | --- |
| `install` | Install packages |
| `clean` | Remove intermediate files |
| `clean-venv` | Remove the virtual environment |
| `generate-data` | Create synthetic data from LLM |
| `ner-manual-train` | NER manual annotate for training from generated (synthetic) data |
| `ner-manual-eval` | NER manual annotate for evaluation from generated (synthetic) data |
| `ner-train-curve` | NER correct annotate for training from generated (synthetic) data |
| `ner-correct` | NER correct annotate for training from generated (synthetic) data |
| `data-merge` | Merge manual and correct data for training data |
| `ner-data-to-spacy` | Convert training and evaluations to spaCy binary data |
| `ner-data-debug` | Run data debug on training and evaluation data |
| `train` | Train pipeline models |
| `load-annotations` | Load training and evaluation data as Prodigy datasets |
| `train-vectors` | Train pipeline models with vectors |
| `evaluate` | Evaluate the model and export metrics |
| `package` | Package the trained model as a pip package |
| `visualize-model` | Visualize the model's output interactively using Streamlit |
| `document` | Export README for project details |

### ⏭ Workflows

The following workflows are defined by the project. They
can be executed using [`spacy project run [name]`](https://spacy.io/api/cli#project-run)
and will run the specified commands in order. Commands are only re-run if their
inputs have changed.

| Workflow | Steps |
| --- | --- |
| `all` | `install` &rarr; `load-annotations` &rarr; `ner-data-to-spacy` &rarr; `train-vectors` &rarr; `evaluate` |
| `visualize` | `package` &rarr; `visualize-model` |

### 🗂 Assets

The following assets are defined by the project. They can
be fetched by running [`spacy project assets`](https://spacy.io/api/cli#project-assets)
in the project directory.

| File | Source | Description |
| --- | --- | --- |
| [`assets/addresses.jsonl`](assets/addresses.jsonl) | Local | LLM-generated (synthetic) data |
| `assets/addresses_train.jsonl` | Local | Annotated training data from LLM-generated (synthetic) data |
| `assets/addresses_eval.jsonl` | Local | Annotated evaluation data from LLM-generated (synthetic) data |

<!-- SPACY PROJECT: AUTO-GENERATED DOCS END (do not remove) -->