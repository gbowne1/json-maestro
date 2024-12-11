@echo off

del docs\CONTRIBUTING.md
del docs\CODE_OF_CONDUCT.md
del docs\CHANGELOG.md
del docs\LICENSE

COPY /Y CONTRIBUTING.md docs\CONTRIBUTING.md
COPY /Y CODE_OF_CONDUCT.md docs\CODE_OF_CONDUCT.md
COPY /Y CHANGELOG.md docs\CHANGELOG.md
COPY /Y LICENSE docs\LICENSE

mdbook serve