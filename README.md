# Named entity recognition for Icelandic
This repository hosts code and models for the named entity recognition (NER) work performed at Reykjavik University in 2019-2020.

The models presented here have been trained on the Icelandic [MIM-GOLD-NER named entity corpus](http://www.malfong.is/index.php?lang=en&pg=mim_gold_ner), annotated as part of this work.

Implemented here are three different NER models, and an voting system combining the output of the three models. The methods used for training are the following:
* A Conditional Random Fields NER model – [Passos et al 2014](https://www.aclweb.org/anthology/W14-1609.pdf)
* Ixa-pipes-ner, a perceptron model with shallow word features and externally trained word clusters – [Agerri & Rigau 2017](https://arxiv.org/pdf/1701.09123.pdf)
* NeuroNER, a Bi-LSTM RNN with pre-trained word embeddings (GloVe) – [Dernoncourt et al.](https://arxiv.org/pdf/1705.05487.pdf)
* CombiTagger, an ensemble voting system – [Henrich et al.](https://www.ru.is/faculty/hrafn/papers/ctagger.pdf)


<!-- # Table of Contents
[Easy to use TOC generator](https://ecotrust-canada.github.io/markdown-toc/) -->
 
# Installation
* software requirements
* dependencies
It is also helpful to provide commands which assist user installing the program or even providing an `install.sh` script which does it for the user.

# Running
How to run the program/application/model and common use-cases and outputs.
For the program to be easily usable this section can be quite long.

<!--  ## API reference (Optional)
If lengthy, this should be a separate document placed as HTML into the `docs/` folder. For more inforation see `documentation` -->

# License
Mention which LICENSE the code uses. For more information about licensing see later.

# Authors/Credit
Reykjavik University
* Ásmundur Alma Guðjónsson <asmundur10@ru.is>
* Svanhvít Lilja Ingólfsdóttir <svanhviti16@ru.is>
* Hrafn Loftsson, Associate Professor <hrafn@ru.is>

## Acknowledgements
This project was funded by the with funding from the [Icelandic Strategic Research and Development Programme for Language Technology](https://www.rannis.is/sjodir/rannsoknir/markaaetlun-i-tungu-og-taekni/) 2019, grant no. 180027-5301.

<!-- # Contribution guidelines (Optional)
Explain how people can contribute to this repository. This can also link to a separate Developer reference
* how to contribute
* creating issues
* where to get data
* testing -->

## Description of folder structure (Optional)

<!--  # Changelog/Versions (Optional) -->

# Papers/References (Optional)
You would have a citation snippet here as a code block
