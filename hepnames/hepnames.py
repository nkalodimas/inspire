import os
import time

from tempfile import mkstemp

from invenio.webpage import page
from invenio.webuser import page_not_authorized
from invenio.webinterface_handler import wash_urlargd
from invenio.config import CFG_SITE_LANG, CFG_SITE_URL, CFG_TMPSHAREDDIR, CFG_HEP_NAME_UPDATE_QUEUE
from invenio.urlutils import redirect_to_url
from invenio.messages import gettext_set_language, wash_language
from invenio.search_engine import perform_request_search
from invenio.bibtask import task_low_level_submission
from invenio.bibedit_utils import get_bibrecord
from invenio.bibrecord import record_get_field_value, record_get_field_values, \
                              record_get_field_instances, field_get_subfield_values, \
                              record_add_field, record_xml_output, record_add_subfield_into
from invenio.hepnames_templates import tmpl_update_hep_name_headers, tmpl_update_hep_name


def update(req, **args):
        '''
        POST: Generates a ticket for updating a Hep Name's data
        GET: Generates hepnames update form

        @param req: Apache request object
        @type req: Apache request object
        @param args: request params
        @type args: dict
        '''
        if req.method == 'POST':
            form = args
            wash_dict = {
                 'ln': (str, CFG_SITE_LANG),
                 'referer': (str, ''),
                 'person': (str, ''),
                 'authorname': (str, ''),
                 'dispname': (str, ''),
                 'status': (str, ''),
                 'username': (str, ''),
                 'email': (str, ''),
                 'twitter': (str, ''),
                 'blog': (str, ''),
                 'field': (list, []),
                 'Advisor1': (str, ''),
                 'Advisor2': (str, ''),
                 'exp': (list, []),
                 'URL': (str, ''),
                 'Abstract': (str, '')
            }

            institutions_numbers = add_institutions_to_wash(form, wash_dict)

            argd = wash_urlargd(form,wash_dict)

            person = ''
            if 'person' in argd and argd['person']:
                person = argd['person']
            ln = wash_language(argd['ln'])
            _ = gettext_set_language(ln)

            if not person:
                return page_not_authorized(req, text="Fatal: HepName Id not specified.")

            # every dictionary represents a record field that has to be created
            # every pair has key:form_field and value:marc field and represents
            # a record subfield that has to be created and added to the record field
            # that it belongs
            form_to_marc_mapping = [
                {'authorname': '100__a',
                'dispname': '100__q',
                'status': '100__g'},
                {'username': '595__m'},
                {'email': '371__m'},
                {'URL': '8564_u'},
                {'Advisor1': '701__a'},
                {'Advisor2': '701__a'}]

            add_institutions_to_form_to_marc_mapping(institutions_numbers, argd, form_to_marc_mapping)

            bib_record = create_bibrecord(person, argd, form_to_marc_mapping)

            record_xml = record_xml_output(bib_record)

            tmp_file_name = create_tmp_xml_file(record_xml)

            comment = argd.get('Abstract', '')

            task_low_level_submission('bibupload', 'hep_name_update', '-v', '9', '-o',
                tmp_file_name, '--post-process', 'bst_hep_name_update[recordId="%s",\
                tmp_file_path="%s",subject="%s updated",\
                content="Follow this link %s/record/edit/#state=hpapply&recid=%s&hpid=", \
                queue="%s", \
                comment="%s"]' % (person, tmp_file_name, argd['authorname'], CFG_SITE_URL,
                                person, CFG_HEP_NAME_UPDATE_QUEUE, comment))

            previous_page = ""
            if argd['referer']:
                previous_page = "<a href=\"%s\">Return to the previous page<a>" % argd['referer']

            body = """
                <h4>Success page for HepNames update</h4>
                <p>The form has been successfully submitted and will be processed manually.</p>
                %s
                """ % previous_page

            title = "HEPNames"

            return page(title=title,
                        body=body,
                        req=req,
                        language=ln)
        elif req.method == 'GET':
            form = args
            argd = wash_urlargd(form,
                                {'ln': (str, CFG_SITE_LANG),
                                 'email': (str, ''),
                                 'IRN': (str, ''),
                                })
            # Retrieve info for HEP name based on email or IRN
            recids = []
            if argd['email']:
                recids = perform_request_search(p="371__m:%s" % argd['email'], cc="HepNames")
            elif argd['IRN']:
                recids = perform_request_search(p="001:%s" % argd['IRN'], cc="HepNames")
            else:
                redirect_to_url(req, "%s/collection/HepNames" % (CFG_SITE_URL))

            if not recids:
                redirect_to_url(req, "%s/collection/HepNames" % (CFG_SITE_URL))
            else:
                hepname_bibrec = get_bibrecord(recids[0])

            referer = req.headers_in.get('referer', '')
            # Extract all info from recid that should be included in the form
            rec_id = recids[0]
            full_name = record_get_field_value(hepname_bibrec, tag="100", ind1="", ind2="", code="a")
            display_name = record_get_field_value(hepname_bibrec, tag="100", ind1="", ind2="", code="q")
            email = record_get_field_value(hepname_bibrec, tag="371", ind1="", ind2="", code="m")
            twitter = ''
            for instance in record_get_field_instances(hepname_bibrec, tag="035", ind1="", ind2=""):
                if 'TWITTER' in field_get_subfield_values(instance, '9'):
                    twitter = field_get_subfield_values(instance, 'a')[0]
                    break
            status = record_get_field_value(hepname_bibrec, tag="100", ind1="", ind2="", code="g")
            keynumber = record_get_field_value(hepname_bibrec, tag="970", ind1="", ind2="", code="a")
            try:
                keynumber = keynumber.split('-')[1]
            except IndexError:
                pass
            research_field_list = record_get_field_values(hepname_bibrec, tag="650", ind1="1", ind2="7", code="a")
            institution_list = []
            for instance in record_get_field_instances(hepname_bibrec, tag="371", ind1="", ind2=""):
                if not instance or field_get_subfield_values(instance, "m"):
                    continue
                institution_info = ["", "", "", "", ""]
                if field_get_subfield_values(instance, "a"):
                    institution_info[0] = field_get_subfield_values(instance, "a")[0]
                if field_get_subfield_values(instance, "r"):
                    institution_info[1] = field_get_subfield_values(instance, "r")[0]
                if field_get_subfield_values(instance, "s"):
                    institution_info[2] = field_get_subfield_values(instance, "s")[0]
                if field_get_subfield_values(instance, "t"):
                    institution_info[3] = field_get_subfield_values(instance, "t")[0]
                if field_get_subfield_values(instance, "z"):
                    institution_info[4] = field_get_subfield_values(instance, "z")[0]
                institution_list.append(institution_info)
            phd_advisor_list = record_get_field_values(hepname_bibrec, tag="701", ind1="", ind2="", code="a")
            experiment_list = record_get_field_values(hepname_bibrec, tag="693", ind1="", ind2="", code="e")
            web_page = ''
            blog = ''
            for instance in record_get_field_instances(hepname_bibrec, tag="856", ind1="4", ind2=""):
                if 'BLOG' in field_get_subfield_values(instance, 'y'):
                    blog = field_get_subfield_values(instance, 'u')[0]
                else:
                    web_page = field_get_subfield_values(instance, 'u')[0]

            # Create form and pass as parameters all the content from the record
            body = tmpl_update_hep_name(rec_id, full_name, display_name, email,
                                                 twitter, status, research_field_list,
                                                 institution_list, phd_advisor_list,
                                                 experiment_list, web_page, blog,
                                                 keynumber, referer)
            title = "HEPNames"
            return page(title=title,
                        metaheaderadd = tmpl_update_hep_name_headers(),
                        body=body,
                        req=req,
                        )

