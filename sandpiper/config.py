
import os
import yaml
from collections import OrderedDict

"""
Sets up constants and reads parameters from config.yml
"""

MODEL_NAME = 'Sandpiper - Migrating issue tickets from JIRA to JitBit'

# yaml.load by default gives unordered dictionary. This code preserves the order
# That way it is easy to maintain the yaml file.
def ordered_load(stream, Loader=yaml.Loader, object_pairs_hook=OrderedDict):
    class OrderedLoader(Loader):
        pass

    def construct_mapping(loader, node):
        loader.flatten_mapping(node)
        return object_pairs_hook(loader.construct_pairs(node))
    OrderedLoader.add_constructor(
        yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
        construct_mapping)
    return yaml.load(stream, OrderedLoader)

# Constants
LOG_ALIAS = 'sandpiper_log'
CONFIG_FILE = 'config.yml'
JITBIT_MIGRATION_SUCCESS = 'JITBIT_MIGRATION_SUCCESS'
DELETE_REFETCH = 'DELETE_REFETCH'
NEW_ONLY = 'NEW_ONLY'

# Configuration file
base_dir_name = os.path.dirname(os.path.abspath(__file__))
dir_name = base_dir_name + os.sep + '..' + os.sep + 'config'
config_path = os.path.join(dir_name, CONFIG_FILE)
data = ordered_load(open(config_path, 'r'), yaml.SafeLoader)

#  print(yaml.dump(data))

# Logging
LOG_DIR = data.get('log_dir', base_dir_name + os.sep + '..' + os.sep + 'logs')
LOG_MAX_BYTES = data.get('log_max_bytes', 10485760)
LOG_BACKUP_COUNT = data.get('log_backup_count', 5)

#URL
JITBIT_API_URL = data.get('jitbit_api_url', None)
assert JITBIT_API_URL is not None
JITBIT_USER = data.get('jitbit_user', None)
assert JITBIT_USER is not None
JITBIT_PWD = data.get('jitbit_pwd', None)
assert JITBIT_PWD is not None
JITBIT_MIGRATE_CATEGORY_ID = data.get('jitbit_migrate_category_id', None)
JITBIT_DELETE_CATEGORY_ID = data.get('jitbit_delete_category_id', None)
assert JITBIT_MIGRATE_CATEGORY_ID is not None
JITBIT_DEFAULT_ASSIGN_EMAIL = data.get('jitbit_default_assign_email', None)
assert JITBIT_DEFAULT_ASSIGN_EMAIL is not None


JIRA_API_URL = data.get('jira_api_url', None)
assert JIRA_API_URL is not None
JIRA_USER = data.get('jira_user', None)
assert JIRA_USER is not None
JIRA_PWD = data.get('jira_pwd', None)
assert JIRA_PWD is not None
JIRA_FILTER_ID = data.get('jira_filter_id', None)
assert JIRA_FILTER_ID is not None
JIRA_TAG_FIELD = data.get('jira_tag_field', 'customfield_10800')


FETCH_ATTACHMENTS = data.get('fetch_attachments', 'NEW_ONLY')

ATTACHMENT_FOLDER = data.get('attachment_folder', None)
assert ATTACHMENT_FOLDER is not None
# Check for directory existence
assert os.path.isdir(ATTACHMENT_FOLDER), 'Directory {dir} does not exist!'.format(dir=ATTACHMENT_FOLDER)


