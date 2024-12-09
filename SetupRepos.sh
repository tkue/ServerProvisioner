#!/bin/bash

DIR="$HOME/bin"

if [ ! -d "$DIR" ]; then
    mkdir "$DIR"
fi

cd "$DIR"

git clone git@gitlab.com:tomkuecken/conky.git
git clone git@gitlab.com:tkuecken/spotify-to-googlemusic.git
git clone git@gitlab.com:tomkuecken/BaseUtils.git
git clone git@gitlab.com:tomkuecken/ServerProvisioner.git
git clone git@gitlab.com:tomkuecken/sql.git
git clone git@gitlab.com:tomkuecken/TorguardVPN.git
git clone https://gitlab.com/tomkuecken/TMUsage
git clone git@gitlab.com:tomkuecken/FindDuplicates.git
git clone git@gitlab.com:tkuecken/workspace.git
git clone git@gitlab.com:tkuecken/notes.git
git clone git@gitlab.com:tkuecken/gists.git
git clone git@gitlab.com:tomkuecken/bash.git
git clone https://gitlab.com/tkuecken/bash