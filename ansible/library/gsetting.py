#!/usr/bin/python

import json
import re
import subprocess

from ansible.module_utils.basic import AnsibleModule

def _escape_single_quotes(string):
    return re.sub("'", r"'\''", string)

def _command(schema, key, value):

    command = " ".join([
        'export `/usr/bin/dbus-launch`',
        ';',
        '/usr/bin/gsettings set', schema, key,
        "'%s'" % _escape_single_quotes(value),
        ';',
        'kill $DBUS_SESSION_BUS_PID &> /dev/null'
    ])

    return command

def _set_value(schema, key, value):

    command = _command(schema, key, value)

    return subprocess.check_output(command, shell=True).strip()

def _get_value(schema, key):

    command = " ".join([
        'export `/usr/bin/dbus-launch`',
        ';',
        '/usr/bin/gsettings get', schema, key,
        ';',
        'kill $DBUS_SESSION_BUS_PID &> /dev/null'
    ])

    return subprocess.check_output(command, shell=True).strip()

def main():

    module = AnsibleModule(
        argument_spec = dict(
            state     = dict(default='present', choices=['present', 'absent']),
            schema    = dict(required=True),
            key       = dict(required=True),
            value     = dict(required=True)
        ),
        supports_check_mode = True
    )

    params = module.params
    state = module.params['state']
    schema = module.params['schema']
    key = module.params['key']
    value = module.params['value']

    old_value = _get_value(schema, key)
    changed = old_value != value

    if changed and not module.check_mode:
        _set_value(schema, key, value)

    print json.dumps({
        'changed': changed,
        'schema': schema,
        'key': key,
        'value': value,
        'old_value': old_value,
	'command': _command(schema, key, value)
    })

if __name__ == '__main__':
    main()
