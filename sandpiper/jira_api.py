

import requests
import urllib.request
import urllib.error
import urllib
import base64
import re
import json
import os
import shutil
import logging
import config

logger = logging.getLogger(config.LOG_ALIAS)

"""
Wrapper class for all of JIRA APIs
"""

class JiraApi(object):

    def __init__(self, base_data=None, data_set_alias_dir=None, master_data_dir=None, debug=None):
        logger.info('Starting JiraApi ..')

    def __del__(self):
        pass

    """
    Used to test if user/pwd and URL are correct
    """

    def check_url_and_user(self):

        ret = False
        # Check URL and user authentication
        url = config.JIRA_API_URL + '/issue/AR-1343'
        logger.info('Connecting to  URL: {url} ...'.format(url=url))

        try:

            response = requests.get(url, auth=(config.JIRA_USER, config.JIRA_PWD))

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

    def get_filter_for_id(self, filter_id):

        ret = ''
        # Check URL and user authentication
        url = config.JIRA_API_URL + '/filter/' + str(filter_id)

        logger.info('[{filter_id}] Connecting to  URL: {url} ...'.format(filter_id=filter_id, url=url))

        try:

            response = requests.get(url, auth=(config.JIRA_USER, config.JIRA_PWD))

            if response.status_code == 200:
                logger.info('[{filter_id}] Successfully connected to URL: {url}'.format(filter_id=filter_id, url=url))
                ret = response.json()['searchUrl']
            else:
                logger.critical('[{filter_id}] ERROR: Unable to completed: {url}'.format(filter_id=filter_id, url=url))
                ret = ''

        except Exception as e:
            logger.critical(e.message)
            raise

        return ret

    def get_filter(self, url):
        assert len(url) > 0, 'Not a valid url {url}'.format(url=url)

        ret = ''

        # Limits the fields and rows returned.
        url += '&fields=key&maxResults=10000'

        logger.info('Connecting to  URL: {url} ...'.format(url=url))

        try:

            response = requests.get(url, auth=(config.JIRA_USER, config.JIRA_PWD))

            if response.status_code == 200:
                logger.info('Successfully connected to URL: {url}'.format(url=url))
                logger.info(response.json())
                ret = response.json()
            else:
                logger.critical('ERROR: Unable to completed: {url}'.format(url=url))
                ret = ''

        except Exception as e:
            logger.critical(e.message)
            raise

        return ret

    def get_issue_info (self, key):

        # Check URL and user authentication
        url = config.JIRA_API_URL + '/issue/' + key + '?expand=renderedFields'
        logger.info('[{key}] Connecting to  URL: {url} ...'.format(key=key, url=url))

        try:

            response = requests.get(url, auth=(config.JIRA_USER, config.JIRA_PWD))

            if response.status_code == 200:
                logger.info('[{key}] Successfully connected to URL: {url}'.format(key=key, url=url))
                #logger.info(response.json())
                return True, response.json()
            else:
                logger.critical('[{key}] ERROR: Unable to completed: {url}'.format(key=key, url=url))
                return False, None

        except Exception as e:
            logger.critical(e.message)
            raise

        return False, None

    def get_attachment(self, key, issue_info):

        ret = False

        # Iterate and get all the attachments
        attachments = issue_info['fields']['attachment']

        if len(attachments) == 0:
            logger.info('[{key}] No attachments found'.format(key=key))
            return True

        key_dir = os.path.join(config.ATTACHMENT_FOLDER, key)

        if os.path.isdir(key_dir) and config.FETCH_ATTACHMENTS == config.NEW_ONLY:
            logger.info('[{key}] Attachments directory exists. Not fetching again as FETCH_ATTACHMENTS is set to: {val}'.format(key=key, val=config.FETCH_ATTACHMENTS))
            return True

        key_dir = JiraApi.manage_folder(key)

        for attachment in attachments:
            file_name = attachment['filename']
            file_id = attachment['id']
            url = attachment['content']
            mime_type = attachment['mimeType']

            logger.info('[{key}] Connecting to  URL: {url} ...'.format(key=key, url=url))

            try:
                response = requests.get(url, auth=(config.JIRA_USER, config.JIRA_PWD), stream=True)

                if response.status_code == 200:
                    logger.info('[{key}] Successfully connected to URL: {url}'.format(key=key, url=url))
                    path = self._create_unique_name(key_dir, file_name)

                    with open(path, 'wb') as out_file:
                        shutil.copyfileobj(response.raw, out_file)

                    del response
                    ret = True
                else:
                    logger.critical('[{key}] ERROR: Unable to completed: {url}'.format(key=key, url=url))
                    ret = False

            except Exception as e:
                logger.critical(e.message)
                raise

        return ret

    """
    Update the 'Tag' field in JIRA
    """

    def post_tag(self, key, tag):

        url = config.JIRA_API_URL + '/issue/' + key
        logger.info('[{key}] Connecting to  URL: {url} ...'.format(key=key, url=url))

        data_in = {'fields': {config.JIRA_TAG_FIELD: [tag]}}

        try:
            response = requests.put(url, auth=(config.JIRA_USER, config.JIRA_PWD), json=data_in)

            if response.status_code == 204:
                logger.info('[{key}] Successfully connected to URL: {url}'.format(key=key, url=url))
                ret = True
            else:
                logger.critical('[{key}] ERROR: Unable to completed: {url}'.format(key=key, url=url))
                ret = False
                raise SystemError(ret)

        except Exception as e:
            logger.critical(e.message)
            raise

        return ret


    @staticmethod
    def manage_folder(key):

        # key directories remove it it exists and recreate it
        key_dir = os.path.join(config.ATTACHMENT_FOLDER, key)
        if os.path.isdir(key_dir):
            shutil.rmtree(key_dir)
        os.mkdir(key_dir)

        return key_dir

    """
    Given a file name -- checks all the files in the directory
    and creates a unique file name if there is a conflict
    """
    def _create_unique_name(self, key_dir, file_name):

        path = os.path.join(key_dir, file_name)
        # If this name is unique nothing to do.
        if not os.path.isfile(path):
            return path

        # The file name already exists. We need to add a prefix to this file to make it unique
        uniq = 1
        while os.path.exists(path):
            uniq_name = str(uniq) + '_' + file_name
            path = os.path.join(key_dir, uniq_name)
            uniq += 1

        return path
