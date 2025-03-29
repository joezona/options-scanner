#!/usr/bin/env sh

echo "Setting up UV (Python tools)"
curl -LsSf https://astral.sh/uv/install.sh | sh
uv sync

echo "################################"
echo "#                              #"
echo "#             DONE!            #"
echo "#                              #"
echo "# Start the app by running:    #"
echo "#                              #"
echo "# uv run streamlit run app.py  #"
echo "#             (or)             #"
echo "#         ./start.sh           #"
echo "#                              #"
echo "################################"

