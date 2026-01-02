#!/bin/bash

# Setup script for deployment
mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"\"\n\
\n\
[server]\n\
headless = true\n\
enableCORS = false\n\
port = \$PORT\n\
\n\
[browser]\n\
gatherUsageStats = false\n\
" > ~/.streamlit/config.toml

# Generate data and train models if not present
if [ ! -f "data/hotel_prices.csv" ]; then
    echo "Generating sample data..."
    python data_generator.py
fi

if [ ! -f "models/hotel_model.pkl" ]; then
    echo "Training models..."
    python model.py
fi