def add_institutions_to_wash(form, wash_dict):
    """
    Adds additional institutions to wash dictionary.
    It is needed because the institutions fields are
    created dynamically by the user in the form page.

    @param form: the received form
    @type form: dictionary
    @param wash_dict: the dictionary containing the
    rules for washing the form arguments
    @type wash_dict: dictionary
    """
    inst_nums = [key[-1] for key in form.keys() if key.startswith('inst')]
    for i in inst_nums:
        wash_dict['inst' + str(i)] = (str, '')
        wash_dict['rank' + str(i)] = (str, '')
        wash_dict['sy' + str(i)] = (str, '')
        wash_dict['ey' + str(i)] = (str, '')
        wash_dict['current' + str(i)] = (str, '')
    return inst_nums

def add_institutions_to_form_to_marc_mapping(institutions_numbers, argd, form_to_marc_mapping):
    """
    For every institution it adds a mapping to the
    form_to_marc_mapping dictionary.

    @param institutions_numbers: the numbers of institutions submitted by the user
    @type institutions_numbers: list[int] e.g[1,2,5]
    @param argd: the washed fields of the form
    @type argd: dictionary
    @param form_to_marc_mapping: a dictionary which 'describes' the fields that
    have to be created and added to the bibrecord
    @type form_to_marc_mapping: dictionary
    """
    for i in institutions_numbers:
        inst = 'inst' + str(i)
        if inst in argd:
            form_to_marc_mapping.append(
            { inst: '371__a',
              'rank' + str(i) : '371__r',
              'sy' + str(i) : '371__s',
              'ey' + str(i) : '371__t',
              'current' + str(i) : '371__z'
            })

