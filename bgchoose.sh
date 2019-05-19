if [ -f "green" ]; then
    echo "We will push blue"
    mv green blue
    sed -i 's/green/blue/g' manifest.yml
elif [ -f "blue" ]; then
    echo "We will push green"
    mv blue green
    sed -i 's/blue/green/g' manifest.yml
fi
