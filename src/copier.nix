{
  lib,
  git,
  python3,
  fetchFromGitHub,
}:
python3.pkgs.buildPythonApplication rec {
  pname = "copier";
  version = "7.2.0";
  format = "pyproject";

  src = fetchFromGitHub {
    owner = "copier-org";
    repo = "copier";
    rev = "v${version}";
    postFetch = ''
      rm -rf $out/.github $out/.vscode $out/docs $out/img $out/tests
    '';
    hash = "sha256-vtPZwKvYak/fZEmNiVkgWLZ9h9Zg816A+YYO7tpJIE8=";
  };

  POETRY_DYNAMIC_VERSIONING_BYPASS = version;

  nativeBuildInputs = [
    python3.pkgs.poetry-core
    python3.pkgs.poetry-dynamic-versioning
  ];

  propagatedBuildInputs = with python3.pkgs; [
    colorama
    dunamai
    funcy
    iteration-utilities
    jinja2
    jinja2-ansible-filters
    packaging
    pathspec
    plumbum
    pydantic
    pygments
    pyyaml
    pyyaml-include
    questionary
  ];

  makeWrapperArgs = [
    "--suffix PATH : ${lib.makeBinPath [git]}"
  ];
}
