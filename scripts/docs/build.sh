#!/bin/bash

set -e
set -u
set -x

cp CONTRIBUTING.md docs/CONTRIBUTING.md
cp CODE_OF_CONDUCT.md docs/CODE_OF_CONDUCT.md
cp CHANGELOG.md docs/CHANGELOG.md
cp LICENSE docs/LICENSE.md

mdbook build
