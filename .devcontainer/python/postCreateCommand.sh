#!/bin/bash

# Install misc commands
aqua install --config .devcontainer/${DEVCONTAINER_NAME}/aqua.yaml

# Install Gemini CLI
npm install -g @google/gemini-cli

# Setup starship config
mkdir -p ${HOME}/.config
cp .devcontainer/${DEVCONTAINER_NAME}/starship.toml ${HOME}/.config/starship.toml
