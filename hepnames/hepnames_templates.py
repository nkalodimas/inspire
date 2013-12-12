## -*- mode: python; coding: utf-8; -*-

"""HepNames update form templates """

import xml.sax.saxutils

def tmpl_update_hep_name_headers():
        """
        Headers used for the hepnames update form
        """
        html = []
        html.append("""<style type="text/css">
                            .form1
                            {
                                margin-left: 0px;
                            }

                            #tblGrid {
                                margin-left: 0px;
                                margin-bottom: 4px;
                            }

                            #tblGrid td {
                                padding-left: 5px;
                            }

                            .form2
                            {
                                margin-left: 0px;
                            }

                            .form2 td {
                                overflow: hidden;
                                display: inline-block;
                                white-space: normal;
                            }

                            .form2 .left_column {
                                width: 270px;
                            }

                            .form2 .right_column {
                                width: 380px;
                            }

                            #submit_btn {
                                width: 130px;
                                height: 30px;
                            }
                       </style>
                       <script type="text/javascript" src="/js/hepnames_update.js"></script>
                        """)
        return "\n".join(html)

def tmpl_update_hep_name(rec_id, full_name, display_name, email,
                         twitter, status, research_field_list,
                         institution_list, phd_advisor_list,
                         experiment_list, web_page, blog,
                         keynumber, referer):
    """
    Create form to update a hep name
    """
    # Prepare parameters
    try:
        phd_advisor = phd_advisor_list[0]
    except IndexError:
        phd_advisor = ''
    try:
        phd_advisor_sec = phd_advisor_list[1]
    except IndexError:
        phd_advisor_sec = ''
    is_active = is_retired = is_departed = is_deceased = ''
    if status == 'ACTIVE':
        is_active = 'selected'
    elif status == 'RETIRED':
        is_retired = 'selected'
    if status == 'DEPARTED':
        is_departed = 'selected'
    if status == 'DECEASED':
        is_deceased = 'selected'

    research_field_html = """
                          <TD><INPUT TYPE=CHECKBOX VALUE=ACC-PHYS  name=field>acc-phys</TD>
                          <TD><INPUT TYPE=CHECKBOX VALUE=ASTRO-PH name=field>astro-ph</TD>
                          <TD><INPUT TYPE=CHECKBOX VALUE=ATOM-PH name=field>atom-ph</TD>
                          <TD><INPUT TYPE=CHECKBOX VALUE=CHAO-DYN name=field>chao-dyn</TD></TR>
                          <tr><TD><INPUT TYPE=CHECKBOX VALUE=CLIMATE name=field>climate</TD>
                          <TD><INPUT TYPE=CHECKBOX VALUE=COMP name=field>comp</TD>
                          <TD><INPUT TYPE=CHECKBOX VALUE=COND-MAT name=field>cond-mat</TD>
                          <TD><INPUT TYPE=CHECKBOX VALUE=GENL-TH name=field>genl-th</TD></TR>
                          <tr><TD><INPUT TYPE=CHECKBOX VALUE=GR-QC name=field>gr-qc</TD>
                          <TD><INPUT TYPE=CHECKBOX VALUE=HEP-EX name=field>hep-ex</TD>
                          <TD><INPUT TYPE=CHECKBOX VALUE=HEP-LAT name=field>hep-lat</TD>
                          <TD><INPUT TYPE=CHECKBOX VALUE=HEP-PH name=field>hep-ph</TD></TR>
                          <TR>
                          <TD><INPUT TYPE=CHECKBOX VALUE=HEP-TH name=field>hep-th</TD>
                          <TD><INPUT TYPE=CHECKBOX VALUE=INSTR name=field>instr</TD>
                          <TD><INPUT TYPE=CHECKBOX VALUE=LIBRARIAN name=field>librarian</TD>
                          <TD><INPUT TYPE=CHECKBOX VALUE=MATH name=field>math</TD></TR>
                          <TR>
                          <TD><INPUT TYPE=CHECKBOX VALUE=MATH-PH name=field>math-ph</TD>
                          <TD><INPUT TYPE=CHECKBOX VALUE=MED-PHYS name=field>med-phys</TD>
                          <TD><INPUT TYPE=CHECKBOX VALUE=NLIN name=field>nlin</TD>
                          <TD><INPUT TYPE=CHECKBOX VALUE=NUCL-EX name=field>nucl-ex</TD></TR>
                          <TR>
                          <TD><INPUT TYPE=CHECKBOX VALUE=NUCL-TH name=field>nucl-th</TD>
                          <TD><INPUT TYPE=CHECKBOX VALUE=PHYSICS name=field>physics</TD>
                          <TD><INPUT TYPE=CHECKBOX VALUE=PLASMA-PHYS name=field>plasma-phys</TD>
                          <TD><INPUT TYPE=CHECKBOX VALUE=Q-BIO name=field>q-bio</TD></TR>
                          <TR>
                          <TD><INPUT TYPE=CHECKBOX VALUE=QUANT-PH name=field>quant-ph</TD>
                          <TD><INPUT TYPE=CHECKBOX VALUE=SSRL name=field>ssrl</TD>
                          <TD><INPUT TYPE=CHECKBOX VALUE=OTHER name=field>other</TD>
                          """
    for research_field in research_field_list:
        research_field_html = research_field_html.replace('VALUE=' + research_field, 'checked ' + 'VALUE=' + research_field)

    institutions_html = ""
    institution_num = 1
    for institution_entry in institution_list:
        institution = """
                      <tr>
                      <td  class="cell_padding"><input name="aff.str" type="hidden">
                      <input type="text" name="inst%(institution_num)s" size="35" value =%(institution_name)s /></td>
                      <td  class="cell_padding"><select name="rank%(institution_num)s">
                      <option selected value=''> </option>
                      <option value='SENIOR'>Senior(permanent)</option>
                      <option value='JUNIOR'>Junior(leads to Senior)</option>
                      <option value='STAFF'>Staff(non-research)</option>
                      <option value='VISITOR'>Visitor</option>
                      <option value='PD'>PostDoc</option>
                      <option value='PHD'>PhD</option>
                      <option value='MAS'>Masters</option>
                      <option value='UG'>Undergrad</option></select></td>
                      <TD class="cell_padding"><INPUT TYPE="TEXT" value=%(start_year)s name="sy%(institution_num)s" SIZE="4"/></TD>
                      <TD class="cell_padding"><INPUT TYPE="TEXT" value=%(end_year)s name="ey%(institution_num)s" SIZE="4"/></TD>
                      <TD class="cell_padding" style="text-align: center;" ><INPUT TYPE=CHECKBOX VALUE='Current' name="current%(institution_num)s"></TD>
                      <TD class="cell_padding"><input type="button" value="Delete row" class="formbutton" onclick="removeRow(this);" /></TD>
                      </tr>
                      """% { 'institution_name': xml.sax.saxutils.quoteattr(institution_entry[0]),
                             'start_year': xml.sax.saxutils.quoteattr(institution_entry[2]),
                             'end_year': xml.sax.saxutils.quoteattr(institution_entry[3]),
                             'institution_num': institution_num
                           }
        institution_num += 1
        institution = institution.replace('value=' + '\'' + institution_entry[1] + '\'', 'selected ' + 'VALUE=' + institution_entry[1])
        if institution_entry[4] == 'Current':
            institution = institution.replace("VALUE='Current'", 'checked ' + "VALUE='Current'")

        institutions_html += institution

    institutions_html += "<script>occcnt = %s; </script>" % (institution_num-1)
    experiments_html = """
                       <select name=exp id=exp multiple=yes>
                       <option value="">           </option>
                       <option value=AMANDA>AMANDA</option>
                       <option value=AMS>AMS</option>
                       <option value=ANTARES>ANTARES</option>
                       <option value=AUGER>AUGER</option>
                       <option value=BAIKAL>BAIKAL</option>
                       <option value=BNL-E-0877>BNL-E-0877</option>
                       <option value=BNL-LEGS>BNL-LEGS</option>
                       <option value=BNL-RHIC-BRAHMS>BNL-RHIC-BRAHMS</option>
                       <option value=BNL-RHIC-PHENIX>BNL-RHIC-PHENIX</option>
                       <option value=BNL-RHIC-PHOBOS>BNL-RHIC-PHOBOS</option>
                       <option value=BNL-RHIC-STAR>BNL-RHIC-STAR</option>
                       <option value=CDMS>CDMS</option>
                       <option value=CERN-LEP-ALEPH>CERN-LEP-ALEPH</option>
                       <option value=CERN-LEP-DELPHI>CERN-LEP-DELPHI</option>
                       <option value=CERN-LEP-L3>CERN-LEP-L3</option>
                       <option value=CERN-LEP-OPAL>CERN-LEP-OPAL</option>
                       <option value=CERN-LHC-ALICE>CERN-LHC-ALICE</option>
                       <option value=CERN-LHC-ATLAS>CERN-LHC-ATLAS</option>
                       <option value=CERN-LHC-B>CERN-LHC-B</option>
                       <option value=CERN-LHC-CMS>CERN-LHC-CMS</option>
                       <option value=CERN-LHC-LHCB>CERN-LHC-LHCB</option>
                       <option value=CERN-NA-060>CERN-NA-060</option>
                       <option value=CERN-NA-061>CERN-NA-061</option>
                       <option value=CERN-NA-062>CERN-NA-062</option>
                       <option value=CERN-PS-214>CERN-PS-214 (HARP)</option>
                       <option value=CESR-CLEO>CESR-CLEO</option>
                       <option value=CESR-CLEO-C>CESR-CLEO-C</option>
                       <option value=CESR-CLEO-II>CESR-CLEO-II</option>
                       <option value=CHIMERA>CHIMERA</option>
                       <option value=COBRA>COBRA</option>
                       <option value=COSY-ANKE>COSY-ANKE</option>
                       <option value=CUORE>CUORE</option>
                       <option value=COUPP>COUPP</option>
                       <option value=DAYA-BAY>DAYA-BAY</option>
                       <option value=DESY-DORIS-ARGUS>DESY-DORIS-ARGUS</option>
                       <option value=DESY-HERA-B>DESY-HERA-B</option>
                       <option value=DESY-HERA-H1>DESY-HERA-H1</option>
                       <option value=DESY-HERA-HERMES>DESY-HERA-HERMES</option>
                       <option value=DESY-HERA-ZEUS>DESY-HERA-ZEUS</option>
                       <option value=DESY-PETRA-MARK-J>DESY-PETRA-MARK-J</option>
                       <option value=DESY-PETRA-PLUTO-2>DESY-PETRA-PLUTO-2</option>
                       <option value=DESY-PETRA-TASSO>DESY-PETRA-TASSO</option>
                       <option value=DOUBLE-CHOOZ>DOUBLE-CHOOZ</option>
                       <option value=DRIFT>DRIFT</option>
                       <option value=EXO>EXO</option>
                       <option value=FERMI-LAT>FERMI-LAT</option>
                       <option value=FNAL-E-0687>FNAL-E-0687</option>
                       <option value=FNAL-E-0690>FNAL-E-0690</option>
                       <option value=FNAL-E-0706>FNAL-E-0706</option>
                       <option value=FNAL-E-0740>FNAL-E-0740 (D0 Run I)</option>
                       <option value=FNAL-E-0741>FNAL-E-0741 (CDF Run I)</option>
                       <option value=FNAL-E-0799>FNAL-E-0799 (KTeV)</option>
                       <option value=FNAL-E-0815>FNAL-E-0815 (NuTeV)</option>
                       <option value=FNAL-E-0823>FNAL-E-0823 (D0 Run II)</option>
                       <option value=FNAL-E-0830>FNAL-E-0830 (CDF Run II)</option>
                       <option value=FNAL-E-0831>FNAL-E-0831 (FOCUS)</option>
                       <option value=FNAL-E-0832>FNAL-E-0832 (KTeV)</option>
                       <option value=FNAL-E-0872>FNAL-E-0872 (DONUT)</option>
                       <option value=FNAL-E-0875>FNAL-E-0875 (MINOS)</option>
                       <option value=FNAL-E-0886>FNAL-E-0886 (FNPL)</option>
                       <option value=FNAL-E-0892>FNAL-E-0892 (USCMS)</option>
                       <option value=FNAL-E-0898>FNAL-E-0898 (MiniBooNE)</option>
                       <option value=FNAL-E-0904>FNAL-E-0904 (MUCOOL)</option>
                       <option value=FNAL-E-0906>FNAL-E-0906 (NuSea)</option>
                       <option value=FNAL-E-0907>FNAL-E-0907 (MIPP)</option>
                       <option value=FNAL-E-0907>FNAL-E-0918 (BTeV)</option>
                       <option value=FNAL-E-0907>FNAL-E-0973 (Mu2e)</option>
                       <option value=FNAL-E-0937>FNAL-E-0937 (FINeSSE)</option>
                       <option value=FNAL-E-0938>FNAL-E-0938 (MINERvA)</option>
                       <option value=FNAL-E-0954>FNAL-E-0954 (SciBooNE)</option>
                       <option value=FNAL-E-0961>FNAL-E-0961 (COUPP)</option>
                       <option value=FNAL-E-0974>FNAL-E-0974</option>
                       <option value=FNAL-LC>FNAL-LC</option>
                       <option value=FNAL-P-0929>FNAL-P-0929 (NOvA)</option>
                       <option value=FNAL-T-0962>FNAL-T-0962 (ArgoNeuT)</option>
                       <option value=FRASCATI-DAFNE-KLOE>FRASCATI-DAFNE-KLOE</option>
                       <option value=FREJUS-NEMO-3>FREJUS-NEMO-3</option>
                       <option value=GERDA>GERDA</option>
                       <option value=GSI-HADES>GSI-HADES</option>
                       <option value=GSI-SIS-ALADIN>GSI-SIS-ALADIN</option>
                       <option value=HARP>HARP</option>
                       <option value=HESS>HESS</option>
                       <option value=ICECUBE>ICECUBE</option>
                       <option value=ILC>ILC</option>
                       <option value=JLAB-E-01-104>JLAB-E-01-104</option>
                       <option value=KAMLAND>KAMLAND</option>
                       <option value=KASCADE-GRANDE>KASCADE-GRANDE</option>
                       <option value=KATRIN>KATRIN</option>
                       <option value=KEK-BF-BELLE>KEK-BF-BELLE</option>
                       <option value=KEK-BF-BELLE-II>KEK-BF-BELLE-II</option>
                       <option value=KEK-T2K>KEK-T2K</option>
                       <option value=LBNE>LBNE</option>
                       <option value=LIGO>LIGO</option>
                       <option value=LISA>LISA</option>
                       <option value=LSST>LSST</option>
                       <option value=MAGIC>MAGIC</option>
                       <option value=MAJORANA>MAJORANA</option>
                       <option value=MICE>MICE</option>
                       <option value=PICASSO>PICASSO</option>
                       <option value=PLANCK>PLANCK</option>
                       <option value=SDSS>SDSS</option>
                       <option value=SIMPLE>SIMPLE</option>
                       <option value=SLAC-PEP2-BABAR>SLAC-PEP2-BABAR</option>
                       <option value=SNAP>SNAP</option>
                       <option value=SSCL-GEM>SSCL-GEM</option>
                       <option value=SUDBURY-SNO>SUDBURY-SNO</option>
                       <option value=SUDBURY-SNO+>SUDBURY-SNO+</option>
                       <option value=SUPER-KAMIOKANDE>SUPER-KAMIOKANDE</option>
                       <option value=VERITAS>VERITAS</option>
                       <option value=VIRGO>VIRGO</option>
                       <option value=WASA-COSY>WASA-COSY</option>
                       <option value=WMAP>WMAP</option>
                       <option value=XENON>XENON</option>
                       </select>
                       """
    for experiment in experiment_list:
        experiments_html = experiments_html.replace('value=' + experiment, 'selected ' + 'value=' + experiment)

    html = []
    html.append("""<H4>Changes to Existing Records</H4>
                    <P>Send us your details (or someone else's).  See our <a href="http://www.slac.stanford.edu/spires/hepnames/help/adding.shtml">help
                     for additions</A>.<BR>If something doesn't fit in the form, just put it in
                    the comments section.</P>
                    <FORM name="hepnames_addition"
                    onSubmit="return OnSubmitCheck();"
                    action="/hepnames.py/update"
                    method=post>
                    <INPUT type=hidden value=nowhere   name=to id=tofield>
                    <INPUT type=hidden value="New HEPNames Posting" name=subject> <INPUT
                    type=hidden value=2bsupplied name=form_contact id=formcont> <INPUT
                    type=hidden value=/spires/hepnames/hepnames_msgupd.file name=email_msg_file>
                    <INPUT type=hidden value=/spires/hepnames/hepnames_resp_msg.file
                    name=response_msg_file>
                    <INPUT type=hidden value=0 name=debug>
                    <INPUT type=hidden value="%(keynumber)s" name=key>
                    <INPUT type=hidden value="%(rec_id)s" name=person>
                    <INPUT type=hidden value="%(referer)s" name=referer>
                    <INPUT type=hidden value="today" name=DV>
                    <TABLE class=form1>
                    <TBODY>
                    <TR>
                        <TD><STRONG>Full name</STRONG></TD>
                        <TD><INPUT SIZE=24 value=%(full_name)s name=authorname> <font size="2">e.g.
        Beacom, Gosta      </font></TD>
                    </TR>
                    <TR>
                        <TD><STRONG>Display Name</STRONG></TD>
                        <TD><INPUT SIZE=24 value=%(display_name)s name='dispname'> <font size="2">e.g.
        Beacom,  Gösta</font></TD>
                    </TR>
                    <TR>
                        <TD><STRONG> Your Email</STRONG></TD>
                        <TD><INPUT SIZE=24 value=%(email)s name='username' ID='username'><FONT SIZE=2>(<STRONG>REQ'D
                        </strong> but not displayed -  contact only)</font> </TD>
                    </TR>
                    <TR>
                        <TD><STRONG>Email </STRONG>(Public)</TD>
                        <TD><INPUT SIZE=24 value=%(email_public)s name='email' id='email'>
                        <input type='button' value='Same as Above' class='formbutton' onclick='copyem();'/>
                        </TD>
                    </TR>
                    <TR>
                        <TD><STRONG>Twitter username</STRONG></TD>
                        <TD><INPUT SIZE=24 value=%(twitter)s name='twitter' ID='twitter'></TD>
                    </TR>
                    <TR>
                        <TD class="left_column" ><span ><STRONG>Your web page</STRONG></span></TD>
                        <TD class="right_column" ><span ><INPUT SIZE=35 value=%(web)s name='URL'></span></TD>
                    </TR>
                    <TR>
                        <TD class="left_column" ><span ><STRONG>Your blog</STRONG></span></TD>
                        <TD class="right_column" ><span ><INPUT SIZE=35 value=%(blog)s name='blog'></span></TD>
                    </TR>
                    <TR>
                        <TD><STRONG>Status</STRONG></TD>
                        <TD>
                        <SELECT NAME=status>
                        <OPTION %(is_active)s value=ACTIVE>Active</OPTION>
                        <OPTION %(is_retired)s value=RETIRED>Retired</OPTION>
                        <OPTION %(is_departed)s value=DEPARTED>Departed</OPTION>
                        <OPTION %(is_deceased)s value=DECEASED>Deceased</OPTION>
                        </SELECT>
                        </TD>
                    </TR>
                    <TR>
                        <TD><STRONG>Field of research</STRONG></TD>
                        <TD> <table><tbody>
                                <TR>
                                %(research_field_html)s
                                </TR>
                            </TBODY></TABLE>
                        </TD>
                    </TR>
                    <table id="tblGrid" >
                    <TR>
                        <td class="cell_padding"><strong> Institution History</strong><br>
                        <FONT size=2>Please take this name from <A href="http://inspirehep.net/Institutions"
                        target=_TOP>Institutions</A><FONT color=red><SUP>*</SUP></FONT></TD>
                        <td class="cell_padding"><strong>Rank</td>
                        <td class="cell_padding"><strong>Start Year</td>
                        <td class="cell_padding"><strong>End Year</td>
                        <td class="cell_padding"><strong>Current</strong></td>
                    </TR>
                    %(institutions_html)s
                    </table>
                    <table><tr>
                    <a href="javascript:addRow();"> Click to add new Institution field row
                    <img src="/img/add.png" style="vertical-align: middle;" ></a></tr></table>
                    <br/>
                    <FONT color=red><SUP>*</SUP></FONT>
                    <span style="font-size:13px;">
                    Institution name should be in the form given
                    in the&nbsp;
                    <A href="http://inspirehep.net/Institutions" target=_TOP>INSTITUTIONS</A>
                    &nbsp;database<BR>
                    &nbsp;&nbsp;(e.g. Harvard U. * Paris U.,
                    VI-VII * Cambridge U., DAMTP * KEK, Tsukuba).
                    </span>
                    <hr>
                    </br>
                    <table class="form2"><tbody>
                    <tr>
                    <TD class="left_column" ><span ><STRONG>Ph.D. Advisor</STRONG></span></TD>
                    <TD class="right_column" ><span ><INPUT SIZE=24 value=%(phd_advisor)s name=Advisor1> <FONT SIZE=2>E.G.
                    Beacom, John Francis</FONT> </span></TD>
                    </TR>
                    <tr>
                    <TD class="left_column" ><span ><STRONG>2nd Ph.D. Advisor</STRONG></span></TD>
                    <TD class="right_column" ><span ><INPUT SIZE=24 value=%(phd_advisor_sec)s name=Advisor2> <FONT SIZE=2>E.G.
                    Beacom, John Francis</FONT> </span></TD>
                    </TR>
                    <tr>
                    <TD class="left_column" ><span ><STRONG>Experiments</STRONG></span>
                    <br /></td>
                    <td style="width:200px;" class="right_column" ><span >
                    %(experiments_html)s
                    </span>
                    </td>
                    <td style="vertical-align:top;"><span ><FONT size=2>Hold the Control key to choose multiple current or past experiments <br>
                     Experiments not listed can be added in the Comments field below </font></span></td></tr>
                    <TR>
                    <TD class="left_column" ><span >Please send us your <STRONG>Comments</STRONG></span></td>
                    <TD class="right_column" ><TEXTAREA NAME=Abstract ROWS=3 COLS=30></textarea>
                    <span style="font-size:12px; vertical-align:text-top;">(not displayed)</span></TD></TR>
                    <tr><td style="width: 450px;"><div style="display:inline; float:left;">
                    <span id="captcha" style="width:100%%;"></span></div>
                    <div style="float: left; padding-left: 10px;">
                    <strong> How many people in image</strong>  <select name="beatspam" id="beatspam"> <option value=""> </option>
                    <option value="1"> one person</option>
                    <option value="2"> two people</option><option value="3"> three people</option>
                    <option value="4"> more than three</option></select>
                    </div>
                    <div style="width: 300px; display:inline-block; float:left; padding-left:10px; padding-top: 10px;">
                    <span style=""><font size="1">Please answer this question in order to confirm that you are a real person and not a SPAM robot.</font></span>
                    </div>
                    </td>
                    </tr>
                    </tbody></TABLE>
                    <br/><INPUT type=submit id="submit_btn" class="formbutton" value="Send Request"></FORM>
                    """ % {'keynumber' : keynumber,
                          'full_name': xml.sax.saxutils.quoteattr(full_name),
                          'display_name': xml.sax.saxutils.quoteattr(display_name),
                          'email': xml.sax.saxutils.quoteattr(email),
                          'email_public': xml.sax.saxutils.quoteattr(email),
                          'twitter': xml.sax.saxutils.quoteattr(twitter),
                          'phd_advisor': xml.sax.saxutils.quoteattr(phd_advisor),
                          'phd_advisor_sec': xml.sax.saxutils.quoteattr(phd_advisor_sec),
                          'web': xml.sax.saxutils.quoteattr(web_page),
                          'blog': xml.sax.saxutils.quoteattr(blog),
                          'is_active': is_active,
                          'is_retired': is_retired,
                          'is_departed': is_departed,
                          'is_deceased': is_deceased,
                          'research_field_html': research_field_html,
                          'institutions_html': institutions_html,
                          'experiments_html' : experiments_html,
                          'keynumber' : keynumber,
                          'rec_id' : rec_id,
                          'referer': referer
                         })
    return "\n".join(html)
