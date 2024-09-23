#!/usr/bin/env python
# -*- coding: utf-8 -*-

# HtmlComponentsBase.py is part of Barleymap web app.
# Copyright (C) 2017 Carlos P Cantalapiedra.
# Copyright (C) 2024 Bruno Contreras Moreira and Najla Ksouri
# (terms of use can be found within the distributed LICENSE file).

import sys

from barleymapcore.m2p_exception import m2pException

class HtmlComponentsBase(object):
    
    @staticmethod
    def _load_input_file(user_file, name = "user_file"):
        output = []
        
        output.append("""
                    <br/><span class="explain_text">Or you rather prefer to upload a file</span>
                    <input type="file" name="{1}" id="{1}" value="{0}" class=""/>
                    <input type="button" id="clear_file_button" value="clear" class="demobutton" style="display:none;"/>
        """.format(user_file, name))
        
        return "".join(output)
    
    @staticmethod
    def _load_query_area_align(input_query, user_file, legend, action, name = "query"):
        output = []
        
        output.append("""
                <!-- QUERY AREA -->
                <fieldset style="border:none">
                    <legend>{2}
                        <input type="button" id="align_demo_button" value="demo" class="demobutton"/>
                        <input type="button" id="clear_demo_button" value="clear" class="demobutton"/>
                    </legend>
                    <textarea rows="16" cols="100" id="{1}_{3}" name="{3}"
                    autofocus="autofocus">{0}</textarea>
                    """.format(input_query, action, legend, name))
        output.append(HtmlComponentsBase._load_input_file(user_file))
        output.append("""
                </fieldset>
        """)
        
        return "".join(output)

    @staticmethod
    def _load_query_area_prot(input_query, user_file, legend, action, name = "query"):
        output = []
        
        output.append("""
                <!-- QUERY AREA -->
                <fieldset style="border:none">
                    <legend>{2}
                        <input type="button" id="prot_demo_button" value="demo" class="demobutton"/>
                        <input type="button" id="clear_demo_button" value="clear" class="demobutton"/>
                    </legend>
                    <textarea rows="16" cols="100" id="{1}_{3}" name="{3}"
                    autofocus="autofocus">{0}</textarea>
                    """.format(input_query, action, legend, name))
        output.append(HtmlComponentsBase._load_input_file(user_file))
        output.append("""
                </fieldset>
        """)

        return "".join(output)

    
    @staticmethod
    def _load_query_area_find(input_query, user_file, legend, action, name = "query"):
        output = []
        
        output.append("""
                <!-- QUERY AREA -->
                <fieldset style="border:none">
                    <legend>{2}
                        <input type="button" id="find_demo_button_full" value="demo full map" class="demobutton"/>
                        <input type="button" id="find_demo_button_region" value="demo region" class="demobutton"/>
                        <input type="button" id="clear_demo_button" value="clear" class="demobutton"/>
                    </legend>
                    <textarea rows="16" cols="100" id="{1}_{3}" name="{3}"
                    autofocus="autofocus">{0}</textarea>
                    """.format(input_query, action, legend, name))
        output.append(HtmlComponentsBase._load_input_file(user_file))
        output.append("""
                </fieldset>
        """)
        
        return "".join(output)
    
    @staticmethod
    def _load_query_area_locate(input_query, user_file, legend, action, name = "query"):
        output = []
        
        output.append("""
                <!-- QUERY AREA -->
                <fieldset style="border:none">
                    <legend>{2}
                        <input type="button" id="locate_demo_button" value="demo" class="demobutton"/>
                        <input type="button" id="clear_demo_button" value="clear" class="demobutton"/>
                    </legend>
                    <textarea rows="16" cols="100" id="{1}_{3}" name="{3}"
                    autofocus="autofocus">{0}</textarea>
                    """.format(input_query, action, legend, name))
        output.append(HtmlComponentsBase._load_input_file(user_file))
        output.append("""
                </fieldset>
        """)
        
        return "".join(output)
    
    @staticmethod
    def _load_output_area(input_multiple, input_sort, send_email, email_to, action):
        output = []
        
        ## <!-- <fieldset style="border:solid thin;width:350px;height:170px;"> -->
        output.append("""
                <fieldset style="border:solid thin;width:350px;height:180px">
                <legend>Output options:</legend>
                    <table style="width:100%;text-align:center;">
                    <tr>
                    """)
        
        ########## MULTIPLE
        
        output.append("""
                        <!-- FILTER MULTIPLE CHECK BOX -->
                        <td style="width:50%;">
                            <label for = "multiple">Show markers with multiple mappings: </label>
                            <input type="checkbox" id="multiple" name="multiple" value="1"
            """)
            
        if input_multiple == "1": output.append(" checked/>")
        else: output.append(" />")
        
        output.append("""
                        </td>
                      </tr>
                      <tr><td><hr/></td></tr>
                      <tr>
                      """)
        
        ############ SORT
        output.append("""
                        <!-- SORTING FIELD -->
                        <td style="width:50%;">
                            <label for = "sort">Sort by: </label>
                            <input type="radio" name="sort" id="sort_cm" value="cm" 
                    """)
        
        if input_sort == "" or input_sort == "cm": output.append(" checked/>")
        else: output.append(" />")
        
        output.append("""
                            <label for ="sort_cm">cM</label>
                            <input type="radio" name="sort" id="sort_bp" value="bp"
                    """)
        if input_sort == "bp": output.append(" checked/>")
        else: output.append(" />")
        
        output.append("""
                            <label for ="sort_bp">bp</label>
                         </td>
                    </tr>
                    <tr><td><hr/></td></tr>
                    <tr><td style="width:50%;">
                    """)
        
        ############## email
        output.append("""
                    <fieldset style="border:none;text-align:center;">
                        <label for="send_email">Send by e-mail</label>
                        <input id="input_send_email" type="checkbox" name="send_email" value="1"
                    """)
        
        if send_email == "1": output.append(" checked/>")
        else: output.append(" />")
        
        if send_email == "1" and email_to: output.append('<input type="email" name="email_to" autocomplete="on" value="'+str(email_to)+'"/>')
        else: output.append('<input type="email" name="email_to" autocomplete="on" value=""/>')
        
        output.append("""
                        <br/><span id="email_text" class="explain_text">Results will be sent to the speficied address.</span>
                        </fieldset>
                        </td></tr></table>
                        """)
        
        return "".join(output)
    
    @staticmethod
    def _load_genes_area(show_markers, show_genes, show_anchored, show_main, show_how,
                         extend, extend_cm, extend_bp, action):
        output = []
        
        ##<fieldset style="border:solid thin;height:170px;padding-bottom: 1em;padding-top: 0%;width:430px">
        output.append("""
                <!-- GENES AND MARKERS OPTIONS -->
                <fieldset style="border:solid thin;padding-bottom: 1em;padding-top: 0%;width:430px;height:180px;">
                    <legend>Genes/Markers enrichment:</legend>
                    """)
        
        output.append("""
                      <table style="width:100%;">
                      """)
        
        output.append("""
                      <tr><td>
                      """)
        ## Show genes
        output.append("""
                      <label for="show_genes">genes:</label>
                      <input type="checkbox" id="show_genes" name="show_genes" value="1"
                      """)
        
        if show_genes == "1": output.append(" checked/>")
        elif show_genes == "0": output.append(" />")
        else: output.append(" checked/>")
        
        output.append("""
                      </td>
                      """)
        
        ## Show markers
        output.append("""
                      <td>
                      """)
        
        output.append("""
                      <label for="show_markers"> markers:</label>
                      <input type="checkbox" id="show_markers" name="show_markers" value="1"
                      """)
        
        if show_markers == "1": output.append(" checked/>")
        else: output.append(" />")
        #if show_markers == "1": output.append(" checked/>")
        #elif show_markers == "0": output.append(" />")
        #else: output.append(" checked/>")
        
        output.append("""
                      </td>
                      """)
        
        ## Show anchored
        output.append("""
                      <td>
                      """)
        
        output.append("""
                      <label for="show_anchored"> anchored:</label>
                      <input type="checkbox" id="show_anchored" name="show_anchored" value="1"
                      """)
        
        if show_anchored == "1": output.append(" checked/>")
        else: output.append(" />")
        
        output.append("""
                      </td></tr>
                      """)
        
        output.append("""
                      </table><hr/>
                      """)
        
        ################# Features on markers or in the intervals
        output.append("""
                      <!-- Radio button: enrichment ON MARKERS or in the intervals -->
                      <fieldset id="onmarker_fieldset" style="border:none;padding:0px;">
                        <table style="text-align:center;">
                      """)
        
        output.append("""
                        <tr><td style="width:50%;">
                            <label for = "show_how">Add features:</label>
                            <input type="radio" name="show_how" id="on_intervals" value="0" 
                    """)
        
        if show_how == "" or show_how == "0": output.append(" checked/>")
        else: output.append(" />")
        
        output.append("""
                            <label for ="on_intervals">on intervals</label>
                            <input type="radio" name="show_how" id="on_markers" value="1"
                    """)
        if show_how == "1": output.append(" checked/>")
        else: output.append(" />")
        
        output.append("""
                            <label for ="on_markers">on markers</label>
                         </td>
                    """)
        
        output.append("""
                      </tr>
                      """)
        
        output.append("""
                      <tr>
                      <td>
                      <input type="checkbox" id="show_main" name="show_main" value="1"
                      """)       
        
        if show_main == "1": output.append(" checked/>")
        elif show_main == "0": output.append(" />")
        else: output.append(" checked/>")
        
        output.append("""
                      <label for="show_main">show only main features</label>
                      """)
        
        output.append("""
                      </td>
                      </tr>
                      """)
        
        output.append("""
                      </table>
                      <hr/>
                      </fieldset>
                      """)
        
        ################# GENES Extend search
        output.append("""
                    <fieldset id="extend_fieldset" style="border:none;padding:0px;">
                    <table>""")
        
        output.append("""
                    <tr><td>
                        <input type="checkbox" id="extend" name="extend" value="1"
                    """)
        
        if extend == "1": output.append(" checked/>")
        else: output.append(" />")
        
        output.append("""
                        <label for="extend">Extend genes/markers search</label>
                      <!--</td></tr>-->
                """)
        
        output.append("""
                            <!--<tr><td>--><span id="extend_cm">
                                <input type="number" name="extend_cm" id="window_cm" pattern="[0-9]+[\.][0-9]+" step="0.1" min="0.0" max="9999.9"
                        """)
        #if not genes_window_cm or genes_window_cm == "": output.append(' value="'+str(ResourcesMng.get_def_genes_window_cm())+'"')
        #else:
        myvar = ' value="'+str(extend_cm)+'"' # If I dont do the cast, it crashes
        output.append(myvar)
        
        output.append("""
                                       style="text-align:right;width:4em"/>
                                <label for="window_cm">cM</label>
                            </span><!--</td></tr>-->
                            """)
        
        output.append("""
                           <!--<tr><td>--><span id="extend_bp">
                                <input type="number" name="extend_bp" id="window_bp" pattern="[0-9]+" step="1" min="1" max="10000000000"
                        """)
        #if not genes_window_bp or genes_window_bp == "": output.append(' value="'+str(ResourcesMng.get_def_genes_window_bp())+'"')
        #else:
        myvar = ' value="'+str(extend_bp)+'"' # If I dont do the cast, it crashes
        output.append(myvar)
        
        output.append("""
                                       style="text-align:right;width:7em"/>
                                <label for="window_bp">bp</label>
                            </span><!--</td></tr>-->
                            """)
        
        output.append("""
                      </td></tr>
                      """)
        
        output.append("""
                      <tr><td>
                      <span id="extend_text" class="explain_text">Search will be extended, according to the specified interval.</span>
                      </tr></td>
                      </table>
                      </fieldset>
                      """)
        
        output.append("""
                </fieldset>
                """)
        
        return "".join(output)
   
    @staticmethod
    def _load_prot_alignment_area(threshold_id, threshold_cov):
        output = []

        output.append("""
                <fieldset id="alignment_fieldset" style="border:solid thin;">
                <legend>Choose an action:</legend>
                    <select name="aligner" id="aligner">
                    """)

        output.append('             <option value="miniprot" selected>protein sequences</option>')

        output.append("""
                    </select>
                    <span id="algorithm_text" class="explain_text">Perform a MINIPROT search. Input must be protein sequences in FASTA format.</span>
                    <br/>
                    <br/>
                    <label for="threshold_id">min. id.</label>
                    <input type="number" name="threshold_id" id="threshold_id" pattern="[0-9]+[\.][0-9]+" step="0.1" min="0.1" max="100.0"
                        """)

        ############# ALIGNMENT THRESHOLDS
        #if not threshold_id or threshold_id == "":
        #    myvar = ' value="'+str(def_threshold_id)+'"'
        #    output.append(myvar)
        #else:
        myvar = ' value="'+str(threshold_id)+'"' # If I dont do the cast, it crashes
        output.append(myvar)

        output.append("""
                            style="text-align:right;width:4em"/>
                    
                    <label for="threshold_cov">min. query cov.</label>
                    <input type="number" name="threshold_cov" id="threshold_cov" pattern="[0-9]+[\.][0-9]+" step="0.1" min="0.1" max="100.0"
                        """)
        #if not threshold_cov or threshold_cov == "":
        #    myvar = ' value="'+str(def_threshold_cov)+'"'
        #    output.append(myvar)
        #else:
        myvar = ' value="'+str(threshold_cov)+'"' # If I dont do the cast, it crashes
        output.append(myvar)

        output.append("""
                            style="text-align:right;width:4em"/>
                    </fieldset>
                    """)

        return "".join(output)


    @staticmethod
    def _load_alignment_area(aligner, threshold_id, threshold_cov):
        output = []
        
        #sys.stderr.write("HTMLCOMPONENTS BASE\n")
        #sys.stderr.write(str(aligner)+"\n")
        #sys.stderr.write(str(threshold_id)+"\n")
        #sys.stderr.write(str(threshold_cov)+"\n")
        
        output.append("""
                <fieldset id="alignment_fieldset" style="border:solid thin;">
                <legend>Choose an action:</legend>
                    <select name="aligner" id="aligner">
                    """)
        
        ############## ALIGNMENT ALGORITHM
        if aligner == "auto":
            output.append('             <option value="gmap,blastn" selected>auto</option>')
        else:
            output.append('             <option value="gmap,blastn">auto</option>')
             
        if aligner == "gmap":
            output.append('             <option value="gmap" selected>cdna</option>')
        else:
            output.append('             <option value="gmap">cdna</option>')
            
        if aligner == "blastn":
            output.append('             <option value="blastn" selected>genomic</option>')
        else:
            output.append('             <option value="blastn">genomic</option>')
   
        output.append("""
                    </select>
                    <span id="algorithm_text" class="explain_text">Perform a BLASTN search. Input data must be in FASTA format.</span>
                    <br/>
                    <br/>
                    <label for="threshold_id">min. id.</label>
                    <input type="number" name="threshold_id" id="threshold_id" pattern="[0-9]+[\.][0-9]+" step="0.1" min="0.1" max="100.0"
                        """)
        
        ############# ALIGNMENT THRESHOLDS
        #if not threshold_id or threshold_id == "":
        #    myvar = ' value="'+str(def_threshold_id)+'"'
        #    output.append(myvar)
        #else:
        myvar = ' value="'+str(threshold_id)+'"' # If I dont do the cast, it crashes
        output.append(myvar)
            
        output.append("""
                            style="text-align:right;width:4em"/>
                    
                    <label for="threshold_cov">min. query cov.</label>
                    <input type="number" name="threshold_cov" id="threshold_cov" pattern="[0-9]+[\.][0-9]+" step="0.1" min="0.1" max="100.0"
                        """)
        #if not threshold_cov or threshold_cov == "":
        #    myvar = ' value="'+str(def_threshold_cov)+'"'
        #    output.append(myvar)
        #else:
        myvar = ' value="'+str(threshold_cov)+'"' # If I dont do the cast, it crashes
        output.append(myvar)
            
        output.append("""
                            style="text-align:right;width:4em"/>
                    </fieldset>
                    """)
        
        return "".join(output)
    
    @staticmethod
    def _load_data(input_data, config_data, input_name):
        output = []

        ### Najla's modifications_19September24: add a new filter to select species

        ### Select species"
        output.append('''

            <label>Select species:</label>
            <br/><br/>
            <div id="{0}_filter_checkbox" class="checkbox-container">
                <label for="filter_pp">
                    <input type="checkbox" id="filter_pp" value="Pp_" onchange="filterOptions('{0}')"> Prunus persica
                </label>

                <label for="filter_pd">
                    <input type="checkbox" id="filter_pd" value="Pd_" onchange="filterOptions('{0}')"> Prunus dulcis
                </label>

                <label for="filter_pa">
                    <input type="checkbox" id="filter_pa" value="Pa_" onchange="filterOptions('{0}')"> Prunus armeniaca
                </label>
                
                <label for="filter_pav">
                    <input type="checkbox" id="filter_pav" value="Pav_" onchange="filterOptions('{0}')"> Prunus avium
                </label>

                <label for="filter_pm">
                    <input type="checkbox" id="filter_pm" value="Pm_" onchange="filterOptions('{0}')"> Prunus mume
                </label>
                
                <label for="filter_other">
                    <input type="checkbox" id="filter_p" value="P" onchange="filterOptions('{0}')"> Wild relatives
                </label>
            </div>
        '''.format(str(input_name)))

        output.append('<select name="{0}" id="{0}" style="width: 100%; height: 62%;" multiple>'.format(str(input_name)))

        ## this is the old line: output.append('<select name="{0}" id="{0}" multiple>'.format(str(input_name)))
       

        if not input_data:
            input_data = []
        elif input_data == "":
            input_data = []
        elif isinstance(input_data, basestring): # If only one dataset provided, best if embeb it in a list
            input_data = [input_data]
        #else: input_data is already a list
        
        #(data_names, data_ids) = load_data(conf_file, verbose = ResourcesMng.get_verbose())
        
        for configured_data in config_data:
            conf_id = configured_data[0]
            conf_name = configured_data[1]
            output.append('           <option value="{0}"'.format(conf_id))
            if conf_id in input_data or len(input_data)==0:
                output.append('selected')
            
            output.append('>{0}</option>'.format(conf_name))
        
        output.append("</select>")
        
        
        ## Najla's modifications 19September2024
        # Add the filter script
        output.append('''<script>
        function filterOptions(selectId) {
            var checkboxes = document.querySelectorAll("#" + selectId + "_filter_checkbox input[type='checkbox']");
            var selectedFilters = Array.from(checkboxes).filter(function(checkbox) {
                return checkbox.checked;
            }).map(function(checkbox) {
                return checkbox.value.toLowerCase();
            });
    
            var select = document.getElementById(selectId);
            var options = select.options;
            var selectedMaps = [];
            var hasSelection = false; // To track if any maps are selected
    
            // Clear previously selected maps and store all maps initially
            for (var i = 0; i < options.length; i++) {
                options[i].selected = false; // Deselect all options
            }
    
            // Iterate through options (maps) and handle filtering logic
            for (var i = 0; i < options.length; i++) {
                var option = options[i];
                var text = option.text.toLowerCase();
                var showOption = false;
    
                // Check if no species filters are selected
                if (selectedFilters.length === 0) {
                    option.disabled = false;
                    continue;
                }
    
                // Check for each selected species filter
                for (var j = 0; j < selectedFilters.length; j++) {
                    var filter = selectedFilters[j];
    
                    // If the filter matches the species prefix
                    if (filter !== "p" && text.startsWith(filter)) {
                        showOption = true;
    
                        // If not already selected, add to selected maps
                        if (!option.selected) {
                            selectedMaps.push(option);
                        }
                        break;
                    }
                    // Handle wild relatives separately
                    else if (filter === "p") {
                        if (text.startsWith("p") && !text.startsWith("pp_") && !text.startsWith("pd_") &&
                            !text.startsWith("pa_") && !text.startsWith("pav_") && !text.startsWith("pm_")) {
                            showOption = true;
                            if (!option.selected) {
                                selectedMaps.push(option);
                            }
                            break;
                        }
                    }
                }
    
                // Disable option if it doesn't match the filter
                option.disabled = !showOption;
            }
    
            // If species checkbox is selected but no maps are selected, select all matching maps
            if (selectedMaps.length > 0) {
                for (var k = 0; k < selectedMaps.length; k++) {
                    selectedMaps[k].selected = true;
                }
                hasSelection = true;
            }
    
            // If no species filters are selected and no maps are selected, set default map
            if (!hasSelection && selectedFilters.length === 0) {
                for (var l = 0; l < options.length; l++) {
                    if (options[l].text === "Pp_Lovell_NCBI_V2") {
                        options[l].selected = true;
                        break;
                    }
                }
            }
        }


        </script>''')
        
        return "".join(output)

## END
