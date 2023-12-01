#!/usr/bin/env python
# -*- coding: utf-8 -*-

# HtmlComponentsHelp.py is part of Barleymap web app.
# Copyright (C) 2017 Carlos P Cantalapiedra.
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
                        
                            Align sequences
                            
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

                        Prunusmap was designed to search the genetic and physical positions of <em>Prunus</em> genetic markers
                        on physical and genetic maps of <i>Prunus persica</i> (NCBI and <a href="https://phytozome-next-jgi.doe.gov">Phytozome</a> <sup>[1,2]</sup>) and <i>Prunus dulcis</i> (NCBI and GDR) <sup>[3,15,16]</sup>).
                        The current version uses the <strong>Pp_NCBI_V2</strong> map<sup>[5]</sup> by default.
                        <br/><br/>
                        Prunusmap provides <strong>three tools</strong> to retrieve data from the maps:
                        <ul class="help_list">
                            <li>"Find markers": to retrieve the position of markers providing their identifiers.</li>
                            <li>"Align sequences": to obtain the position of FASTA sequences by pairwise alignment.</li>
                            <li>"Locate by position": to examine specific loci by map position.</li>
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
                        
                        The next is a list of datasets whose map positions have been pre-computed and stored in this instance of the Barleymap web application.
                        Note that the
                        <a href="https://github.com/Cantalapiedra/barleymap">standalone version</a> or a custom
                        <a href="https://github.com/eead-csic-compbio/prunusmap_web">web version</a> of Prunusmap could be used to create other datasets.
                        
                        <ul class="help_list">
                        
                            <li>
                                <b> IRSC 9K markers</b> <i>Prunus persica</i> dataset<sup>[4,8]</sup>: identifiers look like SNP_IGA_134631, snp_scaffold_1_46157131, snp_1_46757382, Pp8Cl or RosCOS1338-411. 
                                <br/>
                                A full list of markers and their sequences can be found at the <a href="https://www.rosaceae.org/species/rosaceae_family_genera/IRSC_SNP_array">GDR</a>.
                            </li>
                           
                            <li>
                                <b>IRSC 16K markers</b> <i>Prunus persica</i> dataset<sup>[5,8]</sup>: identifiers look like SNP_IGA_679 or Peach_AO_0000136. 
                                <br/>
                                A full list of markers and their sequences can be found at the <a href="https://www.rosaceae.org/Analysis/431">GDR</a>.
                            </li>

                            <li>
                                <b>AdafuelxFlordaguard</b> peach rootstock markers<sup>[6]</sup> with physical and genetic positions: identifiers look like Pp01_60632_SC_0.
                            </li>
                            
                            <li>
                                <b>Axiom 60K</b> <i>Prunus dulcis</i> dataset <sup>[7]</sup>: identifiers look like AX-586141685 or 64598_Pd08_Pd08.
                            </li>
                            
                            <li><b>UniProt proteins</b> of <i>Prunus persica</i> dataset <sup>[9]</sup>, mapped with [miniprot](https://github.com/lh3/miniprot): identifiers look like E3W0H3_PRUPE.</li>
                            
                            <li><b>UniProt proteins of <i>Prunus dulcis</i> cv.Texas_NCBIv2: identifiers looks like A0A1W6CB65_PRUDU </li>
                            
                            <li><b>JGI gene models</b> of <i>Prunus persica</i> <sup>[10]</sup>: identifiers look like ppa000003m.g and Prupe.1G000100 for respectively v1 and v2.</li>

                            <li><b>NCBI gene models</b> of <i>Prunus persica</i> <sup>[11]</sup>: identifiers look like PRUPE_ppa017353mg and LOC18793189 for respectively v1 and v2.</li>

                            <li><b>NCBI gene models</b> of <i>Prunus dulcis</i> <sup>[11]</sup>: identifiers look like LOC117629531.</li>

                            <li><b>GDR gene models of <i>Prunus dulcis</i> cv.Lauranne_v1: identifiers look like Prudu_020918_v1.0.</li>

                            <li><b>GDR gene models of <i>Prunus dulcis</i> cv.Nonpareil_v1: identifiers look like L3X38_000408.</li>
                            
                        </ul>
                        
                        <br/>We shall be pleased to add
                        any dataset you suggest to the web application, granted that its use is free and public.
                        <br/><br/>
                """.format(base_url))
        
        ## ALIGN SEQUENCES
        
        output_buffer.append("""
                    <hr/>
                    <br/>
                    <a class="top_link"  href="#"><img style="width:10px;height:10px;border:none;" src="{0}/img/top.jpg"/></a>
                    <h2 id="align_sequences">Align sequences</h2>
                        
                        <br/>
                        
                        The "Align sequences" tool allows searching the map position of <strong>FASTA formatted sequences</strong> through alignment.
                        This process is slower than "Find markers", but allows adjusting the alignment parameters as needed and searching
                        for any DNA sequences.
                        
                        <br/><br/>
                        
                        Some of the features of "Align sequences" are:
                        
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
                            using the GMAP aligner<sup>[12]</sup>.
                            </li>
                            
                            <li>
                            genomic: it uses the most popular alignment tool, BLASTN<sup>[13]</sup>, to perform all the alignments.
                            </li>
                            
                            <li>
                            auto: every query is searched with GMAP. For those queries without hits, the search is repeated with BLASTN.
                            </li>
                        </ul>
                        
                        Note that the user can choose also the parameters which define minimum thresholds for results of alignment to be reported.
                        The <strong>minimum identity</strong> of alignment can be set with the "min. id." parameter,
                        whereas the <strong>minimum query coverage</strong> in the alignment
                        can be set with the "min. query cov." parameter.
                        Any alignment result with one of those parameters smaller than the thresholds will be discarded by barleymap and thus not reported in
                        the output tables.
                        
                        <br/><br/>
                        
                        Besides that, Prunusmap is able to use 3 different algorithms when searching maps which have more than one
                        database associated to it. The details of how these algorithms work can be found
                        <a href="https://github.com/Cantalapiedra/barleymap#4111-alignment-algorithm">here</a>.
                        Here, just a brief description of the maps and databases included,
                        and the algorithms, is provided.
                        
                        <br/><br/>
                        
                        <h3 id="references_included">References included in Prunusmap web</h3>
                        <a class="top_link" href="#"><img style="width:10px;height:10px;border:none;" src="{0}/img/top.jpg"/></a>
                       
PrunusMap was designed to search the position of Prunus genetic markers on the Prunus persica cv. Lovell Physical Maps (NCBI and Phytozome [1,2]) and the Prunus dulcis cv. Texas, Lauranne and Non_pareil Physical Maps (NCBI [3], GDR [15] and [16]).
i


                        <ul class="help_list">
                            <li><strong><i>Pp_NCBI_V1</strong>: Prunus persica</i> cv. Lovell<sup>[1]</sup></li>
                                <br/>
                                
                                The first published peach genome with NCBI annotation<sup>[11]</sup>. 
                                Chromosome names look like NW_006760385.1, corresponding to assembly GCF_000346465.1.
                                
                                <br/><br/>
                            <li><strong><i>Pp_NCBI_V2</strong>: Prunus persica</i> cv. Lovell<sup>[2]</sup></li>
                                <br/>
                               
                                Current peach genome with NCBI annotation<sup>[11]</sup>.
                                Chromosome names are NC_034009.1 .. NC_034016.1, with unplaced scaffolds from NW_018027148.1 on.
                                This corresponds to assembly GCF_000346465.2.
                                
                                <br/><br/>
                            <li><strong>Pp_JGI_V2</strong>: Prunus persica</i> cv. Lovell<sup>[2]</sup></li>
                                <br/>
                               
                                Current peach genome with chromosome names and gene models from JGI <sup>[10]</sup>.
                                Chromosome names are Pp01 to Pp08, with unplaced scaffolds from scaffold_12 on.

                            <li><strong>Pd_NCBI_V2</strong>: Prunus dulcis</i> cv. Texas<sup>[3]</sup></li>
                                <br/>
                    
                                Current almond genome with NCBI annotation<sup>[11]</sup>.
                                Chromosome names are NC_047650.1 to NC_047657.1 with unplaced scaffolds from NW_023010004.1 on.
                                This corresponds to assembly GCF_902201215.1.

                            <li><strong>Pd_Texas_GDR_V2</strong>: Prunus dulcis</i> cv. Texas<sup>[3]</sup></li>
                                <br/>
                    
                                Chromosome names are Pd01 to Pd08 with unplaced scaffolds from pdulcis26_s034 on.
                                This corresponds to assembly GCF_902201215.1.
                            <li><strong>Pd_Nonpareil_GDR_V1</strong>: Prunus dulcis</i> cv. Nonpareil<sup>[15]</sup></li>
                                <br/>

                                Chromosome names are CM037988.1 to CM037995.1 with unplaced scaffolds from AJFAZ020000011.1 on.
                                This corresponds to assembly GCA_021292205.
                            <li><strong>Pd_Lauranne_GDR_V1</strong>: Prunus dulcis</i> cv. Lauranne<sup>[16]</sup></li>
                                <br/>

                                Chromosome names are Pd01 to Pd08.
                                This corresponds to assembly <a href="https://www.ebi.ac.uk/ena/browser/view/AP019297-AP019304">AP019297-AP019304</a>.

                        </ul>
                        <br/>
                        """.format(base_url))
        
        # PIPELINE IMAGE
        output_buffer.append("""
                        <br/>
                        <center><img width="499" height="526" style="border:none;" src="{0}"/></center>
                        <br/>
                        """.format(base_url+"/img/barleymap_popseq.pipeline_2.png"))
        
        
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
                            
                            The first result shown by Prunusmap is a <strong>graphical representation</strong> of the chromosomes.
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
                                <li>InterPro: IPR identifiers for the gene.</li>
                                <li>GeneOntologies: GO identifiers for the gene.</li>
                                <li>PFAM: Protein Families identifiers for the gene.</li>
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
        
        ## CONFIDENTIALITY
        
        output_buffer.append("""
                    <hr/>
                    <br/>
                    <a class="top_link" href="#"><img style="width:10px;height:10px;border:none;" src="{0}/img/top.jpg"/></a>
                    <h2 id="confidentiality">Confidentiality</h2>
                    
                        <br/>
			While Barleymap uses HTTPS by default, we can not guarantee the security of the data used with the web tool.
                        <br/><br/>
                        Should this naïve confidentiality be not acceptable to some users, we would recommend installing the
                        <a href="https://github.com/Cantalapiedra/barleymap">standalone barleymap</a> version,
                        or setting up their own instace of
                        <a href="https://github.com/Cantalapiedra/barleymap_web">barleymap web</a> version. 
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
            
                    <cite><sup>[3]</sup><a href="https://doi.org/10.1111/tpj.14538" target="_blank">Alioto et al. 2020</a>
                    </cite><br/>
           
                    <cite><sup>[4]</sup><a href="https://doi.org/10.1371%2Fjournal.pone.0035668" target="_blank">Verde et al. 2012</a> IRSC 9K markers downloaded from the <a href="https://www.rosaceae.org/species/rosaceae_family_genera/IRSC_SNP_array">GDR</a>.
                    </cite></br>
            
                    <cite><sup>[5]</sup>Gasic et al. 2022. Unpublished. IRSC 16K markers downloaded from the <a href="https://www.rosaceae.org/Analysis/431">GDR</a>.
                    </cite></br>

                    <cite><sup>[6]</sup><a href="https://doi.org/10.3389/fpls.2022.872208" target="_blank">Guajardo et al. 2022</a>
                    </cite><br>

                    <cite><sup>[7]</sup><a href="https://doi.org/10.3390/plants12020242" target="_blank">Duval et al. 2023</a>
                    </cite><br>

                    <cite><sup>[8]</sup><a href="https://doi.org/10.1093%2Fnar%2Fgky1000" target="_blank">Jung et al. 2019</a>
                    </cite><br>

                    <cite><sup>[9]</sup><a href="https://doi.org/10.1093/nar/gkac1052" target="_blank">The UniProt Consortium. 2023</a>
                    </cite><br>

                    <cite><sup>[10]</sup><a href="https://doi.org/10.1093/nar/gkr944" target="_blank">Goodstein et al. 2012</a>
                    </cite><br>

                    <cite><sup>[11]</sup><a href="https://doi.org/10.1093%2Fnar%2Fgkab1112" target="_blank">Sayers et al. 2021</a>
                    </cite><br>

                    <cite><sup>[12]</sup><a href="https://doi.org/10.1093/bioinformatics/bti310"
                                            target="_blank">Wu and Watanabe 2005</a></cite>
                    <br/>
                    <cite><sup>[13]</sup><a href="https://doi.org/10.1016/S0022-2836(05)80360-2"
                                            target="_blank">Altschul et al. 1990</a></cite>
                    <br/>

                    <cite><sup>[15]</sup><a href="https://doi.org/10.1093/g3journal/jkac097"
                                            target="_blank">D'Amico-Willman et al. 2022</a></cite>
                    <br/>

                    <cite><sup>[16]</sup><a href="https://doi.org/10.1126/science.aav8197"
                                            target="_blank">Sanchez-Perez et al. 2019</a></cite>
                    <br/>

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
