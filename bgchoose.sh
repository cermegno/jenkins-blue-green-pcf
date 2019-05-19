if [ -f "green" ]; then
    echo "We will push blue"
    mv green blue
elif [ -f "blue" ]; then
    echo "We will push green"
    mv blue green
fi
