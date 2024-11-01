#!/bin/bash

set -e
set -u
set -x

rm -rf book
rm -rf docs/README.md

cp README.md docs/README.md

mdbook serve
