{ systemPkgs ? import <nixpkgs> {} }:

let lib  = systemPkgs.lib;
	pkgs = systemPkgs;

	python310 = pkgs.python310.withPackages (pkgs: with pkgs; [
		black
	]);

	PROJECT_ROOT   = builtins.toString ./.;
	PROJECT_SYSTEM = pkgs.system;

in pkgs.mkShell {
	GIT_COMMITTER_EMAIL = "diamondburned@csu.fullerton.edu";
	GIT_AUTHOR_EMAIL    = "diamondburned@csu.fullerton.edu";

	# Poke a PWD hole for our shell scripts to utilize.
	inherit PROJECT_ROOT PROJECT_SYSTEM;

	buildInputs = with pkgs; [
		git
		# Python
		python310
		pyright
		# Go
		go
		# Haskell
		ghc
		haskell-language-server
		ormolu
		# JS
		deno
		nodePackages.prettier
	];
}
