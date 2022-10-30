# Pan_Bacterial_Research_Panel

- Healthcare Acquired infections (HAIs) are one of the largest causes of mortality.

- The Ion AmpliSeq Pan-Bacterial Research Panel is a quick, accurate and cost-effective tool to detect bacterial organisms at genus and species level and detect with 31 different antibiotic classes.

- The panel contains 2 pools:
	- the first containing **`269 amplicons to detect 21 specific species`** and 716 amplicons to assess the presence of 364 antibiotic resistance (AMR) genes.
	- the second containing 24 amplicons for 16S profiling of up to approximately 400,000 16S sequences in public Greengenes database.
	- AMR content has been developed in Collaboration with Lawrence Livermore National Laboratories.

- To analyze the sequencing output from this panel, a Torrent Suite plugin under the name “PanBacterialAnalysis” is available on the ThermoFisher Scientific Plugin store.


* panBacterial_ID_Genes_Designed.bed
* panBacterial_ID_Genes_Reference.fasta

### Pool one's 21 specific species

1. Haemophilus_influenzae [嗜血杆菌流感]
2. Citrobacter_freundii [弗氏柠檬酸杆菌]
3. Streptococcus_salivarius [唾液链球菌]
4. Streptococcus_pyogenes [化脓性链球菌]
5. Streptococcus_sanguinis [血链球菌]
6. Streptococcus_pneumoniae [肺炎链球菌]
7. Proteus_mirabilis [奇异变形杆菌]
8. Enterococcus_faecalis [粪肠球菌]
9. Enterococcus_faecium [粪肠球菌]
10. Candida_albicans [白色念珠菌]
11. Neisseria_meningitidis [脑膜炎奈瑟菌]
12. Enterobacter_cloacae [阴沟肠杆菌]
13. Acinetobacter_baumannii [鲍曼不动杆菌]
14. Escherichia_coli [大肠杆菌]
15. Serratia_marcescens [沙雷氏菌]
16. Klebsiella_oxytoca [产氧克雷伯菌]
17. Klebsiella_pneumoniae [肺炎克雷伯菌]
18. Staphylococcus_haemolyticus [溶血葡萄球菌]
19. Staphylococcus_aureus [金黄色葡萄球菌]
20. Staphylococcus_epidermidis [表皮葡萄球菌]
21. Pseudomonas_aeruginosa [铜绿假单胞菌]



### Notes
In the hierarchy of biological classification, genus comes above species and below family.

family > genus > species

科 > 属 > 种



### Taxonomic rank
https://en.wikipedia.org/wiki/Taxonomic_rank#Examples

For `Human`, genus level is `Homo`, and species level is `H. sapiens`.

For `E. coli`, genus level is `Escherichia`, and species level is `E. coli`.

>Escherichia is a genus of Gram-negative, non-spore-forming, facultatively anaerobic, rod-shaped bacteria from the family Enterobacteriaceae.

>Escherichia是来自肠杆菌科的革兰氏阴性、非孢子形成、兼性厌氧杆状细菌属。

### Homo

>https://en.wikipedia.org/wiki/Homo
Homo (from Latin homō 'man') is the genus that emerged in the (otherwise extinct) genus Australopithecus that encompasses the extant species Homo sapiens (modern humans), plus several extinct species classified as either ancestral to or closely related to modern humans (depending on the species), most notably Homo erectus and Homo neanderthalensis. The genus emerged with the appearance of Homo habilis just over 2 million years ago.[a] Homo, together with the genus Paranthropus, is probably sister to Australopithecus africanus, which itself had previously split from the lineage of Pan, the chimpanzees.



### H. sapiens

> https://en.wikipedia.org/wiki/Human

Humans (Homo sapiens) are the most abundant and widespread species of primate, characterized by bipedalism and large, complex brains. This has enabled the development of advanced tools, culture, and language. Humans are highly social and tend to live in complex social structures composed of many cooperating and competing groups, from families and kinship networks to political states. Social interactions between humans have established a wide variety of values, social norms, and rituals, which bolster human society. Curiosity and the human desire to understand and influence the environment and to explain and manipulate phenomena have motivated humanity's development of science, philosophy, mythology, religion, and other fields of study.




`less panBacterial_ID_Genes_Designed.bed|grep "LEVEL=SPECIES"|awk '{print $8}'|less`

