# Biaoge
## Introduction
Biaoge is a python tool to help researchers to record their data during their experiment. It is based on pandas but it's quite simplified. It can export data to markdown format which can be easily converted into other format.

## Usage
``` python
import Biaoge
bg = Biaoge.Biaoge()
bg.setDesc("Table 1", This is data for experiment 1.)
bg.set("Table 1", "row1", "col1", 0.2)
bg.set("Table 1", "row2", "col2", 0.9)
result = bg.getMarkdown()
print result
```
## Result
Raw Markdown
```
## Table 1
This is data for experiment 1.
|    |col1|col2|
|--- |--- |--- |
|row1|0.2 | -  |
|row2| -  |0.9 |
```
Converted
#### Table 1
This is data for experiment 1.

|    |col1|col2|
|--- |--- |--- |
|row1|0.2 | -  |
|row2| -  |0.9 |
