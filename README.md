# About this project

Scripts for manipulating files in cloud storage and doing multi-lingual searches.


## Installation

Start with a new venv, then install dependencies (may need to update pip).

```
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

## Using 

Run the translation example

```
python -m translate -q "bird -fish"
```


## Mods

- Moved the translation code into its own module.

- Moved the code that gets terms from the index into a method for reusability. 

- Added a further processing step to `translate_query` that removes any excluded data from the search results. This new list is returned along with the individual `excluded`, `included` and `optional` lists.

- Include sample search terms.

- But I haven't tested the modified code with phrases or complex data.