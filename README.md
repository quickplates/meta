<h1 align="center">meta</h1>

<div align="center">

Template for templates 🧶

[![Lint](https://github.com/quickplates/meta/actions/workflows/lint.yaml/badge.svg)](https://github.com/quickplates/meta/actions/workflows/lint.yaml)
[![Test](https://github.com/quickplates/meta/actions/workflows/test.yaml/badge.svg)](https://github.com/quickplates/meta/actions/workflows/test.yaml)

</div>

---

## 💡 About

This repository containts a [`copier`](https://copier.readthedocs.io) template
that can be used to create other templates.

## 📜 Usage

To create a new template,
make sure you have [`copier`](https://copier.readthedocs.io) installed and run:

```sh
copier https://github.com/quickplates/meta path/to/destination
```

## 🚀 Features

- fully reproducible development environments with
  [`Dev Containers`](https://code.visualstudio.com/docs/remote/containers)
  and [`Nix`](https://nixos.org)
- automatic environment activation with [`direnv`](https://direnv.net)
- running tasks with [`Task`](https://taskfile.dev)
- formatting and linting with [`Trunk`](https://trunk.io)
- continuous integration with [`GitHub Actions`](https://github.com/features/actions)

## 💻 Development

Read more about how to contribute and develop the project
[here](https://github.com/quickplates/generic/blob/main/CONTRIBUTING.md).
