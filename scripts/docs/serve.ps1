Remove-Item docs/CONTRIBUTING.md
Remove-Item docs/CODE_OF_CONDUCT.md
Remove-Item docs/CHANGELOG.md
Remove-Item docs/LICENSE

Copy-Item CONTRIBUTING.md docs/CONTRIBUTING.md
Copy-Item CODE_OF_CONDUCT.md docs/CODE_OF_CONDUCT.md
Copy-Item CHANGELOG.md docs/CHANGELOG.md
Copy-Item LICENSE docs/LICENSE

mdbook serve