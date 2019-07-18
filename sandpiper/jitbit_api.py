import requests
import urllib.request
import urllib.error
import urllib
import base64
import re
import json
import os
import logging
import config

logger = logging.getLogger(config.LOG_ALIAS)

"""
Wrapper class for all JitBit APIs
"""

class JitbitApi(object):

    def __init__(self, base_data=None, data_set_alias_dir=None, master_data_dir=None, debug=None):
        logger.info('Starting JitbitApi ..')

    def __del__(self):
        pass

    def check_url_and_user(self):

        ret = False
        # Check URL and user authentication
        url = config.JITBIT_API_URL + '/Authorization'
        logger.info('Connecting to  URL: {url} ...'.format(url=url))

        try:

            response = requests.get(url, auth=(config.JITBIT_USER, config.JITBIT_PWD))

            if response.status_code == 200:
                logger.info('Successfully connected to URL: {url}'.format(url=url))
                logger.info(response.json())
                ret = True
            else:
                logger.critical('Error: Unable to completed: {url}'.format(url=url))
                ret = False

        except Exception as e:
            logger.critical(e.message)
            raise

        return ret

    """
    Pass behalf_of if you want to create ticket for someone else. That is, "Created By" is different
    """

    def post_ticket(self, key, category_id, subject, body, priority_id, behalf_of=None):

        ret = -1

        url = config.JITBIT_API_URL + '/ticket'
        logger.info('[{key}] Connecting to  URL: {url} ...'.format(key=key, url=url))

        in_data = {
                     'categoryId': category_id,
                     'subject': subject,
                     'body': body,
                     'priorityId': priority_id
                  }

        if behalf_of is not None:
            behalf_of_id = self.get_user_id_by_email(behalf_of)
            in_data['userId'] = behalf_of_id

        #logger.info(in_data)

        try:
            response = requests.post(url, auth=(config.JITBIT_USER, config.JITBIT_PWD), data=in_data)

            if response.status_code == 200:
                logger.info('[{key}] Successfully connected to URL: {url}'.format(key=key, url=url))
                ret = response.text
            else:
                logger.critical('[{key}] ERROR: Unable to complete URL: {url}'.format(key=key, url=url))
                ret = -1

        except Exception as e:
            logger.critical(e.message)
            raise

        return ret

    def post_comment(self, key, ticket_id, comment):

        assert ticket_id > 0
        ret = False

        url = config.JITBIT_API_URL + '/comment'
        logger.info('[{key}] Connecting to  URL: {url} ...'.format(key=key, url=url))

        in_data = {'id': ticket_id, 'body': comment}

        try:
            response = requests.post(url, auth=(config.JITBIT_USER, config.JITBIT_PWD), data=in_data)

            if response.status_code == 200:
                logger.info('[{key}] Successfully connected to URL: {url}'.format(key=key, url=url))
                ret = True

            else:
                logger.critical('[{key}] ERROR: Unable to connect to URL: {url}'.format(key=key, url=url))
                ret = False
                raise SystemError(ret)

        except Exception as e:
            logger.critical(e.message)
            raise

        return ret

    def post_attach_file(self, key, ticket_id, attach_file):

        assert ticket_id > 0
        assert os.path.isfile(attach_file)
        ret = False
        url = config.JITBIT_API_URL + '/AttachFile'
        params = {'id': ticket_id}

        logger.info('[{key}] Connecting to  URL: {url} ...'.format(key=key, url=url))

        in_data = {'file': open(attach_file, 'rb')}
        #in_data = {file_name: open(attach_file, 'rb')}
        try:

            # with open(attach_file, 'rb') as f:
            #     response = requests.post(url, auth=(config.JITBIT_USER, config.JITBIT_PWD), params=params, data=f)
            response = requests.post(url, auth=(config.JITBIT_USER, config.JITBIT_PWD), params=params, files=in_data)

            if response.status_code == 200:
                logger.info('[{key}] Successfully connected to URL: {url}'.format(key=key, url=url))
                logger.info(response.text)
                ret = True
            else:
                logger.critical('[{key}] ERROR: Unable to connect to URL: {url}'.format(key=key, url=url))
                ret = False
                raise SystemError(ret)

        except Exception as e:
            logger.critical(e.message)
            raise

        return ret

    def get_user_id_by_email(self, email):
        assert len(email) > 0
        assert re.match(r'[^@]+@[^@]+\.[^@]+', email), 'Not a valid email {email}'.format(email=email)
        ret = -1

        url = config.JITBIT_API_URL + '/UserByEmail'
        params = {'email': email}
        logger.info('[{email}] Connecting to  URL: {url} ...'.format(email=email, url=url))

        try:
            response = requests.post(url, auth=(config.JITBIT_USER, config.JITBIT_PWD), params=params)

            if response.status_code == 200:
                logger.info('[{email}] Successfully connected to URL: {url}'.format(email=email, url=url))
                #logger.info(response.json())
                ret = response.json()["UserID"]

            else:
                logger.critical('[{email}] ERROR: Unable to connect to URL: {url}'.format(email, url=url))
                ret = -1
                raise SystemError(ret)

        except Exception as e:
            logger.critical(e.message)
            raise

        return ret


    def post_set_ticket_status(self, key, ticket_id, status_id):
        ret = False

        url = config.JITBIT_API_URL + '/SetTicketStatus'
        logger.info('[{key}] Connecting to  URL: {url} ...'.format(key=key, url=url))

        params = {'id': ticket_id, 'statusId': status_id
                 }
        try:
            response = requests.post(url, auth=(config.JITBIT_USER, config.JITBIT_PWD), params=params)

            if response.status_code == 200:
                logger.info('[{key}] Successfully connected to URL: {url}'.format(key=key, url=url))
                ret = True
            else:
                logger.critical('[{key}] ERROR: Unable to complete URL: {url}'.format(key=key, url=url))
                ret = False
                raise SystemError(ret)

        except Exception as e:
            logger.critical(e.message)
            raise

        return ret

    def post_set_assignee(self, key, ticket_id, user_id):
        ret = False

        url = config.JITBIT_API_URL + '/SetAssignee'
        logger.info('[{key}] Connecting to  URL: {url} ...'.format(key=key, url=url))

        in_data = {'id': ticket_id, 'UserID': user_id }
        try:
            response = requests.post(url, auth=(config.JITBIT_USER, config.JITBIT_PWD), data=in_data)

            if response.status_code == 200:
                logger.info('[{key}] Successfully connected to URL: {url}'.format(key=key, url=url))
                ret = True
            else:
                logger.critical('[{key}] ERROR: Unable to complete URL: {url}'.format(url=url))
                raise SystemError(ret)

        except Exception as e:
            logger.critical(e.message)
            raise

        return ret

    def post_mark_deleted(self, key, ticket_id):

        assert ticket_id > 0

        # See if the tickets exists
        url = config.JITBIT_API_URL + '/ticket'
        logger.info('[{key}] Connecting to  URL: {url} ...'.format(key=key, url=url))

        in_data = {'id': ticket_id}

        try:
            response = requests.get(url, auth=(config.JITBIT_USER, config.JITBIT_PWD), data=in_data)

            if response.status_code == 200:
                logger.info('[{key}] Successfully connected to URL: {url}'.format(key=key, url=url))
                # Ticket exists. We move the category
                ret = self.post_change_catetory(key, ticket_id, config.JITBIT_DELETE_CATEGORY_ID)
            else:
                logger.critical('[{key}] ERROR: Unable to complete URL: {url}'.format(key=key, url=url))
                ret = -1
                raise SystemError(ret)

        except Exception as e:
            logger.critical(e.message)
            raise

        return ret

    def post_change_catetory(self, key, ticket_id, category_id):
        ret = False

        url = config.JITBIT_API_URL + '/changecategory'
        logger.info('[{key}] Connecting to  URL: {url} ...'.format(key=key, url=url))

        data_in = {'ticketId': ticket_id, 'newCategoryId': category_id }
        try:
            response = requests.post(url, auth=(config.JITBIT_USER, config.JITBIT_PWD), data=data_in)

            if response.status_code == 200:
                logger.info('[{key}] Successfully connected to URL: {url}'.format(key=key, url=url))
                ret = True
            else:
                logger.critical('[{key}] ERROR: Unable to complete URL: {url}'.format(key=key, url=url))
                ret = False
                raise SystemError(ret)

        except Exception as e:
            logger.critical(e.message)
            raise

        return ret


    ##############
    # Methods using urllib2 are not used any longer.
    # Switched to "requests" library as they are more simpler to use
    ###########
    def get_tickets(self):
        url = config.JITBIT_API_URL + '/tickets'

        try:
            request = urllib2.Request(url)
            self._add_basic_auth(request)

            response = urllib2.urlopen(request)

            if response.code == 200 and response.msg == 'OK':
                out_data = json.load(response)
                logger.info(out_data)
                ret = True

            else:
                logger.critical('Error: Unable to complete URL: {url}'.format(url=url))
                ret = False

        except Exception as e:
            logger.critical(e.message)
            raise

        return ret

    def _add_basic_auth(self, request):
        # You need the replace to handle encodestring adding a trailing newline
        # (https://docs.python.org/2/library/base64.html#base64.encodestring)
        base64string = base64.encodestring('%s:%s' % (config.JITBIT_USER, config.JITBIT_PWD)).replace('\n', '')
        request.add_header("Authorization", "Basic %s" % base64string)

        return request