```
POOL=1;LEVEL=SPECIES;TARGET_ID=Staphylococcus_epidermidis
POOL=1;LEVEL=SPECIES;TARGET_ID=Staphylococcus_epidermidis
POOL=1;LEVEL=SPECIES;TARGET_ID=Staphylococcus_epidermidis
POOL=1;LEVEL=SPECIES;TARGET_ID=Klebsiella_pneumoniae
POOL=1;LEVEL=SPECIES;TARGET_ID=Klebsiella_pneumoniae
POOL=1;LEVEL=SPECIES;TARGET_ID=Klebsiella_pneumoniae
POOL=1;LEVEL=SPECIES;TARGET_ID=Pseudomonas_aeruginosa_MPAO1/P1
POOL=1;LEVEL=SPECIES;TARGET_ID=Pseudomonas_aeruginosa_MPAO1/P1
POOL=1;LEVEL=SPECIES;TARGET_ID=Pseudomonas_aeruginosa_MPAO1/P1
POOL=1;LEVEL=SPECIES;TARGET_ID=Enterococcus_faecium
POOL=1;LEVEL=SPECIES;TARGET_ID=Enterococcus_faecium
POOL=1;LEVEL=SPECIES;TARGET_ID=Staphylococcus_haemolyticus_R1P1
POOL=1;LEVEL=SPECIES;TARGET_ID=Staphylococcus_haemolyticus_R1P1
POOL=1;LEVEL=SPECIES;TARGET_ID=Staphylococcus_haemolyticus_R1P1
POOL=1;LEVEL=SPECIES;TARGET_ID=Klebsiella_pneumoniae_subsp._pneumoniae_KPNIH11
POOL=1;LEVEL=SPECIES;TARGET_ID=Klebsiella_pneumoniae_subsp._pneumoniae_KPNIH11
POOL=1;LEVEL=SPECIES;TARGET_ID=Klebsiella_pneumoniae_subsp._pneumoniae_KPNIH11
POOL=1;LEVEL=SPECIES;TARGET_ID=Citrobacter_freundii_ATCC_8090_=_MTCC_1658
POOL=1;LEVEL=SPECIES;TARGET_ID=Citrobacter_freundii_ATCC_8090_=_MTCC_1658
POOL=1;LEVEL=SPECIES;TARGET_ID=Citrobacter_freundii_ATCC_8090_=_MTCC_1658
POOL=1;LEVEL=SPECIES;TARGET_ID=Acinetobacter_baumannii
POOL=1;LEVEL=SPECIES;TARGET_ID=Acinetobacter_baumannii
POOL=1;LEVEL=SPECIES;TARGET_ID=Acinetobacter_baumannii
POOL=1;LEVEL=SPECIES;TARGET_ID=Klebsiella_oxytoca
POOL=1;LEVEL=SPECIES;TARGET_ID=Klebsiella_oxytoca
POOL=1;LEVEL=SPECIES;TARGET_ID=Klebsiella_oxytoca
POOL=1;LEVEL=SPECIES;TARGET_ID=Escherichia_coli_ATCC_8739
POOL=1;LEVEL=SPECIES;TARGET_ID=Escherichia_coli_ATCC_8739
POOL=1;LEVEL=SPECIES;TARGET_ID=Escherichia_coli_ATCC_8739
POOL=1;LEVEL=SPECIES;TARGET_ID=Haemophilus_influenzae_R2866
POOL=1;LEVEL=SPECIES;TARGET_ID=Haemophilus_influenzae_R2866
POOL=1;LEVEL=SPECIES;TARGET_ID=Haemophilus_influenzae_R2866
POOL=1;LEVEL=SPECIES;TARGET_ID=Enterococcus_faecalis_ATCC_29212
POOL=1;LEVEL=SPECIES;TARGET_ID=Enterococcus_faecalis_ATCC_29212
POOL=1;LEVEL=SPECIES;TARGET_ID=Enterococcus_faecalis_ATCC_29212
POOL=1;LEVEL=SPECIES;TARGET_ID=Serratia_marcescens
POOL=1;LEVEL=SPECIES;TARGET_ID=Serratia_marcescens
POOL=1;LEVEL=SPECIES;TARGET_ID=Serratia_marcescens
POOL=1;LEVEL=SPECIES;TARGET_ID=Staphylococcus_aureus
POOL=1;LEVEL=SPECIES;TARGET_ID=Staphylococcus_aureus
POOL=1;LEVEL=SPECIES;TARGET_ID=Staphylococcus_aureus
POOL=1;LEVEL=SPECIES;TARGET_ID=Neisseria_meningitidis_Z2491
POOL=1;LEVEL=SPECIES;TARGET_ID=Streptococcus_pyogenes_MGAS6180
POOL=1;LEVEL=SPECIES;TARGET_ID=Streptococcus_pyogenes_MGAS6180
POOL=1;LEVEL=SPECIES;TARGET_ID=Streptococcus_pyogenes_MGAS6180
POOL=1;LEVEL=SPECIES;TARGET_ID=Streptococcus_sanguinis_SK36
POOL=1;LEVEL=SPECIES;TARGET_ID=Streptococcus_sanguinis_SK36
POOL=1;LEVEL=SPECIES;TARGET_ID=Streptococcus_sanguinis_SK36
POOL=1;LEVEL=SPECIES;TARGET_ID=Enterobacter_cloacae_subsp._cloacae_ATCC_13047
POOL=1;LEVEL=SPECIES;TARGET_ID=Enterobacter_cloacae_subsp._cloacae_ATCC_13047
POOL=1;LEVEL=SPECIES;TARGET_ID=Enterobacter_cloacae_subsp._cloacae_ATCC_13047
POOL=1;LEVEL=SPECIES;TARGET_ID=Klebsiella_pneumoniae
POOL=1;LEVEL=SPECIES;TARGET_ID=Klebsiella_pneumoniae
POOL=1;LEVEL=SPECIES;TARGET_ID=Klebsiella_pneumoniae
POOL=1;LEVEL=SPECIES;TARGET_ID=Proteus_mirabilis_HI4320
POOL=1;LEVEL=SPECIES;TARGET_ID=Proteus_mirabilis_HI4320
POOL=1;LEVEL=SPECIES;TARGET_ID=Proteus_mirabilis_HI4320
POOL=1;LEVEL=SPECIES;TARGET_ID=Streptococcus_salivarius_NCTC_8618
POOL=1;LEVEL=SPECIES;TARGET_ID=Streptococcus_salivarius_NCTC_8618
POOL=1;LEVEL=SPECIES;TARGET_ID=Streptococcus_salivarius_NCTC_8618
POOL=1;LEVEL=SPECIES;TARGET_ID=Candida_albicans
POOL=1;LEVEL=SPECIES;TARGET_ID=Candida_albicans
POOL=1;LEVEL=SPECIES;TARGET_ID=Candida_albicans
POOL=1;LEVEL=SPECIES;TARGET_ID=UNKNOWN
POOL=1;TARGET_ID=Escherichia_coli_ATCC_8739;LEVEL=SPECIES
POOL=1;TARGET_ID=Escherichia_coli_ATCC_8739;LEVEL=SPECIES
POOL=1;TARGET_ID=Escherichia_coli_ATCC_8739;LEVEL=SPECIES
POOL=1;TARGET_ID=Escherichia_coli_ATCC_8739;LEVEL=SPECIES
POOL=1;TARGET_ID=Escherichia_coli_ATCC_8739;LEVEL=SPECIES
POOL=1;TARGET_ID=Enterococcus_faecium;LEVEL=SPECIES
POOL=1;TARGET_ID=Staphylococcus_aureus;LEVEL=SPECIES
POOL=1;TARGET_ID=Staphylococcus_aureus;LEVEL=SPECIES
POOL=1;TARGET_ID=Staphylococcus_epidermidis;LEVEL=SPECIES
POOL=1;LEVEL=SPECIES;TARGET_ID=Acinetobacter_baumannii
POOL=1;LEVEL=SPECIES;TARGET_ID=Acinetobacter_baumannii
POOL=1;LEVEL=SPECIES;TARGET_ID=Acinetobacter_baumannii
POOL=1;LEVEL=SPECIES;TARGET_ID=Acinetobacter_baumannii
POOL=1;LEVEL=SPECIES;TARGET_ID=Acinetobacter_baumannii
POOL=1;LEVEL=SPECIES;TARGET_ID=Acinetobacter_baumannii
POOL=1;LEVEL=SPECIES;TARGET_ID=Acinetobacter_baumannii
POOL=1;LEVEL=SPECIES;TARGET_ID=Acinetobacter_baumannii
POOL=1;LEVEL=SPECIES;TARGET_ID=Acinetobacter_baumannii
POOL=1;LEVEL=SPECIES;TARGET_ID=Acinetobacter_baumannii
POOL=1;LEVEL=SPECIES;TARGET_ID=Acinetobacter_baumannii
POOL=1;LEVEL=SPECIES;TARGET_ID=Acinetobacter_baumannii
POOL=1;LEVEL=SPECIES;TARGET_ID=Acinetobacter_baumannii
POOL=1;LEVEL=SPECIES;TARGET_ID=Acinetobacter_baumannii_LAC_4
POOL=1;LEVEL=SPECIES;TARGET_ID=Acinetobacter_baumannii_LAC_4
POOL=1;LEVEL=SPECIES;TARGET_ID=Acinetobacter_baumannii_LAC_4
POOL=1;LEVEL=SPECIES;TARGET_ID=Acinetobacter_baumannii_LAC_4
POOL=1;LEVEL=SPECIES;TARGET_ID=Acinetobacter_baumannii_LAC_4
POOL=1;LEVEL=SPECIES;TARGET_ID=Acinetobacter_baumannii_LAC_4
POOL=1;LEVEL=SPECIES;TARGET_ID=Acinetobacter_baumannii_LAC_4
POOL=1;LEVEL=SPECIES;TARGET_ID=Acinetobacter_baumannii_LAC_4
POOL=1;LEVEL=SPECIES;TARGET_ID=Acinetobacter_baumannii_LAC_4
POOL=1;LEVEL=SPECIES;TARGET_ID=Acinetobacter_baumannii
POOL=1;LEVEL=SPECIES;TARGET_ID=Acinetobacter_baumannii
POOL=1;LEVEL=SPECIES;TARGET_ID=Acinetobacter_baumannii
POOL=1;LEVEL=SPECIES;TARGET_ID=Acinetobacter_baumannii
POOL=1;LEVEL=SPECIES;TARGET_ID=Acinetobacter_baumannii
POOL=1;LEVEL=SPECIES;TARGET_ID=Acinetobacter_baumannii
POOL=1;LEVEL=SPECIES;TARGET_ID=Acinetobacter_baumannii
POOL=1;LEVEL=SPECIES;TARGET_ID=Acinetobacter_baumannii
POOL=1;LEVEL=SPECIES;TARGET_ID=Acinetobacter_baumannii
POOL=1;LEVEL=SPECIES;TARGET_ID=Acinetobacter_baumannii
POOL=1;LEVEL=SPECIES;TARGET_ID=Acinetobacter_baumannii
POOL=1;LEVEL=SPECIES;TARGET_ID=Acinetobacter_baumannii
POOL=1;LEVEL=SPECIES;TARGET_ID=Acinetobacter_baumannii
POOL=1;LEVEL=SPECIES;TARGET_ID=Acinetobacter_baumannii
POOL=1;LEVEL=SPECIES;TARGET_ID=Enterobacter_cloacae_ECNIH2
POOL=1;LEVEL=SPECIES;TARGET_ID=Enterobacter_cloacae_ECNIH2
POOL=1;LEVEL=SPECIES;TARGET_ID=Enterobacter_cloacae_ECNIH2
POOL=1;LEVEL=SPECIES;TARGET_ID=Enterococcus_faecalis_ATCC_29212
POOL=1;LEVEL=SPECIES;TARGET_ID=Enterococcus_faecalis_DENG1
POOL=1;LEVEL=SPECIES;TARGET_ID=Haemophilus_influenzae_2019
POOL=1;LEVEL=SPECIES;TARGET_ID=Klebsiella_pneumoniae_30684/NJST258_2
POOL=1;LEVEL=SPECIES;TARGET_ID=Klebsiella_pneumoniae_30684/NJST258_2
POOL=1;LEVEL=SPECIES;TARGET_ID=Klebsiella_pneumoniae_30684/NJST258_2
POOL=1;LEVEL=SPECIES;TARGET_ID=Klebsiella_pneumoniae_30684/NJST258_2
POOL=1;LEVEL=SPECIES;TARGET_ID=Klebsiella_pneumoniae_30684/NJST258_2
POOL=1;LEVEL=SPECIES;TARGET_ID=Klebsiella_pneumoniae_30684/NJST258_2
POOL=1;LEVEL=SPECIES;TARGET_ID=Klebsiella_pneumoniae_30684/NJST258_2
POOL=1;LEVEL=SPECIES;TARGET_ID=Klebsiella_pneumoniae
POOL=1;LEVEL=SPECIES;TARGET_ID=Klebsiella_pneumoniae
POOL=1;LEVEL=SPECIES;TARGET_ID=Klebsiella_pneumoniae
POOL=1;LEVEL=SPECIES;TARGET_ID=Klebsiella_pneumoniae
POOL=1;LEVEL=SPECIES;TARGET_ID=Klebsiella_pneumoniae
POOL=1;LEVEL=SPECIES;TARGET_ID=Klebsiella_pneumoniae
POOL=1;LEVEL=SPECIES;TARGET_ID=Klebsiella_pneumoniae
POOL=1;LEVEL=SPECIES;TARGET_ID=Klebsiella_pneumoniae_subsp._pneumoniae_Kp13
POOL=1;LEVEL=SPECIES;TARGET_ID=Klebsiella_pneumoniae_subsp._pneumoniae_Kp13
POOL=1;LEVEL=SPECIES;TARGET_ID=Klebsiella_pneumoniae_subsp._pneumoniae_Kp13
POOL=1;LEVEL=SPECIES;TARGET_ID=Klebsiella_pneumoniae_subsp._pneumoniae_Kp13
POOL=1;LEVEL=SPECIES;TARGET_ID=Klebsiella_pneumoniae_subsp._pneumoniae
POOL=1;LEVEL=SPECIES;TARGET_ID=Klebsiella_pneumoniae
POOL=1;LEVEL=SPECIES;TARGET_ID=Pseudomonas_aeruginosa_B136_33
POOL=1;LEVEL=SPECIES;TARGET_ID=Pseudomonas_aeruginosa
POOL=1;LEVEL=SPECIES;TARGET_ID=Pseudomonas_aeruginosa_PA1
POOL=1;LEVEL=SPECIES;TARGET_ID=Staphylococcus_haemolyticus
POOL=1;LEVEL=SPECIES;TARGET_ID=Staphylococcus_haemolyticus
POOL=1;LEVEL=SPECIES;TARGET_ID=Staphylococcus_haemolyticus
POOL=1;LEVEL=SPECIES;TARGET_ID=Staphylococcus_haemolyticus
POOL=1;LEVEL=SPECIES;TARGET_ID=Staphylococcus_haemolyticus
POOL=1;LEVEL=SPECIES;TARGET_ID=Staphylococcus_haemolyticus
POOL=1;LEVEL=SPECIES;TARGET_ID=Staphylococcus_haemolyticus
POOL=1;LEVEL=SPECIES;TARGET_ID=Staphylococcus_haemolyticus
POOL=1;LEVEL=SPECIES;TARGET_ID=Staphylococcus_haemolyticus
POOL=1;LEVEL=SPECIES;TARGET_ID=Staphylococcus_haemolyticus
POOL=1;LEVEL=SPECIES;TARGET_ID=Staphylococcus_haemolyticus
POOL=1;LEVEL=SPECIES;TARGET_ID=Staphylococcus_haemolyticus
POOL=1;LEVEL=SPECIES;TARGET_ID=Staphylococcus_haemolyticus
POOL=1;LEVEL=SPECIES;TARGET_ID=Staphylococcus_haemolyticus
POOL=1;LEVEL=SPECIES;TARGET_ID=Staphylococcus_haemolyticus
POOL=1;LEVEL=SPECIES;TARGET_ID=Staphylococcus_haemolyticus
POOL=1;LEVEL=SPECIES;TARGET_ID=Staphylococcus_haemolyticus
POOL=1;LEVEL=SPECIES;TARGET_ID=Staphylococcus_haemolyticus
POOL=1;LEVEL=SPECIES;TARGET_ID=Staphylococcus_haemolyticus
POOL=1;LEVEL=SPECIES;TARGET_ID=Staphylococcus_haemolyticus
POOL=1;LEVEL=SPECIES;TARGET_ID=Serratia_marcescens_WW4
POOL=1;LEVEL=SPECIES;TARGET_ID=Streptococcus_pneumoniae_70585
POOL=1;LEVEL=SPECIES;TARGET_ID=Streptococcus_pneumoniae_70585
POOL=1;LEVEL=SPECIES;TARGET_ID=Streptococcus_pneumoniae_70585
POOL=1;LEVEL=SPECIES;TARGET_ID=Streptococcus_pneumoniae_70585
POOL=1;LEVEL=SPECIES;TARGET_ID=Streptococcus_pneumoniae_70585
POOL=1;LEVEL=SPECIES;TARGET_ID=Streptococcus_pneumoniae_A026
POOL=1;LEVEL=SPECIES;TARGET_ID=Streptococcus_pyogenes_MGAS2096
POOL=1;LEVEL=SPECIES;TARGET_ID=Streptococcus_salivarius_CCHSS3
POOL=1;LEVEL=SPECIES;TARGET_ID=Klebsiella_oxytoca
POOL=1;LEVEL=SPECIES;TARGET_ID=Klebsiella_oxytoca
POOL=1;LEVEL=SPECIES;TARGET_ID=Klebsiella_oxytoca
POOL=1;LEVEL=SPECIES;TARGET_ID=Klebsiella_oxytoca
POOL=1;LEVEL=SPECIES;TARGET_ID=Klebsiella_oxytoca
POOL=1;LEVEL=SPECIES;TARGET_ID=Klebsiella_oxytoca
POOL=1;LEVEL=SPECIES;TARGET_ID=Klebsiella_oxytoca
POOL=1;LEVEL=SPECIES;TARGET_ID=Klebsiella_oxytoca
POOL=1;LEVEL=SPECIES;TARGET_ID=Klebsiella_oxytoca
POOL=1;LEVEL=SPECIES;TARGET_ID=Klebsiella_oxytoca
POOL=1;LEVEL=SPECIES;TARGET_ID=Klebsiella_oxytoca
POOL=1;LEVEL=SPECIES;TARGET_ID=Klebsiella_oxytoca
POOL=1;LEVEL=SPECIES;TARGET_ID=Neisseria_meningitidis_WUE_2594
POOL=1;LEVEL=SPECIES;TARGET_ID=Neisseria_meningitidis_WUE_2594
POOL=1;LEVEL=SPECIES;TARGET_ID=Neisseria_meningitidis_WUE_2594
POOL=1;LEVEL=SPECIES;TARGET_ID=Neisseria_meningitidis_WUE_2594
POOL=1;LEVEL=SPECIES;TARGET_ID=Neisseria_meningitidis_WUE_2594
POOL=1;LEVEL=SPECIES;TARGET_ID=Neisseria_meningitidis_WUE_2594
POOL=1;LEVEL=SPECIES;TARGET_ID=Neisseria_meningitidis_WUE_2594
POOL=1;LEVEL=SPECIES;TARGET_ID=Neisseria_meningitidis_WUE_2594
POOL=1;LEVEL=SPECIES;TARGET_ID=Neisseria_meningitidis_WUE_2594
POOL=1;LEVEL=SPECIES;TARGET_ID=Neisseria_meningitidis_WUE_2594
POOL=1;LEVEL=SPECIES;TARGET_ID=Neisseria_meningitidis_WUE_2594
POOL=1;LEVEL=SPECIES;TARGET_ID=Neisseria_meningitidis_WUE_2594
POOL=1;LEVEL=SPECIES;TARGET_ID=Neisseria_meningitidis_WUE_2594
POOL=1;LEVEL=SPECIES;TARGET_ID=Neisseria_meningitidis_WUE_2594
POOL=1;LEVEL=SPECIES;TARGET_ID=Neisseria_meningitidis_WUE_2594
POOL=1;LEVEL=SPECIES;TARGET_ID=Neisseria_meningitidis_WUE_2594
POOL=1;LEVEL=SPECIES;TARGET_ID=Neisseria_meningitidis_WUE_2594
POOL=1;LEVEL=SPECIES;TARGET_ID=Neisseria_meningitidis_WUE_2594
POOL=1;LEVEL=SPECIES;TARGET_ID=Neisseria_meningitidis_WUE_2594
POOL=1;LEVEL=SPECIES;TARGET_ID=Neisseria_meningitidis_WUE_2594
POOL=1;LEVEL=SPECIES;TARGET_ID=Neisseria_meningitidis_WUE_2594
POOL=1;LEVEL=SPECIES;TARGET_ID=Proteus_mirabilis_HI4320
POOL=1;LEVEL=SPECIES;TARGET_ID=Proteus_mirabilis_HI4320
POOL=1;LEVEL=SPECIES;TARGET_ID=Proteus_mirabilis_HI4320
POOL=1;LEVEL=SPECIES;TARGET_ID=Proteus_mirabilis_HI4320
POOL=1;LEVEL=SPECIES;TARGET_ID=Proteus_mirabilis_HI4320
POOL=1;LEVEL=SPECIES;TARGET_ID=Proteus_mirabilis_HI4320
POOL=1;LEVEL=SPECIES;TARGET_ID=Proteus_mirabilis_HI4320
POOL=1;LEVEL=SPECIES;TARGET_ID=Proteus_mirabilis_HI4320
POOL=1;LEVEL=SPECIES;TARGET_ID=Serratia_marcescens_WW4
POOL=1;LEVEL=SPECIES;TARGET_ID=Serratia_marcescens_WW4
POOL=1;LEVEL=SPECIES;TARGET_ID=Serratia_marcescens_WW4
POOL=1;LEVEL=SPECIES;TARGET_ID=Serratia_marcescens_WW4
POOL=1;LEVEL=SPECIES;TARGET_ID=Serratia_marcescens_WW4
POOL=1;LEVEL=SPECIES;TARGET_ID=Serratia_marcescens_WW4
POOL=1;LEVEL=SPECIES;TARGET_ID=Serratia_marcescens_WW4
POOL=1;LEVEL=SPECIES;TARGET_ID=Serratia_marcescens_WW4
POOL=1;LEVEL=SPECIES;TARGET_ID=Serratia_marcescens_WW4
POOL=1;LEVEL=SPECIES;TARGET_ID=Streptococcus_pneumoniae
POOL=1;LEVEL=SPECIES;TARGET_ID=Streptococcus_pneumoniae
POOL=1;LEVEL=SPECIES;TARGET_ID=Streptococcus_pneumoniae
POOL=1;LEVEL=SPECIES;TARGET_ID=Streptococcus_pneumoniae
POOL=1;LEVEL=SPECIES;TARGET_ID=Streptococcus_pneumoniae
POOL=1;LEVEL=SPECIES;TARGET_ID=Streptococcus_pneumoniae
POOL=1;LEVEL=SPECIES;TARGET_ID=Streptococcus_pneumoniae
POOL=1;LEVEL=SPECIES;TARGET_ID=Streptococcus_pneumoniae
POOL=1;LEVEL=SPECIES;TARGET_ID=Streptococcus_pneumoniae
POOL=1;LEVEL=SPECIES;TARGET_ID=Streptococcus_pneumoniae
POOL=1;LEVEL=SPECIES;TARGET_ID=Streptococcus_pneumoniae
POOL=1;LEVEL=SPECIES;TARGET_ID=Streptococcus_pneumoniae
POOL=1;LEVEL=SPECIES;TARGET_ID=Streptococcus_pneumoniae
POOL=1;LEVEL=SPECIES;TARGET_ID=Streptococcus_pneumoniae
POOL=1;LEVEL=SPECIES;TARGET_ID=Streptococcus_pneumoniae
POOL=1;LEVEL=SPECIES;TARGET_ID=Streptococcus_pneumoniae
POOL=1;LEVEL=SPECIES;TARGET_ID=Streptococcus_pneumoniae
POOL=1;LEVEL=SPECIES;TARGET_ID=Streptococcus_pneumoniae
POOL=1;LEVEL=SPECIES;TARGET_ID=Streptococcus_pyogenes_JRS4
POOL=1;LEVEL=SPECIES;TARGET_ID=Streptococcus_pyogenes_JRS4
POOL=1;LEVEL=SPECIES;TARGET_ID=Streptococcus_pyogenes_JRS4
POOL=1;LEVEL=SPECIES;TARGET_ID=Streptococcus_pyogenes_JRS4
POOL=1;LEVEL=SPECIES;TARGET_ID=Streptococcus_pyogenes_JRS4
POOL=1;LEVEL=SPECIES;TARGET_ID=Streptococcus_pyogenes_JRS4
POOL=1;LEVEL=SPECIES;TARGET_ID=Streptococcus_pyogenes_JRS4
POOL=1;LEVEL=SPECIES;TARGET_ID=Streptococcus_pyogenes_JRS4
POOL=1;LEVEL=SPECIES;TARGET_ID=Streptococcus_pyogenes_JRS4
POOL=1;LEVEL=SPECIES;TARGET_ID=Streptococcus_pyogenes_JRS4
POOL=1;LEVEL=SPECIES;TARGET_ID=Streptococcus_pyogenes_JRS4
POOL=1;LEVEL=SPECIES;TARGET_ID=Streptococcus_pyogenes_JRS4
POOL=1;LEVEL=SPECIES;TARGET_ID=Streptococcus_pyogenes_JRS4
POOL=1;LEVEL=SPECIES;TARGET_ID=Streptococcus_pyogenes_JRS4
POOL=1;LEVEL=SPECIES;TARGET_ID=Streptococcus_salivarius_JIM8777
POOL=1;LEVEL=SPECIES;TARGET_ID=Streptococcus_salivarius_JIM8777
POOL=1;LEVEL=SPECIES;TARGET_ID=Streptococcus_salivarius_JIM8777
POOL=1;LEVEL=SPECIES;TARGET_ID=Streptococcus_salivarius_JIM8777
POOL=1;LEVEL=SPECIES;TARGET_ID=Streptococcus_salivarius_JIM8777
POOL=1;LEVEL=SPECIES;TARGET_ID=Streptococcus_salivarius_JIM8777
POOL=1;LEVEL=SPECIES;TARGET_ID=Streptococcus_salivarius_JIM8777
POOL=1;LEVEL=SPECIES;TARGET_ID=Streptococcus_salivarius_JIM8777
POOL=1;LEVEL=SPECIES;TARGET_ID=Streptococcus_salivarius_JIM8777
POOL=1;LEVEL=SPECIES;TARGET_ID=Streptococcus_salivarius_JIM8777
POOL=1;LEVEL=SPECIES;TARGET_ID=Streptococcus_salivarius_JIM8777
POOL=1;LEVEL=SPECIES;TARGET_ID=Streptococcus_salivarius_JIM8777
POOL=1;LEVEL=SPECIES;TARGET_ID=Streptococcus_salivarius_JIM8777
POOL=1;LEVEL=SPECIES;TARGET_ID=Streptococcus_salivarius_JIM8777
POOL=1;LEVEL=SPECIES;TARGET_ID=Streptococcus_salivarius_JIM8777
POOL=1;LEVEL=SPECIES;TARGET_ID=Streptococcus_salivarius_JIM8777
POOL=1;LEVEL=SPECIES;TARGET_ID=Streptococcus_salivarius_JIM8777
POOL=1;LEVEL=SPECIES;TARGET_ID=Streptococcus_salivarius_JIM8777
POOL=1;LEVEL=SPECIES;TARGET_ID=Streptococcus_salivarius_JIM8777
POOL=1;LEVEL=SPECIES;TARGET_ID=Streptococcus_salivarius_JIM8777
```

