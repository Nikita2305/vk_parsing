ROOT="$( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; cd .. ; pwd -P )" 
export PYTHONPATH=${PYTHONPATH}:$ROOT/src
python3 $ROOT/tests/example.py
