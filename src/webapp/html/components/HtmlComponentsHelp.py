#!/usr/bin/env python
# -*- coding: utf-8 -*-

# HtmlComponentsHelp.py is part of Barleymap web app.
# Copyright (C) 2017 Carlos P Cantalapiedra.
# Copyright (C) 2024 Bruno Contreras Moreira and Najla Ksouri
# (terms of use can be found within the distributed LICENSE file).

class HtmlComponentsHelp(object):
    
    @staticmethod
    def _help_menu(output_buffer):
        output_buffer.append("""
            <article class="help_article">
                <section class="help_section">
                    <hr/>
                    <ul class="help_menu">
                        <li><a href="#overview">
                        
                            Overview
                            
                        </a></li>
                        <li><a href="#find_markers">
                        
                            Find markers
                            
                        </a></li>
                            <ul>
                                <li><a href="#datasets_included">
                                
                                    Datasets included in Prunusmap web
                                    
                                </a></li>
                            </ul>
                            
                        <li><a href="#align_sequences">
                        
                            Align sequences and proteins
                            
                        </a></li>
                            <ul>
                                <li><a href="#references_included">
                                
                                    References included in Prunusmap web
                                    
                                </a></li>
                            </ul>
                        <li><a href="#locate_by_position">
                        
                            Locate by position
                            
                        </a></li>
                        
                        <li><a href="#barleymap_output">
                        
                            Prunusmap output
                            
                        </a></li>
                        
                        <li><a href="#download">
                        
                        Download marker datasets
                            
                        </a></li>

                        <li><a href="#confidentiality">
                        
                            Confidentiality
                            
                        </a></li>
                        
                        <li><a href="#disclaimer">
                        
                            Disclaimer
                            
                        </a></li>
                        
                        <li><a href="#references">
                        
                            References
                            
                        </a></li>
                    </ul>
                """)
        
        return
    
    @staticmethod
    def help(base_url):
        output_buffer = []
        output_buffer.append("""
                             <section id="content">
                                <a href="{0}"><img style="width:5%;height:5%;border:none;" src="{1}" alt="back"/></a>
                             """.format(base_url+"/", base_url+"/img/back.gif"))
        
        output_buffer.append("""<br/>""")
        
        HtmlComponentsHelp._help_menu(output_buffer)
        
        ## OVERVIEW
        
        output_buffer.append("""
                    <hr/>
                    
                    <br/>
                    <a class="top_link" href="#"><img style="width:10px;height:10px;border:none;" src="{0}/img/top.jpg"/></a>
                    <h2 id="overview">Overview</h2>
                    
                        <br/>

                        Prunusmap was designed to facilitate the search for genetic and physical positions of <em>Prunus</em> markers across various <strong>species and cultivars</strong> within the <em>Prunus</em> genus.
                        Currently, it supports the following species:
                        <ol><strong>
                            <li> Prunus persica (peach) cv. 'Lovell', 'ChineseCling', 'Zhongyoutao14', '124Pan'and 'Sovetskyi' <sup> [1, 2, 3, 4, 5, 6] </sup> and wild relatives: </li>
                                <ul>
                                    <li> Prunus davidiana <sup> [7] </sup> </li>
                                    <li> Prunus ferganensis <sup> [7] </sup> </li>
                                    <li> Prunus kansuensis <sup> [7] </sup> </li>
                                    <li> Prunus mira <sup> [7] </sup> </li>
                                </ul>
                            <li> Prunus dulcis (almond) cv. 'Texas', 'Lauranne', 'Nonpareil' <sup> [8, 9, 10, 11] </sup> </li>
                            <li> Prunus avium (sweet cherry) cv. 'Satonishiki', 'Tieton' <sup> [12,13] </sup> </li>
                            <li> Prunus armeniaca (apricot) cv. 'Rojo Pasion' <sup> [14] </sup> </li>
                            <li> Prunus mume (Japanese apricot) cv. 'Tortuosa' <sup> [15] </sup> </li> 
                        </ol></strong>

                        Each species has its own naming convention to help differentiate them. 
                        Here is a summary of the naming conventions for the maps associated with each species:
                        <ol>
                            <li><strong><em>Prunus persica</em></strong></li>
                                <ul>
                                <li>Maps are named using the format <strong><span style="color: red;">Pp_Cultivar_GenomeSource_Version</span></strong></li>
                                <li> Example: Pp_Lovell_NCBI_V2</li>
                                </ul>

                            <li><strong><em>Prunus dulcis</em></strong></li>
                                <ul>
                                <li>Maps are starting with <strong><span style="color: red;">Pd</span></strong></li>
                                <li> Example: Pd_Lauranne_GDR_V1</li>
                                </ul>

                            <li><strong><em>Prunus avium</em></strong></li>
                                <ul>
                                <li>Maps are starting with <strong><span style="color: red;">Pav</span></strong></li>
                                <li> Example: Pav_Tieton_GDR_V2</li>
                                </ul>

                            <li><strong><em>Prunus armeniaca</em></strong></li>
                                <ul>
                                <li>Maps are starting with <strong><span style="color: red;">Pa</span></strong></li>
                                <li> Example: Pa_RojPas_NCBI_V1</li>
                                </ul>

                            <li><strong><em>Prunus mume</em></strong></li>
                                <ul>
                                <li>Maps are starting with <strong><span style="color: red;">Pm</span></strong></li>
                                <li> Example: Pm_Tortuosa_GDR_V1</li>
                                </ul>
                         </ol>   

                        The defaut map is  <strong>Pp_Lovell_NCBI_V2</strong> map<sup>[2]</sup>:
                        <br/><br/>

                       Prunusmap provides <strong>four tools</strong> to retrieve data from the maps:
                        <ul class="help_list">
                            <li><span style="color: blue;">"Find markers":</span> to retrieve the position of markers providing their identifiers.</li>
                            <li><span style="color: blue;">"Align sequences":</span> to obtain the position of FASTA sequences by pairwise alignment.</li>
                            <li><span style="color: blue;">"Align proteins":</span> to obtain the position of FASTA amino acid sequences by pairwise alignment.</li>
                            <li><span style="color: blue;">"Locate by position":</span> to examine specific loci by map position.</li>
                        </ul>
                        <br/>
                """.format(base_url))
        
        ## FIND MARKERS
        
        output_buffer.append("""
                    <hr/>
                    <br/>
                    <a class="top_link" href="#"><img style="width:10px;height:10px;border:none;" src="{0}/img/top.jpg"/></a>
                    <h2 id="find_markers">Find markers</h2>
                        
                        <br/>
                        
                        The "Find markers" tool allows searching for loci which are commonly used by the Prunus community.
                        These loci include genetic markers, genes, BAC contigs, WGS contigs, etc. from different <strong>datasets</strong>.
                        Their map positions have been previously computed and stored, so that the users can retrieve
                        them by providing the identifier of the locus.
                        
                        <br/><br/>
                        
                        Be aware that "Find markers" datasets were generated using <strong>fixed parameters</strong>.
                        In those cases when the user wants to perform a more specific search, 
                        e.g. by choosing the alignment tool or parameters, 
                        it is recommended to get the FASTA sequence of the query and use the "Align sequences" tool instead.
                        
                        <br/><br/>
                        
                        As <strong>input data</strong>, the user must provide a list of identifiers to use as queries. Besides that,
                        the user needs to choose which is the <strong>map</strong> (or maps) from which to obtain the positions,
                        using the selection list "Choose maps".
                        
                        <br/><br/>
                        
                        The "Genes/Markers enrichment" area allows the user to customize which <strong>additional data</strong> will be output along
                        with the map positions of queries. First, the user can choose whether to show "genes", "markers" and/or "anchored".
                        The last usually refers to WGS contigs, BAC contigs, or other elements associated to map positions (anchored), 
                        but which lack a biological meaning per se.
                        Besides that, the user can also choose whether to "show only main features" for each map.
                        <!--For example, for Morex Genome, "HORVU" genes are configured as "main" whereas "MLOCs" are not.-->
                        The "Add features" option involves 2 ways to add additional data to the results:
                        
                        <ul class="help_list">
                            <li>
                            "on markers": the additional data is searched for each marker independently.
                            Each additional row is appended after the query position.
                            </li>
                            
                            <li>
                            "on intervals": the additional data is searched in the regions defined by all the queries.
                            Each additional row is added only once, and in its actual position in relation to the queries.
                            </li>
                        </ul>
                        
                        Therefore, the "on markers" option is better to obtain detailed data associated to each query,
                        whereas the "on intervals" option is better to obtain a map-like result.
                        Note that both previous options show additional data in the same position as queries by default.
                        To obtain additional data around the markers the "Extend genes/markers search" option
                        must be activated and the interval, in cM or bp, depending on the value of the "Sort by" option (see below), should be adjusted.
                        
                        <br/><br/>
                        
                        <strong>Other parameters</strong> include whether to show or not markers with multiple mappings,
                        whether to sort the output by centimorgans (cM) or basepairs (bp), and an option to send the results to an email address provided by the user.
                        <!--Note that the option "Sort by" will be applied only for maps with both cM and bp positions available.-->
                        
                        <br/><br/>
                        
                        <h3 id="datasets_included">Datasets included in Prunusmap web</h3>
                        <a class="top_link" href="#"><img style="width:10px;height:10px;border:none;" src="{0}/img/top.jpg"/></a>
                        <br/>
                        
                        Datasets in PrunusMap are organized into 3 groups: <strong> genes, markers and Uniprot proteins </strong> often associated with AlphaFold structural models.

                        Each dataset consists of elements of these categories, along with their precomputed map positions determined through sequence alignment against the reference database.
                        Note that the
                        <a href="https://github.com/Cantalapiedra/barleymap">standalone version</a> or a custom
                        <a href="https://github.com/eead-csic-compbio/prunusmap_web">web version</a> of Prunusmap could be used to create other datasets.

                        <ol> 
                            <li><strong> Genes </strong></li>

                        <br/>
                        <table class="table">
                            <tr>
                                <th> Maps </th>
                                <th> Gene IDs </th>
                                <th> Total </th>
                            </tr>
                            <tr>
                                <td> Pp_Lovell_NCBI_V1 </td>
                                <td> PRUPE_ppa011509mg </td>
                                <td> 28,087 </td>
                            </tr>
                            <tr>
                                <td> Pp_Lovell_NCBI_V2 </td>
                                <td> LOC109948900 </td>
                                <td> 25,030 </td>
                            </tr>
                            <tr>
                                <td> Pp_Lovell_JGI_V1 </td>
                                <td> ppa000092m.g </td>
                                <td> 27,864 </td>
                            </tr>
                            <tr>
                                <td> Pp_Lovell_JGI_V2 </td>
                                <td> Prupe.1G001200 </td>
                                <td> 26,873 </td>
                            </tr>
                            <tr>
                                <td> Pp_ChineseCling_GDR_V1 </td>
                                <td> evm.TU.contig279.5 </td>
                                <td> 26,335 </td>
                            </tr>
                            <tr>
                                <td> Pp_Zhongyoutao14_GDR_V1 </td>
                                <td> Pp01G000510 </td>
                                <td> 30,181 </td>
                            </tr>
                            <tr>
                                <td> Pp_124Pan_GDR_V1 </td>
                                <td> P124PAN00019 </td>
                                <td> 25,155 </td>
                            </tr>
                            <tr>
                                <td> Pp_Sovetskiy_NCBI_V1 </td>
                                <td> gene-ndhA </td>
                                <td> 128 </td>
                            </tr>
                            <tr>
                                <td> Pdavidiana_GDR_V2 </td>
                                <td> Pda01g0001 </td>
                                <td> 27,236 </td>
                            </tr>
                            <tr>
                                <td> Pferganensis_GDR_V2 </td>
                                <td> Pfe01g0001 </td>
                                <td> 28,587 </td>
                            </tr>
                                <td> Pkansuensis_GDR_V2 </td>
                                <td> Pka01g0001 </td>
                                <td> 26,986 </td> 
                            </tr>
                            <tr>
                                <td> Pmira_GDR_V2 </td>
                                <td> Pmi01g0001 </td>
                                <td> 28,519 </td>
                            </tr>

                            <tr>
                                <td> Pd_Texas_GDR_V2 </td>
                                <td> Prudul26A002130 </td>
                                <td> 27,042 </td>
                            </tr>
                            <tr>
                                <td> Pd_Texas_NCBI_V2 </td>
                                <td> LOC117629010 </td>
                                <td> 25,445 </td>
                            </tr>
                            <tr>
                                <td> Pd_Texas_GDR_V3.Phase0 </td>
                                <td> TexasF0_G5 </td>
                                <td> 29,145 </td>
                            </tr>
                            <tr>
                                <td> Pd_Texas_GDR_V3.Phase1 </td>
                                <td> TexasF1_G30142 </td>
                                <td> 30,150 </td>
                            </tr>
                            <tr>
                                <td> Pd_Lauranne_GDR_V1 </td>
                                <td> Prudu_020927_v1.0 </td>
                                <td> 23,266 </tr>
                            </tr>
                            <tr>
                                <td> Pd_Nonpareil_GDR_V1 </td>
                                <td> L3X38_000409 </td>
                                <td> 45,581 </td>
                            </tr>
                            <tr>
                                <td> Pa_RojPas_NCBI_V1 </td>
                                <td> gene_CURHAP_LOCUS15 </td>
                                <td> 52,344 </td>
                            </tr>
                            <tr>
                                <td> Pav_Satonishiki_NCBI_V1 </td>
                                <td> LOC110751831 </td>
                                <td> 28,800 </td>
                            </tr>
                            <tr>
                                <td> Pav_Tieton_GDR_V1 </td>
                                <td> FUN_000009 </td>
                                <td> 39,984 </td>
                            </tr>
                            <tr>
                                <td> Pm_Tortuosa_GDR_V1 </td>
                                <td> PmuVar_Chr2_0001 </td>
                                <td> 29,706 </td>
                            </tr>
                        </table>

                        <br/>
                            
                            <li><strong> Markers </strong> </li>
                        <br/>

                        <table class="table">
                            <tr>
                                <th> Arrays </th>
                                <th> IDs </th>
                                <th> Total </th>
                            </tr>
                            <tr>
                                <td> IRSC 9K peach <sup> [16] </sup> </td>
                                <td> SNP_IGA_134631, snp_scaffold_1_46157131, Pp3Cl, RosCOS1338-411 </td>
                                <td> 9,000 </td>
                            </tr>
                            <tr>
                                <td> IRSC 18K peach <sup> [17] </sup> </td>
                                <td> SNP_IGA_679, Peach_AO_0000136, RosCOS1549-533, Pp2Cl, snp_scaffold_2_255513 </td>
                                <td> 18,000 </td>
                            </tr>
                            <tr> 
                                <td> Axiom 60K almond <sup> [18] </sup> </td>
                                <td> AX-158803044 </td>
                                <td> 71,846 </td>
                            </tr>
                            <tr>
                                <td> IRSC 6K cherry <sup> [19] </sup> </td>
                                <td> RosCOS1139-146_snp_sweet_cherry_Pp1_43832684 </td>
                                <td> 5,696 </td>
                            </tr>
                            <tr>
                                <td> Adafuel <sup> [20] </sup> </td>
                                <td> Pp01_10008318_YC </td>
                                <td> 7,831 </td>
                            </tr>
                        </table>

                        <br/></br>
                            <li><strong> UniProt proteins </strong> </li>
                        <ol>

                        <br/>We shall be pleased to add
                        any dataset you suggest to the web application, granted that its use is free and public.
                        <br/><br/>
                """.format(base_url))
        
        ## ALIGN SEQUENCES
        
        output_buffer.append("""
                    <hr/>
                    <br/>
                    <a class="top_link"  href="#"><img style="width:10px;height:10px;border:none;" src="{0}/img/top.jpg"/></a>
                    <h2 id="align_sequences">Align sequences and proteins</h2>
                        
                        <br/>
                        
                        The "Align sequences" tool allows searching the map position of <strong>FASTA nucleotide sequences</strong> through alignment.
                        The "Align proteins" tools does a similar job using <strong>FASTA amino acids sequences</strong> as input.
                        This process is slower than "Find markers", but allows adjusting the alignment parameters as needed.
                        
                        <br/><br/>
                        
                        Some of the features of "Align sequences" and "Align proteins" are:
                        
                        <ul class="help_list">
                            <li>
                            PrunusMap results are map positions, which may come from different sequence references,
                            which are searched in a pan-genome or multi-reference fashion.
                            </li>
                            
                            <li>
                            It allows using different alignment algorithms, what makes possible to search for sequences with and without introns.
                            </li>
                            
                            <li>
                            Most of the details of this process are hidden from the user, who is interested only in the map and its map positions.
                            </li>
                        </ul>
                        
                        As such, most of the <strong>parameters</strong> are the equivalent to those explained for the "Find markers" tool above.
                        As in "Find markers", the user has to choose a <strong>map</strong> (or maps). Note that when the user chooses a map, he is actually choosing
                        all the <strong>sequence references</strong> associated to that map (in the internal Prunusmap configuration),
                        as references for performing the alignments.
                        
                        <br/><br/>

                        In "Align sequences" the user can choose different options for the <strong>alignment algorithm</strong>,
                        under the option "Choose an action".
                        
                        <ul class="help_list">
                            <li>
                            cdna: it is the recommended option, specially when all the queries come from sequences which could have introns.
                            For example, those from CDS or from markers produced from RNAseq data. All the alignments are performed
                            using the GMAP aligner<sup>[21]</sup>.
                            </li>
                            
                            <li>
                            genomic: it uses the most popular alignment tool, BLASTN<sup>[22]</sup>, to perform all the alignments.
                            </li>
                            
                            <li>
                            auto: every query is searched with GMAP. For those queries without hits, the search is repeated with BLASTN.
                            </li>
                        </ul>
                        
                        <br/><br/>
                        
                        Prunusmap is able to use all 3 algorithms when searching maps which have more than one
                        database associated to it. The details of how these algorithms work can be found
                        <a href="https://github.com/Cantalapiedra/barleymap#4111-alignment-algorithm">here</a>.

                        <br/><br/>

                        Instead, "Align proteins" currently relies on MINIPROT<sup>[23]</sup>, an <strong>alignment algorithm</strong>
                        that aligns protein sequences to genomes considering splicing and frameshifts.

                        <br/><br/>

                        Note that the user can choose also the parameters which define minimum thresholds for results of alignment to be reported.
                        The <strong>minimum identity</strong> of alignment can be set with the "min. id." parameter,
                        whereas the <strong>minimum query coverage</strong> in the alignment
                        can be set with the "min. query cov." parameter.
                        Any alignment result with one of those parameters smaller than the thresholds will be discarded and thus not reported in
                        the output tables.
                        
                        <br/><br/>
                        
                        <h3 id="references_included">References included in Prunusmap web</h3>
                        <a class="top_link" href="#"><img style="width:10px;height:10px;border:none;" src="{0}/img/top.jpg"/></a>
                       
PrunusMap was designed to search the position of Prunus genetic markers on the Prunus persica cv. Lovell Physical Maps (NCBI and Phytozome [24,25]) and the Prunus dulcis cv. Texas, Lauranne and Non_pareil Physical Maps (NCBI [3], GDR [15] and [16]).
                       
                       <br/><br/>

                        <table class="table">
                            <tr>
                                <th> Maps </th>
                                <th> Cultivars </th>
                                <th> Assemblies </th>
                                <th> Chromosomes Number; ID </th>
                                <th> Scaffolds Number; ID </th>
                                <th> References </th>
                            </tr>
                            <tr>
                                <td> Pp_Lovell_NCBI_V1 </td>
                                <td> Lovell </td>
                                <td> GCF_000346465.1 </td>
                                <td> --  </td>
                                <td><strong> 202;</strong> NW_006760184.1 - NW_006760385.1 </td>
                                <td> [1] </td>
                            </tr>
                            <tr>
                                <td> Pp_Lovell_NCBI_V2 </td>
                                <td> Lovell  </td>
                                <td> GCF_000346465.2 </td>
                                <td><strong> 8;</strong> NC_034009.1 - NC_034016.1 </td>
                                <td><strong> 183;</strong> NW_018027148.1 - NW_018027330.1 </td>
                                <td> [2] </td>
                            </tr>
                            <tr>
                                <td> Pp_Lovell_JGI_V1 </td>
                                <td> Lovell </td>
                                <td> GCF_000346465.1 </td>
                                <td> -- </td>
                                <td><strong> 202; </strong> scaffold_1, ... </td>
                                <td> [1] </td>
                            </tr>
                            <tr>
                                <td> Pp_Lovell_JGI_V2 </td>
                                <td> Lovell  </td>
                                <td> GCF_000346465.2 </td>
                                <td><strong> 8; </strong> Pp01 - Pp08 </td>
                                <td><strong> 183; </strong> scaffold_101, ... </td>
                                <td> [2] </td>
                            </tr>
                            <tr> 
                                <td> Pp_ChineseCling_GDR_V1 </td>
                                <td> Chinese Cling  </td>
                                <td> -- </td>
                                <td><strong> 8; </strong> Chr1 - Chr8 </td>
                                <td><strong> 127; </strong> contig1, ... </td>
                                <td> [3] </td>
                            </tr>
                            <tr>
                                <td> Pp_Zhongyoutao14_GDR_V1 </td>
                                <td> Zhongyoutao14  </td>
                                <td> -- </td>
                                <td><strong> 8; </strong> G1 - G8 </td>
                                <td> 0 </td>
                                <td> [4] </td>
                            </tr>
                            <tr>
                                <td> Pp_124Pan_GDR_V1 </td>
                                <td> 124Pan (flat peach)  </td>
                                <td> CNA0019231 </td>
                                <td><strong> 8; </strong> Pp01_RaG00 - Pp08_RaG00 </td>
                                <td><strong> 6; </strong> scaffold_12_RaG00, ... </td>
                                <td> [5] </td>
                            </tr>
                            <tr>
                                <td> Pp_Sovetskyi_NCBI_V1 </td>
                                <td> Sovetskyi </td>
                                <td> GCA_022343065.3 </td>
                                <td><strong> 8; </strong> CM039277.1 - CM039284.1 </td>
                                <td><strong> 228; </strong> JAJDMZ010000009.1 - JAJDMZ010000236.1 </td>
                                <td> [6] </td>
                            </tr>
                            <tr>
                                <td> Pdavidiana_GDR_V2 </td>
                                <td> Prunus davidiana </td>
                                <td> -- </td>
                                <td><strong> 8; </strong> Pda01 - Pda08 </td>
                                <td><strong> 556; </strong> ptg000009l, ... </td>
                                <td> [7] </td>
                            </tr>
                            <tr>
                                <td> Pferganensis_GDR_V2 </td>
                                <td> Prunus ferganensis </td>
                                <td> -- </td>
                                <td><strong> 8; </strong> Pfe01 - Pfe08 </td>
                                <td><strong> 439; </strong> ptg000004l, ... </td>
                                <td> [7] </td>
                            </tr>
                            <tr>
                                <td> Pkansuensis_GDR_V2 </td>
                                <td> Prunus kansuensis </td>
                                <td> -- </td>
                                <td><strong> 8; </strong> Pka01 - Pka08 </td>
                                <td><strong> 330; </strong> ptg000014l, ... </td>
                                <td> [7] </td>
                            </tr>
                            <tr>
                                <td> Pmira_GDR_V2 </td>
                                <td> Prunus mira </td>
                                <td> -- </td>
                                <td><strong> 8; </strong> Pmi01 - Pmi08 </td>
                                <td><strong> 364; </strong> ptg000011l, ... </td>
                                <td> [7] </td>
                            </tr>
                            <tr>
                                <td> Pd_Texas_NCBI_V2 </td>
                                <td> Texas  </td>
                                <td> GCA_902201215.1 </td>
                                <td><strong> 8; </strong> NC_047650.1 - NC_047657.1 </td>
                                <td><strong> 683; </strong> NW_023010004.1 - NW_023010686.1 </td>
                                <td> [8] </td>
                            </tr>
                            <tr>
                                <td> Pd_Texas_GDR_V2 </td>
                                <td> Texas  </td>
                                <td> GCA_902201215.1 </td>
                                <td><strong> 8; </strong> Pd01 - Pd08 </td>
                                <td><strong> 683; </strong> pdulcis26_s0345,... </td>
                                <td> [8] </td>
                            </tr>
                            <tr>
                                <td> Pd_Texas_GDR_V3.Phase0 </td>
                                <td> Texas.Phase0 </td>
                                <td> ERP158378 </td>
                                <td><strong> 8; </strong> Chr01 - Chr08 </td>
                                <td> -- </td>
                                <td> [9] </td>
                            </tr>
                            <tr>
                                <td> Pd_Texas_GDR_V3.Phase1 </td>
                                <td> Texas.Phase1 </td>
                                <td> ERP158378 </td>
                                <td><strong> 8; </strong> Chr01 - Chr08 </td>
                                <td> -- </td>
                                <td> [9] </td>
                            </tr>
                            <tr>
                                <td> Pd_Lauranne_GDR_V1 </td>
                                <td> Lauranne  </td>
                                <td> AP019297-AP019304 </td>
                                <td><strong> 8; </strong> Pd01 - Pd08 </td>
                                <td> 0 </td>
                                <td> [10] </td>
                            </tr>
                            <tr>
                                <td> Pd_Nonpareil_GDR_V1 </td>
                                <td> Nonpareil  </td>
                                <td> GCA_021292205 </td>
                                <td><strong> 8; </strong> CM037988.1 - CM037995.1 </td>
                                <td><strong> 95; </strong>; AJFAZ020000011.1 - AJFAZ020000105.1 </td>
                                <td> [11] </td>
                            </tr>
                             <tr>
                            <tr>
                                <td>Pav_Satonishiki_NCBI_V1 </td>
                                <td> Satonishiki  </td>
                                <td> GCA_002207925.1 </td>
                                <td> -- </td>
                                <td><strong> 10,148; </strong> NW_01892124.1, ... </td>
                                <td> [12] </td>
                            </tr>
                            <tr>
                                <td> Pav_Tieton_GDR_V1 </td>
                                <td> Tieton </td>
                                <td> -- </td>
                                <td><strong> 8; </strong> Chr_1 - Chr8 </td>
                                <td><strong> 53; </strong> contig_9 - contig_61 </td>
                                <td> [13] </td>
                            </tr>
                             <tr>
                                <td> Pa_RojPas_NCBI_V1 </td>
                                <td> Rojo Pasion (apricot without seed) </td>
                                <td> GCA_903112645.1 </td>
                                <td> -- </td>
                                <td><strong> 93; </strong> CAEKDK010000001.1 - CAEKDK010000093.1 </td>
                                <td> [14] </td>
                            </tr>
                            <tr>
                                <td> Pm_Tortuosa_GDR_V1 </td>
                                <td> Tortuosa  </td>
                                <td> -- </td>
                                <td><strong> 8; </strong> Chr1 - Chr8 </td>
                                <td><strong> 24; </strong> scaffold9 - scaffold32 </td>
                                <td> [15] </td>
                            </tr>
                             
                        </table>

                        <br/>
                        """.format(base_url))
        
        # PIPELINE IMAGE
        output_buffer.append("""
                        <br/>
                        <center><img width="499" height="526" style="border:none;" src="{0}"/></center>
                        <br/>
                        """.format(base_url+"/img/prunusflow.png"))
        
        
        ## LOCATE BY POSITION
        
        output_buffer.append("""
                    <hr/>
                    <br/>
                    <a class="top_link" href="#"><img style="width:10px;height:10px;border:none;" src="{0}/img/top.jpg"/></a>
                    <h2 id="locate_by_position">Locate by position</h2>
                        
                        <br/>
                        
                        The "Locate by position" tool allows examining the regions of <strong>specific map positions</strong>,
                        mainly with the purpose of checking which genes, markers or other loci are present in those regions.
                        
                        <br/><br/>
                        
                        The input data are "tuples", with chromosome (or contig) and position (local position within the chromosome or contig)
                        in basepairs or centimorgans (e.g. NC_034016.1 100200).
                        
                        <br/><br/>
                        
                        All the other <strong>parameters</strong> are identical to those in "Find markers".
                        
                        <br/><br/>
                        
                """.format(base_url))
        
        ## OUTPUT
        
        output_buffer.append("""
                    <hr/>
                    <br/>
                    <a class="top_link" href="#"><img style="width:10px;height:10px;border:none;" src="{0}/img/top.jpg"/></a>
                    <h2 id="barleymap_output">Prunusmap output</h2>
                        
                        <br/>
                        
                        On top of the results page, Prunusmap outputs a list of maps selected by the user.
                        He can use the links on that list to navigate to the results of a specific map.
                        
                        <br/><br/>
                        
                        For every map which the user selected, Prunusmap shows up to five tables of results:
                        
                        <ul class="help_list">
                            <li>
                            <a href="#results_map">Map</a>
                            </li>
                            
                            <li>
                            <a href="#results_markers">Map with markers</a>
                            </li>
                            
                            <li>
                            <a href="#results_genes">Map with genes</a>
                            </li>
                            
                            <li>
                            <a href="#results_anchored">Map with anchored elements</a>
                            </li>
                            
                            <li>
                            <a href="#results_unmapped_unaligned">Unmapped markers</a>
                            </li>
                            
                            <li>
                            <a href="#results_unmapped_unaligned">Unaligned markers</a>
                            </li>
                        </ul>
                        
                        <h3 id="results_map">Map</h3>
                        <a class="top_link"  href="#"><img style="width:10px;height:10px;border:none;" src="{0}/img/top.jpg"/></a>
                        
                            <br/>
                            
                            The first result returned by Prunusmap is a <strong>graphical representation</strong> of the chromosomes.
                            Queries with map position are shown on top of those chromosomes.
                            Using the magnifying glass button, the user can toggle between complete chromosomes or just the mapped region.
                            
                            <br/><br/>
                            
                            Below the graphical representation is the <strong>"Map"</strong> table, with the next fields:
                            
                            <ul class="help_list">
                                <li>Marker: identifier of the query sequence, either the user supplied value in "Find markers", the FASTA header
                                of the sequence in "Align sequences", or an arbitrary code "chromosome_position" created in "Locate by position".
                                </li>
                                <li>chr: chromosome (or contig or equivalent).</li>
                                <!--<li>cM: centimorgans position. Only for anchored maps with cM positions (IBSC2012 and POPSEQ).</li>-->
                                <!--<li>bp: basepairs position. Only for anchored maps with bp positions.</li>-->
                                <li>start: basepairs starting position. Only for physical maps.</li>
                                <li>end: basepairs ending position. Only for physical maps.</li>
                                <li>strand: whether the query aligns to the target strand (+) or to the complementary strand (-). Only for physical maps (MorexGenome).</li>
                                <li>multiple positions: whether the current query sequence has more than one different mapping position in the current map.
                                    <br/>This field is shown only if the "Markers with multiple mappings" option has been selected.
                                    <br/>
                                </li>
                                <li>other alignments: whether the current query sequence has other alignment targets which lack map position.
                                    <br/>At least one unmapped alignment should be found for such query.
                                </li>
                            </ul>
                        
                        <h3 id="results_markers">Map with markers</h3>
                        <a class="top_link" href="#"><img style="width:10px;height:10px;border:none;" src="{0}/img/top.jpg"/></a>
                        
                            <br/>
                            
                            The <strong>Map with markers</strong> table shows the mapping results along with the genetic markers that are
                            located in the same positions (or regions if the search is extended). The table has the same fields as the Map table.
                        
                        <h3 id="results_genes">Map with genes</h3>
                        <a class="top_link" href="#"><img style="width:10px;height:10px;border:none;" src="{0}/img/top.jpg"/></a>
                            <br/>
                            
                            The <strong>Map with genes</strong> table shows the mapping results along with the genes that are
                            located in the same positions (or regions if the search is extended). The table has all the fields of the previous tables,
                            plus some additional fields, related to functional annotation of genes:
                            
                            <ul class="help_list">
                                <!--<li>Gene class: High Confidence or Low Confidence classification.</li>-->
                                <li>Description: human-readable description of the gene.</li>
                            </ul>
                        
                        <h3 id="results_anchored">Map with anchored elements</h3>
                        <a class="top_link" href="#"><img style="width:10px;height:10px;border:none;" src="{0}/img/top.jpg"/></a>
                        
                            <br/>
                            
                            <!---The <strong>Map with anchored elements</strong> table shows the mapping results along with the elements that are
                            located in the same positions (or regions if the search is extended). In this case, they are not genes or markers;
                            anchored elements have map position but often lack biological meaning (e.g. WGS contigs, BAC contigs, etc.).
                            The table has the same fields as the Map and the Map with markers tables.-->
                        
                        
                        
                        <h3 id="results_unmapped_unaligned">Unmapped and unaligned markers</h3>
                        <a class="top_link" href="#"><img style="width:10px;height:10px;border:none;" src="{0}/img/top.jpg"/></a>
                        
                            <br/>
                            
                            In addition to the mapping results, two more tables are shown for each map.
                            
                            <ul class="help_list">
                                <li><strong>Unmapped</strong>: shows those queries which have an alignment hit (field "Target ID").</li>
                                    Note that queries in this table could still have map position, through a different alignment.
                                <li><strong>Unaligned</strong>: shows those queries which lack alignment hit (and thus map position).</li>
                            </ul>
                        <br/>
            """.format(base_url))

        ## DOWNLOAD
        
        output_buffer.append("""
                    <hr/>
                    <br/>
                    <a class="top_link" href="#"><img style="width:10px;height:10px;border:none;" src="{0}/img/top.jpg"/></a>
                    <h2 id="download">Download SNP Arrays</h2>
                        
                        <br/><br/>
                        Click the buttons below to download SNP array datasets for Peach, Cherry, and Almond:
                        <br/><br/>
                        
                        <table cellspacing="30">
                            <tr><td>
                            <h3> - Prunus persica: peach </h3>
                            </td>
                            <td>
                                <a href="https://github.com/eead-csic-compbio/prunusmap_web/raw/refs/heads/master/download/IRSC_9K_peach.xlsx" download="IRSC_9K_peach.xlsx">
                                    <img src="{0}/img/excel_download.png" alt="excel_download_icon" width="100" height="100">
                                    <p>IRSC 9K peach array</p>
                                </a>
                            </td><td>
                                <a href="https://github.com/eead-csic-compbio/prunusmap_web/raw/refs/heads/master/download/IRSC_18K_peach.xlsx" download="IRSC_18K_peach.xlsx">
                                    <img src="{0}/img/excel_download.png" alt="excel_download_icon" width="100" height="100">
                                    <p>IRSC 18K peach array</p>
                                </a>
                            </td><td>
                                <a href="https://github.com/eead-csic-compbio/prunusmap_web/raw/refs/heads/master/download/Adafuel_peach.xlsx" download="Adafuel_peach.xlsx">
                                    <img src="{0}/img/excel_download.png" alt="excel_download_icon" width="100" height="100">
                                    <p>Adafuel peach </p>
                            </td></tr>

                        </table>
                        <table cellspacing="30">
                            <tr><td>
                                <h3>- Prunus avium: Cherry </h3>
                            </td>
                            <td>
                                <a href="https://github.com/eead-csic-compbio/prunusmap_web/raw/refs/heads/master/download/IRSC_6K_cherry.xlsx" download="IRSC_6K_cherry.xlsx">
                                    <img src="{0}/img/excel_download.png" alt="excel_download_icon" width="100" height="100">
                                    <p>IRSC 6K cherry</p>
                                </a>
                            </td></tr>
                        </table>
                        <table cellspacing="30">
                            <tr><td>
                                <h3>- Prunus dulcis: Almond </h3>
                            </td>
                            <td>
                                <a href="https://github.com/eead-csic-compbio/prunusmap_web/raw/refs/heads/master/download/Axiom%2060K%20almond.xlsx" download="Axiom 60K almond.xlsx">
                                    <img src="{0}/img/excel_download.png" alt="excel_download_icon" width="100" height="100">
                                    <p>Axiom 60K Prunus dulcis</p>
                                </a>
                            </td></tr>
                        </table>

                        <br/>
            """.format(base_url))
     

        ## CONFIDENTIALITY
        
        output_buffer.append("""
                    <hr/>
                    <br/>
                    <a class="top_link" href="#"><img style="width:10px;height:10px;border:none;" src="{0}/img/top.jpg"/></a>
                    <h2 id="confidentiality">Confidentiality</h2>
                    
                        <br/>
			While Barleymap uses HTTPS by default, we cannot guarantee the security of the data used with the web tool.
                        <br/><br/>
                        Should this naïve confidentiality be not acceptable to some users, we would recommend installing the
                        <a href="https://github.com/Cantalapiedra/barleymap">standalone barleymap</a> version,
                        or setting up their own instace of
                        <a href="https://github.com/eead-csic-compbio/prunusmap_web">prunusmap_web</a> version. 
                        <br/><br/>
            """.format(base_url))
        
        ## DISCLAIMER
        
        output_buffer.append("""
                    <hr/>
                    <br/>
                    <a class="top_link" href="#"><img style="width:10px;height:10px;border:none;" src="{0}/img/top.jpg"/></a>
                    <h2 id="disclaimer">Disclaimer</h2>
                        <br/>
                        This service is available AS IS and at your own risk.
                        EEAD-CSIC do not give any representation or warranty nor assume
                        any liability or responsibility for the service or the results posted
                        (whether as to their accuracy, completeness, quality or otherwise).
                        Access to the service is available free of charge for ordinary use
                        in the course of academic research.
                        <br/><br/>
                    <hr/>
                <!--</section>-->
                <br/>
            """.format(base_url))
        
        ## APPENDIX
        
        output_buffer.append("""
                <br/>
                <a class="top_link" href="#"><img style="width:10px;height:10px;border:none;" src="{0}/img/top.jpg"/></a>
                    <h2 id="references">References</h2>
                <br/>
                <!--<section class="help_section">-->
               
                    <cite><sup>[1]</sup><a href="https://doi.org/10.1038/ng.2586" target="_blank">International Peach Genome Initiative. 2013</a>
                    </cite><br/>
            
                    <cite><sup>[2]</sup><a href="https://doi.org/10.1186%2Fs12864-017-3606-9" target="_blank">Verde et al. 2017</a>
                    </cite><br/>
            
                    <cite><sup>[3]</sup><a href="https://doi.org/10.1111/tpj.15439" target="_blank">Cao et al. 2021 </a>
                    </cite><br/>

                    <cite><sup>[4]</sup><a href="https://doi.org/10.1111/pbi.13767" target="_blank">Lian et al. 2021 </a>
                    </cite><br/>
                    
                    <cite><sup>[5]</sup><a href="https://doi.org/10.3390/plants10030538" target="_blank">Zhang et al. 2021 </a>
                    </cite><br/>

                    <cite><sup>[6]</sup><a href="https://doi.org/10.1371/journal.pone.0269284" target="_blank">Gladysheva-Azgari et al. 2022</a>
                    </cite><br/>
                    
                    <cite><sup>[7]</sup><a href="https://doi.org/10.1186/s12915-022-01342-y" target="_blank">Cao et al. 2022</a>
                    </cite><br/>

                    <cite><sup>[8]</sup><a href="https://doi.org/10.1111/tpj.14538" target="_blank">Alioto et al. 2020</a>
                    </cite><br/>
                    
                    <cite><sup>[9]</sup><a href="https://doi.org/10.1093/hr/uhae106" target="_blank">Castanera et al. 2024</a>
                    </cite><br/>
                    
                    <cite><sup>[10]</sup><a href="https://doi.org/10.1126/science.aav8197" target="_blank">Sánchez-erez et al. 2019</a>
                    </cite><br/>

                    <cite><sup>[11]</sup><a href="https://doi.org/10.1093/g3journal/jkac065" target="_blank">D'Amico-Willman et al. 2022</a>
                    </cite><br/>
                    
                    <cite><sup>[12]</sup><a href="https://doi.org/10.1093/dnares/dsx020" target="_blank">Shirasawa et al. 2017</a>
                    </cite><br/>
                    
                    <cite><sup>[13]</sup><a href="https://doi.org/10.1038/s41438-020-00343-8" target="_blank">Wang et al. 2020</a>
                    </cite><br/>
                    
                    <cite><sup>[14]</sup><a href="https://doi.org/10.1186/s13059-020-02235-5" target="_blank">Campoy et al. 2020</a>
                    </cite><br/>
                    
                    <cite><sup>[15]</sup><a href="https://doi.org/10.1111/nph.17894" target="_blank">Tangchun Zheng et al. 2021</a>
                    </cite><br/>

                    <cite><sup>[16]</sup><a href="https://doi.org/10.1371/journal.pone.0035668" target="_blank">Verde et al. 2012</a> IRSC 9K markers downloaded from the <a href="https://www.rosaceae.org/species/rosaceae_family_genera/IRSC_SNP_array">GDR</a>.
                   </cite><br/>
                    
                    <cite><sup>[17]</sup> IRSC 18K markers downloaded from the <a href="https://www.rosaceae.org/species/rosaceae_family_genera/IRSC_SNP_array">GDR</a>.
                   </cite><br/>
                    
                    <cite><sup>[18]</sup><a href="https://doi.org/10.3390/plants12020242" target="_blank">Duval et al. 2023</a></cite><br>

                    <cite><sup>[19]</sup><a href="https://doi.org/10.1371/journal.pone.0048305" target="_blank">Peace et al. 2012</a></cite><br>

                    <cite><sup>[20]</sup><a href="https://doi.org/10.3389/fpls.2022.872208" target="_blank">Guajardo et al. 2022</a></cite><br>
            
                    <cite><sup>[21]</sup><a href="https://doi.org/10.1093/bioinformatics/bti310" target="_blank">Wu et al. 2005</a></cite><br>
                    
                    <cite><sup>[22]</sup><a href="https://doi.org/10.1093/nar/gkt282" target="_blank">Boratyn et al. 2013</a></cite><br>

                    <cite><sup>[23]</sup><a href="https://doi.org/10.1093/bioinformatics/btad014" target="_blank">Li et al. 2023</a></cite><br/>
                    
                    <cite><sup>[24]</sup><a href="https://doi.org/10.1093/nar/gkab1112" target="_blank">Sayers et al. 2022</a></cite><br>
                    
                    <cite><sup>[26]</sup><a href="https://doi.org/10.1093/nar/gky1000" target="_blank">Jung et al. 2019</a></cite><br/>
                    
                    <cite><sup>[25]</sup><a href="https://doi.org/10.1093/nar/gkr944" target="_blank">Goodstein et al. 2012</a></cite><br>
                    

                </section>
                <br/>
                <hr/>
            </article>
            """.format(base_url))
        
        output_buffer.append("""
            <a href="{0}"><img style="width:5%;height:5%;border:none;" src="{1}" alt="back"/></a>
        </section> <!-- content -->
        """.format(base_url+"/", base_url+"/img/back.gif"))
        
        return "".join(output_buffer)

## END
