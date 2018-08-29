#!/usr/bin/env sh

DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
cd ${DIR}
# Makes no difference whether this is there or not.
# dev_appserver.py app.yaml --clear_datastore=True --auto_id_policy=scattered --support_datastore_emulator=True
dev_appserver.py app.yaml --clear_datastore=True --support_datastore_emulator=True
