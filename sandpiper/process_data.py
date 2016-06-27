
import os
import time
import logging
import config
import progressbar
from argument_parser import ArgumentParser
from log_handler import LogHandler
from jitbit_api import JitbitApi
from jira_api import JiraApi

logger = logging.getLogger(config.LOG_ALIAS)


class ProcessData(object):

    def __init__(self):
        logger.info('Starting ProcessData ..')
        self.jitbit_api = JitbitApi()
        self.jira_api = JiraApi()

        # All assigned by is set to one user.
        self.default_assign_id = self.jitbit_api.get_user_id_by_email(config.JITBIT_DEFAULT_ASSIGN_EMAIL)
        
        self.start_time = time.time()

    def __del__(self):
        end_time = time.time()
        logger.info('Total time to run: {exec_time} seconds'.format(exec_time=end_time - self.start_time))

    def start(self):
        try:
            self.jira_api = JiraApi()

            # Check URL and user authentication
            if not self.jira_api.check_url_and_user():
                assert 'Check URL and User call failed!'

            # We want to run a specific filter in JIRA.
            # First give the filter Id and get the URL to run
            filter_url = self.jira_api.get_filter_for_id(config.JIRA_FILTER_ID)

            # Run the filter and get a list of issues to migrate
            issues_list = self.jira_api.get_filter(filter_url)

            # Setup progress bar
            total = len(issues_list['issues'])
            total_str = '/' + str(total)
            pbar_count = 0
            pbar = progressbar.ProgressBar(widgets=[progressbar.Bar(), progressbar.Counter(), total_str, ' ', progressbar.ETA(), ' ', progressbar.Timer()], maxval=total).start()

            # Iterate over each issue and get details
            for issue in issues_list['issues']:

                key = issue['key']

                pbar_count += 1
                pbar.update(pbar_count)
                logger.info('[{key}] Processing: {pbar_count}{total_str}'.format(key=key, pbar_count=pbar_count, total_str=total_str))

                status, issue_info = self.jira_api.get_issue_info(key)

                if not status:
                    logger.critical('[{key}] ERROR: Not able to get issue info'.format(key=key))
                    continue

                self.jira_api.get_attachment(key, issue_info)
00
                # Now create this issue in JitBit
                self._migrate_to_jitbit(key, issue_info)


            pbar.finish()

        except Exception as e:
            logger.critical(e.message)
            raise


    def test_jitbit(self):

        # Use this to test a single post to JitBit.
        # Hardcoded key will be posted.

        process_key = 'AR-122'
        try:
            self.jira_api = JiraApi()

            # Check URL and user authentication
            if not self.jira_api.check_url_and_user():
                assert 'Check URL and User call failed!'

            filter_url = self.jira_api.get_filter_for_id(config.JIRA_FILTER_ID)

            # Run the filter and get a list of issues to deal with
            issues_list = self.jira_api.get_filter(filter_url)

            # Iterate over each issue and get details
            for issue in issues_list['issues']:

                key = issue['key']

                if key != process_key:
                    continue

                status, issue_info = self.jira_api.get_issue_info(key)

                if not status:
                    logger.critical('[{key}] ERROR: Not able to get issue info'.format(key=key))
                    continue

                self.jira_api.get_attachment(key, issue_info)

                # Now create this issue in JitBit
                self._migrate_to_jitbit(key, issue_info)

0        except Exception as e:
            logger.critical(e.message)
            raise

    def _migrate_to_jitbit(self, key, issue_info):

        try:
            category_id = config.JITBIT_MIGRATE_CATEGORY_ID

            # We append JIRA key to subject
            subject = issue_info['fields']['summary'] + ' (' + key + ')'

            body = issue_info['fields']['description']
            if body is None:
                body = ''

            # We will set all of the priorities to Normal (0)
            priority_id = 0

            # Status. JitBit has only New(1) and Closed(3) exposed via API
            if (issue_info['fields']['status']['name']).lower() == 'closed':
                status_id = 3
            else:
                status_id = 1

            # Created by
            # By default this will be the person creating the ticket.
            # You can create 'on-behalf' of another person
            # This code will get the details of the user from JIRA

            # created_by_email = issue_info['fields']['creator']['emailAddress']
            # created_by_diplay_name = issue_info['fields']['creator']['displayName']
            # created_by_first_name, created_by_last_name = created_by_diplay_name.split(' ')

            # For our purpose we decided that all of the created by will be the
            # logged in user. So nothing to set.


            # Assigned to
            # We are assigning all to one person
            assign_to_id = self.default_assign_id

            # Ready to create the ticket
            ticket_id = self.jitbit_api.post_ticket(key, category_id, subject, body, priority_id)
            if ticket_id > 0:

                self.jitbit_api.post_set_assignee(key, ticket_id, assign_to_id)

                self._add_comments(key, ticket_id, issue_info)
                self._add_attachments(key, ticket_id, issue_info)

                # Status should be the last to be set. Otherwise JitBit will change it.
                self.jitbit_api.post_set_ticket_status(key, ticket_id, status_id)

                # We update the issue on the JIRA side if the migration was successful.
                # We use the 'Tag' field in JIRA for this
                self.jira_api.post_tag(key, config.JITBIT_MIGRATION_SUCCESS)
            else:
                logger.critical('ERROR: could not create a ticket in JitBit for {key}'.format(key=key))

        except Exception as e:

            # If we have a failure anywhere in the process we have to delete the ticket.
            # However, JitBit API does not support delete of tickets.
            # Instead move the ticket to 'Deleted' category.
            if ticket_id > 0:
                self.jitbit_api.post_mark_deleted(key, ticket_id)

            logger.critical(e.message)
            # Don't raise let continue

    def _add_comments(self, key, ticket_id, issue_info):
        assert ticket_id > 0

        comments = issue_info['fields']['comment']
        for comment in comments['comments']:
            comment_text = comment['body']
            # Comments can be anonymous
            comment_author = 'Unknown'
            if 'updateAuthor' in comment:
                comment_author = comment['updateAuthor']['emailAddress']

            comment_data = 'Updated by: ' + '[i]' + comment_author + '[/i]\n\n' + comment_text
            self.jitbit_api.post_comment(key, ticket_id, comment_data)

    def _add_attachments(self, key, ticket_id, issue_info):

        # We will add all the files under the <attachments>/key directory to this issue
        key_dir = os.path.join(config.ATTACHMENT_FOLDER, key)

        if not os.path.exists(key_dir):
            logger.info('[{key}] No attachments to process'.format(key=key))

        for root, sub_dirs, files in os.walk(key_dir, topdown=True):
            for filename in files:
                file_dir = os.path.join(root, filename)
                # Ignore attachments of size 5K or less. These are normally logos or icons that we can skip
                if os.path.getsize(file_dir) > 5120:
                    self.jitbit_api.post_attach_file(key, ticket_id, file_dir)
                else:
                    logger.info('[{key}] File size is < 5K. Ignoring. {file_dir}'.format(key=key, file_dir=file_dir))


def main():

    level = ArgumentParser().start()

    if level is not None:
        LogHandler(log_level=level)
    else:
        LogHandler()

    process_data = ProcessData()

    #process_data.test_jitbit()
    process_data.start()

if __name__ == '__main__':
    main()