`Candida_albicans [白色念珠菌]`

>panBacterial_ID_Genes_Reference.fasta

```
>Candida_albicans_1___U15152.1_1.1327
AACTAAAGAAAGAAGGTTGGAAGATCTAACAAATTTTTTTGTTCCCCGTTAACCGAAACACACATACATATACTTCTGTCCACACACACACTACCACAAATTTTTGAGCTGATTTCAAACAAGGGTTTTAGAATTTTCCGATTTG
>Candida_albicans_2___U15152.1_1.1327
AACTAAAGAAAGAAGGTTGGAAGATCTAACAAATTTTTTTGTTCCCCGTTAACCGAAACACACATACATATACTTCTGTCCACACACACACTACCACAAATTTTTGAGTTGATTTCAAACAAGGGTTTTAGAATTTTCCGATTTG
>Candida_albicans_3___U15152.1_1.1327
CAAATCGGAAAATTCTAAAACCCTTGTTTGAAATCAGCTCAAAAATTTGTGGTAGTGTGTGTGTGGACAGAAGTATATGTATGTGTGCTTCGGTTAACGGGGAACAAAAAAATTTGTTAGATCTTCCAACCTTCTTTCTTTAGTT
>Candida_albicans_4___U15152.1_1.1327
CAAATCGGAAAATTCTAAAACCCTTGTTTGAAATCAACTCAAAAATTTGTGGTAGTGTGTGTGGACAGAAGTATATGTATGTGTGTTTCGGTTAACGGGGAACAAAAAAATTTGTTAGATCTTCCAACCTTCTTTCTTTAGTT
>Candida_albicans_5___U15152.1_1.1327
CAAATCGGAAAATTCTAAAACCCTTGTTTGAAATCAGCTCAAAAATTTGTGGTAGTGTGTGTGTGGACAGAAGTATATGTATGTGTGTTTCGGTTAACGGGGAACGAAAAAATTTGTTAGATCTTCCAACCTTCTTTCTTTAGTT
>Candida_albicans_1___U15152.1_1.15594
TCAATCATTAGGGCTATTTTGACACTTTGAATTACAATTTTATATCAGTGTCGCATTATTACTATTTCCATTTTCAACAAAGTATTGGATATAACACGTTTCTATCAATCATTACCAACCTGACCAACAGAGTATCCATTACTTCT
>Candida_albicans_2___U15152.1_1.15594
AGAAGTAATGGATACTCTGTTGGTCAGGTTGGTAATGATTGATAGAAACGTGTTATATCCAATACTTTGTTGAAAATGGAAATAGTAATAATGCGACACTGGTATAAAATTGTAATTCAAAGTGTCAAAATAGCCCTAATGATTGA
>Candida_albicans_1___U15152.1_1.9902
CCGATTTGTTTTGGTCTTAGTTTTAGCTTGACAATCAAAAAAGAATTACAAAACATCGAACAACCTTCGACCTTCCCCCCACACTCGTTCCCCCTCTCCTTGCCTCGAGTACACTTCACACCTCAGA
>Candida_albicans_2___U15152.1_1.9902
TCTGAGGTGTGAAGTGTACTCGAGGCAAGGAGAGGGAGGACGAGTGTGGGGGGAAGGTCGAAGGTTGTTCGATGTTTTGTAATTCTTTTTTGATTGTCAAGCTAAAACTAAGACCAAAACAAATCGG

```


>panBacterial_ID_Genes_Designed.bed

```
U15152.1_1.1327 20      200     U15152.1_1.1327 0       +       .       POOL=1;LEVEL=SPECIES;TARGET_ID=Candida_albicans
U15152.1_1.9902 20      200     U15152.1_1.9902 0       +       .       POOL=1;LEVEL=SPECIES;TARGET_ID=Candida_albicans
U15152.1_1.15594        20      200     U15152.1_1.15594        0       +       .       POOL=1;LEVEL=SPECIES;TARGET_ID=Candida_albicans

```
