<h1 align="center">meta</h1>

<div align="center">

Template for templates 🧶

[![Lint](https://github.com/quickplates/meta/actions/workflows/lint.yaml/badge.svg)](https://github.com/quickplates/meta/actions/workflows/lint.yaml)
[![Test](https://github.com/quickplates/meta/actions/workflows/test.yaml/badge.svg)](https://github.com/quickplates/meta/actions/workflows/test.yaml)

</div>

---

## 💡 About

This repository contains a [`copier`](https://copier.readthedocs.io) template
that can be used to create other templates.

## 📜 Usage

To create a new template in the current directory,
make sure you have [`copier`](https://copier.readthedocs.io) installed and run:

```sh
copier gh:quickplates/meta .
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

Read more about how to develop the project
[here](https://github.com/quickplates/generic/blob/main/CONTRIBUTING.md).

If you have any ideas on how to improve this template,
please open an issue or submit a pull request.
All contributions are welcome! 🤗
