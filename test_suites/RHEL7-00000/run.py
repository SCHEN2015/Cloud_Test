#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import time
import random
import os

sys.path.append('../../')
from cloud.ec2cli import create_instances
from cloud.ec2cli import run_shell_command_on_instance
from cloud.ec2cli import terminate_instances
from cloud.ec2cli import upload_to_instance
from cloud.ec2cli import download_from_instance

from test_suites.func import load_tscfg
from test_suites.func import prepare_on_instance
from test_suites.func import collect_log_from_instance
from test_suites.func import waiting_for_instance_online


def run_test(instance_name, instance_type=None):

    # prepare
    print 'Preparing environment...'
    prepare_on_instance(TSCFG, instance_name)

    # run test
    print 'Running test on instance...'
    pass

    # get log
    print 'Getting log files...'
    pass

    return


def test(instance_type):
    '''test on specific instance type'''

    instance_name = TSCFG['CASE_ID'].lower() + '-' + instance_type + '-' + str(random.randint(10000000, 99999999))

    try:
        create_instances(region=TSCFG['REGION'], instance_names=(instance_name,), instance_type=instance_type,
                         image_id=TSCFG['IMAGE_ID'], subnet_id=TSCFG['SUBNET_ID'], security_group_ids=TSCFG['SECURITY_GROUP_IDS'])

        waiting_for_instance_online(region=TSCFG['REGION'], instance_name=instance_name, user_name=TSCFG['USER_NAME'])

        print 'Start to run test on {0}...'.format(instance_type)
        run_test(instance_name, instance_type)
        print 'Test on instance type "{0}" finished.'.format(instance_type)

    except Exception, e:
        print 'Failed!'
        print '----------\n', e, '\n----------'

    finally:
        #terminate_instances(region=TSCFG['REGION'], instance_name=instance_name, quick=False)
        pass

    return


# Load test suite Configuration
TSCFG = load_tscfg('./configure.json')

if __name__ == '__main__':

    print 'TSCFG = ', TSCFG

    for instance_type in TSCFG['INSTANCE_TYPE_LIST']:
        test(instance_type)

    #run_test('cheshi-script-test')

    print 'Job finished!'


