#!/bin/bash

set -e
set -u
set -x

rm -rf book
rm -rf docs/README.md
rm -rf docs/CONTRIBUTING.md
rm -rf docs/CODE_OF_CONDUCT.md
rm -rf docs/CHANGELOG.md

cp README.md docs/README.md
cp CONTRIBUTING.md docs/CONTRIBUTING.md
cp CODE_OF_CONDUCT.md docs/CODE_OF_CONDUCT.md
cp CHANGELOG.md docs/CHANGELOG.md

mdbook serve
