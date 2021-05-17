# Named entity recognition for Icelandic
This repository hosts code and models for the named entity recognition (NER) work performed at Reykjavik University in 2019-2020.

The models presented here have been trained on the Icelandic [MIM-GOLD-NER named entity corpus](http://www.malfong.is/index.php?lang=en&pg=mim_gold_ner), annotated as part of this work.

Implemented here are three different NER models, and an voting system combining the output of the three models. An evaluation script outputs the F1 score of each of the three models, given a CoNLL file with correct NE labels.

The methods used for training are the following:
* A Conditional Random Fields NER model – implementation based on [Passos et al 2014](https://www.aclweb.org/anthology/W14-1609.pdf)
* Ixa-pipes-ner, a perceptron model with shallow word features and externally trained word clusters – [Agerri & Rigau 2017](https://arxiv.org/pdf/1701.09123.pdf)
* NeuroNER, a Bi-LSTM RNN with pre-trained word embeddings (GloVe) – [Dernoncourt et al. 2017](https://arxiv.org/pdf/1705.05487.pdf)
* CombiTagger, an ensemble voting system – [Henrich et al. 2009](https://www.ru.is/faculty/hrafn/papers/ctagger.pdf)


<!-- # Table of Contents
[Easy to use TOC generator](https://ecotrust-canada.github.io/markdown-toc/) -->
 
# Installation
* Clone this repo:
    ```
    $ git clone https://github.com/cadia-lvl/NER
    $ cd NER
    ```
* Install sklearn-crfsuite with pip
* Install [TensorFlow](https://www.tensorflow.org/install/pip) version 1.14 for Python 3.
* Install NeuroNER according to the installation guide on https://github.com/Franck-Dernoncourt/NeuroNER
* Install https://github.com/ixa-ehu/ixa-pipe-nerc anywhere according to their guide. Create a softlink called nerc in [ixa-pipe](ixa-pipe):
    ```bash
    $ ln -s /path/to/ixa-pipe-nerc ixa-pipe/nerc    
    ```

* Install https://github.com/hrafnl/CombiTagger anywhere according to their guide, create a softlink (symbolic link) to this directory at the root:
    ```bash
   $ ln -s /path/to/CombiTagger CombiTagger
    ```
* Download the trained ixa-pipe and CRF models, along with the gazetteers from [here](https://drive.google.com/file/d/1Z6mefl2JEX-wwIAe5gBsQ_bZuj4PdDiU/view?usp=sharing). Extract anywhere, and edit the paths in the [config.ini](config.ini) file accordingly. 
* Download the [word embeddings](https://drive.google.com/file/d/12jteoqu-D4u-ogm254wGDpLPQRXQWZ4v/view?usp=sharing) and [the trained model](https://drive.google.com/file/d/1t-C7LuwHDsZ08uNx2vzq2oEnpM4k2-E1/view?usp=sharing) for NeuroNER, extract anywhere, and update token_pretrained_embedding_filepath and pretrained_model_folder in the [parameters.ini](parameters.ini) file accordingly.
<!--* get the Icelandic (MIM-GOLD)[http://www.malfong.is/index.php?lang=en&pg=gull] corpus-->
<!--* dependencies
It is also helpful to provide commands which assist user installing the program or even providing an `install.sh` script which does it for the user. -->

# Running
The evaluation script run_combined_system.sh shows the evaluation of the output of the three models and CombiTagger. It takes a .tsv file on the CoNLL format (with gold labels) as an argument.

<!--  ## API reference (Optional)
If lengthy, this should be a separate document placed as HTML into the `docs/` folder. For more inforation see `documentation` -->

# License
This project is licensed under the Apache License 2.0 - see the (LICENSE)[https://github.com/cadia-lvl/NER/blob/master/LICENSE] file for details.

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

<!-- ## Description of folder structure (Optional) -->

<!--  # Changelog/Versions (Optional) -->

<!-- # Papers/References (Optional)
You would have a citation snippet here as a code block -->
