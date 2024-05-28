#!/usr/bin/env python
# -*- coding: utf-8 -*-

# HtmlLayoutBarleymap.py is part of PrunusMap web app.
# Copyright (C) 2017  Carlos P Cantalapiedra.
# (terms of use can be found within the distributed LICENSE file).

class HtmlLayoutBarleymap(object):
    
    @staticmethod
    def output_html_img_button(action, url, img_url, width = "3%", height = "3%", img_url_hover = None):
        output = []
        if url and img_url:
            output.append("""<a href="{1}">
                          <img style="width:{2};height:{3}; border:0;"
                          onmouseover="hover_{0}(this);" onmouseout="unhover_{0}(this);"
                          src="{4}"/>
                          </a>""".format(action, url, width, height, img_url))
            
            if img_url_hover:
                # Functions to change maps image (zoom or full maps)
                output.append("""
                <script>
                    // Functions to change image with mouse over and out
                    function hover_{0}(element) {{
                        element.setAttribute('src', '{2}');
                    }}
                    function unhover_{0}(element) {{
                        element.setAttribute('src', '{1}');
                    }}
                </script>
                """.format(action, img_url, img_url_hover))
        else:
            Exception("HtmlLayoutBarleymap: No URL or img_url provided for img button.")
        
        return "".join(output)
    
    @staticmethod
    def main_text(citation, base_url, PREFIX_UI_CTRLS_ALIGN, PREFIX_UI_CTRLS_PROT, PREFIX_UI_CTRLS_FIND, PREFIX_UI_CTRLS_LOCATE):
        output = []
        #output.append('<br/>')
        output.append('<div id="main_buttons" style="margin:0px;">')
        output.append('<table id="main_buttons_table" center><tr>')
        output.append('<td style="text-align:center;">')
        output.append(HtmlLayoutBarleymap.output_html_img_button(PREFIX_UI_CTRLS_FIND, base_url+"/"+PREFIX_UI_CTRLS_FIND+"/",
                                                                 base_url+"/img/ui_buttons_find.png", "200px", "100px",
                                                                 base_url+"/img/ui_buttons_find_hover.png"))
        output.append("</td>")
        output.append('<td style="text-align:center;">')
        output.append(HtmlLayoutBarleymap.output_html_img_button(PREFIX_UI_CTRLS_ALIGN, base_url+"/"+PREFIX_UI_CTRLS_ALIGN+"/",
                                                                 base_url+"/img/ui_buttons_align.png", "200px", "100px",
                                                                 base_url+"/img/ui_buttons_align_hover.png"))

        output.append("</td>")
        output.append('<td style="text-align:center;">')
        output.append(HtmlLayoutBarleymap.output_html_img_button(PREFIX_UI_CTRLS_PROT, base_url+"/"+PREFIX_UI_CTRLS_PROT+"/",
                                                                 base_url+"/img/ui_buttons_prot.png", "200px", "100px",
                                                                 base_url+"/img/ui_buttons_prot_hover.png")) 

        output.append("</td>")
        output.append('<td style="text-align:center;">')
        output.append(HtmlLayoutBarleymap.output_html_img_button(PREFIX_UI_CTRLS_LOCATE, base_url+"/"+PREFIX_UI_CTRLS_LOCATE+"/",
                                                                 base_url+"/img/ui_buttons_locate.png", "200px", "100px",
                                                                 base_url+"/img/ui_buttons_locate_hover.png"))
        output.append("</td>")
        output.append('<td style="text-align:center;">')
        output.append(HtmlLayoutBarleymap.output_html_img_button("help", base_url+"/help/",
                                                                 base_url+"/img/ui_buttons_help.png", "200px", "100px",
                                                                 base_url+"/img/ui_buttons_help_hover.png"))
        output.append("</td>")
        output.append("</tr>")
        output.append("</table>")
        output.append("</div>")
        #output.append('<br/>')
        
        output.append('<div id="main_text">')
        output.append(HtmlLayoutBarleymap.text_menu(citation, base_url, show_last_changes = True))
        output.append("</div>")
        
        return "".join(output)
    
    @staticmethod
    def head(base_url):
        return """
        <!DOCTYPE html>
        <!--[if lt IE 7 ]> <html class="ie6"> <![endif]-->
        <!--[if IE 7 ]>    <html class="ie7"> <![endif]-->
        <!--[if IE 8 ]>    <html class="ie8"> <![endif]-->
        <!--[if IE 9 ]>    <html class="ie9"> <![endif]-->
        <!--[if (gt IE 9)|!(IE)]><!--> <html class=""> <!--<![endif]-->
        <head>
            <meta charset="utf-8" />
            <title>PrunusMap</title>
            <meta content="Najla Ksouri, Yolanda Gogorcena, Bruno Contreras Moreira" name="Najla Ksouri, Yolanda Gogorcena, Bruno Contreras Moreira" />
            <meta content="Map markers to Prunus genomes" name="Map markers to Prunus genomes" />
            <meta content="peach, almond, prunusmap, physical map, genetic map, markers, mapping, bioinformatics, blast, gmap, genome, genomics" name="keywords" />
            <link rel="stylesheet" href="{0}" type="text/css" media="screen"/>
        </head>""".format(base_url+"/style.css")
    
    @staticmethod
    def js_scripts(base_url, app_google_analytics_id):
        scripts = ""
        
        scripts = """
            <body>
        <script src="{0}"></script>
        <script src="{1}"></script>
        """.format("https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js", \
                   base_url+"/js/index.js")
        
        scripts = scripts + """
        <!-- Global site tag (gtag.js) - Google Analytics -->
        <script async src="https://www.googletagmanager.com/gtag/js?id="""+app_google_analytics_id+""""></script>
        <script>
            window.dataLayer = window.dataLayer || [];
            function gtag(){dataLayer.push(arguments);}
            gtag('js', new Date());
            gtag('config', '"""+app_google_analytics_id+"""');
        </script>
        """
        
        return scripts
    
    @staticmethod
    def js_scripts_maps(base_url, app_google_analytics_id):
        scripts = ""
        
        scripts = """
            <body>
        <script src="{0}"></script>
        <script src="{1}"></script>
        """.format("http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js", \
                   base_url+"/js/maps.js")
        
        scripts = scripts + """
        <!-- Google Analytics -->
        <script>
            (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
            (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
            m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
            })(window,document,'script','https://www.google-analytics.com/analytics.js','ga');
          
            ga('create', '"""+app_google_analytics_id+"""', 'auto');
            ga('send', 'pageview');
          
        </script>
        """
        
        return scripts
    
    @staticmethod
    def title_header(base_url):
        return """
        <header id="top">
            <h2><a href="{1}/"><img src="{1}/img/logo_PrunusMap.png" alt="Logo" class=logo></a></h2>
            <h3 class="infobar">({0})</h3>
        </header>
        """.format("Welcome to PrunusMap; a toolkit to map markers to the <em> Prunus </em> genomes", base_url)
    
    @staticmethod
    def footer():
        return """
        <footer class="infobar">
            <a href="https://www.eead.csic.es/compbio" target="_blank">Computational and structural biology group</a>
            ::
            <a href="https://www.eead.csic.es/" target="_blank">Estaci&oacute;n Experimental de Aula Dei</a>
            ::
            <a href="https://www.csic.es/" target="_blank">Consejo Superior de Investigaciones Cient&iacute;ficas</a>
        </footer>
        """
    
    @staticmethod
    def text_menu(citation, base_url, show_last_changes = False):
        text_buffer = []
        if show_last_changes:
            text_buffer.append("""
            <br/><strong>Latest changes</strong>
            <br/>
            <br/>20-05-2024:<br/>
            . added new map for Prunus persica cv "ChineseCling" from GDR </br>
            . added new map for Prunus persica cv "Zhongyoutao14" from GDR </br>
            <br/>19-05-2024:<br/>
            . added the cultivar extension "Lovell" to Prunus persica maps </br>
            <br/>29-03-2024:<br/>
            . posted bioRxiv preprint <a href="https://doi.org/10.1101/2024.03.26.586732">https://doi.org/10.1101/2024.03.26.586732</a><br/>
            <br/>01-12-2023:<br/>
            . added Prunus dulcis cv.Texas_NCBIv2 Uniprot Proteins</br>
            . added Adafuel markers</br:>
            <br/>01-10-2023:<br/>
            . added SNP markers from peach 16k array and 60k Axiom SNP: markers</br> 
            . added <em> Prunus dulcis </em> genomes from GDR: Nonpareil.v1, Lauranne.v1 and Texas.v2</br>
            <br/>29-09-2023:<br/>
            . added first version of <em>Prunus persica</em> genome from JGI
            <br/>
            <br/>27-09-2023:<br/>
            . Added SNP markers from the peach 9k array.
            <br/> 
            <br/>27-07-2023:<br/>
            . Web server up and running.
            <br/>


        """.format(base_url))
            
        text_buffer.append("""
            <br/><br/>
            <hr/>
            <b><a href="{2}">PrunusMap</a></b> was designed to search the position of <em>Prunus</em> genetic markers
            on physical and genetic maps of <i>Prunus persica</i> (NCBI and <a href="https://phytozome-next-jgi.doe.gov">Phytozome</a> <sup>[1,2]</sup>) and <i>Prunus dulcis</i> (NCBI and GDR) <sup>[3,8,9]</sup>).
            <br/><br/>
            
            The <strong><i><a href="{2}/find/">Find markers</a></i></strong> option allows to find the position of markers by using their identifiers as input.
            <br/>Note that those markers must be part of one of the
            <!--<strong><a href="{0}#prunusmap_datasets">-->precalculated datasets<!--</a></strong>--> available (e.g.: Illumina 16K markers).
            <br/><br/>
            
            To use the <strong><i><a href="{2}/align/">Align sequences</a></i></strong> option you must provide nucleotide sequences of the markers (in FASTA format).
            <br/>These will be used to retrieve their positions through
            sequence alignment to the selected map (ie Pp_NCBI_V2).
            <br/><br/>
            
            The <strong><i><a href="{2}/locate/">Locate by position</a></i></strong> option allows to examine the map context of specific positions,
            which must be provided as tuples with chromosome (or contig) and position (local position, within the chromosome or contig, in base pairs).
            For example, an user could provide as input "Pp01   10000" to find out which genes are in that specific region of chromosome Pp01.
            <br/><br/>
            
            In addition to locate a list of markers or sequences,
            information of genes, genetic markers, and anchored features,
            that enrich the context around or between the queries will be shown.<br/><br/>
            
            <strong><a href="https://github.com/eead-csic-compbio/prunusmap_web">Prunusmap web</a></strong> 
            works on top of <strong><a href="https://github.com/Cantalapiedra/barleymapcore">barleymap core API</a></strong>, used also in a
            <strong><a href="https://github.com/Cantalapiedra/barleymap">standalone application</a></strong>
            that allows loading custom databases, maps and datasets, among other features.
            <br/>Such application can be used with data from any organism for which sequences anchored to a genetic/physical background are available.
            
            <br/><br/>
            
            <strong>Further information</strong> about how this tool works and help on using it can be found
            <strong><a href="{0}">here</a></strong>.
            <br/>
            Or you may wish to <strong>contact</strong> the <a href="https://www.eead.csic.es/compbio/" target="_blank">Computational and structural biology group</a>
            (<a href="https://www.eead.csic.es">EEAD</a> - <a href="https://www.csic.es">CSIC</a>):<br/>
            <a href="mailto:compbio@eead.csic.es">compbio@eead.csic.es</a>
            <br/><br/>
           
            <strong>Funding:</strong><br/>
            This work was funded by CSIC [grants 2020AEP119 & FAS2022_052], the Spanish Research Agency [grants AGL2017-83358-R MCIN/AEI/10.13039/501100011033 & "A way of making Europe"] and the Government of Arag&oacute;n [grants A44, A09_23R, A10_23R & PhD contract to Najla Ksouri 2018-2023], which were co-financed with FEDER funds.<br/><br/>

            <strong>Citations:</strong>
            <a href="http://link.springer.com/article/10.1007%2Fs11032-015-0253-1">{1}</a>
            <br/><br/>
            <hr/>
            <br/>
            
            <cite><sup>[1]</sup>International Peach Genome Initiative. 2013.
            <a href="https://doi.org/10.1038/ng.2586" target="_blank">
            The high-quality draft genome of peach (Prunus persica) identifies unique patterns of genetic diversity, domestication and genome evolution.
            </a>
            Nature Genetics 45(5):487-94. doi: 10.1038/ng.2586
            </cite>
            <br/>
            
            <cite><sup>[2]</sup>Verde et al. 2017.
            <a href="https://doi.org/10.1186%2Fs12864-017-3606-9" target="_blank">
            The Peach v2.0 release: high-resolution linkage mapping and deep resequencing improve chromosome-scale assembly and contiguity.
            </a>
            BMC Genomics 18(1):225. doi: 10.1186/s12864-017-3606-9
            </cite>
            <br/>
            
            <cite><sup>[3]</sup>Alioto et al. 2020.
            <a href="https://doi.org/10.1111/tpj.14538" target="_blank">
            Transposons played a major role in the diversification between the closely related almond and peach genomes: results from the almond genome sequence.
            </a>
            Plant J. 101(2):455-472. doi: 10.1111/tpj.14538
            </cite>
            <br/>
           
            <cite><sup>[4]</sup>Verde et al. 2012.
            <a href="https://doi.org/10.1371%2Fjournal.pone.0035668" target="_blank">
            Development and evaluation of a 9K SNP array for peach by internationally coordinated SNP detection and validation in breeding germplasm.
            </a>
            PLoS One. 7(6). doi:10.1371/annotation/33f1ba92-c304-4757-91aa-555de64a0768. 
            IRSC 9K markers downloaded from the <a href="https://www.rosaceae.org/species/rosaceae_family_genera/IRSC_SNP_array">GDR</a>.
            </cite>
            </br>
            
            <cite><sup>[5]</sup>Gasic et al. 2022.
            IRSC 16K SNP array for Prunus persica. 
            Unpublished. 
            IRSC 16K markers downloaded from the <a href="https://www.rosaceae.org/Analysis/431">GDR</a>.
            </cite>
            </br>

            <cite><sup>[6]</sup>Guajardo et al. 2022
            <a href="https://doi.org/10.3389/fpls.2022.872208" target="_blank">
            QTLs Identification for Iron Chlorosis in a Segregating Peach-Almond Progeny Through Double-Digest Sequence-Based Genotyping (SBG).
            </a>
            Front. Plant Sci. 13:872208. doi: 10.3389/fpls.2022.872208
            </cite>
            <br>

            <cite><sup>[7]</sup>Duval et al. 2023
            <a href="https://doi.org/10.3390/plants12020242" target="_blank">
            Development and Evaluation of an Axiom 60K SNP Array for Almond (Prunus dulcis).
            </a>
            Plants 12(2): 242. doi: 10.3390/plants12020242
            </cite>
            <br>

            <cite><sup>[8]</sup>D'Amico-Willman et al. 2022
            <a href="https://doi.org/10.1093/g3journal/jkac097" target="_blank">
            Whole-genome sequence and methylome profiling off the almond (Prunus dulcis [Mill.] D.A.Webb) cultivar 'Nonpareil'.
            </a>
            G3 (Bethesda) 12(5):jkac065. doi: 10.1093/g3journal/jkac065
            </cite>
            <br>

            <cite><sup>[9]</sup>Sanchez-Perez et al. 2019
            <a href="https://doi.org/10.1126/science.aav8197" target="_blank">
            Mutation  of a bHLH transcription factor allowed almond domestication.
            </a>
            Science 364(6445):1095-1098. doi: 10.1126/science.aav8197
            </cite>
            <br>

        """.format(base_url+"/help/", citation, base_url))
        
        return "".join(text_buffer)
    
## END
