#!/bin/bash
YUN_API_WRAPPER_PATH=$(cd `dirname $0`; pwd)
export PYTHONPATH="${YUN_API_WRAPPER_PATH}:${YUN_API_WRAPPER_PATH}/thirdparty:${PYTHONPATH}"
echo "your PYTHONPATH now: ${PYTHONPATH}"