def create_bibrecord(person, argd, form_to_marc_mapping):
    """
    Creates a bibrecord from form's data.
    For every dictionary when we find the first existing pair/subfield to be added
    we create a record field and we add the subfield into it.Next subfields are
    added to the previously created record field.
    @param argd: the washed fields of the form
    @type argd: dictionary
    @param form_to_marc_mapping: a dictionary which 'describes' the fields that
    have to be created and added to the bibrecord
    @type form_to_marc_mapping: dictionary
    """
    record = {}
    record_add_field(record, '001', controlfield_value=str(person))

    for record_field in form_to_marc_mapping:
        field_created = -1
        for form_field, marc_field in record_field.items():
            if argd[form_field]:
                if field_created != -1:
                    record_add_subfield_into(record, marc_field[:3], marc_field[5], argd[form_field],
                                             field_position_global=field_created)
                else:
                    field_created = record_add_field(record, marc_field[:3], marc_field[3], marc_field[4],
                                        '', [(marc_field[5], argd[form_field])])

    # add twitter
    if argd['twitter']:
        marc_field = '035__a'
        twitter = argd['twitter']
        field_created = record_add_field(record, marc_field[:3], marc_field[3], marc_field[4],
            '', [(marc_field[5], twitter)])
        if field_created != -1:
                    record_add_subfield_into(record, marc_field[:3], '9', 'TWITTER', field_position_global=field_created)
    # add blog
    if argd['blog']:
        marc_field = '8564_u'
        blog = argd['blog']
        field_created = record_add_field(record, marc_field[:3], marc_field[3], marc_field[4],
                                        '', [(marc_field[5], blog)])
        if field_created != -1:
                    record_add_subfield_into(record, marc_field[:3], 'y', 'BLOG', field_position_global=field_created)
    # add research fields
    marc_field = '65017a'
    for research_field in argd['field']:
        field_created = record_add_field(record, marc_field[:3], marc_field[3], marc_field[4],
                                        '', [(marc_field[5], research_field)])
        if field_created != -1:
                    record_add_subfield_into(record, marc_field[:3], '2', 'INSPIRE', field_position_global=field_created)
    # add experiments
    marc_field = '693__e'
    for experiment in argd['exp']:
        field_created = record_add_field(record, marc_field[:3], marc_field[3], marc_field[4],
                                        '', [(marc_field[5], experiment)])
    return record

def create_tmp_xml_file(record_xml):
    """
    Creates a temp xml file to pass to bibupload cli

    @param record_xml: a string containing the representation
    of the bibrecord in xml format
    @type record_xml: string
    """
    tmp_file_fd, tmp_file_name = mkstemp(suffix='.xml', prefix="updateperson%s" % time.strftime("%Y-%m-%d_%H:%M:%S"),
                                            dir=CFG_TMPSHAREDDIR)
    os.write(tmp_file_fd, record_xml)
    os.close(tmp_file_fd)
    os.chmod(tmp_file_name, 0644)

    return tmp_file_name

