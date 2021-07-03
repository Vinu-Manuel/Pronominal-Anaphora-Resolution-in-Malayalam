# Pronominal-Anaphora-Resolution-in-Malayalam

The pronominal anaphora resolution system is created by using Python language. Developed for resolving anaphora references in Malayalam language. The system selects a suitable candidate from the list of possible antecedent candidates for pronominal anaphora. The antecedent candidates taken into consideration mainly consists of proper nouns. The system uses the case of the entities as the main constraint to resolve the anaphora references. Due to the free word order of the Malayalam language, the system also resolves some cataphora resolution.

The system uses the morphological analyzer <b> mlmorph created </b> by  <b> Santhosh Thottingal </b>. The morphological analyzer can be installed using the command:
pip install mlmorph

Citation for mlmorph:

<pre>
@inproceedings{thottingal-2019-finite,
    title = "Finite State Transducer based Morphology analysis for {M}alayalam Language",
    author = "Thottingal, Santhosh",
    booktitle = "Proceedings of the 2nd Workshop on Technologies for MT of Low Resource Languages",
    month = "20 " # aug,
    year = "2019",
    address = "Dublin, Ireland",
    publisher = "European Association for Machine Translation",
    url = "https://www.aclweb.org/anthology/W19-6801",
    pages = "1--5",
}
</pre>
