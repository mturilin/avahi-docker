#!/usr/bin/python

import os
import sys
import yaml
import shutil


def exit_with_error(message, status=1):
    print >> sys.stderr, message
    sys.exit(status)


if __name__ == '__main__':
    CONFIG_DIR = os.environ.get('CONFIG_DIR', '/config/')
    CONFIG_FILENAME = os.environ.get('CONFIG_FILE', "file_server.yaml")

    if not CONFIG_DIR:
        exit_with_error('CONFIG_DIR must be defined')

    config_file_path = CONFIG_DIR + CONFIG_FILENAME
    config = yaml.load(open(config_file_path))

    samba_enabled = config.get('bonjour_samba_enabled', False)
    afp_enabled = config.get('bonjour_afp_enabled', False)

    if samba_enabled:
        print "Enabling Samba"
        shutil.copy('/root/smb.service', '/etc/avahi/services/')

    if afp_enabled:
        print "Enabling AFP"
        shutil.copy('/root/afp.service', '/etc/avahi/services/')
