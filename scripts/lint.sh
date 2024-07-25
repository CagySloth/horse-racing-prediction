#!/bin/sh

in_place_flag=false

if [ -z "$1" ] || [ "$1" = "--in-place" ] ; then
  echo "Defaulting to apply on 'root'"
  FPATH="."
  if [ "$1" = "--in-place" ]; then
    in_place_flag=true
  fi
else 
  FPATH=$1
  if [ "$2" = "--in-place" ]; then
    in_place_flag=true
  fi
fi

echo $FPATH
echo $in_place_flag

if "$in_place_flag"; then
  ruff format $FPATH
  ruff check $FPATH --fix
  ruff check $FPATH --select I --fix
else
  ruff format $FPATH --check
  mypy $FPATH
  ruff check $FPATH
fi