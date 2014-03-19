## -*- mode: python; coding: utf-8; -*-

"""HepNames update form templates """

import xml.sax.saxutils
try:
    from invenio.config import CFG_BASE_URL
except ImportError:
    from invenio.config import CFG_SITE_URL
    CFG_BASE_URL = CFG_SITE_URL

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

                            input::-webkit-input-placeholder {
                              color: #999;
                            }
                            input:-moz-placeholder {
                              color: #999;
                            }
                            input:-ms-input-placeholder {
                              color: #999;
                            }
                            .ui-autocomplete{
                              max-height: 225px;
                              overflow-y: auto;
                            }
                            .ui-menu-item{
                              font-size: 12px;
                            }
                       </style>
                       <script type="text/javascript" src="/js/hepnames_update.js"></script>
                       <script type="text/javascript" src="%(site_url)s/js/jquery-ui.min.js"></script>
                       <link type="text/css" href="%(site_url)s/img/jquery-ui.css" rel="stylesheet" />
                        """ % {'site_url': CFG_BASE_URL})
        return "\n".join(html)

def tmpl_update_hep_name(rec_id, full_name, display_name, email,
                         orcid, twitter, status,
                         research_field_list,institution_list,
                         phd_advisor_list, experiment_list, web_page,
                         blog, keynumber, referer):
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
                      <input type="text" name="inst%(institution_num)s" id="inst%(institution_num)s" size="35" value =%(institution_name)s /></td>
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
                      <script type="text/javascript">
                        $(function () {
                          autocomplete_kb($("#inst%(institution_num)s"), "InstitutionsCollection");
                        })
                      </script>
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

    experiments_html = ""
    experiments_num = 1
    for experiment_entry in experiment_list:
        experiment = """
                      <tr>
                      <td  class="cell_padding">
                      <input type="text" name="exp%(exp_num)s" id="exp%(exp_num)s" size="35" value =%(exp_name)s /></td>
                      <TD class="cell_padding"><INPUT TYPE="TEXT" value=%(start_year)s name="syExp%(exp_num)s" SIZE="4"/></TD>
                      <TD class="cell_padding"><INPUT TYPE="TEXT" value=%(end_year)s name="eyExp%(exp_num)s" SIZE="4"/></TD>
                      <TD class="cell_padding" style="text-align: center;" ><INPUT TYPE=CHECKBOX VALUE='Current' name="currentExp%(exp_num)s"></TD>
                      <TD class="cell_padding"><input type="button" value="Delete row" class="formbutton" onclick="removeRowExp(this);" /></TD>
                      </tr>
                      <script type="text/javascript">
                        $(function () {
                          autocomplete_kb($("#exp%(exp_num)s"), "ExperimentsCollection");
                        })
                      </script>
                      """% { 'exp_name': xml.sax.saxutils.quoteattr(experiment_entry[0]),
                             'start_year': xml.sax.saxutils.quoteattr(experiment_entry[1]),
                             'end_year': xml.sax.saxutils.quoteattr(experiment_entry[2]),
                             'exp_num': experiments_num
                           }
        experiments_num += 1
        if experiment_entry[3] == 'Current':
            experiment = experiment.replace("VALUE='Current'", 'checked ' + "VALUE='Current'")

        experiments_html += experiment

    experiments_html += "<script>occcntExp = %s; </script>" % (experiments_num-1)

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
                        <TD><STRONG>ORCID </STRONG>(Public)</TD>
                        <TD><INPUT SIZE=24 value=%(orcid)s name='orcid' id='orcid'></TD>
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
                        <td class="cell_padding"><strong> Institution History</strong></TD>
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
                    <table id="tblGridExp" >
                    <TR>
                        <td class="cell_padding"><strong> Experiments</strong><br></TD>
                        <td class="cell_padding"><strong>Start Year</td>
                        <td class="cell_padding"><strong>End Year</td>
                        <td class="cell_padding"><strong>Current</strong></td>
                    </TR>
                    %(experiments_html)s
                    </table>
                    <table><tr>
                    <a href="javascript:addRowExp();"> Click to add new Experiment field row
                    <img src="/img/add.png" style="vertical-align: middle;" ></a></tr></table>
                    <br/>
                    <hr>
                    </br>
                    <table class="form2"><tbody>
                    <tr>
                    <TD class="left_column" ><span ><STRONG>Ph.D. Advisor</STRONG></span></TD>
                    <TD class="right_column" ><span >
                    <INPUT SIZE=24 value=%(phd_advisor)s name=Advisor1 id=Advisor1 placeholder="Start typing for autocomplete">
                    <FONT SIZE=2>E.G.
                    Beacom, John Francis</FONT> </span></TD>
                    </TR>
                    <tr>
                    <TD class="left_column" ><span ><STRONG>2nd Ph.D. Advisor</STRONG></span></TD>
                    <TD class="right_column" ><span >
                    <INPUT SIZE=24 value=%(phd_advisor_sec)s name=Advisor2 id=Advisor2 placeholder="Start typing for autocomplete" >
                    <FONT SIZE=2>E.G.
                    Beacom, John Francis</FONT> </span></TD>
                    </TR>
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
                    <script type="text/javascript">
                        $(function () {
                          autocomplete_kb($("#Advisor1"), "Advisors");
                          autocomplete_kb($("#Advisor2"), "Advisors");
                        })
                      </script>
                    """ % {'keynumber' : keynumber,
                          'full_name': xml.sax.saxutils.quoteattr(full_name),
                          'display_name': xml.sax.saxutils.quoteattr(display_name),
                          'email': xml.sax.saxutils.quoteattr(email),
                          'email_public': xml.sax.saxutils.quoteattr(email),
                          'orcid': xml.sax.saxutils.quoteattr(orcid),
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
